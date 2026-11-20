# Audit of metric completions and finest locally convex convergence — 2026-11-20

**Baseline main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Review branch:** `review/mathematical-audit`. Scope: complete direct rereading of the mathematical bodies of §2.22 and §2.23, without claiming verification of their whole transitive proof graph. The 25-chapter / 747-section inventory is unchanged. This review is independent of, and does not touch, the user-deferred Demailly approximation/regularization or dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss programmes. The fact that the provenance key for the two sections is `demailly-complex-geometry` does **not** make these elementary metric and locally convex results part of the excluded approximation programme.

## Exact integrated anchors and provenance

- §2.22, `docs/sections/metric-completeness-and-compact-balls/index.html`, blob `4ad63fec32bfa9a18a12a5dbb009445a43693c86`; direct mathematical lines **7–82**. Original source variant `demailly-complex-geometry`; approximate-midpoint equation original `4BF7D568` / permanent `D0F673E1134B` (lines 7–14); Lemma 2.22.3 original `B621C59E` / permanent `3B383470A6A3` (lines 18–35); Proposition 2.22.4 original source tag to be read at the statement / permanent `EB12C0B326CA` (lines 40–55); Theorem 2.22.5 permanent `883E85712A41` (lines 60–78).
- §2.23, `docs/sections/completions-and-locally-convex-quotients/index.html`, blob `e2c6d25d35020ccefa739f04aa893e173f73c17e`; direct mathematical lines **7–120**. Source variant `demailly-complex-geometry`; Lemma 2.23.1 original `C85CEBC0` / permanent `0628F713D150` (lines 11–30); Example 2.23.2 permanent `D7A9E3E20E73` (lines 35–46); Lemma 2.23.3 permanent `5F1410BEA2F7` (lines 51–90); Example 2.23.4 permanent `B0973308F142` (lines 95–104); Proposition 2.23.5 permanent `6118C797DA34` (lines 109–120).

## POME-LCS-FINEST-SEQUENTIAL-FINITE-SUPPORT-NET-001

**Severity:** low. **Status:** verified conditional deduction, **not** an error in the printed Lemma 2.23.1. **Hypotheses:** a complex or real vector space (E) with Hamel basis ((e_i)_{i\in I}), endowed with its finest locally convex Hausdorff topology. If constructing the net below, suppose (I) is infinite.

**Exact sequence characterization.** A sequence (x_m\to x) in (E) if and only if (i) there is a **single finite** subset (J\subset I) containing the supports of **all** (x_m-x), and (ii) every coordinate ( (x_m-x)_i\to0), (i\in J). In particular every Cauchy sequence is contained in a finite-dimensional linear subspace and converges there. (The finite union with the support of (x) handles the (x_m) themselves.)

**Proof.** In the notation of the printed Lemma 2.23.1, all seminorms
[
 q_w(\sum_i a_ie_i)=\sum_i w_i|a_i|,\qquad w_i>0,
]
are continuous and generate the topology. Set (y_m=x_m-x). Suppose (\bigcup_m\mathrm{supp}(y_m)) is infinite. Removing any finite prefix leaves infinitely many used coordinates, because each vector has finite support. Recursively choose (m_k>m_{k-1}) and pairwise distinct (i_k) with ((y_{m_k})_{i_k}\ne0). Assign positive weights (w_{i_k}\ge k/|(y_{m_k})_{i_k}|), extending by (w_i=1) elsewhere. Then (q_w(y_{m_k})\ge k), contradicting (y_m\to0). Thus one finite (J) contains all supports. On the finite-dimensional coordinate subspace, ordinary coordinate convergence implies (q_w(y_m)\to0) for every weight (w), and conversely the weights (w_i=1) show coordinate convergence. Lemma 2.23.1 establishes convergence of every Cauchy **net**, hence in particular every Cauchy sequence, to which this argument applies. No sequential compactness assumption is used.

**Sharp net distinction.** Despite this sequence theorem, a convergent **net** need not eventually lie in *any* finite-dimensional subspace. Direct the pairs ((U,J)), where (U) is a balanced convex zero neighborhood and (J\subset I) is finite, by reverse inclusion on (U) and inclusion on (J). Pick (i(U,J)\notin J) and a nonzero scalar (t(U,J)) sufficiently small that (t(U,J)e_{i(U,J)}\in U); the absorbing neighborhood property supplies (t). Then (x_{(U,J)}=t(U,J)e_{i(U,J)}\to0): eventually (U\subset V) for each zero neighborhood (V). For every finite-dimensional subspace (H), choose a finite coordinate set (J_H) containing the supports of a basis of (H). At all indices with (J\supset J_H), (x_{(U,J)}\notin H). This shows explicitly why the printed net proof is necessary and why a sequence-only argument cannot replace it.

