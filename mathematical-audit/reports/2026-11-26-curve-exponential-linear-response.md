# Curve exponential equations: explicit linear response at the zero exponent

Date: 2026-11-26. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Audit parent: dd542c75a75a73305bb20eca24be606edf63eb46.

## POME-CURVE-EXPONENTIAL-LINEAR-RESPONSE-001

Severity: low. Status: verified conditional deduction, not an error in the printed theorem. Proposed optional addition to Theorem 15.31.8 and Theorem 15.31.15; no production patch. The previous finite-energy trace weakening POME-CURVE-TRACE-FINITE-ENERGY-001 is distinct and unchanged.

Integrated anchor: docs/sections/equations-with-prescribed-singularities--singular-measures-on-products-with-a-curve/index.html, blob faaa787720a2f791dc9526724427e9b669516051. Theorem 15.31.8, source tag 964D213D, permanent tag 346FA2C8C90A, lines 112–126 and selection proof 201–213; equation 15.31.9 permanent C82032A970D1. Product application Theorem 15.31.15, source 1A894F9F, permanent 5F0343E9A338, lines 265–277. Inputs: Lemma 15.31.3 (E5EE483B/2CA6CA22B712), Lemma 15.31.4 (CF08BC57/F5E3175FA178), and the existence, barriers and uniform O(lambda) selection in Theorem 15.31.8. No extra smoothness of the measure.

Let Y=P^1, kappa the Fubini–Study probability form, mu a probability with finite continuous Green potential Q(x)=int G(x,y)dmu(y), G=1+log d_ch^2. Write T(f)(x)=int G(x,y) f(y)dmu(y), m=int Q dmu, w0=Q-m, and V=int w0^2 dmu. Let w_lambda be the bounded continuous solution of (15.31.9). Then, in the uniform norm,

    w_lambda = w0 + lambda Z + O(lambda^2),
    Z = T(w0) - (3/2)V.

In particular, dd^c Z=w0 mu, int Z kappa=-(3/2)V and int Z dmu=-(1/2)V. The O(lambda) estimate in the printed theorem is sharp unless V=0. In the latter case w_lambda=w0 for every positive lambda, not just to first order.

### Proof

The printed Dini tail estimate (15.31.11), together with bounded truncations of the Green kernel, gives a bounded map T:C(Y)->C(Y) in the supremum norm, with operator norm at most 1+A_mu. Indeed, continuity of each truncated integral follows by uniform continuity of the truncated kernel on the compact product; the tail error is at most ||f||_infty times the uniform tail in (15.31.11). Fubini is justified by the uniform absolute kernel bound (the same bound is available in the opposite variable by symmetry). In particular int T(f) kappa=0 and int T(f)dmu=int Q f dmu. The distributional Green formula gives dd^c T(f)=f mu-(int f dmu)kappa.

Set q_lambda=w_lambda-int w_lambda kappa. The equation and exact mass one give q_lambda=T(exp(lambda w_lambda)). From the printed barriers ||w_lambda||_infty<=osc Q and the printed selection estimate ||w_lambda-w0||_infty=O(lambda). Uniform Taylor estimates therefore give exp(lambda w_lambda)=1+lambda w0+O(lambda^2) and

    q_lambda = Q + lambda T(w0) + O(lambda^2).

No derivatives of the density or limiting exchange of unbounded potentials occur. In the exact identity int exp(lambda w_lambda)dmu=1, Taylor expansion one order further yields

    int w_lambda dmu = -(lambda/2) int w_lambda^2 dmu + O(lambda^2)
                    = -(lambda/2)V + O(lambda^2).

The constant w_lambda-q_lambda is consequently
    -m - lambda[int T(w0)dmu+V/2]+O(lambda^2).
Symmetry gives int T(w0)dmu=int Q w0 dmu=V, since int w0 dmu=0. Adding the constant to q_lambda proves the formula. Integrating Z and applying the distributional Green identity prove the three additional identities. Also the measure in (15.31.9) equals mu+lambda w0 mu+O(lambda^2) in total variation.

If V>0, ||Z||_infty >= |int Z kappa|=3V/2, so the uniform error divided by lambda tends to ||Z||_infty>0. If V=0, w0=0 mu-almost everywhere, and kappa+dd^c w0=mu=exp(lambda w0)mu for all lambda>0; the printed bounded uniqueness identifies w_lambda=w0. Conversely an o(lambda) uniform error forces Z=0 and V=0. For the example in Proposition 15.31.16 (82D9A1D5/DD2C5D7B64EC, lines 316–343), Q on its circle support is 1-2log 2-epsilon cos(theta) and dmu=(1+epsilon cos(theta))dtheta/(2pi), hence V=epsilon^2/2-epsilon^4/4>0. Sharpness thus occurs also for a singular probability.

