# Audit ledger — 2026-11-08 — Hopf quotient automorphism centralizers

| Stable ID | Severity | Classification | Printed theorem | Precise scope |
| --- | --- | --- | --- | --- |
| `POME-HOPF-AUTOMORPHISM-RESONANCE-CENTRALIZER-001` | Low | **verified conditional deduction** | Theorem 23.3.3 is correct; **no false printed assertion** | Complete explicit holomorphic automorphism groups for all diagonal and triangular contracting maps in the existing theorem. Resonant diagonal eigenvalues admit nonlinear polynomial shears; the group is the entire-map centralizer modulo the deck generator. |

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Exact file:** `docs/sections/contracting-hopf-quotients/index.html`, blob `d09d9bac3785b78b557ff5178ad7a52b34b20dac`. **Original source/permanent theorem:** `demailly-complex-geometry:371996B7` / `D81E3145A1B4`, physical lines **8–21, 26–27, 33–50**; iterate formula `demailly-complex-geometry:F5EE64FF` / `436562DE848D`, lines **29–31**. Section tag `20E4E5F60131`.

**Mathematical content:** Every quotient biholomorphism lifts to a punctured-\(\mathbb C^2\) biholomorphism; an explicit Cauchy integral extends both map and inverse across the origin. The induced deck-group automorphism cannot invert a contraction because its derivative at zero would be conjugate to its expanding inverse. Diagonal Taylor resonances reduce exactly to the single possible relation \(\lambda_1=\lambda_2^q\), \(q\ge2\); these give \((az+c w^q,bw)\). Scalar cases have \(GL_2(\mathbb C)\) centralizer. The Jordan \(p=1\) case admits only \(aI+bN\) by the homogeneous-degree eigenvalue test, and \(p\ge2\) is polynomially conjugate to the scalar case.

**Correction proposed:** optional new proposition, **not** a source correction. Do not identify the entire automorphism group with only the linear-centralizer subgroup for resonant diagonal contractions. Preserve original theorem, both permanent tags and historical attribution. No changes to source, main, reading registry or canonicalization.

**Affected dependents / limits:** any later use of \(\operatorname{Aut}(X_F)\) or equivariance on these specific surfaces; no claim to a classification of all Hopf surfaces, all LCK metrics, or full upstream covering theory. Earlier Hopf meromorphic/tensor/conjugacy findings remain separate and unchanged.

**Coverage:** substantive new selected theorem consequence in §23.3 (previously partially audited); **0 new first visits; 0 entire sections certified**; ToC **25/747/0**. Excluded Demailly regularization/Bergman/\(L^2\)/OT/multiscale/positivity-loss remains **deferred-by-user**; unrelated ledger entries retain their categories. [Complete proof](../reports/2026-11-08-hopf-full-automorphism-resonance-classification.md) · [precise coverage](../coverage/2026-11-08-ch23-hopf-automorphism-centralizers.md).
