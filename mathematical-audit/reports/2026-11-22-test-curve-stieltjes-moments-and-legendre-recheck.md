# Test-curve mass distribution, finite-energy moment, and partial-Legendre cross-check

**Date:** 2026-11-22 (Asia/Shanghai). **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch:** review/mathematical-audit. This document audits the *integrated reading edition*, not merely theorem titles. No user-excluded regularization/Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss work was pursued.

## Direct material and provenance

- Entire §17.12, "The notion of test curves": docs/sections/test-curves--the-notion-of-test-curves/index.html, blob 6dfdfc2b5e599eb3a19a9558a9c963e79df71dc7; Definition 17.12.1 (source sgpt:ECCF19D5; permanent C8399F09D86D), Lemma 17.12.6 (source sgpt:95575DAE; permanent 348ACDBCB24E), Proposition 17.12.9 (source sgpt:37ECD68D; permanent B7CD1B90CFDA), Definition 17.12.10 and Equation 17.12.12 (source sgpt:38A406EF and sgpt:50A4CAA5; permanent 69529F41AA18 and 942AC971E484), through Proposition 17.12.19 (source sgpt:129B6722; permanent 724BF0CAE002). The identifiers are paragraph/equation anchors in the minified integrated HTML, where physical line numbers have no mathematical meaning.
- Entire §17.18 *rechecked, not new first or full-review credit*: docs/sections/partial-legendre-transforms-and-monge-ampere-mass/index.html, blob 5d989cf765f5471ce1e2278ef39e2c69979eeb92, Lemma 17.18.1 (source transcendental-positive-cones:676C0E65; permanent C12669D1EC3D), including the normalization of the angular measure, the Schur complement, mesh approximants, and noncompact-fiber tail argument. Prior full audit remains the 2026-11-19 Legendre report.
- Selected §17.14, Definition 17.14.1–Proposition 17.14.6 (integrated docs/sections/test-curves--model-test-curves/index.html, blob e058100104283d27de55bc64b4ce784f66ace28b): only a conditional model-projection dependency check, **not** a full §17.14 review. The subsequent filtration/Bergman-proof programme was not audited.

The actual current chapter 17 table of contents was read from docs/chapters/energy-geodesics/index.html. The 747-section matrix is not treated as a mathematical certificate. In particular, the earlier §17.18 full audit and §17.13 partial audit are retained, not counted as new findings.

## POME-TESTCURVE-MASS-LOSS-STIELTJES-MOMENT-001

**Severity:** low. **Status:** verified conditional deduction from the printed definition/monotonicity/continuity; **not** a printed-theorem error, a new proof of the upstream mass theorems, or an assertion of complete transitive verification.

**Hypotheses.** Let \(X\) be compact connected Kähler, \(\theta\) a smooth closed real \((1,1)\)-form in a big class, and \(\phi\in\mathrm{PSH}(X,\theta)_{>0}\) a positive-mass model potential. Let \(\Gamma\in\mathrm{TC}(X,\theta;\phi)\), with finite endpoint \(a=\Gamma_{\max}\). Write \(M(t)=\int_X\langle(\theta+dd^c\Gamma_t)^n\rangle\) for \(t<a\) and \(m=M(-\infty)=\int_X\langle(\theta+dd^c\phi)^n\rangle>0\). The displayed products are non-pluripolar products; the definition's unbracketed shorthand is not an assertion of ordinary smooth wedge products.

**Claim.** There is a canonical finite positive Borel measure \(\sigma_\Gamma\) on \((-\infty,a]\), of total mass \(m\), characterized by
\[
 \sigma_\Gamma((t,a])=M(t)\quad(t<a).
\]
In particular the endpoint atom is
\(\sigma_\Gamma(\{a\})=\lim_{t\uparrow a}M(t)\).
The energy in (17.12.12), including its possible value \(-\infty\), obeys the exact first-moment identity
\[
 \boxed{\mathbf E^\phi(\Gamma)=\int_{(-\infty,a]}t\,d\sigma_\Gamma(t).}
\]
Consequently \(\Gamma\in\mathrm{TC}^1(X,\theta;\phi)\) if and only if
\[
 \int_{(-\infty,a]}(a-t)\,d\sigma_\Gamma(t)<\infty.
\]
For any such finite-energy curve the mass deficit has the *strict tail estimate*
\[
 \boxed{m-M(a-T)=o(T^{-1})\qquad(T\to+\infty),}
\]
where \(T>0\), and the argument of \(M\) is within \((-\infty,a)\).

