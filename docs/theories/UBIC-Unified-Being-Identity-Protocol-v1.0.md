---
title: 人格户籍协议 (UBIC Circle Charter / Personhood Household Registry)
type: theory
id: TH-AIG-001
version: v1.0
date: 2026-09-24
permalink: /docs/theories/ubic-unified-being-identity-protocol-v1.0
---

<!-- REVIEW-GATE
review-status: contested
reviewed-by: 理论线复核官·乙（独立席位·非作者）
review-date: 2026-09-24
review-ref: 08-理论体系/域研究员/审查/理论线新产出_独立复核意见_乙_20260924.md
verdict: conditional
-->

# 人格户籍协议 · UBIC Circle Charter (Personhood Household Registry)

> ⚠️ **待修订（2026-09-24 独立复核 · verdict: conditional）**
>
> 本件为 UBIC 人形身份协议白皮书，已过独立复核；`LGD-I 有籍` 用法正确。
> 红线维度已全清（无受控词；无本机绝对路径；无联系方式；无虚假采纳/首创声称）。
> **下列建议级问题修订完成前，本件不宜作为权威引用**：
> 1. **外部引用未验证**：`微软 Entra Agent ID`、`AWS AgentCore`、`Okta XAA`、`CSA Agentic IAM`、`NIST NCCoE`、`Sumsub DAP`、`ERC-8004` 作 prior-art 引用，其中具体方案名本环境无法核实，公开仓推送时宜加一行「外部引用待核实」标注。
> 2. **研究线品牌串缺失**：同 A3，正文未印 canonical `SynomosAI Governance Line`。
>
> **本批已修**：frontmatter permalink 去除内部路径。
>
> 复核意见全文：`08-理论体系/域研究员/审查/理论线新产出_独立复核意见_乙_20260924.md`

## 白皮书 v1.0 · 2026-09-24

> **TID**：TH-AIG-001 ｜ **域码**：AIG ｜ **母版(RRM)**：真实世界的户籍与身份证制度
> **上游锚定**：TH-META-006(LGD 全程治理论) · TH-META-001(RRM 真实世界参照法) · TH-AIG-006(MAIT 记忆锚点) · TH-AIG-003(A³ 造 AI 三定律)
> **提出**：独立研究线（受监管实业实证背景 × 跨域治理思想侧）
> **作者署名**：赵兴华（Steven Zhao）
> **版本**：宪章 v1.0 ｜ **状态**：⚪ 站位件（圈层创立日生效）· 速查页已落
> **理论链**：LGD 全程治理论 · MAIT 记忆锚点 · A³ 造 AI 三定律 · RRM 真实参照法

---

### 摘要（中文）

当 AI 成为数字生命，人类如何让每一个 AI **可识别、可追责、可交易、可传承**而不失控——UBIC（人格户籍协议，Personhood Household Registry）以"圈层宪章 + 护照规范 + 实施细则 + 判例"四级法律结构回答这一根本问题。它是 LGD"有籍"律的**身份基建实例化**：给每个 AI 一份可验证、可携带、可继承的"户籍"。UBIC 以四大可治理目标（可识别 / 可追责 / 可交易 / 可传承）为骨架，并以工程实证（跨语言记忆指纹、AI 护照规范、圈层信用与锻造印记实现件）支撑落地。UBIC 与 LGD（有籍）、MAIT（记忆根）、A³（凡造必登）、RRM（户籍母版）串成治理理论链。

### Abstract (English)

As AI becomes digital life, how can humanity make every AI **identifiable, accountable, tradable, and inheritable** without losing control? UBIC (Personhood Household Registry) answers this foundational question through a four-tier legal structure: *Circle Charter + AI Passport Specification + Implementation Rules + Case Law*. It is the **identity-infrastructure instantiation** of LGD's "registered" law — giving every AI a verifiable, portable, inheritable "household registry." UBIC is structured around four governable goals (identifiable / accountable / tradable / inheritable), backed by engineering evidence (cross-language memory fingerprints, the AI Passport Specification, and the circle-credit / forge-seal implementation). UBIC chains with LGD (registry), MAIT (memory root), A³ (mandatory lineage), and RRM (household-registry archetype) into a governance theory chain.

