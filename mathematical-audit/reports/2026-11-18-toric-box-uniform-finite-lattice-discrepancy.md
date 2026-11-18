# 2026-11-18 — Finite-scale translation-uniform convex lattice discrepancy

**Finding ID:** POME-TORIC-LATTICE-UNIFORM-BOUNDARY-DISCREPANCY-001  
**Severity/status:** low / **verified conditional deduction** (quantitative strengthening, not an error in the printed theorem).  
**Current main:** b6933b772f41b45918f7e25ed1afbbb1fd892272 (read afresh this session).  
**Primary integrated edition:** docs/sections/convex-analysis-and-toric-potentials--lattice-points-and-volume/index.html; blob 5d209b7f4d2156c19bc3fb300303405df6321230. Theorem 21.7.3, source label foundations-of-pluripotential-theory:364BCD30, permanent tag 831AEEB7084F, physical lines 58–62 (statement), 67–88 (cell proof); Proposition 21.7.2, source foundations-of-pluripotential-theory:5E9AEE47, permanent EDD78BC61BD7, lines 28–53. Secondary downstream: docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html, blob 7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c, Theorem 21.9.5, source foundations-of-pluripotential-theory:BD98CC5B, permanent 69D3D97E7701, lines 138–149 and use of 21.7.3 at line 166.

## Quantitative claim

Identify M with Z^n by the fixed basis of §21.7, and take n≥1. Let K be any nonempty compact convex subset of [-R,R]^n, R≥0; **no nonempty-interior assumption** is imposed. Let k≥1 be an integer, a∈R^n arbitrary, and r≥0. Define

\[
t=\frac{r+1}{k},\quad \delta=\frac1k,\qquad
N_{k,r,a}(K)=\#\bigl((kK)^r\cap(\mathbb Z^n+a)\bigr),
\]

where the superscript denotes the closed Euclidean outer parallel set, exactly as in §21.7. Then

\[
\boxed{\left|k^{-n}N_{k,r,a}(K)-\operatorname{vol}_n(K)\right|
 \le 2nt\,[2(R+t)]^{n-1}.}\tag{A}
\]

The bound is **simultaneously uniform** in every convex K contained in the same coordinate box and in every translation a; it is nonasymptotic. When r_k=o(k) it gives the explicit O((r_k+1)/k) error for bounded R, strengthening the fixed-K qualitative assertion of 21.7.3. For fixed r (in particular r=0), the order 1/k is optimal even for full-dimensional polytopes; no claim about the best leading constant is made.

For f real-valued and Lipschitz with constant L on Q_t=[-R-t,R+t]^n, and with M_f=sup_{Q_t}|f|, the weighted form is

\[
\boxed{\begin{aligned}
\left|k^{-n}\!\!\sum_{m\in(kK)^r\cap(\mathbb Z^n+a)}f(m/k)
-\int_K f(x)\,dx\right|
&\le \frac{L\sqrt n}{k}[2(R+t)]^n\\
&\quad+2nM_f\left(t[2(R+t)]^{n-1}
+\delta(2R)^{n-1}\right).
\end{aligned}}\tag{B}
\]

These are purely real convex-geometric estimates; no complex analytic approximation or Bergman, L² or extension argument is involved.

## Self-contained proof

Write C_s=[-s,s]^n and define the inner parallel set K\ominus C_s={x:x+C_s⊂K}. We first establish the two *finite-scale* volume estimates

\[
\begin{split}
\operatorname{vol}(K+C_s)-\operatorname{vol}(K)
&\le 2ns[2(R+s)]^{n-1},\\
\operatorname{vol}(K)-\operatorname{vol}(K\ominus C_s)
&\le 2ns(2R)^{n-1}. \tag{C}
\end{split}
\]

For the first bound, add the coordinate segments [-s,s]e_i successively, retaining convexity. Along any line parallel to e_i, a convex cross-section is either empty or an interval; adding the segment increases the length of every nonempty fiber by precisely 2s. By Fubini, the volume increase is 2s times the (n−1)-dimensional measure of the orthogonal projection of the intermediate body. All those projections lie in [-R-s,R+s]^{n-1}, giving at most 2s[2(R+s)]^{n-1} per step. Summing proves the first inequality, including lower-dimensional K (a zero-length fiber contributes the same formula).

