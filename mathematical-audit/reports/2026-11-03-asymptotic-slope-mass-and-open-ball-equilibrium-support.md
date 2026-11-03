# Asymptotic-slope Monge–Ampère mass and the open-ball equilibrium support

**Date:** 2026-11-03. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Scope:** newly direct proof-level inspection of §16.34.1; independent radial model for §16.34.2. No entire-section certification and no review of the user-excluded approximation/regularization/Bergman/L²/OT/multiscale/positivity-loss programme.

## Exact locations and classification

Integrated page: **docs/sections/logarithmic-total-mass-and-bounded-obstacle-support/index.html**, blob **47387388cb62e2b99cf6f78370c914aa6f75909d**.
* Proposition 16.34.1: source **klimek-pluripotential-theory:7D93BBF9**, permanent **B5EE2E185F5F**, physical lines **7–12**, proof **15–26**.
* Proposition 16.34.2: source **klimek-pluripotential-theory:63C4C42B**, permanent **01D4425BEF42**, physical lines **47–52**, proof **55–69**.
* Section permanent tag **65512695189E**, source **klimek-pluripotential-theory:102D914E**. The linked cohomological mass Proposition 13.5.1 has permanent tag **06A36B9354A5** and was consulted only for its normalization; its complete upstream chain was not recertified.

**POME-LOGMASS-ASYMPTOTIC-SLOPE-001 — low / verified conditional deduction.** The printed one-sided inequality is correct, but the printed *ratio limit* actually implies equality, even for infinite total mass, and more generally yields a sharp two-sided liminf/limsup mass comparison. This is a proposed explanatory strengthening, not a claim of a false theorem.

**POME-LOGMASS-OPEN-BALL-SUPPORT-001 — low / verified conditional deduction.** An explicitly computed open-ball equilibrium has all its nonzero mass on the boundary, disjoint from the original set. This verifies that §16.34.2's support assertion must use closure and cannot be silently strengthened to support in E. The printed proposition is correct.

## 1. Sharp asymptotic-slope mass theorem

Fix $n\ge1$ and $dd^c=(i/2\pi)\partial\bar\partial$. For locally bounded PSH $u,v$ on $\mathbb C^n$ suppose $v(z)\to+\infty$ as $|z|\to\infty$, and
\[
0<a:=\liminf_{|z|\to\infty}\frac{u(z)}{v(z)}
\le b:=\limsup_{|z|\to\infty}\frac{u(z)}{v(z)}<\infty.
\]
(These ratios are well-defined for sufficiently large $|z|$.) Write $M(w)=\int_{\mathbb C^n}(dd^c w)^n\in[0,+\infty]$. Then
\[
\boxed{a^n M(v)\le M(u)\le b^n M(v).}\tag{1}
\]
In particular, if $u/v\to\lambda\in(0,\infty)$ then
\[
\boxed{M(u)=\lambda^n M(v)} \quad\text{in }[0,+\infty].\tag{2}
\]
For the exact hypotheses of §16.34.1, $\lambda=1$, and **equality** holds. No bounded difference of potentials is required.

**Proof without interchanging noncompact limits.** Fix $\delta>0$ small enough that $a-\delta>0$. Outside a large ball,
\[
(a-\delta)v\le u\le(b+\delta)v.
\]
In particular $u\to+\infty$. For the upper inequality, let $w_c=(b+2\delta)v-c$ and $G_c=\{w_c<u\}$. Since $(b+2\delta)v-u\ge\delta v\to+\infty$, each $G_c$ is bounded. On a larger ball its boundary is strictly ordered. The bounded Bedford–Taylor comparison principle (the exact step used in the printed §16.34.1 proof) gives
\[
\int_{G_c}(dd^c u)^n\le\int_{G_c}(dd^c w_c)^n
\le(b+2\delta)^nM(v).
\]
As $c\to+\infty$, the *increasing* Borel sets $G_c$ exhaust $\mathbb C^n$ because $u,v$ are finite at every point. Monotone convergence for positive measures therefore gives $M(u)\le(b+2\delta)^n M(v)$. Let $\delta\downarrow0$.

For the lower inequality apply the same comparison argument with the roles of $v$ and $u$ reversed, observing that $v\le(a-\delta)^{-1}u$ outside a compact set and both are proper. It yields $M(v)\le (a-\delta)^{-n}M(u)$. Let $\delta\downarrow0$. The argument is valid in the extended nonnegative reals; it neither assumes finite total mass nor exchanges two unrelated limits.

