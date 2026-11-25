# Hopf fiber spectral deficits and Radon monotone-net limits — 2026-11-25

Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. This is a mathematical audit of the public integrated edition, not an edit to a theorem, registry, permanent tag or source. Demailly approximation/regularization and the specified Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain **deferred-by-user**.

## POME-HOPF-FIBER-SPECTRAL-DEFICIT-001

**Severity/status:** low / verified conditional deduction (not a false theorem, not a bounded-potential proof certificate).

**Anchors:** docs/sections/unbounded-mass-on-hopf-manifolds/index.html, blob f53618e8d808de21687ff9166971cb9302ea8cfb. Proposition 23.1.4, source non-kahler-pluripotential-theory:9156D54D, permanent DDEBFFAFCD1F, lines 73–100; equation 23.1.5 source 97C333D9/permanent C46F0B405DC2; equation 23.1.11 source 746F570C/permanent 27E901CC3829, lines 188–201; Proposition 23.1.38 source 48EA3D0A/permanent E42306969D71 and equation 23.1.39 source E385367F/permanent 18B65325175F, lines 675–732.

Let X be the standard Hopf threefold with contraction e^(-1), omega=alpha+beta as printed. Set nu=omega^3/6, and A the fiber Haar average. For a smooth real u, let M(u)=integral_X (omega+dd^c u)^3 (no positivity is necessary for the identity). The printed mass formula is
\[
 M(u)-6=6\int_X|u_w|^2\,d\nu.
\]
The smooth formula follows from the integrated threefold identity: the linear term vanishes by dd^c(omega^2)=0; the cubic term vanishes by Stokes; dd^c omega=-alpha^2 gives the quadratic term 3 integral du wedge d^c u wedge alpha^2. On a fiber beta=2 dA_E, so this is the displayed formula.

The fiber characters are chi_(p,q)(w)=exp(2 pi i p Re w+i q Im w); their eigenvalues for -partial_w partial_bar_w are lambda_(p,q)=pi^2 p^2+q^2/4. Although a local w changes by a translation depending on the base, character projections are intrinsic: define
\[
 P_{p,q}u(x)=\int_E u(\tau_a x)\overline{\chi_{p,q}(a)}\,dA_E(a).
\]
Here tau_a is the global scalar action and the measure is Haar probability. This is a smooth function transforming by chi_(p,q) along the action. P_(0,0)=A. Distinct characters are mutually orthogonal in L²(nu), by invariance and Haar orthogonality. The fiberwise Parseval formula integrated against omega_FS² (nonnegative sums, ordinary Tonelli) gives
\[
 M(u)-6=6\sum_{(p,q)\ne(0,0)}\lambda_{p,q}\|P_{p,q}u\|_2^2,
 \qquad \|u-Au\|_2^2=\sum_{(p,q)\ne(0,0)}\|P_{p,q}u\|_2^2.
\]
The lowest eigenvalue is 1/4, occurring only at (0,+/-1), and the next is 1, occurring only at (0,+/-2) (pi²>1). Let P1=P_(0,1)+P_(0,-1). Subtraction proves the sharp stability refinement
\[
 \boxed{M(u)-6-\tfrac32\|u-Au\|_2^2
 \ \ge\ \tfrac92\|u-Au-P1u\|_2^2.}
\]
Equality holds precisely when all projections outside (0,0),(0,+/-1),(0,+/-2) vanish. In particular the original Poincare inequality is an equality iff u-Au is in the first eigenspace. This is an exact characterization of all smooth equality cases; it does not assert that arbitrary eigenmode sections preserve positivity.

Sharpness under strict omega-psh positivity: choose a nonzero real smooth rho compactly supported in the affine base chart. The function u=delta rho(xi) cos(2 Im w), extended by zero, is globally smooth. Only the second modes occur and the two sides of the new inequality agree with nonzero norm. For sufficiently small nonzero real delta, omega+dd^c u is positive by compactness. No larger coefficient than 9/2 can work. The analogous first-mode function proves the original 3/2 coefficient.

