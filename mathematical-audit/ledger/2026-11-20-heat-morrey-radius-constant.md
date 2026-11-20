# 2026-11-20 — Heat kernel growth-radius ledger

**POME-HEAT-MORREY-RADIUS-UNIFORMITY-001: medium / confirmed error in metric-only uniformity; verified repair with \(r_0\)-dependence.**

- **Baseline:** main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; direct §3.10 integrated file \`docs/sections/heat-kernels-on-compact-manifolds/index.html\`, blob \`c59a1b3fab9433f1aae95db99adb4821857b5d8d\`.
- **Precise anchor:** line 7 claims heat constants depend on fixed metrics; Lemma 3.10.5 lines 85–105, source \`transcendental-positive-cones:DD00B1CA\`, permanent \`56A174D59425\`. Lemma 3.10.1 at 10–80 is the conditional Gaussian input, source \`transcendental-positive-cones:327DDB8B\` / permanent \`126365F8EBD6\`.
- **Counterexample:** on the fixed flat three-torus take \(\rho_\delta=1_{B_\delta}dV/\operatorname{vol}(B_\delta)\), \(r_{0,\delta}=\delta^2\), \(A_\delta=\delta\), \(t_\delta=\delta^2\). The ball-growth hypothesis is satisfied for every center, whereas \(t_\delta h_{t_\delta}\rho_\delta(0)\ge c\delta^{-1}\), contradicting a metric-only bound by \(C(1+\delta)\).
- **Correction:** \(\|h_t\rho\|_\infty\le C_g t^{-1}(A+(1+\min\{r_0,1\}^{2-m})\rho(X))\), or permit \(C=C(g,r_0)\). The fixed-\(r_0\) inequality and the separate fixed-\(F\in L^1\) vanishing statement remain valid.
- **Dependents / follow-up:** locate later uses that require constants uniform under \(r_{0,\alpha}\to0\); no assertion that any such downstream theorem is false. Keep source attribution and permanent tags.
- **Earlier results retained:** \`POME-HEAT-FROSTMAN-CRITICAL-QUANTIFIERS-001\` (which already correctly uses \(C_{g,r_0,s}\)) and \`POME-HEAT-CODIM2-LOGARITHMIC-L1-ENDPOINT-001\` concern different limits and are **not** new findings here.

[Complete calculation and proof](../reports/2026-11-20-heat-morrey-radius-constant.md) · [exact scope](../coverage/2026-11-20-ch3-heat-kernel-radius-constant.md).

**Classification:** false metric-only parameter-uniform claim, **not** false fixed-\(r_0\) heat bound. +1 complete direct section, +0 full upstream chains. Excluded Demailly-related programmes stay **deferred-by-user**. No source/main/site edits or CI.
