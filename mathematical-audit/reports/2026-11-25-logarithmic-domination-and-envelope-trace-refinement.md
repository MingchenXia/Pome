# Logarithmic domination and envelope trace refinement — 2026-11-25

Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit parent: 80071aaa307ce43e3fcd208847dbfc5b631966fc. No production changes. All user-excluded Demailly approximation/regularization, Bergman, L2, Ohsawa–Takegoshi, multiscale atlas and positivity-loss work remains deferred-by-user, not certified.

## POME-LOGARITHMIC-MA-SUPPORT-ONE-SIDED-NORM-001

Severity low; verified conditional deduction, NOT a false printed theorem. Source: docs/sections/normalized-characterization-of-compact-extremals/index.html (blob fd5efa1edf755ed59b0c72f3dce7e28fdd1dc2aa), §16.41.1, stable source 8E661DED (article klimek-pluripotential-theory-8E661DED), permanent tag 1129B1616DEE; statement line 17, proof lines 23–33, normalization example line 38. The stated uniqueness and proof are sound under their listed internal inputs. The upper-growth-only counterexample in the source is not a new finding.

**One-sided norm identity.** Let u,v belong to the two-sided logarithmic class L+ in C^n, n>=1, and suppose mu=(dd^c u)^n is carried by a compact K and nonzero. (Nonzero follows from the usual total mass formula for L+, or from local domination itself as remarked below.) Then

    sup_C^n (v-u) = ess sup_mu (v-u).

Here the essential supremum is with respect to mu, not Lebesgue measure. This does not require (dd^c v)^n to be carried by K. In particular, if both measures are carried by K, the global uniform distance equals the supremum of |v-u| on K after deleting any pluripolar subset, or equivalently the infimum of such suprema. More explicitly, if -a <= v-u <= b quasi-everywhere on K, for a,b>=0, then -a <= v-u <= b everywhere. For the specific extremal V_K^* and a candidate u in L+ whose MA measure is carried by K, if -a<=u<=b quasi-everywhere on K, then V_K^*-a<=u<=V_K^*+b globally. Constants are sharp by additive shifts.

**Proof.** Put M=ess sup_mu(v-u), finite since both potentials are in L+ and their difference is globally bounded. Let c=inf_K u, finite by local boundedness. For eps,delta>0 set

    w=(1+eps)u - eps c + M + delta.

On K, w-u=M+delta+eps(u-c)>=M+delta, so v<=w mu-almost everywhere. MA(w)=(1+eps)^n mu by homogeneity and constant invariance of the classical BT product. At infinity w-v=eps log|z|+O(1) tends uniformly to +infinity; hence on each sufficiently large ball boundary strict ordering holds (indeed on a whole collar). Both v,w are locally bounded. Apply the very same bounded local domination principle used in the printed proof, with w as the measure-bearing potential. It gives v<=w throughout each such ball. Exhausting C^n and sending delta and eps to zero gives v-u<=M everywhere. The reverse inequality is immediate. If mu were zero, exactly this argument would hold with arbitrary real M, a contradiction, so nonzero can alternatively be deduced from the domination premise.

Apply the result in both directions if both measures are carried by K. BT measures of locally bounded psh functions charge no pluripolar sets, so removing such sets does not affect the necessary measure inequalities. For the extremal comparison use V_K^*=0 quasi-everywhere on K and its measure support in K as in the source. This proves every assertion, including sharpness by u=V_K^*+constant. The proof is conditional on the local domination and BT diffuseness inputs actually invoked in §16.41.1; no transitive proof-chain certification or claim for unbounded potentials outside L+.

Suggested addition: a corollary immediately after §16.41.1, preserving the normalization and original statement. Potential dependents: compact-obstacle extremal uniqueness and stability, including later global extremal comparisons; no direct downstream reference census was performed.

## POME-OBSTACLE-TRACE-PENALTY-LIMIT-ONE-001

Severity low; verified conditional deduction and explicit clipping proof detail, NOT a printed theorem error. Source: docs/sections/pointwise-estimates-for-obstacle-envelopes/index.html (blob 0afeba79adffb86326ca094ab25ce13daf6b2285), Lemma 16.44.1 (source 509BECF8, article transcendental-positive-cones-509BECF8, permanent 8281BE55D0D3); statement lines 8–12, maximum estimate lines 18–24, logarithmic truncation lines 26–32. Selected dependency: docs/tag/EA811ACFD26E/index.html, Lemma 16.15.7, especially equations and Step 3, physical lines 36–46 and 63; reference/background both kappa. Not an audit of the entire §16.15 or of Demailly approximation.

