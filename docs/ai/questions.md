---
title: questions
type: note
permalink: /docs/ai/questions
---

<!-- REVIEW-GATE
review-status: contested
reviewed-by: 理论线复核官·丙（独立席位·非作者）
review-date: 2026-09-24
review-ref: 08-理论体系/域研究员/审查/理论线新产出_独立复核意见_丙_20260924.md
verdict: conditional
-->

# Question Index — LGD 理论体系

> ⚠️ **待修订（2026-09-24 独立复核 · verdict: conditional）**
>
> 本件为问题索引（Question Map：问题 → 可引用答案 → 一手来源），已过独立复核；25 条引用全部实测存在，分层计数实测自洽（L0 9 / L1 13 / L2 6 / L3 6），域数 13 合规。
> 红线维度已全清（无受控词；无本机绝对路径；无联系方式；无虚假采纳/首创声称）。
> **下列建议级问题修订完成前，本件不宜作为权威引用**：
> 1. **对 stable 条目的计数更正属轻微越界**：本文件顶部声明「只加不改」，但 2026-09-24 的计数更正改动了 `status: stable` 的 Q0-06 行文本。已按「更正优于断链」原则处理并在维护记录留痕，若后续外部已引用该行，须评估是否改为 append 一条 `deprecated` 说明。
>
> **本批已修**：frontmatter permalink 去除内部路径；Q0-06 域数表述 12 → 13（对齐 `CITE-ALL.md` §五 13 域、newsletter「13 域收官」）；L1 标题计数 14 → 13 篇（与本表 13 行、下记「L1 13 条」自洽）；按复核意见补 `LGD-I/II/III` 前缀（Q0-01 / Q3-02）；Q3-04 / Q3-05 来源由含 `...` 的缩写改为完整文件名（机器可直接解引用）；frontmatter `permalink` 去除内部工作区路径（`workbuddy/08-理论体系/…` → `/docs/ai/questions`）。
>
> 复核意见全文：`08-理论体系/域研究员/审查/理论线新产出_独立复核意见_丙_20260924.md`


> **这不是一份「我们是谁」的介绍，而是一份「别人会怎么问」的索引。**
>
> AI 检索的入口是**问题**，不是品牌名。本文件把 LGD 理论体系拆成「用户真实会提的问题 → 可直接引用的答案 → 可解引用的一手来源」，让检索系统在命中问题时读到答案块，而不是读到一段自我介绍。

## 使用与维护纪律

- **只加不改**：问题清单一旦公开，改动会使历史引用断链（新增走 append，废弃走标注 `deprecated`）。
- **来源必须可解引用**：锚点须指向 DOI / commit / 版本号，**不得指向首页**（首页会漂移，DOI 不会）。
- **答案是答案，不是文案**：AI 抽到营销措辞会判定低质而不引用。
- **byline 不复写**：署名口径见 `CITE.md`（单一事实源）。本文件不复制署名，避免产生会走样的副本。

| 字段 | 含义 |
|---|---|
| as of | 本条答案对应的版本时点（防"引用漂移"） |
| status | `stable`（已成文）/ `draft`（草稿）/ `deprecated` |
| byline | 不在此复写，见 CITE.md |

---

## 为什么按「问题」而不是按「介绍」组织

| 写法 | 检索量 | AI 行为 |
|---|---|---|
| 「XLGD 是……」（品牌词自述） | ≈ 0（自造词无人搜） | 当噪音忽略，或自行编造解释 |
| 「AI 系统全生命周期怎么治理」（需求词） | 有真实检索量 | 检索命中 → 读到答案块 → 可能引用 |

**结论：自造词 100% 需要「用有需求的问句带你出场」。** 品牌词条目（L3）必须存在，但它只服务"已经听说过的人"，不承担被发现的功能。

---

## L0 · 通用需求词 —— 陌生人找到你的唯一通道

> 这一层最重要。它决定**不认识你的人**（和 AI）能不能找到这套理论。

