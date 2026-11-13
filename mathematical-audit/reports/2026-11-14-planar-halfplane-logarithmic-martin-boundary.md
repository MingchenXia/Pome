# The planar upper-half-plane Martin boundary from the logarithmic Green kernel (2026-11-14)

**Finding:** POME-MART-HALFPLANE-LOG-GREEN-001.  
**Classification:** low / **verified conditional deduction**. Neither Theorem 3.2.6 nor Theorems 4.5.9, 4.5.12, 4.5.13 is refuted. The explicit Green asymptotics and normalization are proved here, while the existence of the arbitrary positive-harmonic Poisson representation is invoked from integrated Theorem 3.2.6, not certified transitively.

## Frozen integrated sources and anchors

- Production main: **b6933b772f41b45918f7e25ed1afbbb1fd892272**.
- Chapter 3: **docs/sections/kelvin-transforms-and-half-space-potentials/index.html**; blob **f2615a5393af724c3996978212162f94911ff9d9**. Standing dimension $d\ge2$ at physical line 7; Poisson kernel (3.2.5), source **classical-potential-theory:2C60ADF3**, permanent **21F1298C637C**, lines 57–62; half-space representation Theorem 3.2.6, source **classical-potential-theory:1C8A330A**, permanent **6BC86EEF03A9**, and integrability (3.2.7)–(3.2.8), permanent **F3ED29BBAD39** / **8F7C774A9D89**, lines 65–75; its ball/Kelvin derivation and weighted Radon details, lines 80–131.
- Chapter 4: **docs/sections/green-energy-and-martin-boundaries/index.html**; blob **976a90f2a5eba299658f73a1eee8b9d3fef8020f**. Martin cutoff and kernel normalization, line 106; Theorem 4.5.9, source **classical-potential-theory:1677A9F0**, permanent **9D6B5CF5E0CF**, lines 110–122; Theorem 4.5.12, source **classical-potential-theory:57D18B4C**, permanent **6736FBE7368C**, lines 166–185; Theorem 4.5.13, source **classical-potential-theory:854603A2**, permanent **0E65F552B1A6**, lines 190–213.
- Previous **POME-MART-HALFSPACE-ALL-MINIMAL-POISSON-001** proved the analogous reflection calculation only for $d\ge3$, with a power-law Newton Green function. Its stated $d=2$ exclusion is the **new exact case** reviewed here; the earlier $d\ge3$ result is not counted again.

## Precise theorem and hypotheses

Let $H=\{z=x+it:t>0\}\subset\mathbb C\simeq\mathbb R^2$ and $a=i$. Adopt the positive Green convention $-\Delta G_H(\cdot,w)=\delta_w$ and the compactification in §4.5 with $b(w)=G_H(w,a)$ whenever $w$ lies outside a fixed compact subset of $H$. In real dimension **two**, the entire Martin compactification is the one-point compactification of the **Euclidean closed upper half-plane**; its boundary is $\mathbb R\sqcup\{\infty\}$. Every boundary kernel is minimal. The kernels normalized at $a$ are
\[
\boxed{
 K_\xi(x+it)=\frac{t(1+\xi^2)}{(x-\xi)^2+t^2},\quad \xi\in\mathbb R,
 \qquad K_\infty(x+it)=t .
}
\tag{1}
\]
Convergence to the displayed boundary kernels is **locally uniform in the interior**, including every tangential escape to infinity.

For the unique positive harmonic half-plane representation of printed Theorem 3.2.6,
\[
h(x+it)=ct+\int_{\mathbb R}\frac{t}{\pi((x-\xi)^2+t^2)}\,d\nu(\xi),
\quad c\ge0,\quad \int_{\mathbb R}\frac{d\nu(\xi)}{1+\xi^2}<\infty ,
\tag{2}
\]
the **finite** Martin representing measure is exactly
\[
\boxed{\quad
\mu_h=c\delta_\infty+\frac{d\nu(\xi)}{\pi(1+\xi^2)},\qquad
\mu_h(\mathbb R\sqcup\{\infty\})=h(i)<\infty .
\quad}
\tag{3}
\]
Conversely, a finite positive measure $\mu$ on $\mathbb R\sqcup\{\infty\}$ yields (2) through $c=\mu(\{\infty\})$ and $d\nu(\xi)=\pi(1+\xi^2)d\mu|_{\mathbb R}$. No finite-total-mass assumption is made on $\nu$.

## Proof

**1. Correct logarithmic Green normalization and the finite boundary.** Reflection in the real axis gives
\[
G_H(z,w)=\frac1{2\pi}\log\frac{|z-\overline w|}{|z-w|}
=\frac1{4\pi}\log\left(1+\frac{4ts}{(x-\eta)^2+(t-s)^2}\right),
\quad w=\eta+is .
\tag{4}
\]
The identity $-\Delta_z(-(2\pi)^{-1}\log|z-w|)=\delta_w$, boundary cancellation and decay for fixed $w$ verify this positive Green function with the adopted convention. For $z$ in an arbitrary compact subset of $H$ and $\eta$ in a compact real interval, Taylor expansion of the **difference of the two logarithms** yields
\[
\frac{G_H(z,\eta+is)}s
=\frac{t}{\pi((x-\eta)^2+t^2)}+O(s^2)\quad(s\downarrow0),
\tag{5}
\]
uniformly in both compact parameters. This $O(s^2)$ remainder uses the oddness in $s$ of the logarithmic difference, not a pointwise limit with a moving pole. The same formula for $z=a=i$ gives $P_H(a,\xi)=1/[\pi(1+\xi^2)]$. Since $b(w)=G_H(w,a)$ near the finite Euclidean boundary, their ratio proves the first formula in (1).

