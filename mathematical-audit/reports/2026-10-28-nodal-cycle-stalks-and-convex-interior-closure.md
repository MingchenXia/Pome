# Mathematical audit: nodal analytic-cycle stalks and convex intersection closure

**Date:** 2026-10-28 (Asia/Shanghai).  
**Pinned production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Starting audit branch:** `761432437250660fe278ee086c041a8a0b30600a`.  
**Scope:** selected integrated reading-edition statements and their actual proofs, independently checked without altering any production file. Both findings below are **low / verified conditional deductions**, **not false theorems**; neither is a full-section or upstream-dependency certification.

## POME-CYCLE-NODAL-LOCAL-BRANCH-001

**Severity:** low. **Status:** verified conditional deduction (a concrete sheaf restriction and normalization model, original printed proposition correct).

**Exact locus:** `docs/sections/analytic-cycles-and-cartier-cycles/index.html` in pinned `main`, Git blob `d4817ac64b1365bd967d42cd474fec169f992e28`; Definition **20.6.2** at physical line **8**, and Proposition **20.6.3**, statement at line **13** and proof beginning at lines **16–37**. Proposition source label `demailly-complex-geometry:02B65FA7` (HTML id `demailly-complex-geometry-02B65FA7`), permanent tag **`FD8966432506`**. The proposition claims that the stalk of the sheaf of analytic `q`-cycles is free on irreducible `q`-dimensional **germs**, not on global irreducible components.

**Explicit calculation.** Let
\[
 C=\{(x,y)\in\mathbb C^2:y^2=x^2(1+x)\}
\]
with its reduced analytic structure, and let `p=(0,0)`. It is a globally irreducible one-dimensional complex space. Indeed, the polynomial `y²−x²(1+x)` is irreducible in `\mathbb C[x,y]`: if this monic quadratic in `y` factored, then `1+x` would be a square in `\mathbb C(x)`, which is impossible because its zero at `x=-1` has odd order. One may independently see the global irreducibility through the surjective proper polynomial normalization
\[
 \nu:\mathbb C_t\longrightarrow C,\qquad
 t\longmapsto (t^2-1,\;t(t^2-1)).
\]
For `x\ne0`, `t=y/x`; for `x=0`, necessarily `y=0`, with preimages `t=\pm1`. Properness follows because `|t|\to\infty` forces `|t^2-1|\to\infty`. The connected normal parameter line cannot be covered by two proper analytic inverse images of hypothetical global analytic components.

Locally around `p`, choose the holomorphic square root
\[
 g(x)=\sqrt{1+x},\qquad g(0)=1.
\]
Then
\[
 C\cap U=C_+\cup C_-,\quad
 C_\pm=\{y=\pm xg(x)\}\cap U.
\]
These are **two distinct smooth irreducible analytic germs** meeting only at `p`; their tangent directions `y=\pm x` differ. Consequently, for each `\Lambda\in\{\mathbb Z,\mathbb Q,\mathbb R\}`,
\[
 \mathscr Z_1(C)_p
 \cong \Lambda[C_+]\oplus\Lambda[C_-]
 \cong\Lambda^2,
 \qquad
 \mathscr Z_1(C)(C)=\Lambda[C].
\]
The restriction germ homomorphism sends the **single global generator** to
\[
 [C]\longmapsto[C_+]+[C_-]=(1,1),
\]
not to a single basis vector. This is exactly the component-splitting rule in Proposition 20.6.3. Note that the coefficient of each branch is one; this is not a multiplicity-two branch or a claim that the global cycle is reducible.

**Review disposition and affected dependents.** Proposition 20.6.3 and its existing proof are correct on this model. The distinction matters when reading restriction/gluing in §20.6 and local branches of analytic cycles in §20.5; it also forbids a future canonicalization step that identifies the rank of a cycle sheaf stalk with the number of global irreducible components. An optional explanatory example next to Proposition 20.6.3 would strengthen the reading edition, but is a **proposal only**. No claim is made that all analytic-component existence inputs, the normalization theorem, or the later trace construction have been independently certified. The computation itself is elementary and uses no excluded analytic regularization.

## POME-CONVEX-INTERIOR-ANCHOR-001

**Severity:** low. **Status:** verified conditional deduction (a complete, self-contained strengthening of the **correct** printed lemma, with sharp failure at empty-interior intersection).

**Exact locus:** `docs/sections/almost-semigroups/index.html` on pinned `main`, Git blob `33898b2963ad0f8b7e30bf414276642f60925b74`; Lemma **19.7.11** statement at physical lines **173–178**, proof at **180–183**. Stable source label `sgpt:76F15C30` (HTML id `sgpt-76F15C30`), permanent tag **`127837115DD3`**. Printed hypothesis: a decreasing sequence of bounded convex subsets of `\mathbb R^n` whose intersection has positive `n`-dimensional Lebesgue volume. Printed conclusion: closure commutes with their countable intersection.

