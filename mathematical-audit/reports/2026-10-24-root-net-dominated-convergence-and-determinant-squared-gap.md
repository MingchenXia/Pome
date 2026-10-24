# 2026-10-24 — Directed density-root convergence and exact Hermitian determinant-square gaps

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit branch:** 64aa119a69c33891dc59b9b443f5f9a6fc89bb02. Selected integrated proof audit only: §§14.22–14.23 and §§15.29, 15.32. No complete section or upstream PDE existence/stability theorem is certified.

**User exclusion:** All Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof completion remain **deferred-by-user**. This report does not invoke, extend or check those programmes.

## Finding POME-DEGEN-EQUALDET-SQUARE-GAP-001
**Status:** verified conditional deduction; severity low. **Not an error in the printed theorem.**

**Anchors:** Theorem 14.23.1 (source non-kahler-pluripotential-theory-29282980, permanent tag AF9D036E600F); equation 14.23.3 (source non-kahler-pluripotential-theory-9A5C396A, tag CB4E143A2628, lines 37–43); equation 14.23.4 (source non-kahler-pluripotential-theory-0D22D64A, tag 899D523AFD3C, lines 44–54), with Stokes and Sobolev passage lines 56–110. Exact file:
docs/sections/uniqueness-for-degenerate-equations--integral-rigidity-in-dimensions-two-and-three/index.html
at main blob e67714c2fe599f71be40618f9586b6b31095275e.
Context checked: Theorem 14.22.1 (source non-kahler-pluripotential-theory-DC121A4C, tag 919310C73DBE), equation 14.22.10 (tag 7A7369E544A8), and Proposition 14.22.13 (source non-kahler-pluripotential-theory-9858A450, tag F563CACF5D7D), in
docs/sections/uniqueness-for-degenerate-equations--polarized-cofactors-and-propagation/index.html,
blob 56645140ee2a5e1f97f3288e31ad9a48161e73e5, selected lines 14–75, 84–105 and 165–210. The full Hörmander-orbit argument was not re-certified.

**Claim, including all hypotheses:** Let n=2 or n=3, and let A,B be positive definite Hermitian (1,1)-forms on one complex n-dimensional vector space with A^n=B^n. Choose a coframe with A=sum e_i and B=sum lambda_i e_i, where e_i=i theta_i wedge conjugate(theta_i), lambda_i>0, and product lambda_i=1. Write E=e_1 wedge ... wedge e_n, D=A−B, C=(A+B)/2, and
\[
d_{\mathrm{aff}}(A,B)^2=\sum_i(\log\lambda_i)^2.
\]
Then the sign inequalities in (14.23.3) and (14.23.4) have the **exact squared-defect** refinements:
\[
\begin{array}{ll}
 n=2:& -D^2=
  \left[\sum_{i=1}^2(\sqrt{\lambda_i}-\lambda_i^{-1/2})^2\right]E
  \geq d_{\mathrm{aff}}(A,B)^2 E,\\[3pt]
 n=3:& -2C\wedge D^2=
  2\left[\sum_{i=1}^3(\sqrt{\lambda_i}-\lambda_i^{-1/2})^2\right]E
  \geq 2d_{\mathrm{aff}}(A,B)^2 E.
\end{array}
\]
The zero defect occurs if and only if A=B. The inequalities are pointwise and do not assert global stability for unequal determinant densities or on the set where the common determinant is zero.

**Full proof:** In n=2, A²=B²=2E and A wedge B=(lambda_1+lambda_2)E, so -D²=2(lambda_1+lambda_2−2)E. The relation lambda_1 lambda_2=1 implies sum lambda_i^{-1}=sum lambda_i, giving the first squared-sum identity. In n=3, A³=B³=6E, A² wedge B=2(sum lambda_i)E, and A wedge B²=2(sum_{i<j}lambda_i lambda_j)E. Thus
\[
-2C\wedge D^2=2\left(\sum_i\lambda_i+
 \sum_{i<j}\lambda_i\lambda_j-6\right)E.
\]
Since product lambda_i=1, sum_{i<j}lambda_i lambda_j=sum_i lambda_i^{-1}; this is twice the second squared sum. Finally for any lambda>0,
\[
(\sqrt\lambda-\lambda^{-1/2})^2
=4\sinh^2\left(\tfrac12\log\lambda\right)
\geq(\log\lambda)^2
\]
because |sinh t|≥|t|. No unproved interchange of limits occurs.

**Recommended optional mathematical patch (not applied):** add this identity as a separate remark after 14.23.4, preserving the original inequality, tags, version and attribution. Dependents include any subsequent quantitative low-dimensional rigidity or log-spectrum estimates; no existing uniqueness statement is declared false.

## Finding POME-SUBSOL-ROOT-NET-DOMCONV-001
**Status:** verified conditional deduction; severity low. **Not an error in the printed sequential proposition.**