More generally, if Lambda is any positive eigenvalue, let P_<Lambda be the finite sum of projections with lambda<Lambda (including A). Then
\[
 M(u)-6 \ge 6\sum_{0<\lambda_{p,q}<\Lambda}\lambda_{p,q}\|P_{p,q}u\|_2^2
       +6\Lambda\|u-P_{<\Lambda}u\|_2^2 .
\]
The tail coefficient 6 Lambda is optimal by the same compactly supported character construction, using the real part of a character of eigenvalue Lambda. Equality is exactly the absence of frequencies above Lambda. In particular near-saturation of 23.1.39 controls the distance to the full smooth equality subspace without any assumption of a basewise trivialization of the elliptic bundle. The projection onto that subspace is not claimed to send positive metrics to positive metrics.

**Proposed addition/dependents:** add a smooth corollary to 23.1.38, with this spectral refinement and equality cases, not a replacement of the valid printed result. It strengthens the interpretation of the almost-minimal-mass discussion after 23.1.40. No conclusion about capacity convergence or non-pluripolar measures follows just from this L² estimate. The bounded extension of 23.1.38 cites 5.32.1; we record that dependency as deferred-by-user, and do not reopen it. The present smooth proof does not use it. The earlier sharp leading constant, smooth affine nullspace and fiber/trace-free variance findings are not new findings here.

## POME-RADON-MONOTONE-NET-ESSENTIAL-SUP-001

**Severity/status:** low / verified deduction (not a false theorem or demonstrated proof gap).

**Anchors:** docs/sections/measures-and-distributions--radon-measures-and-integration/index.html, blob f0086e0d7fa46b8d1756eebb839b0ba14e663863. Definition 2.2.1 source foundations-of-pluripotential-theory:4720F063/permanent 901C72102EF9, lines 10–16; Proposition 2.2.2 source B0C4661C/permanent D0882F84DCFC, lines 40–54; Proposition 2.2.3 source 34CC47F9/permanent 9CB694815500, lines 56–99. The printed sequence restriction and finite-subset-net counterexample are correct. The following gives precise positive replacements, not an unqualified net version of that statement.

### Essential supremum theorem

Let (S,mu) be any sigma-finite measure space, (I,<=) a nonempty directed set and f_i:S->[0,infinity] measurable with f_i<=f_j whenever i<=j. There exists an increasing sequence of indices i_k (not necessarily cofinal) such that g=sup_k f_(i_k) is an essential supremum of the family and
\[
 \int g\,d\mu=\sup_{i\in I}\int f_i\,d\mu.
\]
If the pointwise supremum f is measurable and integral g is finite, then integral f equals this supremum iff f=g mu-a.e. If integral g is infinite, equality of the integrals is automatic for measurable f, without requiring pointwise/essential agreement.

Proof. The zero-measure case is immediate. Otherwise partition S into countably many sets E_m of finite measure, and choose a probability P equivalent to mu by normalizing the strictly positive integrable density whose value on E_m is 2^(-m)/(1+mu(E_m)). Let h(t)=t/(1+t) with h(infinity)=1. Write a=sup_i integral h(f_i) dP. Choose j_k with integrals at least a-1/k, and inductively choose i_k above both j_k and i_(k-1), using directedness (take i_1=j_1). Put g=sup_k f_(i_k). Ordinary sequence monotone convergence gives integral h(g)=a. For any fixed i, max(f_i,f_(i_k)) is dominated by a member of the net by directedness, so its h-integral is <=a. Taking the increasing sequence limit yields integral h(max(f_i,g))<=a. Since h is strictly increasing on the extended nonnegative interval, the nonnegative difference from h(g) has integral zero, hence f_i<=g P-a.e. and thus mu-a.e. The exceptional null set may depend on i. If a measurable G is any essential upper bound, then g<=G a.e. by taking only the countable union of exceptional sets for i_k. This proves the essential supremum assertion, with no uncountable union of null sets. Ordinary monotone convergence now gives integral g = lim_k integral f_(i_k) <= sup_i integral f_i, while the opposite inequality follows from the essential upper bound. For measurable f>=g, if integral g<infinity, equality is equivalent to f=g a.e., as asserted. The finite-subset example in line 99 has g=0 and f=1.

### Pointwise lower-semicontinuous version

