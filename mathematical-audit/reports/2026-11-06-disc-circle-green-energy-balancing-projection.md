# Exact Green energy and orthogonal balayage for concentric circles in the unit disc

- **Finding:** `POME-GREEN-DISC-CIRCLE-ENERGY-PROJECTION-001`
- **Date:** 2026-11-06.
- **Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Classification:** **low / verified conditional deduction**. The printed statements are **not false**. The exact logarithmic kernel, potentials, mutual energies, mass factors, and norm formulas below are independently computed. Identification with the *general* nearest-point principle uses the positive-definite energy property in Theorem 4.5.2 and is therefore a deduction conditional on that established internal input, not a full reproof of the theory.
- **Reading-edition anchor:** `docs/sections/green-energy-and-martin-boundaries/index.html`, blob `976a90f2a5eba299658f73a1eee8b9d3fef8020f`, physical lines 5–17 (energy and positivity), 34–65 (domination and energy-topology theorem), and 76–86 (projection/balayage and compact equilibrium). Source labels/permanent tags: §4.5.1 `classical-potential-theory:5FDF1F52` / `57DD989B07A4`; Theorem 4.5.2 `classical-potential-theory:AEA69819` / `CC3D1AD9179B`; Theorem 4.5.4 `classical-potential-theory:5FB19CB2` / `CE0D5F4DF7B2`; Theorem 4.5.6 `classical-potential-theory:9D70EB64` / `B15EFD960FD5`.
- **Crosscheck:** `docs/sections/planar-green-functions-and-conformal-maps/index.html`, blob `bfee348bb5f4bbfaa4515e5c9333789a13dae861`, physical lines 10–15; Theorem 3.8.1 source `klimek-pluripotential-theory:B1C110E2`, permanent `E2B11E803D94` (Green-function normalization only).

## Model and logarithmic potential, with no appeal to a global energy theorem

Let (D=\{z\in\mathbb C:|z|<1\}\) and use precisely the positive logarithmic Dirichlet Green kernel
[
G_D(z,w)=\log\left|\frac{1-\overline w z}{z-w}\right|,
\qquad -\Delta_zG_D(z,w)=2\pi\delta_w.
]
For (0<r<1), let (μ_r) denote normalized angular probability on the circle (|w|=r):
[
\int f\,dμ_r=(2\pi)^{-1}\int_0^{2\pi}f(re^{i\theta})\,d\theta.
]
Write (a_r=\log(1/r)>0). The logarithmic mean-value identities are
[
\frac1{2\pi}\int_0^{2\pi}\log|z-re^{i\theta}|\,d\theta
=\log\max\{|z|,r\},\qquad
\frac1{2\pi}\int_0^{2\pi}\log|1-r e^{-i\theta}z|\,d\theta=0,
]
the second because (|rz|<1). The first follows by factoring out whichever of (|z|,r) is larger, expanding (ℜ\log(1-\zeta e^{i\theta})) for (|\zeta|<1), and taking limits at equal radii (the logarithmic singularity is integrable). Consequently
[
\boxed{G_Dμ_r(z)=-\log\max\{|z|,r\}\quad(|z|<1).}
\tag{1}
]
This potential is positive, bounded, and continuous, hence (μ_r) has finite energy. Integration on another circle gives
[
\boxed{I(μ_r,μ_s)=-\log\max\{r,s\}
=\min(a_r,a_s),\qquad
\|\u03bc_r-\u03bc_s\|_E^2=|a_r-a_s|.}
\tag{2}
]
Every coefficient is fixed by the explicit Green normalization above; it is *not* a (dd^c)-measure identity.

## Exact projection and Green equilibrium of an interior disc

