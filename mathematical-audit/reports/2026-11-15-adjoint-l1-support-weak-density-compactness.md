# Bounded-L1 perturbations and weak-L1 compactness of supporting densities

**Date:** 2026-11-15. **Stable ID:** POME-ADJOINT-L1-SUPPORT-UNIFORM-INTEGRABILITY-001.
**Severity:** low. **Status:** verified conditional deduction, not a false printed theorem or a completed source repair.

## Pinned integrated content

Reviewed main SHA: b6933b772f41b45918f7e25ed1afbbb1fd892272.

- docs/sections/normalization-and-weak-adjoint-measures--the-scalar-functional/index.html; blob fff86de757578ed2be369ba752123f62f3d31044: Theorem 11.33.5, source non-kahler-pluripotential-theory:D502EBBF, permanent tag 5E3583383688, statement physical line 89 and proof lines 93–109. Its bounded-L1 continuity is crucial and is treated as an existing, *not transitively certified*, PDE input.
- docs/sections/normalization-and-weak-adjoint-measures--supporting-probability-measures/index.html; blob a8afa97be049b56b6c7d18302499364022feaa39: inequality (11.34.1), source non-kahler-pluripotential-theory:44A5BEA2, permanent tag 4DA0C1CF8861, physical lines 10–15; Theorem 11.34.2, source :97DE633E, tag 86A7D85266AA, statement line 18 and proof lines 22–49; Proposition 11.34.3, source :AE3FA53A, tag CB2DC1F2B712, statement line 52 and proof lines 56–65. Theorem 11.34.7, source :39E54B6B, tag A4850266BE73, line 102, is a conditional dependent in its singleton-support case.

## New theorem (conditional on the three cited integrated inputs)

Retain the standing assumptions of §11.32: connected compact complex manifold X, smooth positive finite volume dV, fixed admissible model reference φ, scalar B_φ on bounded logarithmic densities, and its supporting probability sets A_φ(F).

Let F_j,F be real continuous functions with sup_j ||F_j||_∞ finite and ||F_j-F||_{L¹(dV)} → 0. For arbitrary ν_j ∈ A_φ(F_j), write ν_j=f_j dV using 11.34.2. Then:

1. The density family is **uniformly integrable**:
   \[
   \lim_{\delta\downarrow0}\sup_j\sup_{dV(E)\le\delta}\nu_j(E)=0.
   \]
2. From every subsequence one can extract a further one on which f_j converges in the Banach-space weak topology σ(L¹(dV),L^∞(dV)) to a nonnegative mass-one f with f dV ∈ A_φ(F).
3. If A_φ(F) is a singleton, the *whole* f_j sequence converges weakly in L¹ to its density.
4. For fixed F the entire set A_φ(F), identified with its densities, is weakly compact in L¹, with a common implicit absolute-continuity modulus
   \[
   \Omega_F(\delta)=\sup\{B_\varphi(F)-B_\varphi(F+h): h\in C(X),\ 0\le h\le1,\ \int_X h\,dV\le\delta\}.
   \]
   This tends to zero with δ, and ν(E) ≤ Ω_F(δ) for every ν∈A_φ(F), Borel E, and δ>dV(E).

This strictly strengthens printed Proposition 11.34.3: *bounded L¹*, rather than uniform, convergence of the input densities and *weak L¹*, rather than merely narrow, convergence of the supporting probabilities. It does not yield total variation or strong L¹ convergence, or a numerical modulus.

## Complete proof of the new implication

**Uniform integrability.** Suppose the first assertion fails. Then there are ε>0, indices j_k and Borel E_k with dV(E_k)→0 but ν_{j_k}(E_k)≥ε. Each fixed ν_j is absolutely continuous by 11.34.2, hence the indices can be chosen to tend to infinity. By inner regularity choose compact K_k⊂E_k of ν_{j_k}-mass at least ε/2. By outer regularity of dV and normality of compact X choose continuous 0≤h_k≤1, equal to one on K_k, with ∫h_k dV→0. Apply the supporting inequality (11.34.1) at F_{j_k} to G=F_{j_k}+h_k:
\[
 B_\varphi(F_{j_k}+h_k)\le B_\varphi(F_{j_k})-\int h_k\,d\nu_{j_k}
 \le B_\varphi(F_{j_k})-\varepsilon/2.
\]
Both F_{j_k} and F_{j_k}+h_k remain uniformly bounded and converge to the *same* F in L¹(dV). Theorem 11.33.5 forces both scalar values to converge to B_φ(F), contradicting the gap ε/2.

