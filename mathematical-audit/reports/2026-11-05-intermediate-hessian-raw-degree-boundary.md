# Sharp failure of the absolute-form coefficient bound at the intermediate Hessian degree

**Review date:** 2026-11-05. **Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Stable finding ID:** `POME-HESS-ABSOLUTE-FORM-TOP-DEGREE-FAIL-001`.
**Severity:** low. **Status:** verified conditional deduction (self-contained algebraic countermodel to an **unprinted stronger assertion**, not an error in the printed lemma). No complete theorem-chain or section certification.

## Integrated reading-edition anchors and hypotheses

1. `docs/sections/complex-hessian-equations/index.html`, physical line **7**: the chapter's analytic standing regime is `2 <= m < n` on a Hermitian manifold, so intermediate Hessian cone forms need not be semipositive.
2. `docs/sections/complex-hessian-equations--the-admissible-cone/index.html`, main blob `925e6109ab7d800cde9bec4b0487842b2e6877a8`, physical lines **7–16** (the unnormalized `S_j`, the open `Gamma_m` and its closed cone), **155–164** (the *strict* degree condition `0 <= r < m`), **169–179** (the coefficient proof). Lemma **8.2.7** is source `non-kahler-pluripotential-theory:25ADAEE1`, permanent tag **`B0643A9A1173`**.
3. Direct dependent step, `docs/sections/complex-hessian-equations--bounded-potentials-and-recursive-hessian-currents/index.html`, blob `117b866408974cdf706bf305df75e35e1b8affde`, Proposition **8.9.3**, source `non-kahler-pluripotential-theory:354EA0C7`, permanent **`EB2FA13CDDE0`**, lines **46–56, 61–78**: the absolute-form estimate is invoked *only* for `q <= p < m`; the unwedged `D_m` is asserted distributional, not coefficient-measure bounded.
4. Direct dependent distinction, `docs/sections/complex-hessian-equations--local-capacities-and-decreasing-products/index.html`, blob `115d285f6b1f76d284463c396e7e87db2b9dbdc3`: Lemma **8.11.10**, source `non-kahler-pluripotential-theory:FA167F60`, permanent **`348FF027ECE6`**, lines **239–255**, uses `q <= p < m`; Theorem **8.11.12**, source `non-kahler-pluripotential-theory:B227378C`, permanent **`C044CD1C65C4`**, lines **281–292**, claims weak measure-coefficient convergence only for `p < m`.

The mathematical question is whether one may harmlessly extend Lemma 8.2.7 to `r=m`, with a uniform coefficient constant depending only on `n,m,Xi,omega`, for `Gamma_m` forms. The answer is **no**, for every `2 <= m < n`; this is an endpoint-obstruction check, not a proposed change to the printed assertion.

## Explicit compact smooth model

Work on the flat complex torus `X=(C/(Z+i Z))^n`. Let `beta_j` be the standard smooth positive constant real `(1,1)` form in coordinate `j`, with `omega=sum_{j=1}^n beta_j`. These forms commute under wedge and satisfy `beta_j^2=0`. For `0<epsilon<1/m`, set

\[
 t_\epsilon=-\frac1m+\epsilon,\qquad
 \alpha_\epsilon=\sum_{j=1}^{m}\beta_j+t_\epsilon\beta_{m+1},\qquad
 \Xi=\beta_{m+1}\wedge\cdots\wedge\beta_n.
\]

The fixed `Xi` is a smooth decomposable **strongly positive** complementary `(n-m,n-m)` form. All `alpha_epsilon` are smooth closed real `(1,1)` forms, with uniformly bounded coefficients, and their eigenvalues relative to `omega` are

\[
 \lambda_\epsilon=(\underbrace{1,\ldots,1}_{m},t_\epsilon,
                 \underbrace{0,\ldots,0}_{n-m-1}).
\]

For every `1 <= j <= m`, the exact elementary-symmetric formula, with the zeros included, is

