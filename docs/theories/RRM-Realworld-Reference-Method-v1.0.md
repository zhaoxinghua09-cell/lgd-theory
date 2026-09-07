# 真实世界参照法 · Real-world Reference Method (RRM)
## 白皮书 v1.0 · 2026-09-08

> **TID**：TH-META-001 ｜ **域码**：META ｜ **母版**：第一性原理 / 真实世界成熟机制
> **角色**：元方法（meta-method）—— 全部工具与方法论的"方法生成器"
> **下游锚定**：TH-META-006(LGD 全程治理论) · TH-AIG-006(MAIT 记忆锚点=AI 身份) · TH-AIG-001(UBIC 人格户籍协议) · TH-LAW-001(电子证据链) 等
> **提出 / 品牌**：SynomosAI（治理侧）× MedXpert（实证侧）
> **作者署名**：赵兴华 / Steven Zhao·China（ORCID 0009-0001-0512-1237 ｜ GitHub Medxpert-org · medxpert.cn）
> **版本**：v1.0 ｜ **状态**：🟢 已落地 lgd-theory/docs（DOI 申请中 · 7 维质检已过）
> **官方主页**：https://medxpert.cn ｜ **仓库**：github.com/Medxpert-org/lgd-theory

---

### 摘要（中文）

AI 行业普遍存在一种隐性"原创幻觉"——把**没有真实世界参照的纯生成式方案**当成创新，导致 AI 身份证凭空造、治理框架凭空贴、合规判定凭空答，一落到受监管场景（医疗、金融、身份）就崩。真正的缺口不在"能不能生成"，而在"**生成的东西能不能锚回真实世界的成熟机制**"。

而"如何为 AI 方案寻找真实世界参照"这件事本身，至今**没有任何人把它立成一个可引用的元方法**——行业都在做领域件，少有人定义"造领域件的方法"。本文提出 **真实世界参照法（Real-world Reference Method, RRM）**：把"为每一个 AI 能力缺口 G，找到真实世界的成熟机制 M 并同构映射 S ≅ M"确立为**可引用、可审计、可复现的元方法**，并给出**先验可疑原则**（任何找不到真实世界参照的 AI 方案，默认视为未验证，须显式标注"无参照"）。RRM 已连续 6 次实例化（MAIT / SIDE / AFG / UBIC-Mem / BTSK / LDGF），每次都是"痛点 × 真实机制"的兑现，构成"理论之理论"的顶层站位。

RRM 与通用的 **RWS/RWE（真实世界研究 / 真实世界证据）** 有明确边界：RWS/RWE 是循证医学的*证据*方法论（用真实数据产生证据）；RRM 是治理*设计*的方法论（用真实机制做治理骨架）。RRM 把"参照真实世界"从证据层面提升到了方法层面，是一切下游理论（LGD、MAIT、UBIC…）的"方法生成器"。

### Abstract (English)

The AI industry suffers a hidden "originality illusion": treating *generative solutions with no real-world reference* as innovation — fabricating AI identities, governance frameworks, and compliance verdicts from scratch, which collapse the moment they hit regulated domains (healthcare, finance, identity). The real gap is not "can it generate," but "**can what it generates be anchored back to a proven real-world mechanism**."

Yet "how to find a real-world reference for an AI solution" has, to date, **never been established as a citable meta-method** — the field builds domain artifacts but seldom defines *the method for building them*. This paper proposes the **Real-world Reference Method (RRM)**: making "for every AI capability gap G, find a proven real-world mechanism M and structurally map solution S ≅ M" a *citable, auditable, reproducible meta-method*, with a **prior-suspicion principle** (any AI solution lacking a real-world reference defaults to unverified and must be explicitly labeled "no-reference"). RRM has been instantiated six consecutive times (MAIT / SIDE / AFG / UBIC-Mem / BTSK / LDGF), each fulfilling "pain point × real mechanism," forming a top-layer position as "a theory of theories."

