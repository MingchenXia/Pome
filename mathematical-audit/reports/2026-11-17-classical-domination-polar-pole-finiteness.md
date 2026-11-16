# The pointwise finiteness hypothesis in classical Green domination (2026-11-17)

**Finding ID:** POME-CLASS-DOMINATION-FINITE-POINTWISE-SHARP-001  
**Classification:** low severity; **verified conditional deduction** (sharpness counterexamples to proposed weakenings). **No false printed theorem and no repair of the existing proof are claimed.**  
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Integrated section:** docs/sections/polar-sets-capacity-and-sweeping/index.html  
**Integrated blob:** aa814f26482e8ed27e51c945e9202c797449158b  
**Primary statement:** Theorem 4.3.10, source label classical-potential-theory:FA6C8523, permanent tag C4F5D8B270EB, physical lines 121–130.  
**Related statements read:** Theorem 4.3.2 (lines 8–20), Theorem 4.3.4 (lines 27–38), Theorem 4.3.6 (lines 43–56), Theorem 4.3.9 (lines 100–116). These are contextual checks, not certificates.

## Printed theorem and its hypothesis

Theorem 4.3.10 asserts: on a Greenian open set Ω, if p=G_Ω μ is **finite at every point** and w≥0 is superharmonic with w≥p on supp μ outside a polar subset, then w≥p on all of Ω. The following examples demonstrate that the italicized hypothesis cannot be replaced by either almost-everywhere finiteness or locally integrable/high finite-Lq regularity. They also show why an extended-real comparison at an infinite pole has insufficient content even if no exceptional polar subset is permitted.

## Explicit Green-kernel model, in every dimension d≥2

Take Ω=B(0,1)⊂R^d and μ=δ_0. Write σ_{d−1} for the area of the unit sphere. For the standard normalization −ΔG=δ_0,
\[
p(x)=G_\Omega(x,0)=
\begin{cases}
 \frac{1}{(d-2)\sigma_{d-1}}(|x|^{2-d}-1),&d\ge3,\\[3pt]
 \frac{1}{2\pi}\log(1/|x|),&d=2.
\end{cases}
\]
The function p is positive on Ω\{0}, zero at the sphere in the boundary-limit sense, harmonic away from 0, and p(0)=+\infty. The Riesz measure is exactly the finite compactly supported measure δ_0. The singleton Z={0} is polar: the displayed Green kernel itself is a superharmonic pole function.

1. **Even without permitting an exception.** Choose any fixed 0<η<1 and let w=ηp. This is nonnegative superharmonic. On supp μ={0}, the literal extended-order inequality w(0)≥p(0) reads +∞≥+∞ and holds, with **no excluded point**. Nevertheless w(x)<p(x) for every x≠0 in Ω. Thus removing pointwise finiteness while retaining a comparison at every support point is not a valid domination principle.

2. **Even with a bounded comparison function.** Take w≡0 and use the polar exceptional set Z={0} permitted by the printed formulation. The support comparison is vacuous on supp μ\Z=∅, but w<p at every x≠0. This is the most elementary obstruction to replacing pointwise finiteness by a.e. finiteness in the actual quasi-everywhere formulation.

The Green function is finite Lebesgue-almost everywhere and locally integrable. More sharply, polar coordinates give
\[
p\in L^q(B)\quad\text{for every finite }q\ge1\quad(d=2),
\]
and, for d≥3,
\[
p\in L^q(B)\quad\Longleftrightarrow\quad 1\le q<\frac{d}{d-2}.
\]
At the critical exponent the radial integral is a constant times ∫_0^1 dr/r and diverges. This follows since near zero p(r) is comparable to r^{2-d}, so ∫_0^\epsilon p(r)^q r^{d-1}dr is finite exactly when d−q(d−2)>0; for d=2 use ∫_0^1 r(log(1/r))^qdr<∞. Thus any such finite-Lq assumption, without a genuine pole/support qualification, leaves the counterexample intact.

## Direct proof and dependency review

- **Lines 127–129 (continuous compact-support case):** the printed proof uses p continuous and bounded, so w−p has a lower bound outside supp μ. The exterior argument invokes the polar-exception boundary minimum principle (Theorem 4.3.4) and boundary behavior of compact Green potentials. This selected argument does not apply to δ_0 because p is unbounded at the support and w−p cannot be treated by its boundary comparison there.
- **Line 130 (general measure):** the proof invokes a Lusin/continuous-potential decomposition of restrictions of a finite-everywhere Green potential, then monotone convergence. The source's exact support-continuity lemma and all prerequisites of this decomposition have **not** been independently certified in this session. We do not claim a complete theorem proof.
- Theorem 4.3.2 provides polar pole functions; this example uses the elementary single pole rather than the stronger exact-pole-set construction. Theorem 4.3.9 supplies the related polar-removal interface; the pointwise-finite qualification must be preserved when importing the domination result into further reductions or sweeping proofs.

## Disposition and dependents

**No correction to Theorem 4.3.10 is proposed:** its stated finite-everywhere condition excludes both models. Suggested optional explanatory note, if the main text is later edited through a separate PR: “Finiteness everywhere cannot be weakened to finiteness quasi-everywhere, or to membership in any finite Lq class below the Green singularity threshold; +∞≥+∞ at a polar support point does not give domination.” No edits to the mathematics, source registry, permanent tags, or publication were made here.

Potentially affected **future** deductions are any attempts to generalize Green domination, polar-removal, or sweeping inequalities to potentials with infinite support values; no currently printed dependent theorem was shown false. The earlier user-excluded Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain **deferred-by-user** and were not consulted.

**Actual new proof-level work:** Theorem 4.3.10 support/finiteness hypothesis and its continuous versus general-measure proof division; associated concrete ball/point Green model and sharp integrability range. §4.3 was already partly reviewed: +0 first-visited numbered sections and +0 fully certified sections. No build, test suite, GitHub Actions CI, or website publication was run.
