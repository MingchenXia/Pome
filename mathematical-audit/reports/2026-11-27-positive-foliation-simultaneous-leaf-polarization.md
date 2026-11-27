# Simultaneous integral polarizations for compact submanifolds tangent to a positive foliation

Date: 2026-11-27. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.

Finding **POME-FOL-SIMULTANEOUS-TANGENT-POLARIZATION-001** — low / verified conditional deduction, not a printed error. The argument uses the printed movable tensor-slope input and Kähler Hodge theory; it does not prove those inputs, the leaf quotient existence theorem, or rational connectedness.

## Exact anchors and direct coverage

All paths below are under the immutable main revision above.

* `docs/sections/holomorphic-forms-and-positive-foliations/index.html`, blob 5279e4ea52ab1eb2662dd83802bc132671729c1b, mathematical lines 7–84. Lemma 9.75.1 (source cao-paun-foliations:9588EA1E, tag 597700D273A6), lines 9–16; Lemma 9.75.2 (source 1D5DE36B, tag B52F345AB247), lines 21–28; Theorem 9.75.3 (source D94BC8B0, tag CDF6A16B105C), lines 33–72, especially 53–69. Corollary 9.75.4, lines 77–84.
* `docs/sections/from-local-leaves-to-a-meromorphic-fibration/index.html`, blob 285a6dbc3d2aeddc105f931a2377cc90d2d101de, mathematical lines 8–27, all read. The explicit Ou cycle-space lemma remains external.
* `docs/sections/tangent-slopes-and-covering-rational-curves/index.html`, blob 88c8dc4651dc7d9cd21609d3d453521f97e0190d, mathematical lines 8–58, all read. Lemma 9.76.1 (source AA1A5BE2, tag 4F2E71913C12); Corollary 9.76.2 (source 0B126172, tag 8876081BAAEC). The earlier ramification finding is not a new result.
* `docs/sections/conormal-positivity-of-an-analytic-germ/index.html`, blob 8884dd6b27094e69d54d97004ffa1bd81558c6b8, Theorem 9.73.1 tag E76BA49374E5, selected lines 8–32, 40–74: conditional check of blowup class coefficients, residual divisorial sign and tautological curvature; the extension/positivity input at 34–37 is not reopened. No full coverage claim here.
* `docs/sections/tensor-products-and-involutivity/index.html`, selected lines 7–44, Proposition 10.107.1 tag BB9ADDF87BD1 and Corollary 10.107.2 tag 1BF160484066: tensor semistability explicitly conditional on the cited Kähler/movable theorem.

## Deduction

Let X be compact Kähler and F a saturated subsheaf of T_X of positive minimum slope with respect to a movable class, as in Lemma 9.75.2. Fix any smooth compact Kähler modification X' of X, with induced saturated distribution F'. The identity modification is allowed. The assertion below concerns compact connected smooth complex submanifolds i:W -> X' whose tangent bundle is contained in F' on a dense open subset of W where F' is a subbundle; alternatively it concerns smooth fibers of a resolved fibration when this tangent condition holds. No assertion about singular fibers or existence of such submanifolds is needed.

There is a single Kähler form a on X' and a single integral cohomology class c in H^2(X',Z) such that for every such W, i^*c in real cohomology equals N[i^*a] for a fixed positive integer N. Thus every W is projective, and for k=dim W>0,

    N^k integral_W (i^*a)^k = <(i^*c)^k,[W]> is a positive integer.

In particular, this is a simultaneous lattice-valued volume statement for the chosen a, not a claim that the original prescribed Kähler class is rational.

Proof: Lemma 9.75.2 and its modification clause give the vanishing of every holomorphic two-form on the induced distribution on its bundle locus. By Lemma 9.75.1 choose a and a holomorphic two-form tau on X' such that [a+tau+conjugate(tau)] is rational. Take one denominator N and an integral lift c of N[a+tau+conjugate(tau)] in real cohomology (torsion choices are irrelevant). For every W the pullback i^*tau vanishes on the indicated dense open set, hence everywhere by holomorphicity. Therefore i^*c=N[i^*a] in real cohomology. It is a positive integral (1,1) class, so the integral projectivity criterion gives a positive holomorphic line bundle on W and projectivity. Evaluation of the kth cup power on the integral fundamental class proves the displayed quantization. The choice of a,N,c is independent of W. If W is a smooth fiber of a proper submersion with connected base, these cup-power integers are constant on that base, by differentiable local triviality, with no need to choose global holomorphic polarizing bundles. The same argument for k=1 is valid, even when the two-form restriction vanishes for dimension reasons.

This improves the ordering of the projectivity step in Theorem 9.75.3: once a compact Kähler resolved leaf fibration is available, its smooth fibers satisfying the tangent condition are projective already, before the relative MRC construction. The proof does not show that the integral class on X' is of type (1,1) on X', or that one holomorphic line bundle on X' polarizes all fibers. The class-C model, relative quotient, deformation of uniruledness, projective BDPP and relative-adjoint inputs are still needed for the printed rational-connectedness proof. Proposed correction: none required; optionally record the above corollary after Lemma 9.75.2 and use the earlier projectivity step as available. Affected context: Theorem 9.75.3 and its smooth leaf models, not a new proof of Corollary 9.76.2.

## Other direct checks and remaining obligations

In 9.74 the normal quotient is exactly (v,w) -> w-v, with diagonal kernel, as stated. The pushforward of the fiber cycles to the second factor is necessary: cycles in the relation itself remember the first coordinate. The irreducible leaf/support and quotient existence claims rely on the explicitly retained analytic-graph lemma, not on this elementary tangent calculation. In 9.75.3 the determinant degree comparison is justified conditionally on neatness: saturation adds an effective divisor, the r-exceptional contribution pairs to zero with the pulled-back functional, and the determinant of the rank-h quotient has degree at least h times its positive minimum slope. The multiple-fiber correction m-1 has the stated sign; s-exceptional contributions pull back to p-exceptional divisors. In 9.76.1 the determinant map has degree at least 2 and the common curve class argument avoids taking a simultaneous generic parameter for uncountably many currents. The cone-duality input remains conditional. Section 9.76 has a known prior selected review; no historical first-visit assertion.

Coverage: three whole current direct conditional sections 9.74–76; selected 9.73 and 10.107. Current table of contents and coverage matrix both contain exactly 747 distinct section IDs; their sets coincide. Historical status remains unreconciled where appropriate. No new confirmed printed error or demonstrated proof gap; one conditional deduction; no complete upstream certification. The designated Demailly approximation/regularization, dedicated Bergman/L2/OT, multiscale and positivity-loss proof-completion programmes remain deferred-by-user. No build, tests, CI or production edits.
