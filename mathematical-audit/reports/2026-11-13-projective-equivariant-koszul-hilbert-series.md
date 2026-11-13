# 2026-11-13 — Equivariant Koszul/Hilbert character of twisted holomorphic forms on projective space

**Finding ID:** `POME-PN-GL-EQUIVARIANT-KOSZUL-SERIES-001`  
**Classification:** low / **verified conditional deduction**. The printed Lemma 10.51.3, Proposition 10.51.5 and Theorem 10.51.6 are not refuted. The complete GL-character assertion below is new **relative to the registered mathematical-audit findings**, not a new Euler-characteristic polynomial or a repair of the published theorem.  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Current integrated reading edition:** `docs/sections/hodge-theory-curvature-and-compact-vanishing--twisted-differential-forms-on-projective-space/index.html`; blob `1099020d78b8b36519f68ba31ce180c0d843f518`.

## Exact integrated anchors and hypotheses

The section uses a complex vector space (V) of dimension (N=n+1), (n\geq1), with \(\mathbb P(V)\) parametrizing **lines**, the tautological \(\mathcal O(-1)\), and \(\mathcal O(k)=\mathcal O(-1)^{-k}\). Every dual is **complex linear**. Physical lines are 7–16 (conventions and complexes); 18–20 (the Euler homotopy equation, source `demailly-complex-geometry:B0B10BC1`, permanent `63641BE1C835`); 23–30 (the split Koszul equation, source `demailly-complex-geometry:1D75D102`, permanent `796E28946350`); 34–65 (Lemma 10.51.3, source `demailly-complex-geometry:D4085D2A`, permanent `CA86EAF3228C`, and dimension equation `demailly-complex-geometry:CB63447B` / `CF26F1D71E2F`); 71–90 (Proposition 10.51.5, source `demailly-complex-geometry:E45C60C7`, permanent `74AA0E1253DB`); and 95–149 (Theorem 10.51.6, source `demailly-complex-geometry:EAA2912D`, permanent `BEB304EB7449`).

The source defines \(C^{p,k}=\Lambda^pV^*\otimes\operatorname{Sym}^{k-p}V^*\), with a negative symmetric degree interpreted as zero, and \(Z^{p,k}=\ker(\gamma:C^{p,k}\to C^{p-1,k})\). The Euler contraction \(\gamma\) and exterior derivative \(d\) satisfy \(d\gamma+\gamma d=kI\). For \(k>0\), \(C^{p,k}\simeq Z^{p,k}\oplus Z^{p-1,k}\) by its displayed explicit splitting. Proposition 10.51.5 canonically identifies \(Z^{p,k}\) with \(H^0(\mathbb P(V),\Omega^p(k))\) for \(k>p\), gives \(H^0(\mathcal O)=\mathbb C\), and zero otherwise. The holomorphic coefficients and all tensor operations are equivariant for the natural \(GL(V)\) action.

## New exact equivariant statement

Let \(A\in GL(V)\), and let \(A^*\) act on sections through **the tautological linearization on \(\mathcal O(k)\)**. Put \(e_j(A)=\operatorname{tr}(\Lambda^j A^*\mid\Lambda^jV^*)\), \(e_0(A)=1\), and \(D_A(t)=\det(I-tA^*)=\sum_{j=0}^{N}(-1)^j e_j(A)t^j\). Then, in the formal-power-series ring \(\mathbb C[[t]]\), for every \(0\leq p\leq n\),

\[
\boxed{
\sum_{k=0}^{\infty}
 \operatorname{tr}\!\left(A^*\mid H^0(\mathbb P(V),\Omega^p(k))\right)t^k
=\mathbf1_{p=0}
+\frac{\displaystyle\sum_{j=p+1}^{N}(-1)^{j-p-1}e_j(A)t^j}{D_A(t)}.
}
\]

The expression is exact for *every* invertible matrix, including nondiagonalizable ones. In particular, the first nonzero GL-module in the positive-twist sequence is \(H^0(\Omega^p(p+1))\simeq\Lambda^{p+1}V^*\), via contraction by the Euler vector field. For \(p=n\), the formula reduces to the canonical determinant representation
\[
\bigoplus_{k\geq0}H^0(\Omega^n(k))t^k
\simeq (\det V^*)\,t^{n+1}\bigoplus_{m\geq0}\operatorname{Sym}^mV^*\,t^m
\]
as a graded \(GL(V)\)-module (the notation on the right is formal graded-module notation).

## Direct proof; no analytic vanishing theorem invoked

For fixed \(k>0\), the displayed maps in Eq. 10.51.2 commute with the natural \(GL(V)\) action: the radial field, contraction, exterior differentiation and division by the scalar \(k\) are all equivariant. Thus the splitting holds **as representations**, not only as vector spaces. If \(z_{p,k}(A)\) is the trace on \(Z^{p,k}\), then

\[
z_{p,k}(A)+z_{p-1,k}(A)
=\operatorname{tr}(\Lambda^p A^*)\,
 \operatorname{tr}(\operatorname{Sym}^{k-p}A^*)\quad(k>0),
\]
with \(z_{-1,k}=0\). At \(k=0\), \(z_{0,0}=1\) and \(z_{p,0}=0\) for all \(p>0\); the positive-weight splitting is **not** used at weight zero.

