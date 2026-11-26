# Classical common-collar energy and decreasing directed families

Date: 2026-11-26. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit parent: 840ee1c31632b768f8c22a885e95bb696ca843eb.

## Source and coverage

* Entire mathematical portion of §7.29, physical lines 7–187 of
  `docs/sections/classical-products-with-controlled-unbounded-loci--classical-products-with-compact-unbounded-loci/index.html` (blob 65666651048e9ada933a763b7d381766f8b43965).
  Lemma 7.29.1 source demailly-complex-geometry:828A36D4 / permanent
  438B9224299E, lines 10–44; Theorem 7.29.5 source B0311B48 /
  8FBB0E4DE397, lines 46–135; Lemma 7.29.6 source A5A5FB86 /
  7EADA0AAC4F2, lines 137–173; radial avoidance, degree endpoint
  and displayed duplicate equation fragment, lines 174–187.
  Prior selected and historical reviews remain recorded; no first-ever
  visit assertion.
* Selected downstream §7.31, lines 27–79,
  `docs/sections/classical-products-with-controlled-unbounded-loci--collars-relative-to-the-support-of-the-base-current/index.html` (blob 86de377d6e6f17fc1a08a6e789a681ddfaabfac5).
  Theorem 7.31.2 source 6CBD358C / F6EE68FA9FDA; Corollary 7.31.3
  source AE90937D / CF64F301AEAF; Corollary 7.31.4 source 4876F9E5 /
  EBA900FA96EF. Lemma 7.31.1, source 45184D89 / FDDB630F0AA9,
  invokes the excluded curvature-error regularization argument;
  its proof and that programme are deferred-by-user, not certified.
  No whole §7.31 claim.
* Contextual §5.26 lines 7–44,
  `docs/sections/plurisubharmonic-functions-and-singularities--uniform-exponential-integrability/index.html` (blob d961c0412577bb6abdb8455efc44e2f35760c55c), Lemma 5.26.2
  source 2C0C5ADC / 88C7A8DCE36E. The qualitative local Skoda
  integrability premise is explicit. The weighted negative sum has
  bounded L1 norm by 5.26.1; its exponential integrals contradict
  that premise. No attempt to complete the excluded upstream programme
  or establish a new Skoda proof; not counted as a whole proof audit.

## POME-CLASSICAL-COLLAR-SYMMETRIC-ENERGY-001

Severity low; verified conditional deduction, not a printed theorem error.
Proposed addition after 7.29.5, especially Steps 4–6 (lines 82–130).

Use the exact coordinate-ball setting of Lemma 7.29.1 and Theorem
7.29.5. Let T be closed positive of bidimension (p,p), let
0 <= r <= p-1, and let all potentials under consideration be
nonpositive psh, defined near the closed ball, equal to A psi on a
common boundary collar, where psi=|z-a|^2-R^2 and omega=dd^c psi.
Set M_T=int_B T wedge omega^p. Write

\[
 E(f_0,\ldots,f_r)=
 \int_B f_0 P_T(f_1,\ldots,f_r)\wedge\omega^{p-r}.
\]

All terms are finite by 7.29.5 Step 4; the mass of each unweighted
product in this trace normalization is A^r M_T (Step 3, line 80).

**Claim.** E is fully symmetric, including the weight, not merely
in its Hessian entries. If u_k <= v_k for every k and both tuples
have the same collar, then

\[
 E(v_0,\ldots,v_r)-E(u_0,\ldots,u_r)=
 \sum_{k=0}^r\int_B (v_k-u_k)
 P_T(v_0,\ldots,v_{k-1},u_{k+1},\ldots,u_r)
 \wedge\omega^{p-r}\ge0.
\]

The omitted-factor list has r entries; all differences are defined
almost everywhere for the corresponding trace since each weight is
integrable for it. In particular if 0 <= v_k-u_k <= epsilon_k
off their common pole sets (or equivalently the order inequalities
u_k <= v_k <= u_k+epsilon_k hold everywhere), then

\[
 0\le E(v)-E(u)\le A^r M_T\sum_{k=0}^r\epsilon_k.
\]

**Proof.** For smooth collar potentials, permute Hessian factors
and exchange a weight and a Hessian by the ordinary smooth
common-collar identity (7.29.4) with the other factors and the
closed power of omega included in the base current. This base has
bidimension (1,1) when r>=1. For r=0 symmetry is vacuous.
For arbitrary collar potentials use the coordinate-ball smooth
decreasing majorants already constructed in Step 1, line 66,
with their exact common collar. The weighted convergence of
7.29.5, applied to each permutation of the finite tuple, gives
convergence of the currents. A compact cutoff equal to one off
the collar gives convergence of the corresponding whole-ball
integrals, since the remaining integrals are identical fixed
finite collar integrals. Thus the smooth permutation identities
pass to the limit. This is a corollary of the completed printed
sequential statement, not an ingredient in its induction.

