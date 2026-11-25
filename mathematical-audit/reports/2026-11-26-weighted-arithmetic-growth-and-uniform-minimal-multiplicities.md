# 2026-11-26 — Weighted arithmetic growth and uniform minimal multiplicities

Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit parent: 18eab081c91646d2f439454640ca929088899204. No source changes.

## POME-ARITHMETIC-GROWTH-WEIGHTED-EVALUATION-RANK-001
Severity low; status **verified conditional deduction**, not a printed error.

Anchors: docs/sections/entire-function-growth-and-algebraic-zero-sets--entire-function-growth-and-arithmetic-zero-sets/index.html (blob 465572b3785941e02714482e9d69735fcbcdcc73), theorem 9.55.1 source demailly-complex-geometry:F0566573, permanent 2112DD801FC5, physical lines 11–80; corollary 9.55.8 source CE420F64, permanent 16B6E15BB4A5, lines 85–109; example 9.55.11 source 9C417C3E, permanent DDE636CB719F, line 114. Read their integrated statements/proofs, not a source locator substitution.

Let S be a finite nonempty subset of C^n, P_{<d} the vector space of polynomials of total degree <d (integer d>=1), and r_d(A) the rank of the evaluation functionals on P_{<d} indexed by A subset S. For a nonzero entire f put m_s=ord_s f >=0. For every fixed d there is C(S,d)>=2, independent of f and all its orders, such that, for R>=r>=1,

    log M_f(R)-log M_f(r) >= d^(1-n) W_d(m) log(R/(C(S,d) r)),

where W_d(m) is the maximum sum of the m_s over independent subsets of evaluations, equivalently

    W_d(m) = sum_{k>=1} r_d({s in S: m_s>=k}).

The sum is finite. In particular, for uniform order at least m, the coefficient is m r_d(S)/d^(n-1). This holds also when evaluation on S is not injective; no assumption on the degree of a least vanishing polynomial is needed. The maximum over a finite list of d is admissible with the maximum of their constants, and the corresponding growth coefficients can be maximized for R greater than this common constant times r. If R is smaller, monotonicity suffices.

Proof: for any independent subset B of evaluations, evaluation P_{<d} -> C^B is surjective by finite-dimensional duality. Interpolate each monomial z^alpha of degree d at B by a polynomial R_alpha of degree <d. The tuple P_alpha=z^alpha-R_alpha has leading forms all degree-d monomials, hence their only common zero is 0, and its common zeros contain B. Theorem 9.55.1 gives a coefficient at least d^(1-n) sum_{s in B} m_s by (9.55.3), provided R>C_B r. Choose a maximum-weight independent subset; finitely many subsets B exist for fixed S,d, and the choices of interpolants and constants can be fixed in advance. Taking their maximum gives the uniform constant. For R<=C(S,d)r the asserted bound is automatic. (The empty subset contributes zero.)

For the rank identity, order the evaluations by nonincreasing nonnegative integer weights and retain a functional precisely if independent of those already retained. For each threshold k, the retained functionals of weight >=k span all such functionals: each rejected one was in the span of earlier retained ones with weight at least its own. Hence their number equals r_d({m>=k}). Summing over thresholds gives the stated weight for the greedy subset. Every independent subset has no more than that rank at every threshold, proving optimality within this interpolation procedure. No assertion that the resulting coefficient is optimal for arbitrary configurations.

If delta is the least degree of a nonzero polynomial vanishing on S, r_delta(S)=binomial(delta+n-1,n), so this retains the exact coefficient delta^(1-n) binomial(delta+n-1,n) in the proof of 9.55.8, rather than discarding the positive lower-order terms in (9.55.9). Applied to polynomials and R->infinity, the same inequality gives the weighted degree lower bound and Omega(S)>=sup_d r_d(S)/d^(n-1). For n>=2, after the rank reaches |S| (it does by products of separating linear forms), the quotient cannot increase. For n=1, the same coefficient is attained by the polynomial with the prescribed orders at all points; there the rank stabilizes at |S|.