### Product scalar and normalized potential, including nonunique maxima

Use exactly the product assumptions of Theorem 15.31.15. Put S=max_Y w0, M={x:w0(x)=S}, d=max_M Z, and u=Q-max Q on Y (pullback understood). Then

    log(c_lambda/c) = lambda S + lambda^2 d + o(lambda^2),
    v_lambda = u + lambda (Z-d) + o(lambda) in C(X).

To justify the max step without a differentiable or unique maximizer, evaluate the uniform expansion at a maximizer of Z on M to get the lower derivative bound d. For the upper bound choose x_lambda maximizing w_lambda. Uniform convergence gives w0(x_lambda)->S; by compactness, any sequence violating the upper bound has a subsequence with limit in M, and the difference quotient is <= Z(x_lambda)+O(lambda). This proves the right derivative d (and the same conclusion for any net tending to zero, since this is a real-parameter limit). The formula for c_lambda and v_lambda in the printed theorem gives the claims. No O(lambda^2) error is claimed for the normalized v_lambda in the absence of a quantitative separation of maxima. The unnormalized centered product U_lambda-lambda^{-1}log c has the stronger O(lambda^2) uniform remainder from the first formula.

## Actual coverage and mathematical dependency limits

Read current AGENTS.md (eda69505b93b4782290d9cfac07c8651dedd17c5), documentation/proof-expansions.md (8b37e218c74d5a93637e0f092cf5f29cc338a94d), current branch README and LATEST, LEDGER and SECTION_MATRIX. Current main docs/index.html yields 747 distinct section locators; compared to all 747 matrix rows, no missing/extra/duplicate locators.

- §15.30: docs/sections/equations-with-prescribed-singularities--exact-equations-on-products-with-zero-lower-mass/index.html, blob 650b84dd3d354e2da7c27f66f8670c0c882748f2, lines 7–243, whole current direct conditional review. Checked radial F', Q', normalized radial flux and L^p divergence; comparison directions for arbitrary smooth reference volume, product binomial coefficient, nonclosedness, and convex power barriers; bounded and unbounded factor-density argument. Existing POME-PRODUCT-TRUNC-SCALAR-LOGRATE-001 is NOT new. Scalar monotonicity 15.27.1, bounded solvability 14.19.2, threshold existence 15.28.4 and 15.28.7, and bounded/non-pluripolar product theory are conditional upstream inputs.
- §15.31: above path/blob, lines 7–343 whole current direct conditional review. Checked kernel normalization and distributional Fubini, Riesz pole-null argument, H^1 trace and composition, variational signs/coercivity, continuity via Dini, uniqueness and comparison, product Fubini and truncation, maximal coefficient and circle example. The weak compactness, trace machinery, contact locality (5.28.3–4) and strict domination 14.19.10 are not given new transitive certificates. New response proof only uses the printed curve existence/selection and Green kernel formulas.
- §15.36: docs/sections/equations-with-prescribed-singularities--radial-selection-for-integrable-densities/index.html, blob e007da9bd1c2136d289b278ba69a9cf8d4694d9e, lines 7–199 whole current direct conditional review. Checked monotone smooth density truncation (not Demailly regularization), separation, dominated mass convergence, flux roots, both ends of radial compactness, capacity argument, and finite/infinite moment split. The moment residue from POME-RADIAL-MOMENT-CRITICAL-POLE-COEFF-001 is NOT new. Closed-class full-mass uniqueness in lines 184–194 is explicitly external (25.6); retain that dependency, not independently proved here. Likewise greatest-solution and capacity-continuity inputs 15.35.2–3, 15.34.2 and capacity estimate (5.29.4) remain conditional. No claim for arbitrary nonseparated critical potentials.
- §1.1 lines 120–129, blob ef778e54d8d7413242387e95c52269b3c7d42cae, convention-only recheck, not new coverage.

No new confirmed printed errors or demonstrated gaps; one new conditional quantitative result. Historical first visits not asserted (legacy reports only partially reconciled). No complete upstream proof chains certified. Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain deferred-by-user, untouched; any upstream uses remain unverified black boxes. No tests, builds, CI, publication, registry/tag/body changes or edits to main.
