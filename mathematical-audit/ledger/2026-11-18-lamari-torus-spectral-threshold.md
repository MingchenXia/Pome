# POME-LAMARI-TORUS-SPECTRAL-THRESHOLD-001

- **Date:** 2026-11-18.
- **Severity / status:** **low / verified conditional deduction**; **not** a false theorem or an identified proof gap.
- **Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; exact §11.6 integrated blob \`6dd43b62800206fb0302fd4261372d7882e5170d\`.
- **Sources and anchors:** \`docs/sections/gauduchon-metrics-and-linear-mass--the-gauduchon-criterion-for-positivity/index.html\` Theorem 11.6.1 source \`non-kahler-pluripotential-theory:87DC00D0\` / permanent \`88BE3B63D9E5\` lines 11–73; Corollary 11.6.2 source \`EAE0F4AE\` / permanent \`F83E15A1F529\` lines 82–97; Lemma 11.6.3 source \`DC67F892\` / permanent \`91B8C8A3C10E\` lines 105–126.
- **Hypotheses:** \(X=E^n,\ n\ge2\), \(\omega=\sum\omega_j\) flat Kähler, \(\theta=\sum a_j\omega_j\), \(\omega_j>0\) flat diagonal coordinate forms.
- **New verified result:** \(\kappa_\omega(\theta)=\min a_j\). A smooth Gauduchon test attains this infimum **iff** all \(a_j\) are equal; nevertheless \(\theta-\min a_j\,\omega\ge0\) gives a smooth primal optimizer. For \(\gamma_t=t\omega_1+\sum_{j>1}\omega_j\) the exact gap is \(t\sum_{j>1}(a_j-a_1)/(1+(n-1)t)\), and normalized \(\gamma_t^{n-1}\) converge smoothly to a rank-degenerate positive \(\mathrm{dd}^c\)-closed test form.
- **Justification:** positive trace gives the lower bound and strict nonattainment, exact wedge expansion gives the reverse bound and limiting test. See [complete proof](../reports/2026-11-18-lamari-torus-spectral-threshold.md).
- **Proposed correction:** no source correction required; retain sharp example in audit as a warning not to identify existence of an optimal curvature current with existence of a smooth minimizing Gauduchon test.
- **Affected dependents:** the interpretation of §11.6.2 and the closing criterion following §11.6.3, not their validity. General Hahn–Banach, Gauduchon existence, elliptic Fredholm and current-to-psh steps remain conditional inputs.
- **Duplication/deferral:** no prior identical flat-torus spectral threshold entry found in the readable central audit logs; user-excluded Demailly approximation/regularization and its dedicated programmes remain **deferred-by-user**, not solved.
