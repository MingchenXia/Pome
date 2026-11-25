# Curve model rooftops and all total-variation geodesics

Date: 2026-11-25. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Audit branch parent: d0f68f60501ef0decf26ea54b86b021866f67755.

## Finding POME-CURVE-MODEL-ROOFTOP-ALL-GEODESICS-001

Severity low. Status: verified conditional deduction, not a confirmed error in a printed statement. The entire conclusion below is conditional only on the existing curve model classification and TV distance formula. No regularization proof is reopened.

Source: docs/sections/volumes-under-bounded-mass--model-potentials-on-curves/index.html, blob 4ec0e8d5c90ad5df4e84f17bbc03a2298415e29f. Lemma 13.28.1 (source 3D44FEE1, permanent 2422DD1AB3AB, lines 20–59; in particular order criterion (13.28.3), permanent C63C9A28E474, lines 43–50), Theorem 13.28.4 (source 647BF17A, permanent 74646DD62F50, lines 64–86), Corollary 13.28.7 (source 9002ECF9, permanent FB89848D2500, lines 91–106). The printed corollary constructs a geodesic by linear interpolation of polar measures, but does not characterize every geodesic or the existence of a common lower model. The following complements that result, including zero mass and the ideal locus.

Let Y be a compact connected Riemann surface, theta a smooth positive form, A its area. Use the printed notation p_mu for the ordinary model corresponding to a positive polar measure mu with mu(Y) <= A, U(p_mu)=A-mu(Y), and d_theta(p_mu,p_nu)=||mu-nu||_TV, with the total variation norm (not half the norm). All claims include the cases of zero polar measure and zero non-pluripolar mass.

### 1. Order, rooftop, and an exact compatibility test

Write m=mu wedge nu and M=mu vee nu for the measure infimum and supremum. With respect to the dominating measure rho=mu+nu they have the pointwise minimum and maximum of the two densities; thus they are positive polar measures and m+M=mu+nu.

By (13.28.3) and the proof of 13.28.1, p_mu is the largest theta-psh function v <= 0 such that T_v >= mu. Consequently p_mu <= p_nu if and only if mu >= nu: the reverse implication is inclusion of competitor families; the forward one follows by applying the defining criterion for nu to p_mu, and then using that the polar part of T_{p_mu} is mu. In the last step, since nu is carried by a polar set, the diffuse part of T_{p_mu} gives it no mass.

For the ordinary rooftop P_theta(min(p_mu,p_nu)), a competitor v lies below both obstacles if and only if v <= 0 and T_v dominates both mu and nu. This is equivalent to T_v >= M. Its mass is A, so a competitor exists exactly when M(Y) <= A. In that case its envelope is p_M by the classification. Otherwise the rooftop is identically minus infinity. The least model majorant of p_mu and p_nu is p_m (the largest measure dominated by both). In particular P_theta[max(p_mu,p_nu)]=p_m, also directly by the printed max-polar formula in the proof of 13.28.4. The raw pointwise maximum need not itself be a model.

Since ||mu-nu||_TV=M(Y)-m(Y)=2M(Y)-mu(Y)-nu(Y), the rooftop is nontrivial if and only if

    d_theta(p_mu,p_nu) <= U(p_mu)+U(p_nu).

Whenever it exists, the exact distance is U(p_m)-U(p_M). These formulae apply without a positive-volume premise. For example two distinct saturated point-pole models A delta_x and A delta_y have distance 2A, volumes zero and no common lower model, even though the model space admits a geodesic between them. The ideal subspace satisfies the same formulae because min/max of atomic measures are atomic.

### 2. All metric segments and constant-speed geodesics

Let delta=nu-mu, lambda=|delta|, L=lambda(Y). For L=0 the only segment is the constant one. Suppose L>0. A third model p_xi belongs to the metric segment (equality in the triangle inequality with endpoints) if and only if

    xi = mu + g delta,  0 <= g <= 1 lambda-a.e.,  xi(Y) <= A.

Here g delta is the signed measure with density g against delta. Necessity: write densities of mu, nu, xi with respect to their sum. Equality of TV distances makes the integral of the nonnegative real triangle deficit zero, so the density of xi lies between those of mu and nu almost everywhere. On the set where endpoint densities differ take g to be their affine interpolation coefficient; where they coincide xi has that same density and g can be assigned zero. Sufficiency follows by the same density comparison. Such xi is positive and carried by the union of two polar carriers; no uncountable union of carriers is involved. Its distance from p_mu is integral g d lambda and from p_nu is integral (1-g) d lambda.

It follows that all constant-speed geodesics t -> p_{xi_t}, t in [0,1], are exactly

    xi_t = mu + g_t delta,
    0 <= g_t <= 1 lambda-a.e., xi_t(Y) <= A,
    integral g_t d lambda = t L,
    g_s <= g_t lambda-a.e. for every s <= t.

Indeed any geodesic has the segment property and the distance to the initial endpoint t L. Also for s<t the equality ||xi_t-xi_s||= (t-s)L = integral (g_t-g_s) d lambda forces g_t>=g_s almost everywhere. Conversely these properties imply distance (t-s)L. No simultaneous pointwise representative for uncountably many times is needed: each pairwise measure identity suffices. In particular any geodesic between ideal models consists entirely of ideal models, strengthening the possible existential interpretation of geodesic convexity in the corollary.

### 3. Exact uniqueness criterion and constructive alternative midpoint

