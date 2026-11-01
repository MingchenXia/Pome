# Boundary dual nonattainment in convex conjugation; a separate local analytic-intersection audit

**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (2026-11-02). **Audit branch:** \`review/mathematical-audit\`. **Scope:** substantive nonexcluded mathematics only. No Demailly approximation/regularization, dedicated Bergman, weighted-L2, Ohsawa–Takegoshi, multiscale patching, or positivity-loss proof was audited.

## POME-CONVEX-BOUNDARY-NONATTAIN-SUM-001

**Severity/status:** low / **verified conditional deduction** (a sharp obstruction to dropping a *printed hypothesis*, **not** a counterexample to any printed theorem, not a proof gap and not a repair).

### Exact integrated anchors

- \`docs/sections/convex-analysis-and-toric-potentials--closed-convex-functions-and-supporting-slopes/index.html\`, blob \`66bfd5b3f6cdfaced77dc1741a995e22768141f1\`: **Proposition 21.2.4**, source \`foundations-of-pluripotential-theory:01EDED5C\`, permanent \`72D7B299EAB8\`, physical lines **94–145**, guarantees subgradients on **relative interior**; **Proposition 21.2.6**, source \`foundations-of-pluripotential-theory:57C22F00\`, permanent \`EAC7AAEC7279\`, lines **159–181**, gives closed-convex recovery from relative-interior values.
- \`docs/sections/convex-analysis-and-toric-potentials--legendre-duality-and-convex-envelopes/index.html\`, blob \`347fa1f0fc35c13b1d1c45193ab997ed456966e4\`: **Theorem 21.3.2**, source \`foundations-of-pluripotential-theory:DD2DB654\`, permanent \`011FA81B0000\`, physical lines **24–58**, biconjugation and subgradient/Fenchel equality; **Proposition 21.3.3(4)**, source \`foundations-of-pluripotential-theory:E93FCB56\`, permanent \`53A9D470F1AC\`, lines **87–93, 132–139**, guarantees an **attained minimum** in the conjugate sum formula when both primal functions are finite everywhere.

### Exact pair and all convexity/closedness hypotheses

Work on the one-dimensional real vector space, with the standard pairing. Define two extended-real functions
$$
F(x)=\begin{cases}0&x\geq0,\\+\infty&x<0,\end{cases}\qquad
G(x)=\begin{cases}-\sqrt{-x}&x\leq0,\\+\infty&x>0.\end{cases}
$$
Both are proper, closed, lower semicontinuous, convex functions. For $G$, convexity on $(-\infty,0)$ follows from $G''(x)=1/[4(-x)^{3/2}]>0$; the value $G(0)=0$ is its left limit, and extension by $+\infty$ outside a closed convex effective domain preserves closed convexity. Their domains intersect only at the boundary point zero, so
$$
(F+G)(x)=\chi_{\{0\}}(x),\qquad (F+G)^*(p)=0
\quad\text{for every }p\in\mathbb R.
$$
The individual conjugates are exactly
$$
F^*(q)=\begin{cases}0&q\leq0,\\+\infty&q>0,\end{cases}
\quad
G^*(r)=\begin{cases}1/(4r)&r>0,\\+\infty&r\leq0.\end{cases}
$$
Indeed, with $t=-x\geq0$,
$$
G^*(r)=\sup_{t\geq0}(\sqrt t-rt).
$$
When $r>0$, writing $s=\sqrt t$ gives the strictly concave quadratic $s-rs^2$, maximized at $s=1/(2r)$, with value $1/(4r)$. For $r\leq0$, this supremum is infinite. The formula for $F^*$ is immediate from its half-line domain.

Fix **any** $p\in\mathbb R$. A decomposition $p=q+r$ gives a finite value $F^*(q)+G^*(r)$ if and only if $q\leq0$, $r>0$, equivalently $r\geq p$, $r>0$ and $q=p-r$. All such values are strictly positive, namely $1/(4r)$, while choosing $r\to+\infty$ gives
$$
\boxed{\quad (F+G)^*(p)=0=
\inf_{q+r=p}\left(F^*(q)+G^*(r)\right),
\quad\text{but the infimum is NEVER attained.}\quad}
$$
Thus even **closed, proper convex** $F$ and $G$ with a **closed, proper convex sum** do **not** suffice to extend the attained-\`min\` conclusion of Proposition 21.3.3(4). Its actual assumption that $F,G$ are finite on the entire vector space must not be silently weakened. The example does **not** show failure of equality with an \`inf\`: here equality of values holds exactly.

The failure is also visible at the subgradient level. For $F$, $\partial F(0)=(-\infty,0]$. For $G$, a supporting slope $r$ at $0$ would require, for all $t>0$,
$$
-\sqrt t=G(-t)\geq G(0)+r(-t)=-rt,
\quad\text{hence }r\geq t^{-1/2}.
$$
No finite $r$ has this property, so $\partial G(0)=\varnothing$, although $G$ is closed and finite at zero. At interior points $x<0$ its unique slope is $1/(2\sqrt{-x})\to+\infty$ as $x\uparrow0$. By contrast $\partial(F+G)(0)=\mathbb R$. Consequently,
$$
\partial F(0)+\partial G(0)=\varnothing
\ne\partial(F+G)(0).
$$
This separately proves the **relative-interior** qualification of Proposition 21.2.4 cannot be removed even for a closed proper function; no general unqualified subdifferential sum rule is justified. It is consistent with the *Fenchel equality* in Theorem 21.3.2, which does not claim attainment at every boundary point.

**Proposal and downstream effect:** add, if useful, this explicit boundary example immediately after Proposition 21.3.3(4), with the nonattainment and empty-subgradient calculations. For any later toric/convex argument using dual infimal decomposition, require the printed whole-space finiteness or another genuine relative-interior constraint qualification before asserting an attained splitter. No currently printed downstream theorem has been shown false. No body, registry, source, tag or canonicalization change is authorized or made in this audit.

## Additional first direct mathematical audit: Theorem 6.9.5, analytic-intersection step only

**Source:** \`docs/sections/lelong-numbers-and-multiplier-ideals--analytic-lelong-level-sets-and-generic-values/index.html\`, blob \`065f6d9e1c1a81950ac83247f6f370c39c3796ef\`; **Theorem 6.9.5 (Siu)**, source \`foundations-of-pluripotential-theory:3559E128\`, permanent \`946909269108\`, physical lines **77–102**; **Equation 6.9.6**, source \`foundations-of-pluripotential-theory:F1EA58B3\`, permanent \`75410ECF073E\`, lines **89–94**. First proof-level check of the **arbitrary analytic intersection ⇒ local finite intersection** argument at **lines 96–98**; not a verification of Lemma 6.9.1, its weighted Hilbert-space premises, coherence via weighted estimates, or the full Siu theorem.

Here is the critical quantifier check, without using the excluded analytic programme. Let $(A_\lambda)$ be analytic subsets and $p$ belong to their intersection. The sum of their local ideal germs at $p$ is finitely generated by Noetherianity, and thus generated by finitely many selected ideals indexed $\lambda_1,\ldots,\lambda_q$. Set $B=\bigcap_{j=1}^q A_{\lambda_j}$. **This alone is not yet a common-neighborhood conclusion**: for each $\lambda$ one only gets $B\subset A_\lambda$ as germs, potentially on a neighborhood depending on $\lambda$. The integrated proof correctly addresses this distinction. By local finiteness of irreducible components, shrink around $p$ so only finitely many components $B_i$ passing through $p$ remain. For each such $B_i$ and every $\lambda$, the analytic subset $A_\lambda\cap(B_i)_{\rm reg}$ contains a nonempty open subset of the connected dense smooth locus, because its germ contains $B_i$ at $p$. The identity theorem implies $(B_i)_{\rm reg}\subset A_\lambda$, and closedness yields $B_i\subset A_\lambda$ **globally on the component**. The same shrunk neighborhood therefore works simultaneously for *all* $\lambda$. This validates that specific nontrivial quantifier passage, conditional on the printed standard results on complex analytic irreducibility and Noetherian local rings. Historical attribution to Siu is preserved.

**Remaining dependency:** the equality of the Lelong level set with the multiplier-ideal order intersection at Equation 6.9.6 depends on Lemma 6.9.1 and its extension/Hilbert-space inputs. Those inputs have **not** been checked here and must **not** be counted as certified; the user-excluded weighted-L2 and extension proof-completion work remains *deferred-by-user*. This subsection's direct review is logically separable from those premises, and it supplies **no independent certification** of Siu analyticity. No original mathematical error was found in the local finite-intersection step.

## Coverage, classification, and verification boundary

**Actually newly checked:** further direct boundary-assumption and exact dual computations in already partly sampled §§21.2.4, 21.3.2–3, plus **first direct, selected proof-step review in §6.9.5 lines 96–98**. Section §6.32 was inspected as a **navigation-only section** (15 physical HTML lines, blob \`6bcbf1598c198379c0540725501fe0da0c9ea12f\`), with no independent theorem; it remains without mathematical proof coverage. No other subsection is upgraded to complete. Current ToC remains **25 chapters, 747 numbered sections, zero entire mathematical sections certified**.

**Audit status:** one new low-severity **verified conditional deduction**, no new confirmed error or applied repair. Older ledger items, genuine open proof gaps, external inputs and historical attributions remain in their previous states. All excluded Demailly approximation/regularization and dedicated Bergman, weighted-L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss items remain **deferred-by-user**, not resolved. No build, test suite, CI, formalization, publishing, source edit or main edit was run or claimed.
