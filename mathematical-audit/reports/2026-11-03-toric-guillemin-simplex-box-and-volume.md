# Mathematical audit — Guillemin toric reference metrics on simplices and boxes (2026-11-03)

**Finding ID:** `POME-TORIC-GUILLEMIN-SIMPLEX-BOX-MASS-001`  
**Classification:** low / **verified conditional deduction** (an exact model and normalization check, **not** a counterexample to the printed theorem and **not** a proof of all general dependencies).  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Precise source and scope

The primary integrated reading edition is `docs/sections/convex-analysis-and-toric-potentials--the-guillemin-reference-metric/index.html`, blob `4458eef6df84ef46d601d39506017387ed292e08`, **Theorem 21.10.1**, source `foundations-of-pluripotential-theory:E94A20D6`, permanent tag `B471B994CE64`, physical lines **11–92** (statement 11–21; proof Steps 1–5 at 27–91). This is the first direct proof/model check in §21.10 in this audit. Crosschecks only: `docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html`, blob `7089aa41ae2422b1bd6b5094e46668cbc8ed37be`, Theorem 21.5.1, source `foundations-of-pluripotential-theory:4A0FAEB3`, permanent `409656CC47D4`, lines 10–41; `docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html`, blob `7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c`, Theorem 21.9.5, source `foundations-of-pluripotential-theory:BD98CC5B`, permanent `69D3D97E7701`, lines 139–160; the lattice-polytope charts of Lemma 21.8.2 (source `foundations-of-pluripotential-theory:86BADE82`, permanent `41C54729DBFD`) are premises, not fully reproved here.

The hypotheses are the printed ones: a **full-dimensional smooth lattice polytope** `P` in the character lattice `M`, its associated smooth projective toric variety `X_P`, and the facet functions `ell_rho` with **primitive inward** normals. The convex potential is `G_0(m)=sum_rho ell_rho(m) log ell_rho(m)` on `P` and `+infinity` outside, with `0 log 0=0`. Put `F_0=G_0^*`, `x_i=log|z_i|^2`, and `dd^c=(i/2pi) partial bar-partial`. The vertex-frame weight is `H_v=F_0(Trop(z))-log|chi^v(z)|^2`. No regularization, Bergman, weighted-L2, OT, multiscale, or positivity-loss material is used.

## 1. Exact simplex model: all dimensions, all positive integral degrees

Let `n>=1` and `d` be a positive integer. Take the Delzant simplex

`P_d = {m in R^n : m_i>=0 (1<=i<=n), m_0=d-sum_i m_i>=0}`.

Its `n+1` facet functions are exactly the barycentric lengths `m_0,...,m_n`. Therefore

`G_0(m)=sum_{i=0}^n m_i log m_i`.

For any `x in R^n`, minimizing `G_0(m)-sum_i m_i x_i` subject to `sum_{i=0}^n m_i=d` gives the unique interior solution

`m_i = d e^{x_i}/Z` for `i>=1`, and `m_0=d/Z`, where `Z=1+sum_{i=1}^n e^{x_i}`.

Indeed the stationarity equations are `x_i=log(m_i/m_0)`; strict convexity follows from the restricted Hessian `diag(1/m_i)+ (1/m_0) 11^T`. Substitution into the Legendre expression gives the **exact formula**

`F_0(x)=d log(1+sum_i e^{x_i})-d log d`.

Thus on the torus chart at the zero vertex,

`H_0(z)=d log(1+sum_i |z_i|^2)-d log d`.

On the vertex chart corresponding to `v=d e_j`, set `w_j=1/z_j` and `w_i=z_i/z_j` for `i!=j`. Subtracting `d log|z_j|^2` yields the smooth expression

`H_v(w)=d log(1+sum_{i=1}^n |w_i|^2)-d log d`,

where the index `j` has been replaced by the homogeneous coordinate `w_j`. These formulas verify the singular-logarithm cancellation and transition-weight identity of Theorem 21.10.1 **for this nontrivial family, on all toric boundary charts**. Positivity is explicit: `dd^c H_v=d omega_FS` and `d>0`.

Writing `p_i=e^{x_i}/Z` and `p_0=1/Z` gives

`D^2F_0(x)=d(diag(p_1,...,p_n)-p p^T)`,  
`det D^2F_0(x)=d^n p_0 product_{i=1}^n p_i=d^n (product_i e^{x_i})/Z^{n+1}>0`.

The complex Hessian on the affine chart has determinant `d^n/(1+|z|^2)^{n+1}`. Hence

`integral_{P^n} (dd^c H_0)^n = (n! d^n/pi^n) integral_{C^n} (1+|z|^2)^{-n-1} dV = d^n`,

