# Classified audit ledger — 2026-11-10 — three-band transverse Gaussian rate

- **Stable ID:** POME-THREEBAND-TRANSVERSE-CLT-W1-001
- **Severity:** low.
- **Status:** verified conditional deduction; **not** confirmed error, proof gap, full repair, or genuine duplication.
- **Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Main document:** docs/sections/partial-kernels-and-quotient-equilibrium--three-monomial-bands-from-a-multiplier-ideal-selection/index.html.
- **Main file blob:** dec0c9cf53e927c039d6cf85c52c4da5d65c39cb.
- **Anchors and stable tags:** §18.47 source non-kahler-pluripotential-theory:FCCA87E3, tag 435C250083A1, lines 5–38; Proposition 18.47.4 source :79F7C192, tag AD8335312F45, lines 155–200; Eq. 18.47.5 source :2B37019C, tag CA62D9FD1FF2, lines 176–178; Eq. 18.47.6 source :748138C6, tag 8DAD90BE35BE, lines 181–191; Theorem 18.47.7 source :D3DDF8B8, tag A0E408FAE124, lines 205–220 and proof line 277. All abbreviated source labels use the full namespace non-kahler-pluripotential-theory.
- **Exact added result:** under normalized explicit monomial kernel probability $\Pi_m=(3m+1)^{-1}B_m\nu$, the transverse variable $\sqrt m(x_1-x_2)$ converges to $N(0,2)$ with bounded-Lipschitz error $O(m^{-1/2})$; $\sqrt m\,\mathbb E_{\Pi_m}|x_1-x_2|\to2/\sqrt\pi$. For the metric on the logarithmic cube times angular circles, $W_1(\Pi_m,\mu)=\Theta(m^{-1/2})$ with explicit lower test $|x_1-x_2|/\sqrt2$.
- **Justification:** exact Gaussian product expression from the three bands and the printed squared norms; uniform $e^{-m/2}/\sqrt m$ truncation tails; Gaussian moment estimate; direct coupling to lattice centers plus diagonal Riemann coupling; Kantorovich dual lower bound. Details: [full report](../reports/2026-11-10-threeband-transverse-gaussian-clt-transport.md).
- **Unresolved dependency:** the earlier multiplier-ideal selection and global envelope/positive-current results in §18.47 are **not** transitively proved here. No re-entry to excluded regularization-related proof-completion.
- **Proposed correction:** optional post-Theorem-18.47.7 quantitative remark, **not** a change to an incorrect theorem.
- **Affected dependents:** quantitative reading of normalized kernel measure convergence in Theorem 18.47.7; no global extension to unrelated kernels or other normalizations.
- **Coverage:** §18.47 first selected proof-level visit; §18.30 definition only; 1 new first visit, 0 complete sections. Prior ledger states unchanged; excluded regularization, Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas, positivity-loss remain **deferred-by-user**.
