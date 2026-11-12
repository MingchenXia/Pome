# Classified finding ledger — 2026-11-12 — §5.64

Production baseline: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
Report: [exact local ridge and equatorial global model](../reports/2026-11-12-null-kahler-ridge-equator-density.md).
Exact coverage: [§5.64 increment](../coverage/2026-11-12-ch5-null-kahler-ridge-equator.md).

| Stable ID | Status | Severity | Precise claim and source | Proposed action / dependents |
| --- | --- | --- | --- | --- |
| `POME-NULL-KAHLER-RIDGE-EQUATOR-DENSITY-001` | **verified conditional deduction** | **low** | Theorem 5.64.2, original `transcendental-positive-cones:FBD376B2`, permanent `E682ACE02BAF`, integrated main `docs/sections/null-supported-kahler-currents/index.html`, blob `009f58a180936636f2e5927b9272f87f2c93aa29`, physical lines 43–103 and 108. At a regular two-branch cap tie, exact `dd^c max(0,h)=(i/2π)δ(h)∂h∧∂̄h`; Euclidean trace density `(n-1)!|∇h|/(4π^n)` relative to `H^{2n-1}`. On `P^1` the global continuous potential `log max(1,|z|²)-log(1+|z|²)` represents normalized equatorial arclength; on `(P^1)^n` a sum yields a positive current with smooth-real-hypersurface null support and exact total trace mass `n!`. The general theorem remains correct. | No mathematical correction required; optionally add the exact example to a separate source-review PR. Do not globally assert two-branch regularity, or convert conditional local work to full-section certification. Affects the support/normalization reading of §5.64.2 and is consistent with §5.65.2. |

**Explicit boundary of scope:** The report does not revisit the 2026-10-26 Cantor-support-dimension deduction, nor certify Theorem 5.64.2's general local-chart construction. The Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss programmes remain **deferred-by-user**, neither resolved nor certified; in particular §5.64.3–4 were not audited.

**Counts:** +0 first-visited numbered sections, +0 fully mathematically certified sections; current project ToC 25 chapters / 747 numbered sections. No source, registry, permanent tag, main branch, build, CI or website modifications.
