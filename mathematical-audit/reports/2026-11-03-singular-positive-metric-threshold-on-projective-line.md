# A sharp singular-metric positivity threshold on the projective line

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (2026-11-03).  
**Finding:** `POME-NADEL-STRICT-POLE-JUMP-001` — **low / verified conditional deduction**. The printed theorem has **not** been refuted. This is an independently verified boundary example and a limited proof-step check, not a repair or a proof of its excluded analytic inputs.

## Exact integrated reading-edition anchors

- `docs/sections/strictly-positive-singular-metrics/index.html`, main blob `0816e58d94c6cdd7dd6ee5d1de369ffcdf473b43`; section §10.102, permanent tag `9CCB2D58E4BE`, source `cao-paun-foliations:14FA4891`, physical line 5.
- Theorem **10.102.1**, permanent tag `4F4355678C85`, source `cao-paun-foliations:274E8A7B`, lines **8–13**. The proof's ideal and curvature passage is at lines **18–25**; its nonexcluded pointwise inverse-curvature algebra is at **27–33**. The remaining §10.102 proof lines **27–37** depend on complete/singular-weight L² theory.
- For the divisor/normalization check only: `docs/sections/complex-differential-forms-and-positive-currents--holomorphic-zeros-and-the-poincare-lelong-formula/index.html`, main blob `4231a246a84f17c3808a6f3164644f931aa0c654`; integrated Poincaré–Lelong Theorem 5.5.6, permanent tag `8D4BA339507E`, source `demailly-complex-geometry:09CD57CC`. This is a convention/dependency crosscheck, **not** a fresh certification of that proof.

Theorem 10.102.1 assumes a compact Kähler $Z$, a singular Hermitian metric $h$ on $B$, and the **strict** current inequality $c_1(B,h)\ge\delta\omega$ with \(\delta>0\). It concludes $H^q(Z,K_Z\otimes B\otimes\mathcal I$h$)=0$ for \(q\ge1\), with the full quadratic metric weight. The following example proves the strict inequality cannot be weakened simply to nonnegative curvature, **even with an ample underlying line bundle**.

## Direct calculation of the exact jump

Let $Z=\mathbf P^1$, let \(\omega=\omega_{\rm FS}\) be normalized by \(\int_Z\omega=1\), fix $p\in Z$, and choose $d\in\mathbb Z_{\ge1}$. Take $B=\mathcal O(d)$ with the standard smooth metric $h_0=h_{\rm FS}^{\otimes d}$. Let $s_p\in H^0(Z,\mathcal O(1))$ vanish simply at $p$. For **each real** $0\le a\le d$, define
$
\psi_a=a\log |s_p|_{h_{\rm FS}}^2,\qquad h_a=h_0e^{-\psi_a}.
$
Adding a constant to the weight if desired does not change curvature or the multiplier ideal.

With the book's $dd^c=\frac{i}{2\pi}\partial\bar\partial$, Poincaré–Lelong gives
$
dd^c\log|s_p|_{h_{\rm FS}}^2=[p]-\omega.
$
Hence
$
\boxed{c_1(B,h_a)=(d-a)\omega+a[p].}
$
In particular $c_1(B,h_a)\ge(d-a)\omega>0$ for $a<d$, whereas for $a=d$ the positive curvature current is $d[p]$, supported at one point. It cannot dominate any positive multiple of \(\omega\), since its restriction to the open set $Z\setminus\{p\}$ is zero.