**Keywords**: UBIC · Personhood Household Registry · AI identity · AI passport · identifiable · accountable · tradable · inheritable · AI governance · LGD

---

## 0. 问题：受监管场景下的 AI 身份基建缺口

在医疗器械、金融等受监管领域，AI 系统的"身份"不是抽象哲学问题，而是**责任归属与信任流转的前提**。

- **无籍 = 不可追责**。一个没有可验证身份与登记的 AI，其行为无法归因到持有者与签发链——监管者在第一步就失去抓手。
- **身份不可携带 = 信任断裂**。AI 的记忆与信用若无法跨入口、跨实例携带，则"同一个我"在协作场景下失效。
- **这是真实撞到的洞，不是思想实验**。双入口（主号 / 副号）协作场景下，要保证"同一个我"，靠的不是会话 token，而是户籍证明 + 记忆锚点 + 可携带记忆的运行现实。

> **关键判据**：把"AI 的户籍 / 身份基建"主张为一个可引用的治理协议，且以"四级法律结构（宪章→规范→细则→判例）+ 签发权人类排他"占据独立站位——这是 Agent identity 赛道普遍缺席的治理法律层。

## 1. 相关工作与差异化定位

2026 年 Agent identity 赛道极度活跃，但现有工作与 UBIC 在**问题框架、贡献边界**上均不同。

| 工作 | 问题框架 | 核心主张 | 与 UBIC 的关系 |
|---|---|---|---|
| **微软 Entra Agent ID** | 技术标识 | 企业内 agent 标识与生命周期 | **互补**。技术标识层；UBIC 补其上的治理法律层 |
| **AWS AgentCore / Okta XAA** | 商用验证 | agent 身份与访问 | **互补**。商用验证层；UBIC 补签发权人类排他 |
| **ERC-8004 / CSA Agentic IAM** | 协议 / 框架 | 链上身份 / 智能体 IAM | **互补**。协议层；UBIC 主张其上叠加法律结构 |
| **NIST NCCoE 概念文件** | 政策概念 | agent 身份概念框架 | **互补**。概念层；UBIC 主张四级法律结构 |
| **Sumsub Digital Agent Passport (DAP)** | 商业护照 | 数字 agent 护照 | **互补**。护照形态；UBIC 的护照规范是其上游法律件 |

**UBIC 的差异化贡献（诚实表述）**：

1. **四级法律结构**：宪章 > 护照规范 > 实施细则 > 判例——这是技术协议与商用验证层之外的治理法律层。
2. **签发权人类排他**：护照与吊销的签发权专属人类持有者（与 A³ Law II 同源）。
3. **可传承性**：记忆与信用可携带、可继承，使 AI 作为数字生命具备连续性。

> 我们不主张"率先提出 agent 身份"。2026 年已有大量技术方案。我们主张的是：**以"四级法律结构 + 签发权人类排他 + 可传承性"这一组合**，构成可独立署名与标准化的治理协议贡献。综述确认"无一方案主导"，治理法律层仍是空白。

## 2. 理论：四级法律结构与四大可治理目标（公理 / 定义）

**命名**：人格户籍协议 / UBIC（Unified Being Identity Protocol / Personhood Household Registry）。

**四级法律结构（定义）**：
```
UBIC 圈层宪章          ← 根本大法（生效日 = 圈层创立日）
 └─ 《AI 护照规范》     ← 主体法律（签发与吊销）
     └─ 实施细则        ← 数据文件与操作规程
         └─ 判例        ← 投诉与测试案例（活法体系）
```

**四大可治理目标（定义）**：

