# Chapter 15: dyadic singular sphere measures, sharp reference regularity, and lower-mass obstruction

**Date:** 2026-11-20. **Production baseline:** `main` `b6933b772f41b45918f7e25ed1afbbb1fd892272` (rechecked immediately before this report). **Audit branch:** `review/mathematical-audit`. **Classification:** `POME-SPHERE-DYADIC-HOLDER-SPECTRUM-001`, **low / verified conditional deduction**. This is not a false printed theorem, a certified transitive proof chain, or a production patch.

## Exact direct scope and stable locators

- Full mathematical reading of `docs/sections/equations-with-prescribed-singularities--singular-measures-on-shrinking-spheres/index.html`, physical lines **7–103**, blob **`354dfdf5224fac8896103ec09aa5936351021914`**. Equation 15.26.1 (source label `non-kahler-pluripotential-theory`, permanent `938F2C76C18A`, lines 10–14); Proposition 15.26.2 source label `non-kahler-pluripotential-theory-92442012`, permanent `8F3C95237950`, lines 27–65; Corollary 15.26.3 `AB5B44EC4BDD`, lines 70–80; Theorem 15.26.4 `6076D6F3256C`, lines 85–103.
- Full mathematical reading of `docs/sections/equations-with-prescribed-singularities--lower-mass-and-solvability-for-all-measures/index.html`, physical lines **7–158**, blob **`fc7d4f24f72d9b6ec898eedc961b789e65ef3e25`**. Lemma 15.27.1 permanent `CE5CA1071A3C`, lines 26–52; Lemma 15.27.2 `366F6832AB46`, lines 56–71; Theorem 15.27.3 source label `non-kahler-pluripotential-theory-59B533D4`, permanent `C7AA7377C144`, lines 76–108, equation 15.27.4 permanent `8D5EB0B8CCD7`; Corollaries 15.27.5–6 permanent `810CC86832BF`, `05B92E5A4684`, lines 112–158.
- **Selected dependencies only:** `docs/sections/plurisubharmonic-functions-and-singularities--local-products-and-capacity/index.html`, Lemma 5.27.25 lines **516–539**, blob `ddb2ac8d9de27a22152872e07e5e787d138a790e`, permanent `3242D4BA1F13`; statements/selected reasoning in Theorem 15.25.1 lines 11–19, blob `0defdec5270db7ff34625b638c9ac2a31264ca4a`, and Theorem 15.10.1 lines 11–17, blob `6240b6dc071d12eac1476ed548736d012c1a4fa2`. These checks are **not** full reviews of their enclosing sections. No Demailly regularization or excluded proof-completion programme was opened.

## POME-SPHERE-DYADIC-HOLDER-SPECTRUM-001 (low / verified conditional deduction)

**Assumptions.** Let \((X,h)\) be compact Hermitian of complex dimension \(n\ge2\). Keep the coordinate ball, cutoff \(\chi\), radii \(r_j=r_0 2^{-j}\), sphere probabilities \(\sigma_j\), and global cutoff functions
\[
\psi_j=\chi\log\max\{|z|^2,r_j^2\}+(1-\chi)
\]
from printed Proposition 15.26.2. They equal 1 outside the coordinate ball, and the *same* constant \(K\ge1\) gives \(dd^c\psi_j\ge-Kh\). Fix **any** \(0<\beta<1\). Define
\[
S_{n,\beta}=\sum_{j\ge1}r_j^{n\beta},\qquad
Z_\beta=2K\sum_{j\ge1}r_j^\beta,\qquad
d_{j,\beta}=\frac{r_j^\beta}{Z_\beta},
\]
\[
u_{\beta,0}=\sum_{j\ge1}d_{j,\beta}\psi_j,\qquad
u_\beta=u_{\beta,0}-\sup_Xu_{\beta,0},\qquad
\rho_\beta=\frac1{S_{n,\beta}}\sum_{j\ge1}r_j^{n\beta}\sigma_j.
\]

