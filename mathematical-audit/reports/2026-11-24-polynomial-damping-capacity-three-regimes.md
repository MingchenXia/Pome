# Polynomial damping: three capacity regimes; mixed mass and tensor curvature rotation

Date: 2026-11-24. Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit parent: 074c2f170ad720ab77651de5e1fb9c8128c8a082.

## Finding POME-WEIGHTED-MA-POLYNOMIAL-CAPACITY-THREE-REGIMES-001

**Low / verified conditional deduction. Not a false printed theorem.** Theorem 13.15.11, permanent tag B72AF5B37CB7, source anchor CC944952, integrated file `docs/sections/weighted-monge-ampere-measures/index.html` (blob 37d9ae29e4861e1f280be6450b2c842b5ce452a3), physical lines 224–248. The printed estimate is valid but can be improved by integrating both restricted-mass bounds simultaneously instead of estimating the shallow layer by the largest weight.

Let X be a connected compact complex n-fold, omega a Hermitian form, u nonpositive omega-psh, mu=MA^ext_omega(u), r=max(n-2,0), and delta=Cap_omega(E) for a Borel set E. Assume the exact two estimates of Lemma 13.15.3 (permanent 357B2DE7779E; source anchor 1442AF83; equation 13.15.4 tag F3E7262939D2, lines 81–98):
\[
\mu(E\cap\{-u\le t\})\le \min\{C_\omega(1+t)^r,\delta(1+t)^n\},\quad t\ge0.
\]
The first bound follows from Proposition 13.15.2; the latter's bounded-product Stokes passage at line 60 cites Theorem 5.32.1. That excluded regularization dependency is **deferred-by-user**; it is neither reopened nor certified here. The capacity bound itself uses only the printed bounded truncation and positivity argument.

For every q>r and 0<delta<=1, there is a constant depending only on omega, n, q such that
\[
\int_E(1-u)^{-q}\,d\mu\le C
\begin{cases}
\delta^{(q-r)/(n-r)},&r<q<n,\\
\delta(1+\log(1/\delta)),&q=n,\\
\delta,&q>n.
\end{cases}
\]
At delta=0 the left side is zero. At delta>1 a uniform total-mass bound suffices (and is available from the same calculation). No optimality assertion about the improved exponents or the logarithmic endpoint is made.

### Proof
Write s=-u. Since mu does not charge the pole set, the identity
\[
(1+s)^{-q}=\int_s^\infty q(1+t)^{-q-1}\,dt
\]
holds mu-almost everywhere. Tonelli applies to the nonnegative integrand, even if mu has infinite total mass: mu is sigma-finite on the finite-depth sets by Lemma 13.15.3 and vanishes on the pole set. Consequently
\[
\int_E(1-u)^{-q}\,d\mu
\le q\int_0^\infty (1+t)^{-q-1}
\min\{C_\omega(1+t)^r,\delta(1+t)^n\}\,dt.
\]
More generally the same argument works for the continuously differentiable decreasing weights of Theorem 13.15.9, using -w'(t) in place of q(1+t)^(-q-1).

Put d=n-r>0 and R=delta^{-1/d}>=1. Splitting the integral at 1+t=R gives the upper bound
\[
q\delta\int_1^R x^{n-q-1}\,dx
+\frac{qC_\omega}{q-r}R^{r-q}.
\]
If q<n, the first term is at most q/(n-q) times delta R^{n-q}; both powers equal delta^{(q-r)/d}. If q=n, the first term is (q/d)delta log(1/delta), and the second is qC_omega/(q-r) times delta. If q>n, the first term is at most q delta/(q-n); the second is at most qC_omega/(q-r) times delta since (q-r)/d>1. If delta=0, every finite-depth intersection has zero measure, and increasing their union proves the claim. For delta>1, use only the first restricted-mass bound over the whole integral; it gives qC_omega/(q-r). This argument integrates on the original potential, without exchanging truncation and weak convergence limits.

For r<q<n the new power is strictly larger than the printed (q-r)/(q+n-r), because q>0. At q=n the log-corrected linear modulus is asymptotically strictly smaller than the printed fractional power, and q>n gives linear capacity domination. In particular, for n>=3 the intermediate exponent is (q-n+2)/2. For n=1 or 2 the formula gives q/n in the intermediate range. The integrability threshold q>r has not changed.

### Correction proposal and dependents
Retain the theorem's valid existing estimates for mass and tails. Add the stronger capacity bound as a remark or replace just its capacity display and the last estimate of the proof with the above layer-cake calculation. No permanent tags or registry changes. Theorem 13.15.9 (EE93EE2035F6, anchor 818B97D0, lines 168–210) already uses layer cake for the total and tail bounds; this refinement uses the two simultaneous bounds before integration. Uniform absolute continuity and fixed-depth weighted convergence are unaffected; no new conclusion about unweighted MA convergence or sharpness follows. The downstream logarithmic-weight discussion and Theorem 13.15.13 need not be changed.

