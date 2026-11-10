# Classified ledger — 2026-11-11 — elliptic ruled symmetric tensor algebra

- ID: POME-RULED-SYMTENSOR-BIGRADED-HILBERT-INDECOMP-001
- Severity: low.
- Status: verified conditional deduction (not a confirmed error, proof-gap repair, or full theorem-chain certification).
- Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
- Reader: docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--symmetric-tensors-on-split-elliptic-ruled-surfaces/index.html, blob f361ebba006461edd8e2aca3b48a501938510e2e; source/permanent tags EA1E9CBB/2604E6F7AC76 (lines 28–75), 4B3CCF12/711AF6E8C0D8 (80–129), 81C41791/654B70C2AFD7 (137–160), 38263A71/3B7C9C492833 (165–193), all from non-kahler-pluripotential-theory. Degree d>0 context §12.30.2, source F0217EE5, tag 68FEC9C7A0BC (lines 49–56), blob 2a3e0f45924a48f701cf8de0526f0945824c0574.
- Finding: the bigraded Hilbert series equals 1/(1-x)+dxy/((1-x)^2(1-xy)^2); weight-one indecomposables R_+/(R_+)^2 have canonical dimension d in **every** tensor degree r>=1. Hence degree-N truncations require at least dN+1 algebra generators even though the ordinary Hilbert series is rational.
- Proof/reproducibility: see reports/2026-11-11-elliptic-ruled-symmetric-tensor-bigraded-hilbert-generators.md; only finite coefficient crosscheck r<=8 was performed.
- Affected dependents: optional §12.31.4 strengthening, contextual §12.32; no theorem refuted and no source patch applied.
- Open/conditional: independently certifying the full geometric and elliptic cohomological input chain is outside this run. All existing resolved/unresolved/deferred items remain in their previous state. Excluded regularization programme remains deferred-by-user.
- Actual coverage: selected §12.31 algebraic consequence; §12.30.2 contextual. 0 first visits, 0 whole-section certifications; actual ToC 25/747.
