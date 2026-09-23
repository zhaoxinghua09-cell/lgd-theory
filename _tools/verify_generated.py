#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_generated.py — 生成物口径漂移检出 + 全仓禁用词闸门（push 门禁）

为什么
------
`lgd-theory/book/` 是**生成物**（源：`发布/电子书/_build_book.py` + `docs/*.md`）。
生成物有两个特有的风险，普通「扫全仓禁止形态」的门禁抓不到：

  A. **产物被当源手改** —— 改了产物，下次重建即回退
  B. **源改了但产物没重建** —— 改了 docs/*.md，忘了重跑脚本，产物与源分叉

本脚本用「产物内的口径值必须等于 SSOT 派生值」来同时压制这两类风险：
只要产物与 SSOT 不符，就说明产物已偏离源或被手改。

2026-09-24 加固（两处，均由实测缺陷驱动）
----------------------------------------
1. **禁用词不再写死在本文件里**。
   本文件是公开仓库的一部分。若把品牌名/域名当字面量写进来，
   等于把品牌名永久留在公开仓里 —— 与闸门目的正好相反。
   改为从**仓外配置**读取（见 `load_forbidden_terms()`）；
   读不到就**跳过该类检查**并在输出里明确提示，不静默通过。

2. **扫描范围由 `book/` 扩至全仓文本文件**。
   原实现只扫生成物目录，源码 / 文档 / 门禁脚本自身的残留全部漏网
   （2026-09-24 实测：工作副本仍有 19 个文件命中，而本脚本报 PASS）。

用法
----
    python verify_generated.py <仓库根>

输出 PASS/FAIL；退出码 0/1。
"""
import os
import re
import sys
import zipfile

try:
    import tomllib
except ImportError:
    print("[FATAL] 需要 Python 3.11+")
    sys.exit(2)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.getcwd())
SSOT_PATH = os.path.join(ROOT, "_meta", "source.toml")

# 生成物目录（相对仓库根）——版本号漂移检查用
GEN_DIRS = ["book"]

# 全仓扫描时跳过的目录 / 文件（二进制与外部依赖）
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", "_epub"}
TEXT_EXT = (".md", ".html", ".htm", ".xhtml", ".txt", ".py", ".toml",
            ".json", ".jsonld", ".cff", ".yml", ".yaml", ".tex", ".opf",
            ".xml", ".ncx", ".css", ".sh", ".bat")


def load_forbidden_terms():
    """从**仓外**配置读取禁用词。

    优先级：
      1. 环境变量 LGD_FORBIDDEN_TERMS（逗号分隔）
      2. 用户目录文件 ~/.lgd-gate/forbidden.txt（一行一词，# 开头为注释）

    读不到 ⇒ 返回空列表（调用方据此跳过该类检查并打印提示）。
    设计意图：公开仓库里的文件不得承载任何受控字面量。
    """
    raw = os.environ.get("LGD_FORBIDDEN_TERMS", "")
    if raw.strip():
        return [t.strip() for t in raw.split(",") if t.strip()]
    cfg = os.path.join(os.path.expanduser("~"), ".lgd-gate", "forbidden.txt")
    if os.path.isfile(cfg):
        out = []
        try:
            for line in open(cfg, encoding="utf-8"):
                line = line.strip()
                if line and not line.startswith("#"):
                    out.append(line)
        except Exception:
            pass
        return out
    return []


def read_epub_texts(path):
    """解压 epub，返回 {内部路径: 文本}。"""
    out = {}
    try:
        z = zipfile.ZipFile(path)
    except Exception as e:
        return {"__ERR__": "无法打开: %s" % e}
    for n in z.namelist():
        if not n.lower().endswith((".xhtml", ".html", ".opf", ".ncx", ".xml", ".txt")):
            continue
        try:
            out[n] = z.read(n).decode("utf-8", errors="replace")
        except Exception:
            pass
    return out


def collect_units():
    """返回 [(显示名, 文本, 是否位于生成物目录)]。"""
    units = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            fp = os.path.join(dirpath, fn)
            rel = os.path.relpath(fp, ROOT).replace("\\", "/")
            is_gen = any(rel.startswith(d + "/") for d in GEN_DIRS)
            low = fn.lower()
            if low.endswith(".epub"):
                for inner, txt in read_epub_texts(fp).items():
                    units.append(("%s!%s" % (rel, inner), txt, is_gen))
            elif low.endswith(TEXT_EXT):
                try:
                    units.append((rel, open(fp, encoding="utf-8", errors="replace").read(), is_gen))
                except Exception:
                    pass
    return units


def main():
    ssot = tomllib.load(open(SSOT_PATH, "rb"))
    rel_ver = ssot["release"]["version"]
    lib_ver = ssot["library"]["version"]
    legacy = list(ssot["library"].get("legacy", []))
    author = ssot["author"]

    allowed_author_forms = {
        author["display"], author["cite"], author["zh_display"],
        "%s, %s" % (author["family"], author["given"]),
        "%s %s" % (author["given"], author["family"]),
        "%s / %s" % (author["zh_display"], author["display"]),
    }
    allowed_versions = {rel_ver, lib_ver} | set(legacy)

    terms = load_forbidden_terms()
    units = collect_units()

    print("=" * 72)
    print("生成物口径漂移 + 全仓禁用词检出")
    print("仓库：%s" % ROOT)
    print("扫描单元：%d（含 epub 内部解压）" % len(units))
    print("SSOT 允许版本：%s" % "/".join(sorted(allowed_versions)))
    if terms:
        print("禁用词配置：已加载 %d 条（来源：仓外配置，不落盘于仓库）" % len(terms))
    else:
        print("禁用词配置：[未加载] 环境变量 LGD_FORBIDDEN_TERMS 与 ~/.lgd-gate/forbidden.txt 均无")
        print("                 ⇒ 本轮跳过「禁用词」这类检查（其余检查照跑）")
    print("=" * 72)

    problems = []
    for name, txt, is_gen in units:
        # 禁用词（仓外配置驱动；不区分大小写，字面匹配）
        low = txt.lower()
        for t in terms:
            tl = t.lower()
            start = 0
            while True:
                i = low.find(tl, start)
                if i < 0:
                    break
                ln = txt[:i].count("\n") + 1
                problems.append((name, "禁用词命中", ln, txt[max(0, i - 24):i + len(t) + 24].replace("\n", " ")))
                start = i + len(t)

        # 通用形态：品牌组合式（用配置词两两组合，避免在本文件写死）
        for a in terms:
            for b in terms:
                if a == b:
                    continue
                pat = r"%s\s*[\u00d7xX]\s*%s" % (re.escape(a), re.escape(b))
                for m in re.finditer(pat, txt):
                    ln = txt[:m.start()].count("\n") + 1
                    problems.append((name, "品牌组合式", ln, m.group(0)[:60]))

        # 版本号：**只对生成物目录**检查。
        # 全仓其他文档（论文 / 理论件）各有自己的版本号（v0.1 / v1.2 / v3.2 ...），
        # 那些是文档自身版本，不是文库版本，不属于「产物偏离 SSOT」的判据
        # —— 2026-09-24 实测：一旦扩到全仓，此类误报 140+ 条。
        if is_gen:
            for m in re.finditer(r"\bv(\d+\.\d+\.\d+)\b", txt):
                v = m.group(1)
                if v not in allowed_versions:
                    ln = txt[:m.start()].count("\n") + 1
                    problems.append((name, "版本号不在 SSOT 允许集", ln,
                                     "v%s（允许 %s）" % (v, "/".join(sorted(allowed_versions)))))
            for m in re.finditer(r"\bv(\d+\.\d+(?!\.))\b", txt):
                v = m.group(1)
                if v not in allowed_versions:
                    ln = txt[:m.start()].count("\n") + 1
                    problems.append((name, "短版本号不在 SSOT 允许集", ln,
                                     "v%s（允许 %s）" % (v, "/".join(sorted(allowed_versions)))))

    if not problems:
        print("[PASS] 未发现口径漂移与禁用词命中")
        print("结论：PASS")
        return 0
    seen = set()
    for name, label, ln, got in problems:
        key = (name, label)
        if key in seen:
            continue
        seen.add(key)
        print("[FAIL] %-46s :%-5s %-22s %s" % (name[:46], ln, label, got))
    print()
    print("合计问题：%d" % len(problems))
    print("结论：FAIL —— 未通过。修源头后重跑；勿手改产物。")
    return 1


if __name__ == "__main__":
    sys.exit(main())