A separate sharp family from 9.55.1: if the zero fiber of an n-tuple of degree <=d satisfying its leading-form condition consists of d^n distinct points, uniform order m gives coefficient dm by (9.55.3). Any nonzero component vanishes on S, has degree <=d, and its m-th power has degree <=dm and order >=m. Thus Omega(S)=d, omega_m(S)=dm, and the entire-function growth coefficient for common order m is sharp. No Bezout assertion is needed (cardinality is a hypothesis). Explicit examples are Cartesian grids A_1 x ... x A_n, each A_i containing d distinct complex numbers, using P_i(z)=prod_{a in A_i}(z_i-a). In dimension one arbitrary nonuniform orders are also sharp by the product of linear factors.

Dependencies: weighted Jensen, radial mass, local bounded truncation and finite-slice multiplicity results cited at lines 16,36,62,69,79, including 6.34.1/.2/.5, 6.35.1, 6.36.1, 6.44.5, 6.46.1, remain conditional inputs; they are not reopened. The excluded L2/point-extension arguments in 9.55.12 and downstream 9.55.15/.16 are not audited here. No claim of the full optimal coefficient Omega(S) for general configurations. Proposed addition after 9.55.8; affected comparisons: 9.55.11 and the projective definitions in 9.56.1. Existing statements remain valid.

## POME-MINIMAL-MULTIPLICITY-UNIFORM-BIG-LOCUS-001
Severity low; status **verified conditional deduction**, not a printed error.

Anchors: docs/sections/global-potentials-and-positive-cohomology-classes--minimal-multiplicities-and-positivity-loci/index.html (blob 40c4d72d5f493cde3dfdb343e7d31f3b6c3f4907), definition 10.5.1 source foundations-of-pluripotential-theory:968294F3 permanent 057A3C697CFD lines 11–24, proposition 10.5.2 source A6A9A079 permanent 68A6D68513B0 lines 43–58, proposition 10.5.3 source 21CB9E25 permanent 2DF07B2D5AA9 lines 63–86.

On a fixed connected compact Kähler X, write lambda_x(alpha)=nu(alpha,x) and lambda_D(alpha)=nu(alpha,D) for a prime divisor. For every compact subset K of the big cone, there are C_K, epsilon_0>0 with, simultaneously for all alpha in K, points x and prime divisors D,

    0 <= lambda_x(alpha)-lambda_x(alpha+epsilon[omega]) <= C_K epsilon,
    0 <= lambda_D(alpha)-lambda_D(alpha+epsilon[omega]) <= C_K epsilon.

In fact the estimates hold for every epsilon>0 with a suitable constant, and for alpha,beta in K sufficiently close,

    sup_x |lambda_x(alpha)-lambda_x(beta)| <= C'_K ||alpha-beta||,
    sup_D |lambda_D(alpha)-lambda_D(beta)| <= C'_K ||alpha-beta||.

The latter hold globally on K after enlarging C'_K; if there are no prime divisors interpret the second supremum as zero. This is stronger than separate continuity for a fixed point or divisor.

Proof: use the finite-dimensional linear smooth representative map of (10.2.18), with |theta_alpha-theta_beta|<=c||alpha-beta|| omega as Hermitian forms. For each alpha_0 in K choose a Kähler current S_0>=2 delta_0 omega in alpha_0. For alpha sufficiently near alpha_0, S_alpha=S_0+theta_alpha-theta_alpha0 >=delta_0 omega. A finite covering of K gives one delta>0 and finitely many such choices of S_0. Smooth perturbation leaves point and generic divisorial Lelong numbers unchanged. For each fixed S_0 the point Lelong numbers are uniformly bounded: use a finite coordinate cover with relatively compact smaller charts, one uniform positive radius for Euclidean balls within each larger chart, ordinary Lelong monotonicity, comparison of the local Euclidean trace form to omega, and finite global trace mass. In dimension one the same bound is immediate from measure mass. Thus for all alpha in K and all x, nu(S_alpha,x)<=M; the generic divisor values are also <=M.

