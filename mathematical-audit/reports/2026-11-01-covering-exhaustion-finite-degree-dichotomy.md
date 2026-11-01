# 2026-11-01 — finite-degree obstruction to lifting an exhaustion unchanged

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Finding:** `POME-COVER-PULLBACK-PROPERNESS-DICHOTOMY-001` — **low / verified conditional deduction**. The original statements and proofs are not refuted. This is an optional independent clarification of why the extra sheet-sensitive exhaustion in Theorem 9.28.5 is necessary; it is **not** a repair applied to production files. Only existing elementary covering and metric-compactness properties are used.

## Exact integrated evidence and scope

- Main `docs/sections/separation-strict-exhaustions-and-coverings--strictly-plurisubharmonic-exhaustions-on-coverings/index.html`, blob `ef92b5dc5bb4c143345621ea60ca52f3ca7d1872`: §9.28 introductory hypotheses lines 7–11, Lemma 9.28.1 lines 13–27 (source `demailly-complex-geometry:83A0D387`, permanent `9DBBB1BAE0CF`), Proposition 9.28.2 lines 29–45 (source `demailly-complex-geometry:CD2B2989`, permanent `E200BE9CFD9E`), Proposition 9.28.3 lines 47–101 (source `demailly-complex-geometry:09F8EE91`, permanent `7808CCD76C79`), and Theorem 9.28.5 lines 103–142 (source `demailly-complex-geometry:F653208F`, permanent `73159A8CF2BB`). The section permanent tag is `5FA7A48903C4`.
- Main `docs/sections/global-potentials-and-positive-cohomology-classes/index.html`, blob `6f817fc2a3effc4c21e3ec5f7b1bb63f9ba66480`, §10.1, permanent section tag `CFDF01A8B5A7`, line 7: first direct inspection of the global-potential obstruction and its compact-Kähler hypothesis, **introductory only**, not a theorem certification. Lines 10–13 mention other results including the user-excluded approximation/extension programme; none was audited.
- Current §9.25 (`docs/sections/separation-strict-exhaustions-and-coverings/index.html`, blob `89f1c30a6df3c3df624fd05943a5cc64460824b8`, permanent `D10F3B8AA2A1`) and §§16.1–16.2 (`docs/sections/the-envelope-operators/index.html`, blob `1751b26b427c36506d7ed35ca6f52aefc56f8b04`, tag `2AC9E2799656`; `docs/sections/the-envelope-operators--p-envelopes/index.html`, blob `912f81b3bccf3e1ead96fd18005261a708dfcb4e`, tag `A6FA63C034E6`) were read for orientation only: these pages have no independent numbered proof.

## The finite-degree dichotomy (complete elementary proof)

Let `p:Y -> X` be a surjective covering map between connected Hausdorff, second-countable manifolds (no holomorphic or metric hypothesis is necessary for this step). Let `f:X -> R` be **finite continuous with compact closed sublevels**, i.e. an exhaustion in the convention of §9.26. Then

`f ∘ p` is an exhaustion on `Y` **if and only if** the covering has finite degree.

**Finite degree.** Each point of a compact `K subset X` has an evenly covered neighborhood `U` and a smaller neighborhood with compact closure in `U`. Finitely many of these smaller neighborhoods cover `K`. Over the corresponding compact closures, the inverse image is a finite union of compact lifts, one on each sheet, because the degree is finite. Thus `p^{-1}(K)` is closed in a finite union of such compact sets, and hence compact. In particular, `p^{-1}({f<=c})` is compact for each real `c`, as claimed.

**Infinite degree.** Fix `x_0 in X`. The fiber `p^{-1}(x_0)` is an **infinite closed discrete** subspace of `Y`: it is closed by Hausdorffness of `X`, and discreteness follows from the covering charts. It is not compact, since the open cover of this subspace by singleton sets admits no finite subcover. All its points have `f∘p=f(x_0)`. Therefore the closed sublevel `{f∘p<=f(x_0)}` contains this noncompact closed subspace and cannot be compact.

This proves both implications. Moreover, if the covering is infinite-sheeted and `b:Y -> R` is any continuous function **bounded above on one complete fiber**, then `f∘p+b` is not an exhaustion: that fiber is still contained in one finite closed sublevel. In particular **no globally bounded perturbation of a pulled-back exhaustion can restore properness**. Conversely, every actual finite continuous exhaustion on `Y` must tend to `+infinity` along any sequence of pairwise distinct points of any fixed infinite covering fiber, because each compact sublevel meets the closed discrete fiber in only finitely many points. This is the precise sheetwise growth requirement.

