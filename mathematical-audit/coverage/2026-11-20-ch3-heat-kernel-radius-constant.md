# 2026-11-20 — Chapter 3 heat-kernel audit coverage

**Main SHA:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; **branch:** \`review/mathematical-audit\`.

| Integrated reading-edition file | Current main blob | Directly checked |
|---|---|---|
| \`docs/sections/heat-kernels-on-compact-manifolds/index.html\` | \`c59a1b3fab9433f1aae95db99adb4821857b5d8d\` | Entire mathematical §3.10, physical lines **7–108**, including Nash/weighted heat argument in 3.10.1 (10–80), and growth/weighted pairing proof in 3.10.5 (85–105) |

**New POME-HEAT-MORREY-RADIUS-UNIFORMITY-001:** medium / confirmed error in the **metric-only radius uniformity** implied by line 7, not a refutation of the fixed-radius version of Lemma 3.10.5. Self-contained flat-torus counterexample and radius-explicit corrected estimate: [report](../reports/2026-11-20-heat-morrey-radius-constant.md), [ledger](../ledger/2026-11-20-heat-morrey-radius-constant.md).

**Delta:** +1 whole directly read section; +0 fully certified upstream theorem chains. The selected §3.10 checks of 2026-11-03 and 2026-11-06 remain historical; no new first-visit claim. The spectral/elliptic input and downstream uses of radius uniformity were not transitively verified. Deferred-by-user programmes unchanged; no tests/build/CI/production edits.
