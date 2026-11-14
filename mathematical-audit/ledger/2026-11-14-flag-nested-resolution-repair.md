# 2026-11-14 — flag resolution compatibility ledger

| Finding ID | Severity | Classification | Exact anchor | Resolution state |
| --- | --- | --- | --- | --- |
| POME-OKO-FLAG-AMBIENT-CENTERS-REPAIR-001 | medium | **verified repair proposed only** | Main b6933b772f41b45918f7e25ed1afbbb1fd892272; docs/sections/the-theory-of-okounkov-bodies--flags-and-valuations/index.html, blob 9190d2ae0d3e51ca0ca965000cb9b5b2ec965c85; Theorem 19.3.19 sgpt:44C3D868 / B00AB5301F7A, physical lines 319–331 | A *single* embedded resolution of V⊂W_i with all centers lifted into the ambient W_0 makes the earlier nested smooth strict transforms compatible. Original printed proof **unmodified**; conditional on allowed Hironaka embedded resolution and the normal-target codim-two isomorphism input. |
| POME-OKO-FLAG-NESTED-RESOLUTION-001 | medium | **candidate proof gap, proposed repair available** | Same theorem, particularly lines 323–331 | Existing candidate remains historically recorded; the newly verified *proposed* replacement above addresses the compatibility step. Do not label the printed proof already repaired, the theorem false, or the entire dependency chain certified. |

**Affected dependencies:** lifting existence used in Definition 19.3.20, Lemma 19.3.22, §19.4.7. No claim about the trace/valuation transformation in Proposition 19.3.14; no change to older two-blowup, trace-typing, reader-locator, or other findings.

**Deferred-by-user:** Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme, unchanged.
