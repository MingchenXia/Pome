# Modified-nef pushforward without the big-class reduction; divisorial mass bounds

Date: 2026-11-25. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.

## POME-MODIFIED-NEF-PUSHFORWARD-MULTIPLICITY-001

Severity low; verified conditional deduction and proposed alternative proof, NOT a false printed theorem. The argument uses the existing basic current and minimal-singularity inputs explicitly listed below. It neither invokes nor completes regularization.

Integrated file: docs/sections/plurisubharmonic-functions--the-space-of-currents/index.html (blob b197a4fa4c063c10f1a65cde5b09a34dddc8df86).
* Definition 5.19.15, sgpt-9B41C413, tag 4DFBEC43A4B0, physical lines 132–143.
* Definition 5.19.16, sgpt-CFCDBC6F, tag 0EB97717F408, lines 147–164.
* Proposition 5.19.17, sgpt-086C39B0, tag 191D96316EC3, lines 167–189; specifically clause 2, tag 98B07470D933.
* Lemma 5.19.18, sgpt-6AD0B91F, tag 9F062B47A2B4, lines 194–207.
* Divisorial decomposition 5.19.12–14, lines 103–125, tag F956E74CD8C5 (lemma), equation tag 6720366F8D5B and definition tag 5545837BA9C1.

