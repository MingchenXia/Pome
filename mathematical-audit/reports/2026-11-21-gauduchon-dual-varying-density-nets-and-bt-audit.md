# Varying-density Gauduchon dual maximizers; direct review of three integrated sections

**Date:** 2026-11-21. **Main SHA reviewed:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. All documentation below concerns the integrated Pome reading edition, not source manuscripts. The exclusion of Demailly approximation/regularization and the dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme is respected throughout. Older findings there remain **deferred-by-user**, not resolved or certified.

## Exact reviewed files and source tags

| Scope | Main file | Blob SHA / mathematical lines | Stable source/permanent statement tags |
|---|---|---|---|
| **Whole §7.9** | \`docs/sections/bedford-taylor-products-and-local-capacity--the-ball-dirichlet-problem-with-continuous-density/index.html\` | \`ff1d5dfff1913156b45875eabf921f60af553b99\`, **7–155** | §7.9.1 \`foundations-of-pluripotential-theory:89405657\`/\`0FF4AFFE0ED0\`; §7.9.2 \`69935D4D\`/\`A092925717E1\`; Eq. 7.9.3 \`0390D064\`/\`B8751A529320\` |
| **Whole §7.12** | \`docs/sections/bedford-taylor-products-and-local-capacity--mixed-products-for-a-common-measure/index.html\` | \`e33955e433d3d863f053dc34ed3ed38b3397671f\`, **7–125** | §7.12.1 \`foundations-of-pluripotential-theory:046CCCD5\`/\`AAD1BC0CC6C4\`; §7.12.6 \`D5C83406\`/\`0B504335901F\`; §7.12.8 \`02D188DC\`/\`7071C55A0E4E\` |
| **Whole §12.7** | \`docs/sections/a-gauduchon-variational-volume--a-compact-dual-problem-over-gauduchon-currents/index.html\` | \`1c0f7efb92914b8a55754bd5039d7319392fb03b\`, **7–105** | §12.7.2 \`non-kahler-pluripotential-theory:EF340E54\`/\`FB6C2382E066\`; §12.7.3 \`B931D275\`/\`0537569F9F52\` |

**Selected-input checks only:** Chapter 12.1 states that X is connected and compact; Proposition 11.23.2 (permanent \`0B0003A3A873\`) supplies the adjoint Fredholm compatibility; Proposition 11.33.2 (permanent \`2770AB03C0D2\`) supplies the normalization Lipschitz estimate; Lemma 12.8.1 (permanent \`47843166E777\`) already treats fixed-density *sequential* determinant-measure convergence. These are not counted as full-section reviews.

## POME-GAUDUCHON-DUAL-MAXIMIZER-VARYING-DENSITY-NETS-001: low / verified conditional deduction

**Assumptions.** Let X be a connected compact complex manifold, n>=2, with Hermitian form \(\omega\) and smooth positive probability volume form \(dV\). Let \(\mathscr G_\omega\) be the weakly compact set of positive \(dd^c\)-closed \((n-1,n-1)\)-currents T satisfying \(\int_X\omega\wedge T=1\), as in §12.7 lines 10–26. Define
\[
\sigma_T=\omega\wedge T,\qquad
a_T=(\det P_T)^{1/n},\qquad
f_F=\left(\frac{e^F dV}{\omega^n}\right)^{1/n},\qquad
D_F(T)=\int_X f_F a_T\,d\sigma_T,
\]
\[
M(F)=\max_{T\in\mathscr G_\omega}D_F(T),\quad
\mathscr M(F)=\{T\in\mathscr G_\omega:D_F(T)=M(F)\},
\quad\Gamma_F(T)=f_Fa_T\sigma_T.
\]
Since \(\sigma_T\) is a probability measure and \(\operatorname{tr}P_T=n\) almost everywhere, the matrix arithmetic–geometric mean gives \(0\le a_T\le1\).

**1. Uniform perturbation bound.** For all continuous real F,G,
\[
\boxed{\sup_{T\in\mathscr G_\omega}|D_F(T)-D_G(T)|
\le \|f_F-f_G\|_\infty,\qquad
|M(F)-M(G)|\le \|f_F-f_G\|_\infty.}
\tag{1}
\]
Indeed, the first difference is at most
\(\int_X |f_F-f_G|a_T\,d\sigma_T\le\|f_F-f_G\|_\infty\),
and taking maxima proves the second inequality. This gives *uniform* convergence of the dual objectives as F converges uniformly; one need not first invoke a choice of optimizer.

**2. Upper hemicontinuity for arbitrary directed nets of approximate optimizers.** Let \(F_\alpha\to F\) uniformly for an arbitrary directed index set, and \(T_\alpha\in\mathscr G_\omega\) satisfy
\[
D_{F_\alpha}(T_\alpha)\ge M(F_\alpha)-\epsilon_\alpha,
\quad\epsilon_\alpha\ge0,\quad\epsilon_\alpha\to0.
\]
Putting \(\delta_\alpha=\|f_{F_\alpha}-f_F\|_\infty\to0\), (1) gives
\[
M(F)-2\delta_\alpha-\epsilon_\alpha
\le D_F(T_\alpha)\le M(F).
\tag{2}
\]
Let a subnet \(T_{\alpha_\beta}\) converge weakly to T (compactness of \(\mathscr G_\omega\)); by Lemma 12.7.2's weak upper semicontinuity,
\(D_F(T)\ge\limsup_\beta D_F(T_{\alpha_\beta})=M(F)\),
so \(T\in\mathscr M(F)\). Moreover for every weakly open neighborhood U of the entire compact \(\mathscr M(F)\), eventually \(T_\alpha\in U\): otherwise choose a subnet in the compact closed set \(\mathscr G_\omega\setminus U\), then a convergent subnet with a cluster point outside U, contradiction. If \(\mathscr M(F)=\{T_F\}\), it follows that the **whole net** \(T_\alpha\rightharpoonup T_F\). The uniqueness assertion in Theorem 12.7.3 applies when F is smooth, even though every approximating \(F_\alpha\) may be only continuous.

**3. Joint determinant-measure convergence.** If a subnet \(T_{\alpha_\beta}\rightharpoonup T\), then
\[
\boxed{\Gamma_{F_{\alpha_\beta}}(T_{\alpha_\beta})
\rightharpoonup \Gamma_F(T).}
\tag{3}
\]
First,
\(\|\Gamma_{F_\alpha}(T_\alpha)-\Gamma_F(T_\alpha)\|_{\rm TV}
\le\delta_\alpha\).
The fixed-F masses \(\Gamma_F(T_{\alpha_\beta})(X)=D_F(T_{\alpha_\beta})\)
converge to \(M(F)=D_F(T)\) by (2).
For any real \(h\in C(X)\), choose \(c>0\) such that \(1\pm ch>0\).
Because \(f_{F+n\log(1\pm ch)}=(1\pm ch)f_F\), Lemma 12.7.2 gives
\[
\limsup_\beta\int_X(1\pm ch)\,d\Gamma_F(T_{\alpha_\beta})
\le\int_X(1\pm ch)\,d\Gamma_F(T).
\]
Subtracting the convergent total masses, the two signs give complementary upper and lower limits of \(\int h\,d\Gamma_F(T_{\alpha_\beta})\); these limits agree. Hence fixed-F measures converge weakly, and the total-variation perturbation proves (3). If F has a unique maximizer, the same argument holds for the whole net, with no subnet selection. **No sequential compactness is presumed.**

**Novelty relative to recorded content.** Lemma 12.8.1 treats **fixed F, exact maximizer mass, and sequences**. This finding treats **varying F, approximate maximizers, arbitrary nets, and joint variation of determinant measures**. It does not purport to correct or supersede §12.8.1.

**Dependencies and classification.** The use of weak compactness (§11.7), the determinant infimum and upper semicontinuity (§12.7.2), smooth Hermitian equation and adjoint uniqueness (§§12.2.3, 11.23.2) is explicit. Formulae (1)–(3) are proven conditional on those printed inputs; their full transitive proof chains are *not* independently certified. This is a **verified conditional deduction**, severity **low**, not a false theorem, proof gap or a duplicate. Proposed eventual placement is a *separately reviewable* remark after Theorem 12.7.3 or Lemma 12.8.1, with possible use in §§12.8–12.10. No production or registry patch was made.

## Other direct checks, precise status

**§7.9 (all lines 7–155).** Lemma 7.9.1's linear trace bound and viscosity max argument (17–35); scaling and finite-max Perron argument (58–68); automorphism Jacobian factor \(|J|^{2/n}\), \(C^2\) symmetrization, and semiconcavity estimate (70–110); Alexandrov \(C^{1,1}\) Hessian, strict quadratic bump and locality of max gluing (112–128); radius-\(R^2\) stability, smooth approximation, Bedford–Taylor uniform-limit convergence and comparison uniqueness (130–154). No new confirmed printed error. The **2026-11-04** sharp constant/root exponent finding was selected earlier and is **not** re-counted. The §7.3 comparison and §7.7 automorphism estimates remain upstream dependencies.

**§7.12 (all lines 7–125).** Hölder and Radon integrability (28–35); compactly supported submeasures, decreasing \(E_0\) solutions and strict test by \(\epsilon\rho\) (37–55); common-grid cube averaging, the exact \(c_n=n!\pi^{-n}\) cancellation, weak mixed-product limits and possibly singular \(\mu\) (57–81); local barriers and Borel localization (83–89); mixed repeated factors/binomial formula (94–125). No new confirmed printed error. The §7.11.5/.30/.38 approximants and §7.3.7 decreasing-continuity results remain **unverified transitive** prerequisites.

**§12.7 (all lines 7–105).** Trace/determinant normalization (13–35); matrix variational formula, Lusin field approximation and weak upper semicontinuity (38–65); smooth maximizing-current equality and adjoint scalar elliptic uniqueness, approximation of continuous F (73–105). No new confirmed printed error. Existence/compactness inputs remain conditional.

**Accounting:** three whole current integrated mathematical sections directly reviewed, four selected scope/statement prerequisites, **zero** fully certified upstream proof chains, **zero** newly confirmed printed errors. Retain all existing confirmed/resolved/unresolved findings. All user-excluded work stays **deferred-by-user**, not certified. No tests, builds, CI, website publication or main/source/registry/canonical/tag changes.
