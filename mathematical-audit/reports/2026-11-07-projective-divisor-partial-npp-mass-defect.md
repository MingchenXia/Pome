# 2026-11-07 — Exact partial non-pluripolar mass defect on projective hyperplanes

**Finding:** POME-NPP-PROJECTIVE-DIVISOR-PARTIAL-DEFECT-001. **Severity/status:** low / **verified conditional deduction**, not a false theorem. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

## Integrated source anchors and actual scope

- Main reading edition: docs/sections/non-pluripolar-products--capacity-convergence-and-loss-of-mass/index.html, blob d66813856cb813722806ab912afdfd4815d2da97, physical lines 41–67 (Lemma 13.7.3), 106–134 (Theorem 13.7.5), 138–140 (Example 13.7.6). Theorem source foundations-of-pluripotential-theory:AB4EBE3B, permanent tag 67C4F7EC316E; example source foundations-of-pluripotential-theory:D5678E03, permanent tag ACAEA8D8BE87.
- Bounded-product mass: docs/sections/non-pluripolar-products--global-finiteness-and-bounded-cohomological-mass/index.html, blob 943517743538820940559eae8469ce98ecf5fcd5, physical lines 10–32 (Proposition 13.5.1, source foundations-of-pluripotential-theory:4EE18BE1, permanent 06A36B9354A5) and 123–124 (Example 13.5.6, source D71F11C5, permanent 3D09B5B530AA).
- Pole-discarding definition: docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html, blob 81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c, physical lines 57–64 (Definition 13.2.4, source foundations-of-pluripotential-theory:9D8E4DD8, permanent D79952D7E272).
- Projective normalization: docs/sections/global-potentials-and-positive-cohomology-classes--curvature-and-metrics-defined-by-sections/index.html, blob ff56aa13950da3423135bb0bbaf40bcc980c21a1, lines 108–113 (Example 10.6.7, source E51945FB, permanent 4CE1D9D7D803).

The original printed §13.7.6 shows total loss in dimension one. The following *new* exact model covers **all intermediate mass defects, in every dimension**, and identifies the residual weak limit.

## Statement

Fix an integer $n\geq1$, let $X=\mathbf P^n$, $\omega=\omega_{\mathrm{FS}}$ normalized by $\int_X\omega^n=1$, and put $H=\{Z_0=0\}$. For a real parameter $0<\alpha\leq1$, define
$$
q([Z])=\log\frac{|Z_0|^2}{\sum_{j=0}^n|Z_j|^2},\qquad
u=\alpha q,\qquad u_k=\max\{u,-k\},\quad k>0,
$$
and $T=\omega+dd^cu$, $T_k=\omega+dd^cu_k$, with $dd^c=\frac i{2\pi}\partial\bar\partial$. Then $T=(1-\alpha)\omega+\alpha[H]\geq0$, the functions $u_k$ are bounded $\omega$-psh and decrease in the printed extended-capacity sense to $u$, and
$$
\boxed{\langle T^n\rangle=(1-\alpha)^n\omega^n,\qquad
\int_X\langle T^n\rangle=(1-\alpha)^n.}\tag{1}
$$
Every bounded Bedford–Taylor top product $\mu_k=T_k^n$ has total mass $1$, yet
$$
\boxed{\mu_k\ \xrightarrow{\mathrm{weak}}\
(1-\alpha)^n\omega^n+\bigl[1-(1-\alpha)^n\bigr][H]\wedge\omega^{n-1}.}\tag{2}
$$
The hyperplane probability $[H]\wedge\omega^{n-1}$ is **not** an unqualified product of singular currents. Its total mass is one. Consequently, for any prescribed defect $\beta\in[0,1]$, choose $\alpha=1-(1-\beta)^{1/n}$, including the trivial $\alpha=0$ case when $\beta=0$.

More strongly, write $\epsilon=e^{-k/\alpha}$, $Y=|Z_0|^2/\sum|Z_j|^2$, and split $X$ into the disjoint sets $A_\epsilon=\{Y>\epsilon\}$, $B_\epsilon=\{Y<\epsilon\}$ and $S_\epsilon=\{Y=\epsilon\}$. The three parts of $\mu_k$ have the **exact** masses
$$
\boxed{\begin{aligned}
\mu_k(A_\epsilon)&=(1-\alpha)^n(1-\epsilon)^n,\\
\mu_k(B_\epsilon)&=1-(1-\epsilon)^n,\\
\mu_k(S_\epsilon)&=\bigl[1-(1-\alpha)^n\bigr](1-\epsilon)^n.
\end{aligned}}\tag{3}
$$
Thus the measure escaping to the hyperplane comes from a real-hypersurface contact term and has an explicitly determined finite-level mass.

## Proof

**Positivity and admissible convergence.** The Poincaré–Lelong formula for the coordinate hyperplane gives $dd^cq=[H]-\omega$. Therefore $u$ is $\omega$-psh when $0<\alpha\leq1$. Since the constant $-k$ is also $\omega$-psh, $u_k=\max(u,-k)$ is bounded $\omega$-psh. Clearly $u_k\downarrow u$, including on $H$, so Lemma 13.7.3 establishes extended-capacity convergence. No continuity of the singular Monge–Ampère operator is assumed.

