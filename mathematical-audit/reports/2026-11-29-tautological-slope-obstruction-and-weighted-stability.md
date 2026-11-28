# Finite-scale tautological slope obstruction and weighted stability: 2026-11-29

Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Parent audit head: 34aa21cf1ab7f040287108bcf26d908f9a6de8a1.
This is a conditional downstream and slope audit, not a production change.
All excluded Demailly approximation/regularization and dedicated Bergman,
L2, Ohsawa–Takegoshi, multiscale and positivity-loss work remains
deferred-by-user, not resolved or certified. No excluded proof is reopened.

## POME-TAUTOLOGICAL-NEGATIVE-MAXSLOPE-FINITE-SCALE-001

Low / verified conditional deduction; Theorem 10.108.2 is not refuted.

Integrated reading section:
`docs/sections/tautological-metrics-and-maximal-slopes/index.html`,
blob 313098e0ab266ca5696a16775bc5277539dfe889.
Definition and model conventions line 8. Lemma 10.108.1, source C1E90EFE,
permanent C0B465266C15, lines 12–23; Theorem 10.108.2, source E0E0E4DB,
permanent 9CD904E0945C, lines 28–89.

Keep the exact hypotheses of the theorem: a reflexive sheaf of positive
rank r on a compact Kähler manifold, fixed smooth compact model P of its
projective bundle over the locally free locus, fixed Hermitian error form
Omega_P, and a movable class alpha. Fix the common modification Q, auxiliary
relatively ample A and all comparison constants in lines 34–36, before
varying the metric or the integer m. In the quotient convention, the
relative canonical bundle is O(-r) tensor pi^*det E; pushing the twist
O(m+N) therefore gives symmetric degree d=m+N-r, not m+N+r.
For rank one the fiber is a point and N can be fixed with the corresponding
base twist.

The proof actually gives the following finite-scale obstruction, conditional
on its fiber nonvanishing, generic extension, direct-image positivity,
determinant descent and tensor-slope inputs. Choose a fixed delta>0 small
enough that m*epsilon<=delta ensures the curvature margins of line 36,
including the fiber lower bound of Lemma 10.108.1. This is possible:
the fixed vertical auxiliary metric has a strict margin, and the error
form is bounded by a fixed multiple of the auxiliary positive form plus
base form. Decreasing delta keeps the same base curvature bound C1.
If one metric on the open tautological bundle has curvature at least
-epsilon Omega_P, then for every positive integer m with m*epsilon<=delta,
the construction gives a nonzero saturated subsheaf Gbar_m of
the reflexive ambient twist M tensor det E tensor Sym^d E, satisfying

    -C3 <= mu_alpha(Gbar_m)
         <= deg_alpha M + deg_alpha det E + (m+N-r) mu_alpha,max(E).

The constants C3, N and M are independent of both epsilon and m. This
follows from the fixed error transfer in lines 54–80 and the slope bound
in lines 82–85. No convergence of metrics, compactness of a family of
metrics, or limiting regularization is required.

Suppose mu_alpha,max(E)=-b<0. Put
D=deg_alpha M+deg_alpha det E and
L=(C3+D)/b-(N-r).
Every positive integer m to which the construction applies satisfies
m<=L. Take m0=max(1,floor(L)+1), so that m0>L. If a metric existed with
epsilon<=delta/m0, the construction with m=m0 would contradict this
inequality. Consequently every admissible epsilon satisfies

    epsilon > delta/m0.

In particular the infimum of admissible errors is >=delta/m0>0 (or +infinity
if none exists). This bound depends on the fixed model, auxiliary choices
and alpha; it is not asserted optimal or invariant under changing the
error form. It is a finite-m version of the printed asymptotic contradiction,
not a new certificate for the analytic premises.

Direct audit notes: the Nadel pole in Lemma 10.108.1 has coefficient r-1
in dimension r-1, the threshold for nonintegrability of a nonvanishing
holomorphic germ with the stated squared-log convention; at curvature
r*theta subtracting (r-1)*theta leaves strict positivity. The rank-one
case is separate. The auxiliary B and M are fixed before m varies.
Saturation adds an effective determinant divisor, not its negative.
The rank factor in line 71 cancels on dividing by rank in line 77.
The movable pairing is valid on the boundary as well, since it is
nonnegative on pseudoeffective classes by the premise used there.
The last inequality uses tensor slope additivity, not an assumption
that the symmetric power is semistable.

Outstanding dependencies (not newly certified): Nadel vanishing, generic
multiplier-ideal restriction and fiber L2 extension (not reopened),
HPS2017 Theorem 21.1, arXiv:1611.08768v2, the determinant lemma 10.104.1
(source 2FBA7F63, permanent EC118288B440), meromorphic Grassmannian
extension 9.72.1 (source FF53288F, permanent 0A2146B324EB), exceptional
correction and psh descent, codimension-two extension, and the tensor
slope theorem. Hironaka remains the permitted resolution input.
These are conditions on this review, not newly demonstrated proof gaps.
Affected result: 10.108.2 and its positive-minimum-slope dual obstruction;
the finite bound is a proposed optional addition only.

## POME-WEIGHTED-MA-STABILITY-PARAMETER-001

