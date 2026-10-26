# 2026-10-26 — Strong stability of real convex equilibrium measures and the smooth-boundary density endpoint

**Actual checkpoint (UTC):** 2026-10-26T01:06:06.774Z.
**Reviewed reading-edition main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Pre-write mathematical-audit head:** fda6c6f604017ac7acc8ceb90f2c743b632f7621.
**Scope:** first selected proof-level examination of §§16.42.1–16.42.6; supporting checks of §§16.34.2, 16.36.1, 16.33.6. No whole section, full Bedford–Taylor chain, or general energy theorem is certified.

## Exact integrated reading-edition anchors and provenance

- **§16.42:** docs/sections/equilibrium-densities-and-boundaries-of-real-convex-bodies/index.html, main blob **431eebdd82ef03991a95d2f16bb77dfb084278a7**. §16.42.1 Lemma, original Klimek label **68D40FF9**, permanent **CBCC93967447**, lines **10–30**; §16.42.2 Proposition **3C4B5998**, permanent **B7B8F93CC817**, lines **33–49**; §16.42.3 Proposition **D5322D11**, permanent **86440B2CBCE4**, lines **53–105**; §16.42.4 Lemma **58266096**, permanent **16C56B7B3FDA**, lines **109–119**; §16.42.5 Theorem **010CEA22**, permanent **1E10E926515B**, lines **123–163**; §16.42.6 Theorem **F1D83716**, permanent **69C6DC7FA336**, lines **167–216**. These are current *Pome* section/statement numbers, not original-source locators.
- **§16.34.2:** docs/sections/logarithmic-total-mass-and-bounded-obstacle-support/index.html, main blob **47387388cb62e2b99cf6f78370c914aa6f75909d**, original **63C4C42B**, permanent **01D4425BEF42**, lines **47–66** (support and mass).
- **§16.36.1:** docs/sections/the-real-cube-equilibrium-density/index.html, main blob **712e936992d5ae12cca72b83b85561123e932b27**, original **1EE8289D**, permanent **6BA3C254E28C**, lines **7–34** (product arcsine density and normalization).
- **§16.33.6:** docs/sections/real-compact-sets-and-explicit-extremal-formulas/index.html, main blob **a5f8e9cd6aa60a22f344aadbdf8370422ce3220a**, original **545185F6**, permanent **A1B73D6E87D0**, around lines **101 onward** (real-body formula). Historical attribution to the source is preserved.

Conventions throughout: \(dd^c=i\partial\bar\partial/(2\pi)\), \(M=2^{-n}\), \(\mu_K=(dd^c V_K)^n\), and \(dx\) is real \(n\)-dimensional Lebesgue measure. A density is understood to vanish outside its real compact support. For a signed measure \(\nu\), \(\|\nu\|_{\mathrm{TV}}=|\nu|(\mathbb R^n)\), without the probability-theory factor \(1/2\).

## POME-REAL-CONVEX-EQUILIBRIUM-TV-001

**Severity:** low. **Status:** verified conditional deduction; **the printed theorems are not asserted false**.

**Claim.** Let \((K_i)_{i\in I}\) be an arbitrary directed net of compact, centrally symmetric convex bodies in \(\mathbb R^n\), all with nonempty interior, converging in Hausdorff distance to a centrally symmetric convex body \(K\) with nonempty interior. Then
\[
\boxed{\ \|\mu_{K_i}-\mu_K\|_{\mathrm{TV}}
       =\int_{\mathbb R^n}|f_{K_i}(x)\mathbf 1_{K_i}(x)-f_K(x)\mathbf 1_K(x)|\,dx\longrightarrow0.\ }
\]
In fact, for every \(0<r<1\) one has
\[
\sup_{x\in rK}|f_{K_i}(x)-f_K(x)|\longrightarrow0
\]
eventually on that compact core. No boundary smoothness, sequential subnet extraction, or dominated-convergence theorem for nets is required.

**Proof.**

1. Choose \(b>0\) with \(bB\subset K\). Hausdorff convergence and convexity yield numbers \(\epsilon_i\to0\) with
\[
(1-\epsilon_i)K\subset K_i\subset(1+\epsilon_i)K.
\]
For completeness, if \(d_H(K_i,K)<h<b/2\), then \(K_i\supset(b-h)B\), and the two Hausdorff inclusions together with \(hB\subset h(b-h)^{-1}K_i\) and \(hB\subset (h/b)K\) imply both multiplicative containments with \(\epsilon_i\to0\). Polarity reverses them:
\[
(1+\epsilon_i)^{-1}K^\circ\subset K_i^\circ
\subset(1-\epsilon_i)^{-1}K^\circ.
\]

