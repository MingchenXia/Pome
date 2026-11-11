# 2026-11-11 — Finite-generation degree bounds for graded ideals over arbitrary complex algebras

**Finding ID:** POME-NA-FG-TAIL-NONNOETHERIAN-SHARPNESS-001  
**Severity:** low. **Status:** verified conditional deduction, concerning a finite-generator uniform bound beyond the printed Noetherian argument (**not** a refutation of the printed lemma).  
**Production main audited:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Integrated reading edition:** `docs/sections/non-archimedean-pluripotential-theory/index.html`, Git blob `8448d710690ebe1cc28040f9611d05c9d008a961`.  
**Original source and permanent tags:** Lemma 22.1.94, `sgpt:AB6FE74C` / `76252E7717AC`, physical line 1403; displayed equation 22.1.95, `sgpt:EC9FB89B` / `6126C03E6587`, lines 1404–1406; proof lines 1410–1414. Proposition 22.1.98, `sgpt:4D7EEB4A` / `6A232EAE791C`, lines 1446–1450; use of the ideal decomposition in its proof, lines 1458–1475, especially equation 22.1.99 (permanent `9186BF0A5F55`, lines 1468–1473). The immediately adjacent Lemma 22.1.96, `sgpt:0D0A3D2C` / `AF0C82DE24E9`, lines 1419–1425, is dependency context only.

## Prior art and genuinely new scope

The printed Lemma 22.1.94 assumes a finitely generated commutative complex algebra `R`, an ideal `I ⊂ R[t]` preserved (by inclusion) by every scalar rotation `t ↦ at`, `a ∈ S¹`, and concludes complex-scaling invariance and the finite coefficient-ideal expansion (22.1.95).

**Historical deduplication (essential):** the **one-infinite-order-rotation criterion and the finite-order root-of-unity counterexample were already proved on 2026-10-30** as `POME-NA-ONE-GENERATOR-GRADING-001` ([earlier proof](2026-10-30-shift-averaging-and-one-rotation-grading.md)). The intrinsic graded filtration and finite tail for Noetherian `R` were also recorded earlier as `POME-NA-GRADED-CANON-001`, `POME-NA-TAIL-GENERIC-FIBER-001` ([2026-10-31 proof](2026-10-31-nonarchimedean-graded-tail-generic-ideal.md)) and `POME-NA-S1-IDEAL-TORSION-FLATNESS-001` ([2026-11-02 proof](2026-11-02-circle-invariant-ideals-flatness-and-torsion.md)). **None of those claims or the reused Vandermonde computation is new in this report.**

**The distinct new increment** is the *effective* stabilization bound in terms of the maximum `t`-degree of any chosen finite generating family, even if the coefficient algebra `R` is non-Noetherian; moreover an explicit graded non-finitely-generated ideal shows the finite-generation boundary is sharp. The result also holds for invariance under any infinite (not necessarily multiplicatively closed) set of scalars, by the same previously known Vandermonde method.

Here is the combined statement, with the previously proved grading part included explicitly as a premise for the new bound:

**Theorem.** Let `R` be *any* commutative complex algebra, not assumed reduced or Noetherian, and `I ⊂ R[t]` any ideal. If there exists a scalar `λ ∈ C*` of infinite multiplicative order with `f(λt) ∈ I` for all `f ∈ I`, then `I` is graded by the `t`-degree, and is invariant under the full `C*`-action. Equivalently, it already suffices that `f(at) ∈ I` for all `f ∈ I` and `a` in **any infinite subset** of `C*`; no subgroup or continuity assumption is needed.

Define coefficient ideals
\[
J_j:=\{r\in R:rt^j\in I\},\qquad j\geq0.
\]
They satisfy `J_j ⊆ J_{j+1}` and give the *exact* graded `R`-module identity
\[
I=\bigoplus_{j\geq0}J_j t^j
\]
(the direct sum contains finite-support polynomials, not infinite series). If `I` is finitely generated as an `R[t]`-ideal, its coefficient chain stabilizes at some finite `D`, even when `R` itself is non-Noetherian. More precisely, if `f_1,\ldots,f_s` generate `I` and `D` is their maximum `t`-degree, then `J_j=J_D` for every `j≥D` and
\[
\boxed{\ I=\left(\bigoplus_{j=0}^{D-1}J_jt^j\right)\ \oplus\ J_D\,t^D R[t].\ }
\tag{*}
\]
The rightmost summand is an **entire tail ideal**, not merely its degree-`D` part. This agrees with the parenthesized final `I_m(t^m)` of the printed (22.1.95). Equivalently, as an `R[t]`-ideal,
\[
I=\sum_{j=0}^{D}(J_jt^j)R[t].
\]
The printed finite-type hypothesis ensures the requisite finite generation by Hilbert's basis theorem; it is unnecessary for the first, grading/invariance, conclusion.

## Proof: known grading step and new effective finite-generator bound

**Recalled, not counted as new:** the following Vandermonde extraction recovers `POME-NA-ONE-GENERATOR-GRADING-001`; it is given for completeness only.**

