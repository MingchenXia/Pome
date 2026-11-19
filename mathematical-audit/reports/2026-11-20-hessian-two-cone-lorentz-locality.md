# 2026-11-20: full direct audit of §§8.2 and 8.12; elementary two-Hessian cone duality and sharp diagonal bounds

## Baseline and actual scope

- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (fresh remote main check).
- **Integrated §8.2:** `docs/sections/complex-hessian-equations--the-admissible-cone/index.html`, Git blob `925e6109ab7d800cde9bec4b0487842b2e6877a8`; mathematical content lines **6–269**, including all ten numbered items (§8.2.1–10) and the stated Gårding input.
- **Integrated §8.12:** `docs/sections/complex-hessian-equations--locality-and-maxima-of-bounded-potentials/index.html`, Git blob `8750df56019c14e16704607ca20fa8b90f137fb0`; mathematical content lines **6–169**, including Proposition 8.12.1, Theorem 8.12.2, Lemmas 8.12.3–4, and Proposition 8.12.5.
- **Scope confirmation:** `docs/sections/complex-hessian-equations/index.html` (blob `5331b937ccdaba51f1ec006d5e72dc84f7addfbf`), lines 7–16 explicitly fixes a connected compact Hermitian `n`-fold and **`2 <= m < n`**. In particular, one must *not* manufacture an `m=1` counterexample to §8.2.5's `Gamma_m subset Gamma_2` argument. The note in §8.2 about `m=n` extends *algebraic* claims, not the analytic global scope.
- **No full transitive certification:** Gårding's general `m>2` facts, the viscosity/distribution equivalence in §8.2 lines 29–36, and §8.11's capacity, joint decreasing convergence, and weighted limit theorems remain prerequisites not independently proved in this session.

## Finding POME-HESS-TWO-CONE-LORENTZ-DUALITY-001

**Severity:** low. **Status:** verified repair (audit-only *partial* internal replacement of an explicitly declared external algebraic input; **not** a correction of a false printed theorem). **Scope:** `m=2` only.

**Anchors:** §8.2 lines 7–36 (cone, polar testing, concave root); equations 8.2.1 (`non-kahler-pluripotential-theory:E3011B0D`, permanent `C5A4D9AE83ED`) and 8.2.2 (`:99D246B6`, permanent `B372916B922F`); also Lemma 8.2.5 (`:53FFB5F3`, permanent `7710D01DF6F5`), lines 113–130. Affected downstream algebraic uses include §§8.2.7, 8.5 and 8.12.4–5, but only in the `m=2` specialization.

### Complete independent proof of the two-Hessian algebra

For Hermitian matrices use the real Hilbert–Schmidt pairing `<A,B> = tr(AB)` and write `s(A)=tr A`, `A_0=A-s(A)I/n`. Set
[
mathcal Q(A,B)=s(A)s(B)-operatorname{tr}(AB)
=rac{n-1}{n}s(A)s(B)-langle A_0,B_0angle,quad
mathcal Q(A)=mathcal Q(A,A).
]
Since `S_1(A)=s(A)` and `2S_2(A)=\mathcal Q(A)`, the *exact* open and closed cones are
[
Gamma_2={s(A)>0,;mathcal Q(A)>0}
={s(A)>|A|_{m HS}},qquad
overline{Gamma_2}={s(A)geq|A|_{m HS}}.
]
Here `s(A)>0` is essential: `S_2>0` alone has an unwanted opposite component.

Put `x_A=sqrt{(n-1)/n},s(A)` and `y_A=A_0`. The cone is `x_Ageq|y_A|` with future orientation. Its convexity and stability under addition of positive semidefinite matrices follow at once from the triangle inequality and `tr Bgeq|B|_{m HS}` for `Bgeq0`. A positive definite perturbation moves a closed-cone point to the interior.

