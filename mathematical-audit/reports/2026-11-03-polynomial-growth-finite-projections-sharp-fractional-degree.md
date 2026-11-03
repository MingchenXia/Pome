# Weighted polynomial-growth finite projections: sharp fractional coefficient degrees

**Finding ID:** `POME-AFFINE-FINITE-GROWTH-EXPONENT-001`  
**Classification:** low / **verified conditional deduction** (not a false printed theorem and not a complete proof certification).  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (3 November 2026).  
**Actual integrated reading edition:** `docs/sections/affine-algebraicity-and-linear-growth/index.html`, main blob `8f2301f7696a0b230950918ae20a7f9e57be768b`.  
**Source anchors:** `demailly-complex-geometry:F8362024`, permanent `D8FA405BDFAC` (Lemma **9.61.2**, physical lines 10–26); source equation `demailly-complex-geometry:7EDA0F03`, permanent `D6D620F9E57D` (9.61.3, lines 12–16); `demailly-complex-geometry:A33B88FE`, permanent `D15F5F84A74A` (Theorem **9.61.4**, lines 31–61, especially 44–60). Corollary **9.61.5** (`demailly-complex-geometry:853EA48D`, permanent `A30D3E21C6D2`, lines 65–77) is an affected downstream context, **not** independently recertified.

## Mathematical question

The printed converse of Theorem 9.61.4 assumes the *linear* cone bound `|z''| <= C(1+|z'|)`. The argument constructs the monic fiber polynomial of a linear functional and derives total-degree `<=j` for its `j`-th elementary-symmetric coefficient. We checked whether the conclusion and its quantitative degree control survive arbitrary real polynomial-growth exponents, including the sublinear case, without treating the theorem number as an independent premise.

## Exact conditional strengthening and proof

Let `A` be a **nonempty, reduced, pure complex `p`-dimensional, closed analytic subset** of `C^p x C^r` and assume

```text
   |w| <= C(1+|z|)^s   on A,  C>0,  s>=0.                   (1)
```

Then `A` is an algebraic subset. More precisely, projection `pi:A -> C^p` is finite and proper; if `p>0`, the generic fiber consists of `d>0` distinct points, and for **every** complex-linear functional `ell` on `C^r` the fiber polynomial

```text
 P_ell(z,T) = product_(a in pi^(-1)(z)) (T-ell(a_w))
            = T^d + sum_(j=1)^d c_(ell,j)(z) T^(d-j)
```

initially formed off the analytic branch set extends with **polynomial coefficients** satisfying the *sharp real-exponent degree bound*

```text
             deg c_(ell,j) <= floor(s*j).                   (2)
```

If a coefficient is identically zero, the bound is vacuous. For `p=0`, the compact analytic set `A` is finite and hence algebraic. If `r=0`, the statement is immediate. The `s=0` endpoint is stronger: `A=C^p x F` for some finite set `F subset C^r`.

**Proof, including the analytic/algebraic interface.** For any compact `K subset C^p`, (1) bounds the inverse image inside the closed bounded set `K x closed_ball(0,C(1+sup_K|z|)^s)`; since `A` is closed, `pi` is proper. Every fiber is a compact analytic subset of `C^r` and is finite by the maximum principle on analytic branches. Here we use the *already printed* finite-open-map and exceptional-set steps of Lemma 9.61.2 (lines 21–26): purity and local openness give surjectivity onto `C^p` for `p>0`, and outside a proper analytic set `E` the map is an unramified `d`-sheeted cover. Those upstream theorems are conditional dependencies, **not newly certified here**.

On the complement of `E`, each root `ell(a_w)` has absolute value at most `C||ell||(1+|z|)^s`. Hence the elementary symmetric functions satisfy

```text
 |c_(ell,j)(z)| <= binom(d,j) (C||ell||)^j(1+|z|)^(s*j).
```

The symmetric coefficients are holomorphic on `C^p\E` and locally bounded at `E`; using the existing bounded-removability input cited in the printed proof (physical lines 50–56), they extend holomorphically to all of `C^p`. The inequality survives by continuity. For any multi-index `beta`, Cauchy's estimate on the polydisc `|z_i|<=R`, with `|z|<=sqrt(p)R`, gives

