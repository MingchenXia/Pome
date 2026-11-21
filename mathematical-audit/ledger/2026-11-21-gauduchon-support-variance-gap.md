# POME-GAUDUCHON-SUPPORT-VARIANCE-QUADRATIC-GAP-001

**Date:** 2026-11-21. **Status:** verified conditional deduction. **Severity:** low. **Not** a false theorem, proof-gap repair, or independent certification of all upstream inputs.

Main `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Integrated §12.8 Theorem 12.8.2, source `non-kahler-pluripotential-theory:3606F8FD`, permanent `E9E119AAA269`, `docs/sections/a-gauduchon-variational-volume--supporting-probabilities-represented-by-maximizing-currents/index.html`, blob `ed1ad2bf6220cd086a44d7ee92ca7779666288d9`. The fixed-density determinant-measure continuity at §12.8.1 has source `E1B004B5`, permanent `47843166E777`. Related open uniqueness question: §24.7.1, source `68ABC3B8`, permanent `7C0A1CE5EC77`, `docs/sections/problems-in-hermitian-pluripotential-theory--weak-gauduchon-adjoints/index.html`, blob `e9f7c4bcab38a796064574591d87fdbd9be58331`.

For a compact Hermitian (n\ge2) background, continuous (F,h), and a maximizing current (T\in\mathscr M(F)), set (
u=Gamma_F(T)/M(F)), (R=\operatorname{osc}_X(h)). Then
[
B_0(F+t h)\le B_0(F)-t\int h\,\mathrm d
u-
\frac{t^2}{2n}e^{-|t|R/n}\operatorname{Var}_{\nu}(h),\quad t\in\mathbb R.
]
Proof: keep (T) fixed in (M(F+t h)), take the logarithmic moment generating function, and use (K''(s)=n^{-2}\operatorname{Var}_{\nu_s}(h)\ge n^{-2}e^{-|s|R/n}\operatorname{Var}_{\nu}(h)). Integrate the curvature estimate from (0) to (t). [Complete proof and limitations](../reports/2026-11-21-gauduchon-support-variance-gap-and-weak-adjoints.md).

**Proposed correction:** optional quantitative corollary after Jensen's inequality in §12.8.2, not an alteration of an existing theorem. **Affected dependents:** §11.34 slope/stability analysis and the open §24.7.1 weak-adjoint uniqueness question, which remains open. Prior varying-density net stability `POME-GAUDUCHON-DUAL-MAXIMIZER-VARYING-DENSITY-NETS-001` and earlier energy defects are not new findings here. All specified regularization programmes remain **deferred-by-user**.
