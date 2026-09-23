---
title: 治理不可能域地图 (The Governance Impossibility Map)
type: theory
id: P5
version: v0.3
date: 2026-09-24
permalink: workbuddy/08-理论体系/发布/lgd-theory/docs/theories/p5-governance-impossibility-map-v0.3
---

# 治理不可能域地图 · The Governance Impossibility Map
## 工作稿 v0.3 · 2026-09-24（整理自 papers/ 中英论文）

> **编号**：论文矩阵 P5 ｜ **域码**：边界（Boundary）｜ **母版(RRM)**：Jobin 2019「原则地图」的画地图姿势
> **上游锚定**：TH-META-001(RRM 真实世界参照法) · TH-META-006(LGD 全程治理论) · TH-META-011(治理判定论)
> **提出**：独立研究线（受监管实业实证背景 × 跨域治理思想侧）
> **作者署名**：赵兴华（Steven Zhao）
> **版本**：v0.3 ｜ **状态**：⚪ 工作稿（投稿就绪）· 速查页已落
> **理论链**：LGD 全程治理论 · 治理判定论 · RRM 真实参照法（本图为治理理论栈的边界约束层）

---

### 摘要（中文）

2025–2026 年，AI 治理领域密集出现一批"某些治理目标在结构上不可能同时达成"的结果：可解释性的信息论边界（Rao 2025）、行为式治理的计算理论边界（McCann 2026）、集体问责的公理化边界（Tibebu & Shemtaga 2026）、事前授权的可观测性边界（Meyman 2026；Fernandez 2026；Zhu & Leonard 2026），以及更早的算法透明性哲学批判（2019–2025）。这些结果散落在五个互不引用的文献簇中。本文不证明任何新定理，而是做三件事：①逐块给出五块"不可能域"的精确命题、出处、临界条件与证据强度；②给出一张嵌套-交叠整合图（作者综合主张，非共识）；③在可能域一侧标出既有治理资产（含作者方体系）的站位与避域理由——把不可能性文献从"治理的丧钟"读成"治理的设计约束"。

### Abstract (English)

Between 2025 and 2026, AI governance witnessed a dense cluster of impossibility results: the information-theoretic limits of explainability (Rao 2025), the computational limits of behavioural governance (McCann 2026), the axiomatic limits of collective accountability (Tibebu & Shemtaga 2026), the structural impossibility of observation-based ex-ante authorization (Meyman 2026; Fernandez 2026; Zhu & Leonard 2026), and the earlier philosophical critique of algorithmic clarity (2019–2025). These results are scattered across five mutually non-citing literature clusters. This paper proves no new theorem. It does three things: (1) states each of five impossibility domains precisely — proposition, source, boundary condition, evidential strength; (2) offers a nesting-and-overlap integration map, explicitly flagged as the authors' synthesis rather than consensus; and (3) locates existing governance assets — including the authors' own — inside the possibility domain, converting impossibility literature from a knell into a design constraint.

**Keywords**: AI governance; impossibility theorem; explainability; undecidability; accountability; ex-ante authorization; determination debt

---

## 0. 问题：原则层趋同之后，不可能性结果来了

Jobin、Ienca 与 Vayena（2019）把全球 AI 伦理指南的原则趋同画成一张地图，成为被引数千次的坐标系。2025–2026 年出现了与原则地图对称的另一批文献：不再说"应该怎样治理"，而是证明"某些治理目标在结构上不可能同时达成"。这些结果的共同困境是**没有坐标**——发表于不同学科、使用不同词汇、互不引用；治理者读到其中任何一篇，都无法回答三个实际问题：这与我读过的另一篇是一回事吗？我的治理体系是否已经踩进了不可能域？踩进去了怎么办？

一个可核实的细节说明坐标缺失的程度：Tibebu 与 Shemtaga（2026）在摘要中称其结果是"AI 治理中第一个不可能性结果"，而 Rao（2025-04-29 提交）已证明监管不可能定理，早近一年，且两文无引用关系。这不构成对任何一方的批评，恰恰证明：这些结果之间的地图是缺位的。本文补这张地图。本图是盘点型 + 批判型合体（对标 Jobin 2019 画地图姿势：不做新定理，做坐标系）。

