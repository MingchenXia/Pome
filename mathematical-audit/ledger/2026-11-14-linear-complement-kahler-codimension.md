# 2026-11-14 — linear-complement complete Kähler cusp ledger

| ID | Severity | Status | Target | Hypotheses and conclusion | Proposed change / remaining dependency |
| --- | --- | --- | --- | --- | --- |
| `POME-LINEAR-CODIM-COMPLETE-KAHLER-CUSP-001` | low | **verified conditional deduction** | §9.31 Example 9.31.2, source `demailly-complex-geometry:12510407`, tag `D80B90CDCDA1`, docs/sections/separation-strict-exhaustions-and-coverings--complete-kahler-metrics-on-regular-open-sets/index.html lines 25–42; reviewed main `b6933b772f41b45918f7e25ed1afbbb1fd892272` | For every normal codimension `1<=k<=n`, an explicit `dd^c(|z|^2+phi(log|u|^2))` gives a complete Kähler metric on `C^n\{u=0}` with normal-collar mass `Theta(|log epsilon|^(-k))`. The complement is non-pseudoconvex exactly when `k>=2`. | Optional example expansion only. No original theorem error. Full internal Cartan–Thullen proof remains a distinct upstream dependency; no excluded Demailly/Bergman/L2/OT/regularization work revisited. |

**Deferred-by-user (unchanged, not certified):** dedicated Demailly approximation/regularization and Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas, positivity-loss proof-completion programmes.

**Review limits:** selected Example 9.31.2 and Theorem 9.31.1 hypothesis comparison only. Complete section and downstream theorem chains not certified; no modification to main, source files, registry or tags.

[Detailed self-contained calculation](../reports/2026-11-14-linear-codimension-complete-kahler-cusps.md).