**Conclusions.** The measure \(\rho_\beta\) is a singular non-pluripolar probability. Moreover,
\[
u_\beta\in\operatorname{PSH}(X,h)\cap C^{0,\beta}(X),\qquad
h+dd^cu_\beta\ge\tfrac12h,
\]
\[
\operatorname{MA}_h(u_\beta)\ge
k_\beta\rho_\beta,\qquad
k_\beta=\frac{S_{n,\beta}}{Z_\beta^n}>0,\qquad
0<\operatorname{MA}_h(u_\beta)(X)<\infty.
\]
**Sharpness is for the specific explicit reference** \(u_\beta\), not for every possible potential dominating a fixed measure: at the coordinate center this \(u_\beta\) fails every \(C^{0,\gamma}\) estimate with \(\gamma>\beta\). For \(\beta=1/2\), it is the exact reference constructed in the printed Proposition 15.26.2, establishing the sharpness of *that construction's* exponent.

### Proof: boundedness, positivity and precise regularity

Since
\(\|\psi_j\|_\infty\le C(1+|\log r_j|)\) and
\(\sum_j r_j^\beta(1+j)<\infty\), the series for \(u_{\beta,0}\)
converges uniformly. The coefficients sum to \(1/(2K)\);
pass to \(dd^c\) in currents in the common inequality
\(dd^c\psi_j\ge-Kh\) to obtain \(h+dd^cu_{\beta,0}\ge h/2\).
Subtraction of its finite supremum has no effect on the curvature.

