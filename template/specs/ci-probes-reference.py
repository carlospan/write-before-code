#!/usr/bin/env python3
"""CI 探针最小参考实现 — 覆盖 P1/P2/P3/P4/P5/P7/P9。工程仓按需扩展 P6/P8。
用法: python ci-probes-reference.py --docs-root .
     python ci-probes-reference.py --docs-root . --git-diff  # 启用 P3（需在 git 仓库内）

P1/P2：契约/进度文件尚未由 01 创建时跳过（空模板不算失败）。
"""
import re, sys, pathlib, argparse, subprocess

def probe_p1(contract_path):
    """P1: 契约版本单调递增 + 头部版本与日志最新行一致 + 变更性质列存在"""
    if not contract_path.exists():
        return True, [f"SKIP: 文件不存在（绿场 01 尚未创建）: {contract_path.name}"]
    text = contract_path.read_text(encoding="utf-8")
    issues = []
    m = re.search(r'契约版本：v([\d.]+)', text)
    header_ver = m.group(1) if m else None
    log_rows = re.findall(r'\|\s*v([\d.]+)\s*\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|', text)
    if not header_ver:
        issues.append("头部无契约版本号")
    log_vers = [r[0] for r in log_rows]
    if log_vers and header_ver and log_vers[-1] != header_ver:
        issues.append(f"头部 v{header_ver} 与日志最新 v{log_vers[-1]} 不一致")
    nums = [float(v) for v in log_vers]
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            issues.append(f"版本非递增: v{log_vers[i-1]} -> v{log_vers[i]}")
    return len(issues) == 0, issues

def probe_p2(progress_path):
    """P2: progress 状态值合法 + ✅ 行有完成时间"""
    if not progress_path.exists():
        return True, [f"SKIP: 文件不存在（绿场 01 尚未创建）: {progress_path.name}"]
    text = progress_path.read_text(encoding="utf-8")
    valid_states = {'⬜', '📝', '🔍', '✅', '⏸️'}
    issues = []
    for line in text.splitlines():
        if '|' not in line or '---' in line:
            continue
        cells = [c.strip() for c in line.split('|')]
        cells = [c for c in cells if c]
        if len(cells) < 3:
            continue
        found_state = None
        for c in cells:
            for s in valid_states:
                if s in c:
                    found_state = s
                    break
            if found_state:
                break
        if found_state == '✅':
            time_cell_idx = None
            for i, c in enumerate(cells):
                if '✅' in c:
                    time_cell_idx = i + 1
                    break
            if time_cell_idx and time_cell_idx < len(cells):
                tc = cells[time_cell_idx]
                if not tc or tc == '-':
                    issues.append(f"✅ 行无完成时间: {line.strip()[:80]}")
            else:
                issues.append(f"✅ 行完成时间列缺失: {line.strip()[:80]}")
    return len(issues) == 0, issues

def probe_p3(docs_root, use_git_diff=False):
    """P3: 03 禁止自标 ✅ — diff 中 progress 出现 → ✅ 时，同 PR 须有验收结论文件或维护者签字"""
    progress_path = docs_root / "reference" / "progress.md"
    if not progress_path.exists():
        return True, []  # 无 progress 文件，不适用
    issues = []

    if not use_git_diff:
        # 非 git 模式：扫描 progress 中所有 ✅ 行，检查是否有对应验收文件或签字
        # 这是保守检查：只报缺少证据的 ✅ 行，不阻断（无法确认是哪个 PR 引入的）
        text = progress_path.read_text(encoding="utf-8")
        for line in text.splitlines():
            if '✅' not in line or '|' not in line or '---' in line:
                continue
            # 检查备注列是否有验收标记
            has_acceptance = ('04验收' in line or '04 验收' in line or
                              '维护者验收' in line or '维护者签字' in line)
            if not has_acceptance:
                issues.append(f"✅ 行无验收标记（非 git 模式，建议加 --git-diff 精确检查）: {line.strip()[:80]}")
        return len(issues) == 0, issues

    # git diff 模式：只检查本次 PR 中新增的 ✅ 标记
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
            capture_output=True, text=True, cwd=str(docs_root), timeout=10
        )
        changed_files = result.stdout.strip().splitlines()
    except (subprocess.SubprocessError, FileNotFoundError):
        return True, ["P3: 无法获取 git diff，跳过（非 git 仓库或 git 不可用）"]

    # 检查 progress.md 是否在本次改动中
    progress_changed = any("progress.md" in f for f in changed_files)
    if not progress_changed:
        return True, []  # 本次 PR 没改 progress，不需要检查

    # 获取 progress.md 的 diff
    try:
        diff_result = subprocess.run(
            ["git", "diff", "HEAD~1", "HEAD", "--", "reference/progress.md"],
            capture_output=True, text=True, cwd=str(docs_root), timeout=10
        )
        diff_text = diff_result.stdout
    except subprocess.SubprocessError:
        return True, ["P3: 无法获取 progress.md diff，跳过"]

    # 提取新增的 ✅ 行（diff 中以 + 开头且含 ✅）
    new_checkmarks = []
    for line in diff_text.splitlines():
        if line.startswith('+') and '✅' in line and not line.startswith('+++'):
            new_checkmarks.append(line[1:].strip())

    if not new_checkmarks:
        return True, []  # 没有新增 ✅

    # 检查同 PR 是否有验收相关文件
    has_acceptance_file = any(
        "验收" in f or "accept" in f.lower() for f in changed_files
    )
    # 检查 diff 中是否有维护者签字
    has_signoff = "维护者验收" in diff_text or "维护者签字" in diff_text

    if not has_acceptance_file and not has_signoff:
        for mark in new_checkmarks:
            issues.append(f"progress 新增 ✅ 但同 PR 无验收文件/维护者签字: {mark[:80]}")

    return len(issues) == 0, issues

