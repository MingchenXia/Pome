# Exact ridge density and an equatorial null-supported Kähler representative

**Date:** 2026-11-12. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Finding:** `POME-NULL-KAHLER-RIDGE-EQUATOR-DENSITY-001`.
**Severity/status:** **low / verified conditional deduction**. Neither printed theorem is false; no production correction is required. The local ridge formula is conditional on a regular *two-branch* tie, whereas the projective example is unconditional.

## Current integrated source and exact anchors

- `docs/sections/null-supported-kahler-currents/index.html`, main blob `009f58a180936636f2e5927b9272f87f2c93aa29`; section 5.64, permanent tag `CF37B5381263` (physical line 5), original section source `transcendental-positive-cones:D29CF8E7`.
- Lemma 5.64.1, original `transcendental-positive-cones:C6A5C2FA`, permanent `0B34D9269CEA`, lines 11–26: real-analytic nonzero level sets are null.
- Theorem 5.64.2, original `transcendental-positive-cones:FBD376B2`, permanent `E682ACE02BAF`, lines 31–104. We rechecked the actual local potentials and maxima (43–63), constant choices (65–79), equality locus (81–93), support and cohomological mass (95–103), and the express warning about noncomplex ties (108).
- The related *previously reviewed* Corollary 5.65.2 appears in `docs/sections/local-mass-bounds-for-pluriharmonic-currents/index.html`, blob `4c2db22424afb29ff4ec2f972dc28cb50b8f0b82`, permanent `63CAD58A60D1`, lines 48–65. Only its **statement** is used as a scope comparison; its proof was not reassessed in this run.

The 2026-10-26 report `reports/2026-10-26-null-kahler-current-sharp-support-dimension.md` already establishes a separate sharp Hausdorff-dimension example using a Cantor support. **That proof and its finding are not repeated** here. The new work computes the precise *codimension-one ridge density*, supplies an explicit normalized smooth-interface model, and calculates its trace mass on all products of projective lines.

## 1. Exact local two-branch jump formula

