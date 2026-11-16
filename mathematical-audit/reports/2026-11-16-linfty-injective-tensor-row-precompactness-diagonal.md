# Exact image of bounded-function injective tensor products

**Date:** 2026-11-16. **Finding ID:** POME-TENSOR-LINFTY-INJECTIVE-ROWPRECOMPACT-DIAGONAL-001. **Severity:** low. **Status:** verified conditional deduction (new contrast, not an error in the printed proposition). No source/body change.

## Immutable main and precise anchors

- Reviewed production main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- Integrated reading: `docs/sections/concrete-completed-tensor-products/index.html`, blob `358f584ab4004b3531629e87f1dd73bdea1256d4`, section tag `B34754B4805B`, physical lines 5–84.
- Proposition **2.19.1**, source `demailly-complex-geometry:E56C631F`, permanent tag `84C71E271314`, lines **11–30**: arbitrary-index projective \(\ell^1\) product.
- Proposition **2.19.2**, source `demailly-complex-geometry:4D711A6B`, permanent tag `96A052277244`, lines **33–54**: injective polar and \(\ell^0=c_0\) product.
- Proposition **2.19.3**, source `demailly-complex-geometry:C614F79A`, permanent tag `C9CDFE118A86`, lines **57–83**: products of arbitrary compact spaces, without a Hausdorff premise.
- Norms taken from `docs/sections/open-maps-nuclear-spaces-and-inverse-limits--nuclear-spaces-and-completed-tensor-products/index.html`, blob `ecbf01a4ed81461ba32f1e0c88c6a550ebaa8135`, §2.13 tag `54CD186EFBFD`, **lines 7–13**:
\[
\varepsilon(t)=\sup_{\|\xi\|\le1,\|\eta\|\le1}|(\xi\otimes\eta)(t)|.
\]
No nuclearity or compactification theorem is invoked.

## The new exact statement

For any (possibly empty) discrete sets \(I,J\), coefficient multiplication induces an isometric embedding
\[
\Phi:\ell^\infty(I)\widehat\otimes_\varepsilon\ell^\infty(J)
\hookrightarrow\ell^\infty(I\times J),\quad
\Phi(x\otimes y)(i,j)=x(i)y(j).
\]
Its image consists **exactly** of those bounded matrices \(a=(a_{ij})\) whose family of rows
\(\{a_i=(a_{ij})_{j\in J}:i\in I\}\)
is **relatively norm compact in \(\ell^\infty(J)\)**. Consequently \(\Phi\) is surjective **if and only if** at least one of \(I,J\) is finite.

When both sets are infinite, choose pairwise different \(i_n\in I\) and \(j_n\in J\). Put \(d_{i_nj_n}=1\) and all other entries \(0\). Then the distance in the target norm satisfies the exact sharp equality
\[
\boxed{\operatorname{dist}\bigl(d,\operatorname{im}\Phi\bigr)=1/2.}
\]
The image is a closed proper subspace, and the constant \(1/2\) is attained by the rank-one constant matrix.

## Full proof

