# STRUCTURE — 分层与改动代价

## 五层

| 层 | 目录 | 内容 |
|---|---|---|
| L1 总纲 | `docs/LGD-Lifecycle-Governance-Doctrine-v1.0.md`（+EN、Academic） | 全程治理论主文本 |
| L2 三律与框架 | `docs/theories/A3-Three-Laws-of-AI-Making-v1.0.md`、`XCGS-…`、`UBIC-…`、`BTSK-…`、`RRM-…`、`P5-…`，`docs/theories/angles/TH-ANG-001..005` | 三律、治理框架、身份协议、双时态知识库、参考方法、不可能性图谱、五个角度 |
| L3 分域 | `docs/LGD-{AUT,BIO,CRYPT,DAT,EDU,FIN,GOV,IND,LAW,ROB,UAS,MED}-001-*.md` | 13 域落点 |
| L4 论文与证据 | `papers/*.md(+.ots)`、`arxiv/main.tex`、`cases/`、`research/` | 论文、时间锚、案例、调研 |
| L5 产物与检验 | `book/`、`docs/index.html`、`_tools/`、`tools/`、`.github/workflows/` | 电子书、站点、生成校验、评审门禁 |

## 改动代价

| 你想做 | 改哪里 | 必须重跑 | 必须同步 |
|---|---|---|---|
| 改三律表述 | L2 文本 | `_tools/verify_generated.py` | 全部 13 个分域引用、`book/`、`llms.txt` |
| 改主纲 | L1 文本 | 同上 + `sync_meta.py` | EN 版、Academic 版、DOI/引用文件 |
| 加分域 | 新建 `docs/LGD-XXX-001` | `lgd-ci-gate.yml` | `docs/sitemap.xml`、`_meta/source.toml`、badge 资产 |

## 边界

本仓产出**文本与判据**，不产出可执行判定器。
判定器在 `lgd-engine` 与 `lcas`；证据链在 `uibc-core`；本文不声称"理论已验证"，只声称"文本可追溯、有时间锚"。
