# Audit: decreasing upper-semicontinuous weights over arbitrary directed nets

**Date:** 2026-10-24, Asia/Shanghai. **Reviewed Pome main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Review branch at start:** \`c3ee48024045c9e23ac92f32acbc72ad235b6ab5\`.
**Status and coverage:** first selected proof review of §§5.61–5.63 and §10.101 on the current 25-chapter/747-section reading edition. This is not a certification of any complete section or of the whole project. All dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof completion remains **deferred-by-user**, not repaired.

## Finding POME-USC-WEAK-NET-001

- **Severity:** low.
- **Status:** **verified conditional deduction** (genuine generalization of the *printed sequential* measure lemma; **not** a false theorem, correction of a mistake, or formal verification).
- **Source:** \`docs/sections/positive-current-coefficient-bounds-and-support-maxima/index.html\`, blob \`cb4c3d4e9d653b216cff05eaf23aafb2a01425ec\`; Lemma **5.63.3**, source \`demailly-complex-geometry:6F59E05A\`, permanent tag \`192CB50CA0EA\`, lines **45–79**, particularly the compact-set upper weak inequality (55–65) and decreasing limit (67–79).
- **Hypotheses of the new result:** X is locally compact Hausdorff; I is any directed set; \(\mu_i\) and \(\mu\) are positive Radon measures, \(\mu_i\to\mu\) vaguely along I; \(f_i:X\to[-\infty,\infty)\) is upper semicontinuous and **decreases pointwise along I**, with \(f=\inf_i f_i\); every \(f_i\mu_i\) is a locally finite signed Radon measure. Suppose a Moore–Smith subnet of these signed measures converges vaguely to a locally finite signed Radon measure \(\nu\).
- **Conclusion:** \(f\in L^1_{\mathrm{loc}}(\mu)\), and \(\nu\le f\mu\) as signed Radon measures. There is **no first-countability, sequential compactness, cofinal sequence, or metrizability hypothesis**.

### Proof (not relying on sequential reductions)

**1. Upper weak bound for nets.** If \(\mu_i\to\mu\) vaguely and \(C\subset X\) is compact, every nonnegative \(\phi\in C_c(X)\) with \(\phi\ge1\) on C gives
\[
 \limsup_i\mu_i(C)\le\int\phi\,d\mu.
\]
Locally compact Hausdorff cutoffs and outer regularity imply
\(\limsup_i\mu_i(C)\le\mu(C)\). Furthermore \(\sup_i\mu_i(K)<\infty\) **eventually**, for every compact K: choose one compactly supported cutoff at least one on K, then use vague convergence.

For a bounded nonnegative upper-semicontinuous g with compact support K, its superlevel sets \(\{g\ge t\}\) are compact for t>0. Let \(0\le g\le M\) and \(\delta=M/N\). Upper and lower step sums give
\[
 \delta\sum_{j=1}^{N}\mu_i(\{g\ge j\delta\})
 \ \le\ \int g\,d\mu_i
 \ \le\ \delta\mu_i(K)+\delta\sum_{j=1}^{N}\mu_i(\{g\ge j\delta\}).
\]
For each *fixed finite* N take upper limits of the finitely many terms, apply the compact-set inequality, then let N increase. The upper and lower step integrals converge to \(\int g\,d\mu\), and the \(\delta\mu_i(K)\) error vanishes uniformly on a tail. Hence
\[
                 \limsup_i\int g\,d\mu_i\le\int g\,d\mu. \tag{1}
\]
This finite-step argument is valid for nets; no sequential Fatou lemma is used.

**2. Decreasing upper-semicontinuous nets for a fixed Radon measure.** Suppose \((g_i)\) is a decreasing directed net of nonnegative bounded upper-semicontinuous functions, all supported on one compact K and bounded above by one fixed M, and \(g=\inf_i g_i\). For t>0, \(K_{i,t}=\{g_i\ge t\}\) is a decreasing directed family of compact sets with intersection \(\{g\ge t\}\). Compactness and outer regularity show
\[
 \inf_i\mu(K_{i,t})=\mu\Bigl(\bigcap_iK_{i,t}\Bigr). \tag{2}
\]
Indeed, for any open U containing the intersection, a finite-intersection argument in the compact initial K shows that some \(K_{i,t}\subset U\); choose U with mass arbitrarily close to that of the intersection. Applying finite step sums as above and using **directedness for each finite collection of thresholds** proves
\[
                  \inf_i\int g_i\,d\mu=\int g\,d\mu. \tag{3}
\]
This is the needed Radon/upper-semicontinuous *net* version of decreasing convergence, not an invocation of sequential monotone convergence for arbitrary nets.

**3. Varying weights and measures.** Let \(\nu\) be a convergent subnet limit. Fix a compactly supported continuous test \(\chi\ge0\), \(i_0\in I\), and m>0. On the tail \(i\ge i_0\),
\[
 \int\chi f_i\,d\mu_i\le\int\chi\max(f_{i_0},-m)\,d\mu_i.
\]
On the support of \(\chi\), upper semicontinuity bounds \(f_{i_0}\) above. Apply (1) to
\(g=\chi(\max(f_{i_0},-m)+m)\) and subtract the converging continuous term \(m\int\chi\,d\mu_i\). As the chosen subnet is cofinal, vague convergence gives
\[
 \int\chi\,d\nu\le\int\chi\max(f_{i_0},-m)\,d\mu. \tag{4}
\]
Restrict \(i_0\) to the tail above one fixed index, so the truncated functions have a common upper bound on the support of \(\chi\). Equation (3) for the decreasing net in \(i_0\) turns (4) into
\[
 \int\chi\,d\nu\le\int\chi\max(f,-m)\,d\mu.
\]
Let \(m\to\infty\). After subtracting a common bounded upper function on the compact support, ordinary decreasing convergence for the **single** parameter m yields
\[
                     \int\chi\,d\nu\le\int\chi f\,d\mu. \tag{5}
\]
The left side is finite. The right side cannot be \(-\infty\), while the positive part of f is bounded on the support of \(\chi\). Taking \(\chi=1\) on any given compact set proves \(f\in L^1_{\mathrm{loc}}(\mu)\). Equation (5) for all nonnegative compactly supported continuous \(\chi\) proves \(\nu\le f\mu\).

**Proposed action:** an optional self-contained net corollary after Lemma 5.63.3, with the compact-superlevel-set proof above. Do not silently rewrite the sequential original statement; preserve its exact source label and permanent tag. Dependents: any future argument combining *varying positive measures*, *decreasing qpsh weights* and nonsequential directed convergence; this result does **not** supply compactness of a measure net by itself.

## Independently inspected passages, with boundaries

**§5.61: integration over analytic sets.**
File \`docs/sections/positive-current-extension-and-analytic-integration--integration-over-analytic-sets/index.html\`, blob \`4c8c14a1b438c49f4d43f63e9f54ed1756d09b4f\`.
Lemma 5.61.1 source \`demailly-complex-geometry:C265E60E\`, tag \`8C07385777E6\`, lines **7–39**: checked the actual finite generic-projection computation on each analytic branch. On a suitable polydisc and outside the analytic discriminant, a finite proper projection of degree \(q_s\) gives the *exact* pullback-form identity
\[
 \int_{A_{\mathrm{reg}}\cap P_s}\gamma_s
    =q_s\int_{\Delta'_s}\bigwedge_{j=1}^p i\,dw_j\wedge d\bar w_j<\infty.
\]
A fixed real spanning family of decomposable strongly positive constant forms bounds \(\int_{A_{\mathrm{reg}}\cap V}\beta^p\) by a finite sum of these degree-weighted base volumes. This verifies the indicated finite-mass reduction **conditional on the internal finite-local-projection theorem and the measure-zero discriminant input**. Theorem 5.61.2 source \`demailly-complex-geometry:D713D40C\`, tag \`B7EB7069B315\`, lines **41–53**, also uses the pre-existing Skoda–El Mir extension theorem 5.60.3. Its full proof was not re-established here.

**§5.62: normal currents on CR submanifolds.**
File \`docs/sections/normal-currents-on-cr-submanifolds/index.html\`, blob \`f7082582d5ee3c9af0959dead737c752cdc03434\`.
Selected checks: Theorem 5.62.3 source \`demailly-complex-geometry:549E72A6\`, tag \`88C601DA5D62\`, lines **23–46** (annihilating \(\partial g_j\) and \(\bar\partial g_j\) separately, rank \(n-h(x)\)); Lemma 5.62.4 source \`demailly-complex-geometry:3A316F60\`, tag \`403785A5B419\`, lines **49–84** (compactly supported divergence decomposition in a rectangular box); and Theorem 5.62.5 source \`demailly-complex-geometry:526B65FE\`, tag \`2CCAC11D6524\`, lines **87–126** (connected-leaf propagation of local transverse Radon measures). The finite chart-chain argument uses connectedness of leaves and the base countable-basis hypothesis; it was **read and checked at these selected transitions only**, not fully independently certified.

**§5.63: positive currents and varying measures.**
File \`docs/sections/positive-current-coefficient-bounds-and-support-maxima/index.html\`, blob \`cb4c3d4e9d653b216cff05eaf23aafb2a01425ec\`.
Proposition 5.63.2 source \`demailly-complex-geometry:5612DDE6\`, tag \`7ECC0248E832\`, lines **11–43**: checked the four-term Fourier polarization identity underlying the \(2^p\) coefficient bound and the nonnegative-coordinate-weight limiting step; no optimal-constant claim. Theorem 5.63.4 source \`demailly-complex-geometry:A8039435\`, tag \`949B825CA873\`, lines **83–106**: the *smooth-input* compact-support Bedford–Taylor/Stokes positivity step is consistent; its passage to general discontinuous psh functions cites the smooth-decreasing-majorant Lemma 7.31.1, which belongs to the **user-excluded regularization programme and was not inspected**.

**§10.101: balanced forms and movable classes.**
File \`docs/sections/balanced-forms-and-movable-classes/index.html\`, blob \`626cf11270ca02d97f2ea1d784139a2b8a92ef19\`. Lemma 10.101.1 source \`transcendental-positive-cones:F9131705\`, tag \`255F6B93CCE9\`, lines **20–50**: checked the trace-one Aeppli slice, separation of the affine \(dd^c\)-representatives from the strictly positive smooth cone, and closure via \([\omega^{n-1}]\). These steps are conditional on the internally linked compact Kähler \(dd^c\)-lemma; they do not establish its proof. Proposition 10.101.2 source \`transcendental-positive-cones:D37F07A7\`, tag \`8DC16DCAD850\`, lines **53–71**, additionally invokes the positive pluriharmonic pullback theorem 5.66.2. **That heat/regularization proof was not reopened**; only the logic of passing from the claimed pullback positivity to the dual-cone test was inspected. No independent proof of full BDPP duality is claimed.

## Coverage and test ledger

- First selected nonexcluded proof-level pass here: **5.61, 5.62, 5.63, 10.101**; old matrix rows were inventory-only. Other cited locations are context/dependency-only.
- **One new low-severity conditional deduction**, no newly confirmed false theorem and no whole-section certification.
- Formal mathematical validation: the self-contained finite-step Radon/net proof above. No finite arithmetic/symbolic script, project-wide tests/build, formal proof assistant, CI, website publication, main/source/registry/tag modification, merge or new PR.
- Previously logged issues, including historic withdrawn false positives, are unchanged. The whole user-excluded Demailly approximation/regularization, Bergman/L²/OT/multiscale/positivity-loss programme is **deferred-by-user**, never certified here.
