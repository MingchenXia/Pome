# Exact disc Monge–Ampère capacity and the sharp pole-level rate (13 November 2026)

**Finding ID:** `POME-BT-DISC-CAPACITY-SHARP-001`  
**Classification:** low / **verified conditional deduction**; **no printed theorem is refuted**.  
**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Reading-edition blob:** `docs/sections/bedford-taylor-products-and-local-capacity--weighted-estimates-and-monge-ampere-capacity/index.html`, `801a6ce8d25a6db19202cbc295937a135a9a208e`.

## Precise source anchors and hypotheses

* **Definition 7.4.2:** source `foundations-of-pluripotential-theory:AF32B1A0`, permanent tag `E9E7C75396D2`, physical lines **85–94**. For a bounded open set $D\subset\mathbf C^n$, $\operatorname{Cap}_D(E)=\sup_{v\in\mathrm{PSH}(D),\,0\le v\le1}\int_E(dd^cv)^n$, and outer capacity is defined by open supersets.
* **Proposition 7.4.3:** source `foundations-of-pluripotential-theory:DE1E4FA5`, permanent tag `97EFDB6FDEE3`, lines **97–139**; this supplies monotonicity and countable subadditivity, and the reading edition distinguishes capacity from outer capacity.
* **Proposition 7.4.4:** source `foundations-of-pluripotential-theory:554B46C3`, permanent tag `815E5BBFC34A`, statement lines **143–149**, proof lines **151–165**; its first assertion bounds the outer capacity of a compactly localized pole sublevel by $C\|V\|_{L^1(L)}/s$. We test the *exponent* $s^{-1}$, not its numerical constant.
* **Theorem 7.4.1:** source `foundations-of-pluripotential-theory:93A06A12`, permanent tag `7C68264563C0`, statement around lines **9–16**, proof **18–80**; used only as contextual analytic input in the printed proof of Proposition 7.4.4, not needed for our explicit one-dimensional calculation.

Pome fixes $dd^c=(i/2\pi)\partial\bar\partial$. In one complex variable this equals $(4\pi)^{-1}\Delta$ as a measure relative to the Euclidean area form, so **$dd^c\log|z|^2=\delta_0$**. That factor fixes the result below; it must not be confused with the normalization of Green energy/capacity in Chapter 4.

## New exact capacity theorem

For $0<r<R<\infty$, let $D_R=\{z\in\mathbf C:|z|<R\}$, $K_r=\{|z|\le r\}$, and $E_r=\{|z|<r\}$. Then

\[
\boxed{\operatorname{Cap}_{D_R}(K_r)
=\operatorname{Cap}_{D_R}^{*}(K_r)
=\operatorname{Cap}_{D_R}(E_r)
=\operatorname{Cap}_{D_R}^{*}(E_r)
=\frac{1}{2\log(R/r)}.}
\]

All four equalities use the capacity convention in Definition 7.4.2, not the classical Green-energy capacity of Chapter 4.

### Proof of the upper bound, including nonsmooth competitors

Let $0\le v\le1$ be any subharmonic function on $D_R$, and $\mu=dd^c v$. In particular $v(0)\ge0$ is finite. For every $r<t<R$, the circular-mean/Riesz identity in the stated normalization is

\[
\frac{1}{2\pi}\int_0^{2\pi}v(te^{i\theta})\,d\theta-v(0)
=\int_{|a|<t}\log\frac{t^2}{|a|^2}\,d\mu(a).
\tag{1}
\]

For completeness, this identity follows distributionally from $\Delta v=4\pi\mu$: the circular mean has radial derivative $m'(t)=2\mu(D_t)/t$ for almost every (t), and integrating in (t) yields (1) by Tonelli; endpoint values follow by the usual radial-mean continuity for subharmonic functions. Thus no differentiability of the competitor, no sequence compactness, and no regularization/approximation theorem is needed.

The left side of (1) is at most (1). On $K_r$ the kernel is at least $2\log(t/r)$, giving

\[
2\log(t/r)\,\mu(K_r)\le1,
\qquad
\mu(K_r)\le\frac{1}{2\log(t/r)}.
\]