## Other directly examined material

- §13.1, `docs/sections/non-pluripolar-products/index.html`, blob f9184772a635092cf8ef2e61e44faa65ea82e694, lines 7–36, whole mathematical introduction (section tag E478B9E17C75). Distinguished the local possibly infinite product from finite global compact-Kähler products; the degree-one pole loss and compatibility of restricted truncations are stated with appropriate context. No newly identified mathematical error.
- §13.9, `docs/sections/non-pluripolar-products--maximal-mass-and-comparison/index.html`, blob adbc9c739b3694725aa176e8013ac7f3077f035e, all mathematical lines 7–121. Definition 13.9.1 (4F64B29C315E), Proposition 13.9.2 (44F242B6965F, source 5364CD2E), Definition 13.9.3 (2AF01ACCF985), Corollary 13.9.4 (45601E7EC1EE), Proposition 13.9.5 (FEA17FAE6BAA, source D16465F8), Corollary 13.9.6 (D91589CC5A89, source 5F5C5397). Checked exact-form invariance, perturbation class comparison with the test form held fixed, homogeneity and the big-class squeeze, full mass limsup guard, strict comparison levels and pole exclusion, and the Fatou step in domination. In particular, in the final domination step the inequality t^n mu_rho({u<q_t})<=0 is used for each t>0 before Fatou, not divided after taking the limit. Internal monotonicity 13.8.7–8, locality 13.2.6 and capacity 13.7.5 remain prerequisite inputs, not independently certified in this run. The deferred direction positive volume implies big, referenced in line 49, was not audited here. No new error.
- §11.20, `docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--external-tensor-products-and-complement-convexity/index.html`, blob 95d0c68d98cac2c63e819f870b9786caf8a4cc24, all mathematical lines 7–70; Lemma 11.20.1 (B46ABA0FEC10), Theorem 11.20.2 (0B75DFE662A7), Corollary 11.20.3 (F8F43BAF4F9A). In product frames, M^{-1}partial M is a sum of single-factor connection matrices; bar-partial yields no mixed base terms. Pairing the lifted mean-curvature operator with an arbitrary tensor, not only a pure tensor, is strictly positive by a product orthonormal eigenbasis. Thus at least one positive eigenvalue per block, and the convexity index n+r-k is correct, including n_i=r_i=2. Checked §11.18.2/.4/.5 lines 51–123, blob fab309d460a8411fefcd1ef32a094927d6feea10, for the exhaustion criterion and the integrated degree normalization r lambda int omega^n=2 pi n deg(E). The existence of a Hermitian–Einstein metric for a stable bundle with a Gauduchon form is a genuine non-Hironaka external input, explicitly invoked at §11.18.4 line 99 and inherited by §11.20.3 line 69. Not independently proved here; no error in the conditional deductions. Preserve attribution.
- §11.12, complete repeat of mathematical lines 7–169, blob 9d8c639c4460719360048213e58aa08138dd1a71, file `docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--polar-norms-of-semipositive-finsler-metrics/index.html`. Checked the Schur complement conformal formula, local holomorphic quadratic cancellation, supporting pluriharmonic lower function, real Legendre maximum and strong convexity without real convexity of the primal. Historical 2026-11-08 nonsmooth polar finding is not counted as new. The referenced homogeneous convex regularization is distinct from the excluded Demailly programme but was not examined here; downstream smoothing is conditional.
- §13.15 selected mathematical lines 7–267 only (finite-depth estimates, exponential damping, smooth decreasing weights and polynomial/logarithmic weights); excluded regularization proof passage at line 60 not reopened; §§13.15.12 onward not reviewed. Verified fixed cutoff order in lines 202–209 and the elementary exponential and logarithmic weight calculations. No new printed theorem error.

## Coverage and scope

Three whole current direct sections (§13.1 introductory, §§13.9 and 11.20 mathematical), one whole historical repeat (§11.12), two selected sections (§13.15 and 11.18). Historic first visits not asserted. Current actual rendered TOC and existing coverage matrix both have 747 distinct section locators; checked set equality. One new conditional deduction; zero newly confirmed printed errors, zero new unresolved proof gaps, zero transitive proof-chain certificates. The Hermitian–Einstein input is recorded as a dependency, not as a new false theorem. No software build, tests, CI, publication, source edits, or tag changes. All user-excluded Demailly/Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss work remains deferred-by-user.
