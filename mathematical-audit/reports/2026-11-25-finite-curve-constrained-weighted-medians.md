# Nearest pullback curve models: constrained weighted medians; elliptic rotation

Date: 2026-11-25. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit parent: 6cf7eafc02bb79a56252ab53addaa99f617e92ec.
Finding **POME-CURVE-FINITE-CONSTRAINED-MEDIAN-001** — low / verified conditional deduction, not a printed theorem error. Proposed addition to Proposition 18.24.2 and Example 18.24.4. Corollary 18.24.3 inherits it after division of distances by d. The 2026-10-24 sharp retraction norm and degree-two threshold (POME-CURVE-FINITE-RETRACT-SHARP-001) are prior results, not new findings.

## Exact constrained nearest-point problem

Use the finite surjective holomorphic map r:C'→C of connected compact Riemann surfaces, degree d, and smooth real backgrounds beta and sigma=r*beta, base area A>=0, as in 18.24.1–4. Conditional on the printed polar-measure classification 13.29.1 and weighted pullback lemma 5.43.16, a model q upstairs corresponds to a positive polar measure mu of mass <=dA. Its distance to a pulled-back model with base polar measure nu is ||mu-r*nu||_TV; admissibility means nu>=0 polar and nu(C)<=A. Unlike the arithmetic averaging retraction, the nearest point is a constrained weighted median, including at branch values.

Set rho=r_*mu. If rho=0 the unique minimizer is nu=0. Otherwise partition C into Borel pieces with Borel inverse branches x_i(s), one for each distinct point of each fiber. This is obtained by a countable covering of the unbranched locus by evenly covered disks, disjointifying the disks in enumeration order, and adding the finitely many singleton branch values. Let e_i(s) be the positive ramification multiplicity, with sum_i e_i=d. The restrictions of mu to these sheets, pushed forward to C, have nonnegative densities a_i(s) with respect to rho, with sum_i a_i=1 rho-a.e. (assign zero to unused branches). This follows directly from Radon–Nikodym on the disjoint pieces, not a general disintegration theorem.

Any admissible nu has decomposition f rho+nu_s, with nu_s singular to rho. The pullback of nu_s is supported on the inverse image of a rho-null set, which is mu-null and also r*(f rho)-null, by the weighted pullback formula. Therefore
\[
 \|\mu-r^*\nu\|_{\rm TV}
 = \int_C \sum_i |a_i(s)-e_i(s)f(s)|\,d\rho(s)+d\,\nu_s(C).
\]
Deleting nu_s strictly improves the objective unless nu_s=0 and never violates the budget. Conversely any measurable f>=0 with integral f d rho<=A gives an admissible polar measure, since rho is polar by 5.43.16. Thus no nearest point has an additional singular part. This covers atomic and nonatomic polar measures.

Write b_i=a_i/e_i and G_s(t)=sum_i e_i |b_i-t| for t>=0. Each b_i belongs to [0,1]. Clipping t at max_i b_i strictly decreases G_s where it changes t, so every minimizer can be taken with 0<=f<=1 (indeed all minimizers have this property a.e.). Away from the finitely many breakpoints in t,
\[
 H_s(t)=-G'_s(t)=2\sum_{i:b_i(s)>t}e_i(s)-d.
\]
This is nonincreasing, integer-valued and measurable in (s,t). Since G_s(0)=1,
\[
 G_s(f)=1-\int_0^f H_s(t)\,dt.
\]
For each positive integer j in {d,d-2,...} define L_j(s)=Leb{t>=0:H_s(t)=j}, M_j=int L_j d rho. These are measurable (finite sums of lengths between ordered breakpoints), finite, and ordered vertically by decreasing j. The exact optimal distance is
\[
 \boxed{\rho(C)-\max\{\sum_{j>0}j\,c_j:\ 0\le c_j\le M_j,\ \sum_{j>0}c_j\le A\}.}
\]
Here j ranges only over the indicated positive slopes. To prove the lower bound, for any f the amount of each positive-slope layer included is at most M_j and their total at most A; including zero/negative slopes cannot improve the benefit. For the upper bound, fill layers in decreasing j order, stopping when A is exhausted or no positive layer remains. The finite linear optimization is solved by this greedy rule, by transferring any resource from a smaller j to an unfilled larger j. Select all higher layers at every s and the same fraction c_j/M_j of the marginal layer at every s (skip zero M_j), taking the initial part of that layer in t. Set f(s) to the resulting total layer length. Monotonicity of H_s makes these selected intervals an initial interval [0,f(s)] up to endpoints. This is measurable, spends precisely the selected budget and attains the bound. No compactness assumption on the polar model space is required.

Equivalently there is a multiplier lambda>=0: choose lambda=0 if the positive layers fit, otherwise the positive slope of the marginal layer (at an exact boundary either adjacent admissible threshold works; A=0 can use lambda=d). A function f is optimal iff
\[
 f(s)\in \arg\min_{t\ge0}(G_s(t)+\lambda t)\quad\rho\text{-a.e.},\qquad
 \int f\,d\rho\le A,\qquad \lambda(\int f\,d\rho-A)=0.
\]
The construction above satisfies these conditions. Necessity for every optimizer follows by subtracting the attained dual bound: the objective gap is the sum of the integral of the nonnegative pointwise minimizing gap and the nonnegative complementary-slackness gap. For lambda=0 the pointwise condition is exactly a weighted median interval (weight e_i); the smallest weighted median is the sum of all positive layer lengths. Thus ordinary independent medians are feasible precisely when the integral of the smallest weighted median is <=A. If it exceeds A, the budget is binding and the constrained threshold construction is needed.

