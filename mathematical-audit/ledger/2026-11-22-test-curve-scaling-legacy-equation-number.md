# POME-TESTCURVE-SCALING-LEGACY-EQNUM-001

- **Date:** 2026-11-22
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`
- **Severity/status:** **low / confirmed error (integrated reader equation-number presentation)**. Mathematical statement and proof remain valid.
- **Integrated path:** `docs/sections/test-curves--operations-on-test-curves/index.html`, main blob `3da617be8f58713f764d49ba22f49b803149a5e8`, lines **763–773**.
- **Stable source/reader anchor:** Proposition **17.15.34**, source `sgpt:4C06B8D5` (`data-tag=4C06B8D5`), permanent tag **148305D820BC**.
- **Observation:** inside a `numbered-equation` HTML node, the correct identity `(λΓ)_{-∞}=λΓ_{-∞}` has the unlinked, untagged source-style label `9.92`. Other equations in this reader section carry generated tagged labels `17.15.*`. The literal legacy coordinate violates `AGENTS.md`'s reader-numbering rule.
- **Proof of classification:** for `λ>0`, `(λΓ)_τ=λΓ_{τ/λ}`; passage to the `-∞` endpoint gives the displayed identity. There is no mathematical counterexample or missing proof here.
- **Proposed correction:** generate/link the correct current-section equation number with an approved stable tag, or leave the identity explicitly unnumbered if no equation tag is assigned. Do not invent a permanent tag or alter the proposition's stable anchor. Changes to the production renderer/registry must be separately reviewed; **none applied**.
- **Affected dependents:** reader equation citation/navigation and normalization only, not mathematical theorems.
- **Reproducible inspection:** compare the actual raw HTML lines **768–771** against neighboring tagged equation spans. Text inspected; no build or automated test executed.
- **Status of underlying dependencies:** none newly certified; excluded regularization/Bergman/L²/OT/multiscale/positivity-loss programmes continue **deferred-by-user**.

[Complete dated review](../reports/2026-11-22-test-curve-operations-legacy-equation-and-toric-base-locus.md).
