# POME-VARMA-TV-DATA-NONUNIFORM-001

- **Date:** 2026-11-17.
- **Severity/status:** low / **verified conditional deduction**; not a confirmed error or proof gap.
- **Main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Integrated file/blob:** docs/sections/relative-energy-and-perron-segments--variational-monge-ampere-equations/index.html @ d86dcef056e4e8d03a5974027ed7cc226d35eefc.
- **Exact anchors:** Proposition 17.5.7, foundations-of-pluripotential-theory:B027C133 / 5BDA01022188, lines 125–143; Theorem 17.5.13, foundations-of-pluripotential-theory:0B32BA83 / 109ED281DA22, lines 241–260. Corollary 17.5.26, lines 503–520, contextual.
- **Hypotheses:** $X=\mathbb P^1$, $\theta=\omega_{\rm FS}$ of unit mass, model $\phi=0$, $\lambda>0$ fixed. Smooth $\omega$-psh $u_k$, and smooth positive $\nu_k=e^{-\lambda u_k}(\omega+dd^cu_k)$.
- **Conclusion:** $\|\nu_k-\omega\|_{\rm TV}=O(k^{-1})$ and $u_k\to0$ in $L^1$, but $\|u_k\|_\infty\to2$; densities have a uniform positive lower bound but unbounded upper bound.
- **Justification:** fully explicit smooth $T_r$, exact $u_k(p)$, $t_*\omega=dt$, and bounded signed-measure variation; see [anchored proof](../reports/2026-11-17-variational-ma-tv-data-not-linfty-stable.md).
- **Correction/dependents:** no correction to printed theorems; do not infer TV-to-$L^\infty$ solution stability without additional uniform density/capacity/multiplicative control. Comparison/domination and variational existence remain conditional upstream; not globally certified.
- **Coverage:** existing partly inspected §17.5; newly checked §17.5.7 and §17.5.13 at statement/proof level plus §17.5.26 hypothesis contrast. +0 first-numbered-section visits; +0 entire-section certificates; project index previously counted 25 chapters/747 sections.
- **Deferred-by-user:** all excluded Demailly approximation/regularization and dedicated related proof-completion programmes, untouched.
