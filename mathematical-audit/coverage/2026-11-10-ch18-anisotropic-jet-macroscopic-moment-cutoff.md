# Additive coverage — §18.44 proportional point-jet order — 2026-11-10

**Production revision:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; chapter index \`docs/chapters/index.html\` was directly reread (25 chapters, 747 numbered sections in the retained inventory). **Audit branch:** \`review/mathematical-audit\`.

**Direct mathematical reading:** §18.44, *Anisotropic point jets and isolated poles on fibrations*, at \`docs/sections/partial-kernels-and-quotient-equilibrium--anisotropic-point-jets-and-isolated-poles-on-fibrations/index.html\`, main HTML blob \`1eefb2e68f8091fcd531535ed38b9003774a2f95\`.
- Physical lines 7–46: fixed metrics, curvature variables \(H_j,G_j,g_j\), polynomial degrees, order conventions; selected source labels/permanent tags are in the full report.
- Lines 47–115: direct audit of Theorem 18.44.2, orthogonal monomial model, exact factorization (18.44.5), interior full kernel saddle expansion and total-variation argument. **New selected proof:** macroscopic cutoff \(k_m/m\to\kappa>0\), the product-moment polytope slice, all-order lattice count, and fixed-interior Gaussian transition.
- Lines 132–161: Proposition 18.44.8 read contextually to separate its shrinking-radius/sublinear threshold from the new interior linear threshold; **not re-certified**.
- Lines 182–219: Theorem 18.44.11 and its final scope caveat read contextually; lifted quasi-PSH selecting weights **not** extended to positive \(k_m/m\).

**Stable finding:** \`POME-ANISOTROPIC-JETS-MACROSCOPIC-MOMENT-CUTOFF-001\`, **low / verified conditional deduction**, no printed theorem refuted. [Full report](../reports/2026-11-10-anisotropic-jet-macroscopic-moment-cutoff.md), [ledger](../ledger/2026-11-10-anisotropic-jet-macroscopic-moment-cutoff.md).

**Exact matrix increment:** §18.44 was previously recorded as inventory only; **+1 previously unreviewed numbered section first visited at proof level**, **+0 full-section mathematical certifications**. The total inventory stays **25 chapters / 747 distinct numbered sections / 0 complete-section certifications**. No other section receives a new coverage claim merely because its results are mentioned or used as internal dependencies. In particular §18.42 is **not** certified here.

**Remaining risk:** upstream full-kernel saddle estimate as an internal dependence; boundary/degenerate-observation regimes when some \(t_j\to0\); non-product weights; and extending to fixed quasi-PSH singularities or general fibrations. All are outside this selected deduction. User-excluded Demailly approximation/regularization and its dedicated Bergman–L²–Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion programme remain explicitly **deferred-by-user**. The audit wrote Markdown only, not production main, generated pages, source proofs, registries, tags, tests, build, CI, or website.
