# Uniform weighted intersection comparison and simultaneous nef-boundary orders

Date: 2026-11-25. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Finding: **POME-GAUDUCHON-UNIFORM-WEIGHTED-INTERSECTION-POLYNOMIAL-001** — low / verified conditional deduction, not a printed error. No production patch.

## Anchors and direct audit

All paths below refer to the integrated reading edition on the reviewed main SHA.

- Whole introductory §12.1, `docs/sections/a-gauduchon-variational-volume/index.html` (blob 408aced882e04bc8578f9ab6f68bdc2c1aa1d7fa, mathematical paragraphs before the navigation). Connectedness, positive probability normalization and the nonclosed background conventions are explicit. The forward references in this introduction are not certifications.
- Whole §12.2, `docs/sections/a-gauduchon-variational-volume--the-quotient-and-the-smooth-equation/index.html` (blob 9ec67161d46b3ba20afa1b1c9a0c84f29322763e, physical lines 7–99): Definition 12.2.1 (source non-kahler-pluripotential-theory:6E1DBC11, permanent tag 0C4AF7E2CEBB), Proposition 12.2.2 (CEFAD6D9 / 4AF37F3C8091), Theorem 12.2.3 (876DF057 / 2DB664A6EFDF), Corollary 12.2.4 (E0F8050A / A486E36565B6). The homogeneity exponents, Stokes pairing, infimum concavity and upper semicontinuity, AM–GM equality, conformal Gauduchon uniqueness for n>=2, dimension-one probability normalization and bigness lower bound are consistent. Upper semicontinuity also follows immediately for nets because an infimum of continuous functions is USC. Smooth equation existence (14.2.1), Gauduchon existence/uniqueness (11.4.2) and the other cited analytic inputs are not certified here.
- Whole §12.20, `docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary/index.html` (blob a7c145c5d1ceb0f1326bfb155f75dc9d854f14a0, lines 7–140, before navigation): Proposition 12.20.1 (895EF015 / EBFCF76A5A51), Proposition 12.20.2 (03644B93 / 883742E77C19). Checked the inequality reversal on dividing by log epsilon<0, rescaling, nef intersection coefficient positivity by smooth positive closed representatives, and Hopf determinant and upper-mass comparison conditional on 23.1.1. No claim of checking that latter proof.
- Whole §12.26, `docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--a-maximum-rank-comparison-criterion/index.html` (blob ccce6cecc0a14fcf89c2c385e7d8f87ff10df2c8, lines 7–79). Proposition 12.26.1 (841CBE9E / 94DF4FEA70D3), Corollary 12.26.2 (091774C0 / 87EBA7661A8A), Example 12.26.3 (A6D59DC7 / 698A2684C823). The nonnegative intersection polynomial, maximum-rank open locus, rank under modifications and product nonclosed example are correct. At line 60 the constants for comparison with the unweighted active sum are allowed to deteriorate as a coefficient tends to zero; the weighted comparison below removes this issue while retaining the full polynomial rather than a single fixed-parameter order.
- Selected dependency §12.25.1, `docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--integer-orders-in-fixed-projective-cones/index.html` (blob 82790640609d3d58b131873295a827e8d7869d85, lines 10–60, source 5E026F83 / DAA29135206D). Distributional Stokes and comparison constants min(c,c_h), max(C,C_h) checked, as well as the constant-rank determinant estimate. Rest of §12.25 not assessed.
- Repeat dependency §12.11, `docs/sections/a-gauduchon-variational-volume--nef-limits-and-nonattainment/index.html` (blob 086d12a65c46cfb68c7d6fe952266515ca04623b). Closed nef volume formula after Theorem 12.11.1 (F03E2CAC / 9ECB2B21B601), by commuting infima and closed Stokes, remains conditional on the smooth equation input. No transitive proof certificate.

## Uniform statement

Let X be connected compact Kähler of dimension n>=1, with fixed Kähler form Omega, smooth Hermitian h, smooth strictly positive probability volume mu, smooth closed semipositive forms B_1,...,B_s, and fixed smooth strictly positive functions f_1,...,f_s. For all t_j>=0 and epsilon>0 define

    theta(t) = sum_j t_j f_j B_j,
    B(t) = sum_j t_j B_j,
    P(t,epsilon) = integral_X (B(t)+epsilon Omega)^n.

There are strictly positive constants k,K independent of **all** t and epsilon, including coefficients approaching zero or infinity, such that

    k^n P(t,epsilon) <= V_mu(theta(t)+epsilon h) <= K^n P(t,epsilon).

This is conditional on the printed closed Kähler volume identity (or §12.2.3 and closed Stokes). No regularization or excluded approximation argument enters the deduction.

Proof. Choose m=min_j inf_X f_j>0, M=max_j sup_X f_j<infty, and a,b>0 with a Omega<=h<=b Omega. Put k=min(m,a), K=max(M,b). Termwise positivity for nonnegative coefficients gives m B(t)<=theta(t)<=M B(t), uniformly, even if all t vanish. Thus

    k (B(t)+epsilon Omega) <= theta(t)+epsilon h <= K (B(t)+epsilon Omega).

