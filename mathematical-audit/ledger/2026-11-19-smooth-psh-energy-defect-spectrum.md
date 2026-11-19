# Finding POME-ENERGY-SMOOTH-L1-DEFECT-SPECTRUM-001

Date: 2026-11-19
Status: **verified conditional deduction**; severity **low**; not a false theorem, not a proof-gap repair, not a duplication of the printed \(\ell=\tfrac12\) case.
Review baseline: production `main` **b6933b772f41b45918f7e25ed1afbbb1fd892272**.
Section: `docs/sections/relative-energy-and-perron-segments--continuity-and-compactness/index.html`, blob `6fd38d5ff9d0037e9d0d347814a95ad97331715f`, full mathematical text lines 7–242; Example 17.4.11 `foundations-of-pluripotential-theory:68158160`, permanent `27DF9596E862`, lines 226–242.
Internal conditional identity: Example 17.3.16 `foundations-of-pluripotential-theory:0C651973` / permanent `6EAA0093766C`, integrated lines 220–226, blob `16fdcc4c6a6f0cc75e69ba267bd7da2b2d7922a1`.

**Exact new deduction.** For any \(\ell\ge0\), the smooth, strictly \(\omega_{\mathrm{FS}}\)-psh, \(\sup=0\) functions \(u_a=a\log((|z|^2+\exp(-2\ell/a^2-1/a))/(1+|z|^2))\) converge to zero in \(L^1(\mathbb P^1)\), with \(\omega+dd^cu_a\rightharpoonup\omega\), while \(E_\omega(u_a)\to-\ell\) and \(du_a\wedge d^cu_a\rightharpoonup2\ell\delta_0\). With \(\varepsilon=e^{-a^{-3}}\), energy instead tends to \(-\infty\). The normalized gradient integral is \(a^2(-\log\varepsilon+O(1))\) with uniform \(O(1)\); outside any fixed neighborhood of zero it is \(O_R(a^2)\). All steps are proved in the [complete report](../reports/2026-11-19-smooth-psh-energy-defect-spectrum.md). This does not reproduce the old \(\ell=1/2\) demonstration as a new finding.

**Proposed correction / dependents:** No printed correction required. An optional future editorial addition after Example 17.4.11 could distinguish weak measure continuity from the possible entire range of energy defects. It sharpens the interpretation of Corollary 17.4.5 and the hypotheses needed for energy-compactness arguments in §17.5. Both printed statements remain intact.

**Coverage:** +1 entire §17.4 integrated direct reading (Proposition 17.4.1, Lemma 17.4.3, Proposition 17.4.4, Corollary 17.4.5, Propositions 17.4.6–7, Corollary 17.4.8, Proposition 17.4.9, Lemma 17.4.10, Example 17.4.11), +1 selected upstream identity (§17.3.16), +0 fully certified transitive proof chains. Prior first-visit history is **not** inferred. Existing user-deferred Demailly/Bergman/\(L^2\)/OT/multiscale/positivity-loss files stay **deferred-by-user**, not resolved.
