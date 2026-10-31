# Non-Archimedean graded ideals: the stabilized coefficient is exactly the generic-fiber ideal

**Date:** 2026-10-31. **Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Status:** `low / verified conditional deduction`, **not** a false theorem, not a complete verification of the non-Archimedean correspondence, and not an integrated source repair.

**Stable finding ID:** `POME-NA-TAIL-GENERIC-FIBER-001`.

## Exact integrated source and dependency boundaries

- `docs/sections/non-archimedean-pluripotential-theory/index.html` on the reviewed `main`, Git blob `8448d710690ebe1cc28040f9611d05c9d008a961`.
- Lemma **22.1.94**, original `sgpt:AB6FE74C`, permanent tag `76252E7717AC`, physical lines **1402–1416**. Its homogeneous ideal expansion is Equation **22.1.95**, `sgpt:EC9FB89B`, permanent tag `6126C03E6587`, lines **1404–1406**.
- Lemma **22.1.96**, original `sgpt:0D0A3D2C`, permanent tag `AF0C82DE24E9`, lines **1418–1427**, glues a coherent analytic ideal on `X × A¹` to `X × P¹` and invokes GAGA. **GAGA is retained as an unresolved genuine external input; this report does not prove it.**
- Proposition **22.1.98**, original `sgpt:4D7EEB4A`, permanent tag `6A232EAE791C`, lines **1445–1494**; its punctured-product identity appears at lines **1458–1464**, and its coefficient expansion is Equation **22.1.99**, `sgpt:B0939F32`, permanent tag `9186BF0A5F55`, lines **1466–1473**. Compare the footnote at line **1494**.
- The valuation convention is Equation **22.1.69**, `sgpt:8A8BEA89`, permanent tag `3B8E87503101`, lines **1164–1171**: `σ(v)(∑ f_j t^j) = min_j(v(f_j)+j)`.

This report inspects the actual integrated statements and proofs. Its new assertion is **not** the previously logged unique filtration `POME-NA-GRADED-CANON-001` or the weaker one-generator invariance criterion `POME-NA-ONE-GENERATOR-GRADING-001`. Those concern homogeneity and uniqueness; the new result **identifies the eventual coefficient with the prescribed punctured-fiber ideal** and determines the precise valuation-theoretic consequence used by §22.1.98.

## Statement and elementary proof (after the stated algebraization input)

Let `X` be a projective complex variety, let `J ⊂ O_X` be a coherent ideal, and let `I ⊂ O_{X×A¹}` be a coherent **algebraic**, `C* `-homogeneous ideal whose restriction to `X×C*` equals `p_X^*J`. For each `j≥0` define its intrinsic coefficient ideal sheaf by

```text
J_j(U) = { f in O_X(U) : f t^j is in I(U × A¹) }
```

(on affine open `U`; these ideals glue). Then

1. `J_0 ⊆ J_1 ⊆ ···` and there is a **single integer N** such that `J_j = J_N = J` for all `j≥N`;
2. the polynomial ideal has the **canonical**, non-ambiguous form
   `I = J_0 + J_1 t + ··· + J_{N−1}t^{N−1} + J(t^N)`;
3. for every valuation `v` centered on `X`, with Gauss extension normalized by `σ(v)(t)=1`,
   `σ(v)(I) = min_{0≤j≤N}{v(J_j)+j}`. In particular, the terminal term is **`v(J)+N`**, not `N` unless `J=O_X`.

**Proof.** Work on an affine chart `U=Spec R`. Since `I` is a homogeneous ideal of the noetherian ring `R[t]`, take a finite list of homogeneous generators `f_α t^{d_α}`. We may assume `f_α∈R` and `d_α≥0`. The degree-`j` coefficient is precisely

```text
J_j(U) = ( f_α : d_α ≤ j ) ⊂ R.
```