Telescope E by replacing coordinates in order 0 through r. By
symmetry put the changed coordinate in the weight position in
both terms. The other factors are identical, giving the displayed
identity. Positivity gives its sign; the exact mass from Step 3
gives the bound. No subtraction of infinite integrals occurs.
This uses only the local coordinate convolution already present
in the classical product proof, not Demailly regularization.

## POME-CLASSICAL-COLLAR-DIRECTED-CONTINUITY-001

Severity low; verified conditional deduction. Proposed addition to
7.29.5 (lines 52–56, 130) and 7.31.2 (lines 28–32, 46).

The simultaneous decreasing continuity assertions remain valid for
arbitrary directed decreasing nets of psh functions, provided the
infimum is pointwise the specified psh limit and the printed
common-boundary hypotheses hold for the limit family. In particular
no countable cofinal subset of the index set is required.

**Proof.** Work on a second-countable coordinate neighborhood or
on a relatively compact open set in the printed cover. Fix a
finite family u_{l,i} of decreasing nets over one directed set I.
For every rational a and family member l,

\[
 \{u_l<a\}=\bigcup_{i\in I}\{u_{l,i}<a\}.
\]

The sets on the right are open by upper semicontinuity. The union,
an open subspace of a second-countable space, is Lindelof.
Select countably many indices giving this same union. Over the
finitely many l and countably many a obtain a countable list of
anchor indices j_k (repetitions allowed). If the conclusion for a
given current did not hold along the original net, some weak
neighborhood of the asserted limit would be missed by an index
in every tail. Inductively take a bad index i_k dominating i_{k-1}
and j_k; directedness supplies a common upper bound before choosing
a bad index in its tail. For each l, u_{l,i_k} decreases and its
pointwise infimum is u_l by the selected strict sublevel covers.
The printed sequential theorem now implies convergence of the
corresponding weighted or unweighted currents along i_k, a
contradiction. Apply locally and use a finite partition on the
support of each test form. The bidimension restrictions are
unchanged; no net compactness theorem and no exchange of limits
with varying measures is used.

For 7.31.2 this is conditional on the printed sequential result,
whose 7.31.1 smoothing premise remains deferred-by-user. The
argument does not revisit or strengthen that premise. The statement
requires the actual pointwise decreasing limit; it is not a claim
about arbitrary nets or a merely almost-everywhere convergence
hypothesis.

## Other direct checks and dependencies

The compact support in 7.29.1's smooth-weight exchange removes
the boundary derivative; r+1 <= p is precisely the condition for
the weighted estimate. In 7.29.5 Step 4 the lower semicontinuous
negative truncation is tested against positive measures; Step 5
uses the opposite upper semicontinuous inequality. Step 6 replaces
one weight by a smooth majorant, then uses the exchange with a
base of bidimension (1,1); the order of smoothing limits leaves
at most r-1 Hessian factors at each nontrivial induction step.
The fixed collar permits whole-domain testing, not a bare weak
convergence claim on a noncompact open ball. The sequential
compactness argument there is local for sequences, not a
sequential compactness assertion for arbitrary nets.

The unitary incidence estimate in 7.29.6 has the expected
2s angular powers and one radial power, including s=0. The
compact projection argument establishes Borel measurability.
The previously logged sharpness and top-degree-weight
counterexamples are not new findings. The radial avoidance proof
at lines 174–183 uses a Lipschitz map and the null H^1 hypothesis.

For 7.31.2 the collar modification is only near supp T; extensions
by zero introduce no derivative at points outside this closed
support. For 7.31.3, the cutoff equals -psi on the inner region,
so dd^c chi=-omega there, and integration by parts gives the sign
of the collar error in its displayed formula (line 61). The
q<=n-1 bound permits a base of bidimension n-1, and local weak
boundedness of positive dd^c V_k traces gives the asserted
uniform mass bound. The cited smoothing premise is not certified.
7.31.4's p=0 caveat and Hausdorff dimension-to-null-measure
implication have the correct degree; the separate support and
Hausdorff results invoked are not transitively certified here.

Outstanding: upstream bounded-product, smooth common-collar and
analytic-strata proofs not newly certified; excluded
regularization/curvature loss programmes deferred-by-user.
No new confirmed false statements or demonstrated substantive
proof gaps. No tests/build/CI, no production edits. Matrix has 747
distinct section rows; the 33 Chapter 7 locators were compared
against the current actual chapter page, with no mismatch. Full
TOC comparison not rerun to completion in this increment.
