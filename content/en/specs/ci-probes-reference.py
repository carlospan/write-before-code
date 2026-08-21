#!/usr/bin/env python3
"""Minimal CI probe reference — covers P1/P2/P3/P4/P5/P7/P9.
Extend P6/P8 in the product repo as needed.

Usage:
  python ci-probes-reference.py --docs-root .
  python ci-probes-reference.py --docs-root . --git-diff   # enable P3 (git repo required)

P1/P2: skip (not fail) when contract/progress files do not exist yet (pre-01 empty template).

This English-tree script expects English optional suffixes:
  *-receipt.md, *-acceptance.md
and English markers such as "Completion", "maintainer accept".
The Chinese corpus keeps a parallel script under content/zh/specs/.
"""
import re, sys, pathlib, argparse, subprocess


def probe_p1(contract_path):
    """P1: contract version monotonic + header matches latest log row."""
    if not contract_path.exists():
        return True, [f"SKIP: missing (greenfield 01 not run yet): {contract_path.name}"]
    text = contract_path.read_text(encoding="utf-8")
    issues = []
    # Support EN header "Contract version: vX.Y" and ZH "契约版本：vX.Y"
    m = re.search(r'(?:Contract version|契约版本)[:：]\s*v([\d.]+)', text, re.I)
    header_ver = m.group(1) if m else None
    log_rows = re.findall(r'\|\s*v([\d.]+)\s*\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|', text)
    if not header_ver:
        issues.append("Header missing contract version")
    log_vers = [r[0] for r in log_rows]
    if log_vers and header_ver and log_vers[-1] != header_ver:
        issues.append(f"Header v{header_ver} != latest log v{log_vers[-1]}")
    nums = [float(v) for v in log_vers]
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            issues.append(f"Non-increasing version: v{log_vers[i-1]} -> v{log_vers[i]}")
    return len(issues) == 0, issues


def probe_p2(progress_path):
    """P2: progress status values legal + ✅ rows have completion time."""
    if not progress_path.exists():
        return True, [f"SKIP: missing (greenfield 01 not run yet): {progress_path.name}"]
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
                    issues.append(f"✅ row missing completion time: {line.strip()[:80]}")
            else:
                issues.append(f"✅ row missing completion-time column: {line.strip()[:80]}")
    return len(issues) == 0, issues


def probe_p3(docs_root, use_git_diff=False):
    """P3: implementers must not self-mark ✅ — new ✅ needs accept evidence."""
    progress_path = docs_root / "reference" / "progress.md"
    if not progress_path.exists():
        return True, []
    issues = []

    if not use_git_diff:
        text = progress_path.read_text(encoding="utf-8")
        for line in text.splitlines():
            if '✅' not in line or '|' not in line or '---' in line:
                continue
            has_acceptance = (
                '04 accept' in line.lower() or '04验收' in line or '04 验收' in line or
                'maintainer accept' in line.lower() or '维护者验收' in line or '维护者签字' in line
            )
            if not has_acceptance:
                issues.append(
                    f"✅ row lacks accept mark (non-git mode; prefer --git-diff): {line.strip()[:80]}"
                )
        return len(issues) == 0, issues

    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
            capture_output=True, text=True, cwd=str(docs_root), timeout=10
        )
        changed_files = result.stdout.strip().splitlines()
    except (subprocess.SubprocessError, FileNotFoundError):
        return True, ["P3: git diff unavailable; skipped"]

    progress_changed = any("progress.md" in f for f in changed_files)
    if not progress_changed:
        return True, []

    try:
        diff_result = subprocess.run(
            ["git", "diff", "HEAD~1", "HEAD", "--", "reference/progress.md"],
            capture_output=True, text=True, cwd=str(docs_root), timeout=10
        )
        diff_text = diff_result.stdout
    except subprocess.SubprocessError:
        return True, ["P3: progress.md diff unavailable; skipped"]

    new_checkmarks = []
    for line in diff_text.splitlines():
        if line.startswith('+') and '✅' in line and not line.startswith('+++'):
            new_checkmarks.append(line[1:].strip())

    if not new_checkmarks:
        return True, []

    has_acceptance_file = any(
        "验收" in f or "accept" in f.lower() for f in changed_files
    )
    has_signoff = (
        "maintainer accept" in diff_text.lower()
        or "维护者验收" in diff_text
        or "维护者签字" in diff_text
    )

    if not has_acceptance_file and not has_signoff:
        for mark in new_checkmarks:
            issues.append(f"New ✅ without accept file/sign-off in same PR: {mark[:80]}")

    return len(issues) == 0, issues


