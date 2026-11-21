# 2026-11-21 — Sparse valuative scales and oscillation-controlled relative capacity

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Location:** audit branch review/mathematical-audit only. [Full mathematical proof](../reports/2026-11-21-sparse-valuative-scales-and-relative-capacity.md).

## POME-MULTIPLIER-IDEALS-SPARSE-COFINAL-SCALES-001
- **Severity / status:** low / **verified conditional deduction**; no false theorem; no fully audited upstream proof chain.
- **Anchor:** docs/sections/envelopes-and-model-potentials--divisorial-constraints-under-envelopes/index.html, blob 40f522a64d7e846a4507c27e8ac9b4fa382c514c; Proposition 16.24.1, permanent 585A4246348B, source foundations-of-pluripotential-theory:73492AFD, physical lines 14–42.
- **Hypotheses / conclusion:** quasi-psh u,v; inclusion I(tv)⊆I(tu) on **any unbounded set of positive scales** implies the inclusion on all positive scales. Equality on that set similarly implies equality at all scales.
- **Justification:** generic ideal orders divided by t tend to divisorial Lelong numbers; integer limit 6.12.14 extends to real t by the ideal monotonicity sandwich between floor(t) and ceil(t). Then the valuative criterion 6.12.16 applies.
- **Proposed change:** optional corollary after 16.24.1; no modification to the valid printed statement. **Affected dependents:** I-preorder and equivalence, §16.24 envelope-order comparisons.
- **Open inputs:** independent certification of 6.12.14 and 6.12.16.

## POME-RELATIVE-CAPACITY-OSCILLATION-COMPARISON-001
- **Severity / status:** low / **verified conditional deduction**; no false printed Proposition 16.25.6; no completed upstream proof chain.
- **Anchor:** docs/sections/envelopes-and-model-potentials--singularity-constraints-and-relative-capacity/index.html, blob 4207ba03590b2988456f1df4da4123e1e572c8de; Definition 16.25.5 source 0AAB93DD / permanent E9BD67F94210 lines 104–110, Proposition 16.25.6 source foundations-of-pluripotential-theory:2C3BA6F2 / permanent 1587DBB4654F lines 113–138.
- **Hypotheses / conclusion:** θ-psh φ,ψ with common poles and bounded finite-locus difference m≤φ−ψ≤M; write L=M−m. Then the two capacities compare with factors (1+L)^{±n}, and coincide exactly when L=0.
- **Justification:** transfer any [φ−1,φ] competitor v to q=(1−t)ψ+tv−tM with t=1/(1+L), which belongs to [ψ−1,ψ]; mixed non-pluripolar positivity yields MA(q)≥t^n MA(v). Reverse φ,ψ.
- **Proposed change:** optional gauge-invariant refinement of the (2C+1)^n comparison, preserving its current valid bound. **Affected dependents:** relative-capacity estimates, capacity convergence in equivalent singularity types.
- **Open inputs:** general mixed non-pluripolar positivity and §13.8 constructions.

## Scope and status control
Whole direct: §3.8 (main blob bfee348bb5f4bbfaa4515e5c9333789a13dae861), §16.24 (40f522a64d7e846a4507c27e8ac9b4fa382c514c), §16.25 (4207ba03590b2988456f1df4da4123e1e572c8de), §16.26 (c40b40892fd37beb63802fb6cb253269fb59bd20). No historic first-visit count inferred; **+0 full transitive proof-chain certificates**. Other unreviewed and legacy-unknown entries stay unchanged. User-excluded regularization/Bergman/L²/OT/multiscale/positivity-loss programmes: **deferred-by-user**, not certified. No tests/builds/CI or production writes.
