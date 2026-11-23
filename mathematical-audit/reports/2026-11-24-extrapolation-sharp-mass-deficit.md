# Sharp non-pluripolar mass deficit under envelope extrapolation

Date: 2026-11-24. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Finding **POME-EXTRAPOLATION-SHARP-POINT-POLE-MASS-001**, low / verified conditional deduction; not a false printed theorem.

## 1. Exact anchors and hypotheses

The integrated reading edition, not a source-number match, was inspected:
- docs/sections/envelopes-and-model-potentials--extrapolation-and-model-singularities/index.html, blob 17191d65c793e508c1785dd617ddb1dbc5f5d213, entire mathematical lines 7–312. Theorem 16.22.4 (foundations-of-pluripotential-theory:37CAA8E0, permanent FCFA7EB59B34), lines 98–169; Lemma 16.22.3 (D373FCA8, B36FB6000F3B), lines 62–93; the key tail estimate (16.22.8), lines 139–146.
- docs/sections/non-pluripolar-products--capacity-convergence-and-loss-of-mass/index.html, blob d66813856cb813722806ab912afdfd4815d2da97, selected Corollary 13.7.9 (foundations-of-pluripotential-theory:82DB3E57, permanent D73416504271), lines 176–209; Lemma 13.7.3 and local truncation context. This is a repeat dependency check, not new whole-section coverage.

Let X be a connected compact Kähler n-fold, n>=1, with big smooth closed real (1,1)-form theta. Write M(q) for the non-pluripolar top mass of a theta-psh potential q. Suppose u≼v, 0<M(u)<=M(v)=m, a>1, and a^n(m-M(u))<m. The printed theorem gives the existence and positive mass of E_a=P_theta(au+(1-a)v), with the stated convention at poles. The proof below strengthens its quantitative conclusion to

    m - a^n (m-M(u)) <= M(E_a) <= M(u).

The coefficient a^n is sharp in every complex dimension, even in the Fubini–Study Kähler class on projective space. In particular, the strict threshold cannot be weakened universally to a non-strict one if positive mass is required. The older 2026-11-04 divisorial example (POME-ROOF-EXTRAPOLATION-DIVISOR-THRESHOLD-001) shows that the criterion need not be necessary for particular divisorial data in n>=2; the point-pole family below instead attains the universal bound for every n. These statements are compatible.

## 2. Proof of the quantitative bound

Translation of u and v by constants changes E_a by a constant (the affine shift from lines 113–116), without changing any masses. Assume u<=v<=0. Use the model majorant phi>=v with M(phi)=m from Lemma 16.22.1. In the notation of the printed proof, put u_j=max(u,phi-j), eta_j=P_theta(a u_j+(1-a)phi). The eta_j decrease, have the singularity type of phi and mass m, and satisfy eta_j<=phi. The noncollapse argument at lines 139–146 applies under the strict threshold, independently of the later positive-mass paragraph. Thus eta_j decreases to a theta-psh eta and eta<=E_a(u,v), by lines 146–148. Do not assume M(eta_j) tends to M(eta): that is precisely the possible mass loss.

For an integer k>=1 and j>k, (16.22.8) gives

    mu_eta_j({eta_j <= phi-ak}) <= a^n (m - mu_u({u>phi-k})).

Here mu_q is the non-pluripolar top measure. We now prove that no greater loss occurs on passing to the limit. Fix k and define
    tau_j=max(eta_j,phi-a(k+1)),    tau=max(eta,phi-a(k+1)).
These are theta-psh, all have the singularity type of phi and mass m, and tau_j decreases to tau. Set R(s)=max(0,min(1,s/a)). On the finite locus of phi define
    chi_j=R(eta_j-phi+a(k+1)),     chi=R(eta-phi+a(k+1)),
using R(-infinity)=0; define both weights to be zero on the poles of phi. The weights are Borel and in [0,1]. They are quasi-continuous: locally remove small-capacity neighborhoods of the poles of eta and phi and the sets of failure of continuity of those potentials (and, for each fixed chi_j, of eta_j), by Lemmas 16.11.1–2. On the remaining compact set the differences are continuous real functions. This also proves local capacity convergence chi_j→chi. More explicitly, on that compact remainder eta and phi are finite continuous and bounded; eta<=eta_j<=phi, so all eta_j are bounded there with the same constants. Extended capacity convergence eta_j→eta from Lemma 13.7.3 gives ordinary capacity convergence there by the uniform Lipschitz bound for the inverse of arctan on the common bounded range. R is Lipschitz; the exceptional open sets have arbitrarily small capacity. This establishes the local outer-capacity convergence required in Corollary 13.7.9, with no assumption about global uniform integrability of the untruncated measures.

On the support in the measure-theoretic sense of the nonzero weight chi_j, i.e. the set {chi_j>0}, we have eta_j>phi-a(k+1), so plurifine locality gives chi_j mu_tau_j=chi_j mu_eta_j. All pole sets can be ignored because these products are non-pluripolar. Also chi_j=1 on {eta_j>phi-ak} outside the poles. Hence

    integral chi_j dmu_tau_j >= m - a^n (m - mu_u({u>phi-k})).

Apply Corollary 13.7.9 to tau_j→tau and these weights. Its mass-equality hypothesis is satisfied exactly, for the truncated potentials only. Thus the integrals converge to integral chi dmu_tau. By the same plurifine locality on {chi>0}, this equals integral chi dmu_eta, at most M(eta). Consequently

    M(eta) >= m-a^n(m-mu_u({u>phi-k}))

