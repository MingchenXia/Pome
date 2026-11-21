# Direct mathematical audit: sparse valuative sampling, relative capacity, rooftops and planar Green kernels

**Date:** 2026-11-21. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit-only target:** review/mathematical-audit.

## Exact integrated reading-edition scope

Entire current mathematical content was read directly (not merely through search excerpts) in these four sections:

1. **§3.8 Planar Green functions and conformal maps:** docs/sections/planar-green-functions-and-conformal-maps/index.html, main blob bfee348bb5f4bbfaa4515e5c9333789a13dae861, physical lines 5–86. Theorem 3.8.1 (source klimek-pluripotential-theory:B1C110E2; permanent E2B11E803D94), Proposition 3.8.2 (source 886FBC1A; permanent 3F05222ECC9E), Example 3.8.3 (source 02455EF4; permanent FADCC209A003). Inspected Green singularity normalization, harmonic conjugate, proper degree-one map, square-root reduction of unbounded simply connected domains, polar boundary exceptions and the example showing that minimality matters.
2. **§16.24 Divisorial constraints under envelopes:** docs/sections/envelopes-and-model-potentials--divisorial-constraints-under-envelopes/index.html, blob 40f522a64d7e846a4507c27e8ac9b4fa382c514c, physical lines 5–60. Proposition 16.24.1 (source foundations-of-pluripotential-theory:73492AFD; permanent 585A4246348B; lines 14–42), Lemma 16.24.2 (source AC593099; permanent FFB5A7083041; lines 45–60). Examined local divisorial valuations, multiplier ideals, pullback of regularized suprema across exceptional analytic loci, and generic Lelong number rules.
3. **§16.25 Singularity constraints and relative capacity:** docs/sections/envelopes-and-model-potentials--singularity-constraints-and-relative-capacity/index.html, blob 4207ba03590b2988456f1df4da4123e1e572c8de, physical lines 5–164. All seven entries 16.25.1–16.25.7, particularly Proposition 16.25.4 (source 944C88B6, permanent C32431185924, lines 76–101), Definition 16.25.5 (source 0AAB93DD, permanent E9BD67F94210, lines 104–110), Proposition 16.25.6 (source 2C3BA6F2, permanent 1587DBB4654F, lines 113–138), Proposition 16.25.7 (source A589E3C1, permanent CDA70099F425, lines 141–164). Checked mixed-mass comparison on plurifine loci, rooftop approximants, relative capacity regularity and full-mass tails.
4. **§16.26 Quantitative rooftop extrapolation:** docs/sections/envelopes-and-model-potentials--quantitative-rooftop-extrapolation/index.html, blob c40b40892fd37beb63802fb6cb253269fb59bd20, physical lines 5–50, Theorem 16.26.1 (source foundations-of-pluripotential-theory:459ECABA; permanent 64513E83F854, lines 11–50). Checked the sign of (1-a) on the obstacle, positive-mass minorant, uniform upper bound on competitors via positive-volume integration, the model-envelope inequality and same-mass equality case.

These are whole direct reviews at the fixed main revision, **not** fully verified transitive dependency chains or necessarily first-ever visits. Previously read §20.6 was considered for breadth but **not** counted as new coverage; its prior non-Q-Cartier quadric obstruction was not reported again. §20.8 contains explicit gentle regularization steps, so this run did **not** reopen or audit those steps.

## POME-MULTIPLIER-IDEALS-SPARSE-COFINAL-SCALES-001

**Severity:** low. **Status:** verified conditional deduction; **not** a false printed theorem or complete upstream-chain certification.

**Precise statement.** Let u,v be quasi-psh functions as in Proposition 16.24.1. Let S be *any unbounded subset of (0,+infinity)*. Then the following condition is equivalent to the three conditions of Proposition 16.24.1:
\[
\mathcal I(tv)\subseteq\mathcal I(tu)\qquad \text{for every }t\in S.
\]
In particular, checking only the dyadic integer scales \(t=2^k,\ k\ge0\), suffices to establish inclusion at **every** positive real scale. Equality of the two ideals along such an unbounded set similarly forces equality at every positive scale and all divisorial Lelong numbers.

