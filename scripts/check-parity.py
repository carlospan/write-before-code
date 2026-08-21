#!/usr/bin/env python3
"""Fail if content/en and content/zh markdown file sets diverge (by relative path)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN = ROOT / "content" / "en"
ZH = ROOT / "content" / "zh"


def md_relpaths(base: Path) -> set[str]:
    if not base.is_dir():
        return set()
    return {p.relative_to(base).as_posix() for p in base.rglob("*.md")}


def main() -> int:
    en = md_relpaths(EN)
    zh = md_relpaths(ZH)
    only_en = sorted(en - zh)
    only_zh = sorted(zh - en)
    ok = True
    if only_en:
        ok = False
        print("Only in content/en:")
        for p in only_en:
            print(f"  + {p}")
    if only_zh:
        ok = False
        print("Only in content/zh:")
        for p in only_zh:
            print(f"  + {p}")
    # Optional attachment naming is language-specific; just note py scripts
    en_py = {p.relative_to(EN).as_posix() for p in EN.rglob("*.py")} if EN.is_dir() else set()
    zh_py = {p.relative_to(ZH).as_posix() for p in ZH.rglob("*.py")} if ZH.is_dir() else set()
    if en_py != zh_py:
        ok = False
        print("Python file set mismatch between en/zh:")
        print(f"  en={sorted(en_py)}")
        print(f"  zh={sorted(zh_py)}")
    if ok:
        print(f"OK: {len(en)} markdown files matched between en and zh.")
        return 0
    print("FAIL: corpora out of sync. See CONTRIBUTING.md.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