def _glob_task_artifacts(docs_root, suffixes):
    """Collect matching artifacts under tasks/ and archive/."""
    if isinstance(suffixes, str):
        suffixes = [suffixes]
    found = []
    tasks = docs_root / "specs" / "tasks"
    archive = docs_root / "specs" / "archive"
    for suffix in suffixes:
        if tasks.is_dir():
            found.extend(sorted(tasks.glob(f"*{suffix}")))
        if archive.is_dir():
            found.extend(sorted(archive.rglob(f"*{suffix}")))
    return found


def probe_p4(docs_root):
    """P4: receipt files must have a Completion section."""
    issues = []
    for path in _glob_task_artifacts(docs_root, ["-receipt.md", "-回执.md"]):
        text = path.read_text(encoding="utf-8")
        if not re.search(r"^#{1,3}\s*(Completion|完工|完成情况)", text, re.M):
            issues.append(f"Receipt missing Completion section: {path.relative_to(docs_root)}")
    return len(issues) == 0, issues


def probe_p5(docs_root):
    """P5: acceptance records that claim pass need machine-check evidence."""
    issues = []
    for path in _glob_task_artifacts(docs_root, ["-acceptance.md", "-验收记录.md"]):
        text = path.read_text(encoding="utf-8")
        claims_pass = bool(re.search(
            r"(?i)(pass(ed)?|accepted)|(验收)?通过|结论\s*[:：]\s*通过", text
        ))
        has_evidence = bool(re.search(
            r"passed|failed|exit\s*code|exit_code|\d+\s*passed", text, re.I
        ))
        if claims_pass and not has_evidence:
            issues.append(
                f"Acceptance claims pass without machine-check summary: {path.relative_to(docs_root)}"
            )
    return len(issues) == 0, issues


def probe_p7(docs_root):
    """P7: dead relative markdown links."""
    issues = []
    for md in pathlib.Path(docs_root).rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for m in re.finditer(r'\[.+?\]\((?!https?://|#|mailto:)([^)]+\.md[^)]*)\)', text):
            link = m.group(1).split('#')[0]
            target = (md.parent / link).resolve()
            if not target.exists():
                issues.append(f"Dead link: {md.relative_to(docs_root)} -> {link}")
    return len(issues) == 0, issues


def probe_p9(docs_root):
    """P9: each non-empty archive bucket must have INDEX.md."""
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
            issues.append(f"Archive bucket missing INDEX.md: {child.relative_to(docs_root)}")
    return len(issues) == 0, issues


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs-root", default=".", help="Docs root directory")
    parser.add_argument("--git-diff", action="store_true", help="Enable P3 git-diff checks")
    args = parser.parse_args()
    root = pathlib.Path(args.docs_root)

    probes = [
        ("P1", lambda: probe_p1(root / "reference" / "global-contract.md")),
        ("P2", lambda: probe_p2(root / "reference" / "progress.md")),
        ("P3", lambda: probe_p3(root, use_git_diff=args.git_diff)),
        ("P4", lambda: probe_p4(root)),
        ("P5", lambda: probe_p5(root)),
        ("P7", lambda: probe_p7(root)),
        ("P9", lambda: probe_p9(root)),
    ]

    failed = False
    for name, fn in probes:
        ok, details = fn()
        status = "OK" if ok else "FAIL"
        print(f"[{status}] {name}")
        for d in details:
            print(f"  - {d}")
            if not d.startswith("SKIP") and status == "FAIL":
                failed = True
            if status == "FAIL" and not d.startswith("SKIP"):
                failed = True
        if not ok and details and all(d.startswith("SKIP") for d in details):
            pass
        elif not ok:
            failed = True

    sys.exit(1 if failed else 0)
