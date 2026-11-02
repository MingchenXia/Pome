# 2026-11-02 — Exact special-fiber torsion and flatness of circle-invariant polynomial ideals

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. This is a mathematical audit note, not a change to the canonical reading edition or a verification of the whole non-Archimedean chapter. Both printed lemmas inspected below remain correct. The new result extends the elementary invariant-ideal argument, with a nonflat example that rules out a tempting but invalid inference from a generic product structure to flatness.

## POME-NA-S1-IDEAL-TORSION-FLATNESS-001

**Severity:** low. **Status:** verified conditional deduction (the algebraic corollary is proved directly under the source hypotheses). No confirmed error in the printed lemma; no repair applied.

**Exact source:** `docs/sections/non-archimedean-pluripotential-theory/index.html`, blob `8448d710690ebe1cc28040f9611d05c9d008a961` on the reviewed main. Lemma **22.1.94**, source label `sgpt:AB6FE74C`, permanent tag `76252E7717AC`, statement at physical lines **1402–1403**, equation **22.1.95** source `sgpt:EC9FB89B`, permanent tag `6126C03E6587`, physical lines **1404–1406**, and proof at lines **1410–1414**. Hypothesis/conclusion comparison only: Lemma **22.1.96**, source `sgpt:0D0A3D2C`, permanent tag `AF0C82DE24E9`, physical lines **1418–1426**.

### Statement and complete proof

Let \(R\) be any commutative Noetherian \(\mathbb C\)-algebra (the printed finite-type hypothesis is stronger), and \(I\subseteq R[t]\) an ideal invariant under \(t\mapsto\lambda t\) for every \(\lambda\in S^1\), with the \(S^1\)-action trivial on \(R\). Set
\[
J_q:=\{r\in R:r t^q\in I\},\qquad q\ge0,\qquad A:=R[t]/I.
\]
Then \(J_q\) is an ideal, \(J_q\subseteq J_{q+1}\), and this chain stabilizes at \(J_\infty=J_m\) for some \(m\). The precise conclusions are
\[
\boxed{I=\bigoplus_{q\ge0}J_qt^q,\qquad
 (I:t^\infty)=J_\infty R[t],\qquad
 H^0_{(t)}(A)=\bigoplus_{q\ge0}(J_\infty/J_q)t^q.}
\]
Here the direct sums are **graded \(R\)-module** decompositions; the \(t\)-action on the torsion module uses the natural maps \(J_\infty/J_q\to J_\infty/J_{q+1}\). For the fibers,
\[
\boxed{A/tA\simeq R/J_0,\qquad
 A[t^{-1}]\simeq (R/J_\infty)[t,t^{-1}].}
\]
The exact flatness criterion is
\[
\boxed{\ A\text{ is flat over }\mathbb C[t]
 \iff t:A\to A\text{ is injective}
 \iff J_0=J_\infty
 \iff I=J_0R[t].\ }
\]

**Homogeneous splitting.** For any \(f=\sum_{q=0}^d r_qt^q\in I\), choose \(d+1\) distinct numbers \(\lambda_j\in S^1\). Every translate \(f(\lambda_jt)\) belongs to \(I\). The Vandermonde matrix \((\lambda_j^q)_{j,q}\) is invertible over \(\mathbb C\), so each homogeneous term \(r_qt^q\) belongs to \(I\). This proves the direct sum. Since \(tI\subseteq I\), the coefficient ideals increase, and Noetherianity gives stabilization. This proves—and makes precise—the printed Lemma 22.1.94 without any analytic input.

**Saturation and torsion.** A polynomial \(f=\sum_qr_qt^q\) satisfies \(t^Nf\in I\) exactly when \(r_q\in J_{q+N}\) for each coefficient. Hence it belongs to the saturation \((I:t^\infty)\) exactly when all \(r_q\in J_\infty\): the converse follows by choosing \(N\ge m\) for the finitely many coefficients. This proves the saturation formula. Taking its quotient by \(I\) gives the \(t\)-power torsion \(H^0_{(t)}(A)\), including all its graded pieces.