def _glob_task_artifacts(docs_root, suffix):
    """tasks/ 与 archive 子桶中的 *-回执.md / *-验收记录.md。"""
    found = []
    tasks = docs_root / "specs" / "tasks"
    archive = docs_root / "specs" / "archive"
    if tasks.is_dir():
        found.extend(sorted(tasks.glob(f"*{suffix}")))
    if archive.is_dir():
        found.extend(sorted(archive.rglob(f"*{suffix}")))
    return found

def probe_p4(docs_root):
    """P4: 回执（含已归档）须有「完工」段。"""
    issues = []
    for path in _glob_task_artifacts(docs_root, "-回执.md"):
        text = path.read_text(encoding="utf-8")
        if not re.search(r"^#{1,3}\s*(完工|完成情况)", text, re.M):
            issues.append(f"回执无「完工」段: {path.relative_to(docs_root)}")
    return len(issues) == 0, issues

def probe_p5(docs_root):
    """P5: 验收记录（含已归档）若宣称通过，须有机检痕迹。"""
    issues = []
    for path in _glob_task_artifacts(docs_root, "-验收记录.md"):
        text = path.read_text(encoding="utf-8")
        claims_pass = bool(re.search(r"(验收)?通过|结论\s*[:：]\s*通过", text))
        has_evidence = bool(re.search(
            r"passed|failed|exit\s*code|exit_code|\d+\s*passed", text, re.I
        ))
        if claims_pass and not has_evidence:
            issues.append(f"验收通过但无机检摘要: {path.relative_to(docs_root)}")
    return len(issues) == 0, issues

def probe_p7(docs_root):
    """P7: 死链检测 — markdown 相对链接指向的文件是否存在"""
    issues = []
    for md in pathlib.Path(docs_root).rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for m in re.finditer(r'\[.+?\]\((?!https?://|#|mailto:)([^)]+\.md[^)]*)\)', text):
            link = m.group(1).split('#')[0]
            target = (md.parent / link).resolve()
            if not target.exists():
                issues.append(f"死链: {md.relative_to(docs_root)} -> {link}")
    return len(issues) == 0, issues

def probe_p9(docs_root):
    """P9: specs/archive 下每个有文件的子桶必须有 INDEX.md。"""
    archive = docs_root / "specs" / "archive"
    if not archive.is_dir():
        return True, []
    issues = []
    for child in sorted(archive.iterdir()):
        if not child.is_dir():
            continue
        has_file = any(p.is_file() for p in child.rglob("*"))
        if not has_file:
            continue
        if not (child / "INDEX.md").is_file():
            issues.append(f"归档桶缺 INDEX.md: {child.relative_to(docs_root)}")
    return len(issues) == 0, issues

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs-root", default=".", help="文档根目录")
    parser.add_argument("--git-diff", action="store_true", help="启用 P3 git diff 检查（需在 git 仓库内）")
    args = parser.parse_args()
    root = pathlib.Path(args.docs_root)
    all_ok = True
    probes = [
        ("P1", probe_p1, (root / "reference" / "global-contract.md",)),
        ("P2", probe_p2, (root / "reference" / "progress.md",)),
        ("P3", probe_p3, (root, args.git_diff)),
        ("P4", probe_p4, (root,)),
        ("P5", probe_p5, (root,)),
        ("P7", probe_p7, (root,)),
        ("P9", probe_p9, (root,)),
    ]
    for name, fn, fn_args in probes:
        ok, issues = fn(*fn_args)
        skipped = ok and issues and all(str(i).startswith("SKIP") for i in issues)
        print(f"{'SKIP' if skipped else ('PASS' if ok else 'FAIL')} {name}")
        for i in issues:
            print(f"       {i}")
        if not ok:
            all_ok = False
    print()
    print("ALL PASS" if all_ok else "SOME FAILED")
    sys.exit(0 if all_ok else 1)
