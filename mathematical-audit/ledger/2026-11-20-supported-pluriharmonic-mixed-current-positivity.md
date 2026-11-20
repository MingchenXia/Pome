# 2026-11-20 — Supported mixed pluriharmonic current, positivity boundary

- **Finding:** `POME-PLURI-HYPERSURFACE-SIGNED-MIXED-001`
- **Severity / status:** low / **verified conditional deduction**, counterexample to *removing a hypothesis*, **not** a printed theorem error.
- **Current baseline:** `main` `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Anchor:** §11.22, `docs/sections/gauduchon-metrics-and-linear-mass--pluriharmonic-currents/index.html`, blob `046c12d159f8aaeff268c57d822253da11ed41ba`, Lemma 11.22.1 source `non-kahler-pluripotential-theory:9611A9E5`, permanent `D9A37BB4C36B`, physical lines 10–35 (especially matrix reduction 23–33).
- **Full calculation:** on `E×E`, `D={0}×E`, the real mixed current `iδ_0(z)(dz∧dbarw+dw∧dbarz)` is supported on `D`, order zero and `dd^c`-closed, but its mixed normal coefficients prevent representation as `j_*S` for any `S`. It is not positive; positive-semidefinite coefficient matrices are exactly what the printed proof uses.
- **Proposed action:** retain the printed positivity hypothesis; optionally add a sharpness note in a separately reviewable patch (not a source edit in this audit). No downstream printed application examined here drops positivity.
- **Other directly completed sections:** §11.24 (Fredholm continuous Hermitian operator, lines 7–69, blob `8fd933d027ecdba0c2df8efe7524e3984613857a`) and §11.25 (adjoint mass/capacity, lines 7–27, blob `48117e4e5901381d5ae692cfd29f2cf5f1325abc`). Source/permanent tags `2FF004A4`/`DEA6C8EFE702` and `A07C226C`/`3E5CF25D6E23`. No new printed errors; cited Kähler `dd^c` lemma, elliptic theory and capacity stability not fully transitively certified.
- **Documentation:** [full report](../reports/2026-11-20-supported-pluriharmonic-mixed-current-positivity.md) · [coverage](../coverage/2026-11-20-ch11-pluriharmonic-fredholm-adjoint.md).
- **Coverage delta:** +3 whole direct section readings, +0 complete upstream chains, **no first-ever-visit claim**. All user-excluded analytic programmes deferred-by-user. No builds, CI, main/source/tag/registry/site edits.
