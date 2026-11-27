# Bounded domination with a measure defect and the exact stretching semigroup

Date: 2026-11-28. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit starting head: 4c3f5a69c5a89f5d81f35b4d7281c3d4efb22836.

Scope: selected current integrated mathematics in
`docs/sections/envelopes-and-volumes-of-singularities/index.html` (blob 0bdddc04cbc0cefd05591fdffc0796f3405b2a69), physical lines 119–219 and 926–1347. Also inspected the introductory lines 7–19 and the individual pages of 5.25.2 and 5.24.3. This is not a whole-section or transitive certificate. Historical first-visit status is unreconciled. No excluded approximation, Bergman, L2, OT, multiscale or positivity-loss proof was reopened.

## POME-BOUNDED-DOMINATION-MEASURE-DEFECT-L1-001

Severity low; status verified conditional deduction, NOT a false printed theorem or proof gap. Theorem 16.28.56 (Guedj–Lu), permanent C67CEBABC968, source 15C46513, lines 976–1015. Uses the additional hypothesis described at 1035–1041. The original theorem requires only positive mass of each bounded potential and has no uniform lower-mass hypothesis; preserve that stronger qualitative scope.

Let X be a connected compact complex n-fold, theta smooth semipositive, and assume
\(m=v_-(\theta)>0\). This number is finite by testing the zero potential.
Fix the smooth positive volume dV and let K be the uniform L1 bound for normalized theta-PSH potentials in Theorem 5.25.2 (FC59B7D406A3, source D9A05B95; individual page blob 83e75475a7ad0ef73cc92531c2e789ebaebcca8a, lines 6–12). Write \(V=\int_X dV\).
Let u,v be bounded theta-PSH potentials, \(A=\{u<v\}\), and \(0\le c<1\).
Suppose that on A
\[
 {\bf1}_A\mathrm{MA}_\theta(u)
 \le c{\bf1}_A\mathrm{MA}_\theta(v)+\eta
\]
for a finite positive Borel measure eta. Set \(\delta=\eta(A)\).
If \(0<\delta<m(1-c^{1/n})^n\), then
\[
 \int_X(v-u)_+\,dV
 \le \left[(\sup_X v-\inf_X u)_+V+K\right]
       (\delta/m)^{1/n}.
\]
If delta=0, the qualitative conclusion u>=v holds, even with only the original non-collapsing hypothesis. No optimal exponent, uniform-norm estimate, or extension to unbounded potentials is claimed. In particular this estimate does not follow merely from non-collapsing with zero infimum mass.

Proof. If A is empty, there is nothing to show. For any real b>1 put
\(w=P_\theta(bu-(b-1)v)\) and \(D=\{w=bu-(b-1)v\}\).
The obstacle is bounded and quasi-continuous; constants are competitors. The contact theorem 16.28.4 (45D3A8D823A8, source 50BC4236, lines 119–145) gives bounded w and contact support outside a pluripolar set. The convex combination \(b^{-1}w+(1-b^{-1})v\) lies below u everywhere by 5.24.3 (D1DAB1D38637, source 184DC935; individual page blob 0190e30e991e13d8e3f2cb13442113fadcafc280, lines 6–10). On D, ordered contact and the positivity of mixed bounded products give precisely the inequality at line 997:
\[
 {\bf1}_D[b^{-n}\mathrm{MA}_\theta(w)
 +(1-b^{-1})^n\mathrm{MA}_\theta(v)]
 \le {\bf1}_D\mathrm{MA}_\theta(u).
\]
All bounded Monge–Ampere measures here are finite and vanish on pluripolar sets. Restrict to D intersect A. If \((1-b^{-1})^n\ge c\), then
\[
 \mathrm{MA}_\theta(w)(D\cap A)\le b^n\delta.
\]
If also \(b^n\delta<m\), the contact measure has positive mass on D outside A. At a nonexceptional point there,
\(w=u+(b-1)(u-v)\ge\inf_X u\).
Thus \(\sup_X w\ge\inf_X u\). On A off the negligible exceptional set,
\[
 b(v-u)\le v-w
 \le(\sup_X v-\inf_X u)_+ + (\sup_X w-w).
\]
Integrating over A and using the normalized L1 bound gives
\(b\|(v-u)_+\|_1\le(\sup v-\inf u)_+V+K\).
The assumed strict threshold guarantees a nonempty interval
\[
 (1-c^{1/n})^{-1}<b<(m/\delta)^{1/n}.
\]
Taking the supremum of these numerical b values in the scalar inequality proves the claimed bound; no convergence of envelopes, no endpoint attainment and no interchange of limits is needed. For zero defect, b can be arbitrarily large; the same argument uses positive mass of each w instead of m. Then the almost-everywhere inequality implies the pointwise inequality by 5.24.3.

One may choose eta to be the positive part of the finite signed measure \({\bf1}_A(\mathrm{MA}_\theta(u)-c\mathrm{MA}_\theta(v))\). This is the smallest possible defect mass on A by the Hahn decomposition. For uniformly bounded u,v the constants are uniform, so any sequence of such defects tending to zero for fixed c<1 gives one-sided L1 stability. This statement does not require an assertion of uniform L-infinity stability.

