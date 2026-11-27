# Divisorial endpoint rigidity on the scalar Hopf threefold

Date: 2026-11-27. Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit starting head: 1e9d8df0ece1e521c2416410d4bfbfb01643ceab.

## Scope and exact anchors

- Whole direct conditional reading of §12.35, `docs/sections/a-gauduchon-variational-volume--divisorial-constraints-and-residual-volume/index.html`, blob 718dbcd7fa3ce5d5be061881c917d8a8c99406f7, physical mathematical lines 7–340. Proposition 12.35.1 source BA07E404 / permanent C43B33AA4A18 (32–67); threshold (12.35.2) D8ACD0FADFBD (71–78); residual root (12.35.3) 44DAB02F7C7C (81–94); Theorem 12.35.4 source 6629041C / permanent 7B32818E6010 (101–138); first variation (12.35.5) 3EE856593807 (145–152); Proposition 12.35.7 source 4F49A535 / permanent 280181A9DE22 (169–199); Proposition 12.35.9 source E8B67AAC / permanent E45E9799C813 (226–253); Corollary 12.35.11 source 38159801 / permanent F402CC8C0A7E (264–285); Example 12.35.13 source 6BCE1933 / permanent 76B0694EBA2F (296–340).
- Whole direct conditional reading of §12.36, `docs/sections/a-gauduchon-variational-volume--a-divisorial-threshold-on-the-hopf-threefold/index.html`, blob 9a5ffb97b0e8400fd7a4e65054d66938b8f75200, mathematical lines 7–71. Proposition 12.36.1 source 6F61AFA1 / permanent 3A78333ED147, lines 20–71.
- Selected context §23.1, `docs/sections/unbounded-mass-on-hopf-manifolds/index.html`, blob f53618e8d808de21687ff9166971cb9302ea8cfb, lines 17–97 (Theorem 23.1.1 statement, not its later concentration proof; metric identities in (23.1.3), permanent 25275E5CD565). Selected §12.2 lines 7–90, blob 9ec67161d46b3ba20afa1b1c9a0c84f29322763e (quotient and smooth scalar). Here the vertical form denoted beta in §23.1 is zeta in §12.36, not a change in normalization.

Both primary sections had LEGACY-UNRECONCILED matrix rows without specific coverage. The actual current ToC has 747 distinct numbered sections, all present in the 747 distinct matrix rows. No historical first-visit claim.

## POME-HOPF-DIVISOR-ENDPOINT-RIGIDITY-001

Severity low; verified conditional deduction relative to the printed divisorial subtraction and current calculus. No false printed theorem. The printed proposition establishes a zero-mass endpoint potential; the stronger assertion below determines **all** admissible potentials at that endpoint, not just the displayed one.

### Claim

With the exact scalar Hopf threefold and forms of §12.36, every zeta-PSH function is constant. Consequently every omega-PSH function whose generic Lelong number along H is at least 1 equals sigma_H plus a constant. Its extended non-pluripolar MA measure vanishes, and the endpoint residual lower and upper masses are both zero. In particular the residual upper mass is infinite for every a<1, but zero at a=1.

### Proof

Put s=log|z|^2 on the covering space, alpha=dd^c s and zeta=ds wedge d^c s, in the normalization of (23.1.3). The one-forms ds and d^c s descend because s changes by a constant. In particular zeta has rank one, alpha has rank two, alpha is closed, zeta^2=0, dd^c zeta=-alpha^2. The product formulas give d zeta=-ds wedge alpha and d^c zeta=-alpha wedge d^c s (using d^c d=-d d^c). In particular d zeta wedge zeta=0 and d^c zeta wedge zeta=0. 

Let T=zeta+dd^c v>=0 be the positive (1,1)-current of a zeta-PSH function v. The smooth nonnegative test alpha wedge zeta is dd^c-closed since dd^c(alpha wedge zeta)=-alpha^3=0. Distributional Stokes and zeta^2=0 yield

    integral_X T wedge alpha wedge zeta = 0.

The integrand is a positive measure. In a smooth omega-unitary frame adapted to the orthogonal horizontal and vertical subbundles, write the Hermitian coefficient matrix of T as a positive matrix of measures. Take Radon–Nikodym derivatives with respect to its trace measure. Wedging with alpha wedge zeta gives a positive smooth multiple of the sum of the two horizontal diagonal coefficients. Their sum vanishes, hence each vanishes. Positivity implies the corresponding off-diagonal entries vanish as well (the pointwise Cauchy–Schwarz inequality for the Radon–Nikodym matrix). Therefore T=f zeta, where f is a nonnegative scalar distribution of order zero, locally a measure in smooth coordinates; the scalar is globally defined because zeta is a nowhere-vanishing smooth rank-one form. No smoothness of v or f has been assumed.

