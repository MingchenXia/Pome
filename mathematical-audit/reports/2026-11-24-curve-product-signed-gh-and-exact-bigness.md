# Curve-product metrics and exact bigness threshold — 2026-11-24

Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit only; no changes to mathematical body or tags. The user-deferred Demailly regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss programmes remain deferred-by-user, not certified.

## Anchors and actual scope

All paths below are on the reviewed main under docs/sections/. Direct whole mathematical reading (not a transitive proof certificate):

- multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--several-curve-factors/index.html, blob 93e080ea9c15c5ec03b28c2ec51eb469c769603b, physical lines 7–210, §18.16. Lemma 18.16.1 tag D9950FF0BE1C, Proposition 18.16.2 tag 9E5A9E7C5770, Proposition 18.16.5 tag B61109A06541, Corollary 18.16.6 tag A5CCF14B62D6.
- multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--varying-the-curve-coefficients/index.html, blob d2dc367592df2da185f8d679aabf5df4e68a4a6a, lines 7–130, §18.17. Lemma 18.17.1 tag 9040CE491D09, Proposition 18.17.3 tag 4A625E059F4C, Proposition 18.17.5 source non-kahler-pluripotential-theory:C2C06FA3 / permanent 25F2A9E20F21, lines 101–130; eq. 18.17.6 tag E8AFCE9DFA82.
- multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--arbitrary-curve-backgrounds/index.html, blob 7e89dabe6cc08855d3a0f89a1f2faed9e5ae791d, lines 7–134, §18.18. Lemma 18.18.1 source non-kahler-pluripotential-theory:39C82453 / permanent 7EF34A8A42E5, lines 26–71; Proposition 18.18.3 source non-kahler-pluripotential-theory:7BBFA972 / permanent 347997EB7F21, lines 86–114, eq. 18.18.4 tag 657599C0AEFD; Corollary 18.18.5 tag 15AC4263456B.

Selected dependency reading: volumes-under-bounded-mass--model-potentials-on-curves/index.html blob 4ec0e8d5c90ad5df4e84f17bbc03a2298415e29f, statement/initial proof paragraphs at 20,91,168 (13.28.1,7,11, tags 2422DD1AB3AB, FB89848D2500, 03E01F83CA7A); volumes-under-bounded-mass--background-changes-on-curves/index.html blob 94ff265434461fd6baee6532decdff369da3e177, statements 13.29.1 and 13.29.3 at 14 and 83 (tags C9C98321BEFC and 151BAA2FA1AB); equations-with-prescribed-singularities--degenerating-semipositive-backgrounds/index.html blob 5ed2b285e8306f0a803df40712b93ed4054851a8, definition 15.19.19 and lemma 15.19.20 at 384 and 400 (tags 0EB9DF723176, 022849340F28); selected Corollary 18.20.4 proof lines 88–105 in multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--auxiliary-compact-complex-factors/index.html, blob f1b6f67c60fe76ec140541127caf1203fea7ff7f, tag 47BA03C63283.

## POME-CURVE-GH-SIGNED-DISTORTION-ATOMIC-UNIVERSAL-001

Low / verified conditional deduction, not a printed error. Distinct from the 2026-10-24 POME-CURVE-GH-PERMUTATION-001 (which used the full absolute sum and biholomorphic matching).

Let the coefficient-weighted areas in §18.17 be x_i=a_i A_i and y_i=b_i A_i, or in §18.18 be x_i=B_i and y_i=B'_i. Write
\[
 P=\sum_i(x_i-y_i)_+,\qquad N=\sum_i(y_i-x_i)_+.
\]
For the *particular common-tuple correspondence* R in Proposition 18.17.5, the exact distortion is
\[
 \operatorname{dis}R=2\max(P,N).
\]
The same statement holds for the common normalized polar-measure correspondence in §18.18 and the restriction to ideal models. Indeed, under the printed polar-measure classification, a pair of tuples gives independent distances d_i in [0,2] in the unit-mass polar measure spaces. The difference of product distances is the signed sum \(\sum_i(x_i-y_i)d_i\), lying in [-2N,2P]. For the upper endpoint choose mutually distinct unit Dirac measures in each coordinate with x_i>y_i, and identical zero measures in the remaining coordinates. For the lower endpoint reverse the sign selection. These choices are allowed even for inactive coordinates because the correspondence uses full auxiliary tuples, with zero weight interpreted as omission. They are atomic and therefore also attain distortion in the ideal correspondence.

Using 15.19.20 gives
\[
 |\sum_i(x_i-y_i)|\le d_{\rm GH}\le
 \max(P,N)=\tfrac12\big(\sum_i|x_i-y_i|+|\sum_i(x_i-y_i)|\big).
\]
The lower bound is the printed diameter bound. This is a strict improvement of the printed upper bound when both P and N are positive; the exact value for ordered weights is retained. For example x=(2,0), y=(1,1) gives upper bound 1 rather than 2. It is the *distortion* that is shown optimal for this correspondence, not the GH distance over all correspondences. This argument also improves every previously allowed permutation coupling by replacing the full absolute sum by the displayed half-sum expression after permutation.

Moreover, for ideal subspaces **any** permutation is allowed even if curves have different genus. Every compact connected Riemann surface has a point set of cardinality continuum: a coordinate disk gives the lower bound and a finite coordinate cover gives the upper bound. Choose any bijection of point sets of two such curves. A finite positive atomic measure has countably many nonzero weights, hence corresponds exactly to a nonnegative summable family indexed by the point set. Transfer weights along this bijection (not a pushforward on arbitrary Borel measures). The sum of absolute differences of weights, equal to TV by the signed Jordan decomposition on the countable union of supports, is preserved. Thus each ideal unit-mass factor is abstractly isometric to the same positive l1 unit simplex, independent of the complex structure. With any permutation matching the weighted areas, transport the corresponding families and use the above distortion proof. Equal area multisets give isometric ideal product spaces, including zero weights; e.g. a single unit-area active genus-zero factor and a single unit-area active elliptic factor. This does NOT assert such a bijection preserves general polar measures, topology of potentials, analytic data, or the ordinary-model spaces. No measurability of the arbitrary point bijection is needed for atomic weight transfer.

