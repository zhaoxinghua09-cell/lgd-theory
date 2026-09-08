# The Governance Impossibility Map: Five Impossibility Domains in AI Governance and Where the Possibility Domain Begins (Working Paper v0.3, EN)

> SynomosAI Governance Line · Paper Matrix P5 · English working draft (D6), 2026-09-08
> Chinese master version: P5-governance-impossibility-map-v0.3-zh.md (authoritative for content)
> Position: inventory + critique hybrid (the Jobin-style mapping move: no new theorems, only coordinates)
> © SynomosAI (2026). AS IS. Third-party theorems remain the property of their authors; citations follow official texts. Search data as of 2026-09-08.

---

## Abstract

Between 2025 and 2026, AI governance witnessed a dense cluster of impossibility results: the information-theoretic limits of explainability (Rao 2025), the computational limits of behavioural governance (McCann 2026), the axiomatic limits of collective accountability (Tibebu & Shemtaga 2026), the structural impossibility of observation-based ex-ante authorization (Meyman 2026; Fernandez 2026; Zhu & Leonard 2026), and the earlier philosophical critique of algorithmic clarity (2019–2025). These results are scattered across five mutually non-citing literature clusters. Two verifiable symptoms: Tibebu & Shemtaga self-describe as "the first impossibility result in AI governance" although Rao's regulatory impossibility theorem predates theirs by nearly a year, with no citation in either direction; and on the observation-versus-authorization constraint, three groups independently produced theorem-level or formalized arguments within a single half-year, again without cross-citation. Governors thus face not a scarcity of theorems but an absence of coordinates: no one tells them how these results relate, which regions of governance space they close, and which remain open. This paper proves no new theorem. It does three things: (1) states each of five impossibility domains precisely — proposition, source, boundary condition, evidential strength; (2) offers a nesting-and-overlap integration map, explicitly flagged as the authors' synthesis rather than consensus; and (3) locates existing governance assets — including the authors' own — inside the possibility domain, converting impossibility literature from a knell into a design constraint. The map is, to our knowledge, the first integrated chart and the first survey-level treatment of this literature.

**Keywords**: AI governance; impossibility theorem; explainability; undecidability; accountability; ex-ante authorization; determination debt

---

## §1 Introduction: After the Convergence of Principles, the Impossibility Results

Jobin, Ienca and Vayena (2019) charted the convergence of AI-ethics principles across more than two hundred guidelines and became the coordinate system for everything written since: anyone invoking "AI principles" must now say where they stand on that map. This is the proof of value for the *mapping move* — a map adds no new knowledge, but turns existing knowledge into something navigable.

Between 2025 and 2026 a symmetric body of literature appeared: work that no longer asks *how governance should be done* but proves that *certain governance goals cannot be jointly achieved*. Rao (2025) proves a regulatory impossibility theorem from algorithmic information theory. McCann (2026) establishes the two boundaries of behavioural governance via Rice's theorem and a Coq-mechanized development. Tibebu and Shemtaga (2026) prove an accountability-incompleteness theorem by axiomatic means over human–agent collectives. Meyman (2026), Fernandez (2026) and Zhu & Leonard (2026) independently establish, within a single half-year, that observation cannot constitute ex-ante authorization. Earlier and at the periphery sit the philosophical critique of algorithmic clarity (Kalulé 2019; Springer 2019; IJSL 2025) and an industry-level folk thesis (Palm 2026).

The shared predicament of these results is **the absence of coordinates**:

- They appear in different disciplines — information theory, computational theory, formal ethics, science-and-technology studies, authorization architecture — under different names ("regulatory impossibility theorem", "two boundaries", "accountability horizon"), with zero cross-citation.
- A governor who reads any one of them cannot answer three practical questions: is this the same thing as the other paper I read? has my governance regime already stepped into an impossibility domain? and if so, what now?

One checkable detail shows how deep the absence runs: Tibebu and Shemtaga (2026) call their result "the first impossibility result in AI governance," while Rao (submitted 29 April 2025) had already proved a regulatory impossibility theorem nearly a year earlier; neither cites the other. This is not a criticism of either party — distinct research programmes are hard to discover across fields — it is proof that the map between these results is missing. This paper supplies it.

