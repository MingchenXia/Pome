# Exact real Monge–Ampère atoms of arbitrary weighted hinge arrangements

**Finding ID:** `POME-CONVEX-MA-HINGE-ZONOTOPE-VERTICES-001`  
**Date:** 2026-11-10  
**Severity / classification:** **low / verified conditional deduction**. No false printed theorem; no repair to the integrated source.  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated reading edition:** `docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html`; main blob `7089aa41ae2422b1bd6b5094e46668cbc8ed37be`.  
**Section:** §21.5, source heading `foundations-of-pluripotential-theory:34803B32`, permanent section tag `07CCE1F902ED`, HTML physical lines **5–9**.  
**Main inputs:** Theorem 21.5.1, source `foundations-of-pluripotential-theory:4A0FAEB3`, permanent tag `409656CC47D4`, HTML physical lines **10–42** (Alexandrov measure `n! vol(partial F(E))`); Proposition 21.5.4, source `foundations-of-pluripotential-theory:EAD83A50`, permanent tag `5D8A7A7D734E`, HTML physical lines **99–160** (positive symmetric multilinear mixed real Monge–Ampère measure); Equation 21.5.5, source `foundations-of-pluripotential-theory:24CC29A7`, permanent tag `D38381F0AC43`, HTML physical lines **143–151** (polarization). Reference Theorem 21.5.2 has permanent tag `F4072D9ED060`; its continuity proof is not needed below.

## Exact theorem for a hyperplane arrangement

Let `n >= 1`, let `a_1,...,a_m` be nonzero vectors in `R^n`, and let `b_i in R`, `c_i>0`. Put

```text
h_i(x) = c_i max(<a_i,x>-b_i, 0),       F(x) = sum_{i=1}^m h_i(x).
```

For every ordered `n`-element subset `I={i_1<...<i_n}` with `det A_I != 0`, let `A_I` be the matrix with rows `a_{i_j}` and let `x_I=A_I^{-1}(b_{i_1},...,b_{i_n})^T`. Then, with exactly the **`n!` normalization printed in §21.5**,

```text
MA_R(F) = n! sum_{|I|=n, det A_I != 0}
                   |det A_I| (prod_{i in I} c_i) delta_{x_I}.       (A)
```

Repeated intersection points are grouped by **adding** their coefficients. The empty sum is zero when `m<n` or every `n`-minor vanishes. For any `n` chosen indices `i_1,...,i_n`, the mixed measure satisfies

```text
MA_R(h_{i_1},...,h_{i_n})
  = |det(a_{i_1},...,a_{i_n})| (prod_{j=1}^n c_{i_j})
        delta_{A^{-1}b}                                       (B)
```

when their normals are linearly independent, and is zero when the normals are dependent (including repeated indices). Here `A` has the selected normals as rows and `b` has their corresponding offsets.

The slope body of `F` is the zonotope `Z=sum_i [0,c_i a_i]`; hence the total mass in (A) is `n! vol_n(Z)`. In particular, comparison with (A) gives the finite-dimensional volume identity

```text
vol_n(sum_i [0,c_i a_i])
   = sum_{|I|=n} |det A_I| prod_{i in I} c_i.                (C)
```

The distinction from previously recorded `POME-CONVEX-MA-SEPARABLE-STRATA-PERM-001` is material: (A) covers **non-orthogonal normals, nonconcurrent hyperplanes, arbitrary intersection multiplicities and absolute maximal minors**, rather than a separable coordinate crease/quadratic model. This is not the prior moving-hinge escape-to-infinity example.

## Proof, including support and normalization

**1. A finite sum of fewer than `n` independent hinge directions has zero real MA.** More generally, if `g(x)=sum_{j=1}^k d_j max(<v_j,x>-t_j,0)` and the vectors `v_j` span a proper subspace `V` of `R^n`, every supporting slope of `g` lies in `V`: the function is constant on lines parallel to `V^perp`, and the subgradient inequality along both directions of each such line forces the slope to annihilate `V^perp`. Thus `partial g(E) subset V` for all `E`; Theorem 21.5.1 gives `MA_R(g)=0`. This covers all proper subset sums in the polarization formula when exactly `n` hinges are selected.

**2. An independent `n`-hinge sum has one atom.** Suppose `v_1,...,v_n` are linearly independent. The unique point `x_*` at which all `<v_j,x>=t_j` is `V^{-1}t`. By the elementary subgradient rule for a finite sum of continuous convex functions (or directly by all directional derivatives), at `x_*`,

```text
partial g(x_*) = sum_{j=1}^n [0,d_j v_j]
               = V^T([0,d_1] x ... x [0,d_n]).
```

