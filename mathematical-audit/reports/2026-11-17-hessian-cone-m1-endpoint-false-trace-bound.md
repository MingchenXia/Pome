# Audited counterexample: the m=1 endpoint of the Hermitian cone trace bound

**Finding:** `POME-HESS-CONE-M1-TRACE-BOUND-FALSE-001`  
**Severity/status:** medium / **confirmed error** (only the third inequality in the printed lemma, under the permitted `m=1,n>=2` hypotheses).  
**Main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated reading edition:** `docs/sections/complex-hessian-equations--the-admissible-cone/index.html`, blob `925e6109ab7d800cde9bec4b0487842b2e6877a8`, physical lines **113–133**; local conventions lines **9–42** and the explicit `m=1` endpoint in Lemma 8.2.3, lines **43–74**.  
**Stable source label:** `non-kahler-pluripotential-theory:53FFB5F3`; **reader permanent tag:** `7710D01DF6F5` (Lemma 8.2.5).  
**Reading-edition link:** https://github.com/MingchenXia/Pome/blob/b6933b772f41b45918f7e25ed1afbbb1fd892272/docs/sections/complex-hessian-equations--the-admissible-cone/index.html#L113-L133

## Printed claim and counterexample

The lemma states, for `M` in the closed Hermitian `m`-cone, the simultaneous estimates

\[
W=\sum_i F_i M_{i\bar i}\geq \frac{f}{m!S}\operatorname{tr}M,\qquad
F_i\geq\frac{f}{m!S},\qquad
|M_{1\bar1}|\leq\operatorname{tr}M.
\]

There is **no hypothesis `m>=2` in this lemma**. The section defines `\Gamma_m=\{\lambda:S_j(\lambda)>0,1\le j\le m\}` and explicitly treats `m=1` in its immediately preceding Lemma 8.2.3. Thus the claimed endpoint is within the printed scope.

Choose complex dimension `n=2`, `m=1`, a unitary frame for the reference metric, and

\[
\Lambda=I_2,\qquad M=\begin{pmatrix}2&0\\0&-1\end{pmatrix}.
\]

The eigenvalues of `M` sum to `1>0`, so `M\in\Gamma_1\subset\overline{\Gamma_1}`. However,

\[
|M_{1\bar1}|=2>1=\operatorname{tr}M.
\]

Indeed the stronger family `M_R=\operatorname{diag}(R,1-R)` (`R>1`) has trace `1` and unbounded first diagonal entry. Therefore **no fixed multiplicative constant** in the last inequality follows from closed `\Gamma_1` membership alone. This is a false assertion, not merely a missing justification.

The precise faulty proof step is the sentence at line **124**: "The closed `m`-cone is contained in the closed `2`-cone." This holds for `m>=2`, not for `m=1`. In the example `S_2(M)=-2<0`, invalidating the line **127** estimate `\sum\mu_i^2\leq(\operatorname{tr}M)^2`.

The first two inequalities have **not** been refuted. For the endpoint `m=1`, `F=\sigma_1=S/n`, `F_i=1/n`, and `f/(m!S)=1/n`, so both inequalities hold with equality for every `M\in\overline{\Gamma_1}`. The third assertion alone needs restriction.

## Verified conditional repair (proposed, not applied)

Retain the first two inequalities for all `1\le m\le n` under the existing hypotheses, and state the last inequality only when `m\ge2` (or, independently, when `M\succeq0`). For `2\le m\le n`, closed-cone membership gives `S_1(M)\ge0` and `S_2(M)\ge0`. Consequently

\[
\operatorname{tr}(M^2)
=(\operatorname{tr}M)^2-2S_2(M)\le(\operatorname{tr}M)^2.
\]

Since `M` is Hermitian, `|M_{1\bar1}|\le\|M\|_{op}\le\sqrt{\operatorname{tr}(M^2)}\le\operatorname{tr}M`. The endpoint `m=2` is covered; `m=1` in dimension one is harmless but does not justify the general assertion. This repairs exactly the erroneous clause without changing valid versions or stable tags.

## Affected dependents (actually inspected)

* `docs/sections/complex-hessian-equations--a-trace-estimate-with-a-prescribed-potential/index.html`, blob `3d7fe6d1867a0d8ac268042a59e112329a6c8af3`, lines **9–13, 59–62**: the trace-absorption estimate uses the third clause, but the section **explicitly assumes `m>=2`**. Therefore this inspected use remains valid after the restriction; the full trace estimate is not certified.
* `docs/sections/complex-hessian-equations--bounded-complex-hessians-and-elliptic-extensions/index.html`, blob `fdd9225b1d778e1debaf94f75ef65175d4bd4484`, lines **90–96**: this use cites the **coefficient lower bound**, not the false diagonal-entry clause. The `m=1` case of the coefficient bound is exact, as computed above; no dependent error is established here.
* `docs/sections/complex-hessian-equations--liouville-and-gradient-estimates/index.html`, blob `74cda06ad4bf75ab5fcba6e841c9ad4aa9424981`, lines **10, 113–123**: explicitly allows `m=1` in its elementary Liouville discussion while restricting the gradient proposition to `2<=m<=n`. Its general PDE conclusions are not audited in full.

Other potential readers of this lemma have not been exhaustively searched. Do not infer an incorrect analytic theorem from this local algebraic error.

## Scope and coverage accounting

New **selected** proof inspection of §8.2 Lemma 8.2.5's third clause, plus the above **specific** cross-section references. §8.2 was already partially reviewed; **0 first-visited numbered sections, 0 fully certified sections**. No new build, test suite, CI, formal certification or main-branch edit. Existing project inventory: 25 chapters / 747 numbered sections (previously established, not recomputed here). Demailly approximation/regularization and the dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programme remain **deferred-by-user**, not resolved or certified.
