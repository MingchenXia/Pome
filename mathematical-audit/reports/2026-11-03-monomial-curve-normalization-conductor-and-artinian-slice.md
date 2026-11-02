# Analytic monomial curves: normalization, conductor, and parameter slice (2026-11-03)

**Finding:** \`POME-AN-CURVE-CONDUCTOR-SOCLE-001\` — **low / verified conditional deduction**. This is **not** a false printed theorem or an applied proof repair.  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

## Pinned integrated reading-edition sources

- \`docs/sections/finite-type-algebraic-models-and-analytic-structure-sheaves--analytic-local-models-and-infinitesimal-information/index.html\`, blob \`7a3c24deaab8602c3d2b4be2e31d739f02b5a657\`, **Example 9.60.2**, lines **36–56**, permanent tag \`94F2248906E2\`, original label \`demailly-complex-geometry:74D1BE60\`. Lines 37 and 47–53 identify the analytic local ring and its embedding dimension; lines 38–41 and 55 discuss the special $N=3$ defining ideal.
- Same file, **Proposition 9.60.1**, lines **11–15, 31–32**, permanent tag \`57433F7B0D87\`, source \`demailly-complex-geometry:2090FB67\`: contextual embedding-dimension statement.
- \`docs/sections/finite-type-algebraic-models-and-analytic-structure-sheaves--finite-type-models-and-nilpotent-structure/index.html\`, blob \`96eb7c1f6ee63ce6d222ed3f608a242a0a64b7f0\`, **Proposition 9.58.3**, lines **35–61**, permanent tag \`72F3ADBDFF9A\`, source \`demailly-complex-geometry:5EF3B92E\`: local ring conventions, crosschecked only.

The hypothesis is the **actual printed** analytic local-ring identification for the curve $t\mapsto(t^N,t^{N+1},\ldots,t^{2N-1})$:
\[
R_N=\mathbb C+t^N\mathbb C\{t\}\subset A=\mathbb C\{t\},\qquad N\ge1.
\]
The independent calculations below use only this explicitly stated ring, not the excluded approximation or Bergman/$L^2$/Ohsawa–Takegoshi programme.

## Complete elementary calculations

**1. Integral normalization.** For $N\ge2$ the quotient $t=t^{N+1}/t^N$ belongs to $\operatorname{Frac}(R_N)$. Every $g\in A$ has a convergent residue-class decomposition
\[
g(t)=\sum_{r=0}^{N-1}t^r g_r(t^N),\qquad g_r\in\mathbb C\{x\}.
\]
Here each $g_r(t^N)$ belongs to $R_N$, proving $A\subset\operatorname{Frac}(R_N)$; the reverse inclusion of fields is immediate. The same is trivial for $N=1$. Also $1,t,\ldots,t^{N-1}$ generate $A$ as an $R_N$-module, so $A$ is integral and finite over $R_N$. Since $A$ is an integrally closed discrete valuation ring, any element of the common fraction field integral over $R_N$ is integral over $A$ and hence lies in $A$. Thus
\[
\boxed{\overline{R_N}=A=\mathbb C\{t\}.}
\]

**2. Normalization defect and conductor, including the smooth exception.** The quotient $A/R_N$ has basis $t,\ldots,t^{N-1}$ over $\mathbb C$. Multiplication by the maximal ideal $\mathfrak m_N=t^N A$ of $R_N$ kills this quotient, hence its $R_N$-length (the curve's delta invariant) is
\[
\boxed{\delta(R_N)=\ell_{R_N}(A/R_N)=N-1.}
\]
The conductor is $(R_N:A)=\{f\in A:fA\subset R_N\}$. For $N\ge2$, every $f\in t^NA$ works. If $f$ has a nonzero coefficient of order $1,\ldots,N-1$, then $f\notin R_N$ already; if its constant coefficient is nonzero, $tf$ has a nonzero order-one coefficient and $tf\notin R_N$. Consequently
\[
\boxed{(R_N:A)=
\begin{cases}
A,&N=1,\\
t^N A=\mathfrak m_N,&N\ge2.
\end{cases}}
\]
**The $N=1$ exception matters:** the smooth germ $R_1=A$ has *unit conductor*, not $(t)$. For $N\ge2$, the conductor exponent $N$ and delta invariant $N-1$ are not interchangeable.

**3. Parameter-finite flatness, multiplicity, and the Artinian fiber.** Let $x=t^N$. Sorting terms by their exponents modulo $N$ yields the stronger *free-module* identity
\[
R_N=\mathbb C\{x\}\oplus
\bigoplus_{r=1}^{N-1}t^{N+r}\mathbb C\{x\}.
\]
Thus $R_N$ is finite **free of rank $N$** over the smooth local parameter ring $\mathbb C\{x\}$, and is a one-dimensional Cohen–Macaulay local domain. The non-zero-divisor $x$ is a parameter, and
\[
xR_N=\mathbb C t^N+t^{2N}\mathbb C\{t\},\qquad
R_N/xR_N=\mathbb C\langle 1,t^{N+1},\ldots,t^{2N-1}\rangle.
\]
For $N\ge2$, the images of $t^{N+1},\ldots,t^{2N-1}$ form the maximal ideal of this quotient, and any product of two has order at least $2N+2$ and vanishes modulo $xR_N$. Therefore
\[
\boxed{R_N/(t^N)\simeq
\mathbb C[\epsilon_1,\ldots,\epsilon_{N-1}]
/(\epsilon_i\epsilon_j:\ 1\le i,j\le N-1),\quad N\ge2.}
\]
For $N=1$ the quotient is simply $\mathbb C$. The parameter length and Hilbert–Samuel multiplicity are
\[
\boxed{\ell_{R_N}(R_N/xR_N)=e(R_N)=N.}
\]
For $N\ge2$, the socle of this parameter quotient has dimension $N-1$; for $N=1$ it has dimension $1$. None of these formulas asserts that the **original curve** is nonreduced: $R_N$ embeds in the domain $A$; only its parameter **fiber** has nontrivial square-zero structure for $N\ge2$.

**4. Independent finite sanity check.** An elementary exponent-basis script checked $N=1,\ldots,8$: it returned parameter lengths $1,\ldots,8$, delta dimensions $0,\ldots,7$, and socle dimensions $1,1,2,3,4,5,6,7$. This checks small exponents only and is not a Pome project test, build, or formal verification. The proofs above establish every $N$.

## Verdict, status boundaries, and suggested correction

The inspected original Example **9.60.2 remains correct**; the above is a new, exact, conditional-on-its-printed-ring-formula consequence, **not** a correction of its $N=3$ generators. A **proposed but unapplied** addition after Example 9.60.2 could record the normalization, conductor with its explicit $N=1$ exception, delta invariant, multiplicity, and parameter-fiber algebra. These calculations can be useful for future discussions of normalization, singularity invariants, analytic conductor, and nonreduced scheme-theoretic fibers, but **no dependent theorem has been certified in this session**.

Example 9.60.2's use of Remmert's proper-image theorem for the analytic image is not independently reproved here. Proposition 9.60.1's analytic Nullstellensatz/Cartan coherence inputs are not certified here. No previous unresolved or confirmed status is silently changed; in particular the dedicated Demailly approximation/regularization, Bergman, weighted $L^2$, OT, multiscale atlas, and positivity-loss programme remains **deferred-by-user**.

**Actual coverage:** one additional independent proof/model computation in **already sampled §9.60**, Example 9.60.2; only contextual crosschecks of Proposition 9.60.1 and §9.58.3. No whole numbered section, complete theorem dependency chain, chapter, or collection was certified. No edits to main, sources, proof registry, canonicalization, permanent tags, published site, CI, tests, builds, or formalization.