Its Euclidean/lattice-coordinate volume is `|det V| prod_j d_j`. To establish that no other point carries positive MA measure, partition space by the signs `<v_j,x>-t_j`. This is a **finite** polyhedral stratification. On each stratum with fewer than `n` active equalities, the subgradient lies in one fixed translate of the span of its active normals, so has dimension <`n`. There are only finitely many such strata; the union of their subgradients has Lebesgue measure zero. The only full-rank stratum is the singleton `x_*`. By Theorem 21.5.1, `MA_R(g)=n! |det V| (prod_j d_j) delta_{x_*}`. The finite-stratification argument is essential; nullity of individual subgradient sets alone would not suffice for an arbitrary convex function.

**3. Polarization determines each mixed atom.** Apply the printed Equation 21.5.5 to the `n` selected hinge functions. Every proper-subset diagonal measure is zero by Step 1. Thus their mixed measure is `MA_R(g)/n!`, which is formula (B). If the selected normals are dependent, every subset sum has slopes in a proper linear subspace, and the same polarization makes the mixed measure zero.

**4. Expand arbitrary finite arrangements.** Proposition 21.5.4 states symmetry, additivity and positive homogeneity in all `n` arguments. Expand `MA_R(F,...,F)` into `m^n` mixed terms. A term with a repeated index, or with linearly dependent directions, vanishes by Step 3. Each unordered independent subset `I` of size `n` occurs exactly `n!` times and contributes the same atom from (B). This proves (A) for all offsets, including multiple `n`-tuple intersections at the same point.

**5. Exact slope-body and total-mass check.** The recession function of `F` is `F^infty(v)=sum_i c_i max(<a_i,v>,0)`, i.e. the support function `h_Z(v)` of `Z=sum_i [0,c_i a_i]`. For a finite convex function, `dom F^*={p:<p,v> <= F^infty(v) for all v}`: necessity follows by taking `tv` and letting `t` grow; sufficiency follows because `F(x)` differs from `F^infty(x)` by at most `sum_i c_i |b_i|` uniformly in `x` (the hinge map is 1-Lipschitz). By convex separation this inequality set is precisely `Z`. Thus the slope body `K_F` is `Z`, and Theorem 21.5.1 gives `MA_R(F)(R^n)=n!vol_n(Z)`. Integrating (A) yields (C), including rank-deficient cases. This argument does not assume positivity of a smooth Hessian, absolute-continuity of MA, or a uniform bound on the offsets.

**Example (nonconcurrent arrangement).** For `n=2`, `F(x,y)=max(x,0)+max(y,0)+max(x+y-1,0)`, the three independent pairs meet at `(0,0)`, `(0,1)`, `(1,0)`, with absolute determinants all equal to one. Formula (A) gives

```text
MA_R(F) = 2 delta_(0,0) + 2 delta_(0,1) + 2 delta_(1,0).
```

The zonotope `[0,e_1]+[0,e_2]+[0,e_1+e_2]` has area three; the total mass is six. If `b_3` is changed to zero, all three vertices coalesce at `(0,0)`, and the formula yields one atom of mass six. Hence naive counting of *distinct* intersection points, without summing minors at coincident vertices, is incorrect.

## Classification and limitations

- **Status:** `verified conditional deduction` (low severity). The displayed algebraic/convex proof is complete once the specific internal axioms of §21.5.1 and Proposition 21.5.4 are admitted; those upstream general theorems and their entire dependency chains were **not independently certified in this pass**. No false statement in the printed source is asserted.
- **Suggested source change (not applied):** add a corollary/example after Proposition 21.5.4 with (A)–(C); preserve source attributions and both original theorem tags. The precise `n!` factor matters.
- **Potential dependents:** §21.5 real and mixed MA normalization; §21.11 convex-body interpretations and §21.12 toric piecewise-linear models **only when** the actual hypotheses match. No assertion on general singular non-pluripolar products, unbounded toric metrics, real MA for an infinite arrangement, or non-Archimedean limits.
- **External mathematical inputs:** only elementary finite-dimensional convex separation/subgradient calculus and volume change of variables, explicitly used above; no external complex-analytic proof is invoked. In particular **none** of the excluded Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof programme was opened.
- **Audit scope:** direct selected §21.5.1/.4/.5 statements and normalization plus this new finite model; §21.11/§21.12 are dependent contexts only. §21.5 was already partly reviewed; **0 first proof-level numbered-section visits, 0 completely certified sections**, current ToC baseline **25 chapters / 747 numbered sections**. No tests, builds, CI, formalization or publication were performed.
