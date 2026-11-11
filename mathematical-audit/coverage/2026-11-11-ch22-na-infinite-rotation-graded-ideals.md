# 2026-11-11 — Chapter 22, selected algebraic NA ideal lemma and its dependent use

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (unchanged from existing 25-chapter / 747-numbered-section ToC inventory).

| Exact location | Review performed | Level |
| --- | --- | --- |
| `docs/sections/non-archimedean-pluripotential-theory/index.html`, blob `8448d710690ebe1cc28040f9611d05c9d008a961`, Lemma 22.1.94 `sgpt:AB6FE74C` / permanent `76252E7717AC`, lines 1402–1414 | Original invariant-ideal argument crosschecked; **reused** already-recorded one-rotation Vandermonde and root-of-unity example as background; newly proved uniform finite-generator degree bound even with non-Noetherian `R`, and exhibited non-fg failure. | **New selected complete elementary argument**, not entire section or transitive NA theory. |
| Same page, equation 22.1.95 `sgpt:EC9FB89B` / permanent `6126C03E6587`, lines 1404–1406 | Checked the parenthesized terminal `I_m(t^m)` as a full ideal tail; supplied unambiguous graded `R`-module and `R[t]`-ideal formulas. | Not a confirmed source error. |
| Same page, Proposition 22.1.98 `sgpt:4D7EEB4A` / permanent `6A232EAE791C`, lines 1458–1475; equation 22.1.99 permanent `9186BF0A5F55`, lines 1468–1473 | Located finite-tail dependence of analytic coefficient sheaves. | **Dependency crosscheck only**; full proposition not certified. |
| Same page, Lemma 22.1.96 `sgpt:0D0A3D2C` / permanent `AF0C82DE24E9`, lines 1419–1425 | Identified GAGA input for analytic-to-algebraic ideal passage. | **External dependency only**; not independently verified. |

**Coverage delta:** §22.1 was already partly proof-reviewed: **0 new first-visited numbered sections / 0 mathematically certified complete sections**. Other §22.1 claims, including analytic and algebraic approximation and global-generation inputs, are **not** verified this session. The 25/747 inventory is preserved without resetting historical statuses.

**Novelty safeguard:** the single-rotation argument and root-of-unity obstruction were previously proved as `POME-NA-ONE-GENERATOR-GRADING-001` (2026-10-30); the graded tail for Noetherian bases and generic-fiber interpretation were also previously covered. Only the effective bound by maximal finite-generator degree over **possibly non-Noetherian** `R` and the explicit non-fg counterexample are counted as new in this report.

**Finding:** `POME-NA-FG-TAIL-NONNOETHERIAN-SHARPNESS-001`, severity low, **verified conditional deduction**. [Full report](../reports/2026-11-11-na-infinite-rotation-graded-ideal-finite-tail.md) · [ledger](../ledger/2026-11-11-na-infinite-rotation-graded-ideal-finite-tail.md).

**Deferred-by-user, unchanged:** Demailly approximation/regularization and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme. No tests, builds, CI, publication, source/body/main/tag/canonicalization changes.