**2. Uniform planar infinity asymptotic.** If $R=|w|\to\infty$, then for all $z$ in a fixed compact subset of $H$,
\[
D=(x-\eta)^2+(t-s)^2=R^2(1+O(R^{-1})),\qquad
0<4ts/D=O(R^{-1})
\]
uniformly for **all** $0<s\le R$, including $s/R\to0$. The exact logarithm in (4), with a relative rather than merely additive remainder, gives
\[
G_H(z,w)=\frac{ts}{\pi R^2}(1+O(R^{-1})).
\tag{6}
\]
The expression for $a$ is $s/(\pi R^2)(1+O(R^{-1}))$. As $b=G_H(\cdot,a)$ outside a compact set, division gives $K_\infty=t$ for *every* direction of escape. Also $K_\xi\to t$ as $|\xi|\to\infty$, locally uniformly in $z$.

**3. All Martin points, with no hidden logarithmic end.** In the Euclidean one-point compactification of $\overline H$, each escaping interior sequence has a subsequence with either a finite boundary limit or $|w|\to\infty$. Equations (5)–(6) compute all evaluation-coordinate limits; their convergence is locally uniform. Distinct finite $\xi$ give distinct Poisson poles, none equals $t$, and interior points are separated by the poles of their Green functions. The evaluation compactification of Lemma 4.5.8 therefore identifies the Martin compactification with this compact metrizable Euclidean one-point closure. This uses no *a priori* sequential-compactness assertion for an arbitrary Martin space.

**4. Minimality without invoking the general Martin representation theorem.** For every $h$ in (2) and every $f\in C_c(\mathbb R)$, the horizontal slice measures $h(x+it)\,dx$ converge vaguely to $\nu$ as $t\downarrow0$. Indeed, on a compact $\xi$-interval this is the Poisson approximate identity; off a sufficiently large interval containing $\operatorname{supp}f$, the test-integrated kernel is bounded by $C_ft/(1+\xi^2)$, so the weighted tail tends to zero. The $ct$ term vanishes on compact tests. This also proves uniqueness of $\nu$ without invoking Theorem 4.5.12.

If $0\le h\le K_\infty=t$, the vague trace is zero and (2) reduces to $h=ct$, so $K_\infty$ spans an extreme ray. If $0\le h\le K_\xi=P_H(\cdot,\xi)/P_H(a,\xi)$, trace domination forces $0\le\nu\le \delta_\xi/P_H(a,\xi)$. Moreover $cR\le h(iR)\le K_\xi(iR)=O(R^{-1})$ for $R\to\infty$, hence $c=0$. Thus $h$ is a nonnegative multiple of $K_\xi$. Every boundary point is minimal. The only unrecertified existence input is the already printed Theorem 3.2.6.

**5. Finite measure and exact constant-one model.** Substituting $P_H(\cdot,\xi)=K_\xi P_H(a,\xi)$ into (2) yields (3). Its mass is exactly $h(i)$; $\nu$ itself may have infinite mass. Uniqueness of $c$ also follows directly from
\[
c=\lim_{R\to\infty}\frac{h(iR)}R,
\quad \frac{P_H(iR,\xi)}R=\frac1{\pi(\xi^2+R^2)}
\le \frac1{\pi(1+\xi^2)}\ \ (R\ge1),
\]
by dominated convergence against the weight in (2). For the constant harmonic function $h\equiv1$, the boundary measure in (2) is $d\nu=d\xi$ and $c=0$, so its **normalized Martin probability** is the Cauchy measure
\[
d\mu_1(\xi)=\frac{d\xi}{\pi(1+\xi^2)},\qquad \mu_1(\{\infty\})=0.
\tag{7}
\]
This is a concrete normalized Perron/Poisson test for Theorem 4.5.13, not an assertion that the representing boundary Radon measure $d\xi$ is finite.

## Dependents, correction proposal and boundaries

- **Affected as illustrative/conditional instances:** Theorems 4.5.9, 4.5.12, 4.5.13, and 3.2.6. **No printed assertion is false.** The new content is the logarithmic $d=2$ end calculation and normalized Cauchy harmonic measure, not the already audited $d\ge3$ power-law calculation.
- **Proposed optional reading-edition patch, NOT applied:** include the two-dimensional companion example after Theorem 4.5.13 with formulas (1), (4), (6), (7), and the exact finite-measure conversion (3).
- **External/unverified input:** the *existence* component of the integrated positive half-space harmonic representation in Theorem 3.2.6 (its explicit Kelvin proof is read but not independently transitively certified). The reflection formula, limits, topology, minimality reduction and measure algebra are checked directly here. General Greenian-domain Martin theory and arbitrary boundary regularity remain uncertified.
- **Excluded by user:** Demailly approximation/regularization, dedicated Bergman/$L^2$/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programmes; earlier notes stay **deferred-by-user**, not resolved.
- **Coverage:** previously partly inspected numbered §§3.2 and 4.5; newly first proof-visited numbered sections **0**, entire-section certificates **0**. Production ToC remains **25 chapters / 747 numbered sections**. No build, test, CI, source/main/tag/registry edit, or website publication is asserted.
