# Coverage increment — 2026-11-16 — §§15.26 and 5.27 concentric shell interaction

Reviewed \`main\` **b6933b772f41b45918f7e25ed1afbbb1fd892272**, main §15.26 blob \`354dfdf5224fac8896103ec09aa5936351021914\`, main §5.27 blob \`ddb2ac8d9de27a22152872e07e5e787d138a790e\`. Actual ToC: **25 chapters / 747 numbered sections**.

| Section | Exact material newly reviewed | Scope / outcome |
|---|---|---|
| 15.26 | Equation 15.26.1 / tag \`938F2C76C18A\`, lines 10–23; Proposition 15.26.2 / tag \`8F3C95237950\`, lines 26–65, especially 36–64 | New exact all-concentric-shell nonlinear Bedford–Taylor masses and improved printed-\`a=1/2\` reference coefficient; new **Lipschitz**, non-\`C^1\` singular-shell \`a=1\` reference. Original statement remains correct. |
| 5.27 | Lemma 5.27.25 / tag \`3242D4BA1F13\`, around lines 518–527 and following radial Stokes proof | Precisely checked normalization, radial flux, and extension to stepwise-convex profiles; bounded BT continuity declared as an internal condition, not wholly certified. |
| 15.26 | Corollary 15.26.3 / \`AB5B44EC4BDD\` lines 69–80, Theorem 15.26.4 / \`6076D6F3256C\` lines 84–99 | Dependency-only; conditional extension to the new explicit shell probability, no existence proof certification. |

**Finding:** \`POME-SPHERE-NESTED-MASS-CRITICAL-LIPSCHITZ-001\` — low / verified conditional deduction. [Full proof](../reports/2026-11-16-concentric-sphere-mixed-mass-and-lipschitz-endpoint.md) · [ledger](../ledger/2026-11-16-concentric-shell-mass-lipschitz-endpoint.md).

**Coverage delta:** Both sections already partially visited: **0 newly first-visited numbered sections**; **0 whole-section / whole-chapter certifications**. Earlier Hölder ball mass and individual sphere reports are explicitly retained, not rebranded as progress.

**Excluded scope:** Demailly regularization and the dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss completion programme all **deferred-by-user**. No production edit, test suite, build, GitHub Actions CI, or website publication.
