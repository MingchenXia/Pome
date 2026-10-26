# 2026-10-27 — sharp PSH sublevel capacity and exact Gauduchon Jensen defect

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting review branch:** 5db8b393779ea541959178060daba9668e14f1e0. The mathematical passages below are from the **integrated main reading edition** at this fixed main commit; main source bodies, canonical registries and permanent tags are not changed.

## Finding POME-BT-PSH-SUBLEVEL-CAP-RATE-001

**Status:** verified conditional deduction. **Severity:** low. **Original results:** no demonstrated error. **Source:** Theorem 7.4.1, source label **foundations-of-pluripotential-theory-93A06A12**, permanent tag **7C68264563C0**, physical lines **11–81** of **docs/sections/bedford-taylor-products-and-local-capacity--weighted-estimates-and-monge-ampere-capacity/index.html**, blob **801a6ce8d25a6db19202cbc295937a135a9a208e**. Definition 7.4.2, permanent tag **E9E7C75396D2**, lines **86–93** of the same file. Theorem 7.2.5, permanent tag **2A84C325AB58**, is an explicit conditional upstream mass bound.

### Hypotheses, conclusion and proof

Let \(D\Subset\mathbb C^n\) denote a bounded open set (no smoothness assumed), and let \(K,L\Subset D\) be compact sets with \(K\subset\operatorname{Int}L\). For \(V\in\operatorname{PSH}(D)\), define the relative Monge–Ampère capacity as in Definition 7.4.2. For each \(t>0\) put
\[
E_t=K\cap\{x\in D:V(x)<-t\}.
\]
The weighted Chern–Levine–Nirenberg inequality gives the **uniform weak-type estimate**
\[
\boxed{\operatorname{Cap}_D(E_t)
\ \le\ \frac{C_{K,L,n}}{t}\,\|V\|_{L^1(L)}.}
\tag{A}
\]
The constant is the exact type of constant supplied by Theorem 7.4.1; it is independent of \(t\), \(V\), and the capacity competitor. Indeed, for an arbitrary \(v\in\operatorname{PSH}(D)\), \(0\le v\le1\), the Bedford–Taylor measure \((dd^cv)^n\) is positive. Because \(|V|\ge t\) on \(E_t\),
\[
t\int_{E_t}(dd^cv)^n
\le\int_K|V|(dd^cv)^n
\le C_{K,L,n}\|V\|_{L^1(L)}\|v\|_{L^\infty(L)}^n
\le C_{K,L,n}\|V\|_{L^1(L)}.
\]
Taking the supremum over all \(v\) proves (A). There is no exchange of a weak limit and a supremum. If the sublevel is non-Borel in another setting, use outer capacity with an appropriately verified open-set comparison; **here \(V\) is upper semicontinuous and \(\{V<-t\}\) is Borel (indeed open)**, so Definition 7.4.2 suffices. The same argument yields a mixed \(q\)-factor weak-type estimate, \(0\le q\le n\), with \(dd^cv_1\wedge\cdots\wedge dd^cv_q\wedge\beta^{n-q}\) and the same \(t^{-1}\) rate, for all bounded competitors \(0\le v_i\le1\). This latter assertion is a selected consequence, not a new definition of capacity.

### Sharpness of the exponent

The exponent \(t^{-1}\) **cannot be replaced by \(o(t^{-1})\)** under these hypotheses, even in complex dimension one with a fixed singularity. Let \(D=\Delta\), \(K=\overline{\Delta}_{1/2}\), \(L=\overline{\Delta}_{3/4}\), and \(V(z)=\log|z|\), taking \(V(0)=-\infty\). Then \(\|V\|_{L^1(L)}<\infty\) and for \(t>\log2\),
\[
E_t=\Delta_{e^{-t}}.
\]
For \(t>0\), the bounded subharmonic capacity competitor
\[
v_t(z)=\max\left\{0,\ 1+\frac{\log|z|}{t+1}\right\},
\qquad 0\le v_t\le1\ \text{on }\Delta,
\]
is harmonic off the circle \(|z|=e^{-(t+1)}\) and constant on its interior. Under the collection's convention \(dd^c=\frac{i}{2\pi}\partial\bar\partial\), the radial derivative jump gives
\[
dd^cv_t(\Delta)=\frac{1}{2(t+1)},
\quad \operatorname{supp}(dd^cv_t)=\{|z|=e^{-(t+1)}\}
\subset E_t.
\]
Consequently
\[
\boxed{\frac{1}{2(t+1)}\le \operatorname{Cap}_\Delta(E_t)
\le \frac{C_{K,L,1}\|\log|z|\|_{L^1(L)}}{t}.}
\tag{B}
\]
The circle of radius \(e^{-(t+1)}\), rather than \(e^{-t}\), is essential: the sublevel is **strict**, and the latter boundary circle is not contained in \(E_t\). Formula (B) rigorously establishes optimal order. This is a mathematical corollary, not an incorrect theorem in the existing reading edition.

