# 2026-11-20 — Planar Wiener test: superexponential obstacles and the sharp two-stage logarithmic threshold

**Finding:** POME-WIENER-PLANAR-SUPEREXP-LOGLOG-001  
**Disposition:** low / **verified conditional deduction**; **not** an error in a printed theorem.  
**Reviewed current main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Scope:** complete direct reading of the integrated mathematical text of §4.4, but **not** a transitive certification of its upstream potential-theory proofs. No change to published text, permanent tags or source repositories.

## Exact integrated anchors

- Integrated §4.4, **docs/sections/perron-theory-and-fine-boundary-limits/index.html**, main blob **4bc2fb9317e2b6f6bb5b2d90208c677da8275eba**, mathematical physical lines **7–381**, section permanent tag **5CFAC22DC258**. Theorem **4.4.26**, source **classical-potential-theory:BE9DEDF9**, permanent tag **A856D11F5895**, lines **345–380**: exact Helms relative-capacity Wiener criterion, with convergence meaning thinness/irregularity.
- §4.4.22 (regularity iff nonthin complement), lines **305–314**, permanent tag **2B657EA5CC09**; §4.4.20 (thinness amplification and sphere-density estimate), lines **267–280**, permanent tag **201EE1A61AF0**; §4.4.5–6 (barriers and exterior-cone sufficient criteria), lines **51–81**, tags **2F74CBABB2A6**, **123C9AB7C052**.
- Selected capacity normalization in **docs/sections/potentials-energy-and-capacity/index.html**, blob **4962a7cd576a64cb47fa0955dcc80cf87c3da9d1**: Proposition **4.1.16** (Green potential and flux), lines **450–482**; Theorem **4.1.19**, lines **560–625** (compact outer capacity); Example **4.1.21**, lines **628–642**, tag **FC1E9D9B42F0** (exact planar concentric-ball relative capacity and circle equilibrium measure). These are selected input checks, not an entire §4.1 review.

## A planar model not covered by the earlier higher-dimensional sparse-ball finding

The existing report **POME-WIENER-SPARSE-BALLS-LOGLOG-001** (2026-10-30) established the corresponding **d≥3 power-kernel** model. The present calculation treats **d=2**, where the Wiener shells are doubly exponentially spaced in Euclidean radius and the condenser capacity behaves as the reciprocal of a logarithm. It does not re-count that report.

Fix $\alpha,\beta\ge0$, set $\lambda=2$, and for integers $j$ sufficiently large define
\[
A_j=(j+1)^\alpha[\log(j+\mathrm e)]^\beta,\qquad
\rho_j=\exp(-2^{j+1/2}),\qquad
s_j=\frac1{20}\exp(-2^{j+1/2}A_j).
\]
Put
\[
F_j=\overline{B(\rho_je_1,s_j)},\quad
E=\{0\}\cup\bigcup_{j\ge J}F_j,\quad
\Omega=B(0,1)\setminus E\subset\mathbb R^2.
\]
Choose $J$ large enough that every $F_j$ lies in $B(0,1/4)$. Then $E$ is compact, the balls are pairwise disjoint, $\Omega$ is a bounded connected Greenian plane domain, and $0\in\partial\Omega$.

**Sharp conclusion**:
\[
\boxed{\begin{aligned}
0\text{ is regular for }\Omega
&\iff \alpha<1\ \text{or}\ (\alpha=1,\ \beta\le1),\\
0\text{ is irregular for }\Omega
&\iff \alpha>1\ \text{or}\ (\alpha=1,\ \beta>1).
\end{aligned}}
\]
In particular the **double borderline $\alpha=\beta=1$ is regular**, although the complement occupies no exterior cone at the origin. This is a conclusion **conditional on the integrated Wiener criterion and the reviewed Green-capacity facts**, not an independent proof of general planar Perron theory.

### Proof: exact shell isolation

For the convention used in §4.4.26's planar proof, $\Phi(x)=\log(1/|x|)$, the shell
\[
S_j=\{2^j\le\Phi(x)\le2^{j+1}\}
=\{e^{-2^{j+1}}\le|x|\le e^{-2^j}\}.
\]
Its logarithmic midpoint radius is $\rho_j$. Since $A_j\ge1$, we have $s_j\le\rho_j/20$, so the whole $F_j$ belongs to $S_j$ for all sufficiently large $j$. The radii of consecutive centers are separated by a superexponential factor; $F_k$ is outside $S_j$ when $k\ne j$. The singleton $0$ and the complement of the unit disk do not meet these shells. Thus the **actual Wiener test set** $(\mathbb R^2\setminus\Omega)\cap S_j$ is exactly $F_j$ for all large $j$, without using a capacity-comparison shortcut for unions of obstacles.

