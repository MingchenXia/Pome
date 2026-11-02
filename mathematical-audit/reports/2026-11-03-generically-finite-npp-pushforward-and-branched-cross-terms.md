# Generically finite maps: degree-weighted non-pluripolar pullback and failure of the birational pushforward product identity

**Date:** 2026-11-03. **Finding:** **POME-NPP-FINITE-DEGREE-PUSH-SECOND-FAIL-001**. **Severity / status:** low / **verified conditional deduction**. **Not a false printed proposition, not an applied repair.**

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Current integrated reading edition:** docs/sections/non-pluripolar-products--fiber-integration-and-modifications/index.html, exact blob **9954a43d90d5cae8ef744968636d7a5912348fce**. **Stable source:** foundations-of-pluripotential-theory:3F4A3A88; **permanent proposition tag:** 0811FFDF15B7 (Proposition 13.6.3, physical lines 36–54). Section permanent tag FBE95DA26374. The printed first and second identities are stated for a **modification**, not for arbitrary finite maps. The proof uses the unique isomorphism sheet outside a proper analytic set (lines 50–54). Corollary 13.6.1, source foundations-of-pluripotential-theory:BAE2819F, permanent BEC54934FC2C (lines 11–30), is only a contextual fiber-formula crosscheck.

## A verified degree extension of the *first*, pullback-pushforward formula

Let f:Y→X be a surjective proper generically finite holomorphic map of **generic degree d** between connected compact Kähler manifolds of the same complex dimension n. For any closed positive (1,1)-currents T_1,...,T_p on X, 1≤p≤n, the natural local-psh pullbacks are well-defined and

\[
\boxed{ f_*\langle f^*T_1\wedge\cdots\wedge f^*T_p\rangle
  =d\,\langle T_1\wedge\cdots\wedge T_p\rangle. }
\]

**Proof.** Choose a proper analytic subset A⊂X containing critical values and the images of exceptional fibers so that f^{-1}(X\setminus A)→X\setminus A is a finite unramified d-sheeted cover. Such an A exists because the proper generically finite map is locally finite over a dense Zariski-open subset; one may equivalently restrict to the locus of finite étale fibers and take its analytic complement. A and f^{-1}(A) are proper analytic, hence pluripolar. No local pullback potential is identically −∞ on an open subset: f is dominant on every open subset of Y, and the pole set of a genuine psh potential cannot contain an open subset of X.

On a sufficiently small coordinate ball disjoint from A, f has d holomorphic inverse sheets. The local Bedford–Taylor truncations (and hence their non-pluripolar limits by plurifine locality) are invariant under biholomorphic coordinate changes. Pushing forward sums exactly d identical local products. Compact Kähler finiteness of the products is supplied by the printed Theorem 13.5.4. Non-pluripolar products give analytic sets zero trace mass. In particular the current upstairs gives f^{-1}(A) zero mass; its pushforward gives A zero mass, by the same smooth-trace-form argument used at line 54 of Proposition 13.6.3. The product downstairs also gives A zero mass. Equality off A therefore extends as equality of positive (p,p)-currents on all X. No limiting interchange through a branch set, and no regularization programme, is involved. □

For d=1 this recovers the **first** identity of Proposition 13.6.3. The degree factor is compulsory; the statement holds for all 1≤p≤n, not just top degree. In top degree it gives the corresponding factor d for the total non-pluripolar masses.

## Failure of the *second* identity for a degree greater than one

The other printed identity,
\[
\pi_*\langle R_1\wedge\cdots\wedge R_p\rangle
 =\langle\pi_*R_1\wedge\cdots\wedge\pi_*R_p\rangle,
\]
cannot be generalized from modifications to finite maps of generic degree d>1. Its proof really requires **one sheet**, not merely that the map is finite away from a branch set: the wedge of sums over sheets has cross-sheet terms.