**Naming and demarcation.** We call this chart the **Governance Impossibility Map**. Two demarcations: (i) this paper has nothing to do with the design-theory notion of "impossible maps" — that is a critique of maps as design methodology, whereas this is an integration chart of governance results, stated here at first use; (ii) the phrase "regulatory impossibility results" is Rao's coinage and is used here only to refer to his theorem, never as a general label for this map. No abbreviation is used for the map anywhere in this paper.

---

## §2 Five Impossibility Domains: Proposition, Source, Boundary Condition, Evidential Strength

### 2.1 Domain ① — Philosophical layer: the algorithmic-clarity critique (critique-grade)

- **Proposition**: there is a structural tension between the closedness of algorithmic systems and law's demand for determinacy and transparency; demanding that algorithmic decisions be fully restatable in legal language may be a category error. Representative works: Kalulé (2019); Springer (2019); *Against Algorithmic Clarity* (IJSL 2025).
- **Boundary condition**: the tension erupts when governance requires that algorithmic decisions be completely restatable for legal procedure.
- **Evidential strength**: critique-grade (conceptual argument, no formal theorem).
- **Map position**: outermost ring. It marks an impossibility at the level of *language and concepts*: the complete legal restatement of algorithmic behaviour is itself questionable.

### 2.2 Domain ② — Explainability layer: the regulatory trilemma (information-theoretic grade)

- **Proposition** (Rao 2025, arXiv:2504.20676; v1 2025-04-29, v2 2025-11-03): "explanation" is formalized as a simpler approximation of a model, measured by Kolmogorov complexity. Core results: (i) a complexity-gap theorem — any explanation significantly simpler than the model must differ from it on some inputs; (ii) a **regulatory impossibility theorem**: no governance framework can simultaneously pursue unrestricted AI capabilities, human-interpretable explanations, and negligible error.
- **Boundary condition**: infeasible only when all three goals are pushed to their limits simultaneously; relaxing any one exits the domain.
- **Evidential strength**: information-theoretic grade (formal bounds; exponential/polynomial characterizations for Lipschitz functions).
- **Map position**: middle ring. It marks an impossibility at the level of *information*: explanation, as lossy compression, has a mathematical floor.

### 2.3 Domain ③ — Determination layer: the two boundaries of behavioural governance (theorem-grade)

- **Proposition** (McCann 2026, arXiv:2604.27292; v1 2026-04-30, v3 2026-05-26): every system has two boundaries — expressiveness and governance — independently defined in nearly all deployed systems, yielding three regions: governed capabilities (the only useful region), ungoverned capabilities (risk), and governance addressing non-existent capabilities (theatre). By Rice's theorem (1953), for any Turing-complete architecture, the property "this program's effects comply with the governance policy" is undecidable — behavioural governance fails structurally in the general case. The proposed exit is **coterminous governance**: the two boundaries made provably identical, which requires an *architectural decision* (separating computation from effect) so that governance checks become part of the execution pipeline. Proofs mechanized in Coq (454 theorems, 36 modules, 0 admitted).
- **Boundary condition**: the impossibility is fully realized when governance takes the form of post-hoc, semantic-level adjudication of arbitrary program behaviour.
- **Evidential strength**: theorem-grade (classical computability result + mechanized proof).
- **Map position**: inner ring. It marks an impossibility at the level of *computation*: semantic-level compliance determination is undecidable — unless the architecture changes rather than the governance.
- **Nearest-neighbour demarcation (Chalupa, must-cite)**: Chalupa's Decision Demonstrability and Identity Failure framework (2026–, Zenodo preprint series) and the Decision Closure Framework (committee draft v1.3, 2026-03-20: Continuous Closure, Authority Rebinding, Failure Transition Control) are the nearest neighbour on the *decision-execution axis*. Demarcation: Chalupa answers when a decision may be executed and who holds authority when legitimacy conditions fail; Domain ③ (McCann) answers whether semantic-level determination is computable, and Domain ④ whether responsibility can be allocated. Chalupa offers no determination debt, no formalizability spectrum, no jurisdictional mapping; his FTC (Failure Transition Control) neighbours the authorization semantics of Domain ⑤, and the map places this body of work on the execution side of the ③/⑤ boundary.