RRM is clearly bounded against generic **RWS/RWE (Real-World Study / Real-World Evidence)**: RWS/RWE is an *evidence* methodology of evidence-based medicine (producing evidence from real data); RRM is a governance-*design* methodology (using real mechanisms as governance scaffolding). RRM elevates "referencing the real world" from the evidence layer to the method layer, serving as the "method generator" for all downstream theories (LGD, MAIT, UBIC…).

**Keywords**: meta-method · real-world reference · governance design · AI governance · structural isomorphism · prior-suspicion principle · LGD · lifecycle governance

---

## 0. 问题：AI 的"原创幻觉"与"造方法的方法"空白

在医疗器械、金融、身份等受监管领域，一个被反复撞到的洞是：**AI 方案缺乏对真实世界机制的锚定**。

- **凭证有效 ≠ 方案可信**。一个 AI 合规判定若凭空给出"符合某法规"的结论，即便输出格式严谨，其推理链条也无真实制度母版可依——监管者无法审计"它凭什么这么说"。
- **原创幻觉**。行业习惯把"没有真实世界参照的纯生成式方案"包装成创新。AI 身份证凭空造、AI 治理框架凭空贴、合规判定凭空答，落到受监管场景即崩。
- **"造方法的方法"无人认领**。大家都在做领域件（ID、凭证、KYC、认证、追责、定标…），却没人把"**如何为 AI 方案寻找真实世界参照**"立成一个可引用的元方法。这正是顶层站位（理论之理论）的空白。

> **关键判据**：把"AI 方案须同构真实世界成熟机制"主张为一个*可引用的元方法*，且具有"先验可疑原则"这一可操作红线的，全球范围内极少。这是 RRM 独占性最高的站位。

## 1. 相关工作与差异化定位

RRM 不是凭空而来，但与下列相邻工作在**问题框架、贡献边界、可操作用度**上均不同。

| 工作 | 问题框架 | 核心主张 | 与 RRM 的关系 |
|---|---|---|---|
| **RWS/RWE**（NMPA/CMDE/FDA/EMA/乐城真实世界数据指南） | 循证医学证据 | 用真实诊疗数据产生证据 | **边界清晰**：RWS/RWE 是*证据*方法论；RRM 是*治理设计*方法论。RRM 把"参照真实世界"从证据层升到方法层 |
| **Design Patterns**（Gamma et al., 1994, GoF） | 软件工程结构复用 | 抽象可复用的软件结构模式 | **互补**。GoF 抽象的是*软件结构*；RRM 平移的是*真实世界制度机制*为治理骨架，且带"先验可疑"红线 |
| **Analogy / Case-based Reasoning**（认知科学） | 类比迁移 | 用旧案例解新问题 | 同主题早期思想；RRM 将其工程化为"母版映射 + 国际视角优先 + 无参照即未验证"的治理约束 |
| **First-Principles Thinking**（Musk 等） | 通用思维方法 | 从基本事实推演 | 通用思维法；RRM 增加"真实世界成熟机制优先 + 可溯源 + 可审计"的治理硬约束 |
| **监管沙盒 / 适应性治理**（OECD/IMF 等） | 政策试验 | 在受控环境试错 | 政策层实践；RRM 是更具操作性的"单个方案如何找母版"的方法生成器 |

**RRM 的差异化贡献（诚实表述）**：

1. **问题框架差异**：行业谈"具体的 AI 框架"，RRM 谈"**造框架的方法**"——它是元层（meta-layer）站位，生成而非竞争于领域件。
2. **先验可疑原则（独有可操作红线）**：任何找不到真实世界参照的 AI 方案，默认视为未验证，须显式标注"无参照"。这不是泛泛的"要谨慎"，而是可写进发布闸门的硬性判据。
3. **国际视角优先 + 先对标再自建**：参照优先取自 ISO/W3C/EU/WHO/NIST 现行标准；元原则"不满足于用标准，要立自己的标准"——但**先对标、再自建**。
4. **实例化即理论 + 6 次实证**：每一个具体领域件都是 RRM 的一次实例化；RRM 不解决具体问题，它**生成并统摄**所有领域件。已连续 6 次复用验证，独占性来自复用频次与可引用性。

