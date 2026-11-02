# 2026-11-02 — Exact special-fiber torsion and flatness of circle-invariant polynomial ideals

**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. This is a mathematical audit note, **not** a change to the canonical reading edition or a verification of the whole non-Archimedean chapter. The original statements inspected below remain **correct**. The new result is a precise extension of the elementary invariant-ideal argument, with a nonflat example that prevents an invalid inference from generic product structure to flatness.

## POME-NA-S1-IDEAL-TORSION-FLATNESS-001

**Severity:** low. **Status:** verified conditional deduction (in fact an independently proved algebraic corollary of the displayed hypotheses); no confirmed error in the printed lemma and no repair applied.

**Exact source:** `docs/sections/non-archimedean-pluripotential-theory/index.html`, blob `8448d710690ebe1cc28040f9611d05c9d008a961` on the reviewed main. Lemma **22.1.94**, source label `sgpt:AB6FE74C`, permanent tag `76252E7717AC`, statement **physical lines 1402–1403**, formula **22.1.95** source `sgpt:EC9FB89B`, permanent tag `6126C03E6587`, lines **1404–1406**, and proof lines **1410–1414**. Comparison only: Lemma **22.1.96**, source `sgpt:0D0A3D2C`, permanent tag `AF0C82DE24E9`, lines **1418–1426**.

### Precise conclusion

Let (R) be a commutative Noetherian (mathbb C)-algebra (finite type, as printed in Lemma 22.1.94, is more than necessary). Let (Isubseteq R[t]) be an ideal stable under (t\mapsto \lambda t) for each (lambdain S^1). Define
[
J_q:=\{rin R:r t^qin I\},qquad qge0,
]
and (A=R[t]/I). Then all of the following hold.

1. Each (J_q) is an ideal, (J_0\subseteq J_1\subseteq\cdots), and for some (m) one has (J_q=J_m=:J_\infty) for all (qge m). More precisely,
   [
   I=\bigoplus_{qge0}J_qt^q
   ]
   as a graded (R)-module (the finite-tail notation in 22.1.95 denotes the same ideal).
2. The exact (t)-saturation and (t)-power torsion are
   [
   (I:t^\infty)=J_\infty R[t],qquad
   H^0_{(t)}(A)=\{\bar f\in A:t^N\bar f=0\text{ for some }N\}
        \simeq\frac{J_\infty R[t]}{I}
        =\bigoplus_{qge0}(J_\infty/J_q)t^q.
   ]
   The direct-sum display is as a *graded (R)-module*; multiplication by (t) uses the natural quotient maps (J_\infty/J_q\to J_\infty/J_{q+1}).
3. The special fiber and punctured-family restriction are
   [
   A/tA\simeq R/J_0,qquad
   A[t^{-1}]\simeq (R/J_\infty)[t,t^{-1}].
   ]
   In particular, (operatorname{Spec} A\to\operatorname{Spec}\mathbb C[t]) is a constant family away from (t=0), but it **need not be flat** at the origin.
4. There is an *exact* flatness criterion:
   [
   \boxed{A\text{ is flat over }\mathbb C[t]
        \iff t:A\to A\text{ is injective}
        \iff J_0=J_\infty
        \iff I=J_0R[t].}
   ]
   Thus a flat (S^1)-invariant closed subscheme of the trivial affine family with the circle acting trivially on (operatorname{Spec}R) is itself the pullback of its special fiber. This is a claim specifically for **ideals in the trivial product** with the stated action; it is not a claim about general equivariant test configurations or nontrivial linearisations.

### Complete elementary proof

For (f=\sum_{q=0}^{d}r_qt^q\in I), each (lambda\in S^1) gives (f(\lambda t)\in I). Choose (d+1) distinct elements of the circle. Inverting the complex Vandermonde matrix expresses each homogeneous term (r_qt^q) as a complex linear combination of these translates, so every such term lies in (I). This proves the graded decomposition. Since (tI\subseteq I), the coefficient ideals increase; the ascending chain stops by Noetherianity.

