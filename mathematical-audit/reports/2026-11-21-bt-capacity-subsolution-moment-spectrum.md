# Bedford–Taylor capacity, subsolution moment spectrum, and selected non-Archimedean dependencies

**Audit date:** 2026-11-21. **Reviewed \`main\`:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Audit target:** \`review/mathematical-audit\`. **Status:** no new confirmed printed error; one **low / verified conditional deduction**, dependent on the stated internal proofs. No claim of transitive certification.

## Immutable reading-edition scope

- **§7.1, Bedford–Taylor products and local capacity**: \`docs/sections/bedford-taylor-products-and-local-capacity/index.html\`; blob \`41bc964bad8bf8505892c2cb3762e5cce2071ae6\`. Read the complete mathematical introduction, physical lines 7–16; section tag \`2F5912FF9FEA\`. This is an introductory section, **not** a certification of the results it points to.
- **§7.4, Weighted estimates and Monge–Ampère capacity**: \`docs/sections/bedford-taylor-products-and-local-capacity--weighted-estimates-and-monge-ampere-capacity/index.html\`; blob \`801a6ce8d25a6db19202cbc295937a135a9a208e\`. Complete direct mathematical lines **7–214**. Theorem 7.4.1 source \`foundations-of-pluripotential-theory:93A06A12\`, permanent \`7C68264563C0\`, statement 11–15, proof 20–78; Definition 7.4.2 \`AF32B1A0 / E9E7C75396D2\` lines 85–94; Proposition 7.4.3 \`DE1E4FA5 / 97EFDB6FDEE3\` lines 97–139; Proposition 7.4.4 \`554B46C3 / 815E5BBFC34A\` lines 143–163; Błocki Proposition 7.4.5 \`564DB76B / EB80820D2146\` lines 170–203, capacity estimate 207–214.
- **§7.11, Local energy moments**: \`docs/sections/bedford-taylor-products-and-local-capacity--local-energy-moments/index.html\`; blob \`e619f7aa95f80ce11aa676193b054db3180e59d4\`. **Selected**, not whole-section: Definition 7.11.1 lines 13–22, source \`foundations-of-pluripotential-theory:D8DE74C5\`, permanent \`E1129C8F823C\`; Theorem 7.11.2 source \`C2BB479D\`, permanent \`05F71889C324\`, statement 25–40, proof 45–91; Proposition 7.11.5 source \`3263E506\`, permanent \`1151DF7B32E4\`, lines 98–177; selected mixed-energy Theorem 7.11.33 lines 705–818 and Corollary 7.11.38 lines 823–870. Intermediate §§7.11.8–7.11.32 **not** completely read in this session.
- **§22.1, Non-Archimedean pluripotential theory**: \`docs/sections/non-archimedean-pluripotential-theory/index.html\`; blob \`8448d710690ebe1cc28040f9611d05c9d008a961\`. **Selected**, not whole-section: lines 24–169 including Definition 22.1.2 source \`sgpt:B01CC65A\`, permanent \`657951EB240B\` (29–44); volume Definition 22.1.7 source \`sgpt:6F37B588\`, permanent \`A92D6DFAC0CF\` (119–123); monotone mass-deficit Lemma 22.1.9 source \`sgpt:DA29B884\`, permanent \`587EEDE88F4F\` (142–170). The previously reported countable-cofinal-Kähler-ray finding \`POME-NA-KAHLER-COFINAL-RAY-INVLIMIT-001\` is **not** repeated.

## New finding: POME-BT-SUBSOLUTION-MOMENT-SPECTRUM-001

**Severity/status:** low / **verified conditional deduction**. Neither Theorem 7.11.2 nor Proposition 7.11.5 is asserted false. The proof is algebraically complete given their stated tail and cube-average bounds; **their full transitive analytic proof chains remain uncertified**.

Let \(B\subset\mathbb C^n\) be a ball, \(n\ge1\), and \(\mu\) a finite positive Borel measure such that
\[
0\le\mu\le(dd^cw)^n,\quad w\in\mathrm{PSH}(B)\cap L^\infty(B).
\]
Write \(m=\mu(B)\), \(M=\sup_Bw-\inf_Bw\), and for \(\varphi\in\mathcal E_0(B)\), \(p\ge1\), set
\[
E=e_p(\varphi),\qquad N=n+p,\qquad K=2^{n+p}(n+1)!M^nE.
\]
Then **simultaneously for every real \(0<q<N\)**,
\[
\boxed{\quad\int_B(-\varphi)^q\,d\mu\le
\frac{N}{N-q}\,m^{\,1-q/N}K^{\,q/N}.\quad} \tag{A}
\]
At the endpoint, \(-\varphi\in L^{N,\infty}(\mu)\) with
\[
\boxed{\quad \sup_{t>0}t\,\mu\{-\varphi>t\}^{1/N}\le K^{1/N}.\quad} \tag{B}
\]
Theorem 7.11.2 prints the \(q=p\) case of (A); (A) covers **the entire subcritical moment spectrum**, and (B) identifies the critical weak endpoint. The strong \(q=N\) bound is **not** claimed.

**Proof.** The precisely stated tail estimate (7.11.3) reads
\[
\mu\{-\varphi>t\}\le\min(m,Kt^{-N}).
\]
If \(m=0\) or \(K=0\), the tail and all integrals vanish. Otherwise put \(T=(K/m)^{1/N}\). Tonelli's layer-cake identity for any real \(0<q<N\) yields
\[
\begin{aligned}
\int_B(-\varphi)^q\,d\mu
 &=q\int_0^\infty t^{q-1}\mu\{-\varphi>t\}\,dt\\
 &\le mT^q+qK\int_T^\infty t^{q-N-1}\,dt\\
 &=mT^q+\frac{qK}{N-q}T^{q-N}
 =\frac{N}{N-q}m^{1-q/N}K^{q/N}.
\end{aligned}
\]
The same tail bound without integrating gives (B). At \(q=p\), \(N/(N-p)=1+p/n\), recovering exactly (7.11.4) and its constant. For scalar \(a>0\), \(e_p(a\varphi)=a^{n+p}e_p(\varphi)\) whereas the left side of (A) scales by \(a^q\); thus the exponent \(q/(n+p)\) on \(e_p\) is forced by homogeneity, **without claiming the numerical constant is geometrically optimal**.

**Transfer to the canonical cube averages.** Additionally suppose \(\operatorname{supp}\mu\Subset B\) and let \(\mu_j\) be the actual cube-averaging measures (7.11.5). Proposition 7.11.5(2)–(3), in particular inequality (7.11.6) with exponent \(q\), implies for every \(1\le q<N\), all \(j\ge j_0\), and all \(\varphi\in\mathcal E_0(B)\),
\[
\boxed{\quad\int_B(-\varphi)^q\,d\mu_j\le
D_{n,q}\frac{N}{N-q}\,
m^{1-q/N}K^{q/N}.\quad} \tag{C}
\]
Indeed, on each cube \(Q\) the normalized Lebesgue average of \((-\varphi)^q\) is at most \(D_{n,q}(-\varphi(z))^q\) for every \(z\in Q\), and integration in \(z\) against \(\mu\) followed by summation gives \(\int(-\varphi)^q\,d\mu_j\le D_{n,q}\int(-\varphi)^q\,d\mu\). Apply (A). **No endpoint weak-\(L^N\) transfer to \(\mu_j\) is asserted**: an \(L^q\) cube-average inequality for \(q<N\) alone does not imply it.

This is a conditional quantitative strengthening of the existing subsolution framework, useful when bounding changing-density energy integrals (later §7.11) and the inputs to mixed-product limits (§7.12). It does **not** remove any prerequisites, justify exchanging other limits, or supply a new Monge–Ampère existence theorem.

**Proposed change:** optionally add (A)–(C) as a corollary *after* equation (7.11.4), retaining all original statements, tags, and attribution. This report is an audit-only proposal; no reading-edition source or registry files were altered.

## Additional proof checks and open dependencies

1. **§7.4.1, lines 31–77:** the common quadratic collar makes the modified Bedford–Taylor products agree near \(\partial B\); the compactly supported cutoff argument uses the positive \(dd^cV\) term only for \(q\le n-1\), and the additional complex coordinate reduces \(q=n\) to that case. The factor \(\pi/4\) from the \(w\)-disc is consistent with the \(\beta_w=dV_2\) normalization. The proof still depends on the earlier CLN bound §7.2.5, Bedford–Taylor decreasing convergence §7.3.7, and the stated submean/convolution facts.
2. **§7.4.3–§7.4.5, lines 97–203:** checked the direction of the restriction/extension capacity inequalities, the outer-capacity neighborhoods, Borel-null enlargement of pluripolar sets, and each of the \(n\) Błocki integrations by parts. This direct check found no new confirmed statement/sign mistake. The arbitrary positive-current weighted extension is expressly *not* claimed: §7.4 lines 82–83 supplies a hypersurface obstruction.
3. **§7.11.2 and §7.11.5, lines 25–176:** checked the substitution \(s=t/2\), exponent \(n+p\), layer-cake balancing, cube/polydisc dimension \(2n\), the \(32^n\) scaling factor, and transfer to compact-support cube measures. Mixed-energy §7.11.33 and truncation Corollary 7.11.38 were inspected **selectively** for boundary collar, \(j^{-n-1}\) choice, energy control and \(T^{-1}\) truncation error; the intervening convergence arguments were not certified.
4. **§22.1.2–§22.1.9, lines 24–169:** checked the **reversed** directed Kähler order, transitions, nonnegative terms in the mixed-mass expansion (22.1.9), and the distinction between decreasing nets and sequential compactness. This is **not** a fresh full §22.1 review. The previously recorded cofinal-ray deduction remains historic progress, not newly claimed here.

**Unresolved:** complete proof-chain verification of CLN/weighted Bedford–Taylor convergence and capacity locality (§§7.2–7.5), the subsolution theorem's dependence on Błocki and the bounded-density Dirichlet solver (§7.10), the intermediate varying-density convergence chain (§7.11.8–§7.11.32), and non-Archimedean mixed-mass/\(\mathcal I\)-model transition results. None is marked resolved. Dependencies that would enter the user's excluded Demailly regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof-completion programme are **deferred-by-user**, not explored or certified.

**Accounting:** +2 complete direct mathematical sections (§§7.1 and 7.4, including the short introductory §7.1); +2 other sections checked selectively (§§7.11 and 22.1); +1 conditional quantitative deduction; +0 complete transitive certifications. Historical-first-visit status remains unreconciled. No tests, builds, CI, publishing or production edits were performed.
