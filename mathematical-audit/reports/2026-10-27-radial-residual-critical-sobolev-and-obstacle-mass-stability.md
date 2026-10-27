# 2026-10-27 — Critical Sobolev regularity of radial Monge–Ampère residuals and sharp obstacle-mass stability

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Scope:** first selected nonexcluded proof-level passages of §§11.46–11.47 (radial inverse / convex obstacle), and independent selected checks in §9.49 (convex neighborhoods of analytic subspaces). The formulas below are conditional on the exact integrated source statements identified below. No complete section or transitive analytic/coherence dependency chain is certified; neither finding alleges a false printed theorem. Dedicated Demailly approximation/regularization and Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss work are excluded by the author, not addressed or resolved here.

## POME-RADIAL-RESIDUAL-CRITICAL-SOBOLEV-001

**Status / severity:** verified conditional deduction / low.
**Proposed action:** add an optional quantified regularity-and-sharpness corollary after §11.46.17; do not change Theorem 11.46.8 or its stated derivative thresholds.
**Integrated anchors:** docs/sections/normalization-and-weak-adjoint-measures--residual-regularity-in-radial-singularity-types/index.html; main blob 2b3580e24274771d63446a63973adfd55402892a; source variant non-kahler-pluripotential-theory. Reference profile Lemma 11.46.2 tag 3CE4F16CE935 lines 20–58; inverse Theorem 11.46.8 tag F273E69013C1 lines 66–127; its derivative equation (11.46.10) tag 96AA5EC1C8FC lines 76–81; exact flux (11.46.11) tag FEE50B8F4491 lines 87–116; sharpness Proposition 11.46.17 tag F4F876167D51 lines 173–202, including model density (11.46.18) tag 405FC6263C95 lines 179–199.

**Statement.** Under exactly the hypotheses of Theorem 11.46.8, suppose 0<δ<1 in its relative-density bound, and write R=U-u_α for the residual, canonically extended over the pole o. For complex dimension k≥2, put
\[
p_*=\frac{k}{1-\delta}.
\]
Then
\[
\boxed{R\in W^{2,p}_{\mathrm{loc}}\text{ at }o\quad\text{for every }1\le p\le p_* .}
\]
The *endpoint is included*. For every p>p_* there are normalized positive smooth-off-the-pole radial densities obeying the same relative-error bound for which R is **not** in W^{2,p} on any neighborhood of o. Thus the universal second-Sobolev-derivative exponent is sharp, including its logarithmic endpoint. If δ≥1 instead, the printed estimates give R∈W^{2,\infty}_{loc} and, in fact, the stated C² extension with zero Hessian at o.

There is also a sharp intermediate Hölder consequence not made explicit by the printed theorem: for 1/2<δ<1,
\[
\boxed{R\in C^{1,\,2\delta-1}_{\mathrm{loc}}\text{ at }o,}
\]
and a larger exponent cannot be guaranteed. At δ=1/2 the printed C¹ extension is valid, but no positive C^{1,β} exponent can be guaranteed from its pointwise density assumption alone. These claims require **no bounds on derivatives of** q/q_α.

**Upper Sobolev proof, including the distributional issue.** Theorem 11.46.8 supplies, with r=|z|², L=1-\log r and 0<r≪1,
\[
|R'(r)|\le Cr^{\delta-1}L^{\alpha-2},
\qquad
|R''(r)|\le Cr^{\delta-2}L^{\alpha-2},
\qquad
|R(r)-R_0|\le Cr^\delta L^{\alpha-2}.
\]
In real coordinates \(\rho=|z|\), the radial Hessian formula
\[
D^2 R=2R'(r)I+4R''(r)\,z\otimes z
\]
(up to the usual identification of the radial real unit vector) shows
\[
|D^2R(z)|\le C\rho^{2\delta-2}(1+|\log\rho|)^{-(2-\alpha)}.
\]
The local L^p norm is controlled by
\[
C\int_0^{\rho_0}
\rho^{2k-1-p(2-2\delta)}
(1+\log(1/\rho))^{-p(2-\alpha)}\,d\rho.
\]
For p<p_* the power is strictly larger than -1; at p=p_* it equals -1, but the logarithm is integrable because p_*(2-\alpha)>1 (indeed k≥2, 0<α<1). This proves classical Hessian integrability off the pole.

