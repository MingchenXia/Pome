# Classified ledger — 2026-11-11 — Green boundary test classes

- **ID:** `POME-GREEN-BDY-HARMONIC-VS-PLURIHARMONIC-001`
- **Severity/status:** **low / verified conditional deduction** (not a confirmed error, proof gap, duplicate, or certified repair).
- **Main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated path/blob:** `docs/sections/green-level-measures-and-boundary-representation/index.html` / `895dbdfaa3c78ce41abe556f573644d857ab7517`.
- **Anchors:** §7.20.3 `klimek-pluripotential-theory:62713F04` / `EC62871F80C4`, physical lines 85–105; §7.20.4 `klimek-pluripotential-theory:D0489F01` / `438C4583CB39`, lines 109–132; convention line 7.
- **Assumptions:** complex dimension \(n\ge2\); \(a_t=(t,0,\ldots,0)\); test \(v=|z_1|^2-|z_2|^2\), Euclidean harmonic but not pluriharmonic; normalized Green boundary probability \(\rho=2^n\mu\).
- **Verified calculation:** on \(\Delta^n\), \(\int v\,d\rho=0\ne t^2=v(a_t)\) for every \(0<t<1\); on \(B\), \(\int v\,d\rho=n t^2/(n+1)+O_n(t^4)\), giving a strictly positive discrepancy \(t^2/(n+1)+O_n(t^4)\) for small \(t>0\). The product polydisc kernel nevertheless reproduces all continuous separately harmonic functions by iterated one-variable Poisson integration.
- **Correction proposed, not applied:** clarify after §7.20.4 that Green boundary measures are **not** ordinary Euclidean harmonic measures in dimension \(n>1\), and distinguish the valid reproducing classes. The printed propositions themselves remain valid.
- **Affected dependents:** potential downstream applications substituting real-harmonic for pluriharmonic tests; no actual printed false dependent located.
- **Proof/dependency boundary:** self-contained spherical-moment and polydisc computations conditional on §7.20.3–4's already printed kernels and normalizations; their full upstream proof chains not recertified.
- **Coverage:** first proof-level visit to §7.20: **+1**, fully certified numbered sections: **0**; ToC inventory **25 chapters, 747 sections**. Other unreviewed sections remain open.
- **Excluded programme:** Demailly approximation/regularization and dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proofs remain **deferred-by-user**.
- **Full report:** [2026-11-11 Green boundary test classes](../reports/2026-11-11-green-boundary-kernels-harmonic-versus-pluriharmonic.md).
