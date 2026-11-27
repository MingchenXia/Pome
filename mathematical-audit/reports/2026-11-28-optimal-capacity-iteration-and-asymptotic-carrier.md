# Optimal abstract capacity iteration and asymptotic carrier domination

Date: 2026-11-28. Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Starting audit head: 32ffcb92cb20a62ac3e1ab72c6d1bc43d892ae5b. No source, registry, tag, main, website, CI or build changes.

## 1. POME-CAPACITY-ITERATION-OPTIMAL-CONSTANT-001

Severity low; status **verified conditional deduction**, not a false printed lemma.

Integrated reading edition: `docs/sections/continuous-solutions-and-normalization/index.html`,
blob `e4a9ece552056fdc387f170362cc1cc5c5fd4091`.
Lemma 14.19.14 (370AD0860DAD; source 38A63EDA), lines 209–249;
Lemma 14.19.16 (9C1A40570E78; source 15EC6B6A), lines 254–298,
especially equation 14.19.17 (3CFE977F80E0; line 261) and the recurrence on line 276.
Theorem 14.19.19 (EA32B8891E2B; source FD57C562), lines 303–324.

Retain all of Lemma 14.19.16's hypotheses. In particular the bounded potentials,
positive Hermitian background, fixed epsilon, sublevel capacity estimate and
power domination with A, alpha > 0 are unchanged. Write
a(s)=Cap(U_s)^(1/n), K=(C_H A)^(1/n). The printed proof establishes that
a(s)>0, is nondecreasing, and satisfies

    t a(s) <= K a(s+t)^(1+alpha),  s,t>0, s+t<delta_epsilon.

The constant 2/(1-2^(-alpha)) is valid, but can be replaced by

    C_opt(alpha) = (1+alpha)^(1+1/alpha)/alpha.

Proof: for any r>1 assume for contradiction that
r K a(D)^alpha/(1-r^(-alpha)) < D, with 0<D<delta_epsilon.
Start s_0=D, t_j=r K a(s_j)^alpha, s_(j+1)=s_j-t_j.
Inductively a(s_j)<=r^(-j)a(D): the geometric sum bounds the
total of all constructed t_j strictly below D, so s_(j+1)>0;
apply the recurrence at (s_(j+1),t_j) to get
a(s_(j+1))<=a(s_j)/r. Thus the s_j decrease to a positive
s_infty, and monotonicity yields 0<a(s_infty)<=r^(-j)a(D) for all j,
a contradiction. No continuity of a is needed. Consequently

    D <= [r/(1-r^(-alpha))] K a(D)^alpha.

The derivative of r/(1-r^(-alpha)) has the sign of
1-(1+alpha)r^(-alpha), so its unique minimum is at
r=(1+alpha)^(1/alpha), giving C_opt. The resulting conclusion is

    D <= C_opt(alpha) (C_H A)^(1/n) Cap(U_D)^(alpha/n).

Sharpness for the abstract recurrence, NOT claimed for actual
Monge–Ampere capacities: on (0,delta_epsilon) let
a(s)=(s/(C_opt K))^(1/alpha). This is positive and nondecreasing.
The ratio t a(s)/(K a(s+t)^(1+alpha)) equals
C_opt x/(1+x)^(1+1/alpha), where x=t/s. Its maximum over x>0
is exactly 1, at x=alpha. Hence it satisfies the entire recurrence
and attains equality in the optimized conclusion at every D.
No smaller universal constant can follow from the recurrence and
monotonicity alone. At alpha=1, C_opt=4, exactly the printed
constant, so Theorem 14.19.19's application remains unchanged.

Proposed optional replacement: add the optimized statement and
the distinction between recurrence sharpness and geometric sharpness.
No correction to the valid existing inequality is required.
Dependencies: 14.19.14 and its modified-comparison input 14.19.6;
the integration-by-parts approximation invocation at line 97
(5.32.1) remains deferred-by-user, not certified. The direct
algebra after that premise (lines 99–124), strict domination
(133–169), positive individual mass (175–186), exponential
comparison (190–200), thin sublevel inclusion and positivity
reserve (209–249), and original iteration (254–324) were checked.
In particular 0<= (1-epsilon)(w-v)<=t/2 ensures both inclusions
at line 239 and the stated C_H. No whole-section claim.

## 2. POME-RELATIVE-MA-ASYMPTOTIC-CARRIER-TV-001

Severity low; status **verified conditional deduction**, not a printed error.
Integrated file `docs/sections/relative-equations-under-positive-lower-mass/index.html`,
blob `75535cb099b754589883aa9f9fa4867fabd89d86`.
Standing hypotheses lines 8–49, uniform lower mass line 81,
Lemma 15.37.13 (E5ED88B4042A; source F56DEC9E), lines 271–337;
Proposition 15.37.17 (D220D741C684; source 8424FFA4), lines 345–386;
Theorem 15.37.19 (6FBF04A6D4DE; source 4EA71F8C), lines 395–419.

