# Ledger — 2026-11-11 — Hessian self-products versus Sobolev capacity

**ID:** POME-HESS-SINGLE-POTENTIAL-HIGHER-SOBOLEV-CAP-FAIL-001  
**Status:** low / **verified conditional deduction**; no printed error.  
**Main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

For one fixed bounded continuous strictly admissible \(u=a\chi\sum_{j=1}^m|x_j|\), the diagonal products \(\mathcal H_r=Q_r(u,\ldots,u)\wedge\omega_0^{m-r}\), \(2\le r\le m\), have exact positive mass \(r!(n-r)!a^r(2\pi)^{-r}\operatorname{Vol}_{2n-r}(E_r)\) on compact sets \(E_r\subset\{x_1=\cdots=x_r=0\}\) of **zero** first-order Sobolev capacity.

**Anchors:** `docs/sections/complex-hessian-equations--sobolev-capacity-and-two-hessian-factors/index.html`, blob `25f25433cb9b17de6715a5b05f8b3c15b95a18cd`: Lemma 8.10.2 source/permanent `non-kahler-pluripotential-theory:1DDAECA7/FFBF9CD42640` lines 58–96; Lemma 8.10.6 `:350D7B3A/2A6BE9847309` lines 185–207; Example 8.10.7 `:36B886BE/AEB4F2397BBF` lines 209–251.

**Comparison:** printed Example 8.10.7 uses two different potentials and degree two; this all-degree **single self-product** calculation is new. **Proposed correction:** optional remark, no source edit. **Affected:** §8.11 Hessian-capacity motivation and any invalid degree≥2 use of §8.10 first-trace bound. **Conditional input:** canonical-product identification Theorem 8.11.12, source/permanent `:B227378C/C044CD1C65C4`, not fully certified. **Deferred-by-user:** entire excluded Demailly regularization and Bergman/L2/OT/multiscale/positivity-loss programme, unchanged.

[Full anchored proof](../reports/2026-11-11-single-bounded-hessian-sobolev-capacity-all-degrees.md) · [coverage](../coverage/2026-11-11-ch8-single-hessian-sobolev-capacity.md).