Use the book's normalization \(dd^c=\frac{i}{2\pi}\partial\bar\partial\).
Take a coordinate region in which \(\omega=dd^c\rho_i=dd^c\rho_j\), and let two positive caps from Theorem 5.64.2 be the **only** active branches on an open neighborhood:
\[
 b_i=c_i-\rho_i>0,\qquad b_j=c_j-\rho_j>0,\qquad
 u=\max(b_i,b_j).
\]
Set
\[
 h=(c_j-c_i)+\rho_i-\rho_j.
\]
The difference of the local potentials is pluriharmonic, so \(dd^c h=0\). The local potential of the current is
\[
 \rho_i+u=\max(c_i,c_i+h)=c_i+h_+,\qquad h_+=\max(h,0).
\]
Consequently, in distributions,
\[
 \boxed{\,T=\omega+dd^cu
       =\frac{i}{2\pi}\delta(h)\,\partial h\wedge\bar\partial h.\,} \tag{R1}
\]
Here \(\delta(h)\) is the pullback of the one-dimensional Dirac distribution **only on the regular locus \(dh\ne0\)**. One verifies (R1) there in coordinates with \(h\) as a real coordinate: the one-dimensional distributional identities \((t_+)'=\mathbf1_{t>0}\) and \((t_+)''=\delta_0\), the chain rule, and \(\partial\bar\partial h=0\) give the formula. This does not use Demailly approximation or any Bergman/L2/Ohsawa–Takegoshi theorem. Positivity is apparent.

Fix standard Euclidean real coordinates \(z_\ell=x_\ell+iy_\ell\), real volume \(dV_{2n}\), and \(\beta=dd^c|z|^2=\pi^{-1}\sum_\ell dx_\ell\wedge dy_\ell\). At a regular interface point a unitary coordinate change puts \(\partial h=(|\nabla h|/2)\,dz_1\). Wedge (R1) with \(\beta^{n-1}\) to obtain
\[
 T\wedge\beta^{n-1}
  =\frac{(n-1)!}{4\pi^n}\,
       \delta(h)|\nabla h|^2\,dV_{2n}
  =\boxed{\frac{(n-1)!}{4\pi^n}
       |\nabla h|\,d\mathcal H^{2n-1}\big|_{\{h=0\}}}. \tag{R2}
\]
The second equality is precisely the one-dimensional coarea identity for a regular real level set. Thus a genuine regular two-branch switch carries **strictly positive, absolutely continuous \((2n-1)\)-dimensional surface density**, not volume measure. The constants \(4\pi^n\), the factorial, and the single gradient power matter.

**Scope limitation:** The genericity choice in lines 65–93 excludes identically coincident branches on a connected overlap; it does **not** assert that all multiple ties or critical-level points are regular. Therefore (R1)–(R2) are only asserted on a region with exactly two active caps and \(dh\ne0\), not as an unproved global decomposition of every current constructed in Theorem 5.64.2.

## 2. An explicit global smooth-interface model on \(\mathbb P^1\)

In the affine coordinate \(z\in\mathbb C\) take
\[
 \omega_{\rm FS}=dd^c\log(1+|z|^2),\qquad
 v(z)=\log\max\{1,|z|^2\}-\log(1+|z|^2).
\]
The expression is unchanged on substituting \(w=1/z\): because the same formula with \(w\) gives \(v\), it extends to a globally continuous function on \(\mathbb P^1\). Directly,
\[
 -\log 2\le v\le0,\qquad
 \omega_{\rm FS}+dd^cv=dd^c\log\max\{1,|z|^2\}
\]
on the affine chart, and the corresponding formula is valid in the infinity chart. The latter potential is constant on \(|z|<1\) and pluriharmonic on \(|z|>1\), so the positive current is supported **exactly** on the unit circle.

At \(|z|=1\), apply (R1) to \(h=\log|z|^2\), for which \(|\nabla h|=2\). Formula (R2), or direct radial integration by parts, gives the exact positive measure
\[
 \boxed{\;\omega_{\rm FS}+dd^cv
      = \frac{d\theta}{2\pi}\Big|_{\{|z|=1\}}.\;} \tag{R3}
\]
In particular the total mass is \(1=\int_{\mathbb P^1}\omega_{\rm FS}\). No point mass occurs at \(0\) or \(\infty\): in each relevant chart the displayed local potential is constant near the coordinate origin. This is an explicit continuous-potential, null-supported representative of the Kähler class, with **smooth real-hypersurface** rather than Cantor support. Adding any constant \(>\log2\) makes the potential strictly positive as in the printed theorem without changing the current.

## 3. Products: exact trace measure, support and class

Let \(X=(\mathbb P^1)^n\), with projections \(\pi_i\), set \(\omega_i=\pi_i^*\omega_{\rm FS}\), \(\omega=\sum_i\omega_i\), and choose
\[
 u=n\log2+1+\sum_{i=1}^n\pi_i^*v,\qquad
 T=\omega+dd^cu=\sum_{i=1}^n \pi_i^*\nu,\quad
 \nu=\frac{d\theta}{2\pi}\bigg|_{|z|=1}.
\]
The potential \(u\ge1\) is continuous and \(\omega\)-psh, \(T\ge0\) is closed, and \(T\in[\omega]\). Since every summand is positive and nonzero, its support is **exactly** the finite union
\[
 \boxed{\operatorname{Supp}T=
   \bigcup_{i=1}^n\bigl(\{|z_i|=1\}\times
                 \prod_{j\ne i}\mathbb P^1\bigr).} \tag{R4}
\]
Each component is a smooth real hypersurface, so the union is closed and Lebesgue-null. As \(\omega_i^2=0\) and the factors commute,
\[
 \boxed{\;
 T\wedge\omega^{n-1}
 =(n-1)!\sum_{i=1}^n
       \pi_i^*\nu\wedge\bigwedge_{j\ne i}\omega_j,\qquad
 \int_X T\wedge\omega^{n-1}
     =n!=\int_X\omega^n.\;} \tag{R5}
\]
This explicitly tests the positive-current normalization, the support claim and the Stokes mass identity at the same time, including \(n=1\). Nothing from the excluded analytic regularization programme is invoked.

## Status, dependents and proposed action

**Verified conditional deduction, low severity**: (R1)–(R2) hold subject to the stated two-branch regularity; (R3)–(R5) are fully computed model identities. The printed Theorem 5.64.2 is **not** a false theorem, and this report does **not** certify its entire general proof or the general trace-growth theory. An optional separately reviewable editorial addition is a short example after Theorem 5.64.2 recording (R3) and the product formula (R5); no source/reader changes were made.

**Affected dependents:** This is a consistency and normalization crosscheck for Theorem 5.64.2's null-support representative and its trace against \(\omega^{n-1}\); it also respects the conditional local trace-growth conclusions of Corollary 5.65.2. The prior Cantor-dimension example remains a different, sharper support-dimension phenomenon. Lemma 5.64.3 and Corollary 5.64.4 invoke the user's excluded Demailly regularization; those steps remain **deferred-by-user**, **not** solved, certified or reopened.

**Actual coverage:** New selected nonexcluded proof-level examination of §5.64, lines 43–103 and 108; §5.65 Corollary 5.65.2 statement only. Both numbered sections were already partially reviewed: **0 newly first-visited sections, 0 fully certified sections**. The current main table of contents remains 25 chapters and 747 numbered sections. No build, tests, CI, formal verification or publication was performed.
