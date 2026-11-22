# 2026-11-22: local smooth Hessian-capacity filtration

**ID:** POME-HESSIAN-LOCAL-CAPACITY-FILTRATION-001  
**Severity/status:** **low / verified conditional deduction**, NOT a printed error, not a repaired proof and not a complete transitive-chain certification.  
**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

**Source:** \`docs/sections/complex-hessian-equations--local-capacities-and-decreasing-products/index.html\`, blob \`115d285f6b1f76d284463c396e7e87db2b9dbdc3\`, Definition 8.11.2 (source \`non-kahler-pluripotential-theory:016F1DC8\`, tag \`FA49D2074193\`, lines 48–61) and equation 8.11.3 (source \`non-kahler-pluripotential-theory:32422401\`, tag \`A08EAEC63C44\`, lines 64–71). Scope \`2≤m<n\` from §8.1 line 7.

**Hypotheses and conclusion:** For a fixed coordinate ball \`U\`, \`0≤q≤s≤m\` and compact \`K\Subset U\`, there exists \`C_{K,q,s}\` such that \`c_q(E)≤C c_s(E)\` on all Borel \`E⊂K\` and \`c_q^*(E)≤C c_s^*(E)\` on arbitrary \`E⊂K\`. This establishes a nested *null-set* hierarchy. No reverse comparison or whole-manifold constant is asserted.

**Proof:** Set all \`q\` unshifted cone factors in Eq. 8.11.3 equal to the same arbitrary normalized smooth competitor \`a\`; the LHS is \`q^q(dd^c a)^q ω^{n-q}\`, and the RHS is \`C Λ_s((qa+b-B)/L)\` for a fixed local strongly PSH \`b\` and uniform \`B,L\`. Integrate, take supremum over \`a\`, and use the zero-factor \`ω^n\` case for \`q=0\`. Intersect arbitrary outer open neighborhoods with a fixed relatively compact open neighborhood of \`K\` before taking infima. Full argument in [report](../reports/2026-11-22-hessian-capacity-filtration-and-green-pole-direct-audit.md).

**Proposed correction:** optional new conditional corollary only; preserve original statements, tags and attribution. **Affected dependents:** §§8.11.6, 8.11.10–14, and §8.12 quasicontinuous locality. **Remaining dependencies:** smooth Gårding inequality §8.2, smooth decreasing Hessian approximation §8.6, recursive-current construction §8.9. Do not infer their full proof certification. All excluded user-deferred Demailly-related work remains deferred-by-user.
