# Classified audit findings — 2026-11-07 (new analytic-density metric checks)

Reviewed production main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

| Stable finding ID | Severity | Status | Pinpoint |
| --- | --- | --- | --- |
| \`POME-MA-ANALYTIC-FLAT-NULL-JETS-001\` | low | **verified conditional deduction** | §14.29.1/.6–10/.13/.15–16, integrated main \`docs/sections/uniqueness-for-degenerate-equations--a-real-analytic-density/index.html\` blob \`2f00a81edc49855971bb3a6d774603ee5bbf40db\`, lines 11–20, 56–105, 143–165, 172–206; §14.26.2 source rank-one formulas |
| \`POME-MA-ANALYTIC-ALIGN-ALIAS-001\` | low | **genuine duplication** (one rendered formula, not a duplicate theorem); **candidate** browser rendering failure | §14.29 physical line 66 source \`non-kahler-pluripotential-theory:EDC080E0\` / permanent \`14762A8A84D0\`, repeated line 107 source \`:2A55FD4B\` / permanent \`7FEE08922F33\` |

**New mathematical result:** in Theorem 14.29.1's explicit degenerate solutions, the smallest generalized eigenvalue of either solution metric relative to the fixed Fubini–Study background is comparable to the **square** of the distance from the two disjoint real analytic hypersurfaces. Thus the inverse metric belongs locally to \`L^s\` exactly for \`0<s<1/2\`; it is critical weak \`L^{1/2}\`, not strong \`L^{1/2}\`. The solution forms have **identical infinite-order jets** on the zero strata yet differ on the intervening band. The complete endpoint rationalization, proof of the integrability threshold, source tags, and scope are in [the mathematical report](../reports/2026-11-07-real-analytic-degenerate-ma-flat-jets.md).

**Canonicalization note:** the second standalone equation contains the same displayed algebra as the labeled second row of (14.29.6)–(14.29.7); do **not** delete the independent source label or permanent tag. Propose a future display-only patch retaining both anchors. Nested math-environment rendering is not browser-tested.

**Affected dependents:** precise regularity context of §14.21.13, §14.29.15–16; any use of inverse-ellipticity integrability. No false theorem or fully verified global theorem; the global background's construction remains conditional. **0 first visits; 0 fully certified sections**. Prior classified findings untouched. Owner-excluded Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss stays **deferred-by-user**, not resolved.
