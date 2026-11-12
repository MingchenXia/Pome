# Sharp local integrability spectra in the discontinuous constant-MA gluing model

**Date:** 2026-11-12. **Finding:** `POME-MA-GLUING-LOCAL-LP-SPECTRUM-001`. **Severity:** low. **Status:** **verified conditional deduction** (a matching local upper estimate and a sharp weak-Lebesgue endpoint). **No printed theorem is refuted.**

## Revision, reading-edition anchors and distinctness

- Reviewed production `main`: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- Integrated HTML `docs/sections/equations-with-prescribed-singularities--local-density-and-boundary-control/index.html`, blob `44fa705661cd5778904e1b9a6ea7299fb19e13ff`.
- Lemma **15.21.8**, original source label `non-kahler-pluripotential-theory:09B4FC75`, permanent tag `5E22269BEE55`, physical lines **79–141**: the subharmonic logarithmic product, Newtonian potential, and constant-density local determinant, particularly (15.21.7)–(15.21.10), lines **82–131**.
- Theorem **15.21.12**, original source label `non-kahler-pluripotential-theory:A866D6A3`, permanent tag `5FC2412C22E9`, physical lines **153–232**: the compact gluing, Hessian formula (15.21.14) at **190–197**, transition points and printed *lower* `L^p` obstruction at **199–231**.
- Section **15.21** is *previously partially audited*. The printed lower bound `F >= c_k |z-a_k|^{2\alpha_k-2}` and global failure of every `L^p` for `p>1` are **existing** facts, not newly reported as discoveries. The older `POME-CONSTANT-MA-DISCONTINUITY-DIMENSION-001` (2026-10-27) concerns the exact discontinuity locus and higher-dimensional products. **New here** is the opposite local upper bound, the exact strong/weak integrability threshold at each individual transition pole, and the accumulation-point local `L^p` failure.

## Setup from the printed construction

Fix an isolated point `a_k=2^{-k-4}` and exponent `\alpha=\alpha_k=a_k`, so `0<\alpha<1/2`; write `\zeta=z-a_k`. Near `a_k`, the printed construction has
\[
h(z)=\alpha\log|\zeta|^2+H_k(z),\quad
b(z)=e^{H_k(z)}|\zeta|^{2\alpha},\quad
a_{z\bar z}=b^{-1},
\qquad P(z,w)=a(z)+b(z)|w|^2,
\]
where `H_k` is smooth real harmonic. The global compact gluing is obtained on a small ball by
\[
P_0=P+M,\quad Q(z,w)=C(|z|^2+|w|^2-R^2/4),\quad
v=\tfrac12(P_0+Q+\chi(P_0-Q)).
\]
Here `\chi` is a smooth convex regularization of absolute value, equal to `|t|` for `|t|>=1`. The smooth density of the global `\theta`-Monge–Ampère measure on the gluing region is
\[
F=C^{-2}\det H_v,\qquad
H_v=\lambda H_P+(1-\lambda)CI+\frac{\chi''(P_0-Q)}2\,g g^*,
\quad \lambda=\frac{1+\chi'(P_0-Q)}2,\quad g=\partial(P_0-Q).
\]
At the transition point `Z_k=(a_k,w_k)`, with `w_k>0` as defined in the proof of Theorem 15.21.12, one has `P_0(Z_k)=Q(Z_k)`. By continuity of `P_0,Q`, choose a product neighborhood `V_k=D_k\times E_k\Subset B_R`, centered at `Z_k`, small enough that `|w|>=c_k>0` and `1/4<=\lambda<=3/4` everywhere. All estimates below are on `V_k\setminus(\{a_k\}\times E_k)`; the omitted analytic subset has zero `\theta^2`-volume and bounded Bedford–Taylor measures do not charge it.

## New matching upper bound (all terms accounted for)

First verify a derivative bound omitted from the lower-bound argument. Because `b^{-1}=e^{-H_k}|\zeta|^{-2\alpha}`, we may choose `q>2` with `\alpha q<1`. Thus `b^{-1}\in L^q_{\mathrm{loc}}` around `a_k`. By the displayed Newton potential in Lemma 15.21.8,
\[
a(z)=\frac1\pi\int_U\log|z-\xi|^2\,b(\xi)^{-1}\,dA(\xi).
\]
On a smaller disc about `a_k`, the nearby contribution to `\partial_z a` is uniformly bounded by Hölder's inequality: the kernel `(z-\xi)^{-1}` belongs uniformly to `L^{q'}` on a fixed bounded disc for `q'=q/(q-1)<2`; the part of the integral over points `\xi` separated from `a_k` has a bounded derivative. The usual distributional differentiation (or truncation followed by dominated/Hölder convergence) therefore gives `|\partial_z a|<=C_k`. No global `L^q` bound on the entire surface is used.