> 我们不主张"率先提出类比/参照思维"。认知科学与软件工程早有类比推理与设计模式。我们主张的是：**以"AI 治理方案须同构真实世界成熟机制 + 先验可疑原则 + 国际视角优先 + 6 次实例化实证"这一组合**，构成可独立署名与标准化的*元方法*贡献。

## 2. 理论：映射公理与形式化

**命名**：真实世界参照法 / RRM（Real-world Reference Method）。

**正式表述（映射公理）**：
> 对任意 AI 能力缺口 G，存在真实世界的成熟机制 M 与之**结构同构**；我们给出的方案 S 应满足 **S ≅ M**。
> 且 M 的优先序为：
> ① 已查证国际现行标准/制度 ＞ ② 成熟社会机制（如公证、KYC、户籍）＞ ③ 自创机制（仅当前两者均不存在时）。

**先验可疑原则（Prior-Suspicion Principle）**：
> 若对能力缺口 G 无法找到真实世界参照 M，则方案 S 默认标记为 **"无参照·未验证"**，不得对外作为已验证理论发布。

**国际视角优先**：
> 参照应优先取自 ISO / W3C / EU / WHO / NIST 等现行标准；"不满足于用标准，要立自己的标准"——但**先对标、再自建**。

**实例化即理论**：
> 每一个具体领域件（身份证、凭证、KYC、认证、追责、定标……）都是 RRM 的一次实例化；RRM 不解决具体问题，它**生成并统摄**所有领域件。

**原始映射表（已固化）**：

| AI 痛点 G | 真实世界参照 M | 我们的方案 S ≅ M |
|---|---|---|
| AI 没有身份证 | 身份证 / 户籍 | AI 身份证（三锚一票） |
| 凭证不可信 | 公证处 | 可验证凭证（VC） |
| 对方靠不靠谱 | 银行 KYC | AI KYC 尽调 |
| 谁来认证 | UL / CE 认证 | AI 溯源认证 |
| 出事了追责 | 警察 + 审计 | 溯源审计报告 |
| 标准谁定 | ISO | 参与定标 |

## 3. 形式化模型与判据

**定义 1（真实世界参照）**。对 AI 能力缺口 G，一个真实世界参照 M 是一个已查证、可溯源的成熟机制（国际标准 / 制度 / 社会机制），满足 provenance(M) 可指回权威真源。

**定义 2（结构同构映射）**。方案 S 与参照 M **结构同构** ⇔ `S ≅ M`，即 S 在"标识—凭证—行为—审计—门禁"等关键维度上保持与 M 同构的治理骨架。

**定义 3（先验可疑算子）**。设 `ref(G)` 为"为 G 找到的参照集合"，
```
verified(S) ⇔ (ref(G) ≠ ∅) ∧ (S ≅ M_for_G) ∧ (provenance(M_for_G) 可溯源)
unverified(S) := (ref(G) = ∅) → label(S, "无参照·未验证")
```
即：有参照且同构且可溯源 ⟺ 可视为已验证；无参照 ⟹ 强制标注"无参照·未验证"。

**判据（对照行业痛点）**：上述 `provenance(M)` 谱系使"这个 AI 方案有没有真实依据"成为**可外部审计**的命题——直接回答"凭空造框架"的原创幻觉。RRM 的红线（无参照即未验证）使发布闸门具备可执行的去伪判据。

## 4. 工程实证（6 次实例化）

RRM 不是空想——它已被连续 6 次实例化，每一次都是"痛点 × 真实机制"的兑现：

