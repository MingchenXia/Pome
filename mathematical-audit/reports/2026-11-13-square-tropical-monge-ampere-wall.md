# 2026-11-13 — An exact square-slope wall crossing for real Monge–Ampère atoms

**Finding:** `POME-TORIC-SQUARE-DIAGONAL-ATOM-WALL-001`  
**Severity / status:** **low / verified conditional deduction** (an independent polyhedral test and exact refinement; the printed results are **not false**).

## Production edition and precise anchors

Reviewed **main**: `b6933b772f41b45918f7e25ed1afbbb1fd892272` (current at inspection).
- `docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html`, blob `7089aa41ae2422b1bd6b5094e46668cbc8ed37be`. Theorem **21.5.1**, source `foundations-of-pluripotential-theory:4A0FAEB3`, permanent tag `409656CC47D4`, physical lines **10–39** (especially the `n!` Alexandrov normalization and inverse-gradient pushforward at lines 11–21); Theorem **21.5.2**, source `foundations-of-pluripotential-theory:6403CF44`, permanent tag `F4072D9ED060`, physical lines **43–85** (vague stability under locally uniform convergence, and full mass).
- `docs/sections/convex-analysis-and-toric-potentials--compact-convex-envelopes-and-full-mass-limits/index.html`, blob `b3b4e34fff767a717df812a381f905589b257fb3`. Lemma **21.6.1**, source `foundations-of-pluripotential-theory:30FFD831`, permanent tag `FCDAD9CEC8CE`, physical lines **10–28** (compact-domain convex envelope); Lemma **21.6.2**, source `foundations-of-pluripotential-theory:55EDF0D7`, permanent tag `F2FABB0A312F`, physical lines **32–46** (vague plus total mass implies narrow convergence).
- Internal convex duality dependency: Theorem 21.3.2 (Fenchel–Moreau), permanent tag `011FA81B0000`. Its full proof was not re-certified here.

## Exact example and statements

Let \(N_{\mathbb R}=M_{\mathbb R}=\mathbb R^2\), with standard lattice volume, let \(P=[0,1]^2\), and for every \(c\in\mathbb R\) put
\[
 F_c(x,y)=\max\{0,\ x,\ y,\ x+y+c\},\qquad F_0=x_++y_+.
\]
Every \(F_c\) is a finite globally Lipschitz convex function with the **same exact slope body** \(K_{F_c}=P\); hence its Pome-normalized Alexandrov measure has mass \(2!\operatorname{vol}(P)=2\). Both primal potentials and their Legendre conjugates satisfy the **global** bounds
\[
 \|F_c-F_0\|_{L^\infty(\mathbb R^2)}
 =\|F_c^*-F_0^*\|_{L^\infty(P)}=|c|.
\]

Despite this global uniform convergence, the complete real Monge–Ampère measure is
\[
 \operatorname{MA}_{\mathbb R}(F_c)=
 \begin{cases}
 \delta_{(-c,0)}+\delta_{(0,-c)},&c>0,\\
 2\delta_{(0,0)},&c=0,\\
 \delta_{(0,0)}+\delta_{(-c,-c)},&c<0.
 \end{cases}                                                    \tag{1}
\]
In particular the square has two distinct regular triangulations on either side of \(c=0\), while at the wall both atoms coalesce. This explicit *secondary-fan/diagonal* switch preserves the entire slope body and its total volume; no mass escapes to infinity.

Write \(\nu_c=\frac12\operatorname{MA}_{\mathbb R}(F_c)\) (probabilities). For \(c>0\) and **every** \(1\le p\le\infty\), Euclidean Wasserstein distances obey
\[
 W_p(\nu_c,\nu_0)=c\quad\text{while}\quad
 \|\nu_c-\nu_0\|_{\mathrm{TV}}=2.                        \tag{2}
\]
Here \(\|\sigma\|_{\mathrm{TV}}=|\sigma|(\mathbb R^2)\), rather than half that norm. For \(c=-d<0\), \(W_p(\nu_{-d},\nu_0)=2^{1/2-1/p}d\) for finite \(p\) (and \(\sqrt2d\) for \(p=\infty\)), whereas \(\|\nu_{-d}-\nu_0\|_{\mathrm{TV}}=1\). Thus even globally uniform convergence of both \(F_c\) and \(F_c^*\), full mass, and convergence in **every** finite Wasserstein topology do **not** imply total-variation convergence. This is not the earlier distant-mass \(W_1\) obstruction in §21.6 or the §21.5.3 escape example.

## Self-contained polyhedral derivation