Since `H_k` is smooth and `0<\alpha<1/2`, on `0<|\zeta|<\epsilon_k` we have
\[
\begin{aligned}
b&=O_k(|\zeta|^{2\alpha}),&
b_z&=O_k(|\zeta|^{2\alpha-1}),&
b_{z\bar z}&=O_k(|\zeta|^{2\alpha-2}),\\
b^{-1}&=O_k(|\zeta|^{-2\alpha})
       =O_k(|\zeta|^{2\alpha-2}),&
P_z&=O_k(|\zeta|^{2\alpha-1}),&
P_w&=O_k(1).
\end{aligned}
\]
The equality of big-O orders for `b^{-1}` here uses `\alpha<1/2` and `|\zeta|<1`. As `Q` has bounded first derivatives and constant Hessian, and `\chi''` is bounded, the diagonal entries of the **full** regularized maximum Hessian satisfy
\[
0\le (H_v)_{z\bar z}
 \le C_k\bigl(1+|\zeta|^{2\alpha-2}
                   +|\zeta|^{4\alpha-2}\bigr)
 \le C_k'|\zeta|^{2\alpha-2},
\qquad
0\le (H_v)_{w\bar w}\le C_k'.
\]
The gradient-square term has therefore been bounded explicitly and cannot introduce a worse singularity. Positivity of `H_v` gives
\[
\det H_v=(H_v)_{z\bar z}(H_v)_{w\bar w}-|(H_v)_{z\bar w}|^2
       \le C_k''|\zeta|^{2\alpha-2}.
\]

For the **lower** bound, retain the verified printed determinant identity (15.21.14): with `S=\lambda H_P+(1-\lambda)CI>=0`, adding the positive rank-one term cannot decrease its determinant, while in complex dimension two
\[
\det S=\lambda^2\det H_P+\lambda(1-\lambda)C\,\operatorname{tr}H_P+(1-\lambda)^2C^2
      \ge c_k\,|w|^2 b_{z\bar z}.
\]
The explicit derivative
\[
b_{z\bar z}=|\zeta|^{2\alpha}e^{H_k}
  \left|\frac{\alpha}{\zeta}+\partial_z H_k\right|^2
\]
is bounded below by `c_k'|\zeta|^{2\alpha-2}` sufficiently close to the pole. Combining both bounds, after shrinking `V_k`, yields the **two-sided sharp comparison**
\[
\boxed{\quad
c_k|\zeta|^{-2(1-\alpha_k)}
 \le F(z,w)\le
C_k|\zeta|^{-2(1-\alpha_k)}
\qquad ((z,w)\in V_k,\ z\ne a_k).\quad}
\]
Constants depend on `k` and the chosen neighborhood; there is no claim of uniformity in `k`.

## Exact local strong/weak Lebesgue spectrum and accumulation

Put `p_k^*=(1-\alpha_k)^{-1}`. On the product neighborhood `V_k`, `\theta^2` is a positive constant multiple of planar area `dA(z)dA(w)`. The comparison above and polar integration give
\[
F\in L^p(V_k,\theta^2)\ \Longleftrightarrow\
\int_0^{\epsilon_k}r^{1-2p(1-\alpha_k)}\,dr<\infty
\ \Longleftrightarrow\ p<p_k^*.
\]
At `p=p_k^*` the integral diverges logarithmically. The distribution function of `F` on a slightly smaller product neighborhood obeys, for sufficiently large `t`,
\[
 c_k t^{-p_k^*}\le
 \operatorname{Vol}_{\theta^2}\{(z,w)\in V_k:F(z,w)>t\}
 \le C_k t^{-p_k^*};
\]
hence `F\in L^{p_k^*,\infty}_{\mathrm{loc}}(V_k)\setminus L^{p_k^*}(V_k)`. This **sharp weak endpoint** is new, while the failure for `p>=p_k^*` appeared implicitly in the printed lower estimate.

As `k\to\infty`, the transition points `Z_k=(a_k,w_k)` converge to a point `Z_\infty=(0,w_\infty)` in the gluing ball: continuity of `a` and the displayed formula for `w_k` show this directly. Because `\alpha_k\downarrow0`, we have `p_k^*\downarrow1`. Every neighborhood of `Z_\infty` contains `Z_k` and a sufficiently small product `V_k` for arbitrarily large `k`. For every fixed `p>1` choose such a `k` with `p>=p_k^*`; the integral over that product alone diverges. Thus **`F\notin L^p_{\rm loc}` at `Z_\infty` for every `p>1`**, even though for each fixed isolated transition pole there is a strictly larger-than-one local `L^p` interval. This refines the global non-`L^p` statement without challenging it.

## Status, exact coverage and dependency boundary

**Verified conditional deduction, not a new counterexample to a printed result and not a proof repair.** The local upper estimate and integrability calculation are self-contained after the explicit formulas (15.21.7), (15.21.9), (15.21.13), (15.21.14). The compact gluing, positivity and identification of the global Bedford–Taylor product are used as **internal conditional inputs** from Lemma 15.21.8, Theorem 15.21.12 and the bounded product construction in §5.27; they are not re-certified from first principles. No external regularization theorem or Demailly/Bergman/L²/OT/multiscale/positivity-loss programme is used or revisited.

**Proposed optional clarification:** record the two-sided asymptotic, threshold `p_k^*`, weak endpoint, and accumulation-point local failure as a remark immediately following Theorem 15.21.12. No body edit is made. **Affected dependents:** local regularity conclusions inferred solely from the behavior of the density in a single neighborhood, and the existing global example `F\notin\bigcup_{p>1}L^p(X)`; no general smooth-positivity theorem is refuted.

**Actually reviewed:** the local Newton kernel and its derivative near each isolated pole (§15.21.8, lines 79–140), the Hessian of the regularized maximum and localization of the transition points (§15.21.12, lines 163–231), with §5.27 invoked only as a named dependency. The whole §15.21 or surrounding Bedford–Taylor chain is **not certified**. It was previously partly visited: **0 newly first-visited numbered sections**, **0 fully certified sections**; current main ToC remains **25 chapters / 747 numbered sections**. No builds, tests, CI, formal verification, registry, permanent-tag, source, main or site writes.
