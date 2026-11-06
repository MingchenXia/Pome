# Ledger increment — 2026-11-07 — countable polar sets and fine-topological sequences

**Stable ID:** POME-FINE-POLAR-COUNTABLE-NOSEQUENCES-001.
**Severity / status:** **low / verified conditional deduction**; the printed §4.2 propositions are correct, not refuted and not repaired.
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Primary source:** docs/sections/fine-topology-and-balayage/index.html, blob d4c8eed09391441b4b6d13e2fa402a60da70be0d, §4.2.5–6 physical lines 85–141. §4.2.5 source foundations-of-pluripotential-theory:01F6C408 / permanent 9E787ECDB068; §4.2.6 source foundations-of-pluripotential-theory:1BE55D99 / permanent 498B2C3E2413.
**Supporting source:** docs/sections/potentials-energy-and-capacity/index.html, blob 4962a7cd576a64cb47fa0955dcc80cf87c3da9d1, §4.1.11 lines 303–325; source foundations-of-pluripotential-theory:7F3FDDFF / permanent 64A94A9EE9E3.
**Hypotheses:** $\Omega\subset\mathbb R^d$ nonempty open, $d\ge2$, *classical fine topology*; rely conditionally on internal polar-union, fine-discreteness and no-isolated-point propositions.

**Complete new inference:** all countable sets are polar, hence fine closed/discrete. A convergent sequence lies in a countable fine-discrete set, and convergence then forces eventual equality to its limit. From this: nonseparability, failure of first countability everywhere (nested local-base neighborhoods would construct a nonstationary convergent sequence), nonsequentiality (every subset sequentially closed but not every subset closed), and lack of countable tightness at every point (the complement of a point accumulates finely at the point, no countable part does). The detailed six-part proof in the report contains all quantifiers.

**Affected dependence checks:** §4.2.22–23, §4.4 fine limits and §5.47 classical/plurifine comparison. No net claim or transfer to plurifine topology. **General proof status remains conditional** on the specified internal propositions; full §4.2 is not certified.

**Proposed correction:** optional explanatory remark after §4.2.8; no mathematical statement or permanent tag change needed and no production patch applied. **Resolved/unresolved/deferred state:** additive new conditional result only, with existing ledger findings unchanged. User-excluded Demailly regularization and Bergman/L²/OT/multiscale/positivity-loss remains **deferred-by-user**. [Proof](../reports/2026-11-07-classical-fine-topology-no-convergent-sequences.md) · [coverage](../coverage/2026-11-07-ch4-fine-topology-countability-obstructions.md).
