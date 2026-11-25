# Joint background, density and boundary stability for local Dirichlet replacement

Date: 2026-11-25. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit parent: 89c3b351bb3ed3c8785f24096c93ff8a09ffa110.

## Finding POME-HOM-DIRICHLET-NONCLOSED-JOINT-STABILITY-001

Severity low; verified conditional deduction, not a false printed theorem. The prior external existence input POME-HOM-DIRICHLET-SMOOTH-EXT-001 remains open. The earlier POME-BT-BALL-DIRICHLET-SHARP-ROOT-STABILITY-001 (2026-11-04, §7.9.3, fixed closed background) is not recounted. The new ingredient is the simultaneous signed background perturbation estimate for arbitrary smooth, possibly nonclosed forms, including the homogeneous replacement used in §15.8.

Exact source: docs/sections/equations-with-prescribed-singularities--homogeneous-replacement-on-a-coordinate-ball/index.html, blob a9db59d6db0717cd2da92f3c0120b494fa4f731e. Lemma 15.7.1 (source tag 6A868117, permanent 5C54B7FA3A8B, lines 14–28); Theorem 15.7.2 (source tag 95D653E5, permanent B0FDBEE3B071, lines 32–92). In particular, Step 3 (line 75) proves uniform convergence without an explicit density rate, and lines 36–38 give fixed-background boundary contraction.

### Statement and proof

Write B=B_R in C^n, beta=dd^c|z|², q(z)=|z|²-R². Let u,v be the smooth strictly admissible Dirichlet solutions in Lemma 15.7.1 for data (theta,F,phi) and (eta,G,psi), respectively. The forms theta and eta need not be closed. Define the real numbers

    b = max over z of lambda_max_beta(eta(z)-theta(z)),
    r = max over z of (F(z)^(1/n)-G(z)^(1/n)),
    d = max over boundary of (psi-phi),
    L = max(0,b)+max(0,r).

Then

    v(z)-u(z) <= d + L(R²-|z|²).

In fact the sharper signed-background version holds with L=b+max(0,r), which is allowed to be negative. Indeed theta-eta+b beta >= 0, and for w=v+Lq-d,

    theta+dd^c w >= eta+dd^c v + max(0,r) beta > 0.

For a positive matrix A and t>=0, relative to beta, (det(A+tI))^(1/n) >= (det A)^(1/n)+t. Diagonalize and expand the product; the mean of the k-fold eigenvalue products is at least their geometric mean, (det A)^(k/n), by AM–GM (each eigenvalue appears equally often). Summing the binomial expansion gives the assertion. Thus the density of w is >=F, and its boundary value is psi-d<=phi. The printed smooth comparison at line 28 gives w<=u, proving the estimate. No integration by parts or closedness enters.

Interchanging the two data sets gives the reverse one-sided estimate. In particular, if -c beta<=eta-theta<=c beta and c>=0,

    |v(z)-u(z)| <= ||psi-phi||_infty
       + (c+||F^(1/n)-G^(1/n)||_infty)(R²-|z|²).

The signed estimate is stronger than this symmetric bound: in the homogeneous case, if eta<=theta, the replacement for eta lies below that for theta with the same boundary data.

### Continuous boundary values and the zero-density endpoint

For smooth positive F,G, the existing smooth comparison with constant shifts yields boundary contraction even for arbitrary variable F,G separately fixed. Approximate continuous boundary values uniformly by smooth functions. The resulting solutions converge uniformly on the closed ball, by contraction, and their bounded products converge by a common smooth correction and finite expansion (the same internal input as 15.7.2 Step 3); positivity passes to the limit. The estimates survive this limit, and do not assert smoothness. For the homogeneous endpoint use precisely the increasing constant-density construction of Theorem 15.7.2. Apply the smooth estimate first with positive constant densities tending to zero, then pass to uniform limits. In particular for the same background and boundary data,

    0 <= H_phi(z)-v_epsilon,phi(z)
       <= epsilon^(1/n)(R²-|z|²),   0<epsilon<=1.

More generally, for a smooth positive F, compare with a constant delta>0 and pass delta down to zero to get 0<=H_phi-v_F,phi<=(sup F)^(1/n)(R²-|z|²); monotonicity for delta <= min F gives the lower bound. The result for continuous phi follows by the preceding uniform approximation. For two homogeneous replacements the signed estimate applies with r=0.