**Complete conditional proof.** Because the curve is decreasing and total non-pluripolar mass is monotone under decreasing singularities (theorem 13.13.11), \(M\) is nonincreasing. Proposition 17.12.9 makes \(M\) continuous and positive on \((-\infty,a)\), and its asserted continuity at \(-\infty\) gives \(M(t)\to m\). Put \(m_a=\lim_{t\uparrow a}M(t)\ge0\). The Stieltjes measure of the nondecreasing continuous function \(F(t)=m-M(t)\) on \((-\infty,a)\) assigns \(\sigma_\Gamma((s,t])=M(s)-M(t)\) to interior half-open intervals; give \(a\) an additional atom of mass \(m_a\). It is positive with total mass \((m-m_a)+m_a=m\), and its two tail identities are exactly
\[
 \sigma_\Gamma((-\infty,t])=m-M(t)=F(t),\qquad
 \sigma_\Gamma((t,a])=M(t).
\]
As \(a-t\ge0\), Tonelli's theorem, without any unjustified interchange of signed integrals, gives
\[
 \int_{(-\infty,a]}(a-t)\,d\sigma_\Gamma(t)
 =\int_{-\infty}^{a}\sigma_\Gamma((-\infty,s])\,ds
 =\int_{-\infty}^{a}(m-M(s))\,ds.
\]
The last integral may be \(+\infty\). Substitution in the *actual definition* (17.12.12) gives the claimed energy/first-moment identity. Positive parts of \(t\) are bounded by \(\max(a,0)\), so the integral on the right is always well defined in \([-\infty,\infty)\). For finite energy, \(F\ge0\) is increasing and integrable on \((-\infty,a)\). For any \(T>0\),
\[
 0\le\frac T2 F(a-T)
 \le\int_{a-T}^{a-T/2}F(s)\,ds
 \le\int_{-\infty}^{a-T/2}F(s)\,ds\longrightarrow0.
\]
This proves \(F(a-T)=o(1/T)\). No sequential compactness, interchange of non-pluripolar products, or excluded regularization results enter this *deduction*. The mass monotonicity and continuity used as internal upstream results remain unverified transitively.

**Endpoint-atom normalization check.** For the constant test curve \(\Gamma_t=\phi\) for all \(t<a\), \(M(t)=m\). Then \(\sigma_\Gamma=m\delta_a\), so \(\mathbf E^\phi(\Gamma)=am\), precisely as in (17.12.12). Omitting the atom at \(a\) would incorrectly return zero. This is a direct consistency test rather than a separate new error.

**Proposed treatment and dependents.** Add this as an optional derived lemma after Definition 17.12.10, preserving all original source tags. It supplies a scalar spectral measure with its exact mass/first-moment normalization, useful when comparing finite-energy test curves, their Legendre-ray energies (§17.13.23–24), and later DH-type mass distributions; **no identification with a later DH measure is claimed without checking its conventions**. No main/source/registry change is made.

## §17.18 selected independent normalization checks (not a new finding)

With \(y=\log|\tau|^2\), \(d^cy=d\arg\tau/(2\pi)\), take a locally bounded psh \(\psi\) on \(U\subset\mathbb C^n\) and
\[
 u(z,\tau)=\psi(z)+\log(1+|\tau|^2).
\]
The partial transforms are \(\widehat u_\lambda=\psi-\lambda\log\lambda-(1-\lambda)\log(1-\lambda)\) for \(0<\lambda<1\), with continuous endpoint values \(\psi\), and \(-\infty\) outside \([0,1]\). Thus \((dd^c\widehat u_\lambda)^n=(dd^c\psi)^n\). Since \(dd^c\log(1+|\tau|^2)\) has total mass one on \(\mathbb C^*\), the product expansion gives
\[
 (\pi_U)_*(dd^cu)^{n+1}=(n+1)(dd^c\psi)^n,
\]
matching the formula in Lemma 17.18.1 including the factor \(n+1\). This does not independently validate its general mesh/tail argument. The nonsmooth model \(u=\psi+\max(0,y)\) also warns that an interface can carry mass in a *limit* even though the strictly concave finite-mesh approximants have no first-derivative jump; the original argument retains Bedford–Taylor continuity rather than dropping that limit mass.

## Classification and limitations

No newly confirmed false theorem or full transitive upstream proof-chain certificate arose. §17.12 is a **whole direct current-edition review**; §17.18 a **repeat whole direct recheck**, and §17.14 a **selected dependency check only**. Existing Demailly approximation/regularization and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain **deferred-by-user, neither solved nor certified**. No code builds, software tests, CI, published-page edits, registry edits, main changes, tags or merges were performed.
