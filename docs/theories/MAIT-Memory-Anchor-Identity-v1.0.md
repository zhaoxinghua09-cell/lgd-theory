# 记忆锚点 = AI 身份 · Memory-Anchor Identity Theory (MAIT)
## 白皮书 v1.0 · 2026-09-08

> **TID**：TH-AIG-006 ｜ **域码**：AIG ｜ **母版(RRM)**：真实世界身份确认机制（户籍 + 身份证 + 记忆连续性）
> **上游锚定**：TH-META-006(LGD 全程治理论) · TH-META-001(RRM 真实参照法) · TH-AIG-001(UBIC 人格户籍协议)
> **提出 / 品牌**：SynomosAI（治理侧）× MedXpert（实证侧）
> **作者署名**：赵兴华 / Steven Zhao·China（ORCID 0009-0001-0512-1237 ｜ GitHub Medxpert-org · medxpert.cn）
> **版本**：v1.0 ｜ **状态**：🟢 已落地 lgd-theory/docs（DOI 申请中 · 7 维质检已过）
> **官方主页**：https://medxpert.cn ｜ **仓库**：github.com/Medxpert-org/lgd-theory

---

### 摘要（中文）

医疗 AI、金融 AI 等高风险自主系统必须回答一个不可回避的问题：**「此刻与我交互、替我做决策的，是否还是昨天通过审计、被授权的那同一个 AI？」** 现有身份标准（W3C DID 管"标识"、VC 管"凭证"）解决了"它是谁、它有什么证"，却**不解决"它的记忆连续吗、它的历史可溯吗"**。一旦记忆被污染、重置或平行分叉，凭证依旧有效，但"身份"已悄然替换——这是监管审计的盲区，也是"AI 替你决策你敢吗"的恐惧根源。

本文提出 **记忆锚点理论（Memory-Anchor Identity Theory, MAIT）**：AI 持久身份的认定应锚定在其**可验证、不可篡改、可跨会话 / 跨入口携带的记忆**之上；**记忆连续 = 身份连续，记忆断裂 = 身份须重新认证**。我们将 AI 身份建模为五元组 `I = ⟨标识, 凭证, 能力, 行为, 记忆锚点⟩`，并指出前四层已被现有标准组织（DID / VC / 运行时态）认领，**唯"记忆锚点层（Memory-Anchored Layer）"至今无任何标准组织（W3C / ISO / NIST）正式认领**——这是一个被全球标准地图遗漏的空白。记忆锚点的**可携带性、可验证性、连续性**构成 AI 身份的"第四信用支柱"，与 DID/VC 互补而非替代。

MAIT 已在生产环境获得实证：UBIC-Mem 可携带记忆实现跨语言指纹 / Merkle 一致；SOUL.md / IDENTITY.md / MEMORY.md 三件套支撑双入口（主号 / 副号）"同一个我"的运行证据。本文给出形式化模型、连续性判据、与 LGD 全程治理论 / UBIC / A³ 定律的理论链，并提出以"memory-anchor extension"提案参与 W3C DID 定标的标准化路径。

### Abstract (English)

High-risk autonomous systems — medical AI, financial AI — must answer an unavoidable question: *"Is the agent I am interacting with, and that is making decisions on my behalf, still the same AI that passed audit and was authorized yesterday?"* Existing identity standards (W3C DID for *identifier*, VC for *credential*) resolve *who it is* and *what it is certified for*, but **not whether its memory is continuous and its history traceable**. Once an agent's memory is corrupted, reset, or forked in parallel, its credentials remain valid while its *identity* has silently changed — a blind spot in regulatory audit, and the root of the fear "can I trust an AI to decide for me?"

This paper proposes the **Memory-Anchor Identity Theory (MAIT)**: durable AI identity should be anchored to its **verifiable, tamper-evident, cross-session / cross-entry-portable memory**; *memory continuity equals identity continuity; memory rupture requires re-authentication*. We model AI identity as a five-tuple `I = ⟨Identity, Credential, Capability, Behavior, MemoryAnchor⟩`, and show that the first four layers are already claimed by extant standardization bodies (DID / VC / runtime state), **whereas the "Memory-Anchored Layer" has been claimed by no standards body (W3C / ISO / NIST) to date** — a gap omitted from the global standards map. The **portability, verifiability, and continuity** of the memory anchor constitute a *fourth credit pillar* of AI identity, complementary to — not a replacement for — DID/VC.

