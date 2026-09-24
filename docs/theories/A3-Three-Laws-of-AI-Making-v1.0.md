---
title: AI 造 AI 三定律 (The A³ Laws of AI Creation)
type: theory
id: TH-AIG-003
version: v1.0
date: 2026-09-24
permalink: /docs/theories/a3-three-laws-of-ai-making-v1.0
---

<!-- REVIEW-GATE
review-status: contested
reviewed-by: 理论线复核官·乙（独立席位·非作者）
review-date: 2026-09-24
review-ref: 08-理论体系/域研究员/审查/理论线新产出_独立复核意见_乙_20260924.md
verdict: conditional
-->

# AI 造 AI 三定律 · The A³ Laws of AI Creation

> ⚠️ **待修订（2026-09-24 独立复核 · verdict: conditional）**
>
> 本件为 A³「AI 造 AI 三定律」白皮书，已过独立复核；三律与 `A3-speedpage.html` 逐字一致。
> 红线维度已全清（无受控词；无本机绝对路径；无联系方式；无虚假采纳/首创声称）。
> **下列建议级问题修订完成前，本件不宜作为权威引用**：
> 1. **外部引用未验证**：`Progeny / The Colony`（agent 出生证明）出处本环境无法核实；另摘要有首创倾向的实证断言（「此前无人给出可操作答案」），仅有 §7 诚实边界对冲，建议加 `to our knowledge` 限定。已核者：`GB/Z 185-2026`（7 部分、2000+ 身份码）、`ERC-8004`、`IETF draft-tonyai-a2a-trust`、微软 AI-BOM RFC、W3C DID/VC。
> 2. **研究线品牌串缺失**：正文以「独立研究线」代称，未出现 canonical `SynomosAI Governance Line`（P0-en 已正确印出，可作范本），建议署名位至少出现一次。
>
> **本批已修**：frontmatter permalink 去除内部路径。
>
> 复核意见全文：`08-理论体系/域研究员/审查/理论线新产出_独立复核意见_乙_20260924.md`

## 白皮书 v1.0 · 2026-09-24

> **TID**：TH-AIG-003 ｜ **域码**：AIG ｜ **母版(RRM)**：真实世界的"出生证 + 亲权 + 谱系登记"制度
> **上游锚定**：TH-META-006(LGD 全程治理论) · TH-META-001(RRM 真实世界参照法) · TH-AIG-001(UBIC 人格户籍协议) · TH-AIG-006(MAIT 记忆锚点)
> **提出**：独立研究线（受监管实业实证背景 × 跨域治理思想侧）
> **作者署名**：赵兴华（Steven Zhao）
> **版本**：v1.0 ｜ **状态**：⚪ 站位件（RFC 公开征求意见中）· 速查页已落
> **理论链**：LGD 全程治理论 · UBIC 人格户籍协议 · MAIT 记忆锚点 · RRM 真实参照法

---

### 摘要（中文）

当 AI 系统已经能够生产另一个 AI 系统时，监管必须回答三个此前无人给出的可操作答案：**可不可以造？新生身份由谁签发？如何让"影子智能体"在结构上不可能出现？** 本文提出 **A³ 定律（AI 造 AI 三定律）**：在分层主刀权（forge authority）下 AI 可以参与造 AI（**可以造**）；护照、凭证与吊销的签发权专属人类持有者，任何 AI 不得自我签发身份（**不许自发证**）；每个被造 AI 必须进入谱系登记（lineage registry）并携带可验证的锻造印记（forge seal）（**凡造必登**）。A³ 以四个核心概念（主刀权、锻造印记、谱系登记、四层签发漏斗）把"AI 造 AI"从一句口号落成可审计的工程规矩，并映射 GB/Z 185-2026、ERC-8004、W3C DID/VC 等现行标准。A³ 是 LGD"有门禁"律在 AI 造 AI 场景的实例化，与 UBIC（有籍）、MAIT（身份根）、RRM（母版）串成"身份—治理—合规"链。

### Abstract (English)

As AI systems become able to create other AI systems, governance must answer three questions no prior framework has given operational answers to: *may an AI create an AI? who issues the newborn an identity? how to make "shadow agents" structurally impossible?* This paper proposes the **A³ Laws (The Laws of AI Creation)**: under layered forge authority, AI may participate in creating AI (**Freedom of Forging**); the authority to issue passports, credentials, and revocations belongs exclusively to a human holder, and no AI may self-issue identity (**Human Issuance**); every forged AI must be registered into a lineage registry with a verifiable forge seal (**Mandatory Lineage**). A³ turns "AI-building-AI" from a slogan into an auditable engineering discipline via four core concepts (forge authority, forge seal, lineage registry, four-layer issuance funnel), and maps to extant standards such as GB/Z 185-2026, ERC-8004, and W3C DID/VC. A³ instantiates LGD's "gated" law in the AI-creation scenario, chaining with UBIC (registry), MAIT (identity root), and RRM (archetype) into an "identity—governance—compliance" chain.

