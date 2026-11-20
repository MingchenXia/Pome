# 2026-11-20 — Planar superexponential Wiener obstacles

**POME-WIENER-PLANAR-SUPEREXP-LOGLOG-001** — **low / verified conditional deduction**; NOT confirmed printed error, NOT independent proof of the Wiener criterion; distinct from 2026-10-30 **POME-WIENER-SPARSE-BALLS-LOGLOG-001** (d≥3 only).

- Main baseline: **b6933b772f41b45918f7e25ed1afbbb1fd892272**.
- Exact reading anchor: **docs/sections/perron-theory-and-fine-boundary-limits/index.html**, blob **4bc2fb9317e2b6f6bb5b2d90208c677da8275eba**, section §4.4 physical mathematical lines **7–381**; Theorem 4.4.26 **345–380**, source **classical-potential-theory:BE9DEDF9**, permanent **A856D11F5895**; section tag **5CFAC22DC258**. Selected §4.1.16/.19/.21 capacity input, file and blob specified in detailed report.
- Model: $F_j=\overline B(e^{-2^{j+1/2}}e_1,\frac1{20}e^{-2^{j+1/2}(j+1)^\alpha(\log(j+\mathrm e))^\beta})$, $E=\{0\}\cup\bigcup F_j$, $\Omega=B_1\setminus E$, $\alpha,\beta\ge0$. Wiener shell $E_j=F_j$ for large $j$; $2^jC^*_{B_{1/2}}(E_j)\asymp j^{-\alpha}(\log j)^{-\beta}$.
- **Proved conditional conclusion:** boundary $0$ is regular iff $\alpha<1$ or $\alpha=1,\beta\le1$, and irregular iff $\alpha>1$ or $\alpha=1,\beta>1$.
- Input verification: integrated Theorem 4.4.26, §4.4.22, §4.1.16/.19/.21; planar Green-circle energy comparison fully written. The upstream fine-topology/Perron proof chains are **not fully certified**.
- Proposal: optional new example after §4.4.26; do not alter main, body, registry, source labels, permanent tags, or historical attribution. Affected downstream: planar boundary regularity, sparse-obstacle tests; no extant theorem shown false.
- Status ledger: resolved **0**, new confirmed errors **0**, new verified conditional deductions **1**, full upstream certifications **0**, pre-existing unresolved and **deferred-by-user** exclusions **unchanged**.

[Detailed English mathematical proof](../reports/2026-11-20-planar-wiener-superexponential-obstacles.md) · [exact coverage](../coverage/2026-11-20-ch4-perron-fine-boundary-full.md).
