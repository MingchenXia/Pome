# Quantitative L1-to-capacity bound for bounded-density Dirichlet solutions

2026-11-19. Finding **POME-BT-DIRICHLET-L1-CAPACITY-MODULUS-001**: **low / verified conditional deduction**. The printed statements are not refuted; their full transitive dependency chains have not been certified.

## Source lock and actual coverage

Reviewed main SHA: b6933b772f41b45918f7e25ed1afbbb1fd892272. Integrated file: docs/sections/bedford-taylor-products-and-local-capacity--bounded-measurable-densities/index.html, blob 762b841b0cb243784dc988f04dbf2779da66c469.

The directly reviewed §7.10 reading edition is in physical lines 5–110. Lemma 7.10.1 is source foundations-of-pluripotential-theory:74804636, permanent C09E42A43E93, statement lines 10–15 and proof lines 17–35. Theorem 7.10.2 is source foundations-of-pluripotential-theory:9C25B561, permanent C9116FCEFCD2, statement lines 37–47, proof steps 1–4 lines 49–108. The section tag is D4D4A913D86D.

Prerequisite *context only*: §7.5.4, source foundations-of-pluripotential-theory:34043611, permanent 56B45ADBA326, physical lines 63 onward of docs/sections/bedford-taylor-products-and-local-capacity--quasi-continuity-and-convergence-in-capacity/index.html, blob 464778b7ca6f1a456e36b24ecb4a0c93ab6948d3; §7.9.2, source foundations-of-pluripotential-theory:69935D4D, permanent A092925717E1, statement physical lines 41–51 and normalization line 58 of docs/sections/bedford-taylor-products-and-local-capacity--the-ball-dirichlet-problem-with-continuous-density/index.html, blob ff1d5dfff1913156b45875eabf921f60af553b99.

## New precise deduction

Let B=B(a,R) be a ball in C^n, n≥1, with $\eta=dd^c|z|^2$ and the Pome normalization $dd^c=(i/2\pi)\partial\bar\partial$. Let $u,v\in\operatorname{PSH}(B)\cap L^\infty(B)$ have the same continuous boundary trace $\varphi\in C(\partial B)$ in the pointwise boundary-limit sense. Assume
\[
0\le(dd^cu)^n\le M\eta^n,\qquad 0\le(dd^cv)^n\le M\eta^n,\quad M<\infty.
\]
Then for every $\varepsilon>0$,
\[
\boxed{\operatorname{Cap}_B^*(\{|u-v|>\varepsilon\})
\le \frac{(n+1)^{n+1}}{n^n}
\frac{M}{\varepsilon^{n+1}}\int_B|u-v|\,\eta^n.}\tag{*}
\]
This is **global outer Bedford–Taylor capacity**, not just local capacity. In particular, it applies to the two solutions $U_{f,\varphi},U_{g,\varphi}$ of the printed Theorem 7.10.2 whenever $0\le f,g\le M$ a.e. and they have the *same* boundary data. No estimate of this type is claimed for arbitrary different boundary traces or unbounded psh functions.

### Complete argument

**1. Compactness at the boundary.** For every $s>0$, $\{u<v-s\}\Subset B$, and similarly with u and v swapped. Otherwise a sequence in the relevant error set would approach a boundary point after taking a subsequence; the common pointwise limit $\varphi$ gives the contradiction $0\le-s$. This is exactly the compact-sublevel hypothesis of Lemma 7.10.1.

**2. One-sided comparison.** For any $s,t>0$, printed Lemma 7.10.1 and the measure upper bound give
\[
t^n\operatorname{Cap}_B(\{u<v-s-t\})
\le\int_{\{u<v-s\}}(dd^cu)^n
\le M\int_{\{u<v-s\}}\eta^n
\le \frac{M}{s}\int_B(v-u)_+\,\eta^n.\tag{1}
\]
All sets are Borel and both Monge–Ampère measures are Bedford–Taylor measures of bounded psh functions.

**3. Arbitrary-threshold outer regularization.** A careful reading of the Tietze-extension proof of printed Lemma 7.5.4 (which states the threshold pair $\delta,\delta/2$) shows the same argument gives, for any real-valued Borel quasi-continuous h, compact $K\subset\operatorname{Int}L\Subset B$, and $0<b<c$,
\[
\operatorname{Cap}_B^*(K\cap\{h>c\})
\le\operatorname{Cap}_B(L\cap\{h>b\}).\tag{2}
\]
Indeed, choose an open G of arbitrarily small capacity such that h is continuous on L\G, extend h|_(L\G) continuously to the ambient metric space, and cover the left set by $G\cup(\operatorname{Int}L\cap\{\tilde h>b\})$. The portion outside G lies in $L\cap\{h>b\}$; send $\operatorname{Cap}_B(G)$ to zero. Both $(v-u)_+$ and $(u-v)_+$ are real-valued quasi-continuous by the printed §7.5.2 and the closure remark after Definition 7.5.1.

