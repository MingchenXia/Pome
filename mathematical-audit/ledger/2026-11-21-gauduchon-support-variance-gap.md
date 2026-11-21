# POME-GAUDUCHON-SUPPORT-VARIANCE-QUADRATIC-GAP-001

**Date:** 2026-11-21. **Severity:** low. **Status:** verified conditional deduction. Not a false printed theorem, duplicate of an earlier net stability finding, or repair of a proof gap.

Main SHA \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. Integrated §12.8.2, source \`non-kahler-pluripotential-theory:3606F8FD\`, permanent \`E9E119AAA269\`, \`docs/sections/a-gauduchon-variational-volume--supporting-probabilities-represented-by-maximizing-currents/index.html\`, blob \`ed1ad2bf6220cd086a44d7ee92ca7779666288d9\`. Related §24.7.1, source \`68ABC3B8\`, permanent \`7C0A1CE5EC77\`; blob \`e9f7c4bcab38a796064574591d87fdbd9be58331\`.

On a compact connected Hermitian \(n\ge2\) manifold with nonsingular reference \(0\), for continuous \(F,h\), an arbitrary maximizing \(T\) at \(F\), \(\nu=\Gamma_F(T)/M(F)\), and \(R=\operatorname{osc}_X h\),
\[
B_0(F+t h)\le B_0(F)-t\int_Xh\,\mathrm d\nu
-\frac{t^2}{2n}e^{-|t|R/n}\operatorname{Var}_\nu(h),
\quad t\in\mathbb R.
\]
Proof: retain \(T\) in the dual maximum, apply \(-n\log\) to the exponential moment of \(h\) under \(\nu\), and bound the tilted variance below by \(e^{-|s|R/n}\operatorname{Var}_\nu(h)\); integrate its second derivative. [Detailed proof](../reports/2026-11-21-gauduchon-support-variance-gap-and-weak-adjoints.md).

**Status boundaries:** this is an explicit quantitative upper support gap, not actual twice differentiability of \(B_0\), and does not solve the continuous-data weak-adjoint uniqueness conjecture of §24.7.1. **Proposed correction:** optional corollary to §12.8.2 without source edit. **Affected dependents:** §11.34 support slopes and §24.7 open question. Dependencies §12.7 duality/§11.34 supports remain conditional, not certified. Earlier \`POME-GAUDUCHON-DUAL-MAXIMIZER-VARYING-DENSITY-NETS-001\` and §17.4 energy-defect results were explicitly excluded from new-finding counts. Demailly approximation/regularization and its dedicated related programmes remain **deferred-by-user**.
