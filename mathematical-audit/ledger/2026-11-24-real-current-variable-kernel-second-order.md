# POME-REAL-CURRENT-RADIAL-SMOOTHING-SECOND-ORDER-001
**Date:** 2026-11-24. **Severity:** low. **Classification:** verified conditional deduction; not a false printed theorem; no full upstream-chain certificate. **Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

**Precise anchors:** \`docs/sections/real-currents-submersions-and-homotopies--global-smoothing-and-the-poincare-lemma-for-currents/index.html\`, main blob \`597a770e3f087693b98968c6e5fcf8bcd9ca0841\`; Lemma 5.54.1 (source \`demailly-complex-geometry:7A345420\` / permanent \`A748F8312A04\`, lines 11–35), Theorem 5.54.2 (source \`demailly-complex-geometry:C92BDA92\` / permanent \`7D93F6AD9C80\`, lines 40–81; operator construction lines 51–54).

With the special permissible choice \(\rho_\varepsilon(v)=\varepsilon^{-m}\rho(v/\varepsilon)\), where \(\rho\ge0\) is fixed smooth radial, compactly supported in the unit ball, of mass one, let \(M_k=\int |v|^k\rho(v)\,dv\). For any **finite signed** Radon measure \(\mu\) on \(\Omega\), considered as a degree-\(m\) current, and \(\psi\) from Lemma 5.54.1,
\[
\left|\langle R_\varepsilon\mu-\mu,\phi\rangle\right|
\le \frac{M_2\varepsilon^2}{2}\|\psi\|_\infty^2|\mu|(\Omega)
\|D^2\phi\|_{\mathrm{op},\infty},
\]
and
\[
\varepsilon^{-2}(R_\varepsilon\mu-\mu)
\longrightarrow \frac{M_2}{2m}\Delta(\psi^2\mu)
\quad\text{in distributions}.
\]
For \(\phi\in C_c^\infty(\Omega)\), the error in the rescaled pairing is at most
\(M_3\varepsilon\|\psi\|_\infty^3|\mu|(\Omega)\|D^3\phi\|_{\mathrm{op},\infty}/6\).
Taylor expansion of \(\phi(x+\varepsilon\psi(x)v)\), cancellation of the radial first moment and isotropy of the quadratic moment prove the bounds. The exponent two is sharp already for \(\mu=\delta_{x_0}\) and \(\phi=|x-x_0|^2\) near an interior point with \(\psi(x_0)>0\).

**Proposed additive remark:** after Theorem 5.54.2, explicitly state the above under *fixed radial scaling*, not arbitrary approximate identities. The variable weight belongs **inside** the Laplacian. **Affected dependents:** quantitative distributional error estimates using §5.54.2, conditional on their test regularity and finite measure mass. **Not established:** total variation second-order convergence, new current-cohomology claims, full ancestor certification, or any excluded psh regularization result.

[Detailed proof and cross-checks](../reports/2026-11-24-real-current-signs-and-second-order-smoothing.md).
