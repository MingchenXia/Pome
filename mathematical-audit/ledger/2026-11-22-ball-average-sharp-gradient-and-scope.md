# 2026-11-22 — classical ball-average gradient and dependency classification

## POME-CLASSICAL-BALL-AVERAGE-SHARP-GRADIENT-001

- **Severity/status:** low / **verified conditional deduction**; the integrated Theorem 3.3.4 remains valid, and no false theorem is alleged.
- **Main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Precise anchor:** docs/sections/classical-harmonic-analysis/index.html, blob 75e982788e627af602981823a82863cbd36ee712, physical lines 41–78, especially (3.3.5) at 42–44. Source classical-potential-theory:3425B8A6, permanent F549D908E93A; equation source classical-potential-theory:4E47B4BE, permanent 6CEBA4319BDE.
- **Hypotheses:** \(d\ge2\), \(r>0\), \(x\in\Omega_r\), real continuous \(f\) near \(\overline{B(x,r)}\).
- **Assertion:** \(|\nabla A_rf(x)|\le [v_{d-1}/(v_dr)]\operatorname{osc}_{\partial B(x,r)}f\), with the best possible constant even for globally smooth \(0<f<1\).
- **Proof/counterexample:** center the boundary integrand at \((\max f+\min f)/2\), use \(\int_S|e\cdot\theta|\,dS=2v_{d-1}\), and approach equality with \(f_\varepsilon(z)=(1+\tanh(z_1/\varepsilon))/2\). The complete calculation and sharpness limit are in [the dated report](../reports/2026-11-22-classical-ball-averages-green-potentials-and-trace-rotation.md).
- **Proposed correction:** none required. May add a separate corollary after Theorem 3.3.4; **audit only**, no registry, body, tags or canonicalization edit.
- **Affected dependents:** quantitative average-gradient applications in classical harmonic estimates; no invalidated existing downstream statement and no claim of transitive proof verification.

## Non-finding classification

Entire current §§3.3 and 3.5 received new direct reading; §20.2 selected 20.2.4, 20.2.21–27 only. The latter relies conditionally on §5.18.9/§16.9/§18.1 approximation and metric properties; these **must not** be promoted to verified chains from this audit. No newly confirmed error, proof gap or duplication. All specifically excluded Demailly regularization and Bergman/L²/OT/multiscale/positivity-loss work remains **deferred-by-user**, not resolved or certified.