For (f=\sum_q r_qt^q), membership of (t^Nf) in (I) is equivalent, degree by degree, to (r_q\in J_{q+N}) for each (q). If such an (N) exists then (r_q\in J_\infty) for every (q). Conversely, if all coefficients belong to (J_\infty), choose one (N\ge m); then all (r_q\in J_{q+N}) and (t^Nf\in I). This proves the saturation formula. Its quotient by (I) is precisely the (t)-power-torsion submodule of (A), and taking homogeneous pieces gives the stated direct sum.

Reducing modulo (t) leaves the degree-zero ideal (J_0). After inverting (t), every (r\in J_\infty) lies in (IR[t,t^{-1}]), because (rt^m\in I), and the reverse inclusion is clear; hence the Laurent-ring description.

If (A) is flat over (mathbb C[t]), tensoring the injective map (mathbb C[t]\xrightarrow{t}\mathbb C[t]) with (A) shows that multiplication by (t) on (A) is injective. Conversely, (t)-injectivity implies (J_{q+1}\subseteq J_q): if (r\in J_{q+1}), then (t\cdot(rt^q)=0) in (A), hence (rt^q\in I). As the (J_q) are already increasing, all are equal to (J_0), so (I=J_0R[t]). Finally (A\simeq(R/J_0)\otimes_{\mathbb C}\mathbb C[t]), a free (possibly infinite-rank) (mathbb C[t])-module after choosing a (mathbb C)-vector-space basis of (R/J_0). It is therefore flat. This also proves all equivalences without any analytic regularisation or external algebraic-geometry theorem.

### Sharp nonflat model and the algebraisation distinction

Take (R=\mathbb C[z]) and the homogeneous ideal (I=(z^2,tz)\subset\mathbb C[z,t]). Then
[
J_0=(z^2),\quad J_q=(z)\quad(q\ge1),\qquad
H^0_{(t)}(A)=\mathbb Cz\pmod I,\quad tz=0.
]
Every nonzero fiber has coordinate ring (\mathbb C[z]/(z)\simeq\mathbb C), but the central fiber has coordinate ring (\mathbb C[z]/(z^2)); it is a nonreduced double point. The family is not flat because of the nonzero element (z\in A) killed by (t). This supplies an explicit counterexample to the **unprinted** shortcut “the ideal is pulled back on (t\ne0), therefore the extension over (t=0) is flat or a pulled-back ideal.”

Lemma 22.1.96 only asserts **algebraicity** of an analytic ideal whose punctured restriction is pulled back. Its proof invokes **GAGA** on (X\times\mathbb P^1): that is a genuine named external input in the displayed argument unless supplied internally elsewhere, and **is not proved in this audit**. Neither Lemma 22.1.94 nor 22.1.96 asserts flatness, and the example does not contradict either. The affine algebraic model also applies chartwise after algebraisation if the algebraic ideal is circle-invariant, but no extra geometric hypotheses are inferred from Lemma 22.1.96.

### Proposed addition, affected use, and precise coverage

An optional corollary after Lemma 22.1.94 could state the saturation/flatness criterion and the explicit example. It makes the distinction between *punctured product*, *algebraic extension*, and *flat constant family* explicit for later NA degeneration arguments; it does **not** change a proof, a source result, its historical attribution or its stable tags. Potential dependents to check before use: Lemma 22.1.96's algebraisation comparison and later NA (S^1)-equivariant ideal constructions (selected source at 22.1.98); no specific dependent statement has been shown false.

**Actual new inspection:** first direct proof-level examination of the invariant-ideal Vandermonde argument and its Noetherian-tail step in **22.1.94**, plus a precise hypothesis/conclusion crosscheck of **22.1.96**. The larger §22.1 had prior selected audits: this is **not** its first reviewed mathematical section, nor a full proof-chain or section certification. No Demailly approximation/regularisation, Bergman, weighted (L^2), Ohsawa–Takegoshi, multiscale-atlas or positivity-loss programme was examined. No tests, site build, CI or formal verification are claimed.