### 2.4 Domain ④ — Accountability layer: the accountability horizon (theorem-grade)

- **Proposition** (Tibebu & Shemtaga 2026, arXiv:2604.07778; v1 2026-04-09, v2 2026-06-02): human–agent collectives are formalized as state-policy tuples within a structural causal model; autonomy is a four-dimensional information-theoretic profile (epistemic, executive, evaluative, social). Accountability is axiomatized by four minimal properties: **Attributability** (responsibility requires causal contribution), **Foreseeability Bound** (responsibility cannot exceed predictive capacity), **Non-Vacuity** (at least one agent bears non-trivial responsibility), **Completeness** (all responsibility must be fully allocated). The **accountability-incompleteness theorem**: when compound autonomy exceeds the *Accountability Horizon* and the interaction graph contains a human–AI feedback cycle, no framework can satisfy all four axioms simultaneously; the impossibility is structural — transparency, audits, and oversight cannot resolve it without reducing autonomy. Below the threshold, legitimate frameworks exist: a sharp phase transition. Experiments on 3,000 synthetic collectives show zero violations.
- **Boundary condition**: compound autonomy × human–AI feedback cycle — jointly required; reducing autonomy or breaking the cycle exits the domain.
- **Evidential strength**: theorem-grade (axiomatic proof + large-scale synthetic validation).
- **Map position**: inner ring, responsibility side. It marks an impossibility at the level of *social choice*: responsibility allocation, as a mathematical structure, has an unsatisfiable region.

### 2.5 Domain ⑤ — Authorization–observation layer: observability is not ex-ante authorization (theorem-grade)

- **Proposition** (three independent discoveries, first half of 2026, mutually non-citing — the hardest evidence for coordinate absence):
  - **Meyman 2026** (FERZ research programme, Zenodo 10.5281/zenodo.19647542, v1.3.3 June 2026): no observability architecture can produce an artifact satisfying an ex-ante authorization requirement. Three lemmas: observational signals are causally posterior to the governed system's generation of the candidate action; artifacts derived from observational characterization cannot be independently verified; no composition of observational outputs escapes these constraints. Corollaries: latency independence and intervention independence. Monitoring, guardrails and human-in-the-loop approval may describe, filter or interrupt behaviour, but do not produce the pre-execution authorization artifact.
  - **Fernandez 2026** (Agent Governance Series, Zenodo 10.5281/zenodo.19669430 et seq.): attestation is **necessary but never sufficient** — integrity and coverage must be separated; attestation proves trust in measurement, not completeness of execution-relevant reality (two theorems, three corollaries, 100k-step experiments).
  - **Zhu & Leonard 2026** (Applied Sciences 16(10):4917, 2026-05-14): under a fixed information structure, deployment feasibility splits into three regimes — and **perfect post-deployment monitoring cannot resolve ambiguity intrinsic to the observation structure**, because the monitor shares the very signals that generate the ambiguity.
