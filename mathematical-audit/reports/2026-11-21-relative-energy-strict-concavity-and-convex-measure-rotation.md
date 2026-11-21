# Direct audit: relative Monge–Ampère energy and selected convex-measure arguments

**Date:** 2026-11-21. **Reviewed main SHA:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Audit-only branch:** \`review/mathematical-audit\`.

## Exact current reading-edition scope

1. **Complete §17.1, Relative energy and Perron segments**, \`docs/sections/relative-energy-and-perron-segments/index.html\`, main Git blob \`493edc98a5b3be47ec22f02827ad167596105a9d\`, mathematical introduction lines 5–19 (37 physical lines). Scope: connected compact Kähler background, model-potential and positive-mass hypotheses, roadmap and stated dependence on capacity integration by parts. This is an introduction, **not** proof-chain certification.
2. **Complete §17.3, Relative Monge–Ampère energy**, \`docs/sections/relative-energy-and-perron-segments--relative-monge-ampere-energy/index.html\`, blob \`16fdcc4c6a6f0cc75e69ba267bd7da2b2d7922a1\`, mathematical lines 7–324 (337 physical lines). Checked the common mixed mass, finite energy, beta-integral first variation, concavity, net continuity, finite-energy characterization, curve example, mixed finite-energy integrability, and truncation error comparison. Principal original source: \`foundations-of-pluripotential-theory\`.
3. **Selected dependency recheck, not whole §17.2**, \`docs/sections/relative-energy-and-perron-segments--integration-by-parts-for-bounded-differences/index.html\`, blob \`5779ef1a17a52e02052c7485a7aa04adf606aace\`; inspected definition 17.2.1 (lines 16–41), capacity limit Lemma 17.2.2 (48–72), Lemma 17.2.3 (77–150), integration-by-parts Theorem 17.2.5 (155–193), and sign Lemma 17.2.7 (198–228). **§17.2 was already directly audited on November 19**, including POME-NPP-IBP-DIRICHLET-SEMINORM-001; neither is a new whole section or new finding here. In particular the line-131 bound on \`dd^c chi\` uses the four *unperturbed* potentials in \`zeta_0\`, so the changed coefficient \`(1+epsilon)lambda\` of the perturbed maxima does **not** refute that margin estimate.
4. **Selected only §21.11**, \`docs/sections/convex-functions-and-convex-bodies/index.html\`, blob \`2a123a863642a5a75caa173f0f73aff439a02ea4\`, lines 563–610 (Minkowski sum of gradient images), 625–668 (Alexandrov mass), and 673–736 (vague convergence, comparison, Legendre pushforward). The printed §21.11.55 already explicitly explains that weak convergence uses compactly supported tests and gives a mass-escape example (lines 674–683); **no new counterexample** is claimed. Not a whole §21.11 review.

### Finding POME-RELENERGY-STRICT-CONCAVITY-DIRICHLET-GAP-001

**Severity:** low. **Status:** verified conditional deduction, **not** a false theorem, proof gap, or completed upstream-chain certification.

**Anchors:** §17.3 Proposition 17.3.4, source \`foundations-of-pluripotential-theory:44639882\`, permanent \`9086ABF36774\`, lines 42–90; equation 17.3.5 source \`foundations-of-pluripotential-theory:A392067F\`, permanent \`46190A7C1B2F\`; §17.3 Proposition 17.3.9, source \`foundations-of-pluripotential-theory:A4AB3054\`, permanent \`356D15D0C316\`, physical lines 96–117, particularly the second-variation identity at lines 110–116. Normalization \`dd^c=i/(2pi)partial barpartial\`. Internal inputs are the signed-current integration by parts Theorem 17.2.5 and the smooth Stokes identity; no excluded Demailly/OT/Bergman programme is used.

**Precise hypotheses.** Let \`(X,omega)\` be a connected compact Kähler manifold of complex dimension \`n>=1\`. Let \`theta\` be a smooth closed real \`(1,1)\`-form and \`phi\` a positive-mass model potential. Let \`u,v\` be **smooth real-valued** \`theta\`-psh functions with \`u,v ~ phi\` (hence in the relative bounded-difference class), satisfying the **common strictly positive lower bound**
\[
\theta+dd^cu\geq\delta\omega,\qquad
\theta+dd^cv\geq\delta\omega,\qquad\delta>0.
\]
Write \`h=v-u\`, \`u_t=(1-t)u+tv\`, and \`D_\omega(h)=\int_Xdh\wedge d^ch\wedge\omega^{n-1}\`. Then for every \`0<=t<=1\`:
\[
\boxed{\ E_\theta^\phi(u_t)-(1-t)E_\theta^\phi(u)-tE_\theta^\phi(v)
\ \geq\ \frac{n\delta^{n-1}}2\,t(1-t)\,D_\omega(h).\ }
\]
The right side is nonnegative and strictly positive for \`0<t<1\` when \`h\` is nonconstant; the equality case modulo constants follows because \`X\` is connected. In complex dimension one the formula is an **identity**, so the factor \`1/2\` is sharp in that dimension.

**Complete proof.** The two curvature bounds imply \`theta_{u_t}=(1-t)theta_u+t theta_v >= delta omega\` for all \`t\`. The polynomial first-variation argument of Proposition 17.3.4 and the second variation in Proposition 17.3.9 give
\[
\frac{d^2}{dt^2}E_\theta^\phi(u_t)
=n\int_Xh\,dd^ch\wedge\theta_{u_t}^{n-1}.
\]
Since \`theta_{u_t}\` is closed and smooth, Stokes gives
\[
\frac{d^2}{dt^2}E_\theta^\phi(u_t)
=-n\int_Xdh\wedge d^ch\wedge\theta_{u_t}^{n-1}.
\]
With \`d^ch=i(\bar\partial h-\partial h)/(4\pi)\` we have \`dh\wedge d^ch=i\partial h\wedge\bar\partial h/(2\pi)\geq0\`, so positivity of wedge products yields
\[
E''(t)\leq -n\delta^{n-1}D_\omega(h)=-A.
\]
Set \`q(t)=A t(1-t)/2\`. Then \`(E-q)''<=0\`, so concavity of \`E-q\` places it above its chord, which is the claimed inequality. The positive form \`dh\wedge d^ch\wedge\omega^{n-1}\` integrates to zero exactly when \`dh=0\`, i.e. \`h\` is constant on connected \`X\`. In dimension one \`theta_{u_t}^{n-1}=1\`, so \`E''=-D_\omega(h)\` identically, giving equality.

**Limitations, nonduplication and proposed placement.** This is a **smooth, uniformly strictly positive** conditional strong-concavity estimate, not a statement for arbitrary singular finite-energy potentials and not a self-contained certification of non-pluripolar product calculus. It is distinct from the previously logged §17.2 Dirichlet seminorm (which only establishes semidefiniteness/Cauchy–Schwarz for bounded quasi-psh differences, without a quantitative energy chord gap), and from earlier Gauduchon mass coercivity. If desired, add an audit-only proposed corollary after Proposition 17.3.9; do not edit source/body or permanent tags on this branch. Dependents: quantitative strictness of relative energy along smooth positive segments, uniqueness modulo constants for the corresponding local concavity equality case, and potential Poincaré coercivity estimates. No global uniqueness theorem is newly certified.

## Other mathematical checks and open dependencies

- §17.3.4: \`binom(n,j) int_0^1 r^j(1-r)^(n-j)dr=1/(n+1)\`, giving the correctly normalized \`1/(n+1)\` energy and its first variation; signed-current factors are defined in §17.2.1, not through an unjustified classical product.
- §17.3.13: a decreasing **net** is reduced to an auxiliary sequence using \`L^1\` convergence, but the limit of the full energy net is controlled through monotonicity; the selected indices are *not* asserted to be cofinal. No sequential-compactness substitution is made.
- §17.3.14: total mass equality on the truncation locus and the \`k^{-1}\` tail bound show that finite extended energy forces full relative mass; the converse uses full mass plus locality and an integrable common tail.
- §17.3.19: the half-level truncation estimate (17.3.21) has the correct cutoff \`k/2\`, and the comparison of measures includes the fixed \`j\` factors; this is distinct from the already logged §16.5 half-level proof repair.
- §21.11.53, source \`sgpt:A4553D04\`, permanent \`F30A95FDA78E\`, lines 643–668: for full-dimensional \`P\`, the convex closed gradient image contained in \`P\` has equal volume iff it equals \`P\`; lower-dimensional bodies are explicitly separate. §21.11.57 source \`sgpt:E51EE4AF\`, permanent \`8DE662F4EFE6\`, lines 705–736: the pushforward identity uses Legendre subgradient inversion on the a.e. differentiability locus, not pointwise differentiability everywhere.
- **Uncertified upstream inputs:** plurifine/non-pluripolar locality and polarization (§13.2), mass invariance (§13.8), model-potential and mixed-mass assertions (§16.21–16.22), relative-capacity continuity (§16.25–16.27), and the Rockafellar gradient-image/Legendre duality inputs in §21.11. These are not falsely reported as new external findings or fully verified chains; further examination is outside this run. If a dependent invokes excluded regularization, log the dependence without reopening that programme.

**Outcome:** +2 current complete direct mathematical sections (§17.1 introduction, §17.3 substantive), +1 selected prior-complete prerequisite (§17.2), +1 selected partial section (§21.11), +1 low-severity verified conditional deduction, +0 confirmed printed errors, +0 certified complete upstream chains. None is claimed to be an historical first visit. The earlier §17.2 finding and §21.11 weak-convergence qualification are not repeated as new results. No tests, builds, GitHub Actions CI, source/body, canonicalization, registry, main, permanent-tag or published-site changes.
