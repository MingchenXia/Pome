# Pome mathematical audit: classical sweeping energy and the projective-line Legendre ray

Date: 2026-11-23. Main SHA: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit branch: review/mathematical-audit.
Current direct scope: entire mathematical §17.17, lines 7–246. Targeted, NOT whole-new §4.2: fine neighborhoods lines 24–129, Green energy and reduction lines 173–286, 290–329, balayage lines 334–450, quasi-Lindelöf and quasi-open arguments lines 485–550. §4.2 had a recorded full historical audit on 2026-11-21; this is a selected independent follow-up. Historical first visits are not asserted.

The explicitly user-excluded Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programs were neither opened nor certified.

## POME-BALAYAGE-ENERGY-NONEXPANSIVE-PROJECTION-001

Classification: low severity; **verified conditional deduction**, NOT an incorrect printed theorem. Upstream premise: the finite-Green-energy balayage and positive-definite bilinear energy already stated in Pome §§4.2.11 and 4.2.18. The transitive proofs of those premises are NOT fully certified.

Precise integrated anchors:
- docs/sections/fine-topology-and-balayage/index.html, main blob d4c8eed09391441b4b6d13e2fa402a60da70be0d.
- Proposition 4.2.11, source foundations-of-pluripotential-theory:0EBEB570, permanent 2BC493B5F349; mathematical lines 196–250 (symmetric finite bilinear energy, signed positivity).
- Theorem 4.2.16, source foundations-of-pluripotential-theory:23EEEACB, permanent F28E6D45483F; lines 380–400.
- Theorem 4.2.18, source foundations-of-pluripotential-theory:08AABB73, permanent 0056FED1AF8C; lines 408–450. Its inherited orthogonality equation (4.2.17) has permanent tag 7DCA4DACFD19 at lines 384–389.

**Statement.** Let B be an open Euclidean ball in real dimension d>=2, and A a compact subset of B. Let E_B be the real vector space of finite signed Radon measures compactly supported in B whose positive and negative Jordan parts both have finite Green energy I_B. Define the signed sweeping operator by

\[
S_A(\sigma)=\bigl(\sigma^+\bigr)^A-\bigl(\sigma^-\bigr)^A,
\]

where the positive balayage of finite-energy measures is the one from Theorem 4.2.18. Then S_A is linear, its values are signed finite-energy measures supported on A, and for every sigma in E_B and every finite-energy signed tau supported on A,

\[
I_B(\sigma-S_A\sigma,\tau)=0,\qquad S_A^2\sigma=S_A\sigma.
\]

In particular, for any two finite-energy positive measures mu, nu, the following exact **two-input Pythagorean identity** and sharp contraction hold:

\[
\boxed{
I_B(\mu-\nu)=
I_B(\mu^A-\nu^A)
+I_B\bigl((\mu-\mu^A)-(\nu-\nu^A)\bigr).
}
\]

\[
\boxed{I_B(\mu^A-\nu^A)\le I_B(\mu-\nu).}
\]

The contraction constant one is optimal for every compact nonpolar A: take mu a nonzero finite-energy positive measure supported on A, nu=0. If A is polar, S_A is zero, so its operator norm is zero. This is an algebraic orthogonal projection in the Green-energy inner-product space of finite-energy signed measures; it does NOT assert that the space is already complete in that norm or that an abstract Hilbert-space projection theorem was invoked.

**Proof.** For a positive finite-energy source mu, the inherited identity (4.2.17) gives I_B(mu-mu^A,tau)=0 for each positive finite-energy tau supported on A. Let tau be signed, with Jordan decomposition tau^+-tau^-. Its Jordan parts have finite energy by the hypotheses, so apply the equality separately and subtract. The same yields the equality for any signed source sigma by subtracting its two positive Jordan parts. Since Theorem 4.2.18 asserts positive additivity and homogeneity, the signed extension is linear; one may also check linearity by writing an arbitrary signed equality as an equality of sums of positive measures. As S_A sigma is supported on A and has finite-energy Jordan parts (each part is bounded by the sum of the two positive sweeps, and the nonnegative Green kernel gives finite energy), applying the fixed-support clause in Theorem 4.2.18 shows S_A(S_A sigma)=S_A sigma. Expanding sigma=S_A sigma+(sigma-S_A sigma), its mixed energy term is zero by the established orthogonality, giving

\[
I_B(\sigma)=I_B(S_A\sigma)+I_B(\sigma-S_A\sigma).
\]

Apply this to sigma=mu-nu. Positivity of the last term is Proposition 4.2.11. For a nonpolar compact A, the equilibrium-measure variational formula of Proposition 4.2.12 (lines 259–285) supplies a nonzero positive finite-energy measure on A; sweeping fixes it. Polar compact A supports no nonzero finite-energy measure and Theorem 4.2.18's swept measures have finite energy, so all such sweeps vanish.

This deduction uses **signed differences**, not an unwarranted comparison of positive energies I_B(mu) and I_B(nu), and requires compact source supports and finite energies. Neither probability normalization nor preservation of total mass is asserted: the printed sweeping theorem only gives the mass inequality.

