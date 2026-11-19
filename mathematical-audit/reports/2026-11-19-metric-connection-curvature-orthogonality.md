# Complete metric connections: exact curvature obstruction to exact–coexact orthogonality

**Finding:** `POME-CONN-CURVATURE-ORTHOGONALITY-IFF-FLAT-001`  
**Date:** 2026-11-19  
**Classification:** low / **verified conditional deduction** (the printed statements are correct).  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`  
**Integrated HTML:** `docs/sections/complete-metric-laplacians-and-reduced-cohomology/index.html` (blob `93b74f8a110bb6c45a7e53cdaed0910af7eb5118`).  
**Actual direct review:** all mathematical lines 7–103 of §2.21. No transitive verification of invoked upstream theorems is claimed.

## Precisely anchored integrated statements

- Proposition 2.21.2, source `demailly-complex-geometry:CF433F03`, permanent tag `E40060D5FC24`, lines 10–36: equality of maximal Hilbert adjoints and compactly supported graph cores for a metric connection **without** flatness.
- Theorem 2.21.3, source `demailly-complex-geometry:CDC5D23B`, permanent tag `CE09CDC33E77`, lines 40–81: maximal connection-Hodge Laplacian, joint weak-energy domain, essential self-adjointness, smooth kernel. Flatness is **not** assumed.
- Corollary 2.21.5, source `demailly-complex-geometry:63A1AB33`, permanent tag `A76DD53006C1`, lines 85–103: orthogonal Hodge decomposition and reduced cohomology **under flatness**. Its proof at lines 95–102 uses `D^2=0`.

The additional result below proves that the flatness hypothesis in the *orthogonality and complex* part cannot be dropped, even on a flat compact Kähler base. It does not invalidate Proposition 2.21.2 or Theorem 2.21.3.

## Exact characterization (all dimensions, all bundle ranks)

Let \(M\) be a smooth Riemannian manifold without boundary and \(E\to M\) a finite-rank Hermitian bundle with a smooth metric connection \(\nabla\). Let \(D_q:\Omega_c^q(E)\to\Omega_c^{q+1}(E)\) be the exterior covariant derivative and \(\delta_{q+2}=D_{q+1}^{\mathrm{formal}*}\). The following are equivalent:

1. \(\nabla\) is flat, i.e. \(R^\nabla=0\).
2. \(\langle D_0 u,\delta_2\eta\rangle_{L^2}=0\) for every \(u\in\Omega_c^0(E)\), \(\eta\in\Omega_c^2(E)\).
3. The compactly supported exact one-forms \(D_0\Omega_c^0(E)\) are orthogonal to the compactly supported coexact one-forms \(\delta_2\Omega_c^2(E)\).

When \(M\) is complete, Proposition 2.21.2 identifies the Hilbert adjoints; these equivalent properties also characterize orthogonality of the **closures** of the maximal images \(\operatorname{Ran}D_0\) and \(\operatorname{Ran}\delta_2\) (with the appropriate degree indices). Consequently, if a proposed extension of Corollary 2.21.5 asserts its orthogonal exact/coexact decomposition for every degree without flatness, it is false.

**Proof.** Formal adjunction for compactly supported smooth forms gives the exact, normalization-independent identity
\[
\langle D_0u,\delta_2\eta\rangle
=\langle D_1D_0u,\eta\rangle
=\langle R^\nabla u,\eta\rangle.
\tag{1}
\]
Flatness implies (2). Conversely, if (2) holds, equation (1) for all compactly supported test two-forms \(\eta\) yields \(R^\nabla u=0\) as a smooth two-form for every compactly supported section \(u\). At any point \(x\) and any \(v\in E_x\), choose a compactly supported local section with value \(v\) at \(x\). It follows that \(R^\nabla_xv=0\); hence \(R^\nabla=0\). Conditions (2) and (3) are the same statement. In dimensions zero and one every connection has identically zero two-form curvature, and (2) is vacuous when \(\Omega^2=0\), so the equivalence remains valid.

For completeness of the Hilbert-space claim: flatness gives \(D_1D_0u=0\) distributionally for every \(u\in\operatorname{Dom}D_0\); zero is in \(L^2\), so \(D_0u\in\operatorname{Dom}D_1\) and for every \(\eta\in\operatorname{Dom}\delta_2=(D_1)^*\),
\[
\langle D_0u,\delta_2\eta\rangle
=\langle D_1D_0u,\eta\rangle=0.
\]
Continuity extends this to closures. Conversely, orthogonality of the closures implies (2) by restriction to compact test forms and therefore flatness by (1). This uses the maximal-adjoint identification in Proposition 2.21.2; it does *not* assume closed image ranges.

## Smooth compact countermodel with an explicit nonzero pairing

Take the flat two-torus \(M=(\mathbb R/2\pi\mathbb Z)^2\) with \(dx^2+dy^2\), and the trivial Hermitian line bundle with unitary connection
\[
\nabla=d+\mathrm i\sin x\,dy.
\]
This is globally smooth; the curvature is \(R^\nabla=\mathrm i\cos x\,dx\wedge dy\not\equiv0\). Set \(u=1\) and \(\eta=R^\nabla u=\mathrm i\cos x\,dx\wedge dy\). These are smooth globally supported sections/forms on a compact manifold. Equation (1) yields
\[
\boxed{\ 
\langle D_0u,\delta_2\eta\rangle
=\|R^\nabla u\|_{L^2}^2
=\int_0^{2\pi}\!\int_0^{2\pi}\cos^2x\,dx\,dy
=2\pi^2>0.\ }
\]
In particular \(D_1D_0u\ne0\): even the sequence \(\Omega^0(E)\xrightarrow{D_0}\Omega^1(E)\xrightarrow{D_1}\Omega^2(E)\) is not a complex. The base is compact, geodesically complete, and Kähler, and the coefficient bundle is topologically trivial. Thus neither base completeness nor base Kählerness repairs the loss of flatness. This is a test of a **hypothesis**, not a counterexample to the actual flat-connection Corollary 2.21.5.

## Review of the integrated proof steps and dependencies

- **Proposition 2.21.2, lines 20–36:** distributional closedness, complete-metric cutoffs, the \(D,\delta\) product commutators, local first-order matrix mollifier commutators and graph-core argument are organized in the correct logical order. No invalid use of flatness was found. Internal inputs: complete gradient cutoffs at §6.26.1, wedge/contraction estimate at §10.82.2, and the locally established commutator calculation. Their complete prior proofs were not re-certified.
- **Theorem 2.21.3, lines 59–81:** scalar principal symbol and local \(H^2\) regularity allow the compact cutoff test; the resulting quadratic estimate controls the energy and passes to \(V\). The adjoint-domain argument identifies the maximal operator with its adjoint, rather than merely proving symmetry. The compact core / double-adjoint step is explicitly present; the full upstream proofs of elliptic regularity §2.18.3 and Hilbert graph-orthogonality were not re-certified. The zero-dimensional clause is separate.
- **Corollary 2.21.5, lines 95–103:** correctly assumes flatness before claiming \(\operatorname{Ran}D\subseteq\ker D\), uses closed kernels and orthogonal complements, and explicitly refrains from a closed-range assertion. Equation (1) shows the necessity of that assumption for the exact/coexact orthogonality. No contradiction of the printed corollary was found.

**Proposed documentation-only correction:** add a short remark after Corollary 2.21.5 that \(\langle Du,\delta\eta\rangle=\langle R^\nabla u,\eta\rangle\) and that the displayed orthogonal splitting cannot generally extend to nonflat metric connections. Keep the printed flatness hypothesis and Theorem 2.21.3 unchanged.

**Affected dependents:** any use of §2.21.5 to identify reduced \(L^2\)-cohomology with harmonic forms, or to declare exact/coexact images orthogonal, must verify \(D^2=0\). §2.21.3 self-adjointness remains applicable to curved connections. No source, publication, registry, canonicalization or permanent-tag edits are authorized by this report.

**Coverage delta:** §2.21, all three integrated proof-bearing entries directly checked (lines 7–103), **+1 complete direct section reading; +0 completed transitive proof-chain certificates**. Earlier complete/partial legacy status is not claimed without reconciling historical reports. Other chapters are not certified. Demailly regularization and the specifically excluded Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss proof-completion programmes remain **deferred-by-user**, not verified; routine Hilbert-space \(L^2\) analysis in this distinct section was checked, not the excluded approximation programme. No tests, builds, CI, or website changes were performed.
