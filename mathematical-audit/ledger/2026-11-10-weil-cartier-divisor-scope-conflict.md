# Classified finding — POME-WEIL-CARTIER-DIVISOR-SCOPE-001

- Date: 2026-11-10.
- Reviewed main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- Severity: **medium**.
- Status: **confirmed error (unqualified claim under reduced-complex-space scope)**. If an unstated manifold convention was intended, the mathematically necessary correction is an explicit smoothness/Cartier hypothesis; not a refutation of the manifold theorem.
- Fault: Proposition **20.7.3**, `docs/sections/meromorphic-sections-and-divisor-classes/index.html`, blob `d0c40d1e3f6f515eb13169ed1cd3fb447ca161c8`, lines **17, 25–27**, source tag `00A05C89`, permanent tag `ACC6D09EDDD9`.
- Conflicting internal evidence: §20.6.2/4/5, `docs/sections/analytic-cycles-and-cartier-cycles/index.html`, blob `d4817ac64b1365bd967d42cd474fec169f992e28`, lines **8, 29–41, 47–74**, source tags `BE0C86A8`, `BD1D45B4`, `E054C396`, permanent tags `BE0C86A8DD65`, `AA96C35C8290`, `0C462992AB3A`. Global convention §1.1 line 11 permits reduced singular complex spaces.
- Counterexample: the normal quadric `x1*x2+x3*x4=0`, Weil prime `A=(x1=x3=0)`, is explicitly proven non-Cartier in §20.6.5; if `O(A)` were a line bundle with meromorphic section having divisor `A`, its coefficient in a local frame would make `A` Cartier. Direct rank-one parametrization/scaling obstruction given in [report](../reports/2026-11-10-weil-cartier-divisor-scope-conflict.md).
- Correction proposed, **not applied**: restrict ambient `X` to a **complex manifold** for the full proposition; or on reduced/singular spaces restrict divisor-to-line-bundle claims and `M*/O*` quotient to **Cartier** divisors. Do not conflate a rank-one reflexive Weil divisor sheaf with a line bundle.
- Affected dependents / still open: §20.8 and §9 singular-space uses of divisor line bundles require individual hypothesis checks. Poincaré–Lelong on manifolds unaffected. No whole-section certification.
- Distinct from `POME-DIVISOR-CHERN-NONPRINCIPAL-001`, which concerns `c_1` versus principal divisors on a smooth elliptic curve and was not a singular-space claim.
- User-excluded analytic-regularization programme stays **deferred-by-user**.