**Fibers.** Modulo \(t\), only the degree-zero ideal \(J_0\) survives. After inverting \(t\), each \(r\in J_\infty\) belongs to the localized ideal because \(rt^m\in I\). Conversely, every homogeneous coefficient of \(I\) lies in \(J_\infty\). This gives the asserted Laurent quotient, so the family is a trivial product off the central fiber, even if the special fiber differs.

**Flatness.** If \(A\) is \(\mathbb C[t]\)-flat, tensoring the injective map \(\mathbb C[t]\xrightarrow{t}\mathbb C[t]\) by \(A\) shows that multiplication by \(t\) on \(A\) is injective. This injectivity implies \(J_{q+1}\subseteq J_q\): if \(r\in J_{q+1}\), then \(t(rt^q)=0\) in \(A\), hence \(rt^q\in I\). The opposite inclusion holds already, so all \(J_q\) coincide and \(I=J_0R[t]\). Conversely, if \(I=J_0R[t]\), then
\[
A=(R/J_0)\otimes_{\mathbb C}\mathbb C[t].
\]
Choosing a \(\mathbb C\)-vector-space basis of \(R/J_0\) exhibits this as a free (possibly infinite-rank) \(\mathbb C[t]\)-module. Thus it is flat. This proves the full equivalence without assuming that the graded ring is finite as a \(\mathbb C[t]\)-module.

### Explicit sharp nonflat family

Take \(R=\mathbb C[z]\) and \(I=(z^2,tz)\subset\mathbb C[z,t]\). The ideal is invariant under all \(t\mapsto\lambda t\), and
\[
J_0=(z^2),\qquad J_q=(z)\ (q\ge1),\qquad
H^0_{(t)}(A)\simeq\mathbb C\cdot\bar z,\quad t\bar z=0.
\]
For each \(t\ne0\), the fiber has coordinate ring \(\mathbb C[z]/(z)\simeq\mathbb C\), a reduced point, whereas the central fiber has ring \(\mathbb C[z]/(z^2)\), a nonreduced double point. Thus the algebraic, circle-invariant extension is a product over the punctured line but is **not flat** at \(0\). This refutes only the **unprinted** implication “punctured product \(\Longrightarrow\) flat or globally pulled-back ideal,” not the printed lemma.

### The algebraisation boundary and mathematical dependencies

Lemma 22.1.96 asserts **algebraicity**, not flatness, of an analytic coherent ideal \(\mathcal I\) on \(X\times\mathbb C\), for projective \(X\), when its restriction to \(X\times\mathbb C^*\) equals \(p^*\mathcal J\). The printed proof glues to \(X\times\mathbb P^1\) and invokes **GAGA**. This GAGA step is a genuine named mathematical input to that proof unless separately discharged by a matching integrated internal proof; **this run did not verify GAGA**. Its conclusion is consistent with the example and does not imply any \(t\)-flatness or homogeneity of arbitrary non-equivariant ideals. We inspected only Lemma 22.1.96's exact hypotheses and conclusion; we did not inspect the subsequent global-generation/L² argument in Lemma 22.1.97.

**Proposed optional addition, not applied:** record the graded saturation, central-fiber torsion and flatness criterion after Lemma 22.1.94, with the example \((z^2,tz)\). It would prevent conflation of a punctured product, algebraisation, equivariant triviality and flat degeneration. **Potential dependents** include the ideal and model-geometric arguments later in §22.1, especially those importing analytic ideals through Lemma 22.1.96, but no specific downstream theorem is hereby proved false. Historical attribution, original source label and permanent tags must remain unchanged.

**Actual new coverage:** first direct proof-level review of Lemma 22.1.94's Vandermonde and Noetherian steps; one hypothesis-level crosscheck of Lemma 22.1.96. The broader §22.1 had already been partly audited, so **no newly first-reviewed numbered section** and **zero whole-section certifications**. The project ToC remains **25 chapters / 747 numbered sections / zero fully mathematically certified sections**. Previous confirmed findings remain unchanged. The entire user-excluded Demailly approximation/regularisation, dedicated Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remains **deferred-by-user** and was not reopened. No project build, tests, CI, formal verification or website publication was performed.
