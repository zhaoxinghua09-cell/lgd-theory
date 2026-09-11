# lgd-theory

![LGD](assets/badges/lgd-aligned-en.svg)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22456647.svg)](https://doi.org/10.5281/zenodo.22456647)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)

> **Start here** · 2-minute version: [`TLDR.md`](TLDR.md) (CN/EN) · How to cite: [`CITE.md`](CITE.md) · Full library: [`book/`](book/) (LGD-Library v1.1, EPUB/HTML) · Brand & badges: [`badge/EMBEDS.md`](badge/EMBEDS.md) · AI-crawler index: [`llms.txt`](llms.txt) · **Web homepages**: [GitHub Pages](https://zhaoxinghua09-cell.github.io/lgd-theory/) · [medxpert.cn/lgd.html](https://medxpert.cn/lgd.html)


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

**Proposed by**: MedXpert × SynomosAI — a dual-brand collaboration between a regulated-industry practice line (medical devices) and a cross-domain governance thought line (AI & autonomous systems).
**Author**: Zhao Xinghua / Steven Zhao · China · [ORCID 0009-0001-0512-1237](https://orcid.org/0009-0001-0512-1237) · [medxpert.cn](https://medxpert.cn)

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
├── LICENSE                   ← CC BY 4.0
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

> Zhao, X. (2026). *Lifecycle Governance Doctrine (LGD): Registry, Evidence, and Gates Across the Full Life of AI and Devices.* MedXpert × SynomosAI. ORCID 0009-0001-0512-1237. v1.1.0. **DOI:** https://doi.org/10.5281/zenodo.22456647

## Honest boundaries

LGD is a **civil-society framework, not legal or regulatory advice**; device-regulation references are structural alignment, not an equivalence claim or compliance guarantee. Where a lifecycle link has no tooling yet, it is stated as a gap — LGD never claims fake completeness.

---

© XLGD · MedXpert × SynomosAI · CC BY 4.0 · cite the author when sharing

<sub>XLGD — X distinction mark. [xlgd](https://github.com/zhaoxinghua09-cell/xlgd)</sub>

---

## Machine-readable metadata

- Structured citation: [`schema.jsonld`](schema.jsonld) — schema.org `ScholarlyArticle`
- Agent collaboration conventions: [`AGENTS.md`](AGENTS.md)
- Citation pack: [`CITE.md`](CITE.md) · TL;DR: [`TLDR.md`](TLDR.md)
- Concept DOI: <https://doi.org/10.5281/zenodo.22456647> · ORCID: [0009-0001-0512-1237](https://orcid.org/0009-0001-0512-1237)
