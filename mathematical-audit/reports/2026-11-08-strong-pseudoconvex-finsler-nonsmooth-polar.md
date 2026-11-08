# 2026-11-08 — A smooth strongly pseudoconvex Finsler metric with a nonsmooth strongly convex polar

**Finding ID:** POME-FINSLER-POLAR-NONSMOOTH-STRONGLY-PSCONVEX-001. **Severity:** low. **Status:** verified conditional deduction / sharpness example; **not** a false printed theorem and **not** a repair of the existing compactness gap.

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Integrated reading edition:** `docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--polar-norms-of-semipositive-finsler-metrics/index.html`, blob `9d8c639c4460719360048213e58aa08138dd1a71`. Relevant statements: Lemma **11.12.1**, source `non-kahler-pluripotential-theory:14B27C66`, permanent tag `82E28EBCB904`, physical lines **28–65**; Proposition **11.12.2**, source `non-kahler-pluripotential-theory:F21E637C`, permanent tag `672C05CD55F8`, lines **69–99**; Lemma **11.12.3**, source `non-kahler-pluripotential-theory:86EFA793`, permanent tag `BD7ECB0F942E`, lines **101–143**. Corollary **11.12.6**, source `non-kahler-pluripotential-theory:44897B42`, permanent tag `3DE300A9B2AD`, lines **145–155**, is only a downstream contextual read; its smoothing argument is not reviewed.

## Precise statement

Let `X` be any compact connected complex manifold, e.g. an elliptic curve, and let `E=X\times\mathbb C^2` be the trivial holomorphic bundle. On every nonzero fiber set
\[
G(v_1,v_2)=|v_1|^2+|v_2|^2+
\frac{2|v_1|^2|v_2|^2}{|v_1|^2+|v_2|^2},
\qquad G(0)=0.
\]
Then:
1. `G` is positive, smooth on `E^\times`, complex homogeneous of degree two, and **strongly pseudoconvex**: its vertical complex Hessian is positive definite everywhere on `E^\times`.
2. The Kobayashi curvature (in the convention of §11.12, lines 19–25) is **identically zero**, because `G` is independent of base coordinates. Nevertheless `G` is **not real convex** in fiber variables.
3. The polar square
\[
Q(\xi)=\sup_{v\ne0}\frac{|\xi(v)|^2}{G(v)}
\]
is positive, continuous, complex homogeneous, plurisubharmonic, and **uniformly strongly real convex** on each dual fiber in the sense of Lemma 11.12.3. But `Q` is **not differentiable at the nonzero covector** \(\xi_0=(1,1)/\sqrt2\). In fact
\[
 Q(\xi_0)=\frac{1+\sqrt3}{4},
\]
and there are two distinct maximizing projective directions. Consequently one cannot deduce smoothness, `C^1`-regularity or uniqueness of the polar maximizer from the smoothness, vertical strict plurisubharmonicity and semipositive Kobayashi curvature of `G`, even over a **compact** base.

## Complete proof and exact calculations

Put \(x=|v_1|^2\), \(y=|v_2|^2\), \(r=x+y>0\), and \(q=xy/r\). The Hermitian matrix of the vertical Levi form of \(q\) is
\[
H_q=
\begin{pmatrix}
y^2(y-x)/r^3 & 2xy\,\overline{v_1}v_2/r^3\\
2xy\,v_1\overline{v_2}/r^3 & x^2(x-y)/r^3
\end{pmatrix}.
\]
Direct expansion gives
\[
\operatorname{tr}H_q=\frac{(x-y)^2}{r^2}\ge0,
\qquad
\det H_q=-\frac{x^2y^2}{r^4}.
\]
Since \(H_G=I+2H_q\), one has
\[
\operatorname{tr}H_G=2+2(x-y)^2/r^2>0,\qquad
\det H_G=1+2(x-y)^2/r^2-\frac{4x^2y^2}{r^4}\ge\frac34>0,
\]
because \(xy\le r^2/4\). Both eigenvalues of the Hermitian matrix `H_G` are therefore strictly positive. Base derivatives vanish, so its Schur complement `S` is zero and \(\mathcal K_G=0\). Complex homogeneity and positivity are immediate from the formula.

On the real affine line \(v(t)=(1+t,1-t)\),
\[
G(v(t))=2(1+t^2)+\frac{(1-t^2)^2}{1+t^2}
=3-t^2+O(t^4).
\]
The second real derivative at the origin is \(-2<0\), hence `G` is not real convex.