The argument does not assert an obstruction to a non-invariant exhaustion on `Y`: Proposition 9.28.3 explicitly constructs a smooth `delta` at bounded distance from the **proper lifted metric distance**, not from `f∘p`, and Theorem 9.28.5 adds it to a convexly reweighted pullback.

## Explicit holomorphic model and Levi check

Take `X=C^*`, `Y=C`, and `p(w)=exp(w)`, with `w=x+iy`. Set

`f(z)=|z|^2+|z|^{-2}`.

This is a smooth strictly plurisubharmonic exhaustion on `C^*`: its complex Hessian coefficient is `partial_z partial_bar_z f = 1+|z|^{-4}>0`; its closed sublevels bound the modulus above and away from zero. The pullback is

`f(exp w)=exp(2x)+exp(-2x)=2 cosh(2x)`.

Its coefficient `partial_w partial_bar_w(f∘p)=exp(2x)+exp(-2x)>0`, so it remains **strictly** plurisubharmonic, but is not an exhaustion because it is independent of `y`. This separates the failure of properness from any loss of strict Levi positivity.

For any `epsilon>0`, `F_epsilon(w)=2 cosh(2 Re w)+epsilon |w|^2` is smooth, strictly plurisubharmonic, and proper. Indeed both summands are subharmonic and the second has strictly positive complex Hessian; `F_epsilon>=epsilon|w|^2` makes all closed sublevels compact. This is an explicit sheet-sensitive correction and is compatible with, but does not replace, the general Theorem 9.28.5 construction. On the finite-degree cover `p_d(z)=z^d:C^* -> C^*`, in contrast, `f∘p_d=|z|^{2d}+|z|^{-2d}` is already a strict-PSH exhaustion. Hence the dichotomy is sharp.

## Independent global-current normalization crosscheck (no new finding ID)

For the introduction to §10.1, the obstruction to a global potential can also be seen directly without the maximum principle: on a positive-dimensional **compact Kähler** `(X,omega)`, if a positive closed real `(1,1)`-current `T` has `T=dd^c u` globally for a distribution `u`, then

`int_X T wedge omega^{n-1} = <u,dd^c omega^{n-1}> = 0`

by distributional Stokes and `d omega=0`. A positive current with zero total trace mass relative to a Kähler form is zero. This is a local verification of the stated cohomological obstruction, not a proof of the general `dd^c`-lemma or of any referenced approximation machinery. The compactness and closed-Kähler hypotheses cannot be silently dropped; on `C`, for example, `dd^c|z|^2` is nonzero positive and globally exact.

## Status, proposed action, dependents, coverage boundary

- **Status:** `POME-COVER-PULLBACK-PROPERNESS-DICHOTOMY-001` — **low / verified conditional deduction**, not a false theorem, proof gap, duplication, or production repair. The precise finite/infinite-cover statement and bounded-correction obstruction are proved above. Optional addition: a short remark after Proposition 9.28.3 or before Theorem 9.28.5, retaining all current permanent tags and source attribution.
- **Affected interpretation:** Proposition 9.28.2 (proper lifted metric distance), Proposition 9.28.3 (sheetwise unbounded smooth exhaustion), Theorem 9.28.5 (need for the additive covering-distance term), plus the defining exhaustion convention of §9.26. None of these original results is contradicted. No claim of certification of the full metric smooth-approximation lemma or downstream Stein/jet interpolation.
- **Actual new work:** the topological if-and-only-if, fiberwise bounded-perturbation obstruction, explicit logarithmic-cover example with checked Levi coefficients, and §10.1 Stokes/mass normalization. The §9.28 section was previously partially sampled; it is **not** first covered or fully certified. §10.1 is first inspected directly for its compact-Kähler potential paragraph, but this is an introduction, not a complete proof review. §§9.25, 16.1, 16.2 were structural/contextual rechecks only.
- **All other historical entries unchanged.** The user-excluded Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**, not resolved and not reopened. No source, proof registry, canonicalization, tags, main, site, CI, formalization, test suite, or publication changes. **Current collection: 25 chapters, 747 numbered ToC sections, zero complete mathematical-section certifications.**