| 领域件（已落） | 痛点 G | 真实机制 M | 同构方案 S |
|---|---|---|---|
| **MAIT 记忆锚点=AI 身份**（TH-AIG-006） | AI 无持久身份 | 户籍/身份证绑"记忆" | 可验证记忆为根锚（W3C DID 未认领空白） |
| **SIDE 微信即本机密钥**（TH-AIG-xx） | 身份缺本地凭证 | 钥匙/口令本地持有 | openid 经 HKDF→Fernet，"身份即密钥" |
| **AFG 抗编造护栏**（TH-LAW-xx） | AI 编造合规结论 | 医疗器械可追溯证据链 | 七环证据链＋三层防伪（不编造/可重放/可追责） |
| **UBIC-Mem 记忆可携带**（治理线） | 记忆无载体 | 护照/签证可携带 | 四层记忆＋SHA-256 指纹＋跨语言一致 |
| **BTSK 双时态知识库**（TH-xx） | 知识不进化 | 法规版本+实例时态 | 双时间轴＋内外双循环＋双机同步 |
| **LDGF 决策治理框架**（TH-xx） | 治理缺框架 | Cynefin/OODA/Wardley/RMF | 四维正交函数＋OODA 闭环 |

**支撑性真源**：
- 已查证的**国际标准地图**（W3C DID/VC、C2PA、ISO 42001、MCP-I/TRAIL、NIST 800-63、EU AI Act / NIST AI RMF、FDA SaMD / MDR / NMPA）：为"国际视角优先"提供对标清单。
- 方法论总纲：RRM 是"AI 世界理论体系"方法学卷的基座，天然串起上方六件——**一篇顶六篇**。

**关键判据**：RRM 的独占性来自——① 内部 6 次复用验证；② 全球无人把"AI 方案须同构真实机制"立为**可引用的元方法**（行业多在谈具体框架，少谈"造框架的方法"）。

## 5. 与 LGD / MAIT / UBIC / A³ 的理论链

RRM 是"方法的方法"，位于治理理论矩阵的元层，向下生成各理论：

```
RRM（元方法 / 第一性原理 / 方法生成器）
 ├─ 母版：医械全生命周期监管（NMPA/FDA/MDR） → 抽象 → LGD 三律（有籍·有证·有门禁）
 ├─ 母版：人类身份确认（户籍+身份证+记忆连续性） → 抽象 → 标识+凭证+记忆锚点 → MAIT
 ├─ 母版：户籍/护照登记制度 → 抽象 → UBIC 人格户籍协议
 ├─ 母版：证据法/公证/电子存证 → 抽象 → AFG 抗编造护栏 / 电子证据链
 └─ 母版：决策科学（Cynefin/OODA/Wardley/RMF） → 抽象 → LDGF 决策治理框架
```

- **LGD 全程治理论（TH-META-006）**：RRM 的"医械全生命周期监管"母版抽象出的"有籍·有证·有门禁"三律，是 LGD 的直接来源。
- **MAIT 记忆锚点=AI 身份（TH-AIG-006）**：RRM 的"人类身份确认"母版（户籍+身份证+记忆连续性）映射为 AI 的"DID+VC+记忆锚点"。
- **UBIC 人格户籍协议（TH-AIG-001）**：RRM 的"户籍/护照"母版映射为 AI 身份登记与可携带证明。
- **A³ 造 AI 三定律（TH-AIG-003）**：RRM 提供方法骨架，A³ 提供行为边界；二者串成"身份—治理—合规"链。

## 6. 占位与标准化路径

- **首发（顶六篇）**：作为 SynomosAI 方法论总纲 / 《AI 世界理论体系》方法学卷的基座对外发布——它天然串起 MAIT/SIDE/AFG/UBIC-Mem/BTSK/LDGF 六件，一篇顶六篇。
- **第三方引用**：随 A³ Laws + XCGS + LDGF 治理方法论三件套一并对外；通过开源社区与公开竞赛获取第三方引用，长期瞄准 ISO/W3C 标准参与（元原则"不满足于用标准，要立自己的标准"）。
- **不另起炉灶，补其空白**：RWS/RWE 已占"证据"位；RRM 占"方法"位，二者互补。主张在治理论述中明确"参照层"作为独立于"证据层"的方法论构件。
- **可引用身份**：本文建议引用格式见 §8；配套 Zenodo DOI 与 ORCID 回链随发布闸门一并落地。