For `A,B` in the future cone, put `a=|y_A|`, `b=|y_B|`. Cauchy–Schwarz and the identity
[
(x_Ax_B-ab)^2-(x_A^2-a^2)(x_B^2-b^2)=(x_Ab-x_Ba)^2
]
give the **reverse Lorentz Cauchy–Schwarz inequality**
[
mathcal Q(A,B)geqsqrt{mathcal Q(A)mathcal Q(B)}geq0.
]
In particular,
[
F(A)=sqrt{sigma_2(A)}
=sqrt{rac{mathcal Q(A)}{n(n-1)}}
]
satisfies `F(A+B)geq F(A)+F(B)` and, by homogeneity, is concave. Its exact derivative on the open cone is
[
DF_A(B)=rac{mathcal Q(A,B)}{n(n-1)F(A)}geq F(B)quad(Binoverline{Gamma_2}).
]
It is strictly positive for every nonzero `B` in the closed cone, because `x_A>|y_A|` while `x_B>0`. This provides the linearized ellipticity and polarized positivity at order two without appealing to an external Gårding theorem.

The cone is **self-dual under `\mathcal Q`**. The forward implication is the preceding inequality. Conversely, if `B` is not in the future closed cone, then either `x_B<0`, in which case the future test `(x_A,y_A)=(1,0)` has negative pairing, or `x_Bgeq0` and `\|y_B\|>x_B`, in which case the future null test `(x_A,y_A)=(1,y_B/\|y_B\|)` has pairing `x_B-\|y_B\|<0`. Perturb any boundary test into the interior if desired. Finally, the precise polarization identity is
[
rac{Awedge Bwedgeomega^{n-2}}{omega^n}
=rac{mathcal Q(A,B)}{n(n-1)}
]
for the `\omega`-Hermitian endomorphisms of `A,B`. It gives the claimed *algebraic* equivalence of the `m=2` cone condition and its smooth positive-test formulation. It **does not by itself prove** the analytic viscosity–distributional equivalence for nonsmooth potentials.

For general `m>2`, the broader Gårding input at §8.2 line 16 remains recorded as an **external dependency**, not silently certified by this special-case proof.

## Finding POME-HESS-TWO-CONE-SHARP-DIAGONAL-001

**Severity:** low. **Status:** verified conditional deduction (strict strengthening of a valid printed estimate, not a theorem error). **Anchors:** §8.2.5 source/permanent `non-kahler-pluripotential-theory:53FFB5F3 / 7710D01DF6F5`, physical lines 113–130; §8.2.7 `:25ADAEE1 / B0643A9A1173`, lines 159–179. **Hypothesis:** `n>=3`, `M` Hermitian in `\overline{\Gamma_m}`, `m>=2` (in the chapter, `2<=m<n`). For every unit vector `v`,
[
oxed{-rac{n-2}{n}operatorname{tr}M
leq langle Mv,vangle
leqoperatorname{tr}M.}
]
This refines the original `|M_{1\bar1}|<=tr M` by explicitly controlling the negative side. The two constants are simultaneously sharp **for `m=2`**. For higher `m`, no sharpness claim is made.

**Proof.** The definition `\overline{\Gamma_m}\subseteq\overline{\Gamma_2}` gives `\|M_0\|_{m HS}\leq\sqrt{(n-1)/n}\,s`, where `s=tr M\geq0`. For `P_v=vv^*`, `\|P_v-I/n\|_{m HS}=\sqrt{(n-1)/n}`. Therefore
[
langle Mv,vangle
=rac{s}{n}+langle M_0,P_v-I/nangle
inleft[rac{s}{n}-rac{n-1}{n}s,;rac{s}{n}+rac{n-1}{n}sight].
]
For any `s>0`, the closed-cone matrices `M_+=sP_v` and `M_-=(2s/n)I-sP_v` attain the respective upper and lower endpoints; both have trace `s` and `tr(M_\pm^2)=s^2`, hence `S_2(M_\pm)=0`. Adding `\epsilon I` makes them strictly `\Gamma_2`-admissible, and the bounds approach equality as `\epsilon\downarrow0`. There is no need to diagonalize `M` simultaneously with an unrelated Hessian `\Lambda`.