\[
 S_j(\lambda_\epsilon)
 =\binom mj+t_\epsilon\binom m{j-1}
 =\binom mj\left(1-\frac{j}{m(m-j+1)}
                       +\frac{j\epsilon}{m-j+1}\right).
\]

For `j<m`, this is strictly positive even at `epsilon=0`, since `m(m-j+1)>j`. At the top degree, `S_m(\lambda_\epsilon)=1+mt_\epsilon=m\epsilon>0`. Thus every `alpha_epsilon` belongs to the **open** `Gamma_m(omega)`, and the limit `alpha_0` belongs to its closed cone.

Write `B=beta_1 wedge ... wedge beta_n`. Since `Xi` already contains the last `n-m` coordinate factors, wedge expansion gives the *exact* identities

\[
 \alpha_\epsilon^m\wedge\Xi=m!\, B,\qquad
 \alpha_\epsilon^m\wedge\omega^{n-m}
  =m!(n-m)! S_m(\lambda_\epsilon)\,B
  =m!(n-m)!m\epsilon\,B .
\]

If the asserted absolute coefficient inequality were extended from `r<m` to `r=m`, choose all `m` inputs equal to `alpha_epsilon`. Then its putative constant would have to satisfy

\[
 C_{n,m,\Xi}\ \ge \frac{|\alpha_\epsilon^m\wedge\Xi|}
      {(m\alpha_\epsilon)^m\wedge\omega^{n-m}}
 =\frac1{m^{m+1}(n-m)!\epsilon}\longrightarrow\infty.
\]

All arguments use a *fixed* background `omega`, a *fixed* strongly positive test form `Xi`, and uniformly bounded, smooth, strictly `m`-admissible inputs. Consequently **no finite constant** of the printed kind can work at `r=m`. The simplest instance is `n=3,m=2`, with eigenvalues `(1,1,-1/2+epsilon)`, where the ratio is `1/(8 epsilon)`.

In fact the closed-cone limit already displays a stronger qualitative separation:

\[
 \alpha_0^m\wedge\omega^{n-m}=0,
 \qquad \alpha_0^m\wedge\Xi=m!B\ne0.
\]

Thus **zero top scalar m-Hessian trace does not force the unwedged m-fold form to vanish** for intermediate Hessian cones. This is possible because `Gamma_m` contains forms that are not semipositive; it does not contradict the nonnegativity of the scalar `m`-Hessian wedge. For `m=n`, where the relevant cone is positive semidefinite and `Xi` has degree zero, this particular obstruction does not apply.

## Relationship to the printed arguments and proposed action

- Lemma **8.2.7** is **correct as printed**: its strict requirement `r<m` is **necessary** for a general pointwise coefficient estimate of this form in the chapter's intermediate regime. No printed theorem is falsified and no proof replacement is required.
- Proposition **8.9.3** uses the lemma at strictly smaller degrees and carefully separates the unwedged top-degree distributional current. Lemma **8.11.10** and Theorem **8.11.12** also retain this distinction. This model independently confirms the importance of that separation, **not** the validity of all their analytic existence, approximation or convergence steps.
- **Logical limitation:** a countermodel among arbitrary smooth `Gamma_m` forms does not independently disprove a stronger measure-coefficient statement restricted to the special subclass `omega+dd^c u` for *globally bounded potentials*. It proves only that the existing **pointwise** cone estimate cannot supply such a statement.
- **Proposed optional editorial clarification**, without changing theorem hypotheses, source attribution or tags: append after Lemma 8.2.7 a note that the strict `r<m` restriction is sharp, with the above diagonal `Gamma_m` family; maintain the explicit `p<m` versus `p=m` typing in §§8.9 and 8.11.

No user-excluded Demailly approximation/regularization, Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof-completion was examined. No false theorem, general current-theoretic claim, complete section, tests/build/CI, or formal verification is asserted.