For the second bound, apply successive erosions by [-s,s]e_i. Minkowski erosion satisfies (A\ominus S)\ominus T=A\ominus(S+T), so after n steps one obtains K\ominus C_s. In a coordinate fiber, erosion changes interval length \ell to max(\ell−2s,0); the loss is at most 2s on each nonempty fiber. Every intermediate eroded body lies within [-R,R]^n. Fubini bounds each loss by 2s(2R)^{n-1}, proving the second inequality. Empty intermediate bodies pose no problem. The argument works also for n=1, with the convention that the zero-dimensional projection has measure one.

Now tile R^n by half-open cells A_m=m/k+[0,1)^n/k for m∈Z^n+a. Let U be the union of those cells whose anchors m/k belong to (K)^{r/k}, equivalently m∈(kK)^r. The tiling gives vol(U)=k^{-n}N_{k,r,a}(K). For x∈U, the anchor is at coordinatewise distance less than δ; that anchor is at Euclidean distance at most r/k from K, hence x∈K+C_t. Conversely, if x∈K\ominus C_\delta, the anchor of the unique cell containing x differs in each coordinate by less than δ, so the anchor belongs to K and its cell is selected. We have the **uniform sandwich**

\[
K\ominus C_\delta\subset U\subset K+C_t. \tag{D}
\]

By (C), the positive overcount is at most D_out=2nt[2(R+t)]^{n-1}, while the negative undercount is at most D_in=2nδ(2R)^{n-1}. Since t≥δ, D_in≤D_out. This proves (A), with no appeal to asymptotic intrinsic-volume or Steiner formulae.

For (B), every selected cell and anchor lie in Q_t. On a cell, |f(x)−f(m/k)|≤L√n/k. Summing cellwise gives an error at most (L√n/k)vol(U)≤(L√n/k)[2(R+t)]^n. Also (D) and (C) imply vol(U\triangle K)≤D_out+D_in. Bounding f by M_f gives the second term of (B). Importantly, all bounds are independent of a.

Finally, take K=[0,1]^n, a=0 and r=0. For every k, N_{k,0,0}(K)=(k+1)^n, hence

\[
k^{-n}N_{k,0,0}(K)-\operatorname{vol}(K)
=(1+k^{-1})^n-1=\frac n k+O(k^{-2}).
\]

Thus no general bound o(k^{-1}) holds even for a fixed smooth-sided lattice polytope; the finite-scale rate in (A) is optimal in order. This elementary exact count, not an old arithmetic test, is the sharpness argument.

## Classification, dependencies and proposed correction

**Printed result:** Theorem 21.7.3 is correct; this is an optional **quantitative corollary** after it. It does not remove or replace the earlier qualitative moving-body theorem POME-LATTICE-MOVING-BODY-001, nor the Haar-shift checks; these are different quantifiers and do not supply the new explicit box-uniform constant (A). The present proof uses only Euclidean coordinate tiling, convex fibers, Fubini and finite-measure additivity, and is independent of the excluded programme.

**Affected downstream:** Theorem 21.9.5 identifies h^0(X_P,L^k)=#(kP∩M). If P lies in a fixed coordinate box, formula (A) with r=0 gives the explicit conditional dimensional estimate |k^{-n}h^0(X_P,L^k)−vol(P)|≤(2n/k)[2(R+1/k)]^{n−1}. This is an estimate on counts, **not** a certification of the toric section correspondence or general Okounkov-body convergence. It also applies directly to varying convex polytopes with a common box, without assuming their Hausdorff convergence, but makes no claim about the target limit unless bodies converge.

**Coverage:** proof-level revisit only of §21.7.3, Proposition 21.7.2 context and §21.9.5 counting consequence. §§21.7 and 21.9 were already partially audited; **+0 newly first-visited sections, +0 complete section certifications**. Actual prior table of contents is 25 chapters, 747 numbered sections; no all-project review asserted. All former unresolved and genuine-duplicate entries retain their separate statuses. Demailly regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss dedicated programmes remain **deferred-by-user**, neither resolved nor certified. No build, test suite, GitHub Actions CI, source/body/registry, main-branch or website changes were made.