**Exact ambient volume distribution.** On the chart $Z_0\ne0$ set $w_j=Z_j/Z_0$, $t=\sum_{j=1}^n|w_j|^2$ and $Y=(1+t)^{-1}$. The adopted normalization yields
$$
\omega^n=\frac{n!}{\pi^n}\frac{dV_{\mathbf C^n}}{(1+t)^{n+1}},\qquad
\int_{\mathbf C^n}f(t)\,dV_{\mathbf C^n}
=\frac{\pi^n}{(n-1)!}\int_0^\infty f(t)t^{n-1}\,dt.
$$
The radial pushforward under $Y$ is exactly the Beta$(1,n)$ probability
$$
d(Y_*\omega^n)(y)=n(1-y)^{n-1}\mathbf1_{(0,1)}(y)\,dy.\tag{4}
$$
Thus $\omega^n(A_\epsilon)=(1-\epsilon)^n$ and $\omega^n(B_\epsilon)=1-(1-\epsilon)^n$. This computation independently verifies the factors $n!$, $\pi$ and the global mass-one convention.

**Bulk and the interface.** On $A_\epsilon$ the truncation equals $\alpha q$, so $T_k=(1-\alpha)\omega$ because $dd^cq=-\omega$ outside $H$. On $B_\epsilon$, including $H$, it equals $-k$, so $T_k=\omega$. In both regions the top Bedford–Taylor measure agrees with the corresponding smooth density. The remaining part $\sigma_k=\mathbf1_{S_\epsilon}\mu_k$ is positive and supported on $S_\epsilon$. Since $u_k$ is globally bounded, the integrated bounded-potential Stokes formula, Proposition 13.5.1, gives $\int_X\mu_k=\int_X\omega^n=1$. Subtracting the two bulk masses computed from (4) proves all three equalities (3), with no ignored boundary contribution.

**Identification of the weak limit.** The $B_\epsilon$ bulk has mass $1-(1-\epsilon)^n\to0$, and the $A_\epsilon$ bulk converges in total variation to $(1-\alpha)^n\omega^n$. Both $u_k$ and $\omega$ are invariant under $G=U(1)\times U(n)$, acting on $Z_0$ and on $(Z_1,\ldots,Z_n)$; hence $\sigma_k$ is $G$-invariant. The group acts transitively on $S_\epsilon$, so the normalized interface probability is the Haar-orbit measure represented by
$$
(\phi,\xi)\longmapsto [\sqrt\epsilon\,e^{i\phi}:\sqrt{1-\epsilon}\,\xi],\qquad
\xi\in S^{2n-1}.
$$
As $\epsilon\downarrow0$, these points converge uniformly in $(\phi,\xi)$ to $[0:\xi]$. Thus the normalized interfaces converge weakly to the unique invariant probability on $H\cong\mathbf P^{n-1}$, namely $[H]\wedge\omega^{n-1}$. Their masses converge by (3) to $1-(1-\alpha)^n$. Together with the bulk limits, this proves (2); it does not rely on passing a singular wedge product through a weak limit.

**Non-pluripolar measure.** On $X\setminus H$ the current $T$ is smooth and equals $(1-\alpha)\omega$. All local potentials of $T$ have poles on $H$ when $\alpha>0$, and Definition 13.2.4 makes the non-pluripolar product assign zero mass there. Therefore its top measure is exactly $(1-\alpha)^n\omega^n$ on the whole $X$ (the smooth volume itself does not charge $H$). This proves (1). Notice that for $\alpha=1$ the NPP mass is zero whereas $\mu_k$ converges to the hyperplane probability; for $0<\alpha<1$ both smooth and hyperplane components persist.

## Status, dependencies and affected theorems

This **does not refute Theorem 13.7.5**, whose lower inequality reads $1\ge(1-\alpha)^n$ in this model and whose extra mass-limsup condition fails whenever $\alpha>0$. It also does not refute Example 13.7.6; it strengthens that example with a continuum of exact losses and a full projective weak-limit formula. The sharp model is **conditional on the integrated bounded Bedford–Taylor/Stokes mass identity (Proposition 13.5.1)** and on the definition/compatibility of the non-pluripolar product (Definition 13.2.4). Those general inputs were inspected but not fully recertified; the radial density, boundary mass and weak limiting measure were independently computed here.

A possible **proposed** addition is a quantitative multi-dimensional example after Example 13.7.6. It would help prevent unguarded identification of the weak limit of bounded truncations with a singular non-pluripolar product in downstream §§13–17 and emphasizes the mass guard also relevant to the weighted Corollary 13.7.9. No production body, source, registry, canonicalization or permanent-tag change is made.

This is selected additional §13.7 coverage, **not a whole-section or general product certification**. Previous errors, proof gaps, candidates, external dependencies, duplicates and repairs remain at their prior statuses. The owner's excluded Demailly approximation/regularization, dedicated Bergman, weighted $L^2$, OT, multiscale and positivity-loss programmes stay **deferred-by-user**, neither solved nor reopened.
