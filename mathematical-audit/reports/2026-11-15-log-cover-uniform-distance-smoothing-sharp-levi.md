# 2026-11-15 — an explicit distance-level, sheet-uniform smoothing and sharp Levi floor on exponential coverings

**Finding ID:** POME-COVER-LOG-UNIFORM-DISTANCE-SHARP-LEVI-001. **Status:** low / verified conditional deduction (the displayed model and bounds are directly proved; this is not a false production theorem, applied repair, or full verification of the general theorem). **Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; **audit parent branch HEAD at creation:** \`1740dd07663ff23297ac41f8fe2fdf269b302265\`. **Scope:** a new quantitative test of the *simultaneous* approximation, uniform-sheet derivative, exhaustion, and positivity conclusions in §9.28, in every complex dimension. Distinct from \`POME-COVER-PULLBACK-PROPERNESS-DICHOTOMY-001\` (2026-11-01), which used \`epsilon |z|^2\` as an illustrative correction but did not meet the bounded-distance-from-lifted-distance or sheet-uniform positive-derivative requirements; and from \`POME-COVER-PSH-COMPLETE-KAHLER-COMPOSITION-001\` (2026-11-02), which concerned metric completeness of convex compositions.

## Integrated reading-edition evidence

- Main \`docs/sections/separation-strict-exhaustions-and-coverings--strictly-plurisubharmonic-exhaustions-on-coverings/index.html\`, blob \`ef92b5dc5bb4c143345621ea60ca52f3ca7d1872\`. Section permanent tag \`5FA7A48903C4\`, underlying source \`demailly-complex-geometry\`.
- Proposition 9.28.2, source label \`CD2B2989\`, permanent tag \`E200BE9CFD9E\`, physical lines 30–45: completeness of the lifted length metric and properness of the lifted distance function.
- Proposition 9.28.3, source \`09F8EE91\`, permanent \`7808CCD76C79\`, lines 48–101, especially convolution bounds 59–76, cancellation 84–90 and base-form lower bound 92–98. It requires \`|delta-delta_0|<=1\` *and* uniform positive-order base-coordinate derivatives over all covering sheets; a mere arbitrary smooth proper bump does not check these.
- Theorem 9.28.5, source \`F653208F\`, permanent \`73159A8CF2BB\`, physical lines 104–142, especially the convexly reweighted strictness/properness step 121–140.
- Context only: \`docs/sections/separation-strict-exhaustions-and-coverings--local-holomorphic-separation-and-strict-exhaustion/index.html\`, blob \`c04701d0358d43a3a3f1aed61e7cdd2a48305417\`, §9.26's finite-continuous-exhaustion convention. Its lemma/proof chain was not audited afresh. The purely structural §9.25 page \`docs/sections/separation-strict-exhaustions-and-coverings/index.html\`, blob \`89f1c30a6df3c3df624fd05943a5cc64460824b8\`, permanent \`D10F3B8AA2A1\`, contains no theorem and earns no new mathematical coverage.

## Explicit model and full proof

Let \(m\ge1\), \(X=(\mathbb C^*)^m\), \(Y=\mathbb C^m\), and
\[
 \pi(z_1,\ldots,z_m)=(e^{z_1},\ldots,e^{z_m}).
\]
This is a connected holomorphic unramified covering. Equip \(X\) with the **real** complete Riemannian length metric
\[
 ds_g^2=\sum_{j=1}^m|dw_j/w_j|^2.
\]
Its lift is the Euclidean metric \(\sum|dz_j|^2\), so with \(y_0=0\),
\(\delta_0(z)=|z|\). Completeness of the base is elementary from the metric product of the complete cylinders \(\mathbb R\times(\mathbb R/2\pi\mathbb Z)\), with coordinates \((\log|w_j|,\arg w_j)\); no general Hopf–Rinow theorem is needed.

Define
\[
 \boxed{\delta(z)=\sqrt{1+|z|^2}},\qquad
 \boxed{\psi(w)=\sum_{j=1}^m(|w_j|^2+|w_j|^{-2})},\qquad
 \boxed{F(z)=\delta(z)+\psi(\pi z)}.
\]
The exact distance approximation is
\[
 0<\delta-\delta_0=\frac1{\sqrt{1+|z|^2}+|z|}\le1.
\]
All its closed sublevels are Euclidean balls; hence \(\delta\) is a smooth proper exhaustion. In standard real Euclidean coordinates, every derivative \(D^\nu\delta\) of **positive** order is globally bounded. For clarity, \(|\nabla\delta|=|z|/\sqrt{1+|z|^2}\le1\). Repeated differentiation of \((1+|z|^2)^{1/2}\) gives finite linear combinations of polynomials divided by positive powers of \(1+|z|^2\); for \(|\nu|=k\ge1\), the bound is \(O((1+|z|)^{1-k})\). In particular all derivatives of order at least one are bounded uniformly on \(\mathbb C^m\).

To interpret *uniformity over sheets*, fix a relatively compact holomorphic coordinate chart \(U\Subset(\mathbb C^*)^m\) carrying holomorphic logarithms \(L_j(w_j)\). All inverse sheets over \(U\) are
\(z=L(w)+2\pi i k\), \(k\in\mathbb Z^m\). On each compact \(K\Subset U\), the derivatives of \(L\) of any fixed order are bounded independently of \(k\). The chain rule and the global positive-order bounds just proved show
\[
 \sup_{k\in\mathbb Z^m}\sup_{w\in K}
 |D_w^\nu(\delta(L(w)+2\pi i k))|<\infty,\qquad |\nu|\ge1.
\]
The corresponding **zero-order** supremum is infinite; the positivity of the derivative order is crucial, just as in Proposition 9.28.3.

Use \(H_u=(\partial^2u/\partial z_j\partial\bar z_k)\), the Hermitian coefficient matrix underlying \(dd^c u=(i/2\pi)\partial\bar\partial u\). Put \(s=|z|^2\), \(h(s)=\sqrt{1+s}\). Direct differentiation gives
\[
 H_\delta=h'(s)I+h''(s)\,\bar z\otimes z,\quad
 h'(s)=\frac1{2\sqrt{1+s}},\qquad
 h''(s)=-\frac1{4(1+s)^{3/2}}.
\]
Thus for \(z\ne0\) the radial complex eigenvalue and transverse eigenvalues are respectively
\[
 \lambda_\parallel(s)=h'(s)+s h''(s)
   =\frac{s+2}{4(1+s)^{3/2}}>0,\qquad
 \lambda_\perp(s)=\frac1{2\sqrt{1+s}}>0
\]
(the transverse eigenvalue has multiplicity \(m-1\)); at \(z=0\) all eigenvalues equal \(1/2\). This proves \(\delta\) is strictly psh, with \(H_\delta\ge0\) and a sheet-independent upper Hessian bound. Any positive Hermitian form \(\gamma\) on the base consequently satisfies \(H_\delta\ge-\pi^*\gamma\), so the actual lower-bound conclusion of Proposition 9.28.3 holds directly.

Next, for each \(w_j\in\mathbb C^*\),
\[
 \frac{\partial^2}{\partial w_j\partial\bar w_j}
 (|w_j|^2+|w_j|^{-2})=1+|w_j|^{-4}>0.
\]
The base function \(\psi\) is smooth strictly psh and exhaustive, because each sublevel confines every \(|w_j|\) to a closed annulus bounded away from zero and infinity. Its pullback is
\[
 \psi(\pi z)=\sum_j(e^{2\Re z_j}+e^{-2\Re z_j}),\qquad
 H_{\psi\circ\pi}=\operatorname{diag}(e^{2\Re z_j}+e^{-2\Re z_j})\ge2I.
\]
Consequently
\[
 \boxed{H_F\ge2I\quad\hbox{on all of }\mathbb C^m.}
\]
The constant **2 is the exact infimum of the least eigenvalue for this displayed \(F\)**: along \(z=(it,0,\ldots,0)\) as \(t\to+\infty\), every base Hessian coefficient is exactly \(2\), while all eigenvalues of \(H_\delta\) tend to zero. We claim optimality only for this explicit \(F\), not for all possible covering exhaustions or arbitrary normalization of the metric.

Finally \(F\ge\sqrt{1+|z|^2}+2m\). Every closed finite sublevel of \(F\) is closed and contained in a Euclidean closed ball, hence compact; \(F\) is an exhaustion. This proves in all dimensions, by direct calculation, the **simultaneous** distance approximation, sheet-uniform positive-order derivative estimates, lower Hermitian Hessian control, and smooth strictly-psh properness. In contrast, \(\psi\circ\pi\) alone is not proper because it is invariant under the infinite deck translations \(z\mapsto z+2\pi i k\), which is the already-known 2026-11-01 dichotomy and is **not** counted as new.

## Mathematical status and action

- **Status:** POME-COVER-LOG-UNIFORM-DISTANCE-SHARP-LEVI-001 — low / verified conditional deduction; the computations are self-contained, with no excluded analytic input. The original Proposition 9.28.2, Proposition 9.28.3 and Theorem 9.28.5 survive this concrete stress test. No false statement or proof gap is claimed, no original theorem is modified, and the general covering-space theorem has *not* been transitively verified.
- **New aspect:** matching the exact \(L^\infty\) distance error and *all positive-order sheet-uniform derivatives* while obtaining a globally **sharp for this \(F\)** Levi lower bound \(2I\) on a rank-\(m\) infinite covering. The earlier \(\epsilon |z|^2\) correction was not bounded distance from \(\delta_0\) and had unbounded first derivatives on distant sheets.
- **Proposed optional correction/editorial insertion:** give these formulas as a short quantitative example after Proposition 9.28.3 or Theorem 9.28.5. No statement correction is necessary. Retain all permanent labels and historical attribution.
- **Affected dependents:** the metric-distance smoothing and strict-exhaustion arguments of §§9.28.2–9.28.5; optional models for §9.26 exhaustion convention. No downstream Stein, jet interpolation, analytic approximation, or general metric completeness theorem is certified by this test.
- **Coverage:** detailed independent model calculation and selected comparison with specified integrated paragraphs, not a whole-section proof verification. Section 9.28 was **previously partly audited**; §9.25 was already inspected structurally. **+0 newly first-visited mathematical sections; +0 fully certified sections**. Current chapter/section inventory 25/747.
- **Deferred-by-user:** Demailly approximation/regularization and dedicated Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programmes remain deferred, not solved, revisited, or certified.
- **Verification:** analytic derivatives checked on paper and the radial spectral formula sampled numerically at \(s=0,1,4,100,10^4\) locally; the samples are **not** proof. No repository build, project tests, CI, GitHub Actions or website publication were performed.
