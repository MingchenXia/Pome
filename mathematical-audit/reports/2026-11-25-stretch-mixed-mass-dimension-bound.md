# Dimension-sensitive stretching and a lower-volume chord bound

Date: 2026-11-25. Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit-only; no source, registry, tag or production edits.

## Scope and immutable anchors

- docs/sections/volumes-under-bounded-mass/index.html, blob 94d79bfca61602054b9d09b79a76306e11a67d79, mathematical introduction lines 8–26: connected compact complex X, n>=1, bounded mass property, big smooth real theta (not necessarily closed); definitions of ordinary singularity volumes, envelopes and model types. This introduction was read in full.
- docs/sections/volumes-under-bounded-mass--strict-barriers-and-background-variation/index.html, blob 2fb8697ad0f1e916245d9adafde27f40f97b46f3, Lemma 13.20.1 (source tag 1DBB631B, permanent EDD01F5B65E5), lines 11–72; Corollary 13.20.3 (40A9BCB2 / D51B82B18D30), lines 77–93; Proposition 13.20.4 (DE77A39F / 0729BE10D92E), lines 98–111; model comparison paragraph 115–128; Proposition 13.20.6 (95AB9149 / F4C607C7C503), lines 135–169. Direct read of the entire mathematical section, including previously recorded local gap POME-VOL-BG-ZERO-TEST-001 (not a new finding). The claim of individual positivity in lines 122–128 invokes 16.28.69; its upstream proof was not checked in this run.
- docs/sections/volumes-under-bounded-mass--comparison-of-singularity-volumes/index.html, blob 7d55ffb2d7cb91897029a9a2101788eb8aa70141, lines 20–78: selected dependency check of Theorem 13.17.1 (D7019DA65027) and Proposition 13.17.2 (1C00C4C5A656), already directly reviewed earlier; no fresh full coverage claim.
- docs/sections/volumes-under-bounded-mass--model-comparison-under-background-changes/index.html, blob 9031cedd29e8ed20dc720a8119d326ff727a2113: Proposition 13.25.1 (61209D2B61BD) lines 11–40, fixed parameters at 44–50, Proposition 13.25.2 (F274299A5A71) lines 54–70, Corollary 13.25.3 (1ED63BC3072B) lines 75–100. Nonexcluded selected direct review.
- docs/sections/volumes-under-bounded-mass--two-sided-background-perturbations/index.html, blob 45c385fe6dc2c7a8b877b27e3bf854da9c4ac463: Lemma 13.26.1 (D5C96B9222A4), lines 14–32; Theorem 13.26.3 (218C2CE831D1), lines 36–91. Nonexcluded selected direct review. The analytic choice of strict rho in 13.25 line 44 is conditional; the regularization-based existence/approximation programme, including the analytic approximation criteria 13.25.5 and 13.26.7, is not audited here. Retain deferred-by-user.

## POME-STRETCH-MIXED-MASS-DIMENSION-BOUND-001

Severity low; verified conditional deduction, not a printed theorem error. The printed small-stretch coefficient is sufficient. Its exponential dependence on n can be replaced by a linear one, using the same mixed mass input. No optimality claim for the geometric coefficient.

Use the assumptions and notation of Lemma 13.20.1. Write m=lower vol_theta(u)>0, K=v_+(Omega)<infinity and define

    C_1=1, C_n=n(1-1/n)^(-(n-1)) for n>=2.

Then for every 0<=a<=m/(2 C_n K), the family A_(1+a)(u,r) is nonempty. In fact it is nonempty for every 0<=a<m/(C_n K). For n>=2, C_n<=en, by log(1+x)<=x. Thus the uniformly admissible stretch can be chosen with denominator 2 C_n K instead of 2^(n+1)n K.

Proof. For s,t theta-psh, put

    B_i = binom(n,i) int_X (theta+dd^c s)^(n-i) wedge (theta+dd^c t)^i.

Products are the positive non-pluripolar mixed products. For 0<lambda<1, positivity under increasing the smooth background, multilinearity and the bounded mass estimate for Omega-psh potentials give

    sum_(i=0)^n (1-lambda)^(n-i) lambda^i B_i
      = int_X MA_theta((1-lambda)s+lambda t)
      <= K.

Equivalently one can use the inequality obtained by domination in Omega. The non-pluripolar polynomial identity follows by restricting to the common finite locus (the mixed measures give no mass to the union of the pole sets). This uses the same inputs as lines 45–51 of the printed proof, in particular 13.14.2–3 and 13.14.16; no excluded approximation is invoked.

For n>=2 choose lambda=1/n. If 0<=a<=lambda/(1-lambda)=1/(n-1), for every i>=1,

    a^i / [(1-lambda)^(n-i)lambda^i]
      <= a / [(1-lambda)^(n-1)lambda] = C_n a.

Multiplying the previous nonnegative sum by C_n a gives a simultaneous bound on all positive-degree terms, not n separate bounds:

    sum_(i=1)^n a^i B_i <= C_n K a.

For n=1 the corresponding assertion is just a B_1<=aK, directly by the mass bound. Since m<=K, a<m/(C_n K) implies the required range a<=1/(n-1) when n>=2.

Now repeat only the nonexcluded contact argument of lines 24–42: if the family for b=1+a is empty, the decreasing truncation envelopes q_j tend uniformly in supremum to -infinity. The contact theorem then bounds m by the integral of (T_u+a T_(u_j))^n over {u<=-k}, for each k and sufficiently large j. The constant term is bounded by MA_theta(u)({u<=-k}); the remaining terms by C_n K a, independently of j and k. The constant term tends to zero because the measure is finite and gives no mass to the pole set. Thus m<=C_n K a, contradicting the strict inequality. At a=0, u is the competitor. This proves the claimed interval including its half-margin endpoint. We do not assert existence at a=m/(C_n K).

