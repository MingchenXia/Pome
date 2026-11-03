# Classification ledger increment — 2026-11-03 — Guillemin simplex/box normalization

- **ID:** `POME-TORIC-GUILLEMIN-SIMPLEX-BOX-MASS-001`.
- **Severity / status:** low / **verified conditional deduction**. Not a false theorem or proof-gap allegation; no repair to main.
- **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Anchor:** `docs/sections/convex-analysis-and-toric-potentials--the-guillemin-reference-metric/index.html`, blob `4458eef6df84ef46d601d39506017387ed292e08`, §21.10.1, source `foundations-of-pluripotential-theory:E94A20D6`, permanent `B471B994CE64`, lines 11–92, especially Steps 1–5 lines 27–91.
- **Crosscheck dependencies (NOT certified):** §21.5.1 (`foundations-of-pluripotential-theory:4A0FAEB3`, permanent `409656CC47D4`, lines 10–41, real MA); §21.9.5 (`foundations-of-pluripotential-theory:BD98CC5B`, permanent `69D3D97E7701`, lines 139–160, lattice sections); Delzant chart data Lemma §21.8.2 (`foundations-of-pluripotential-theory:86BADE82`, permanent `41C54729DBFD`).
- **Hypotheses checked:** full-dimensional smooth integral polytope, primitive inward facet normals, integral `d,d_i>=1`, toric frames and `dd^c=i/(2pi) partial bar-partial`.
- **Exact verified calculations:** for `P=d Delta_n`, `F_0=d log(1+sum e^{x_i})-d log d` and `int omega^n=d^n=n!vol(P)=lim (n!/k^n)binom(kd+n,n)`; for `P=prod [0,d_i]`, `F_0=sum_i[d_i log(1+e^{x_i})-d_i log d_i]` and `int omega^n=n!prod d_i`. All toric boundary charts are explicitly smooth with the printed frame-transition sign. Complete proof and determinant/radial integrals: [report](../reports/2026-11-03-toric-guillemin-simplex-box-and-volume.md).
- **Proposed action:** preserve printed theorem and provenance; use these exact models as future regression examples for normalization/sign/factorials, not as a claim of global mathematical certification.
- **Affected dependents:** §21.12–13 toric volume/metric interpretations and §21.9 section-growth comparisons, *only conditionally*.
- **Coverage:** new selected proof/model check in previously unreviewed §21.10, premises-only checks §21.5/8/9; **25 chapters / 747 ToC sections / 0 fully mathematically certified complete sections**.
- **Deferred by user:** all Demailly approximation/regularization, Bergman, weighted-L2, OT, multiscale, positivity-loss entries stay deferred, not resolved.