Fix (0<R<r<1), let (K=\{|z|\le R\}\Subset D), and set (a=\log(1/r)), (b=\log(1/R)), so (0<a<b). Define
[
\boxed{\nu=\frac ab,μ_R.}\tag{3}
]
Equation (1) implies (G_D\nu=(a/b)(-\log\max\{|z|,R\})). For (|z|\le R), both (G_D\nu) and (G_Dμ_r) equal (a). On (R<|z|<r), the first is ((a/b)\log(1/|z|)\le a), whereas the latter is (a). On (r\le|z|<1), the first is ((a/b)\log(1/|z|)\le\log(1/|z|)=G_Dμ_r). Hence
[
G_D\nu\le G_Dμ_r\text{ everywhere on }D,\qquad
G_D\nu=G_Dμ_r\text{ pointwise on }K.\tag{4}
]
For **every** finite-energy positive measure (η) supported on (K), (4) gives
(I(μ_r-\nu,η)=0), in particular (I(μ_r-\nu,\nu)=0).
By the positive-definite inner product on signed finite-energy measures from Theorem 4.5.2,
[
\|\u03bc_r-η\|_E^2
=\|\u03bc_r-\nu\|_E^2+\|\u03b7-\nu\|_E^2
\ge\|\u03bc_r-\nu\|_E^2.\tag{5}
]
The minimizer is unique. Thus (3) is the **actual unrestricted** orthogonal projection of (μ_r) onto the whole positive cone supported on (K), not merely onto radial measures; by Theorem 4.5.6 it coincides with balayage (μ_r^K). Directly from (2),
[
\boxed{\nu(K)=a/b,\qquad
\|\u03bc_r-\nu\|_E^2=a-a^2/b.}\tag{6}
]
Equilibrium also follows directly: (G_Dμ_R=b) on (K). For any finite-energy probability (η) on (K), (I(μ_R,η)=b); Cauchy–Schwarz and (I(μ_R)=b) imply (I(η)\ge b), with equality only for (η=μ_R). Thus the relative Green capacity is
[
\boxed{C_D(K)=1/b=1/\log(1/R),\qquad μ_K=\u03bc_R/b,\qquad\nu=a\u03bc_K.}\tag{7}
]
Here (μ_K) denotes the capacity-equilibrium measure of mass (C_D(K)), *not* the probability (μ_R).

## Two topology checks and an essential distinction

If (r_j\to r\in(0,1)) with (r_j\ne r), (2) gives (μ_{r_j}\toμ_r) **strongly in energy**, whereas their mutually disjoint circle supports imply
[
\|\u03bc_{r_j}-μ_r\|_{\mathrm{TV}}=2
\quad\text{for every }j.
]
Thus the positive-cone strong-energy topology in Theorem 4.5.4 must **not** be silently upgraded to total-variation convergence. If (r_j\uparrow1), (2) gives (μ_{r_j}\to0) strongly in energy because (μ_{r_j}) has energy (a_{r_j}\to0); however each (μ_{r_j}(D)=1), and the measures converge only vaguely to zero on (D) by escape through the boundary. This is consistent with the stated *vague* topology and illustrates why no total-mass conclusion follows on a noncompact Greenian domain.

For a finite signed combination (σ=\sum_{j=1}^m c_jμ_{r_j}), put (t_j=a_{r_j}). The exact Gram kernel yields the additional nonnegative-energy identity
[
I(σ)=\sum_{i,j}c_ic_j\min(t_i,t_j)
=\int_0^{\infty}\left(\sum_{j:t_j\ge u}c_j\right)^2du\ge0.\tag{8}
]
This checks signed positivity on this concrete family directly, including cancellation, without assuming any sequential-compactness or interchange of unbounded limits.

## Disposition and dependency ledger

No printed theorem was refuted or fully certified. This is new selected model coverage of §4.5.2, §4.5.4 and §4.5.6, including an exact **nonradially restricted** nearest-point argument. The general theorem that signed Green energy is positive-definite remains the internal hypothesis in the unrestricted projection step (5); the disk Green identity (1), mutual energy (2), explicit potential order (4), mass and norm (6), and topology examples are independent calculations. No source, registry, permanent tag, or publishing change is proposed. A useful optional reading-edition illustration is to append (1)–(7) as an example near §4.5.6, preserving all existing results and provenance. It is **not** an instruction to change the production text.