Let \(t=|z-z'|\) for points of the inner coordinate ball.
The radial functions satisfy
\[
|\psi_j(z)-\psi_j(z')|
\le2\log(1+t/r_j).
\]
For \(r_j\ge t\), use \(\log(1+t/r_j)\le t/r_j\):
\[
t\sum_{r_j\ge t}r_j^{\beta-1}=O(t^\beta)
\quad(0<\beta<1).
\]
This is a finite geometric sum whose final term dominates.
For \(r_j<t\), the geometric tails give
\[
\sum_{r_j<t}r_j^\beta\log(1+t/r_j)
\le C_\beta t^\beta\sum_{\ell\ge0}
2^{-\beta\ell}(1+\ell)=O(t^\beta).
\]
All \(\psi_j\) coincide with one fixed smooth function in the
cutoff transition region; elsewhere outside the inner ball the series
is smooth or constant. A finite cover and boundedness establish
\(u_\beta\in C^{0,\beta}(X)\). In particular the value at the center
is finite since \(\sum_j r_j^\beta|\log r_j|<\infty\).

For any \(N\), on the inner ball every \(dd^c\psi_j\) is positive.
The positivity of mixed bounded Bedford–Taylor products gives
\[
(h+dd^c\sum_{j\le N}d_{j,\beta}\psi_j)^n
\ge\sum_{j\le N}d_{j,\beta}^n(dd^c\psi_j)^n
=\sum_{j\le N}d_{j,\beta}^n\sigma_j.
\]
For the second equality we directly checked Lemma 5.27.25,
physical lines 522–539: under \(dd^c=\frac{i}{2\pi}\partial\bar\partial\)
the radial shell product equals a **normalized probability**, with
no extra \(n!\) factor. Uniform convergence of the bounded potentials
implies weak Bedford–Taylor convergence. Fix a finite subset of
diagonal terms, pass to the weak limit under a nonnegative test
function, then exhaust the finite subsets. This yields the asserted
global lower bound (all spheres lie inside the inner ball).
The sphere probabilities charge no pluripolar set by that same
lemma, so neither does their countable convex sum.
Their supports form a countable union of real hypersurfaces, hence
\(\rho_\beta\perp dV\). Finite-chart bounded-potential estimates
give finite total Monge–Ampère mass, and the lower bound makes it
positive.

### Exact dyadic sharpness and log-periodic profile

Let \(e\) be any unit vector, \(q=2^{-\beta}\), and \(k\) so large
that \(r_ke\) and 0 lie in the inner ball. Then
\[
\begin{aligned}
u_\beta(r_ke)-u_\beta(0)
&=\frac{2}{Z_\beta}\sum_{j>k}r_j^\beta\log(r_k/r_j)\\
&=\frac{2r_k^\beta\log2}{Z_\beta}
\sum_{\ell\ge1}\ell 2^{-\beta\ell}\\
&=\frac{2r_k^\beta\log2}{Z_\beta}
\frac{q}{(1-q)^2}>0.
\end{aligned}
\]
For any \(\gamma>\beta\), division by \(r_k^\gamma\) diverges,
proving failure of \(C^{0,\gamma}\) *at the center*. More precisely,
for \(r=tr_k\) and \(1/2\le t\le1\), one has
\[
u_\beta(re)-u_\beta(0)=
\frac{2r_k^\beta}{Z_\beta}
\left[\frac{q}{1-q}\log t+
\frac{q\log2}{(1-q)^2}\right].
\]
After division by \(r^\beta\), this displays a nonconstant
dyadically periodic profile in the logarithmic radial scale;
there is no single universal constant leading coefficient.

### Existing theorem consequences and proposed correction

If \(\nu\ne0\) and \(\nu\le M\rho_\beta\) with \(M<\infty\),
then \(\nu\le(M/k_\beta)\mathrm{MA}_h(u_\beta)\).
Printed Theorem 15.25.1 *conditionally* gives a normalized Hölder
homogeneous solution with some positive coefficient; printed
Theorem 15.10.1 *conditionally* gives the unique **bounded**
exponential solution for every \(\lambda>0\). We **do not**
certify the complete proof chains of these input theorems,
nor uniqueness among unbounded exponential solutions.

**Status:** low / verified conditional deduction; no false theorem
or independently certified repair. **Proposed correction:** optional
remark after Proposition 15.26.2 describing the beta-family, without
editing the original fixed measure, permanent tags, provenance or
normalizations. **Dependents:** optional extensions of Corollary
15.26.3 and Theorem 15.26.4 only.

## Direct audit of all mathematical §15.27 (no new printed error)

- Lemma 15.27.1 (lines 26–52): with \(a>c_h(q)\),
  \(\tau=c_h(q)/a<1\), the strict domination comparison applied
  to each *bounded* translate \(v+A\) yields \(v+A\ge u\) for
  every real \(A\), contradicting the existence of a finite point
  of \(u\). The monotonicity \(q\le r\Rightarrow c_h(q)\ge c_h(r)\)
  and homogeneity \(c_h(tq)=c_h(q)/t\) have the correct direction.
  Theorem 15.2.2 is a **declared upstream dependency**.
- Lemma 15.27.2 (lines 56–71): the Gauduchon trace bound
  controls \(c_h(q_j)\) from above, and the lower-density estimate
  and bounded \(L^p\)-norm control it from below. The argument
  takes ordinary subsequences and uses valid sequential compactness;
  it makes no net-to-sequence inference. Theorems 14.19.19
  and 14.19.21 are **uncertified upstream dependencies**.
- Theorem 15.27.3 (lines 76–108): the mixture weights
  \(2^{-j}\) sum to one, the density is bounded below by
  \(\frac12\min_Xf_1>0\), and any positive scaled subsolution
  would force \(a2^{-j}\le c_h(f_j)\le2^{-2j}\) for every \(j\),
  a contradiction. The lower-mass scalar infimum relies on
  Theorems 12.15.4 and 12.2.3, not transitively certified here.
- Corollaries 15.27.5–6 and notes (lines 112–158):
  the envelope-class equivalence uses Theorem 15.37.4;
  an \(L^p\) (\(p>1\)) density has a continuous scaled
  solution by the referenced result; mixing
  \(g_t=(1-t)g+tf\) gives \(L^1\) density of measures
  without positive scaled subsolutions. The text **correctly
  does not exclude unbounded exponential solutions**.

No additional confirmed original mathematical error or separate
proof gap was found. External/internal **upstream still to certify**
include 15.2.2, 12.15.4, 12.2.3, 14.19.19/.21,
15.37.4, 15.25.1 and 15.10.1. Any analytic regularization
dependency remains recorded, **not reopened**.

**Coverage delta:** two entire direct mathematical section
readings, three selected prerequisite checks, zero fully certified
transitive proof chains; prior historical first visits unreconciled.
Demailly regularization/Bergman/L2/Ohsawa–Takegoshi/multiscale/
positivity-loss programmes remain **deferred-by-user**.
No tests, build, CI, publication, source/registry or main changes.
