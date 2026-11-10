# Newton-polytope shell measures: uniform Gaussian concentration and sharp codimension-sensitive transport

Date: 2026-11-10. Stable finding **POME-NEWTON-SHELL-CODIM-TRANSPORT-001**. **Severity:** low. **Status:** verified conditional deduction; a new quantitative refinement of the printed measure limit, **not** a false-theorem allegation, complete dependency audit, or proof repair.

## Pinned main sources and precisely checked scope

- Production **main**: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- Integrated reading edition: `docs/sections/partial-kernels-and-quotient-equilibrium--newton-selection-and-moment-shell-limits/index.html`; Git blob `65fe8b5b93df2243f35a45d139e4f6f7829a905a`, 201 physical lines.
- §18.45 setup and Equation 18.45.1: source `non-kahler-pluripotential-theory:4CCEF308`, permanent tag `5CEF27CB9AAA`, physical lines 5–38; selected space `V_m` and invariant smooth positive sampling density `a(r)`.
- Lemma 18.45.3: source `non-kahler-pluripotential-theory:7F9C5680`, permanent tag `F0A638931204`, lines 52–87, especially uniform convex coercivity, gradient diffeomorphism, and compact `r(Q)`.
- Theorem 18.45.7: source `non-kahler-pluripotential-theory:E068131C`, permanent tag `2EC775894117`, lines 94–135, including the exact monomial norms at 109–118, uniform local Laplace normalization at 119–123 and lattice-grid counting at 124–132.
- Theorem 18.45.11: source `non-kahler-pluripotential-theory:45F963D6`, permanent tag `C6669A63F760`, lines 144–164. Its Equation 18.45.12: source `non-kahler-pluripotential-theory:393C1130`, permanent tag `BAC3E7E057E7`, physical lines 145–148; proof's exact monomial probability law at line 159.
- Example 18.45.14: source `non-kahler-pluripotential-theory:9B9B702A`, permanent tag `9600E351F18B`, lines 179–187; checked as a positive-codimension sanity model, not as a complete audit of its entire section.

**First proof-level visit of §18.45**, previously *inventory-only* in the durable section matrix. No other numbered section is newly claimed reviewed. The selected direct-monomial analysis does not use or extend the owner-excluded Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss proof-completion programme.

## New result (probability-normalized kernel)

Retain exactly the assumptions printed before Lemma 18.45.3: `X=(P^1)^n`, `L=O(k_1,...,k_n)`, integer affine base point `b∈Z^n`, a nonempty rational convex polytope `Q⊂int P` with dimension `0≤d≤n`, lattice `Λ=W∩Z^n`, smooth torus-invariant `w`, smooth positive invariant probability `ν`, and `F=φ_0+w` strictly convex with positive-definite Hessian. Write `N_m=dim V_m`. For sufficiently large `m` it is positive. Define the probabilities
[
Pi_m := N_m^{-1} B_m
u,qquad
Pi := rac{1}{operatorname{vol}_{Lambda}(Q)}
 Psi_*(mathrm dq_{Lambda},mathrm d	au)
       = rac{mu_Q}{d!operatorname{vol}_{Lambda}(Q)}.
]
For `d=0`, this is interpreted as Haar measure on the sole real `n`-torus. Give `X` the distance of any fixed smooth Riemannian metric (in particular, the product Fubini–Study metric). Then
[
oxed{ W_1^X(Pi_m,Pi)le C m^{-1/2}. }	ag{A}
]
If the affine dimension is **strictly less than `n`**, there are constants `c,C>0` such that, for all sufficiently large `m`,
[
oxed{c m^{-1/2}le W_1^X(Pi_m,Pi)le C m^{-1/2}.}	ag{B}
]
Thus the qualitative convergence of the printed Theorem 18.45.11 has an **optimal uniform Lipschitz-test rate** for every lower-dimensional rational Newton polytope, including `d=0`. No matching lower estimate is asserted when `d=n`.

There is also a uniform conditional normal-fluctuation statement: under the selected normalized monomial probability corresponding to `q=α/m∈Q`,
[
sqrt m,(r-r(q))  Longrightarrow 
  N!igl(0,(D^2F(r(q)))^{-1}igr)                     	ag{C}
]
uniformly for `q` in the compact polytope, in the bounded-Lipschitz test topology. The Gaussian covariance is independent of the sampling density `a` to leading order.

## Self-contained computation and justification

### 1. Exact probabilities and uniform concentration