for every k. Let k increase to infinity after this fixed-k limit; the sets exhaust the finite locus relevant to mu_u, since u<=phi and mu_u ignores poles. Hence M(eta)>=m-a^n(m-M(u)). Monotonicity and eta<=E_a<=u (the last inequality follows from the normalized obstacle) give both bounds. If M(u)=m, equality follows immediately. This strengthens the printed lines 150–168 without assuming mass continuity for the untruncated decreasing sequence, without interchanging the two limits, and without regularization.

## 3. Sharpness: isolated projective point, every n

Let theta be probability-normalized Fubini–Study on P^n, integral theta^n=1. In homogeneous coordinates set
    g([Z_0:...:Z_n])=log((sum_{i=1}^n |Z_i|^2)/(sum_{i=0}^n |Z_i|^2)).
It is smooth outside p=[1:0:...:0], has logarithmic pole at p, and is theta-psh (the local sum-of-squares logarithm plus the smooth background potential is psh). Take v=0 and u=cg for 0<c<1. Then u<=v and u is theta-psh by convexity. For any a>1 with ac<=1, au=acg is itself theta-psh and therefore equals its obstacle envelope. This last identification uses the everywhere-upper-bound property for usc obstacles in Proposition 16.11.4.

For any d in (0,1], the affine chart Z_0=1 has theta+dd^c(dg)=dd^c F_d(t), t=log|z|^2, where
    F_d(t)=(1-d)log(1+exp(t))+dt.
The slope tends to d at -infinity and 1 at +infinity. On each finite annulus the smooth radial Stokes identity gives the integral of (dd^c F_d)^n as the difference of the nth powers of its boundary slopes. Indeed on a sphere the restriction of d^c F_d wedge (dd^c F_d)^(n-1) is (F_d')^n times d^c t wedge (dd^c t)^(n-1); the sphere integral of this last expression is constant in radius and equals 1 by applying the same identity to F_0=log(1+exp(t)), whose Fubini–Study total mass is 1. This uses the given dd^c convention and no factorial change. The hyperplane Z_0=0 is smooth for dg and has zero measure, and the pole p is discarded by the non-pluripolar product. Thus M(dg)=1-d^n, including d=1, when the radial top measure is zero off p.

It follows that M(v)=1, M(u)=1-c^n, and M(E_a)=1-(ac)^n for ac<1. The lower bound is an equality, for every a>1 and every 0<c<1/a. At ac=1 the obstacle is still a potential but its mass is zero, while M(u)>0; the printed strict hypothesis exactly becomes equality. This is not a counterexample to the printed theorem, but an obstruction to a universal strengthening allowing equality and retaining positive mass. No assertion about arbitrary point-pole models or all individual extrapolation thresholds is made.

## 4. Other direct review and remaining dependencies

- Section 16.11, docs/sections/envelopes-and-model-potentials--obstacles-and-rooftops/index.html, blob e9129aaaab9e9f172da9704bffe939839f8afeb6, mathematical lines 7–176, whole direct. The countable Choquet subfamily, pluripolar exceptional union, usc obstacle pointwise bound, constant shifts, decreasing obstacle limits (including empty competitors), associativity as greatest common minorant, and the P^1 two-pole example were checked. No new source error established. Dependencies: local capacity chart comparison, quasi-continuity, Choquet lemma, submean inequality, Lelong atom normalization.
- Section 16.22 whole direct, including maximal model construction via increasing approximate maximizers, the contact measure bound, normalization, noncollapse, domination by countably many extrapolation obstacles, model characterization, zero Lelong/full-mass example, and relative singularity-envelope proof. No new source error established. Dependencies include increasing non-pluripolar mass continuity (13.8.9), mass monotonicity, contact domination/concentration (16.13.1/4/5), and 16.21.2/3. These are not transitive certifications.
- Section 16.27, docs/sections/envelopes-and-model-potentials--comparison-of-relative-capacities/index.html, blob 1c209671c3de0740018b2aaad7aa321f5647313d, selected nonexcluded mathematical lines 7–13, 35–61, 64–343. Lemma 16.27.1 (source 2E285F1C, permanent 49691FF58A24) and the bounded-test passage using it at line 62 are explicitly deferred-by-user insofar as they invoke Demailly regularization 6.17.7. No attempt to certify or replace that programme. The remaining argument was read: truncation/gluing and integration by parts, penalty contact support, capacity and volume estimates, Hölder optimization, comparison of heights, tail splitting, monotone modulus, background scaling, and local-global ball gluing. The bounded-test-dependent conclusions are conditional; no new source error established. In particular the new mass-deficit proof does not use 16.27.1 or 16.27.2.

Proposed change: optional strengthened quantitative conclusion and the fixed-relative-truncation argument in a separately reviewable source patch; do not edit the reading edition or tags in this audit. Affected potential dependents: 16.22.9–11, 16.27.12, and other uses of extrapolation where a quantitative lower bound is useful. No downstream proof is claimed corrected or fully certified.

Coverage delta: 2 whole direct mathematical sections, 1 nonexcluded partial section, 1 selected repeat dependency, 1 verified conditional deduction, 0 confirmed source errors, 0 newly established unresolved proof gaps, 0 complete transitive certifications. Historical first visits remain unreconciled. Demailly approximation and all specifically excluded proof-completion programmes remain deferred-by-user. No builds, tests, CI, source/registry/tag changes or publication.
