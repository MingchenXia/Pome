# 2026-11-09 — quantitative boundary-flux and compactification ledger

Reviewed production main b6933b772f41b45918f7e25ed1afbbb1fd892272. Full argument: [dated report](../reports/2026-11-09-nonproper-mass-all-dimensions-first-variation.md). Branch: review/mathematical-audit.

| Stable ID | Severity | Status | Exact target | Verdict, correction, dependents |
| --- | --- | --- | --- | --- |
| POME-FB-ALLDIM-LINEAR-FLUX-001 | low | verified conditional deduction | §16.43.1 source klimek-pluripotential-theory:ED092E5C, permanent A9104D666EA7, lines 8–39; §16.43.2 source C328B16E, permanent BD99C3A4D1ED, lines 43–51; §9.22.2 source BDF5266C, permanent CE10A564601F, lines 49–92 | Assuming stated existence §9.22.2, products with affine space give all complex dimensions n≥2. Compact cutoff perturbations have strictly positive first-order boundary flux Δ=nAε+O(ε²), A>0, despite u≤v and u−v→0 at infinity. **Printed results correct**. Proposed explanatory remark only; no theorem replacement. Dependents: mass-at-infinity comparisons / potential unprinted dimension-restricted inferences. |
| POME-FB-COMPACT-MASS-BRIDGE-001 | low | verified repair (proposed only) | §16.43.1 line 38, with compact §13.5.1 source foundations-of-pluripotential-theory:4EE18BE1, permanent 06A36B9354A5, lines 10–29 | Extend compact-support ψ by zero from C^n to P^n and apply §13.5.1 to (ω_FS/2+εdd^cψ̃); ∫ top mass=2^−n. **Proof clarification, not a demonstrated substantive proof gap or false theorem.** Proposed one-paragraph insertion; dependent §16.43.2 and the quantitative extension above. |

Reviewed reading-page blobs: §16.43 b9a79bd1d3254676b65d10031e314a2de1d5a0c4; §9.22 1279ba00791fa992f753ddd35a63cfc0fa36973f; §16.35 568257f81e9f31491e0cdde36ba8efb357423cd7 (boundary lemma source 5DEAA8D5, tag 6F70A6B34439, lines 81–92); §13.5 943517743538820940559eae8469ce98ecf5fcd5.

**Coverage:** selected steps only in §§16.43, 9.22, 16.35 and 13.5. The latter two are prerequisite/normalization checks, not proof-chain certificates. 0 newly first-visited sections; 0 complete mathematical-section certifications; current actual ToC 25 chapters / 747 sections.

**Preserve other classifications:** existing confirmed errors, proof gaps, candidates, genuine duplications and external-dependency ledger entries are unchanged. The dedicated Demailly regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss program stays **deferred-by-user**; it is not resolved or certified. No edits to main, generated docs, source, canonicalization, tags, GitHub Actions, or website.