All manifolds in this subsection are compact Kähler, as required by its opening line and the properness of the modification. Let pi:Y→X be a proper bimeromorphic morphism of smooth manifolds. Let gamma and omega be Kähler forms on Y and X. For every pseudo-effective class beta on Y and every prime divisor D on X, write D' for its strict transform. Then

    nu(pi_* beta,D) <= nu(beta,D').

Moreover, for any closed positive (1,1)-current T on Y,

    Reg(pi_*T) = pi_*(Reg T).

The first formula gives Proposition 5.19.17(2) directly on the boundary as well as in the big cone. There is even a proof directly from Definition 5.19.15, without any minimal-singularity current.

### Proof and dependency boundaries

Write alpha=pi_*beta and choose a smooth closed real (1,1)-representative eta of the class of pi_*gamma. This is available on the compact Kähler target. Choose C>0 with C omega-eta positive. For a closed positive current U on Y, the generic Lelong number along D of pi_*U equals that of U along D': the map is biholomorphic in a neighborhood of a general point of D. Generic Lelong numbers are unchanged by a smooth summand. These are the generic-divisor facts already used in Lemma 5.19.18 (with the modification and Siu inputs 9.10.5 and 5.16.7). The target class alpha is pseudo-effective by pushforward of a positive representative.

If beta is modified nef, for every epsilon>0 choose a closed current V_epsilon in beta with U_epsilon=V_epsilon+epsilon gamma positive and having zero generic Lelong number at every prime divisor of Y. Set

    W_epsilon=pi_*U_epsilon + epsilon(C omega-eta).

It is positive, closed, has class alpha+epsilon C[omega], and has zero generic Lelong number at every prime divisor on X, simultaneously. Thus W_epsilon-epsilon C omega is a representative of alpha satisfying Definition 5.19.15 for parameter epsilon C. This proves the printed proposition without reducing to big classes, without cone closure, and without regularizing any current. In particular the argument does not assert the false pointwise estimate pi_*gamma <= C omega; only its smooth cohomology representative is bounded.

For the general inequality, take U_epsilon with minimal singularities in the big class beta+epsilon[gamma]. The same construction W_epsilon gives a positive representative of alpha+epsilon C[omega]. A minimal-singularity current in that latter big class is less singular than W_epsilon. Hence

    nu(alpha+epsilon C[omega],D)
      <= nu(W_epsilon,D)
       = nu(U_epsilon,D')
       = nu(beta+epsilon[gamma],D').

Let epsilon decrease to zero, using Definition 5.19.16. Scaling the positive parameter by C does not change the limit. This proves the inequality, not an equality of class multiplicities.

For completeness, the compatibility asserted after Definition 5.19.16 can be checked without regularization. For a fixed pseudo-effective beta, the minimal multiplicities in beta+epsilon[gamma] increase as epsilon decreases, by adding a smooth positive form in the opposite direction; they are bounded above by the corresponding multiplicity of any fixed positive representative of beta. Independence of gamma follows by comparing two Kähler forms by positive constant multiples. If beta is big, take a Kähler current K in beta with K>=delta gamma for some delta>0. For a minimal current U_epsilon in beta+epsilon[gamma], put t=epsilon/(delta+epsilon). Then

    (1-t) U_epsilon + t K - (1-t) epsilon gamma

is positive in beta, since t delta=(1-t)epsilon. Its generic Lelong number is (1-t)nu(U_epsilon,D')+t nu(K,D'). Comparing with the minimal current in beta and letting epsilon tend to zero gives the missing reverse inequality with the boundary limit. These calculations use existence of minimal currents and a Kähler current in a big class, not their approximation by analytic singularities. They also justify the equivalence between vanishing of every class multiplicity and modified nefness: the minimum in each perturbed big class has all its generic divisorial Lelong numbers zero simultaneously if the boundary limits all vanish. Conversely the Definition 5.19.15 representatives imply those minimum values vanish at every positive parameter.

The decomposition identity follows by writing T=Reg T+sum_E a_E[E] as in 5.19.13. Proper pushforward commutes with the weak convergence of the series, since test forms pull back to smooth test forms on the compact source. If E is exceptional with image of complex codimension at least two, pi_*[E]=0: a test form of degree (n-1,n-1) restricts after pullback to zero on the smooth rank-deficient locus of E, which has full integration measure there. Otherwise pi_*[E]=[D] for the unique image prime divisor, because the map is generically one-to-one; lower-dimensional exceptional subsets have zero integration measure. Distinct nonexceptional divisors give distinct image divisors. Lemma 5.19.18 gives that pi_*Reg T is non-divisorial. Thus the displayed decomposition is exactly the divisorial decomposition on X, by uniqueness of generic coefficients.

The closed-convex cone assertion on line 143 also admits a direct proof. Fix a linear choice of smooth representatives for the finite-dimensional real (1,1)-cohomology. If modified-nef beta_j tends to beta, for each epsilon>0 take a j with its smooth difference representative tau of beta-beta_j satisfying tau>=-epsilon gamma/2. A Definition 5.19.15 representative for beta_j at epsilon/2, plus tau, then satisfies the same definition for beta at epsilon. The extra summand tau+epsilon gamma/2 is smooth positive, so all generic divisorial coefficients remain zero. Convexity follows by summing positive representatives with zero generic divisorial coefficients, and scaling follows by rescaling epsilon. Pseudo-effectivity follows by weak compactness of positive representatives in beta+epsilon[gamma], whose masses are bounded by their cohomological pairings with gamma^(n-1). This is not a new transitive proof of the basic current theory.

Proposed correction: optional insertion of the short W_epsilon proof after 5.19.17(2), and of the multiplicity inequality and decomposition identity as a separate corollary. No alteration to the printed statement, labels, or Boucksom attribution. Directly affected results are 5.19.15–18; further consumers of modified-nef pushforward inherit a shorter argument, not a newly certified upstream chain. The comparison with minimal currents relies on existence and the singularity-order/Lelong monotonicity dictionary; the decomposition calculation relies on 5.19.12–14 and 5.19.18. These inputs are not transitively certified. The analytic-singularity existence input of 5.19.10 (lines 88–90) is deferred by user; it is not used above.

## POME-DIVISORIAL-LELONG-GAUDUCHON-MASS-BOUND-001

Severity low; verified conditional deduction, not a printed error. Alternative to the external upper-semicontinuity input in Proposition 5.17.7.

Integrated file: docs/sections/plurisubharmonic-functions--quasi-plurisubharmonic-functions/index.html (blob 8891129803a9c17d6a779d0944614e111b414a52), Proposition 5.17.7, sgpt-0EA3F6EB, tag A1D8E7565DF1, lines 82–92. Its proof cites GZ17 Exercise 2.7 and uses normalized compactness.

Let X be compact connected, theta a closed smooth real (1,1)-form, and E a prime divisor represented on a smooth proper modification p:Z→X. Take any Gauduchon metric h on Z, so dd^c h^(n-1)=0. For every theta-psh u, pullback gives the positive closed current T=p^*theta+dd^c(u∘p). The Siu coefficient inequality gives T>=nu(u,E)[E]. Pair with h^(n-1) and integrate:

    nu(u,E) <= integral_Z p^*theta wedge h^(n-1)
                  / integral_E h^(n-1).

Indeed the distributional pairing of dd^c(u∘p) with h^(n-1) vanishes exactly, and the denominator is strictly positive. There is no need to establish L1 continuity of pullback or upper semicontinuity of divisorial Lelong numbers. For a fixed smooth model this bound holds simultaneously for every potential and for any finite collection of distinct prime divisors with the sum of their weighted coefficients bounded by the same numerator, by the divisorial decomposition. The numerator is nonnegative whenever the potential space is nonempty. If it is empty the original upper-bound assertion is vacuous.

Dependencies: holomorphic pullback of local PSH potentials and generic divisorial decomposition on a compact complex manifold (not just its Kähler special case), Gauduchon existence and smooth-model realization of E. Resolution is the permitted external input. This is an alternative conditional proof of the bound; the cited upper-semicontinuity result is not thereby established or removed from other consumers. Do not infer this bound for arbitrary changing models with a single fixed denominator. Proposed insertion: add the pairing proof as an alternative under these explicit inputs, retaining the historical reference. No downstream result is refuted.

## Coverage

* §5.17, lines 7–120, read all mathematical text. Closed-background definition, compactness qualification, monotone-net cofinal-tail argument, pullback descent and local-potential balayage checked. The broad mutatis-mutandis remark is not a certificate of every possible extension. The external upper-semicontinuity premise is not independently verified.
* §5.19, lines 7–207, nonexcluded mathematical text directly assessed; 5.19.10's analytic-singularity existence dependency explicitly deferred, not reopened. The normalized Poincare–Lelong coefficient at lines 63–76, order of minimal singularities, and generic divisorial coefficients checked. No whole-section certification including the excluded input.
* §5.22, docs/sections/plurisubharmonic-functions-and-singularities--plurisubharmonic-potentials/index.html, blob bf6e5ca74ac04a3d79565bb58bda8d968a68be68, lines 7–102, entire mathematical text directly assessed. The sign in the distributional representative construction is correct; nonclosed backgrounds are explicitly distinguished from local dd^c potentials. In Lemma 5.22.4 (tag 0DED015E67EF, lines 79–102), taking d and wedging by gamma^(n-2) yields da=B-aC; the pointwise inverse is smooth and the W^(k,1) bootstrap follows by the product rule. Elliptic regularity for u is a dependency, not independently certified here.
* Global convention checked in docs/sections/conventions/index.html, line 123: X connected compact, dimension >=1 unless stated otherwise. No disconnected counterexample is used.
* Actual current TOC docs/chapters/index.html, blob c0c07abf4d8f7575b54cff2ec694fcf987f51cf8: 747 section numbers, matched exactly to 747 distinct rows of SECTION_MATRIX.md, no missing or extra entries before update.

Two whole direct mathematical sections, one nonexcluded selected section; two conditional deductions, zero new confirmed false statements, zero new demonstrated proof gaps, zero fully certified transitive chains. Historic first-visit status is not asserted. The user-excluded Demailly approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss programme remains deferred-by-user, not resolved or certified. No source, main, registry, tag, website, build, tests or CI changes.
