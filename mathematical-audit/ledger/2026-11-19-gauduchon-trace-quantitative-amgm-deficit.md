# Classified finding — 2026-11-19 Gauduchon trace

| Finding ID | Severity | Status | Original theorem status | Direct anchors | Proposed action |
| --- | --- | --- | --- | --- | --- |
| `POME-GAUDUCHON-TRACE-AMGM-SQRT-DEFICIT-001` | low | **verified conditional deduction** | Proposition 11.5.4 and Equation 11.5.6 **not refuted** | Main `b6933b772f41b45918f7e25ed1afbbb1fd892272`; `docs/sections/gauduchon-metrics-and-linear-mass--conservation-of-the-trace-mass/index.html` lines 57–75, source `non-kahler-pluripotential-theory:C78BBFF1` / permanent `BFC1330527CA`, equation `671B7CA8` / permanent `1F99A7154650`, global equation `D615B576` / permanent `B78F87EF7411` | Optionally add the proven sharp anisotropy remainder and equality cases through a separate reviewed production PR; **no production change now**. |

**Proof location:** [full new theorem and direct review](../reports/2026-11-19-gauduchon-trace-quantitative-amgm-deficit.md). For eigenvalues `lambda_j>0`, `G=(prod lambda_j)^(1/n)`, the exact difference of AGM deficit and the scaled square-root error is `2 sqrt(G)(avg sqrt(lambda_j)-sqrt(G))>=0`. `diag(T,1,...,1)` proves coefficient `1/n` sharp as `T->infinity`; integration using the Gauduchon distributional trace identity gives the global deficit. Equality requires the solution form to be pointwise proportional to the Gauduchon metric; proportionality is **constant** only if the background is closed and the Gauduchon metric is Kähler (`n>=2`).

**Resolved/verified in this run:** the conditional deduction above, the printed trace conservation proof and arithmetic-geometric-mean computation as written (direct checks). This is not a formal/full dependency certification.

**New confirmed error / new standalone proof gap / new genuine duplicate:** none identified in §11.5 after its direct whole-section review. Do not manufacture a defect from an unchecked transitive dependency.

**Unresolved upstream obligations:** global Gauduchon existence theorem §11.4.2, general distributional pairing under the earlier project conventions, and the cited unbounded-density extension §13.14.12 were not transitively re-certified. The report's elementary algebra is independently given.

**Deferred-by-user (unchanged):** the Demailly approximation/regularization programme, its Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion dependencies remain explicitly **deferred**, not resolved or certified. No progress is claimed on them.

**Coverage:** Main integrated blob `34af83ff391b5e5590cd9cb10ca4cd2b3faff02c`, all §11.5 mathematical lines 5–82 directly reviewed; +1 direct whole-section review, +0 completely verified upstream chains, and no asserted increment to historical first visits (previously unreconciled). No tests/builds/CI/website or source-body changes.