- **Boundary condition**: fully realized when governance mistakes observational capability for authorization capability; exit by making authorization an independent pre-execution verdict rather than an observational derivative.
- **Evidential strength**: theorem-grade (formal lemmas/theorems + experimental validation; the MDPI version peer-reviewed).
- **Map position**: inner ring, execution side, complementary to Domain ③ — Domain ③ says semantic-level compliance determination is undecidable; Domain ⑤ says retrospective observation does not constitute ex-ante authorization. Together they prohibit the governance illusion of *substituting a bolted-on observability stack for an explicit authorization/determination architecture*.
- **Output-state nearest neighbour (L2D lineage, must-cite)**: Learning to Defer (Chow 1957 → Madras et al. 2018 → Mozannar & Sontag 2020 → the Oxford survey of 2025) studies "handing over to a human when the AI is uncertain," superficially isomorphic to suspension. Demarcation: L2D is a **per-prediction routing action** (a statistical learning objective with no institutional semantics); the suspension discussed in this map and in the doctrine of governance determinability is an **institutional state** — carrying ledger fields, audit chains, debt aging and lifecycle gates. In one sentence: L2D answers "route to whom"; institutional suspension answers "who is accountable during the suspension, how much debt accrues, and when reconsideration triggers." The phrase *institutional suspension* is, at the phrase level, unoccupied (title-level hits for "algorithmic deferral": one irrelevant).
- **Institutional lineage anchor (asset, not collision)**: the "determination-up-front" institution family is decades old — advance rulings (WTO Trade Facilitation Agreement; CBP binding rulings), declaratory judgment (28 U.S.C. §2201; *Abbott Labs v. Gardner* 1967 establishing pre-enforcement review), FDA Pre-Sub/Q-Submission (with MDUFA VI adding the Focused Follow-Up Pre-Submission); and the **MDUFA dual-clock "stop-clock on deficiency letter, restart on response" mechanism is the official precedent for suspension accounting** (roughly 70% of first-round 510(k)s receive deficiency letters — suspension is the norm, not the exception), while MDUFA VI's draft "Not Grantable" letter is an institutional precedent for terminal output states. On the engineering side, BPMN escalation events and the Camunda execution models show suspension as a mature mechanism — without debt semantics or sector metrics. This lineage supplies historical depth for Domain ⑤ and the suspended state; it is not itself impossibility evidence.

### 2.6 Periphery: folk thesis and early survey (not mapped)

- Palm (2026, LinkedIn) — the "regulatory incompleteness thesis": who audits the auditors; perfect regulation is impossible, feasible regulation is necessarily incomplete. No theorem-grade proof; **not mapped**, kept as a peripheral note — its value is the signal that impossibility narratives are spreading through industry (2026), and a spreading narrative most needs a map.
- *On Controllability of AI* (arXiv:2008.04071, 2020) — assembles control-theoretic classics (uncontrollability/unobservability, the Good Regulator theorem, the law of requisite variety) into an argument for AI uncontrollability. Demarcation: it is a cross-domain citation compilation for one position (self-described as non-comprehensive), not a coordinate chart of governance-task impossibility, and it predates the 2025–2026 burst of governance theorems. Cited here as an intellectual precursor of the observational dimension of Domain ⑤; the map's increment — five-cluster propositions, boundary conditions, possibility-domain positioning — is not covered by it.

---

## §3 Nesting and Overlap: The Integration Map (Author Synthesis)

```
Folk periphery: Palm, "regulatory incompleteness thesis" (2026, no theorem — a diffusion signal)
┌──────────────────────────────────────────────────────────────┐
│ Domain ① Philosophical: algorithmic-clarity critique (critique-grade)│
│   "legal determinacy vs algorithmic closedness" — conceptual tension │
│   ┌──────────────────────────────────────────────────────────┐ │
│   │ Domain ② Explainability: regulatory trilemma (info-theoretic,│ │
│   │   Rao 2025) capability × interpretability × error            │ │
│   │   ┌──────────────────────────────────────────────────────┐ │ │
│   │   │ Domain ③ Determination: two boundaries (theorem-grade, │ │ │
│   │   │   McCann 2026) semantic compliance undecidable (Rice); │ │ │
│   │   │   exit = architectural separation → coterminous gov.   │ │ │
│   │   │   ╔══════════════════════════════════════════════════╗ │ │ │
│   │   │   ║ Domain ⑤ Authorization–observation (theorem-grade, ║ │ │ │
│   │   │   ║   Meyman 2026 / Fernandez 2026 / Zhu & Leonard     ║ │ │ │
│   │   │   ║   2026 — three independent, mutually non-citing)   ║ │ │ │
│   │   │   ║   observability ≠ ex-ante authorization            ║ │ │ │
│   │   │   ╚══════════════════════════════════════════════════╝ │ │ │
│   │   │   ┌──────────────────────────────────────────────────┐ │ │ │
│   │   │   │ Domain ④ Accountability: horizon (theorem-grade,   │ │ │ │
│   │   │   │   Tibebu & Shemtaga 2026) beyond threshold ×        │ │ │ │
│   │   │   │   feedback cycle → four axioms unsatisfiable        │ │ │ │
│   │   │   │   ✦ possible anchor: Attributability alone held by  │ │ │ │
│   │   │   │   object-identity anchoring (see §4)                │ │ │ │
│   │   │   └──────────────────────────────────────────────────┘ │ │ │
│   │   └──────────────────────────────────────────────────────┘ │ │
│   └──────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
(Domain ④ overlaps Domain ③ under "high autonomy + feedback cycle";
 Domain ⑤ sits beside ③ — one about determination, one about authorization)
```