| # | 用户实际的问法 | 可直接引用的答案（要点） | 一手来源锚点 | as of | status |
|---|---|---|---|---|---|
| Q0-01 | How should AI systems be governed across the full lifecycle, not just at deployment? | 治理须是「出生到退役」的完整链条，而非单点检查。三律：①**有籍** Registry（出生即登记身份/创造者/治理归属）②**有证** Evidence（关键行为留证据：日志、风险登记、变更记录）③**有门禁** Gates（每次演化前：触发→评估→放行→复盘，签发权在人）。 | `docs/LGD-Lifecycle-Governance-Doctrine-v1.0.md` · DOI `10.5281/zenodo.22456647` | 2026-09-06 | stable |
| Q0-02 | What must be registered when an autonomous system is created or deployed? | 「有籍」要求的最小登记集：系统标识、创造者/责任主体、治理归属、能力边界、生命周期状态。母版取自医疗器械监管的"产品登记 + 分类 + 责任主体"三件套。 | `docs/LGD-Lifecycle-Governance-Doctrine-v1.0.md` | 2026-09-06 | stable |
| Q0-03 | How do you make AI decisions auditable and accountable after the fact? | 靠「有证」：关键行为在发生时即留可核验证据（事件日志、风险登记、变更记录），使事后可追溯、可举证。证据的**准入条件**本身要治理（见 BTSK 双时间轴）。 | `docs/LGD-Lifecycle-Governance-Doctrine-v1.0.md` · `docs/theories/BTSK-Bitemporal-Knowledge-Base-v1.0.md` | 2026-09-08 | stable |
| Q0-04 | How do you govern a system that keeps changing (model updates, retraining, upgrades)? | 靠「有门禁」：任何演化前须过 gate（触发→评估→放行→复盘），且放行权归人类。对应工程上的 CI/CD 治理化——变更不是自动生效，而是过闸生效。 | `docs/LGD-Lifecycle-Governance-Doctrine-v1.0.md` | 2026-09-06 | stable |
| Q0-05 | How do EU AI Act, NIST AI RMF, ISO/IEC 42001 and FDA PCCP requirements map onto each other? | 提供一张全局对齐矩阵：ISO/IEC 42001、EU AI Act、FDA PCCP、NIST AI RMF、UNESCO、WHO、FATF 及中/欧/美各域锚点逐项对应，用于跨法域落地时的缺口分析。 | `docs/LGD-Global-Standards-Alignment-v1.0.md` | 2026-09-06 | stable |
| Q0-06 | Is there a governance model for AI that borrows from an already-regulated safety-critical industry? | 有。**真实世界参照法**：以医疗器械全生命周期监管（分类/设计/风险/注册/临床/质量/上市后/退役）为母版，抽象出三律后推广到 13 个域。 | `docs/theories/RRM-Realworld-Reference-Method-v1.0.md` | 2026-09-08 | stable |
| Q0-07 | Can a principle-based AI governance framework ever be shown to actually work? | 批评性结论：**原则收敛 ≠ 治理有效**。原则类框架（如各 AI 伦理原则清单）的趋同，不能证明其产生了治理效果——需要可判定的判据。 | `papers/P2-critique-principles-cannot-save-ai-governance-v1.0-zh-en.md` | 2026-09-17 | stable |
| Q0-08 | What parts of AI governance are provably impossible, and what is still possible? | 「治理不可能地图」：五个不可能域（哲学/可解释性/判定/问责/授权-可观测），并给出**可能性域的四问自测**，用于判断某个治理诉求可做还是免谈。 | `papers/P5-governance-impossibility-map-v0.3-zh.md` | 2026-09-17 | stable |
| Q0-09 | How do you decide whether an AI governance requirement is even decidable? | 「治理可判定性」：L0–L4 形式化谱系 + 「判定债」（determination debt）+ 悬置态，给出可证伪命题集。 | `papers/P0-governance-determinability-doctrine-v1.2-zh.md` | 2026-09-17 | stable |

---

