# Sharp quantitative Hausdorff continuity of Okounkov bodies in the semigroup pseudometric

**Finding ID:** `POME-OKO-SG-HAUSDORFF-HOLDER-SHARP-001`  
**Date:** 2026-11-14 (Asia/Shanghai)  
**Classification:** low / **verified conditional deduction**; no printed theorem is asserted false.  
**Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated §19.2:** `docs/sections/the-theory-of-okounkov-bodies--almost-semigroups/index.html`, Git blob `33212916f9ea7754f51f8194cfb76c2fcbe8efab`.  
**Integrated §19.7:** `docs/sections/almost-semigroups/index.html`, Git blob `33898b2963ad0f8b7e30bf414276642f60925b74`.  

## Exact source anchors and scope

- §19.2, physical lines **7–19**: closed pointed cone `C`, finite slices, and ambient dimension `n >= 0`; **the quantitative result below assumes n >= 1**.
- Equation **19.2.1**, lines **22–29**, original source `sgpt:2379D50B`, permanent tag `A3A5C96E566B`: the limsup symmetric-difference pseudometric `d_sg`.
- Definitions **19.2.3–4**, lines **57–60, 90**, source `sgpt:C5989909` / `sgpt:09011B25`, permanent tags `923345ACA44A` / `B62535F66376`: full-lattice semigroups and compact convex Okounkov bodies.
- Theorem **19.2.5**, lines **91–111**, source `sgpt:D2CDA8AC`, permanent tag `37D86D761E81`: full degree-wise lattice-count limit `k^{-n} #S_k -> vol Δ(S)`; its proof invokes the Kaveh–Khovanskii input in §19.7.20. The pointwise interior filling / Hausdorff limit is a different clause, not needed for the initial counting estimate.
- Definition **19.2.9** and Theorem **19.2.10**, lines **69–84**, sources `sgpt:E4CCE4D8`, `sgpt:870F54F8`, permanent tags `78B565EC56CF`, `2534E787147E`: positive-volume almost-semigroup closure, **qualitative** Hausdorff continuity and volume identity.
- §19.7 Theorems **19.7.20** and **19.7.32**, lines **299–319** and **536–648**, source labels `sgpt:282DA4DD` / `sgpt:ED83BFDD`, permanent tags `85641516C8CA` / `1551B679B8B7`: respectively the counting input and the existing continuity extension. Only the expressly identified consequences are used here, not a complete re-certification of those theorems.

This is a direct, independent *quantitative consequence* of the actual integrated statements; it does not reproduce the previous full-lattice conductor or exact combinatorial symmetric-difference observations. The historical Kaveh–Khovanskii attribution is retained.

## Statement (sharp exponent)

Let `n >= 1`. Let `Q = {x in R^n : (x,1) in C}`, a compact convex set. If the positive-volume class is nonempty, `D = diam(Q) > 0`. For **any two** positive-volume almost semigroups `S,T in overline(S'(C))_{>0}`, the extension in Theorem 19.2.10 satisfies

```text
vol_n(Delta(S) symmetric_difference Delta(T)) <= d_sg(S,T),

d_H(Delta(S), Delta(T)) <=
    D * (d_sg(S,T) / min(vol(S), vol(T)))^(1/n).
```

Here `d_H` is Euclidean Hausdorff distance, `vol` has the printed, unnormalized Euclidean convention, and `d_sg` is a pseudometric (the bound is invariant under its zero-distance equivalence). For every fixed positive lower bound `v` on both semigroup volumes, the extension is therefore uniformly `1/n`-Hölder with modulus `D v^{-1/n}`. **No exponent greater than `1/n` can hold uniformly for all such pairs in dimension `n`.**

## Complete proof of the new geometric and counting steps

**1. A one-sided convex cap estimate.** Let `K,L` be nonempty full-dimensional compact convex sets contained in `Q`; put `h = sup_{x in K} dist(x,L)`. Fix `x in K` with `dist(x,L)=h`. For any `0<t<h/D` the homothetic set `K_t = x+t(K-x)` is contained in `K` by convexity and contained in the ball `B(x,tD)`, which is disjoint from `L`. Hence
```text
vol(K\L) >= vol(K_t) = t^n vol(K).
```
Letting `t` increase to `h/D` proves `h^n vol(K) <= D^n vol(K\L)`. (If `h=0`, the inequality is immediate.) Interchange `K,L` to obtain
```text
d_H(K,L)^n <= D^n *
 max( vol(K\L)/vol(K), vol(L\K)/vol(L) )
 <= D^n vol(K triangle L)/min(vol K,vol L).
```
This uses neither smooth boundary nor any interior-ball theorem.

