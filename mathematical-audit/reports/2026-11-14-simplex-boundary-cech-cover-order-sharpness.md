# Exact Čech nerve of a simplex boundary: sharp cover-order bound and the acyclic-cover qualifier

Date: 2026-11-14. Finding: **POME-CECH-ORDER-ACYCLICITY-SHARP-001**. Severity: **low**. Classification: **verified conditional deduction** (not a false printed theorem, not a repair). Main examined: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Audit branch is notes-only `review/mathematical-audit`.

## Integrated reading edition, labels, and exact anchors

- `docs/sections/sheaf-cohomology-and-acyclic-resolutions--soft-sheaves-and-paracompact-comparison/index.html`, main blob `c40db93edfa6c8a63b15001ecb40837fa321d6a8`: §10.44, source `demailly-complex-geometry:2FF44C0F`, permanent section `DF8C0003C01A` at physical line 5; **Proposition 10.44.14**, source `demailly-complex-geometry:AE979C9C`, permanent tag `54F5489B5EF9`, lines 199–217 (alternation over the integers, tuples with repeated indices, and support-preserving homotopy); **Corollary 10.44.15**, source `demailly-complex-geometry:634855A9`, permanent `FC813BFC2984`, lines 221–229 (two separate hypotheses for cohomological-dimension vanishing).
- `docs/sections/sheaf-cohomology-and-acyclic-resolutions--sheaves-resolutions-and-cohomology/index.html`, blob `7a67c86dfb218e1846f0735a8f24f57b65f431fd`: **Theorem 10.43.16**, source `demailly-complex-geometry:B5A98C8B`, permanent `678E4157C53F`, lines 295–305 (Čech-to-Godement comparison for acyclic covers). Examined as an identified conditional input, not wholly recertified.
- `docs/sections/spectral-sequences-support-and-cup-products--the-sphere-calculation/index.html`, blob `2a90367f355fa5c9a2b27a0746d388e3877ae503`: **Proposition 10.66.1**, source `demailly-complex-geometry:1FDB87F2`, permanent `91C788EF5865`, lines 8–25 (independent sphere-cohomology statement and Mayer–Vietoris proof, not treated as new).
- `docs/sections/spectral-sequences-support-and-cup-products--local-systems-and-a-singular-comparison-with-supports/index.html`, blob `66ca556aac90cacad01dec69e61943398c888865`: **Theorem 10.70.3**, source `demailly-complex-geometry:223C7EB2`, permanent `9E4C37619D42`, lines 72–96 (constant-sheaf/singular comparison on manifolds, retained as an internal conditional input).

The reviewed §10.44.14–15 assertions are **correct as printed**. This audit checks the exact scope of their cover hypotheses by an explicit finite integral Čech model. It neither reopens nor depends on the user-excluded regularization programme.

## An exact good cover in every dimension

Let $n\ge1$, let $A$ be an arbitrary abelian group, and realize
$
X_n=\partial\Delta^{n+1}
=\left\{t=$t_0,\ldots,t_{n+1}$\in[0,1]^{n+2}:
\sum_i t_i=1,\quad\prod_i t_i=0\right\}\simeq S^n.
$
For each vertex index $i\in\{0,\ldots,n+1\}$, set $U_i=\{t\in X_n:t_i>0\}$. These $n+2$ relatively open sets cover $X_n$. For every nonempty proper index set $I$, the intersection $U_I=\cap_{i\in I}U_i$ is nonempty (it contains the barycenter of the face on $I$) and **contractible**. Indeed, put
$
p_I(t)_i=\begin{cases}t_i/\sum_{j\in I}t_j&i\in I,\\0&i\notin I,\end{cases}
\qquad H(s,t)=(1-s)t+sp_I(t).
$
Every $t\in U_I$ has support containing $I$, and the support of $H(s,t)$ is contained in the original proper support of (t). Thus this continuous homotopy stays in $X_n\cap U_I$, fixes the face interior $\Delta_I^\circ$, and ends there. That face interior is convex. On the other hand, $\bigcap_{i=0}^{n+1}U_i=\varnothing$, since a point of the boundary has at least one zero coordinate. Consequently this is a finite cover of **order exactly $n+1$** (there are nonempty intersections of $n+1$ distinct members, but none of $n+2$).

Each $U_I$ is a contractible open subset of the topological manifold $X_n$, hence the constant sheaf $\underline A$ is acyclic there by the singular/sheaf comparison of §10.70.3 and the elementary singular prism homotopy. Accordingly the **acyclic-cover clause** of §10.43.16 applies. This identification is conditional on that previously stated internal comparison theorem; we do not claim a new complete verification of §10.70.3.

## An integral computation of the entire Čech cochain complex

