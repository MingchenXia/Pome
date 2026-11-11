# Diagonal proper maps: sharp pluricomplex Green distortion and residual degree
Date: 2026-11-11

**Stable finding:** POME-GREEN-PROPER-DIAGONAL-POWER-EXACT-SHARP-001  
**Severity/status:** low / **verified conditional deduction**, **not a refutation** of the printed propositions.  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Primary integrated reading edition:** `docs/sections/isolated-pole-green-envelopes-and-continuity/index.html` (blob `e82b6baaa0061f55aeea2f88ec0567d9653ecd61`), Proposition **7.17.3**, source label `klimek-pluripotential-theory:FBA066A7`, permanent tag `2CC830293978`, physical lines **52–69**. Supporting Proposition **7.17.2**, source label `klimek-pluripotential-theory:75CBD17E`, permanent tag `7B9EA3C07531`, physical lines **34–50**. The one-pole classical measure is Proposition **7.18.2**, source label `klimek-pluripotential-theory:E1312773`, permanent tag `AD17D2D77F97`, in `docs/sections/classical-monge-ampere-measures-at-one-exceptional-point/index.html` (blob `902375361e37c15e45e7f4b7055bfe4cd6a6db9d`, physical lines **56–70**). Proper finite maps are compared with Proposition **7.16.4** (source `klimek-pluripotential-theory:2CB6C014`, permanent `CF1B00103D5B`, `docs/sections/relative-extremals-on-bounded-hyperconvex-domains/index.html`, blob `c6560283c5ff9e2587ffe93f7f2e7ba687105243`, physical lines **96–109**).

## Precise statement

Let \(n\geq2\), \(d_1,\ldots,d_n\) be positive integers, and let \(P=\Delta^n\). Consider the proper finite map
\[
 F:P\longrightarrow P,\qquad F(z_1,\ldots,z_n)=(z_1^{d_1},\ldots,z_n^{d_n}).
\]
Write \(d_-=\min_jd_j\), \(d_+=\max_jd_j\), \(D=\prod_jd_j\), and normalize the pluricomplex Green function to have pole coefficient one relative to \(\log|z|\). Then

1. \(F^{-1}(0)=\{0\}\), its generic/topological degree is \(D\), and at every \(z\in P\)
   \[
   d_+g_P(z,0)\ \leq\ g_P(F(z),0)\ \leq\ d_-g_P(z,0).
   \]
   Both constants are **attained at nonzero points arbitrarily close to the pole**, hence \(d_+\) is the smallest permissible coefficient on the left and \(d_-\) the largest permissible coefficient on the right. If all \(d_j=d\), the exact identity is \(g_P\circ F=d\,g_P\); if not all agree, no scalar \(c\) gives \(g_P\circ F=c\,g_P\).

2. The same exponents are the sharp local Łojasiewicz bounds for Euclidean norms:
   \[
   c|z|^{d_+}\leq |F(z)|\leq C|z|^{d_-}\quad (z\to0).
   \]
   Thus Proposition 7.17.3 cannot replace its pair of growth exponents by the **single generic degree** without losing sharpness. Its singleton-fiber hypothesis is essential, not redundant.

3. Assuming the established bounded Bedford–Taylor decreasing-continuity and one-pole mass input cited above, its **classical one-pole measure** (not the non-pluripolar product) satisfies
   \[
   M_{g_P\circ F}=\frac{D}{2^n}\delta_0,\qquad M_{g_P}=\frac1{2^n}\delta_0.
   \]
   The factor \(2^{-n}\) is essential under Pome's \(dd^c=\frac{i}{2\pi}\partial\bar\partial\) convention. Consequently the product degree \(D\) measures residual mass while \(d_-,d_+\) measure anisotropic Green distortion; these are genuinely different invariants.

For example in dimension two, \(F_1(z)=(z_1^d,z_2^d)\) and \(F_2(z)=(z_1,z_2^{d^2})\), for \(d\ge2\), have the **same** degree \(D=d^2\) and residual mass \(d^2/4\), but the sharp Green exponents are respectively \((d,d)\) and \((d^2,1)\). This compares fixed multiplicity with distinct directional behaviour.

## Complete direct proof of the sharp Green assertions

The printed polydisc formula from Proposition 7.17.2 gives
\[
 g_P(z,0)=\max_j\log|z_j|,\qquad
 g_P(F(z),0)=\max_j d_j\log|z_j|.
\]
Every \(\log|z_j|\le0\), with the usual \(-\infty\) convention at zero. Hence
\(d_+\log|z_j|\le d_j\log|z_j|\le d_-\log|z_j|\) for every \(j\). Taking coordinatewise maxima proves the double inequality, including points with zero coordinates and the pole in the extended-real sense.

