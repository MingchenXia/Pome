# Convex Kobayashi metric: sharp logarithmic boundary-distance inequality and proper geodesicity

**Date:** 2026-11-19. **Finding:** `POME-CONVEX-KOBAYASHI-LOG-BOUNDARY-PROPER-GEODESIC-001`. **Classification:** low / **verified conditional deduction** (an additional consequence; **no false printed theorem or independent proof gap confirmed**). **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Review branch:** `review/mathematical-audit`.

## Exact integrated source and scope

- Complete direct mathematical reading of `docs/sections/disc-interpolation-on-convex-domains/index.html`, blob `c0f853924bef4d4b35d3580d5c330de6613b1407`, lines **10–95**: printed Theorem **9.18.1** (original label `klimek-pluripotential-theory:9F2D2DA4`, permanent tag **`7F33F823B79C`**, lines 10–58); Proposition **9.18.2** (original `klimek-pluripotential-theory:B5E61683`, permanent **`0A57323E9BD0`**, lines 60–86); the explicit nonconvex counterexample in lines 87–95.
- Dependency statements only in `docs/sections/schwarz-estimates-and-invariant-distances/index.html`, blob `11789d8f51f81ec69de4fbb206c1186c73540b0e`: Proposition 9.17.2 (permanent **`6BCDD3D7DD27`**), Proposition 9.17.3 (**`75C57846C83D`**), Proposition 9.17.4 (**`F0CC92394671`**), Proposition 9.17.5 (**`32C365095F79`**). Their complete transitive proof chains are **not** certified here.
- The excluded Demailly regularization/Bergman/weighted-L2/Ohsawa–Takegoshi/multiscale/positivity-loss programme was not opened, proved or reclassified. Previous notes on that programme remain **deferred-by-user**.

## Additional theorem

Let `D` be **any nonempty bounded convex domain** in `C^n`, `n>=1`, and put `d_D(z)=dist_Euclidean(z,partial D)`. With the normalization `q(0,t)=atanh(t)` of the printed section, the Kobayashi distance `k_D=delta_D` satisfies, for **all** `a,b in D`,

\[
\boxed{\big|\log d_D(a)-\log d_D(b)\big|\le 2k_D(a,b).}\tag{A}
\]

The factor **2** is optimal, even among unit discs. Consequently, every closed `k_D`-ball is compact (so `(D,k_D)` is a **proper** metric space), and every two points can be joined by an **isometrically parametrized minimizing `k_D`-geodesic**. These statements strengthen the printed completeness/attainment conclusions; they do not change the published hypotheses or conclusion.

### Proof of the sharp logarithmic estimate

Fix `a,b in D`, suppose `d_D(a)>=d_D(b)`, and choose `xi in partial D` with `|b-xi|=d_D(b)`. Such a nearest point exists because `partial D` is compact. By convexity there is a real supporting hyperplane to `D` at `xi`. The ball `B(b,d_D(b))` is contained in `D` and tangent to this hyperplane at `xi`. Therefore its outward real unit normal must be `nu=(xi-b)/d_D(b)` (any hyperplane supporting a Euclidean ball at a given point has that normal).

Write `nu` in complex coordinates and define the complex-affine holomorphic function

\[
F(z)=-\sum_{j=1}^n(z_j-\xi_j)\overline{\nu_j}.
\]

Then `Re F(z)>0` on `D`, `F(b)=d_D(b)` is positive real, and `Re F(a)>=d_D(a)`: the ball `B(a,d_D(a))` lies in the same supporting half-space, so its center is at least its radius from the hyperplane. Thus `F:D\to\mathbb H=\{\Re w>0\}` is holomorphic.

For `w_1=x_1+iy_1,w_2=x_2+iy_2\in\mathbb H`, the explicit half-plane pseudohyperbolic formula gives

\[
\left|\frac{w_1-w_2}{w_1+\overline{w_2}}\right|^2
=\frac{(x_1-x_2)^2+(y_1-y_2)^2}
{(x_1+x_2)^2+(y_1-y_2)^2}
\ge \left(\frac{x_1-x_2}{x_1+x_2}\right)^2.
\]

Taking `atanh` yields `k_H(w_1,w_2)>=|log(x_1/x_2)|/2`. Schwarz contraction for `F`, followed by the displayed real-part inequalities, proves

\[
k_D(a,b)\ge k_{\mathbb H}(F(a),F(b))
\ge\tfrac12\log\frac{\Re F(a)}{\Re F(b)}
\ge\tfrac12\log\frac{d_D(a)}{d_D(b)}.
\]