**命名与划界**：本文将这张图命名为**治理不可能域地图（the Governance Impossibility Map）**。两点划界：①本文与设计批评界的 "impossible map" 概念无关——那是对地图作为方法论的设计批判，本文是治理结果的整合图；②"regulatory impossibility results" 一词由 Rao（2025）首创，本文仅在指称其定理时使用，不作为本地图的统称。全文不使用任何缩写指代本地图。

## 1. 相关工作与差异化定位

本文定位为**坐标整合**，而非新定理。其差异化在于把五个独立进路的不可能结果收进一张可导航的坐标系，并指出它们"方向一致、进路独立"的收敛证据。

| 相邻工作 | 性质 | 与本地图的关系 |
|---|---|---|
| **Jobin, Ienca & Vayena 2019** | 原则趋同地图 | **方法论先例**。本地图沿用"画地图"姿势，但对象从原则转向不可能性结果 |
| **Rao 2025（监管不可能定理）** | 信息论定理 | **域②来源**。术语"regulatory impossibility results"归其首创 |
| **McCann 2026（两边界）** | 计算理论定理（Coq 机械化） | **域③来源** |
| **Tibebu & Shemtaga 2026（问责地平线）** | 公理化定理 | **域④来源** |
| **Meyman / Fernandez / Zhu & Leonard 2026** | 授权-观测层定理 | **域⑤来源（三组独立发现）** |
| **Kalulé / Springer / IJSL** | 哲学批判 | **域①来源** |

**诚实表述**：本地图不主张首创任何定理，也不主张首创地图姿势（Jobin 2019 在先）。其学术增量是三条整合主张（见 §3）：五进路方向一致的收敛证据、嵌套关系综合、以及"坐标缺位"的两组实证（互不引用）。

## 2. 理论：五块不可能域（公理 / 定义）

### 2.1 域①哲学层：算法清晰性批判（批判级）
- **命题**：算法系统的封闭性与法律对确定性、透明性的要求之间存在结构性张力；要求算法决策达到法律所要求的"清晰"可能是范畴错误。代表：Kalulé（2019）、Springer（2019）、IJSL 2025《Against Algorithmic Clarity》。
- **临界条件**：当治理要求"算法决策可被法律程序完整复述"时，张力爆发。
- **证据强度**：批判级（概念论证，无形式化定理）。地图定位：最外环——语言与概念层面的不可能。

### 2.2 域②可解释性层：监管三难（信息论级）
- **命题**（Rao 2025，arXiv:2504.20676）：以 Kolmogorov 复杂度将"解释"形式化为对模型的更简近似。核心：①复杂度鸿沟定理——任何显著比原模型简单的解释必然在某些输入上不一致；②**监管不可能定理**——"任何治理框架都无法同时追求：不受限的 AI 能力、人类可解释的解释、可忽略的误差"。
- **临界条件**：三目标同时取极限时不可兼得；放松任一目标即退出不可能域。
- **证据强度**：信息论级（复杂度界形式化证明；对 Lipschitz 函数给出指数/多项式精确界）。地图定位：中间环——信息层面的不可能（解释作为有损压缩有数学下界）。

### 2.3 域③判定层：行为式治理的两个边界（定理级）
- **命题**（McCann 2026，arXiv:2604.27292）：每个系统有两个边界——能力边界（expressiveness）与治理覆盖边界（governance），产生三区域：受治理能力（唯一有用区）、未治理能力（风险）、针对不存在能力的治理（theater）。由 Rice 定理（1953）：对任何图灵完备架构，"此程序的效果符合治理策略"这一非平凡语义属性**机器不可判定**——行为式治理在一般情况下结构性失败。出口是**共端治理（coterminous governance）**：两边界可证同一，要求"计算与效果分离"的架构决策。证明以 Coq 机械化（454 定理、36 模块、0 admitted）。
- **临界条件**：治理采取"事后外挂、语义级判定任意程序行为"的形态时，不可判定性全额兑现。
- **证据强度**：定理级（计算理论经典结果 + 机械化证明）。地图定位：内环——计算层面的不可能（语义级合规判定不可判定，除非改变架构）。
- **最近邻辨析（Chalupa DIP/DCF，必引）**：Chalupa 的 Decision Demonstrability & Identity Failure 框架与 Decision Closure Framework 是本域决策执行中心的最近邻；划界：Chalupa 回答"决策何时允许执行、合法性条件失效时权威归谁"（决策→执行轴），McCann 回答"语义级判定在计算上是否可判"（可计算性轴），本图域④回答"责任能否分配"（社会选择轴）。

