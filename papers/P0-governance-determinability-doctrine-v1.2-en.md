---
title: The Doctrine of Governance Determinability — Theoretical Framework (Working
  Paper v1.2)
type: paper
lang: en
source: P0-governance-determinability-doctrine-v1.2-zh.md
version: v1.2-en
date: 2026-09-24
permalink: //papers/p0-governance-determinability-doctrine-v1.2-en
---

# The Doctrine of Governance Determinability — Theoretical Framework (Working Paper v1.2)

> **The Doctrine of Governance Determinability** — Working Paper v1.2
> SynomosAI Governance Line · 2026-09-08 · Status: internal working paper, unpublished
> Core thesis: **Cannot be determined → cannot be governed.** *What cannot be determined cannot be governed.*
> Project review: completed (see §14); the core body's five items show zero collision; terminology landmines cleared
> Ownership: timestamp and fingerprint are recorded in the package manifest; © SynomosAI Governance Line; copyright and disclaimer at the end
> **v1.1 changes (L2/L4/L5 finalized, 2026-09-08)**: added **§12 Failure Modes and the Quantitative Linkage with Determination Debt** (citing AIDLC-FMEA), **§13 Criterion Validity Period and Spectrum Decay**, **§14 Chinese Reference Network** (fixed citations of Xue Lan / Zhang Qizai / Zheng Ge), and **Appendix A System-wide Falsifiability List** (the full immunity engineering of LGD / XCGS / A³ / Passport / Coexistence Doctrine / RRM); the pre-publication checklist was renumbered to §15.
> **v1.2 changes (evening of 2026-09-08; submission hard-prerequisites R3/R5/R6/R10/R11/R12 all finalized)**: **§0A Adjacent-Term Disambiguation** (four pairs: regulatory debt / mandate suspension / reconstructability / L2D; R3 of the 24th + R10 of the 26th); **§0B Institutional Genealogy Anchor** (advance ruling / declaratory judgment / Abbott Labs 1967, R11); **§6 post-MDUFA clock-stop/start official precedent note** (R12); **§9 added a Rules-as-Code row** (Catala / L4 / defeasible / Hildebrandt, R6); **Appendix B Debt Genealogy "Six Siblings" table** (verification / assurance / compliance / regulatory / technical / determination — determination debt = the sole upstream member, R5); the AI Passport falsifiability row supplemented with a GB/Z 185 alignment positioning note (F3).

---

## 0. One-Page Overview

**In one sentence**: The efficacy bottleneck of AI governance frameworks lies not at the principle layer but at the **determination layer** — when regulatory criteria cannot be formalized to the degree where enterprises and regulators can reach *consistent determinations*, governance can only produce statements, not enforcement.

**Three pillars**: ① the tri-element determination model with four-state output ② the L0–L4 criterion formalizability spectrum ③ determination debt and lifecycle gates.

**Four-layer foundation** (standing on the shoulders of giants, not contending with them):

| Layer | Conclusion | Source |
|---|---|---|
| Philosophical layer | Rules are inherently indeterminate, yet can be made *determinable* through institutional discretion | Kelsen / Hart / Dworkin; Hernandez 2015 |
| Formal layer | For Turing-complete systems, behavioral compliance is machine-undecidable; structured (syntactic determination) can recover decidability | Rice's theorem; McCann 2026 (machine proof) |
| Execution layer | Runtime authorization can be executed deterministically and leaves replayable evidence | FERZ (authorization discipline, three-state adjudication, 5TS) |
| **Regulatory determination layer (this Doctrine)** | **The determinability of regulatory criteria is the first-order constraint on governance efficacy, and can be engineered into a spectrum, procedures, metrics, and instances** | **This Doctrine** |

**Theoretical stack**: LGD (lifecycle skeleton) → Governance Determinability Doctrine (determination core) → ACD family (determination instances, ACD-MD for medical devices first) → XCGS (evidence-chain base).

## 0A. Adjacent-Term Disambiguation (added in v1.2 · R3/R10 · guarding against keyword-mismatch leakage)

> Per Lesson One from §6.4 of the 22nd entry: nearest-neighbor frameworks often use different word roots (they use "Demonstrability," we use "Determinability"), so keyword-level search misses them — hence the explicit disambiguation of four neighbor pairs.

| Neighbor | Proposed by | Surface isomorphism with this Doctrine | Substantive difference (boundary sentence) |
|---|---|---|---|
| **regulatory debt** | medical-device jargon (Odelle / LinkedIn, 2026) | both are "debt" | it is **regulatory-action arrears** (should-have-filed-but-didn't); determination debt is **determination-ontology arrears** (should-have-determined-but-didn't) — the former is one downstream consequence of the latter |
| **Mandate Suspension** | Chalupa DIP framework's seven failure modes (2026) | both contain the "suspension" root | it refers to **organizational authorization being suspended** (who is empowered to act changes); this Doctrine's suspension refers to **the determination procedure being paused pending determination** (the regulatory characterization question has no answer yet) — the former is a permission event, the latter a determination state |
| **Reconstructability** | Chalupa (2026, Zenodo) | both require "independently reconstructable" | the English term is occupied by him; this Doctrine retains the Chinese "replayable" + the L0–L4 formalizability spectrum (he has no spectrum, no metrics) — semantically neighboring, the spectrum is ours alone |
| **Learning to Defer (L2D)** | Chow 1957 → Madras 2018 → Mozannar & Sontag 2020 → Oxford review 2025-12 | both are "when AI is uncertain, hand it to a human" | L2D is a **per-prediction routing action** (statistical learning objective, no institutional semantics); this Doctrine's suspension is an **institutional state** — with ledger fields (suspended_reason / debt_aging / retrigger_condition), an audit chain, and M1–M6 metrics. In one sentence: **L2D answers "route to whom"; suspension answers "who is responsible during suspension, how much debt has accrued, and when to restart"** |

**Overall acknowledgment and boundary-setting with Chalupa**: his Decision Demonstrability framework has argued that the three criteria of auditability / interpretability / compliance are necessary but insufficient, and has given seven classes of organizational failure modes — **he diagnoses the pathology of decision-identity failure (the decision-execution center); this Doctrine supplies the determination-procedure solution (the determination center)**: the L0–L4 spectrum, four-state output, determination debt, and M1–M6 metrics, plus jurisdiction mapping, are all absent from his work. Complementary and mutually cited, not competing.

