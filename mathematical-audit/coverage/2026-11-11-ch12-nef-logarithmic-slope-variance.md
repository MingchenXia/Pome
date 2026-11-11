# Exact mathematical audit coverage — 2026-11-11

**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Finding:** \`POME-GAUD-NEF-LOGSLOPE-VARIANCE-001\` (low / verified conditional deduction).  
**Inventory:** the actual main ToC shows **25 chapters, 747 numbered sections**; this is NOT an assertion of exhaustive review.

| Location and checked blob | Exact direct inspection | Status / exclusion |
| --- | --- | --- |
| §12.20, \`docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary/index.html\`, blob \`a7c145c5d1ceb0f1326bfb155f75dc9d854f14a0\` | Proposition 12.20.1 (source \`non-kahler-pluripotential-theory:895EF015\`, tag \`EBFCF76A5A51\`, lines 19–70): definition of order and metric-change invariance; Proposition 12.20.2 (source \`:03644B93\`, tag \`883742E77C19\`, lines 78–101): closed-nef coefficients and polynomial; this run proves a **new full-ray variance formula** for its normalization root, strictness, sharp global distortion and Hölder bounds. | **Selected proof-level extension** in an already visited section, not complete original theorem certification. The earlier polynomial order is not counted as a new proof or discovered error. |
| §12.11, \`docs/sections/a-gauduchon-variational-volume--nef-limits-and-nonattainment/index.html\`, blob \`086d12a65c46cfb68c7d6fe952266515ca04623b\` | Theorem 12.11.1 (source \`non-kahler-pluripotential-theory:F03E2CAC\`, permanent \`9ECB2B21B601\`, lines 10–38): positive normalization root equals top intersection number for closed nef backgrounds. | **Internal conditional mathematical input**; its full PDE/quotient chain not reverified. |
| Projective product \(P^r\times P^{n-r}\) | Independent exterior-power count and exact logarithmic derivative for \(\theta=\alpha,\ h=\alpha+\beta\), \(1\le r<n\); sharp \(\varepsilon^{(n-r)/n}\) and \(1/n\) universal endpoint exponent. | Newly proved model; does not enlarge section-level coverage. |

**New stable finding:** [Complete dated proof](../reports/2026-11-11-nef-volume-logarithmic-slope-variance.md) · [classified ledger](../ledger/2026-11-11-nef-logarithmic-slope-variance.md).

**Counts:** 0 newly first-visited numbered mathematical sections; 0 whole mathematical sections certified; 0 newly confirmed false printed theorems. No claims of compiled tests, rendering checks, formalization, CI, or publication. Main and published reading edition unchanged.

**Owner-deferral remains in force:** the Demailly regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale atlas/positivity-loss programme was not opened; historical audit notes remain **deferred-by-user**, never certified.