There is no hidden point-supported distributional second derivative. Integrating by parts on {|z|>ε}, the boundary term in passing from the classical gradient to the distributional Hessian is bounded by a constant times
\[
\epsilon^{2k-1}\sup_{|z|=\epsilon}|\nabla R|
\le C\epsilon^{2k+2\delta-2}(1+|\log\epsilon|)^{-(2-\alpha)}\longrightarrow0.
\]
The analogous first-derivative boundary term is even smaller because R is continuous. Therefore the weak Hessian is the classical one extended as a function, and R genuinely belongs to W^{2,p}. For δ≥1 the same pointwise Hessian bound is locally bounded, and tends to zero at the pole.

**Sharpness of p_*.** Use exactly the probability-density perturbation q_c in printed (11.46.18): q_c=q_α[1+c(r^δχ_0-Bχ_1)] with disjoint cutoffs and sufficiently small c>0. The compensation term leaves the central flux unchanged for small r. Proposition 11.46.17, lines 187–199, obtains
\[
R_c'(r)\sim \frac{c\alpha(1-\alpha)}{\delta}
r^{\delta-1}L^{\alpha-2}.
\]
On each small punctured sphere, a real tangent vector orthogonal to the radial direction has Hessian eigenvalue 2R_c'(r). Hence |D²R_c| has a corresponding positive lower bound. The p-th Hessian integral diverges for p>p_* because then the radial power is strictly less than -1; the logarithmic decay cannot overcome this power divergence. The same model *does* attain the critical p_* because the logarithm is integrable there. No new PDE existence input is introduced beyond the stated radial inverse.

**Intermediate Hölder proof and sharpness.** For 1/2<δ<1, put β=2δ-1∈(0,1). The bounds on ∇R and D²R read
\[
|\nabla R(z)|\le C|z|^\beta (1+|\log|z||)^{-(2-\alpha)},\quad
|D²R(z)|\le C|z|^{\beta-1}(1+|\log|z||)^{-(2-\alpha)}.
\]
Since ∇R(0)=0, compare any two points z,w a distance h apart. If min(|z|,|w|)≤2h, both gradients are O(h^β). Otherwise the segment stays a distance ≥h from the origin, so integrating the Hessian bound yields O(h·h^{β-1})=O(h^β). The exact q_c model has |∇R_c(z)| asymptotic to a positive constant times |z|^β(1+|\log|z||)^{-(2-\alpha)} along any radial ray, which is not O(|z|^γ) for γ>β. At δ=1/2 this gradient is asymptotic to a positive multiple of the logarithmic factor alone, so it tends to zero but is not Hölder of any positive exponent. This refines—not refutes—the printed C¹ threshold and sharpness statement.

**Affected dependents:** residual regularity in degenerate radial Monge–Ampère equations; finite-energy and singular-model examples where a bound in W^{2,p} is needed; endpoint Schauder/Sobolev comparison. The integrated inverse Theorem 11.46.8, explicit normalized q_c model and local radial coordinates are the conditional upstream inputs; no general nonradial regularity is inferred.

## POME-RADIAL-OBSTACLE-KOLMOGOROV-SHARPNESS-001

