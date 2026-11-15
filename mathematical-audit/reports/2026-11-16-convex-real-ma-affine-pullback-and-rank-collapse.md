# Affine covariance and singular-rank collapse for real mixed Monge–Ampère measures

**Date:** 2026-11-16  
**Finding ID:** `POME-CONVEX-MA-GL-AFFINE-PULLBACK-MIXED-001`  
**Status:** **verified conditional deduction** (low severity). **Not** a false theorem, a demonstrated proof gap, or a repair to the printed text.  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Current integrated reading edition:** `docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html`, Git blob `7089aa41ae2422b1bd6b5094e46668cbc8ed37be`, section source `foundations-of-pluripotential-theory:34803B32`, permanent section tag `07CCE1F902ED`.

## Precise anchors and assumptions

- Theorem **21.5.1**, source `foundations-of-pluripotential-theory:4A0FAEB3`, permanent tag `409656CC47D4`: physical lines **10–40**, particularly the subgradient-volume definition on lines **11–14**, measure representation on **15–21**, and measurability/subgradient duality on **24–40**.
- Proposition **21.5.4**, source `foundations-of-pluripotential-theory:EAD83A50`, permanent tag `5D8A7A7D734E`: physical lines **99–159**, including the smooth and `C^{1,1}` determinant formula and the mixed-measure construction; polarization equation **21.5.5**, source `foundations-of-pluripotential-theory:24CC29A7`, permanent tag `D38381F0AC43`, physical lines **135–159**.
- Theorem **21.5.2**, source `foundations-of-pluripotential-theory:6403CF44`, permanent tag `F4072D9ED060`, physical lines **44–86**: background only; its general convergence theorem is **not** newly certified.

The work concerns **finite convex functions on the whole `N_R ≃ R^n`**, with (n\geq1). The metric normalization in Pome is (\mathrm{MA}_{\mathbb R}(F)(E)=n!\operatorname{vol}(\partial F(E))). The statement below requires no differentiability, smoothness or coercivity.

## Theorem proved in this audit

Let (A:\mathbb R^n\to\mathbb R^n) be a real linear map, (b\in\mathbb R^n), (\lambda_i>0), and (\ell_i(x)=\langle q_i,x\rangle+c_i) arbitrary affine functions. For arbitrary finite convex (F_1,\ldots,F_n), set
[
 H_i(x)=\lambda_iF_i(Ax+b)+\ell_i(x).
]
If (A) is invertible and (\phi(y)=A^{-1}(y-b)), then **as Radon measures**,
[
 \boxed{\;
 \operatorname{MA}_{\mathbb R}(H_1,\ldots,H_n)
 =|\det A|\Bigl(\prod_{i=1}^n\lambda_i\Bigr)
    \phi_*\operatorname{MA}_{\mathbb R}(F_1,\ldots,F_n).\;}
 \tag{1}
]
For the diagonal measure, the coefficient is (\lambda^n|\det A|), **not** (\lambda^n(\det A)^2) in the pushforward form; the latter square occurs in the **density with respect to (dx)** when (F) is smooth. If (operatorname{rank}A<n), then
[
 \boxed{\operatorname{MA}_{\mathbb R}(H_1,\ldots,H_n)=0.}\tag{2}
]
Both conclusions also hold for any subtuple polarizations of (n) convex functions, with repeated entries allowed.

### Proof for one convex function

First suppose (A) invertible, (H(x)=\lambda F(Ax+b)+\langle q,x\rangle+c). The supporting-slope inequality for (F), followed by the bijection (z=Ax+b), gives the **exact** subgradient identity
[
 \partial H(x)=q+\lambda A^{\mathsf T}\partial F(Ax+b).
]
Indeed, the forward implication is immediate; conversely, take any supporting inequality for (H) and substitute (x'=A^{-1}(z'-b)) to recover the supporting inequality for (F). Consequently
[
 \partial H(E)=q+\lambda A^{\mathsf T}\partial F(AE+b)
]
for every Borel (E). The right-hand set is Lebesgue measurable in the completed sense by Theorem 21.5.1. Since affine linear maps on the slope space scale (n)-dimensional Lebesgue volume by (\lambda^n|\det A|), the Pome (n!)-normalized definition yields
[
 \mathrm{MA}_{\mathbb R}(H)(E)
 =\lambda^n|\det A|\,\mathrm{MA}_{\mathbb R}(F)(AE+b)
 =\lambda^n|\det A|\,\phi_*\mathrm{MA}_{\mathbb R}(F)(E).
 \tag{3}
]
This argument uses no approximation and applies directly to arbitrary finite convex (F).

