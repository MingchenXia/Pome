# Bounded half-space harmonic functions: unique $L^\infty$ Poisson traces

**Finding:** `POME-HALFSPACE-BOUNDED-POISSON-ISOMETRY-001`  
**Severity/status:** low / **verified conditional deduction**. This does **not** refute a printed theorem or certify all upstream arguments.  
**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` on 2026-11-07.

**Integrated source and exact anchors.** `docs/sections/kelvin-transforms-and-half-space-potentials/index.html`, main blob `f2615a5393af724c3996978212162f94911ff9d9`, physical lines **55–75, 80–136, 138–180**. Theorem 3.2.6 source `classical-potential-theory:1C8A330A` / permanent `6BC86EEF03A9`; Equation 3.2.7 source `classical-potential-theory:C0A46F1A` / permanent `F3ED29BBAD39`; Equation 3.2.8 source `classical-potential-theory:358F89A3` / permanent `8F7C774A9D89`; Theorem 3.2.12 source `classical-potential-theory:BB6DAC3F` / permanent `9ADD2DF19642`; Equation 3.2.13 source `classical-potential-theory:E7E82020` / permanent `AB2849CD8791`.

**Internal measure dependency.** `docs/sections/measures-and-distributions--densities-and-differentiation-of-integrals/index.html`, main blob `1b600ca8444edebc8e05e300cb86ae371e9f8535`, physical lines **7–46**, Lemma 2.8.1 source `foundations-of-pluripotential-theory:43819F13` / permanent `9790D3B21542`.

## Claim

Fix $d\ge2$ and $H=\mathbb R^{d-1}\times(0,\infty)$. Put
$$
p_t(x')=\frac{2t}{s_{d-1}(|x'|^2+t^2)^{d/2}}.
$$
The Poisson operator
$$
\mathcal P:L^\infty(\mathbb R^{d-1})\longrightarrow
\mathscr H_b(H),\qquad
f\longmapsto\big((x',t)\mapsto (p_t*f)(x')\big)
$$
is a **linear isometric bijection** onto the space of real-valued bounded harmonic functions, with supremum norm. In particular, any nonnegative bounded harmonic $h$ has representation $h=p_t*g$ for **unique** $g\in L^\infty$, $0\le g\le\|h\|_\infty$ a.e.; there is no $ct$ term or singular boundary measure.

The already printed Theorems 3.2.6 and 3.2.12 are **correct**. The new result narrows them to the bounded class and proves uniqueness of the $L^\infty$ trace, not claimed explicitly in §3.2.

## Complete new deduction

Let $m=d-1$. Formula (3.2.13) says $\int_{\mathbb R^m}p_t=1$. The scaling $p_t(x)=t^{-m}p_1(x/t)$ and integrability of $p_1$ give, for every $\varphi\in C_c(\mathbb R^m)$, the approximate-identity limit $p_t*\varphi\to\varphi$ uniformly: use uniform continuity inside a fixed $\delta$-ball and the vanishing $\int_{|y|>\delta}p_t(y)\,dy$ outside.

**Step 1: vanishing atom at infinity.** If $0\le h\le M$, Theorem 3.2.6 gives
$$
h(x',t)=ct+\int_{\mathbb R^m}p_t(x'-z)\,d\nu(z),\quad
c\ge0,\quad \nu\ge0,\qquad
\int_{\mathbb R^m}(1+|z|^2)^{-d/2}\,d\nu(z)<\infty.
$$
As $ct\le M$ for every $t>0$, necessarily $c=0$.

**Step 2: boundary convergence for a possibly infinite measure.** For nonnegative $\varphi\in C_c^\infty(\mathbb R^m)$, Tonelli gives
$$
I_t:=\int_{\mathbb R^m}\varphi(x')h(x',t)\,dx'
=\int_{\mathbb R^m}(p_t*\varphi)(z)\,d\nu(z)
\le M\int_{\mathbb R^m}\varphi\,dx'.
$$
We prove $\lim_{t\downarrow0}I_t=\int\varphi\,d\nu$, **without assuming finite total mass of $\nu$**. Fix $R\ge1$ with $\operatorname{supp}\varphi\subset B_R$. For $|z|\le2R$ we have uniform convergence $(p_t*\varphi)(z)\to\varphi(z)$ and $\nu(\overline B_{2R})<\infty$. If $0<t\le1$, $|z|>2R$, and $x'\in\operatorname{supp}\varphi$, then $|z-x'|\ge|z|/2$, so
$$
0\le(p_t*\varphi)(z)
\le C_{\varphi,R}\,t(1+|z|^2)^{-d/2}.
$$
The total tail integral is at most $C_{\varphi,R}t\int(1+|z|^2)^{-d/2}d\nu$, which tends to zero. It follows that
$$
\int\varphi\,d\nu
=\lim_{t\downarrow0}I_t
\le M\int\varphi\,dx'.
$$
The inequality for all nonnegative compactly supported tests implies $\nu\le M\,dx'$ as Radon measures. Applying the **internally proved** Lemma 2.8.1, $\nu=g\,dx'$ with $0\le g\le M$ almost everywhere. Thus $h=p_t*g$.

**Step 3: arbitrary signs.** Let $u$ be real bounded harmonic and $M=\|u\|_\infty$. Apply Steps 1–2 to $h=u+M\in[0,2M]$ and obtain $h=p_t*g$, $0\le g\le2M$. By (3.2.13), $p_t*1=1$, so
$$
u=p_t*f,\qquad f=g-M,\qquad \|f\|_\infty\le M.
$$

**Step 4: converse, injectivity and sharp norm.** Theorem 3.2.12 shows that $p_t*f$ is bounded harmonic and
$\|\mathcal P f\|_\infty\le\|f\|_\infty$.
For each $\varphi\in C_c^\infty(\mathbb R^m)$, Fubini implies
$$
\int\varphi(x')(p_t*f)(x')\,dx'
=\int(p_t*\varphi)(z)f(z)\,dz.
$$
Translation continuity in $L^1$ and the normalized approximate identity yield
$\|p_t*\varphi-\varphi\|_{L^1}\to0$. Consequently,
$$
\lim_{t\downarrow0}\int\varphi(x')(p_t*f)(x')\,dx'
=\int\varphi(x')f(x')\,dx'.
$$
Two equal Poisson extensions thus have equal boundary distributions and agree almost everywhere. The construction in Step 3 gives
$\|f\|_\infty\le\|\mathcal Pf\|_\infty$, and the printed Poisson bound gives the reverse inequality: **the operator is an isometry**.

## Genuine boundary phenomena and status

The function $h(x',t)=t$ is positive harmonic with vanishing finite-boundary trace but unbounded growth; it illustrates why the $ct$ term in (3.2.7) cannot be suppressed without a boundedness hypothesis. The atom-at-zero Poisson harmonic function $h(x',t)=p_t(x')$ is positive with $c=0$, but is unbounded near $(0,0)$ and has singular representing measure $\delta_0$. These are two different failure modes.

**Dependencies and limitations.** This verifies Steps 1–4 *conditional* on the printed positive half-space representation (Theorem 3.2.6), Poisson harmonicity and normalization (Theorem 3.2.12, Equation 3.2.13), internal bounded Radon-density Lemma 2.8.1, and elementary integration/approximate identity. It does not certify their entire transitive proof chains. No Demailly approximation/regularization or dedicated Bergman/weighted-$L^2$/Ohsawa–Takegoshi/multiscale/positivity-loss work was used.

**Proposed separately reviewable correction (optional):** insert the bounded-class isometric representation as a corollary after §3.2.12. Affected dependents are uniqueness of bounded half-space Dirichlet solutions and interpretation of the nonzero $ct$ freedom. No source-body, canonicalization, registry, permanent-tag or production changes have been made.

**Coverage:** selected new proof in previously partly audited §3.2; §2.8.1 is a checked internal *dependency*, not a fresh full proof. No first-visit recount, no entire-section certification. Current ToC baseline: 25 chapters / 747 numbered sections / 0 whole-section mathematical certifications.
