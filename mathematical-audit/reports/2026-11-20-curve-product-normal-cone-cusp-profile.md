# Direct mathematical audit: exact normal cone and cusp profiles on products with a curve

**Date:** 2026-11-20  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Integrated file:** docs/sections/bott-chern-classes-and-singular-loci--equations-on-products-with-a-curve/index.html  
**Exact main blob:** d68563036cd1286475ebf2b704999c3e20cff589  
**Scope:** entire mathematical §10.23, physical lines **7–49**, including Theorem 10.23.1 (11–49), equation (10.23.2) (20–22) and equation (10.23.3) (37–39). Section permanent tag FE10733FC7A7; theorem tag 3BB4C60DE3DF; equation tags 464F29927E86 and 1DB31DDE4B07.  
**Context only:** §10.22, docs/sections/bott-chern-classes-and-singular-loci--radial-densities-and-metric-completeness/index.html, blob 239bbc1a79923b3728c535de109261f852efe059. The cited Theorem 13.14.3 and full-mass uniqueness were identified but not independently proved.

## POME-CURVE-PRODUCT-NORMAL-CONE-CUSP-PROFILES-001

**Status:** verified conditional deduction. **Severity:** low. No false printed theorem or missing original proof is alleged. The formulas below strengthen the local normal geometry of the valid Theorem 10.23.1, conditional on its exact radial-density hypotheses, without re-certifying its global Monge–Ampère inputs.

Let the curve factor have normal current
\[
\omega_C+dd^c v=\frac{i}{2\pi}f(r)\,dz\wedge d\bar z,\qquad f=Fg>0
\]
on a punctured coordinate disc around \(p_0\). With the standard Riemannian convention that \((i/2)\,dz\wedge d\bar z\) corresponds to \(dx^2+dy^2\), the normal real metric and area are
\[
g_\perp=\frac{f(r)}{\pi}(dr^2+r^2d\vartheta^2),\qquad
dA_\perp=\frac{f(r)}{\pi}\,dx\,dy.
\]
The full product metric is exactly \(g_\perp\oplus g_N\) there, also when \(\omega_N\) is non-Kähler. Let \(\kappa=C_0/\pi\).

### Power density: exact cone and area

If \(f(r)=C_0r^{2\tau}\), \(\tau>-1\), define
\[
s(r)=\frac{\sqrt\kappa}{\tau+1}\,r^{\tau+1}.
\]
Direct substitution gives **exactly**
\[
g_\perp=ds^2+(\tau+1)^2s^2d\vartheta^2.
\]
The punctured normal metric is flat, its metric completion adds a cone point of total angle \(2\pi(\tau+1)\), and its disk area is
\[
A(r)=\int_{|z|<r}F\omega_C
=\frac{C_0}{\tau+1}r^{2(\tau+1)}
=\pi(\tau+1)s(r)^2.
\]
The product-tube volume is this expression times \(\int_N\omega_N^{n-1}/(n-1)!\). The cone angle can exceed \(2\pi\) for \(\tau>0\): this does **not** assert nondegenerate smoothness of the metric at the added point.

**Proof.** The radial derivative is \(ds/dr=\sqrt\kappa r^\tau\), and \(\sqrt\kappa r^{\tau+1}=(\tau+1)s\), yielding the cone metric. Its Gaussian curvature is zero outside the apex. Since \(dA_\perp=(C_0/\pi)r^{2\tau}dx\,dy\), the polar integral is \(2C_0\int_0^r\rho^{2\tau+1}d\rho\); substituting \(s\) yields the last equality.

### Logarithmic density: curvature, circumference, intrinsic tube volume

Suppose \(f(r)=C_0r^{-2}t^{-b}\), where \(t=\log(1/r)\), \(b>1\). Then the exact normal metric is the conformal cylinder
\[
g_\perp=\kappa t^{-b}(dt^2+d\vartheta^2).
\]
Its circle circumference, normal inner-disk area and Gaussian curvature are
\[
L(t)=2\pi\sqrt\kappa\,t^{-b/2},\qquad
A(t)=\int_{|z|<e^{-t}}F\omega_C
=\frac{2C_0}{b-1}t^{1-b},\qquad
K(t)=-\frac{b}{2\kappa}t^{b-2}.
\]
These are **identities**, not merely asymptotic statements.