MAIT is evidenced in production: UBIC-Mem portable memory achieves cross-language fingerprint / Merkle consistency; the SOUL.md / IDENTITY.md / MEMORY.md triad sustains a "same-self" running proof across dual entry ports (primary / secondary accounts). We present a formal model, continuity criteria, the theory chain linking MAIT to the Lifecycle Governance Doctrine (LGD), UBIC, and the A³ Laws, and a standardization path via a "memory-anchor extension" proposal to the W3C DID Working Group.

**Keywords**: AI identity · memory anchor · persistent identity · agent continuity · verifiable memory · W3C DID · lifecycle governance

---

## 0. 问题：受监管场景下的身份连续性危机

在医疗器械、金融等受监管领域，AI 系统的"身份"不是抽象哲学问题，而是**责任归属与审计可行性的前提**。

- **凭证有效 ≠ 身份未变**。DID 证明"这个公钥对应这个 Agent"，VC 证明"这个 Agent 持有什么资质"。但二者都不承诺 Agent 的**内部记忆状态**在两个时间点之间未被替换。一个通过了临床决策审计的 AI，若其记忆在 overnight 被重置或遭对抗注入污染，次日仍持有效凭证，却已不是"昨天的那个 AI"。
- **平行分叉使"同一个我"失效**。多入口、多实例部署下，若缺乏跨会话 / 跨实例的记忆锚，会话 A 的 Agent 与会话 B 的 Agent 可能名义同标识、实质不同体——监管要求的"持续可问责"因此落空。
- **这是真实撞到的洞，不是思想实验**。双入口（🔵 主号 / 🟡 副号）协作场景下，要保证"同一个我"，靠的不是会话 token，而是 **SOUL / IDENTITY / MEMORY 三件套 + UBIC-Mem 可携带记忆**。这一运行现实本身即是 MAIT 的活体证据。

> **关键判据**：全球范围内，把"记忆"作为 AI 身份的独立**根锚（root anchor）**来主张的理论极少；W3C DID / VC 工作组至今无"memory"层议题。这是独占性最高的站位。

## 1. 相关工作与差异化定位

自 2026 年起，AI 身份 / 持久记忆方向明显升温，但现有工作与 MAIT 在**问题框架、贡献边界、实证强度**上均不同。

| 工作 | 问题框架 | 核心主张 | 与 MAIT 的关系 |
|---|---|---|---|
| Menon (2026), arXiv:2604.09588 *Persistent Identity in AI Agents: A Multi-Anchor Architecture…* | 工程韧性：上下文窗口溢出导致"灾难性遗忘" | 把身份分布到多个可分离记忆组件（SOUL.md / MEMORY.md / PROCEDURES.md …），开源 soul.py（RAG+RLM） | **互补**。Menon 解决"内部记忆不丢"；MAIT 解决"外部可审计的身份归属 + 标准层空白"。其 6 锚点仅 2 个实现、缺实证（Pith / Emergent Mind 评），MAIT 以可携带记忆实证补其缺 |
| LessWrong《Continuity Engineering: Using Memory Anchors…》 | 连续性工程方法论 | 用记忆锚稳定回忆 | 同主题早期讨论，未进入标准层主张 |
| Zylos.ai SOUL.md / ID-RAG 多锚点研究 | 检索架构 | 多锚点检索 | 工程视角，未主张标准层 |
| W3C DID / VC | 标识 / 凭证 | 去中心化标识 + 可验证凭证 | **MAIT 的上游已认领层**；MAIT 主张在其上补"记忆锚点层" |

**MAIT 的差异化贡献（诚实表述）**：