By the integral alternating homotopy of §10.44.14, it suffices to use increasing index tuples. All proper subsets of the $n+2$ vertices occur as simplices in the nerve, whereas the full vertex set does not. Therefore the alternating Čech complex of this cover with constant coefficients has
$
C^q=\bigoplus_{\substack{I\subset\{0,\ldots,n+1\}\\|I|=q+1}}A\qquad$0\le q\le n$,\qquad C^q=0\ $q>n$,
$
with the usual signed omission coboundary. Every nonempty intersection is connected, so (\underline A$U_I$=A), and all restriction homomorphisms are the identity. This is exactly the simplicial cochain complex of the boundary of the $$n+1$$-simplex, with coefficients in **any** $A$, not merely a field.

For an entirely elementary calculation, adjoin to this boundary cochain complex the single top term $C^{n+1}_{\Delta}=A$ from the full simplex. In all lower degrees the two complexes agree. The full simplex cochain complex has the explicit integral contraction obtained by inserting the vertex $0$ (the usual augmented simplicial cone, with identity in degree zero). Thus its positive-degree cohomology vanishes. In particular, for $n\ge1$,
$
\operatorname{im}$\delta^{n-1}$=\ker$\delta^n_\Delta$,
\qquad
\delta^n_\Delta(c)=\sum_{j=0}^{n+1}(-1)^j c_{\{0,\ldots,n+1\}\setminus\{j\}}.
$
The displayed map is **surjective for every abelian group $A$**, since a cochain supported on the facet omitting vertex $0$, with value $a\in A$, maps to $a$. Thus $\delta^n_\Delta$ induces an integral, coefficient-functorial isomorphism
$
\boxed{H^n(C^\bullet$\mathcal U,\underline A$)\cong A.}
$
The remaining positive degrees below $n$ vanish by the same contraction, and $H^0=A$ because the nerve is connected. In particular a single-facet $n$-cochain of value $a\ne0$ is a nontrivial class; no factorial, positivity, or division hypothesis is involved.

By the stated acyclic-cover comparison this also computes (H^n$S^n,\underline A$\cong A), agreeing with the already printed Proposition 10.66.1 by a **different explicit cover-level calculation**. For every nonzero $A$, the upper-degree vanishing conclusion of Corollary 10.44.15 is optimal: it cannot be strengthened from $q>n$ to $q\ge n$ even for a finite good cover of exact order $n+1$.

## Why one non-acyclic cover cannot replace either hypothesis

On the same $X_n\simeq S^n$, consider instead the single-open-set cover `{X_n}`. It has order $1$, so for $n\ge1$ it satisfies the intersection multiplicity condition of the **hypothetical** $n=0$ version with no acyclicity requirement. Its positive-degree alternating Čech groups are all zero, while (H^n$X_n,\underline A$=A\ne0). It is not acyclic for $\underline A$. Hence the theorem's distinction between **arbitrarily fine** low-order covers and **one acyclic** low-order cover is indispensable. A single low-order cover, without the acyclicity requirement, supplies no global cohomological-dimension bound.

This is a counterexample only to the **unauthorized weakened assertion**, **not to the printed corollary**. In the printed proof, the two routes—direct-limit exhaustion versus acyclic-cover comparison—are properly separated.

## Mathematical classification, impact and further work

**POME-CECH-ORDER-ACYCLICITY-SHARP-001: low / verified conditional deduction.** Hypotheses: $n\ge1$, $A\ne0$ an arbitrary abelian group; finite open-star cover of the simplex boundary; internal singular/sheaf comparison §10.70.3 and acyclic-cover comparison §10.43.16. Complete new ingredient: the explicit intersection deformation retraction and integral facet-sum cochain calculation, with sharpness and a non-acyclic singleton-cover stress test. The topological combinatorics is proved here; its identification with sheaf cohomology relies on the explicitly recorded internal comparison. There is **no confirmed error, no proposed textual repair, and no new external dependency**.

Affected logical dependents: applications of Corollary 10.44.15 estimating $\operatorname{cd}X$ from covering order; uses of Proposition 10.44.14 in integral or torsion coefficients; Čech comparison at Theorem 10.43.16. **Recommendation:** preserve both distinct cover hypotheses and the integral alternating convention; no source/registry/canonical-tag changes are justified. A future broader audit may check the full general singular/sheaf comparison and support versions, but this finding does not certify those chains.

Coverage: targeted mathematical passage §§10.44.14–15 with contextual hypothesis comparison §§10.43.16, 10.66.1 and 10.70.3, all previously partly reviewed. **0 newly first-visited numbered sections; 0 wholly certified sections.** The main reading TOC remains 25 chapters / 747 numbered sections. No builds, browser verification, formalization, CI, or publication performed. User-excluded Demailly approximation/regularization and its dedicated Bergman/L²/OT/multiscale/positivity-loss programme remain **deferred-by-user, not resolved**.
