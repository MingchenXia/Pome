# 2026-11-20 — Convex slope bodies: sharp finite-energy boundary threshold (Chapter 21, §21.4)

**Finding:** POME-TORIC-SLOPE-ENERGY-BOUNDARY-THRESHOLD-001  
**Classification:** low / **verified conditional deduction**, **not** a false printed theorem or a reported proof gap.  
**Main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Reading-edition path:** docs/sections/convex-analysis-and-toric-potentials--slope-bodies-and-bounded-growth/index.html  
**Reading-edition blob:** 56a9a1c19e7234e2aa258d5ad1b66a5679ace190.  
**Permanent tags:** §21.4 root 8CD47210DEE8; Definition 21.4.1 E8746DA689A7 (lines 11–16); Proposition 21.4.2 D6E7C0B06FAD (20–55); Lemma 21.4.3 9AEE54E3B1E1 (63–76); Proposition 21.4.4 374D75E96CF6 (81–96); Example 21.4.5 56EB803309C2 (101); Lemma 21.4.6 F7AECD623994 (109–123). The permanent identifiers are the stable reading-edition locators; an original-source label has not independently been resolved in this run.

## Precise result and proof

Work in $N_{\mathbb R}=M_{\mathbb R}=\mathbb R$, with $P=[-1,1]$ and support function $h_P(x)=|x|$. For each real $q>0$ define the extended-real function
\[
H_q(p)=
\begin{cases}
(1-|p|)^{-q},& |p|<1,\\
+\infty,& |p|\geq 1,
\end{cases}
\qquad F_q=H_q^*.
\]
Then $H_q$ is a proper closed convex function: $p\mapsto |p|$ is convex, $t\mapsto (1-t)^{-q}$ is increasing and convex on $[0,1)$, and the boundary values tend to $+\infty$. Hence $F_q$ is a finite convex function. Indeed $F_q(x)\geq -1$ from $p=0$, while
$F_q(x)\leq |x|-1$ since $|p|<1$ and $H_q(p)\geq1$.
Fenchel–Moreau duality as stated in Theorem 21.3.2 gives
\[
F_q^*=H_q,\qquad
K_{F_q}=\overline{\operatorname{dom}H_q}=[-1,1]=P.
\]
By Proposition 21.4.2, $F_q\in\mathcal P(\mathbb R,P)$; since $P$ has nonempty interior and $K_{F_q}=P$, in fact $F_q\in\mathcal E(\mathbb R,P)$.

For $x\geq0$, the supremum defining $F_q(x)$ never improves by taking $p<0$. Write $p=1-\delta$, $0<\delta\leq1$. Thus
\[
F_q(x)=x-\inf_{0<\delta\leq1}\{x\delta+\delta^{-q}\}.
\]
For $x\geq q$, the unique minimizer is
$\delta=(q/x)^{1/(q+1)}$, and substitution yields the **exact** formula
\[
\boxed{
F_q(x)=x-(q+1)q^{-q/(q+1)}x^{q/(q+1)}
\quad (x\geq q).
}
\]
By symmetry the same formula with $|x|$ holds for $x\leq-q$. Consequently
\[
h_P(x)-F_q(x)
=(q+1)q^{-q/(q+1)}|x|^{q/(q+1)}
\longrightarrow+\infty.
\]
In particular $F_q\notin\mathcal E^\infty(\mathbb R,P)$ for **every** $q>0$, even though the full slope body is $P$ and $F_q$ is globally 1-Lipschitz.

By Definition 21.4.1, the finite-energy criterion is exact:
\[
\int_P F_q^*(p)\,dp
=\int_{-1}^1(1-|p|)^{-q}\,dp
=\begin{cases}2/(1-q),&0<q<1,\\+\infty,&q\geq1.\end{cases}
\]
Therefore
\[
0<q<1:\quad F_q\in\mathcal E^1\setminus\mathcal E^\infty,
\qquad
q\geq1:\quad F_q\in\mathcal E\setminus\mathcal E^1.
\]
Since $h_P$ itself belongs to $\mathcal E^\infty$, **both inclusions** displayed in Proposition 21.4.2 are strict, already in complex/real toric dimension one:
\[
\boxed{
\mathcal E^\infty(\mathbb R,P)
\subsetneq\mathcal E^1(\mathbb R,P)
\subsetneq\mathcal E(\mathbb R,P).
}
\]

