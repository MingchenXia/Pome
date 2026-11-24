# Fixed-test-compact capacities: exact regularity criterion and net boundary

Date: 2026-11-24. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.

Finding **POME-FIXED-TEST-COMPACT-CAPACITY-REGULARITY-001** — low / verified conditional deduction. The printed ball theorem is correct; this is a generalization with a sharp failure criterion, not a confirmed false source statement.

## Immutable reading-edition anchors

- docs/sections/logarithmic-families-and-a-fixed-ball-capacity/index.html (blob 98d00aa7b2db4f81163a56d6f448946fd0c75499): Theorem 16.31.3, article klimek-pluripotential-theory-A80EBCDF, permanent E215D05E52EC, lines 58–82; Theorem 16.31.1 lines 11–32, permanent 62CEBBF93786; Proposition 16.31.2 lines 37–54, permanent A76B9D558430. Proposition 16.31.4 lines 87–104, permanent 4146861A3795.
- docs/sections/polynomial-descriptions-of-logarithmic-envelopes/index.html (blob 15d7e0207da1d72653382a1512ca380311b5d5e3): Proposition 16.30.1 lines 11–31, permanent F5C5050EEDEB; Proposition 16.30.2 lines 36–49, permanent F983146D5FCD.
- docs/sections/maps-and-regularity-of-global-extremals/index.html (blob b20154011d37d46a4d0cc7751863207e5debf183): opening conventions and entire mathematical body lines 7–162, notably Proposition 16.32.8 permanent 7C8B2A4D660E.

## Statement and proof

Use the raw Lelong-class extremal V_E and its upper regularization V_E^*, with the convention that the latter is identically +infinity for pluripolar E. For every nonempty compact test set F in C^n (n >= 1), define
\[
 a_F(E)=\exp(-\sup_F V_E^*).
\]
The following hold.

1. Monotonicity, values in [0,1], exact vanishing on pluripolar sets, and continuity on increasing sequences with bounded union hold for every such F.
2. Continuity on decreasing sequences of compact obstacles holds **if and only if F is L-regular**, i.e. V_F^*=0 everywhere on F. In that case the continuity also holds for arbitrary decreasing directed nets of compact obstacles.
3. If F is non-pluripolar, put C_F=sup_F V_F^*<infinity. For any decreasing directed net of compact obstacles K_i with intersection K,
\[
 a_F(K)\leq \lim_i a_F(K_i)\leq e^{C_F}a_F(K).
\]
The factor exp(C_F) is optimal for this fixed F, even for decreasing sequences. Zero on the right forces zero limit.
4. Increasing-sequence continuity must not be replaced by arbitrary increasing-net continuity, even for a regular ball test set.

Proof of 1: the nonpolar-family dichotomy (16.31.1) gives a finite PSH extremal on all of C^n when E is nonpolar; compactness of F gives a finite supremum there. If E is polar, the supremum is +infinity. Monotonicity follows directly from the competitor constraint. Proposition 16.31.2 gives decreasing regularized extremals for increasing sequences E_j with bounded union. For a nonpolar union, a nonpolar term exists by countable-union polarity. On the subsequent tail these are finite USC functions; compactness of F shows that the supremum commutes with their decreasing limit. Explicitly, for any real threshold strictly below the limit of the suprema, the nonempty closed superlevel sets in F have the finite intersection property. The polar-union case is immediate. Exponentiation proves the assertion.

Proof of 2–3: let (K_i) be decreasing on a directed index set. Work on a tail inside one fixed K_i0. Any open neighborhood of K eventually contains K_i: otherwise the compact sets K_j outside that neighborhood, j >= i0, have the finite intersection property, contradicting the definition of K. This also proves eventual emptiness if K is empty. For any u in the Lelong class with u<=0 on K and any epsilon>0, the open sublevel {u<epsilon} contains K, so u-epsilon is an admissible competitor for all sufficiently late K_i. Hence
\[
 V_K=\sup_i V_{K_i},\qquad V_K^*=(\sup_i V_{K_i}^*)^*.
\]
The second identity follows by the raw/star sandwich and monotonicity, and does not use a sequential approximation of the net.

