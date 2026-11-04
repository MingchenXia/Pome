# Logarithmic continuity without the square-root Dini condition: exact finite intrinsic distance

**Finding:** `POME-METRIC-DINI-NONNECESSITY-LOGPOLE-001`  
**Date:** 2026-11-04  
**Status:** **verified conditional deduction** (an independent, explicit boundary model; printed results correct).  
**Severity:** low (useful hypothesis boundary, not an invalid theorem).  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (unchanged).

## Exact integrated targets and scope

- `docs/sections/plurisubharmonic-functions-and-singularities--potential-regularity-and-metric-distance/index.html`, main **blob `26695e8698b9114b97108efb16ec94f3984ee308`**, physical lines **10–44, 52–105, 109–124**.
- Theorem **5.39.1**, source `non-kahler-pluripotential-theory:EF691FCE`, permanent tag `230882F1D833`: Hölder trace masses and intrinsic-distance upper bounds, lines **10–44**.
- Equation **5.39.5**, source `non-kahler-pluripotential-theory:618F80CA`, permanent tag `06D8010B670C`: the square-root Dini function `D(r)=r+int_0^r sqrt(m(t))/t dt`, lines **58–63**.
- Theorem **5.39.6**, source `non-kahler-pluripotential-theory:97B8A37E`, permanent tag `21429B9E1BF3`: sufficient Dini criterion for compact local metric completion, lines **66–105**.
- Corollary **5.39.7**, source `non-kahler-pluripotential-theory:2F17E044`, permanent tag `380EB17A4350`: the log-modulus exponent `a>2` and explicit statement that the Dini condition is *only sufficient*, lines **109–124**.
- Corollary **5.39.8**, source `non-kahler-pluripotential-theory:017413AB`, permanent tag `D3B517FBCE4F`: uniform compactness of distance pseudometrics; **dependency context only**, lines **126–169**.

This is **new exact logarithmic boundary/model scrutiny in a previously partially reviewed section**, not the first audit of §5.39 and not a section-level certificate. Earlier finding `POME-METRIC-COMPLETIONS-GH-001` concerned completed pseudometric/Gromov–Hausdorff convergence and remains separate.

## Proposition: all positive logarithmic exponents yield a finite-distance pole

For every real `a>0`, fix `R<exp(-(a+2))`, put `U={z in C: |z|<R}`, `A={0}`, and define

\[
v_a(0)=0,\qquad v_a(z)=\bigl(\log(1/|z|)\bigr)^{-a}\quad(0<|z|<R).
\]

Let `theta=0` and `eta_a=dd^c v_a` on `U\setminus A`, with the book's normalization `dd^c=(i/(2pi))partial barpartial` and `omega_E=dd^c|z|^2`. Then:

1. `v_a` is continuous subharmonic on all of `U` and `eta_a` is a smooth **strictly positive** Hermitian form on `U\setminus A`. It has no residual Dirac mass at zero.
2. Its **optimal common modulus of continuity**, for sufficiently small `s>0`, is
   \[
   m_a(s)=\bigl(\log(1/s)\bigr)^{-a}.
   \]
   Thus *no alternative, smaller valid modulus* can make the square-root Dini integral finite when `0<a<=2`:
   \[
   \int_0^s\frac{\sqrt{m_a(t)}}{t}\,dt
   =\begin{cases}
   +\infty,&0<a\le 2,\\
   \displaystyle\frac{(\log(1/s))^{1-a/2}}{a/2-1},&a>2.
   \end{cases}
   \]
3. Despite this failure for `0<a<=2`, the intrinsic `eta_a`-metric completion adds **one point over the deleted origin**, with **exact radial distance**
   \[
   d_{\eta_a}(\{|z|=r\},0_{\mathrm{comp}})
   = C_a\bigl(\log(1/r)\bigr)^{-a/2},\qquad C_a>0,
   \]
   where `C_a` depends only on `a` and the harmless Riemannian conversion constant of `omega_E`. In particular the metric is incomplete for every `a>0` although the pole is at finite distance.

Consequently the printed `a>2` threshold in Corollary 5.39.7 is **not a necessary threshold for finite metric distance**. This agrees with the corollary's explicit caution and does **not** refute Theorem 5.39.6.

### Proof: positivity, exact mass, and best modulus

Set `r=|z|`, `L=log(1/r)`, and `h(r)=L^{-a}`. Differentiation gives