Locally at $p$, choose coordinate $z$ and a nonvanishing smooth trivialization. Up to a smooth bounded term, \(\psi_a=a\log|z|^2\). A holomorphic germ \(f$z$=z^k g$z$\), $g(0)\ne0$, has $|f|^2e^{-\psi_a}\in L^1_{\rm loc}$ if and only if
$
\int_0^\varepsilon r^{2k-2a+1}\,dr<\infty
\quad\Longleftrightarrow\quad k>a-1
\quad\Longleftrightarrow\quad k\ge\lfloor a\rfloor.
$
The last equivalence also holds **at integral** $a$: the borderline $k=a-1$ gives logarithmic divergence. Therefore
$
\boxed{\mathcal I(h_a)=\mathcal O(-\lfloor a\rfloor p).}
$
The actual sheaf in the theorem is
$
K_Z\otimes B\otimes\mathcal I(h_a)
\simeq\mathcal O(d-2-\lfloor a\rfloor).
$
The elementary standard affine-cover Čech computation yields
$h^1(\mathbf P^1,\mathcal O(k))=\max\{-k-1,0\}$. One can see this by representing Čech classes by Laurent monomials on the overlap: for $k\le-2$, precisely \(-k-1\) negative powers remain after quotienting by sections on the two affine charts. Thus, without any analytic approximation or L² estimate,
$
\boxed{h^1\bigl(Z,K_Z\otimes B\otimes\mathcal I(h_a)\bigr)
=\max\{\lfloor a\rfloor-d+1,0\}.}
$
For **every** $0\le a<d$, this dimension is zero. At the endpoint $a=d$,
$
c_1(B,h_d)=d[p]\ge0,\quad
\mathcal I(h_d)=\mathcal O(-dp),\quad
K_Z\otimes B\otimes\mathcal I(h_d)=\mathcal O(-2),\quad
\boxed{h^1=1}.
$
Thus the strict positivity hypothesis is genuinely indispensable in this singular-metric formulation, notwithstanding the ampleness of $B$. The failure at the endpoint is induced by the jump of the ideal, not by failure of $B$ to be ample.

## Independent nonexcluded check of the inverse-curvature factor

In line 27–30 the displayed estimate reduces, with \(x_j=\lambda_j^{-1}\in(0,1]\) for $j\in J$ and \(|J|=q\ge1\), to
$
\frac{\prod_{j\in J}x_j}{\sum_{j\in J}x_j}\le\frac1q.
$
Indeed \(\prod_{i\in J}x_i\le x_j\) for each $j$, so summing proves the bound. The constant is optimal at $x_j=1$ (and for $q=1$ the ratio is identically one). It supplies the $2/(q\delta)$ algebraic coefficient in the printed inequality without asserting that the theorem's L² existence step, its cutoffs or its fine resolution has been verified.

## Status, dependent claims and proposal

**Status:** low / **verified conditional deduction** — explicit completely calculated threshold model; **no false printed theorem** and **no full verification** of Theorem 10.102.1. The existing strict positivity formulation passes this independent boundary test. **Proposed documentation-only clarification:** add the \(\mathbf P^1\) endpoint model as a remark after the theorem, without altering its statement or historical attribution; flag any downstream application that assumes mere $c_1(B,h)\ge0$ for separate review. No specific erroneous downstream application was identified in this limited pass.

**Dependency boundary:** the theorem's strong openness reference, quasi-equisingular analytic approximants `080EF8C715CF`, weighted/complete L² existence and extension estimates, logarithmic cutoffs, and local exactness are **not** re-proved or certified in this run. In particular the user's excluded Demailly approximation/regularization and dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale and positivity-loss completion programme remain **deferred-by-user**, not resolved. The metric example uses only the elementary local integrability definition, divisor curvature convention, and Čech cohomology.

**Coverage:** first limited direct proof-step and theorem-hypothesis audit of previously inventory-only **§10.102.1**, restricted to its formulation, the linear-algebra ratio, and a new explicit projective-line singular-metric boundary model; §5.5.6 was convention-checked only. The whole §10.102, all analytic dependencies and the whole project are **not certified**. Current table of contents: **25 chapters, 747 numbered sections, zero whole mathematical-section certificates**.

**Execution:** audit note only. No modification of production `main`, source proofs, registries, tags, publication, CI, project build, test suite or formalization.