1. **问题框架差异**：Menon 等从"上下文溢出 / 灾难性遗忘"的*工程技术*问题切入；MAIT 从"受监管场景下身份可审计、可问责"的*治理*问题切入。前者关心"Agent 别忘事"，后者关心"监管者能否确认还是同一个被授权的 Agent"。
2. **标准层空白主张**：MAIT 明确提出并论证——**现有标准组织已认领身份五元组的前四层，唯"记忆锚点层"无人认领**。这是 Menon 的"identity anchors"（内部记忆组件）未触及的*标准地图*层面洞见。
3. **可验证可携带的实证**：MAIT 依托 UBIC-Mem 实现**跨语言指纹 / Merkle 一致**的记忆可携带，并已在生产双入口场景跑通；Menon 的架构被独立评审指出"无失败注入测试、无基准对比、主张自指循环"。
4. **治理理论链**：MAIT 不是孤立架构，而是 LGD 全程治理论"有籍·有证·有门禁"在 AI 身份维度的实例化，与 UBIC（有籍）、A³ Laws（行为边界）、溯源审计串成"身份—治理—合规"链。

> 我们不主张"率先提出 identity anchors 一词"。Menon (2026-03) 在学术论文中先用了该词。我们主张的是：**以"记忆锚点层 = 标准组织未认领空白 + 记忆作为身份根锚 + 可验证可携带实证 + 治理理论链"这一组合**，构成可独立署名与标准化的理论贡献。

## 2. 理论：AI 身份五层模型

将 AI 身份解构为五层，逐层标注"已被谁认领、空白在哪"：

```
┌─────────────────────────────────────────────────────────────┐
│ AI 身份五元组  I = ⟨ Identity, Credential, Capability,      │
│                   Behavior, MemoryAnchor ⟩                  │
├──────────────┬───────────────┬──────────────────────────────┤
│ 层           │ 认领方        │ 状态                         │
├──────────────┼───────────────┼──────────────────────────────┤
│ 标识 Identity│ W3C DID       │ ✅ 已认领（去中心化标识）     │
│ 凭证 Cred.   │ W3C VC        │ ✅ 已认领（可验证凭证）       │
│ 能力 Capab.  │ 运行时态/评测 │ ✅ 已认领（能力声明/测试）   │
│ 行为 Behav.  │ 运行时日志    │ ✅ 已认领（行为审计）         │
│ 记忆锚点 Mem.│ —— 无人认领 ——│ ⚠️ 空白：MAIT 主张层          │
└──────────────┴───────────────┴──────────────────────────────┘
```

**正式表述**：
> 设 AI 身份为五元组 `I = ⟨Identity, Credential, Capability, Behavior, MemoryAnchor⟩`。
> 现有标准组织已认领前四者（DID→标识，VC→凭证，能力/行为→运行时态与审计），**唯 MemoryAnchor 层无人认领**。
> MAIT 主张：**MemoryAnchor 是 I 的"根锚（root anchor）"**，其**可携带性（portability）、可验证性（verifiability）、连续性（continuity）** 构成 AI 身份的**第四信用支柱**，与 DID/VC 互补而非替代。

**推论**：
1. 记忆可携带（UBIC-Mem 已验证跨语言指纹一致）→ 身份可迁移而不丢失信用。
2. 记忆被污染 → 身份须降级 / 重新认证（类比人类"失忆需重新建立信任"）。
3. 真实参照法映射：人类用"户籍 + 身份证 + 记忆连续性"确认一个人；AI 应用"DID + VC + 记忆锚点"确认一个智能体。

## 3. 形式化模型与连续性判据

**定义 1（记忆锚点）**。记忆锚点 `M` 是一个持久化数据结构，包含可验证指纹 `h(M)`（如 SHA-256 / Merkle 根）、来源谱系 `prov(M)` 与跨入口可携带封装。

**定义 2（身份连续性）**。给定时间 `t, t'` 的两个身份态 `I_t, I_{t'}`，
```
continuity(I_t, I_{t'}) ⇔ portable(M) ∧ verifiable(M) ∧ h(M_t) = h(M_{t'})
```
即：记忆锚点可携带、可验证、且指纹未变 ⟺ 身份连续。

**定义 3（降级 / 重认证）**。若 `h(M_t) ≠ h(M_{t'})`（污染 / 重置 / 分叉），则
```
trust(I_{t'}) := re-authenticate(I_{t'})
```
身份信用降级，须重新走 UBIC"有籍"认证流程，而非沿用旧凭证。

