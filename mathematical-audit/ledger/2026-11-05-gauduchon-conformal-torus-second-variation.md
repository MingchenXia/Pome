# Classified audit finding — 2026-11-05

**ID:** POME-GAUD-CONFORMAL-TORUS-EXACT-VARIATION-001  
**Date:** 2026-11-05  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Severity:** low  
**Status:** verified conditional deduction (**not** confirmed error, proof gap, verified repair or full theorem certification).

**Primary target:** docs/sections/a-gauduchon-variational-volume--second-variation-on-background-classes/index.html, blob 4992f82c6e84918ead47a972eab7e3238a147655, physical lines 22–28, 33–75. Proposition 12.4.1: source non-kahler-pluripotential-theory:C55D0CC4 / permanent 67FDDBC10DBD; equation block source :86F8F24F / permanent E544AEC2FDDB; background-class form source :B96CF85C / permanent 6BCEC0329DE5.

**Hypotheses and finding:** On E^n with omega=sum i dz_j dbarz_j/2 and probability mu=omega^n/n!, the positive, usually nonclosed family theta_t=(1+t f(x_1))omega has an explicit smooth solution. For m=mean(f) and v=mean((f-m)^2), its precise Gauduchon root-volume is (n!)^(1/n)[(1+tm)/mean((1+tf)^(-(n-1)))]^(1/n). At t=0, lambda'/lambda=m; lambda''/lambda=-(n-1)v; -(log lambda)''=m^2+(n-1)v. The explicit solution has A_chi=diag(nm-(n-1)f,f,...,f), and the normalized adjoint-probability trace calculations reproduce both identities and both equality cases of Proposition 12.4.1.

**Mathematical proof and assumptions:** [Full exact ODE construction, normalization, differentiation, and n=2 cosine calculation](../reports/2026-11-05-gauduchon-conformal-torus-exact-second-variation.md). Identification of the constructed Monge–Ampère constant with lambda_mu uses Theorem 12.2.3, source non-kahler-pluripotential-theory:876DF057 / tag 2DB664A6EFDF (docs/sections/a-gauduchon-variational-volume--the-quotient-and-the-smooth-equation/index.html, blob 9ec67161d46b3ba20afa1b1c9a0c84f29322763e, physical lines 49–80). Smooth-dependence Proposition 12.3.2, source :6D3F0AB8 / tag 94AFD9E43DE0 (blob d94e3fc055b0642a86495c27ad8f5af6f24f17d1, lines 34–58) was context only.

**Affected dependents:** §12.4.4 Hessian form; §12.6 metrics; §12.2.3 quotient, §11.23.2 adjoint. They are **not independently certified**. No original printed theorem is false. An optional proposed insertion is an example after Proposition 12.4.1; no body edit authorized in this audit.

**Prior related but separate issue:** POME-GAUD-SECONDVAR-EQ-ALIAS-NESTED-001, previously confirmed duplicated equation alias at §12.4 line 79; neither reopened nor falsely resolved by this model.

**Coverage and deferrals:** only the selected proof/model and explicit crosschecks listed above; zero whole sections certified. All old entries preserved. All owner-excluded approximation/regularization, Bergman, weighted L², OT, multiscale and positivity-loss work remains deferred-by-user, not resolved.