## 7. 讨论与诚实边界

- **元方法 ≠ 领域真理**：RRM 只规定"怎么找参照"，不保证"找到的参照一定最优"；参照错，方案错。发布时须保留此边界。
- **非法规 / 非认证**：对标的 ISO/W3C 等标准，仅作"结构对齐 / 借鉴"参考，未过第三方审计不称"符合认证"。
- **与邻近站位互补**：RRM 是"造方法的方法"（顶层）；A³ Laws 是行为边界、LDGF 是治理骨架、MAIT 是身份根锚——RRM 生成它们，不与它们竞争。
- **盲区**：RRM 对"真实世界尚无对应机制的纯前沿问题"（如 AGI 自我意识）暂时无参照可依，须显式标注"无参照域"，交由后续自建标准补足。
- **对 RWS/RWE 的诚实评价**：循证医学的 RWS/RWE 在*证据产生*上成熟且必要；RRM 在*治理设计的方法生成*上补其未覆盖处，二者互补而非竞争。我们尊重既有术语，但主张本理论的独立贡献边界（方法层 vs 证据层）。

## 8. 结论

AI 治理的缺口，不在"能不能生成"，而在"生成物能否锚回真实世界的成熟机制"。**真实世界参照法（RRM）把"为 AI 方案寻找真实世界参照"从隐式直觉提升为可引用、可审计、可复现的元方法，并以"先验可疑原则"给出可执行的去伪红线。** RRM 以"映射公理 + 6 次实例化实证 + 治理理论链"占据这一顶层站位，并给出可落地的占位与标准化路径。窗口已开，定义权待认领。

## 参考文献

1. NMPA / CMDE. 真实世界数据用于医疗器械临床评价技术指导原则. (中国)
2. 海南省药品监督管理局. 乐城先行区临床真实世界数据用于支持进口药械注册申报工作指南（试行）. 2026-04-29.
3. FDA. Real-World Evidence Program / 21st Century Cures. (US)
4. EMA. Framework for the Use of Real-World Data in EU Medicines Regulation. (EU)
5. Gamma, E., Helm, R., Johnson, R., Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software.* Addison-Wesley.
6. Kolodner, J. (1993). *Case-Based Reasoning.* Morgan Kaufmann.
7. OECD. *AI Principles / Adaptive Policy.* (政策试验参考)
8. ISO/IEC 42001:2023 — AI Management System.
9. W3C Decentralized Identifiers (DID) v1.0 / Verifiable Credentials Data Model. W3C Recommendation.
10. Zhao, X. (2026). *Lifecycle Governance Doctrine (LGD).* SynomosAI / MedXpert. Zenodo DOI 10.5281/zenodo.22456648.
11. Zhao, X. (2026). *Memory-Anchor Identity Theory (MAIT).* SynomosAI × MedXpert.
12. Zhao, X. (2026). *UBIC 人格户籍协议 / UBIC-Mem 记忆可携带律.* SynomosAI.
13. Zhao, X. (2026). *A³ Laws 造 AI 三定律.* SynomosAI.

---

### 建议引用格式（Suggested Citation）

> Zhao, X. (2026). *Real-world Reference Method (RRM): A Meta-Method for Grounding AI Solutions in Proven Real-World Mechanisms.* SynomosAI × MedXpert. ORCID: 0009-0001-0512-1237. https://medxpert.cn

---

© SynomosAI × MedXpert · 内部白皮书草稿（待去敏 + 7 维质检后随 lgd-theory 发布）

---

# Real-world Reference Method (RRM) — Full English Version

