# Finding ledger — 2026-11-10 — macroscopic point-jet moment truncation

| ID | Severity | Status | Main revision | First proof-level coverage | Printed assertion | Resolution / remaining dependencies |
| --- | --- | --- | --- | --- | --- | --- |
| \`POME-ANISOTROPIC-JETS-MACROSCOPIC-MOMENT-CUTOFF-001\` | low | **verified conditional deduction** | \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` | §18.44, first selected proof-level visit | Theorem 18.44.2 **correct** in its stated regime \(k_m=o(m)\); the new proportional-order case is not asserted by it | Proved \(m^{-q}B_m\nu_Y\to\mathbf1_{\{\sum H_j\ge\kappa\}}\theta^q/q!\) in total variation for \(k_m/m\to\kappa\in(0,\sum d_j)\), the positive box-slice volume/inclusion-exclusion formula for \(N_m/m^q\), and the interior fixed-radius Gaussian boundary layer. Relies on the internally printed one-factor/full-kernel interior saddle asymptotic, not independently certified throughout §18.42. No complete proof-chain certification. |

**Pinned reading edition:** \`docs/sections/partial-kernels-and-quotient-equilibrium--anisotropic-point-jets-and-isolated-poles-on-fibrations/index.html\`, blob \`1eefb2e68f8091fcd531535ed38b9003774a2f95\`. Theorem 18.44.2 source \`non-kahler-pluripotential-theory:BC433784\`, permanent \`7840E247F9D5\`, physical lines 47–115; Equation 18.44.5 source \`:5CD68BC7\`, permanent \`238CE4ED10CD\`, lines 74–80. Contextual Proposition 18.44.8 source \`:9383A964\`, permanent \`443408C4E29A\`, lines 132–161, and Theorem 18.44.11 source \`:6C7F82CE\`, permanent \`154EDD25787A\`, lines 182–213.

**Why this is new:** Previous §18.44 matrix row contained inventory only, with no selected proof check. This is an exact \(\kappa m\)-order *half-space cut* and conditional Gaussian transition away from the degenerate coordinate divisors. It does not duplicate §18.45's rational Newton **lower-dimensional shell** transport rate, §18.47's selected **three bands**, or §18.44.8's **sublinear** homogeneous-center scaling.

**Suggested source change (proposal only):** append a bounded-scope remark after Theorem 18.44.2. Do **not** transplant Theorem 18.44.11's quasi-PSH multiplier-ideal argument to \(k_m/m\not\to0\): small curvature loss is no longer ensured. No theorem found false, no source/body/registry/canonicalization edit performed.

**Still unresolved / deferred:** general non-product metric cases, full proof of §18.42 interior asymptotics in the global dependency chain; no changes to existing resolved or unresolved ledger categories. The Demailly approximation/regularization and its dedicated Bergman–L²–Ohsawa–Takegoshi, multiscale-atlas, positivity-loss completion programme stay \`deferred-by-user\`, not resolved.

[Full mathematical report](../reports/2026-11-10-anisotropic-jet-macroscopic-moment-cutoff.md) · [Exact coverage](../coverage/2026-11-10-ch18-anisotropic-jet-macroscopic-moment-cutoff.md).
