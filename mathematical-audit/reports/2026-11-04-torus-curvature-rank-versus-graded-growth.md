# Exact metric-dependent curvature ranks with invariant graded growth on a complex torus

**Finding:** `POME-SECTION-CURVRANK-METRIC-DEPENDENCE-001`  
**Date:** 2026-11-04 (Asia/Shanghai)  
**Classification:** low / **verified conditional deduction** (the printed statements remain correct; not a theorem error or a repaired proof).  
**Production main inspected:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Audit base branch:** `review/mathematical-audit`, previously at `8c9e57ecc34b4d820613c57e2da69dde766cc82e`.

## Exact integrated reading-edition targets

- `docs/sections/flags-convex-bodies-and-section-growth/index.html`, main blob `83557f0e15275253661fe679c75407e6636d497c`.
- Proposition **19.9.19**, source `non-kahler-pluripotential-theory:77A30A69`, permanent tag `C8B2CB1B6819`, physical lines **391–426**: the section-map rank at an appropriate maximum is at most the rank of the semipositive curvature there.
- Corollary **19.9.20**, source `non-kahler-pluripotential-theory:CBB2BC97`, permanent tag `14480FFA5B57`, physical lines **430–448**: `kappa(L) <= r_h^+ <= r` and `h^0(L^p)=O(p^{r_h^+})`.
- Proposition **19.9.23**, source `non-kahler-pluripotential-theory:04D312FB`, permanent tag `5C0C7B20BA7A`, physical lines **503–516**: the Euler polynomial has degree at most the maximum pointwise curvature rank.
- Example **19.9.25**, permanent tag `DE28BE657AA4`, physical lines **532–544**, supplies the different, sharp *positive growth* example; only compared, not recertified.

The exact normalization in this reading edition is `dd^c = i/(2pi) partial bar-partial`, with a metric written as `|e|_h^2 = exp(-chi)`.

## Statement of the independent model

For each complex dimension `n >= 1` and each integer `0 <= r <= n`, there is a smooth Hermitian metric `h_r` on **the same trivial holomorphic line bundle** `L = O_X` over the same flat complex torus
\[
 X=(\mathbb C/(\mathbb Z+i\mathbb Z))^n
\]
for which
\[
\max_X\operatorname{rank}\beta_r
=\max_{\{\beta_r\geq0\}}\operatorname{rank}\beta_r=r,\qquad
h^0(X,L^p)=1\quad(p\geq0),\qquad\kappa(L)=0.
\]
For any fixed positive-rank holomorphic vector bundle `E`, the polynomial `chi(X,L^p tensor E)` is constant in `p` (and for `E=O_X`, is identically zero). In particular, for `r=n` the curvature has **positive-definite open regions**, but its Chern class vanishes, its Euler polynomial has degree less than `r`, and the section count stays constant.

Thus the **upper bounds** of Corollary 19.9.20 and Proposition 19.9.23 cannot be reversed merely from the value of the rank of an arbitrary metric's curvature; the numerical quantities `r` and `r_h^+` are not holomorphic-line-bundle invariants. None of these converse or invariance claims is made in Pome.

## Full direct verification

Write `z_j=x_j+iy_j`, where `x_j` is a well-defined circle-valued coordinate on the torus, and choose
\[
\varphi_r=-\sum_{j=1}^r \cos(2\pi x_j),\qquad
|1|_{h_r}^2=e^{-\varphi_r}.
\]
The sum is empty and `h_0` is flat when `r=0`. Since `partial_z partial_{bar z} f(x) = f''(x)/4`, the curvature is
\[
\beta_r=dd^c\varphi_r
=\frac{i\pi}{2}\sum_{j=1}^r\cos(2\pi x_j)\,dz_j\wedge d\bar z_j .
\]
This is a globally defined smooth real `(1,1)` form. Its Hermitian matrix is diagonal with precisely `r` potentially nonzero entries, hence the maximum rank is exactly `r`. At every point with `x_1=\cdots=x_r=0` (modulo `1`), each coefficient is positive; `\beta_r\geq0` and `rank beta_r=r` there. Thus `r_{h_r}^+=r`. For `r>0`, the coefficient changes sign at `x_j=1/2`, so **no global semipositivity** is being assumed or inferred. This precisely matches the hypotheses of 19.9.19–20.

A global section of `L^p=O_X` is a holomorphic function on a connected compact complex manifold; by the maximum-modulus principle it is constant. Hence `h^0(X,L^p)=1` for every `p>=0`, the section-ratio field is `C`, and `kappa(L)=0`. The upper bound `1=O(p^r)` in the printed corollary holds for every chosen metric, but is strict as an exponent whenever `r>0`.

The global curvature `\beta_r=dd^c\varphi_r` is exact, and is closed. For each `j>=1`,
\[
\beta_r^j=d\left(d^c\varphi_r\wedge\beta_r^{j-1}\right),
\]
so its de Rham class is zero. In particular `c_1(L)=0` and all `p`-dependent terms of the Hirzebruch–Riemann–Roch polynomial vanish:
\[
\chi(X,L^p\otimes E)=\int_X \operatorname{ch}(E)\operatorname{td}(TX).
\]
The complex tangent bundle of this torus is holomorphically trivial, so `td(TX)=1`. For `E=O_X` and `n>=1`, the integrand has no top-degree part, whence `chi(X,O_X)=0`, independently of `p` and `r`. This demonstrates that the **pointwise** bound `beta_r^{r+1}=0` and the **cohomological** Chern-degree bound need not be sharp together.

Finally, compare the same `X,L` with `h_0`: the flat metric yields `r_{h_0}^+=r(h_0)=0` while `h_n` has `r_{h_n}^+=r(h_n)=n`. Thus the curvature-rank bounds are genuinely metric-sensitive even with the holomorphic bundle and its graded section ring held fixed. The construction uses only elementary local differentiation, compactness and Stokes; no approximation, Bergman kernel, weighted `L^2`, Ohsawa–Takegoshi, or positivity-loss argument.

## Logical status, dependencies and proposed placement

- **Verified conditional deduction, low severity.** Exact model and its metric/section/Euler calculations are verified. The integrated original results are **not** refuted or otherwise fully certified.
- **Upstream inputs:** the maximum modulus principle and the analytic Hirzebruch–Riemann–Roch statement already used by Proposition 19.9.23; the latter is invoked only for the Euler-polynomial interpretation (the model's `h^0=1` calculation does not require it). No user-excluded approximation programme is entered.
- **Affected dependents:** interpretations of 19.9.19–20, 19.9.23 and the sharpness comparison with Example 19.9.25. In particular, 19.9.25 exhibits **attainment** on a positive line bundle, while this fixed trivial-bundle family exhibits arbitrarily large **strictness** of the curvature-rank upper bound.
- **Proposed correction:** none to the theorem statements. Optionally insert a short remark after Corollary 19.9.20 distinguishing metric-dependent rank upper bounds from the intrinsic `kappa(L)` and intrinsic Euler polynomial degree. Preserve original attributions and all permanent tags.
- **Precise coverage:** first independent all-rank metric-variation model at 19.9.19–20 and 19.9.23; these statements had already received selected proof reading. This does **not** certify all of §19.9, any general source theorem, or the HRR prerequisite.
- **Deferred-by-user:** all earlier Demailly approximation/regularization, dedicated Bergman, weighted-`L^2`, OT, multiscale-atlas, and positivity-loss findings remain deferred, neither resolved nor recertified.