Proposed addition: separate quantitative corollary after 16.28.56 or the definition of v_-; do not strengthen the hypotheses of the printed theorem. The subsequent exponential comparison discussion at line 1019 and relative classes are not refuted. Inputs: bounded contact, ordered contact, positivity of mixed products and normalized compactness. The contact theorem's antecedent uses smooth approximation in 16.28.2 line 57; no review of that approximation or its prerequisites is made here. All cited analytic inputs remain conditional in this audit.

## POME-RELATIVE-ENVELOPE-STRETCH-SEMIGROUP-001

Severity low; status verified conditional deduction. Lemma 16.28.63 permanent C172793BD93F, source 732C08AC, lines 1134–1155; definition 16.28.61 permanent 7EF949B941B4, source 1025E1CB, lines 1082–1100.

For any fixed smooth real theta and reference phi in PSH(X,theta), use the printed convention
\[
 {\cal A}_b(u,\varphi)
 =\{h\in{\rm PSH}(X,\theta):b^{-1}h+(1-b^{-1})\varphi\le u\}
\]
for b>=1, interpreting the b=1 condition as h<=u. Q_b denotes its largest member when nonempty (line 1094). Whenever b,s>=1, the following exact identity holds, with simultaneous existence:
\[
 Q_s(Q_b(u,\varphi),\varphi)=Q_{bs}(u,\varphi).
\]
More precisely the right side exists iff Q_b exists and the left side exists. To see this without subtracting infinities at common poles, suppose \(h\in{\cal A}_{bs}(u,\varphi)\). Put \(g=s^{-1}h+(1-s^{-1})\varphi\), which is theta-PSH, using the stated b,s=1 conventions. Then \(b^{-1}g+(1-b^{-1})\varphi\le u\), hence \(g\le Q_b\) and h is in \({\cal A}_s(Q_b,\varphi)\). Conversely any h in the latter family satisfies the defining inequality for \({\cal A}_{bs}\) by substitution. This is equality of the competitor sets, not just comparison of suprema. The two directions apply pointwise at poles since the expressions only use nonnegative convex coefficients and no undefined differences. Thus the asserted semigroup identity follows. In particular the first assertion of 16.28.63 follows exactly for a fixed reference, and the existence part does not require u<=phi. The condition \(Q_b\preceq\varphi\) in the printed relative-class conclusion still uses the stated order or a bounded translation.

A second consequence is that the all-real-scale condition in Definition 16.28.61 can be tested along any unbounded subset B of [1,infinity). If \({\cal A}_B\) is nonempty at one scale B>=b, a competitor h there yields
\[
 (b/B)h+(1-b/B)\varphi\in{\cal A}_b(u,\varphi)
\]
by exact substitution. Hence an unbounded set of nonempty scales suffices, independently of monotonicity of u-phi. In particular it suffices to test dyadic scales. This does not assert that finitely many scales suffice or that the limiting Q is nontrivial. The existing finite-rooftop argument 16.28.64 (46B23EB58AAB, source 644EC8A3, lines 1160–1183) is consistent with this identity; its counterexample to arbitrary countable rooftops is unaffected. No new external inputs are needed beyond the maximal-envelope construction at line 1094.

## Other reviewed direct steps

- 16.28.4–7, lines 119–219: fixed quasi-continuous weight before the bounded capacity limit; semipositive-background decreasing envelopes; finite truncation before unbounded contact exhaustion; disjoint rooftop partition assigning the common contact set once; fixed-point mass bound. These are conditional on the cited bounded-product and envelope inputs. The smooth approximation in earlier 16.28.2 is not reopened.
- 16.28.55, lines 944–971: the a-omega envelope is bounded from below, and ordered contact transfers its positive mass without requiring a uniform positive mass infimum. The exact background decomposition and finite-truncation restriction are consistent.
- 16.28.58–59, lines 1027–1075: scaling by t^n and smooth gauge invariance are identities of competitor sets. On a modification, the pushforward equality is first checked on the isomorphism locus and then uses polar-null measures on both sides, so infinite mass is permitted. Exact pullback, not an independent upstairs metric, is essential. Conditional on 13.14.3 and 5.43.18.
- 16.28.62–65, lines 1109–1210: changes of reference use the factor (b-1)C, finite rooftops use convex averaging, and the limit a->1 uses a uniform normalized L1 bound even though h_a varies. No sequential compactness of h_a is required: the L1 norm of (1-a)P_{theta,F}[h_a] tends to zero.
- 16.28.68–70, lines 1226–1286: the smaller-background competitor is the sum of an epsilon-theta potential and a delta-theta scaled envelope. The positive lower bound for each delta permits the scalar limit; it does not imply existence at delta=0.
- 16.28.72–73, lines 1295–1347: splitting off a smooth finite head gives the competitor for each stretch with b 2^{-N}<=1 (or b epsilon 2^{-N}<=1); the infinite mass and ideal assertions depend on 13.14.18–19, not independently certified here. No excluded approximation programme resumed.

No new confirmed error, proof gap, or full upstream certification. Two conditional deductions. Selected section 16.28, not entire; no other newly complete section. No builds, tests, CI, registry, source or published changes.
