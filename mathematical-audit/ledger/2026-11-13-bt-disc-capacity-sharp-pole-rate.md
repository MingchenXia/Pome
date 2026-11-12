# 2026-11-13 — Bedford–Taylor disc capacity and sharp logarithmic sublevels

| Field | Value |
| --- | --- |
| Stable ID | `POME-BT-DISC-CAPACITY-SHARP-001` |
| Severity | **low** |
| Status | **verified conditional deduction** |
| Printed result status | Definition 7.4.2 and Proposition 7.4.4 **not refuted** |
| Main SHA | `b6933b772f41b45918f7e25ed1afbbb1fd892272` |
| Exact integrated file | `docs/sections/bedford-taylor-products-and-local-capacity--weighted-estimates-and-monge-ampere-capacity/index.html` |
| Main blob | `801a6ce8d25a6db19202cbc295937a135a9a208e` |
| Source/permanent tags | Definition: `foundations-of-pluripotential-theory:AF32B1A0` / `E9E7C75396D2` (lines 85–94); Proposition: `:554B46C3` / `815E5BBFC34A` (143–165); context: `:DE1E4FA5` / `97EFDB6FDEE3` (97–139), `:93A06A12` / `7C68264563C0` (9–80) |
| Hypotheses tested | (D_R\subset\mathbf C) a Euclidean disc; (0<r<R); (operatorname{Cap}) with (dd^c=(i/2\pi)\partial\bar\partial) and competitors (0\le v\le1); (V=\log|z|^2) on (D_1); fixed nested compact discs (K\Subset\operatorname{Int}L\Subset D_1) |
| Mathematical conclusion | Closed/open radius-(r) disc capacities and outer capacities all equal (1/[2\log(R/r)]); for (V=\log|z|^2), outer capacity of ({V<-s}) is **exactly (1/s)** |
| Justification | Circular-mean/Riesz identity bounds arbitrary competitors; radial maximum produces uniform circle curvature with mass (1/[2\log(R/r)]); inner approximation by smaller closed discs treats the open disc correctly; open neighborhoods treat outer compact capacity. See full report |
| Proposed correction | Optional self-contained post-Proposition 7.4.4 sharpness example; no correction to printed theorem necessary |
| Affected dependents | §§7.5–7.6 quantitative uses of (O(s^{-1})), whose exponent cannot improve without additional hypotheses |
| Unresolved | Full general CLN/Bedford–Taylor chain not certified, no general exponent sharpness beyond the stated logarithmic example |
| Deferred-by-user | Demailly approximation and dedicated Bergman, L², OT, multiscale-atlas and positivity-loss programme **unchanged**, neither resolved nor reviewed |
| Coverage | Previously partly read §7.4; +0 first visits, +0 entire-section certifications; actual main ToC 25 chapters / 747 numbered sections |

**Proof:** [2026-11-13-bt-disc-capacity-sharp-pole-rate.md](../reports/2026-11-13-bt-disc-capacity-sharp-pole-rate.md).