Triangularize \(A^*\). Each monomial of degree \(m\) in a triangular eigenbasis contributes the product of its diagonal eigenvalues, so direct summation of the monomial traces gives, without invoking an external character theorem,
\[
\sum_{m\geq0}\operatorname{tr}(\operatorname{Sym}^m A^*)t^m
=\prod_{i=1}^{N}(1-\lambda_i t)^{-1}=D_A(t)^{-1}.
\]
Writing \(H_p(A;t)=\sum_{k\ge0}z_{p,k}(A)t^k\), the recurrence for \(k>0\) yields, for \(p>0\),
\[
H_p(A;t)
=\frac{e_p(A)t^p}{D_A(t)}-H_{p-1}(A;t)+\mathbf1_{p=1},
\qquad H_0(A;t)=D_A(t)^{-1}.
\]
Hence
\[
H_p(A;t)=\frac{\sum_{j=0}^{p}(-1)^{p-j}e_j(A)t^j}{D_A(t)}-(-1)^p
\qquad(p>0).
\]
Subtracting \((-1)^pD_A(t)\) in the numerator cancels *all* terms of degrees \(0,\ldots,p\), leaving exactly \(\sum_{j=p+1}^{N}(-1)^{j-p-1}e_j(A)t^j\), proving the boxed formula. For \(p=0\), observe separately that \(D_A(t)^{-1}=1+\sum_{j=1}^{N}(-1)^{j-1}e_j(A)t^j/D_A(t)\). This completes the proof including weight zero.

The \(k=p+1\) coefficient is \(e_{p+1}(A)\), and Eq. 10.51.1 identifies its representation with \(\Lambda^{p+1}V^*\): \(\gamma: \Lambda^{p+1}V^*\to Z^{p,p+1}\) is an isomorphism with inverse \(d/(p+1)\). Taking \(p=n=N-1\) leaves only the \(j=N\) term; the generating function \(e_N(A)t^N/D_A(t)\) proves the top-form determinant claim.

## Independent specializations and normalization boundary

At \(A=I\), \(e_j(I)=\binom Nj\). For \(n=2\), the complete degree-zero Hilbert series are
\[
H_0(I;t)=\frac1{(1-t)^3},\quad
H_1(I;t)=\frac{3t^2-t^3}{(1-t)^3},\quad
H_2(I;t)=\frac{t^3}{(1-t)^3}.
\]
Thus \(h^0(\Omega^1(k))=k^2-1\) for \(k\ge2\) and \(h^0(\Omega^2(k))=\binom{k-1}{2}\) for \(k\ge3\). The leading coefficient in general is \(\binom np k^n/n!\), consistent with rank \(\Omega^p=\binom np\). These **dimension** comparisons are checks, not the new finding: the previously registered `POME-PN-TWISTED-EULER-POLYNOMIAL-001` already covers the nonequivariant Euler-characteristic polynomial and Serre symmetry.

A nontrivial check is \(n=2\), \(p=1\): \(H_1(A;t)=(e_2(A)t^2-e_3(A)t^3)/D_A(t)\), so the natural degree-two representation is \(\Lambda^2V^*\), not a scalar vector space. For \(A=cI\), the action in degree \(k\) is exactly \(c^k\) times the identity even though its **projective** action on \(\mathbb P(V)\) is trivial. Hence this character identity depends on the **chosen lift** \(A\in GL(V)\) and the tautological linearization; it must not be advertised as a character of \(PGL(V)\) without adjusting the twist. This is an actual normalization distinction, not a defect in the printed result.

## Status, dependencies, correction and affected results

**Status:** verified conditional deduction, not a false theorem, genuine duplication, or repaired published statement. **Correction proposed:** optional separate corollary after the explicit GL-equivariant splitting (10.51.2), with this character formula and the central-scalar warning; there is no need to alter the original statement or permanent labels. The character calculation is algebraically complete **conditional only on** the source's identification of global sections with horizontal polynomial forms (Proposition 10.51.5), which was rechecked at physical lines 80–89. No use was made of Demailly approximation, Bergman, L², Ohsawa–Takegoshi, multiscale arguments or positivity-loss techniques. The negative-twist and higher-cohomology identifications in Theorem 10.51.6 remain dependent on its own Nakano/Serre/Hodge inputs and are **not** newly certified.

**Dependents:** the GL-representation normalization of Proposition 10.51.5 and of the top-form determinant example at lines 143–149; representation-sensitive uses of these cohomology groups, not the analytic positivity/vanishing proof. No dependency or other finding was silently reclassified.

**Actual coverage:** additional *selected proof-level review* in already partially audited **§10.51**, particularly Eqs. 10.51.1–2 and Proposition 10.51.5, with statement/representation comparison to Lemma 10.51.3 and Theorem 10.51.6. **Zero newly first-visited numbered sections and zero fully certified sections.** Current main table of contents: 25 chapters and 747 numbered sections; all previous ledger findings and user deferrals remain unchanged. No build, test, CI, source, main, site or formalization run is claimed.
