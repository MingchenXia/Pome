# Mixed absolutely continuous variational cofinality in every degree
2026-11-26. Reviewed production main `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Finding POME-MIXED-AC-VARIATIONAL-COFINALITY-001

Severity low; **verified conditional deduction**, not a false printed statement or a complete upstream proof certificate. This extends the diagonal variational formula in Corollary 13.31.4 and the finite-test numerical cofinality of Theorem 13.32.3 to mixed absolutely continuous wedges of every degree. The earlier POME-NPP-MIXED-AC-WEDGE-ORDER-001 (2026-11-10) supplied the upper inequality; it is not counted again. No approximation theorem is reproved here.

**Anchors (current integrated HTML, physical line numbers):**
- `docs/sections/absolutely-continuous-and-non-pluripolar-mass/index.html`, blob `bea17d8041a7af4a252913e0f700b44d77521f82`, Lemma 13.31.1 source 6D2B462A/permanent C7894CAD8593, lines 8–98; Corollaries 13.31.3 source A2E98A80/permanent 1E1CF458220D, lines 104–120, and 13.31.4 source AA4B08E5/permanent 04768594F11F, lines 125–136.
- `docs/sections/numerical-positive-products/index.html`, blob `60abb2fa549c5fc76d759af419f863fedace7cfd`, Lemma 13.32.2 source 314E95A0/permanent 85B840A3A734, lines 31–42; Theorem 13.32.3 source 320251B7/permanent AD36F0CA2A0B, statement lines 47–55 only, nonexcluded exceptional correction at lines 69–71; Proposition 13.32.5 source 49C0DE98/permanent 37818757E0D6, lines 86–100; Proposition 13.32.6 source 30448720/permanent B28D656FB542, lines 105–126.

### Statement

Let X be a connected compact Kähler manifold of dimension n, with big classes alpha_1,...,alpha_r. Let T_i,min be closed positive currents with minimal singularities in their respective classes. Fix any finite family of smooth Kähler forms beta_1,...,beta_s on X. For any 1<=p<=n and index tuples I=(i_1,...,i_p), J=(j_1,...,j_{n-p}), with repetitions permitted, write

    M(I,J) = integral_X <T_i1,min ... T_ip,min> wedge beta_j1 ... beta_j(n-p).

Then

    M(I,J) = sup integral_X (T_i1)_ac wedge ... wedge (T_ip)_ac wedge beta_j1 ... beta_j(n-p),

where the supremum is over closed positive currents T_i in alpha_i, with a single current used for each repeated index. Moreover, a *single sequence* of tuples T_i,k attains all these suprema in the limit simultaneously. For these tuples the pointwise ac mixed wedges, interpreted as locally integrable currents, are themselves closed positive currents. This is not an assertion that ac wedges of arbitrary positive currents are closed, nor that the supremum is attained by a fixed tuple.

### Proof

Upper bound. The already recorded mixed ac wedge order (POME-NPP-MIXED-AC-WEDGE-ORDER-001) gives the current inequality between the ac wedge and its non-pluripolar counterpart. Pair with the indicated smooth positive product and apply the minimal-singularity mixed-mass bound, with the remaining factors the smooth Kähler forms. This proves the bound for every tuple, also when indices repeat. No polarization of a diagonal inequality is used.

Lower bound. Use only the *statement* of Theorem 13.32.3 for the finite list of big classes consisting of the alpha_i and the Kähler classes [beta_j]. On a common modification pi_k:Y_k -> X it provides Kähler representatives kappa_i,k and lambda_j,k with effective rational divisors E_i,k and F_j,k and exact class identities

    pi_k^* alpha_i = [kappa_i,k]+[E_i,k],
    pi_k^* [beta_j] = [lambda_j,k]+[F_j,k].

All top mixed products of kappa and lambda converge to their corresponding minimal-current mixed masses. In particular the product for I,J converges to M(I,J). Define T_i,k=(pi_k)_*(kappa_i,k+[E_i,k]); these are closed positive in alpha_i.

On the complement of the images of the exceptional locus and all E_i,k, the map is an isomorphism and the ac tensor of T_i,k is the transported smooth kappa_i,k. The excluded sets are proper analytic sets of Lebesgue measure zero (properness and the analytic-image theorem, already used in the printed comparison; their preimages are proper analytic as well). Thus by change of variables

    integral_X (T_i1,k)_ac ... (T_ip,k)_ac beta_J
      = integral_Yk kappa_i1,k ... kappa_ip,k pi_k^*beta_J.

The equality also holds as currents without the beta factors: the right-hand pushforward of the smooth mixed wedge has coefficient measures that give the excluded set zero mass. Indeed its trace measure against a fixed positive smooth complementary power on X is the pushforward of the smooth nonnegative measure obtained by wedging with the pulled-back complementary power; the preimage of the excluded set has zero measure. Positivity bounds all coefficient measures by the trace. Off the excluded set the ac density is the smooth transported wedge, so the pushforward equals the locally integrable ac wedge everywhere, and is closed. This proves the additional assertion about the selected tuples.

On Y_k, replace the lambda factors in the top mixed intersection, one at a time, by pi_k^*beta. The difference at each step is the intersection of [F_j,k] with the remaining closed smooth semipositive factors (kappa, lambda and pulled-back beta). By Stokes/cohomological invariance this is integration of their wedge on the effective divisor, with multiplicities, hence nonnegative. In particular

    integral_Yk kappa_I lambda_J
      <= integral_Yk kappa_I pi_k^*beta_J
      <= M(I,J),

where the last inequality is the upper bound applied to T_i,k. Squeezing proves the claim simultaneously for all tuples; the list is finite and the printed theorem already chooses one common model sequence. This works also for p=n (empty test list), p=1, and n=1. No sign-changing test is used for a monotonicity inequality.

### Further finite-dimensional consequence

For each p let V_p be the real span, in H^{n-p,n-p}(X,R), of products of n-p Kähler classes (the empty product means 1). It is finite dimensional. Choose finitely many such products forming a basis and include all their Kähler factors in the preceding list, for each p. Then the same model sequence gives convergence of the cohomological pairings on V_p uniformly on every bounded subset of V_p, because convergence on a finite basis implies convergence in the dual norm. Here the ac products are closed by the preceding argument, and minimal non-pluripolar products are closed by the printed NPP calculus. This does not assert that V_p is the entire complementary Hodge group in arbitrary intermediate degree, nor convergence of actual current representatives against arbitrary nonclosed tests. In degree n-1, V_p=H^{1,1}(X,R) by the Kähler cone spanning argument in Proposition 13.32.5. No equality of variational suprema for arbitrary boundary pseudo-effective tuples is claimed.

### Dependency and recommendation

Add the statement as a proposed corollary of 13.31.1/13.32.3, cross-reference 13.32.5. Its numerical use is in positive products and mixed variational mass comparisons. The same-class existence assertion, gentle approximation and its strictness machinery remain deferred-by-user and are used only as a black-box hypothesis, not verified, repaired or reopened here. The local radial convolution in the earlier ac dominance proof is ordinary local Bedford–Taylor calculus, not Demailly regularization. The mixed-mass bound and the proper-image theorem remain conditional upstream inputs. No full dependency chain certified.

## Coverage

- 13.31: direct read of the entire integrated mathematical text, physical lines 8–136, including the measure maximal estimate and the cutoff argument for singular measures, matrix density monotonicity, Fatou, and the two determinant-volume corollaries. The lower bound is conditional on the same-class theorem. Earlier mixed ac order and degree-one defect findings retained, not recounted. No new printed error identified.
- 13.32: selected nonexcluded mathematical review only: lines 31–42, 47–55 (statement), 69–71 (finite intersection correction), 77–126 (definition, numerical cofinality, order and boundary continuity). Exceptional correction uses t>0 and t<=min delta_i; pulled-back omega may be degenerate, but t gamma is strictly positive. Each polynomial is controlled for a fixed model, no uniform constants over models required. The pairing squeeze in 13.32.6 uses finite-dimensional form comparison and pseudo-effective order, and the boundary claim is only for decreasing perturbations. Lines 11–26 and the regularization-dependent construction at 60–69 are not audited or certified. This is not a whole-section review.
- 16.8: selected lines 7–188 of `docs/sections/comparison-of-singularities--the-p-and-mathcal-i-preorders/index.html` (blob 99e301ceb84460dc9bfeff03280d517dc8890ea5): positive-mass background independence and polynomial continuation to zero perturbation in Lemma 16.8.4 (A3C93A5CDBF4), mixed-mass equivalence in Proposition 16.8.7 (C7C64ABB4647). The use of a positive Kähler perturbation is essential when original mass is zero. Conditional on envelope mass preservation and positive-mass characterization, not a review of the entire preorder section or the excluded regularization dependencies.
- 24.4: selected exposition lines 7–87 of `docs/sections/problems-in-hermitian-pluripotential-theory--closed-positivity-and-geometric-equations/index.html` (blob 38793fe10e89d1e4aebe46d639f48211285007d9). Closed nef versus nonclosed strictly positive backgrounds, bounded mass distinction and endpoint problem 24.4.6 (81116FD94515) read; open problems remain open. No claim about the remainder of the section or cited geometric theorems.
- Current ToC: 747 section locators in docs/index.html, 747 unique matrix rows, no missing locator (exact set comparison). Historical first visits remain unreconciled. No builds, tests, CI, publication, main/source/registry/tag changes; no new confirmed errors or proof gaps and zero complete upstream certifications. All excluded programmes remain deferred-by-user.