**White Paper v1.0 · 2026-09-08**
TID: TH-META-001 · Domain: META · Role: meta-method (method generator)
Upstream: none (first principle) · Downstream: LGD (TH-META-006), MAIT (TH-AIG-006), UBIC (TH-AIG-001), AFG/LDGF/BTSK
Author: Zhao Xinghua / Steven Zhao·China (ORCID 0009-0001-0512-1237 · GitHub Medxpert-org · medxpert.cn)
Brand: SynomosAI (theory) × MedXpert (evidence)

## Abstract

The AI industry suffers a hidden "originality illusion": treating generative solutions with no real-world reference as innovation. The real gap is not "can it generate," but "can what it generates be anchored back to a proven real-world mechanism." Yet "how to find a real-world reference for an AI solution" has never been established as a citable meta-method. We propose the **Real-world Reference Method (RRM)**: making "for every AI capability gap G, find a proven real-world mechanism M and structurally map S ≅ M" a citable, auditable, reproducible meta-method, with a **prior-suspicion principle** (any AI solution lacking a real-world reference defaults to unverified). RRM has been instantiated six consecutive times (MAIT / SIDE / AFG / UBIC-Mem / BTSK / LDGF), forming a top-layer position as "a theory of theories." RRM is clearly bounded against RWS/RWE: the latter is an *evidence* methodology of medicine; RRM is a governance-*design* methodology — elevating "referencing the real world" from the evidence layer to the method layer.

## 1. The Problem: Originality Illusion and the Gap of "Method for Methods"

In regulated domains, a repeatedly hit hole is the *lack of anchoring to real-world mechanisms*.
- **Valid output ≠ trustworthy solution.** An AI compliance verdict stated from scratch, however well-formatted, has no real institutional archetype behind its reasoning — the regulator cannot audit "why it says so."
- **Originality illusion.** The industry packages "generative solutions with no real-world reference" as innovation.
- **"Method for methods" unclaimed.** Everyone builds domain artifacts; few define *the method for building them*. This is the top-layer (theory-of-theories) gap.

## 2. Related Work and Differentiation

- **RWS/RWE** (NMPA/FDA/EMA/Lecheng RWD guidelines): *evidence* methodology; RRM is *governance-design* methodology — clear boundary, complementary.
- **Design Patterns** (GoF, 1994): abstracts *software structure*; RRM translates *real-world institutional mechanisms* into governance scaffolding, with a prior-suspicion red line.
- **Analogy / Case-based Reasoning**: early thought; RRM engineers it into "archetype mapping + international-priority + no-reference-unverified" governance constraints.
- **First-Principles Thinking**: generic; RRM adds "real-mechanism priority + traceability + auditability" hard constraints.
- **Regulatory sandbox / adaptive governance** (OECD/IMF): policy-layer practice; RRM is the more operational "how a single solution finds its archetype" generator.

**RRM's differentiating contributions (honest):**
1. *Framing*: industry talks frameworks; RRM talks *the method for building frameworks* (meta-layer).
2. *Prior-Suspicion Principle (unique operable red line)*: no reference ⇒ unverified, must be labeled. A hard criterion writable into a publish gate.
3. *International-priority + benchmark-then-build*: reference from ISO/W3C/EU/WHO/NIST first; "don't settle for using standards, set your own" — but *benchmark first, then build*.
4. *Instantiation-is-theory + 6 empirical cases*: RRM generates, not competes with, domain artifacts; validated six consecutive times.

We do **not** claim to have coined analogy/reference thinking. We claim the *combination* — AI governance solutions must structurally map to proven real-world mechanisms + prior-suspicion principle + international priority + six-case evidence — as an independently citable and standardizable *meta-method* contribution.

## 3. Theory: Mapping Axiom and Formalization

**Naming**: Real-world Reference Method / RRM.

**Mapping Axiom**: For any AI capability gap G, there exists a proven real-world mechanism M structurally isomorphic to it; our solution S should satisfy **S ≅ M**. Priority of M: ① verified international standard/institution ＞ ② mature social mechanism (notary, KYC, household registry) ＞ ③ self-created mechanism (only when both former are absent).