## 0B. Institutional Genealogy Anchor (added in v1.2 · R11 · the historical depth of "determination front-loading")

"Doing determination before execution" is a mature family of institutions in administrative and trade law; this Doctrine is a mapping of it onto AI regulatory determination, not an invention from nothing:

- **advance ruling (binding ruling)**: institutionalized by the WTO Agreement on Trade Facilitation; U.S. CBP binding rulings — issue binding determinations in advance on the regulatory characterization of "future conduct";
- **declaratory judgment**: 28 U.S.C. §2201; *Abbott Labs v. Gardner* (1967) established "pre-enforcement review" — authoritative characterization can be obtained without final enforcement;
- **FDA Pre-Sub / Q-Submission**: MDUFA VI added the Focused Follow-Up Pre-Submission (45-day written response) — the existing medical-device mechanism for regulatory-determination front-loading.

**Positioning**: the Determinability Doctrine formalizes this "determination front-loading" institutional logic into the criterion spectrum (§4) and lifecycle determination points (§8) — institutional practice preceded theoretical naming; what theory adds is the three-layer mechanism of determinability grading, suspension bookkeeping, and cross-jurisdiction divergence.

---

## 1. Why "Systematization" Is the Competitive Position Itself

None of the four postures of highly-cited works (inventory / critique / operationalization / integration) is "proposing new principles" — the Determinability Doctrine does not make the Nth principle framework, but does *operational + integrative*: integrating the conclusions of the three-layer foundation into a measurable, testable, instantiable determination-layer theory. Compared with nearest neighbors on degree of systematization:

| Predecessor | Form | Has | Lacks |
|---|---|---|---|
| FERZ deterministic governance | product + white paper + standard | five-dimensional model, three-state adjudication, replayable evidence, institutional governance theory (authorization discipline) | regulatory criterion layer, criterion spectrum, debt metrics, cross-jurisdiction, China, lifecycle welding |
| McCann formal governance | machine-proof paper | decidability boundary, co-terminal governance | regulatory scenarios, institutional landing, metrics, instances |
| legal determinability | theoretical tradition | philosophical argument, automatable-boundary thought | any engineering: no spectrum, no procedure, no metrics |
| closure-gap review | academic review | gap identification and classification | gap stock measurement and elimination mechanism |
| government compliance questionnaire (e.g., Amsterdam) | L1 tool | usable triage | theorization, clause provenance, cross-jurisdiction, debt bookkeeping |

**This Doctrine fills exactly the rightmost column of this table.**

---

## 2. Terms and Definitions (D1–D10)

- **D1 Governance object**: an AI system that has entered the regulatory field of view, or one of its changes.
- **D2 Determination**: a regulatory characterization act performed on a governance object by an explicit subject, based on criteria with formalization degree ≥ L1 and complete evidence. Distinguished from FERZ's runtime authorization (action authorization): authorization answers "can this action be executed now," while determination answers "what is this object / change, in regulatory terms."
- **D3 Criterion**: the rule set on which a determination is based, graded by formalization degree into L0–L4 (§4).
- **D4 Evidence**: an archivable, replayable factual record; one of the inputs to determination.
- **D5 Determination subject**: the natural or legal person responsible for the determination result (P6: cannot be outsourced to an algorithm).
- **D6 Determination point**: a position in the lifecycle where a determination must occur (a state-transition point).
- **D7 Suspension (undetermined)**: the **explicit** determination result when any one of criterion, evidence, or subject is missing.
- **D8 Determination debt**: the stock of governance requirements that have been declared but do not yet meet determination conditions (the accumulation of suspended entries). An original concept of this Doctrine, providing a stock metric for the closure gap. **Translation discipline: the English is fixed as `determination debt`, never rendered `judgment-debt` (that term has been named by others, behavioral-science perspective, different conceptual space) or `decision debt` (software-engineering discourse).**
- **D9 Determination drift**: the phenomenon where the same criterion yields inconsistent determinations at different times or in different jurisdictions.
- **D10 Replay**: a third party reproducing the same determination result with the same evidence and criteria (the operationalization of A4).

---

## 3. Axioms (A1–A4)

- **A1 Determination-Driven Law**: every actual regulatory action in a governance system is driven by some explicit or implicit determination; there is no governance action without a determination.
- **A2 Tri-Element Law**: a determination is valid only when criterion, evidence, and subject are all present; if any is missing, the result must be suspension.
- **A3 Maintenance Law**: determinability decays as system complexity and change frequency grow, and must be continuously maintained; there is no once-and-for-all determination system.
- **A4 Replay Law**: the public credibility of governance is proportional to the replayability of its determinations.

> A1 responds to the "vacant principles" phenomenon: principles are vacant precisely because the determination step is missing between principle and action. A2 is the minimal set for engineering. A3 explains why determination systems rot and why a dashboard is needed. A4 connects with the legal tradition that "authority comes from publicly justifiable reasons," and corroborates FERZ's replay discipline (but it covers single-point authorization, whereas this Doctrine covers the full lifecycle).

---

## 4. Criterion Formalizability Spectrum (L0–L4, the core organizing framework of this Doctrine)

| Tier | Name | Criterion form | Determination method | Instance | Human-discretion share |
|---|---|---|---|---|---|
| **L0** | Declaration | principles, slogans ("be responsible") | undecidable — can only be restated | most ethics declarations | 100% |
| **L1** | Checklist | checklists, yes/no questionnaires | manual determination, no clause provenance | MDCG 2020-3 chart; Amsterdam AI Act questionnaire | high |
| **L2** | Rule | discrete-attribute rule table (input → characterization → action → clause provenance) | semi-automatic, human confirmation | **NMPA's two-fold algorithm-change classification + safety levels A/B/C** (ACD-MD domain package) | medium |
| **L3** | Code | rules-as-code, machine-executable | automatic determination + audit | sota.io's Art. 83 determination implementation; OECD government-side Rules as Code | low |
| **L4** | Proof | formal verification, machine-provable | proof is determination | McCann-style machine proof (Theorem 454) | approaching zero |