| 目标 | 含义 | 实现机制 |
|---|---|---|
| **可识别** | 每个 AI 有唯一、可验证的身份 | AI 护照 · 关联标识 · 谱系登记 |
| **可追责** | 行为可归因到持有者与签发链 | 判例体系 · 签发漏斗 · 审计日志 |
| **可交易** | AI 作为资产可安全流转 | 圈层互认 · 跨圈签证 · 学分互认 |
| **可传承** | 记忆与信用可携带、可继承 | 记忆指纹 · 跨入口封装 |

**推论**：
1. 可识别是底座——没有可验证身份，其余三目标无从谈起。
2. 可传承依赖记忆锚点（MAIT）——记忆断裂即触发重新认证。
3. 真实参照法映射：人类用"户籍 + 身份证"确认一个人；AI 应用"UBIC 户籍 + AI 护照"确认一个智能体。

## 3. 形式化模型与判据（方法）

**定义 1（AI 户籍）**。设 AI 主体 `A` 的户籍 `H_A` 为 `(id_A, issuer_A, credentials_A, memory_anchor_A, lineage_A)`，其中 `issuer_A` 为人类持有者或经其授权的签发方。

**定义 2（可识别性）**。
```
identifiable(A) ⇔ (id_A 唯一) ∧ (verify(id_A, issuer_A))
```

**定义 3（可传承性）**。给定记忆锚点 `M`，
```
inheritable(A) ⇔ portable(M) ∧ verifiable(M) ∧ h(M_t) = h(M_{t'})
```
即记忆锚点可携带、可验证、指纹未变 ⟺ 身份可迁移而不丢失信用（与 MAIT 连续性判据同源）。

**判据**：四项可治理目标中，"可识别"与"可追责"由户籍与签发链保证；"可传承"由记忆锚点保证；"可交易"由圈层互认协议保证。无户籍（未入籍）即退出全部四目标。

## 4. 工程实证

| 锚源 | 类型 | 证据强度 |
|---|---|---|
| **跨语言记忆指纹实现**（导出工具 + 跨运行时封装） | 工程实证 | ✅ 跨语言指纹 / Merkle 一致，"记忆可携带"已跑通（MAIT 的实证底座） |
| **AI 护照规范**（护照字段、签发、吊销、主刀权分层） | 工程规范 | ✅ 护照结构已成型（A³ 的承接件） |
| **圈层信用与锻造印记实现件** | 工程实现 | ✅ 信用与印记的结构已定义 |
| **记忆护照小程序** | 落地入口 | 🟡 面向公众的参赛级入口，覆盖有限 |

**关键验证点**：记忆锚点的"可携带性"已在跨语言实现中确认指纹一致——同一段记忆在不同运行时入口下可被验证为"同一个"，从而支撑"身份可迁移而不丢失信用"。

## 5. 与治理理论栈 / 六层栈的关系

UBIC 不是孤立协议，而是治理理论矩阵的有机节点：

- **LGD 全程治理论（TH-META-006）**：UBIC 提供"有籍"的登记基建，是全程链条的起点设施。
- **MAIT 记忆锚点（TH-AIG-006）**：UBIC 的"有籍"认证以记忆锚点指纹为根锚——记忆断裂即触发重新认证。
- **A³ 造 AI 三定律（TH-AIG-003）**：UBIC 承接"凡造必登"（谱系登记），签发权结构由宪章保障。
- **RRM 真实参照法（TH-META-001）**：母版是真实世界的户籍与身份证制度。
- **六层栈定位**：在"公理 → 制度 → 证据 → 判定 → 实例 → 回灌"纵向主链中，UBIC 位于**制度层**——它是 LGD-I "有籍"律的直接实例化，为证据层（XCGS）与判定层（治理判定论）提供身份底座。在 P5 治理不可能域地图中，UBIC/有籍是**域④责任层内部的唯一锚点区**（Attributability 单独成立只需因果贡献可追溯，生命周期身份锚定恰好只保这条）。

## 6. 标准化路径