Since dd^c dd^c v=0, we have dd^c T=dd^c zeta. Apply dd^c to f zeta and wedge with zeta. All terms differentiating f disappear: the second derivative term contains zeta^2, while the first derivative terms contain d zeta wedge zeta or d^c zeta wedge zeta. These are identities of distributions multiplied by smooth forms, not products of singular currents. Thus

    -alpha^2 wedge zeta = dd^c T wedge zeta
                        = f dd^c zeta wedge zeta
                        = -f alpha^2 wedge zeta.

The form alpha^2 wedge zeta is everywhere a positive smooth volume form. Multiplication by it identifies scalar distributions with top-degree currents, so f=1 as a distribution. Hence dd^c v=0. By local distributional harmonic regularity and the maximum principle on the connected compact manifold, v is constant (and its canonical quasi-PSH representative agrees everywhere).

Apply Proposition 12.35.1 to subtract [H] from omega+dd^c u for any u satisfying the Lelong threshold. The canonical L1 difference u-sigma_H is zeta-PSH, hence constant. Equality almost everywhere becomes equality of quasi-PSH representatives. The extended product off H is zeta^3=0 and does not charge H, proving the claim. All residual admissible potentials at a=1 are smooth constants, so even the unrestricted residual upper mass is zero. The infinite upper mass for a<1 is the already printed statement (not counted as new). This proves the discontinuity at the endpoint, despite the continuous variational volume.

The same trace argument works on the standard scalar Hopf n-fold for n>=3: use the dd^c-closed (n-1,n-1)-test alpha^(n-2) wedge zeta; after identifying T=f zeta, wedge the dd^c identity with alpha^(n-3) wedge zeta. Its coefficient is the positive volume alpha^(n-1) wedge zeta. The argument does not extend to n=2 by the latter wedge (negative exponent); no surface assertion is made.

### Proposed insertion and dependents

Add the rigidity claim after Proposition 12.36.1, keeping its tag and all existing statements. The proof strengthens the a=1 clause and distinguishes the residual upper mass from the variational volume. No original claim is refuted. The endpoint application is conditional on the divisor subtraction in §5.38.1 and the extended-product locality/noncharging in §13.14.3, whose full proofs were not reopened. No claim is made for a general nef rank-one background without the Hopf differential identities.

## Other checks in the primary sections

- §12.35.1: generic Lelong inequalities give a positive residual via the cited subtraction lemma; the L1 representative is necessary. The converse is direct Poincare–Lelong; Stokes and the stated Lamari criterion give the threshold including its endpoint. This is a positive-current feasibility condition, not bounded residual feasibility. The n=1 Green argument uses connectedness.
- §12.35.4: checked equality of residual extended measures off the union of divisors, including arbitrary real coefficients, and noncharging of the divisor. The uniqueness step uses the printed threshold rigidity and bounded scalar comparison, not merely equality of total masses. These are conditional inputs (§12.10.12, §15.28.7, §14.19.10); no claim of transitive verification.
- §12.35.7: local smooth parameter families patch by uniqueness; capacity convergence follows by removing an open set of arbitrarily small capacity around the fixed analytic support; zero coefficients are omitted rather than evaluating 0*(-infinity). The generic Lelong calculation on a smooth modification uses the finite sum of pullback vanishing orders; smooth remainder contributes zero. The local multiplier ideal jump uses integrability exponent floor(a) in the printed convention.
- §12.35.9 and .11: independently checked normalization g=Vm/(2a), integral g=k, V=2k/H, T=Omega/a, integral beta wedge T=2k, D_mu(T)=sqrt(V)H. Differentiating V_s gives V_s'/2sqrt(V_s)=-(d+V_s H_s'/2)/(sqrt(V_s)H_s). For the height example H_s=(1/2)log((3-s)/(1-s)), derivative of sqrt(V_s) has the printed sign and factor 2. The improper integral is finite by the fundamental theorem on truncated intervals and the limit sqrt(V_s)->0. The endpoint non-bigness test is closed and supported where 1+tau<epsilon. The ordinary-type volume/first moment assertions of §20.3 are conditional inputs, not independently certified here.
- §12.36: with gamma_t=alpha+t zeta, checked dd^c gamma_t^2=0, numerator 2(1+2t) and denominator 4t, hence threshold 1. Checked R_a^3=6(1-a)^2 mu_0 and the perturbation scalar 6 epsilon^2(1+epsilon). The upper mass comparison uses determinant monotonicity and the existing smooth sequence of §23.1.1. That sequence's full construction was not reaudited.

## Status and exclusions

Two whole direct conditional sections, two selected context sections, one new conditional deduction, zero newly confirmed printed errors, zero demonstrated proof gaps, zero complete upstream-chain certifications. The previous matrix rows do not justify historical first-visit assertions. The Demailly approximation/regularization and dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss proof programmes remain deferred-by-user, not resolved or certified. Only the cited divisorial subtraction consequence is used, without reopening its regularization prerequisites. No tests, builds, CI, publication or production/source/registry/tag edits.
