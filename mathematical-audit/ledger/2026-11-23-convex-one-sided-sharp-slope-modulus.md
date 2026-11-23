# POME-CONVEX-ONE-SIDED-SLOPE-QUADRATIC-MODULUS-001

**Date:** 2026-11-23. **Severity:** low. **Status:** verified conditional deduction (not a confirmed error or proof gap). **Main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

**Statement reviewed:** sgpt:F7AADC82, permanent tag 66B643EAC79A, §21.11.63, **docs/sections/convex-functions-and-convex-bodies/index.html**, blob 2a123a863642a5a75caa173f0f73aff439a02ea4, physical lines 865–925. Original convex derivative convergence statement is correct and needs no repair.

**New quantitative deduction.** For \(|t|\le\rho\), assume a convex \(f\) differentiable at zero, \(g(t)\le g(0)+g'(0)t+(L/2)t^2\), \(f(t)\le g(t)+\delta\), and \(f(0)\ge g(0)-\eta\), with \(\delta,\eta,L\ge0\). Then for each \(0<h\le\rho\),
\[
|f'(0)-g'(0)|\le Lh/2+(\delta+\eta)/h.
\]
When \(L>0\) and \(\eta+\delta\le L\rho^2/2\), the sharp optimized bound is \(\sqrt{2L(\eta+\delta)}\). Proof: use the supporting affine line of \(f\) and test at \(t=\operatorname{sgn}(f'(0)-g'(0))h\). The model \(g(t)=Lt^2/2\), \(f(t)=at\), \(\delta=a^2/(2L)\), \(\eta=0\) makes equality and proves both the constant and exponent sharp.

**Caveat:** §21.11.63 has only pointwise limsup hypotheses, which yield qualitative convergence but *no uniform finite-scale rate*. This deduction imposes strictly stronger uniform control. **Proposed change:** optional separate remark via a reviewable patch; no production edit. **Potential dependents, not certified:** variational derivative controls in §§11.34–11.38, 17.16. **Upstream:** elementary convex supporting-line inequality only, with no external theorem or excluded approximation programme. **Complete proof and coverage:** [report](../reports/2026-11-23-quantitative-convex-slope-and-affine-residual-rotation.md) and [scope](../coverage/2026-11-23-convex-functions-and-affine-residuals.md).
