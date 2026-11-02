# Fixed-slot Hessian comparison: a Gauduchon trace with nonconstant second-Hessian mass

**Date:** 2026-11-03  
**Finding:** **POME-HESS-GAUD-TRACE-SECOND-MASS-001**  
**Classification:** **low / verified conditional deduction**. Neither an error in the printed theorem nor an applied source repair. The smooth model and its strict mass inequality are independently calculated. The bounded comparison part uses the existing positive mixed-product/contact theory as an explicitly identified conditional premise.  
**Production main:** **b6933b772f41b45918f7e25ed1afbbb1fd892272** (not modified).

## Pinpointed integrated reading edition and dependencies

- **docs/sections/complex-hessian-equations--hessian-mass-and-global-comparison/index.html**, blob **580d3bc2b10ebd01d880b2a31fc6930436570aac**. Proposition **8.13.3**, source **non-kahler-pluripotential-theory:987BD409**, permanent tag **CCDE5B297235**, physical lines **45–63**: mixed contact comparison with a total-mass defect. Theorem **8.13.4**, source **non-kahler-pluripotential-theory:776C8B26**, permanent tag **53F870DE5980**, lines **69–120**: the simultaneous full Hessian mass/comparison criterion for powers from n−m through n−1. Example **8.13.5**, source **non-kahler-pluripotential-theory:870AB319**, permanent tag **0DB9D80DE230**, lines **128–149**, is a **different** variable-background example, with already printed nonconstant total mass.
- **docs/sections/complex-hessian-equations--locality-and-maxima-of-bounded-potentials/index.html**, blob **8750df56019c14e16704607ca20fa8b90f137fb0**. Theorem **8.12.2**, source **non-kahler-pluripotential-theory:D838B734**, permanent tag **655B0BBF4F9C**, physical lines **38–65**: positive mixed contact inequality for bounded admissible potentials. The existing §8.9.6 bounded mixed products and §8.11.12 decreasing-continuity input are assumed, not recertified here.
- The printed chapter assumes a compact complex n-fold with a smooth positive Hermitian form ω and intermediate degree **2 ≤ m < n**. In particular the explicit model below has **(n,m)=(3,2)**. We use the project's convention **ddᶜ=(i/2π)∂∂̄**.

## New fixed-slot characterization (smooth proof, bounded comparison conditional on the internal mixed theory)

Fix **1 ≤ r ≤ m** and smooth m-admissible potentials z₁,…,zₘ₋ᵣ. Write

\[
\Theta_z
=(\omega+dd^c z_1)\wedge\cdots\wedge
(\omega+dd^c z_{m-r})\wedge\omega^{n-m},\qquad
\mu_{r,z}(u)=(\omega+dd^c u)^r\wedge\Theta_z.
\]

Empty products have their usual meaning. These are the fixed-slot mixed Hessian measures of Theorem 8.12.2. **The total mass of μᵣ,𝓏(u) is independent of all smooth m-admissible u if and only if**

\[
\boxed{\quad
dd^c\bigl(\omega^{r-q}\wedge\Theta_z\bigr)=0
\quad\text{for every }1\le q\le r.\quad}
\tag{F}
\]

**Proof of both directions.** Expanding \(\mu_{r,z}(tf)\) for any smooth real f and all sufficiently small positive and negative t gives

\[
\int_X\mu_{r,z}(tf)
=\sum_{q=0}^{r}\binom rq t^q
 \int_X(dd^c f)^q\wedge\omega^{r-q}\wedge\Theta_z.
\]

If (F) holds, Stokes/integration by parts in one factor of \(dd^c u\) makes each q≥1 term vanish for **every** smooth u, hence gives mass invariance. Conversely, if the mass is independent of smooth admissible u, the displayed polynomial is constant in a neighborhood of zero. Every positive-degree coefficient vanishes for all smooth f. Polarization yields, for each q,

\[
\int_X dd^c f_1\wedge\cdots\wedge dd^c f_q
 \wedge\omega^{r-q}\wedge\Theta_z=0
\]

for arbitrary smooth real f₁,…,f_q. Integrate by parts in f₁. Arbitrary f₁ and arbitrary pointwise complex Hessians of f₂,…,f_q (real quadratic functions with cutoffs) detect every coefficient of \(dd^c(\omega^{r-q}\wedge\Theta_z)\); thus (F). The argument is **entirely smooth** and uses no analytic approximation theorem.

**Comparison consequence and its converse.** Under the existing bounded Hessian mixed-product continuity theorem, smooth mass invariance extends to bounded admissible u by decreasing approximation; this analytic dependency is **not re-proved**. The contact inequality of §8.12.2 and equality of total masses then give

\[
\mu_{r,z}(v)(\{u<v\})\le
\mu_{r,z}(u)(\{u<v\})
\]

for all bounded admissible u,v. Conversely, if this unmodified comparison inequality holds for every such pair, apply it first to smooth \(u,v+C\) with C sufficiently large and then with u and v exchanged. Constant shifts do not change μ, so the two total masses coincide. The smooth argument above forces (F). Thus, **conditional on the already integrated bounded mixed-product/contact machinery**, (F) characterizes the fixed-slot unmodified comparison principle. For r=m the condition reduces exactly to the first clause of the printed Theorem 8.13.4; for a fixed smaller r it can be strictly weaker.

## Explicit degree-one/degree-two separation on a Gauduchon three-torus

Let