**Proposed change:** optional short quantitative corollary immediately after Theorem 7.4.1 or Definition 7.4.2. **Dependents:** local capacity convergence and exceptional-set estimates in §§7.5–7.6 and comparison/capacity arguments elsewhere. All Bedford–Taylor weighted theory used here is treated as an already stated internal input; its complete transitive correctness is not certified by this deduction.

## Finding POME-GAUD-JENSEN-DEFECT-001

**Status:** verified conditional deduction. **Severity:** low. **Original results:** Theorem 12.3.1 and Proposition 12.4.1 remain correct as used; the result is a quantitative refinement. **Source:** Proposition 12.4.1, source label **non-kahler-pluripotential-theory-C55D0CC4**, permanent tag **67FDDBC10DBD**, equations (12.4.2)–(12.4.3), physical lines **23–69** of **docs/sections/a-gauduchon-variational-volume--second-variation-on-background-classes/index.html**, blob **4992f82c6e84918ead47a972eab7e3238a147655**. Related: Theorem 12.3.1, tag **2220E0C47510**, physical lines **14–45**, **docs/sections/a-gauduchon-variational-volume--the-equality-case-of-concavity-and-the-first-variation/index.html**, blob **d94e3fc055b0642a86495c27ad8f5af6f24f17d1**. The smooth Hermitian Monge–Ampère equation, implicit-function regularity, and adjoint probability (Theorem 14.2.1; Proposition 11.23.2) are **conditional internal inputs**, not re-proved.

### Exact integrated Jensen deficit

Let \(X\) be compact connected of complex dimension \(n\ge1\), fix a smooth positive probability volume \(\mu\), and choose \(\theta_0,\theta_1\in\mathscr P\), the positive-background cone of §12.2. Put \(\theta_s=(1-s)\theta_0+s\theta_1\), \(\chi=\theta_1-\theta_0\), and let \(\lambda_s=\lambda_\mu(\theta_s)>0\). Since \(\mathscr P\) is convex, all \(s\in[0,1]\) lie in \(\mathscr P\). Let \(\Omega_s=\theta_s+dd^cu_s\) be the unique normalized smooth solution form, and let \(\nu_s\) denote its adjoint probability. Define
\[
A_s=\Omega_s^{-1}\bigl(\chi+dd^c\dot u_s\bigr),
\qquad r_s=\frac{\dot\lambda_s}{\lambda_s},
\qquad Q_s=\int_X\|A_s-r_sI\|_{\Omega_s}^2\,d\nu_s.
\]
Proposition 12.4.1 gives, pointwise for \(s\in[0,1]\),
\[
-\lambda_s''=\frac{\lambda_s}{n}Q_s,\qquad Q_s\ge0.
\]
For every \(0\le t\le1\), the **exact affine-chord concavity defect** is
\[
\boxed{
\lambda_t-\bigl[(1-t)\lambda_0+t\lambda_1\bigr]
=\frac1n\int_0^1\bigl(\min\{t,s\}-ts\bigr)
\,\lambda_s Q_s\,ds.
}
\tag{C}
\]
The kernel \(G_t(s)=\min(t,s)-ts\) is the nonnegative Dirichlet Green kernel for \(-d^2/dt^2\) on \([0,1]\): it vanishes at \(t=0,1\) and its distributional second derivative in \(t\) is \(-\delta_s\). The two sides of (C) have identical second derivatives in \(t\) and vanish at both endpoints, proving equality. Only integration over a smooth one-dimensional *finite interval* occurs; there is no interchange of directed limits.

