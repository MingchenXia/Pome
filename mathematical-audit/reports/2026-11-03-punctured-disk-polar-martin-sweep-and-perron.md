# Polar Martin boundary: exact compact sweeping and Perron invisibility on a punctured disk (2026-11-03)

**Finding:** POME-MART-PUNCTURE-SWEEP-PERRON-POLAR-001  
**Status / severity:** low / **verified conditional deduction** (a new compact-sweep density and polar-boundary Perron model; no false printed theorem, no general Martin proof certification).  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Target branch:** review/mathematical-audit.

## Exact integrated sources and prior-work boundary

The current main integrated reading page is
docs/sections/green-energy-and-martin-boundaries/index.html,
blob 976a90f2a5eba299658f73a1eee8b9d3fef8020f.

- Lemma **4.5.8**: source classical-potential-theory:AB110663; permanent tag D878F27BAB16; physical lines **94–102** (evaluation compactification).
- Theorem **4.5.9**: source classical-potential-theory:1677A9F0; permanent tag 9D6B5CF5E0CF; lines **106–122** (cutoff normalization and joint continuity).
- Lemma **4.5.10**: source classical-potential-theory:F432655F; permanent tag B0A113187C30; lines **126–149** (compact sweeping, normalized representing measure).
- Theorem **4.5.12**: source classical-potential-theory:57D18B4C; permanent tag 6736FBE7368C; lines **165–185** (minimal Martin boundary and representation).
- Theorem **4.5.13**: source classical-potential-theory:854603A2; permanent tag 0E65F552B1A6; lines **189–214** (continuous Perron data and ball Poisson kernel).

**Nonduplicate scope.** The prior POME-MART-EXTERIOR-BALL-INFINITY-001 already deduced the end kernels of an exterior ball using Kelvin inversion, which is conformally equivalent in dimension two to a punctured disk. The boundary *kernel alone* is therefore **not** a new finding. This report instead computes the previously unchecked **exact weighted compact sweep of the polar-end kernel** (including its density and normalization in the cutoff-dependent Martin coordinates), and proves directly that a continuous Perron datum at this *minimal* boundary point has **zero effect** on the Perron solution. The earlier projective compact-sweep consistency item POME-MART-SWEEP-PROJECTIVE-001 addressed abstract uniqueness, not this concrete polar-end computation.

## Setup and complete formulae

Let D be the unit disk in the complex plane, Omega = D\{0}, and fix a in Omega. Put L = log(1/|a|)>0 and d sigma_r(theta)=d theta/(2 pi) on the circle C_r={|z|=r}. The Dirichlet Green function for Omega equals that of D, since a point is polar:
\[
 G_D(z,w)=\kappa\log\left|\frac{1-\overline w z}{z-w}\right|,\qquad \kappa>0.
\tag{1}
\]
The normalization constant is the one dictated by -Delta G=c_2 delta; it cancels in all Martin ratios. If b=phi(G_D(\cdot,a)) is the cutoff potential in lines 106–110, then b(y)=G_D(y,a) near **both** the puncture and the unit circle. For sufficiently small r<|a|, the entire C_r lies where this equality holds.

The Martin compactification is the closed disk, with interior D\{0} and boundary Delta={0} union S^1. Its normalized kernels are
\[
 K_0(z)=\frac{\log(1/|z|)}{L},\qquad
 K_\zeta(z)=\frac{P(z,\zeta)}{P(a,\zeta)},\quad
 P(z,\zeta)=\frac{1-|z|^2}{|z-\zeta|^2},\quad |\zeta|=1.
\tag{2}
\]
Every boundary kernel equals 1 at a and is minimal, hence Delta_1=Delta.

For every sufficiently small r, the compact reduction of the **polar-end** kernel to C_r is exactly
\[
 \widehat R_{C_r}K_0(z)
   =\frac{\log(1/\max\{|z|,r\})}{L}
   =\min\left\{K_0(z),\frac{\log(1/r)}{L}\right\}.
\tag{3}
\]
Writing K_t(z)=G_D(t,z)/b(t) for interior t, its **unique compact representing measure** is
\[
 \boxed{\displaystyle
 \gamma_{0,C_r}(dt)
   =\frac{b(t)}{\kappa L}\,d\sigma_r(t)
   =\frac{\log\left|\frac{1-\bar a t}{a-t}\right|}{L}\,
     d\sigma_r(t).}
\tag{4}
\]
It is a **probability measure**, is generally **not uniform on C_r** if a is not the center, and converges weakly in the Martin compactification to delta_0 as r decreases to zero.

If f is any real continuous function on Delta, the **Perron solution** for boundary limits in this compactification is
\[
 \boxed{\displaystyle
 H_f(z)=\int_{S^1}P(z,\zeta)f(\zeta)\,d\sigma_1(\zeta).}
\tag{5}
\]
In particular, its unique minimal representing measure for the constant 1 is
\[
 \chi|_{S^1}=P(a,\zeta)\,d\sigma_1(\zeta),\qquad \chi(\{0\})=0.
\tag{6}
\]
Thus changing f(0) while keeping f on S^1 fixed does not change H_f, **even though 0 is a minimal Martin boundary point**. This is consistent with Theorem 4.5.13: resolutivity does not assert pointwise attainment at polar irregular boundary points.

## Verification