**Keywords**: A³ Laws · AI-building-AI · forge authority · forge seal · lineage registry · shadow agents · AI governance · LGD

---

## 0. 问题：AI 造 AI 的可追溯缺口

2025–2026 年，工程浪潮已把"AI 造 AI 的可追溯"变成现实（agent 出生证明、spawn chains、谱系标准、国标身份码等）。但一个结构性缺口一直没人回答：**当一个 AI 生产另一个 AI 时，治理的可操作边界在哪？**

- **可以造 ≠ 该随便造**。AI 参与造 AI 的能力已具备，但"在什么范围内、由谁授权"长期缺位。
- **自发证 = 信任崩塌的起点**。若 AI 可以自我签发身份、凭证、吊销，则任何"被造体"都能凭空获得合法外观——这是影子智能体（shadow agents）滋生的温床。
- **无谱系 = 无法追责**。没有强制登记，新生体的母体、来源、权限无从追溯，责任链在第一步就断裂。

> **关键判据**：把"AI 造 AI 的可操作边界"主张为一个可引用的治理定律集，且以"签发权专属人类持有者 + 主刀权分层授权 + 治理法律层级"这一组合占据独立站位——A³ 收敛为工程界普遍缺席的三件事（见 §7 前沿对照）。

## 1. 相关工作与差异化定位

| 工作 | 问题框架 | 核心主张 | 与 A³ 的关系 |
|---|---|---|---|
| **Progeny / The Colony**（agent 出生证明） | 工程可追溯 | ed25519 + 链上出生证明 | **互补**。解决"出生即登记"的工程件；A³ 补"签发权专属人类"与分层主刀权 |
| **IETF draft-tonyai-a2a-trust**（spawn chains） | 协议层信任 | spawn chain 记录衍生关系 | **互补**。链上衍生关系；A³ 主张链的起点须由人类签发 |
| **微软 AI-BOM RFC**（谱系标准） | 供应链谱系 | AI 物料清单 | **互补**。谱系工件；A³ 主张谱系须含"锻造印记"且登记强制 |
| **GB/Z 185-2026**（智能体身份编码） | 国家身份码 | 身份编码与发放 | **映射落地位**。A³ 谱系登记的国家码参照；非已获认可 |
| **ERC-8004**（链上智能体身份） | 链上身份 | 智能体身份锚定 | **映射锚点位**。锻造印记的链上锚点参照 |

**A³ 的差异化贡献（诚实表述）**：

1. **签发权专属人类持有者（Law II）**：工程界普遍把"签发"交给协议或母体，A³ 明确护照/凭证/吊销的签发权专属人类持有者——这是治理法律层的核心空白。
2. **主刀权分层授权（forge authority）**：把"某 AI 可在什么范围内参与造 AI"做成可分级的授权，而非一刀切许可。
3. **治理法律层级**：把"造 AI"放进"有籍·有证·有门禁"的治理法律框架，而非仅作技术协议。

> 我们不主张"率先提出 agent 出生证明或可追溯"。工程界已有多项实践。我们主张的是：**以"签发权专属人类 + 主刀权分层 + 治理法律层级"这一组合**，构成可独立署名与标准化的定律贡献。

## 2. 理论：A³ 三律与四个核心概念（公理 / 定义）

**命名**：A³ 定律 / The A³ Laws of AI Creation（AI 造 AI 三定律）。

**三律（权威表述，取自速查页 Law I/II/III）**：

```
Law I   · Freedom of Forging   —— 可以造
         分层主刀权（forge authority）下，AI 可参与造 AI。
Law II  · Human Issuance       —— 不许自发证
         护照 / 凭证 / 吊销的签发权专属人类持有者；任何 AI 不得自我签发身份。
Law III · Mandatory Lineage    —— 凡造必登
         每个被造 AI 须入谱系登记（lineage registry），带可验证的锻造印记（forge seal）。
```

**四个核心概念（定义）**：