Let S be a topological space with a positive Borel measure inner regular by compact sets on open sets (in particular a Radon measure as in 2.2.1). For any increasing directed net of nonnegative lower semicontinuous functions f_i, its pointwise supremum f is lsc and
\[
 \boxed{\int f\,d\mu=\sup_i\int f_i\,d\mu.}
\]
No sigma-finiteness, countable cofinality, or uniform boundedness is required.

Proof. For any open superlevel U={f>t}, the open sets U_i={f_i>t} increase with the directed order and cover U. Every compact K subset U is contained in finitely many U_i and hence in one U_j by directedness. Consequently inner regularity gives mu(U)=sup_i mu(U_i), including infinite values. To pass from levels to integrals without exchanging an uncountable supremum with an integral, fix N>=1 and k>=1, set delta=2^(-k), and take the finite simple function s=delta sum_(l=1)^(N*2^k) 1_{f>l delta}. For each threshold l delta, choose i_l with mu(U_(i_l)) arbitrarily close from below to mu(U), or arbitrarily large if that measure is infinite. Choose a common upper index j. Then f_j>=delta sum_l 1_{f_j>l delta}, and integral f_j is at least the sum of the corresponding finitely many measures multiplied by delta. Thus sup_i integral f_i>=integral s (the infinite term case follows by an arbitrarily large lower bound). Let k grow with fixed N: the simple functions tend to min(f,N) pointwise and are bounded above by f; Fatou gives integral min(f,N)<=sup_i integral f_i. Then N->infinity by sequence monotone convergence. The reverse inequality is immediate.

For a second-countable S, there is moreover an increasing sequence of indices whose pointwise supremum is f: for each rational t>=0 choose a countable subcover of {f>t} by {f_i>t} using second countability; enumerate the resulting countably many indices, choose successive common upper bounds, and use all rational superlevels. If all levels are empty take a single index. This sequence is **not** asserted to be cofinal. The dual decreasing upper-semicontinuous version holds under an integrable initial upper bound, by restriction to a tail and subtraction from that bound when it is continuous; more generally if the differences are lsc. We do not assert it for arbitrary measurable nets.

**Proposed addition/dependents:** add these two qualifications to the warning after 2.2.3, preserving its counterexamples and all sequence results. Particularly relevant to later net arguments in weak convergence, envelope and capacity theory. No specific downstream theorem has been newly refuted or fully certified.

## Actual coverage

- §2.2 Radon measures and integration, physical lines 6–247 (all mathematical text): compact exhaustion, regularity localization for locally finite measures, support, sequence MCT/Fatou/DCT, Vitali example, Jensen supporting slopes, image measures, countability, pi-lambda theorem, finite/sigma-finite product construction, separable Borel products, completion, signed total variation and Jordan decomposition were directly checked. No new error established. Standard underlying measure axioms and Lebesgue measure construction not independently reconstructed here.
- §23.1 Unbounded mass on Hopf manifolds: selected physical lines 28–100, 176–201, 675–905, smooth mass identity, radial/Fourier normalization, fiber Poincare and positive flux; NOT whole section. Bounded approximation citation recorded, not audited. The heat-concentration construction and shrinking-defect classification were not reviewed here.
- §24.13 Questions from global pluripotential theory, docs/sections/questions-from-global-pluripotential-theory/index.html, blob 3ec2a57565f616b8e5dc19284561312415001270, physical lines 6–52: read all seven printed problem/conjecture statements and accompanying context, including trace, numerical dimension and partial Okounkov bodies. No solution claimed. Regularization-related problems 24.13.2 and 24.13.7 remain recorded and deferred; no attempt to reopen their excluded prerequisites. This is whole problem exposition, not whole proof certification.

The actual current docs/index.html table of contents was compared against SECTION_MATRIX.md: 747 numbered sections, 747 distinct rows, zero missing or duplicate IDs. Historical first visits remain unreconciled where stated; this run adds one whole direct mathematical reading, one whole problem-exposition reading and one selected partial reading, two classified deductions, zero newly confirmed printed errors, zero demonstrated new proof gaps, zero complete transitive proof-chain certificates. No build, tests, CI, source, registry, tag, main or site edits.