**Sharpness and normalization.** For $\lambda>0$ set
\[
v(z)=\tfrac12\log(1+|z|^2),\qquad u(z)=\lambda v(z).
\]
Both are smooth PSH, their asymptotic ratio is exactly $\lambda$, and the §13.5.1 radial computation gives $M(v)=2^{-n}$ and $M(u)=\lambda^n2^{-n}$. Thus the exponent $n$ and the constants in (1) cannot improve even in the smooth radial class. For $n=1$ this also checks the factor $1/2$ in Pome's $dd^c$ convention.

**Status and dependency:** The comparison is a complete deduction conditional on the previously stated bounded-domain Bedford–Taylor comparison principle. This run independently verified its use, the compactness of each sublevel and the two limit operations; it did not independently prove the full upstream Bedford–Taylor construction.

## 2. A sharp support example for nonclosed E

Take $E=B_R=\{|z|<R\}\subset\mathbb C^n$ with $R>0$ (bounded, non-pluripolar and open). The Lelong-class extremal is
\[
\boxed{V_{B_R}^*(z)=\max\{0,\log(|z|/R)\}.}\tag{3}
\]
Indeed the displayed function is PSH, has logarithmic growth and vanishes on $B_R$, so it is an admissible minorant for the envelope. Conversely, for any admissible $w$ and any unit vector $\xi$, $t\mapsto w(t\xi)$ is subharmonic, is nonpositive for $|t|<R$, and is at most $\log^+|t|+O(1)$ at infinity. On $|t|>R$, subtract the harmonic $\log(|t|/R)$ and then a small positive multiple $\epsilon\log(|t|/R)$; the exterior maximum principle gives $w(t\xi)\le\log(|t|/R)+\epsilon\log(|t|/R)$. Let $\epsilon\downarrow0$. This proves (3) at every point, hence for the upper semicontinuous regularization.

For an independent direct mass calculation define the smooth radial PSH potentials
\[
u_m(z)=\frac1{2m}\log\bigl(1+(|z|/R)^{2m}\bigr),\qquad m\in\mathbb N.
\]
They decrease locally uniformly off $|z|=R$ and pointwise everywhere to (3). For any smooth radial PSH $f(|z|)$, Stokes and the $dd^c=i/(2\pi)\partial\bar\partial$ convention give
\[
\int_{B_r}(dd^c f)^n=2^{-n}\,[r f'(r)]^n
\]
provided the radial derivative vanishes suitably at the origin. This follows as well by writing $f=F(\log r^2)$, whose complex Hessian has $n-1$ tangential eigenvalues $F'/r^2$ and one radial eigenvalue $F''/r^2$, then integrating the determinant. Applied to $u_m$, the formula becomes
\[
\int_{B_r}(dd^c u_m)^n
=2^{-n}\left(\frac{(r/R)^{2m}}{1+(r/R)^{2m}}\right)^n.
\tag{4}
\]
As $m\to\infty$, (4) tends to $0$ for $r<R$ and to $2^{-n}$ for $r>R$. Radial invariance and bounded Bedford–Taylor decreasing continuity on compact sets identify the limiting measure:
\[
\boxed{(dd^cV_{B_R}^*)^n=2^{-n}\,\sigma_{\partial B_R},}\tag{5}
\]
where $\sigma_{\partial B_R}$ is normalized rotation-invariant surface probability. Hence
\[
\mu_{B_R}(E)=0,\qquad
\mu_{B_R}(\overline E)=2^{-n}.
\]
Even when $E$ is a perfectly regular *open ball*, the conclusion “$\mu_E$ is supported on $E$” is **false**. The original §16.34.2 correctly says $\overline E$.

**Status and affected dependents:** This is an exact check of §16.34.2's closed-set support quantifier and of the $2^{-n}$ normalization; it also illustrates the dependency of later equilibrium-measure arguments on careful distinction between E and its closure. It does not certify §16.34.2's full obstacle-gluing or external pluripolar-pole lemma for arbitrary bounded sets.

## Recommendation and coverage boundaries

Optional reading-edition proposal (not implemented): after §16.34.1 add the equality consequence for ratio $1$, or the more precise two-sided slope statement (1). Retain the proposition's one-sided inequality and source attribution; neither statement nor any permanent/source label needs replacement. After §16.34.2, consider the open-ball example (3)–(5), explicitly emphasizing why the support uses $\overline E$.

New direct verification: §16.34.1 lines 7–26, §16.34.2 lines 47–69 only for support/model and its displayed mass. One normalization crosscheck at the linked §13.5.1, not new review of that entire section. No previously registered error or gap is marked resolved; user-deferred proof programmes remain deferred-by-user. Current actual ToC has **25 chapters, 747 numbered sections, and zero fully certified mathematical sections**. No project build, CI, full test suite, formalization, or publication was performed.