**Prior-Suspicion Principle**: If no real-world reference M can be found for G, solution S defaults to labeled **"no-reference · unverified"** and must not be published as verified theory.

**International-priority**: Reference preferentially from ISO/W3C/EU/WHO/NIST; benchmark first, then build.

**Instantiation-is-theory**: Each domain artifact is one instantiation of RRM; RRM generates and governs all of them.

## 4. Formal Model and Criteria

- **Def 1 (Real-world Reference)** `M`: a verified, traceable mature mechanism (international standard / institution / social mechanism) with `provenance(M)` pointing to an authoritative source.
- **Def 2 (Structural Isomorphism)** `S ≅ M`: S preserves the governance skeleton (identity—credential—behavior—audit—gate) isomorphic to M.
- **Def 3 (Prior-Suspicion Operator)**:
  `verified(S) ⇔ (ref(G) ≠ ∅) ∧ (S ≅ M_for_G) ∧ (provenance(M_for_G) traceable)`
  `unverified(S) := (ref(G) = ∅) → label(S, "no-reference · unverified")`

The `provenance(M)` provenance makes "does this AI solution have a real basis" an *externally auditable* proposition — directly answering the originality-illusion hole.

## 5. Engineering Evidence (6 Instantiations)

RRM instantiated six consecutive times:

| Artifact | Gap G | Mechanism M | Solution S |
|---|---|---|---|
| MAIT (TH-AIG-006) | no durable AI identity | household registry + ID card + memory | verifiable memory as root anchor (W3C DID unclaimed gap) |
| SIDE | no local credential | key/password held locally | openid → HKDF → Fernet, "identity is key" |
| AFG | AI fabricates compliance | med-device traceable evidence chain | 7-ring evidence + 3-layer anti-fabrication |
| UBIC-Mem | no memory carrier | passport/visa portability | 4-layer memory + SHA-256 fingerprint + cross-language consistency |
| BTSK | knowledge not evolving | regulation versioning + instance temporality | dual timeline + dual-loop + dual-machine sync |
| LDGF | no governance framework | Cynefin/OODA/Wardley/RMF | 4-D orthogonal function + OODA loop |

Benchmark map (W3C DID/VC, C2PA, ISO 42001, NIST 800-63, EU AI Act / NIST AI RMF, FDA SaMD / MDR / NMPA) backs the "international-priority" claim.

## 6. Theory Chain with LGD / MAIT / UBIC / A³

RRM is the "method of methods" at the meta-layer, generating downstream theories:
- **LGD** ← archetype: medical-device lifecycle regulation → "registry · evidence · gates."
- **MAIT** ← archetype: human identity confirmation (registry + ID + memory continuity) → DID + VC + memory anchor.
- **UBIC** ← archetype: household/passport registry → AI identity registration + portable proof.
- **AFG / evidence chain** ← archetype: evidence law / notary / e-storage.
- **LDGF** ← archetype: decision science (Cynefin/OODA/Wardley/RMF).

## 7. Occupation and Standardization Path

- **First release (six-in-one)**: as the基座 of the SynomosAI methodology compendium / AI-world theory-system methods volume — naturally chaining the six artifacts above.
- **Third-party citation**: with A³ Laws + XCGS + LDGF governance trio; via OSS community and open competitions; long-term ISO/W3C engagement.
- **Don't reinvent; fill the gap**: RWS/RWE owns the "evidence" slot; RRM owns the "method" slot — complementary. Assert the "reference layer" as a methodology component independent of the "evidence layer."
- **Citable identity**: Zenodo DOI + ORCID backlink delivered via the publish gate.

## 8. Discussion and Honest Boundaries