### 2.4 域④责任层：问责地平线（定理级）
- **命题**（Tibebu & Shemtaga 2026，arXiv:2604.07778）：将人机混合系统形式化为 Human-Agent Collectives（状态-策略元组 + 结构因果模型），自主性以四维信息论画像刻画（认知 / 执行 / 评估 / 社交）。问责框架公理化为四条最小性质：**归因性 Attributability**、**可预见界 Foreseeability Bound**、**非空虚 Non-Vacuity**、**完备性 Completeness**。**问责不完备定理**：当复合自主性超过**问责地平线（Accountability Horizon）**且交互图含人机反馈环时，任何框架都无法同时满足四公理；不可能性是结构性的——透明、审计、监督均无法解决，除非降低自主性。地平线以下合法框架存在：锐利相变。3000 个合成 collectives 实验零违例。
- **临界条件**：复合自主性 × 人机反馈环——两个条件同时满足时不可兼得；降低自主性或切断反馈环即退出。
- **证据强度**：定理级（公理化证明 + 大规模合成实验验证）。地图定位：内环偏责任侧——社会选择层面的不可能（责任分配作为数学结构有不可满足区）。

### 2.5 域⑤授权-观测层：可观测性不构成事前授权（定理级）
- **命题**（三组独立发现，2026 上半年，互不引用）：
  - **Meyman 2026**（FERZ 研究纲领，Zenodo 10.5281/zenodo.19647542）：**没有任何可观测性架构能产出满足事前（ex-ante）授权要求的制品**。三引理：观测信号对被治理系统的候选动作是因果后验的；依赖观测刻画的制品无法被验证者独立验证；观测输出的任何组合都无法逃脱此约束。推论：时延无关、干预无关。
  - **Fernandez 2026**（Agent Governance Series，Zenodo 10.5281/zenodo.19669430）：认证投影（attestation）**必要而不充分**——完整性（integrity）与覆盖（coverage）必须分离。两定理三推论 + 10 万步实验。
  - **Zhu & Leonard 2026**（Applied Sciences 16(10):4917）：固定信息结构下部署可行性三 regime 划分——**完美的事后监控也无法解决观测结构固有的歧义**。
- **临界条件**：治理把"观测能力"误当"授权能力"时全额兑现；把授权做成执行前独立裁决（而非观测衍生品）即退出。
- **证据强度**：定理级（形式化引理/定理 + 实验验证；MDPI 版经同行评审）。地图定位：内环偏执行侧，与域③互补（一个关于判定、一个关于授权）。
- **输出态最近邻辨析（L2D 谱系，必引）**：Learning to Defer（Chow 1957 → … → 牛津综述 2025）是"AI 不确定时交给人类"的 ML 成熟领域，与悬置表面同构；划界：L2D 是每次预测的路由动作（无制度语义），本图域⑤与治理判定论的悬置是制度态（带台账字段、审计链、度量与生命周期门禁）。
- **制度谱系锚**："判定前移"制度族在行政法/贸易法成熟存在数十年——advance ruling（WTO《贸易便利化协定》）、declaratory judgment（28 U.S.C. §2201）、FDA Pre-Sub/Q-Submission（MDUFA VI 的"缺陷信停钟、响应重启"机制是悬置核算的官方先例）。

### 2.6 外缘注记：民间版论题与早期综述（不入图）
- Palm（2026，LinkedIn）"监管不完备性论题"：无定理级证明，**不入图**，作外缘注记（证明不可能性叙事正在业界扩散）。
- "On Controllability of AI"（arXiv:2008.04071，2020）：跨域文献汇编，列为域⑤观测维度的思想前驱并引用；地图增量不被其覆盖。

