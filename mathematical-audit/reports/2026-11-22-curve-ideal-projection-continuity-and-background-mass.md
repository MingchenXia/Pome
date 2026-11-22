# Current reading-edition audit: ideal-class geometry and background transport (22 November 2026)

- Reviewed main commit: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- Review-only branch: `review/mathematical-audit`. This document is an **audit note**, not a production/source correction or a formal-verification certificate.
- Direct whole-section readings: §18.5 and §18.6. Entire short introductory §17.11 also read. Selected dependency checks only: §18.4.2/.4/.8 and the curve potential/compactness arguments quoted in §18.6.
- No Demailly regularization, Bergman, L², Ohsawa–Takegoshi, multiscale atlas or positivity-loss proof-completion material was revisited. Any such external dependency remains deferred by user.

## New finding: `POME-IDEAL-CURVE-PROJECTION-ONLY-CONTINUOUS-AT-ZERO-001`

**Classification:** low / **verified conditional deduction** (not a false printed theorem, not a repair, and not certification of all prerequisites). The deduction uses the current curve and ideal-projection assertions of §§18.4 and 18.6. Its additional smooth-measure approximation is proved below.

**Anchor and provenance.** Integrated file `docs/sections/multiplier-ideal-envelopes-and-goodness--geometry-of-ideal-classes/index.html`, main blob `64b1c0de9266a28727de07ca3502a13ab974f001`, lines **7–140**, especially Theorem 18.6.4 at lines **43–86** (source label `E7B73391`, permanent tag `A55ADED04CFD`) and the discontinuity observation at **91–104**. The projection property is Theorem 18.4.2 (source `3A211D73`, permanent `7F20FD198864`) in `docs/sections/multiplier-ideal-envelopes-and-goodness--ideal-projection/index.html`, blob `f1979b73c857f4874dd4a5cb10b93bcc047ebbdc`, lines **22–51**.

### Exact statement

Let (Y) be a **compact connected Riemann surface**, let (	heta>0) be a smooth real ((1,1))-form with (int_Y	heta=1), and let (mathrm dV) be a smooth positive probability volume form. Give
[
mathcal K_	heta={uinmathrm{PSH}(Y,	heta):sup_Yu=0}
]
its (L^1(Y,mathrm dV)) topology. The normalized ideal projection
[
Pi:mathcal K_	hetalongrightarrowmathcal K_	heta,qquad
Pi(u)=P_	heta[u]_{mathcal I}
]
is **continuous precisely at (u=0)**.

In fact, at every (uinmathcal K_	heta) there are two sequences (s_j,a_j	o u) in (L^1), with (s_j) smooth and (a_j) rational finite-atomic Green models, such that
[
Pi(s_j)=0,qquad Pi(a_j)=a_jlongrightarrow u.
]
Consequently the two limiting images are distinct whenever (u
e0).

### Complete conditional proof

1. **At zero.** Each (vinmathcal K_	heta) is nonpositive, is itself an admissible competitor for its ideal projection, and satisfies
   [
   vlePi(v)le0.
   ]
   Because the smooth positive (	heta) makes (0) (	heta)-psh, the projection of (0) is (0). Thus
   [
   0le|Pi(v)|_{L^1(mathrm dV)}
   =-int_YPi(v),mathrm dV
   le-int_Yv,mathrm dV=|v|_{L^1(mathrm dV)}.
   ]
   This proves continuity at zero without assuming global Lipschitz continuity.

2. **Atomic approximants with fixed projections.** Theorem 18.6.4 constructs for every (uinmathcal K_	heta) normalized Green potentials (a_j) associated to finite atomic probability curvature measures with rational coefficients, with
   [
   a_j	o uquad	ext{in }L^1,qquad Pi(a_j)=a_j.
   ]
   The proof in the reading edition establishes the second identity from exact Lelong masses and total curvature mass one. This argument requires connectedness.

3. **Smooth approximants with zero projections.** Set (
u=	heta+mathrm{dd}^{mathrm c}u), a positive probability measure on the compact curve. Approximate (
u) weakly by smooth nonnegative probability forms (ho_j). For completeness, first approximate (
u) by finite atomic probabilities using small finite Borel partitions; then replace each point mass with a nonnegative smooth bump of the same mass supported in a sufficiently small coordinate disk. Uniform continuity of test functions guarantees weak convergence of the resulting smooth forms. The ordinary Green-kernel/Poisson construction on the compact connected Riemann surface supplies a smooth real function (s_j), unique up to a constant, satisfying
   [
   	heta+mathrm{dd}^{mathrm c}s_j=ho_j,qquadsup_Y s_j=0.
   ]
   Hence (s_jinmathcal K_	heta). Normalized (L^1)-compactness gives a convergent subsequence from every subsequence; any limit (s) satisfies (	heta+mathrm{dd}^{mathrm c}s=
u) by continuity of (mathrm{dd}^{mathrm c}) on distributions, and (sup s=0) by normalized psh (L^1)-compactness. Thus (mathrm{dd}^{mathrm c}(s-u)=0). A harmonic distribution on a compact connected curve is constant, and the normalization makes it zero. Every subsequential limit is (u), so the full sequence (s_j	o u) in (L^1). Because every (s_j) is smooth, all its multiplier ideals are trivial. Since (0inmathrm{PSH}(Y,	heta)), the ideal-envelope definition gives (Pi(s_j)=0). This is standard **linear Poisson theory on a curve**, not the user-deferred Demailly regularization programme.

