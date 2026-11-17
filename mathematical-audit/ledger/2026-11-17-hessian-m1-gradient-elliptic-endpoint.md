# Classified finding — 2026-11-17 — scalar Hessian gradient endpoint

**Finding ID:** \`POME-HESS-M1-GRADIENT-ELLIPTIC-ENDPOINT-001\`  
**Severity:** low  
**Status:** verified conditional deduction (**not** a false printed theorem; **not** a source repair already applied).  
**Production main SHA:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`  
**Location:** \`docs/sections/complex-hessian-equations--liouville-and-gradient-estimates/index.html\`, blob \`74cda06ad4bf75ab5fcba6e841c9ad4aa9424981\`, §8.3, Proposition 8.3.3, source \`non-kahler-pluripotential-theory:hessian:hessian-trace-to-gradient\` / source tag \`A456C079\`, permanent tag \`B863BB49A505\`, lines 109–117, 122–129, 131–151.

**New deduction:** The proposition's gradient conclusion also holds for \(m=1\), \(n\ge1\), with no auxiliary feedback trace bound: \(\Gamma_1\) and the uniform normalized \(m=1\) Hessian density bound imply \(0<\operatorname{tr}_\omega\theta_u\le nB\), hence a fixed uniform bound on \(\Delta_\omega u\), and fixed-coefficient elliptic \(W^{2,p}\) plus Morrey gives \(C^1\).

**Sharpness / hypothetical weakening only:** For \(n\ge2\) on the flat torus, \(\Delta_{\mathbb R}u_\epsilon=\epsilon^{-2}\rho(x/\epsilon)-\epsilon^{2n-2}\) has uniformly bounded solutions, \(\sup|\partial u_\epsilon|\asymp\epsilon^{-1}\), trace-positive \(\omega+dd^cu_\epsilon\), and even \(\operatorname{tr}_\omega\theta_{u_\epsilon}\le A(1+R_\epsilon^2)\) for fixed \(A\). Their first-Hessian densities are unbounded, so this does **not** contradict Proposition 8.3.3 or its endpoint extension with fixed \(B\).

**Proposed correction / dependents:** Optional separate \(m=1\) endpoint paragraph after §8.3.3; do not reuse the false \(m=1\) eigenvalue bound from §8.2.5 (old error \`POME-HESS-CONE-M1-TRACE-BOUND-FALSE-001\`). Applicable to scalar first-Hessian bounds; §§8.4–8.5 unchanged and not newly certified. Standard fixed-coefficient elliptic \(W^{2,p}\) estimates are conditionally invoked, rather than fully recertified.

[Full proof and sharpness family](../reports/2026-11-17-hessian-m1-gradient-elliptic-endpoint.md) · [Coverage](../coverage/2026-11-17-ch8-m1-gradient-elliptic-endpoint.md). Excluded Demailly/dedicated Bergman/\(L^2\)/OT/multiscale/positivity-loss work remains **deferred-by-user**.
