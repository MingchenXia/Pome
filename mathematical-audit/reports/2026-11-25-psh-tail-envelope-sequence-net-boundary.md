# PSH tail envelopes: direct proof, net obstruction, and extension-proof qualification

Date: 2026-11-25. Production main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Audit-only; no changes to the reading edition, tags or external sources.

## Scope and immutable anchors

- SGPT integrated §5.14, Properties of plurisubharmonic functions:
  docs/sections/plurisubharmonic-functions--properties-of-plurisubharmonic-functions/index.html, blob e7d871122eca3eb7416ab8a993063cdc8d3987f3, physical mathematical lines 7–393, whole direct reading (upstream dependencies conditional).
- Foundations of pluripotential theory integrated §5.6, Maps of currents and local mass:
  docs/sections/complex-differential-forms-and-positive-currents--maps-of-currents-and-local-mass/index.html, blob 1d9d81f147a96878236944fcae54aeb8f6f58098, mathematical lines 7–165, whole direct reading.
- Current docs/index.html section numbers compared with SECTION_MATRIX.md: 747 distinct numbers in each, no differences, no duplicate matrix rows. Historical first visits are not asserted.

## POME-PSH-L1-TAIL-ENVELOPE-NET-OBSTRUCTION-001

Severity low; verified conditional deduction and proposed internal proof replacement. Corollary 5.14.8 (SGPT source 6A1C7D0B, permanent E23F3D6154AB, lines 129–175) is correct as printed for sequences. The following eliminates the two external GZ17 invocations at lines 146 and 168, conditionally on the elementary submean inequality, upper-envelope theorem, and the already stated uniqueness/discrepancy/countable-union results. It also proves that replacing sequences by arbitrary nets in the pointwise quasi-everywhere conclusion is false, even for uniformly bounded PSH nets.

### Direct proof of the sequence result

In a coordinate chart let B(x,r) be a Euclidean ball whose closure lies in the chart, and let a positive radius margin keep all B(y,r), for y near x, in one compact K in that chart. Write A_r u(y) for the volume mean over B(y,r). The submean inequality gives

    u_j(y) <= A_r u_j(y)
           <= A_r u(y) + ||u_j-u||_{L1(K)}/Vol(B(0,r)).

Finite chart covers of compact sets, with smaller interior balls, imply eventual local uniform upper bounds for the sequence; each finite initial part is also locally bounded above. The function A_r u is continuous on the smaller chart region: translation continuity of local L1 (or dominated convergence on the indicators of translated balls against |u|) proves this. Thus for v_N=(sup_{j>=N} u_j)^* we have

    v_N(x) <= A_r u(x) + sup_{j>=N} ||u_j-u||_{L1(K)}/Vol(B(0,r)).

For any fixed N, u_j<=v_N for j>=N. Local L1 convergence has an almost-everywhere convergent subsequence on each relatively compact chart, so u<=v_N almost everywhere and then everywhere by 5.14.6. Alternatively apply the order of distributions and uniqueness of PSH representatives. Let N tend to infinity in the upper estimate and then r decrease to zero. The submean inequality and upper semicontinuity give A_r u(x)→u(x), also when u(x)=-infinity. Consequently inf_N v_N=u everywhere. Proposition 5.14.5 identifies v_N with its raw tail supremum off a pluripolar set, and 5.14.7 takes the countable union of these sets. The desired pointwise limsup equality follows off that union. No external Hartogs/pointwise limsup theorem is needed for this deduction. The fixed-radius estimate also applies on a chart to directed L1-convergent nets for sufficiently late tails there; it is not a claim of a globally uniformly upper-bounded tail for an arbitrary net on a noncompact manifold.

### Sharp failure for nets

Let D be the unit disc, and index by the directed set of all nonempty finite subsets F of D, ordered by inclusion. For z in D put

    u_F(z)=max(-1, |F|^{-2} sum_{a in F} log(|z-a|/2)).

Each summand is nonpositive subharmonic, with its usual -infinity value at a. Thus each u_F is subharmonic, and -1<=u_F<=0. For all a in D,

    integral_D log(2/|z-a|) dA(z)
       <= integral_{|w|<2} log(2/|w|) dA(w) = 2 pi.

Consequently ||u_F||_{L1(D)} <= 2 pi/|F|. For every finite integer bound the index can be enlarged so that all later indices exceed that cardinality. Hence the original net tends to zero in L1(D), and in every finite Lp by boundedness. Yet for every z in D, all F containing the index {z} give u_F(z)=-1. Thus the pointwise net limit, and its directed limsup, are identically -1 everywhere. In particular the discrepancy with the L1 limit is not pluripolar. This uses no countability assumption, and no assertion of a monotone net.

