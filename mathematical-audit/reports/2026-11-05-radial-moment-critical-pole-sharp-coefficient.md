# 2026-11-05 — sharp first-moment pole and cutoff growth at the radial critical exponent

**Finding:** POME-RADIAL-MOMENT-CRITICAL-POLE-COEFF-001.
**Classification:** low / **verified conditional deduction**; the printed proposition is correct, not a false theorem and not a general analytic proof-chain certification.
**Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

## Exact current reading-edition anchors

- Main file: [§15.36 Radial selection for integrable densities](../../docs/sections/equations-with-prescribed-singularities--radial-selection-for-integrable-densities/index.html), main blob **e007da9bd1c2136d289b278ba69a9cf8d4694d9e**. Its integrated **Proposition 15.36.8**, source **non-kahler-pluripotential-theory:013390C6**, permanent tag **704167C1A830**, appears at physical HTML lines **118–137**. The crucial **Equation 15.36.9**, source **non-kahler-pluripotential-theory:13638BD6**, permanent tag **24634670B4B5**, is at **124–127**; its derivation and boundary-term condition are at **140–154**. The scalar-centering proof is at **155–179**.
- Context only: Lemma **15.36.2**, source **non-kahler-pluripotential-theory:D81523C8**, permanent tag **91B8E02B5759**, at physical lines **19–57** of the same HTML; Theorem **15.36.5**, source **non-kahler-pluripotential-theory:C917100A**, permanent tag **AACA90B5B52B**, at **63–113**. The underlying radial density construction is Lemma **15.30.1**, source **non-kahler-pluripotential-theory:4A877CC1**, permanent tag **B30B4EF45772**. These upstream theorems are **not independently certified here**.

## Hypotheses and exact new estimates

Use **precisely** the printed §15.36 model: $Y=\mathbb P^k$ with $k\ge2$, the Fubini–Study probability volume $\kappa^k$, the radial potential $u_\alpha$ and probability density $q_\alpha$ from §15.30, with $0<\alpha<1$. Write
$$
\alpha_c=\frac{k}{k+1},\qquad M_\alpha=\int_Y u_\alpha q_\alpha\,\kappa^k\le0,
$$
and, in the same radial variable $x=1-\psi\ge1$ as the **actual Equation 15.36.9**, put
$$
A_\alpha(x)=\alpha x^{\alpha-1},\qquad
F_\alpha(x)=A_\alpha(x)+(1-A_\alpha(x))e^{1-x},\qquad
Q_\alpha(x)=F_\alpha(x)^k.
$$
For every $0<\alpha<\alpha_c$, the following **uniform additive-error bound** is exact:
$$
\boxed{\quad
\frac{\alpha^{k+1}}{k-(k+1)\alpha}
\ \le\ -M_\alpha\
\le\frac{\alpha^{k+1}}{k-(k+1)\alpha}+k\alpha .
\quad} \tag{A}
$$
Consequently the first-moment divergence is a **simple pole with an explicit residue**:
$$
\boxed{\quad
\lim_{\alpha\uparrow\alpha_c}
(\alpha_c-\alpha)(-M_\alpha)
=\frac{\alpha_c^{k+1}}{k+1}.
\quad} \tag{B}
$$
For the elliptic fivefold example mentioned after Proposition 15.36.8, $k=2$ and $\alpha_c=2/3$, so the precise coefficient in (B) is **$8/81$**. This refines the printed mere finiteness/divergence dichotomy, without strengthening it to a joint parameter-limit statement for the nonlinear equations.

There is also a **physical truncated first-moment** asymptotic, not merely a formal truncation of the integral representation. Let
$$
J_\alpha(R)=\int_{\{1\le x\le R\}}(-u_\alpha)q_\alpha\,\kappa^k,\qquad R>1.
$$
For each fixed $\alpha\ge\alpha_c$ with $\alpha<1$, the exact results are
$$
\boxed{J_{\alpha_c}(R)=\alpha_c^{k+1}\log R+O_k(1)}\tag{C}
$$
and, when $\alpha>\alpha_c$,
$$
\boxed{
J_\alpha(R)\sim
\frac{k(1-\alpha)\alpha^k}{(k+1)\alpha-k}
\,R^{(k+1)\alpha-k}.
}\tag{D}
$$
Thus the transition from finite moment to infinite moment is **logarithmic at equality** and **polynomial beyond equality**, with the leading coefficient determined, including the boundary term omitted if one naively truncates Equation 15.36.9.

## Complete elementary justification

