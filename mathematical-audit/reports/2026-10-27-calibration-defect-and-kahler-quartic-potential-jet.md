# Quantitative complex calibration and the curvature quartic of a Kähler potential

**Audit date:** 2026-10-27 (Asia/Shanghai).  
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Review head before this increment:** a619aa2756a221271ac24b1bf166d7e898532a87.  
**Scope:** first *selected statement-and-proof-level* inspection of current reading-edition §§10.89 and 10.94. Neither section, the upstream current calculus, nor the full project is certified. The excluded Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion programme has not been examined. The string "demailly-complex-geometry" is a public source identifier here, **not** an indication that these independent Hermitian linear-algebra and Kähler-coordinate proofs belong to the excluded programme.

## Source passages inspected

- §10.89: \`docs/sections/hermitian-volume-and-complex-calibration/index.html\`, main blob \`dfaec751e0c2e79937b0126d572a87bc300f3261\`. Proposition **10.89.2** (source label \`demailly-complex-geometry-E9A95F3B\`, permanent tag \`AB0853CAC9B1\`), physical lines **10–26**, including the real-skew-adjoint tangent projection and equality test. Theorem **10.89.3** (source label \`demailly-complex-geometry-6F717209\`, tag \`EB0F17719184\`), lines **28–41**, especially Stokes at line 38. Example **10.89.4** (source label \`demailly-complex-geometry-35C1AFC1\`, tag \`75AEF98694BC\`), lines **43–49**, checked to distinguish reversed orientation.
- §10.94: \`docs/sections/kahler-normal-coordinate-jets/index.html\`, main blob \`4fd58352bd134c2715fc4cbf1e0074a42a7e0657\`. Theorem **10.94.2** (source label \`demailly-complex-geometry-07136048\`, tag \`64B6971EF741\`), lines **10–29**; normal metric and curvature coefficient equation **10.94.3** tag \`F8EFB833957C\`, lines **16–23**; Kähler symmetry equation **10.94.4** tag \`89C5EDFA346C\`, lines **24–27**. The proof's second-order metric coefficients, holomorphic cubic elimination and sign computation occupy lines **31–79**, with equation **10.94.5** tag \`E855089CB081\` and cubic transformation **10.94.6** tag \`9F6B4FD758C3\`.
- Both integrated proofs are read as mathematical statements at this pinned public main revision. No source-repository changes, project build, formal verification, CI, or publication were performed.

## POME-CALIBRATION-ANGLE-DEFECT-001

**Severity:** low. **Status:** verified conditional deduction. **Printed Proposition 10.89.2 and Theorem 10.89.3:** no error found.  
**Hypotheses:** exactly the Hermitian metric, positive integer p, compact oriented embedded real C¹ submanifolds Y and Z, exact associated form ω=dγ, complex-oriented analytic interior of Z and equal oriented boundary currents of Theorem 10.89.3. The real metric here is the one specified by §10.89, and ω=(i/2)Σdz∧dbar z in unitary coordinates.

For an oriented real 2p-dimensional tangent plane L and any real orthonormal basis (e_a)_(1≤a≤2p) of L, set

\[
c(L)=\frac{(\omega^p/p!)|_L}{dV_L},\qquad
D_J(L)=\sum_{a=1}^{2p}\left\|P_{L^\perp}Je_a\right\|^2.
\]

The second quantity is frame independent. Let the signed block coefficients of ω|_L from Proposition 10.89.2 be a_1,...,a_p∈[-1,1], choosing the block basis to have the given orientation. Then

\[
c(L)=\prod_{j=1}^{p}a_j,\qquad
D_J(L)=2\sum_{j=1}^p(1-a_j^2).
\]

The **pointwise quantitative Wirtinger inequality**, valid for every oriented L, is

\[
1-c(L)\geq \kappa_p D_J(L),\qquad
\boxed{\kappa_1=\tfrac14,\quad \kappa_p=\tfrac1{2p}\ (p\geq2).}
\]

Consequently the **exact calibrated deficit identity** and its quantitative consequence are

\[
\boxed{\operatorname{Vol}(Y)-\operatorname{Vol}(Z)
=\int_Y [1-c(T_yY)]\,dV_Y
\ \geq\ \kappa_p\int_Y D_J(T_yY)\,dV_Y.}
\]

**Complete proof:** A=P_LJ|_L is skew-adjoint and has squared singular values a_j², each twice, so ∥P_LJe_a∥² sums to 2Σa_j². Because J is an isometry, subtracting from 2p gives the displayed D_J identity. For p=1, with -1≤a_1≤1,

\[
1-a_1\geq\tfrac12(1-a_1^2)=\tfrac14D_J.
\]

For p≥2, put q=p^{-1}Σa_j²∈[0,1]. By AM–GM,

\[
\prod_j a_j\leq\prod_j|a_j|
=\Bigl(\prod_j a_j^2\Bigr)^{1/2}
\leq q^{p/2}\leq q,
\]

and therefore 1-∏a_j≥1-q=D_J/(2p). The Stokes computation in Theorem 10.89.3 gives ∫_Y ω^p/p!=∫_Z ω^p/p!=Vol(Z). Substituting c(TY) proves the exact identity and inequality; no limiting argument is involved.

**Sharpness of the universal constants (varying ambient dimension):** for p≥2 take a totally real 2p-plane L in C^(2p), spanned by the real coordinate axes. Then a_j=0, c=0 and D_J=2p, attaining κ_p=1/(2p). For p=1 in C², take the oriented plane spanned by a unit real vector e_1 and cos(t)Je_1+sin(t)e_2, where e_2 is orthogonal to the complex line through e_1. It has a_1=cos(t) and D_J=2sin²(t), so the ratio (1-c)/D_J tends to 1/4 as t→0. These are sharp **pointwise universal** constants, not an assertion that a particular Y/Z pair attains global equality. In ambient dimensions too small to admit totally real 2p-planes the displayed constant need not be optimal.

**Equality rigidity:** If Vol(Y)=Vol(Z), the continuous nonnegative density 1-c(TY) integrates to zero. Thus c(TY)=1 at every interior point; Proposition 10.89.2 implies J(TY)=TY and the *positive* complex orientation. The cited C¹ holomorphic-tangent regularity then makes the interior of Y locally complex analytic. Conversely these conditions force zero deficit. This also explains why the mixed component orientations of Example 10.89.4 cannot be silently allowed.

**Dependencies/limitations:** Proposition 10.89.2 (orthogonal block decomposition), Theorem 10.89.3 (C¹ Stokes and exactness), and its cited holomorphic-tangent regularity for the last geometric statement only. Those upstream theorems were inspected at the stated passages but not globally certified. **Proposed correction:** none required to the printed mathematics; an optional quantitative corollary after 10.89.3. **Affected dependents:** volume-minimizing complex cycles, equality statements and possible quantitative near-calibration estimates. No claim about Hausdorff proximity or regularity follows solely from a small integral defect.

## POME-KAHLER-QUARTIC-POTENTIAL-001

**Severity:** low. **Status:** verified conditional deduction. **Printed Theorem 10.94.2:** no error found.  
**Hypotheses:** smooth Kähler metric with the *section-specific* convention ω=iΣg_(l bar m) dz_l∧dbar z_m. Use holomorphic normal coordinates furnished by Theorem 10.94.2 and the **unscaled** Chern curvature coefficients C_(j bar k l bar m) of equations 10.94.3–4. These conventions differ by a constant scalar from the unitary ω of §10.89 and must not be mixed.

There is a smooth real local Kähler potential Φ, adjusted by the real part of a holomorphic polynomial of degree ≤4, with the **explicit fourth-order jet**

\[
\boxed{\displaystyle
\Phi(z)=\sum_l|z_l|^2
-\frac14\sum_{j,k,l,m}C_{j\bar k l\bar m}(0)
 z_jz_l\bar z_k\bar z_m+O(|z|^5),\quad
\omega=i\partial\bar\partial\Phi.
}
\]

**Proof with coefficient and sign:** The Kähler symmetries in 10.94.4 make

\[
Q(z)=\sum_{j,k,l,m}C_{j\bar k l\bar m}(0)z_jz_l\bar z_k\bar z_m
\]

real and symmetric in the two holomorphic and two antiholomorphic indices. Direct differentiation of the four symmetric terms gives

\[
\partial_l\partial_{\bar m}Q
=4\sum_{j,k}C_{j\bar k l\bar m}(0)z_j\bar z_k.
\]

The polynomial Φ_0=Σ|z_l|²-Q/4 therefore satisfies

\[
\partial_l\partial_{\bar m}\Phi_0
=\delta_{lm}-\sum_{j,k}C_{j\bar k l\bar m}(0)z_j\bar z_k,
\]

which matches the entire degree-two normal-coordinate metric jet 10.94.3; notably the factor is **1/4**, not 1/2, and the sign is negative under the stated unscaled Chern convention. A smooth local real Kähler potential Φ̃ exists by the elementary local ∂∂bar Poincaré lemma. Now ∂∂bar(Φ̃-Φ_0)=O(|z|³). In the Taylor polynomial of the smooth difference through total degree four, every mixed monomial z^α bar z^β with |α|,|β|≥1 must vanish: otherwise a mixed second derivative has a nonzero homogeneous term of degree ≤2. All remaining terms are holomorphic or antiholomorphic, and reality identifies them as the real part of a holomorphic polynomial. Subtract that pluriharmonic polynomial without changing ω. Taylor's theorem gives the stated O(|z|⁵) remainder.

**Independent normalization test actually performed:** in complex dimension one, the Fubini–Study potential Φ=log(1+|z|²) has metric g=(1+|z|²)^(-2)=1-2|z|²+O(|z|⁴). Thus C_(1 bar 1 1 bar 1)=2 and the formula predicts -C|z|⁴/4=-|z|⁴/2, precisely the Taylor coefficient of log(1+|z|²). A local SymPy mixed-derivative check also returned ∂_z∂_bar z(|z|²-C|z|⁴/4)=1-C|z|²; this small arithmetic check is not a project test or formal verification.

**Dependencies/limitations:** the checked normal-coordinate metric jet and curvature sign of Theorem 10.94.2; elementary existence of a local smooth Kähler potential (not independently reconstructed in this run); ordinary smooth Taylor expansion. Neither the normal-coordinate lemma cited inside the theorem nor general Chern curvature identities were comprehensively certified. **Proposed correction:** none; optionally record this as a curvature-potential Taylor corollary, preserving the unscaled curvature and avoiding conversion to the ddᶜ=i/(2π)∂bar∂ convention without the corresponding factor. **Affected dependents:** local metric/curvature expansions, curvature-jet normalizations and geometric local asymptotics.

## Coverage, classifications and exclusions

Exactly two previously **inventory-only** ToC section rows, §§10.89 and 10.94, receive **selected proof-level** annotations. No entire section, chapter or prerequisite chain is certified. There is **no newly confirmed false theorem or proof gap**, no ledger item resolved, and the two independent deductions should not be counted as repairs. The actual project ToC had 747 unique section keys before this increment; no ToC source or numbering is changed.

The dedicated author-excluded Demailly approximation/regularization, Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme remains **deferred-by-user**, not resolved, checked or certified. No mathematical body, source repository, permanent tag, registry, main branch, CI, build, formalization or published site was changed.
