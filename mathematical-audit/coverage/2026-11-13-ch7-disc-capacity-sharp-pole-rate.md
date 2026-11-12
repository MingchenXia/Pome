# Exact selected coverage — 2026-11-13 — Chapter 7, §7.4

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (fresh read), Chapter 7 actual ToC 33 numbered sections, full project 25 chapters / 747 numbered sections. **Only the following specified passage was newly analyzed mathematically; not a full-section certification.**

| Section and page | Stable source/permanent labels | Main integrated physical lines | What was checked | Status |
| --- | --- | --- | --- | --- |
| §7.4, `docs/sections/bedford-taylor-products-and-local-capacity--weighted-estimates-and-monge-ampere-capacity/index.html`, blob `801a6ce8d25a6db19202cbc295937a135a9a208e` | Definition 7.4.2 `foundations-of-pluripotential-theory:AF32B1A0` / `E9E7C75396D2` | 85–94 | In dimension one, exact capacity of closed and open discs, both inner and outer capacities; checked (dd^c) normalization by radial distribution | **New exact conditional deduction** |
| Same | Proposition 7.4.3 `:DE1E4FA5` / `97EFDB6FDEE3` | 97–139 | Monotonicity and outer-capacity definition used to pass from closed to open discs and back; only these elementary steps, not all clauses | **Context only** |
| Same | Proposition 7.4.4 `:554B46C3` / `815E5BBFC34A` | 143–165 | Explicit (V=\log|z|^2) gives (\operatorname{Cap}^{*}_{D_1}(K\cap\{V<-s\})=1/s) for all sufficiently large (s); verifies sharpness of the printed (s^{-1}) exponent | **New exact conditional deduction; original proposition not refuted** |
| Same | Theorem 7.4.1 `:93A06A12` / `7C68264563C0` | 9–80 | Located the weighted CLN input invoked by the printed proof; no new verification of its whole analytic dependency chain | **Conditional internal dependency** |

Finding: `POME-BT-DISC-CAPACITY-SHARP-001`, severity low, status **verified conditional deduction**. [Full English report](../reports/2026-11-13-bt-disc-capacity-sharp-pole-rate.md) and [classified ledger](../ledger/2026-11-13-bt-disc-capacity-sharp-pole-rate.md).

**Credit reconciliation:** §7.4 was already a partially visited section in the durable 747-row SECTION_MATRIX; newly first-visited numbered sections **0**, fully certified numbered sections **0**. Chapter 7's remaining 32 sections are not implied verified by this entry. Existing findings (including unrelated Chapter 4 Green-energy disc capacity and historical conditional CLN checks) are not repeated or reclassified. Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss programme remains **deferred-by-user**; no proof reopening. Audit Markdown only; no main, source, canonical registry, tags, tests, CI, build or publication changes.