**Status / severity:** verified conditional deduction / low.
**Proposed action:** optional sharp quantitative weak-measure stability corollary after §11.47.11, keeping the statement explicitly weaker than total-variation stability.
**Integrated anchors:** docs/sections/normalization-and-weak-adjoint-measures--envelopes-for-singular-radial-obstacles/index.html; main blob 6b7ce2bc15721b43ea2b2294294cfcca84be2ff3; source variant non-kahler-pluripotential-theory. Convex reference Lemma 11.47.2 tag 3CD979065654 lines 26–40; minorant envelope Theorem 11.47.5 tag 7444FA94A222 lines 55–104; curvature bound (11.47.6) tag 7B822F7684AE lines 60–82; mass and sup-norm Corollary 11.47.8 tag EA98BEE991F7 lines 106–122, including (11.47.9) tag 2FE2F9FAF60D; uniform C^{1,1} Theorem 11.47.11 tag 278AD9E56CEA lines 130–184.

**Statement.** Fix the dimensions and reference data in §11.47, a<b, M>0, and F,G∈\(\mathcal F_{a,b,M}\). Let μ_F be the probability measure on \(\mathbb R\) obtained by pushing the non-pluripolar measure MA_κ(E_F) forward under x=log|z|² away from the pole and hyperplane (both have zero mass). Set
\[
\delta=\|F-G\|_\infty,\qquad
L_*=\|A''\|_\infty+M>0.
\]
Then
\[
\boxed{
\sup_{x\in\mathbb R}
\left|\mu_F((-\infty,x])-\mu_G((-\infty,x])\right|
\le \min\{1,\,2k\sqrt{2L_*\delta}\}.
}
\]
The universal square-root exponent 1/2 is optimal even when both obstacles are C^\infty, both total profiles A+F and A+G remain strictly convex, and no noncontact/free interval occurs. This is a **Kolmogorov (CDF) bound**, not a bound on total-variation distance between the measures.

**Proof.** By the order and translation properties of the greatest convex minorant,
\[
\|C_F-C_G\|_\infty\le\delta.
\]
Theorem 11.47.5 gives monotone, globally L_*-Lipschitz derivatives C_F' and C_G', since \(0\le C_F''\le \sup(g_F'',0)\le L_*\) almost everywhere and similarly for G. Therefore D=C_F-C_G has |D|≤δ and D' is 2L_*-Lipschitz. For arbitrary h>0, the first-order increment with Lipschitz remainder yields
\[
|D'(x)|\le \frac{2\delta}{h}+L_*h.
\]
Take \(h=\sqrt{2\delta/L_*}\) (and use D≡0 for δ=0), giving
\[
\|C_F'-C_G'\|_\infty\le 2\sqrt{2L_*\delta}.
\]
Corollary 11.47.8 and the zero mass of both endpoints give the exact cumulative distribution
\[
\mu_F((-\infty,x])=C_F'(x)^k.
\]
Both derivatives lie in [0,1], so \(|s^k-t^k|\le k|s-t|\). Combining proves the displayed inequality; the trivial probability bound supplies the minimum with 1. This argument does not interchange any unproved limit of general currents.