At a nonzero point on the \(j\)-th coordinate axis all other logarithms are \(-\infty\). The ratio
\(g_P(F(z),0)/g_P(z,0)\) is **exactly \(d_j\)**. In particular, axes realizing \(d_+\) and \(d_-\) show each bound is optimal in every punctured neighbourhood of zero. They also rule out proportionality when the \(d_j\)'s differ. This is more precise than merely exhibiting an asymptotic extremizing sequence.

For \(0<|z|<1\), set \(m=\max_j|z_j|\); then \(|z|/\sqrt n\le m\le|z|\). Since \(0\le|z_j|<1\),
\[
 |F(z)|\ge\max_j|z_j|^{d_j}\ge m^{d_+}\ge n^{-d_+/2}|z|^{d_+},
 \quad
 |F(z)|\le\sqrt n\,m^{d_-}\le\sqrt n\,|z|^{d_-}.
\]
Along axes with the extremal exponents, changing \(d_+\) downwards or \(d_-\) upwards makes the corresponding power bound impossible as \(z\to0\). Properness follows because preimages of compact subsets of \(P\) have all coordinates bounded away from the unit-circle boundary; a regular value with every coordinate nonzero has precisely \(\prod_jd_j\) inverse points. This independently verifies the admissible assumptions, inequality directions, and power normalizations of Proposition 7.17.3 for this entire family.

## Residual mass: conditional dependence stated precisely

The printed Proposition 7.18.2, together with the maximality of the polydisc Green function off its pole, gives \(M_{g_P}=2^{-n}\delta_0\). We outline the needed **finite-map change-of-variables** separately so that it is not silently inferred from numerical degree alone.

For any locally bounded PSH \(v\) on the target, the classical BT measure satisfies
\[
 F_*(dd^c(v\circ F))^n=D\,(dd^cv)^n.
\]
For smooth \(v\), \(dd^c(v\circ F)=F^*dd^cv\) and the identity is the ordinary proper holomorphic change-of-variables formula, including branch points (a proper analytic branch locus has zero volume for the smooth top form). For bounded PSH \(v\), decrease smooth local PSH approximants to \(v\) and invoke ordinary bounded BT continuity on compact subdomains; properness lets one localize both sides. This is **ordinary bounded BT calculus**, not the user-deferred Demailly regularization/Bergman/L²/OT programme.

Apply this formula to \(v_k=\max\{g_P,-k\}\). Then \(v_k\circ F=\max\{g_P\circ F,-k\}\), so the formula holds at each finite truncation level. By the one-pole *classical* measure definition and its monotone truncation theorem, both measures converge to their classical pole measures. Properness allows weak pushforward of these compactly supported measures. Their limits are supported at the sole inverse pole, giving
\[
 F_*M_{g_P\circ F}=D M_{g_P}=\frac D{2^n}\delta_0
 \quad\Longrightarrow\quad
 M_{g_P\circ F}=\frac D{2^n}\delta_0.
\]
Here the critical analytic inputs are the printed ordinary bounded BT continuity and classical pole-measure passage; the audit has **not** independently certified the full upstream theory. The Green power bounds and their sharpness, by contrast, are proved here directly from the exact formula.

## Classification, dependents, and action

- **Status:** verified conditional deduction, low severity. This is **not** a confirmed error, not a genuine duplication, not a repair to a false theorem and not a full certification of §§7.16–7.18. The exact Green inequalities and local power estimates require only the explicit polydisc Green formula; the residual-mass identity remains conditional on the named bounded BT and classical one-pole measure inputs.
- **Proof review:** The direction of both logarithmic inequalities in the printed Proposition 7.17.3 is consistent with the negative Green-function convention. Its fiber-maximum argument explicitly uses the singleton fiber; there is no premise loss in the checked lines 52–69.
- **Suggested clarification only:** after Proposition 7.17.3, add this diagonal-power example to distinguish \((d_-,d_+)\) from generic degree \(D\) and to warn that **classical** residual mass is not the non-pluripolar product. No reading-edition edit is made by this audit.
- **Dependents inspected:** Proposition 7.17.2 (polydisc formula), Proposition 7.18.2 (normalization and one-pole classical measure), and Proposition 7.16.4 (proper finite maps) only in the stated roles; no claim is made about all their other conclusions.
- **Exclusions:** Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, positivity-loss proof-completion programme remain **deferred-by-user**, not resolved, certified or reopened. No source/registry/permanent-tag changes.

## Actual scope

New mathematical proof-level check in already partly reviewed §7.17, supported by one-pole mass normalization in already partly reviewed §7.18 and finite-map context in already partly reviewed §7.16. **0 newly first-visited numbered sections; 0 wholly certified sections.** The current main table-of-contents baseline remains **25 chapters / 747 numbered sections**. A small four-case numerical check of the displayed ratio inequality was executed; this is only a consistency test, not a proof of the general formula. No build, project test suite, CI, publication, or formal verification was run.