**Refinement.** Under the smooth penalized-equation existence, uniform convergence and differential inequality already invoked in Lemma 16.44.1, one may replace its upper bound by the stronger inequality, on all of the connected compact Kähler Z,

    0 <= m+Delta_kappa v <= B exp(A(v-min f)),
    B=m+sup_Z Delta_kappa f,

in distributions. The coefficient 1 in front of B is optimal, even for constant f (then v=f and H=m=B). For a logarithmic obstacle f=g-psi in the stated hypotheses, the corresponding global inequality holds with B=(C+1)m+sup Delta_kappa g and min f replaced by inf f. In particular the right hand side is globally bounded; no blow-up near poles is needed. This concerns only this obstacle problem, not the excluded analytic regularization programme.

**Proof.** The cited Step 3 with background equal to reference kappa gives, at a maximum x_beta of Q=log H_beta-A a_beta, for fixed metric-dependent A (chosen so the trace term has nonnegative coefficient),

    0 >= beta(1-B/H_beta(x_beta)) + nonnegative term - A m.

For beta>Am this implies H_beta(x_beta)<=B/(1-Am/beta). Maximizing Q and using a_beta(x_beta)>=min f yields, pointwise,

    H_beta(x) <= B/(1-Am/beta) exp(A(a_beta(x)-min f)).

Uniform convergence a_beta->v and distributional convergence dd^c a_beta->dd^c v permit testing against any nonnegative smooth function and taking beta to infinity. This proves the refined bound, with v itself in the exponential rather than replacing it by the obstacle f. Positivity of kappa+dd^c v proves the lower bound. No exchange of an unproved limit with a nonlinear measure is used; only a linear trace and uniform convergence of exponentials.

For the logarithmic obstacle give an explicit version of lines 26–32. As in the printed proof assume a bounded envelope v (connectedness and normalized L1 compactness furnish its upper bound on a nonempty pole-free open set; a constant is a lower competitor). Fix nonnegative rho in C_c^\infty((0,1)) with integral 1. Define

    chi_R(t)= integral_0^1 max(t,-R-s) rho(s) ds,
    psi_R=chi_R(psi).

The function chi_R is smooth, convex and nondecreasing, 0<=chi_R'<=1, equals t for t>=-R and is constant for t<=-R-1. Thus psi_R extends smoothly at the logarithmic poles; off them the chain rule gives dd^c psi_R>=-C kappa (C>=0), and the same holds on the constant neighborhoods. Pointwise psi<=psi_R<=max(psi,-R). For R>sup_Z(v-g) and R>inf f-min_Z g, we have v<=g-max(psi,-R)<=f_R:=g-psi_R<=f; hence P_kappa(f_R)=v. On the modified region psi<-R we have psi_R<=-R, hence f_R>=min g+R>inf f, and elsewhere f_R=f; therefore inf f_R=inf f. Finally m+sup Delta f_R<=(C+1)m+sup Delta g. Apply the smooth refinement to this one fixed smooth obstacle f_R, giving the global bound directly, without a further limit in R. The sum-of-logarithmic-divisor case has the same constant-neighborhood property since all coefficients are positive and the smooth part is locally bounded. This is elementary clipping of a fixed smooth-off-poles obstacle, not a construction of Demailly approximants.

Suggested correction/addition: retain the actual printed valid weaker inequality and optionally record the stronger global form; give the explicit one-sided clipping formula if desired. Dependent uses of the existing local trace estimate remain valid; no downstream theorem is asserted refuted or fully proved. Remaining premises: smooth penalized solution existence, uniform convergence, the differential inequality preceding Step 3, and the normalization estimate used to bound the logarithmic envelope are not certified transitively in this session.

## Scope and coverage

- Whole direct mathematical reads: §16.41 (lines 7–38) and §16.44 (lines 7–37), including all mathematical paragraphs in those files.
- Whole direct introductory reads: §16.1 (lines 7–19, blob 1751b26b427c36506d7ed35ca6f52aefc56f8b04); §16.2 (line 7, blob 912f81b3bccf3e1ead96fd18005261a708dfcb4e). The latter expressly specifies connected compact Kähler manifolds.
- Selected dependency: §16.15.7 as above. Other fetched §16.3, §16.6 and §16.8 excerpts do not count as whole reads and no excluded proofs are reopened. The matrix legacy status does not establish first-ever visits.
- Checked §16.41's two-sided growth, exceptional-set removal, measure-bearing argument of local domination, and order of epsilon/delta limits. Checked §16.44's maximum-principle sign, linear distributional limit, and exact clipping sandwich. No new false printed theorem or unresolved demonstrated proof gap. Two new conditional deductions, zero complete upstream-chain certifications.
- Checked the 44 section locators of Chapter 16 against the matrix and retained all 747 existing rows; not a new whole-project mathematical audit. No tests, project builds, CI, source, registry, permanent tag, main or site changes.
