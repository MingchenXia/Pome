# POME-CAP-C1-SMOOTH-SETWISE-FAIL-001

- **Date:** 2026-11-19.
- **Severity/status:** **low / verified conditional deduction** (sharp failure of a proposed *setwise* strengthening; printed Theorem 13.12.8 remains correct, no false theorem).
- **Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Integrated file/blob:** docs/sections/non-pluripolar-products--quasi-continuous-functions/index.html / 110ec8727eca146a1304cfd43fdbeb4eebf96290.
- **Stable statement:** sgpt:B4CE255F, permanent tag 272876B00528, integrated lines 100–116. The other seven entries of §13.12, lines 9–99, were also directly checked.
- **Hypotheses actually tested:** on a flat elliptic curve, smooth strictly θ-psh functions uniformly bounded and converging in \(C^1\) (hence globally in capacity), smooth Monge–Ampère measures with a common strict positive density *lower* bound, and constant bounded continuous weight χ=1.
- **Exact countermodel:** periodic microcell densities \(\rho_j\) supported on a union of sets of total fixed Lebesgue measure ≤1/64; solve \(v_j''=4\pi(1-\varepsilon)(\rho_j-1)\) periodically and set \(u_j=j^{-2}v_j(jx)\). The exact identity \(\theta+dd^cu_j=[\varepsilon+(1-\varepsilon)\rho_j]\theta\) gives weak convergence to θ; on the fixed Borel union \(A\) the measures assign ≥3/4, but θ(A)≤1/64. Full construction and estimates in [report](../reports/2026-11-19-quasicontinuity-smooth-setwise-boundary.md).
- **Proposed correction:** optional warning after Theorem 13.12.8: *weak* current convergence does not imply convergence of arbitrary Borel masses. Extra uniform density domination (sufficient, not necessary) restores setwise convergence on a fixed compact smooth reference; never infer total variation without additional justification.
- **Affected dependents:** any current argument substituting discontinuous indicators for continuous tests or claiming setwise/TV convergence merely from capacity convergence and bounded psh potentials.
- **Duplication guard:** old POME-BT-UNIFORM-BL-SQRT-SHARP-001 has uniformly bounded oscillatory densities and hence **does** converge setwise; old POME-CAP-WEIGHT-UNIFORM-BOUND-SHARP-001 concerns unbounded weights. Neither yields this fixed-Borel-set counterexample.
- **Unresolved:** upstream Kähler/BT capacity comparison and weighted product continuity were only traced, not certified. User-excluded regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss work **deferred-by-user**.
- **Coverage:** prior 2026-10-25 selected §13.12 visit retained; +0 first visits, +1 whole direct integrated section reading, +0 complete upstream certifications. No main/source/site/build/CI change.