## 3. 方法：嵌套与交叠整合图 + 可能域四问检验

**整合图（作者综合主张，非共识）**：
```
民间层注记：Palm「监管不完备性论题」（2026，无定理，叙事扩散信号）
┌─────────────────────────────────────────────────────────┐
│ 域① 哲学层：算法清晰性批判（批判级）                        │
│   ┌───────────────────────────────────────────────────┐ │
│   │ 域② 可解释性层：监管三难（信息论级，Rao 2025）        │ │
│   │   ┌─────────────────────────────────────────────┐ │ │
│   │   │ 域③ 判定层：两边界（定理级，McCann 2026）      │ │ │
│   │   │   ╔═════════════════════════════════════════╗ │ │ │
│   │   │   ║ 域⑤ 授权-观测层（定理级，三组独立发现    ║ │ │ │
│   │   │   ║   互不引用）观测≠事前授权；监控≠许可     ║ │ │ │
│   │   │   ┌───────────────────────────────────────┐ │ │ │ │
│   │   │   │ 域④ 责任层：问责地平线（定理级，       │ │ │ │ │
│   │   │   │   Tibebu & Shemtaga 2026）              │ │ │ │ │
│   │   │   └───────────────────────────────────────┘ │ │ │ │
│   │   └─────────────────────────────────────────────┘ │ │ │
│   └───────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
（责任层与判定层在"高自主性+人机反馈环"条件下交叠；域⑤与域③并列内环）
```

**三条整合主张（核心学术增量）**：
1. **方向一致、进路独立**：五块域不互相推导，却从概念批判、信息论、计算理论、公理化社会选择、授权架构分析五个独立进路逼近同一结论。
2. **嵌套关系是综合主张，非共识**：各域内部结论归原作者；嵌套若被修正，地图以可修正方式容纳。
3. **互不引用的实证（两组）**：①域②与域④——Rao 先于 Tibebu 近一年，后者自称"第一个"；②域⑤内部——Meyman、Fernandez、Zhu & Leonard 半年内独立给出同构结论。

**可能域四问检验（任何治理体系都可自测）**：
1. 你的治理动作依赖语义级判定吗？（域③：对图灵完备系统不可判定）
2. 你的问责承诺隐含 Completeness 吗？（域④：超阈值不可满足）
3. 你的透明度承诺忽视解释的信息下界吗？（域②：解释是有损压缩）
4. 你的"可观测性"被当成"授权能力"卖了吗？（域⑤：监控≠许可）

> 四问之后仍站得住的资产，才是不可能性文献之后仍然有效的资产。

## 4. 与治理理论栈 / 六层栈的关系（应用定位）

不可能域之外的全部区域是**可能域**。本图标出六类治理资产在可能域的站位与避域理由——以作者方体系（LGD / 治理判定论 / ACD 家族 / XCGS / A³ / 共存论）为实例，方法可推广：

| 资产 | 站位 | 避域理由 |
|---|---|---|
| **治理判定论** | L0–L4 判据谱系 | 避开域③：监管判定不判定任意程序语义，只判定离散申报属性 |
| **LGD-I 有籍** | 域④内部的唯一锚点区 | Attributability 单独成立只需因果贡献可追溯——生命周期身份锚定恰恰只保这条 |
| **ACD 家族（判定器）** | L2 规则态实例 | 避开域③：输入离散申报属性，输出四态定性（含悬置态） |
| **XCGS 证据链** | 可能域通行证（观测与记录侧） | 域⑤是它的边界而非坟墓：只声称"判定可被第三方重验的基础设施"（records ≠ verdicts） |
| **A³ / PCC（母体约束）** | 域④边界外的制度回灌 | 不解决责任分配的数学不可能，但在自主性逼近阈值前引入源头约束 |
| **共存论** | 对域②的制度回应 | 三难允许"人机互补的误差分配"，人在环是误差的制度性分担 |
| **LGD-III 有门禁** | 域⑤的定理级背书区 | Meyman 证明"监控堆栈不产生授权制品"——门禁必须是制度化的显式判定 |