Both backgrounds are strictly positive for epsilon>0. Apply the quotient definition directly: each numerator is ordered because gamma^(n-1) is positive, and the denominator is unchanged. Taking infima and raising the resulting nonnegative inequalities to power n proves the assertion using V_mu(B(t)+epsilon Omega)=P(t,epsilon). No exchange of a parameter limit and an optimizing metric is required. For epsilon=0, the same comparison holds using the closed nef formula, or by §12.11.1 for each fixed t; the constants remain uniform. The case s=0 is the same statement with k=a,K=b.

Expand with B_0=Omega and t_0=epsilon:

    P(t,epsilon) = sum_{|alpha|=n} C_alpha epsilon^{alpha_0} product_{j=1}^s t_j^{alpha_j},
    C_alpha = n!/(alpha_0!...alpha_s!) integral_X B_0^{alpha_0} wedge ... wedge B_s^{alpha_s} >= 0.

Define A={alpha:C_alpha>0}; it is finite and includes (n,0,...,0). For a parameter path t_j(epsilon)=c_j(epsilon) epsilon^{p_j}, with p_j>=0 and c_j bounded above and away from zero for small epsilon, set

    d(p)=min_{alpha in A}(alpha_0+sum_{j=1}^s alpha_j p_j).

Every monomial is bounded by a constant times epsilon^{d(p)} for 0<epsilon<=1; choose a minimizing monomial for the reverse bound. Consequently the simultaneous order exists and equals d(p); the logarithmic error in this statement is O(1/|log epsilon|). The order is concave, continuous and piecewise affine in the exponent vector, with integer slopes. More generally for positive t_j with no power asymptotics, write p_j(epsilon)=log(t_j)/log(epsilon). Direct substitution, including negative p_j, yields the same bounded logarithmic error uniformly in p_j(epsilon): compare the polynomial with its largest monomial, using the minimum and sum of the strictly positive fixed coefficients. Zero parameters simply delete all monomials with positive corresponding exponent. This gives exact lower and upper logarithmic orders via liminf and limsup of the finite minimum, even for oscillating paths. No assertion that these are the orders of a single fixed background when t varies.

For fixed positive active coefficients, p_j=0, the smallest alpha_0 is n-R, where R is the maximal rank of the active sum: (B(t))^(R+1)=0 and the positive continuous density B(t)^R wedge Omega^(n-R) is positive on a nonempty open set. This recovers §12.26.2. The new formula controls simultaneous approach to parameter faces, not just separate fixed-background limits.

Example: X=P^1 x P^1, B_1 and B_2 normalized pullbacks with B_1^2=B_2^2=0, integral B_1 wedge B_2=1, Omega=B_1+B_2. Then P=2(t_1+epsilon)(t_2+epsilon), so along t_j=epsilon^{p_j}, the simultaneous order is min(p_1,1)+min(p_2,1). Both generators have nonzero coefficients at every epsilon, yet the fixed-active-rank order zero would give the wrong simultaneous exponent. For f_j=1, h=Omega the comparison is an equality; thus the exponent is exact even in the closed case. Positive variable f_j need not preserve closedness but preserve the order by the comparison.

If pi:Y->X is a modification with Y compact Kähler, the same argument gives the analogous polynomial on Y for any fixed Kähler Omega_Y and Hermitian h_Y. It does not assert that all mixed coefficients involving Omega_Y coincide with those on X. In fact the support of that polynomial agrees with the support on X: for alpha with alpha_0=k, the smooth positive-semidefinite (n-k,n-k) product of the B_j has positive pairing with Omega^k iff it is nonzero somewhere, equivalently on a nonempty open set. If nonzero, its pullback is nonzero on the intersection with the biholomorphic locus; if identically zero, its pullback is zero. Positivity and a strictly positive Omega_Y^k then prove the same criterion on Y. Thus d(p) is unchanged under these modifications, even for simultaneous paths. The constants and the leading coefficients may change.

## Classification and next actions

No false theorem or unresolved proof gap demonstrated. Proposed optional corollary immediately following 12.26.2, preserving its fixed-background statement and permanent tag. Affected scope: uniform versions of §12.25/§12.26 comparisons, and simultaneous paths in §12.20; no downstream result is refuted. The closed volume identity remains an internal but not fully audited premise. The result does not address coefficient *functions* that lose a uniform positive lower bound, non-Kähler modifications, or backgrounds outside this comparison cone.

Coverage: three full current mathematical sections (§§12.2, 12.20, 12.26), one full introductory section (§12.1), one selected dependency (§12.25.1), one whole repeat dependency (§12.11). §12.6 was fetched but not assessed and is not upgraded. No first-ever visit claim. All excluded approximation programmes remain deferred-by-user. No build, tests, CI, website publication, or production source/registry/tag change.