- Meta-method ≠ domain truth: RRM prescribes *how to find references*, not that the found reference is optimal.
- Not regulation / not certification: benchmarked standards are "structural alignment / reference," not "compliant" without third-party audit.
- Complementary to neighbors: RRM = method generator (top); A³ = behavioral bounds; LDGF = governance skeleton; MAIT = identity root.
- Blind spot: pure-frontier problems with no real-world counterpart (e.g., AGI self-awareness) must be explicitly labeled "no-reference domain."
- **Honest appraisal of RWS/RWE**: mature and necessary for *evidence generation*; RRM complements its uncovered *governance-design method generation*. We respect the existing term but assert this theory's independent contribution boundary (method layer vs evidence layer).

## 9. Conclusion

The gap in AI governance is not "can it generate," but "can its output anchor back to a proven real-world mechanism." **The Real-world Reference Method (RRM) elevates 'finding a real-world reference for AI solutions' from implicit intuition to a citable, auditable, reproducible meta-method, with a prior-suspicion principle as an operable de-fabrication red line.** RRM occupies this top-layer position via "mapping axiom + six-case evidence + governance chain," with a concrete occupation and standardization path. The window is open; the definition right awaits claim.

## References

1. NMPA/CMDE. Real-World Data for Medical Device Clinical Evaluation Technical Guidance. (China)
2. Hainan NMPA. Lecheng RWD for Imported Device Registration Guidelines (Trial). 2026-04-29.
3. FDA. Real-World Evidence Program / 21st Century Cures. (US)
4. EMA. Framework for the Use of Real-World Data in EU Medicines Regulation. (EU)
5. Gamma, E., et al. (1994). *Design Patterns.* Addison-Wesley.
6. Kolodner, J. (1993). *Case-Based Reasoning.* Morgan Kaufmann.
7. OECD. AI Principles / Adaptive Policy.
8. ISO/IEC 42001:2023.
9. W3C DID v1.0 / VC Data Model. W3C Recommendation.
10. Zhao, X. (2026). *Lifecycle Governance Doctrine (LGD).* SynomosAI/MedXpert. Zenodo DOI 10.5281/zenodo.22456648.
11. Zhao, X. (2026). *Memory-Anchor Identity Theory (MAIT).* SynomosAI × MedXpert.
12. Zhao, X. (2026). *UBIC / UBIC-Mem.* SynomosAI.
13. Zhao, X. (2026). *A³ Laws.* SynomosAI.

**Suggested Citation**: Zhao, X. (2026). *Real-world Reference Method (RRM): A Meta-Method for Grounding AI Solutions in Proven Real-World Mechanisms.* SynomosAI × MedXpert. ORCID: 0009-0001-0512-1237.

---

## 10. 落地执行段 · Landing & Execution

### 10.1 执行器映射（理论 → 工具）
| 理论构件 | 执行器（落地工具） | 锚定 slug |
|---|---|---|
| 映射公理 S ≅ M | 方法生成器（全部工具的"方法层"） | method-generator |
| 先验可疑原则 | 参照校验台（标注"无参照·未验证"） | reference-validator |
| 论证结构化 | RRM 论证教练器 | rrm-coach |
| 实证底座 | 6 次实例化（MAIT / SIDE / AFG / UBIC-Mem / BTSK / LDGF） | — |

### 10.2 发布与引用路径
- **仓库**：`lgd-theory/docs/`（随 LGD 文库 v1.x 发布）
- **可发现**：白皮书 + 速查页（含 JSON-LD）同步入库，供搜索引擎与 AI 抓取
- **可引用身份**：Zenodo DOI（A³ 通道申请中）｜ ORCID 0009-0001-0512-1237 ｜ GitHub Medxpert-org
- **建议引用**：见上方 Suggested Citation

### 10.3 如何使用
1. 对任何 AI 能力缺口 G，先用 **RRM 论证教练器**检索真实世界成熟机制 M
2. 找不到 M → 强制标注"无参照·未验证"（去伪红线，可写入发布闸门）
3. 找到 M → 用 **方法生成器**做同构映射 S ≅ M，产出领域件

© SynomosAI × MedXpert · 已落地 lgd-theory/docs · CC BY 4.0
