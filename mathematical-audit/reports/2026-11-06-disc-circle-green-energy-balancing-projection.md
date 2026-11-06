# Exact Green energy and orthogonal balayage for concentric circles in the unit disc

- **Finding:** \`POME-GREEN-DISC-CIRCLE-ENERGY-PROJECTION-001\`
- **Date:** 2026-11-06.
- **Reviewed production \`main\`:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- **Classification:** **low / verified conditional deduction**, not a false printed theorem. The disc kernel, potentials, mutual energies and projection candidate are independently calculated. Identifying the candidate as the *unrestricted* positive-cone projection uses the established positive-definite energy inner product in Theorem 4.5.2; this is not a complete independent proof of the general theory.
- **Reading-edition anchors:** \`docs/sections/green-energy-and-martin-boundaries/index.html\`, blob \`976a90f2a5eba299658f73a1eee8b9d3fef8020f\`; §4.5.1 physical lines **5–13**, source \`classical-potential-theory:5FDF1F52\`, permanent \`57DD989B07A4\`; Theorem **4.5.2**, lines **16–29**, \`classical-potential-theory:AEA69819 / CC3D1AD9179B\`; Theorem **4.5.4**, lines **46–65**, \`:5FB19CB2 / CE0D5F4DF7B2\`; Theorem **4.5.6**, lines **76–86**, \`:9D70EB64 / B15EFD960FD5\`.
- **Normalization crosscheck:** \`docs/sections/planar-green-functions-and-conformal-maps/index.html\`, blob \`bfee348bb5f4bbfaa4515e5c9333789a13dae861\`, Theorem **3.8.1**, physical lines **10–15**, \`klimek-pluripotential-theory:B1C110E2 / E2B11E803D94\`.

## Exact disc potential and energy Gram kernel

Let \(D=\{z\in\mathbb C:|z|<1\}\). Use the positive Dirichlet Green kernel, in the normalization of §3.8.1,
\[
G_D(z,w)=\log\left|\frac{1-\overline w z}{z-w}\right|,
\qquad -\Delta_zG_D(z,w)=2\pi\delta_w.
\]
For \(0<r<1\), let \(\mu_r\) be normalized angular probability on \(|w|=r\):
\[
\int f\,d\mu_r=\frac1{2\pi}\int_0^{2\pi}f(re^{i\theta})\,d\theta,
\qquad a_r=\log(1/r)>0.
\]
The two circle means are
\[
\frac1{2\pi}\int_0^{2\pi}\log|z-re^{i\theta}|\,d\theta
=\log\max\{|z|,r\},\qquad
\frac1{2\pi}\int_0^{2\pi}\log|1-re^{-i\theta}z|\,d\theta=0.
\]
Indeed, factoring out the larger radius reduces the first to the mean of
\(\operatorname{Re}\log(1-\zeta e^{i\theta})\) for \(|\zeta|<1\), which is zero by its absolutely convergent Taylor series. At equal radii the integrable logarithmic singularity gives the same result by a limit. The second mean has \(|rz|<1\). Consequently, for *every* \(z\in D\),
\[
\boxed{G_D\mu_r(z)=-\log\max\{|z|,r\}.}\tag{1}
\]
This potential is bounded and continuous. Integrating on \(|z|=s\) gives
\[
\boxed{I(\mu_r,\mu_s)=\min\{a_r,a_s\},\quad
I(\mu_r)=a_r,\quad
\|\mu_r-\mu_s\|_E^2=|a_r-a_s|.}\tag{2}
\]
These are exact finite-energy identities; no general convergence theorem was invoked.

## An unrestricted compact-support projection

Fix \(0<R<r<1\), and write \(K=\{|z|\le R\}\Subset D\),
\(a=\log(1/r)\) and \(b=\log(1/R)\), with \(0<a<b\).
Define the positive measure
\[
\boxed{\nu=\frac ab\,\mu_R.}\tag{3}
\]
By (1), for \(|z|\le R\) both \(G_D\nu\) and \(G_D\mu_r\) equal \(a\).
For \(R<|z|<r\), \(G_D\nu=(a/b)\log(1/|z|)\le a=G_D\mu_r\);
for \(r\le|z|<1\), \(G_D\nu=(a/b)\log(1/|z|)\le\log(1/|z|)=G_D\mu_r\).
Therefore
\[
G_D\nu\le G_D\mu_r\ \text{on }D,\qquad
G_D\nu=G_D\mu_r\ \text{pointwise on }K.\tag{4}
\]

For any *arbitrary*, not necessarily rotationally invariant, finite-energy positive measure \(\eta\) supported on \(K\),
\[
I(\mu_r-\nu,\eta)=0,\qquad I(\mu_r-\nu,\nu)=0.
\]
Using positivity of signed Green energy from the internal Theorem 4.5.2, expansion gives
\[
\|\mu_r-\eta\|_E^2
=\|\mu_r-\nu\|_E^2+\|\eta-\nu\|_E^2
\ge\|\mu_r-\nu\|_E^2.\tag{5}
\]
Strict definiteness gives uniqueness. Thus \(\nu\) is the **unrestricted energy projection** onto the *whole* cone of finite-energy positive measures supported on \(K\); Theorem 4.5.6 identifies it with the balayage \(\mu_r^K\). Direct calculation from (2) gives
\[
\boxed{\nu(K)=\frac ab,\qquad
\|\mu_r-\nu\|_E^2=a-\frac{a^2}{b}.}\tag{6}
\]

Moreover \(G_D\mu_R=b\) on \(K\). If \(\eta\) is any finite-energy *probability* supported on \(K\), then \(I(\mu_R,\eta)=b\); Cauchy–Schwarz and \(I(\mu_R)=b\) yield \(I(\eta)\ge b\), with equality only for \(\eta=\mu_R\). Thus
\[
\boxed{C_D(K)=\frac1b=\frac1{\log(1/R)},\qquad
\mu_K=\frac{\mu_R}{b},\qquad \nu=a\mu_K.}\tag{7}
\]
Here \(\mu_K\) is the **capacity equilibrium measure** (of mass \(1/b\)); \(\mu_R\) is the minimum-energy *probability*. This distinction is essential when matching §4.5.6's capacity convention.

## Strict separation of energy and total-variation topologies

If \(r_j\to r\in(0,1)\), \(r_j\ne r\), then (2) gives strong energy convergence
\(\mu_{r_j}\to\mu_r\). But two distinct circles carry mutually singular probability measures, so
\[
\boxed{\|\mu_{r_j}-\mu_r\|_{\mathrm{TV}}=2\quad\text{for all }j.}
\]
Strong positive-cone energy convergence **does not imply total-variation convergence**. If instead \(r_j\uparrow1\), then \(I(\mu_{r_j})=\log(1/r_j)\to0\), so \(\mu_{r_j}\to0\) strongly in energy even though every \(\mu_{r_j}\) has total mass one: their supports escape the boundary, and the convergence is only vague inside \(D\).

For any finite signed combination \(\sigma=\sum_{j=1}^m c_j\mu_{r_j}\), putting \(t_j=a_{r_j}\), (2) also gives the directly nonnegative Gram identity
\[
\boxed{I(\sigma)=\sum_{i,j}c_ic_j\min(t_i,t_j)
=\int_0^\infty\left(\sum_{j:t_j\ge u}c_j\right)^2du\ge0.}\tag{8}
\]
This checks signed-energy positivity on the explicit radial span without assuming sequential compactness or changing any limiting order.

## Status, proposed addition and unresolved inputs

The original Theorems 4.5.2, 4.5.4 and 4.5.6 remain **unrefuted**. The result is a precise model calculation and conditional deduction, not an independent certification of arbitrary-domain Green-energy positivity, completeness or sweeping. Equations (1)–(4), (6), and the topology counterexample are independent computations; unrestricted projection (5) uses the general positive-energy input, and the terminology of balayage uses the printed Theorem 4.5.6. An optional separately reviewable source addition would place (1)–(7) as an example beside Theorem 4.5.6; no production/source/canonical/registry or tag changes were made. No excluded regularization/Bergman/weighted-L²/OT/multiscale/positivity-loss work was reopened.