2. Fix \(r<1\). For \(x\in rK\) and \(\eta\in K_i^\circ\),
\[
|x\cdot\eta|\le \frac{r}{1-\epsilon_i}<1
\]
eventually, uniformly. The maps
\[
S_x(\eta)=\frac{\eta}{\sqrt{1-(x\cdot\eta)^2}}
\]
are therefore jointly uniformly continuous in \(x\in rK\) and \(\eta\) in a common compact set of polar slopes. Uniform Hausdorff convergence of \(K_i^\circ\) to \(K^\circ\) implies uniform Hausdorff convergence of the compact images \(S_x(K_i^\circ)\) to \(S_x(K^\circ)\). Convex hull is nonexpansive under Hausdorff distance, so the convex bodies \(H_{i,x}=\operatorname{conv}S_x(K_i^\circ)\) converge to \(H_x=\operatorname{conv}S_x(K^\circ)\) uniformly for \(x\in rK\). Their volumes converge uniformly: the bodies lie in a fixed ball and contain a fixed small ball (indeed \(K_i^\circ\subset S_x(K_i^\circ)\)), so Hausdorff inclusions give uniform multiplicative volume bounds. The exact source formula, Proposition 16.42.3,
\[
f_{K_i}(x)=\frac{n!}{(4\pi)^n}\operatorname{vol}(H_{i,x}),
\]
now proves the claimed local uniform density convergence.

3. Theorem 16.42.6 supplies a **body-independent** boundary-layer bound
\[
\mu_L\{x\in L:m_L(x)\ge s\}\le
\Phi_n(s),\qquad
\Phi_n(s):=\frac{2(n+1)M\log(1/s)}{\operatorname{arcosh}(1/s)}
\longrightarrow0\quad(s\uparrow1)
\]
for every centrally symmetric real convex body \(L\). Because \(K_i\subset(1+\epsilon_i)K\), if \(x\in K_i\setminus rK\), then
\(m_{K_i}(x)\ge m_K(x)/(1+\epsilon_i)\ge r/(1+\epsilon_i)\).
Thus
\[
\begin{aligned}
\|\mu_{K_i}-\mu_K\|_{\mathrm{TV}}
&\le |rK|\sup_{x\in rK}|f_{K_i}(x)-f_K(x)|\\
&\quad+\Phi_n\!\left(\frac{r}{1+\epsilon_i}\right)+\Phi_n(r).
\end{aligned}
\]
For fixed \(r\), the first term tends to zero and continuity of \(\Phi_n\) bounds the eventual upper limit by \(2\Phi_n(r)\). Let \(r\uparrow1\). This proves total-variation convergence along the original directed net, with no interchange of two unproved limits. \(\square\)

**Why the hypotheses matter.** Full-dimensionality of the *limit* is essential for the fixed-core argument; shrinking intervals \([-\epsilon,\epsilon]\) have full equilibrium mass \(1/2\) but no absolutely continuous total-variation limit at the collapsed point. Symmetry is used for both the polar-volume interior formula and the dimension-only boundary-layer bound. This note asserts no analogous theorem for arbitrary nonsymmetric Hausdorff limits.

**Suggested correction/addition:** optional theorem following Theorem 16.42.6; retain the existing theorem, its provenance, and permanent tags. **Affected dependents:** any use of stability of real equilibrium measure under moving symmetric convex obstacles, particularly convergence against merely bounded measurable (not necessarily continuous) test functions. The conclusion is strictly stronger than compact-test weak convergence. The underlying bounded Bedford–Taylor products, real-body formula, polar volume continuity and energy cocycle are conditional upstream inputs, not fully re-proved here.

## POME-SMOOTH-CONVEX-DENSITY-LORENTZ-001

**Severity:** low. **Status:** verified conditional deduction; **Theorem 16.42.5 is correct as used**, not a false theorem.

**Claim.** Let \(K\subset\mathbb R^n\) be a convex body with \(C^2\) boundary, without symmetry or positive curvature assumptions. Then there are \(a_K,b_K,T_K>0\) such that for \(T\ge T_K\),
\[
\boxed{\ a_K T^{-2}\le
|\{x\in K:f_K(x)>T\}|\le b_K T^{-2}.\ }
\]
Consequently
\[
f_K\in L^{2,\infty}(K),\qquad
f_K\notin L^{2,q}(K)\ (0<q<\infty),\qquad
f_K\in L^p(K)\iff 0<p<2.
\]
For every real \(\beta\),
\[
\boxed{\ \int_K\frac{f_K(x)^2}{[\log(e+f_K(x))]^\beta}\,dx<\infty
\quad\Longleftrightarrow\quad\beta>1.\ }
\]
The critical exponents are independent of \(n\); the earlier exact cube-density Lorentz finding POME-CUBE-LORENTZ-ENDPOINT-001 (which has an additional logarithmic tail in dimension \(n>1\)) is **not** repeated and does not contradict this result, since a real cube does not have \(C^2\) boundary in dimension \(n>1\).

