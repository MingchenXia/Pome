# 2026-10-25 — exponential damping against non-pluripolar measures: capacity-controlled rates and a fixed logarithmically slow example

**Reviewed integrated `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch before this increment:** `e5cd7f073f0a34a5ceab7fd0e89c561a646d3145`. **Session began:** 2026-10-25 14:53 Asia/Shanghai. The mathematical statements below concern Pome's current reading edition, **not** an audit of Demailly approximation or regularization.

## Exact source anchors and review boundary

- `docs/sections/plurisubharmonic-functions-and-singularities--integration-against-non-pluripolar-measures/index.html`, main blob `15c449ab02d6f8df98edfa07f5286af7ac8e72d1`: §5.44.5, source `non-kahler-pluripotential-theory`, permanent tag `D260E972F57C`, reader label `1D86C745`, **lines 48–86**; in particular capacity splitting (65–78) and the `L^p` density assertion (80–86). Related selected mathematical checks: §5.44.2 (11–30), §5.44.4 (37–43), §5.44.7 (92–165), §5.44.10 (174–199), §5.44.12 (215–263). These **are not** whole-section or transitive proof certifications.
- `docs/sections/plurisubharmonic-functions-and-singularities--hermitian-capacity/index.html`, blob `77a9098e9bb922425d11c5b04d8927a3997ad44e`: §5.29.2, permanent tag `5CEF121C5391`, lines **36–77**; Eq. 5.29.4 tag `3EF8F920CDD3`, lines **41–44**, gives `Cap_omega({v<-t})<=C/t` for all normalized `omega`-psh `v` and `t>1`.
- `docs/sections/plurisubharmonic-functions-and-singularities--normalized-compactness/index.html`, blob `d7ff8eafea43197c77de4bfd335bed0764ab4f69`: §5.25.1 permanent `45B3FA75B7BD` (14–26), §5.25.2 permanent `FC59B7D406A3` (32–51), §5.25.3 permanent `0AD144F69807` (57–63). Checked the moving-point upper limit, connected finite-ball propagation, and decreasing-limit `L^1` argument.
- `docs/sections/plurisubharmonic-functions-and-singularities--uniform-exponential-integrability/index.html`, blob `d961c0412577bb6abdb8455efc44e2f35760c55c`: §5.26.2 permanent `88C7A8DCE36E`, lines **18–41**, including the exact dyadic weighted-sum contradiction. Its qualitative one-function Skoda integrability input is **not** independently reproved here.
- `docs/sections/plurisubharmonic-functions-and-singularities--plurisubharmonic-potentials/index.html`, blob `(dependency context only)`, line 7 stipulates **connected compact** `X` and the smooth-background/Hermitian conventions. The example below uses `X=P^1`.

**Statuses:** Both findings below are **low / verified conditional deduction** from the printed and specifically named capacity/psh inputs. Neither asserts an error in the printed Lemma 5.44.5. The excluded Bergman/`L^2`/Ohsawa–Takegoshi/multiscale/positivity-loss programme, and all Demailly approximation/regularization work, remains **deferred-by-user**, not certified.

## POME-CAP-DOM-EXP-MODULUS-001 — a quantitative modulus under capacity domination

**Status:** verified conditional deduction. **Severity:** low. **Hypotheses:** Let `X` be a connected compact complex manifold, `omega` a fixed Hermitian form, and `mu` a finite positive measure satisfying for every Borel set `E`
[
  mu(E)le A,operatorname{Cap}_{omega}(E)^{gamma}
  qquad(A<infty, gamma>0).
]
Let `v` range over `PSH(X,omega)` with `sup_X v=0`. For `0<lambda<=1/2` there exists a constant independent of `v` and `lambda` such that
[
 oxed{int_X(1-e^{lambda v}),dmu le C_{mu,omega,gamma}
 egin{cases}
 lambda^gamma,&0<gamma<1,\
 lambda(1+|loglambda|),&gamma=1,\
 lambda,&gamma>1.
 end{cases}}
]

**Proof.** Set `T=-v>=0`, allowing `T=+infty` on the polar set. Since the assumed domination forces `mu` to vanish on pluripolar sets, Tonelli's theorem gives
[
 int_X (1-e^{-lambda T})dmu
   =lambdaint_0^infty e^{-lambda t},mu(T>t),dt.
]
By §5.29.4, for `t>1`, `mu(T>t)<=A(C_0/t)^gamma=:Dt^{-gamma}`; for `0<t<=1`, the tail is at most `M=mu(X)`. Therefore
[
 I_lambdale lambda M+
 lambda Dint_1^{1/lambda}t^{-gamma}dt+
 lambda Dint_{1/lambda}^infty e^{-lambda t}t^{-gamma}dt.
]
The last term is at most `D lambda^gamma` times `int_1^infty e^{-s}s^{-gamma}ds`. The middle term equals `O(lambda^gamma)` for `gamma<1`, `O(lambda log(1/lambda))` for `gamma=1`, and `O(lambda)` for `gamma>1`. This proves all cases uniformly, including for arbitrary families of normalized potentials (no extraction of sequences). `\square`

**Proposed optional addition:** State the tail-to-Laplace estimate after Lemma 5.44.5, distinctly from its `L^p)-density linear bound. **Affected dependents:** estimates for vanishing exponential weights against measures controlled by Hermitian capacity. This is an *upper-bound deduction*, not a statement of optimality within the entire capacity-dominated class.