```text
 |[z^beta] c_(ell,j)| <= binom(d,j)(C||ell||)^j
                       (1+sqrt(p) R)^(s*j) R^(-|beta|).
```

For `|beta|>s*j`, this tends to zero as `R->infinity`. Thus (2) follows, **with the integer floor**, and all such coefficients are polynomials.

Finally `P_ell(z,ell(w))` vanishes on `A` by density of regular fibers and continuity. If `b=(b_z,b_w) notin A`, the finite fiber `pi^(-1)(b_z)` admits a linear functional `ell` distinguishing `b_w` from each of its vertical coordinates (exclude finitely many proper hyperplanes of linear forms). Properness lets the `d` roots over neighboring unbranched fibers converge along a subsequence to points of the fiber over `b_z`, so `P_ell(b_z,ell(b_w)) !=0`. Consequently the polynomial zero sets of **all** these `P_ell` intersect exactly in `A`. Noetherianity, as in printed Theorem 9.58.2, reduces this to finitely many equations; no analytic regularization is used.

When `s=0`, apply (2) to each vertical coordinate functional. Their fiber polynomials have **constant** coefficients, so only finitely many vertical coordinate values can occur. Hence `A` lies in finitely many horizontal planes `C^p x {w}`. Each irreducible component is pure `p`-dimensional and maps surjectively to `C^p` by the same finite-open-map argument, and therefore equals one of these planes. (For `p=0` the conclusion is simply a finite set.)

## Optimality and reproducible examples

For coprime positive integers `a,b`, put

```text
 A_(a,b) = {(z,w) in C^2 : w^b = z^a}.
```

It is a reduced irreducible affine curve parametrized by `z=t^b, w=t^a`. It satisfies the growth bound with the **fractional** exponent `s=a/b`, since `|w|=|z|^(a/b)`. Its generic projection fiber has `d=b` points, and

```text
 P_id(z,T) = T^b - z^a,   c_(id,b)(z) = -z^a.
```

The coefficient of order `j=b` has **exact** degree `a=floor(s*b)`. Thus (2) cannot be improved uniformly, including for `0<s<1`; sublinear growth does **not** make all finite covers trivial. At `s=0` the horizontal finite unions `C^p x F` attain the classification.

The calculation explicitly distinguishes *polynomial equations for a multivalued finite cover* from the false inference that each coordinate `w` is itself a polynomial in `z`. For example `w^2=z` has `s=1/2` and is not a polynomial graph.

## Finding classification and follow-up

- **Status:** verified conditional deduction, **not** confirmed error / proof gap / resolved entire theorem.
- **Severity:** low. The printed Theorem 9.61.4, its linear growth bound, and its coefficient-degree estimate are consistent with this computation.
- **Precise new coverage:** an independent growth-exponent extension and sharp algebraic models for *the converse* of Theorem 9.61.4 (physical lines **44–60**), plus Lemma 9.61.2's proper finite projection premise (physical lines **21–26**) and the stated equation (physical lines **12–16**). These lines were **previously partially reviewed**: do not count the section as first opened and do not certify all §9.61 or the algebraic/analytic equivalence.
- **Outstanding dependencies:** finite-open-map/analytic branch-set claims, proper-image/dimension inputs, locally bounded extension across analytic exceptional loci, and the algebraic Noetherian conclusion are used only as explicitly identified earlier results; their complete proof chains were not reverified. No Hironaka or excluded approximation machinery is used.
- **Proposed change (not applied):** optional *remark after Theorem 9.61.4* giving the arbitrary real exponent `s>=0`, degree `floor(s*j)`, and the sharp `w^b=z^a` test. Preserve all original source labels, permanent tags, historical provenance and source formulations; do **not** overwrite the original linear theorem.
- **Potential dependents:** polynomial control in later §9.61.5–6 and finite-projection/section-growth examples; do not claim those are independently verified or that this proof patches them.
- **Audit boundaries:** no source, canonical registry, published HTML, build, CI, formalization or production `main` changes. Owner-excluded Demailly approximation/regularization, its Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss proof programme remains **deferred-by-user**, not resolved.