**2. Count the unavoidable symmetric difference of full-lattice semigroups.** First suppose `S,T in S'(C)`, with `K=Delta(S)` and `L=Delta(T)`. Every point of `S_k` belongs to `kK` and every point of `T_k` belongs to `kL`; hence
```text
#(S_k intersect T_k) <= #(k(K intersect L) intersect Z^n).
```
The compact convex intersection `K intersect L`, including a potentially lower-dimensional intersection, is Jordan measurable, so the upper bound divided by `k^n` converges to `vol(K intersect L)`. On the other hand, Theorem 19.2.5 yields the two full limits `#S_k/k^n -> vol(K)` and `#T_k/k^n -> vol(L)`. Substituting in Equation 19.2.1 gives
```text
d_sg(S,T) >= vol(K)+vol(L)-2 vol(K intersect L)
            = vol(K triangle L).
```
Combining with Step 1 proves both inequalities for actual full-lattice semigroups. In particular, an unproved assertion about the asymptotic density of the **intersection semigroup** is not necessary.

**3. Pass to positive-volume almost semigroups without interchanging limits.** By the *defined pseudometric closure*, choose sequences `S_j,T_j in S'(C)` tending in `d_sg` to `S,T`. The pseudometric triangle inequality implies `d_sg(S_j,T_j) -> d_sg(S,T)`. Theorem 19.2.10 gives Hausdorff convergence of the two convex bodies, and its volume formula gives `vol(S_j)->vol(S)>0` and likewise for `T_j`. Hausdorff convergence of compact convex bodies in the fixed compact `Q` implies almost-everywhere convergence of their indicator functions off their zero-Lebesgue-measure boundaries; dominated convergence gives the needed continuity of symmetric-difference volume. Passing to the limit in the established finite-stage inequalities proves the displayed bounds. Using **sequences here is legitimate because closure is taken in a pseudometric space**, which is first-countable after zero-distance identification; this is not an assumption about weak compactness of currents or arbitrary directed nets.

**4. Sharpness with honest generating semigroups.** Take `Q=[0,1]^n` and the cone over `Q`. For integers `q>=2`, write `h=1/q`, and let
```text
S   = {(m,k) in Z^n x N : 0<=m_i<=k for every i};
T_h = {(m,k) in S : m_1+...+m_n >= h*k}.
```
Both are additive semigroups. For each coordinate `i`, both `(e_i,1)` and `(e_i,2)` belong to `T_h` because `2h<=1`. Their difference gives `(0,1)` in the **group generated by** `T_h`, and subtracting this from `(e_i,1)` gives `(e_i,0)`. Thus `T_h` (and `S`) really generates `Z^{n+1}`, so no weaker non-full-lattice class has been substituted.

The bodies are `K=Q` and `L_h=Q intersect {sum x_i >= h}`; the removed corner is the simplex `{x_i>=0,sum x_i<h}`, with exact volume `h^n/n!`. Standard cube-grid Riemann sums give
```text
d_sg(S,T_h)=h^n/n!,  vol(S)=1,
vol(T_h)=1-h^n/n!,  d_H(K,L_h)=h/sqrt(n).
```
The nearest point of `L_h` to the removed vertex `0` is `(h/n,...,h/n)`; projection along the all-ones vector proves the same upper bound for every other removed point. Therefore `d_H` is proportional to `d_sg^(1/n)` as `q->infinity`, while the two volumes remain uniformly bounded away from zero. A hypothetical uniform exponent `alpha>1/n` would imply `h <= constant*h^(n*alpha)` for arbitrarily small `h`, impossible.

## Audit classification and recommended disposition

**Low / verified conditional deduction.** The printed §19.2.5 and §19.2.10 and the §19.7 semigroup results are **not refuted**. A possible standalone addendum is the sharp dimension-dependent Hölder estimate and its explicit cube-corner family; the production body is intentionally unchanged. Dependencies: Theorem 19.2.5's full degree-wise counting limit and Theorem 19.2.10's existing continuity extension, with §19.7.20/32 as their named internal sources. Neither their original lengthy proofs nor general Okounkov-body constructions, valuation regularity, external algebraic inputs or §19.4–§19.6 were transitively certified. No user-excluded Demailly regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss programme was examined. Preserve such earlier notes **deferred-by-user**, not resolved.
