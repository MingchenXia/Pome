# 2026-11-20 — Supported pluriharmonic currents: positivity is essential; Hermitian Fredholm and adjoint audit

**Production baseline:** `main` `b6933b772f41b45918f7e25ed1afbbb1fd892272` (read freshly). **Classification:** `POME-PLURI-HYPERSURFACE-SIGNED-MIXED-001` — **low / verified conditional deduction**, explicitly a counterexample to *dropping* a printed hypothesis, **not** an error in the printed Lemma 11.22.1.

## Exact integrated reading scope

All mathematical paragraphs, displays, statements and printed proofs of these three current reading-edition sections were read directly:

| Section and current `main` path | Blob SHA | Physical mathematical lines | Stable source / permanent tags |
|---|---|---|---|
| §11.22 `docs/sections/gauduchon-metrics-and-linear-mass--pluriharmonic-currents/index.html` | `046c12d159f8aaeff268c57d822253da11ed41ba` | 7–133 | Lemma 11.22.1 `non-kahler-pluripotential-theory:9611A9E5` / `D9A37BB4C36B` (11–35); Lemma 11.22.2 `33E1F4AD` / `25BD2AAB112A` (44–60); Lemma 11.22.3 `004EE9C6` / `40BA141971D9` (68–96); Lemma 11.22.4 `03684AFE` / `3CD7629C6061` (105–122) |
| §11.24 `docs/sections/gauduchon-metrics-and-linear-mass--fredholm-theory-for-a-continuous-hermitian-form/index.html` | `8fd933d027ecdba0c2df8efe7524e3984613857a` | 7–69 | Lemma 11.24.1 `2FF004A4` / `DEA6C8EFE702` (11–67); estimate tags `616C6C2B269A`, `88F9E749216F`, `0EB6296FE2B1` |
| §11.25 `docs/sections/gauduchon-metrics-and-linear-mass--limits-of-adjoint-measures/index.html` | `48117e4e5901381d5ae692cfd29f2cf5f1325abc` | 7–27 | Proposition 11.25.1 `A07C226C` / `3E5CF25D6E23` (11–21) |

**Historical scope distinction:** §§11.22.1–2 and 11.22.4, 11.24.1 and 11.25.1 have previous selected-input/checkpoint history. This is a current *whole-text direct review* of three sections, **not** a claim of first-ever visits, transitive proof-chain certification or a repeated discovery of the earlier higher-dimensional fiber-Liouville and adjoint-density results. Previously deferred analytic programmes remain deferred.

## New finding: the positivity condition in Lemma 11.22.1 is indispensable

Lemma 11.22.1 assumes that a positive `(q,q)` current `R` is supported on a smooth hypersurface `D` and that `dd^cR` has order zero; it concludes `R=j_*S` for a positive current `S` on `D`. The following **compact, order-zero, real `dd^c`-closed counterexample** shows that the conclusion fails even under the stronger condition `dd^cR=0` if the positivity of `R` is omitted.

Let `E=ℂ/(ℤ+iℤ)`, `X=E_z×E_w`, and `D={z=0}×E_w`, with inclusion `j:D→X`. Write `δ_0(z)` for the periodic Dirac scalar distribution in the first coordinate, constant in the second coordinate. In terms of the globally defined holomorphic forms `dz,dw`, put

```tex
R=i\,\delta_0(z)\bigl(dz\wedge d\bar w+dw\wedge d\bar z\bigr).
```

Up to the harmless positive normalization of the flat Haar volume, this is a **real** `(1,1)` current of **order zero** whose support is contained in `D`. Indeed, complex conjugation exchanges the two summands, with the wedge signs cancelling conjugation of `i`. Since the distribution has no `w` dependence,

```tex
\partial\bigl(\delta_0(z)\,dz\wedge d\bar w\bigr)=0,
\qquad
\bar\partial\bigl(\delta_0(z)\,dw\wedge d\bar z\bigr)=0.
```

The first identity holds because `∂δ_0(z)` has a factor `dz`; the second because `\bar∂δ_0(z)` has a factor `d\bar z`. Consequently `∂\bar∂R=0`, hence `dd^cR=0`. No limiting or approximation argument is involved.