For epsilon>0, write V_e=V_{theta_alpha+epsilon omega}. The current theta_alpha+dd^c V_e is >=-epsilon omega. With t=epsilon/(delta+epsilon), its convex combination with S_alpha, weights (1-t),t, is positive in alpha. Minimality gives

    lambda_x(alpha) <= (1-t) nu(V_e,x)+t nu(S_alpha,x).

Here proposition 10.5.2 identifies minimal-potential Lelong numbers with class multiplicities in both big classes. By monotonicity of the envelopes lambda_x(alpha)>=lambda_x(alpha+epsilon[omega]); subtracting yields a bound t M<=M epsilon/delta. Taking infima over points of D, using the preceding generic-value identity in lines 33–39, gives exactly the same estimate for lambda_D. No choice of a point simultaneously generic for uncountably many classes is needed.

For h=||alpha-beta||>0, the smooth form comparison theta_beta<=theta_alpha+ch omega implies V_theta_beta<=V_theta_alpha+ch omega, so lambda_x(beta)>=lambda_x(alpha+ch[omega])>=lambda_x(alpha)-Mch/delta. Reverse alpha,beta for the other inequality. Taking generic infima again yields the uniform divisor estimate. In fact this works for every pair in K with the same constants, since the one-sided radial estimate has no smallness restriction. The epsilon=0 and h=0 cases are immediate.

Dependencies: local positive-current trace and ordinary Lelong monotonicity, the smooth representative map, minimality and additivity of Lelong numbers in 10.5.2 and generic infimum formula are conditional inputs. This is an elementary consequence of the printed convex mixture, not a proof of Demailly approximation or the non-Kähler locus theorem. Proposed addition after 10.5.3. No assertion of uniform continuity at the boundary of the big cone or that pointwise Lelong numbers are spatially continuous.

## Direct coverage and exclusions

- §9.54, docs/sections/entire-function-growth-and-algebraic-zero-sets/index.html, ec4e258d279d6ebbfdaa68a903b4907ef0fab372, line 5: complete navigation-only heading, no mathematical statement.
- §9.55, above blob, lines 7–114: selected arithmetic and weighted-current growth arguments. Checked radius inclusions, sign of logarithm, strip pasting and truncation premise, coefficient and subadditivity, planar line configuration. No complete upstream certification. Lines 119 onward invoking point extension or singular weighted L2 are outside this audit.
- §9.56, docs/sections/entire-function-growth-and-algebraic-zero-sets--refined-bounds-for-simultaneous-vanishing-orders/index.html, 8ff4e22eede7fe72ba7bbceeb221ef8b2ed20cf7: selected lines 7–56 (projective definition, squarefree monic polynomial elimination, generic linear section; multiplier ideal coherence treated solely as an input), 159–171 (derivative argument in the small fractional degree case), 177–192 (limit deductions conditional on theorem 9.56.4). Theorem 9.56.4 source label available by permanent D5C665BE2BA4; lemma 9.56.3 and extension-dependent large fractional degree proof not audited.
- §10.1, docs/sections/global-potentials-and-positive-cohomology-classes/index.html, 6f817fc2a3effc4c21e3ec5f7b1bb63f9ba66480: introductory lines 7–16, mathematical overview only; excluded inputs in lines 10 and 13 noted as dependencies, not investigated.
- §10.4, docs/sections/global-potentials-and-positive-cohomology-classes--positivity-cones-and-divisorial-decomposition/index.html, bb15c51bfaf241d9b74bb16415c3083c4bc9f42e, selected lines 7–119 (cone closures, mixed Hodge index, discrete log-concavity and nef boundary). Later approximation programme not audited.
- §10.5, above blob, selected lines 7–86 (minimal multiplicity definitions, comparison, homogeneity and lower semicontinuity). No whole-section certification; lines 91 onward outside this run.

Historical coverage remains unreconciled; no historical first-visit claim. Two new conditional deductions, zero new confirmed printed errors, zero new demonstrated proof gaps, zero complete upstream-chain certificates. Demailly approximation/regularization and its designated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain deferred-by-user. No build, tests, CI, publication or changes to production files or permanent labels.