**Proof.** Fix any prime divisor E over a sufficiently small open neighborhood of a chosen point. Select t_k in S with t_k tending to infinity. Restrict each ideal inclusion to the local model and take generic orders:
\[
\operatorname{ord}_E\mathcal I(t_kv)\ge
\operatorname{ord}_E\mathcal I(t_ku).
\]
For any quasi-psh w, the asymptotic order formula in Corollary 6.12.14 yields
\[
\lim_{m\to\infty,\;m\in\mathbb N}
\frac{\operatorname{ord}_E\mathcal I(mw)}m=\nu(w,E).
\]
The same limit holds along arbitrary real \(t\to+\infty\). Indeed locally add a bounded constant to arrange w<=0; this does not affect any multiplier ideal. Put m=floor(t). Monotonicity of ideals gives
\[
\mathcal I((m+1)w)\subseteq\mathcal I(tw)\subseteq\mathcal I(mw),
\]
and consequently the corresponding generic orders are squeezed between those at m and m+1. Divide by t and use m/t,(m+1)/t -> 1. Therefore division of the displayed order inequality by t_k and passage to the limit gives \(\nu(v,E)\ge\nu(u,E)\). Since E was arbitrary, the local valuative criterion, Theorem 6.12.16, gives the ideal inclusions for all t>0 exactly as in the proof of Proposition 16.24.1. The converse is immediate. Apply both directions for equality.

**Dependencies and qualification.** This deduction is conditional on the internal *asymptotic multiplier-ideal order* statement 6.12.14 and the *valuative criterion* 6.12.16; these were inspected only through the hypotheses and references of §16.24, not fully audited here. The dyadic criterion is not a finite test and says nothing about a bounded set of scales. Proposed correction: optional corollary after Proposition 16.24.1, leaving the printed theorem, tags and historical attribution intact. Dependents: checking I-equivalence, ordered singularity classes, model-envelope comparison via divisorial valuations.

## POME-RELATIVE-CAPACITY-OSCILLATION-COMPARISON-001

**Severity:** low. **Status:** verified conditional deduction, **not** an error in Proposition 16.25.6.

**Precise statement.** Let φ,ψ be θ-psh, with a common polar set, such that on their common finite locus
\[
m\le\phi-\psi\le M,\qquad -\infty<m\le M<+\infty.
\]
Set \(L=M-m\). For any Borel \(A\subset X\),
\[
\boxed{(1+L)^{-n}\operatorname{Cap}_{\theta,\psi}(A)
\le \operatorname{Cap}_{\theta,\phi}(A)
\le (1+L)^n\operatorname{Cap}_{\theta,\psi}(A).}
\]
Taking m and M to be the infimum and supremum of the finite-locus difference makes the coefficient depend only on its oscillation. In particular, if φ−ψ is constant away from their poles, the two relative capacities agree **exactly**.

**Proof.** Put t=(1+M-m)^{-1}. Given a competitor v in [φ−1,φ] for Cap_{θ,φ}, define
\[
q=(1-t)\psi+tv-tM.
\]
On the finite locus,
\[
q\le\psi+t(M-M)=\psi,\qquad
q\ge\psi+t(m-1-M)=\psi-1.
\]
Both inequalities hold globally in the extended-valued sense (or quasi-everywhere, which suffices), so q is a competitor for Cap_{θ,ψ}. Positivity of mixed non-pluripolar products yields
\[
\operatorname{MA}_\theta(q)
=\langle((1-t)\theta_\psi+t\theta_v)^n\rangle
\ge t^n\operatorname{MA}_\theta(v).
\]
Taking masses on A and the supremum over v gives
\(\operatorname{Cap}_{\theta,\phi}(A)\le t^{-n}\operatorname{Cap}_{\theta,\psi}(A)\).
Swapping φ and ψ exchanges [m,M] with [−M,−m] and preserves L, yielding the other inequality. For L=0 these bounds both equal one; this also matches the existing constant-shift invariance. The estimate is **gauge-invariant**, whereas the symmetric parameter C of the printed bound \((2C+1)^n\) may be much larger than L (e.g. φ=ψ+c).

