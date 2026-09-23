#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_remote.py — 线上发布记录 ↔ 单一真值源 的核对

为什么需要它
------------
`sync_meta.py` 只校「本地文件 ↔ 真值源」。但一份发布物还有**第三个副本**：
**平台上已发布的记录**（Zenodo / 仓库前台 / 镜像）。

2026-09-18 实测发现：本地全部改干净后，Zenodo 线上记录里
作者的 affiliation 仍是旧的双品牌组合式、题名也与本地正本不同、
关联链接仍指向商业域 —— 这些**本地改不了**，只能去平台操作，
但**必须能被检出**，否则会长期无人发现。

用法
----
    python check_remote.py [<仓库根>]

⚠️ 需要联网。**刻意不放进推送闸门**（闸门必须离线可跑、必须稳定），
   定为定期/发布前手动执行。
退出码：0 = 一致；1 = 存在不一致。
"""
import json
import os
import sys
import urllib.request

try:
    import tomllib
except ImportError:
    print("[FATAL] 需要 Python 3.11+")
    sys.exit(2)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()
SSOT_PATH = os.path.join(ROOT, "_meta", "source.toml")

# 平台侧记录的公开 API（概念 DOI 会自动解析到最新版本）
ZENODO_API = "https://zenodo.org/api/records/"


def load_forbidden_terms():
    """从**仓外**配置读取受控词（本文件会进公开仓库，不得写死任何品牌字面量）。

    优先级：环境变量 LGD_FORBIDDEN_TERMS（逗号分隔）
            >  ~/.lgd-gate/forbidden.txt（一行一词，# 为注释）
    读不到 ⇒ 返回空列表，调用方跳过该类检查并打印提示。
    """
    raw = os.environ.get("LGD_FORBIDDEN_TERMS", "")
    if raw.strip():
        return [t.strip() for t in raw.split(",") if t.strip()]
    cfg = os.path.join(os.path.expanduser("~"), ".lgd-gate", "forbidden.txt")
    if os.path.isfile(cfg):
        try:
            return [l.strip() for l in open(cfg, encoding="utf-8")
                    if l.strip() and not l.startswith("#")]
        except Exception:
            return []
    return []


def fetch(recid):
    req = urllib.request.Request(ZENODO_API + str(recid),
                                 headers={"Accept": "application/json",
                                          "User-Agent": "lgd-theory-consistency-check/1.0"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    ssot = tomllib.load(open(SSOT_PATH, "rb"))
    doi = ssot["release"]["doi_concept"]
    recid = doi.rsplit(".", 1)[-1]
    want_title = ssot["title"]["full"]
    want_ver = ssot["release"]["version"]
    want_home = ssot["repo"]["homepage"]
    want_line = ssot["line"]["brand"]

    print("=" * 72)
    print("线上记录 ↔ 单一真值源 核对")
    print("真值源：%s" % os.path.relpath(SSOT_PATH, ROOT))
    print("线上记录：Zenodo concept %s" % recid)
    print("=" * 72)

    try:
        rec = fetch(recid)
    except Exception as e:
        print("[SKIP] 无法访问线上记录（%s）。请在有网环境重跑。" % e)
        return 0

    md = rec.get("metadata", {})
    problems = []

    # 题名
    got_title = (md.get("title") or "").strip()
    if got_title != want_title:
        problems.append(("题名", got_title, want_title))

    # 版本
    got_ver = str(md.get("version") or "").strip()
    if got_ver != want_ver:
        problems.append(("版本号", got_ver, want_ver))

    # 作者 affiliation（不得出现双主体组合式，也不得出现仓外配置的受控词）
    terms = load_forbidden_terms()
    if not terms:
        print("[WARN] 未加载仓外受控词配置 ⇒ 本轮按「仅查组合式」执行"
              "（设 LGD_FORBIDDEN_TERMS 或建 ~/.lgd-gate/forbidden.txt 可完整启用）")
    for c in md.get("creators", []):
        aff = (c.get("affiliation") or "").strip()
        if ("×" in aff) or any(t.lower() in aff.lower() for t in terms):
            problems.append(("创作者 affiliation", aff, "应为空或独立研究线标识"))
        if not (c.get("orcid") or "").strip():
            problems.append(("创作者 ORCID", "缺失", ssot["author"]["orcid"]))

    # 关联标识：不应指向受控域
    for r in md.get("related_identifiers", []):
        ident = r.get("identifier", "")
        if any(t.lower() in ident.lower() for t in terms):
            problems.append(("关联链接", ident, want_home))

    # 研究线标识应可被检索到（关键词 / 描述）
    blob = json.dumps(md, ensure_ascii=False)
    if want_line and want_line not in blob:
        problems.append(("研究线标识", "线上记录未出现", want_line))

    print()
    if problems:
        for label, got, want in problems:
            print("[FAIL] %-18s 线上=%-52s 期望=%s" % (label, str(got)[:52], str(want)[:44]))
        print()
        print("合计不一致：%d" % len(problems))
        print("结论：FAIL —— 线上记录与真值源不符。本地无法修正，需到平台操作")
        print("      （Zenodo 用「New version」发布新版本，不要就地改历史记录）。")
        return 1

    print("[PASS] 线上记录与真值源一致")
    return 0


if __name__ == "__main__":
    sys.exit(main())