The geodesic is unique if and only if delta=0 or lambda is supported on a single point. In the one-point case the integral condition forces g_t=t on that point, so the affine measure interpolation is the only geodesic.

If lambda is not concentrated on one point, choose a Borel set E with 0<lambda(E)<L (a finite Radon measure on a compact metrizable space that is not a point mass has two distinct support points and disjoint positive-measure neighborhoods). Set h=1_E - lambda(E)/lambda(Y\E) * 1_{Y\E}. This bounded function has lambda integral zero and is nonzero lambda-a.e. Replace h by -h if needed so that integral h d delta <= 0. For sufficiently small eps>0 let g=1/2+eps h. Then 0<=g<=1, integral g d lambda=L/2 and the mass of xi=mu+g delta is at most that of (mu+nu)/2, hence at most A. The midpoint xi is distinct from the affine midpoint and has both endpoint distances L/2. Piecewise affine interpolation from mu to xi and xi to nu is a second constant-speed geodesic: on each half the interpolation coefficient is respectively 2t g and g+(2t-1)(1-g), increasing in t for every fixed lambda-a.e. point. Positivity, mass bound and polar support are preserved by convex interpolation. This construction remains in the ideal locus for atomic endpoints.

The criterion is not contradicted by the possible saturation of the mass bound at both endpoints; choosing the sign of h explicitly deals with that boundary. If a curve has a nonzero atomless polar measure, even the segment from zero polar measure to that measure has multiple geodesics. A difference supported on one point gives uniqueness even at saturation.

Proposed correction: no source theorem needs replacement. Add a corollary following 13.28.7 (or an independent section-level note) giving these exact compatibility and geodesic criteria. Affected applications: the model geodesic convexity in 13.28.7, the atomic subspaces in 13.28.17 and 13.28.22, and any future use of common lower models in the curve case. Do not infer uniqueness from completeness/geodesicity, or existence of a rooftop from existence of a metric geodesic. No claim about higher-dimensional model spaces or their complete upstream proofs.

## Direct integrated reading and cross-section rotation

* Section 13.28 (same file/blob above): mathematical lines 7–395, including the classification, norm identity, closedness and density, zero-mass convergence, Cantor example, ordinary type pseudometrics, diffuse concentration, all-obstacle topology and zero-mass relative class. The compactness subsequence arguments are in metric L1 spaces; the extension from sequential continuity to nets in lines 234–250 is valid because the map is between metric spaces. In the mass bound lines 129–135 the coefficient 2 comes from the positive remaining mass; no unjustified weak-to-TV inference. The proof of 13.28.24 uses a separate compactness argument at each obstacle, followed by the summable-tail estimate from 13.28.22. The ideal multiplier-input and model-envelope references are not independently certified; no analytic approximation or regularization proof reopened. Historical first visits unreconciled.
* Section 13.8, docs/sections/non-pluripolar-products--mass-comparison-and-projective-fibers/index.html, blob dd89e44c511fd6f6bdd164a09a77c1637c42b410: nonexcluded mathematical lines 7–211, 218–274. Lemma 13.8.1 (source F84147BD, permanent 663159428707) compact support of g_k on {tau >= -k/eps} and decreasing limit/Stokes signs are consistent; subtract the smooth Omega contribution only after using positivity. Lemma 13.8.2 (source 2D5BFAF8, permanent 984FFB015C24) projection onto the simplex, rank defect outside the full-dimensional cell, determinant approximation with locally bounded distributional second derivatives, and the change of variables in lines 135–153 are consistent: the vertical factor dx_i wedge d alpha_i/(2 pi) has integral one in angle; the simplex t-density t^(N-1)/(N-1)! cancels the N! to N. The locally bounded v passage uses a common compact vertical support over each compact base test, not arbitrary nonproper pushforward continuity. Proposition 13.8.5 (source CCE5A11D, permanent A00B4940B406) uses local truncation and non-pluripolarity of the omitted polar set; the existence proof of the smooth-off-poles reference at line 212 invokes 6.17.1 and remains deferred-by-user. Theorem 13.8.7 (source 6A80B686, permanent 60DE4F681F75) is conditional on that existence and the stated product inputs; the beta concentration and epsilon-polynomial limit are correct. Corollary 13.8.8 (source EDC7A6A4, permanent A8BA63307F6C) correctly extracts n!/(n-p)! for the mixed coefficient only after polynomial equality; in the ordered case use fixed singularity truncation plus lower semicontinuity, not coefficientwise comparison from a polynomial inequality. Corollary 13.8.9 (source DC306F8A, permanent 56037F3B58D7) passes from a.e. increase to extended capacity and uses mass comparison plus lower semicontinuity. The prior finite-N beta bias finding POME-NPP-PROJECTIVE-BETA-BERNSTEIN-BIAS-001 is unchanged, not relogged. No full-section count for this excluded-dependency section.
* Actual current contents: docs/index.html, blob 68e66f6b30cdaaee887dc3c91580cdd0a38d8801. All 747 section-number entries exactly match the 747 unique rows of SECTION_MATRIX.md. No historic first-visit count inferred.

Delta: one whole direct mathematical section; one selected nonexcluded section; one new classified conditional deduction; zero new confirmed printed errors, zero new demonstrated proof gaps, zero complete transitive proof-chain certifications. Demailly regularization and its dedicated Bergman/L2/OT/multiscale/positivity-loss programme remain deferred-by-user; no builds, software tests, CI, source edits, registry edits, permanent tag changes or publication.
