# Internal Lelong–Jensen proof already supplies the Hausdorff trace estimate (2026-11-02)

**Stable finding:** `POME-HAUSDORFF-LELONG-INTERNAL-001`  
**Severity / disposition:** low / **verified repair** of an external-proof dependency **proposed, not applied**. This is neither a false source theorem nor an entirely certified proof chain.  
**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Scope:** direct integrated-reading-edition proof inspection of §6.33.1–5 against Corollary 5.34.3, not the excluded Demailly approximation, Bergman, weighted-`L^2`, Ohsawa–Takegoshi, atlas, or curvature-loss programmes.

## Exact source and stable anchors

1. `docs/sections/plurisubharmonic-functions-and-singularities--analytic-types-and-restriction/index.html`, blob `cff8b3156b07aff2f3d881d83d04608e87b7f2c8`: **Corollary 5.34.3**, source `non-kahler-pluripotential-theory:5103AFE8`, permanent tag `C6F4FBF73B9E`, physical lines **74–87**. Its proof at line **80** imports the bidimensional Lelong monotonicity formula from `DemCADG`, Chapter III, formulas (5.5)–(5.8), pp. 158–159, as a mathematical step. The historical attribution must remain, but an unproved external input here is avoidable.
2. `docs/sections/lelong-densities-generalized-masses-and-multiplicity--lelong-densities-of-positive-currents/index.html`, blob `48bb9c525a826e4d1e337b755fac22aaa3016e66`: **Theorem 6.33.1**, source `demailly-complex-geometry:B0B6D8E5`, permanent tag `7ACCEC6E0526`, lines **25–80**, and annular identity **6.33.2**, source `:2564C820`, permanent tag `F451CA98766C`, lines **31–35**; **Corollary 6.33.5**, source `demailly-complex-geometry:5906DE01`, permanent tag `6FD01B620D33`, lines **82–94**. The section's standing normalization `dd^c=i/(2π)∂∂bar`, `β=dd^c|z|²` and its `p`-plane calibration appear at lines **7–23**. The coefficient-measure domination dependency is permanently tagged `1C212E45A497` (line **16**, recalled at line **93**).
3. **Theorem 6.33.13**, source `demailly-complex-geometry:BA3602B4`, permanent tag `2B9769222A07`, lines **209–240**, is a *different* statement: its Hausdorff bound is for positive-Lelong *level sets*. Do not collapse its meaning or tag into Corollary 5.34.3, which concerns the measure of arbitrary Hausdorff-null Borel sets.

## Exact hypothesis transport and self-contained deduction

Let `X` have complex dimension `n`, let `T` be closed positive of bidegree `(j,j)` with `1≤j<n`, and put `p=n-j≥1`. On a coordinate domain `Ω⊂C^n`, `T` has bidimension `(p,p)`, precisely the quantified class of Theorem 6.33.1. Put
[
eta=dd^c|z|^2,qquad mu=Twedgeeta^p,qquad
D_T(a,r)=r^{-2p}mu(B(a,r)).
]
Theorem 6.33.1 asserts monotonicity for **open** balls, with its half-open-annulus identity and correct left-continuity convention. For any compact inner chart `K⊂Ω` and `0<r_0<dist(K,C^n\setminus Ω)`, Corollary 6.33.5 already states the *uniform-in-center* estimate
[
mu(B(a,r))le C_K r^{2p},quad
C_K=rac{mu(K_{r_0})}{r_0^{2p}},qquad
ain K,quad 0<rle r_0.
]
This is exactly the nontrivial estimate assumed in the printed proof of Corollary 5.34.3.