Write M_i=sup_F V_{K_i}^* and M=sup_i M_i. These numbers are nondecreasing. If M=+infinity, monotonicity gives sup_F V_K^*=+infinity and the capacities converge to zero. If M<infinity, every V_{K_i}^* is a finite PSH member of the Lelong class by 16.31.1. As V_{K_i}^*-M<=0 on F, it is a raw competitor for V_F. Thus
\[
 V_{K_i}^*\leq M+V_F\leq M+V_F^* .
\]
For nonpolar F the last majorant is finite USC. Taking the supremum and then USC regularization yields
\[
 M\leq\sup_F V_K^*\leq M+C_F .
\]
Exponentiation proves the sharp-factor bound; when F is regular the factor is one. This argument requires neither a ball interior nor a positive Lebesgue measure assumption on the test set. In particular an L-regular compact of zero ambient Lebesgue measure works too.

Conversely take the closed thickenings F_j={dist(z,F)<=1/j}. These are compact, decrease to F, and V_{F_j}^*=0 on F by 16.30.2 (or simply the contained-ball profile at each point of F). Thus a_F(F_j)=1, whereas a_F(F)=exp(-C_F). This proves necessity of regularity, including the case C_F=+infinity for polar F, and shows that for nonpolar F the above multiplicative defect is attained. For a concrete nonpolar counterexample to an unrestricted test-compact version, take F=closed unit ball union {2e_1}. By 16.31.2 polar invariance and 16.30.1, V_F^*=log^+|z|. Hence a_F(F)=1/2 and all a_F(F_j)=1.

Proof of 4: index the finite subsets of the closed unit ball by inclusion. Each obstacle is pluripolar and has capacity zero, but the union is the entire unit ball, which has test-ball capacity one. The union is bounded. Countable-union polarity cannot be upgraded to this directed union.

Proposed supplement: append the compact-test criterion and sharp multiplicative defect to Theorem 16.31.3 without changing its ball statement or the distinction between sequences and nets. Downstream 16.37.5 (fixed-ball capacity continuity used in its polar-intersection case) stays valid as printed; the new generalization is not a replacement for the Robin-capacity comparison. No direct source modification or dependency certification is proposed.

## Actual coverage and outstanding inputs

- Whole direct current section 16.31 (mathematical lines 11–104): checked the normalized weighted pole-series contradiction, the normalized polar-obstacle perturbation, countable discrepancy union, fixed-ball boundary essential-sup argument, and hyperplane-at-infinity restriction of the canonical projective representative. No new printed error identified. The argument here uses, rather than proves transitively, the logarithmic-class global pole theorem, the canonical envelope discrepancy theorem, Hartogs lemma, and the projective growth correspondence.
- Whole direct current section 16.32 (mathematical lines 7–162): verified the direct and reverse polynomial-growth argument, unequal-degree reduction by powers, compact hull-neighborhood convention, relative/global comparisons and proper finite fiber maximum, component separation and localization, pointwise regularity transfer, three counterexamples, nonthin interval step, and the elementary equal-dimensional C^1 critical-value argument plus regular perturbation for nested smooth neighborhoods. The generic-rank pullback, proper finite-map PSH theorem, interval nonthinness and underlying envelope results remain inputs, not newly proved transitive chains. No new printed error identified.
- Selected section 16.30 lines 11–49: norm-ball profile and decreasing compact obstacle argument; the ordinary Euclidean radial convolution in 16.30.2 is not the excluded Demailly programme. Remaining polynomial-representation proofs not certified in this session.
- Selected section 16.37 lines 80–111 (blob 525f388094d0efb6b9ef9f8701d8ac459fd22814): fixed-ball/Robin comparison, using prior integration-by-parts and support inputs. No complete §16.37 certification.

Actual current docs/index.html table of contents: 747 section locators. Before updating, the matrix had 747 rows, 747 distinct locators, no omissions or extras. Historic first-ever visits are not asserted; legacy statuses are not a claim of no earlier review. This session adds two whole direct readings and two selected readings, one classified deduction, zero newly confirmed false printed statements, zero new unresolved proof gaps and zero complete transitive certifications.

Demailly approximation/regularization and its dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programme remain deferred-by-user, not resolved or certified. No build, software tests, CI, publication or production source/tag/registry change.
