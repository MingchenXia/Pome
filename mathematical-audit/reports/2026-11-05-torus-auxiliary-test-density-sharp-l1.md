# A sharp $L^1$ auxiliary-density model on flat complex tori

**Date:** 2026-11-05. **Stable finding ID:** POME-DEGENMA-TORUS-AUXILIARY-L1-SHARP-001.
**Classification:** low / verified conditional deduction (a complete independent model calculation, *not* a verification of the general theorem).
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

## Current integrated reading anchors

- Main file: docs/sections/uniqueness-for-degenerate-equations--bounded-uniqueness-and-connectedness/index.html, blob 52185a663bef778cc6da47299bda5c32fcb05670, physical lines 172–225. Proposition **14.24.13**, source label non-kahler-pluripotential-theory:0687B449, permanent tag **7F590FD94846**; equation **14.24.14**, source non-kahler-pluripotential-theory:9AB915D8, permanent **6928CCD52E25**. Equation **14.24.15**, source :4514E499, permanent **768EAB7723D9**, lines 183–188, is the local Dirichlet input in the printed general proof. The quantitative gluing conclusion is at lines 205–225.
- In the same file, Proposition **14.24.2** (source non-kahler-pluripotential-theory:02FAC4D4, permanent **2C3AA01F259B**), its mixed comparison computation and equation 14.24.3 occupy physical lines 30–75 (the exact page should be consulted for final line offsets).
- Crosscheck only: docs/sections/uniqueness-for-degenerate-equations--comparison-and-invariant-mass/index.html, blob 7683a63656f9b4311a77d1db8e260a1bdc65f0b0, physical lines 8–16 and 37–68: Guan–Li condition (equation 14.25.1, source :4B4D43A0, permanent 0B3AF72C81CB) and Theorem 14.25.3 (source :27525A10, permanent FE27B72E2DB5). No claim that all bounded comparison or smooth existence inputs have been verified.

## Printed assertion being tested

Proposition 14.24.13 assumes a fixed compact Hermitian background $(X,\omega)$, a number $B_0>\|1\|_{L^2(\omega^n)}$, and a smooth function $g\geq1$ with $\|g\|_{L^2(\omega^n)}\leq B_0$. It supplies a smooth strictly $\omega$-psh potential $q$ and a uniform $\varepsilon>0$ such that
\[
(\omega+dd^cq)^n\geq \varepsilon g\,\omega^n.
\]
The proof uses local smooth Dirichlet equations, an $L^2$ Alexandrov–Bakelman–Pucci estimate, and a finite smooth gluing argument. Nothing in the printed statement asserts that $L^2$ is a necessary hypothesis or that its constructed $\varepsilon$ is optimal.

## Exact all-dimensional torus computation

Let $E=\mathbb C/(\mathbb Z+i\mathbb Z)$, $X=E^n$, and on each factor use
\[
\omega_j=\frac i2\, dz_j\wedge d\bar z_j=dx_j\wedge dy_j,\qquad
\omega=\sum_{j=1}^n\omega_j,\quad V=\int_X\omega^n=n!.
\]
The normalization used in Pome is $dd^c=\frac{i}{2\pi}\partial\bar\partial$. Let $g=g(x_1)$ be any smooth, positive, one-periodic function (the printed application takes $g\geq1$) and write
\[
m=\int_0^1g(x)\,dx=\frac1V\int_Xg\,\omega^n>0.
\]
The smooth function $4\pi(g/m-1)$ has zero mean on $\mathbb R/\mathbb Z$. Hence it has a smooth periodic twice-antiderivative $q=q(x_1)$, unique up to an additive constant:
\[
q''(x_1)=4\pi\left(\frac{g(x_1)}m-1\right).
\]
Indeed, the zero mean makes $q'$ periodic and choosing its integration constant so that $\int_0^1q'=0$ makes $q$ periodic as well. Direct differentiation gives
\[
dd^cq=\frac{q''}{4\pi}\,\omega_1
      =\left(\frac gm-1\right)\omega_1 .
\]
Consequently
\[
\omega_q=\frac gm\,\omega_1+\sum_{j=2}^n\omega_j>0,\qquad
\boxed{\ \omega_q^n=\frac gm\,\omega^n\ } .
\]
This calculation proves smooth strict positivity in every dimension and requires no Monge–Ampère existence theorem, Demailly approximation, Bergman construction, or external regularization input. It also supplies a direct normalization/sign check.

## Optimality of the coefficient and the hypothesis comparison

For this particular $g$, the largest possible constant $\varepsilon$ for which **some** smooth potential can obey $\omega_{\tilde q}^n\geq\varepsilon g\omega^n$ is exactly
\[
\boxed{\ \varepsilon_*(g)=\frac1m=\frac V{\int_X g\,\omega^n}\ } .
\]
The constructed $q$ attains equality. Conversely, since $\omega$ is closed, a smooth Stokes expansion gives $\int_X(\omega+dd^c\tilde q)^n=\int_X\omega^n=V$. Integrating the desired pointwise inequality gives $\varepsilon\leq V/\int_Xg\omega^n=1/m$. No statement about general non-Kähler mass invariance is being used.

