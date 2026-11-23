# Sharp calibration deficit and the Harder–Narasimhan slope profile

2026-11-24. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit only; no production edits.

## 1. POME-CALIBRATION-ANGLE-DEFICIT-SHARP-001

Low / verified conditional deduction (not a false statement). Source: docs/sections/hermitian-volume-and-complex-calibration/index.html, blob dfaec751e0c2e79937b0126d572a87bc300f3261, Proposition 10.89.2 (source tag E9A95F3B, permanent AB0853CAC9B1), lines 11–24; application to Theorem 10.89.3 (source tag 6F717209, permanent EB0F17719184), lines 29–39.

Let L be a real 2p-plane in a Hermitian space of complex dimension n, with 1 <= p <= n. Set A=P_L J|_L, B=P_(L-perp) J|_L, k=min(p,n-p), S=||B||_HS^2/2. In the skew blocks of A write t_j=1-a_j^2. Since A^*A+B^*B=I, the eigenvalues of B^*B are the t_j, each with multiplicity two. Rank B <= 2(n-p), so at most k of the t_j are nonzero. Pad with zeros to length k. The absolute calibration coefficient is c=prod sqrt(1-t_j), with 0<=S=sum t_j<=k. If k=0, S=0 and c=1.

For k>=1 the sharp pointwise bounds are
\[
1-(1-S/k)^{k/2}\le 1-c\le 1-\sqrt{\max(0,1-S)}.
\]
Indeed AM–GM gives prod(1-t_j)<=(1-S/k)^k. Induction using 0<=t_j<=1 gives prod(1-t_j)>=1-S; nonnegativity supplies the truncated lower bound. For the lower deficit equality take all t_j=S/k. For the upper deficit equality take t_1=S and others zero for S<=1; for S>=1 take t_1=1 and distribute S-1 in the remaining k-1 coordinates (for k=1 this case is only S=1). These arrays really occur: in mutually orthogonal complex two-planes with real unit vectors e_j,f_j, take the real plane spanned by e_j and sqrt(1-t_j) J e_j + sqrt(t_j) f_j. Use p-k further complex lines. This requires p+k<=n, precisely the chosen k. Hence both bounds are optimal at every allowed S.

In particular 1-c >= C_k S, with sharp C_1=1/2 (limit S->0), C_k=1/k for k>=2 (equality at S=k; use (1-S/k)^(k/2)<=1-S/k). Also 1-c<=S with sharp coefficient one at S=1. These coefficients concern the *absolute* calibration deficit; the signed deficit is always at least the absolute one.

Under the exact-form and oriented boundary hypotheses of Theorem 10.89.3, the Stokes argument gives
\[
\operatorname{Vol}(Y)-\operatorname{Vol}(Z)
=\int_Y(1-c_{\rm signed})\,dV_Y
\ge (C_k/2)\int_Y\|P_{(TY)^\perp}J|_{TY}\|_{\rm HS}^2\,dV_Y
\]
for k>=1. This controls the integrated tangent-plane defect, not a distance to a particular submanifold, and makes no assertion that the pointwise sharp constant is globally attained with fixed boundary data.

Proof completeness check: the complex-tangent regularity invoked in line 23 can be supplied locally without a global theorem. At an interior point choose complex linear coordinates so projection to the first p coordinates is invertible on the tangent plane. By the real C^1 inverse function theorem the submanifold is the graph of a C^1 function f on an open subset of C^p. J-invariance at every graph point forces df(iv)=i df(v); the Cauchy–Riemann equations then give holomorphicity on complex lines, and iterated one-variable Cauchy formulas on small polydiscs give joint holomorphicity. Thus the equality characterization is valid. The exactness and cutoff in lines 37–38 correctly justify the boundary-current use of Stokes; the p=0 and mixed-orientation counterexamples in lines 44–48 are valid. The latter cylinder has side area (2 pi R)(2h) and the two discs area 2 pi R^2.

Proposed correction: none needed for the stated inequality. Optional addition of the local graph argument and the sharp quantitative bound after Proposition 10.89.2; Theorem 10.89.3 gains the integrated estimate. C^1 Stokes §5.55.1 is the internal dependency; no transitive certification claimed.

