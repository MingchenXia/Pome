# 2026-11-08 — classified audit ledger: punctured bidisk

| Stable finding ID | Severity / status | Source, anchor and factual finding | Proposed disposition / affected dependents |
| --- | --- | --- | --- |
| `POME-STEIN-PUNCTURED-BIDISK-HARTOGS-MAX-001` | **low / verified conditional deduction** | Theorem 9.26.1 `demailly-complex-geometry:57C45FF9` / `C1041DBBD4EC` (lines 7–14); Proposition 9.26.2 `demailly-complex-geometry:310AF940` / `A1FE9ED85940` (lines 40–66). `C^2\{0}` has global point separation and a strict PSH function but neither a PSH exhaustion nor holomorphic convexity; a two-disk maximum argument proves both facts. | Keep global holomorphic convexity in the exhaustion conclusion, closedness in submanifold inheritance, and distinguish the separately valid finite-intersection clause. Optional reviewed exposition patch only. **No printed theorem is false.** |

Production main `b6933b772f41b45918f7e25ed1afbbb1fd892272`; §9.26 integrated blob `c04701d0358d43a3a3f1aed61e7cdd2a48305417`. [Complete proof](../reports/2026-11-08-punctured-bidisk-hartogs-maximum.md) · [precise coverage](../coverage/2026-11-08-ch9-ch16-structural-and-sharpness.md).

**Unresolved/previous:** No old confirmed error, proof gap, candidate, external dependency, genuine duplication or verified repair has been reclassified by this local sharpness proof. All explicitly excluded approximation/regularization, Bergman/L2/OT/multiscale/positivity-loss items remain **deferred-by-user**, not resolved or certified.
