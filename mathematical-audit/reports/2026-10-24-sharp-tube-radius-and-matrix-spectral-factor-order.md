# Audit of selected complex-geometric sections: a sharp tubular subharmonic radius and matrix spectral-factor order

**Review date:** 2026-10-24 (Asia/Shanghai).  
**Reviewed Pome `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Reading edition:** the actual `docs/sections/.../index.html` files at the blob SHAs stated below, not the original source theorem numbers.  
**Classification:** two *verified conditional deductions*, not allegations of a false theorem.  
**Scope:** first selected proof-level inspection of §§9.19 and 9.21–9.24, previously inventory-only in the coverage matrix. No full section or upstream analytic chain certified.

The owner-excluded Demailly approximation/regularization and its dedicated Bergman, `L²`, Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof programme is **deferred-by-user**, not reopened or certified. The weighted `\bar\partial` existence theorem encountered in §9.21.1 is an **unverified upstream input**, not an invitation to restart that excluded programme.

## POME-TUBE-RADIUS-SHARP-001 — verified conditional deduction / low

**Source and anchor:** Proposition 9.19.1, source label `klimek-pluripotential-theory-7EB9EC12`, permanent tag `EF227A55DB12`, integrated `docs/sections/boundary-distance-counterexamples-in-higher-dimension/index.html`, main blob `e078f8041dbae929c9d2076e62a72326622c158d`, physical lines **8–35** (definition and Laplacian at 14–30; exterior collar at 32–34).

**Claim (sharpening of the printed sufficient radius):** Let `m≥3`, `R>0`, and `0<r<R`. In `R^m=R²×R^{m-2}`, write
[
C_R={(Rcos t,Rsin t,0):tinmathbb R},qquad
ho=(x_1^2+x_2^2)^{1/2},qquad
s(x)=operatorname{dist}(x,C_R)=sqrt{(ho-R)^2+|y|^2}.
]
Put `T_r={s<r}` and `D_r={s>r}`, and set
[
r_{mathrm{crit}}=rac{m-2}{m-1}R.
]
Then:

1. The function `-dist(·,∂T_r)=s-r` is subharmonic **throughout `T_r` if and only if `r≤r_crit`**.
2. The boundary-distance function `dist(·,∂D_r)=s-r` is subharmonic on **some full interior collar `r<s<r+δ` if and only if `r<r_crit`**.

In both assertions `D_r` is connected for `m≥3`, and `T_r` is bounded, connected and nonconvex; its complement is likewise nonconvex. Hence the sufficient condition `R>2r` used in the printed proposition is sharp for `m=3` only up to inclusion of the endpoint, and can be improved in higher dimensions. Nothing here contradicts Proposition 9.19.1.

**Proof.** Since `r<R`, on `T_r` one has `rho>R-r>0`, and the nearest point on `C_R` is unique away from the core circle. Extending the segment from its nearest circle point to normal length `r` remains in the half-space `rho>0`; the one-Lipschitz inequality for `s` and the extended segment give
[
operatorname{dist}(x,partial T_r)=r-s(x).
]
Away from `C_R`, cylindrical coordinates yield
[
Delta s
=left(partial_{hoho}+rac1hopartial_ho+Delta_yight)s
=rac{m-2}{s}+rac{ho-R}{ho s}
=rac{m-1-R/ho}{s}.
	ag{1}
]
The smallest possible `rho` in `T_r` is approached from above at the inward radial normal with `rho=R-r`. Thus (1) is nonnegative everywhere in the smooth locus of `T_r` exactly when
[
R-rgerac{R}{m-1}
iff rle r_{mathrm{crit}}.
]
At the critical endpoint, `rho>R-r` in the interior makes (1) strictly positive away from `C_R`. To cover that core without assuming removability, set `s_epsilon=(s²+epsilon²)^{1/2}`. Direct differentiation gives
[
Delta s_epsilon
=rac{m-1-R/ho}{s_epsilon}+rac{epsilon^2}{s_epsilon^3}ge0
quad	ext{on }T_r
]
whenever `r≤r_crit`. Since `s_epsilon↓s` locally boundedly, the distributional decreasing-limit theorem implies `s-r` is subharmonic everywhere in `T_r`.

If `r>r_crit`, select `rho` strictly between `R-r` and `R/(m-1)`, put `y=0`, and observe `s=R-rho<r`. Formula (1) is **negative at this smooth interior point**, disproving subharmonicity. This proves (1).

For the exterior collar, take `delta>0` small enough that `r+delta<R`. Normal-segment shortening shows `dist(x,∂D_r)=s-r` throughout `r<s<r+delta`. If `r<r_crit`, take `delta<r_crit-r`; then `rho>R-r-delta>R/(m-1)` and (1) is positive there. Conversely, if `r≥r_crit`, every such collar contains inward-radial points with `y=0`, `s=r+epsilon`, `rho=R-r-epsilon>0` and `rho<R/(m-1)`, at which (1) is negative. This proves (2). The path argument for connectedness of `D_r` in the printed proof requires only `r<R` and `m-2≥1`.

**Correction proposal:** an optional sharp-radius remark after Proposition 9.19.1, preserving its label, attribution, radius-specific example and all permanent tags. **No source/body change is applied.** Dependents: geometric boundary-distance counterexamples and their dimension dependence. The only analytical limiting input above is the standard elementary monotone limit for subharmonic functions, independently checkable here using `s_epsilon`.

## POME-CIRCLE-SPECTRAL-FACTOR-ORDER-001 — verified conditional deduction / low

**Source and anchor:** Theorem 9.23.1, source label `klimek-pluripotential-theory-02D391FB`, permanent tag `35AF621E1787`, integrated `docs/sections/smooth-positive-matrix-factorization-on-the-circle/index.html`, main blob `04780d065ee474f3bb3255db297ac435e00485a1`, physical lines **7–69**. The Hilbert minimizer and constant boundary matrix appear at lines 28–34 and 58–66; unitary uniqueness at lines 68–69.

**Claim (canonical matrix and its exact determinant):** With normalized Haar measure `dm=dtheta/(2pi)`, for a smooth strictly positive Hermitian matrix symbol `W:S¹→Herm_m` (`m≥2`), let `A(W)` be the matrix of minimal weighted Hardy norms:
[
v^*A(W)v
=min_{substack{fin H^2(S^1,mathbb C^m)\ f(0)=v}}
int_{S^1}f^*Wf,dm.
	ag{2}
]
Then `A(W)` is positive definite, and for any outer spectral factor `W=H^*H` holomorphic and invertible on the closed disc,
[
A(W)=H(0)^*H(0),qquad
oxed{logdet A(W)=int_{S^1}logdet W,dm.}
	ag{3}
]
For any two such symbols and `0≤t≤1`,
[
W_1le W_2implies A(W_1)le A(W_2),qquad
A(tW_1+(1-t)W_2)ge tA(W_1)+(1-t)A(W_2).
	ag{4}
]
The inequalities use the Loewner order. Furthermore, if `W≥cI`, then
[
cIle A(W)le int_{S^1}W,dm;
]
in particular `W≤CI` also gives `A(W)≤CI`.

**Proof.** The proof of Theorem 9.23.1 obtains the unique minimizer `f_v=Fv` of (2), where `F(0)=I`, and proves by variation and Fourier sign control that
[
F^*WF=A
quad	ext{on }S^1
]
for a positive constant Hermitian matrix `A`. Integrating shows `v^*Av` is exactly the minimum (2). The proof also shows `F` is invertible on the *entire closed disc*, by a Blaschke-zero cancellation argument, and constructs `H=A^{1/2}F^{-1}`. Hence `H(0)=A^{1/2}`. Every other admissible `H` differs by a constant left unitary, so `H(0)^*H(0)=A` is independent of the factor.

Since `det H` is a nowhere-zero holomorphic function on the simply connected disc, `log|det H|` is harmonic and continuous on its closure. The mean-value property and `det W=|det H|^2` yield
[
intlogdet W,dm
=2intlog|det H|,dm
=2log|det H(0)|
=logdet A.
]
This proves (3). Monotonicity follows by comparing the integrands for **each fixed admissible `f`** before minimizing. For concavity, for each `v`,
[
egin{split}
v^*A(tW_1+(1-t)W_2)v
&=inf_{f(0)=v}left(tQ_{W_1}(f)+(1-t)Q_{W_2}(f)ight)\
&ge tinf_{f(0)=v}Q_{W_1}(f)
 +(1-t)inf_{f(0)=v}Q_{W_2}(f).
end{split}
]
This establishes (4) for all `v`. If `W≥cI`, Parseval gives `Q_W(f)≥c\|f\|_2^2≥c|f(0)|^2`. Testing (2) with the constant function `f=v` gives `A(W)≤∫W,dm`. All assertions follow.

**Scope:** the proof uses the exact smooth, positive, closed-disc-invertible factor constructed in §9.23.1; it does not assert factorization for merely measurable symbols. The spectral-factor construction's Toeplitz coercivity, difference-quotient regularity, elimination of interior zeros, and unitary uniqueness were **directly checked**, but the entire underlying Hardy-space analytic framework has not been separately certified. This is **not** a false Pome theorem. **Correction proposal:** optional supplementary corollary after Theorem 9.23.1, retaining the original theorem/tag and normalized angular measure. Dependents: circle Riemann–Hilbert and boundary-matrix normalizations, spectral-factor stability.

## Other selected integrated proof checks — no new defect certified

| Section | Actual inspected passage, stable source and status |
| --- | --- |
| **9.21** | `docs/sections/hyperconvexity-and-the-space-of-holomorphic-functions/index.html`, blob `24d99bc46c2bd2bd0a785e28d545193f0749e708`: Lemma 9.21.2 tag `8BD46FA4016F`, lines 41–57 (Hilbert restriction compactness, rank-`N_m` polynomial approximation and converse min-max); Proposition 9.21.3 lines 62–99 (three-ball interpolation and basis bounds); Proposition 9.21.4 lines 104–133 (tail envelope and holomorphic hull). The `\bar\partial` existence theorem quoted in Lemma 9.21.1, lines 20–35, was **not reopened** and is not certified by these selected checks. |
| **9.22** | `docs/sections/a-smooth-boundary-for-a-proper-biholomorphic-image/index.html`, blob `1279ba00791fa992f753ddd35a63cfc0fa36973f`: Lemma 9.22.1 source `klimek-pluripotential-theory-D16FE002`, permanent `9D4AAB621920`, lines 7–45 (uniform (C^m) shear-band estimates and local level-set transport); Theorem 9.22.2 source `klimek-pluripotential-theory-BDF5266C`, permanent `CE10A564601F`, lines 49–96 (shrinking inverse shears, local domain convergence, and both inverse identities). Selected estimates matched the displayed hypotheses; no complete proof certificate claimed. |
| **9.24** | `docs/sections/smooth-green-functions-on-strongly-convex-domains/index.html`, blob `e19df8fd1692c138eddd5f2fff8822de588e03ec`: Lemma 9.24.1 tag `EEFBD40AC261`, lines 10–50 (almost-analytic reflection estimates); Lemma 9.24.2 tag `CB9F3D62BE1C`, lines 54–84 (smooth stationary lift and positivity of `g·f'`); Lemma 9.24.3 tag `106A14BC1AFE`, lines 88–102 (projected coercivity); Proposition 9.24.4 tag `495B56CEC1A8`, lines 106–172 (linearized kernel/coercivity and Sobolev inverse); Theorem 9.24.5 tag `A2E9734AB1F5`, lines 176–202 (off-diagonal inverse-function argument and Green identity). Theorem 9.20.5, maximality and Green boundary comparisons remain **conditional internal dependencies**, not independently certified here. |

**Coverage accounting:** §§9.19, 9.21, 9.22, 9.23 and 9.24 transition from *inventory only* to **selected statement/proof passages inspected**. §9.20 is context only and was already audited earlier. Neither these sections nor any dependency graph is fully certified. Existing ledger statuses and the actual **747** table-of-contents rows remain intact.

**No** software test, full build, CI workflow, formal proof assistant, website publication, original source update, canonical registry edit, permanent-tag rewrite, or merge was performed in this mathematical review. Only the separate audit report, existing audit ledger, matrix and latest checkpoint are proposed for the review branch.
