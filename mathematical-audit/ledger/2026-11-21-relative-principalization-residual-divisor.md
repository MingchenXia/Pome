# POME-RELPRINC-RESIDUAL-DIVISOR-NONEXCEPTIONAL-001

**Baseline:** main b6933b772f41b45918f7e25ed1afbbb1fd892272; audit branch review/mathematical-audit.

**Status:** low severity / confirmed error in an ancillary *proof sentence*, **not a false theorem**. Suggested one-sentence repair is verified locally, conditional on Hironaka principalization, but is not yet applied to production.

**Anchor:** docs/sections/complex-spaces-and-modifications--proper-images-and-relative-principalization/index.html, blob b44fe157b8c01363da7799990b8ef6ed82525553, Theorem 9.7.5, source foundations-of-pluripotential-theory:1524D010, permanent 689628C7AF7F, Step 3 physical line 120. Cross-check docs/sections/complex-spaces-and-modifications--blowups-and-resolution/index.html, blob f452f4b1abe5cdfe348ae11fcd934febcfdd570b, Theorem 9.6.7 lines 91–107, source B74A86AD, permanent 24330D25741D.

**False surplus assertion:** \(H'\) is supported on exceptional divisors of \(g\). For \(M=\mathbb P^2\), \(W=\{p\}\), and \(L\) a projective line disjoint from \(p\), let \(\mathfrak a=\mathcal I_L=\mathcal O(-L)\). The restriction to \(W\) is the unit ideal. Principalizing the Cartier divisor \(L\) is an isomorphism, so \(g=\mathrm{id}\) has no exceptional divisors while \(H'=L\neq0\). The three required formulas (9.7.6)–(9.7.8), and \(H'\cap W'=\varnothing\), nevertheless hold. Thus the theorem is valid and the extra claim is false.

**Proposed repair:** \(\operatorname{Supp}H'=V(\mathfrak a_t\mathcal O_{M'})=g^{-1}(V(\mathfrak a_t))\), disjoint from \(W'=g^{-1}(W_t)\) because \(\mathfrak a_t\) is the unit ideal near \(W_t\). Step 4 independently establishes that \(H\), *not* \(H'\), is exceptional for \(f\).

**Affected dependents:** Step 3 itself and possible future claims incorrectly treating \(H'\) as exceptional. No downstream misuse established. No canonically merged tags or body edits.

**Other new scope:** complete §7.6 mathematical lines 7–80, docs/sections/bedford-taylor-products-and-local-capacity--increasing-limits-and-exceptional-envelopes/index.html, blob 5e763bdc928794938c37dc3c7a51cc406472d076, Theorem 7.6.1 source 36787F42/permanent A4C45B704647 and Corollary 7.6.2 source 2ACED3F4/permanent D865A8538D7D. No new confirmed error; cited proofs not transitively certified. Selected §9.6.7 only.

**Documentation:** [full report](../reports/2026-11-21-relative-principalization-residual-divisor-and-increasing-bt.md) and [exact coverage](../coverage/2026-11-21-ch7-increasing-bt-ch9-relative-principalization.md).

**Unresolved/external:** cited Bedford–Taylor/CLN/capacity proof chains; remaining §9.7; Hironaka principalization admitted as external. **Deferred-by-user:** all excluded Demailly/Bergman/L2/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss work, neither resolved nor certified.
