#!/usr/bin/env python3
"""test_text_contract.py — 文本仓的结构契约测试（离线可跑）。

跑法：python -m unittest discover tests  （或 python tests/test_text_contract.py）
退出码 0 = 契约成立；非 0 = 逐条列出违约。

覆盖三条不变式：
  1. 仓库根必须有 LICENSE / README.md / CITE.md（引用可解析的前提）
  2. _meta/source.toml 可解析，且其中列出的路径都存在
  3. docs/ 下每个 .md 非空且以一级标题开头（单一来源可读）
"""
import pathlib, re, sys, tomllib, unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
REQUIRED = ["LICENSE", "README.md", "CITE.md"]
SOURCE = ROOT / "_meta" / "source.toml"

def _paths_from_toml(node):
    out = []
    if isinstance(node, dict):
        for v in node.values():
            out += _paths_from_toml(v)
    elif isinstance(node, list):
        for v in node:
            out += _paths_from_toml(v)
    elif isinstance(node, str):
        # 只把"像仓内相对路径"的串当路径。URL / DOI（10.xxxx/yyy）/ 邮箱都不是路径。
        s = node
        is_url = s.startswith(("http://", "https://"))
        is_doi = bool(re.match(r"10\.\d{4,}/", s))
        is_mail = ("@" in s and "://" not in s)
        looks_like_path = ("/" in s or s.endswith(".md")) and not s.startswith("/")
        if looks_like_path and not (is_url or is_doi or is_mail):
            out.append(s)
    return out

class TextContract(unittest.TestCase):
    def test_required_root_files(self):
        for f in REQUIRED:
            self.assertTrue((ROOT / f).exists(), f"根目录缺 {f}")

    def test_source_toml_parses_and_paths_exist(self):
        self.assertTrue(SOURCE.exists(), "_meta/source.toml 缺失")
        data = tomllib.loads(SOURCE.read_text(encoding="utf-8"))
        for sec in ("release", "title", "author", "repo"):
            self.assertIn(sec, data, f"source.toml 缺 [{sec}] 段")
        self.assertRegex(data["release"].get("version", ""), r"\d+\.\d+\.\d+",
                         "source.toml release.version 不是 x.y.z")
        missing = [p for p in _paths_from_toml(data) if not (ROOT / p).exists()]
        self.assertEqual(missing, [], f"source.toml 指向了不存在的路径: {missing}")

    def test_docs_md_have_heading(self):
        bad = []
        for p in (ROOT / "docs").rglob("*.md"):
            text = p.read_text(encoding="utf-8", errors="ignore").strip()
            # 剥掉可选的 YAML front matter（本仓 docs 按 Astro/permalinks 约定带 ---title--- 头）
            if text.startswith("---"):
                m = re.match(r"^---\s*\n.*?\n---\s*(\n|$)", text, re.DOTALL)
                if m:
                    text = text[m.end():].strip()
            # 再剥掉开头连续的 HTML 注释块（本仓用 <!-- REVIEW-GATE ... --> 记录复核席位）
            while text.startswith("<!--"):
                end = text.find("-->")
                if end < 0:
                    break
                text = text[end + 3:].strip()
            if not text:
                bad.append(f"{p.relative_to(ROOT)} 为空")
            elif not re.match(r"^#{1,3}\s+\S", text):
                bad.append(f"{p.relative_to(ROOT)} 未以标题开头")
        self.assertEqual(bad, [], "文档标题缺失: " + "; ".join(bad))

if __name__ == "__main__":
    unittest.main(verbosity=2)