Take X=Y=ℙ², fix an integer k≥2, and let
\[
f_k([z_0:z_1:z_2])=[z_0^k:z_1^k:z_2^k].
\]
This map is finite of topological degree k². Let ω be the Fubini–Study form in the normalization dd^c=(i/2π)∂\bar∂ and ∫_{ℙ²}ω²=1, and set R_1=R_2=ω. Then
\[
\int_{\mathbb P^2} f_{k*}\langle\omega^2\rangle=1.
\]

There is **no singular-product loophole on the right**. On the affine target chart w_0=1, the k² inverse roots of (w_1,w_2) have moduli |w_j|^{1/k}. Properly pushing forward the standard local Fubini–Study potential gives
\[
 f_{k*}\omega=dd^c\Psi,\qquad
 \Psi(w_1,w_2)=k^2\log(1+|w_1|^{2/k}+|w_2|^{2/k}).
\]
This is a continuous locally bounded psh potential, including across the branch axes. The same holds on all standard projective charts, so its non-pluripolar square is its ordinary bounded Bedford–Taylor square.

If H=[ω]∈H^{1,1}(ℙ²,ℝ), then f_k^*H=kH, since the inverse image of a hyperplane is a degree-k divisor. By the projection formula and ∫H²=1,
\[
 [f_{k*}\omega]\cdot H
 =H\cdot f_k^*H=k,
 \qquad\text{hence }[f_{k*}\omega]=kH.
\]
The bounded-potential cohomological mass identity (printed Proposition 13.5.1, permanent tag **06A36B9354A5**, physical lines 11–26 of docs/sections/non-pluripolar-products--global-finiteness-and-bounded-cohomological-mass/index.html, blob **943517743538820940559eae8469ce98ecf5fcd5**) now yields
\[
\boxed{\int_{\mathbb P^2}
       \langle (f_{k*}\omega)^2\rangle=k^2
       \quad\ne\quad
       \int_{\mathbb P^2}f_{k*}\langle\omega^2\rangle=1.}
\]
At k=2 these masses are exactly 4 and 1. Both sides are well-defined positive measures, so the currents differ. The original **bimeromorphic** proposition is not contradicted.

## Dependency and audit classification

The precise comparison was with Proposition 13.6.3 (the isomorphism-sheet argument, lines 36–54) and the integrated non-pluripolar definitions and plurifine locality in §13.2 (especially Lemma 13.2.2, permanent D59675D9F6D8, and Proposition 13.2.6, permanent 7F7123F92478; docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html, blob **81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c**, lines 35–58 and 81–145). Compact finiteness invokes Theorem 13.5.4 (tag 3783DE0B4D00, lines 85–123; blob **943517743538820940559eae8469ce98ecf5fcd5**). The Stokes/cohomological identity is from Proposition 13.5.1, as anchored above. These are **selected internal inputs**, not a claim of complete transitive verification of the Bedford–Taylor, compact-finiteness, or finite-map existence theories.

**Affected dependents:** any proposed replacement/canonicalization of §13.6.3 that silently weakens “modification / bimeromorphic” to “proper generically finite”; any use of finite-map pushforward as a homomorphism for mixed non-pluripolar products. For pullback-pushforward, replace the coefficient 1 by generic degree d. For general arbitrary upstairs currents, retain the birational hypothesis; the explicit ℙ² countermodel prohibits a universal identity at degree >1.

**Status:** verified conditional deduction (new exact model and degree extension), **not** confirmed original error, not an unresolved original proof gap, and not a code patch. The single-sheet proof in the actual integrated reading edition remains correct. No excluded Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss programme was opened. No compilation, CI, website publication, formalization or project test is asserted.

**Coverage:** one fresh nonexcluded theorem-level extension and independently calculated smooth/continuous-potential branched-cover countermodel in **previously partly reviewed §13.6.3**, with only supporting targeted checks in §§13.2 and 13.5. Not full certification of any of those sections. Current baseline: **25 chapters, 747 numbered sections, zero entire sections mathematically certified**.
