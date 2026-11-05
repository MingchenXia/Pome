# Classified finding — 2026-11-06

**ID:** POME-GAUD-RECOVERY-SMOOTH-DERIVATIVE-BOUNDARY-001  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Severity:** low  
**Status:** verified conditional deduction. **Neither a confirmed error nor a missing-proof repair.**

**Target and stable locator.** Integrated **docs/sections/a-gauduchon-variational-volume--recovering-a-positive-class-from-its-gauduchon-derivative/index.html**, blob **829d10abfa8f92c7c77fde66704adb6486ccdc93**, lines **10–27, 32–43**; Proposition **12.5.1**, source **non-kahler-pluripotential-theory:765CFEAC**, permanent **4BBB232A044C**.

**Hypotheses checked.** Compact connected complex manifold, n>=2, fixed smooth strictly positive **probability** mu, smooth strictly positive backgrounds, unit root volume, normalized Gauduchon minimizing forms, full derivative on smooth real (1,1) test forms.

**New result.** On the flat torus E^n with mu=omega_0^n/n!, take gamma_t=(t+sin^2(pi x_1))alpha_1+sum_{j>1}alpha_j and theta_t=(n!(t+sin^2(pi x_1)))^(-1/n)gamma_t. Direct wedge and AGM computations show dd^c gamma_t^(n-1)=0, theta_t^n=mu, lambda_mu(theta_t)=1, and gamma_t minimizes the defining quotient. The derivative representative Xi_t=gamma_t^(n-1)/D_mu(gamma_t) converges **smoothly** to a semipositive, degenerate limit while the normalized solution theta_t has C0 size asymptotic to t^(-1/n). Its L^q norms exhibit the exact threshold q=n/2; in n=2 the positive current masses diverge logarithmically. This is **boundary nonuniformity**, not an error in the printed interior recovery.

**Full argument and precise caveat:** [proof](../reports/2026-11-06-gauduchon-derivative-boundary-noncompactness.md). The quotient/minimizer portion is direct; identifying Xi_t with the actual derivative uses existing **Proposition 12.3.2**, source non-kahler-pluripotential-theory:6D3F0AB8, permanent **94AFD9E43DE0**, supporting file blob **d94e3fc055b0642a86495c27ad8f5af6f24f17d1**, lines **34–58**. Definition 12.2.1 and Theorem 12.2.3, source :876DF057, permanent **2DB664A6EFDF**, file blob **9ec67161d46b3ba20afa1b1c9a0c84f29322763e**, lines **7–21, 49–79**, were reviewed for conventions and dependency status only.

**Proposed correction:** no theorem correction. Optional boundary-stability qualification after Proposition 12.5.1: require uniform positivity to claim continuity of the inverse recovery in a family.

**Affected dependents:** §12.6 Hessian metric/completion and §§12.7–12.11 duality/degeneration discussions. None was independently certified. This is distinct from the earlier §12.4 conformal-background second-variation check and does not change its status.

**Coverage and deferrals:** new selected §12.5 model and proof-hypothesis check, not entire §12.5 or Chapter 12. Existing resolved/unresolved/candidate/duplicate classifications all retained. Demailly approximation/regularization and the Bergman, weighted-L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**, neither resolved nor reopened. Audit Markdown only; no source/registry/main/tag changes.
