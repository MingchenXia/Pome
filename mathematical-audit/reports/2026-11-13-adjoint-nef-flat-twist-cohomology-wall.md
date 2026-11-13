# The nef boundary of flat-twist independence for adjoint section envelopes

**Date:** 2026-11-13  
**Stable finding ID:** `POME-ADJOINT-NEF-FLAT-TWIST-COHOMOLOGY-WALL-001`  
**Status:** verified conditional deduction (countermodel to an *unprinted* nef weakening; **not** a false assertion in Pome).  
**Severity:** low for the printed theorem, material scope warning for any proposed nef generalization.  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated reading-edition file:** `docs/sections/flat-twists-of-adjoint-section-envelopes/index.html`, blob `f106e8f79d1a1341045f1e3c41cdeb531b5f699b`.  
**Section:** §19.11, permanent section tag `13F152BD9389`.  
**Theorem 19.11.1:** source `cao-paun-foliations:24E1B42B`, permanent `1D4EB7891AC1`, HTML physical lines 8–13 and proof lines 16–59.  
**Key dependency:** proof lines 23–35, especially lines 29–33 (Nadel vanishing / equality of dimensions for flat twists); equation 19.11.2 source `cao-paun-foliations:91A7CA06`, permanent `354F33395764`, lines 37–40.

## Scope of the check

The printed theorem assumes an **ample** $A$, in addition to projectivity, $K_Z+F$ pseudo-effectivity, semipositive $h_F$, and $\mathcal I(h_F)=\mathcal O_Z$. We do not challenge this theorem. This independent test asks whether the positivity of $A$ can be relaxed to **nef with a smooth semipositive metric**, leaving all other assumptions intact. It cannot. The test isolates the cohomological role of strict positivity in the proof's flat-twist dimension comparison; it does **not** attempt to reproach or complete Nadel, Bergman, $L^2$, or regularization arguments.

## Explicit connected projective countermodel to the nef extension

Let $E$ be a smooth complex elliptic curve and $Z=E\times\mathbb P^1$, with projections $p_1,p_2$. In additive line-bundle notation set

\[
K_Z=p_2^*\mathcal O_{\mathbb P^1}(-2),\quad
F=p_2^*\mathcal O_{\mathbb P^1}(2),\quad
A=p_2^*\mathcal O_{\mathbb P^1}(1),\quad m_0=1.
\]

Consequently $K_Z+F\simeq\mathcal O_Z$ is pseudo-effective and $D=K_Z+F+A=A$. Equip $F$ and $A$ with the pullbacks of smooth positive Fubini–Study metrics. Their curvatures are smooth semipositive on $Z$, and $\mathcal I(h_F)=\mathcal O_Z$. The line bundle $A$ is **nef but not ample**: its degree on every elliptic fiber $E\times\{y\}$ is zero. Thus all the other printed hypotheses hold.

Every $\rho\in\operatorname{Pic}^0(Z)$ has the form $p_1^*\eta$ with $\eta\in\operatorname{Pic}^0(E)$. For each integer $k\ge1$, the Künneth formula and $H^1(\mathbb P^1,\mathcal O(k))=0$ give, for $q=0,1$,

\[
H^q(Z,kD+\rho)\cong H^q(E,\eta)\otimes
H^0(\mathbb P^1,\mathcal O(k)),
\quad H^2(Z,kD+\rho)=0.
\]

For $\eta\ne\mathcal O_E$, a nonzero section of the degree-zero bundle $\eta$ would have an effective zero divisor of degree zero, hence would be nowhere vanishing and trivialize $\eta$, a contradiction. Therefore $h^0(E,\eta)=0$. Riemann–Roch and Serre duality on $E$ give $h^1(E,\eta)=0$. For $\eta=\mathcal O_E$, both cohomology dimensions are one. It follows **exactly** that

\[
(h^0(Z,kD+\rho),h^1(Z,kD+\rho))
=
\begin{cases}
(k+1,k+1),&\rho=\mathcal O_Z,\\
(0,0),&\rho\ne\mathcal O_Z.
\end{cases}
\]

