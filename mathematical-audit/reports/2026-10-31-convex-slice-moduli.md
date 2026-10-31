# Convex-section continuity: quantitative interior bound and failure of endpoint Hölder control

**Audit date:** 2026-10-31. **Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Scope:** elementary convex geometry in the integrated reading edition only; no production/source/registry/tag edits.

**Stable finding ID:** `POME-OKO-SLICE-MODULI-001`.
**Severity/status:** **low / verified conditional deduction**; the printed theorem is correct. The already existing `POME-OKO-SLICE-001` subsequence-quantifier proof gap and its proposed repair are **not** new findings and are **not** changed or certified as integrated.

## Exact integrated anchors and dependencies

- `docs/sections/almost-semigroups/index.html`, production blob `33898b2963ad0f8b7e30bf414276642f60925b74`.
- Lemma **19.7.9**, source `sgpt:68EC4013`, permanent tag `806DFD35CCE5`, physical lines **96–106** (compact convex sections and continuity), proof **108–134**, especially formula at **129–130**.
- Theorem **19.7.6**, source `sgpt:3312EB21`, permanent tag `AFBD46E7C0A4`, physical lines **45–59** (sequence characterization; existing proof-quantifier warning).
- Theorem **19.7.14**, source `sgpt:7B965039`, permanent tag `72547EEEBFE4`, physical lines **197–208** (slice continuity is used for the inductive multiplicative Brunn–Minkowski proof).
- Section location in current chapter 19 ToC: `docs/chapters/sections-okounkov/index.html`, §19.7 **Almost semigroups**.
- All mathematics below follows from elementary convexity and is independent of KK12/conductor, projective-volume asymptotics, and the user-excluded analytic regularization programme.

## New quantitative statement

Let \(K\subset\mathbb R^n\) be a nonempty compact convex set, with \(n\ge 1\), and let
\[
a=\min_{x\in K}x_1<b=\max_{x\in K}x_1,\qquad
K_t=\{y\in\mathbb R^{n-1}:(t,y)\in K\},\qquad
D=\operatorname{diam}_{\mathbb R^n}K.
\]
Every \(K_t\), \(a\le t\le b\), is nonempty, compact and convex. For every \(0<\delta\le (b-a)/2\) and all \(s,t\in[a+\delta,b-\delta]\),
\[
\boxed{\ d_{\rm Haus}(K_s,K_t)\ \le\ \frac{D}{\delta}|s-t|.\ }\tag{*}
\]
Thus the section map is Lipschitz on any compact *interior* projection interval. No positive Hölder exponent at an endpoint follows from compactness and convexity alone, even for a single positive-area planar convex body. Nor is there any uniform endpoint modulus over bodies contained in a fixed rectangle with the same projection interval.

### Complete elementary proof of (*)

Assume \(a+\delta\le t<s\le b-\delta\). Fix points \((b,z_b)\in K\) and \((a,z_a)\in K\). Given \(y\in K_t\), convexity puts
\[
y_s=\frac{b-s}{b-t}y+\frac{s-t}{b-t}z_b\in K_s.
\]
Both \((t,y)\) and \((b,z_b)\) lie in \(K\); the difference of their vertical coordinates is at most \(D\). Consequently,
\[
\operatorname{dist}(y,K_s)\le |y-y_s|\le D\frac{s-t}{b-t}
\le D\frac{s-t}{\delta}.
\]
Conversely, for any \(z\in K_s\), convexity gives
\[
z_t=\frac{t-a}{s-a}z+\frac{s-t}{s-a}z_a\in K_t,
\quad
\operatorname{dist}(z,K_t)\le D\frac{s-t}{s-a}
\le D\frac{s-t}{\delta}.
\]
Take both suprema in the definition of Hausdorff distance. Neither convergence of subsequences nor a nonempty interior assumption was used.

### Fixed-body logarithmic obstruction at an endpoint

In \(\mathbb R^2\) define \(T=e^{-3}\) and
\[
g(0)=0,\qquad g(t)=\frac{1}{\log(e/t)}\quad(0<t\le T),\qquad
K=\{(t,y):0\le t\le T,\ |y|\le g(t)\}.
\]
Put \(L(t)=\log(e/t)\ge4\). Direct differentiation gives
\[
g'(t)=\frac{1}{tL(t)^2},\qquad
g''(t)=\frac{2-L(t)}{t^2L(t)^3}<0.
\]
Thus \(g\) is nonnegative, increasing, continuous at \(0\), and concave on \([0,T]\). Its upper hypograph and reflected lower epigraph intersect in a **compact convex** set \(K\) of **positive planar area**. The slices satisfy
\[
K_0=\{0\},\quad K_t=[-g(t),g(t)],\quad
d_{\rm Haus}(K_t,K_0)=g(t).
\]
For every \(\gamma>0\),
\[
\lim_{t\downarrow0}\frac{d_{\rm Haus}(K_t,K_0)}{t^\gamma}
=\lim_{t\downarrow0}\frac{1}{t^\gamma\log(e/t)}
=+\infty.
\]
The printed continuity result therefore does **not** imply any fixed positive endpoint Hölder exponent, even with a fixed positive-volume body. In dimensions \(n>2\), product with a nonempty compact Euclidean ball in the remaining \(n-2\) vertical directions retains this obstruction.

### No uniform endpoint modulus across bounded bodies

For each \(0<h<1\), put
\[
g_h(t)=\min\{t/h,1\}\quad(0\le t\le1),\qquad
K^{(h)}=\{(t,y):0\le t\le1,\ |y|\le g_h(t)\}.
\]
Because \(g_h\) is concave, \(K^{(h)}\) is compact convex with positive area; every \(K^{(h)}\subset[0,1]\times[-1,1]\) and has projection interval \([0,1]\). Nevertheless
\[
d_{\rm Haus}(K^{(h)}_h,K^{(h)}_0)=1
\quad\text{while }h\downarrow0.
\]
Thus no body-independent endpoint modulus can be derived merely from a common outer bound and common projection interval. Moreover on the rising side \(t<h\) the exact section slope is \(1/h\), illustrating the interior-bound blow-up as an interior cutoff approaches the boundary.

## Mathematical disposition and dependents

The original **Lemma 19.7.9 is true**. The new contribution is the explicit interior Lipschitz estimate and two sharp *scope obstructions* to an endpoint regularity inference. It is **not** a false-theorem report, a proof-completion claim for the older `POME-OKO-SLICE-001` entry, or a claim about convergence of whole Okounkov bodies. In particular, when a proof using convex slices (including §19.7.14) passes to endpoint limits, it may use the printed continuity for each **fixed** body but cannot demand a uniform Hölder modulus across moving bodies without additional hypotheses.

**Proposed separately reviewable optional addition:** after Lemma 19.7.9, record (*) and the warning that endpoint continuity may be arbitrarily slower than a power. Preserve all source numbers, permanent tags, authorship and historical attribution. No existing theorem's hypotheses or statement need correction.

**Actual new proof coverage:** §19.7.9 quantitative two-sided convex interpolation and endpoint geometry; §19.7.6 and §19.7.14 inspected as context only. No entire section, KK12 result, analytic input or book is certified. Three exact rational piecewise-linear checks \(h=1/2,1/5,1/20\) separately confirmed slopes \(2,5,20\); they do not replace the proof. No build, CI, formalization or publication was run. The coverage inventory remains **25 chapters / 747 actual numbered ToC sections / zero whole mathematical section certifications**. All excluded Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work stays **deferred-by-user**.