If \(b>2\), let \(s\) be the finite radial distance to the missing divisor:
\[
s(t)=\frac{2\sqrt\kappa}{b-2}t^{-(b-2)/2},\qquad
c_b=\frac{2\sqrt\kappa}{b-2}.
\]
Then
\[
L(s)\asymp s^{b/(b-2)},\quad
K(s)=-\frac{2b}{(b-2)^2}s^{-2},\quad
A(s)=\frac{2C_0}{b-1}(s/c_b)^{2(b-1)/(b-2)}.
\]
Thus the normal circumference collapses faster than linearly, with limiting cone angle zero; the intrinsic area exponent is strictly greater than two. The local full metric completion adds the divisor copy of \(N\), with its existing metric.

For \(b=2\), put \(R=\sqrt\kappa\log(t/t_0)\) for a fixed initial \(t_0\). Then
\[
A(R)=\frac{2C_0}{t_0}e^{-R/\sqrt\kappa},\qquad
K=-\frac1\kappa .
\]
The normal end is a complete constant-negative-curvature finite-area cusp.

For \(1<b<2\), the radial distance from \(t_0\) is
\[
R(t)=\frac{2\sqrt\kappa}{2-b}\bigl(t^{(2-b)/2}-t_0^{(2-b)/2}\bigr).
\]
As \(R\to\infty\),
\[
A(R)\asymp R^{-2(b-1)/(2-b)},\qquad
K(R)\sim-\frac{2b}{(2-b)^2}R^{-2}.
\]
This is a complete finite-area horn of asymptotically zero negative curvature; no points of the deleted divisor appear at finite distance.

**Proof.** As \(dr/r=-dt\), the density gives the cylinder metric above. With conformal factor \(\lambda(t)=\kappa t^{-b}\), the normal Gaussian curvature is \(K=-(2\lambda)^{-1}\partial_t^2\log\lambda\). Circle length is \(2\pi\sqrt\lambda\). Polar integration yields
\[
A(t)=2C_0\int_t^\infty u^{-b}du=\frac{2C_0}{b-1}t^{1-b}.
\]
Radial distance is the integral of \(\sqrt\lambda\,dt\). Evaluating it for \(b>2\), \(b=2\), and \(1<b<2\) gives the three formulas. Eliminating \(t\) gives the claimed exact or asymptotic intrinsic profiles. There are no curve/N cross-terms, so the product-completion conclusions follow. For all \(b>1\) the normal circle circumference tends to zero.

## Direct review of the printed proof; limits

The global reduction to the curve \(dd^c\)-equation and the degree-one product identity (Theorem 10.23.1, lines 34–42), the radial zero-flux/no-atom checks (44–46), and the local integrability, boundedness, Hölder, Lelong and completeness thresholds (15–29 and 44–48) have been checked. The displayed primitive \(P_b\) differentiates to \(P_b''=4C_0t^{-b}\), and the metric thresholds agree exactly. The local normal metric is independent of the harmonic correction to the total potential.

**Uncertified upstream inputs:** global solvability of the mean-zero \(dd^c\)-equation on a compact Riemann surface; identification of the extended Monge–Ampère product via Theorem 13.14.3; full-mass Kähler uniqueness; any global barrier arguments beyond the local metric identities. No transitive proof chain is certified and no statement of Theorem 10.23.1 is refuted.

**Proposed correction/action:** optional local geometric corollary explaining the cone/cusp/finite-area profiles. Do **not** alter theorem wording, historical attribution, canonicalization or permanent tags without separate review.

**Affected dependents:** geometric interpretation of Theorem 10.23.1 and comparisons with §10.22 radial completeness examples. **Coverage:** +1 entire directly read section (§10.23, lines 7–49); one selected neighboring §10.22 context check; +0 complete transitive certifications. No historical-first-visit assertion.

Demailly approximation/regularization and its Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes remain **deferred-by-user**, not resolved. No tests/build/CI/site or source changes.
