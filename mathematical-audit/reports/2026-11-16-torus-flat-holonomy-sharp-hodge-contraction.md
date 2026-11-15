# 2026-11-16 — sharp flat-holonomy Hodge contraction on higher-dimensional tori

**Finding ID:** POME-HODGE-TORUS-SHARP-HOLONOMY-HOMOTOPY-001  
**Classification:** low / verified conditional deduction (the explicit Fourier theorem is proved independently; the general printed theorems are not transitively certified).  
**Printed status:** no incorrect theorem or failed proof is asserted; Proposition 2.21.2, Theorem 2.21.3, Corollary 2.21.5, and Theorem 10.46.4 survive this model check.  
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272 (2026-11-16 read).  
**Audit branch:** review/mathematical-audit; this is audit documentation, not a source amendment.

## Exact current reading-edition anchors and provenance

- docs/sections/complete-metric-laplacians-and-reduced-cohomology/index.html, blob 93b74f8a110bb6c45a7e53cdaed0910af7eb5118: the hypotheses and source convention at physical lines 5–9; Proposition 2.21.2 at 10–38, source demailly-complex-geometry:CF433F03, permanent tag E40060D5FC24; Theorem 2.21.3 and its form-domain identity at 40–83, source demailly-complex-geometry:CDC5D23B, permanent tag CE09CDC33E77, equation source demailly-complex-geometry:4AEDA159, permanent tag F4319A4DE391 at 46–49; Corollary 2.21.5 at 85–104, source demailly-complex-geometry:63A1AB33, permanent tag A76DD53006C1.
- docs/sections/differential-operators-and-elliptic-regularity--maximal-domains-and-formal-adjoints/index.html, blob 63b73681ef8b511fff1308685388f027ead75a77: Proposition 2.17.2, source label demailly-complex-geometry:5AFFEC4D76E3, permanent tag 5AFFEC4D76E3, for the formal-adjoint sign convention. It is a background crosscheck only.
- docs/sections/hodge-theory-curvature-and-compact-vanishing--compact-hodge-theory-and-analytic-duality/index.html, blob b7001303a35ddd5c91f40e81cfc93523e8d6b8ab: Theorem 10.46.4, source demailly-complex-geometry:7CE52240, permanent tag BD1EEDFB2146, at physical lines 108–140 (finite-dimensional harmonic representatives and closed smooth images). This is a comparison, not a complete rereview of section 10.46.

These references were read as current integrated reader statements; the source identities are provenance, not a replacement by source theorem numbers.

## Exact model theorem (real dimension m >= 2)

On the Euclidean torus T^m = R^m/(2π Z)^m with oriented coordinate coframe dx_1,...,dx_m, take the trivial Hermitian complex line and its flat *metric* connection

\[
\nabla_\alpha=d+i\sum_{j=1}^m\alpha_j\,dx_j,\qquad \alpha\in\mathbb R^m.
\]

The holonomy around the j-th fundamental circle is \(\exp(-2\pi i\alpha_j)\) under the convention for parallel transport; the sign does not affect triviality. Let \(D_\alpha\) be the exterior covariant derivative, \(\delta_\alpha=D_\alpha^*\) its maximal Hilbert adjoint, and \(\Delta_{\alpha,q}=D_\alpha\delta_\alpha+\delta_\alpha D_\alpha\) acting on degree-q forms. Define

\[
d(\alpha)=\operatorname{dist}(\alpha,\mathbb Z^m),\qquad
\gamma(\alpha)=
\begin{cases}
d(\alpha),&\alpha\notin\mathbb Z^m,\\
1,&\alpha\in\mathbb Z^m.
\end{cases}
\]

Then the following hold in *every* form degree \(0\leq q\leq m\).

1. The complete \(L^2\) spectrum, with multiplicities, is the multiset
   \[
   \operatorname{Spec}(\Delta_{\alpha,q})
   =\{\,|k+\alpha|^2:k\in\mathbb Z^m\,\},\qquad
   \text{each Fourier frequency having multiplicity }\binom mq.
   \]
   In particular, all the nonzero eigenvalues are at least \(\gamma(\alpha)^2\).
