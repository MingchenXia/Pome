# Finding ledger — 2026-11-13 — finite convex envelope without compact domains

| Stable ID | Severity | Classification | Original result | Affected dependencies | Status / proposed action |
| --- | --- | --- | --- | --- | --- |
| \`POME-CONVEX-NONCOMPACT-HULL-NONATTAIN-001\` | low | **verified conditional deduction** (sharp scope counterexample, **not a false printed theorem**) | Lemma 21.6.1; \`foundations-of-pluripotential-theory:30FFD831\` / \`FCDAD9CEC8CE\`, statement lines 10–12, proof lines 14–30 | Proposition 21.3.3(2) \`E93FCB56/53A9D470F1AC\`; Theorem 21.3.2 \`DD2DB654/011FA81B0000\` | **Verified**: without common compact effective domains, even two nonnegative closed proper convex functions can have a non-lsc convex envelope with no attained finite barycentric infimum at any nonzero point of its effective domain. Keep printed compactness; no source edit proposed. |

**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. Exact integrated file and blob: \`docs/sections/convex-analysis-and-toric-potentials--compact-convex-envelopes-and-full-mass-limits/index.html\` / \`b3b4e34fff767a717df812a381f905589b257fb3\`. Distinct from the earlier §21.11 *decreasing family* / epigraph-closure counterexample and §21.6.2 Wasserstein finding. [Complete computation](../reports/2026-11-13-noncompact-convex-envelope-nonattainment.md) · [coverage](../coverage/2026-11-13-ch21-convex-noncompact-hull.md).

**Counts:** current main ToC 25/747; §21.6 already partly inspected; +0 first visits / +0 full section certifications. Entire excluded Demailly/regularization and dedicated Bergman/\(L^2\)/OT/multiscale/positivity-loss programme remains **deferred-by-user**. No changes to its ledger status.