In particular, if \(m>0,\eta>0\), and \(0<a<b<1\) satisfy \(\lambda_s\ge m\) and \(Q_s\ge\eta\) for \(s\in[a,b]\), then
\[
\lambda_t-\bigl[(1-t)\lambda_0+t\lambda_1\bigr]
\ge \frac{m\eta}{n}\int_a^b(\min\{t,s\}-ts)\,ds.
\tag{D}
\]
Equality in (C) at any interior \(t\) forces \(Q_s=0\) throughout the segment by smoothness and strict positivity of \(G_t\) for \(s\in(0,1)\). Proposition 12.4.1 and Theorem 12.3.1 then give precisely the known equality criterion
\[
\theta_1=c\,\theta_0+dd^cf\qquad(c>0,\ f\in C^\infty(X,\mathbb R)).
\]
Thus (C) refines, rather than replaces, the printed equality theorem. In dimension one, every \(Q_s\) vanishes, and (C) correctly reduces to linearity of \(\lambda_\mu=\int_X\theta\).

As a transparent strict example, on \(X=\mathbb P^1\times\mathbb P^1\) let \(\alpha,\beta\) be the normalized factor Kähler forms. Take \(\theta_0=\alpha+\beta\), \(\theta_1=2\alpha+\beta\). By closedness and the intersection formula used in §12.6.2,
\(\lambda_s=\sqrt{2(1+s)}\), giving at \(t=\frac12\)
\[
\lambda_{1/2}-\tfrac12(\lambda_0+\lambda_1)
=\sqrt3-\frac{\sqrt2+2}{2}>0.
\]
This verifies nontriviality independently of the adjoint-density calculation.

**Proposed change:** optional exact-deficit corollary after Proposition 12.4.1, cross-referenced to equality in 12.3.1. **Dependents:** finite-dimensional Gauduchon root-volume concavity, Hessian metric, and strict interpolation estimates. No claim of a uniform global modulus of strict concavity without a genuine lower bound on \(\lambda_s Q_s\).

## First new high-centrality selected proof inspection: §18.1

**Source:** **docs/sections/good-singularities/index.html**, main blob **638301f48e081c04a2d766e827b577b073acb359**, 1326 physical lines. Newly inspected the nonexcluded equivalence **(2)↔(3)** of Theorem 18.1.2, source label **sgpt-78C13CE2**, permanent tag **F9085BB700B0**, lines **41–94**, and the selected finite-maximum/Choquet/supremum argument of Proposition 18.1.19, source label **sgpt-CCE5B1B6**, permanent tag **FD679E0ECD3D**, lines **415–438**, with supporting Proposition 18.1.17, tag **AC437613D2C1**, lines **364–402**.

For closed big \(\theta\) and positive-mass \(\varphi\), the equivalence of equality between ordinary and multiplier-ideal model envelopes and equality of ordinary and ideal-model masses is derived using the *already stated internal* definition of \(\operatorname{vol}\theta_\varphi\), mass comparison 16.3.14, and monotonicity 16.6.18; the converse uses Proposition 16.3.9. The two directions and their hypotheses were matched, without attempting the separate analytic-approximation implication of Theorem 18.1.2. Proposition 18.1.19 correctly assumes a **nonempty** locally uniformly upper-bounded family: Choquet's countable extraction preserves the upper-semicontinuous supremum, successive finite maxima remain \(\mathcal I\)-good by Proposition 18.1.17, and increasing \(d_S\)-convergence plus the closure corollary gives the conclusion. These are **selected conditional checks**, not a full proof verification of any whole theorem's upstream dependencies.

**Excluded by the author's scope change:** the implication involving quasi-equisingular / Demailly approximants in Theorem 18.1.2, the proof programme around analytic approximations in §18.1, the asymptotic proof of Theorem 18.1.46 using its dedicated techniques, all dedicated Bergman/L²/OT/multiscale/positivity-loss steps. Those remain **deferred-by-user**, neither resolved nor certified. Mentioning an existing cross-reference here is *not* an attempt to re-prove it.

## Coverage and method

- **New selected proof-level inventory upgrade:** §18.1 **only** (specified paragraphs above), not the whole section.
- **Incremental selected proof checks:** §§7.2–7.4, particularly the entire current §7.4.1 weighted estimate and §7.4.2 definition; §§12.2–12.5, particularly §12.4.1 second variation and §12.3.1 equality; contextual definitions in §§7.1, 12.1, 18.2–18.3. These latter rows already had selected audits (except introduction-only rows) and should not be counted as newly reviewed entire sections.
- No new confirmed false printed theorem and no new independent external proof input established. The two numbered results above are precise **conditional deductions** from identified internal theorems, not formal verification.
- Previously registered errors, external inputs and unresolved/deferred entries retain their existing statuses. No source/body/registry/tag changes, build, tests, CI, formal proof or publication were performed.