On the other hand, `R` has **only normal–tangential mixed coefficients**. Every current `j_*S` of bidegree `(1,1)` arising from a scalar current `S` on `D` satisfies `(j_*S)(\alpha)=S(j^*\alpha)=0` for every smooth test `(1,1)` form `\alpha` all of whose monomials contain a `dz` or `d\bar z` factor. Taking a smooth test form proportional to `i(dz\wedge d\bar w+dw\wedge d\bar z)` yields a nonzero pairing with `R`, but its pullback to `D` is zero. Thus **`R\neq j_*S` for every current `S` on `D`**.

Finally, the Hermitian coefficient matrix of `R` has zero diagonal and a nonzero off-diagonal entry; testing against the vectors `(1,1)` and `(1,-1)` shows opposite signs, so `R` is **not positive**. This is exactly the hypothesis used in the printed proof, lines 23–33, to remove mixed normal coefficients by the positive-semidefinite matrix inequality. The printed lemma is not contradicted.

**Affected reasoning:** Lemma 11.22.1 and any use of its hypersurface-supported descent require *positivity*, not just order-zero and pluriharmonicity. The current section retains positivity throughout; no incorrect application was identified in the passages checked. **Proposed correction:** no necessary change to the theorem; an optional note can add this mixed-coefficient counterexample as a sharpness warning, preserving existing tags and historical attribution. No source/registry/body change is authorized here.

## Checks on the other proofs in this rotation

- **§11.22.2, lines 52–59:** the compact Kähler hypothesis is needed for the `dd^c` lemma for **currents** used to write the closed pushforward `F_*(Ω^{N-p})=γ+dd^cU`. Since `S` is smooth, `⟨U,dd^cS⟩` is legitimate; the final bound uses the positive trace of `S`. The full underlying Kähler current `dd^c` lemma is **not** certified here.
- **§11.22.3, lines 73–96:** the Hodge heat flow preserves type, reality and `dd^c` closure by Kähler commutation. Its `C^0` uniform convergence for continuous data is justified through the Weitzenböck bound; restoring positivity by `cε_tω^p` requires **closed** Kähler `ω`. This is Hodge heat smoothing, **not** the user-excluded Demailly approximation programme.
- **§11.22.4, lines 110–132:** zero vertical trace plus positivity kills the vertical and mixed measure coefficients. The remaining coefficients are harmonic in the fiber and, after positive base testing, constant on `ℂ` or on compact connected Riemann-surface fibers. The bidisc non-descent example correctly shows why an arbitrary disc fiber cannot be substituted. Existing higher-dimensional positive-pluriharmonic Liouville work is **not** counted again.
- **§11.24.1, lines 21–67:** checked the frozen-coefficient `W^{2,p}` estimate, positive-gradient-contact/ABP sign, strong maximum principle for `p>2n`, uniform `L_s-1` estimate and continuity method. The argument's reliance on smooth comparison and local nondivergence-form elliptic estimates does not yield an endpoint `p=2n` statement. Earlier reported endpoint and adjoint-stability analyses remain unchanged, not recounted.
- **§11.25.1, lines 11–26:** the constant mass `M` follows **conditionally** from Gauduchon persistence and the cited mass-variation theorem. Weak continuity is the bounded Bedford–Taylor product capacity statement; no general assertion of approximation-independent adjoint measures on arbitrary Hermitian backgrounds is made. The section explicitly leaves that general question open.

**Statuses:** one **low / verified conditional deduction** (hypothesis sharpness, not an original theorem error); zero new confirmed errors, zero new proof gaps or genuine duplications; the Kähler current `dd^c` lemma, elliptic theory and bounded capacity-product continuity are still **upstream dependencies not transitively certified**. The excluded Demailly approximation/regularization, Bergman, `L^2`, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes stay **deferred-by-user**.

**Audit boundaries:** +3 complete **direct mathematical section readings** (§§11.22, 11.24, 11.25), +0 fully certified transitive proof chains. No tests, builds, CI, website publication, original source/body edits, registry/canonicalization changes, permanent-tag changes, branch merge or PR creation.