The set $E$ is closed because its only accumulation point outside the individual closed discs is $0$, which is included. All discs lie on a single ray with disjoint radial projections and leave arbitrarily small gaps, so no exterior solid cone with vertex $0$ is contained in $E$. The connectedness of $\Omega$ follows by locally detouring polygonal paths around the finitely many discs that meet any compact path away from $0$; discs can accumulate only at the removed point $0$.

### Proof: uniform translated-disk relative capacity

Work in the fixed capacity ball $B_0=B(0,1/2)$ used in §4.4.26. For $K=\overline{B(c,s)}\subset B(0,1/4)$, the planar Green kernel is
\[
G_{B_0}(x,y)=\frac1{2\pi}\log\frac1{|x-y|}-H_{B_0}(x,y),
\quad 0\le H_{B_0}(x,y)\le M
\quad (x,y\in B(0,1/4)),
\]
with $M$ independent of $c$ and $s$ (the harmonic correction has uniformly bounded boundary data). Every probability measure $\nu$ supported on $K$ has Green energy at least
\[
I_{B_0}(\nu)\ge\frac1{2\pi}\log\frac1{2s}-M,
\]
since $|x-y|\le2s$ throughout $K\times K$. Conversely the uniform probability $\sigma$ on $\partial B(c,s)$ has logarithmic energy $(2\pi)^{-1}\log(1/s)$, by the circle equilibrium calculation in §4.1.21; subtracting the nonnegative harmonic correction only decreases its Green energy. Consequently, the equilibrium minimum-energy characterization yields constants independent of $j$ such that
\[
\frac{c}{\log(1/s_j)}\le C_{B_0}(F_j)
\le\frac{C}{\log(1/s_j)}
\quad (j\ge J).
\]
Compact capacitability in §4.1.19 gives $C_{B_0}^*(F_j)=C_{B_0}(F_j)$. This explicitly uses **relative Green capacity**, not logarithmic transfinite-diameter capacity.

### Proof: the exact critical series

Since
\[
\log(1/s_j)=2^{j+1/2}A_j+\log20,
\]
the two-sided capacity estimate gives
\[
2^j C_{B_0}^*(F_j)
\asymp A_j^{-1}
=(j+1)^{-\alpha}[\log(j+\mathrm e)]^{-\beta}.
\]
By Theorem 4.4.26, the complement is thin at $0$ **if and only if** the positive series of these terms converges. The elementary integral test gives convergence exactly when $\alpha>1$, or $\alpha=1$ and $\beta>1$. By §4.4.22, **thin complement means irregular boundary**, while divergence gives regularity. This proves the stated classification, including both critical equalities.

## Whole-section direct audit notes and limitations

All of the current integrated mathematical §4.4, physical lines 7–381, was read directly this run: (i) bounded Perron classes, completed harmonic measures, polar changes and restriction, **7–46**; (ii) local barriers, ball/cone/segment regularity, regular exhaustions, **49–81**; (iii) Green boundary limits, planar Greenian characterization, **84–114**; (iv) exterior compactification, Poisson–Kelvin formula, at-infinity supermean conventions and compactified Perron theory, **117–252**; (v) fine thinness, sweeping, fine limits, planar continua, and Wiener test, **255–381**.

The printed Wiener theorem's direction, exterior harmonic normalization, and the exact $d=2$ shell scale were checked against the statements and formulas. **No new confirmed printed false statement is claimed.** Full reconstruction of the upstream polar-discrepancy, fine-topology, sweeping, exterior lowering, or Perron-integrability theorems was **not** completed. In particular, inspection of a complete section does **not** certify its transitive proof graph. Any unverified dependency remains **unresolved/external as previously classified**, and nothing in this run changes the previously deferred status of the Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss programme.

**Suggested nonoperative patch:** optionally add the planar two-parameter example after Theorem 4.4.26, preserving original theorem, proof, source attribution, and permanent tags. The result informs §§4.4.20–26 and boundary-regularity applications using sparse planar obstacles; it does not repair or replace those theorems. No source, published text, tests, build, CI, or website was changed during this mathematical audit.