With a_*=m/(2 C_n K) and H=Q_(1+a_*)(u,r), convex interpolation gives for 0<=a<=a_*

    (1-a/a_*)u+(a/a_*)H <= Q_(1+a)(u,r) <= u.

The printed volume addition, homogeneity and order inequalities therefore give, for either singularity volume (not only the upper volume),

    (1-a/a_*)^n vol_theta(u) <= vol_theta(Q_(1+a)(u,r))
      <= vol_theta(u).

The lower-volume version follows by applying precisely the same order/addition argument to the lower volume. In particular both volumes converge as a decreases to zero; this scalar estimate works along arbitrary nets of admissible a tending to zero.

For a uniform lower-volume threshold delta>0, if the class is nonempty then delta<=K. Replace the b_delta at 13.25 lines 44–50 by 1+delta/(2 C_n K). Given the existing strict rho with margin kappa, the proof of 13.25.2 yields the improved uniform margin

    kappa_delta = kappa delta/(2 C_n K+delta).

The correction w=b_delta^(-1)H+(1-b_delta^(-1))rho still satisfies w<=u after the common normalization. This improves the quantitative factors of 13.25.2–3 and 13.26.1/.3 without changing their hypotheses. The strict analytic rho existence premise stays deferred; the estimates conditional on a supplied strict potential do not need analyticity. No claim of sharpness, no claim of a new existence theorem for strict analytic potentials.

## POME-LOWER-VOLUME-BACKGROUND-CHORD-001

Severity low / verified conditional deduction; original Proposition 13.20.6 not disproved. Independent improvement of the linear bound at lines 148–160, which also avoids the already recorded zero-test prerequisite issue.

Choose a Hermitian Omega >= theta+omega and let K=v_+(Omega). For v theta-psh, set F_v(t)=int_X MA_(theta+t omega)(v), t in [0,1]. By non-pluripolar mixed expansion F_v(t)=sum_(i=0)^n A_i t^i with A_i>=0; the pure smooth term does not charge the pole locus. In particular F_v(0)=int MA_theta(v), F_v(1)<=K. Hence for 0<=epsilon<=1,

    0<= F_v(epsilon)-F_v(0) <= epsilon(F_v(1)-F_v(0))
       <= epsilon(K-F_v(0)).

For theta<=eta<=theta+epsilon omega, each v in the ordinary theta-singularity type of u is an admissible eta-competitor; its eta mass is bounded above by F_v(epsilon). Taking the infimum of the resulting inequality (the factor 1-epsilon is nonnegative) and applying background monotonicity of 13.17.1 gives

    0 <= lower vol_eta(u)-lower vol_theta(u)
      <= epsilon (K-lower vol_theta(u)).

This holds even at zero lower volume and requires no strict potential for the particular u. This is not a claim about upper volume, since its new competitor family can be larger. The uniform coefficient on the full interval cannot be reduced below K-lower vol_theta(u) in general: on projective space with a fixed Kähler omega, theta=c omega (c>0), u=0, eta=theta+omega at epsilon=1, and Omega=theta+omega, the closed-background total-mass identity gives equality. It gives equality for every epsilon when n=1. No assertion of sharp infinitesimal slope for n>1.

## Additional dependency simplification and review notes

For Proposition 13.25.1 one can avoid the cited gauge-type comparison 18.5.1 in the ordinary-model part. If p=P_theta[p] and theta'=theta+dd^c f, then p-f+inf_X f is an admissible nonpositive competitor for P_theta'[p-f]. For any other competitor w, w+f-sup_X f is a nonpositive theta-psh competitor for P_theta[p]. Thus

    p-f+inf_X f <= P_theta'[p-f] <= p-f+sup_X f.

USC regularization preserves the upper bound because the right side is USC. The same sandwich works with the ideal relation if p is an ideal model, since addition of a bounded smooth function does not change multiplier ideals. The curvature identity and max identity at lines 25–28 then give the original conclusions, using the printed ordinary-model/idempotence inputs. This is a local dependency simplification, not an upstream certificate.

13.20.3–4: normalization and strict-current margin check, including t<delta/C. 13.20.6 second part: addition in background eta+t(theta-delta omega), which is big since the strict current from (1+t)w is >=delta omega; then order comparison to (1+t)theta and exact homogeneity. 13.25.2–3: uniform margin and three-error bound |2e_m-e_u-e_v|<=2M for each e in [0,M]; projection invariance conditional. 13.26.1/.3: verified the nonexcluded form inequalities (c>=1/2), maximum sandwich, and comparison of two transport choices; convergence uses 13.21.4 and 5.29.19 as printed, not newly proved. Analytic choice and approximation results excluded as noted above. No new confirmed false theorem or newly demonstrated proof gap; no re-count of POME-VOL-BG-ZERO-TEST-001. Dependencies include contact theorem 15.8.6, ordered contact 13.14.6, volume monotonicity and addition 13.17.1–2, projection invariance 13.19.5/13.22.4, bounded mass and non-pluripolar multilinearity. Complete transitive verification not asserted.

Actual coverage: whole current §13.16 introduction, direct whole §13.20 mathematical text with the stated conditional inputs, selected nonexcluded §§13.25–26, selected dependency recheck §13.17. Historical first visits unreconciled. No builds/tests/CI, no production changes.