Example showing the constraint is genuine: r(z)=z^3, A=1, choose two different points above 1, and place mass 3/2 at each, zero at the third. The upstairs polar mass is 3, hence admissible. Unconstrained fiber median is base mass 3/2, violating the base budget 1. The admissible nearest base mass is 1 at 1 (any other fiber only increases the distance); distance is 2, whereas the unconstrained median would give 3/2. The example of 18.24.4 with mass 1 on just one sheet has smallest median zero, nearest distance 1; its averaged distance is 4/3 as printed. For an ideal model mu is atomic, hence rho and f rho are atomic: a nearest point in the pullback space can be chosen ideal, and in fact every nearest point is ideal by the no-singular-part assertion. Conversely no claim of a canonical continuous nearest-point selection or uniqueness in general is made.

## Exact anchors and coverage

All paths below are in main at the SHA above, in the integrated continuous reading edition. Whole direct means every mathematical paragraph read, not full transitive proof certification. Historical first visits not asserted.

- §18.23, docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--finite-curve-factors/index.html, blob 87f97f2e03fb722d66ebf35be56c8bceef7c31f6, lines 7–76. Prop 18.23.1 source non-kahler-pluripotential-theory:CA9D0D47 permanent 6235BDB38282 (16–46); Example 18.23.2 source :19AC45D8 permanent 47BCB7DF51C8 (50–76). Degree scaling of Gauduchon constants and area, explicit quadratic cover example and norm-four polar difference checked. No new error.
- §18.24, docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--models-pulled-back-by-a-finite-curve-map/index.html, blob dd427a692bda2c364ae83207717a16bcac070cdc, lines 7–115. Prop 18.24.1 source :84211D78 permanent 424A6AE6F169 (10–22), Prop 18.24.2 source :6421C90F permanent C8EE003DDDC9 (29–63), Cor 18.24.3 source :5D79DF2B permanent F204E0019263 (67–82), Example 18.24.4 source :542A2364 permanent 2C40EC6336AD (89–115). Fiber maximum and open-map USC, scaled TV and mass, closed image, retraction and non-nearest example checked. All source labels here have prefix non-kahler-pluripotential-theory. New result above is conditional on their identified dependencies, not a correction of a false statement.
- §18.25, docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--hopf-surface-fibers-and-unbounded-ambient-mass/index.html, blob 23b0b6d65db6f0e3119cca84a69006c215243902, lines 7–66. Example 18.25.1 source non-kahler-pluripotential-theory:1701EF92 permanent 6CA9B76E77A0 (10–66). Checked free proper scalar action, compact annulus, incidence blowup charts, degree-one pullback mass lower bound and distance-one model. Conditional on 23.1.1, 13.14.15 and 18.22.1/3; those upstream proofs not re-certified.
- Independent rotation §2.20, docs/sections/elliptic-systems-and-unique-continuation/index.html, blob 7e1c07728654308341d90c33f05873112c53052c, lines 7–275. Lemma 2.20.1 tag CB1875F07408 (8–50), Theorem 2.20.4 tag 2D8A7E49E474 (55–174), Prop 2.20.11 tag CE8EC0706B26 (179–258), Cor 2.20.12 tag 1ADDDDB90B14 (263–270), Remark 2.20.13 tag ED67DD231FDF (275). Checked cooperative ODE component comparison, uniform derivative ratios, exponent arithmetic (G_n~n^(29/16), r_nG_n~n^(1/8)), sign of i∂_x^3 on e^(-izx), cutoff dominance and nondivision at middle zeros, all-derivative flat extension. Recomputed AB commutator -4it∂_x^2 D-2i∂_x^2 and determinant b^2 a. For a real covector with xi nonzero a or b can vanish only at tau/xi=±1 and t^2=2, outside printed |t|<1; no contradiction with scalar-principal unique continuation. No new proof gap identified.
- Selected dependency reread §5.43.16, docs/sections/plurisubharmonic-functions-and-singularities--pullback-and-descent/index.html, blob e5cccf608a51dd1629374fc68a1d3d7e6fd15958, lines 318–346, source non-kahler-pluripotential-theory:01A85B2E permanent 151A1D744DE7. Weighted Borel pullback, TV, atom and polar-carrier properties.
- Selected dependency reread §13.29.1, docs/sections/volumes-under-bounded-mass--background-changes-on-curves/index.html, blob 94ff265434461fd6baee6532decdff369da3e177, lines 13–37, source non-kahler-pluripotential-theory:405CAA19 permanent C9C98321BEFC. Polar classification and metric; gauge proof uses earlier results, not a new transitive certification.

Unresolved: full upstream proof chains and reconciliation of historical coverage; no general continuous nearest selection asserted. Demailly approximation/regularization and the specified Bergman/L2/OT/multiscale/positivity-loss programme remain deferred-by-user, not resolved. No tests/build/CI or source/main/registry/tag/site edits.
