# POME-PERRON-ASYMMETRIC-TIME-SLOPE-001 — asymmetric nonclosed Perron time slopes

Date: 2026-11-23. Reviewed main SHA \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

**Status:** verified conditional deduction. **Severity:** low. **Not** a confirmed original-theorem error, repaired proof, or complete upstream proof-chain certification.

**Anchor:** \`docs/sections/perron-interpolation-and-the-geodesic-equation/index.html\`, main blob \`dc8dc381257360c94fe1c792499bb1ddf1bf5997\`, Theorem 17.16.7 lines 110–138, source \`non-kahler-pluripotential-theory:CADEDF46\`, permanent \`66E38862017F\`. Direct inputs: Lemma 5.41.1 (source \`909C5329\` / permanent \`ADD743D2224C\`, lines 11–18 in \`docs/sections/plurisubharmonic-functions-and-singularities--the-minimum-principle/index.html\`), and Proposition 17.16.6 (source \`071B00B3\`, permanent \`5D2A9C4885B8\`, §17.16 lines 79–102).

For compact connected complex \(X\), smooth possibly **nonclosed** real \((1,1)\) form \(\theta\), and ordinary-equivalent \(\theta\)-psh endpoints \(u_0,u_1\), define finite optimal global constants \(m=\sup\{a:u_0+a\le u_1\}\), \(M=\inf\{b:u_1\le u_0+b\}\). The Perron segment satisfies \(m(t-s)\le u_t^{\rm P}-u_s^{\rm P}\le M(t-s)\) for \(s<t\) outside common poles, equivalently globally as inequalities of extended-valued potentials. The constants are sharp on constant-translation endpoints and yield monotone interpolation if \(m\ge0\) or \(M\le0\). The proof uses the explicit affine **lower** competitors \(u_0+mt\), \(u_1-M(1-t)\), the **upper** convex chord, and secant-slope monotonicity. See [full proof and delimitations](../reports/2026-11-23-asymmetric-perron-slopes-and-kiselman-envelope-review.md).

**Deduplication:** the earlier \`POME-GEODESIC-TIME-LIPSCHITZ-INTERPOLATION-001\` already established **symmetric** time Lipschitz and affine endpoint perturbation stability for §17.7, including an energy consequence. Neither is claimed as new. Here the **oriented one-sided optimal constants** and the nonclosed Hermitian §17.16 setting are the additional conclusion.

**Dependents:** §§17.16–17.17 bounded-type Perron segments/rays; no finite-energy metric or weak geodesic regularity follows without further inputs. **Proposed action:** optional reviewable mathematical corollary after Theorem 17.16.7, retaining all original source labels/tags. The prior printed theorem remains valid.

**Unresolved/external boundaries:** local Kiselman from SGPT (§5.41.3) and closed-Kähler \(d_2\) completion/CAT(0) (§17.16.19) are not independently certified; Theorem 5.32.1 invoked in §5.40.3 and all other user-excluded analytic regularization/Bergman/L²/OT/multiscale/positivity-loss programmes are **deferred-by-user**, not certified. No original mathematical error was confirmed by the present calculation.