The independent two-sided estimate is useful for coefficientwise tests and intermediate-Hessian torsion bounds, but it does **not** upgrade the printed Lemma 8.2.7 absolute estimate to degree `r=m`: the earlier counterexample `POME-HESS-ABSOLUTE-FORM-TOP-DEGREE-FAIL-001` remains valid. Prior §8.2.5 coefficient-constant notes were checked for conceptual overlap; the present registered contribution is the explicit full Lorentz proof and the two-sided negative endpoint, not an old one-sided `|M_{1\bar1}|` estimate.

## Second directly reviewed section: §8.12

- **§8.12.1,** source `non-kahler-pluripotential-theory:C5CC915B`, tag `9989CBEEE646`, lines 10–32: strict-set locality uses a smoothed max that agrees *exactly* with the dominating approximation away from the `\epsilon_j` transition, weighted convergence from §§8.11.11–13, then `\delta\downarrow0`; no exchange of unrelated limits was inserted.
- **§8.12.2,** source `:D838B734`, tag `655B0BBF4F9C`, lines 37–60: shift by `\epsilon>0` includes the contact set `\{u=v\}` through dominated convergence against the *fixed* measure `\mu_r(u)`; on the disjoint `\{u<v\}` use strict locality. The printed inequality is not contradicted.
- **§8.12.3,** source `:B518F16E`, tag `132BB9E1B1F5`, lines 66–91: binomial expansion of the shifted `m`-product has nonnegative mixed coefficients, so the two extreme terms survive; no incorrect factor of `\binom{n}{m}` was identified.
- **§8.12.4,** source `:5AEBD34D`, tag `3A8C156268BF`, lines 96–112: reviewed the `2,d\omega\wedge d^c\omega` cross-term and degree bookkeeping, notably the `R_{m-1},dd^c\omega^{n-m}` term. Its weighted convergence depends explicitly on §8.11.10–12, not independently certified here.
- **§8.12.5,** source `:B038046B`, tag `BB9187C844DA`, lines 114–170: the truncation contradiction uses `0\leq w-u\leq s`, `mCs<1`, and `\mu_0|_U=\omega^n|_U`; it correctly needs the **degree less than `m`** absolute form estimate of §8.2.7, not a false degree-`m` extension. The torsion bound is only conditional on the weighted-capacity prerequisites above. No newly confirmed false theorem or independent proof gap was established by this direct reading.

## Classification, dependencies, and edit boundary

- **Confirmed errors:** none established in these sections.
- **Verified repair:** POME-HESS-TWO-CONE-LORENTZ-DUALITY-001, algebra only at `m=2`; no claim to solve the general `m` Gårding proof or the viscosity/distributional input.
- **Verified conditional deduction:** POME-HESS-TWO-CONE-SHARP-DIAGONAL-001; sharp for `m=2`, not claimed sharp for `m>2`.
- **Genuine external dependencies still open:** Gårding theory beyond this special case, classical viscosity/distributional equivalence, and the actual §§8.11.10–13 weighted capacity and monotone Hessian products. These inputs are logically separate from the user-excluded Demailly programme.
- **Historical attribution:** retained unchanged in the source reading edition.
- **Coverage increment:** **2 whole sections read directly (§§8.2, 8.12); 1 contextual §8.1; 0 complete upstream chains**. Previous partial visits of §§8.2 and 8.12 are retained without a new first-visit claim.
- **Proposed source correction:** none compulsory; optional future PR could insert the elementary `m=2` Lorentz proof as a clearly scoped supplement near §8.2 and the improved lower coefficient bound as a remark after §8.2.5. This audit does not change the actual reading edition.
- **Exclusion:** the Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes are **deferred-by-user, not resolved/certified**. No review of their prerequisites was undertaken.
- **Operations:** mathematical Markdown audit only; no software tests, builds, GitHub Actions, publication, main/source/body/registry/canonicalization/tag modifications or merge.