**六层栈定位**：在"公理 → 制度 → 证据 → 判定 → 实例 → 回灌"纵向主链中，P5 治理不可能域地图位于**边界约束层**——它是 LGD 六层主链左侧（RRM 方法层）与右侧（各实例化）的**结构性护栏**：任何治理主张在落地前须过"四问检验"，确认自己不在哪块不可能域内。本图与治理判定论（命题层升维）并列，是 LGD 理论栈的两大升维方向之一。

## 5. 应用：对治理者的含义——从"完美合规"到"债务管理"

五块域合起来的治理教训只有一条：**以"完美合规"为默认目标的治理范式，会把大量资源投入不可能域**。转向是——治理的有效产出不是"合规声明"，而是"判定与债务管理"：

1. **显式化判定点**：把治理要求落到离散、可判定的属性上（域③的出口；Rules as Code 运动——Catala / L4 / Hildebrandt——已为"规则即代码"的可判定性提供体系与批判基础）。
2. **显式化悬置**：判据、证据、主体不齐时，输出"悬置"并记账，而非硬判或默默放行——治理失败的主要形态是**判定债务**（已声明但未具备判定条件的要求之存量）的隐形累积。
3. **显式化边界**：对每项治理承诺，说明它假设自己不在哪块不可能域内——承诺可审计的前提是承诺可定位。

**债务族谱（辨析）**：技术债、验证债、保证债、合规债、监管债均已具名；本图的**判定债务是族谱第六位、唯一指向判定本体的上游成员**——其余五种记录"证据/动作/合规物的欠账"，判定债务记录"监管定性本身的欠账"。引用本概念时须显式作此辨析。

## 6. 边界与诚实限制

1. **嵌套图是综合主张，可修正**：接受嵌套标注为作者综合主张；地图的值在坐标功能而非几何精确。
2. **定理边界可能被未来工作放松**：每块域已标临界条件；定理边界变化表现为域的收缩/扩张而非地图失效。
3. **民间版论题不入图**：无定理级证据，入图会降低证据标准。
4. **不否定治理**：地图的全部用意是把治理资源从不可能域撤出、投向可能域（身份锚定、离散判定、证据复放、债务管理）。
5. **作者方资产入图非循环**：地图独立成立（§2–§3 不依赖作者方资产）；§4 是地图的一个应用实例，方法可推广。
6. **命名划界**：与设计批评界 "impossible map" 概念无关；"regulatory impossibility results" 一词由 Rao（2025）首创；全文不使用缩写指代本地图。
7. **查重与采用（如实）**：九轮检索零撞车，命名短语双库 0 占用；本图为整合图与综述性梳理，**不主张首创**；外部引用实测为 0，不声称已被引用或采纳。

## 7. 结论

AI 治理的有效域是有结构边界的。治理者面对的不是定理太少，而是没有人告诉这些结果之间是什么关系、哪些区域无法到达、哪些仍可行。**治理不可能域地图把五块互不引用的不可能结果收进一张可导航的坐标系，并给出可能域四问检验，把不可能性文献从"治理的丧钟"读成"治理的设计约束"。** 地图以"五进路方向一致的收敛证据 + 坐标缺位的实证 + 嵌套整合"占据整合图站位，并给出可落地的应用方法。窗口已开，定义权待认领。

## 参考文献

1. Jobin, Ienca & Vayena (2019). *The global landscape of AI ethics guidelines.* Nature Machine Intelligence.
2. Rao, S. (2025). *The Limits of AI Explainability (regulatory impossibility theorem).* arXiv:2504.20676.
3. McCann, A. L. (2026). *The Two Boundaries: Why Behavioral AI Governance Fails Structurally.* arXiv:2604.27292.
4. Tibebu, H. & Shemtaga, H. (2026). *The Accountability Horizon.* arXiv:2604.07778.
5. Rice, H. G. (1953). *Classes of recursively enumerable sets and their decision problems.* Trans. AMS.
6. Meyman, E. (2026). *On the Impossibility of Observability-Based Authorization.* FERZ / Zenodo 10.5281/zenodo.19647542.
7. Fernandez, M. (2026). *Agent Governance Series.* Zenodo 10.5281/zenodo.19669430.
8. Zhu & Leonard (2026). *Deployment feasibility regimes.* Applied Sciences 16(10):4917.
9. Kalulé (2019); Springer (2019); IJSL 2025《Against Algorithmic Clarity》.
10. Chalupa (2026). Decision Demonstrability & Identity Failure / Decision Closure Framework. Zenodo.
11. Catala / L4 / Hildebrandt（Rules as Code 体系与批判）.
12. MDUFA V/VI (FDA)；advance ruling / declaratory judgment（行政法制度谱系）.
13. *On Controllability of AI* (arXiv:2008.04071, 2020).
14. Zhao, X. (2026). *Lifecycle Governance Doctrine (LGD).* 独立研究线.
15. Zhao, X. (2026). *Governance Determinability Doctrine（治理判定论）.* 独立研究线（工作稿）.

