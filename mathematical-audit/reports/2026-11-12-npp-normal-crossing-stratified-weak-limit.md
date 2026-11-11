# Stratified weak limits of smooth projective normal-crossing Monge–Ampère products

**Date:** 2026-11-12. **Finding:** `POME-NPP-SNC-STRATIFIED-MASS-DEFECT-001`. **Severity:** low. **Status:** verified conditional deduction; **not** a false theorem, a proof gap, or a repair. No source/body amendment is proposed.

**Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (not the review-branch SHA). **Integrated source:** `docs/sections/non-pluripolar-products--capacity-convergence-and-loss-of-mass/index.html`, blob `d66813856cb813722806ab912afdfd4815d2da97`. Theorem 13.7.5, source `foundations-of-pluripotential-theory:AB4EBE3B`, permanent `67C4F7EC316E`, physical lines 106–135; Example 13.7.6, source `foundations-of-pluripotential-theory:D5678E03`, permanent `ACAEA8D8BE87`, lines 138–143. Also read: `docs/sections/non-pluripolar-products--global-finiteness-and-bounded-cohomological-mass/index.html`, blob `943517743538820940559eae8469ce98ecf5fcd5`, Proposition 13.5.1 source `foundations-of-pluripotential-theory:4EE18BE1`, permanent `06A36B9354A5`, physical lines 10–39; and `docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html`, blob `81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c`, Definition 13.2.4 source `foundations-of-pluripotential-theory:9D8E4DD8`, permanent `D79952D7E272`, lines 57–66. Normalization is `dd^c=i/(2π)∂∂̄`, with `∫_{P^n}ω_FS^n=1`.

## Precise theorem and proof

Fix an integer `n≥2` and `X=P^n`. Let `[Z_0:…:Z_n]` be homogeneous coordinates, `H_i={Z_i=0}` for `1≤i≤n`, and `0≤λ_i≤1`. Write `N(Z)=Σ_{j=0}^n|Z_j|²` and `ω=dd^c log N` (with the usual homogeneous local interpretation). The singular `ω`-psh functions and their smooth decreasing approximations are

```text
u_i        = λ_i log(|Z_i|²/N),
u_i,eps    = λ_i log((|Z_i|² + eps N)/N),       eps>0,
T_i        = ω + dd^c u_i = (1-λ_i)ω + λ_i[H_i],
T_i,eps    = ω + dd^c u_i,eps
           = (1-λ_i)ω + λ_i A_i,eps,
A_i,eps    = dd^c log(|Z_i|² + eps N).
```

Here `A_i,eps` is the Fubini–Study form associated with the positive-definite Hermitian quadratic form `|Z_i|²+eps N`; in particular it is smooth, positive, closed and cohomologous to `ω`. The section `Z_i` and the normalized Poincaré–Lelong identity give the displayed formula for `T_i`. The functions `u_i,eps` decrease pointwise to `u_i`, including their poles. Thus the *smooth* top products `μ_eps=∧_{i=1}^n T_i,eps` are probability measures by cohomology and Stokes.

For `S⊂{1,…,n}`, put `H_S=∩_{i∈S}H_i ≅ P^{n-|S|}` (with `H_empty=X`) and let `ν_S` be its normalized Fubini–Study probability measure: `ν_S=[H_S]∧ω^{n-|S|}`, including `ν_empty=ω^n` and `ν_{all}=δ_[1:0:…:0]`. Define `c_S=∏_{i∈S}λ_i∏_{i∉S}(1-λ_i)`. Then the **entire weak limit**, not merely its total mass, is

```text
μ_eps   -->   Σ_{S⊂{1,…,n}} c_S ν_S      weakly as eps↓0.
```

In contrast, the **singular non-pluripolar product** is precisely

```text
⟨T_1∧…∧T_n⟩ = (∏_{i=1}^n(1-λ_i)) ω^n,
mass = ∏_{i=1}^n(1-λ_i).
```

Hence the singular non-pluripolar product is the `S=empty` stratum of the classical smooth weak limit; the **positive, stratified lost-mass measure** is `Σ_{S≠empty}c_Sν_S`. Its total mass is `1-∏_i(1-λ_i)`. Whenever at least one `λ_i>0`, the full product masses do **not** converge to the non-pluripolar mass, exactly the extra hypothesis of Theorem 13.7.5.

**Proof of the weak limit without interchange of singular wedge limits.** For each fixed `S`, form the smooth positive probability measure

```text
ν_S,eps = (∧_{i∈S} A_i,eps) ∧ ω^{n-|S|}.
```

