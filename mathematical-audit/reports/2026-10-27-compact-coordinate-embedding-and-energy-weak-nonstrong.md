# Mathematical audit — 2026-10-27: compact-coordinate embeddings and energy weak/strong separation

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Audit branch before report:** 228abedaaea2ac833f281ee60f65a11711cc3eaf.
All claims below concern the actual integrated Pome reading edition. No source, registry, tag, website, or main-branch edits are proposed or made. All dedicated Demailly approximation/regularization, Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion work remains **deferred-by-user** and unexamined.

## POME-COMPACT-CHART-EMBEDDING-BILIPSCHITZ-001

**Severity:** low. **Status:** verified conditional deduction; **not** an error or repair of the printed lemma.

**Exact source:** docs/sections/complex-differential-forms-and-positive-currents--complex-manifolds-and-differential-forms/index.html, main blob 886a687d5029616950683fe55defce1fe6854b12; Lemma 5.2.7, permanent tag 98494B0CCC31, original source foundations-of-pluripotential-theory:C99D5F6B, physical lines 153–174, especially 163–171. The lemma constructs a continuous, injective smooth map F into Euclidean space using coordinate cutoffs, and establishes topological embedding.

**Stronger claim.** The SAME map
\[
F=(\chi_1,\ldots,\chi_k,\chi_1\kappa_1,\ldots,\chi_k\kappa_k):X\longrightarrow\mathbb R^{k+2nk}
\]
is a smooth embedding. For connected compact X endowed with any smooth Riemannian metric g, the extrinsic chord metric \(d_F(x,y)=|F(x)-F(y)|\) and intrinsic Riemannian distance \(d_g\) are **globally bi-Lipschitz equivalent**:
\[
0<c\,d_g(x,y)\le |F(x)-F(y)|\le C\,d_g(x,y)
\]
for all distinct x,y, with constants depending on the chosen data. For a disconnected compact X, apply the statement separately to each component; do not compare distinct components by an infinite geodesic distance.

**Proof.** The printed construction supplies an open finite cover by W_i on which \(\chi_i=1\) and \(\kappa_i\) is a coordinate chart. Consequently, the \(i\)-th \(2n\)-dimensional block of F is \(\kappa_i\) throughout W_i and \(dF_x\) has full real rank \(2n\) for each \(x\in W_i\). The original proof establishes that F is a homeomorphism onto F(X). Thus F is an injective immersion and a smooth embedding.

On connected X let \(C=\sup_X\|dF\|_g\), finite by compactness. Integrate dF along a minimizing g-geodesic to get \(d_F\le C d_g\). For the lower bound select finitely many smaller coordinate balls V_i, with convex images, closures inside regions \(\chi_i=1\), covering X. On each such ball the metric tensor is bounded above by \(A_i\) times the coordinate Euclidean tensor. If x,y belong to V_i, their coordinate straight segment stays inside V_i and
\[
d_g(x,y)\le\sqrt{A_i}|\kappa_i(x)-\kappa_i(y)|\le\sqrt{A_i}\,d_F(x,y).
\]
A Lebesgue number \(\delta>0\) of the finite V_i cover gives this estimate uniformly whenever \(d_g(x,y)<\delta\). On the compact set \(d_g(x,y)\ge\delta\), injectivity implies a positive minimum \(m_\delta\) for d_F; since \(\mathrm{diam}_gX=D<\infty\), there \(d_F\ge(m_\delta/D)d_g\). Combine regimes. The connected zero-dimensional case (a singleton) is trivial. No Whitney embedding theorem, approximation lemma, or unproved limit interchange was used.

**Proposed disposition and dependents.** Add an optional corollary after Lemma 5.2.7 to justify quantitative comparisons involving the Euclidean embedding metric on compact manifolds. The printed weaker lemma is correct. Its cutoff input Proposition 5.2.6 was inspected in the selected reading text but the entire topology chain was not transitively certified.

## POME-GREEN-ENERGY-WEAK-NONSTRONG-SPHERES-001

**Severity:** low. **Status:** verified conditional deduction; **not** a false theorem or proof repair.

**Exact source:** docs/sections/green-energy-and-martin-boundaries/index.html, main blob 976a90f2a5eba299658f73a1eee8b9d3fef8020f; Theorem 4.5.4, permanent tag CE0D5F4DF7B2, original source classical-potential-theory:5FB19CB2, physical lines 46–68; neighboring Example 4.5.5, tag 61A5D2A82793, source classical-potential-theory:898691BF, lines 70–73. The printed theorem correctly equates **vague** and **weak energy** convergence for energy-bounded positive sequences. It does not assert strong convergence from those premises.

