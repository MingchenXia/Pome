# 2026-11-13 — Equivariant projective Koszul character finding

- **ID:** `POME-PN-GL-EQUIVARIANT-KOSZUL-SERIES-001`
- **Severity/status:** low / **verified conditional deduction**; **not** a confirmed error and **not** a published repair.
- **Main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated source:** `docs/sections/hodge-theory-curvature-and-compact-vanishing--twisted-differential-forms-on-projective-space/index.html`, blob `1099020d78b8b36519f68ba31ce180c0d843f518`.
- **Permanent/source labels and anchors:** Eq. 10.51.1 `63641BE1C835` / `demailly-complex-geometry:B0B10BC1`, lines 18–20; Eq. 10.51.2 `796E28946350` / `:1D75D102`, lines 23–30; Lemma 10.51.3 `CA86EAF3228C` / `:D4085D2A`, lines 34–65; Proposition 10.51.5 `74AA0E1253DB` / `:E45C60C7`, lines 71–90; Theorem 10.51.6 `BEB304EB7449` / `:EAA2912D`, lines 95–149.
- **Hypotheses:** \(\dim_\mathbb CV=n+1\), \(0\leq p\leq n\), \(A\in GL(V)\), tautological lift/linearization, formal parameter \(t\).
- **Claim:** the generating character is \(\mathbf 1_{p=0}+[\sum_{j=p+1}^{n+1}(-1)^{j-p-1}\operatorname{tr}(\Lambda^j A^*)t^j]/\det(I-tA^*)\). Direct complete algebraic proof from the explicit equivariant Euler/Koszul splitting; see [report](../reports/2026-11-13-projective-equivariant-koszul-hilbert-series.md).
- **Specific boundary:** central \(cI\) acts in the tautologically linearized degree \(k\) by \(c^k\), despite trivial projective action; character is a \(GL(V)\)-representation statement, not canonically a \(PGL(V)\) one.
- **Proposed addition:** optional corollary after Eq. 10.51.2; **no source/body/registry edits authorized here**.
- **Dependencies:** the global-section identification in original Proposition 10.51.5 remains a printed input; original higher-cohomology Nakano/Serre vanishing chain not verified in this run. The prior `POME-PN-TWISTED-EULER-POLYNOMIAL-001` numerical Euler polynomial is **not** counted as new progress.
- **Affected dependents:** tautological linearization convention and determinant representation of top forms; no other theorem status changes.
- **Coverage:** previously sampled §10.51; first-visit increment 0, complete-section increment 0. **Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss remain deferred-by-user** (not resolved).
