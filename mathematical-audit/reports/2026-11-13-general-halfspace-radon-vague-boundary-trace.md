# Canonical vague boundary trace for every positive half-space harmonic function

**Finding ID:** POME-HALFSPACE-GENERAL-RADON-VAGUE-TRACE-001  
**Classification:** low / **verified conditional deduction**. The printed half-space representation is not false.  
**Date:** 2026-11-13. **Reviewed main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

## Precisely inspected reading edition

- Integrated file: docs/sections/kelvin-transforms-and-half-space-potentials/index.html; main blob f2615a5393af724c3996978212162f94911ff9d9.
- Theorem **3.2.6** (nonnegative harmonic half-space representation), source **classical-potential-theory:1C8A330A**, permanent tag **6BC86EEF03A9**, physical lines **64–76**, proof of weighted Radon measure and converse lines **78–132**.
- Equation **3.2.7**, source **classical-potential-theory:C0A46F1A**, permanent tag **F3ED29BBAD39**, physical lines **66–69**.
- Equation **3.2.8**, source **classical-potential-theory:358F89A3**, permanent tag **8F7C774A9D89**, physical lines **70–74**.
- Poisson normalization **3.2.13** and Theorem **3.2.12**, source **classical-potential-theory:E7E82020** / **classical-potential-theory:BB6DAC3F**, permanent tags **AB2849CD8791** / **9ADD2DF19642**, lines **140–155**; normalization is used as the approximate-identity input.
- This report performs a new general-Radon boundary reconstruction. It is **not** the earlier 2026-11-02 conical large-height growth result and **not** the 2026-11-07 bounded-harmonic L-infinity isometry; those reports remain separately classified.

## Claim

Let $d\ge 2$, $H=\mathbb R^{d-1}\times(0,\infty)$, and $h\ge0$ be harmonic on $H$. Use exactly the representation printed in Theorem 3.2.6,
$$
h(x,t)=ct+\int_{\mathbb R^{d-1}}p_t(x-z)\,d\nu(z),\qquad
p_t(w)=\frac{2t}{s_{d-1}(|w|^2+t^2)^{d/2}},
$$
where $c\ge0$ and $\nu$ is a positive Radon measure satisfying
$$
I_\nu:=\int_{\mathbb R^{d-1}}(1+|z|^2)^{-d/2}\,d\nu(z)<\infty.
\tag{1}
$$
The total mass $\nu(\mathbb R^{d-1})$ need **not** be finite.

**New conclusion:** as $t\downarrow0$, the *locally finite* measures $h(x,t)\,dx$ converge **vaguely** to the full measure $\nu$:
$$
\boxed{\quad
\lim_{t\downarrow0}\int_{\mathbb R^{d-1}}\varphi(x)h(x,t)\,dx
=\int_{\mathbb R^{d-1}}\varphi(z)\,d\nu(z),
\qquad\varphi\in C_c(\mathbb R^{d-1}).
\quad}
\tag{2}
$$
Consequently the pair $(c,\nu)$ in Theorem 3.2.6 is **unique** within the printed admissible class: equation (2) reconstructs $\nu$ without any boundedness assumption on $h$ or density assumption on $\nu$, and
$$
c=\lim_{t\to\infty}\frac{h(0,t)}t
\tag{3}
$$
recovers the coefficient. The identity (3) was already audited in a different large-height study; **only the unrestricted vague boundary reconstruction and consequent full-pair uniqueness are new here**.

## Proof of the new boundary reconstruction

The normalization in printed Equation 3.2.13 gives $\int p_t=1$. Furthermore $p_t(w)=t^{-(d-1)}p_1(w/t)$ and $p_1\in L^1$, so $(p_t)$ is an approximate identity. Thus for every $\varphi\in C_c(\mathbb R^{d-1})$,
$$
\|p_t*\varphi-\varphi\|_\infty\longrightarrow0\qquad (t\downarrow0).
\tag{4}
$$
Indeed, use uniform continuity of $\varphi$ on a small ball and use the integrable tail of $p_1$ after the scaling change of variables. This does not involve the measure $\nu$.

