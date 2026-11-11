# Classified ledger — 2026-11-12 — Sharp cone necessity in harmonic Poisson boundary limits

- **Stable ID:** \`POME-HARM-FATOU-CONE-UNIVERSAL-SHARPNESS-001\`.
- **Severity/status:** **low / verified conditional deduction**. Original Theorems 3.3.9 and 3.3.14 are **not** refuted, and no proof-gap repair is claimed.
- **Main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; **integrated file/blob:** \`docs/sections/classical-harmonic-analysis/index.html\` / \`75e982788e627af602981823a82863cbd36ee712\`.
- **Anchors:** Theorem 3.3.9 source \`classical-potential-theory:4ADDEE1E\`, permanent \`CAE5D89698DF\`, lines 119–139; Theorem 3.3.14 source \`classical-potential-theory:7C0C933C\`, permanent \`EEE7DD56F49D\`, lines 190–212 (kernel estimate 196–203).
- **Hypotheses:** \(d\ge2\), unit ball, bounded real measurable \(f\) with approximate boundary value \(a\) at a fixed \(\zeta\), and a prescribed sequence \(x_n\to\zeta\).
- **Verified mathematical statement:** universal convergence of \(P[f\sigma](x_n)\to a\) for every such \(f\) occurs **if and only if** \(|x_n-\zeta|/(1-|x_n|)\) is eventually bounded. For escaping-aperture sequences, a bounded \(0\le f\le1\) built from disjoint shrinking spherical caps has boundary density zero at \(\zeta\) yet Poisson values bounded away from zero along a subsequence. Explicit quantitative proof in linked report.
- **Proposal:** add an optional clarification of the sharpness of nontangential approach; do **not** change the theorem itself.
- **Affected dependents:** any use of the Fatou theorem with unrestricted spatial approach absent genuine boundary continuity; **no printed false dependent proven**.
- **Dependency boundary:** normalized ball kernel, cap-volume comparability, elementary annular estimates. Does not certify the whole Dirichlet theory or §3.3.
- **Distinct from:** previous half-space Poisson weak-trace uniqueness and Poisson \(L^p\)/total-variation sharpness findings.
- **Coverage:** additional selected proof/model check in already partially reviewed §3.3; **+0 first numbered sections, +0 fully mathematically certified sections**; main ToC 25/747.
- **Deferred-by-user:** Demailly regularization/approximation and dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss proofs remain excluded.
- **Proof:** [full English report](../reports/2026-11-12-sharp-cone-fatou-bounded-poisson.md).
