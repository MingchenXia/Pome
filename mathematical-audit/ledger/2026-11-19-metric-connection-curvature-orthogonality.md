# 2026-11-19 — metric-connection curvature and orthogonality

- **Stable finding ID:** \`POME-CONN-CURVATURE-ORTHOGONALITY-IFF-FLAT-001\`.
- **Severity / status:** **low / verified conditional deduction**; *no false printed theorem* and *no independently established proof gap*.
- **Scope / baseline:** \`main\` \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`, \`docs/sections/complete-metric-laplacians-and-reduced-cohomology/index.html\` blob \`93b74f8a110bb6c45a7e53cdaed0910af7eb5118\`, directly inspected mathematical lines **7–103**.
- **Source / permanent:** Proposition 2.21.2 \`demailly-complex-geometry:CF433F03\` / \`E40060D5FC24\` (10–36); Theorem 2.21.3 \`:CDC5D23B\` / \`CE09CDC33E77\` (40–81); Corollary 2.21.5 \`:63A1AB33\` / \`A76DD53006C1\` (85–103).
- **Hypotheses:** smooth finite-rank Hermitian bundle with metric connection; complete Riemannian base for maximal Hilbert adjoints. Compact support suffices for the elementary curvature identity.
- **Complete mathematical check:** \(\langle D_0u,\delta_2\eta\rangle=\langle R^\nabla u,\eta\rangle\); vanishing of all such pairings iff \(R^\nabla=0\). On a flat \(2\pi\)-periodic torus with \(\nabla=d+i\sin x\,dy\), choose \(u=1\) and \(\eta=i\cos x\,dx\wedge dy\): pairing \(=2\pi^2>0\).
- **Correction / dependents:** preserve the printed *flat* Corollary 2.21.5 and unrestricted Theorem 2.21.3; consider a cautionary remark blocking any nonflat Hodge-decomposition reuse. Reduced \(L^2\) cohomology and exact/coexact orthogonality require a genuine complex \(D^2=0\).
- **Residual:** §6.26.1 gradient cutoffs; §10.82.2 wedge/contraction and principal symbol; §2.18.3 local elliptic regularity; Hilbert adjoint and commutator lemmas — as existing internal dependencies, **not** fully transitive certified. No new external theorem invoked; regularization programme remains deferred by user.
- **Evidence:** [full proof](../reports/2026-11-19-metric-connection-curvature-orthogonality.md); [exact coverage](../coverage/2026-11-19-ch2-metric-connection-curvature-orthogonality.md).