**Three integrative claims (the core scholarly increment of this paper)**:

1. **Convergent direction, independent routes.** The five domains do not entail one another, yet five independent routes — conceptual critique, information theory, computability theory, axiomatic social choice, authorization architecture — approach the same conclusion: governance effectiveness has a structural boundary. The convergence of independent routes is itself evidence: this is not the artifact of one method.
2. **Nesting is this paper's synthesis, not consensus.** The philosophical layer (conceptual impossibility) is outermost; the explainability and determination layers sit inside it side by side (one about the information content of explanation, one about the computability of determination); the accountability layer overlaps the determination layer under "high autonomy + feedback cycle"; the authorization–observation layer sits beside the determination layer (one about the existence of ex-ante authorization artifacts, one about the computability of semantic-level determination). Each domain's internal conclusion belongs to its authors; if later work corrects the nesting, the map accommodates the correction.
3. **Two empirical symptoms of non-citation.** (i) Between Domains ② and ④: Rao precedes Tibebu by nearly a year, yet the latter claims "first" and neither cites the other. (ii) Inside Domain ⑤: Meyman, Fernandez, and Zhu & Leonard independently produced isomorphic conclusions within one half-year, again without cross-citation. Across this literature even "who was first" and "how many domains exist" lack coordinates. The necessity of a public coordinate system is proven by the literature's own behaviour.

---

## §4 The Possibility Domain: What Stands, and Why

Everything outside the impossibility domains is the **possibility domain**. This section locates six classes of governance assets — using the authors' own portfolio (LGD, the doctrine of governance determinability, the ACD family, XCGS, A³, coexistence) as the worked instance; the method generalizes to any regime.

| Asset | Position | Avoidance rationale (which domain it avoids, and how) |
|---|---|---|
| **Doctrine of governance determinability** (working paper, cited as such) | L0–L4 criteria spectrum | Avoids Domain ③: regulatory determination never adjudicates arbitrary program semantics (that is undecidable); it adjudicates **discrete declared attributes** (update type, safety level, performance comparison) — which fall naturally inside the decidable boundary. McCann's exit (architectural separation) has its regulatory-side counterpart: "determine attributes, not behaviour." |
| **LGD-I "registered" (identity anchoring)** | The only anchor region inside Domain ④ | Of the four axioms, **Attributability** alone holds provided causal contribution is traceable — and lifecycle identity anchoring (registration / record / deregistration) secures exactly that. Tibebu himself concedes legitimate frameworks exist below the horizon: anchoring pins accountability on the feasible side of the threshold. |
| **ACD family (determinators)** | L2 rule-state instances | Avoids Domain ③: inputs are discrete declared attributes; output is a four-state verdict including **suspension** (explicit ledger entry when criteria, evidence, or subject are missing) — impossibility-aware determination output. |
| **XCGS evidence chain** | Passport of the possibility domain (records side) | **Domain ⑤ bounds it, it does not bury it**: Meyman's theorem forbids treating observational derivatives as authorization artifacts, not record-keeping and replay themselves. XCGS claims only to be infrastructure for third-party replay of determinations (the records ≠ verdicts discipline) — precisely the lawful side Meyman's demarcation opens. None of the five domains forbids archiving and replay. |
| **A³ / PCC (progenitor constraint)** | Institutional feedback outside Domain ④'s boundary | Does not solve the mathematical impossibility of responsibility allocation, but introduces source-side constraints before autonomy approaches the threshold, keeping systems out of the "no viable framework" region. |
| **Coexistence doctrine** | Institutional response to Domain ② | The trilemma forbids "zero error + full explanation + full capability" and permits "institutionally allocated error between human and machine" — human-in-the-loop is not perfect explanation; it is the institutional sharing of error. |
| **LGD-III "gated"** | Theorem-grade endorsement region of Domain ⑤ | Meyman proves that monitoring stacks do not produce authorization artifacts — the structural argument for *explicit determination gates*: gates must be institutionalized determinations (LGD-III), not telemetry dashboards. LGD-III stands on the same side as Domain ⑤. |

