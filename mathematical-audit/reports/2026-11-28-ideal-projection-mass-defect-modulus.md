# Ideal projection: a quantitative modulus from ordinary mass defects

Date: 2026-11-28. Reviewed main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
Finding **POME-KAHLER-IDEAL-PROJECTION-MASS-DEFECT-MODULUS-001** — low / verified conditional deduction, optional extension, not a false printed theorem.

## Exact anchors and coverage

* `docs/sections/the-envelope-operators--multiplier-ideal-envelopes/index.html`, blob `e37e0c4f6273acf41ee2e6d46d99ee5018bf78d5`: direct nonexcluded lines 7–405 and 430–608; 406–427 (Bergman quasi-equisingular argument) deferred-by-user, not certified. Props 16.6.29 (permanent 2D7AF550FFF7, source sgpt:66C7014F), 16.6.30 (0C703BE43035, sgpt:234A6979), 518–599; 16.6.27 (F7C47263CB3C, sgpt:DD837F85), 436–492; 16.6.28 (2A3BCF353C03, sgpt:618F7858), 497–513; 16.6.11 (363E28FF4A61, sgpt:898F78D9), 213–247.
* `docs/sections/non-pluripolar-products--properties-of-non-pluripolar-products/index.html`, blob `4ace6181d3767e6d5ac3a681c36e392e33b717a2`: selected lines 7–165, 578–626 (Lemma 13.13.30 statement and competitor convention, permanent 1CC7CDBE65A9, sgpt:8560C5E9). Its full proof and upstream chain not certified here.
* `docs/sections/volumes-under-bounded-mass--volumes-of-multiplier-ideal-envelopes/index.html`, blob `0b4c115fa8ffbe1cdfa4fcac49875a76fa44fffc`: selected nonexcluded 45–70, 140–174 (converse direction only), 176–329 (countable divisorial profiles, residual trace, surface example). Proposition 13.24.2 (71B65CF5AD10, F0A00405), Theorem 13.24.5 (8BB867A0263F, 42C40148), Lemma 13.24.7 (487BF774470F, F763B26D), Proposition 13.24.8 (20027E32C14E, A0F87E92). Approximation results 13.24.1/.3 and forward implication of 13.24.5 depending on .3 are deferred-by-user in this audit; no proof-completion work on them.
* Global convention checked: connected compact X, n>=1. Chapter 16 current table of contents has 44 sections, exactly matching existing matrix rows; total matrix 747 distinct section identifiers. Historical first-visit status remains unreconciled.

## Ordered estimate

Work on a connected compact Kähler manifold of dimension n>=1, with fixed closed smooth real (1,1)-form theta. Let m(u) be the total non-pluripolar top mass, and Q(u)=P_theta[u]_I. Fix a smooth positive volume form dV. Use the printed extrapolation Lemma 13.13.30, order and convexity of Q (16.6.27–28), ideal-envelope membership (16.6.11), normalized L1 compactness (5.17.3), and closed non-pluripolar mass monotonicity (13.13.11) and positive multilinearity as inputs. These are not newly certified transitive results; strong openness and valuative inputs are recorded dependencies, not reopened.

For u ≼ v and 0<m(u)≤m(v)=M, set r=((M-m(u))/M)^(1/n). Then

    ||Q(v)-Q(u)||_1 ≤ C_theta r,
    m(Q(u)) ≥ (1-r)^n m(Q(v)).

Here C_theta is any common bound on the L1 norm of normalized theta-psh functions, independent of the two potentials. The order convention is that u ≼ v means u≤v+constant. No model-potential assumption on u or v is needed.

Proof: choose any s in (r,1). Lemma 13.13.30 applied with a=1/s gives an admissible eta with (1-s)v+s eta≤u; alternatively shift u by a constant before using the lemma, which does not affect Q or mass. Convexity and order of Q, with the scaling identity for positive scalar multiples of the background, yield

    (1-s)Q(v)+s Q(eta) ≤ Q(u) ≤ Q(v) ≤ 0.

The envelopes are normalized with sup zero (a normalized competitor exists and Q≤0); hence away from the common negligible pole sets,

    0 ≤ Q(v)-Q(u) ≤ s(Q(v)-Q(eta)) ≤ -s Q(eta).

Integrating gives the stated bound with s in place of r. Positive multilinearity of non-pluripolar products gives mass of the convex combination at least (1-s)^n m(Q(v)), and monotonicity gives the same lower bound for m(Q(u)). Send the real parameter s down to r in the numerical inequalities only. This includes equal mass r=0 without assuming a limiting eta exists; equality of Q follows from L1 equality and canonical psh representatives. No subtraction of infinite values is used in the competitor inequalities.