Keep the standing semipositive big background, model reference,
positive lower mass and the relative class E_phi. Let u_j in E_phi
converge in L1 to u in PSH(X,theta). Write mu_j for their extended
non-pluripolar Monge–Ampere measures. Assume each mu_j is finite.
Suppose a finite positive non-pluripolar measure nu satisfies

    d_j := (mu_j - nu)_+(X) -> 0,

where the plus denotes the positive part of the signed finite
measure in its Jordan decomposition. Unlike the printed fixed
carrier hypothesis, mu_j need not be dominated by nu.

Then u belongs to E_phi, u_j -> u in capacity, and
mu_j -> mu_u weakly, with mu_u <= nu.

Proof: start with any subsequence and choose a further subsequence,
indexed j_k, with d_(j_k)<=2^(-k). Put
eta_k=(mu_(j_k)-nu)_+ and rho=nu+sum_k eta_k.
Each eta_k<=mu_(j_k), hence is non-pluripolar. The positive series
defines a finite non-pluripolar measure rho, since its total mass
is at most nu(X)+1. By the Jordan decomposition
mu_(j_k)<=nu+eta_k<=rho, so Theorem 15.37.19 applies exactly as
printed to this subsequence. It yields class membership, capacity
convergence and weak convergence to mu_u. For every nonnegative
continuous test f,

    integral f dmu_(j_k) <= integral f dnu + ||f||_infty d_(j_k).

Pass to the weak limit; positive continuous tests determine order
of finite Radon measures, giving mu_u<=nu. This limit and the
potential are independent of the extracted subsequence. The
subsequence contradiction criterion gives the two convergences
for the original sequence: failure of capacity convergence
would give a fixed positive threshold and a subsequence with
capacity bounded below, and failure of weak convergence would
give a continuous test and a subsequence violating its scalar
limit. This is a sequential result, not an assertion about
extracting sequences from arbitrary weakly compact nets.

Corollary (total variation compactness criterion). Under the
same standing assumptions and L1 convergence, if {mu_j} is
relatively compact in the total variation norm of finite measures,
then u is in E_phi, u_j converges in capacity and
||mu_j-mu_u||_TV -> 0. Indeed, every subsequence admits a further
subsequence converging in TV to a finite positive measure nu.
This nu is non-pluripolar: its mass on each pluripolar set is
bounded by the TV distance from a non-pluripolar mu_j, tending
to zero. The preceding result applies since d_j<=||mu_j-nu||_TV.
Weak convergence identifies nu=mu_u. The subsequence criterion
now gives full capacity and TV convergence. Conversely, TV
convergence implies relative TV compactness for a sequence.
Thus in this setting TV precompactness is precisely the added
compactness criterion for TV convergence, not a consequence
of fixed domination alone. The prior finding
POME-MA-DOMINATED-WEAK-NOT-TV-001 remains valid and is not counted
as new. In particular, the same corollary applies when all mu_j
have densities with respect to a fixed non-pluripolar finite
measure and the densities are relatively compact in L1 of that
measure.

No independent existence theorem or upper-mass bound is asserted.
The proposed addition is a corollary of the printed theorem.
Potential dependents: the later moving-carrier results and
relative equation approximation in section 15.37 may use it
when their finite measures satisfy the stronger norm hypothesis;
no claim that they generally satisfy it, or that their proofs
are thereby completed.

Direct proof reading: 15.37 lines 8–419, including the finite
and extended domination proofs (85–243), scalar/exponential
comparison (248–263), finite contact partitions and summable
rooftop extraction (271–337), the double monotone limit in
capacity and nonnegative weighted lower semicontinuity (345–386),
and uniform deep-tail domination (395–419). Conditional on
the cited contact, stretching, lower-mass, bounded-product and
tail results; no transitive certification. This is a repeat of
previously reported selected 15.37.13/.17/.19 coverage, now
with a new corollary; no historical-first-visit claim.
The later moving-carrier/existence proofs were not audited.

## Coverage and scope accounting

- 14.19: newly selected direct conditional lines 61–124 (line
  97 approximation premise deferred), 133–324; remainder not reviewed.
- 15.37: selected direct conditional lines 8–419; prior selected
  coverage acknowledged; remainder not certified.
- Current chapter 14 and 15 TOCs matched all 29 and 37 respective
  numbered rows of the existing matrix; 747 unique numbered rows
  retained. No other chapter's TOC freshly reconciled in this run.
- Two new conditional deductions; zero newly confirmed printed
  errors, demonstrated proof gaps, whole-section certificates, or
  complete upstream proof-chain certifications.
- The Demailly approximation/regularization, dedicated Bergman,
  L2, Ohsawa–Takegoshi, multiscale and positivity-loss programme
  remains deferred-by-user, not resolved or certified. The
  regularization-based 15.5 was screened by subject and excluded
  from this run's mathematical coverage. No tests, builds, CI,
  automatic publication, production/source/registry/tag edits.
