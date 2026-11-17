# POME-CLASS-GREEN-EQUILIBRIUM-QUADRATIC-GAP-001

**Date:** 2026-11-18. **Status:** verified conditional deduction. **Severity:** low. **Not a false theorem.**

**Main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Integrated file:** docs/sections/fine-topology-and-balayage/index.html, blob d4c8eed09391441b4b6d13e2fa402a60da70be0d.

**Anchors:** §4.2.11 (source foundations-of-pluripotential-theory:0EBEB570, permanent 2BC493B5F349, lines 196–200); §4.2.12 (source foundations-of-pluripotential-theory:F837B7D4, permanent AF6AC1F168D7, lines 259–283). Contextual §§4.1.17/4.1.26 (permanent 5B4ACD7E054D/E54414B74C32).

**Exact new deduction:** for compact \(K\Subset B\), \(m=C_B(K)>0\), normalized equilibrium \(e_K=\lambda_K/m\), and finite-Green-energy probability \(\tau\) supported on \(K\),
\[
I_B(\tau)-m^{-1}=I_B(\tau-e_K)
 =\|\nabla G_B(\tau-e_K)\|_2^2.
\]
For every signed finite-energy \(\eta\), the discrepancy in the pairing against \(\eta\) is at most the square root of this gap times \(I_B(\eta)^{1/2}\). Any arbitrary net of near-minimizing probabilities converges in the same energy norm without subnet arguments. Sphere-probability perturbations \((1+t x_1)e_K\) give equality in the dual estimate for the signed test \(x_1e_K\), establishing its coefficient and exponent.

**Dependency/status precision:** printed Propositions 4.2.11–12 are retained as correct conditional inputs. Quasi-everywhere equality of the equilibrium potential, polar-null property and positive-definite signed energy are not globally reproved. This is an additive stability statement, not a repair and not total-variation convergence. Proposed *audit-only* optional corollary immediately following §4.2.12; affects later compact reduction and balayage usage, not the source registry.

**Coverage:** §4.2 already partially reviewed: +0 first sections/+0 whole-section certificates; targeted contextual §4.1. 25 chapters/747 sections inventory remains. Excluded regularization/Bergman/L²/OT/multiscale/positivity-loss programme remains deferred-by-user. [Full proof](../reports/2026-11-18-classical-green-equilibrium-quadratic-energy-gap.md) · [coverage](../coverage/2026-11-18-ch4-green-equilibrium-quadratic-gap.md).