## Unordered estimate

Let u,v have positive mass, w=max(u,v), M=m(w), and define the nonnegative ordinary top-mass defect D=2M-m(u)-m(v). This notation is local to this note and is not an identification with a mixed-mass metric elsewhere in Pome. Put r_u=((M-m(u))/M)^(1/n), r_v analogously. The ordered estimate applied twice and the triangle inequality give

    ||Q(u)-Q(v)||_1 ≤ C_theta (r_u+r_v)
                   ≤ 2^(1-1/n) C_theta (D/M)^(1/n).

Thus a uniform positive lower mass bound delta gives a uniform Hölder modulus with D/delta, even for arbitrary directed nets with D tending to zero; no sequential compactness or cofinal sequence is required.

Likewise, by monotonicity Q(w)≥max(Q(u),Q(v)). From the ordered mass bound, and 1-(1-r)^n≤nr for r∈[0,1],

    0 ≤ D_Q := 2m(max(Q(u),Q(v)))-m(Q(u))-m(Q(v))
      ≤ n m(Q(w))(r_u+r_v)
      ≤ n m(V_theta) 2^(1-1/n) (D/M)^(1/n).

Here V_theta is the normalized minimal-singularity potential (13.13.7). This is a bound on the same top-mass defect after projection, not an assertion of an optimal exponent or of a stronger metric estimate. It is not a claim of continuity in ambient L1 alone. The proofs require neither regularization nor any new mixed-mass inequality beyond positivity and multilinearity.

## Direct audit observations

* 16.6.9: the actual competitor transport gives min(g)≤Q_{theta+ddc g}(u-g)+g-Q_theta(u)≤max(g) a.e.; interpret via inequalities of potentials at common poles. 16.6.10: descent is a bijection of admissible families; one can use 16.6.11 to ensure Q itself is a competitor, avoiding an unproved pointwise exchange of pullback and usc supremum at exceptional points. The statement is not refuted.
* 16.6.17 (lines 291–321): its stated bigness conclusions can be made explicit using 13.13.3 and 13.13.4: the pullback or pushforward of a minimal current of the original big class has the same strictly positive top mass; apply 13.13.3 in the target Kähler manifold, then mass monotonicity gives the printed volume comparison. No need to assume the pulled-back class is big before applying that criterion. This is a conditional clarification, not a new proof of the positive-mass bigness criterion (quoted BEGZ10 in 13.13.3).
* 16.6.29–30: the two printed monotone-net arguments use the correct decreasing numerical errors; the normalized L1 bound controls all indices and the a.e. order extends canonically. The new two-point estimate gives a common quantitative version of their key step. It does not replace their separate mass-continuity inputs, nor prove 16.6.31's speculative interpolation claims.
* 13.24.2: positivity of the ideal model is essential for the stated relative-class equivalence; the counterexample at 13.24.11's following paragraph is retained. 13.24.5 converse: s_j is selected with defect <delta s_j^n, yielding a common positive lower volume via the convex competitor, before invoking L1 convergence. No invocation of the deferred approximation direction is needed.
* 13.24.7–10: the log integral uses the Beta(1,2) density, giving -3/2. On each fixed modification the positive tail trace bound involves its own finite constant; no uniformity over all modifications or interchange of those quantifiers is needed. In 13.24.8, after removing S the residual has bounded local potentials, hence charges no pluripolar set in degree one. The top mass computation uses finite truncations and the closed mass comparison before expanding the smooth correction L=Ckappa-theta. Since dd^c L=0 in dimension two, the dd^c h term in the integrated residual trace against L vanishes by Stokes, leaving (C-A) times the integral of L wedge kappa; the entire trace correction need not vanish. The explicit nonclosed perturbation is real and pluriclosed; three distinct hyperplane coefficient vectors are independent by Vandermonde. The printed statements are conditional on their cited valuative and non-pluripolar results; none of these dependencies is newly certified here.

Affected dependents: 16.6.29–30 can optionally cite the quantitative estimate; the closed-case estimates may inform 13.24.5 but are not claimed for arbitrary nonclosed backgrounds. No source correction is required. No confirmed new theorem error, no newly demonstrated proof gap, no full transitive proof certificate. Selected direct coverage of three sections; the exclusion is maintained at proof level, not declared resolved. No builds, software tests, CI, publication, or source/registry edits.