Take `f(t)=\sum_{j=0}^d c_jt^j∈I`. From the *one-way* inclusion `f(λt)∈I` and iteration, each
\[
f(\lambda^k t)=\sum_{j=0}^d\lambda^{kj}c_jt^j,\qquad0\le k\le d,
\]
lies in `I`. The coefficient matrix `V=(\lambda^{kj})_{0\le k,j\le d}` is Vandermonde in the pairwise distinct scalars `1,\lambda,\ldots,\lambda^d`, since `λ` has infinite multiplicative order. Its determinant
\[
\det V=\prod_{0\le i<j\le d}(\lambda^j-\lambda^i)
\]
is a nonzero complex number, and hence a unit of every complex algebra `R`. Invert the system inside the complex vector space `R[t]`: each `c_jt^j` is a complex-linear combination of the above `f(\lambda^k t)` and therefore belongs to `I`. For an arbitrary infinite set of scalars, instead choose `d+1` distinct elements of that set and apply the same Vandermonde argument. This proves the exact decomposition into homogeneous pieces; arbitrary complex rescaling then preserves each piece.

**New effective step (not dependent on Noetherianity of `R`):** Each `J_j` is an ideal of `R`. Multiplication of `rt^j∈I` by `t` shows `J_j⊆J_{j+1}`. If `f_1,\ldots,f_s` generate `I`, we have just proved that *every homogeneous term* `c_{k,j}t^j` of every `f_k` belongs to `I`. These finitely many homogeneous terms also generate `I`: they contain each `f_k` by summation and themselves lie in `I`. Put `D=\max_k\deg_t f_k` for a nonzero ideal (use `D=0` for the zero ideal). Let `A⊂R` be the ideal generated by the finitely many coefficients `c_{k,j}`. For all `q`, comparison of the coefficients of an arbitrary expression of an element of `I` as `R[t]`-linear combinations of the homogeneous generators gives `J_q⊆A`. Conversely, for each `q≥D`, multiplication of the homogeneous generator `c_{k,j}t^j∈I` by `t^{q-j}` gives `c_{k,j}∈J_q`. Thus `A⊆J_q` for all `q≥D`. Hence `J_q=A=J_D` for these `q`, proving (*).

## Two sharp boundary examples

1. **Previously known (`POME-NA-ONE-GENERATOR-GRADING-001`): an infinite-order rotation cannot be replaced by a finite-order rotation alone.** Fix `q≥1` and a primitive `q`th root of unity `ζ`. In `C[t]`, the proper ideal `I=(t^q-1)` is invariant under `t↦ζt`, but not under arbitrary `t↦at`: for `a^q≠1`, the polynomial `a^qt^q-1` does not vanish at `t=1` and is not in `I`. The ideal is not graded, since neither `t^q` nor `1` belongs to it.

2. **New sharpness check: without finite generation a uniform finite tail can fail over a non-Noetherian coefficient ring.** Set `R=C[x_1,x_2,\ldots]` and `I=(x_jt^j:j≥1)⊂R[t]`. This ideal is already invariant under *all* scalings. Its coefficient ideals are `J_0=0` and `J_q=(x_1,\ldots,x_q)` for `q≥1`, a strictly increasing chain. Thus no finite `D` can make (* ) true. The graded/invariance conclusion survives unchanged.

These examples are exact algebraic counterexamples to **weakened hypotheses**, not counterexamples to Lemma 22.1.94.

## Downstream and editorial assessment

The proof of Proposition 22.1.98 invokes Lemmas 22.1.94 and 22.1.96 in passing to coherent coefficient ideal sheaves in equation 22.1.99. The finite-tail clause is indispensable there, since subsequent constructions take the minimum over finitely many coefficients. The previously established single-rotation theorem, and the present new degree bound, are valid algebraically but do **not** by themselves verify the analytic coherence, GAGA gluing, or global-generation inputs of that proposition. Lemma 22.1.96 relies on GAGA as a genuine external mathematical input; its application was located but not independently certified. No inference about the rest of the non-Archimedean identification theorem is warranted.

**Proposed optional clarification only:** after (22.1.95), spell out that the terminal `I_m(t^m)` is the full tail `I_m t^mR[t]`, or use (*). The one-infinite-order-rotation criterion was already registered on 2026-10-30; the additional arbitrary infinite-scalar-set version is a short variant, not an independent NA proof programme. Do not remove the finite-generation requirement from the finite-tail assertion. Preserve source attribution, both stable tags, the actual printed lemma, and downstream analytic hypotheses.

**Audit coverage:** new direct proof check of §22.1.94 and its use at §22.1.98 (lines 1458–1475); adjacent §22.1.96 reviewed only for dependency classification. §22.1 had prior selected proof-level visits, therefore **0 newly first-visited numbered sections** and **0 whole-section certifications**. Current inventory remains **25 chapters / 747 numbered sections**. No project build/tests/CI/formal verification/publication was performed. No production/source/registry/tag/canonicalization modification is authorized or made. Demailly approximation/regularization and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**, not solved or reviewed.