Low / verified conditional deduction; not a false printed theorem.
Integrated section
`docs/sections/equations-with-prescribed-singularities--holder-continuity-from-bounded-stability/index.html`,
blob 6a5a19947ef5767f9828fa2230e6f251db21d743.
Theorem 15.5.4, source 1B17D9EF, permanent 56C5E320D330,
statement lines 98–106, proof lines 112–166. Retain ALL its hypotheses
and the stated weighted smoothing estimates as black-box inputs; their
proofs and all excluded regularization inputs remain deferred.
The earlier 2026-10-30 POME-HOLDER-ABSTRACT-SMOOTHING-OPT-001 concerns
the sharp final interpolation with only two given bounds. It is not
recounted here; the new point is a different earlier choice of parameter.

Let alpha be the reference Hölder exponent (0<alpha<=1), n>=1,
eta=2alpha/(alpha+2n), gamma=1/(6n+1). The printed choice q=eta*gamma/2
is sufficient but can be replaced throughout this argument by
q=eta*gamma. Indeed 0<eta<=2/3, 0<q<1, so for epsilon=delta^q,
epsilon tends to zero and delta/epsilon tends to zero. Thus
b=(epsilon-2K delta)/A0 satisfies epsilon/(2A0)<=b<=epsilon/A0
for sufficiently small delta, just as at line 132.

Write F for the unshifted transform at line 123. Use, without proving
or modifying the excluded input, the inequalities at line 129:
omega+dd^c F >= -epsilon omega and
phi <= F <= R_delta phi+2K delta.
For T=(1-epsilon)F the curvature lower bound is epsilon^2 omega.
With sup phi=0, M=||phi||_infty and fixed B>=M+2K+1, the competitor
psi=T-B epsilon is continuous, omega-psh, and -M-B<=psi<=0.
The weighted bound at line 118 and the pointwise estimate at line 137
give

    integral (psi-phi)_+ dmu <= C(delta^eta + delta) <= C' delta^eta.

The square-capacity stability Proposition 14.19.23 (source 8D465062,
permanent 3B70BD39881D, integrated
`docs/sections/continuous-solutions-and-normalization/index.html`,
blob e4a9ece552056fdc387f170362cc1cc5c5fd4091, lines 370–379)
applies with a fixed competitor bound; its exponent is gamma.
Therefore sup(T-phi)<=C delta^(eta*gamma)+B epsilon<=C' epsilon,
also at equality q=eta*gamma. No estimate used here requires
delta^(eta*gamma)=o(epsilon). Since phi<=0,
0<=F-phi<=(T-phi)/(1-epsilon)<=2C' epsilon.
The same logarithmic penalty and monotonicity at lines 152–158 give
t0>=kappa delta and ||R_(kappa delta)phi-phi||_infty<=C delta^q,
where kappa>0 is fixed. The gradient estimate at line 160 is unchanged.
The last interpolation gives exponent q/(1+q), hence

    beta_new = 2alpha / ((alpha+2n)(6n+1)+2alpha).

This strictly improves the printed
alpha/((alpha+2n)(6n+1)+alpha), with the same type of uniformity.
No sharpness in the PDE class is claimed. Proposed optional replacement:
only the parameter q and resulting exponent in Theorem 15.5.4 and its
proof. The existing weaker statement is valid conditional on its inputs.

## Other direct downstream checks

- 15.5.1 source CA85850B / permanent CA29182325B0, lines 11–89:
  the competitor bound and log-radius argument are consistent conditional
  on the stated smoothing premises; alpha=2eta gives the displayed
  2(p-1)/(np+3(p-1)) endpoint, approached strictly. No new error.
- 15.6.1 source E9203C4F / permanent 02C5F4AFC7FF,
  `docs/sections/equations-with-prescribed-singularities--local-continuity-in-a-semipositive-big-background/index.html`,
  blob 222db429ecdbb24a04be5a0fc5039299e216b937, lines 7–81.
  The strict barrier cancels the curvature error because s*kappa=e.
  The comparison theorem 15.4.1 (source D2BDFCB4 / permanent
  72397EB33655) explicitly allows an unbounded comparison potential;
  its upper bound v<=0 is met. On each compact subset of U the
  lower bound for rho makes the radius factor uniform, and the
  convergence of continuous averages is locally uniform. No continuity
  across the pole set, nor a power estimate absent a power bound for
  the curvature modulus, follows. All smoothing premises deferred.
- 10.53 (permanent 92F5D28F54DB),
  `docs/sections/spectral-sequences-support-and-cup-products/index.html`,
  blob ab6d205468700bcac45daab8cd763377fa2e60c1, line 5: heading-only
  navigation to 10.54–75; no mathematical statement to certify.
- Global conventions §1.1 and 15.4.1 statement checked for context.

## Coverage and limits

Whole direct conditional reading of current §10.108 mathematical lines
8–89; whole downstream conditional recheck of §§15.5 (7–167) and
15.6 (7–81), whose older selected visits are documented in the 2026-10-30
checkpoint despite the legacy-unreconciled matrix rows. Heading-only
§10.53; selected premise statement 14.19.23 and 15.4.1, no upstream
proof-chain certification. No historical first-visit claim.
Two verified conditional deductions, zero newly confirmed printed errors,
zero newly demonstrated proof gaps, zero complete transitive certificates.
No tests/build/CI, publication, or changes to production content, registry,
source repos or permanent tags.
