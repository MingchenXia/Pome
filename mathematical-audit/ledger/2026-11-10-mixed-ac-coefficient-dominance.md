# 2026-11-10 — mixed absolutely continuous wedge order

- **Finding ID:** \`POME-NPP-MIXED-AC-WEDGE-ORDER-001\`
- **Severity:** low
- **Status:** **verified conditional deduction** (not confirmed error, proof gap, verified repair or genuine duplication).
- **Main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- **Anchors:** §13.31.1 \`transcendental-positive-cones:6D2B462A\` / \`C7894CAD8593\`, \`docs/sections/absolutely-continuous-and-non-pluripolar-mass/index.html\` physical 8–16, 21–97; §7.3.7 \`foundations-of-pluripotential-theory:8B1F9B78\` / \`D87C13B3250A\`, \`docs/sections/bedford-taylor-products-and-local-capacity--decreasing-continuity-and-symmetry/index.html\` 133–229; §§13.2.1–.4 \`foundations-of-pluripotential-theory:D7E74DBE,CE1D6DA5,9D8E4DD8\` / \`6632853A40C9,D59675D9F6D8,D79952D7E272\`, \`docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html\` 9–63.
- **Hypotheses:** \`p<=n\`, closed positive \`(1,1)\`-currents \`T_i\`; locally finite *mixed* non-pluripolar wedge. No individual density smoothness or closedness of \`T_{i,ac}\`.
- **Proved conclusion:** \`0<= wedge_i(T_i)_ac <= <wedge_i T_i>\` as \`(p,p)\` currents. Smooth local mollifier Fatou + monotone BT; common non-pluripolar truncations and plurifine locality. Sharp strictness on products of unit circles, with top-degree mass exactly one and zero individual absolutely continuous parts.
- **Existing work comparison:** Previously recorded \`POME-FULLMASS-SINGULAR-AC-001\` is a separate compact full-mass and total-variation example; this result is the *mixed lower-degree* current inequality. No prior finding reclassified.
- **Dependents:** selected §§13.2/13.13 products and §13.32 numerical pairings only as possible applications, not independently checked.
- **Proposed patch:** optional corollary/remark after §13.31.1; source/body/registry not changed.
- **Upstream conditional:** §§7.3.7, 13.2.1–4, local differentiation in §13.31.1; no complete upstream certification.
- **User-deferred:** Demailly regularization, dedicated Bergman/L²/OT/multiscale/positivity-loss programme remains deferred-by-user, neither resolved nor re-opened.
- **Full proof:** [report](../reports/2026-11-10-mixed-ac-coefficient-dominance.md).