\[
X=\bigl(\mathbb C/(\mathbb Z+i\mathbb Z)\bigr)^3,\quad
\beta_j=\frac{i}{2\pi}\,dz_j\wedge d\bar z_j,\quad
x_j=\Re z_j,
\]
\[
b(x_1)=2+\cos(2\pi x_1),\qquad
g(x_1)=b(x_1)^{-1},\qquad
\boxed{\ \omega=\beta_1+b\beta_2+g\beta_3.\ }
\]

This is a globally smooth, strictly positive Hermitian form. Since \(bg\equiv1\),

\[
\omega^2=2\bigl(b\,\beta_1\beta_2+
                   g\,\beta_1\beta_3+\beta_2\beta_3\bigr),
\qquad
dd^c\omega^2=0.
\]

Here \(\beta_i\beta_j\) denotes the wedge product. The terms with varying b or g already contain β₁, while their ddᶜ derivatives are proportional to β₁; the remaining coefficient bg is constant. **But**

\[
dd^c\omega=\tfrac14 b''\,\beta_1\beta_2+
            \tfrac14 g''\,\beta_1\beta_3\ne0.
\]

Consequently, for **m=2, r=1 and fixed second slot z₁=0**, the measure

\[
\mu_{1,0}(u)=(\omega+dd^c u)\wedge\omega^2
\]

has constant total mass for every bounded 2-admissible u, conditional only on the existing construction of this bounded measure. The §8.12.2 contact inequality therefore gives **unmodified comparison for this one-moving-slot measure**, even though the full second-Hessian comparison principle need not hold.

We now verify the failure of full degree-two comparison by a **completely explicit smooth mass calculation**, not by contraposition from Theorem 8.13.4. Set

\[
c(x_2)=\cos(2\pi x_2),\quad
a(x_1)=\sqrt{2+g(x_1)},\quad f(x_1,x_2)=a(x_1)c(x_2).
\]

For sufficiently small real t, \(tf\) is strictly admissible. With \(B_3=\int_X\beta_1\beta_2\beta_3>0\), the complex Hessian in the first two complex coordinates is one quarter the real x-Hessian, and

\[
\frac{(dd^c f)^2\wedge\omega}{\beta_1\beta_2\beta_3}
 =\frac{g}{8}\bigl(a a''c c''-(a')^2(c')^2\bigr).
\]

Since \(\int_0^1(c')^2\,dx_2=2\pi^2\) and
\(\int_0^1cc''\,dx_2=-2\pi^2\), twice integrating by parts in periodic x₁ yields

\[
\begin{aligned}
\frac1{B_3}\int_X(dd^c f)^2\wedge\omega
&=-\frac{\pi^2}{8}\int_0^1 g(a^2)''\,dx_1\\
&=-\frac{\pi^2}{8}\int_0^1 g''(2+g)\,dx_1\\
&=\frac{\pi^2}{8}\int_0^1(g')^2\,dx_1>0 .
\end{aligned}
\tag{Q}
\]

By \(dd^c\omega^2=0\), the coefficient linear in t in the full second-Hessian mass vanishes. As \(\omega^3=6\beta_1\beta_2\beta_3\), we obtain the **exact polynomial identity**

\[
\boxed{\quad
\int_X H_2(tf)
=6B_3+\frac{\pi^2t^2 B_3}{8}
\int_0^1(g')^2\,dx_1
>6B_3=\int_XH_2(0)
\quad(t\ne0\text{ sufficiently small}).\quad}
\]

Choose C>\(|t|\|f\|_\infty\). Then \(0<tf+C\) everywhere and \(H_2(tf+C)=H_2(tf)\). An unmodified full degree-two comparison inequality for the pair \((0,tf+C)\) would force \(\int_XH_2(tf)\le\int_XH_2(0)\), a contradiction. This distinguishes **a true Gauduchon degree-one comparison** from the **false stronger degree-two comparison**, on the **same** Hermitian background and within the allowed 2≤m<n range.

For a limited independent scalar crosscheck, symbolic differentiation of the normalized Hessian determinant and numerical periodic quadrature agree with (Q): \(\int_0^1(g')^2dx_1\approx2.532541670117358\) and the coefficient in (Q) divided by B₃ is approximately \(3.124398051666559\). This is **not** a project test, a formal proof, or evidence about other chapters.

## Disposition, dependencies, and exact coverage

**No printed mathematical error.** Theorem 8.13.4 already requires every \(dd^c\omega^{n-q}=0\) for q≤m; the concrete Gauduchon metric shows that retaining just its q=1 condition would be wrong for m=2. The printed Example 8.13.5 instead varies mass at linear order on a non-Gauduchon metric and must **not** be canonicalized with the present quadratic, Gauduchon example.

**Optional proposed addition (not applied):** after Theorem 8.13.4, state the smooth fixed-slot criterion (F), cite existing bounded mixed locality for the conditional bounded consequence, and mention the \(b,1/b\) three-torus counterexample to inference from one-slot to full comparison. Preserve the original theorem, historical attribution, source labels and permanent tags.

**Actual newly reviewed steps:** independent smooth fixed-slot polarization/Stokes characterization in §§**8.13.3–4**, an independently calculated degree-two mass countermodel, and the exact **8.12.2** fixed-slot contact inequality as a *quoted upstream result*. This section was previously partially sampled: **no first-reviewed section and no complete section or all-dependency certification**. The bounded Hessian approximation machinery is referenced only, not re-audited; no Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale atlas or positivity-loss proof programme was opened. Retain all preexisting statuses as found. Actual current table of contents: **25 chapters / 747 numbered sections / zero entire mathematical-section certifications**.

No production main, source, proof registry, canonicalization, permanent tags, project tests, build, GitHub Actions CI, formalization or website publication changed.
