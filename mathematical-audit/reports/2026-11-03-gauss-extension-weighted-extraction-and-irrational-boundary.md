# Gauss extensions: a weighted-divisor proof and the irrational boundary

**Date:** 2026-11-03. **Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Scope:** Non-Archimedean Chapter 22, §22.1.66–69, especially the sentence immediately after equation 22.1.69. **No claim of complete §22.1 review.**

## Exact reading-edition anchors and provenance

- `docs/sections/non-archimedean-pluripotential-theory/index.html`, blob `8448d710690ebe1cc28040f9611d05c9d008a961` on reviewed `main`.
- §22.1.66 **Valuations**: source label `sgpt:435B98BE`, permanent tag `618C84432CDA`, physical lines **1102–1104**.
- Definition **22.1.67**: source `sgpt:5735BD72`, permanent `433FF564E9A3`, physical lines **1108–1125**. Its center convention is used below.
- Definition of *divisorial* as **rational** positive multiples of divisor orders, and the separate mention of real positive multiples: physical lines **1150–1152**.
- Gauss extension **(22.1.69)**: source label `sgpt:8A8BEA89`, permanent `3B8E87503101`, physical lines **1164–1171**; the printed text attributes the divisorial-preservation assertion to **BHJ17, Lemma 4.2**.
- The surrounding Berkovich topology is specified at physical lines **1129–1146**, and is used for the separate limit example below.

The two items below are deliberately distinguished. The first independently proves one **specific cited external mathematical input**, without changing the printed statement or the historical attribution. The second is a **new conditional model observation**, not a counterexample to the printed rational-divisorial assertion.

## Finding POME-NA-GAUSS-DIVISORIAL-REPLACEMENT-001

**Status:** verified repair (self-contained replacement for the particular cited proof step, proposed only). **Severity:** low. **Printed assertion:** correct; **not** a false theorem. **No edit to the reading edition.**

### Claim and exact hypotheses

Let (X) be an irreducible variety over (mathbf C), (E) a prime divisor on a normal birational model (Y\to X), and (v=(p/q)\operatorname{ord}_E), where (p,q>0) are coprime integers. Then on (mathbf C(X)(t)),

[
  sigma(v)\left(\sum_i f_i t^i\right)
  =\min_i\left(\frac p q\operatorname{ord}_E(f_i)+i\right)
  =\frac1q\operatorname{ord}_{F}\left(\sum_i f_i t^i\right)
]

for a prime divisor (F) over (X\times\mathbf A^1). The statement applies to rational functions by taking a quotient of polynomials; nonzero coefficient functions (f_i) may have poles along (E).

### Local birational proof (independent of BHJ17)

At the generic point of (E), its DVR has uniformizer (z) and residue field (k(E)). Work over that generic point with the two transverse coordinates ((z,t)). Choose integers (r,s) with (ps-qr=1). On the two-dimensional algebraic torus perform the unimodular monomial change

[
  z=u^p w^r,\qquad t=u^q w^s.
]

It is birational since the exponent matrix has determinant (1). The model containing the chart (u\in\mathbf A^1, w\in\mathbf G_m), together with the unchanged tangential coordinates on (E), has a divisor (F=\{u=0\}) mapping into (E\times\{0\}). Closure on a birational model defines a prime divisor over (X\times\mathbf A^1). The generic-order valuation satisfies

[
\operatorname{ord}_F(z)=p,\quad
\operatorname{ord}_F(t)=q,\quad
\operatorname{ord}_F(h)=0\quad(h\in k(E)^\times).
]

To verify *the entire Gauss formula*, not just the values on two generators, write (f_i=z^{a_i}h_i) with (a_i=\operatorname{ord}_E(f_i)\in\mathbf Z) and (h_i) an (E)-unit. The initial contribution of (f_i t^i) in the (u)-coordinate is

[
 u^{p a_i+q i} w^{r a_i+s i}\overline{h_i}.
]

Among terms with the minimal (u)-order, the (w)-exponents (r a_i+s i) are **distinct** for distinct (i): equality both of (p a_i+qi) and of (r a_i+si) forces ((a_i,i)) to coincide, since the matrix is unimodular. The nonzero initial terms therefore cannot cancel in (k(E)[w,w^{-1}]). Consequently

[
 \operatorname{ord}_F(\sum_i f_i t^i)=\min_i(pa_i+qi)
]

exactly, and the displayed formula follows. The argument also covers negative (a_i), hence rational coefficients. This is the standard local weighted-divisor extraction; no pluripotential approximation, (L^2) estimates, Ohsawa–Takegoshi, or conjectural input is used. It proves exactly the cited divisoriality clause, not the other statements in BHJ17.

**Suggested correction:** retain the existing BHJ17 attribution but optionally insert the preceding short weighted-extraction proof after equation 22.1.69. It changes neither the assertion nor the chosen convention that *divisorial* requires rational scaling.

