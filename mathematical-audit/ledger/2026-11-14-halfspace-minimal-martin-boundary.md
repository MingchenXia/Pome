# 2026-11-14 ledger: explicit upper-halfspace Martin boundary

| Stable ID | Status | Severity | Base main | Scope | Proof and remaining dependency | Correction / affected statements |
| --- | --- | --- | --- | --- | --- | --- |
| `POME-MART-HALFSPACE-ALL-MINIMAL-POISSON-001` | **verified conditional deduction** (no printed error) | low | `b6933b772f41b45918f7e25ed1afbbb1fd892272` | `docs/sections/green-energy-and-martin-boundaries/index.html` lines 106, 110–122, 166–185, 190–213, permanent `9D6B5CF5E0CF`, `6736FBE7368C`, `0E65F552B1A6`; `docs/sections/kelvin-transforms-and-half-space-potentials/index.html` lines 57–76, `21F1298C637C`, `6BC86EEF03A9` | Direct reflection/asymptotic/topological proof yields all kernels and all minimal points for \(d\ge3\), and identifies finite Martin measure with weighted Radon boundary data. Upstream existence of arbitrary positive harmonic Poisson/Radon representation (Theorem 3.2.6) not transitively certified; planar \(d=2\) not checked. | Suggested optional explanatory halfspace example in §4.5, not a required theorem correction. Dependents: halfspace cases of 4.5.9/12/13 and 3.2.6. |

**Preserved:** all prior confirmed errors, open proof gaps, external inputs and deferred-by-user findings remain unchanged; do not upgrade this conditional model check to general Martin or full-section certification.

[Full dated proof](../reports/2026-11-14-upper-halfspace-explicit-minimal-martin-boundary.md) · [precise coverage](../coverage/2026-11-14-ch4-halfspace-minimal-martin-boundary.md).