4. **Only-if continuity.** If (Pi) were continuous at (u), the smooth sequence would yield (Pi(u)=0), while the atomic sequence would yield (Pi(u)=u). Hence (u=0). Step 1 proves the converse.

The proof does **not** assert that the quotient metric on ideal classes is pathological, or that (Pi) is noncontinuous in a stronger topology. It is specific to the (L^1) topology on the normalized potential space.

**Suggested patch (proposal only):** add a conditional corollary after Theorem 18.6.4 stating the exact continuity locus of the projection. Retain the printed theorem, its historical attribution, both permanent tags, and the stronger and weaker topologies separately. **Affected dependents:** §18.6's (L^1)-completion and mass-continuity discussion; any later claim that transports ideal models by (L^1)-continuous projection. No existing later theorem was declared false based on this observation.

## Other direct mathematical review (no new confirmed errors)

### §18.5, background transport and mass

Integrated file `docs/sections/multiplier-ideal-envelopes-and-goodness--changes-of-background-and-envelope-mass/index.html`, main blob `b1f37213571516320cd74288e4b3cbd1be2166bc`, lines **7–89**; section tag `FD3DFA6C79CF`.

- **Proposition 18.5.1** (source `41400384`, permanent `07B0D783C3F0`, lines 11–29): checked both competitor transports (vmapsto v-f+min f) and (v'mapsto v'+f-max f). Each restores the zero obstacle and preserves the corresponding ideal equivalence or ordinary type; the resulting inequalities have the stated directions.
- **Proposition 18.5.2** (source `BF2F5187`, permanent `6E8985733CBC`, lines 36–56): checked the distinction between equal positive currents and background-dependent **nonclosed** Hermitian total Monge–Ampère mass. The conclusion rests on the explicit nonclosed torus mass computation in Example 11.1.12 / Eq. 11.1.13, which was identified, **not independently re-certified** here.
- **Proposition 18.5.5** (source `47D5441C`, permanent `A2602BC06784`, lines 77–89): checked the exact direction of the inference from (P_omega[U]=0) and ideal projection Proposition 18.4.4. The construction of the infinite-mass (U) in Proposition 16.28.72 remains an **unverified upstream dependency**, not a new construction in this session.

### §18.6, ideal classes on a curve

Integrated file `docs/sections/multiplier-ideal-envelopes-and-goodness--geometry-of-ideal-classes/index.html`, main blob `64b1c0de9266a28727de07ca3502a13ab974f001`, lines **7–160**, section tag `3D693DBCCBE2`.

- **Proposition 18.6.1** (source `C2DA1190`, permanent `47A414940A74`, lines 20–35): checked the nondegeneracy of the (L^1) metric by psh representatives, total boundedness via normalized compactness, and equivalence of smooth volume forms on compact (X).
- **Theorem 18.6.4** (source `E7B73391`, permanent `A55ADED04CFD`, lines 43–87): checked unit total curvature mass, recovery of fixed logarithmic coefficients from ideal equivalence, weak finite-atomic probability approximation, rational weight rounding, convergence of normalized Green potentials by compactness/uniqueness, and the smooth witness proving incompleteness. The permanent label and the curve-specific connectedness and (int	heta=1) hypotheses were retained.
- **Proposition 18.6.6** (source `5F66399A`, permanent `8B21A468DD06`, lines 110–140): checked the sign and mass in (	heta+mathrm{dd}^{mathrm c}((1-	au)a_j)=	au	heta+(1-	au)
u_j); the polar subtraction leaves non-pluripolar mass (	au). Its weak limit (	au	heta) is consistent with the (d_S)-gap ((1-	au)/2) despite convergence in (d_{mathcal I}).
- **Example 18.6.8** (source `1415C673`, permanent `0F685C3DE85F`, lines 151–160): checked the smaller semipositive background (t	heta), monotone (tdownarrow0) scalar bound, and rational analytic types. Section 11.39 normalization-scalar conclusions were **not** fully reopened.

### §17.11, test-curves introduction

Integrated `docs/sections/test-curves/index.html`, main blob `0ece4d0eccf9c5e35e7ae6c4bc55335897e74e80`, lines **7–19**, permanent section tag `BA6AA7598BE3`. The Ross–Witt Nyström attribution, Legendre-sign convention (concave curves handled through negatives of convex functions) and signposting to §§17.12–17.15 and §22.1 were checked. This is **complete introductory reading**, not proof-chain certification of the correspondence itself.

## Coverage, limitations and classification

- **This session:** +2 current whole directly read mathematical sections (§§18.5, 18.6), +1 whole short introduction (§17.11), +1 new conditional deduction, **0 newly confirmed printed errors, 0 fully certified transitive proof chains**. Prior historical visits still need reconciliation.
- **Not covered:** complete proofs of §§11.1, 11.39, 16.28, 17.12–17.15, or all upper/lower analytical dependencies of §§18.4–18.6. Do not promote any of these to fully certified.
- The user-excluded Demailly/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof-completion programme remains **deferred-by-user**, not resolved.
- No builds, repository tests, CI, website publication, source/registry/entry changes, canonicalization or permanent-tag edits were performed.