**Proof.** Theorem 16.42.5 gives
\[
c_K d(x)^{-1/2}\le f_K(x)\le C_K d(x)^{-1/2}
\quad\text{a.e. on }\operatorname{int}K,
\qquad d(x)=\operatorname{dist}(x,\partial K),
\]
and zero equilibrium mass on \(\partial K\). Its preceding real-analytic approximation lemma (16.42.4) establishes a uniform normal tubular neighborhood for a \(C^2\) convex boundary. In those normal coordinates the Jacobian is
\(J(p,t)=\prod_{j=1}^{n-1}(1-t\kappa_j(p))=1+O(t)\) uniformly. Thus
\[
|\{x\in K:d(x)<s\}|
=s\mathcal H^{n-1}(\partial K)+O(s^2)
\quad(s\downarrow0),
\]
also for \(n=1\) with counting measure on the two endpoints.
Up to null sets, for large \(T\),
\[
\{d<(c_K/T)^2\}\subseteq\{f_K>T\}
\subseteq\{d<(C_K/T)^2\}.
\]
The tube asymptotic proves the two-sided \(T^{-2}\) distribution estimate. Standard layer-cake integration now gives exactly weak \(L^2\), failure of every finite Lorentz \(L^{2,q}\), and \(L^p\)-membership precisely for \(p<2\). In the collar the critical logarithmic integral is comparable to
\[
\int_0^{s_0}\frac{dt}{t[\log(1/t)]^\beta},
\]
which converges precisely when \(\beta>1\); all integrals over the complementary interior are finite by local boundedness.

**Independent exact normalization check:** for the Euclidean real ball \(K=B_R\), Proposition 16.42.3 gives
\[
f_{B_R}(x)=C_R(1-|x|^2/R^2)^{-1/2},
\quad C_R=\frac{n!\operatorname{vol}(B_1)}{(4\pi)^nR^n}.
\]
For \(T>C_R\), directly
\[
|\{f_{B_R}>T\}|=
\operatorname{vol}(B_1)R^n
\left[1-\left(1-\frac{C_R^2}{T^2}\right)^{n/2}\right],
\quad
\lim_{T\to\infty}T^2|\{f_{B_R}>T\}|
=\frac n2\operatorname{vol}(B_1)R^n C_R^2>0.
\]
This checks the exponent and its nonzero tail coefficient without claiming the general \(C^2\) body has a universal leading coefficient. \(\square\)

**Suggested correction/addition:** optional Lorentz/Orlicz corollary after Theorem 16.42.5. **Affected dependents:** selection of \(L^p\), Lorentz and Orlicz data classes for equilibrium measures on smooth real convex obstacles; avoid extrapolating the nonsmooth cube's logarithmic loss to \(C^2\) bodies. Depends on the printed two-sided boundary estimate, its normal-tube geometry, and real/complex MA comparison, each recorded as upstream conditional.

## Coverage and verification boundary

The actual source proof reading covered the determinant normalization in 16.42.1, contact/cube comparisons in 16.42.2, full polar-volume and radial argument in 16.42.3, the **ordinary real convex Gaussian** approximation and normal geometry in 16.42.4 (not the user-excluded Demailly program), the upper/lower barriers and boundary-mass passage in 16.42.5, and the bounded-energy cocycle, projective scaling and quantitative boundary-layer estimate in 16.42.6. The supporting 16.34.2 total-mass and support proof, 16.36.1 cube density, and 16.33.6 real-body formula were checked for conventions and admissible use, not fully independently proved. The prior 16.39.1 foliation/Baran audit is historical and is not recounted as new mathematics.

No new confirmed false printed theorem or proof gap is asserted in this increment. The resulting two mathematical corollaries are verified **conditional deductions**, not certification of Bedford–Taylor product theory, real Monge–Ampère continuity, or the nontrivial global bounded-energy cocycle. Historical attribution and all permanent tags remain intact. Existing errors, unresolved dependencies and prior reports retain their earlier statuses.

**Strict exclusion:** Demailly approximation/regularization, dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof completion are **deferred-by-user**, not reopened, resolved or certified. The §7.31.1 regularization-dependent chain was identified only as excluded context; no audit coverage is claimed for it. No source manuscript, generated body, proof registry, canonicalization, website, GitHub Actions CI, or main-branch write is proposed. This run did not run the project tests, local build or formal proof checks.
