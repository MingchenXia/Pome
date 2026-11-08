# Finding ledger — POME-HESS-NEARMIN-LOCAL-MASS-001

- **Date:** 2026-11-09; **status:** verified conditional deduction; **severity:** low.
- **Not an error:** The printed Lemma 8.13.7, Theorem 8.13.8, Lemma 8.12.3 and Lemma 8.2.10 are retained unchanged. Their complete upstream analytic proofs were **not** certified.
- **Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Primary file and blob:** docs/sections/complex-hessian-equations--hessian-mass-and-global-comparison/index.html, 580d3bc2b10ebd01d880b2a31fc6930436570aac.
- **Stable labels and anchors:** Lemma 8.13.7 source non-kahler-pluripotential-theory:D2B92D4C / permanent 0F8C3F6B0122, physical lines 174–224; Theorem 8.13.8 source non-kahler-pluripotential-theory:AEE5FFB9 / permanent B83D4B8CE619, lines 226–280.
- **Inputs:** §8.12.3 source non-kahler-pluripotential-theory:B518F16E / permanent 132BB9E1B1F5 (blob 8750df56019c14e16704607ca20fa8b90f137fb0, lines 67–96); §8.2.10 source non-kahler-pluripotential-theory:6FFAAFB0 / permanent A1FFEE061CF5 (blob 925e6109ab7d800cde9bec4b0487842b2e6877a8, lines 262–end).
- **Hypotheses:** compact connected Hermitian \(X\), \(2\le m<n\); bounded canonical admissible \(u,v\); \(0<\alpha<1\); \(0<s<(1-\alpha)^3/C\). No closedness of \(\omega\) or openness of \(E_s\).
- **New exact claim:** \(H_m(u)(E_s)\ge (1-\alpha)^m[1+Cs(1-\alpha)^{-m}]^{-1}\mathrm{Vol}_\omega(E_s)>0\), with \(E_s=\{u<\alpha v+\inf(u-\alpha v)+s\}\).
- **Specialization:** for every \(t>0\), the strict near-infimum set \(\{u<\inf u+t\}\) carries positive \(H_m(u)\)-mass; for \(0<t<1/(4C)\) the explicit lower-volume factor \(2^{-m}/(1+C2^{m-1}t)\) holds.
- **Justification:** Lemma 8.2.10 upgrades a.e. order to canonical pointwise order, establishing positive volume; §8.12.3 supplies the \((1-\alpha)^m\omega^n\) background; §8.13.8 supplies the bounded comparison ratio. The \(\eta^{-3}\) recursion was independently rechecked (see full report).
- **Proposal:** optional explanatory remark, not a production patch. **Affected dependents:** §8.13.10 strict domination and §8.12.5 positive mass as contextual comparisons only. No downstream incorrectness established.
- **Unresolved:** full Hermitian torsion and weighted Hessian-current continuity inputs §§8.11–8.12; no section certification. Earlier ledgers remain as classified.
- **Deferred-by-user, unchanged:** dedicated Demailly regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme.
- **Proof:** [dated detailed report](../reports/2026-11-09-hessian-near-minimum-local-mass.md). **Exact coverage:** [§8.13 selected recursion](../coverage/2026-11-09-ch8-modified-comparison-near-minimum.md).