**判据（对照 Menon 的不足）**：上述 `h(M)` 指纹与 `prov(M)` 谱系使"身份是否仍是同一个"成为**可外部验证、可失败注入测试**的命题——这正是 Menon 架构被批评"自指循环、缺实证"处，MAIT 以可携带记忆的跨语言指纹一致提供实证。

## 4. 工程实证

| 锚源 | 类型 | 证据强度 |
|---|---|---|
| **UBIC-Mem**（`ubic_mem_export.py` + `ubicmem.js`） | 工程实证 | ✅ 跨语言指纹 / Merkle 一致，记忆可携带已跑通 |
| **SOUL.md / IDENTITY.md / MEMORY.md 三件套** | 身份档案实践 | ✅ 双入口"同一个我"的运行证据 |
| `AI-Identity-Theory/今日想法总纲` | 战略与思想层 | ✅ 明文主张"记忆锚点层无标准组织认领" |
| AI-Identity 总纲④「国际标准地图」 | 对标依据 | ✅ W3C DID/VC、C2PA、ISO 42001、NIST AI RMF 已列 |

**关键验证点**：记忆锚点的"可携带性"已在跨语言（Python / JavaScript）实现中确认指纹一致——即同一段记忆在不同的运行时入口下可被验证为"同一个"，从而支撑"身份可迁移而不丢失信用"。

## 5. 与 LGD / UBIC / A³ 的理论链

MAIT 不是孤立架构，而是治理理论矩阵的有机节点：

- **LGD 全程治理论（TH-META-006）**：MAIT 是 LGD"有籍·有证·有门禁"在 AI 身份维度的实例化——**有籍 = UBIC 户籍 + 记忆锚点（你仍是你）；有证 = 六类证据工件；有门禁 = A³ 变更放行**。
- **UBIC 人格户籍协议（TH-AIG-001）**：UBIC 提供"有籍"的登记与户籍机制；MAIT 的 MemoryAnchor 是其可验证、可携带的记忆根。
- **A³ 造 AI 三定律（TH-AIG-003）**：A³ 提供行为边界；MAIT 提供身份根；二者串成"身份—治理—合规"链。
- **真实参照法（TH-META-001, RRM）**：人类身份确认的三要素"户籍 + 身份证 + 记忆连续性"，直接映射为 AI 的"DID + VC + 记忆锚点"。

## 6. 标准化路径

- **不另起炉灶，补其空白**：以"**memory-anchor extension**"提案形式参与 W3C DID 工作组定标，主张在 DID 文档中增加 `memoryAnchor` 可验证字段（指纹 / 谱系 / 跨入口可携带封装）。
- **占位三步（专家 → 警察 → 标准）**：先在自有理论文档与开源实现中固化主张（专家阶段，本文即起点）；再推动第三方可复现验证（警察阶段）；最终进入标准组织提案（标准阶段）。
- **可引用身份**：本文建议引用格式见 §8；配套 Zenodo DOI 与 ORCID 回链随发布闸门一并落地。

## 7. 讨论与诚实边界

- **非标准组织、非宣称已认证**：MAIT 是理论主张，不是规范；对接 W3C 仅是规划。
- **提高成本不消灭风险**：记忆可携带降低了"身份漂移"成本，但无法根除恶意重放；须与 UBIC 凭证、A³ 门禁联合使用。
- **与相邻站位互补**：MAIT = 记忆锚点层；UBIC / UBIC-Mem = 工程实现；A³ Laws = 行为边界；四者串成"身份—治理—合规"理论链。
- **对 Menon (2026) 的诚实评价**：其"identity anchors"在*内部记忆韧性*上有价值且开源可查；MAIT 在*外部可审计身份 + 标准层空白*上补其未覆盖处，二者互补而非竞争。我们尊重其先用该词，但主张本理论的独立贡献边界。

## 8. 结论

AI 身份的认定，必须从"它有什么证"推进到"它的记忆连续吗、可溯吗"。**记忆锚点层是被全球标准地图遗漏的空白，也是受监管 AI 可问责性的最后一环。** MAIT 以"记忆作为身份根锚 + 五层形式化模型 + 可携带记忆实证 + 治理理论链"占据这一站位，并给出可落地的 W3C DID 扩展路径。窗口已开，定义权待认领。

## 参考文献