**Explicit sharpness model.** On \(\Omega=\mathbb R^3\), use the Newton kernel \(G(x,y)=|x-y|^{-1}\) and let \(\sigma_r\) be the uniform probability on the sphere S_r of radius r. The shell theorem gives
\[
G\sigma_r(x)=\frac1{\max\{r,|x|\}},\qquad
I(\sigma_r)=\frac1r,\qquad
I(\sigma_r,\sigma_s)=\frac1{\max\{r,s\}}.
\]
Take \(r_j=4^{-j}\) and \(\mu_j=\sqrt{r_j}\,\sigma_{r_j}\). Each \(\mu_j\) is positive and has finite energy, while
\[
\mu_j(\mathbb R^3)=2^{-j},\qquad
I(\mu_j)=1,\qquad
I(\mu_j,\mu_k)=2^{-(k-j)}\quad(k>j),
\]
and therefore
\[
\|\mu_j-\mu_k\|_{\mathcal E}^2=2-2^{1-(k-j)}
\quad(k>j),\qquad
\|\mu_j-\mu_{j+1}\|_{\mathcal E}=1.
\]
Total mass tends to zero, so \(\mu_j\to0\) vaguely (even against bounded continuous functions); by Theorem 4.5.4 this energy-bounded positive sequence also converges **weakly in energy** to zero. Nevertheless the energy norm stays exactly one and the sequence is not even strongly Cauchy. This model does **not** contradict completeness of the positive cone.

**Derivation and checks.** Rotational symmetry, harmonicity inside/outside S_r, behavior at infinity, and continuity at radius r yield the displayed shell potential. Integrating it over either normalized sphere proves the energy and cross-energy formulas, and multiplying by the factors \(\sqrt{r_j}\sqrt{r_k}\) proves all pairings. Vague convergence follows directly from \(|\int f\,d\mu_j|\le2^{-j}\|f\|_\infty\), without sequential compactness. The weak-energy assertion is **conditional on the printed Theorem 4.5.4** and is not a claim of its complete upstream proof certification. The normalization agrees with the spherical calculation in Example 4.5.5.

**Proposed disposition and dependents.** An optional example after Theorem 4.5.4 warns arguments in energy/geodesic settings not to replace bounded-energy vague convergence by strong convergence or to infer energy-norm convergence without additional hypotheses. This is *not* the earlier signed-energy incompleteness example in 4.5.5: that example contains a strong-Cauchy sequence without a signed Radon limit, whereas our example remains in the complete positive cone and is never strong-Cauchy. No unproved extension from sequences to arbitrary nets is asserted.

## Other selected checks, no new defect ID

**Foundational normalizations (§5.2).** The printed Proposition 5.2.6 cutoff/Stokes passage and equations 5.2.8–10 were directly compared. With \(\beta=(i/2)\sum dz_j\wedge d\bar z_j\), \(\beta^n/n!=dV_{2n}\), and \(dd^c=(i/2\pi)\partial\bar\partial\), one calculates \((dd^c u)^n=n!\pi^{-n}\det(u_{j\bar k})\,dV_{2n}\). This agrees with the §7.1 introduction. §7.1 was used only for the stated convention, not counted as newly proof-reviewed.

**Multiplier-ideal integral closure, algebraic part only (§6.10).** Directly checked Proposition 6.10.6, tag 675539E4A76C, original source foundations-of-pluripotential-theory:914E443D, physical lines 83–93 of docs/sections/lelong-numbers-and-multiplier-ideals--restriction-products-and-integral-closure/index.html, blob 878526739ee043892cdc85040a280504328b6dea. From \(|a_j|\le C_j|g|^j\) in an integral equation for F, set \(\lambda=|F|/|g|\) where \(|g|>0\). The inequality \(\lambda^d\le\sum_jC_j\lambda^{d-j}\) gives \(\lambda\le\max\{1,\sum_jC_j\}\): for \(\lambda>1\) divide by \(\lambda^{d-1}\). On \(|g|=0\) the same equation forces \(F=0\). Hence \(|F|\le C|g|\) and the direct integrability argument is valid. Its **finite-generation input** from 6.8.9 is not certified. Theorem 6.10.1's OT and Hilbert-space steps, and the dedicated excluded proof-completion programme, were neither opened nor retried.

## Coverage and unresolved boundary

The 747-row actual ToC inventory is unchanged. Two previously inventory-only rows, **§5.2** and **§6.10**, receive *selected passage* coverage only (Lemma 5.2.7, the displayed normalization and cutoff passages; Proposition 6.10.6's algebraic/integrability proof only). §4.5 already had selected audits: its new Theorem 4.5.4 sphere boundary test is an **increment**, not first-time review of the section. No complete section certified. No old finding reclassified, and every excluded Demailly regularization/Bergman/L2/OT/multiscale/positivity-loss item remains **deferred-by-user**. No project builds, tests, GitHub Actions CI, publication, or formal verification were performed.
