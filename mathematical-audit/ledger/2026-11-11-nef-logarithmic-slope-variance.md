# Classified finding — 2026-11-11 — nef root-volume moving exponent

| Field | Record |
| --- | --- |
| Finding ID | \`POME-GAUD-NEF-LOGSLOPE-VARIANCE-001\` |
| Severity | low |
| Status | **verified conditional deduction** |
| Mathematical issue | Distinguish the printed *volume* order \(n-r\) from the **normalization root** exponent \((n-r)/n\), and determine the variation of its effective logarithmic slope for every positive perturbation size. |
| Main SHA | \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` |
| Primary location | \`docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary/index.html\` (blob \`a7c145c5d1ceb0f1326bfb155f75dc9d854f14a0\`), Proposition 12.20.2, source \`non-kahler-pluripotential-theory:03644B93\`, permanent \`883742E77C19\`, lines 78–101 |
| Required formula | Theorem 12.11.1, \`docs/sections/a-gauduchon-variational-volume--nef-limits-and-nonattainment/index.html\` (blob \`086d12a65c46cfb68c7d6fe952266515ca04623b\`), source \`non-kahler-pluripotential-theory:F03E2CAC\`, permanent \`9ECB2B21B601\`, lines 10–38 |
| Hypotheses | Compact Kähler \(X\), \(\dim_\mathbb C X=n\ge2\); smooth closed nef \(\theta\); Kähler \(h\); smooth strictly positive probability \(\mu\). |
| Verified conclusion | Put \(P(\varepsilon)=\sum_{j=0}^nc_j\varepsilon^j\) with nonnegative \(c_j=\binom nj\int\theta^{n-j}h^j\), \(L=P^{1/n}\) (printed internal input), and \(w_j=c_j\varepsilon^j/P\). Then \(d\log L/d\log\varepsilon=\frac1n\sum j w_j\) and its derivative in \(\log\varepsilon\) is \(\mathrm{Var}_w(j)/n\ge0\), strictly positive whenever at least two coefficients are positive. Exact exponent and derivative at zero, universal sharp \(1/n\) Hölder bound and product-projective sharp examples also proved. |
| Status of original result | **Not false**. Proposition 12.20.2 already establishes the integral-order polynomial expansion; this entry does **not** re-report that expansion as a discovery. |
| Proposed adjustment | Optional new reader remark after Proposition 12.20.2 containing the variance identity and optimal root Hölder estimate with correct coefficient \((\sum_{j=1}^n j c_j)^{1/n}\). **No patch applied** to main/source/registry/tags. |
| Dependent results | Relative to the printed closed-nef identity and coefficient positivity in §§12.11.1, 12.20.2; optional quantitative input for §§12.21–12.25. Elliptic/quotient prerequisites remain conditional. |
| Full proof | [2026-11-11 report](../reports/2026-11-11-nef-volume-logarithmic-slope-variance.md) |
| Actual coverage | Previously partially audited §12.20, selected proof algebra; §12.11 dependency only. **0 new first section visits / 0 complete sections certified**. ToC: 25 chapters / 747 sections. |
| Excluded work | Demailly approximation/regularization and all dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion remain **deferred-by-user**, neither reviewed nor certified. |

No tests, build, GitHub Actions CI, formalization, automatic publication, or direct source changes were performed.