For a constant background shift eta=theta+c beta, c real, the equality H_eta,phi=H_theta,phi-cq follows directly from the maximality characterization at line 92: adding cq is an order-preserving bijection of the admissible competitors with identical boundary data. Thus the background coefficient is exactly sharp, not just an upper bound, and this identity works for nonclosed theta as well. For theta=0 and phi=0, v_epsilon=epsilon^(1/n)q and H=0 by smooth uniqueness and homogeneous maximality. This saturates the density bound pointwise, including at the center, and excludes any universal better power of epsilon near zero. To saturate all three nonnegative contributions simultaneously, take theta=0, eta=c beta, F=s^n, G=t^n, s>=t>0, phi=0, psi=d constant with c,d>=0. Then u=sq, v=(t-c)q+d and v-u=d+(c+s-t)(R²-|z|²). Each coefficient 1 is optimal.

Proposed correction: none required for the printed theorem. Add the one-sided estimate after Theorem 15.7.2 as an optional quantitative strengthening. The affected direct consumer is Theorem 15.8.1 (permanent F6FD255985FF), which uses homogeneous replacement in its contact-support step. Its conclusion does not need to change. This audit does not replace or certify the Guan–Li existence theorem for nonclosed backgrounds (the existing external-dependency finding remains open).

## Coverage and dependency checks

* §15.7 complete current mathematical lines 7–92. Strict subsolution construction, positive matrix log-determinant linearization, comparison sign, boundary barriers, translation correction and uniform Lipschitz estimate, direction of the epsilon monotone limit, uniform approximation of continuous boundary data, and strict upper-test comparison were checked. The smooth Guan–Li existence input in line 23 remains external; local product continuity and upper-test characterization are treated as internal premises, not transitively certified. This is a complete direct conditional reading, not a new historical first-visit claim.
* §15.8 selected ONLY lines 95–107, docs/sections/equations-with-prescribed-singularities--contact-support-in-a-big-background/index.html, blob 39893363c8507e9ff37e42f4d6ec69c7abacaf70. Conditional on the previously established continuity and strict barrier premise: the Laplacian lower bound for H gives the stated upper comparison against the quadratic barrier with C' chosen so Delta(H-barrier)>=0; the boundary collar for max(p,H-a) follows by continuity on the compact boundary and equal trace. The limit is locally uniform across the boundary since H>=p and the difference from the pasted function is <=a. Then maximality forces equality. The contact conclusion uses the local bounded product and noncharging of Z. Lines 7–93 (analytic barrier and regularization continuity) were not audited; their excluded programme remains deferred-by-user. No whole-section certificate.
* §13.13 selected lines 89–165, docs/sections/non-pluripolar-products--properties-of-non-pluripolar-products/index.html, blob 4ace6181d3767e6d5ac3a681c36e392e33b717a2. Theorem 13.13.9 (B3DC3180FF35, source 65F7AFC0), Theorem 13.13.11 (0E5F6133B048, source 00CC32E0), Corollary 13.13.12 (37623491DEDC, source CDCC4217). The common countable Choquet family across finitely many j and the directed finite upper bounds justify the mass-net argument; no cofinal sequence is assumed. The sequence of finite maxima has the correct almost-everywhere limit by the envelope property, so the cited sequential semicontinuity theorem applies. The cited DDNL results remain conditional premises. No new claim beyond the existing net audits, and no full-section certification.
* §16.3 selected lines 14–75 and 109–159, docs/sections/the-envelope-operators--p-envelopes--rooftop-operator-and-the-definition-of-the-p-envelope/index.html, blob 97681f31628eb362950837daaadde67d10507a2f. The rooftop greatest-lower-bound argument, contact estimate (with possible harmless overlap on the two contact sets), change-of-background by a smooth potential, and mixed-mass preservation by monotonicity and increasing limit were directly checked conditional on their cited premises. The rest is not counted as reviewed this run.

Matrix check against actual docs/chapters/index.html: 747 section locators in the TOC, 747 unique matrix locators, no missing or extra locators. Legacy statuses preserved. One whole direct conditional section, three selected, one new conditional deduction, zero new confirmed statement errors, zero new demonstrated proof gaps, zero complete transitive certifications. No build, tests, CI, main/source/registry/tags/site changes. All user-excluded programmes remain deferred-by-user, not resolved.