\[
h'(r)=\frac{a}{rL^{a+1}},\quad
h''(r)=\frac{a(a+1-L)}{r^2L^{a+2}},\quad
\Delta h(r)=h''(r)+\frac{h'(r)}r
=\frac{a(a+1)}{r^2L^{a+2}}>0.
\]

The function is bounded near the isolated point, hence its subharmonic extension there is unique. More directly, `r h'(r)=aL^{-a-1}->0`, so the distributional Laplacian has **no atom** at zero. By the normalizations,

\[
\eta_a=\frac{\Delta h}{4}\,\omega_E
=\frac{a(a+1)}{4r^2L^{a+2}}\,\omega_E,
\qquad
\int_{|z|<r}dd^cv_a=\frac{a}{2}L^{-a-1}.
\]

Both identities follow by integrating the radial Laplacian; the second explicitly checks the `dd^c log|z|^2=delta_0` convention.

Because `L>a+2` throughout the chosen disk, `h''(r)<0`. Hence `h` is increasing, concave, and `h(0)=0`. Concavity implies
`|h(r_1)-h(r_2)| <= h(|r_1-r_2|)`. Therefore, for `z,w in U` separated by at most `s`, the Euclidean reverse triangle inequality yields

\[
|v_a(z)-v_a(w)|\le h(||z|-|w||)\le h(s).
\]

The pair `z=0,w=s` gives equality, so the asserted modulus is *optimal*. Substituting `L=log(1/t)` in the Dini integral proves the divergence/convergence dichotomy in (2), including the borderline `a=2`.

### Proof: exact metric distance and uniqueness of the added point

The metric is rotationally symmetric and, relative to the Euclidean Hermitian metric, has radial length element

\[
ds_{\eta_a}=c_0\frac{\sqrt{a(a+1)}}{2rL^{(a+2)/2}}\,|dr|
\quad\text{on radial paths},
\]

for a fixed convention-dependent `c_0>0`. Its integral from radius `r` to the origin is

\[
c_0\frac{\sqrt{a(a+1)}}2
\int_{\log(1/r)}^\infty t^{-(a+2)/2}\,dt
=c_0\frac{\sqrt{a(a+1)}}a\,L^{-a/2}.
\]

Along **any** curve approaching zero, the length is at least this radial integral, since the positive angular term can only increase length and total radial variation must span the same radius range. Radial segments realize equality in the metric completion. At radius `r`, the complete angular circumference has order `L^{-(a+2)/2}->0`. Hence points approaching zero from different angles have the *same* completion limit. This proves (3), without using Theorem 5.39.6 or the Dini criterion.

As a quantitative contrast, the printed cutoff estimate bounds `mu(B_r)` by a multiple of `m_a(2r)`, whereas the actual mass above is smaller by a factor of order `1/L`. Even when `a>2`, the general Dini estimate yields `O(L^{1-a/2})`, while this explicit metric has the strictly faster `L^{-a/2}` rate. These comparisons diagnose a **sufficient-proof estimate**, not an error in its direction.

### Optional higher-dimensional realization

On a product coordinate polydisk in `C^n`, take

\[
v_a(z_1,\ldots,z_n)=h(|z_1|)+\sum_{j=2}^n|z_j|^2,\qquad
A=\{z_1=0\}.
\]

Then `dd^c v_a` is a smooth positive-definite Hermitian form away from the analytic divisor `A`; the optimal local modulus is comparable to `L_s^{-a}` (the smooth transverse terms contribute only `O(s)`). The normal-direction distance to `A` has exactly the one-variable radial order. Thus the phenomenon is not peculiar to complex dimension one. This product observation does not claim a complete classification of all metric-completion fibers.

## Classification and proposed amendment

**Mathematical status:** **verified conditional deduction**, **low severity**. **No original theorem is false**, **no missing proof is thereby repaired**, and **no section is certified**. The general `D`-criterion and its applications are preserved. In particular, any downstream use of the *sufficient* Dini bound remains conditional on its hypotheses; this model does not remove those hypotheses from the *general* theorem.

**Suggested reading-edition addition, not applied:** after Corollary 5.39.7, append a short one-dimensional radial example `v(z)=(-log|z|)^{-a}` for `0<a<=2`, with `Delta v=a(a+1)/(|z|^2(log(1/|z|))^{a+2})`, to make the printed "not necessary" clause quantitative. Retain all original permanent tags, historical attribution and source versions. No source/body/registry/canonicalization change is authorized by this audit note alone.

**Dependencies:** elementary distributional radial calculus, the Pome `dd^c` convention, concavity/subadditivity of `r\mapsto(-log r)^{-a}`, and the intrinsic Riemannian length definition. **No** regularization, Bergman kernels, weighted L², Ohsawa–Takegoshi, multiscale atlas, positivity-loss machinery, Hironaka input, convergence-of-nets assumption, or unproved analytical existence theorem enters this check.

**Coverage accounting:** only the selected current-main statements/estimates identified above, and the explicit radial example. The existing section ledger and all older error/proof-gap/external/deferred-by-user categories remain unchanged. No build, test suite, CI, website publication, formal verification, or full section proof verification was performed.
