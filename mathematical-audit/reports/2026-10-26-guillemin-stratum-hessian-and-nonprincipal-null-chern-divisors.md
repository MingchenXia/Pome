# Mathematical audit — toric boundary Hessians and divisor-class distinction

**Date:** 2026-10-26 (one actual audit session; no intervening continuous work claimed).  
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Audit branch before work:** 08addf9b957793fcd958f87f5e1bafb54e044da3.  
**Scope:** first new selected proof-level read of §21.10.1 and §20.7.3. Context crosschecks §21.8.2–3 and §21.9.2/.5 only. This does not certify entire chapters, nor the external/canonical dependencies used by the integrated proofs.

Both original propositions remain mathematically correct in the passages checked. These are *new deductions and a counterexample to an unprinted converse*, not repairs of false statements. Earlier findings POME-TOR-GUIL-001 (the one-dimensional segment), POME-TOR-CHART-XREF-CYCLE-001 (a forward-reference cycle), and the fixed-point jet finding are preserved unchanged and not counted as new work.

## POME-GUILLEMIN-STRATUM-HESSIAN-001

**Status:** verified conditional deduction; **severity:** low; **suggested placement:** optional corollary following Theorem 21.10.1, without changing source/registry/tags.  
**Integrated source:** \`docs/sections/convex-analysis-and-toric-potentials--the-guillemin-reference-metric/index.html\`, main blob \`4458eef6df84ef46d601d39506017387ed292e08\`; source theorem label \`E94A20D6\`, permanent tag \`B471B994CE64\`, lines 10–19 and proof lines 24–89; especially lines 37–65 (local inverse), 67–73 (smooth potential), 75–87 (Hessian), 89 (transition). Prerequisites: Lemma 21.8.2 label \`86BADE82\`, tag \`41C54729DBFD\`; §21.9.2 label \`86CCC496\`, tag \`7B4A7CC50CDC\`.

**Hypotheses.** Let P be a full-dimensional smooth lattice polytope in M_R. Let v be a vertex with primitive edge basis e_1,...,e_n, and let w=(w_i) be the associated affine chart on X_P. Write t_i=ell_i(m) and
\[
G_0(t)=\sum_{i\in I}t_i\log t_i+g(t)
\]
near a point q in the relative interior of a face Q corresponding to the vanishing coordinates I={i:w_i^0=0}; put J={1,...,n}\setminus I. The smooth g is the sum of the terms of the remaining facets and is defined in a neighborhood of q. For j in J, q satisfies g_j(q)=\log|w_j^0|^2, and q_i=0 for i in I (q_i denotes its t-coordinate). At J empty, q=v. Empty-block determinants/products below mean 1.

**Claim (exact boundary determinant).** In the ordinary complex coordinates w, the Hermitian matrix of second derivatives of the local Guillemin weight H_v at w^0 is block diagonal. Its I block is
\[
\operatorname{diag}_{i\in I}\big(e^{-1-g_i(q)}\big);
\]
its J block is
\[
\left(\frac{(g_{JJ}(q)^{-1})_{jk}}{w_j^0\overline{w_k^0}}\right)_{j,k\in J}.
\]
Therefore
\[
\boxed{\quad
\det\left(\frac{\partial^2H_v}{\partial w_j\partial\bar w_k}(w^0)\right)
=\frac{\prod_{i\in I}e^{-1-g_i(q)}}
       {\big(\prod_{j\in J}|w_j^0|^2\big)\det g_{JJ}(q)} >0.
\quad}
\]
This is a *coordinate determinant* of the local complex Hessian, not a coordinate-free volume density. If one writes the curvature form as (i/2pi) partial-bar-partial H_v, the corresponding top wedge acquires its normalizing factors. The formula includes points on every torus orbit, not just the dense torus and not just vertices.

At the torus-fixed point p_v=(w_1=...=w_n=0), let R_v denote the facets not containing v. Then
\[
\boxed{\quad
\frac{\partial^2H_v}{\partial w_i\partial\bar w_j}(p_v)
=\delta_{ij}\exp\left[-1-
\sum_{\rho\in R_v}(\log\ell_\rho(v)+1)
  \langle e_i,u_\rho\rangle\right].
\quad}
\]
These are explicit strictly positive diagonal entries in the *primitive edge chart*, involving only the facet data of P. They are not intrinsic eigenvalues of a metric independently of that chart.

**Proof.** Theorem 21.10.1 Step 2 uses the map
\[
\Psi(t)=\big((t_i e^{1+g_i(t)})_{i\in I},(g_j(t))_{j\in J}\big).
\]
Its Jacobian at q is block triangular: the I block has entries e^{1+g_i(q)}, its mixed I-to-J block vanishes, and its J block g_{JJ}(q) is positive definite. The inverse-function theorem yields t=t(y_I,x_J) smoothly for y_I near zero, x_j near log|w_j^0|². Step 3 writes H_v as a smooth function h(y_I,x_J), with y_i=|w_i|² and x_j=log|w_j|², and Step 4 computes
\[
h_{y_i}(0,x_J)=e^{-1-g_i(q)},\qquad
(h_{x_jx_k}(0,x_J))_{j,k\in J}=g_{JJ}(q)^{-1}.
\]
At w_i^0=0 for i in I, every term in a mixed or off-diagonal normal second derivative contains a vanishing w_i or its conjugate; the surviving normal entries equal h_{y_i}. The tangential entries are h_{x_jx_k}/(w_j^0\bar w_k^0). Taking determinants proves the first formula because the J block is congruent to g_{JJ}^{-1} under the invertible diagonal matrix diag(1/w_j^0).

If I is the full index set, Q={v}, q=v, J empty. The smooth remainder is
\[
g(t)=\sum_{\rho\not\ni v}\ell_\rho(v+\sum_i t_ie_i)\log\ell_\rho(v+\sum_i t_ie_i).
\]
Differentiating at t=0 gives
\[
g_i(v)=\sum_{\rho\not\ni v}
(\log\ell_\rho(v)+1)\langle e_i,u_\rho\rangle,
\]
yielding the fixed-point formula. No external toric curvature theorem is used beyond the displayed internal local inversion and monomial-chart identities.

**Independent elementary sign/normalization checks:** For P=[0,d], g'(0)=-(log d+1), so the fixed-point Hessian entry is d; this equals the direct derivative at w=0 of H_0=d log(1+|w|²)-d log d (the previously reported one-dimensional example, not counted again). For the standard simplex conv(0,e_1,...,e_n), the fixed-point matrix at v=0 is the identity. These are algebraic checks, not a project test run.

**Dependencies affected:** toric reference-metric positivity and local volume-form computations in §§21.10–21.13. This gives an optional explicit boundary coefficient usable for consistency checks. The original source proves positive definiteness but does not print this all-strata determinant. No claimed repair to the existing chart reference cycle.

## POME-DIVISOR-CHERN-NONPRINCIPAL-001

**Status:** verified conditional deduction (counterexample to a tempting *unprinted* converse); **severity:** low; **suggested placement:** a cautionary example following Proposition 20.7.3.  
**Integrated source:** \`docs/sections/meromorphic-sections-and-divisor-classes/index.html\`, main blob \`d0c40d1e3f6f515eb13169ed1cd3fb447ca161c8\`; original source label \`00A05C89\`, permanent tag \`ACC6D09EDDD9\`, statement lines 12–17 and proof lines 22–27. It asserts the correct normalized Poincare–Lelong current identity, divisor-to-line-bundle map, and kernel equal to principal divisors.

**Claim (sharp logical distinction).** There are integral divisors D on compact complex manifolds with
\[
c_1(\mathcal O(D))=0\in H^2(X,\mathbb Z)
\]
(and hence zero real Chern class) but D is *not principal*. On an elliptic curve E=C/Lambda, choose two distinct points p,q and let D=[p]-[q]. The difference has zero integral Chern class but is not the divisor of any global meromorphic function. The example also applies to E×Y by taking the pullback of D, for any connected compact complex manifold Y.

**Proof.** The translation moving p to q is isotopic to the identity through translations, so the point classes [p] and [q] define the same integral class in H²(E,Z); equivalently both have degree one. Consequently c_1(O(D))=0, by the divisor Chern-class statement of Proposition 20.7.3 (or by the two isotopic point classes). Suppose div(f)=[p]-[q] for a meromorphic function f on E. Lift f to a doubly periodic meromorphic function on C. It has precisely one simple pole modulo Lambda; choose a fundamental parallelogram with the representatives of poles in its interior and none on the boundary. The integrals of f(z) dz on paired opposite edges cancel by periodicity, so the boundary integral is zero. The residue theorem gives instead 2pi i times the nonzero residue at its unique simple pole, a contradiction. A simple pole has nonzero residue by definition. For E×Y, any such principal divisor would restrict on a generic fiber E×{y} to [p]-[q], impossible; choosing y generically avoids a function vanishing or blowing up identically on that fiber, since its divisor is precisely the two horizontal components. Thus no such meromorphic function exists.

**Adjudication.** Proposition 20.7.3 says that *the divisor-to-Pic map* has principal-divisor kernel; it does **not** assert that the kernel of the Chern-class map consists of principal divisors. This example documents that distinction and does not allege any printed mathematical error. Affected dependents: linearly equivalent vs numerically/cohomologically equivalent divisors in §§20.7–20.8, and line-bundle examples elsewhere. We do not assert anything about torsion in Pic^0, the full Picard group, or general singular complex spaces.

## Precisely inspected scope and remaining boundaries

- Directly read and checked the entire integrated Theorem 21.10.1 proof, lines 24–89, including vertex-chart inversion, log cancellation, boundary positivity, and metric transitions. The exact determinant deduction above is strictly local in those coordinates.
- Directly read Proposition 20.7.3's statement and proof, lines 12–28, including the Poincare–Lelong sign with dd^c=(i/2pi)partial-bar-partial, local quotient cancellation, Cartier gluing and principal-divisor kernel. The new elliptic counterexample does not certify all of the upstream local factoriality/noetherian inputs.
- Crosschecked only the needed vertex-chart and character-section identities in §§21.8.2–3 and 21.9.2/.5; no whole-section or source-to-source dependency certification.
- Earlier findings on these nearby topics, including the one-dimensional Guillemin metric, fixed-point jets, toric anticanonical sections, and the chart-reference dependency cycle, remain unchanged and are *not* new findings.
- The complete Demailly approximation/regularization and its special Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, positivity-loss proof-completion program is **deferred-by-user** and has not been reopened, solved or certified. A general historical use of Demailly as a source is not a proof audit of that excluded program.
- No repository build, project tests, CI, formalization, public-site publication, source-body or tag updates were conducted. This report is public mathematical audit prose only and contains no private research source material.
