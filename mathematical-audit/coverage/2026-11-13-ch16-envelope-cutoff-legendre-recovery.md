# Exact selected coverage, 2026-11-13 — Chapter 16 cutoff envelopes

Production main: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. Audit-only review branch. Current actual ToC: 25 chapters / 747 numbered sections.

| Section / exact step | Integrated path / blob | Original / permanent stable labels and physical line anchors | What was actually verified | What was **not** verified |
| --- | --- | --- | --- | --- |
| §16.29.2 left-constant normalized decreasing family and cutoff \(\Gamma_c\) | \`docs/sections/envelope-systems-over-hermitian-perturbations/index.html\`; \`856e240bbc5c86058ff861873f11e87db021e1bd\` | \`non-kahler-pluripotential-theory:DC46E61D\` / \`F0A985779829\`; lines 24–47 | Nested compact zero sets, existence of common zero, \(\sup\Gamma_c=0\), no sequential extraction | Entire §16.29, all projection and mass theorems |
| §16.29.3 regularized cutoff Legendre transform | same blob | \`non-kahler-pluripotential-theory:C6135113\` / \`160B15BF08FE\`; lines 51–66 | \(\sup U_t=ct\), raw cutoff limit, honest PSH exceptional-set passage giving \(U_t-ct\downarrow\Gamma_c\) | Theorem 17.17.5 complete proof; any assertion of an attained maximizing parameter |
| §18.4.2 normalization crosscheck | \`docs/sections/multiplier-ideal-envelopes-and-goodness--ideal-projection/index.html\`; \`f1979b73c857f4874dd4a5cb10b93bcc047ebbdc\` | \`non-kahler-pluripotential-theory:3A211D73\` / \`7F20FD198864\`; lines 22–29, 45–46 | Read the exact \(\sup_X P_\theta[\cdot]_{\mathcal I}=0\) statement and normalization step | All multiplier-ideal preservation/strong openness dependencies |

**Finding:** [\`POME-ENVSYS-CUTOFF-LEGENDRE-RECOVERY-001\`](../reports/2026-11-13-envelope-curve-cutoff-legendre-recovery.md), low / verified conditional deduction, printed theorem not refuted. [Ledger](../ledger/2026-11-13-envelope-curve-cutoff-legendre-recovery.md).

**Novelty / additive-only accounting:** §16.29 had earlier selected proof checks; this run covers a different exact premise (common zero set, cutoff recovery), not the prior ideal-projection reference-kind or volume issues. **+0 unique newly first visited sections / +0 complete certified sections**. All Demailly approximation/regularization and dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss work remains **deferred-by-user**. No build, tests, CI, source, published HTML, or site modifications.