For \(\xi_0=(1,1)/\sqrt2\), normalize \(|v_1|^2+|v_2|^2=1\) and put \(t=2|v_1||v_2|\in[0,1]\). The triangle inequality for \(\xi_0(v)\) is an equality for two nonnegative real coordinates; thus
\[
Q(\xi_0)=\max_{0\le t\le1}\frac{1+t}{2+t^2}.
\]
The derivative has numerator \(2-2t-t^2\), so the unique maximizing value is
\[
t_*=\sqrt3-1\in(0,1),\qquad
\frac{1+t_*}{2+t_*^2}=\frac{1+\sqrt3}{4}.
\]
Choose \(a>b>0\) with \(a^2+b^2=1\) and \(2ab=t_*\). Both \(u=(a,b)\) and \(u'=(b,a)\) attain the maximum, are not complex-proportional, and have equal `G`-values. Write \(h=(1,-1)/\sqrt2\) and for fixed \(u\) set \(R_u(\varepsilon)=|(\xi_0+\varepsilon h)(u)|^2/G(u)\). At \(\varepsilon=0\), \(R_u(0)=Q(\xi_0)\) while
\[
R'_u(0)=\frac{(a+b)(a-b)}{G(u)}>0.
\]
For every positive \(\varepsilon\),
\[
Q(\xi_0+\varepsilon h)\ge R_u(\varepsilon).
\]
Consequently the lower right Dini derivative of `Q` along `h` is positive. But swapping the coordinates of `v` leaves `G` invariant and swaps \(\xi_0+\varepsilon h\) with \(\xi_0-\varepsilon h\), hence
\[
Q(\xi_0+\varepsilon h)=Q(\xi_0-\varepsilon h).
\]
If `Q` were differentiable at \(\xi_0\), this even restriction to the `h`-line would have derivative zero, contradicting the positive lower right derivative. Thus `Q` is not `C^1` at \(\xi_0\).

For clarity the *strong convexity* assertion is not deduced from differentiability. On the compact fiber unit sphere, `G` is positive and its real Hessian has a finite upper bound \(D^2_{\mathbb R}G\le2L I\). Homogeneity propagates this bound off zero, and `G` extends `C^1` across zero with derivative zero, so integration along real segments yields
\[
G(v+w)\le G(v)+dG(v)[w]+L|w|^2.
\]
Optimization over complex scalar multiples of `v` gives the exact nonconvex Legendre identity
\[
Q(\xi)=\max_v\bigl(2\operatorname{Re}\xi(v)-G(v)\bigr).
\]
At any dual covector \(\xi\), select an arbitrary maximizer `v`; stationarity and the preceding quadratic upper bound imply
\[
Q(\xi+\eta)\ge Q(\xi)+2\operatorname{Re}\eta(v)+L^{-1}|\eta|^2.
\]
Subtracting \(L^{-1}|\xi+\eta|^2\) supplies a global affine support to \(Q-L^{-1}|\cdot|^2\) at every point, so that function is convex. Nonuniqueness of the maximizer is permitted. Finally, \(\log Q\) is plurisubharmonic away from the zero section: for each fixed nonzero fiber `v`, \(\log|\xi(v)|^2-\log G(v)\) is psh and the locally uniformly bounded-above supremum equals the continuous \(\log Q\); similarly `Q` is psh (and continuous at zero). Equivalently, Proposition 11.12.2 applies because \(\mathcal K_G=0\).

## Classification, proposed correction and dependencies

**Not a theorem error:** Printed Proposition 11.12.2 and Lemma 11.12.3 assert only psh and *real strong convexity*, never smoothness of the polar. This example explains why those conclusions must not be silently upgraded to a smooth polar metric, even with strong pseudoconvexity and flat Kobayashi curvature. A short optional remark following Lemma 11.12.3 could state the sharpness, with the formula above; no source edit is made here. Its **downstream relevance** is Corollary 11.12.6, which invokes a separately stated smoothing construction: this example shows there is a real need for a separate smoothing input; **that proof has not been certified here**, and no excluded Demailly approximation/regularization programme is reopened.

**Existing finding preserved:** `POME-FINSLER-POLAR-GLOBAL-MARGIN-001` (2026-10-27) remains the distinct *medium confirmed error under unqualified noncompact-base hypotheses*. It concerns global uniformity across the base; the present example works on a **compact** base and concerns **nondifferentiability along a fiber**, not missing compactness.

**Precise coverage:** re-read integrated §11.12 setup, Lemma .1 and Proposition .2 hypotheses, and proved the new explicit model against Lemma .3; contextual Corollary .6 only. This is **additive selected theorem-level scrutiny of an already partly audited ToC section**: **0 first section visits, 0 full mathematical-section certifications**, actual 25 chapters/747 sections/0 certified. No full underlying global Finsler theory, smoothing, external theorem, or transitive dependency certified. All earlier unresolved and deferred-by-user findings remain classified as before. No builds, tests, GitHub Actions, website publication, or changes to production main, source text, canonicalization, permanent tags or registries.