For `q=α/m`, the angle-orthogonal monomial terms in the printed norm decomposition give **exactly**
[
mathrm dP_{m,q}(r,	au)=
rac{e^{-mPhi_q(r)}a(r),mathrm dr,mathrm d	au}
{int_{mathbb R^n}e^{-mPhi_q(s)}a(s),mathrm ds},
quad
Phi_q(r)=F(r)-qcdot r+F^*(q)ge0.
]
Thus `Π_m = N_m^{-1} Σ_{q∈Q_m} P_{m,q}` where `Q_m=m^{-1}(mQ∩Z^n)`. The unique zero of `Φ_q` is `r(q)=(∇F)^{-1}(q)`.

The printed bound `F(r)-q·r ≥ δ Σ|r_j|-||w||∞` is **uniform** for `q∈Q`, since `Q⊂int P` is compact; `F^*` is bounded on `Q`. Combining it with compact-set strict convexity gives, for some uniform `ρ,λ,c_ρ>0`,
[
Phi_q(r)ge lambda |r-r(q)|^2quad(|r-r(q)|leho),
qquad
Phi_q(r)ge c_hoquad(|r-r(q)|geho).
]
The latter inequality follows by a compact annulus argument plus uniform coercivity, and **not** from an unjustified global Hessian lower bound.

The smooth invariant density `a(r)` on the compact product of projective lines decays exponentially in each logarithmic coordinate, and it is uniformly bounded below on a fixed neighborhood of the compact set `r(Q)`. In particular, all its polynomial moments are finite. Integration in the radius-`m^{-1/2}` ball gives
[
int e^{-mPhi_q}a,mathrm drge c_0 m^{-n/2}.
]
Gaussian integration inside the fixed `ρ`-ball and the exponential tail outside it then give, for `p=1,2`, uniformly for `q∈Q`,
[
int |r-r(q)|^p,mathrm dP_{m,q}le C_p m^{-p/2}.       	ag{1}
]
The tail estimate for weighted moments uses `e^{-mc_ho}int |r-r(q)|^p a(r)mathrm dr`; it is **not** inferred from a probability tail bound alone.

With `r=r(q)+m^{-1/2}z`, Taylor's theorem on the fixed compact neighborhood yields
[
mPhi_q(r)=rac12 z^	op H(q)z+O(m^{-1/2}|z|^3),
quad H(q)=D^2F(r(q))>0,quad
a(r)=a(r(q))+o(1).
]
Uniform Gaussian domination for bounded `z`, the uniform tail estimate, and (1) give the uniform Gaussian limit (C), and uniform integrability for its first moments. No general non-pluripolar mass theorem is invoked.

### 2. Coupling the monomial concentration

For fixed `q`, couple a random `(r,	au)` with `(r(q),	au)`, keeping the angle exactly unchanged. The map `(r,	au)mapsto([1:e^{r_1/2+i	au_1}],...,[1:e^{r_n/2+i	au_n}])` has globally bounded derivative in its `r` variables for the product Fubini–Study metric (its radial speed in each factor is proportional to `e^{r_j/2}/(1+e^{r_j})`, hence bounded). Any other fixed smooth metric has an equivalent distance on compact `X`. By (1),
[
W_1^Xigl(P_{m,q},Psi(q,cdot)_*mathrm d	auigr)
le C m^{-1/2},                                      	ag{2}
]
uniformly in `q`. Mixture of these couplings yields the same upper bound between `Π_m` and the equally weighted **discrete shell** measure
[
Pi_m^{m shell}=N_m^{-1}sum_{qin Q_m}Psi(q,cdot)_*mathrm d	au.
]

### 3. Quantitative lattice coupling (including the lower-dimensional lattice)

If `d=0`, the assumption `b∈Z^n` gives `Q_m=Q` for every `m`; the discrete and limiting shell laws agree exactly. If `d≥1`, take fundamental half-open lattice cells of `m^{-1}Λ` centered at the points in `Q_m`. Their diameter is `O(m^{-1})`; the union differs from `Q` only within a relative boundary layer of thickness `O(m^{-1})`. A polytope has finite `(d-1)`-dimensional facet measure, so this symmetric difference has `d`-volume `O(m^{-1})`. Normalize the union measure by `N_m/m^d=operatorname{vol}_Λ(Q)+O(m^{-1})`. Coupling each cell to its center costs `O(m^{-1})`, and the remaining normalized boundary-layer mass costs `O(m^{-1})` in Wasserstein distance because `Q` and the cells have uniformly bounded diameter. Thus
[
W_1left(N_m^{-1}sum_{qin Q_m}delta_q,rac{mathbf1_Q,mathrm dq_Λ}{operatorname{vol}_Λ(Q)}ight)
le C/m.                                               	ag{3}
]
The inverse gradient `q↦r(q)` is Lipschitz on compact `Q⊂int P`, so pushing (3) through `Ψ` with identically coupled angles shows `W_1^X(Pi_m^{m shell},Pi)le C/m`. Combining with (2) proves (A). The lattice dimension is `d`, not the ambient dimension `n`; there is no unwarranted factor `m^n`.