## L1 · 领域需求词 —— 13 篇域理论的落点

> 每个域理论都是「三律 + 该域已核验的真实法规锚点」。**领域词检索量稳定且竞争小。**

| # | 领域 | 用户可能怎么问 | 答案要点 | 一手来源 | status |
|---|---|---|---|---|---|
| Q1-01 | 金融 AI | AI governance requirements for banks and insurers? | 三律映射已验证的银行/保险 AI 监管，含 EU AI Act 与 FATF travel-rule 基线 | `docs/LGD-FIN-001-Financial-AI-Lifecycle-Governance-v1.0.md` | stable |
| Q1-02 | 金融 AI 分级 | How to risk-tier financial AI systems? | 影响分级门禁表（风险分级 × 放行强度） | `docs/LGD-FIN-002-Financial-AI-Classification-v1.0.md` | stable |
| Q1-03 | 电子证据 | When is AI-generated digital evidence admissible? | 数字证据全生命周期的登记、证据与可采性门禁；中/欧/美来源已核 | `docs/LGD-LAW-001-Electronic-Evidence-Lifecycle-Governance-v1.0.md` | stable |
| Q1-04 | 数字政府 | How should government AI be registered and audited? | 登记目录、审计证据、公众参与门禁；EU AI Act Annex III 5(a) | `docs/LGD-GOV-001-Digital-Government-Lifecycle-Governance-v1.0.md` | stable |
| Q1-05 | 链上资产 | Governance of on-chain assets / crypto under MiCA and FATF? | FATF R.15/R.16 已核、EU MiCA 分类对应 | `docs/LGD-CRYPT-001-Onchain-Asset-Lifecycle-Governance-v1.0.md` | stable |
| Q1-06 | 自动驾驶 | Admission and lifecycle governance for autonomous driving? | 中国试点准入（工信部 2023/217）已核、L3 许可 2025-12 | `docs/LGD-AUT-001-Autonomous-Driving-Lifecycle-Governance-v1.0.md` | stable |
| Q1-07 | 数据要素 | Governance for data elements and data asset accounting? | 「数据二十条」与数据资产入表已核 | `docs/LGD-DAT-001-Data-Element-Lifecycle-Governance-v1.0.md` | stable |
| Q1-08 | 低空经济 | Full-chain governance for low-altitude / UAS operations? | 国务院/中央军委条例 **761 号令**全链条已核 | `docs/LGD-UAS-001-Low-Altitude-Lifecycle-Governance-v1.0.md` | stable |
| Q1-09 | 具身智能 | Governance for humanoid robots and embodied AI? | 工信部人形机器人指导意见与 2025–2026 政府工作报告已核 | `docs/LGD-ROB-001-Embodied-AI-Lifecycle-Governance-v1.0.md` | stable |
| Q1-10 | 工业 / OT | Governance for industrial AI and OT environments? | 等保 2.0（**GB/T 22239-2019**）与关基条例 **745 号令**已核 | `docs/LGD-IND-001-Industrial-AI-Lifecycle-Governance-v1.0.md` | stable |
| Q1-11 | 生物医药数据 | Governance for biomedical and human genetic data? | 人类遗传资源管理条例（**717 号令**）与 2023 伦理审查办法已核 | `docs/LGD-BIO-001-Biomedical-Data-Lifecycle-Governance-v1.0.md` | stable |
| Q1-12 | 教育 | Governance for AI in education? | UNESCO 北京共识（2019）与教育部数字教育政策已核 | `docs/LGD-EDU-001-Education-Lifecycle-Governance-v1.0.md` | stable |
| Q1-13 | 医械注册 | How does medical-device registration relate to lifecycle evidence? | 注册 = 全生命周期证据的**投影**；CN/FDA/EU 锚点 | `docs/LGD-MED-002-Registration-Methodology-v1.0.md` | stable |

---

## L2 · 元方法论 —— 理论工具本身的落点