2. The harmonic space has dimension \(\binom mq\) if \(\alpha\in\mathbb Z^m\), and zero otherwise. Thus **all twisted cohomology degrees vanish as soon as even one holonomy component is nontrivial**. The jump locus is the *joint* integral lattice, not a union of coordinate-integral hyperplanes.
3. Let \(\Pi_{\alpha,q}\) be the orthogonal harmonic projection, and \(G_{\alpha,q}\) the inverse of the Laplacian on \((\ker\Delta_{\alpha,q})^\perp\), extended as zero on its kernel. Then
   \[
   \|G_{\alpha,q}\|_{L^2\to L^2}=\gamma(\alpha)^{-2}
   \]
   and the canonical degree-minus-one contracting homotopy \(H_{\alpha,q}=\delta_\alpha G_{\alpha,q}\) satisfies
   \[
   D_\alpha H_\alpha+H_\alpha D_\alpha=I-\Pi_\alpha
   \quad\text{on smooth forms},\qquad
   \|H_{\alpha,q}\|_{L^2\to L^2}=\gamma(\alpha)^{-1}\quad(1\le q\le m).
   \]
   Its degree-zero component is zero. Both constants are exact.
4. For every smooth form orthogonal to the harmonic forms, the optimal global energy estimate is
   \[
   \|u\|_2^2\leq\gamma(\alpha)^{-2}
   \bigl(\|D_\alpha u\|_2^2+\|\delta_\alpha u\|_2^2\bigr).
   \]
   Every displayed constant is attained by a single nearest admissible Fourier mode. The differential ranges are closed for each fixed \(\alpha\).
5. For \(\alpha\notin\mathbb Z^m\), any *bounded* degree-minus-one contracting homotopy \(K\) satisfying \(K_1D_{\alpha,0}=I\) on smooth zero-forms must obey \(\|K_1\|\geq d(\alpha)^{-1}\). Thus the canonical \(H_{\alpha,1}\) has the smallest possible operator norm, even among homotopies that mix Fourier frequencies.
6. The degree-q heat trace is exactly
   \[
   \operatorname{Tr}\exp(-t\Delta_{\alpha,q})
   =\binom mq\sum_{k\in\mathbb Z^m}e^{-t|k+\alpha|^2},\qquad t>0.
   \]
   This is smooth in \(\alpha\), although the harmonic dimension is discontinuous at every integer parameter. As \(\alpha\to a\in\mathbb Z^m\) through nonintegral vectors, the optimal homotopy norm diverges exactly as \(1/|\alpha-a|\).

## Independent proof

Use the orthonormal Fourier basis \(e_k(x)=(2\pi)^{-m/2}e^{ik\cdot x}\) and the orthonormal real exterior basis \(dx_I\). Write \(v=k+\alpha\). Because the coefficients of the flat connection are constant,

\[
D_\alpha(e_k\eta)=i e_k(v^\flat\wedge\eta),\qquad
\delta_\alpha(e_k\eta)=-i e_k\iota_v\eta.
\]

The second identity follows from the complex Hilbert-adjoint convention (linear in the first argument) and the elementary adjunction between exterior multiplication and contraction. In particular, the sign is fixed, rather than inferred from a source's unscaled complex-geometric curvature notation. The exterior-algebra anticommutator satisfies

\[
\iota_v(v^\flat\wedge\eta)+v^\flat\wedge\iota_v\eta
=|v|^2\eta.
\]

Consequently \(\Delta_{\alpha,q}(e_k\eta)=|k+\alpha|^2e_k\eta\), in every degree, with no connection-curvature term. Complete Fourier expansion identifies the maximal self-adjoint realization with diagonal multiplication by \(|k+\alpha|^2\) on the domain of square-summable weighted coefficients. No unproved interchange of unbounded operators is made: start on Fourier polynomials, where every identity is finite, and close using this explicit diagonal domain. This directly verifies the model instance of the main maximal-domain statement.

A frequency has zero eigenvalue exactly when \(k=-\alpha\in\mathbb Z^m\). There is at most one such frequency; every constant exterior basis vector contributes one harmonic form. For nonzero frequencies, the smallest \(|k+\alpha|\) is \(\gamma(\alpha)\): at an integral parameter the shortest nonzero vector of \(\mathbb Z^m\) has length one. Hence the reduced inverse \(G_\alpha\) is diagonal with scalar \(|v|^{-2}\) away from the kernel, proving its exact norm.