Name the four slope vectors \((0,0),(1,0),(0,1),(1,1)\) and their affine intercepts \(0,0,0,c\). For a proposed slope \((p,q)\), use convex-combination weights \((\lambda_{00},\lambda_{10},\lambda_{01},\lambda_{11})\ge0\) of sum one, constrained by
\[
 p=\lambda_{10}+\lambda_{11},\qquad q=\lambda_{01}+\lambda_{11}.
\]
A feasible combination exists **exactly** for \((p,q)\in P\). Writing \(t=\lambda_{11}\), all such combinations are parametrized by the closed interval
\[
 \max(0,p+q-1)\le t\le\min(p,q),
\]
with \(\lambda_{10}=p-t,\ \lambda_{01}=q-t,\ \lambda_{00}=1-p-q+t\).

The convex conjugate is the closed convex envelope of the four costs \(0,0,0,-c\). More explicitly, its finite value is the minimum of \(-ct\) over the preceding interval:
\[
 F_c^*(p,q)=
 \begin{cases}
 -c\min(p,q),&c>0,\\
 0,&c=0,\\
 (-c)\max(0,p+q-1),&c<0,
 \end{cases}\qquad (p,q)\in P,                         \tag{3}
\]
and \(F_c^*=+\infty\) outside \(P\). To check (3) without an unproved exchange of infima, call the right-hand side \(G_c\). It is closed and convex (on \(P\), \(-c\min(p,q)\) is a maximum of two affine functions for \(c>0\), and the \(c<0\) expression is likewise a maximum). Directly,
\[
 G_c^*(x,y)
 =\sup_{\lambda\in\Delta_4}\sum_{ij}\lambda_{ij}
   \bigl(\langle(i,j),(x,y)\rangle+a_{ij}\bigr)
 =\max\{0,x,y,x+y+c\}=F_c.
\]
The middle equality is valid because the original four-weight simplex is compact and the expression is affine in its weights. Closed convex biconjugacy then yields \(G_c=F_c^*\).

The conjugate is differentiable at Lebesgue-a.e. point of the interior of \(P\). When \(c>0\), its gradients are \((-c,0)\) on the open triangle \(p<q\) and \((0,-c)\) on \(p>q\). Each triangle has lattice area \(1/2\). When \(c<0\), the gradients are \((0,0)\) on \(p+q<1\) and \((-c,-c)\) on \(p+q>1\), again on two area-\(1/2\) triangles. When \(c=0\), the gradient is identically zero on the interior. The diagonals and the boundary of \(P\) have two-dimensional Lebesgue measure zero. Theorem 21.5.1's gradient pushforward, **including the factor \(2!=2\)**, therefore gives precisely (1). As an independent consistency check using the original Alexandrov definition, the two active three-slope vertices have subdifferential triangles of area \(1/2\), and elsewhere the subdifferential has dimension at most one. This proves the support and masses without a dubious distributional product of delta Hessians.

The global uniform bounds follow because only the last affine summand changes by \(c\), and the difference tends to \(c\) along \(x=y\to+\infty\); (3) attains its maximum absolute difference \(|c|\) at \((1,1)\). For the distance formulas, \(\nu_0=\delta_0\), so the only transport coupling from \(\nu_0\) transports each atom directly from the origin. Taking its \(p\)-cost gives (2) and its negative-\(c\) analogue. For \(c>0\), the two supports are disjoint from \(\{0\}\), giving total variation norm \(2\); for \(c<0\), half the limiting atom persists at the origin, giving norm \(1\).

## Classification, correction and scope

**Verified conditional deduction, low severity; no confirmed error in §§21.5–21.6.** The new exact family independently tests the \(n!\) normalization, subgradient/Legendre pushforward, vague/narrow mass stability, and the **invalid strengthening to total variation**. It is compatible with Theorems 21.5.1–2 and Lemma 21.6.2. An optional proposed addition following §21.5.2 or §21.6.2 would clarify this topology boundary with (1)–(3); no production edit is authorized by this audit.

**Affected dependents:** any toric convex/full-mass argument that would infer TV convergence of real MA measures merely from uniform convex potential or conjugate convergence. No listed printed theorem is declared false. No multivariate toric complex MA pullback identity is claimed without its own normalization check.

**Unresolved / not certified:** the general proofs of Theorems 21.5.1–2, Lemma 21.6.2, and their upstream convex compactness or abstract measure statements are not fully re-proven by this exact model. It establishes a test case and a sharp topology obstruction, not an entire-section certificate.

**Deferred-by-user:** all Demailly approximation/regularization and dedicated Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion work remains deferred; no premise or completion was revisited.