If the boundary distances are in the opposite order, exchange `a,b`. This gives (A) without any boundary smoothness.

**Sharpness.** In `D=Delta`, take `a=0,b=r in (0,1)`. Then `d_D(0)=1`, `d_D(r)=1-r` and `k_D(0,r)=atanh(r)=\frac12\log((1+r)/(1-r))`. Hence

\[
\lim_{r\uparrow1}
\frac{|\log d_D(0)-\log d_D(r)|}{k_D(0,r)}=2.
\]

No smaller global Lipschitz constant is possible.

### Properness and geodesic proof

If `k_D(a,z)<=R`, (A) gives `d_D(z)>=d_D(a)e^{-2R}>0`. The closed metric ball therefore lies in the Euclidean-compact set

\[
\{z\in\overline D:\ d_D(z)\ge d_D(a)e^{-2R}\}\subset D.
\]

The printed Theorem 9.18.1 establishes that `k_D` induces the Euclidean topology. Its closed balls are Euclidean closed; hence they are compact. This proves **properness**, not just Cauchy completeness.

For distinct `a,b`, take the extremal disc supplied by printed Theorem 9.18.1, normalized `f(0)=a`, `f(t)=b`, `0<t<1`, `k_D(a,b)=atanh(t)=T`. Put `gamma(s)=f(tanh(s))`, `0<=s<=T`. Holomorphic contraction and the disc-distance formula give

\[
k_D(\gamma(s),\gamma(r))\le |s-r|.
\]

For `0<=s<=r<=T`, the triangle inequality applied to the chain `a,gamma(s),gamma(r),b` gives

\[
T\le k_D(a,\gamma(s))+k_D(\gamma(s),\gamma(r))
+k_D(\gamma(r),b)\le s+(r-s)+(T-r)=T.
\]

Every inequality is therefore equality and `k_D(gamma(s),gamma(r))=|s-r|`. This constructs a minimizing metric geodesic. **No uniqueness of geodesics** is asserted.

## Direct audit of the printed proof (no printed error confirmed)

1. Theorem 9.18.1, lines 17–43: rechecked normalization of the interpolation nodes and the rational coefficient `L(zeta)`; `A<B<1` makes its boundary values strictly between 0 and 1, its only interior pole is removable since `f(A)=g(A)`, and convexity puts the interpolating disc into `D`. The triangle inequality follows; no unproved exchange of limits is used here.
2. Lines 45–55: the local affine-disc upper bound and coordinate Caratheodory lower bounds give metric topology. Montel plus a supporting hyperplane prevents extremal discs from landing on `partial D`. The half-plane boundary obstruction proves completeness; (A) is a quantitative strengthening.
3. Proposition 9.18.2, lines 60–86: with the explicitly **complex bilinear** pairing, the stationary-disc boundary lift puts `G(z,zeta)/zeta` in the open left half-plane on the circle, so its winding is zero and `G` has exactly one simple interior zero. The implicit-function argument for the holomorphic left inverse is consistent. This presupposes the listed lift; it is **not** an existence theorem for stationary discs.
4. Lines 87–95: the nonconvex `D_epsilon` example uses normal-family compactness and the identity theorem correctly; no assertion that the one-disc distance always satisfies the triangle inequality is made.

**Status:** `verified conditional deduction` for (A), properness, and the metric-geodesic strengthening; **original printed statements not refuted**. Residual dependency audit: the complete proofs of §9.17 Schwarz–Pick/distance theory, the disc-joining proposition, and the Montel/maximum-principle inputs were read only at the level needed for this section, not certified transitively. All direct mathematics of §9.18 was read; there is no claim of a globally verified Chapter 9.

## Proposed insertion and dependents

An optional corollary after Theorem 9.18.1 may state (A), its optimality, properness, and geodesicity, with the self-contained half-plane proof above. Keep original stable tags and original historical attribution; no source/body/registry/canonicalization edits were made. Its immediate dependent uses are the quantitative boundary escape assertion in the completeness proof of Theorem 9.18.1 (lines 49–55) and the interpretation of its extremal discs as metric geodesics. No other downstream theorem was certified in this run.

## Coverage and operations

**One newly directly read complete section (§9.18)**; statement-level context in §9.17; **zero** complete transitive dependency chains. This is not a claim that §9.18 had never been seen before; legacy status is unreconciled. No local build, tests, CI, automatic website publication or changes to main/source/tag/registry were performed.