**Dependencies and qualification.** Uses Definition 16.25.5 and the same mixed-product positivity/total-mass assumptions as Proposition 16.25.6. We do not claim optimality for L>0, nor independent verification of all mixed non-pluripolar products. Proposed correction: optional strengthening next to Proposition 16.25.6, without replacing the valid existing bound or changing canonical statements. Dependents: quantitative equivalence of relative capacities for bounded-difference singularity types and stability of capacity-small sets under constant normalization.

## Other checks, unresolved inputs and exclusions

- **§3.8.1:** the conjugate differential of harmonic H is closed, and simply connectedness supplies a single-valued primitive. The map \((z-a)e^{-H-iK}\) has only a simple zero at a and modulus \(e^{-G}\); properness plus the argument-principle degree count yields a disc biholomorphism. The half-square-root reduction of unbounded D is injective and bounded after the reciprocal translation; the latter does not rely on an already assumed Riemann mapping theorem. The canonical planar boundary regularity, Green existence, polar boundary minimum principle and Myrberg theorem remain upstream inputs **not** independently proved here.
- **§3.8.2–3:** the logarithmic coefficient and 2π Laplacian normalization agree; bounded harmonic puncture-removability yields the finite Robin asymptotic constant. The two positive Poisson terms show why merely polar-exception boundary limits do not imply uniqueness. No new false printed statement identified.
- **§16.24.2:** pullback of the regularized supremum was checked through the biholomorphic locus and its measure-zero complement, rather than assuming pullback of arbitrary Lebesgue null sets through exceptional fibers; infima over point y and family j commute. The generic-Lelong sum rule requires a common generic point and the countable-proper-analytic-exception argument. Not a full upstream verification of 5.10.2 or 6.9.7.
- **§16.25.2–4:** the envelope may leave the original individual singularity type, as the printed proof warns; rooftop truncation and increasing limits were checked with this distinction. The mixed comparison uses mass loss precisely, not an unproved claim of equal mixed mass for arbitrary u,v.
- **§16.25.7:** t≤1 ensures the comparison obstacle remains in the reference singularity class; full mass cancels the defect, and the deep sublevel measures decrease to a µ_u-null pole set.
- **§16.26.1:** with a>1 the negative factor (1−a) reverses the inequality between v and its singularity envelope. The lower bound on η is therefore correctly oriented. The positive-volume set K and the normalized L¹ bound supply an upper bound on **all** competitors; this was not replaced by any unwarranted pointwise boundedness of the obstacle. The equality-case model-envelope argument still depends on the previously proved §16.22 results.
- Remaining not transitively certified: the local valuative criterion §6.12.16 and order formula §6.12.14; Choquet/envelope and exceptional-set lemmas §5.10/§5.47; §13.8 mixed products; §§16.21–16.22 model-envelope/positive-mass statements; and the external canonical planar Green existence/regularity and polar minimum principles in §3.8. These are recorded as **dependencies**, not automatically classified as errors.
- Explicitly excluded **Demailly approximation/regularization and its Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme** remain **deferred-by-user**, neither resolved nor certified. A citation to such an input does not authorize reopening that programme.

**This run's increment:** four entire present integrated sections directly read; two new low-severity conditional deductions; zero newly confirmed source theorem errors; zero full transitive proof-chain certificates. Historical first-visit counts are not inferred from unreconciled legacy records. No tests, builds, CI, website publication, main/source/registry/canonical/tag edits, or PR operations were performed.