Its total mass is one by `[A_i,eps]=[ω]`. Fix `i∈S` and a compact `K⊂X\H_i`. In a local trivialization `dd^c log|Z_i|²=0` on `K`, so `A_i,eps→0` in `C^∞(K)`; consequently `0≤A_i,eps≤δ_K(eps)ω` there, where `δ_K(eps)→0`. The other positive factors have total cohomological mass one, giving `ν_S,eps(K)≤δ_K(eps)`. It follows that **every** weak subsequential limit is supported on all the hyperplanes `H_i` with `i∈S`, hence on `H_S`; no claim of simultaneous continuity of singular current wedges was made. For every `eps>0`, `ν_S,eps` is invariant under `U(n+1-|S|)` acting on the homogeneous coordinates *not* indexed by `S`, because the quadratic forms defining all its factors and `ω` are invariant. On the projective space `H_S` this group acts transitively, so there is exactly one invariant probability measure: `ν_S=[H_S]∧ω^{n-|S|}`. Any weak subsequential limit must therefore be `ν_S`. Compactness of probability measures on the compact metrizable `X` proves weak convergence of the entire family as `eps↓0`. Expanding the **smooth** wedge `∧_i[(1-λ_i)ω+λ_iA_i,eps]` into finitely many terms yields the claimed formula.

For the non-pluripolar product, on `X\∪_{λ_i>0}H_i` each `[H_i]` vanishes, so the usual bounded-potential product is the smooth measure `∏_i(1-λ_i)ω^n`. The product defined by truncation has zero mass on the pluripolar union and therefore is its extension by zero. Since `ω^n` gives no mass to a hypersurface, the global formula follows. This uses only the stated non-pluripolar locality/zero-polar-mass convention (13.2.4), not a hypothetical singular continuity theorem. The group-invariance uniqueness and cohomological total masses also show why no unaccounted or signed mass can appear.

**Exact example (n=2).** With `λ_1=λ_2=1/2`, the weak smooth Monge–Ampère limit is

```text
(1/4)ω² + (1/4)[H_1]∧ω + (1/4)[H_2]∧ω
        + (1/4)δ_[1:0:0],
```

while `⟨T_1∧T_2⟩=(1/4)ω²`. The defect `3/4` consists of masses `1/4,1/4,1/4` on two distinct hyperplanes and their point intersection. Choosing all `λ_i=1` recovers the earlier unit classical normal-crossing intersection mass, but does not reproduce these intermediate-stratum coefficients.

## Audit classification, prior-work separation and dependents

- **Status/severity:** `POME-NPP-SNC-STRATIFIED-MASS-DEFECT-001`, **low / verified conditional deduction**. No printed Theorem 13.7.5, Corollary 13.7.9 or Example 13.7.6 is refuted. The proof is self-contained modulo the already displayed projective/positive-current, Poincaré–Lelong and NPP-locality conventions; these upstream theories are **not** certified wholesale.
- **Prior results preserved:** Example 13.7.6 has a one-point complete loss on `P^1`; the 2026-11-07 `POME-NPP-PROJECTIVE-DIVISOR-PARTIAL-DEFECT-001` already computed a **single** hyperplane and its `(1-λ)^n` top mass and weak limit; the earlier `POME-BT-HAUSDORFF-SUBFAMILY-SHARP-001` checked the **all-λ=1 classical complete-intersection endpoint**. This increment computes a **distinct divisor for each factor, all `2^n` transverse-intersection strata and their exact weights**, beyond either old case. No old result is refiled.
- **Affected dependents:** mass-conservation hypotheses in §13.7.5/13.7.9, and any later argument asserting weak continuity of non-pluripolar products merely from extended-capacity convergence. The model confirms the stated mass hypothesis cannot be omitted; it establishes no general convergence theorem.
- **Proposed action:** optional expository example illustrating normal-crossing stratified mass defects; **no source-body, registry, tag or canonicalization edit**. Do not make an additive example into a purported missing proof.
- **Actual coverage:** selected §13.7.5/.6 and definitional crosschecks §§13.2.4, 13.5.1. All were previously partly reviewed: **+0 first proof-level section visits; +0 full mathematical section certifications**. Actual current production ToC: **25 chapters / 747 numbered sections**. No Demailly approximation/regularization, Bergman, `L²`, Ohsawa–Takegoshi, multiscale or positivity-loss proof programme; that work remains **deferred-by-user**, neither resolved nor verified. No build, CI, site or formalization claimed.