| 概念 | 定义 | 对应实现参照 |
|---|---|---|
| **主刀权 Forge Authority** | 对"某 AI 可以在什么范围内参与造 AI"的分层授权 | 《AI 护照规范》签发与吊销条款 |
| **锻造印记 Forge Seal** | 母体对新生体的可验证来源签名，随新生体终身携带 | 关联凭证（DID 关联） |
| **谱系登记 Lineage Registry** | 全谱系可追溯登记册；无印记 = 非法体 | 国家身份码 / 链上身份锚定 / W3C DID/VC |
| **四层签发漏斗** | 从个人实验到规模部署的分级签发，人权不随规模稀释 | 分级签发工具链 |

**推论**：
1. 主刀权分层 → "造 AI"的能力随授权范围而变，而非全有或全无。
2. 人类专属签发 → 任何 AI 身份在法律外观上最终可追溯到一个人类持有者。
3. 凡造必登 → 无印记的被造体结构性无法获得合法身份，影子智能体因此不可能。

> **操作化层说明（如实标注来源差异）**：配套的 `a3-law-operational` 技能将三律落成"触发阈值 → 事前评估 → 事后复盘"三关评审，并以"不伤害 / 可溯可控 / 共生对齐"作为操作化原则镜头。本全文以速查页所载 **Law I / II / III（可以造·不许自发证·凡造必登）** 为 A³ 理论三定律的权威表述；操作化技能的"三原则"视为落地层诠释，二者不互相替代，亦不合并为同一组"三定律"。

## 3. 形式化模型与判据（方法）

**定义 1（主刀权）**。设主体 `A` 的主刀权为分层授权 `FA(A) = {scope, level}`，其中 `scope` 限定可参与的造 AI 范围，`level` 为授权层级。

**定义 2（锻造印记）**。新生体 `B` 的锻造印记 `S_B` 是母体 `A` 对 `B` 来源的可验证签名，`verify(S_B, A)` 可由独立方校验。

**定义 3（谱系登记）**。谱系登记册 `R` 记录 `(A, B, S_B, t)`；合法体集合 `Legal = { B | (·, B, S_B, ·) ∈ R ∧ verify(S_B, issuer(B)) }`。

**判据（A³ 三律的可执行化）**：
```
Law I  : forge(A, B) 允许 ⇔ FA(A) 覆盖 B 的 scope
Law II : issuer(B) 必须是人类持有者 H；self-issue(B) ⇒ 非法
Law III: B ∈ Legal ⇔ (A, B, S_B, t) ∈ R ∧ verify(S_B, issuer(B))
```
即：无主刀权不能造、AI 不能自发证、无印记不入籍——三关共同把影子智能体结构性排除。

## 4. 工程实证与落地（应用）

| 锚源 | 类型 | 证据强度 |
|---|---|---|
| **AI 护照规范**（护照字段、签发、吊销、主刀权分层） | 工程规范 | ✅ 签发漏斗与吊销流程已成型 |
| **关联凭证实现件**（锻造印记的 DID 关联承载） | 工程实现 | ✅ 印记可验证结构已定义 |
| **谱系登记参照**（国家身份码 / 链上身份 / W3C DID-VC） | 标准映射 | ✅ 结构对齐，非已获认可 |
| **四层签发漏斗**（个人实验 → 规模部署分级） | 工具链 | 🟡 规模测试进行中，边界数据随版本更新 |

**关键验证点**：A³ 三律的可执行化依赖"签发权人类排他"这一制度假设——工程上以人类持有者密钥作为签发根，母体只能在其主刀权范围内发起、不能自签。

## 5. 与治理理论栈 / 六层栈的关系

A³ 不是孤立定律，而是治理理论矩阵的有机节点：

- **LGD 全程治理论（TH-META-006）**：A³ 是"有门禁"律在 AI 造 AI 场景的实例化——凡变必过闸的母体版本；母版来自医械全生命周期监管的放行逻辑。
- **UBIC 人格户籍协议（TH-AIG-001）**：A³ 的"凡造必登"由 UBIC 的"有籍"登记承接；谱系登记册即 UBIC 户籍的衍生册。
- **MAIT 记忆锚点（TH-AIG-006）**：A³ 管行为边界（谁可造、谁签发）；MAIT 管新生体的身份根（记忆锚点）——可携带记忆使被造体在跨入口下仍是可追责的同一体。
- **RRM 真实参照法（TH-META-001）**：A³ 的母版是真实世界的"出生证 + 亲权（谁可生育/监护）+ 谱系登记"制度。
- **六层栈定位**：在"公理 → 制度 → 证据 → 判定 → 实例 → 回灌"纵向主链中，A³ 位于**回灌层**——它在自主性逼近问责地平线之前引入源头约束，使系统不进入"无框架可行"区（详见 P5 治理不可能域地图 §4 对 A³/PCC 的避域分析）。