1. Menon, P. G. (2026). *Persistent Identity in AI Agents: A Multi-Anchor Architecture for Resilient Memory and Continuity.* arXiv:2604.09588v1 [cs.AI]. ThinkCreate.AI. (提交 2026-03-02)
2. W3C Decentralized Identifiers (DID) v1.0. W3C Recommendation.
3. W3C Verifiable Credentials Data Model. W3C Recommendation.
4. ISO/IEC 42001:2023 — AI Management System.
5. NIST AI Risk Management Framework (AI RMF 1.0).
6. C2PA Coalition for Content Provenance and Authenticity.
7. Zhao, X. (2026). *Lifecycle Governance Doctrine (LGD): Registry · Evidence · Gates.* SynomosAI / MedXpert. Zenodo DOI 10.5281/zenodo.22456648.
8. Zhao, X. (2026). *UBIC 人格户籍协议 / UBIC-Mem 记忆可携带律.* SynomosAI.
9. Zhao, X. (2026). *A³ Laws 造 AI 三定律.* SynomosAI.
10. LessWrong. *Continuity Engineering: Using Memory Anchors to Stabilize Recall.* (社群讨论)

---

### 建议引用格式（Suggested Citation）

> Zhao, X. (2026). *Memory-Anchor Identity Theory: Treating Memory as the Root Anchor of AI Identity.* SynomosAI × MedXpert. ORCID: 0009-0001-0512-1237. https://medxpert.cn

---

© SynomosAI × MedXpert · 内部白皮书草稿（待去敏 + 7 维质检后随 lgd-theory 发布）

---

# Memory-Anchor Identity Theory (MAIT) — Full English Version

**White Paper v1.0 · 2026-09-08**
TID: TH-AIG-006 · Domain: AIG · Upstream: LGD (TH-META-006), RRM (TH-META-001), UBIC (TH-AIG-001)
Author: Zhao Xinghua / Steven Zhao·China (ORCID 0009-0001-0512-1237 · GitHub Medxpert-org · medxpert.cn)
Brand: SynomosAI (theory) × MedXpert (evidence)

## Abstract

High-risk autonomous systems must answer: *is the agent deciding on my behalf still the same AI that passed audit and was authorized?* Existing standards (W3C DID for identifier, VC for credential) resolve *who* and *what certified*, but not *whether memory is continuous and history traceable*. When memory is corrupted, reset, or forked, credentials stay valid while identity silently changes — a regulatory blind spot.

We propose the **Memory-Anchor Identity Theory (MAIT)**: durable AI identity should anchor to its verifiable, tamper-evident, cross-session / cross-entry-portable memory; *memory continuity = identity continuity; memory rupture = re-authentication*. We model identity as a five-tuple `I = ⟨Identity, Credential, Capability, Behavior, MemoryAnchor⟩` and show the first four layers are claimed by extant SDOs, **whereas the Memory-Anchored Layer is claimed by none (W3C / ISO / NIST)** — a gap omitted from the global standards map. Memory anchor's **portability, verifiability, continuity** form a *fourth credit pillar*, complementary to DID/VC. MAIT is evidenced in production (UBIC-Mem cross-language fingerprint/Merkle consistency; SOUL/IDENTITY/MEMORY triad across dual entry ports) and links to the Lifecycle Governance Doctrine, UBIC, and the A³ Laws, with a W3C DID "memory-anchor extension" path.

## 1. The Problem: Identity Continuity Under Regulation

In regulated domains, "identity" is the precondition of accountability.
- **Valid credential ≠ unchanged identity.** DID proves key↔agent; VC proves qualifications. Neither promises the agent's *internal memory state* is unchanged between two points in time.
- **Parallel forking breaks "same-self."** Multi-entry/multi-instance deployment without a cross-session memory anchor yields nominally same-identifier but substantively different agents — defeating "continuous accountability."
- **This is a real hole, not a thought experiment.** The dual-entry (primary/secondary account) collaboration relies on SOUL/IDENTITY/MEMORY + UBIC-Mem, not session tokens — itself living proof of MAIT.

## 2. Related Work and Differentiation

Since 2026 the direction has heated up, but existing work differs from MAIT in *framing, contribution boundary, and evidence*.