**Methodological point.** Possibility-domain positioning is not self-promotion. Any governance regime can be audited by the same four questions: Does your governance action rely on semantic-level determination (Domain ③)? Does your accountability promise presuppose Completeness (Domain ④)? Does your transparency promise ignore the information floor of explanation (Domain ②)? Is your "observability" being sold as authorization capability (Domain ⑤)? Assets that survive all four are exactly the assets that survive the impossibility literature. This is the paper's expected citation scene: readers of future impossibility results need a list of what these results kill and what they leave standing.

---

## §5 What This Means for Governors: From "Perfect Compliance" to "Debt Management"

One lesson follows from the five domains: **a governance paradigm whose default goal is perfect compliance will pour resources into impossibility domains** — semantic-level audits of arbitrary behaviour (Domain ③), perfect legal restatement of algorithmic decisions (Domain ①), zero-error full explanation (Domain ②), full responsibility allocation for hyper-autonomous systems (Domain ④), and "if monitoring is good enough, authorization takes care of itself" (Domain ⑤).

The turn: **the effective output of governance is not compliance declaration but determination and debt management** —

1. **Make determination points explicit**: land governance requirements on discrete, decidable attributes (the exit of Domain ③; the Rules-as-Code movement — Catala, L4, defeasible reasoning, with Hildebrandt's critique — supplies the system and its limits; this map positions the regulatory-side exit as "determine declared attributes, not program semantics").
2. **Make suspension explicit**: when criteria, evidence, or subject are missing, output *suspension* and record it — never guess, never stall silently, never wave through. The dominant failure mode of governance is not "no principles" but the silent accretion of **determination debt** — the stock of declared requirements that never acquired determination conditions. Demarcation table (the debt family): technical debt (classic), verification debt (evidence shortfall, CACM), assurance debt (Frontiers), compliance debt (vendor / Gartner compliance-as-code), regulatory debt (medtech parlance) — **determination debt is the sixth sibling and the only one pointing at the determination itself**: the upstream cause of the others. Cite with explicit demarcation.
3. **Make boundaries explicit**: for every governance promise, state which impossibility domain it assumes itself outside of — a promise can be audited only if it can be located.

This section is the counterpart of the authors' critique short paper, *Principles Will Not Save AI Governance* (P2, working paper): P2 critiques the suspension of principles; this map gives the geometric reason — principles assume they stand in the possibility domain, and they may not.

---

## §6 Limitations and Replies

1. **"The nesting is philosophically contestable."** Accepted. The nesting is flagged as the authors' synthesis; the map's value lies in its coordinate function, not geometric exactness. Later corrections are map updates, not map failures — the core increments (five convergent routes; the documented absence of coordinates) stand.
2. **"Boundary conditions may be relaxed by future work."** Possibly, and the map welcomes it: each domain states its boundary condition (§2); a relaxed theorem shrinks a domain rather than invalidating the map.
3. **"Why is the folk thesis not mapped?"** No theorem-grade evidence; mapping it would lower the map's evidential standard. The peripheral note preserves its signal value.
4. **"Does this negate governance?"** The opposite. The map's entire purpose is to withdraw governance resources from impossibility domains and redeploy them where governance works: identity anchoring, discrete determination, evidence replay, debt management — all outside the domains and all feasible. Impossibility domains are **design constraints**, not governance's terminus, and still less a reason for inaction.
5. **"Is self-positioning in §4 circular?"** The map stands independently (§2–§3 depend on no asset of the authors); §4 is one application instance and the method generalizes. The doctrine is cited as an unpublished working paper, so no published conclusion is used to support itself.

---

## Appendix A: Acknowledgement and Demarcation Table

| Source | Type | Use in this paper |
|---|---|---|
| Rao 2025 (arXiv:2504.20676, Shrisha Rao) | Information-theoretic theorem | Domain ②; ownership of "regulatory impossibility results" |
| McCann 2026 (arXiv:2604.27292, Alan L. McCann) | Theorem-grade (Coq-mechanized) | Domain ③; coterminous governance |
| Tibebu & Shemtaga 2026 (arXiv:2604.07778, Haileleol Tibebu, Hewan Shemtaga) | Theorem-grade | Domain ④; the Attributability anchor argument |
| Rice 1953 | Classical theorem | Theoretical source of Domain ③ |
| Chalupa 2026 (DIP framework + DCF committee draft v1.3, Zenodo) | Nearest-neighbour framework | Demarcation at the ③/⑤ execution side; decision-execution vs determination centre |
| L2D lineage (Chow 1957; Madras et al. 2018; Mozannar & Sontag 2020; Oxford survey 2025) | Mature ML field | Domain ⑤ output-state demarcation: routing action vs institutional state |
| Catala / L4 / Hildebrandt (Rules as Code) | System + critique | §5 engineering and legal foundation of the determination exit |
| MDUFA V/VI (FDA) | Regulatory institution | Official precedent of suspension accounting (stop-clock; Not-Grantable letter) |
| advance ruling / declaratory judgment (WTO TFA; 28 U.S.C. §2201; Abbott Labs 1967) | Administrative-law lineage | Historical depth of Domain ⑤ / suspension |
| Meyman 2026 (Edward Meyman, FERZ programme, Zenodo 10.5281/zenodo.19647542) | Theorem-grade (three lemmas) | Domain ⑤; observability ≠ authorization |
| Fernandez 2026 (Marcelo Fernandez, Agent Governance Series, Zenodo 10.5281/zenodo.19669430) | Theorem-grade | Domain ⑤; integrity ≠ coverage |
| Zhu & Leonard 2026 (Applied Sciences 16(10):4917) | Formal framework (peer-reviewed) | Domain ⑤; three deployment regimes |
| *On Controllability of AI* (arXiv:2008.04071, 2020) | Early cross-domain survey | Demarcated citation in §2.6; precursor of the observational dimension |
| Kalulé 2019 / Springer 2019 / IJSL 2025 | Philosophical critique | Domain ① |
| Palm 2026 (LinkedIn) | Folk thesis | Peripheral note (not mapped) |
| Jobin, Ienca & Vayena 2019 | Source of the mapping move | §1 methodological precedent |
| Zhou Li'an 2024 (the impossible trinity of governance, Peking University) | Social-science precursor | Chinese governance scholarship's impossibility structure (targets/resources/rules); demarcation: organizational governance ≠ AI regulatory determination |

## Appendix B: Pre-Submission Checklist Status

- ☑ No abbreviation refers to the map anywhere; Chinese master name 「治理不可能域地图」 + English *the Governance Impossibility Map*; both demarcations embedded at §1
- ☑ Propositions verified against primary sources (Rao / McCann / Tibebu arXiv abstracts read directly; Domain ⑤ trio via Zenodo/MDPI records; 2026-09-08)
- ☑ Evidential-strength grading marked throughout
- ☑ Collision sweep: nine rounds total (R1–R7 company machine; R8a/R8b/R9 home machine), zero map-type integration found; exact phrase "governance impossibility map" = 0 hits on both OpenAlex (title + full-text) and Google
- ☑ Citation package: Chalupa DIP+DCF ✓ / debt-family demarcation ✓ / Rules as Code ✓ / L2D ✓ (TC260 and the Chinese trio attach to the Chinese journal version)
- ☐ Remaining before submission: final sensitive-information scan; SSRN submission is an external action requiring confirmation
