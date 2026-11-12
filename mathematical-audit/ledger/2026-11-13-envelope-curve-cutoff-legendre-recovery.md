# 2026-11-13 classified finding ledger — cutoff Legendre recovery

| Stable ID | Severity | Status | Reviewed production main | Primary source | Outcome |
| --- | --- | --- | --- | --- | --- |
| \`POME-ENVSYS-CUTOFF-LEGENDRE-RECOVERY-001\` | low | **verified conditional deduction** | \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` | §16.29.2–3 | Any normalized decreasing ideal-envelope curve has a nonempty common zero set equal to \(\{\Gamma_c=0\}\), its Legendre ray satisfies \(\sup_XU_t=ct\) for all \(t>0\), and \(U_t-ct\downarrow\Gamma_c\) pointwise. |

**Not a printed error or a repaired theorem.** Full proof: [dated report](../reports/2026-11-13-envelope-curve-cutoff-legendre-recovery.md). Pinned section file \`docs/sections/envelope-systems-over-hermitian-perturbations/index.html\` blob \`856e240bbc5c86058ff861873f11e87db021e1bd\`. Definition 16.29.2 original/permanent \`non-kahler-pluripotential-theory:DC46E61D\` / \`F0A985779829\` (physical lines 24–47); Proposition 16.29.3 \`:C6135113\` / \`160B15BF08FE\` (lines 51–66).

**Affected dependents / proposed correction:** The cutoff identity supplies a directly checkable normalization for the rays in §§16.29 and 17.17 and clarifies that no maximizer \(\tau<c\) exists in general. Optional expository note only; no production patch. The original proposition is correct, and no false theorem is alleged.

**Conditional prerequisites and status:** §18.4.2 ideal-envelope normalization, §17.17.5 ray PSH regularization, standard upper-envelope polar discrepancy and decreasing PSH limits. These upstream results are not certified by this finding. All owner-excluded regularization/Bergman/\(L^2\)/OT/multiscale/positivity-loss work retains **deferred-by-user**, neither solved nor re-reviewed.

**Coverage accounting:** selected §§16.29.2–3 plus statement-only §18.4.2; §16.29 was previously partly visited, so **0 new first-visited numbered sections; 0 complete numbered-section certifications; current ToC 25 chapters / 747 sections**. No tests/build/CI/site publication.
