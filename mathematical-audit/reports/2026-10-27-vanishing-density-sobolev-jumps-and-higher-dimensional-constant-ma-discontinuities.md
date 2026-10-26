# Pome mathematical audit — 27 October 2026
## Vanishing-density Sobolev jumps and higher-dimensional constant-MA discontinuities

**Reviewed `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (independently fetched as current `main` during this review). **Review branch before writing:** `73a3e3e094c607129b9d4d2329c9c6de99b13034`.
**Scope:** fresh, limited proof-level inspection of actual integrated reading-edition §§15.20 and 15.21, both previously marked inventory-only in the 747-row matrix; supporting §14.26.14 and §5.27.1 are referenced as *conditional internal inputs*, not independently certified. No entire section, source theorem or analytic dependency chain is certified. Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme are **deferred-by-user**, neither read nor certified.

### Finding POME-DEGENERATE-MA-THIRD-SOBOLEV-JUMP-001

**Status:** verified conditional deduction (not a false printed theorem). **Severity:** low. **Correction:** optional explicit sharp Sobolev-obstruction corollary after Proposition 15.20.8, keeping its original C^{1,1}-but-not-C² conclusion.

**Exact integrated source.** `docs/sections/equations-with-prescribed-singularities--symmetry-and-the-selected-projective-limit/index.html`, blob `5939b066b23315e66c9f8ec26a97677825fa2a16` on reviewed main. Source label `non-kahler-pluripotential-theory-39588581`, permanent tag `517F0BB04B80`, Proposition 15.20.8, physical lines **193–237**, especially the explicit slope lines **222–236**. Theorem 15.20.4 label `non-kahler-pluripotential-theory-4BBFED99`, permanent `72B88B8B1639`, lines **52–65,135–185**; the bounded radial-flux Lemma 15.20.5 label `non-kahler-pluripotential-theory-DCDE8A82`, permanent `5D3F7173CA27`, lines **78–130**.

**Precisely verified statement.** Keep the particular symmetric projective data and the notation of Proposition 15.20.8; no assertion is made for arbitrary Hermitian equations with smooth nonnegative density. For every `λ>0`, and also for the selected zero-exponent solution `u_*`, the solution is locally `W^{2,∞}` on the open band `-1<r<1`, but fails to belong to `W^{3,1}_{loc}` in *every* neighborhood of *every* point of either hypersurface `r=+t_*` or `r=-t_*`. More precisely, writing `u_λ+ρ=G_λ(r)`, the distribution `D_r^3G_λ` contains a nonzero Dirac mass at each transition; at `r=t_*`, its coefficient is
[
J=z_0(t_*)-p'(t_*)>0.
]
This exact coefficient is independent of `λ>0`; the same holds for `u_*`.

**Proof from the displayed integrated formulas.** Proposition 15.20.8, lines 222–228, gives on the positive part of the band
[
h_lambda=G_lambda'=
egin{cases}
-int_0^r z_0(s),ds,&0le r<t_*,\\
-p(r),&t_*<r<1.
end{cases}
]
The two functions match continuously at `t_*` by the defining first-contact identity `∫_0^{t_*}z_0=p(t_*)` (Theorem 15.20.4, lines 138–144). Each has smooth derivative up to its respective side, and the one-sided second derivatives of `G_lambda` are `-z_0(t_*)` and `-p'(t_*)`; their difference is `J>0` (lines 230–236). On a sufficiently small interval `I` around `t_*`, the function `G_lambda''` is piecewise smooth and bounded, with jump `J`. For every `φ∈C_c^infty(I)`, integration by parts on the two sides yields
[
langle D_r^3G_lambda,phiangle
=int_{Isetminus{t_*}}G_lambda'''(r)phi(r),dr
+Jphi(t_*).
]
The regular contribution above is locally integrable, while `Jδ_{t_*}` is singular with respect to `dr`. Thus `D_r^3G_lambda` is not an `L^1_{loc}` function. The smooth term `ρ(r)` cannot remove this atom. Since `r` is a smooth submersion at each point of the transition hypersurface (lines 230–236), complete it to a local coordinate `(r,y)`; the same singular distribution is `Jδ_{t_*}⊗dy`, up to a smooth positive coordinate density. Hence `u_lambda
otin W^{3,1}_{loc}` there. Conversely the displayed branches of `G_lambda''` are uniformly bounded on a smaller closed band, so `u_lambdain W^{2,infty}_{loc}`. Exchange symmetry supplies the opposite hypersurface, with nonzero jump of opposite orientation. Proposition 15.20.8 states `u_lambda-u_*` is constant throughout the band, so the argument applies unchanged to `u_*`.

**Dependency and limitation:** conditional on the model construction and the positive-exponent radial formula proved in Theorem 15.20.4 / Proposition 15.20.8. This strengthens the *regularity obstruction* only; it does not show a gap in the printed proof of non-C² or refute its conclusion. Dependents: claims of higher Sobolev regularity for smooth but vanishing right-hand sides (§§15.18–15.21) must not be deduced without new hypotheses.

### Finding POME-CONSTANT-MA-DISCONTINUITY-DIMENSION-001

**Status:** verified conditional deduction (not a false printed theorem). **Severity:** low. **Correction:** optional sharp-dimension and exact-discontinuity-locus corollary after Theorem 15.21.12, without altering the original theorem or its proof.

**Exact integrated source.** `docs/sections/equations-with-prescribed-singularities--local-density-and-boundary-control/index.html`, blob `44fa705661cd5778904e1b9a6ea7299fb19e13ff` on reviewed main. Source label `non-kahler-pluripotential-theory-09B4FC75`, permanent `5E22269BEE55`, Lemma 15.21.8, lines **79–141**, especially formula (15.21.9), lines **96–107**, and the pole/continuity proof, **114–140**. Source label `non-kahler-pluripotential-theory-A866D6A3`, permanent `5FC2412C22E9`, Theorem 15.21.12, lines **153–232**, with gluing (15.21.13–14), lines **163–197**, and the singular `L^p` tests, lines **199–231**. The smooth trace criterion Theorem 15.21.2 has permanent `9826C9FA5510`, lines **18–40**.

**New precise statements.**

1. In the bounded psh bidisk model of Lemma 15.21.8, `P(z,w)=a(z)+b(z)|w|²`, the *entire discontinuity locus* is exactly
[
{(0,w): win Wsetminus{0}}.
]
In particular, `P` is continuous at every other point, including every individual pole `(a_k,w)` and all points with `w=0`.

2. In **every** complex dimension `n≥2` there exists a locally bounded psh function on a polydisk whose Bedford–Taylor top power is a strictly positive *constant multiple of Lebesgue measure* but which is discontinuous. In every `n≥2` there is also a **compact flat Kähler torus** carrying a bounded minimal-singularity `θ`-psh potential with a.e. positive `L^1` density belonging to no `L^p, p>1`, whose density is strictly positive and constant on a coordinate ball where the solution is discontinuous.

3. Dimension `n=1` is the sharp obstruction: in a complex curve, a distributional/subharmonic solution of `θ+dd^cu=f,dV` with smooth `θ,f,dV` is smooth locally. Thus the local constant-density discontinuity phenomenon begins in dimension two.

**Proof of (1).** The text sets `h(z)=Σ α_k log|z-a_k|²`, `b=e^h` with `b=0` at poles, `a_k=α_k=2^{-k-4}`, `Σα_k=1/16`, and verifies `a(z)` is continuous and `0≤b≤1`. Away from `S={0,a_k:k≥1}`, `b` is smooth. At a fixed nonzero pole `a_k`, split `h(z)=α_k log|z-a_k|²+H_k(z)` with `H_k` harmonic and smooth near `a_k` (the same local factorization is explicitly used in lines 205–222). It follows that `b(z)=|z-a_k|^{2α_k}e^{H_k(z)}→0=b(a_k)`: continuity holds there. At `0`, the text proves `b(0)>0`, while `b(a_k)=0` and `a_k→0`; consequently `b` is not continuous at `0`. If `w_0≠0`, `P(a_k,w_0)=a(a_k)→a(0)≠P(0,w_0)`, as already shown in lines 137–140. If `w_0=0`, then for `(z,w)→(0,0)`, `|b(z)|w|²|≤|w|²→0` and `a(z)→a(0)`, so `P` **is** continuous there. No other points can be discontinuities.

**Proof of local (2).** On `(U×W)×D^{n-2}` set
[
P_n(z,w,zeta)=P(z,w)+sum_{j=3}^n|zeta_j|^2.
]
This is bounded psh on any relatively compact polydisk. Outside the product of the original pluripolar exceptional set `S×W` with the extra disk factors, the complex Hessian is block diagonal with the 2×2 Hessian of `P` and the identity in the remaining variables. Lemma 15.21.8 computes `det(P_{jar k})=1` away from the exceptional set. Therefore `det H(P_n)=1` there. Using the explicit Pome convention `dd^c=i/(2π)∂ar∂` (compare (15.21.3)) gives
[
(dd^cP_n)^n=rac{n!}{pi^n},dA(z),dA(w)prod_{j=3}^n dA(zeta_j).
]
The exceptional set is pluripolar (lines 134–137), and bounded Bedford–Taylor top powers do not charge pluripolar sets; hence the equality holds globally as a measure. The exact discontinuity locus of `P_n` is the locus in (1) times the remaining disk factors.

**Proof of compact (2).** Let `(X_2,θ_2,u_2,F_2)` be the specific compact flat-torus construction from Theorem 15.21.12. For `n>2`, take the product with the flat elliptic torus `E^{n-2}`, set `X_n=X_2×E^{n-2}`, `θ_n=pr_2^*θ_2+η` where `η` is the product's flat positive form, and `u_n=pr_2^*u_2`. If `T_2=θ_2+dd^cu_2`, dimension-counting/multilinearity gives the *exact equal-density identity*
[
(θ_n+dd^cu_n)^n
=inom{n}{2}T_2^2wedge η^{n-2}
=(F_2circ pr_2)inom{n}{2}θ_2^2wedge η^{n-2}
=(F_2circ pr_2),θ_n^n.
]
For bounded potentials the equality is obtained by local Bedford–Taylor mixed products or by separate continuous monotone approximants, not by an unjustified multiplication of arbitrary singular currents. The product `η^{n-2}` has finite positive mass, so `F_2circ pr_2` is `L^1` and fails every `L^p` with `p>1`, exactly as `F_2` does. The potential is bounded and thus of minimal ordinary singularity type. It is discontinuous at every lift of the original discontinuities, inside a coordinate ball where the density is the original positive constant. For `n=2` this is precisely the published construction.

**Proof of (3).** In dimension one the equation is a linear distributional Poisson equation. In any local holomorphic coordinate `z`, the scalar coefficient `u_{zar z}` is a smooth function (subtract the smooth coefficient of `θ` from that of `f,dV`). Standard local Weyl/elliptic regularity for distributions yields `uin C^infty`. No global connectedness, Kähler hypothesis, or positive density lower bound is required for this local claim.

**Source-independent checks performed:** verified the power-series coefficient `Σ_{k≥1}2^{-k-4}=1/16`; separately recomputed the Hessian block-determinant ratio and `n!` normalization for the product; checked continuity at the accumulation point `(0,0)` using the explicit bound `0≤b≤1`; rechecked the regularized maximum Hessian formula (15.21.14) and the positivity and `L^p` threshold logic (lines 190–231) as prerequisites of the compact example. No project build, CI, formalization, or published-site changes were performed.

**Limitations and dependents.** The higher-dimensional extension uses the *already printed* bounded Bedford–Taylor example and its compact gluing. The complete upstream classical Bedford–Taylor construction and all analytic elliptic inputs were not re-proved in this run. In particular no claim is made about globally smooth strictly positive densities or about solutions having smooth boundary traces: Theorem 15.21.2 remains compatible. Applications include differentiating minimal-singularity MA solutions on locally smooth-density loci; such differentiability requires genuinely additional hypotheses. There is **no newly confirmed false source theorem** in this report.

## Coverage, duplicate check, disposition

Two previously inventory-only current-ToC rows, **§§15.20–15.21**, receive *selected proof-level* annotations for the passages specified above. Theorem 15.20.4's general radial uniqueness uses its existing conditional flux lemma; we did not certify the full family of Hermitian equation existence/regularity theorems. Theorem 15.21.12's compact gluing is directly checked in the indicated lines; we did not certify every earlier approximation theorem. Prior `LEDGER.md` was searched for the exact source section numbers and these distinct Sobolev and dimension-lifting claims; earlier bounded-equation and regularity findings are not counted again.

The actual ToC and cumulative section matrix have **747 unique entries**, not 747 verified sections. All previous confirmed error, proof-gap, dependency, repair and `deferred-by-user` statuses remain as recorded. Proposed mathematics here is **audit-only**: do not modify main, original statements, registry, permanent tags, or published reading edition without a separate reviewable change.
