# 2026-11-23 — classical support dimension and b-divisor volume-order premise

## POME-BT-SUPPORT-DIMENSION-COEFFICIENT-BREAKDOWN-001

- **Severity/status:** low / **verified conditional deduction** (sharp hypothesis model), not an error in the printed theorem.
- **Main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Exact source:** docs/sections/classical-products-with-controlled-unbounded-loci--collars-relative-to-the-support-of-the-base-current/index.html, blob 86de377d6e6f17fc1a08a6e789a681ddfaabfac5, Corollary 7.31.4 source demailly-complex-geometry:4876F9E5, permanent EBA900FA96EF, lines 69–84; supporting §7.28.1 source demailly-complex-geometry:F96C3380, permanent 1BBBF8109419, lines 6–67.
- **Hypotheses/model:** \(1\le p<n\), \(Y=\{z_{p+1}=\cdots=z_n=0\}\) in a ball, \(T=[Y]\) closed positive bidimension \(p\), \(u=\log|z_{p+1}|\) psh.
- **Complete countermodel to a *proposed weakening*, not to the printed result:** \(\dim_\mathbb C(L(u)\cap\operatorname{supp}T)=p\); \(u|_Y=-\infty\). For \(u_M=\max(u,-M)\), \(-u_MT=MT\), so its mass against every fixed positive trace test on \(Y\) diverges **linearly** in \(M\). Yet \(dd^c(u_MT)=0\) for all \(M\). No classical coefficient-integrable product \(dd^c(uT)\) is defined.
- **Correction/affected dependents:** optional sharpness note after §7.31.4, emphasizing why analytic dimension at most \(p-1\) cannot be relaxed to \(p\) for arbitrary base currents and why convergent unweighted truncations alone do not prove classical-product existence. No production theorem correction, no changes to source tags.

## POME-BDIV-REGULARIZATION-NET-VOLUME-ORDER-001

- **Severity/status:** medium / **candidate proof gap; external dependency unresolved**. Neither Theorem 20.1.15 nor its volume equality is certified false.
- **Main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Exact source:** docs/sections/the-theory-of-b-divisors/index.html, blob 4a793dfd462badcb351f54a36cb030cde14a399b; Lemma 20.1.7 source sgpt:54FCB4C1, permanent F5B2C1F1E318, lines 66–99; Example 20.1.9 source sgpt:048A0D73, permanent 7AF528B0FB3B, lines 100–126; Theorem 20.1.15 source sgpt:A0644B2C, permanent 6EB1B4E1D222, lines 209–259, especially 251–259.
- **Missing demonstrated step:** Lemma 20.1.7 gives upper semicontinuity under coordinatewise *net* convergence and equality only for a decreasing net. Theorem 20.1.15 invokes the equality after convergence of its approximant b-divisors without recording monotonicity. The bounds \(a_E^j\le a_E\) are not the needed order comparison \(a_E^j\le a_E^{j+1}\). Example 20.1.9 refutes the general inference even for nef Cartier b-divisors with fixed root.
- **Conditional remedy fully checked:** If \(\varphi_j\ge\varphi_{j+1}+O(1)\), then every divisorial Lelong coefficient on each modification is nondecreasing, so \(\{\operatorname{Reg}\pi^*T_j\}\succeq\{\operatorname{Reg}\pi^*T_{j+1}\}\). Consequently \(\mathbb D(T_j)\) is a decreasing b-divisor sequence and Lemma 20.1.7 implies the volume equality. Whether the actual quasi-equisingular approximants satisfy this was not checked, by explicit exclusion.
- **Correction/dependents:** document actual monotone-order premise or supply an independently proved special continuity statement. Affects the proof of Theorem 20.1.15 and dependencies in §§20.1.24–27. Original theorem status remains unconfirmed by this candidate.
- **Deferred-by-user:** the Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss proof programme is not reopened or certified.

[Complete anchored report](../reports/2026-11-23-classical-products-support-threshold-and-bdiv-net-volume.md) · [coverage](../coverage/2026-11-23-classical-unbounded-products-and-bdiv-net-volume.md).