**1. Norm and completion.** Let \(t=\sum_{r=1}^N x_r\otimes y_r\), and set \(a_{ij}=\sum_r x_r(i)y_r(j)\). For a unit norm functional \(\eta\in(\ell^\infty(J))'\), form
\(f_\eta=\sum_r\eta(y_r)x_r\). For each \(i\),
\[
|f_\eta(i)|=\bigl|\eta((a_{ij})_j)\bigr|\le\sup_j|a_{ij}|.
\]
Applying any unit \(\xi\in(\ell^\infty(I))'\) shows
\(\|t\|_\varepsilon\le\sup_{i,j}|a_{ij}|\).
Point evaluations \(\delta_i\otimes\delta_j\) prove the reverse inequality. If one set is empty, both tensor and matrix spaces are zero. Thus the injective norm is **exactly** the grid supremum norm. The completion is the uniform closure of finite sums of separated bounded functions and injects isometrically into the complete target.

**2. Necessity of compact rows.** For a finite separated sum, all rows belong to \(\operatorname{span}\{y_1,\ldots,y_N\}\) and are bounded by the matrix supremum norm. A bounded subset of a finite-dimensional normed space has a finite net for every positive radius. Uniform limits preserve total boundedness of the row family: approximate within \(\epsilon/3\) by a finite sum and use an \(\epsilon/3\)-net of its rows. Thus every matrix in the completed tensor image has relatively norm-compact rows (the row ambient Banach space is complete).

**3. Sufficiency of compact rows.** Suppose the rows of \(a\) are totally bounded. Choose \(b_1,\ldots,b_N\in\ell^\infty(J)\) with every \(a_i\) at distance strictly below \(\epsilon\) from some \(b_r\). Assign \(i\) to the first such \(b_r\), obtaining a finite disjoint partition \(I=\bigsqcup_{r=1}^NI_r\). The separated matrix
\[
b_{ij}=\sum_{r=1}^N\mathbf1_{I_r}(i)b_r(j)
\]
lies in the algebraic image and obeys \(\|a-b\|_\infty\le\epsilon\). Since \(\epsilon\) was arbitrary, \(a\in\operatorname{im}\Phi\). This uses finite nets, not a presumed sequential compactness theorem or an unjustified interchange of limits.

If \(I\) is finite, its rows form a finite family. If \(J\) is finite, all bounded row families are relatively compact in finite-dimensional \(\mathbb C^J\). These cases are surjective.

**4. Infinite-diagonal obstruction and sharp constant.** For the displayed \(d\), the rows \(d_{i_n}=e_{j_n}\) satisfy \(\|e_{j_n}-e_{j_m}\|_\infty=1\) for \(n\ne m\). If \(a\in\operatorname{im}\Phi\) and \(r=\|a-d\|_\infty<1/2\), then
\[
\|a_{i_n}-a_{i_m}\|_\infty\ge1-2r>0,\qquad n\ne m,
\]
contradicting total boundedness of the row family of \(a\). Hence distance is at least \(1/2\). The constant rank-one matrix \(a_{ij}=1/2\) has distance exactly \(1/2\), proving optimality and non-surjectivity if both factors infinite.

## Actual integrated §2.19 proof audit, not just titles

- **Proposition 2.19.1, lines 11–30.** For an algebraic \(\ell^1(I)\otimes\ell^1(J)\) tensor the coefficient \(\ell^1(I\times J)\) norm is bounded by every projective representation cost. Coordinate finite-support truncations of each factor converge projectively. Conversely a finite matrix decomposes into coordinate tensors at projective cost exactly its coefficient \(\ell^1\) norm. Finite matrices are dense in the target; even uncountable indices are valid since summable families have countable support. The printed conclusion and proof check out.
- **Proposition 2.19.2, lines 33–54.** The closed absolutely convex hull of simple unit dual tensors is the projective unit ball, so its polar is the injective unit ball. This is **not** a false identification of the full injective-tensor dual. Finite-coordinate phase tests give \(c_0(I)'=\ell^1(I)\), including arbitrary indices. Hence \(\|t\|_\varepsilon=\sup|a_{ij}|\) for \(c_0\) factors, and finite matrices are dense in \(c_0(I\times J)\). No proof defect found.
- **Proposition 2.19.3, lines 57–83.** Given \(f\in C(K\times L)\), compactness of \(L\) and finite product-neighborhood subcovers prove that \(x\mapsto f(x,\cdot)\in C(L)\) is norm continuous, **without assuming K or L Hausdorff**. Its image is compact. A finite norm net and the explicit continuous weights \(\theta_r(x)\) in the printed proof approximate \(f\) by a finite separated sum uniformly. Point evaluations give the reverse norm inequality; empty compact spaces yield zero. No unjustified use of Tietze, normality or a measure representation theorem was found.

All **three printed statements and their actual proofs** have now been directly reviewed. None is false, none has a confirmed proof gap. This local complete statement/proof reading does **not** certify §2.13 transitively or the entire chapter.

## Classification, proposed correction, dependency impact

**Classification:** low / verified conditional deduction (the new criterion and counterexample concern an **unprinted** tempting \(\ell^\infty\) analogue). **Proposed edit, not applied:** optionally add a cautionary remark after §2.19.3 with the exact criterion and distance \(1/2\); **no printed correction is necessary**. Affected reasoning: any *future* attempt to transfer the \(c_0\) or \(C(K)\) identification directly to arbitrary bounded functions. No known Pome downstream theorem is invalidated.

Earlier finding `POME-TENSOR-FOURIER-PI-EPS-GAP-001` concerns a finite-dimensional \(\ell^1\) \(\pi/\varepsilon\)-norm gap; this result concerns infinite-dimensional \(\ell^\infty\) injective **image/surjectivity** and is mathematically distinct.

Coverage: prior §2.19 partial visits; **0 newly first-visited numbered sections**, **0 new transitive end-to-end section certificates**, but all three local statements/proofs have been inspected this run (including the formerly contextual §2.19.3). Current existing ToC count **25 chapters / 747 numbered sections**, with Chapter 2 independently inspected as listing 24 sections. The excluded Demailly regularization and Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programmes remain **deferred-by-user**, neither resolved nor certified. No project build, test suite, CI, website publication, main/body/registry/permanent-tag edits.
