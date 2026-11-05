# Classified findings — 2026-11-06 — polar-boundary minimum principle

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Exact integrated source:** `docs/sections/polar-sets-capacity-and-sweeping/index.html`, blob `aa814f26482e8ed27e51c945e9202c797449158b`, physical lines 24–38, context 60–81 and 121–130. Primary source `classical-potential-theory:B6612815`, permanent `09FD5942CD4F`.

| Stable finding ID | Severity / status | Exact claim checked | Correction |
| --- | --- | --- | --- |
| `POME-CLASSICAL-MINIMUM-INFINITY-NECESSARY-001` | **low / verified conditional deduction** | For every \(d\ge3\), on \(\Omega=\{|x|>1\}\), \(u=|x|^{2-d}-1\) is smooth bounded harmonic with zero *finite* boundary limit but \(u<0\) and \(u\to-1\) at infinity. Dropping the printed infinity condition is false even without a polar exception. | **No theorem change.** Optional sharpness example after §4.3.4. |
| `POME-CLASSICAL-MINIMUM-LOWERBOUND-NECESSARY-001` | **low / verified conditional deduction** | For every \(d\ge2\), on \(\Omega=\{0<|x|<1\}\), \(Z=\{0\}\) polar and \(u=\log|x|\) (\(d=2\)) or \(u=1-|x|^{2-d}\) (\(d\ge3\)) is harmonic, zero on the outer boundary, negative throughout, and unbounded below at the permitted exception. Dropping the lower bound while retaining polar exceptions is false even in bounded domains. | **No theorem change.** Optional separate example; do not conflate with the case \(Z=\varnothing\). |

**Complete mathematical justification:** [dated English report](../reports/2026-11-06-classical-polar-boundary-minimum-sharpness.md), including direct radial Laplacian calculations and all boundary quantifiers.

**False theorem vs proof gap:** Neither finding is a printed false theorem, a proof-gap certification, a numerical check or a repaired proof. Theorem 4.3.4 is consistent with both. The general Greenian boundary behavior referenced in §4.3.10 is **not certified** by checking the compact-support use at line 128.

**Downstream interfaces, not full coverage:** Theorem 4.3.7 (source `classical-potential-theory:5388371B`, tag `ABDF7610F7B2`), and Theorem 4.3.10 (source `classical-potential-theory:FA6C8523`, tag `C4F5D8B270EB`): only boundary principle dependence inspected, other steps unreviewed. See [additive coverage](../coverage/2026-11-06-ch4-polar-boundary-minimum-models.md).

**Existing ledgers:** all pre-existing confirmed errors, proof gaps, candidates, external dependencies, duplications, verified repairs and conditional deductions retain their prior statuses. Demailly approximation/regularization and dedicated Bergman, weighted-\(L^2\), OT, multiscale-atlas and positivity-loss proof-completion remain **deferred-by-user**, not resolved, reopened or certified.