This formula immediately gives monotonicity. For `j≥N_U:=max_α d_α`, the coefficient stabilizes at `(f_α)_α`. On inverting `t`, every `t^{d_α}` is a unit, so `I[t^{−1}]=(f_α)_α R[t,t^{−1}]`. The stipulated identity on `U×C*` therefore identifies `(f_α)_α` **with `J(U)`**. Projectivity (indeed quasi-compactness) gives a finite affine cover and a common integer `N=max_U N_U`, proving the sheaf identity globally. The canonical finite expansion follows by collecting the homogeneous pieces. The Gauss formula is the minimum of the valuations of the homogeneous generators, equivalently of the finitely many coefficient ideals `J_j t^j`; for `j>N`, `v(J)+j≥v(J)+N`, so the infinite tail contributes only its first index. No sequential compactness, analytic limiting interchange, or L² argument is used. QED.

An even shorter way to identify the stabilized ideal, **once homogeneous stabilization is known**, is to restrict the homogeneous expansion to the fiber `t=1`: then `I|_{t=1}=J_N`, while the punctured-product hypothesis gives `I|_{t=1}=J`. The affine-generation proof above also explains why stabilization is uniform on a finite cover.

For the **analytic** `S¹`-invariant ideal appearing in Proposition 22.1.98, this statement is conditional on the already printed Lemmas 22.1.94 and 22.1.96: first invoke algebraization (GAGA), then decompose the invariant ideal algebraically into homogeneous pieces. The new argument starts **after** that external algebraization premise and does not certify it.

## Exact sharp model; the terminal ideal need not be the unit ideal

Take `X=P¹`, a point `p∈X`, `J=I_p`, and integers `a>b≥1`, `k≥1`. Consider the algebraic `S¹`-invariant ideal on `X×A¹`

```text
I = p_X^*(J^a) + t^k p_X^*(J^b).
```

Its punctured restriction is `p_X^*(J^b)` because `t` becomes invertible and `J^a ⊂ J^b`. The actual coefficient ideals are `J_j=J^a` for `0≤j<k` and `J_j=J^b` for `j≥k`; hence `N=k` and the terminal ideal is the **proper** ideal `J^b`. For `v_c=c ord_p` with rational `c>0` (a divisorial valuation),

```text
σ(v_c)(I) = min{ a c, b c + k }.
```

The slope changes exactly at `c=k/(a−b)`. In the minimal instance `a=2,b=k=1`, `σ(v_c)(I)=min{2c,c+1}`; at `c=3`, this is `4`. Replacing the terminal ideal by `O_X` would incorrectly produce `min{6,1}=1`. Thus the final coefficient in Equation 22.1.99 is not an ignorable decoration, and the footnote at physical line 1494 is mathematically essential. These are examples of **graded ideals**, not claimed to arise as multiplier ideals of a particular geodesic ray.

## Disposition and precisely affected downstream reasoning

**Proposed optional, separately reviewable insertion** immediately after Equation 22.1.99: “More precisely, the eventual coefficient ideal `a_N` equals the ideal `I(mφ)` on the punctured product, since restricting the homogeneous expansion to the fiber `t=1` gives `a_N`. In particular `a_N` need not be the unit ideal.” This is an explanatory refinement of a **correct** printed statement, not a theorem correction.

The identification clarifies the Gauss valuation minimum at lines 1479–1489, and the terminal nonsmooth singularity contribution in the downstream analytification Proposition 22.1.98 and Corollary 22.1.100. It **does not** prove Lemma 22.1.97 (which relies on an external family vanishing/global-generation result), the GAGA step of Lemma 22.1.96, the convergence in §22.1.98, or the Boucksom–Jonsson correspondence §22.1.111. These retain their earlier external/conditional statuses. The user's exclusion of Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programme is respected: **none was re-examined**. Hironaka remains the only generally permitted unproved resolution input; this report explicitly flags the other outside input rather than silently treating it as proved.

**Actual new coverage:** complete elementary graded-ideal coefficient/fiber proof under the stated algebraization hypothesis; selected direct review of §§22.1.94, 22.1.96, 22.1.98 and Eqs. 22.1.69, 22.1.95, 22.1.99; §22.1.97 **statement only as unresolved boundary**, no L² proof reading; §22.1.100 dependency only. No entire mathematical section, chapter, external theorem, project build, tests, CI, publication, or formal proof certification. The project inventory remains **25 chapters and 747 distinct numbered ToC sections, with zero fully certified mathematical sections**. Production `main`, source text, registries, original references and permanent tags remain unchanged.