Let $t\uparrow R$. The resulting upper bound is independent of (v), hence applies to the supremum in Definition 7.4.2.

### Exact extremizer and boundary mass

Set
\[
v_r(z)=\max\left\{0,\frac{\log(|z|/r)}{\log(R/r)}\right\}.
\]
It is subharmonic on $D_R$, $0\le v_r<1$, and continuous across (|z|=r). Its radial derivative jumps from (0) to $1/[r\log(R/r)]$. The distributional radial Laplacian gives

\[
dd^cv_r
=\frac{1}{2\log(R/r)}\,\sigma_r,
\qquad
\int\phi\,d\sigma_r=\frac1{2\pi}\int_0^{2\pi}\phi(re^{i\theta})\,d\theta.
\tag{2}
\]

The boundary circle belongs to $K_r$, proving the matching lower bound for $\operatorname{Cap}_{D_R}(K_r)$. For the *open* disc $E_r$, the extremizer in (2) alone puts its mass on the excluded boundary, so one must **not** claim it directly attains the open-disc supremum. Instead take closed $K_{r'}\subset E_r$ with $r'\uparrow r$. Monotonicity and the already proved closed-disc formula give the same supremum for $E_r$. Because $E_r$ is open, its outer capacity equals its capacity by definition. For $K_r$, its outer capacity is at least its capacity and at most the capacities of $E_{r+\eta}$ for $0<\eta<R-r$; send $\eta\downarrow0$.

This also proves $\operatorname{Cap}_{D_R}^{*}(\{0\})=0$ by sending $r\downarrow0$.

## Sharpness of Proposition 7.4.4

Let $D=D_1$ and $V(z)=\log|z|^2\in\mathrm{PSH}(D)$. Although $V(0)=-\infty$, it belongs to $L^1_{\mathrm{loc}}(D)$. For each $s>0$,

\[
\{V<-s\}=E_{e^{-s/2}},
\qquad
\boxed{\operatorname{Cap}_D^*(\{V<-s\})=\frac1s.}
\tag{3}
\]

Choose fixed compact discs $K=K_a$, $L=K_b$ with $0<a<b<1$. If $s>-2\log a$, then $\{V<-s\}\subset\operatorname{Int}K$, so

\[
\operatorname{Cap}_D^*\bigl(K\cap\{V<-s\}\bigr)=s^{-1}.
\tag{4}
\]

Consequently, the order $s^{-1}$ in Proposition 7.4.4 **cannot be replaced uniformly by $o(s^{-1})$** even in complex dimension one for one fixed $V,K,L,D$ satisfying all printed hypotheses. This is a sharpness check, **not** a false statement and **not** a verification of the general theorem's complete CLN dependency chain. It is also distinct from the Chapter 4 Green-energy circle measure calculations, which use a different capacity and normalization.

## Status and dependents

* **Status:** verified conditional deduction; severity **low**. The explicit one-variable measure and capacity calculation is self-contained once elementary distributional polar coordinates/Jensen are accepted; the existing printed Proposition 7.4.4 is consistent. No hypothesis needs to be removed or added.
* **Proposed nonproduction correction/addition:** optionally add a short example after Proposition 7.4.4 recording (2)–(4), with the factor (2), and distinguishing open- versus closed-disc extremization. Do not modify source content, stable tags or canonical registry in an audit-only commit.
* **Affected dependents:** quantitative uses of Proposition 7.4.4 in §7.5 (capacity convergence) and §7.6 (exceptional envelopes) inherit an $s^{-1}$ rate that is generally optimal at logarithmic poles. This does **not** prove optimality in every narrower hypothesis class of those results.
* **Remaining inputs:** the full proofs of Theorem 7.4.1 and the general Bedford–Taylor continuity chain are not certified by this calculation. No user-excluded Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, atlas or positivity-loss work was opened or performed.

**Coverage credit:** selected new proof/sharpness check in previously partly reviewed §7.4; zero new first-visited numbered sections; zero complete theorem-chain or entire-section certifications. Actual production table of contents: 25 chapters / 747 numbered sections. No build, CI, test suite or publication was run.
