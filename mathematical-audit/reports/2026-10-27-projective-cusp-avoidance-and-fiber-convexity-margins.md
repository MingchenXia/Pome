# Mathematical audit — sharp avoidance dimension for an algebraic non-integrability locus, and exact Finsler fiber margins

**Date:** 2026-10-27 (Asia/Shanghai). **Current \`main\` reviewed:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Starting audit branch HEAD:** \`0dd559673f4d539ff49838a3da3ddc003c96a7a5\`. Scope: specific proof passages in §§9.56, 10.77 and 11.10; **not** entire sections or dependencies. No determination below asserts that a printed theorem is false.

**Excluded without reopening:** Demailly approximation/regularization and the dedicated Bergman, $L^2$, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme, including attempts to complete their prerequisites. Any former notes on those subjects remain **deferred-by-user**, not resolved. In particular **Lemma 9.56.3's extension proof was not audited**. The cubic example below analyzes the elementary *geometry* of Lemma 9.56.2, not any extension machinery.

## POME-PROJ-CUSP-AVOIDANCE-DIM-SHARP-001

**Status:** verified conditional deduction (elementary explicit example, no claim of complete upstream certification). **Severity:** low. **Target:** Lemma 9.56.2, integrated reader \`docs/sections/entire-function-growth-and-algebraic-zero-sets--refined-bounds-for-simultaneous-vanishing-orders/index.html\`, blob \`8ff4e22eede7fe72ba7bbceeb221ef8b2ed20cf7\`, physical lines 27–59 (statement 27–40; dimension/linear-slice proof 42–57). Source book \`demailly-complex-geometry\`, source statement label \`B00A1430\`, permanent tag \`C0DCD035F833\`. Definition 9.56.1 tag \`145E38D5855C\` (lines 11–23) was read for projective/homogeneous conventions.

**Claim:** The projective dimension $n-a-1$ of the avoiding linear subspace in Lemma 9.56.2 cannot be increased in general. For every $n\geq 3$ there is an explicit *single irreducible reduced* cubic divisor and a coefficient $0<r<1$ whose non-integrability locus is exactly a linear $\mathbb P^{n-2}$. Thus an avoiding $\mathbb P^1$ exists, whereas **no** $\mathbb P^2$ avoids the locus.

**Proof.** In homogeneous coordinates $[Z_0:\cdots:Z_n]$ set
\[
P=Z_0Z_1^2-Z_2^3,\qquad r=11/12,\qquad \Delta=r[\{P=0\}].
\]
The polynomial is irreducible: considered as a polynomial of degree one in $Z_0$ over the UFD $\mathbb C[Z_1,\ldots,Z_n]$, its coefficients $Z_1^2$ and $-Z_2^3$ are coprime. It is primitive and irreducible over the fraction field, hence irreducible in the full polynomial ring. Its projective hypersurface is reduced. Its gradient is
\[
(\partial_{Z_0}P,\partial_{Z_1}P,\partial_{Z_2}P,\ldots)
=(Z_1^2,\,2Z_0Z_1,\,-3Z_2^2,\,0,\ldots,0),
\]
so its singular locus is precisely $L=\{Z_1=Z_2=0\}\simeq\mathbb P^{n-2}$. Away from $L$ the reduced divisor is locally a smooth coordinate hypersurface, and $|p|^{-2r}$ is locally integrable because $r<1$. Thus $A\subseteq L$.

At every point of $L\cap\{Z_0\ne0\}$, the local equation is $x^2-y^3$ times a nonvanishing frame factor, independent of the other $n-2$ local coordinates. In the region $0<|y|<\varepsilon$, $|x|<|y|^{3/2}/2$, we have $|x^2-y^3|\leq(5/4)|y|^3$. For every fixed $y$ the $x$-disk has area $\pi|y|^3/4$. By Tonelli, the integral over this region is bounded below by a constant multiple of
\[
\int_0^\varepsilon \rho^{\,4-6r}\,d\rho
=\int_0^\varepsilon \rho^{-3/2}\,d\rho=+\infty.
\]
A smooth projective metric and changing a reduced local equation change the density by bounded positive factors. This proves $L\cap\{Z_0\ne0\}\subseteq A$. Local integrability is an open property in the base point (an integrable neighborhood of a point is also one at all nearby points), so $A$ is closed; the displayed subset is dense in $L$, and hence $L\subseteq A$. Therefore $A=L$ and $a=\dim A=n-2$.

The projective line $Y=\{Z_0=Z_3=\cdots=Z_n=0\}=\mathbb P(\mathrm{span}(e_1,e_2))$ is disjoint from $L$, and the homogeneous polynomial $Q=Z_2$ is not identically zero on it, as permitted by the lemma. Conversely, any projective plane $\mathbb P(V)$, $\dim_{\mathbb C}V=3$, meets $\mathbb P(W)=L$, $\dim_{\mathbb C}W=n-1$, because
\[
\dim(V\cap W)\geq 3+(n-1)-(n+1)=1.
\]
Hence the projective dimension $n-a-1=1$ is sharp in this family. This also makes the codimension-two estimate for the non-integrability locus sharp. No $L^2$ extension or regularization was invoked.

**Disposition:** The statement and selected argument of Lemma 9.56.2 remain correct. Optional post-lemma example making the slicing dimension optimal; retain its source tag and history. **Dependents:** the geometric avoidance premise subsequently used in §9.56 (including §9.56.3, whose analytic proof is **not** audited) and related projective vanishing-order arguments. Nothing here certifies those downstream statements.

## POME-FINS-FIBER-MARGIN-EXACT-001

**Status:** verified conditional deduction (direct exact finite-dimensional convexity computation). **Severity:** low. **Target:** Example 11.10.1, \`docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--homogeneous-convex-regularization/index.html\`, main blob \`318cdba84254005afa50cbf80bb8535a72fbb800\`, physical lines 23–57, especially 43–55. Source book \`non-kahler-pluripotential-theory\`, source label \`3BB3B9F5\`, permanent tag \`196112D1B85A\`.

Let $D=\{|z|<1/2\}$, $t=|z|^2$, and
\[
Q(z,v_1,v_2)=\max\left\{|v_1|^2+|v_2|^2,\;\frac{|v_1|^2}{1-t}+t|v_2|^2\right\}.
\]
For a **fixed fiber** define its sharp global quadratic convexity margin
\[
c_*(z)=\sup\{c\geq0: Q(z,\cdot)-c|\cdot|^2
  \text{ is convex on }\mathbb C^2\simeq\mathbb R^4\}.
\]
Then
\[
\boxed{c_*(z)=|z|^2\text{ for }0<|z|<1/2,\qquad c_*(0)=1.}
\]
Indeed for $0<t<1/4$ and $c\leq t$, both
\[
(1-c)|v|^2,\qquad (1/(1-t)-c)|v_1|^2+(t-c)|v_2|^2
\]
are convex, and so is their maximum. For $c>t$, the second branch is strictly active at $(v_1,v_2)=(1,0)$ because $(1-t)^{-1}>1$. On its small real fiber segment $(1,s)$ the difference $Q-c|v|^2$ has second derivative $2(t-c)<0$, so it is not convex. At $z=0$, $Q(0,v)=|v|^2$ gives $c_*(0)=1$ directly.

**Consequence:** A continuous psh complex-homogeneous squared norm may be strongly convex on every individual fiber, and even have a *larger* margin on one special fiber, while the best fiberwise margin tends to zero nearby. Thus pointwise fiber strong convexity does not supply the uniform neighborhood margin needed by the **separate** Theorem 11.10.4 (source label \`56776404\`, permanent tag \`3FA7CB52F1E5\`, main lines 114–147). This quantitatively sharpens, rather than duplicates or refutes, the printed qualitative Example 11.10.1. **Disposition:** optional formula after the example; no theorem/body/registry edit, and no attempt to complete Demailly's excluded programme. **Dependents:** strictly positive margin hypothesis for projectivized Finsler approximation in §11.10 and uses of that hypothesis downstream.

## Independent nonexcluded §10.77 proof review — no new defect ID

Main HTML \`docs/sections/compact-curves-periods-and-complex-tori--complex-coordinates-and-uniformization-of-surfaces/index.html\`, blob \`204220f127fea276be5d864be3e1db1a9bec1e2a\`, source \`demailly-complex-geometry\`. Selected direct reads: compact genus-zero Lemma 10.77.5 (source \`42A75BDF\`, tag \`6E44892C19CA\`, lines 84–103); topological bordered exhaustion Lemma 10.77.6 (source \`819D086D\`, tag \`A2808AF4FEA1\`, lines 106–140); normalized univalent distortion Lemma 10.77.7 (source \`AF8D9E71\`, tag \`0FE8A815392E\`, lines 142–193); uniformization Theorem 10.77.10 (source \`DF887547\`, tag \`F2BDA05453B5\`, lines 194–213).

Specific checks: for exterior $H(\zeta)=\zeta+\sum_{k\geq1}b_k\zeta^{-k}$ the annular Jacobian integral produces the *positive* $\pi\sum k|b_k|^2(r^{-2k}-R^{-2k})$; its outer disk estimate yields $|b_1|^2\leq 1+2|b_1|$, hence $|a_2|\leq2(1+\sqrt2)<5$ and $\lvert f''/f'\rvert\leq12/(1-|z|^2)$ as printed. The normal-family passage correctly propagates upper bounds using only an **upper** bound on the derivative at the next center; no lower derivative bound is needed for the forward estimate. The compact-genus-zero argument uses precisely an earlier Hodge decomposition input; the final proper-plane-domain step invokes an earlier Riemann mapping result. These dependencies are **conditional here**, not independently recertified. Lemma 10.77.6's full surface-topological construction was read but not formally topologically verified.

**Outcome:** no new confirmed error in these selected steps, no re-registration of the stated estimates as new findings; §10.77 is **selected proof inspection only**, not fully certified.

## Coverage and safety accounting

New direct limited-scope inspections: §9.56.1–2 and §10.77.5–7/.10; incremental explicit sharpness inspection §11.10.1 with §11.10.4 used for dependency matching (prior historical §11.10 checks preserved and not counted as an independent first pass of the whole proof). Three numbered ToC rows receive specified coverage; the repository's 747 numbered ToC inventory is unchanged, **zero sections fully certified**. No original statements, source repositories, canonical proof replacements, permanent tags, published docs, GitHub Actions CI, tests/builds, or website changed. No formal verification claimed.