**Affected dependencies:** subsequent uses of divisorial Gauss valuations in §22.1, especially circle-invariant ideal / test-configuration arguments; only this elementary valuation fact is independently justified, not their whole analytic or algebraic chains.

## Finding POME-NA-GAUSS-IRRATIONAL-BOUNDARY-001

**Status:** verified conditional deduction. **Severity:** low. **No false printed statement.**

### Explicit sharpness of the rational scaling convention

On (X=\mathbf P^1), let (z) be a coordinate near (0), and set (v_\alpha=\alpha\operatorname{ord}_{z=0}) for (\alpha>0). Its Gauss extension to (mathbf C(z,t)) gives the monomial weight

[
 W_\alpha\left(\sum_{i,j}c_{ij}z^it^j\right)
       =\min_{c_{ij}\ne0}(i\alpha+j)
]

for any nonzero polynomial (and the valuation of a rational quotient is the difference of the corresponding minima). This is a genuine valuation: for positive (\alpha) it is the monomial-weight valuation, or equivalently the local initial-form valuation with multiplicative associated graded ring.

If (\alpha=p/q\in\mathbf Q_{>0}) in lowest terms, the preceding weighted-divisor construction shows (W_\alpha=(1/q)\operatorname{ord}_{F_{p,q}}): the Gauss extension is divisorial in precisely the sense used by §22.1.66.

If (\alpha\notin\mathbf Q), then

[
 W_\alpha(\mathbf C(z,t)^\times)=\mathbf Z\alpha+\mathbf Z,
]

which has rational rank **2**. In contrast, any positive *real multiple* of a prime-divisor order has a cyclic value group of rational rank **1**. Thus (W_\alpha) is **not** even real-scaled divisorial. Its residue field is (mathbf C): among monomials of a nonzero polynomial the least (i\alpha+j) is unique; equality of weights for a rational quotient forces the same initial exponent, so every value-zero residue is constant. In the rational case, (z^q/t^p) has value zero and transcendental residue, giving the contrasting residue-transcendence degree one. These assertions are about the explicit smooth two-variable local model, not arbitrary rank-two valuations.

### A non-closed divisorial locus, checked without compactness

Choose **any** sequence (p_k/q_k\in\mathbf Q_{>0}) converging to an irrational (\alpha>0), and view the valuations (W_{p_k/q_k}) and (W_\alpha) on the affine chart ((z,t)) of (\mathbf P^1\times\mathbf P^1). All are centered at ((0,0)) and have full support. For any fixed nonzero polynomial (P(z,t)), its finitely many weights (i\alpha+j) have a **unique minimum** at the irrational limit. Consequently the same monomial is uniquely minimal for all sufficiently large (k), and (W_{p_k/q_k}(P)\to W_\alpha(P)). Taking differences proves convergence on every nonzero rational function.

The Berkovich topology recalled in lines 1139–1146 is generated by the functions (v\mapsto e^{-v(f)}) on regular-function charts, together with open support conditions. Full-support valuations satisfy the support conditions uniformly, so this explicit pointwise calculation proves

[
 W_{p_k/q_k}\longrightarrow W_\alpha\quad\text{in the Berkovich analytification,}
]

although every term is divisorial and the limit is not. Thus the rationally divisorial locus is not closed, even among valuations centered at one smooth point. **This is an ordinary sequence** and makes no claim about sequential compactness of the full Berkovich space or interchange of unrelated limits.

**Suggested annotation:** when referring to §22.1.69, do not extend its divisorial-preservation claim to all real-scaled divisor orders: irrational scaling already invalidates that strengthening on (\mathbf P^1). The source does not make that invalid strengthening.

**Affected dependencies:** any later approximation or valuation-density argument that distinguishes divisorial valuations from more general quasi-monomial valuations. No envelope, psh metric, BHJ comparison theorem, or continuity theorem is certified by this model.

## Scope and evidence boundaries

Only the printed definition, rational/real scaling distinction, Gauss formula and the specified topology were inspected directly. The proof above replaces the *specific* cited BHJ17 divisoriality step; no claim is made to replace BHJ17 in general. The prior `POME-NA-DIV-POINTWISE-NONUSC-001` concerns **limits of Fubini–Study functions at closed-support semivaluations**, a different result: the present example concerns **limits of valuations themselves** and the rational-rank jump. The previously logged §22.1 Fubini–Study equation-label error, §22.1.88 errors, and other unresolved/deferred items are unchanged. This review did not touch the user-excluded Demailly approximation/regularization, Bergman, weighted (L^2), Ohsawa–Takegoshi, multiscale-atlas or positivity-loss programmes.

No source, main, body, registry, tag, CI, test, build, formalization or website change is implied by this audit report.
