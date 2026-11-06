# A necessary polar boundary exception in the planar extremal

**Finding ID:** `POME-PLANAR-ISOLATED-POLAR-BOUNDARY-EXCEPTION-001`  
**Date:** 2026-11-06  
**Status:** **verified conditional deduction** (self-contained sharpness model; printed theorem correct).  
**Severity:** low.  
**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (unchanged).

## Exact source pinning and scope

- `docs/sections/planar-green-functions-and-conformal-maps/index.html`, blob `bfee348bb5f4bbfaa4515e5c9333789a13dae861`; **Proposition 3.8.2**, physical lines **53–69**, source `klimek-pluripotential-theory:886FBC1A`, permanent tag `3F05222ECC9E`. **Example 3.8.3**, lines **73–83**, source `klimek-pluripotential-theory:02455EF4`, permanent tag `FADCC209A003`. Kernel normalization: line 7.
- `docs/sections/polynomial-descriptions-of-logarithmic-envelopes/index.html`, blob `15d7e0207da1d72653382a1512ca380311b5d5e3`; **Theorem 16.30.5**, lines **93–115**, source `klimek-pluripotential-theory:485FC789`, permanent tag `E171A0405847`.
- General theorems cited by these passages, including the planar polar-exception minimum principle, Myrberg and the Siciak polynomial formula, have **not** been independently certified. The calculation below does **not** use any general polynomial-extremal representation or approximation theorem.

## Exact example

Fix real `R>1` and let `a=R`. Define
\[
K=S^1\cup\{a\}, \qquad \Omega=\{z\in\mathbb C:|z|>1,\ z\ne a\}.
\]
The compact set `K` is nonpolar because `S^1` is nonpolar (normalized arclength on it has finite logarithmic energy). With the ordinary logarithmic-growth class \(\mathcal L(\mathbb C)\) and the **raw** extremal
\[
V_K(z)=\sup\{v(z):v\in\mathcal L(\mathbb C),\ v\le0\text{ on }K\},
\]
the precise answers are
\[
\boxed{
V_K(z)=\begin{cases}
0,& |z|\le1\ \text{or }z=a,\\
\log|z|,& |z|>1,\ z\ne a,
\end{cases}}
\tag{A}
\]
and
\[
\boxed{V_K^*(z)=\log^+|z|\quad(z\in\mathbb C).}\tag{B}
\]
Thus `V_K^*(a)-V_K(a)=log R>0`; the raw extremal is not upper semicontinuous at the isolated point `a`.

### Upper bound by the annular maximum principle

Take any admissible `v`. Since `v\le0` on `S^1`, the subharmonic maximum principle on the unit disc gives `v\le0` for `|z|\le1`. The logarithmic growth hypothesis gives a constant `C_v>=0` such that `v(z)\le\log T+C_v` on every sufficiently large circle `|z|=T`. On the annulus `1<|z|<T` compare with the harmonic function
\[
b_T(z)=\left(1+\frac{C_v}{\log T}\right)\log|z|.
\]
The two boundary comparisons imply `v\le b_T` throughout the annulus. For a fixed exterior point send `T\to\infty` to obtain `v(z)\le\log|z|`. The extra constraint at `a\in K` independently gives `v(a)\le0`. This proves the upper bound in (A), without using the general polynomial identity.

### Lower bound by explicit admissible polynomials

The function zero belongs to \(\mathcal L\) and is admissible. For `m>=0` define
\[
P_m(z)=\frac{z^m(z-a)}{R+1},\qquad
q_m(z)=\frac{1}{m+1}\log|P_m(z)|.
\]
Each `q_m` is subharmonic and has logarithmic growth. On `S^1`, `|P_m(z)|\le1`; at `a`, `P_m(a)=0`. Thus `q_m` is admissible. At any fixed `|z|>1` with `z\ne a`,
\[
q_m(z)=\frac{m}{m+1}\log|z|+
 \frac{\log|z-a|-\log(R+1)}{m+1}
\longrightarrow\log|z|.
\]
The zero competitor and upper bound settle `|z|\le1` and `z=a`. This proves (A). Since \(\log^+|z|\) is continuous and coincides with (A) off `a`, (B) follows by upper-semicontinuous regularization. This proof is **independent** of the general polynomial representation in Theorem 16.30.5, with which it is consistent.

## Sharp boundary implication

The finite boundary of `Omega` is precisely `S^1\cup\{a\}`. On `Omega` the canonical `u=V_K^*=\log|z|` is strictly positive and harmonic, is bounded near **all** of its finite boundary, and has `u(z)-\log|z|\equiv0` at infinity. Nevertheless,
\[
\lim_{\Omega\ni z\to\xi}u(z)=
\begin{cases}
0,&\xi\in S^1,\\
\log R,&\xi=a.
\end{cases}
\]
The singleton \(\{a\}\) is polar, e.g. the pole set of \(\log|z-a|\). Moreover **any** exceptional boundary set allowing the printed quasi-everywhere zero-limit conclusion must contain `a`. Since `R` can be arbitrarily large, the exceptional finite positive boundary limit \(\log R\) admits no uniform bound for this family. Thus even **boundedness of the canonical extremal near the finite boundary** does not allow deleting the polar-exception qualifier in Proposition 3.8.2.

For a direct measure check, the radial normal derivative of \(\log^+r\) jumps from `0` to `1` across `S^1`. Hence distributionally \(\Delta V_K^*=ds|_{S^1}\). With the reading edition's \(dd^c=i(2\pi)^{-1}\partial\bar\partial\) convention,
\[
dd^cV_K^*=\frac{1}{4\pi}\,ds|_{S^1},\qquad
\int_{\mathbb C}dd^cV_K^*=\frac12.
\]
The isolated point `a` carries no current mass. The `dd^c` normalization here is deliberately distinguished from the positive Green kernel's \(-\log|z-a|\) singularity in §3.8 line 7.

## Verdict and dependent scope

**Not a counterexample to a printed theorem.** Proposition 3.8.2 correctly states a zero boundary limit only outside a **polar** set. Example 3.8.3 adds positive Poisson spikes unbounded at a boundary point to demonstrate a *different* nonuniqueness phenomenon; this calculation instead gives a **bounded canonical extremal** and shows why polar exceptions persist. The polynomial Theorem 16.30.5 is consistent with (A), not certified in general.

**Proposed correction:** no change to the printed statement. An optional explanatory example directly after Proposition 3.8.2 could note `S^1\cup\{R\}`. Preserve historical attribution, source labels, and permanent tags. **Potential dependents** are arguments that incorrectly replace the §3.8.2 quasi-everywhere boundary conclusion by an everywhere statement. No such downstream invalidity is claimed verified here.

**Actual coverage:** targeted complete calculation of (A), (B), the exceptional boundary limit, and the radial distribution, plus selected source comparisons. No entire §3.8, §16.30, or theorem dependency chain was certified. All prior findings remain classified as before; the user-excluded regularization/Bergman/weighted-L²/OT/multiscale/positivity-loss programme remains **deferred-by-user**. No source, main, tests, builds, CI, formal verification or site publication were changed or run.