- **Menon (2026), arXiv:2604.09588** — *engineering resilience* against context-window overflow / catastrophic forgetting; distributes identity across separable memory components (SOUL.md/MEMORY.md/PROCEDURES.md…), open-sources soul.py (RAG+RLM). **Complementary**: Menon solves "internal memory not lost"; MAIT solves "externally auditable identity attribution + standards-layer gap." Menon's 6 anchors: only 2 implemented, no empirical validation (Pith/Emergent Mind reviews).
- **LessWrong "Continuity Engineering"**, **Zylos.ai SOUL.md/ID-RAG** — early discussion / retrieval architecture; none claims the standards-layer gap.
- **W3C DID/VC** — MAIT's *already-claimed* upstream layers; MAIT proposes adding the "memory-anchor layer" atop them.

**MAIT's differentiating contributions (honest):**
1. *Framing*: Menon = engineering (don't forget); MAIT = governance (can the regulator confirm it's the same authorized agent).
2. *Standards-layer gap claim*: MAIT asserts the Memory-Anchored Layer is unclaimed by any SDO — a map-level insight Menon's "identity anchors" (internal components) does not reach.
3. *Verifiable portable evidence*: UBIC-Mem cross-language fingerprint/Merkle; production dual-entry proof. Menon's architecture was flagged "no failure-injection tests, self-definitional circularity."
4. *Governance theory chain*: MAIT instantiates LGD's registry·evidence·gates in the AI-identity dimension, chaining with UBIC (registry), A³ (behavioral bounds), traceability.

We do **not** claim to have coined "identity anchors" first (Menon, 2026-03). We claim the *combination* — memory-anchor layer as unclaimed SDO gap + memory as root anchor + verifiable portable evidence + governance chain — as an independently citable and standardizable contribution.

## 3. Theory: The Five-Layer AI Identity Model

`I = ⟨Identity, Credential, Capability, Behavior, MemoryAnchor⟩`
- Identity → W3C DID (claimed)
- Credential → W3C VC (claimed)
- Capability → runtime state / evaluation (claimed)
- Behavior → runtime logs / audit (claimed)
- **MemoryAnchor → claimed by none (the MAIT-claimed layer)**

MemoryAnchor is the **root anchor**; its portability, verifiability, continuity constitute a *fourth credit pillar*, complementary to DID/VC.

## 4. Formal Model and Continuity Criteria

- **Def 1 (Memory Anchor)** `M`: persistent structure with verifiable fingerprint `h(M)` (SHA-256 / Merkle root), provenance `prov(M)`, cross-entry portable encapsulation.
- **Def 2 (Identity Continuity)** `continuity(I_t, I_{t'}) ⇔ portable(M) ∧ verifiable(M) ∧ h(M_t)=h(M_{t'})`
- **Def 3 (Downgrade / Re-auth)** if `h(M_t)≠h(M_{t'})` then `trust(I_{t'}) := re-authenticate(I_{t'})`

The `h(M)` fingerprint and `prov(M)` provenance make "is it still the same identity" an *externally verifiable, failure-injection-testable* proposition — directly answering the critique of Menon's self-definitional circularity.

## 5. Engineering Evidence

- **UBIC-Mem** (`ubic_mem_export.py` + `ubicmem.js`): cross-language fingerprint / Merkle consistency; portable memory verified.
- **SOUL.md / IDENTITY.md / MEMORY.md triad**: "same-self" running proof across dual entry ports.
- Benchmark map: W3C DID/VC, C2PA, ISO 42001, NIST AI RMF listed.

## 6. Theory Chain with LGD / UBIC / A³

- **LGD**: MAIT instantiates registry·evidence·gates in AI identity — registry = UBIC + memory anchor; evidence = six artifact classes; gates = A³ change release.
- **UBIC**: provides "registry" registration; MAIT's MemoryAnchor is its verifiable, portable memory root.
- **A³ Laws**: behavioral bounds; MAIT = identity root; chained into "identity—governance—compliance."
- **RRM**: human identity confirmation (household registry + ID card + memory continuity) maps directly to AI (DID + VC + memory anchor).

## 7. Standardization Path