For completeness, every tail's upper-regularized supremum in this example is identically zero: the tail contains a sequence of indices with cardinalities tending to infinity, whose functions converge to zero in L1, and the envelope is PSH, between that subsequence and 0. The order argument above applies. This isolates the failure to the raw pointwise identification, rather than the regularized envelope formula. It illustrates why one cannot take an uncountable union of exceptional sets in the sequence proof. Do not weaken the sequential hypothesis of 5.14.8 without a separate argument. No printed downstream theorem is refuted; any downstream invocation for a genuinely arbitrary nonmonotone net must instead justify its own pointwise step.

## POME-PSH-REMOVABLE-LOG-PENALTY-UPPER-BOUND-001

Severity low; proof gap / verified local repair proposed (not a false theorem).
Theorem 5.14.10 (source 1E88697D, permanent DAE812E1A818), proof step labeled 8621511D, lines 204–212, claims that phi+epsilon log|f|², assigned -infinity on Z, is PSH, and that this increasing family is locally uniformly upper bounded. The argument at the pole invokes only the submean inequality and has not yet stated the local upper-bound premise. Submean at the pole alone does not ensure upper semicontinuity. For the auxiliary assertion without that premise, take D, Z={0}, f(z)=z and phi=-log|z|² on D minus {0}. This phi is harmonic there. For 0<epsilon<1 the penalized function tends to +infinity at zero, while its assigned value is -infinity. This is not a counterexample to the theorem: it violates both alternatives of the theorem, and is a counterexample only to an unqualified auxiliary step.

Replacement: explicitly start this step under the local upper-bound hypothesis of alternative (2). Work on a smaller coordinate ball where |f|<=1 (rescale the nonzero defining function by a constant). At each point of Z, the logarithm tends to -infinity and phi is locally upper bounded. The penalized extension is therefore USC. Off Z it is PSH; restriction to any affine complex line is locally subharmonic or identically -infinity, and at each point of Z the submean inequality holds because the value is -infinity. The line criterion proves PSH (the extension is not identically -infinity on the chart). With log|f|²<=0 the family is increasing as epsilon decreases to zero and uniformly locally bounded above; its regularized supremum extends phi, including at zeros of f outside Z by USC and the submean property of phi on the open complement of Z. More explicitly, the equality there holds away from {f=0}; on {f=0} outside Z both PSH functions agree almost everywhere in a neighborhood, hence everywhere by 5.14.6. At Z the regularization has precisely the limsup of phi from the complement, since phi equals the envelope off Z and the raw penalized supremum on Z is -infinity. Alternative (1) first establishes the local upper bound and then invokes this qualified step.

The already recorded POME-PSH-CODIM2-DIRECTION-IMAGE-001 at line 237 is a separate issue: closed-ball truncation is not an analytic source for Remmert. Its 2026-11-16 proposed dimension/measure-zero repair remains unchanged, not counted again. Neither issue refutes codimension-two removability or bounded-above extension.

## Remaining direct checks and dependencies

§5.14: 5.14.1 uses a multiplier-ideal order estimate, not reopened; its conclusion also implies the null-set assertion in 5.14.4. 5.14.2 upper envelope and decreasing-net statements are conditional on earlier local results. 5.14.3 already has the separate POME-CHOQUET-TOPOLOGICAL-REPAIR-001 countable-base replacement; not new. 5.14.5 discrepancy, 5.14.6 representative order, and 5.14.7 weighted countable union (local Josefson input) checked. In 5.14.14 the reduction to one variable can be justified: a pole on a fixed torus-invariant punctured-disc slice forces that entire slice to be identically -infinity (a nontrivial radial subharmonic function has finite convex logarithmic profile). Vary the coordinates successively to force the whole polyannulus to be identically -infinity, contradiction. The external Kiselman principle (5.14.15) and BT balayage (5.14.21) remain named inputs at their present location; no global assertion that an internal equivalent is absent. The epsilon gluing proof in 5.14.16 and boundary-limsup replacement in 5.14.20, and precise local domination hypotheses in 5.14.22 checked directly, earlier gluing/BT inputs conditional.

§5.6: checked fixed compact test cutoffs, bidegree shift and even real dimension sign in 5.6.1; local submersion pullback, differentiation and chart gluing in 5.6.2; product-measure formula and Borel multiplication in 5.6.3–4; canonical local potentials and transverse divisor pullback in 5.6.5–6; trace factor (n-p)! and Riemannian volume normalization in lines 135–165. No new demonstrated gap in that section. Ordinary local coefficient mollification here is the elementary distribution operation, not the excluded Demailly approximation programme. Earlier §§5.2–5.5 current and potential results are inputs, not transitively certified.

No tests, builds, CI, production changes, or complete transitive proof-chain certifications. All user-excluded programmes remain deferred-by-user, not solved. Whole direct reading does not mean independent proof of every cited theorem.