Suggested reviewable addition: place a short signed-energy corollary after Theorem 4.2.18; retain all existing source attribution, permanent tags and exact source versions. Affected dependents: quantitative stability of finite-energy sweeping, harmonic-measure approximations and the classical capacity/energy formalism; no downstream proof is declared certified by the addition.

## POME-LEGENDRE-P1-RAY-UNIFORM-VELOCITY-001

Classification: low severity; **verified conditional deduction**, NOT an incorrect printed theorem. Conditional on the explicit smooth ray in Proposition 17.17.11, whose formula is directly verified; the general envelope-ray/Perron upstream chains are not transitively certified.

Precise integrated anchors:
- docs/sections/test-curves-and-legendre-duality/index.html, main blob 704ed205a974fe18e2dc502b13ceaf382b4af4b3, entire mathematical lines 7–246.
- Definition 17.17.2: source non-kahler-pluripotential-theory, permanent 7D4FF1072CEF, lines 21–41.
- Theorem 17.17.5: source non-kahler-pluripotential-theory:0C9A47EA, permanent 548B64628B04, lines 69–123; equation (17.17.6), permanent DD25DD31A00B, lines 109–122.
- Theorem 17.17.8: source non-kahler-pluripotential-theory:1786FAA0, permanent 062DEC0E6527, lines 132–181.
- Proposition 17.17.11: source non-kahler-pluripotential-theory:42E4DFA8, permanent 377F0AD20B28, lines 184–246; explicit equation (17.17.12), source 1A6C8986 and permanent 9BA75154C113, lines 206–211.

**Statement.** For the smooth ray on X=P^1, normalized so that omega=dd^c log(1+|z|^2), integral omega=1, and

\[
U_t(z)=\log\frac{1+e^t|z|^2}{1+|z|^2},\qquad
\omega_t=\omega+dd^cU_t,
\]

put v_t=partial_t U_t. For each t>=0, the pushforward probability measure (v_t)_*omega_t is exactly uniform Lebesgue measure on [0,1]. Thus for every real q>=0,

\[
\boxed{\int_{\mathbb P^1}|\partial_t U_t|^q\,\omega_t=\frac1{q+1}.}
\]

For the normalized one-dimensional Aubin–Mabuchi energy E(U)=1/2 integral U(omega+omega_U), E(0)=0, we also have

\[
\boxed{E(U_t)=t/2.}
\]

The results concern the **smooth slice measures**, not the singular inverse transforms; they make no assertion about an unverified d_p metric identification.

**Proof.** Direct differentiation gives v_t(z)=e^t|z|^2/(1+e^t|z|^2). With w=e^{t/2}z, the curvature form omega_t=dd^c log(1+|w|^2) is the pullback of the normalized Fubini–Study form. After integrating out the angular variable, the latter has radial density drho/(1+rho)^2 for rho=|w|^2. The substitution p=rho/(1+rho) gives dp=drho/(1+rho)^2; thus p is uniformly distributed on [0,1]. The exceptional poles z=0,infinity have zero smooth area measure. Integrating p^q proves the displayed moment formula. For smooth paths in complex dimension one, direct differentiation of E(U)=1/2 integral U(omega+omega_U), followed by integration by parts on compact P^1, gives E'(t)=integral v_t omega_t=1/2. Since U_0=0, the energy formula follows. The factor 1/2 is consistent with the Pome dd^c convention and integral omega=1.

Suggested optional reviewable note: append the distribution and energy calculation to the example after Proposition 17.17.11. It documents the quantitative toric interpretation without changing its correspondence or claiming it proves general Perron maximality.

## Additional direct checks and limitations

- Entire §17.17: tested the strict cutoff tau<c in Definition 17.17.2, the need for the tau<=0 branch at the pole in Proposition 17.17.11, normalization sup_X U_t=ct, the bounded-in-time inverse estimate (17.17.6), and the affine obstacle-envelope argument in lines 152–180. The order of the infimum over M>0 and the limit s downarrow 0 in Theorem 17.17.8 is valid because sM ranges over all positive t for each fixed s. No new definite mathematical error found.
- Selected §4.2: tested positive definiteness versus finite-energy signed differences (lines 196–250), equilibrium normalization and capacity scaling (259–285), sweeping mass inequality and characterization (380–450), point-mass harmonic-measure example (455–481), and quasi-Lindelöf Choquet countability logic (491–518). The preexisting §4.2 full-section review on 2026-11-21 is not counted as a new first visit. The further quasi-open argument (523–550) was sampled only, not independently certified.
- Theorem 4.2.18 remains conditional on the earlier decomposition of finite-energy measures with continuous potentials (Proposition 4.2.11 and Theorem 4.1.10), the ball Green representation (4.1.16), and the polar-set comparison (4.2.13). These are nonexcluded inputs; their full transitive proofs were not reverified.
- §17.17 general correspondence still depends on internal §§5.40–5.41 and §17.16 (especially Legendre inversion, Perron gluing and the envelope minimum principle). These are not claimed as complete upstream certificates.

Accounting: one entire current mathematical §17.17 directly read; one historical-full §4.2 selectively revisited (not new full coverage); two new verified conditional deductions, zero confirmed new original errors, zero fully certified transitive proof chains. All 747 TOC section rows and deferred-by-user statuses remain intact. No builds, tests, CI, branch merge, source/body/registry/permanent-tag edits or publication.