The Euler characteristic is zero for **every** flat twist, but $h^0$ varies maximally. In particular this also holds for nontrivial *torsion* flat twists. The failure is not a normalization artifact.

For any nontrivial flat twist there are no nonzero sections of any $kD+\rho$; the nonnegative section envelope $B_\rho$ is identically zero and $\log B_\rho\equiv-\infty$. For the trivial twist, $p_2^*\mathcal O(1)$ is globally generated. At each $x\in Z$ choose a section nonzero at $x$ and scale it to make the root integral in the definition of $B_0$ equal to one (the relevant metrics are smooth and the integral is finite and positive). Hence $B_0(x)>0$ **for every $x$**. The standard local submean inequality for $|f|^{2/k}$ in a trivialization, with fixed smooth weights and volume, also bounds the normalized envelopes locally above uniformly in $k$; so the regularized $\log B_0$ is finite. The two regularized envelopes are unequal.

This explicitly disproves the statement obtained by replacing **ample $A$** in Theorem 19.11.1 with **arbitrary nef $A$**. It does **not** disprove Theorem 19.11.1 as printed.

## Exact positivity-wall calculation

Let $M$ be a degree-one ample bundle on $E$, choose positive integers $a,b$, and consider the rational class

\[
D_{a/b}=p_2^*\mathcal O(1)+(a/b)p_1^*M.
\]

With $m_0=b$ and $A_{a,b}=p_2^*\mathcal O(b)+a p_1^*M$ we have $D_{a/b}=K_Z+F+A_{a,b}/m_0$, and **$A_{a,b}$ is ample**. For $k$ divisible by $b$, $kD_{a/b}+\rho$ is a genuine line bundle and Künneth together with elliptic Riemann–Roch (positive degree, vanishing $H^1$) yields

\[
h^0(Z,kD_{a/b}+p_1^*\eta)
=(k+1)\,\frac{ka}{b}
\quad\text{for every }\eta\in\operatorname{Pic}^0(E).
\]

Thus any positive rational elliptic-direction coefficient removes the **section-space obstruction** and gives quadratic section growth, uniformly over flat twists. At coefficient zero, $h^0$ is $k+1$ for the identity twist and zero for all other twists. This is a sharp cohomological positivity wall; it is **not** an independent proof of the printed theorem's equality of normalized extremal envelopes for $a/b>0$.

## Mathematical classification and dependency implications

- **Finding:** `POME-ADJOINT-NEF-FLAT-TWIST-COHOMOLOGY-WALL-001`: **low / verified conditional deduction**, entirely outside the user-excluded regularization programme. The counterexample is complete and uses only elementary line bundles, Künneth, elliptic Riemann–Roch and holomorphic submean bounds.
- **Printed theorem:** Theorem 19.11.1 is **not refuted and not certified** by this check. Its Nadel vanishing and analytic proof chain at lines 23–58 remains a conditional input, with the user-excluded dedicated $L^2$/regularization proof-completion scope left **deferred-by-user**.
- **Why the step matters:** Under this nef weakening, $H^1$ for the identity twist is nonzero, while $h^0$ for nontrivial twists vanishes, so the flat-twist $h^0$ equality used in the printed proof at lines 29–33 cannot be obtained from equal Euler characteristics alone.
- **Proposed action (no production edit):** Retain the **ample** assumption. If an extension is proposed, demand a substitute for vanishing and an explicit uniform nonemptiness argument in every flat direction; mere nefness or smooth semipositivity is insufficient.
- **Affected dependents:** Any proposed nef extension of §19.11.1 or any downstream assertion of flat-twist independence that drops the strictly positive perturbation. No existing printed dependent has been shown false.

## Coverage and exclusions

This is a new algebraic/analytic *scope test* for a previously partially inspected §19.11. It does **not** certify all of §19.11, does not audit the full Nadel / $L^2$ chain, and counts **zero newly first-visited numbered sections and zero entirely certified sections**. Current main ToC: **25 chapters, 747 numbered sections**, independently recounted from `docs/chapters/index.html`. No tests, builds, browser checks, CI, website publication, source/registry/tag or production-main changes were made.
