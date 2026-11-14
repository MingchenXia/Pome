# POME-TC-DECREASING-INF-NEGATIVE-INFTY-NONCOMMUTE-001

**Date:** 2026-11-14. **Severity:** low. **Status:** verified conditional deduction, not a false theorem.

On $\mathbf P^1$, the explicitly constructed model test curves $\Gamma^j_\tau=u_{c e^{\tau/j}}$ ($\tau<0$, $0<c<1$) have all negative-infinity endpoints equal to zero, yet the negative-infinity endpoint of their decreasing infimum is $u_c\neq0$, even though $\inf_j\int\langle\theta_{\Gamma^j_{\tau_0}}\rangle=1-c>0$. The reading edition already warns that the two operations need not commute; Proposition 17.15.40 itself remains correct.

**Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Integrated anchors:** `docs/sections/test-curves--operations-on-test-curves/index.html`, blob `3da617be8f58713f764d49ba22f49b803149a5e8`, Definition 17.15.37 `sgpt:2102B018` / `BDCF69FED30F` lines 813–839; Proposition 17.15.40 `sgpt:06038274` / `82DA4D86CC78` lines 843–858; printed warning lines 862–866. Supporting Definition 17.12.1 `sgpt:ECCF19D5` / `C8399F09D86D` and §16.3.4/.17 tags `395DB7860949`/`6623E38E5FC2`.

**Proposed change:** optional illustrative example, independently reviewable; do not alter main, original proof, registry, tags, or website. Prior §17.15.31 Choquet proof gap remains separate. All excluded Demailly regularization and dedicated programmes stay deferred-by-user.
