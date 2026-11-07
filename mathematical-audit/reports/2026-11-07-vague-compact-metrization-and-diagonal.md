# Vague compactness on Euclidean domains is metrizable and sequentially compact
**Date:** 2026-11-07. **Finding:** `POME-MEASURE-VAGUE-METRIZABILITY-DIAGONAL-001`.
**Severity:** low. **Status:** verified conditional deduction; **not** a false printed theorem and **not** a full-section certification.
**Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Integrated anchors and hypotheses
- `docs/sections/measures-and-distributions--nets-and-compactness/index.html`, main blob `7e4a226a48f88a97b3db1a8dd7d8582c909aeea1`, **physical lines 7–10, 14–30, 36–48, 53–67, 72–88**. The primary target is Theorem **2.7.3**, source `foundations-of-pluripotential-theory:5470287F`, permanent tag `DF30CEF15D17`. Its dependencies include Proposition **2.7.1** (permanent `4603E36ECC71`) and Lemma **2.7.2** (permanent `8734A1486521`).
- `docs/sections/measures-and-distributions--radon-measures-and-integration/index.html`, main blob `f0086e0d7fa46b8d1756eebb839b0ba14e663863`, **physical lines 7–15 and 22–28**: measures are **positive** by convention, and compact exhaustions have increasing interiors covering `Omega`.
- `docs/sections/measures-and-distributions--positive-linear-functionals/index.html`, main blob `0562702a346f7d8f09974afe97c90bc911bf7790`, **physical lines 65–73**: Theorem **2.3.3** (Riesz representation), source `foundations-of-pluripotential-theory:DE073A6A`, permanent tag `0C614771FB98`. This is the precisely identified internal representation dependency, not a newly certified theorem.

Let `Omega` be an open subset of `R^d` with a compact exhaustion `K_r`, and let `chi_r >= 0` be continuous, compactly supported, equal to 1 on `K_r`. Fix finite `M_r >= 0`. The printed set is
```
M = {positive Radon measures mu on Omega : integral chi_r dmu <= M_r for all r}.
```
No global bound on `mu(Omega)` is assumed. For every `r`, `mu(K_r) <= M_r` uniformly over `M`.

## New result: a concrete countable metric
There exists a **countable** family of real compactly supported continuous functions `(g_j)_{j>=1}` such that
```
d_vag(mu,nu) = sum_{j=1}^infinity 2^{-j}
               min(1, |integral g_j d(mu-nu)|)
```
is a metric on `M` inducing **exactly** its vague topology (not only its convergent sequences). Consequently `M` is compact metrizable, and **every sequence** in `M` has a vaguely convergent subsequence with limit in `M`. More strongly, a completely explicit diagonal proof of sequential compactness is available using Theorem 2.3.3; the general Tychonoff product of *all* test-function coordinates is not necessary here.

### Countable tests and support control
On `R^d`, take all finite rational combinations of dyadic-grid tensor-product piecewise-linear tent functions whose supports are contained compactly in `Omega`; add all the countably many `chi_r`. This is a countable family `D={g_j}`. Given `f in C_c(Omega,R)`, choose `r` such that `supp f` is compactly contained in `int K_r`. Uniform continuity, dyadic-grid multilinear interpolation, and rational approximation of its finitely many nodal values provide `g_j` with **both** `supp f` and `supp g_j` contained in `K_r`, and `||f-g_j||_infty < epsilon` for arbitrary `epsilon>0`. For sufficiently fine grids, all contributing tents remain in `int K_r` because `supp f` has a positive distance from its complement. This support control, not mere abstract density, is what permits a uniform mass estimate.

For any `mu,nu in M` and such a pair `f,g_j`,
```
|integral (f-g_j) d(mu-nu)| <= 2 M_r ||f-g_j||_infty .
```
Thus equality of all `g_j` integrals implies equality of all compactly supported continuous test integrals and hence of measures by the uniqueness clause of 2.3.3. The displayed series therefore separates points; symmetry, triangle inequality, and finite upper bound are immediate.

For **arbitrary nets**, vague convergence implies convergence of each fixed `g_j` coordinate and therefore convergence in `d_vag` by separating a finite prefix from the summable tail. Conversely, `d_vag` convergence implies convergence of every `g_j` coordinate; approximate each fixed `f` by a support-controlled `g_j` as above, bound the two approximation integrals by `2M_r epsilon`, and let `epsilon` decrease. This proves equality of the two **topologies**, rather than merely an equivalence for sequences.

### Direct diagonal subsequence argument
Given any sequence `(mu_n)` in `M`, for each fixed `g_j` choose `r(j)` with `supp g_j subset K_{r(j)}`. Then
```
|integral g_j dmu_n| <= M_{r(j)} ||g_j||_infty
```
uniformly in `n`. Successive Bolzano–Weierstrass extractions and a diagonal choice yield a subsequence `(mu_{n_k})` for which all countably many `g_j` integrals converge. For each `f in C_c(Omega,R)`, the support-controlled approximation estimate shows that `(integral f dmu_{n_k})` is Cauchy. The limit functional `L(f)` is linear and positive. Applying the **specified existing Riesz theorem 2.3.3** produces a positive Radon measure `mu`; since `chi_r` is a compactly supported test,
```
integral chi_r dmu = lim_k integral chi_r dmu_{n_k} <= M_r .
```
Thus `mu in M`, and by construction `mu_{n_k}` converges vaguely to `mu`. This argument never assumes a convergent subsequence in an arbitrary product or invokes sequential compactness of a nonmetrizable space.

## Boundary of the result and classification
The conclusion depends on the **Euclidean, second-countable, locally compact** test-function setting and uniform compact-set mass control. It does **not** license the substitution of sequences for nets in arbitrary topological products, the compactness of general current spaces without corresponding bounds, nor weak convergence against every bounded continuous function on a noncompact `Omega`. No false theorem or missing hypothesis was found in Theorem 2.7.3: this is a strengthened result and an alternative sequential proof. The internal Riesz representation theorem remains a dependency, not an independently certified theorem.

**Proposed documentation-only addition:** after Theorem 2.7.3, optionally insert a short corollary asserting compact metrizability and vague sequential compactness for its Euclidean hypotheses, with the support-controlled countable-test argument. Do not change theorem text, canonical tags, or source records without separate review. **Dependents/scope:** strengthens the available compactness mechanism for locally bounded positive Radon measures; arbitrary currents and other topologies require separate testing.

**Coverage:** direct selected review of §2.7 Theorem 2.7.3 with its proof, net and product preliminaries; dependency-only crosscheck of §2.2 and §2.3.3; no whole-section certification, and no statement about the excluded Demailly programme. No software test, build, CI, formal verification or publication is claimed.