A further consequence directly tests Proposition 21.4.4's monotone smooth approximation. Let $F_{q,j}\downarrow F_q$ be **any** pointwise-decreasing sequence of smooth bounded-class convex approximants furnished there. Proposition 21.4.4 gives $F_{q,j}^*\uparrow H_q$ pointwise on $P$. For every $j$ and $p$,
$F_{q,j}^*(p)\geq-F_{q,j}(0)\geq-F_{q,1}(0)$, since $F_{q,j}(0)$ is decreasing. Monotone convergence after adding the common constant $F_{q,1}(0)$ therefore gives
\[
\lim_{j\to\infty}\int_P F_{q,j}^*\,dp
=\int_P H_q\,dp.
\]
In particular, for $q\geq1$ **every such approximating sequence** has its finite (individual) conjugate energies diverge to $+\infty$. Neither decreasing locally uniform convergence nor individual bounded-class membership provides a uniform finite-energy estimate. For $0<q<1$ those energies converge to $2/(1-q)$, even though the limit exits the bounded class. This strengthens the scope distinction between the printed inclusions and the printed approximation theorem, without contradicting either.

## Direct audit of every mathematical item in §21.4

- **Definition 21.4.1 (lines 11–16):** checked the nonempty slope domain and its closure; checked the positive-volume restriction for the full-slope definition of $\mathcal E$ and the zero-volume convention when $P$ has empty interior. The new example uses a full-dimensional $P$.
- **Proposition 21.4.2 (20–55):** checked the three-way equivalence via conjugation/subgradients; normalization at $x=0$, Lipschitz estimate, bounded conjugate characterization, nesting of classes, compact-slope Minkowski addition, and the degenerate-body convention. No invalid equality or missing assumption found. Its infimal-convolution input from Proposition 21.3.3(4) was inspected at the selected proof lines 132–138, not independently certified end-to-end.
- **Lemma 21.4.3 (63–76):** checked that evenness of the **fixed** mollifier yields an even convex radius-profile and hence monotonicity. The statement would not follow for an arbitrary nonsymmetric mollifier; the printed symmetric assumption is present. The smooth-convolution input from §2.5 was not transitively certified.
- **Proposition 21.4.4 (81–96):** checked decreasing max truncations, decreasing convolution radii, global Lipschitz error, local uniform convergence, the legitimate interchange of two suprema when conjugating a decreasing sequence, and pointwise-to-local-uniform convex convergence. The exact conjugate-energy behavior above is new; not a refutation.
- **Example 21.4.5 (101):** confirmed the distinct zero-volume convention and the full-dimensional Minkowski-sum obstruction. It is not the new full-dimensional finite-energy threshold.
- **Lemma 21.4.6 (109–123):** checked the finite-simplex separation argument, $\log\sum e^{t_i}-\max t_i\in[0,\log m]$, and the sign in the monomial quotient. No new error.

**Selected dependencies read:** docs/sections/convex-analysis-and-toric-potentials--legendre-duality-and-convex-envelopes/index.html, blob 347fa1f0fc35c13b1d1c45193ab997ed456966e4, Proposition 21.3.3(4) proof lines 132–138; docs/sections/convex-analysis-and-toric-potentials--closed-convex-functions-and-supporting-slopes/index.html, blob 66bfd5b3f6cdfaced77dc1741a995e22768141f1, Proposition 21.2.6 statement line 159. They are *selected reads only*.

## Disposition and affected dependents

**Severity:** low. **Status:** verified conditional deduction on the printed convex duality results; **no false theorem, no newly diagnosed proof gap**. Recommended **audit-only** addition is the explicit $q=1$ finite-energy boundary, with warnings against inferring uniform conjugate-energy bounds from local uniform convergence. Relevant dependents are the $\mathcal E^\infty\subset\mathcal E^1\subset\mathcal E$ comparison in §21.4.2, the smooth decreasing approximation in §21.4.4, and any later toric energy arguments that conflate full slope body, finite conjugate integral, and bounded slope potential. No dependent theorem is here claimed false.

**Coverage:** §21.4 mathematical lines 7–123 read in full (+1 directly reviewed section; previously unreconciled, not a first-visit claim); two short selected dependency reads (+0 complete upstream proof-chain certifications). No builds, tests, CI, changes to main/source/registry/permanent tags, or website publishing. All Demailly regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programmes remain **deferred-by-user**, not resolved or certified.
