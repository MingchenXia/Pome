# POME-NPP-CP1-TRUNCATION-SHELL-W1-001

**Date:** 2026-11-11. **Severity:** low. **Status:** verified conditional deduction (not a confirmed error or independent verification of the full upstream theory). **Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

**Pinned source:** docs/sections/non-pluripolar-products--capacity-convergence-and-loss-of-mass/index.html, blob d66813856cb813722806ab912afdfd4815d2da97; Example 13.7.6, original foundations-of-pluripotential-theory:D5678E03, permanent ACAEA8D8BE87, physical lines 138–140; conditional related statements Theorem 13.7.5, tag 67C4F7EC316E, lines 107–134 and Corollary 13.7.9, tag D73416504271, lines 176–200ff.

For the printed projective-line pole \(u=\log|z|^2-\log(1+|z|^2)\), \(u_k=\max(u,-k)\), \(\varepsilon=e^{-k}\), \(r_k=(e^k-1)^{-1/2}\), the exact current measure is
\[
\mu_k=\mathbf1_{|z|<r_k}\omega_{\rm FS}
 +(1-\varepsilon)\sigma_{r_k}.
\]
The interior and boundary masses are respectively \(\varepsilon\) and \(1-\varepsilon\), with no pole atom. For the standard chordal metric \(d_{\rm ch}(z,0)=|z|/\sqrt{1+|z|^2}\), exact \(W_1(\mu_k,\delta_0)=\varepsilon^{1/2}-\varepsilon^{3/2}/3\); exact \(\|\mu_k-\delta_0\|_{\rm TV}=2\), while the limiting non-pluripolar current vanishes. The smooth squared chordal distance has expectation \(\varepsilon-\varepsilon^2/2\).

New mass-hypothesis check: weights \(\chi_k=\mathbf1_{|z|\le r_k}\to0\) locally in capacity (disk capacity \(O(1/k)\)) but \(\int\chi_k\,d\mu_k=1\), whereas the limiting NPP weighted integral is zero. This does not contradict Corollary 13.7.9 because its **total-mass matching hypothesis fails**; it differs from the earlier POME-NPP-ROUGH-WEIGHT-CIRCLE-001 which tests the *limit-weight quasi-continuity* assumption under conserved mass.

**Proposed correction/addition:** optional precise charge/transport remark after Example 13.7.6; no change to original theorem, tag, attribution or source. **Dependents:** interpretation of Theorem 13.7.5, Corollary 13.7.9, projective-line quantitative benchmarks. **Status of prerequisites:** original Fubini–Study and NPP conventions used; upstream full proofs and all other section claims not certified. All excluded Demailly/Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss work remains **deferred-by-user**.

[Full source-anchored proof](../reports/2026-11-11-fs-truncated-pole-exact-shell-and-transport.md).