**4. Optimize the two comparison thresholds.** Fix $\varepsilon>0$ and $0<\alpha<\varepsilon$. Choose K compact containing $\{u<v-\varepsilon\}$ and L a compact neighborhood of K. Apply (2) to $h=(v-u)_+$ with $c=\varepsilon$, $b=\varepsilon-\alpha$. Then apply (1) with
\[
s=\frac{\varepsilon-\alpha}{n+1},\qquad
t=\frac{n(\varepsilon-\alpha)}{n+1};
\quad\frac1{s\,t^n}=\frac{(n+1)^{n+1}}{n^n(\varepsilon-\alpha)^{n+1}}.
\]
Let $\alpha\downarrow0$. This yields
\[
\operatorname{Cap}_B^*(\{u<v-\varepsilon\})
\le\frac{(n+1)^{n+1}M}{n^n\varepsilon^{n+1}}
\int_B(v-u)_+\,\eta^n.
\]
Switching u,v gives the analogous estimate involving $(u-v)_+$. Outer-capacity subadditivity and $(u-v)_++(v-u)_+=|u-v|$ prove (*). The density normalization $\eta^n=n!\pi^{-n}dV_{2n}$ is consistent with the printed convention.

### Sharp homogeneity (not a claim about the prefactor)

The exponent n+1 is forced among homogeneous inequalities $C_n M\varepsilon^{-p}\int_B|u-v|\eta^n$ with constants independent of the amplitude. On B(0,R) take $u_\lambda=\lambda(|z|^2-R^2)$, $v_\lambda=0$, $M_\lambda=\lambda^n$, and $\varepsilon_\lambda=\lambda R^2/2$. The error set $B(0,R/\sqrt2)$ has strictly positive capacity independent of $\lambda$, whereas the right-hand side of the proposed p-exponent bound scales as $\lambda^{n+1-p}$. It vanishes as $\lambda\downarrow0$ for $p<n+1$ and as $\lambda\uparrow\infty$ for $p>n+1$. Thus p=n+1 is mandatory. We do **not** assert that the displayed numerical constant is best possible.

## Printed-proof audit and dependency classification

- Lemma 7.10.1 lines 10–35: checked the nested sublevels, boundary comparison condition, positivity of every mixed term, orientation of the comparison inequality and capacity supremum. No new defect.
- Theorem 7.10.2 Step 1, lines 54–63: mollified nonnegative density stays in [0,M]; barriers H_(M,phi) and H_(0,phi) give boundary trace and uniform boundedness; local L1 extends to global L1 on a finite-volume ball. No new defect.
- Step 2, lines 64–79: upper tail via Hartogs lemma on a quas i-continuity good set, lower tail via precompact error sets and density bound, and outer-capacity passage checked. The quantitative estimate (*) improves this step by treating two solutions symmetrically and optimizing thresholds.
- Steps 3–4, lines 80–108: local-capacity continuity identifies the limiting MA measure; the strictly positive $\varepsilon^n\eta^n$ perturbation forces envelope maximality, then uniqueness; the common barrier gives subsequence-to-full-sequence convergence; a constant handles boundary variation; convolution of the nth roots preserves the L-infinity difference. No new confirmed false statement or independent proof gap found.

**Uncertified upstream:** Bedford–Taylor comparison §7.3.11, quasi-continuity §7.5.2, convergence §7.5.8, Hartogs compactness §5.10.4, continuous-density Dirichlet §7.9.2 and product calculus. Their use remains conditional, notwithstanding the direct local inspection of §§7.5.4 and 7.9.2.

**Proposed correction/extension:** optionally add (*) as a corollary of printed Lemma 7.10.1 and quasi-continuity, recording both density upper bounds and *identical continuous boundary data*. Affected potential dependents: bounded-density ball Dirichlet stability, Bedford–Taylor comparison, capacity/convergence and equal-boundary local patching. This is an optional additive proof, **not** a correction of a false theorem. No source/body/registry/identifier edits were made.

**Status:** low / verified conditional deduction, no new confirmed error. Existing Demailly regularization, Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss projects remain **deferred-by-user**, never resolved or certified. Actual new scope: **+1 entire direct-section proof review of §7.10**, no transitive-chain certification, no claim of a first-ever visit. No builds, tests, CI or website publication were run.