If (A) has nonzero kernel, every (v\in\ker A) satisfies (H(x+tv)=H(x)+t\langle q,v\rangle) for all real (t). For (p\in\partial H(x)), the supporting inequality in both directions (t\to\pm\infty) forces (\langle p,v\rangle=\langle q,v\rangle). Hence
[
 \partial H(\mathbb R^n)\subset q+(\ker A)^\perp=q+\operatorname{im}A^{\mathsf T},
]
a proper affine subspace of zero (n)-dimensional volume. Thus (\mathrm{MA}_{\mathbb R}(H)=0). This also covers the affine function (H) obtained when (A=0).

### Proof for the mixed measure

Proposition 21.5.4 constructs the mixed measure by the signed finite polarization of the diagonal measures:
[
 n!\,\mathrm{MA}_{\mathbb R}(F_1,\ldots,F_n)
 =\sum_{J\subseteq\{1,\ldots,n\}}(-1)^{n-|J|}
 \mathrm{MA}_{\mathbb R}\!\left(\sum_{j\in J}F_j\right).
 \tag{4}
]
For invertible (A), apply (3), with (\lambda=1), to **every** term
(sum_{j\in J}H_j=(\sum_{j\in J}\lambda_jF_j)\circ(A\cdot+b)+\sum_{j\in J}\ell_j).
The same common factor (\lvert\det A\rvert\phi_*) comes out of the finite signed combination. Polarization and the already established multilinearity then give (1), including the separate factors (\lambda_j). For singular (A), the just-proved diagonal zero-measure assertion applies to every polarized sum; (4) gives (2). The equality of the signed combinations is an equality of locally finite measures and therefore introduces no illegitimate interchange of infinite masses.

### Exact normalization and sharpness tests

For (F(x)=|x|^2/2), the printed smooth formula gives (\mathrm{MA}_{\mathbb R}(F)=n!\,dx). Invertible (A) gives
[
 \mathrm{MA}_{\mathbb R}(\lambda F\circ A)
 =n!\lambda^n(\det A)^2\,dx,
]
because (\phi_*(dx)=|\det A|\,dx). Thus **two determinant factors in the density but only one in the pushforward measure** are compulsory.

For a genuinely nonsmooth test, (F(x)=\sum_{j=1}^n|x_j|), its subgradient at zero is the cube ([-1,1]^n); away from zero at least one subgradient coordinate is fixed, so the slope image there has zero volume. Hence
[
 \mathrm{MA}_{\mathbb R}(F)=n!2^n\delta_0,
 \qquad
 \mathrm{MA}_{\mathbb R}(F\circ A)=n!2^n|\det A|\delta_0
 \quad(A\text{ invertible}),
]
and the last measure is zero if (A) is singular. This checks the determinant **to the first power on a point mass**, independently from the smooth-density calculation.

For the explicit (2\times2) matrix (A=\left(\begin{smallmatrix}2&1\\0&3\end{smallmatrix}\right)), (\det A=6): the smooth quadratic case has density (72\,dx), while (F(x)=|x_1|+|x_2|) gives (48\delta_0). With (F_1=x_1^2/2), (F_2=x_2^2/2), the original mixed measure is (dx), and the transformed mixed measure is (36\,dx). Exact symbolic checks of these determinant and mixed-polarization identities, including singular-rank examples, were **actually executed** (SymPy, 2026-11-16); this is not a project test/build.

## Classification, scope and dependents

**Low / verified conditional deduction.** All printed statements sampled here are consistent with the calculations; **no confirmed false theorem and no identified missing proof step**. The analytic fact used for arbitrary nonsmooth (F) is precisely the internal Theorem 21.5.1, and the mixed-polarization/continuity infrastructure is Proposition 21.5.4. Their full upstream chains were not transitively certified in this run. This is an **additional exact algebraic functoriality theorem**, not a repair, and it has no connection to the excluded Demailly approximation or positivity-loss program.

Suggested **documentation-only** follow-up (no production change made): explicitly distinguish the one-determinant pushforward covariance from the two-determinant smooth Jacobian density whenever §21.5 is used for coordinate changes or degenerate toric valuations. Potential downstream checks: §21.6 real-convex full-mass limits, §§21.12–21.13 toric Monge–Ampère normalization, and §§19.2/19.7 lattice-coordinate conventions. None of these dependents is certified by this model check.

**Coverage:** new direct proof/model comparison only for selected passages of existing partly reviewed §21.5; **0 newly first-visited numbered sections, 0 wholly certified sections**. Current main table of contents: **25 chapters / 747 numbered sections**. No user-excluded work was reopened. No production source, registry, tags, CI, build or website was changed.