**Dependencies affected:** the interpretation of Lemma 2.23.1 and nonmetrizable convergence in Examples 2.23.2–2.23.4. **Proposed correction:** optional explanatory note distinguishing sequence support stabilization from convergent nets; *no* mathematical statement needs revision. The separate prior finding `POME-LCS-ORDINAL-PLANK-SEQUENTIAL-DEFECT-001`, concerning a Cauchy sequence in the *incomplete quotient* (F), is retained, not recounted here.

## POME-METRIC-COMPLETION-APPROX-MIDPOINT-IFF-LENGTH-001

**Severity:** low. **Status:** verified conditional deduction. **Hypotheses:** nonempty finite-distance metric space ((E,d)); (widehat E) its metric completion. This builds on the printed approximate-midpoint definition (2.22.2) and complete-space equivalence in Proposition 2.22.4, neither of which is contradicted.

**Claim.**
[
 E\text{ has approximate midpoints}\quad\Longleftrightarrow\quad
 \widehat E\text{ is a length metric space}.
]
If these equivalent conditions hold, (E) has arbitrarily fine near-distance finite chains, but (E) **need not admit even one nonconstant continuous path**.

**Proof of forward direction.** For (x,y\in\widehat E) and (\delta>0), choose (a,b\in E) with (d(a,x),d(b,y)<\delta). Select (z\in E) such that
[
 \max\{d(a,z),d(b,z)\}<\tfrac12d(a,b)+\delta.
]
The triangle inequality gives
[
 \max\{d(x,z),d(y,z)\}<\tfrac12d(x,y)+3\delta.
]
Since (\delta) is arbitrary, (widehat E) has approximate midpoints. It is complete by definition, so the printed Proposition 2.22.4 makes it a length space.

**Reverse direction.** If (widehat E) is a length space, for (a,b\in E) take a connecting curve in (widehat E) of length below (d(a,b)+\epsilon). A point (z\in\widehat E) halfway along its accumulated length satisfies both endpoint distances at most ((d(a,b)+\epsilon)/2). Approximate (z) by a point of (E) to within (\epsilon) and let (\epsilon\downarrow0). This gives (2.22.2) in (E).

**Example showing completeness cannot simply be omitted in the length-space conclusion.** (E=\mathbb Q\subset\mathbb R) with the Euclidean metric has *exact* rational midpoints and (epsilon)-chains of total length exactly (d(a,b)). Its completion is (mathbb R), a length space. But every connected subset of (mathbb Q) is a singleton (separate two different rationals by an irrational cut), so every continuous map ([0,1]\to\mathbb Q) is constant. Consequently its intrinsic path-length distance between distinct points is (+\infty), whereas its original metric is finite. The printed Proposition 2.22.4 expressly requires completeness, and is correct.

**Dependencies affected:** §2.22.3–5, and only interpretive downstream uses of complete length spaces such as §9.28.1. **Proposed correction:** optional statement about completion and a rational-line example, without revising the printed hypotheses. The previously recorded `POME-METRIC-PROPER-APPROX-MIDPOINT-GEODESIC-001` concerns exact minimizers under local compactness and is *not* repeated.

## Direct review and outstanding checks

Checked Lemma 2.22.3's dyadic error budget and Lipschitz interpolation, Proposition 2.22.4's necessity of completeness, and the exact locality assumption in Theorem 2.22.5. Checked Lemma 2.23.1's positive-weight seminorm system and Cauchy-net limit argument, Example 2.23.2's complete nonopen bijection, Lemma 2.23.3's deleted-corner ordinal example and open quotient construction, Example 2.23.4's scalar completed-tensor obstruction, and Proposition 2.23.5's Fréchet quotient reduction. **No new confirmed printed error**; neither the Fréchet projective-tensor quotient theorem nor its referenced internal §2.13.5/§2.12.1 subproofs are independently recertified here. §9.28.1 is used only as a selected cited result; no whole dependency-chain certification.

**Coverage delta:** +2 complete direct mathematical section readings (§§2.22–2.23) **in this session**; +0 entirely verified transitive chains; no historic-first-visit claim. The two main HTML blobs are unchanged. Prior audit findings remain open/resolved/deferred in their original classifications. No build, test, CI, publication, registry, source, tag or main-branch write was performed.