where the final radial integral equals `pi^n/n!`. There is **no missing factor of n!** in the complex total mass.

The real Alexandrov normalization in Theorem 21.5.1 instead gives `MA_R(F_0)(R^n)=n! vol(P_d)=d^n`, in agreement with the complex total mass. The toric integration can also be checked directly: writing `z_i=r_i e^{i phi_i}` and `x_i=log r_i^2`, one has `(dd^c F_0(Trop))^n=n!det D^2F_0(x) dx_1...dx_n dphi_1...dphi_n/(2pi)^n` on the torus.

Finally Theorem 21.9.5 predicts `h^0(P^n,O(kd))=#(kP_d cap Z^n)=binom(kd+n,n)`, and so `lim_{k->infinity} (n!/k^n)h^0=d^n`. The complex, real, polytope and section-growth normalizations all agree.

## 2. Exact box model: separate boundary facets and mixed intersections

Take the smooth lattice box `P=prod_{i=1}^n [0,d_i]` with `d_i` positive integers. Both facets in each factor contribute, so

`G_0(m)=sum_i [m_i log m_i+(d_i-m_i)log(d_i-m_i)]`,

and independent one-variable Legendre duality yields

`F_0(x)=sum_i [d_i log(1+e^{x_i})-d_i log d_i]`.

This is the Guillemin potential on `X_P=(P^1)^n`. At each of the `2^n` vertex charts, replace `z_i` by `w_i=1/z_i` for every upper-endpoint coordinate; subtracting the appropriate `d_i log|z_i|^2` makes `H_v=sum_i d_i log(1+|w_i|^2)-sum_i d_i log d_i` smooth on the entire chart. Its curvature is `omega=sum_i d_i pr_i^* omega_FS`, a positive Kähler form. Since the square of each pullback is zero and `integral_{P^1}omega_FS=1`,

`integral_{(P^1)^n} omega^n=n! product_i d_i=n! vol(P)`.

Again the finite-degree character basis gives `h^0(X_P,L^k)=product_i(kd_i+1)`, hence `lim (n!/k^n)h^0=n!product_i d_i`. This independently detects the **mixed-intersection factorial** that would be invisible in the simplex alone.

## 3. Audit of printed general proof steps and limitations

- **Step 1 (lines 27–36):** compactness of `P`, strict convexity of `G_0` in its interior, the boundary directional derivative `-infinity`, and smooth Legendre inversion have the right hypotheses; both families give explicit inverses. The bound `F_0~h_P` is consistent with bounded `G_0` on compact `P`.
- **Step 2 (lines 37–66):** the split `G_0=sum_{i in I}t_i log t_i+g` relies on the **Delzant** facets at the vertex. In the simplex and box, solving for the boundary coordinates gives the stated smooth inverse even with several vanishing `w_i`. Removing smoothness/Delzant hypotheses is **not** licensed by this audit.
- **Step 3 (lines 67–74):** cancellation of `t_i log t_i` against `t_i x_i` is exact in the computed charts; it does not mean the uncorrected `F_0(Trop)` extends smoothly as a scalar function in *every* trivialization.
- **Step 4 (lines 75–88):** positive complex Hessians follow directly from the explicit Fubini–Study and product weights. The mixed derivative blocks vanish at coordinates `w_i=0`, consistent with the printed Jacobian argument.
- **Step 5 (lines 89–91):** the weights satisfy `H_v-H_{v'}=log|chi^{v'-v}|^2`; `e^{-H_v}=|chi^{v-v'}|^2 e^{-H_{v'}}`. The sign and character direction are correct in both model families.

**Status:** verified conditional deduction, **not** confirmed error, verified full-section proof, or verified repair. The complete general polytope/fan/chart existence results (especially §21.8–9), Alexandrov pushforward for nonsmooth potentials (§21.5), and all global dependents are **not recertified** here. The exact audited consequence is that the printed theorem passes these all-dimensional simplex and box boundary/volume/character checks. No edits to source, reading body, tags, registry or main are proposed. **Affected dependents:** §21.12–21.13 toric metrics, any comparison of toric Monge–Ampère mass to Newton-body volume, and asymptotic section counts in §21.9.5, all only as normalization crosschecks.

## Existing findings and exclusions

Do not change any prior resolved/unresolved/deferred statuses. In particular, Demailly approximation/regularization and its dedicated Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain **deferred-by-user** and were not inspected. Actual coverage is **a new targeted proof/model pass of §21.10.1**, with §21.5.1 and §21.9.5 as premises and normalization crosschecks; **no complete section certified**, and no builds, CI, formal verification, tests, or website publication were run.