**Sharpness.** Choose an interior \(x_0\in(a,b)\) and \(\phi\in C_c^\infty((-1,1))\) with \(\phi'(0)\ne0\). Since A is strictly convex, \(m_0=\min_{[x_0-\eta,x_0+\eta]}A''>0\) for a small fixed η>0. Choose c>0 small enough that \(c\|\phi''\|_\infty<m_0/2\) and \(c\|\phi''\|_\infty<M/2\). For small ε>0 put
\[
F_\epsilon(x)=c\epsilon\,\phi((x-x_0)/\sqrt\epsilon),
\qquad G=0.
\]
These smooth functions belong to the same fixed \(\mathcal F_{a,b,M}\); they satisfy \(\|F_\epsilon\|_\infty\asymp\epsilon\), \(\|F_\epsilon''\|_\infty\le c\|\phi''\|_\infty\), and \(A+F_\epsilon\) is globally convex. Thus the convex minorant is simply \(C_{F_\epsilon}=A+F_\epsilon\), whereas \(C_0=A\). At x_0,
\[
C_{F_\epsilon}'(x_0)-C_0'(x_0)
=c\sqrt\epsilon\,\phi'(0),
\]
and therefore
\[
\mu_{F_\epsilon}((-\infty,x_0])-\mu_0((-\infty,x_0])
=kA'(x_0)^{k-1}c\phi'(0)\sqrt\epsilon+O(\epsilon).
\]
Because \(A'(x_0)>0\), its magnitude is bounded below by a fixed positive multiple of \(\sqrt{\|F_\epsilon\|_\infty}\). This excludes every uniform exponent greater than 1/2 for the specified bounded-C² obstacle class. Notice that the construction needs no contact-set topological transition, so such transitions cannot be blamed for the sharp exponent.

**Nonclaim:** no total-variation continuity follows from the CDF bound. The previously registered general weak-versus-total-variation obstruction (POME-MA-DOMINATED-WEAK-NOT-TV-001) remains a separate earlier finding and is not repeated as new progress. The present result is precisely a sharp rate in the radial non-pluripolar mass distribution, using the actual §11.47 derivative bounds and exact radial flux formula.

**Affected dependents:** radial obstacle selection, quantitative weak convergence of equilibrium measures, contact-set perturbations and mass transport. General nonradial obstacle envelopes and their total-variation distances are not covered.

## Additional independent coverage: convex neighborhoods on singular analytic spaces

**Newly selected direct proof passages, with no additional finding ID:** §9.49 in docs/sections/convex-neighborhoods-and-coherent-vanishing--convex-functions-near-analytic-subspaces/index.html, main blob 9e940da0044eb3d6f16b470c0db81106506c93eb, source variant demailly-complex-geometry. Lemma 9.49.1 tag DD53C11960A9 lines 10–33: nonnegative ambient partitions and same-positive-subspace rule, not an unrestricted sum of q-convex functions. Lemma 9.49.2 tag 71E35F5F0916 lines 37–71: the frame-normalized \(H_\xi\log(h^*Hh)\) inequality and local uniform lower Levi bound. Lemma 9.49.3 tag 339FB068D13D lines 75–84: locally stationary dimension stratification. Proposition 9.49.4 tag DBED5041C4 lines 87–154: exact normal Gram term \(\theta_\lambda\epsilon_\lambda^{-1}(dw_\lambda)^*dw_\lambda\), small negative cutoff error, and compact-locally-finite parameter choice. Theorem 9.49.8 tag 9EBE244C8709 lines 157–198: logarithmic barrier composition and compactness of sublevel sets. Selected computations and local dimension inequalities are consistent on this pass; this does not certify analytic ideal coherence or the full transitive proof of all strongly q-convex neighborhood theorems. No previous compact-submanifold obstruction is counted again.

As contextual comparison only, §7.31.2–4, docs/sections/classical-products-with-controlled-unbounded-loci--collars-relative-to-the-support-of-the-base-current/index.html, blob 86de377d6e6f17fc1a08a6e789a681ddfaabfac5, lines 27–77, was read for the relative-support collar and compact-current-difference arguments. Its reliance on the smoothing Lemma 7.31.1 (tag FDDB630F0AA9) was recorded, **not re-audited**; no coverage upgrade or claim of independent proof certification for §7.31 is made.

## Verification boundary and ledger disposition

This report establishes two new *conditional deductions* from the identified integrated radial theorems, with explicit normalized sharpness families and the distributional Sobolev endpoint justified. It detects no new false printed mathematical theorem and repairs no published body. Three previously inventory-only ToC rows (§§9.49, 11.46, 11.47) receive selected proof-level status only; the existing 747 unique ToC rows and all prior unresolved/resolved/deferred ledger statuses are retained unchanged. Neither project builds nor Python/JavaScript tests, CI, browser checks, formalization or website publication were performed. All work concerns public integrated reading-edition content and contains no private source scan or unpublished research document.