**1. Kernel limits and the distinct boundary points.** Green functions of D and D\{0} agree by the removable-polar-set maximum principle. For y tending to 0 the numerator G_D(y,z) tends to kappa log(1/|z|) locally uniformly for z in Omega; b(y) tends to kappa L. This gives K_0. For y tending to zeta on S^1, the elementary normal-derivative expansion of the displayed disk Green kernel yields the quotient of Poisson kernels, locally uniformly in z. Every Euclidean escaping net has a subnet approaching 0 or S^1; these limits exhaust the evaluation closure. The polar kernel is unbounded near 0, each circle kernel is bounded there, and different circle kernels have different boundary singularities. Together with the interior Green poles, these functions separate every point of the closed disk, so the evaluation-compactification lemma identifies the Martin compactification as claimed. This is a normalization crosscheck; as noted above, the equivalent end-kernel geometry has previously been audited.

**2. Minimality and uniqueness.** Suppose 0<=h<=K_0 is harmonic on the punctured disk. A harmonic function with O(log(1/|z|)) growth at an isolated puncture decomposes as c log(1/|z|)+g, where g extends harmonically across 0; this follows directly by circle Fourier series (negative Laurent harmonic modes violate the logarithmic bound). At S^1, both h and K_0 tend to zero, so g has zero continuous boundary values and vanishes by the maximum principle. Hence h is proportional to K_0. For 0<=h<=K_zeta, h is bounded near 0 and extends harmonically through it. Its positive disk Poisson boundary measure is supported only at zeta: for any continuous nonnegative test g supported in an arc disjoint from zeta, compare the radial boundary integrals of h with those of K_zeta, whose limits vanish on that arc. Hence h is a multiple of K_zeta. The disk Poisson representation and positive harmonic boundary trace are the established classical ball inputs; a general Martin representation theorem is **not** assumed here.

**3. Sweeping and the exact density.** Jensen's circular mean identity applied to (1) gives for z in Omega
\[
 \int_{C_r}G_D(z,t)\,d\sigma_r(t)
  =\kappa\log(1/\max\{|z|,r\}).
\tag{7}
\]
Indeed the averages of log|1-\bar t z| and log|z-t| are respectively 0 and log max(|z|,r). The right side divided by kappa L is a positive Green potential supported on C_r, agrees with K_0 on and outside C_r, is constant inside C_r, and is no larger than K_0 anywhere. By the positive-superharmonic minimum principle in each component of Omega\C_r (the puncture is polar), it is the smallest positive superharmonic majorant of K_0 on C_r. This proves (3). Comparing (7) with the definition K_t=G_D(t,.)/b(t) proves (4), and uniqueness follows from the distributional Riesz identity.

Since b(t)=G_D(t,a) is harmonic near the origin and b(0)=kappa L, its **exact circular mean** is kappa L for r<|a|. Therefore the measure in (4) has total mass one, not just asymptotically one. Its density relative to sigma_r converges uniformly to one as r decreases to zero. Since the supports C_r converge to 0 in the *identified Martin compactification*, gamma_{0,C_r} converges weakly to delta_0. This proves an explicit special-case compact-sweep convergence consistent with the limit mechanism of Theorem 4.5.12. The cutoff b is essential to the finite-r density; incorrectly declaring gamma_{0,C_r}=sigma_r would silently change the normalization.

**4. Perron invisibility of a polar minimal end.** The positive disk Poisson extension H of the circle restriction of f is bounded and harmonic on Omega. For each epsilon>0, the harmonic functions H+epsilon K_0 and H-epsilon K_0 are respectively admissible upper and lower Perron competitors: at every point of S^1 they have the required f boundary limit, while at 0 they tend to +infinity and -infinity. (A constant may be added to enforce a bounded-below convention in the upper class; no issue arises on taking epsilon to zero.) Consequently the upper and lower envelopes both equal H, proving (5) **independently of the prescribed finite f(0)**. Finally the disk Poisson formula gives 1=integral K_zeta(z) P(a,zeta) d sigma_1(zeta). Minimal representation uniqueness, or alternatively boundedness near 0 versus divergence of K_0, gives chi({0})=0, proving (6).

## Classification, limitation and proposed editorial insertion

**No confirmed error in the printed results.** Theorem 4.5.13 is **not** claiming boundary-value attainment at the polar Martin point; Theorem 4.5.12 does **not** claim that minimality of a boundary kernel implies positive harmonic measure. The extra polar point has a nonzero minimal kernel and exact probability sweeps (4), yet is invisible to chi and to all continuous Perron solutions (5). This distinction is the actual new finding and not a contradiction.

**Proposed addition only, not applied:** place (3)–(6), with the cutoff-weighted rather than uniform sweep and the warning about polar boundary values, as an example after Theorem 4.5.13. Affected conceptual dependents: Lemma 4.5.10 compact reduction normalization, Theorem 4.5.12 minimal representation/sweep convergence, and Theorem 4.5.13 continuous Perron representation. General Martin representation, arbitrary Greenian-domain sweeping, Choquet/fine-topological prerequisites and full-section correctness remain **unverified**. No regularization, Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas or positivity-loss argument was opened; these stay **deferred-by-user**, not resolved.

**Scope and operations:** only selected model-level §4.5.10/.12/.13 checks, with §4.5.8/.9 normalization crosschecks; §4.5 was already partly sampled. No new first-reviewed numbered section, no whole-section certification; actual ToC remains 25 chapters / 747 numbered sections / zero complete mathematical-section certifications. No builds, tests, GitHub Actions, site publication, formal verification, original sources, canonical registry, or production main modifications.
