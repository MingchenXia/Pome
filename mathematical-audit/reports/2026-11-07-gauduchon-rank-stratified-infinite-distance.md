# Rank-stratified exact logarithmic distance on invariant Gauduchon cones — 2026-11-07

**Finding ID:** `POME-GAUD-RANK-STRATIFIED-LOGDIST-001`. **Severity:** low. **Status:** verified conditional deduction. **Classification:** additional exact model and sharpness calculation; **no false theorem, no general proof certification and no source patch**.

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Integrated reading edition:** `docs/sections/a-gauduchon-variational-volume--the-hessian-metric-and-its-completion/index.html`, blob `23a7f2a1dab791569c39a0ff5f056f52bfc200fe`. Selected physical HTML line anchors:
- Proposition **12.6.5**, lines 150–165, 169–217; source `non-kahler-pluripotential-theory:95BE22FD`, permanent tag `47DDBF953B9C`. Formula **12.6.7**, source `non-kahler-pluripotential-theory:75DECB89`, tag `85B17908B21F`.
- Lemma **12.6.9**, lines 231–269; source `non-kahler-pluripotential-theory:016ADD09`, tag `81EECB4E9700` (exact ambient matrix distance and geometric-mean path).
- Theorem **12.6.12**, lines 284–351; source `non-kahler-pluripotential-theory:0545D460`, tag `B01FA2265C81`. Its lower bound **12.6.16**, lines 294–299 and proof lines 345–351; source `non-kahler-pluripotential-theory:86BD9982`, tag `5EC99A6A3831`.

## Exact two-block calculation

Let `n>=2`, choose `1<=r<n`, and write `p=n-r`. On any compact complex-parallelizable quotient to which Proposition 12.6.5 applies (the standard complex torus is a concrete example), fix its invariant holomorphic coframe, `h_0`, `H=integral_X h_0^n>0`, and normalized invariant probability `mu=h_0^n/H`. Let `P,Q` be orthogonal Hermitian projections on coefficient space with `P+Q=I`, `rank P=p`, `rank Q=r`. Fix `W=span_R{P,Q}` (or any larger real linear coefficient space containing these projections) and the semipositive rank-`p` endpoint `A_0=P`.

For `t>0` put
```text
A_t = P + t Q,                    det A_t = t^r,
lambda(A_t) = (H t^r)^(1/n),
a = H^(-1/n),
B_t = A_t/lambda(A_t) = a[t^(-r/n) P + t^(p/n) Q].
```
Every `B_t` lies in the determinant-one hypersurface `S_W={A in W:A>0,H det A=1}`. The scalar matrix `B_1=aI` is the natural basepoint. This parameterization exhausts `S_W` if `W=span_R{P,Q}`: any positive `xP+yQ` with `Hx^p y^r=1` occurs for `t=y/x`.

**Exact intrinsic metric and distance:**
```text
g_(B_t)(dB_t,dB_t) = [r(n-r)/n^2] (dt/t)^2,
d_W(B_s,B_t) = [sqrt(r(n-r))/n] |log(t/s)|   (s,t>0).
```
In particular, for `0<t<1`,
```text
d_W(B_1,B_t) = [sqrt(r(n-r))/n] log(1/t),
d_W(B_star,B_t) = [sqrt(r(n-r))/n] log(1/t) + O_(B_star)(1)
```
for every fixed `B_star in S_W` and every `W` containing `P,Q`. The first identity remains exact for all such larger `W`: the full positive-matrix distance is a lower bound for the intrinsic distance, while its minimizing geometric-mean path is block-diagonal, stays in `span{P,Q}`, and has constant determinant.

### Proof without invoking compactness or limit interchange

Write `B_t=x(t)P+y(t)Q` with `x(t)=a t^(-r/n)`, `y(t)=a t^(p/n)`. The Hessian metric displayed in (12.6.7) gives
```text
g = (1/n) tr(B^(-1) dB B^(-1) dB)
  = (p/n) (d log x)^2 + (r/n) (d log y)^2.
```
Substitution yields
```text
g = [p r^2/n^3 + r p^2/n^3] (d log t)^2
  = [pr/n^2] (d log t)^2.
```
Thus for the two-dimensional `W`, the normalized hypersurface is globally isometric to the real line with coordinate `[sqrt(pr)/n] log t`, and the intrinsic distance formula follows *exactly*. In a larger `W`, apply (12.6.10) to `B_s,B_t`: their relative eigenvalues are `(t/s)^(-r/n)` repeated `p` times and `(t/s)^(p/n)` repeated `r` times. The resulting ambient lower bound equals the displayed distance. The same two-block curve lies in `S_W` and achieves this bound, so the larger-space intrinsic distance is equal. The final fixed-reference asymptotic is the ordinary triangle inequality:
```text
|d_W(B_star,B_t)-d_W(B_1,B_t)| <= d_W(B_star,B_1).
```
No sequential compactness, weak convergence, Bergman kernel, weighted L2 estimate, or regularization is used.

## Comparison with the printed boundary estimate and rank information

At the nonzero rank-`p` semipositive endpoint `A_0=P`, the printed (12.6.16) gives only
```text
d_W(B_star,B_t) >= [r/(n sqrt(n))] log(1/t) + O(1).
```
This is valid but not optimal on these explicit rays: their *exact* coefficient is `sqrt(r(n-r))/n`, depending on the nullity `r`. The full logarithmic metric separates different rank strata, even though all such rays satisfy `lambda(A_t)->0` and `A_t->P`. The newly established coefficient is **sharp within the model**, because equality holds for every pair `B_s,B_t`. We make no claim of a universal rank-only coefficient for arbitrary nongeneric approaches, nor of a general `W` geodesic-convexity theorem.

As a check, for `n=3, r=1` this gives `sqrt(2)/3 |log t|`; for `n=2, r=1` it gives `(1/2)|log t|`. These are exact symbolic substitutions, not numerical tests.

## Classification and downstream scope

Theorem 12.6.12 and its lower bound (12.6.16) **remain correct**. This increment strengthens the bound on a specified family and checks the determinant normalization and intrinsic-versus-ambient distance distinction. The matrix metric (12.6.7) and ambient formula (12.6.10) are explicitly identified **conditional internal inputs**. The displayed two-block metric/distance computation is fully proved under them. The general Gauduchon smooth-equation and invariant averaging proof chains in Proposition 12.6.5 remain unverified here. The result can serve as a sharp rank-stratified benchmark for further boundary/completion statements in §12.6 and for comparisons with degenerating Hermitian classes; it does **not** change published bodies, canonicalizations, or tags.

**Actual coverage:** §12.6.5/7, §12.6.9/10/11, and §12.6.12/13/16, **selected passages only**. This section was partly reviewed previously, so it is **not** a new first section visit and **not** a complete §12.6 certification. The current collection baseline remains 25 chapters, 747 numbered sections, and zero complete mathematical-section certifications. The user's excluded Demailly approximation/regularization and its dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**, without any new work on it. No build, test suite, GitHub Actions, formal verification, or publication was run.
