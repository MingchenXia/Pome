# 2026-11-22 classification: generic domains of existence

## POME-HOLOMORPHY-GENERIC-DOMAIN-EXISTENCE-001

- **Severity / status:** low / **verified conditional deduction**; no printed theorem error, no full transitive proof-chain certification.
- **Reviewed production baseline:** main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- **Primary integrated file:** \`docs/sections/holomorphic-hulls-and-domains-of-holomorphy/index.html\`, blob \`f2bbaea02a3b85847acc503b83d0cf4dfa11e9d0\`, physical lines **16–38** (Proposition 9.13.1: source \`klimek-pluripotential-theory:5FBBEDD6\`, permanent \`36B688C7F361\`) and **51–89** (Theorem 9.13.2: source \`klimek-pluripotential-theory:18A483AD\`, permanent \`8FBCDB96A2E2\`), especially **84–88** (Montel/Baire/discrete interpolation).
- **Hypotheses:** holomorphically convex open \(\Omega\subset\mathbb C^n\); Fréchet compact-open topology on \(\mathcal O(\Omega)\); precise local-extension definition of §9.13.
- **Conclusion:** functions having *no* local analytic extension across any boundary piece form **exactly** a dense \(G_\delta\), and extendable functions form a meagre \(F_\sigma\). Proof via rational ball pairs, closed nowhere-dense bounded-extension sets, Montel, interpolation with divergent prescribed values, identity theorem, and Baire.
- **Missing upstream certification:** independent proof of the whole §9.13.1 interpolation dependency (printed and directly reviewed, but not certified transitively); no other missing step in the conditional deduction identified. Retain all attributions.
- **Proposed optional correction:** add a corollary to Theorem 9.13.2 recording the residual-set strengthening. Do not directly change mathematical body, registry, permanent tags or canonicalization.
- **Affected dependents:** §9.13.2 domain-of-existence applications; none requires a repair. Distinct from existing \`POME-HULL-JET-INTERP-001\`.
- **Evidence:** [full proof](../reports/2026-11-22-holomorphy-generic-domain-existence-and-hartogs-audit.md), [coverage](../coverage/2026-11-22-ch9-hartogs-hulls-domain-rotation.md). Demailly and all designated programmes remain **deferred-by-user**.