**Verified stronger lemma, including arbitrary families.** Let `(D_i)_{i\in I}` be any family of convex subsets of `\mathbb R^n`, without boundedness, directedness, or countability assumptions. Assume that there exist `x_0\in\mathbb R^n` and `r>0` with the **same open ball**
\[
 B(x_0,r)\subseteq\bigcap_{i\in I}D_i.
\]
Then
\[
 \boxed{\ \overline{\bigcap_{i\in I}D_i}
 =\bigcap_{i\in I}\overline{D_i}.\ }
\]
The inclusion left-to-right is automatic. To prove the reverse, fix `y\in\bigcap_i\overline{D_i}` and `t\in(0,1)`. Put `q_t=(1-t)x_0+ty`. For each **independent** index `i`, choose a point `y_i\in D_i` with
\[
 \lVert y_i-y\rVert<\frac{(1-t)r}{t}.
\]
The point
\[
 z_i=x_0+\frac{t}{1-t}(y-y_i)
\]
lies in `B(x_0,r)\subseteq D_i`. By convexity of `D_i`,
\[
 q_t=(1-t)z_i+t y_i\in D_i.
\]
This common `q_t` therefore lies in **every** `D_i`. Letting `t\uparrow1`, `q_t\to y` proves `y\in\overline{\bigcap_i D_i}`. The argument does **not** extract a common subsequence across infinitely many index sets, assert sequential compactness of an arbitrary family, or interchange limit and intersection. It works for any index set because the approximants `y_i` are chosen separately, while `q_t` is exactly the same point for all `i`.

**Deduction of the existing Lemma 19.7.11.** A convex subset of `\mathbb R^n` of positive `n`-dimensional volume has nonempty interior; otherwise its affine span is proper and its volume is zero. Hence the original positive-volume hypothesis supplies a common open ball in the intersection. The stronger lemma gives the original conclusion immediately. In particular, the original lemma does not need the separate assumptions of boundedness, monotonicity, or countability **once a common ball is available**.

**Sharp endpoint counterexample.** Empty interior cannot be allowed without additional conditions, even for bounded decreasing nonempty convex sets with a nonempty common intersection. In `\mathbb R^2` put
\[
 D_j=\{(0,0)\}\cup
 \{(x,y): |x|<1,\ 0<y<1/j\},\qquad j\ge1.
\]
Each `D_j` is bounded and convex (a line segment from the origin to a point in the open strip has positive `y` and `|x|<1` except at its origin); the sets decrease and
\[
 \bigcap_j D_j=\{(0,0)\},
 \quad
 \bigcap_j\overline{D_j}=[-1,1]\times\{0\},
 \quad
 \overline{\bigcap_j D_j}=\{(0,0)\}.
\]
Thus the equality fails if one drops the positive-volume or common-interior condition. The original Lemma 19.7.11 is correct.

**Review disposition and affected dependents.** This proof is a proposed optional replacement/supplement to the current volume-continuity proof, not a production change. It supplies a robust general-family closure rule for possible convex-lattice/Okounkov-body arguments in §19.7, but does not certify any unreviewed semigroup asymptotic theorem, Kaveh–Khovanskii input, or the previously recorded separate §19.7.9 slice-convergence proof gap. Neither theorem nor its proof uses an excluded regularization technique.

## Coverage, duplication checks, and limits

- **§20.6:** incremental direct test of the actual Definition 20.6.2 and Proposition 20.6.3, including local-stalk rank, restriction multiplicities and the printed component-gluing proof. This section already had selected coverage (notably a distinct quadric Weil/Cartier example); the nodal example is **not** a restatement of that older class-group computation.
- **§19.7:** incremental independent closure-lemma proof and endpoint counterexample for Lemma 19.7.11. Earlier work on Lemma 19.7.9 and §19.7.20 remains historically recorded, **not reclassified as newly discovered**. No other §19.7 proof is certified.
- Fresh chapter-directory read confirmed **25 actual current chapter indexes and 747 distinct numbered section links**. None of the 747 sections or any chapter is certified in full.
- **Existing confirmed errors, proof gaps, external dependencies, repairs and deferred-by-user matters are unchanged**; a conditional illustration is not evidence of a false theorem or of a verified whole-section proof. Both findings are low-severity conditional mathematical deductions; the local algebraic calculations and convex proof above are complete.
- All Demailly approximation/regularization and dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work remains **deferred-by-user**, neither inspected nor certified. No source, published body, canonical registry, permanent tag, website, `main`, CI, software tests, build, browser test or formalization was modified or executed. Only audit Markdown on the designated review branch is proposed.
