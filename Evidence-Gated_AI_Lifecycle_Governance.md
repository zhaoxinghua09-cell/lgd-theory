# Evidence-Gated AI Lifecycle Governance（证据门禁式 AI 生命周期治理）

> LGD 旗舰「证据+门禁」维度的**官方英文别名**（非独立理论、非独立预印本）。归属既有 lgd-theory Zenodo 记录（10.5281/zenodo.22456647）。

> 英文别名阐述稿 v0.1 · 2026-09-13 · **按 2026-09-13 已锁定决策「不另发独立预印本」**：本稿作为既有 lgd-theory Zenodo 记录（10.5281/zenodo.22456647）的**下一版本并入内容**，而非新建独立预印本。本机网络不可达 Zenodo，元数据已备齐，可达网络一键并入。

**Author:** Zhao, X. (ORCID 0009-0001-0512-1237) · SynomosAI Governance Line
**License:** CC BY 4.0
**Keywords:** AI governance, agent lifecycle, evidence gate, continuous verification, auditability, standard alignment

---

## Abstract (EN)

As autonomous systems (AI agents, intelligent devices, robotic processes) move from
single-shot inference to long-running, stateful operation, the dominant governance
question shifts from *"was this model trustworthy at release?"* to *"is this
particular agent, in its current state, allowed to act now?"*. We present
**Evidence-Gated AI Lifecycle Governance (EG-ALG)** — the official English alias of the
*Lifecycle Governance Doctrine (LGD)* — as a methodology that makes an
*evidence gate* — a verifiable, replayable check on identity, state, and intent —
the **default** control point at every lifecycle transition, rather than an optional
hardening layer. The gate is binary: absent a valid anchor (Registry) and a valid
fingerprint (Evidence), the default outcome is **rejection, not passage**. EG-ALG
is positioned as an *implementation layer (How)* that complements — and does not
compete with — existing frameworks such as ISO/IEC 42001, the EU AI Act, NIST AI
RMF, and the Chinese national guide GB/Z 185—2026 (*Artificial Intelligence —
Interconnection of Agents*, Parts 2–3 on identity codes and identity management).
It is a concrete operationalization of the broader *Lifecycle Governance Doctrine
(LGD)*, whose three laws are Registry, Evidence, and Gates.

## 摘要（中文）

随着自治系统（AI 智能体、智能设备、自动化流程）从单次推理走向长时、有状态运行，治理的核心问题从"模型发布时是否可信"转变为"此刻这个具体智能体是否被允许行动"。本文提出**证据门禁式 AI 生命周期治理（EG-ALG）**：将"证据门禁"——对身份、状态、意图的可验证、可重放检查——作为**每一次生命周期跃迁的默认控制点**，而非可选的加强项。门禁是二元的：缺有效锚点（Registry）或缺有效指纹（Evidence），默认结果为**拒绝而非放行**。EG-ALG 定位为**实现层(How)**，与 ISO/IEC 42001、EU AI Act、NIST AI RMF 以及中国国家标准 GB/Z 185—2026《人工智能 智能体互联》（第2/3部分：身份码与身份管理）**互补而非竞争**，是更广义的"全程治理论（LGD，三律：有籍·有证·有门禁）"的可操作化。

---

## 1. Motivation

Prior identity and governance schemes overwhelmingly judge trustworthiness **at
issuance** (signing time) and rarely recompute it afterward. Yet an agent's memory,
permissions, and behavioral boundary all drift after issuance. *Presuming continued
trust from one-time issuance is unsound.* EG-ALG responds by making continuous
verification the default behavior; passage is the exception, rejection the default.

## 2. Positioning and relationship to standards

EG-ALG explicitly **aligns with** the following frameworks and adds an
implementation layer on top of them:

| Framework | Relationship |
|---|---|
| GB/Z 185—2026 (身份码 / 身份管理) | Built upon; we adopt the identity-code-per-agent and full-lifecycle identity-management framing and supply the *runtime continuous-verification How*. We make **no claim of originality** over identity-code uniqueness, which the standard already covers. |
| ISO/IEC 42001 | AI management-system control objectives; EG-ALG supplies per-transition evidence gates. |
| EU AI Act | Risk-tier obligations; EG-ALG supplies verifiable gate records for conformity evidence. |
| NIST AI RMF | Measure/Mitigate functions; EG-ALG supplies replayable evidence artifacts. |
| LGD (Lifecycle Governance Doctrine) | EG-ALG is the operational layer of LGD's three laws: Registry → Evidence → Gates. |

> **Scope note.** EG-ALG does not propose a new identity-code scheme. It assumes
> an identity anchor exists (per GB/Z 185—2026 or equivalent) and focuses on the
> *runtime* question: *given an anchor, how do we verify, at each action, that the
> agent is still the one authorized, with unaltered state, and intended purpose?*

## 3. The Evidence Gate

An evidence gate `G` is evaluated before each lifecycle transition `T_i → T_{i+1}`:

```
G(agent, T_i, T_{i+1}) =
    valid_anchor(agent)            # Registry: identity code resolvable & unrevoked
 && valid_fingerprint(agent, T_i)  # Evidence: recomputed hash matches last sealed state
 && intent_matches(agent, T_{i+1}) # purpose bound to authorized scope
 && no_downgrade_switch()          # no "skip-verification" kill-switch permitted
```

- **Default = reject.** If any clause is false or unverifiable, the transition is
  blocked. There is no silent fallback to "allow".
- **No degradation switch.** A "skip verification" toggle, once present, is
  inevitably used under operational pressure; therefore EG-ALG forbids such a
  switch. Relaxation is permitted only via a *newly issued authorization*, which
  itself leaves a record.
- **Offline-replayable.** Every gate decision is sealed with the inputs and the
  hash; a third party can recompute the decision from the record alone, without
  trusting the generator.

## 4. Determinations Debt (判定债务)

When a gate cannot be evaluated (anchor missing, fingerprint drift unexplainable,
intent unbounded), the system incurs **Determinations Debt** — a measurable,
accumulating liability that must be discharged (re-anchored, re-evidenced) before
the agent proceeds, or the agent is retired. This makes "cannot verify" a
first-class, accountant-visible state rather than an invisible risk. The concept
underpins the 2026 theme of the self-organized benchmark championship **UIBC**
(Universal Intelligent-agent Benchmark Championship): *Determination of Migration
and Accountability*.

## 5. Conclusion

EG-ALG contributes an implementation-layer methodology — the evidence gate as
default — that is standards-aligned, offline-replayable, and machine-checkable.
It is offered for technical discussion and as a contribution candidate to
standardization venues (e.g., the ITU Focus Group on Trust and Identity for
Humans and Agentic AI) under an *align-and-implement* posture.

---

*英文别名阐述稿（非独立预印本，并入 lgd-theory 既有 DOI 10.5281/zenodo.22456647 的新版本）。Not a standard proposal; not compliance advice. © XLGD · SynomosAI Governance Line.*
