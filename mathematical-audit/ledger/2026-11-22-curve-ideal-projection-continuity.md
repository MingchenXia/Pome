# POME-IDEAL-CURVE-PROJECTION-ONLY-CONTINUOUS-AT-ZERO-001

**Date:** 2026-11-22. **Status:** low / **verified conditional deduction**; not a false theorem, a claimed source correction or an end-to-end upstream certificate.

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

**Stable anchor:** Theorem 18.6.4 (source E7B73391, permanent A55ADED04CFD), docs/sections/multiplier-ideal-envelopes-and-goodness--geometry-of-ideal-classes/index.html, blob 64b1c0de9266a28727de07ca3502a13ab974f001, lines 43–86, plus lines 91–104. Projection Theorem 18.4.2 (source 3A211D73, permanent 7F20FD198864), docs/sections/multiplier-ideal-envelopes-and-goodness--ideal-projection/index.html, blob f1979b73c857f4874dd4a5cb10b93bcc047ebbdc, lines 22–51.

**Hypotheses:** connected compact Riemann surface \(Y\), smooth positive \(\theta\) of unit total mass, smooth positive probability \(\mathrm dV\); \(\mathcal K_\theta=\{u\in\operatorname{PSH}(Y,\theta):\sup_Yu=0\}\) with its \(L^1(\mathrm dV)\) topology.

**Claim:** \(\Pi(u)=P_\theta[u]_{\mathcal I}\) on \(\mathcal K_\theta\) is continuous precisely at \(u=0\).

**Proof core:** \(u\le\Pi(u)\le0\) yields \(\|\Pi(u)\|_1\le\|u\|_1\) at zero. For every target \(u\), normalized finite-atomic rational Green models \(a_j\to u\) in \(L^1\) have \(\Pi(a_j)=a_j\) (Theorem 18.6.4), while smoothing the probability curvature measure \(\theta+\mathrm{dd}^{\mathrm c}u\) and solving the **linear curve Poisson equation** gives smooth normalized \(s_j\to u\) with \(\Pi(s_j)=0\). If \(\Pi\) is continuous at \(u\), these two limits give \(u=0\). Details and exact upstream distinctions are in the [dated report](../reports/2026-11-22-curve-ideal-projection-continuity-and-background-mass.md).

**Correction:** no repair needed; optional conditional corollary after Theorem 18.6.4. **Affected:** §18.6 ideal-metric completion and future \(L^1\)-projection-continuity statements. **Unresolved upstream:** not every Green/compactness/ideal-envelope theorem has been independently certified. **Deferred-by-user:** Demailly regularization, Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss proof-completion programmes.