For completeness, that monotonicity is **proved internally**, rather than merely reasserted: Theorem 6.33.1 first computes, for smooth closed positive `T`,
[
r^{-2p}int_{B(0,r)}Twedgeeta^p
 =int_{partial B(0,r)}Twedge d^clog|z|^2
                  wedge(dd^clog|z|^2)^{p-1}
]
by Stokes and the boundary identities
`d^c|z|²=r²d^c log|z|²`,
`β|_{∂B_r}=r²(dd^c log|z|²)|_{∂B_r}`.
Stokes on an annulus yields
[
D_T(0,r_2)-D_T(0,r_1)
 =int_{{r_1le |z|<r_2}}
       Twedge(dd^clog|z|^2)^pge0.
]
The logarithmic Hessian is semipositive by its explicit orthogonal-projection matrix. For general positive closed currents, §6.33.1 passes through **ordinary local convolution of coefficient distributions** (not a Demailly approximation theorem), weak convergence on spheres of zero trace mass, and approximation of arbitrary radii from below. This correctly preserves the open-ball, left-continuous and half-open-annulus conventions. These steps are present in lines **47–80** and were checked here; no global regularization or curvature-loss theorem is needed.

Now let `E⊂K` be Borel. For a sufficiently fine cover of `E` by sets `A_i` of diameters `d_i<r_0/2`, choose `a_i∈E∩A_i` whenever nonempty. The subset `E∩A_i` lies in `B(a_i,2d_i)` (use arbitrarily small positive radii for zero-diameter members); hence
[
mu(E)le 2^{2p}C_Ksum_i d_i^{2p}.
]
Taking arbitrarily fine diameter-normalized Hausdorff covers proves the slightly **quantitative** consequence
[
oxed{ mu(E)le 2^{2p}C_K,mathcal H^{2p}(E) },qquad Esubset K 	ext{Borel}.
]
The displayed constant is a safe cover constant, not claimed sharp. In particular `H^{2p}(E)=0` implies `μ(E)=0`. The already integrated coefficient-measure domination (tag `1C212E45A497`) gives `|T_{I\bar J}|(E)≤C_{n,j}mu(E)=0` for every coefficient. A countable inner-chart cover finishes Corollary 5.34.3 on `X` with no external proof input.

The proof uses exactly `p=n-j` and the same normalization on both sides. In particular, **no factorial, opposite monotonicity direction, or closed/open-ball substitution** is introduced. The permitted local convolution in §6.33.1 is routine distribution theory, unrelated to the user's excluded regularization programme.

## Disposition and dependent work

- **The printed Corollary 5.34.3 is correct.** The issue is *proof self-containment / reference routing*, not a false mathematical assertion. At its line **80**, propose the internal replacement “By Theorem 6.33.1 and Corollary 6.33.5” instead of invoking `DemCADG` as the necessary proof input. Retain `DemCADG` as **historical attribution** in the bibliography/history; it is not a remaining unproved dependency for this corollary once the internal replacement is explicitly installed.
- This also protects downstream uses of coefficient-current nonconcentration, while not changing canonicalization, source labels, permanent tags, or the distinct Theorem 6.33.13 level-set statement.
- **Verification limits:** inspected Theorem 6.33.1's Stokes, positivity, cutoff/good-radii, and limit passages, Corollary 6.33.5's uniform-center passage, and the Corollary 5.34.3 implication. The full proof graph of positive-current coefficient domination and every theorem in §6.33 was **not** independently recertified. Status is **verified proposed repair**, not applied source modification, no full section certificate.
- Prior `POME-HAUSDORFF-TRACE-EXPONENT-SHARP-001` (sharpness by analytic-plane currents) and `POME-LELONG-LEVEL-SHARP-DIM-001` (large-Lelong-set dimension) are **unchanged and not recounted** as new work. This finding uniquely concerns **replacement of the unnecessary external mathematical input with the already existing integrated proof**.

**Actual new coverage:** new direct *cross-section dependency alignment and quantitative Hausdorff cover proof* in previously sampled §§5.34.3 and 6.33.1/.5. **No new first-covered section and no entirely certified section**. The actual reading-edition ToC remains **25 chapters / 747 numbered sections**. All Demailly approximation/regularization and dedicated Bergman, `L^2`, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion items remain **deferred-by-user**, not resolved or reopened. This report proposes an audit-only patch, without altering production main, text, proofs, permanent tags, registry, site, CI, builds or formalization.
