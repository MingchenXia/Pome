# 2026-11-23 — Green-energy balayage and explicit Legendre-ray speed

Reviewed main SHA: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit branch: review/mathematical-audit. Detailed proofs and physical anchors: [full report](../reports/2026-11-23-fine-balayage-projection-and-legendre-ray.md).

## POME-BALAYAGE-ENERGY-NONEXPANSIVE-PROJECTION-001

**Status:** verified conditional deduction. **Severity:** low. **Printed theorem false?** No.

Input §§4.2.11, 4.2.16, 4.2.18 in docs/sections/fine-topology-and-balayage/index.html, main blob d4c8eed09391441b4b6d13e2fa402a60da70be0d, physical lines 196–250 and 380–450. Source labels foundations-of-pluripotential-theory:0EBEB570, :23EEEACB, :08AABB73; permanent tags 2BC493B5F349, F28E6D45483F, 0056FED1AF8C; orthogonality Eq. 4.2.17, tag 7DCA4DACFD19.

For compact A in a ball B and two finite-energy positive measures mu,nu, signed finite-energy differences satisfy exactly
\[
I_B(\mu-\nu)=I_B(\mu^A-\nu^A)+I_B((\mu-\mu^A)-(\nu-\nu^A)).
\]
Consequently I_B(mu^A-nu^A)<=I_B(mu-nu), with sharp coefficient one when A is nonpolar; zero map when A is polar. This is an algebraic idempotent energy-orthogonal projection for signed finite-energy measures, **not a Hilbert completeness assertion**. Complete proof in report. Proposed correction: optional corollary after §4.2.18. Affected dependents: Green-energy stability, sweeping approximations and capacity; no whole chain certified.

## POME-LEGENDRE-P1-RAY-UNIFORM-VELOCITY-001

**Status:** verified conditional deduction. **Severity:** low. **Printed theorem false?** No.

Input §17.17.11, docs/sections/test-curves-and-legendre-duality/index.html, main blob 704ed205a974fe18e2dc502b13ceaf382b4af4b3, lines 184–246. Source non-kahler-pluripotential-theory:42E4DFA8, permanent 377F0AD20B28; Eq. 17.17.12 source 1A6C8986, tag 9BA75154C113.

For U_t=log((1+e^t|z|^2)/(1+|z|^2)), its velocity partial_t U_t has exactly uniform [0,1] distribution with respect to omega+dd^c U_t. Hence all nonnegative moments are 1/(q+1), and E(U_t)=t/2 in the normalized Aubin–Mabuchi convention. Proof uses the normalized Fubini–Study radial measure and the change of variables p=rho/(1+rho); the energy identity follows by first variation. Proposed correction: optional quantitative note after the smooth projective-line example. Affected dependents: toric ray speed calculations only; general Legendre and Perron existence not certified.

Excluded Demailly/regularization/Bergman/L²/OT/multiscale/positivity-loss proof programs remain deferred-by-user, not resolved. No production edits or tests.