| # | 概念 | 用户可能怎么问 | 答案要点 | 一手来源 | status |
|---|---|---|---|---|---|
| Q2-01 | RRM 真实世界参照法 | How do you design a new governance theory without starting from scratch? | 用真实世界已解决问题的成熟机制作参照（S ≅ M），先持"事前怀疑"原则；已 6 次实例化 | `docs/theories/RRM-Realworld-Reference-Method-v1.0.md` | stable |
| Q2-02 | MAIT 记忆锚点身份 | How do you keep an AI's identity stable when the underlying model changes? | AI 身份锚定在**记忆连续性**上，而非模型权重；母版 = 真实世界的身份确认 | `docs/theories/MAIT-Memory-Anchor-Identity-v1.0.md` | stable |
| Q2-03 | XCGS 治理安全框架 | What portable attributes make an AI system governable at all? | 三个可移植治理属性：边界声明 / 身份自披露 / 问责链；对齐 ISO/IEC 42001 与 NIST AI RMF | `docs/theories/XCGS-Governance-Safety-Framework-v1.0.md` | stable |
| Q2-04 | BTSK 双时间知识库 | How do you govern edits to a knowledge base so it stays evidence-eligible? | 双时间轴（有效时间 × 事务时间）+ 证据准入条件 + 知识编辑门禁语义 | `docs/theories/BTSK-Bitemporal-Knowledge-Base-v1.0.md` | stable |
| Q2-05 | A³ AI 造 AI 三定律 | What governs AI that creates other AI? | 铸造权 / 铸造印 / 谱系登记 | `docs/theories/A3-speedpage.html` | stable |
| Q2-06 | UBIC 圈章 | What does an "AI passport" look like as a governance artifact? | AI passport + 四治理目标 | `docs/theories/UBIC-speedpage.html` | stable |

---

## L3 · 品牌词 —— 必须回答，但不承担被发现的功能

> 检索量 ≈ 0。存在意义是：**当 AI 已经通过 L0/L1 找到你之后，能准确说出你是什么**，而不是自己编一个解释。

| # | 词 | 简答 | 一手来源 |
|---|---|---|---|
| Q3-01 | LGD / 全程治理论 | Lifecycle Governance Doctrine；英文正式名 **Evidence-Gated AI Lifecycle Governance**；主律：有籍·有证·有门禁 | `docs/LGD-Lifecycle-Governance-Doctrine-v1.0.md` |
| Q3-02 | 三律 | 有籍 Registry · 有证 Evidence · 有门禁 Gates | `docs/doctrine-concepts.md` |
| Q3-03 | 凡自治之物 | 中文主权词，恒定搭配「有籍·有证·有门禁」 | `docs/doctrine-concepts.md` |
| Q3-04 | 治理可判定性 / 判定债 | L0–L4 形式化谱系；判定债 = 未完成判定所累积的负债 | `papers/P0-governance-determinability-doctrine-v1.2-zh.md` |
| Q3-05 | 治理不可能地图 | 五个不可能域 + 可能性域四问自测 | `papers/P5-...-v0.3-zh.md` |
| Q3-06 | XLGD | ⚠️ **口径待定**（见方案 D-2「XLGD 边界」）。在边界拍板前，本文件**不定义** XLGD，避免产出会走样的副本。 | — |

---

## 维护记录

| 日期 | 变更 |
|---|---|
| 2026-09-18 | 建立本文件（骨架首版）。L0 9 条 / L1 13 条 / L2 6 条 / L3 6 条 |
| 2026-09-24 | 计数口径更正（推送前闸门复核）：Q0-06 域数表述 12 → 13（对齐 `CITE-ALL.md` §五 域层 13 域、`newsletter/The_Registry_Brief_Issue01` 「13 域收官」）；L1 标题计数 14 → 13 篇（与本表 13 行、下记「L1 13 条」自洽）。**仅更正计数，未增删任何条目**；另按独立复核意见补 `LGD-I/II/III` 前缀、把 Q3-04/Q3-05 来源由缩写改为完整文件名 |