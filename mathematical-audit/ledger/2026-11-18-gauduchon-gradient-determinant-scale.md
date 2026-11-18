# POME-GAUD-GRADIENT-DETERMINANT-SCALE-001 — determinant-sensitive Gauduchon gradient bound

- **Date / status:** 2026-11-18; **low / verified conditional deduction**. No false printed theorem and no new proof gap alleged.
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; review branch precommit HEAD `672c13274fa6c23ccaf86f4a5673d01f4f77fd09`.
- **Integrated anchors:** `docs/sections/smooth-monge-ampere-equations--the-gradient-bound-by-rescaling/index.html` blob `4081db05fb0a989451c4e536f8e285501c399e81`, Proposition 14.16.1 source `non-kahler-pluripotential-theory:6B4FF351`, permanent `EFE7268223F4`, lines 13–19, proof 24–73; Eq. 14.16.3 permanent `3DCC81BE4D1E`, lines 51–66. Cone Liouville theorem §14.15.2 source `non-kahler-pluripotential-theory:7A4BB576`, permanent `AC61FE141521`, lines 51–154, and stability Lemma 14.15.1 source `D0FAF6CD`, permanent `6E3495B1A225`, lines 31–47. Matrix Eq. 14.13.1 permanent `D281466AD7B7`, lines 16–35.
- **Hypotheses:** fixed compact Hermitian background, n>=2, \(|u|\le B\), positive matrix \(Q_u\), Hessian bound \(\|dd^cu\|\le K(1+A^2)\), \(A=\sup|\partial u|\).
- **New result:** \(A\le C(X,\gamma,\gamma_0,B,K)(1+(\sup\det_\gamma Q_u)^{1/(2n)})\). Proof: if ratio diverges, rescale at gradient maximum, obtain a nonconstant bounded Lipschitz admissible maximal entire limit via vanishing determinant, contradict §14.15.2.
- **Dependencies:** fixed matrix identity §14.13.1, local elliptic compactness, conditional cone Liouville theorem §14.15.2; no transitive certification of Hessian estimate, continuation or existence.
- **Proposed correction:** none required. Optional new lemma following Proposition 14.16.1; it is NOT applied.
- **Affected:** §14.16 gradient bounds and possible §14.17 parameter refinements. Original F/b hypotheses are not being silently dropped from the printed theorem.
- **Distinctness:** not the previous `POME-GAUD-LIOUVILLE-MAXIMALITY-NECESSARY-001` radial counterexample; does not count that example as new progress.
- **Coverage:** §14.15 and §14.16 whole direct arguments inspected; §14.13 formula context; no complete transitive dependency certification. Demailly and dedicated excluded programmes remain **deferred-by-user**.
- **Report:** [complete proof](../reports/2026-11-18-gauduchon-gradient-determinant-scale.md). No software builds/tests/CI, no source/main/registry/tag/site edits.