Thus if one restricts to the one-coordinate family $g=g(x_1)\geq1$ and imposes only the $L^1$ bound $\int_Xg\omega^n\leq B_1$ (where $B_1\geq V$), then the **best uniform constant** is $V/B_1$. The constant test function $g=B_1/V$ proves this is optimal. Under the printed $L^2$ assumption, Cauchy–Schwarz yields $m\leq B_0/\sqrt V$, so the **best uniform constant within this model class** is
\[
\boxed{\ \varepsilon_{L^2,\mathrm{one\ coordinate}}=\frac{\sqrt V}{B_0}\ } ,
\]
again attained by the constant function $g=B_0/\sqrt V$. This is *not* asserted to be the optimal constant for Proposition 14.24.13 on an arbitrary Hermitian manifold.

The $L^2$ bound is not a necessary condition in this highly symmetric model. Choose a fixed smooth nonnegative $h$ supported in $(-1/4,1/4)$ with $\int_\mathbb Rh=1$ and, for integers $N\geq2$, let
\[
g_N(x_1)=1+Nh\bigl(N(x_1-\tfrac12)\bigr),
\]
periodically extended. These are everywhere at least $1$, smooth, and satisfy
\[
\int_Xg_N\,\omega^n=2V,\qquad
\|g_N\|_{L^2(\omega^n)}^2
=V\left(3+N\int_\mathbb Rh^2\right)\longrightarrow\infty.
\]
Nevertheless the explicit periodic potentials $q_N$ above satisfy, for **every $N$**,
\[
\omega_{q_N}^n=\tfrac12g_N\,\omega^n,\qquad
\omega_{q_N}\geq\tfrac12\omega.
\]
Thus even unbounded height, derivatives, and $L^2$ norms do not preclude a *uniform* smooth strict auxiliary comparison potential in this one-coordinate torus family. In contrast, constants $g_N\equiv N$ show that no positive uniform $\varepsilon$ can hold in this Kähler model without **any** mass or integral bound.

## An independent check of the connectedness proof's numerical factor

The original proof of Proposition 14.24.2 (physical lines around the equation following mixed comparison) writes $d=\kappa^{-1/n}-1$ and $\gamma=nd$. If $x,y$ denote the two pieces of the common measure, its displayed comparison yields
\[
(1+\gamma t)x+(1-nt)y\leq(1+\gamma t/2)(x+y).
\]
Rearranging gives $(\gamma/2)x\leq(n+\gamma/2)y$, and hence
\[
\frac{y}{x+y}\geq\frac{\gamma}{2(n+\gamma)}
=\frac{d}{2(1+d)}
=\frac{1-\kappa^{1/n}}2.
\]
This verifies the printed factor for this *one algebraic step*. The modified comparison inequality, mixed MA estimate, $W^{1,2}$ chain rule, continuity of bounded solutions, and general local Dirichlet theorem remain genuine unverified dependencies in this pass. No inference about the whole connected-positive-locus uniqueness theorem follows just from this arithmetic.

## Audit disposition

**Finding:** POME-DEGENMA-TORUS-AUXILIARY-L1-SHARP-001 — **low / verified conditional deduction**. The specific torus construction, Stokes optimality, the uniform $L^1$ family, and the concentration family are directly proved. The original Proposition 14.24.13 and Theorems 14.24.1/14.25.3 are **not refuted**; the original general $L^2$ proof is **not certified** by an exactly solvable subfamily.

**Proposed change:** an optional, separately reviewable example after Proposition 14.24.13 illustrating the natural $L^1$ mass obstruction in the Kähler one-coordinate setting and the distinction between a sufficient $L^2$ hypothesis and a necessary one. No changes to the statement, normalization, historical attribution, source bodies, or permanent tags are justified here.

**Affected logical dependents:** only as an illustrative check of the auxiliary test-potential step in the proofs of Theorem 14.24.1 and Corollary 14.24.17. The independent Guan–Li uniqueness route of §14.25 is crosschecked only at its mass-conservation premise. The entire actual §§14.24–14.25 are *not* certified.

**Coverage accounting:** first new exact one-coordinate torus model at §14.24.13–15 and first direct algebraic check of the numerical fraction in §14.24.2; §14.25.1/.3 is dependency/context only. The collection remains 25 chapters, 747 numbered sections, zero fully mathematically certified sections. All existing findings and all owner-excluded Demailly approximation/regularization and dedicated Bergman, weighted $L^2$, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain **deferred-by-user** rather than resolved.

**Execution:** manuscript-level algebra/analytic calculations only; no software test, build, formal verification, CI, or website publication was performed.