---

### 建议引用格式（Suggested Citation）

> Zhao, X. (2026). *The Governance Impossibility Map: Five Impossibility Domains in AI Governance and Where the Possibility Domain Begins.* 独立研究线（工作稿 v0.3）.

---

© 独立研究线 · CC BY 4.0

---

# The Governance Impossibility Map — Full English Version

**Working Paper v0.3 · 2026-09-24**

## Abstract

Between 2025 and 2026, AI governance witnessed a dense cluster of impossibility results (Rao 2025; McCann 2026; Tibebu & Shemtaga 2026; Meyman / Fernandez / Zhu & Leonard 2026; plus the earlier philosophical critique 2019–2025), scattered across five mutually non-citing clusters. This paper proves no new theorem; it states each of five impossibility domains precisely, offers a nesting-and-overlap integration map (author synthesis, not consensus), and locates governance assets inside the possibility domain — converting impossibility literature from a knell into a design constraint.

## 1. The Problem: After Convergence of Principles, the Impossibility Results

Jobin, Ienca & Vayena (2019) mapped the convergence of AI-ethics principles. 2025–2026 produced a symmetric body of work proving that certain governance goals cannot be jointly achieved. The shared predicament is the absence of coordinates: different disciplines, different vocabularies, zero cross-citation. One checkable detail: Tibebu & Shemtaga (2026) call their result "the first impossibility result in AI governance," while Rao (submitted 29 April 2025) had already proved a regulatory impossibility theorem nearly a year earlier, with no citation either way. This proves the map between these results is missing.

**Naming and demarcation.** We call this chart the *Governance Impossibility Map*. (i) Unrelated to the design-theory notion of "impossible maps"; (ii) "regulatory impossibility results" is Rao's coinage, used only for his theorem. No abbreviation refers to the map.

## 2. Five Impossibility Domains (Propositions, Sources, Boundary Conditions, Strength)

- **Domain ① — Philosophical (critique-grade):** structural tension between algorithmic closedness and law's demand for determinacy; erupts when governance requires full legal restatement of algorithmic decisions.
- **Domain ② — Explainability / regulatory trilemma (info-theoretic):** Rao (2025, arXiv:2504.20676) — no framework can simultaneously pursue unrestricted capability, human-interpretable explanation, and negligible error. Relax any one to exit.
- **Domain ③ — Determination / two boundaries (theorem-grade):** McCann (2026, arXiv:2604.27292) — by Rice's theorem, semantic-level compliance determination is undecidable for Turing-complete architectures; exit = architectural separation (coterminous governance). Coq-mechanized (454 theorems). Nearest neighbour: Chalupa DIP/DCF (decision-execution axis).
- **Domain ④ — Accountability horizon (theorem-grade):** Tibebu & Shemtaga (2026, arXiv:2604.07778) — beyond the Accountability Horizon × human–AI feedback cycle, the four axioms (Attributability, Foreseeability Bound, Non-Vacuity, Completeness) cannot be jointly satisfied; below threshold, legitimate frameworks exist.
- **Domain ⑤ — Authorization–observation (theorem-grade):** Meyman (2026, Zenodo 19647542) / Fernandez (2026, Zenodo 19669430) / Zhu & Leonard (2026, Applied Sciences 16(10):4917) — observability does not constitute ex-ante authorization; monitoring ≠ permission. Nearest neighbour: L2D lineage (routing action vs institutional state); institutional lineage anchor: advance rulings / declaratory judgment / MDUFA stop-clock.

