# 2026-11-19 — finite-family rooftop mass inequality

- **ID:** POME-ROOFTOP-FINITE-FAMILY-MASS-INEQUALITY-001.
- **Severity / status:** low / **verified conditional deduction**; **not** a false theorem, not an independently confirmed proof gap, and not a duplicate of the printed binary result.
- **Main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Integrated source:** docs/sections/envelopes-and-model-potentials--rooftops-and-mass-inequalities/index.html, blob e6a5d5222b356a650b3834f30f8d597efb15d052, physical lines 5–180. Original source foundations-of-pluripotential-theory; printed tags: 3499B9FD713C (Proposition 16.23.1, lines 10–44), E33C504A684F (Proposition 16.23.2, 46–56), 37241FAAC9EF (Proposition 16.23.3, 58–96), F4294ED919CC (Lemma 16.23.4, 101–128), 641CB44C78E9 (Theorem 16.23.5, 130–179).
- **Hypotheses:** compact connected Kähler X, big {θ}, finite integer N≥2, θ-psh u_i; total non-pluripolar mass M; finite rooftop Pθ(u_1,...,u_N). In the mass inequality, the rooftop must not be identically −∞.
- **Deduction:** if ΣM(u_i)>(N−1)M(max u_i), the common rooftop exists; whenever it exists, ΣM(u_i)≤(N−1)M(max u_i)+M(P(u_1,...,u_N)). Proof: induction of binary contact measure domination; common-model truncations; decreasing zero-contact mass lemma; replacement of each model input by its equal-mass potential. See full report for the exact arguments and excluded limit cases.
- **Proposed correction:** none mandatory. Optional finite-arity proposition after Theorem 16.23.5. No alteration of the original two-input statements.
- **Potential dependents:** arguments needing simultaneous finite common minorants or finite-family non-pluripolar mass comparisons; no current broken dependent established.
- **Unresolved conditional inputs:** 16.13.5 binary contact, 16.21.3 model concentration, 16.22.11 modelization, 16.23.3 extrapolation, bounded weighted Bedford–Taylor and monotone non-pluripolar mass continuity. No transitive certification.
- **Deferred-by-user:** all Demailly regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss audit work (historical notes preserved, not resolved).
- **Actual coverage:** whole §16.23 direct proof reading, +1 direct whole-section, +0 complete upstream certifications; first visit not asserted; current main ToC 25 chapters / 747 sections. No tests/build/CI/publication.