Dependencies: curve polar/atomic classification 13.28.1, 13.28.7, 13.28.11, 13.29.1 and the printed product identifications and correspondence lemma. Their complete upstream chains are not certified. Proposed optional strengthening after 18.17.5 and 18.18.3; the original results are correct and retained. No other dependent theorem is refuted.

## POME-CURVE-PRODUCT-EXACT-BIGNESS-MARGIN-001

Low / verified deduction (the smooth gauge existence in 5.29.22 is an internal conditional input); not a printed error. Lemma 18.18.1 states sufficient positivity and some nonbigness cases, but does not assert that a nonzero f with a zero can give a big background. We close this gap in the characterization, not in its printed proof.

Use precisely the §18.18 data: M=Y x C_0 x Z, smooth curve forms sigma_i of area B_i>=0, reference eta_i>0 with area A_i, tau>0 on C_0, Kähler kappa on Z, f>=0 smooth on Y. Define the fixed product Hermitian form
\[
 \Omega=p^*\sum_i\pi_i^*\eta_i+s^*\tau+r^*\kappa.
\]
The optimal domination margin, allowing arbitrary quasi-PSH u, is exactly
\[
 \sup\{\epsilon\ge0:\ \Theta_{\sigma,f}+dd^cu\ge\epsilon\Omega
                      \text{ for some quasi-PSH }u\}
 =\min(1,\min_i B_i/A_i,\min_Y f).
\]
The supremum is attained by a smooth u. In particular the background is big if and only if all B_i>0 and f>0 everywhere.

Proof of necessity: pair the inequality against the closed positive test form T_i at physical line 65 in §18.18 (all curve factors except i, C_0, and the top power kappa^k). The dd^c term vanishes by Stokes for currents, and comparison gives B_i>=epsilon A_i. For the auxiliary curve, take the positive (n-1,n-1) form T_0 of line 59, pulled back from Y x Z. Multiply it by any nonnegative smooth function h on Y, pulled back to M. This product remains closed: the base Y form already has top degree. Pairing gives, after cancellation of the positive constants int_C0 tau and int_Z kappa^k,
\[
 \int_Y h(f-\epsilon)\bigwedge_i\pi_i^*\eta_i\ge0.
\]
All nonnegative smooth h are allowed, so continuity implies f>=epsilon at every point, even if u has poles along exceptional slices. This avoids any unjustified restriction of singular currents to fibers. Finally pair against p^*(wedge_i pi_i^* eta_i) wedge s^*tau wedge r^*(kappa^(k-1)), a closed positive (n-1,n-1) form. Only the kappa term survives on either side, giving epsilon<=1 since its pairing is positive. Here k>=1 is the printed assumption.

For sufficiency use the smooth gauge decomposition from 5.29.22, sigma_i=(B_i/A_i)eta_i+dd^c chi_i, and take u=-sum_i chi_i circ pi_i circ p. The resulting form is block diagonal with factors B_i/A_i, f(y), and 1 relative to Omega, and dominates the claimed minimum times Omega. The proof allows zeros and arbitrary smooth (possibly sign-changing) sigma_i of nonnegative area. Bigness in the sense of existence of a strict current is independent of the chosen Hermitian form by compactness and comparison of positive forms. The inequality already forbids strict currents if f has even one zero. No regularization input used.

Proposed optional strengthened lemma after 18.18.1; applies directly to the coefficient case 18.17, including 18.16.6. No assertion for a general higher-dimensional semipositive auxiliary form in 18.20.4.

## Direct-review observations and boundaries

- §18.16: partial sup over one factor is locally bounded above; replacing competitors by their maximum with a fixed lower translate ensures nontrivial slices. The usc regularization preserves the upper bounds by usc of the right sides. The induction bounds remaining coordinates, including at poles by ordinary dominance. The separated obstacle is essential. The ideal identities use the printed atomic Green representatives, divisor dominance and addition/pullback of ideal types; these are conditional upstream inputs (5.37.4, 5.37.7, 5.38.5, 20.3.20). Rational approximants use finitely many atoms and simultaneous denominators with the coefficient of D. The zero upper-volume conclusion uses 18.14.1, not a new mass-continuity argument.
- §18.17: zero weights are omitted rather than multiplying -infinity by zero. The normalization and injectivity follow from finite sections and separate suprema. Analytic density uses rational *scaled* pole coefficients, not preservation of analytic singularities under irrational scaling. Fiber diameter formula uses only discarded coordinates, while noncompactness uses separated Dirac models. The displayed original GH upper bound is valid but nonsharp as shown above.
- §18.18: smooth gauge at area zero gives a singleton, not necessarily the zero potential. Fiber integration applies to smooth product projections and the finite sum of coordinate differences almost everywhere, avoiding infinity minus infinity on polar sets. The uniform limit in 18.18.5 is conditional on 5.29.23, not an assertion about varying auxiliary coefficients controlling potentials. No newly confirmed false printed theorem or proof gap in these direct reads.

The earlier 2026-10-24 selected §§18.17–18.18 work is not counted again as new. Today's three whole direct mathematical reads are not historic first visits; matrix legacy remains unreconciled. Four selected context sections (§§13.28–29, 15.19, 18.20); no complete transitive proof chains certified. No software tests/build/CI or publication performed. No source, registry, permanent-tag or main change.
