# POME-SH-HARTOGS-L1-SHARP-UPPER-001

- **Date:** 2026-11-23.
- **Reviewed main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Severity / status:** **low / verified conditional deduction**. **NOT** a confirmed printed error, proof repair, or transitive certification.
- **Reading-edition anchors:** **docs/sections/subharmonic-functions/index.html** (blob **3d06e9703f2eb184cf63a2c45524ed6acbeeebd2**), §3.4.12(2), physical 219–239 and 260–273, source **foundations-of-pluripotential-theory:7E2C1398**, permanent **E76E281548A5**; §3.4.20 physical 418–456, source **foundations-of-pluripotential-theory:CAECA7D8**, permanent **5784B80133BF**.
- **Hypotheses:** \(K\Subset U\Subset\Omega\subset\mathbb R^d\); \(u\in\mathrm{SH}(\Omega)\cap C^{1,1}(U)\); \(v\in\mathrm{SH}(\Omega)\cap L^1_{\mathrm{loc}}(\Omega)\); sufficiently small \(\delta=\int_U|v-u|\).
- **Claim proved:** \(\sup_K(v-u)\le C\delta^{2/(d+2)}\). The exponent is optimal, even for fixed smooth strictly subharmonic \(u(x)=|x|^2\) and smooth subharmonic \(v_\varepsilon=u+a\varepsilon^2\phi(x/\varepsilon)\), since \(\delta_\varepsilon=a\varepsilon^{d+2}\int\phi\) and \(v_\varepsilon(0)-u(0)=a\varepsilon^2\). See [complete quantitative proof and checks](../reports/2026-11-23-quantitative-hartogs-c11-envelopes-and-boundary-problems.md).
- **Proof basis:** radial submean mollifier inequality from §3.4.13; zero first mollifier moment; quadratic Taylor remainder; local \(L^1\)-to-mollification bound; optimization. No exclusion-program input.
- **Proposed correction/addition:** optional separate quantitative corollary after §3.4.20 with its stronger \(C^{1,1}\) assumption; leave original theorem, its assumptions, all tags and historical attribution intact.
- **Potential dependents:** quantitative local upper semicontinuity and obstacle/envelope estimates where the limit is \(C^{1,1}\); no claim that any other result has been fully certified.
- **Limitations:** only the **upper** pointwise deviation; existing §3.4.24 rules out symmetric \(L^\infty\) convergence. Not a claim about an arbitrary nonsmooth limit or nonradial signed kernel.
- **Unresolved prerequisites:** whole Weyl/positive-distribution and global elliptic existence chains not independently certified. User-excluded regularization and analytic subprogrammes remain **deferred-by-user**, not resolved.
