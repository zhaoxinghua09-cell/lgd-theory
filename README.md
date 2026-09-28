# lgd-theory
## 许可说明 · License Notice

> **本仓库使用自定义许可，不是 MIT / Apache-2.0**。平台显示为 `Other`（NOASSERTION），
> 属识别算法的正常结果，**不代表本仓库处于无许可状态**。

- **权利状态**：全部内容保留所有权利（All Rights Reserved）。未经书面许可，
  不得复制、改编、再分发、公开传播或用于衍生作品。
- **可否引用**：可以。允许在**注明出处**的前提下引用与学术、公共讨论；
  引用时请同时标注仓库名、原文链接 `https://github.com/zhaoxinghua09-cell/lgd-theory`
  与权利人「赵兴华 / Steven Zhao·China」。
- **完整条款**：见仓库根目录 [LICENSE](LICENSE)。
- **分层许可（2026-09-28 统一口径）**：本仓**理论文本与方法论 = 保留所有权利（ARR）**；机器可校验规范层（`uibc-core` 仓 `lgd-core/`：manifest schema + validator + 测试）中的**代码 = Apache-2.0**，以该仓 LICENSE 为准；公众号公开文章另行按 CC BY 4.0 署名发布。
- **Zenodo 存档许可沿革（2026-09-28 起）**：本仓 Zenodo 存档（concept DOI `10.5281/zenodo.22456647`）v1.5.0 及更早版本的元数据曾标注 CC BY 4.0——已发布快照不可变，按其原标注保留；**自 v1.6.0（version DOI `10.5281/zenodo.23019507`，2026-09-28）起新版存档不再授予任何许可（保留所有权利）**，显式声明见该版本描述区。
- **规范执行层指针**：三律的机器可校验规范（manifest schema + validator + 28 项测试）见 [`zhaoxinghua09-cell/uibc-core`](https://github.com/zhaoxinghua09-cell/uibc-core) 仓 `lgd-core/` 目录（本仓 = 理论总仓/上游，该目录 = 规范执行层/下游）。
- **联系**：zhaoxinghua06@126.com ｜ ORCID 0009-0001-0512-1237
- **品牌状态限定**：MedXpert、SynomosAI、LGD 等为相关项目标识，
  **均未申请实体注册、未申请商标注册**；出现仅作来源标识，
  不构成对法人实体或商标权的任何主张。
- **免责**：本仓库内容不构成法规意见或注册代理服务；关键数据以监管机构最新发布为准。

---


![LGD](assets/badges/lgd-aligned-en.svg)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22456647.svg)](https://doi.org/10.5281/zenodo.22456647)
[![Cite](https://img.shields.io/badge/Cite-BibTeX%20%7C%20APA-0b1e3a?logo=latex&logoColor=white)](CITE.md)
[![TL;DR](https://img.shields.io/badge/TL%3BDR-2%20min-14b8a6)](TLDR.md)
[![License: ARR custom](https://img.shields.io/badge/License-All_Rights_Reserved_(custom)-lightgrey.svg)](LICENSE)

> **Start here** · 2-minute version: [`TLDR.md`](TLDR.md) (CN/EN) · How to cite: [`CITE.md`](CITE.md) · Full library: [`book/`](book/) (LGD-Library v1.1, EPUB/HTML) · Brand & badges: [`badge/EMBEDS.md`](badge/EMBEDS.md) · AI-crawler index: [`llms.txt`](llms.txt) · **Web home**: [GitHub Pages](https://zhaoxinghua09-cell.github.io/lgd-theory/)


**Domain badges** · 金融 · 证据 · 政务 · 链上 · 驾驶 · 数据 · 低空 · 具身 · 工业 · 生物 · 教育 · 医械注册 —— 16 方向 × EN/CN（`assets/badges/directions/`，v8 象牙色调）：
![FIN](assets/badges/directions/lgd-aligned-fin-en.svg)
![LAW](assets/badges/directions/lgd-aligned-law-en.svg)
![GOV](assets/badges/directions/lgd-aligned-gov-en.svg)
![CRYPT](assets/badges/directions/lgd-aligned-crypt-en.svg)
![MED](assets/badges/directions/lgd-aligned-med-en.svg)

**The three laws**（`assets/badges/laws/`）· **LGD-powered**（`assets/badges/powered/`）：
![REGISTERED](assets/badges/laws/lgd-registered-en.svg)
![EVIDENCED](assets/badges/laws/lgd-evidenced-en.svg)
![GATED](assets/badges/laws/lgd-gated-en.svg)
![Powered](assets/badges/powered/lgd-powered-en.svg)

**Lifecycle Governance Doctrine (LGD) — 全程治理论** · *Registry · Evidence · Gates across the full life of AI and devices*

> 中文：凡自治之物——有籍、有证、有门禁，由生到退，全程可溯、可证、可问责。
> English: Every self-governing entity (AI, intelligent device, agent) shall carry a **registry**, **evidence**, and **evolution gates** — traceable, provable, and accountable across its full lifecycle.

**Canonical naming**（统一口径 · 对外引用请照此）

- 🇬🇧 **English formal term**: **Evidence-Gated AI Lifecycle Governance**
- 🇨🇳 **唯一中文主权词**: **凡自治之物**（恒定搭配 **有籍 · 有证 · 有门禁**）
- 🔤 **缩写**: **LGD** ｜ **全称**: Lifecycle Governance Doctrine（全程治理论）
- 📐 **对标口径**: 对齐 GB/Z 185—2026 系列与 ISO/IEC 42001 / NIST AI RMF / EU AI Act / IETF·CSA 方向 —— 本论提供**实现层（How）+ 医械域实例化 + 跨域母版**

**Proposed by**: SynomosAI Governance Line — an independent research initiative bridging a regulated-industry practice background (medical devices) and a cross-domain governance thought line (AI & autonomous systems).
**Author**: Zhao Xinghua (Steven Zhao) · ORCID [`0009-0001-0512-1237`](https://orcid.org/0009-0001-0512-1237) · full byline via [`CITE.md`](CITE.md)

---

## What is LGD?

Mainstream AI-governance efforts are **single-point**: some solve *identity* ("who is it" — passports/registration), some solve *evidence* ("prove it" — audit trails/explainability), some solve *gates* ("who lets it grow" — change control/alignment review). **Almost no one chains these single points into one lifecycle thread.**

LGD claims the missing dimension: governance is not a registration event nor a policy paper, but an **unbroken chain from birth to retirement**. Every self-governing entity should be governed along that chain.

## The Doctrine — three laws

| Law | Claim | Plain wording |
|---|---|---|
| **LGD-I · Registry（有籍）** | Every entity is registered at birth — identity, creator, governance owner, records. | Register everything; no exemption by size or privacy. |
| **LGD-II · Evidence（有证）** | Every key act leaves evidence — decision logs, risk records, change records, human-oversight proof, incident ledger. | Claims must carry source & signature (traceability). |
| **LGD-III · Gates（有门禁）** | Every evolution passes a gate — capability upgrade, re-release, permission expansion go through trigger → assessment → release → review. | High-stakes authority belongs to humans; machines request, humans authorize. |

**Corollary**: the **medical-device lifecycle regulation** (classification → design → risk → registration → clinical → quality → post-market → retirement) is the closest *real-world reference model* for governing AI. LGD generalizes that model to every regulated autonomous thing: financial AI, autonomous driving, robotics, low-altitude systems, data assets, and more.

## Repository layout

```
lgd-theory/
├── README.md                 ← this file
├── llms.txt                  ← machine-readable index for AI crawlers
├── LICENSE                   ← custom, All Rights Reserved (theory texts)
├── CHANGELOG.md
└── docs/
    ├── LGD-Lifecycle-Governance-Doctrine-v1.0.md   ← flagship paper (EN/CN)
    └── (per-domain series: financial AI, autonomous driving, data assets, ...)
```

## Publications

- **Flagship paper (v1.0, 2026-09)**: `docs/LGD-Lifecycle-Governance-Doctrine-v1.0.md` — full statement: abstract, three laws, medical-device reference model, "three checks" for putting any entity under LGD, honest boundaries.
- **Meta-method & sister theories (`docs/theories/`, 2026-09-08)**:
  - **RRM — Real-world Reference Method (TH-META-001)**: `docs/theories/RRM-Realworld-Reference-Method-v1.0.md` — the meta-method behind the whole series: for every AI capability gap, find a proven real-world mechanism and map it structurally (S ≅ M); with the prior-suspicion principle. Instantiated 6× (MAIT / SIDE / AFG / UBIC-Mem / BTSK / LDGF).
  - **MAIT — Memory-Anchor Identity Theory (TH-AIG-006)**: `docs/theories/MAIT-Memory-Anchor-Identity-v1.0.md` — AI identity anchored in memory continuity (vs. passport-only identity); mother template: real-world identity confirmation (registry + ID + memory continuity). JSON-LD speedpages: `docs/theories/MAIT-speedpage.html`, `docs/theories/RRM-speedpage.html`.
- **Cross-domain governance angles (`TH-ANG`, 2026-09-10)** — the second blank axis: **angles** cut across *all* domains (retirement / memory / accountability / runtime / insurability), while **domains** cut across industries. Every descriptive English name collided at the theory layer (5/5), so all five use **LGD-coined terms** (theory-layer zero collision), with the descriptive name kept as a search-facing subtitle. Coined-term repos each carry definition + collision rationale + citation format:

| Angle | Coined term | Descriptive subtitle | Repo |
|---|---|---|---|
| #1 | **Terminance** | Retirement Governance | [terminance](https://github.com/zhaoxinghua09-cell/terminance) |
| #2 | **Mnemoship** | Portable Memory Law | [mnemoship](https://github.com/zhaoxinghua09-cell/mnemoship) |
| #3 | **Culpachain** | Multi-Agent Accountability | [culpachain](https://github.com/zhaoxinghua09-cell/culpachain) |
| #4 | **Runtigil** | Runtime Gatekeeping | [runtigil](https://github.com/zhaoxinghua09-cell/runtigil) |
| #5 | **Assurability** | Governance-Conditioned Insurability | [assurability](https://github.com/zhaoxinghua09-cell/assurability) |

  Collision rule (criterion v3, theory-first): **theory-layer collision = one-vote veto**; brand-layer collision = advisory only.
- **Domain series (planned)**: Financial AI (TH-FIN-001) · Electronic evidence chains (LAW) · Digital government trust (GOV) · On-chain asset governance (CRYPT) · Autonomous driving · Data-element lifecycle. Each domain = one theory paper mapping its own real-world regulatory model onto the three laws.

## Suggested citation

> Zhao, X. (2026). *Lifecycle Governance Doctrine (LGD): Registry, Evidence, and Gates Across the Full Life of AI and Devices.* SynomosAI Governance Line. v1.1.0. **DOI:** https://doi.org/10.5281/zenodo.22456647

## Honest boundaries

LGD is a **civil-society framework, not legal or regulatory advice**; device-regulation references are structural alignment, not an equivalence claim or compliance guarantee. Where a lifecycle link has no tooling yet, it is stated as a gap — LGD never claims fake completeness.

---

© XLGD · SynomosAI Governance Line · All Rights Reserved (theory texts; citation with attribution permitted — see LICENSE)

<sub>XLGD — X distinction mark. [xlgd](https://github.com/zhaoxinghua09-cell/xlgd)</sub>

---

## Machine-readable metadata

- Structured citation: [`schema.jsonld`](schema.jsonld) — schema.org `ScholarlyArticle`
- Agent collaboration conventions: [`AGENTS.md`](AGENTS.md)
- Citation pack: [`CITE.md`](CITE.md) · TL;DR: [`TLDR.md`](TLDR.md)
- Machine-readable index for AI crawlers: [`llms.txt`](llms.txt)
- Concept DOI: <https://doi.org/10.5281/zenodo.22456647> · ORCID: see [`CITE.md`](CITE.md)

## Knowledge bases (Chinese · Zhihu, public)

- 治理理论 · governance theory (this doctrine's home library): <https://zhida.zhihu.com/repositories/7685648966830716995>
- AI 治理与 A³ 法则: <https://zhida.zhihu.com/repositories/7685783071642929696>
- 检验与静默失败 · verification & silent failures: <https://zhida.zhihu.com/repositories/7687140878311277913>
- AI Agent 技能库 · the skill set: <https://zhida.zhihu.com/repositories/7687141648483994426>

## Sibling repositories (theory stack)

- **uibc-core / lgd-core** — machine-checkable spec of the three laws (manifest schema + validator + 28 tests; code Apache-2.0, theory texts ARR): <https://github.com/zhaoxinghua09-cell/uibc-core> (path `lgd-core/`)
- **agent-skills** — 109 zero-dependency skills implementing the three laws: <https://github.com/zhaoxinghua09-cell/agent-skills>
- **assayance** — Assayance / 试真法 (Falsifiable Assurance): <https://github.com/zhaoxinghua09-cell/assayance>
- **silent-failure-catalog** — 14 documented silent failure modes: <https://github.com/zhaoxinghua09-cell/silent-failure-catalog>
- **xlgd** — the `X` distinction mark: <https://github.com/zhaoxinghua09-cell/xlgd>