**Legal provenance**: Krištofík (2024) has argued that the indeterminacy of legal language delimits the boundary of the automatable region — this spectrum is an **operational upgrade** of his thought: from a boundary proposition of "where automation is impossible" to an engineering spectrum of "which tier is decidable, at what cost, and how to choose."

**Formalization defense**: McCann proves that semantic-level determination is undecidable for Turing-complete systems, while structured determination can recover decidability — this is exactly the theoretical basis for why L2/L3 are feasible: regulatory determination does not determine arbitrary program semantics, but only determines **discrete declared attributes** (update type, performance comparison, safety level), the latter inherently falling within the decidability boundary.

---

## 5. Determination Procedure and Four-State Output

```
Determination function: D(x) = Subject(D5) × Criterion(D3, L≥1) × Evidence(D4, complete) → {Admit, Conditional Admit, Prohibit, Suspend}
```

- **Admit / Prohibit / Conditional Admit**: of the same family as the AEGIS domain four-category and FERZ three-state adjudication; this Doctrine gives the domain-independent general form and notes the provenance.
- **Suspend (D7) is the original increment of this Doctrine**: when the criterion is not formalized, evidence is incomplete, or the subject is absent, determination **does not guess, does not delay, does not silently pass** — instead it explicitly outputs suspension, records the missing element, and **books it into determination debt**.
- The three exits from suspension: supplement evidence → re-determine; raise the criterion tier (L0→L2) → re-determine; rule in transit (see M6) → hold and set a retrigger condition.

**Explicit boundary with FERZ**: ALLOW/DENY/ABSTAIN are the three runtime-authorization states (execution layer); this Doctrine's four states are regulatory-characterization determinations (regulatory determination layer). ABSTAIN blocks execution awaiting human override; suspension blocks no execution — it **keeps the books for the regulatory rule system** — these are two different layers that need each other.

---

## 6. Metrics (making the theory testable, comparable, rankable)

| # | Metric | Definition | Use |
|---|---|---|---|
| M1 | Determination coverage rate | determination points set / determination points that should be set | governance-system completeness |
| M2 | Debt stock | number of suspended entries and their aging distribution | quantification of the closure gap |
| M3 | Replay completeness rate | replayable determinations / all determinations | public credibility (operationalization of A4) |
| M4 | Average determination latency | change occurs → determination complete | governance friction |
| M5 | Cross-jurisdiction divergence count | number of jurisdiction pairs triggered into divergent determinations by the same change | explicit divergence management |
| M6 | In-transit change exposure | number of determination points covered by announced-but-not-yet-effective rules | rules-change risk management |

**Core assertion**: the strength comparison between two governance systems = a combination of M1–M6, not the number of principles or the quality of wording. This makes governance maturity, for the first time, measurable, rankable, and regressible like a performance metric.

**Official-precedent note (added in v1.2 · R12)**: the semantics of the M-series metrics have a regulatory official precedent — in the **MDUFA V dual-clock system** (FDA days vs. Total Time to Decision, 112 days), the "deficiency letter stops the clock, applicant response restarts it" is the official version of "suspension + aging" accounting (semantically isomorphic to M2/M4); about 70% of 510(k) first-round submissions receive a deficiency letter — **suspension is the norm, not the exception**; the MDUFA VI draft (FY2028–2032, published for comment 2026-07) adds a "Not Grantable" letter (75–90 day final-determination window) as an institutional precedent for output states. This Doctrine ports this regulator-side accounting semantics to the **enterprise side + suspension side**; P3 backtest data can be directly benchmarked against the MDUFA official report caliber (citation claims no naming credit).

---

## 7. Core Propositions (P1–P6, with falsifiability conditions)

- **P1 Main Proposition**: cannot be determined → cannot be governed. Upper bound of governance efficacy = determination efficacy.
  *Falsifiable*: if some regulated domain is found to run stably long-term with zero determination points yet withstands audit, P1 is constrained.
- **P2 Suspension-is-Debt**: the main form of governance failure is not "no principles," but the accumulation of determination debt — the closure gap between statement and execution is the debt stock.
  *Falsifiable*: if gap size is uncorrelated with the debt metric.
- **P3 Front-Loading Law**: the closer the determination point is to the change source, the lower the total governance cost. Determining at change time is better than at annual-report time, better than after an incident.
  *Falsifiable*: if systematic counterexamples exist (post-hoc determination has lower total cost and is replayable).
- **P4 Tiering Law**: the optimal criterion tier is determined by `change frequency × violation cost` — high-cost low-frequency (medical devices, finance) merit L2–L3; high-frequency low-cost (content moderation) rationally stays at L1. Forcing global L3 is over-governance; tolerating global L0 is a governance liability.
  *Falsifiable*: if optimal tier is uncorrelated with the frequency-cost product.
- **P5 Divergence Law**: cross-jurisdiction criterion divergence cannot be eliminated (threefold difference of legal status / governance subject / risk composition — see existing mapping research which has proven that mapping flattens differences), it can only be explicitly managed — the metric is M5.
  *Falsifiable*: if a cross-jurisdiction zero-divergence criterion set appears and is sustainable.
- **P6 Subject Law**: determination responsibility cannot be outsourced to an algorithm. AI may generate determination drafts, but the subject must confirm manually (case law already supports defeats of black-box algorithmic decisions; regulation requires a human in the loop).
  *Falsifiable*: if some jurisdiction explicitly waives the enterprise's manual-confirmation obligation and permits algorithmic self-characterization.

---

## 8. Welding with LGD: Lifecycle Gate State Machine (LGD formalization, amplified and landed)

The three laws of LGD (Lifecycle Governance Doctrine) gain a formalization vehicle in the Determinability Doctrine — each law corresponds to a class of constraint in the state machine:

| Lifecycle stage | Determination point (D6) | LGD law | Required evidence artifact (D4) | Determination output |
|---|---|---|---|---|
| Planning / initiation | classification characterization | **LGD-I Registered** (object anchorable) | intended-use statement, risk grading | Admit (with constraints) |
| Registration / filing | market-path | LGD-I + LGD-II | registration dossier, clinical evidence | Admit |
| Deployment | launch gate | **LGD-III Gated** | verification report, release record | Admit / Prohibit |
| **Change** (core) | materiality characterization | LGD-II (replayable evidence) | change list, performance comparison, impact assessment | **all four states open** (ACD's home field) |
| Monitoring | periodic re-determination | LGD-II + A3 Maintenance Law | real-world data, audit record | Conditional Admit / Suspend |
| De-listing | exit determination | LGD-I (deregister) | de-listing notice, user notification | Admit |

**Restatement of the three laws in determinability terms**:
- LGD-I Registered = the determination object is anchorable (the object precondition of A2; echoes the formal-layer conclusion that "the governance boundary must equal the capability boundary")
- LGD-II Evidenced = the determination is replayable (full-lifecycle instantiation of A4)
- LGD-III Gated = the determination point is institutionalized (the landed form of P1)

**No one has made this table for an evidence-gated lifecycle**: IMDRF N90 is a regulatory framework (not a theory), Bentley is a single-scenario IoT paper (no determination layer), FERZ 5TS is single-point authorization testing (not a full-lifecycle state machine). This table is the amplification of LGD.

---

## 9. Systematic Comparison with Predecessors (honest boundary-setting · acknowledgment list)

| Predecessor | What it contributes | This Doctrine's increment |
|---|---|---|
| Kelsen / Hart / Dworkin; Hernandez 2015 | indeterminate yet determinable through institutional discretion | engineers the philosophical proposition into a spectrum and procedure |
| Krištofík 2024 | legal-language indeterminacy delimits the algorithmizable boundary | L0–L4 operational spectrum + optimal-tier selection law (P4) |
| Critical school (Springer 2019; IJSL 2025 "Against Algorithmic Clarity") | tension between algorithmic closure vs. legal openness | gives an engineering response: the suspended state preserves openness, L2 rules do not cancel discretion (P6) |
| Rice's theorem; McCann 2026 (2604.27292 / 2605.01030) | semantic determination undecidable; structured recovers decidability | the regulatory-layer counterpart of the formal-layer conclusion: determine discrete declared attributes, not program semantics |
| FERZ (authorization discipline, 5TS, three-state adjudication, replayable evidence) | deterministic authorization at the execution layer | regulatory determination-layer theory; determination debt; cross-jurisdiction divergence; lifecycle welding |
| arXiv 2604.19818 (closure gap) | gap identification and four-layer framework | gap stock measurement (M2 debt) and elimination mechanism (suspension exit) |
| AEGIS (arXiv 2603.22322) | medical-device AI change four-category and filing guidance | domain-independent determination procedure + China anchor (AEGIS covers US+EU only) |
| IMDRF N90 / FDA PCCP / NMPA criteria | regulator-native criteria | spectrum positioning of criteria (mostly L1–L2) and engineering encapsulation (ACD domain package) |
| OECD Rules as Code | government-side rule encoding | enterprise-side mirror: the regulated party's determination engineering |
| **Rules-as-Code determinability system** (Catala / L4 / defeasible reasoning / Hildebrandt critique) | legal and engineering foundation of rules-as-code | the academic foundation of this Doctrine's L2/L3 tiers (v1.2 · R6): the feasible boundary and critique of legal automation have been systematized; this Doctrine adds the regulatory-determination-side **tier-selection law (P4), suspension bookkeeping, and debt metrics** |
| **Meyman / FERZ Impossibility Theorem** (observation ≠ prior authorization, 2026) | structural limit at the authorization-observation layer (domain ⑤, theorem-level) | theorem-level endorsement of LGD-III's explicit gate (v1.2): a monitoring stack produces no authorization artifact → the gate must be institutionalized determination, not a telemetry dashboard |

**Citation-network discipline**: the reference lists of the P-series papers must cover all nine rows of the table above (highly-cited coordinates + 2026 frontier + critics), each abstract carrying one of their keywords once; terminology discipline: *determination* ≠ *determinism*; acknowledge first, then assert.

---

## 10. Instantiation and Backtesting Protocol

- **ACD-MD (NMPA algorithm-change determiner) = the first complete instance of this Doctrine**: takes seven discrete attributes as input (update type / whether the core algorithm changed / whether the training set was deprecated / statistical performance comparison / software safety level A/B/C / scope-of-use change / whether self-learning is involved), outputs a four-state characterization + clinical-evaluation path + clause-by-clause provenance + archivable determination record. Corresponds to spectrum tier L2, with the determination point located at the "Change" row (§8).
- **Backtesting protocol**: replay the determination on N publicly available NMPA / FDA change cases, reporting agreement rate, suspension rate, and divergence count (M3/M2/M5) — the backtest report itself is the core evidence of the P3 operational paper.
- **Migration prediction (falsifiable)**: automotive OTA (the four-tier grading of Document No. 45) and generative-AI filing (material-change determination) can construct isomorphic L2 domain packages (the second and third ACD-family instances); if some domain cannot supply L2 criteria, that is boundary evidence for the P4 tiering law in that domain — the way the theory fails is also defined in advance.

---

## 11. Theoretical Boundaries

1. This Doctrine handles **feasibility** (can it be determined), not **legitimacy** (should it be regulated); value judgment remains with the human subject (P6).
2. This Doctrine does not replace principle frameworks, but gives the **conditions under which principle frameworks can be executed** — the principle layer and the determination layer are complementary.
3. The suspended state preserves the openness of legal concepts (responding to the "algorithmic clarity" critique): L2 rules do not cancel discretion, but make discretion occur at clearly defined suspension exits.
4. The China scenario is the first complete instance of this Doctrine, not the only scenario; the spectrum, debt, and metrics are all jurisdiction-independent.

---

## 12. Failure Modes and the Quantitative Linkage with Determination Debt (added in v1.1)

**Acknowledgment and boundary-setting**: AIDLC-FMEA (He, Pan, Chu, IEEE Access 2026, 14: 94251–94275, DOI 10.1109/ACCESS.2026.3701925) has extended FMEA to the full lifecycle of AI governance and proposed the Extended Governance Risk Priority Number (eGRPN) — **the pit of failure-mode classification and risk-priority number belongs to it**. The increment of this section is a different matter: **how failure modes map onto the four-state determination output and determination debt**, i.e., giving failure modes a "determinability restatement" and a detectable debt signal.

| Failure mode (determinability restatement) | Behavior on the four states | Debt behavior | Detection signal (linked to M-series) |
|---|---|---|---|
| Vacant principles | criterion stuck at L0/L1 but used as if L2; determination replaced by "compliance statement" | debt accumulates **invisibly** (no suspension record) | M1 coverage audit: determination points that should be set vs. actually set |
| Compliance theater | suspension disguised as admit | illusion of zero debt on the books | M3 replay spot-check: can sampled determinations be replayed |
| Criterion drift (D9) | same criterion yields inconsistent output across time/jurisdiction | debt-aging calibers confused, cross-system incomparable | M5 cross-jurisdiction divergence count |
| Gate corruption | determination point exists but never triggers long-term | suspension held indefinitely, debt booked interest-free | M2 aging distribution: long-tail entries |
| Blind running on in-transit rules | announced-but-not-yet-effective rules treated as current criteria | determinations need batch rework (exposure realized) | M6 in-transit change exposure |

**Core assertion (falsifiable)**: a failure mode with a high eGRPN score must, under the four-state framework, manifest as at least one abnormal debt signal (one of M1/M2/M3/M5/M6); if a high-eGRPN failure mode shows completely no anomaly on the four states and debt metrics, this section's mapping is invalid. **eGRPN measures the "risk-priority number"; this section measures the "debt state" — the two metric sets are complementary; joint regression is welcome.**

---

## 13. Criterion Validity Period and Spectrum Decay (added in v1.1)

"Governance entropy / regulatory entropy" as a metaphor has been used by multiple parties (network-science papers, consulting commentary); this Doctrine invents no new theoretical term, and does only one thing: **give an operationalization table of decay mechanism, magnitude, and detection signal for each tier's criteria from L0 to L4** — the landed form of the A3 Maintenance Law of this Doctrine (determinability decays with complexity and change frequency).

| Tier | Typical decay mechanism | Half-life magnitude | Detection signal | Re-determination trigger |
|---|---|---|---|---|
| L0 Declaration | wording drift from public opinion and leadership turnover | monthly | change in official phrasing | wording comparison |
| L1 Checklist | guideline version update | yearly | MDCG / guidance revision | version diff |
| L2 Rule | supporting细则 taking effect changes the rule table | quarterly | announcement + supporting-document release rhythm (e.g., the style of Announcement No. 63) | M6 exposure clearance / addition |
| L3 Code | rule-table change out of sync with code | controllable | code-repository diff | CI regression |
| L4 Proof | proven system architecture refactored | longest | system-refactoring event | re-prove |

**Core assertion (falsifiable)**: the higher the criterion tier, the lower the empirical decay rate (higher maintenance cost, stronger drift resistance); if regulatory evidence shows the reverse (L2 fails more easily than L0), the tiering law P4 needs revision. **Relation to M6**: in-transit change exposure is exactly the "announced-but-not-yet-effective" part of L2-tier decay — GMP Announcement No. 107 (effective 2026-11-01) is a ready-made empirical case: the determination output for the same input switches around the effective date, and the exposure-clearance event can be recorded.

---

## 14. Chinese Reference Network (added in v1.1 · L4 landed)

The fixed three-scholar citation trio for this Doctrine's Chinese materials (embedded in the P2 short paper, carried by the P4 white paper and all Chinese-version materials; the citation-positioning language is fixed and does not claim framework replacement):

| Scholar | Work / project | Fixed citation-positioning language |
|---|---|---|
| **Xue Lan** (Tsinghua CISS) | *AI Governance in a Global Perspective* (Digital Economy Development and Governance, 2026, Issue 1): three tiers × three functions | General framework of Chinese governance theory; **this Doctrine = the determination-layer deepening of its "regulation and standards" dimension** |
| **Zhang Qizai** (Chinese Academy of Social Sciences) | *Enterprise Economy* 2026(02); the CASS major innovation project "Research on the Theory, Methods, and Pathways of AI Governance and Regulatory Institution Building" (five dimensions), launched 2026-07-28 | a national-level theory project just launched; among its five dimensions the **"methods and tools" layer has no determination formalization yet** — this Doctrine stakes out that layer, used as a nationally-endorsed citation |
| **Zheng Ge** (Shanghai Jiao Tong University Koguan Law School) | *Politics and Law Review* 2026(04): "separation of evaluation from construction" | **he addresses "who determines" (subject institution); this Doctrine addresses "how to determine" (determination procedure)** — complementary and mutually cited, composing a complete determination-institution theory |

**Discipline**: ① the three scholars' citations enter the reference lists of P2/P4/all Chinese-version materials (Zheng Ge already embedded in the main text on the 17th); ② the positioning language must not be written as "remedying X's deficiency," uniformly using "deepening / procedural completion / complementarity"; ③ before submission to the Chinese first-publishing journal (J4, TBD), re-check document numbers and issue numbers per the journal format.

---

## Appendix A · System-wide Falsifiability List (added in v1.1 · L2 landed)

> The Determinability Doctrine already has the P1–P6 falsifiability conditions (§7); this list fills in the remaining assets within the system — a falsifiability condition ≠ an admission of fragility, it is the entry ticket to immunity.

| Asset | Falsifiability condition |
|---|---|
| **LGD-I Registered** | if ≥5 regulated AI systems appear that, across the full lifecycle, have unanchorable identities (no registration/filing anchor at all) yet still achieve full-lifecycle accountability recovery as mature cases, then "Registered is a precondition of lifecycle governance" is falsified |
| **LGD-II Evidenced** | if some regulatory jurisdiction, without any impact-assessment evidence-archiving requirement, maintains major-change determinations with zero dispute for over ten years, then "Evidenced is a precondition of determination replayability" is falsified |
| **LGD-III Gated** | if, under the FDA PCCP + NMPA two-fold system, the measured major-change miss-determination rate is <1% with no remediation need, then "explicit gate优于 post-hoc review" is falsified |
| **XCGS evidence-chain base** | if cases exist that, after full-chain audit, still cannot replay the key determination process (≥3 cases, spanning 2 domains), then the sufficiency of the "evidence-chain base" is falsified |
| **A³ / PCC (Progenitor Constraint)** | if "three-zero" cases appear where AI progeny cause harm yet the progenitor has zero liability obligation, the market has zero negative pricing, and regulation has zero pursuit, then the necessity of the constraint is falsified |
| **AI Passport (passport model)** | if some jurisdiction adopts replicable/transferable agent-identity credentials and runs them long-term without responsibility-attribution confusion (the "single-identity anchoring" is proven unnecessary), then the institutional necessity of the passport model is constrained. **Positioning note (v1.2 · F3)**: within China, the agent-identity anchoring function is already carried by the GB/Z 185—2026 series of national standards; for this jurisdiction this asset shifts to an alignment-and-audit complementary posture, and no longer claims origination |
| **Coexistence Doctrine** | if the error rate of verifiable human-machine joint determination is higher than human-alone determination in **all** controlled experiments, then the core prediction of "complementary coexistence" is falsified |
| **RRM (Reality Reference Method)** | a single instantiation failure does not falsify (domain difference is a method precondition); if **three consecutive** cross-domain instantiations all fail to find a usable reference model, then the portability claim is constrained |

## Appendix B · Debt Genealogy "Six Siblings" Table (added in v1.2 · R5 · guarding against metaphor misuse + repurposing as a citation asset)

> When determination debt is cited externally, **this table must** accompany the disambiguation (the 25th: the debt-metaphor family has been occupied by multiple domains; keyword mismatch is the most dangerous leakage).

| Debt | Occupant | Points to | Relation to determination debt |
|---|---|---|---|
| technical debt | software-engineering classic (from 1992) | future cost of structural shortcuts | the eldest sibling, metaphor source |
| **verification debt** | CACM (2026) + arXiv 2026 (AI-assisted development iteration scenarios, 3 title-level hits all 2026) | the evidence gap between published and proven (generation faster than verification) | sibling: evidence-side arrears |
| **assurance debt** | Frontiers paper (assurance by design) | cumulative cost of not designing assurance upfront, remediated afterward | sibling: assurance-side arrears |
| **compliance debt** | Kovr + Gartner compliance-as-code context (incl. Compliance Debt Ratio metric) | cumulative burden of manual compliance vs. automation | sibling: action-side arrears |
| regulatory debt | Odelle / LinkedIn (medical-device jargon, disambiguated on the 24th) | regulatory-action arrears | already disambiguated: action-side |
| **determination debt** | **this Doctrine** (0-occupancy maintained, triple independently confirmed) | **suspended-undecided determination-ontology arrears** | **the family's only member pointing at "determination" itself, the upstream cause**: determination suspension → subsequent verification/assurance/compliance actions lose their anchor |

**External positioning-language template (fixed)**: "verification debt is evidence arrears, compliance debt is action arrears — determination debt is their **upstream cause**: the determination itself that should have been made but wasn't. AI generation outpacing verification (CACM) and AI iteration outpacing determination (this Doctrine) are the two ends of an isomorphic phenomenon."

---

## 15. Pre-Publication Checklist

☐ Final naming check (Chinese main name "治理判定论" + English "The Doctrine of Governance Determinability"; **GDD abbreviation deprecated**; final targeted de-duplication round before publication)
☐ Citation-network completeness (§9 eleven rows fully covered + §14 Chinese three-scholar fixed citations)
☐ v1.2 new-item review (§0A four-pair disambiguation / §0B institutional genealogy anchor / §6 MDUFA note / §9 two rows / Appendix B debt-genealogy table / AI Passport positioning note)
☐ v1.1 new-item review (§12 AIDLC-FMEA boundary sentence / §13 decay table / Appendix A eight-asset falsifiability conditions complete)
☐ Terminology-discipline self-check (no "deterministic governance" used as our own; determination/determinability consistent; determination-debt citation always attaches Appendix B)
☐ Sensitivity scan (real names / emails / accounts / local paths — 0 hits)
☐ Ownership five-piece set (timestamp + fingerprint, with package manifest)
☐ External actions confirmed one by one (arXiv / Zenodo / ITU submissions are all external actions)

---

## 16. Submission-Ready Addendum (Submission-ready Addendum · v1.2)

> This section is roughly equivalent to the English-state and naming-gate consolidation piece of the "submission package." The main text is a Chinese working paper; when submitting externally (Zenodo / SSRN / journal), use this section's English title / Abstract / Keywords as metadata, and the main text may attach the full Chinese text or a separate English version (external action, confirmed one by one).

### 16.1 English Title and Authorship

- **Title (EN)**: *The Doctrine of Governance Determinability: Why What Cannot Be Determined Cannot Be Governed*
- **Subtitle (CN)**: 治理判定论 · 理论纲要（工作稿 v1.2）
- **Author**: Zhao, Xinghua (Steven Zhao) — ORCID 0009-0001-0512-1237
- **Affiliation (brand)**: SynomosAI Governance Line
- **Stable URL**: `https://github.com/zhaoxinghua09-cell/lgd-theory` → `papers/P0-governance-determinability-doctrine-v1.2-zh.md` (obtains a new version of the Zenodo concept DOI 10.5281/zenodo.22456647 with the lgd-theory release)
- **TID**: TH-META-011 (finalized 2026-09-10; GDD abbreviation deprecated)

### 16.2 Abstract (EN, ~150 words)

> The efficacy bottleneck of AI governance frameworks lies not at the principle layer but at the **determination layer**: when regulatory criteria cannot be formalized to a degree where enterprises and regulators can reach *consistent determinations*, governance produces statements but not enforcements. This working paper proposes the **Doctrine of Governance Determinability** — its core thesis: *what cannot be determined cannot be governed*. Built on three pillars (the tri-element determination model with four-state output; the L0–L4 formalizability spectrum; determination debt and lifecycle gates), the doctrine integrates three prior foundations (legal indeterminacy theory, Rice's theorem on behavioral compliance, FERZ's deterministic governance) and engineeringizes them into a spectrum, a procedure, metrics, and instances. It introduces **determination debt** as the stock metric of suspended determinations, distinguishes it from adjacent "debt" metaphors (verification / assurance / compliance / regulatory), and maps the doctrine onto China's medical-device change-determination instance (ACD-MD). The paper explicitly positions itself as complementary to — not superseding — nearest-neighbor frameworks (Chalupa's Decision Demonstrability, L2D, Rules as Code), and claims no originality over the concept of "determinability" itself.