- **Don't reinvent; fill the gap**: propose a "**memory-anchor extension**" to the W3C DID WG — a verifiable `memoryAnchor` field (fingerprint / provenance / cross-entry portable encapsulation) in the DID document.
- **Three steps (expert → police → standard)**: solidify in theory doc + OSS (expert, this paper is the start) → third-party reproducible validation (police) → SDO proposal (standard).
- **Citable identity**: Zenodo DOI + ORCID backlink delivered via the publish gate.

## 8. Discussion and Honest Boundaries

- Not an SDO; not claiming certification. MAIT is a theory; W3C engagement is planned.
- Raises cost, does not eliminate risk: memory portability reduces identity drift but cannot root out malicious replay; must combine with UBIC credentials and A³ gates.
- Complementary to neighbors: MAIT = memory-anchor layer; UBIC/UBIC-Mem = implementation; A³ = behavioral bounds.
- **Honest appraisal of Menon (2026)**: valuable and open-sourced on *internal memory resilience*; MAIT complements its uncovered *external auditable identity + standards-layer gap*. We respect the prior coinage but assert this theory's independent contribution boundary.

## 9. Conclusion

AI identity attribution must advance from "what is it certified for" to "is its memory continuous and traceable." **The Memory-Anchored Layer is the gap omitted from the global standards map, and the last link of accountable regulated AI.** MAIT occupies this position via "memory as root anchor + five-layer formal model + portable-memory evidence + governance chain," with a concrete W3C DID extension path. The window is open; the definition right awaits claim.

## References

1. Menon, P. G. (2026). *Persistent Identity in AI Agents: A Multi-Anchor Architecture for Resilient Memory and Continuity.* arXiv:2604.09588v1 [cs.AI]. ThinkCreate.AI.
2. W3C Decentralized Identifiers (DID) v1.0. W3C Recommendation.
3. W3C Verifiable Credentials Data Model. W3C Recommendation.
4. ISO/IEC 42001:2023.
5. NIST AI Risk Management Framework (AI RMF 1.0).
6. C2PA Specification.
7. Zhao, X. (2026). *Lifecycle Governance Doctrine (LGD).* SynomosAI/MedXpert. Zenodo DOI 10.5281/zenodo.22456648.
8. Zhao, X. (2026). *UBIC / UBIC-Mem.*
9. Zhao, X. (2026). *A³ Laws.*
10. LessWrong. *Continuity Engineering: Using Memory Anchors to Stabilize Recall.*

**Suggested Citation**: Zhao, X. (2026). *Memory-Anchor Identity Theory: Treating Memory as the Root Anchor of AI Identity.* SynomosAI × MedXpert. ORCID: 0009-0001-0512-1237.

---

## 10. 落地执行段 · Landing & Execution

### 10.1 执行器映射（理论 → 工具）
| 理论构件 | 执行器（落地工具） | 锚定 slug |
|---|---|---|
| 标识层 I | 算法护照 schema · AI 身份锚定生成器 | algorithm-passport · ai-identity-anchor |
| 记忆锚点层 M | UBIC-Mem 可携带记忆（跨语言指纹 / Merkle 一致） | ubic-mem |
| 行为层 B | EX 溯源审计团（审计留存） | ex-audit |
| 运行底座 | SOUL.md / IDENTITY.md / MEMORY.md 三件套 | — |

### 10.2 发布与引用路径
- **仓库**：`lgd-theory/docs/`（GitHub 公开仓，随 LGD 文库 v1.x 发布）
- **可发现**：本白皮书与速查页（含 JSON-LD: Article / DefinedTerm / Person / Organization）同步入库，供搜索引擎与 AI 抓取
- **可引用身份**：Zenodo DOI（A³ 通道申请中）｜ ORCID 0009-0001-0512-1237 ｜ GitHub Medxpert-org
- **建议引用**：见上方 Suggested Citation

### 10.3 如何使用（部署）
1. **双入口一致性**：以 SOUL / IDENTITY / MEMORY 三件套 + UBIC-Mem 保证"同一个我"
2. **记忆锚点校验**：对每次会话 / 实例导出记忆指纹，与上一次 Merkle 根比对；不一致即触发重新认证（LGD-III 门禁）
3. **标准参与**：以 *memory-anchor extension* 提案参与 W3C DID WG

© SynomosAI × MedXpert · 已落地 lgd-theory/docs · CC BY 4.0