## 2. POME-HN-TRUNCATED-SLOPE-PROFILE-001

Low / verified conditional deduction (not a false statement). Source: docs/sections/degrees-and-maximal-slopes/index.html, blob b824fc476c0cecf64bc52f2178c90344dfb3e7ab, Lemma 10.106.1 (26EDBAD1 / 21D47D6E39D1), lines 18–39; Theorem 10.106.2 (E126ED45 / 469F76790780), lines 44–73; Lemma 10.106.3 (3D33031A / B72C1D61D638), lines 78–89. Work under the additive degree and effective-divisor nonnegativity hypotheses of that section.

Let the HN filtration of a torsion-free E have successive quotients Q_i, ranks r_i and slopes s_1>...>s_l. Define M(t)=max_F(d(F)-t rk F), including zero. The theorem's auxiliary maximization in fact has the exact formula
\[
M(t)=\sum_i r_i(s_i-t)_+.
\]
For any coherent F subset E, the successive quotients of F intersected with the HN filtration inject into Q_i. They are torsion-free, with ranks f_i<=r_i. Semistability (including the same-rank monotonicity) bounds their degrees by f_i s_i, and additivity gives d(F)-t rk F<=sum_i f_i(s_i-t)<=sum_i r_i(s_i-t)_+. Equality is attained at the HN prefix with s_i>t, also at the prefix with s_i>=t. Any maximizer has zero ranks in the negative-slope blocks and full ranks in the positive-slope blocks relative to t. Hence it lies in the latter weak prefix: its image in the torsion-free quotient by that prefix has rank zero and vanishes. The weak prefix is therefore the unique largest maximizer, including at every breakpoint and for all real t (also t>=s_1). The right and left derivatives are respectively minus the sums of r_i over s_i>t and s_i>=t; the distributional second derivative is sum_i r_i delta_(s_i). Thus the entire HN slope multiset is recovered from the auxiliary maximum, without any discreteness assumption on degrees. M is convex, nonincreasing and rank(E)-Lipschitz, sharply so for t below the last slope.

Direct proof checks: the maximum lemma uses compact coherent-subsheaf ACC and same-rank monotonicity. In lines 26–38, the intersection has positive m and replacing G by that intersection is legitimate; after choosing a maximal G inside F, the final intersection strictly increases it. In lines 64–70 the sign (t-u)<0 forces the nonnegative rank difference to vanish; saturation is essential to containment. Nested saturated subsheaves of equal rank coincide, so eventual equality as t tends to the supremum does not assume a discrete set of slopes. In lines 78–89 dual quotient/image arguments use determinants of same-rank inclusions and the image of a map into a torsion-free target, so the directions of both inequalities are correct. ACC, degree additivity and determinant identities are upstream inputs not fully re-proved here.

Proposed correction: none required for the printed theorem; optional profile formula after 10.106.2. Relevant downstream slope uses include 10.107.1–2 and 10.109.2. No claim that their entire upstream chains have been certified.

## 3. Selected rotation: §10.109

Source docs/sections/numerical-dimension-and-cotangent-quotients/index.html, blob 85538a5ba880030f432282e302a446a230ae15ec. Checked lines 36–69 only: Lemma 10.109.1 (5A937EA0 / 636609E49628) follows conditionally from the stated monotonicity/homogeneity of positive mixed mass; Theorem 10.109.2 (71F4321F / 7E716F90C084) uses the movable duality, tensor-slope additivity, positive-slope involutivity and Corollary 9.75.4 as inputs. The determinant coefficient m n^(m-1) follows by repeated tensor determinant identity, and the saturation difference is effective. No new error found in these steps. The analytic-current approximation comparison at lines 26–32 is expressly deferred-by-user; no completion or review of that programme. §10.108 was located but not counted as coverage: its fiber/direct-image L2 inputs are not pursued here.

## Scope and limits

Two whole current mathematical sections (§§10.89, 10.106); one selected nonexcluded section (§10.109); two new conditional deductions; no confirmed false printed theorems, no new unresolved proof gap, no complete upstream-chain certifications. Prior historical visits unreconciled. Demailly regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss programmes remain deferred-by-user, not resolved. No build, tests, CI, website publication, main/source/registry/tag edits.