### 16.3 Keywords (EN)

`AI governance` · `determinability` · `determination debt` · `formalizability spectrum` · `suspended determination` · `lifecycle gate` · `LGD`

### 16.4 How to cite (unified citation format)

> Zhao, X. (2026). *The Doctrine of Governance Determinability: Why What Cannot Be Determined Cannot Be Governed* (Working Paper v1.2, TH-META-011). SynomosAI Governance Line. GitHub: `zhaoxinghua09-cell/lgd-theory`; Zenodo DOI 10.5281/zenodo.22456647. ORCID: 0009-0001-0512-1237.

### 16.5 Naming-Gate Final Checklist (consolidated v3 criteria + M1 translation discipline)

Go through item by item before submission; only submit when all green (citing the 26th's six-round ledger rules):

| # | Check item | Status | Evidence |
|---|---|---|---|
| 1 | Main name `Governance Determinability` / Chinese "治理判定论" — no named theory occupies the same space | ✅ | §14 project-review five items zero collision |
| 2 | GDD abbreviation deprecated across the corpus | ✅ | no GDD abbreviation in full text |
| 3 | Sub-concept `determination debt` (判定债务) English anchor unique, not confused with `judgment-debt` / `decision debt` | ✅ | §15 D8 + Appendix B + M1 report §8 translation discipline |
| 4 | `Adjudication Debt` (裁决债务, TH-META-012) boundary-set from `Value Debt` / `judgment-debt` | ✅ | M1 report §4 + §8 |
| 5 | Not mixed with FERZ `deterministic governance`; no claim of determinability origination | ✅ | §0A / §14 discipline sentences |
| 6 | Citation package six items complete (Chalupa DIP+DCF / debt-genealogy six siblings / Rules as Code / L2D spectrum / institutional genealogy anchor / Chinese three-scholar) | ✅ | §0A / §0B / §9 / §14 / Appendix B |
| 7 | Sensitivity scan (real names / emails / accounts / local paths) 0 hits | ☐ final check before submission |
| 8 | External actions (Zenodo / SSRN / arXiv / ITU) confirmed by the author one by one; AI does not hold credentials | ☐ confirm at submission |

### 16.6 Submission-Channel Memo (external action, not executable in this environment)

- **Zenodo** (preferred for timestamp): direct connection at zenodo.org is a network-layer black hole in this environment (http=000); must be submitted by the author via web page on an internet-capable machine; P2/P5 have verified DOIs can be issued (22669389 / 22668958, state=findable). This draft enters the new version of concept DOI 10.5281/zenodo.22456647 with the lgd-theory release.
- **SSRN** (second choice for grabbing timestamp): registration has no barrier; previously blocked by home-network proxy 502, main channel switched to Zenodo.
- **arXiv cs.CY**: requires domain endorsement (one endorsement permanently valid), one step slower.

---

## Copyright and Disclaimer

© SynomosAI Governance Line (2026). This framework is a working paper, released under the CC BY 4.0 license (reusable with attribution). Provided "AS IS," without any express or implied warranty; the consequences of use are borne by the user. Third-party frameworks, standards, terms, and results cited herein belong to their respective right holders; this paper only makes academic citation and acknowledgment, and citation relations are subject to each right holder's official text.

---

## Appendix C · Terminology Table (术语对照表)

> This table standardizes the Chinese–English terminology used throughout this translation. All English renderings are fixed and applied uniformly; no term was invented beyond the source text's own usage. Where the source already supplied an English term (e.g., *determination debt*, *suspended determination*, *closure gap*), it is retained as canonical.

| # | 中文 (Source) | English (This Translation) | Notes / Scope |
|---|---|---|---|
| 1 | 治理判定论 / 判定论 | Governance Determinability Doctrine / the Doctrine | English title per §16.1; "the Doctrine" used as shorthand for 判定论 |
| 2 | 全程治理 / LGD | Lifecycle Governance (Doctrine) / LGD | LGD = Lifecycle Governance Doctrine |
| 3 | 判定 | determination | core term; ≠ determinism |
| 4 | 治理对象 (D1) | governance object | the AI system / change under regulation |
| 5 | 判据 | criterion / criteria | graded L0–L4 |
| 6 | 证据 (D4) | evidence | archivable, replayable record |
| 7 | 判定主体 (D5) | determination subject | responsible natural/legal person |
| 8 | 判定点 (D6) | determination point | lifecycle state-transition point |
| 9 | 悬置 / undetermined (D7) | suspended determination (undetermined) | explicit result when criterion/evidence/subject missing |
| 10 | 判定债务 (D8) | determination debt | fixed; never "judgment-debt" / "decision debt" |
| 11 | 判定漂移 (D9) | determination drift | inconsistent determination over time/jurisdiction |
| 12 | 复放 (D10) | replay | third-party reproduction of a determination |
| 13 | 公理 A1–A4 | Axioms A1–A4 | — |
| 14 | 判定驱动律 (A1) | Determination-Driven Law | — |
| 15 | 三要素律 (A2) | Tri-Element Law | criterion + evidence + subject |
| 16 | 维护律 (A3) | Maintenance Law | determinability decays, needs upkeep |
| 17 | 复放律 (A4) | Replay Law | credibility ∝ replayability |
| 18 | 判据可形式化谱系 | criterion formalizability spectrum | L0–L4 |
| 19 | L0 声明态 | Declaration tier (L0) | — |
| 20 | L1 清单态 | Checklist tier (L1) | — |
| 21 | L2 规则态 | Rule tier (L2) | — |
| 22 | L3 代码态 | Code tier (L3) | rules-as-code |
| 23 | L4 证明态 | Proof tier (L4) | formal verification |
| 24 | 四态输出 | four-state output | Admit / Conditional Admit / Prohibit / Suspend |
| 25 | 准入 | Admit | — |
| 26 | 条件准入 | Conditional Admit | — |
| 27 | 禁止 | Prohibit | — |
| 28 | 悬置（输出态） | Suspend (Suspended) | the fourth output state |
| 29 | 度量 M1–M6 | Metrics M1–M6 | — |
| 30 | 判定覆盖率 (M1) | determination coverage rate | — |
| 31 | 债务存量 (M2) | debt stock | — |
| 32 | 复放完整率 (M3) | replay completeness rate | — |
| 33 | 平均判定时延 (M4) | average determination latency | — |
| 34 | 跨辖区差量数 (M5) | cross-jurisdiction divergence count | — |
| 35 | 在途变更敞口 (M6) | in-transit change exposure | — |
| 36 | 命题 P1–P6 | Propositions P1–P6 | — |
| 37 | 主命题 (P1) | Main Proposition | cannot be determined → cannot be governed |
| 38 | 悬置即债务 (P2) | "Suspension is debt" | — |
| 39 | 前置化律 (P3) | Front-Loading Law | determine near the change source |
| 40 | 层级律 (P4) | Tiering Law | optimal tier = f(frequency × cost) |
| 41 | 差量律 (P5) | Divergence Law | cross-jurisdiction divergence uneliminable |
| 42 | 主体律 (P6) | Subject (Responsibility) Law | responsibility non-outsourcable |
| 43 | LGD-I 有籍 | LGD-I: Registered (object anchorable) | — |
| 44 | LGD-II 有证 | LGD-II: Evidenced (replayable) | — |
| 45 | LGD-III 有门禁 | LGD-III: Gated (institutionalized gate) | — |
| 46 | 生命周期门禁状态机 | lifecycle gate state machine | — |
| 47 | ACD-MD | Algorithm Change Determiner for Medical Devices (ACD-MD) | NMPA algorithm-change determiner |
| 48 | ACD 家族 | ACD family | determination instances |
| 49 | XCGS 证据链底座 | XCGS evidence-chain foundation | — |
| 50 | A³ / PCC（Progenitor Constraint） | A³ / Progenitor Constraint | — |
| 51 | AI Passport（护照模式） | AI Passport (passport model) | — |
| 52 | 共存论 | Coexistence Doctrine | — |
| 53 | RRM 现实参照法 | RRM (Reality Reference Method) | — |
| 54 | closure gap | closure gap | retained (established term) |
| 55 | eGRPN | Extended Governance Risk Priority Number (eGRPN) | from AIDLC-FMEA |
| 56 | AIDLC-FMEA | AIDLC-FMEA | — |
| 57 | 邻位术语辨析 | adjacent-term disambiguation | §0A |
| 58 | 制度谱系锚 | institutional genealogy anchor | §0B |
| 59 | 监管判定层 | regulatory determination layer | this Doctrine's layer |
| 60 | 执行层 | execution layer | FERZ's layer |
| 61 | 判定前移 | determination front-loading | before-execution determination |
| 62 | advance ruling | advance ruling (binding ruling) | WTO / CBP |
| 63 | declaratory judgment | declaratory judgment | 28 U.S.C. §2201 |
| 64 | 辖区 | jurisdiction | — |
| 65 | 差量 | divergence | — |
| 66 | 账龄 | debt aging | — |
| 67 | 敞口 | exposure | — |
| 68 | 在途 | in-transit / in-flight | announced-not-yet-effective |
| 69 | 原则悬空 | vacant principles (principles left hanging) | principles without determination anchor |
| 70 | 合规表演 | compliance theater | suspension disguised as admit |
| 71 | 门禁腐化 | gate corruption | determination point never triggers |
| 72 | 规则在途盲跑 | blind execution against in-transit rules | — |
| 73 | 治理熵 / regulatory entropy | governance entropy / regulatory entropy | metaphor |
| 74 | 半衰期 | half-life | decay magnitude |
| 75 | 谱系衰变 | spectrum decay | A3 landed form |
| 76 | 评建分离 | separation of evaluation from construction | Zheng Ge |
| 77 | 不可能性定理 | impossibility theorem | Meyman / FERZ |
| 78 | 复放纪律 / 复放证据 | replay discipline / replayable evidence | FERZ |
| 79 | 三态裁决 | three-state adjudication | FERZ ALLOW/DENY/ABSTAIN |
| 80 | 五维模型 | five-dimensional model | FERZ |

---

## § Translator's Note

This English version was translated from the Chinese working paper **P0-governance-determinability-doctrine-v1.2-zh.md** (v1.2, dated 2026-09-08). Translation date: **2026-09-24**.

- **Source basis**: The entire Chinese body (§0 through §16, plus Appendices A/B and the Copyright & Disclaimer section) was translated in full, section by section, with no omission, compression, or summarization. Section numbering, table structures, footnote/block-quote notes, and list hierarchy from the source are preserved.
- **Pre-existing English retained**: The §16.2 Abstract, §16.3 Keywords, and §16.4 How-to-cite paragraphs were already in English in the source and are reused verbatim, per the brief. Where the Chinese body and these English paragraphs differ in detail, the source's own English text is treated as authoritative and self-consistent.
- **Terminology table**: A unified Chinese–English terminology table is provided in **Appendix C** (above), applied consistently throughout. The term *determination debt* is fixed and never rendered as "judgment-debt" or "decision debt," per the source's own translation discipline (D8). The concept of *determinability* is distinct from *determinism* throughout.
- **No external assertions added**: No claim of academic citation, adoption, or endorsement beyond the source was introduced (external-citation status remains as stated in the source: none asserted).
- **No git / no network**: This is a single-file deliverable; no version-control commands were run and no content was published or uploaded.

**Translator's discretionary flags for the author (not changes to content)**:
1. The source contains its own affiliation "SynomosAI Governance Line," author identity, ORCID, GitHub URL, and Zenodo DOI (in §16 and the Copyright section). These were retained faithfully as source content. For blind journal submission the author may wish to redact the affiliation/identity block — this is a submission-policy choice, not a translation change.
2. Public institutional references present in the source (FDA, NMPA, WTO, OECD, IMDRF, CBP, IEEE, Frontiers, CACM, Gartner, Kelsen/Hart/Dworkin, etc.) and the Chinese-reference-network scholars (Xue Lan / Zhang Qizai / Zheng Ge with their institutions) were translated as-is. No new institution, company, or internal code name was added beyond the source.
3. No local absolute paths (D:\ or C:\) appear in the output; the only URL retained is the source's own public GitHub/Zenodo reference.