On a nonzero frequency, \(H_\alpha\) is the multiplier \(-i\iota_v/|v|^2\). The exterior-operator norm of \(\iota_v:\Lambda^q\to\Lambda^{q-1}\) is exactly \(|v|\) for \(q\ge1\): a simple wedge containing \(v^\flat/|v|\) attains equality, while the decomposition into its \(v\)-containing and \(v\)-orthogonal parts gives the upper bound. This proves the claimed exact norm. Multiplying the anticommutator by \(|v|^{-2}\) yields the homotopy identity on each nonzero frequency; on the zero frequency its right-hand side is zero, exactly \(I-\Pi\). Fourier-polynomial density extends the claimed bounded operators, and the identity holds on smooth forms (also on the appropriate graph domains). Since \(D_\alpha^2=0\), for a closed \(L^2\) form \(f\), the identity gives \(f=\Pi f+D_\alpha Hf\) distributionally; \(Hf\) lies in the maximal domain of \(D_\alpha\). Thus each \(L^2\) closed-form range equals the corresponding exact-form range plus the finite harmonic part, and the ranges are closed. The full Hodge decomposition follows degreewise. The same diagonal eigenvalue calculation gives the energy estimate and equality on a minimal nonzero mode.

For the optimality assertion take \(k_0\in\mathbb Z^m\) minimizing \(|k+\alpha|=d(\alpha)>0\), and \(f=e_{k_0}\) a unit zero-form. The degree-zero homotopy identity forces \(K_1D_{\alpha,0}f=f\). But \(\|D_{\alpha,0}f\|=d(\alpha)\), so \(1\le\|K_1\|d(\alpha)\). The constructed \(H_{\alpha,1}\) attains equality. Since no differential limit or selected subsequence is involved, this lower bound holds for every bounded homotopy, including non-Fourier-diagonal ones.

Finally, each eigenvalue occurs in \(\binom mq\) exterior components, proving the trace formula. For \(\alpha\) in a compact set, the Gaussian series and every fixed-order parameter derivative converge absolutely and uniformly after a common polynomial-times-Gaussian majorant. This justifies smoothness of the trace in \(\alpha\); it does *not* imply continuity of the multiplicity of the zero eigenvalue. Near \(a\in\mathbb Z^m\), the unique nearest frequency is \(-a\), so \(d(\alpha)=|\alpha-a|\), proving the sharp divergent inverse norm. All claims follow.

## Mathematical audit decision

The explicit higher-dimensional computation agrees with the **printed** Proposition 2.21.2, Theorem 2.21.3, Corollary 2.21.5 and compact Hodge Theorem 10.46.4. No false original theorem, proof gap, canonical duplicate or tag conflict has been found in the selected passages. This is a new joint-parameter, all-degree spectral/heat/cochain-norm calculation, rather than the already recorded 2026-10-28 *one-circle* cohomology-dimension example (POME-HODGE-HARMONIC-UPPER-SEMICONT-001). That earlier result is not re-registered or revised.

**Potential editorial clarification, not a required repair:** the constants in compact Hodge decompositions depend on holonomy and can blow up sharply when a family approaches trivial holonomy, even though all fixed-parameter ranges are closed. This is a proposed illustration only; no change to the mathematical body or theorem statements is authorized here.

**Dependents checked:** the fixed-connection Hodge decomposition at 2.21.5 and the compact smooth decomposition at 10.46.4 are compatible with the example; no transitive verification of the general elliptic regularity, complete-cutoff lemma, arbitrary flat bundles or general parameter families is asserted. No Demailly approximation/regularization, Bergman, L2-estimate, Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof programme was opened.

**Coverage delta:** substantive additional *selected theorem/model* review in already partly visited sections 2.17, 2.21 and 10.46; **0 newly first-visited numbered sections; 0 complete sections certified**. Actual current table of contents: 25 chapters / 747 numbered sections. No project build, project tests, GitHub Actions, source edits, publication, or permanent-tag changes were carried out.