**Anchors:** Theorem 15.29.1 (source non-kahler-pluripotential-theory-0DF693AB, tag 346B39C3F0B6) and equation 15.29.2 (tag 77553DB34B46), physical lines 20–36 of
docs/sections/equations-with-prescribed-singularities--gauduchon-tests-for-integrable-densities/index.html,
blob 8cd9c2d08a4f60ed96d0f5197f4f7ae4df276998.
Proposition 15.32.5 (source non-kahler-pluripotential-theory-643758CB, tag 4C06D1B94BD1, lines 66–105), inequality 15.32.8 (tag CA92BD48A42D, lines 183–195), and Proposition 15.32.9 (source non-kahler-pluripotential-theory-0EDDC796, tag 2210D4123A64, lines 197–233) of
docs/sections/equations-with-prescribed-singularities--stability-of-the-subsolution-threshold/index.html,
blob 903ae0ce7173604063a833295dd94e971b18fd72.

**Net theorem:** Let X be the compact Hermitian manifold and dV the smooth positive reference volume of §§15.29–15.32. Let D_h={p in L^n(dV): rho_h(p)<infinity}, normed by ||p||_D=||p||_n+rho_h(p), where
\[
 \rho_h(p)=\sup_{\gamma\ {\rm Gauduchon}}
      \int_X|p|a_\gamma\,dV
\]
as in (15.29.2). Let D_h^0 denote the closure of bounded functions in D_h. Then p∈D_h^0 **if and only if** for every directed net (q_i) satisfying |q_i|≤|p| almost everywhere and q_i→0 **in measure**, we have ||q_i||_D→0. This requires no countable cofinal subset or sequential compactness.

**Complete proof:** By the order-ideal property in Proposition 15.32.9, every q_i belongs to D_h. Fix K>0 and decompose q_i=q_i^K+r_i^K according to |p|≤K or |p|>K. With V=∫_X dV, for every epsilon>0,
\[
\|q_i^K\|_{2n}^{2n}
\leq \epsilon^{2n}V+K^{2n}\,dV(\{|q_i|>\epsilon\}).
\]
Convergence in measure means the final measure tends to zero **as a net**. First take limsup over i and then let epsilon↓0: ||q_i^K||_{2n}→0. The printed estimate (15.32.8) for r=2n yields rho_h(q_i^K)→0, as well as ||q_i^K||_n→0.

The other part satisfies, uniformly in i,
\[
\|r_i^K\|_n\leq \|p1_{\{|p|>K\}}\|_n,\quad
\rho_h(r_i^K)\leq
\rho_h(|p|1_{\{|p|>K\}}).
\]
Both right-hand sides tend to zero as K→infinity, the latter by the equivalent tail condition in Proposition 15.32.9. The triangle inequality proves full-net convergence by taking the net limit for fixed K before taking K→infinity. Conversely, the dominated **sequence** q_j=p1_{|p|>j} tends to zero in measure; the hypothesized net property forces rho_h(q_j)→0, which is exactly the tail criterion (2) of Proposition 15.32.9 and hence p∈D_h^0.

**Sharp boundary: pointwise nets cannot replace measure convergence.** Direct the finite subsets F⊂X by inclusion. Take p=1 and q_F=1_{X\setminus F}. At each point x, q_F(x) decreases eventually to zero. But for every F, q_F=1 almost everywhere (finite sets have smooth volume zero), so ||q_F||_D=||1||_D>0, and the net does not converge in measure. This works even on a compact Kähler manifold. It demonstrates why pointwise convergence of chosen representatives is not an invariant notion for arbitrary L^n nets. The published Proposition 15.32.9 explicitly assumes **sequences converging in measure** and is not contradicted.

**Recommended optional patch (not applied):** append a net-in-measure corollary after Proposition 15.32.9 with the pointwise-net warning; retain its original statement and source provenance. Dependents are net-based density-root constructions and scalar threshold continuity under actual D_h-norm convergence. No conclusion is drawn about convergence in pluripotential capacity of associated Monge–Ampère solutions. The duality and subcritical estimate are established internal **conditional dependencies**, not newly proved PDE theorems.

## Other direct audit checks and limitations

- Re-checked the Hermitian/real cofactor coefficient 1/(8π), the product-rule/weighted Stokes sign in §14.22, the dimensions-two/three mixed determinant coefficients, and the W^{2,n} product-limit accounting in §14.23. No additional false statement or proof gap established in these selected passages.
- Re-checked the positive Gauduchon test functional (15.29.2), its sup/monotonicity, completeness proof in §15.32.5, the proof split in §15.32.9, and the displayed factor-root statement 15.32.11 only as context. Full upper/lower mass and existence inputs were not independently certified.
- No scripts, project tests, build, browser verification, GitHub Actions, website publication, formalization, PR, merge, main/source/body/registry/canonical-tag edits or user-excluded regularization checks were performed.
