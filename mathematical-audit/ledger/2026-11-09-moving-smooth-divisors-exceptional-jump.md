# Finding POME-BDIV-EXCEPTIONAL-COEFFICIENT-JUMP-001

- **Status:** verified conditional deduction.
- **Severity:** low.
- **Main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Exact original:** `docs/sections/divisorial-currents-on-compact-modifications/index.html` blob `79d6e21f9d3784bf3761846f77f90ad075253644`, Proposition 20.4.22, `non-kahler-pluripotential-theory:B3489943` / `D7373D3639FA`, lines 437–464; Corollary 20.4.24 lines 469–480.
- **Direct upstream check:** `docs/sections/divisors-and-logarithmic-limits-on-analytic-cycles/index.html` blob `dae567406b2030e550664ca57b1fe77911d956d4`, Lemma 20.5.2, `demailly-complex-geometry:72B4BF94` / `551A781E3A1C`, lines 11–27.
- **Hypotheses and result:** `g:Bl_pℙ²→ℙ²`, smooth degree-`m` divisors `D_t={Z₁^m+t(Z₀^m+Z₂^m)=0}` avoiding `p` for `t≠0`, `D_t→mL`. The currents `g^*[D_t]` converge weakly to `m[\widetilde L]+m[E]` although `ν(g^*[D_t],E)=0` for each `t≠0` and `ν(g^*(m[L]),E)=m`. Every `m≥1` occurs.
- **Justification:** two explicit blowup chart equations and local `L¹` convergence of logs, plus fixed-class calculation. [Full proof](../reports/2026-11-09-moving-smooth-divisors-exceptional-jump.md).
- **Printed theorem status:** no error; **do not** mark 20.4.22 as repaired. Its weak topology does not contain coefficientwise continuity.
- **Proposed correction:** remark/example after 20.4.22 warning against using weak pullback continuity to pass individually to exceptional coefficients or strict transforms.
- **Potential dependents to inspect, not asserted erroneous:** §§20.1–20.2 and §20.4.26.
- **Coverage:** §20.4 selected new projective model; §20.5 local convergence proof used, not re-certified. Zero full sections certified. Prior ledger and deferred-by-user categories unchanged.