**Closedness of the support relation under L¹ perturbations.** Compact metrizability of X gives a narrowly convergent further subsequence ν_j→ν. Uniform integrability implies ν≪dV: for a null compact K and an open U⊃K of arbitrarily small volume, Portmanteau gives ν(K)≤ν(U)≤liminf_j ν_j(U), and the common small-set modulus makes this arbitrarily small. Write ν=f dV. For every η>0, with M bounding |F_j| and |F|,
\[
\int|F_j-F|\,d\nu_j\le\eta+2M\,\nu_j\{|F_j-F|>\eta\}.
\]
Chebyshev gives dV{|F_j−F|>η}→0, so uniform integrability makes the second term vanish; then η→0 proves the integral goes to zero. In the defining support inequality
\[
B_\varphi(G)\le B_\varphi(F_j)-\int_X(G-F_j)\,d\nu_j\qquad(G\in C(X))
\]
the scalar term converges by 11.33.5, the fixed G term by narrow convergence, and the varying F_j term by the preceding estimate. Thus ν∈A_φ(F).

**Weak L¹ convergence.** Fix any q∈L^∞(dV). By regularity/Lusin approximation there are continuous q_m, uniformly bounded by ||q||∞, converging to q in L¹(dV). Splitting into |q_m−q|≤η and its complement, Markov's inequality plus uniform integrability gives
\[
\lim_{m\to\infty}\sup_j\int|q_m-q|\,d\nu_j=0.
\]
The limit ν inherits the same small-set bound and satisfies the analogous estimate. Since ∫q_m dν_j→∫q_m dν for continuous q_m, first let j→∞ and then m→∞ to obtain ∫q dν_j→∫q dν for *every* bounded measurable q. This is exactly σ(L¹,L^∞) convergence of f_j. If A_φ(F) is a singleton, a subsequence contradiction for each fixed q proves convergence along the whole original sequence.

**Fixed-F modulus and weak compactness.** If Ω_F(δ) did not tend to zero, take continuous 0≤h_k≤1 of vanishing L¹(dV) norm but with B_φ(F)−B_φ(F+h_k) bounded away from zero, contradicting 11.33.5. For a supported ν the same support inequality yields ∫h dν ≤ B_φ(F)−B_φ(F+h). Given E and δ>dV(E), use inner regularity for ν, outer regularity for dV, and a continuous cutoff equal to one on a compact K⊂E with ∫h dV<δ. Let ν(K)↑ν(E) to obtain ν(E)≤Ω_F(δ). This bound holds for *all* ν in A_φ(F). Its narrow compactness from 11.34.2 and the weak-L¹ upgrade above yield weak-L¹ compactness of the densities: the density map from the compact metrizable narrow space is sequentially continuous into weak L¹, hence continuous and has compact image.

## Why ordinary narrow compactness is insufficient

On the unit circle with normalized Lebesgue measure, let
\[
 E_N=\bigcup_{k=0}^{N-1}[k/N,k/N+1/N^2),\qquad f_N=N\mathbf1_{E_N}.
\]
Then ∫f_N=1, |E_N|=1/N, and ∫_{E_N}f_N=1. Nevertheless f_N dx→dx *narrowly* by Riemann sums. Thus the narrowly compact family consisting of these absolutely continuous measures and their absolutely continuous limit is **not uniformly integrable**. The new proof genuinely needs bounded-L¹ scalar continuity 11.33.5, not simply the conclusions of 11.34.2.

## Status, dependencies, suggested patch and actual coverage

Status **verified conditional deduction**; no incorrect original statement is claimed. The printed 11.34.2, 11.34.3 and 11.34.7 are unaffected. Proposed *separately reviewable*, not implemented, source addition: a bounded-L¹ strengthening immediately following 11.34.3, with the implicit modulus and precisely the hypotheses above.

The 11.33.5 proof invokes the PDE barriers and convergence of §§15.12.3 and 15.9.4, which have **not** been independently reverified here; the global nonlinear PDE conclusion is conditional. Elementary regularity, compactness and continuous approximation of measures are the other inputs. Affected uses are the support-map/singleton criteria of §§11.34–11.38. The Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion programme remain **deferred-by-user**, neither opened nor certified.

Actual new scope: the exact 11.33.5 L¹-continuity quantifier and 11.34.1–.3 support inequality/absolute-continuity logic checked together, plus a new complete conditional deduction. These numbered sections were **previously partly visited**: +0 first-visited sections and +0 fully certified sections. Actual ToC 25 chapters/747 numbered sections. No main, source text, registry or permanent tag edited; no project build, test suite, GitHub Actions CI or website publication.