**Periphery (not mapped):** Palm (2026) folk thesis (no theorem); *On Controllability of AI* (arXiv:2008.04071, 2020) as intellectual precursor of Domain ⑤.

## 3. Method: Integration Map and the Four-Question Test

The nesting map (author synthesis, not consensus) places ① outermost, ② and ③ inside it side by side, ④ overlapping ③ under high autonomy + feedback cycle, and ⑤ beside ③. Three integrative claims: convergent direction / independent routes; nesting is synthesis not consensus; two empirical symptoms of non-citation (② vs ④; the ⑤ trio). The **four-question test** for any governance regime: (1) does it rely on semantic-level determination (③)? (2) does its accountability promise presuppose Completeness (④)? (3) does its transparency promise ignore the information floor of explanation (②)? (4) is its observability sold as authorization capability (⑤)?

## 4. Relation to the Governance Stack

The possibility domain lies outside the five domains. Six asset classes are located: Governance Determinability Doctrine (avoids ③ via discrete declared attributes); LGD-I registered (the only anchor inside ④ — Attributability alone); ACD family (avoids ③, outputs suspension); XCGS evidence chain (Domain ⑤ bounds it, does not bury it — records ≠ verdicts); A³/PCC (institutional feedback outside ④'s boundary); Coexistence doctrine (institutional response to ②); LGD-III gated (theorem-grade endorsement region of ⑤). In the six-layer stack (axiom → institution → evidence → determination → instance → feedback), the Map is the **boundary-constraint layer** — a structural guardrail for the LGD main chain.

## 5. Application: From "Perfect Compliance" to "Debt Management"

Governance's effective output is determination and debt management: (1) make determination points explicit (discrete, decidable attributes; Rules-as-Code); (2) make suspension explicit (ledger entry when criteria/evidence/subject missing — *determination debt* is the sixth sibling of the debt family, the only one pointing at determination itself); (3) make boundaries explicit (state which domain each promise assumes itself outside of).

## 6. Limitations and Honest Boundaries

Nesting is contestable (flagged as synthesis); theorem boundaries may relax (domains shrink, map stands); folk thesis unmapped (no theorem-grade evidence); the map does not negate governance; self-positioning is not circular (map stands independently); naming demarcations upheld; collision sweep zero; **no claim of original theorem, no claim of external citation or adoption (external citations measured at zero)**.

## 7. Conclusion

The effective domain of AI governance has a structural boundary. The Governance Impossibility Map collects five mutually non-citing impossibility results into one navigable coordinate system and supplies a four-question possibility-domain test, converting impossibility literature from a knell into a design constraint.

**Suggested Citation**: Zhao, X. (2026). *The Governance Impossibility Map.* 独立研究线（working paper v0.3）.

---

© 独立研究线 · CC BY 4.0

---

## 落地执行段 · Landing & Execution

### 执行器映射（理论 → 工具）
| 理论构件 | 落地形态 | 锚定参照 |
|---|---|---|
| 五块不可能域 | 治理资产四问自检表 | 域①②③④⑤ 判据 |
| 整合图 | 治理主张定位画布 | 嵌套坐标系 |
| 四问检验 | 治理方案避域审计 | 判定/问责/解释/观测 四问 |
| 判定债务 | 悬置台账 | 治理判定论工作稿 |

### 发布与引用路径
- **仓库**：`lgd-theory/docs/theories/`（随文库发布）；完整工作稿见 `papers/`（中英双语）
- **可发现**：本白皮书与速查页同步入库，供检索与抓取
- **建议引用**：见上方 Suggested Citation

### 如何使用
1. 对任何治理主张，先跑**四问检验**，确认它假设自己不在哪块不可能域；
2. 落地"判定点"而非"语义级审计"、"悬置记账"而非"硬判/放行"；
3. 把不可能域读成设计约束，把资源投向可能域（身份锚定、离散判定、证据复放、债务管理）。

© 独立研究线 · CC BY 4.0