### 4. Why codimension forces the exponent `1/2`

Assume `d<n`. The compact moment shell `S_Q=Psi(Q	imes(S^1)^n)` supports `Π`. Thus the function `f(x)=operatorname{dist}_X(x,S_Q)` is 1-Lipschitz and `∫f,mathrm dPi=0`. Choose a nonempty relatively compact open ball `K` in `relint Q` (for `d=0`, let `K=Q`). Its `d`-dimensional lattice-frequency tends to the **positive** fraction `vol_Λ(K)/vol_Λ(Q)`.

Near `r(K)`, the smooth embedded submanifold `r(b+W)subsetmathbb R^n` has tangent `H(q)^{-1}W`, of dimension `d`; its normal space `N_q` has dimension `n-d≥1`. In compact logarithmic-angle charts, smooth metrics are uniformly bi-Lipschitz equivalent to the Euclidean product metric. The distance to the shell has the standard first-order normal approximation for `q` in the closure of `K`, uniformly for bounded displacements:
[
sqrt m, figl(Psi(r(q)+z/sqrt m,	au)igr)
ge c_1|operatorname{pr}_{N_q}z|-O(m^{-1/2}|z|^2),        	ag{4}
]
where `Ψ(r,	au)` here means the same torus-coordinate map evaluated at arbitrary logarithmic `r`; the notation differs only in its input coordinates. Since `K` lies away from the relative boundary of `Q`, minimizers in the distance comparison are local and (4) is unaffected by possible corners on the far boundary of `Q`. Uniform Gaussian convergence (C) and the second-moment bound (1) imply
[
liminf_{m	oinfty}inf_{qin Kcap Q_m}
sqrt m int f,mathrm dP_{m,q}
ge c_1inf_{qinar K}mathbb E
|operatorname{pr}_{N_q}Z_q|>0,
quad Z_qsim N(0,H(q)^{-1}).
]
The infimum is positive because `H(q)^{-1}` is uniformly positive definite and the normals have positive dimension. The positive lattice fraction from `K` now gives `∫f,mathrm dΠ_m≥c m^{-1/2}`. Kantorovich–Rubinstein duality proves the lower bound (B). This is a **uniform-over-tests** sharpness statement, not a claim that every smooth test has a square-root error.

In the printed Example 18.45.14 the affine direction is `(1,-1)` and the shell is `r_1+r_2=0` (`|z_1z_2|=1`); the normal component is nonzero and the same lower-bound mechanism applies. In the product-Fubini–Study case its conditional radial Hessian is `H(t)=(1-t^2/4)I_2`, giving strictly positive variance of `r_1+r_2` throughout `-1/2≤t≤1/2`. This explicitly checks the dimensional mechanism without asserting an exact distance constant for `W_1^X`.

## Judgment, proposed addition, and unresolved dependencies

**No incorrect printed theorem identified in this selected calculation.** The exact monomial probability law, the affine lattice count, and the weak shell limit of Theorem 18.45.11 agree with the direct derivation. The report establishes only its **quantitative** consequence (A)–(B) in a fixed smooth metric; it does not certify every argument or current identity in §§18.45.3/.7/.11, nor the global non-pluripolar-product claims. It does not imply any rate for the unnormalized `m^{-d}B_mν` stronger than its own lattice-normalization errors without an additional computation; no rate is asserted for arbitrary continuous tests without a modulus of continuity.

**Proposed source-body change (not applied):** an optional remark after Theorem 18.45.11 on `W_1^X(Π_m,Π)=O(m^{-1/2})`, with sharpness for `d<n` and a pointer to the compact inverse-gradient and cell-coupling arguments. Leave original source labels, permanent tags, normalization, attribution, and distinct variants untouched. The quantitative statement may be used by later explicit Newton-shell comparisons; it does not replace any Demailly/Bergman/L²/OT regularization-dependent statement.

**Coverage:** §18.45 selected monomial norm, probability limit, Laplace concentration, and lattice-count proof passages read at the anchors above. **One first selected proof-visited numbered section; zero complete section certifications.** Current main inventory: 25 chapters / 747 sections. All pre-existing confirmed errors, proof gaps, external-input entries, duplicate classifications and deferred-by-user items remain unchanged. No builds, tests, CI, formal verification or publication were performed.