Fix $\varphi$ and $R\ge1$ with $\operatorname{supp}\varphi\subset B_R$. The measure $h(\cdot,t)\,dx$ is locally finite since $h$ is smooth and finite on $H$. For $0<t\le1$ and $|z|\ge2R+2$, the support condition implies $|x-z|\ge |z|/2$ whenever $\varphi(x)\ne0$. Hence
$$
|(p_t*\varphi)(z)|
\le \frac{2t}{s_{d-1}}\int_{B_R}\frac{|\varphi(x)|\,dx}{(|x-z|^2+t^2)^{d/2}}
\le C_{\varphi,R,d}\,t(1+|z|^2)^{-d/2}.
\tag{5}
$$
The *entire* outside contribution has the uniform estimate
$$
\left|\int_{|z|\ge2R+2}(p_t*\varphi)(z)\,d\nu(z)\right|
\le C_{\varphi,R,d}\,t I_\nu\longrightarrow0.
\tag{6}
$$
This bound is essential: there is no justified appeal to finite total mass outside a compact set.

On the fixed closed ball $|z|\le 2R+2$, the Radon measure is finite. Equation (4) gives
$$
\int_{|z|\le2R+2}(p_t*\varphi)(z)\,d\nu(z)
\longrightarrow \int_{|z|\le2R+2}\varphi(z)\,d\nu(z)
=\int\varphi\,d\nu.
\tag{7}
$$
For nonnegative $\varphi$, Tonelli now yields the exact identity
$$
\int\varphi(x)h(x,t)\,dx
=ct\int\varphi\,dx+\int(p_t*\varphi)(z)\,d\nu(z).
\tag{8}
$$
Both sides are finite, and the same identity holds for signed or complex-valued $\varphi$ by decomposing real/imaginary parts and applying the same absolute estimate to $|\varphi|$. Equations (6)–(8), together with $ct\int\varphi\,dx\to0$, prove (2) for every compactly supported continuous test. No extraction of a subsequence, tightness of the full measure on the noncompact boundary, or interchange of unproved limits is required. The limit is taken over the entire directed parameter $t\downarrow0$.

For completeness, (3) follows directly from the printed representation:
$$
\frac{h(0,t)}t-c
=\frac2{s_{d-1}}\int(|z|^2+t^2)^{-d/2}\,d\nu(z).
$$
For $t\ge1$, the integrand is dominated by the integrable weight (1) and converges pointwise to zero, so dominated convergence proves (3). If two admissible pairs give the same $h$, their boundary traces coincide by (2), hence their Radon measures coincide; then (3) identifies their linear coefficients. This proves uniqueness without a finite-mass or absolute-continuity assumption.

## Why the topology cannot be silently strengthened

1. **Failure of total variation even for a probability trace.** Take $\nu=\delta_0$ and $c=0$. For every $t>0$, $h(x,t)\,dx=p_t(x)\,dx$ is an absolutely continuous probability measure, while $\delta_0$ is singular to it. With the usual total-variation norm of a signed measure,
$$
\|p_t(x)\,dx-\delta_0\|_{\rm TV}=2\qquad\text{for every }t>0.
$$
Nevertheless (2) holds. The printed theorem is not contradicted; only a hypothetical stronger TV conclusion would be false.
2. **Infinite admissible boundary mass.** Lebesgue measure $d\nu=dz$ satisfies (1) for $d\ge2$ because the boundary has dimension $d-1$. Its Poisson integral is $h\equiv1$, so the trace is infinite on the whole boundary and the family is naturally treated as locally finite Radon measures, *not* as a family of finite measures admitting narrow convergence. For the separate $ct$ contribution, even $h=t$ has an infinite total integral on the horizontal space for every $t>0$, yet its vague boundary trace is zero.

## Audit disposition

**Status:** verified conditional deduction, **low** severity, with a complete elementary proof of (2)–(3) *conditional on* the printed existence/normalization statements in §3.2. Theorem 3.2.6 is **not** labelled false and its entire upstream ball-boundary construction is **not** certified here. No dependence on Demailly approximation/regularization, Bergman, weighted $L^2$, Ohsawa–Takegoshi, multiscale atlas or positivity-loss completion was introduced.

**Suggested change, not applied:** add an optional corollary after Theorem 3.2.6 stating (2) and full-pair uniqueness. Preserve the historical attribution and all original/permanent tags. Relevant downstream uses include recovering general singular boundary data and interpreting the $ct$ Martin term; no particular existing downstream theorem was found incorrect.

**Coverage accounting:** new selected analysis inside previously partly audited §3.2; **zero credited new first-visited numbered sections and zero complete-section mathematical certifications**. Actual current reading ToC baseline: **25 chapters / 747 numbered sections**. Production main, source texts, registries, permanent labels, CI, builds and website are unchanged.