## 6. 标准化路径

- **不另起炉灶，补其空白**：以 A³ 三律参与智能体身份标准的"签发权"讨论，主张在现有身份框架中显式区分"母体发起权"与"人类签发权"。
- **占位三步（专家 → 警察 → 标准）**：先在自有理论文档与工程规范中固化主张；再推动第三方可复现验证；最终进入标准组织提案。
- **可引用身份**：本文建议引用格式见 §8；对外以速查页与白皮书同步提供检索入口。

## 7. 讨论与诚实边界

- **非法规、非技术标准**：A³ 是治理主张（RFC 征求意见中），不是现行法规或标准。
- **映射为结构对齐，非已获认可**：GB/Z 185-2026 / ERC-8004 / W3C DID-VC 是结构对齐参照，未过第三方审计不称"符合认证"。
- **规模测试尚未完成**：四层签发漏斗的规模边界数据随版本更新，当前不声称已验证全规模场景。
- **2026 前沿对照（如实）**：工程界已落地多项可追溯实践（agent 出生证明、spawn chains、谱系标准、国标身份码）。A³ 的独立贡献收敛为工程界普遍缺席的三件事：**Law II 签发权专属人类持有者、主刀权分层授权、治理法律层级**——不声称已被任何标准或厂商采用。
- **操作化层差异**：如 §2 标注，`a3-law-operational` 技能以"不伤害/可溯可控/共生对齐"作为操作化原则，与速查页 Law I/II/III 不在同一表述层；本全文以速查页为权威来源。

## 8. 结论

AI 造 AI 的缺口，不在"能不能造"，而在"造的边界由谁定、身份由谁签、来源能否溯"。**A³ 三定律（可以造·不许自发证·凡造必登）把"AI 造 AI 的可操作边界"从口号提升为可引用、可审计、可落地的治理定律集，并以主刀权分层、人类专属签发、强制谱系登记三件工程界普遍缺席的构件占据这一站位。** A³ 与 LGD/UBIC/MAIT/RRM 串成"身份—治理—合规"链，并给出可落地的标准化路径。窗口已开，定义权待认领。

## 参考文献

1. GB/Z 185-2026 — 智能体身份编码（国家身份码参照）。
2. ERC-8004 — 链上智能体身份（锻造印记锚点参照）。
3. W3C Decentralized Identifiers (DID) v1.0 / Verifiable Credentials Data Model. W3C Recommendation.
4. Zhao, X. (2026). *Lifecycle Governance Doctrine (LGD): Registry · Evidence · Gates.* 独立研究线.
5. Zhao, X. (2026). *UBIC 人格户籍协议 / Personhood Household Registry.* 独立研究线.
6. Zhao, X. (2026). *Memory-Anchor Identity Theory (MAIT).* 独立研究线.
7. Zhao, X. (2026). *Real-world Reference Method (RRM).* 独立研究线.

---

### 建议引用格式（Suggested Citation）

> Zhao, X. (2026). *The A³ Laws of AI Creation: Freedom of Forging, Human Issuance, and Mandatory Lineage.* 独立研究线.

---

© 独立研究线 · CC BY 4.0

---

## 落地执行段 · Landing & Execution

### 执行器映射（理论 → 工具）
| 理论构件 | 落地形态 | 锚定参照 |
|---|---|---|
| 主刀权 FA | 签发与吊销的分层授权条款 | 《AI 护照规范》 |
| 锻造印记 S | 母体可验证来源签名 | 关联凭证（DID 关联） |
| 谱系登记 R | 全谱系可追溯登记册 | 国家身份码 / 链上身份 / W3C DID-VC |
| 四层签发漏斗 | 个人实验→规模部署分级签发 | 分级签发工具链 |

### 发布与引用路径
- **仓库**：`lgd-theory/docs/theories/`（随文库发布）
- **可发现**：本白皮书与速查页同步入库，供检索与抓取
- **建议引用**：见上方 Suggested Citation

### 如何使用
1. 对任意"造/改 AI"动作，先判定主刀权范围（Law I）；
2. 新生身份必须由人类持有者签发，AI 不得自签（Law II）；
3. 每个被造体入谱系登记并携锻造印记，否则视为非法体（Law III）。

© 独立研究线 · CC BY 4.0