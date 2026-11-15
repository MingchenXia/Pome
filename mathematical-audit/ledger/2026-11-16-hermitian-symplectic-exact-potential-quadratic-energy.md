# 2026-11-16 — exact Hermitian-symplectic potential energy

- **POME-HERMSYMP-GLOBAL-QUADRATIC-POTENTIAL-001** — **low / verified conditional deduction**, not a false theorem and not a source repair. On a compact complex fourfold with smooth positive Hermitian-symplectic form \(\omega\), the canonical completion energy F has the **globally exact quadratic** law along \(\omega_u=\omega+dd^cu>0\):
  \[
  F(\omega_u)-F(\omega)=-\tfrac16\int_Xu\,dd^c(\omega^3)
  +\tfrac14\int_Xdd^c(\omega^2)\wedge du\wedge d^cu.
  \]
  Its potential Hessian \(H_{\omega_u}(dd^cv,dd^cw)=\frac12\int_Xdd^c(\omega^2)\wedge dv\wedge d^cw\) is independent of u, with exact polarized four-point defect. If \(dd^c(\omega^2)\ne0\), all positive potential basepoints have indefinite Hessian (infinite indices), so none is a local extremum; if it vanishes, F is potential-invariant. This verifies and refines, but does not refute, printed Proposition 11.2.17 and Theorem 11.2.19.
- **Anchors:** reviewed main b6933b772f41b45918f7e25ed1afbbb1fd892272; docs/sections/monge-ampere-energy-and-torsion/index.html blob fe1ca06167b8f5bc9868e9a9876397afad4e7ff5, lines 211–319; sources non-kahler-pluripotential-theory:F8C97F67/69225BEF; permanent tags AE6CE389C569/04BD04D6C676; Eq. 11.2.18 BAFFEA611460, Eq. 11.2.20 8B6CFC8EA37B.
- **Proposed patch:** optional new smooth-potential corollary following Thm 11.2.19; no production change. **Upstream:** compact Stokes and canonical-completion finite-dimensional projection (checked directly); the bounded-psh regularization passage in Cor. 11.2.21 stays **deferred-by-user**. No claim about full Aeppli Hessian indices or complete §11.2 verification.
- [Full proof](../reports/2026-11-16-hermitian-symplectic-exact-potential-quadratic-energy.md) · [exact coverage](../coverage/2026-11-16-ch11-exact-potential-energy.md). Prior §11.2 partly reviewed; +0 first visits/+0 complete certifications. No tests/build/CI/site changes.