## POME-NONPOLAR-SLOW-EXP-001 — one fixed absolutely continuous non-pluripolar measure has logarithmically slow decay

**Status:** verified conditional deduction. **Severity:** low. **Hypotheses:** In the same normalization as the current Pome `P^1` computations, take the Fubini–Study form
[
 omega_{mathrm{FS}}=dd^clog(1+|z|^2)
]
on the affine chart and any `0<a<1`. Define
[
 v_a(z)=alograc{|z|^2}{1+|z|^2},qquad
 omega_{mathrm{FS}}+dd^cv_a=(1-a)omega_{mathrm{FS}}+a[0]ge0,
 quadsup_{mathbb P^1}v_a=0.
]
Let `t=-log|z|` on `0<|z|<e^{-e}`. Define **one fixed** probability measure `mu` by pushing forward
[
  dmu=rac{dt}{t(log t)^2},rac{dartheta}{2pi},
  qquad tin[e,infty),quad 0leartheta<2pi,
  quad z=e^{-t+iartheta},
]
and put zero mass elsewhere. The mass is one because `int_e^infty dt/[t(log t)^2]=1`. The measure is absolutely continuous with respect to Euclidean area on the punctured chart, has **no atom at the origin**, and hence charges no pluripolar set.

Then the **exact logarithmically slow asymptotic** holds:
[
 oxed{lim_{lambdadownarrow0}log(1/lambda)
   int_{mathbb P^1}(1-e^{lambda v_a}),dmu=1.}
]
Consequently no estimate `O(lambda^delta)` for any `delta>0` follows merely from a measure being finite and non-pluripolar, **even for a fixed normalized potential**. This does **not** contradict the printed qualitative Lemma 5.44.5 or its additional `L^p) (`p>1`) density hypothesis.

**Proof.** Writing `L=1/lambda`,
[
 -v_a(e^{-t+iartheta})
 =aig(2t+log(1+e^{-2t})ig).
]
Thus
[
 I_lambda=int_e^infty
 ig(1-e^{-alambda(2t+log(1+e^{-2t}))}ig)
 rac{dt}{t(log t)^2}.
]
For the upper bound split at `L`. On `[e,L]`, use `1-e^{-x}<=x` and `2t+log(1+e^{-2t})<=3t`:
[
 int_e^L(cdots)rac{dt}{t(log t)^2}
 le3alambdaint_e^Lrac{dt}{(log t)^2}
 =O((log L)^{-2}).
]
The last estimate follows by splitting at `sqrt L`: the first piece is `O(sqrt L)`, the second `O(L/(log L)^2)`. On `[L,infty)`, the integrand is at most one, and the remaining probability is exactly `1/log L`. Therefore `limsup(log L)I_{1/L}<=1`.

Conversely, for any fixed `M>1`, on `t>=ML` the integrand is at least `1-e^{-2aM}`. Consequently
[
 I_{1/L}ge rac{1-e^{-2aM}}{log(ML)}.
]
It follows that `liminf(log L)I_{1/L}>=1-e^{-2aM}` for every `M`. Let `M` tend to infinity to obtain the lower bound one. `\square`

**Proposed optional addition:** Add this explicit distributional counterexample to distinguish mere finite non-pluripolarity from any **uniform algebraic convergence rate** in §5.44.5. **Affected dependents:** arguments attempting quantitative exponential damping using only non-pluripolarity must acquire quantitative measure domination or an `L^p) density hypothesis. **Not** a counterexample to Pome's original lemma.

## Audit boundary and unverified prerequisites

The directly inspected §5.25 compactness proof uses connectedness and the local Hartogs alternative; the §5.26 dyadic construction correctly prevents an identically `-infty` limit through uniform `L^1` control. The §5.44.5 sublevel/capacity split is valid, and the displayed `p>1` restriction is essential for its final Hölder step. The separate fixed-measure Cegrell lemma (§5.44.2), qualitative single-potential Skoda theorem (§5.26 introductory paragraph), and bounded nonclosed-current product/limiting calculus in §5.44.7 were **not** independently proved in this increment. No claim of a false theorem, full section certification, build, CI, formal proof, or publication is made. No user-excluded approximation chain was investigated.