For $x\ge1$ and $0<\alpha<1$ we have $0\le A_\alpha(x)\le\alpha<1$ and
$$
0\le F_\alpha(x)-A_\alpha(x)=(1-A_\alpha(x))e^{1-x}\le e^{1-x},
\qquad
0\le A_\alpha(x)\le F_\alpha(x)\le1.
$$
The map $z\mapsto z^k$ has Lipschitz constant $k$ on $[0,1]$, hence
$$
0\le F_\alpha(x)^k-A_\alpha(x)^k\le k e^{1-x}. \tag{1}
$$
Equation 15.36.9 is the printed, exact radial change-of-variable identity
$$
-M_\alpha
=\alpha\int_1^\infty x^{\alpha-1}F_\alpha(x)^k\,dx
\quad(\alpha<\alpha_c).
$$
Subtract the elementary integral
$$
\alpha\int_1^\infty x^{\alpha-1}A_\alpha(x)^k\,dx
=\alpha^{k+1}\int_1^\infty x^{(k+1)(\alpha-1)}\,dx
=\frac{\alpha^{k+1}}{k-(k+1)\alpha}.
$$
By (1), the nonnegative remainder is at most
$$
k\alpha\int_1^\infty x^{\alpha-1}e^{1-x}\,dx\le k\alpha,
$$
since $x^{\alpha-1}\le1$ for $x\ge1$. This proves (A), with an additive error uniform all the way up to the critical exponent, and (B) follows immediately. At $k=2$, $\alpha_c^{k+1}/(k+1)=(2/3)^3/3=8/81$.

For (C)–(D), note that the radial probability measure has **cumulative mass $Q_\alpha(x)$ outside the $x$-cutoff**: as $x$ increases from $1$ (hyperplane at infinity) toward $+\infty$ (the pole), $Q_\alpha(x)$ decreases from $1$ to $0$. The potential satisfies $-u_\alpha=x^\alpha-1$. Thus the **actual truncated measure** obeys the Stieltjes identity
$$
J_\alpha(R)
=\int_1^R (x^\alpha-1)(-dQ_\alpha(x))
=\alpha\int_1^R x^{\alpha-1}F_\alpha(x)^k\,dx
-(R^\alpha-1)F_\alpha(R)^k . \tag{2}
$$
The contribution of the difference $F_\alpha^k-A_\alpha^k$ in the integral in (2) lies between $0$ and $k\alpha$, **uniformly in $R$ and $\alpha$**. Put $\delta=(k+1)\alpha-k$. The principal integral is exactly
$$
\alpha^{k+1}\frac{R^\delta-1}{\delta}\quad (\delta\ne0),
\qquad\text{or}\qquad \alpha_c^{k+1}\log R\quad(\delta=0).
$$
Since $F_\alpha(R)/A_\alpha(R)\to1$ exponentially fast relative to the power scale, the boundary term satisfies
$$
(R^\alpha-1)F_\alpha(R)^k
=\alpha^k R^\delta(1+o(1)).
$$
When $\delta=0$ it approaches $\alpha_c^k$, proving (C). When $\delta>0$, subtracting the boundary term leaves
$$
J_\alpha(R)
=\left(\frac{\alpha^{k+1}}{\delta}-\alpha^k\right)R^\delta+o(R^\delta)
=\frac{k(1-\alpha)\alpha^k}{\delta}R^\delta+o(R^\delta),
$$
which is (D). All limits in (C) and (D) are **at fixed $\alpha$**. We do not interchange them with $\lambda\downarrow0$ or assert uniformity in $\alpha$ at a moving critical exponent.

## Classification, proposal, and dependent statements

**Status:** verified conditional deduction; **severity:** low. The printed Proposition 15.36.8 is **correct**. The calculations prove a new sharp quantitative consequence of its exact radial representation (not the full representation theorem). The previous finding **POME-RADIAL-MOMENT-SPECTRUM-001** recorded an energy-moment *finiteness spectrum*, and **POME-PRODUCT-TRUNC-SCALAR-LOGRATE-001** concerned **density truncation** on §15.30; neither is being relabeled or repeated as this newly derived sharp boundary coefficient.

**Proposed change only:** after Proposition 15.36.8, optionally add inequalities (A), the critical residue (B), and the cutoff transition (C)–(D) in a separately reviewable mathematical patch. Retain original source attribution, permanent tags, conventions and existing proofs. **Affected dependents:** scalar centering and threshold normalization in §15.36.8; the $k=2$ elliptic fivefold illustration after §15.36.8; convergence-to-the-threshold interpretation in Theorem 15.36.5 and the finite-moment normalization of Corollary 15.36.11. None of those statements is changed by this audit.

**Actual new coverage:** direct computation from §15.36.8–9, physical lines 118–154; §15.36.5 and §15.30.1 only inspected as hypothesis/flux context. This is **not** certification of the entire §15.36, nor of existence, radial reduction, comparison, scalar selection, or the external closed-class uniqueness used by §15.36.11.

**Project scope:** actual current table of contents contains 25 chapters and 747 numbered sections; zero full sections are mathematically certified. Previously confirmed errors, gaps, external inputs, genuine duplicates and prior repairs remain at their original status. All explicitly excluded Demailly approximation/regularization, Bergman, weighted-$L^2$, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programmes remain **deferred-by-user** and were neither reopened nor certified. Only audit notes were written: no main/source/registry/tag changes, build, CI, formal verification or publication.
