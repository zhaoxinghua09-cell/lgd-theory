#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_meta.py — LGD 理论体系「单一真值源」派生与校验

用途
----
把「同一事实」的所有承载位与 `_meta/source.toml` 对齐。

     python _tools/sync_meta.py --check     # 只校验（门禁用：不一致 → exit 1）
     python _tools/sync_meta.py --apply     # 从 SSOT 派生写入各承载位

为什么
------
2026-09-18 复盘：版本号在 4 个文件里各写一个值（3 处 1.1.0 / 1 处 1.0），
署名 5 种形态并存，同一份电子书在两个目录各存一份。
根因不是"抄错"，是**同一事实被复制到多处承载** —— 副本越多，漂移概率按副本数递增。
本脚本是"只留一处、其余皆派生"的执行器。

判定原则
--------
- **值一致性**（本脚本负责）：版本号 / 题名 / DOI / 仓库地址 / 主页 / ORCID
  必须与 SSOT **完全相等**。
- **形态合法性**（verify_signature.py 负责）：某个位置出现了不属于该位置允许
  集合的写法。注意二者不同 —— 署名在不同位置有不同规范形态（CFF 分字段、
  LaTeX 用 Given Family、引文用 "Zhao, X."），那是**规范差异**不是不一致。
"""
import os
import re
import sys

try:
    import tomllib  # Python 3.11+ 标准库，只读
except ImportError:  # pragma: no cover
    print("[FATAL] 需要 Python 3.11+（tomllib）")
    sys.exit(2)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# 被检查的仓库根：取第一个非选项参数，缺省为当前目录
_args = [a for a in sys.argv[1:] if not a.startswith("-")]
ROOT = os.path.abspath(_args[0]) if _args else os.getcwd()
SSOT_PATH = os.path.join(ROOT, "_meta", "source.toml")

# ---------------------------------------------------------------------------
# 精确值承载位规格
#   (文件, 说明, 正则带 1 个捕获组, SSOT 取值路径, 期望命中次数或 None=至少1次)
# ---------------------------------------------------------------------------
EXACT = [
    # ── CITATION.cff（GitHub「Cite this repository」按钮直读此文件）────────────
    ("CITATION.cff", "发布版本", r'(?m)^version:[ \t]*"([^"]*)"', "release.version", 1),
    ("CITATION.cff", "题名", r'(?m)^title:[ \t]*"([^"]*)"', "title.full", 1),
    ("CITATION.cff", "DOI", r'(?m)^\s+value:[ \t]*"([^"]*)"', "release.doi_concept", 1),
    ("CITATION.cff", "仓库地址", r'(?m)^repository-code:[ \t]*"([^"]*)"', "repo.url", 1),
    ("CITATION.cff", "主页", r'(?m)^url:[ \t]*"([^"]*)"', "repo.homepage", 1),
    ("CITATION.cff", "ORCID", r'(?m)^\s+orcid:[ \t]*"https://orcid\.org/([^"]*)"', "author.orcid", 1),
    ("CITATION.cff", "CFF 姓", r'(?m)^\s*-?\s*family-names:[ \t]*(\S+)', "author.family", 1),
    ("CITATION.cff", "CFF 名", r'(?m)^\s*-?\s*given-names:[ \t]*(\S+)', "author.given", 1),

    # ── .zenodo.json（决定线上 Zenodo 记录版本）──────────────────────────────
    (".zenodo.json", "发布版本", r'"version"[ \t]*:[ \t]*"([^"]*)"', "release.version", 1),
    (".zenodo.json", "题名", r'"title"[ \t]*:[ \t]*"([^"]*)"', "title.full", 1),
    (".zenodo.json", "仓库地址", r'"identifier"[ \t]*:[ \t]*"([^"]*github\.com[^"]*)"', "repo.url", 1),
    (".zenodo.json", "主页", r'"identifier"[ \t]*:[ \t]*"([^"]*github\.io[^"]*)"', "repo.homepage", 1),
    (".zenodo.json", "ORCID", r'"orcid"[ \t]*:[ \t]*"([^"]*)"', "author.orcid", 1),

    # ── schema.jsonld（网页结构化数据）───────────────────────────────────────
    ("schema.jsonld", "发布版本", r'"version"[ \t]*:[ \t]*"([^"]*)"', "release.version", 1),
    ("schema.jsonld", "题名", r'"headline"[ \t]*:[ \t]*"([^"]*)"', "title.full", 1),
    ("schema.jsonld", "ORCID", r'"identifier"[ \t]*:[ \t]*"https://orcid\.org/([^"]*)"', "author.orcid", 1),
    ("schema.jsonld", "主页", r'"url"[ \t]*:[ \t]*"([^"]*)"', "repo.homepage", 1),
    ("schema.jsonld", "仓库地址", r'"codeRepository"[ \t]*:[ \t]*"([^"]*)"', "repo.url", 1),
    ("schema.jsonld", "作者展示名", r'"name"[ \t]*:[ \t]*"([^"]*)"', "author.display", 1),

    # ── 纯文本承载位 ─────────────────────────────────────────────────────────
    ("README.md", "作者展示名", r'^\*\*Author\*\*:[ \t]*([^·\n]+?)[ \t]*·', "author.display", 1),
    ("README.md", "ORCID", r'ORCID[^\n]*?orcid\.org/(\d{4}-\d{4}-\d{4}-\d{4})', "author.orcid", None),
    ("TLDR.md", "作者展示名", r'Author:[ \t]*([^·\n]+?)[ \t]*·', "author.display", 1),
    ("llms.txt", "作者展示名", r'^-[ \t]*author:[ \t]*([^·\n]+?)[ \t]*·', "author.display", 1),
    ("llms.txt", "主页", r'^-[ \t]*homepage:[ \t]*(\S+)', "repo.homepage", 1),
    ("llms.txt", "DOI", r'^-[ \t]*doi:[ \t]*(\S+)', "release.doi_concept", 1),
]

# 版本号「全文所有 vX.Y.Z 形态都必须等于 SSOT」的文件
VERSION_SCAN = ["CITE.md", "CITE-ALL.md", "README.md", "TLDR.md"]


def load_ssot():
    with open(SSOT_PATH, "rb") as f:
        return tomllib.load(f)


def dig(d, path):
    cur = d
    for k in path.split("."):
        cur = cur[k]
    return cur


def read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None


def main():
    apply_mode = "--apply" in sys.argv
    ssot = load_ssot()
    ok, bad, missing = 0, [], []

    print("=" * 72)
    print("SSOT 派生一致性校验" + ("  [APPLY 模式]" if apply_mode else "  [CHECK 模式]"))
    print("SSOT: %s" % os.path.relpath(SSOT_PATH, ROOT))
    print("=" * 72)

    for rel, label, pat, ssot_path, times in EXACT:
        fpath = os.path.join(ROOT, rel)
        s = read(fpath)
        if s is None:
            missing.append("%s（文件不存在）" % rel)
            continue
        want = dig(ssot, ssot_path)
        found = re.findall(pat, s, re.M)
        if not found:
            bad.append((rel, label, "未找到承载位", "%s → %s" % (ssot_path, want)))
            continue
        uniq = sorted(set(found))
        if uniq == [want]:
            ok += 1
        else:
            bad.append((rel, label, "/".join(uniq), "%s → %s" % (ssot_path, want)))
            if apply_mode:
                s2 = re.sub(pat, lambda m: m.group(0).replace(m.group(1), want), s, flags=re.M)
                with open(fpath, "w", encoding="utf-8", newline="") as f:
                    f.write(s2)

    # 版本号全文扫描
    want_ver = dig(ssot, "release.version")
    for rel in VERSION_SCAN:
        s = read(os.path.join(ROOT, rel))
        if s is None:
            missing.append("%s（文件不存在）" % rel)
            continue
        vers = sorted(set(re.findall(r'\bv(\d+\.\d+\.\d+)\b', s)))
        if not vers:
            ok += 1
        elif vers == [want_ver]:
            ok += 1
        else:
            bad.append((rel, "版本文本", "/".join("v" + v for v in vers), "release.version → v" + want_ver))

    print()
    for rel, label, got, want in bad:
        print("[FAIL] %-16s %-10s 实际=%-28s 期望=%s" % (rel, label, got, want))
    for m in missing:
        print("[WARN] %s" % m)
    print()
    print("通过 %d 项 / 不一致 %d 项 / 缺失 %d 项" % (ok, len(bad), len(missing)))
    if apply_mode:
        print("已按 SSOT 派生写入。请重跑 --check 复验。")
        return 0
    if bad:
        print("结论：FAIL —— 存在副本与 SSOT 不一致（改 SSOT 后跑 --apply，或手改副本）")
        return 1
    print("结论：PASS —— 所有承载位与 SSOT 一致")
    return 0


if __name__ == "__main__":
    sys.exit(main())