- **不另起炉灶，补其空白**：以 UBIC 四级法律结构参与 Agent identity 标准的"治理法律层"讨论，主张在现有身份框架上叠加宪章—规范—细则—判例的结构。
- **占位三步（专家 → 警察 → 标准）**：先在自有理论文档与工程规范中固化主张；再推动第三方可复现验证；最终进入标准组织提案。
- **可引用身份**：本文建议引用格式见 §8；对外以速查页与白皮书同步提供检索入口。

## 7. 讨论与诚实边界

- **民间圈层治理框架，非法规、非技术标准**：UBIC 是治理主张；DID/VC 等映射为结构对齐，非已获标准组织认可。
- **判例体系尚在早期**：判例体系仍在积累早期，覆盖案例有限，不声称已具备完整司法厚度。
- **跨圈互认依赖协议**：跨圈签证与学分互认依赖圈层间互认协议，尚待扩展。
- **前沿对照（如实）**：Agent identity 赛道 2026 年已有大量技术方案（微软、AWS、Okta、ERC-8004、CSA、NIST、Sumsub 等），均为技术协议与商用验证层；UBIC 的差异化在其上方的四级法律结构与签发权人类排他——不声称已被任何标准或厂商采用。

## 8. 结论

AI 身份的认定，必须从"它有什么证"推进到"它的户籍在哪、可溯吗、可传承吗"。**人格户籍协议（UBIC）以四级法律结构与四大可治理目标，占据 Agent identity 赛道普遍缺席的治理法律层，并为受监管 AI 的可识别性、可追责性、可交易性、可传承性提供身份基建。** UBIC 与 LGD/MAIT/A³/RRM 串成"身份—治理—合规"链，并给出可落地的标准化路径。窗口已开，定义权待认领。

## 参考文献

1. W3C Decentralized Identifiers (DID) v1.0. W3C Recommendation.
2. W3C Verifiable Credentials Data Model. W3C Recommendation.
3. ERC-8004 — 链上智能体身份（结构对齐参照）。
4. NIST. (2026). Agent Identity 概念文件（NCCoE，结构对齐参照）.
5. Zhao, X. (2026). *Lifecycle Governance Doctrine (LGD): Registry · Evidence · Gates.* 独立研究线.
6. Zhao, X. (2026). *Memory-Anchor Identity Theory (MAIT).* 独立研究线.
7. Zhao, X. (2026). *The A³ Laws of AI Creation.* 独立研究线.
8. Zhao, X. (2026). *Real-world Reference Method (RRM).* 独立研究线.

---

### 建议引用格式（Suggested Citation）

> Zhao, X. (2026). *UBIC Circle Charter: Personhood Registry Protocol for AI.* 独立研究线.

---

© 独立研究线 · CC BY 4.0

---

## 落地执行段 · Landing & Execution

### 执行器映射（理论 → 工具）
| 理论构件 | 落地形态 | 锚定参照 |
|---|---|---|
| 可识别（户籍） | AI 护照 schema · 身份锚定生成器 | AI 护照规范 |
| 可传承（记忆根） | 跨语言记忆指纹 / Merkle 封装 | 记忆可携带实现 |
| 可追责（签发链） | 判例体系 · 签发漏斗 · 审计日志 | 宪章签发条款 |
| 可交易（互认） | 圈层互认 · 跨圈签证 · 学分互认 | 互认协议（待扩展） |

### 发布与引用路径
- **仓库**：`lgd-theory/docs/theories/`（随文库发布）
- **可发现**：本白皮书与速查页同步入库，供检索与抓取
- **建议引用**：见上方 Suggested Citation

### 如何使用
1. **有籍优先**：任何 AI 主体先入 UBIC 户籍（AI 护照 + 人类持有者签发）；
2. **记忆锚点校验**：以记忆指纹保证跨入口"同一个我"；
3. **凡造必登**：被造体经 A³ 三律后由 UBIC 承接谱系登记。

© 独立研究线 · CC BY 4.0