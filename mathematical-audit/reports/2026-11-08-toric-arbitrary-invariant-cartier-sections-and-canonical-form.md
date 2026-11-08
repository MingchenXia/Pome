# All invariant Cartier divisors on a smooth complete toric variety: sections and canonical form

**Finding:** POME-TORIC-INVARIANT-DIVISOR-SECTION-CANONICAL-001  
**Date:** 2026-11-08  
**Classification:** low / **verified conditional deduction** (additional direct algebraic proof; no false printed theorem).  
**Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch only:** review/mathematical-audit.

## Exact integrated targets

- docs/sections/convex-analysis-and-toric-potentials--smooth-lattice-polytopes-and-projective-charts/index.html, blob f442a7b663689b97a9b89689b8b7ae8b366a53fe: Lemma 21.8.2, source foundations-of-pluripotential-theory:86BADE82, permanent 41C54729DBFD, physical line 25 and its proof; Theorem 21.8.3, source foundations-of-pluripotential-theory:0F7315B0, permanent E49F0370E203, lines 108–150 (vertex charts); standing hypotheses line 89.
- docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html, blob 7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c: Proposition 21.9.2, source foundations-of-pluripotential-theory:86CCC496 / permanent 7B4A7CC50CDC, lines 34–61 (orbit boundary and character divisors); Proposition 21.9.3, source foundations-of-pluripotential-theory:43543C56 / permanent C62B8871AA1C, lines 69–102 (chart overlaps); Lemma 21.9.4, source foundations-of-pluripotential-theory:D75B0BB2 / permanent 00432B20A966, lines 112–134 (Laurent expansion); Theorem 21.9.5, source foundations-of-pluripotential-theory:BD98CC5B / permanent 69D3D97E7701, lines 138–166 (ample-polytope section basis and torus-action sign).

The present result is **not** a re-run of the 2026-11-02 polytope-translation/weight-shift finding, the 2026-10-28 facet-order/DH model, or the 2026-11-07 point-blowup jet computation. It treats **arbitrary invariant Cartier divisors, including non-nef and non-effective divisors**, and separately derives the canonical divisor directly from a meromorphic top differential.

## Statement (conditional on the stated integrated chart and Laurent results)

Let \(P\subset M_{\mathbb R}\) be any full-dimensional smooth lattice polytope of dimension \(n\geq 1\); let \(X_P\) be its smooth projective toric variety, \(T=\operatorname{Hom}(M,\mathbb C^*)\), and let \(\rho\) run over the facets of \(P\). Write \(u_\rho\in N\) for the primitive **inward** normal and \(D_\rho\) for the associated torus-invariant prime divisor. For **arbitrary integers** \(a_\rho\), put
\[
 D=\sum_\rho a_\rho D_\rho,\qquad
 P_D=\{m\in M_{\mathbb R}:\langle m,u_\rho\rangle+a_\rho\geq 0\ \text{for every }\rho\}.
\]
Then:

1. \(D\) is Cartier, with explicit local equations on all vertex charts, without imposing effectivity, nefness or ampleness.
2. \(P_D\) is bounded whenever nonempty, and with the natural meromorphic section \(s_D\) having divisor \(D\),
\[
 H^0(X_P,\mathcal O(D))=
 \bigoplus_{m\in P_D\cap M}\mathbb C\,\chi^m s_D,
 \qquad h^0(X_P,\mathcal O(D))=\#(P_D\cap M).
\]
The direct sum is zero when \(P_D\cap M=\varnothing\). Under the natural pullback linearization \((t\cdot f)(x)=f(t^{-1}x)\) on the rational-function model of \(\mathcal O(D)\), the summand indexed by \(m\) has character \(\chi^{-m}\), consistently with the final paragraph of printed Theorem 21.9.5.
3. The invariant meromorphic top form
\[
 \Omega=\frac{d\chi^{e_1}}{\chi^{e_1}}\wedge\cdots\wedge
       \frac{d\chi^{e_n}}{\chi^{e_n}}
\]
(for any basis \(e_1,\ldots,e_n\) of \(M\)) satisfies
\[
 \operatorname{div}(\Omega)=-\sum_\rho D_\rho,\qquad
 K_{X_P}\simeq\mathcal O\Big(-\sum_\rho D_\rho\Big).
\]
Consequently, independently of whether \(-K_{X_P}\) is ample,
\[
 H^0(X_P,-K_{X_P})\cong
 \bigoplus_{\substack{m\in M\\\langle m,u_\rho\rangle\geq -1\;\forall\rho}}
 \mathbb C\,\chi^m s_{-K}.
\]

## Proof

**Cartier charts.** Fix a vertex \(v\). The \(n\) facet normals \(u_{v,1},\ldots,u_{v,n}\) passing through \(v\) are a lattice basis of \(N\), dual to the primitive edge basis \(e_{v,1},\ldots,e_{v,n}\) of \(M\) (Lemma 21.8.2(4)). In the affine chart \(U_v\simeq\mathbb C^n\) of Theorem 21.8.3, the toric boundary components meeting the chart are precisely \(D_{\rho_i}\cap U_v=\{w_i=0\}\), with \(w_i=\chi^{e_{v,i}}\) on \(T\) (Proposition 21.9.2). Set
\[
 p_v=\sum_{i=1}^n a_{\rho_i}e_{v,i}\in M,\qquad
 f_v=\chi^{p_v}=\prod_{i=1}^n w_i^{a_{\rho_i}} .
\]
Negative exponents are allowed: \(f_v\) is a **meromorphic** local defining function. Its divisor on \(U_v\) is exactly \(D|_{U_v}\). On overlaps \(f_v/f_{v'}\) is a nowhere-vanishing holomorphic function because both meromorphic functions have the same Cartier divisor, or directly by Proposition 21.9.3's monomial transitions. Thus the sheaf \(\mathcal O(D)\) has frame \(1/f_v\) on \(U_v\), while its distinguished meromorphic section \(s_D=1\) has coefficient \(f_v\). This proves Cartierness for **all integer coefficient choices**.

**Sections.** A holomorphic section \(s\) restricts on the dense torus to \(s=f\,s_D\), where \(f\) is holomorphic on \(T=(\mathbb C^*)^n\). Lemma 21.9.4 gives a unique normally convergent Laurent series \(f=\sum_{m\in M}c_m\chi^m\). Its expression in the frame \(1/f_v\) is the holomorphic function
\[
 g_v=f f_v=\sum_{m\in M}c_m\chi^{m+p_v}
 =\sum_{m\in M}c_m\prod_iw_i^{\langle m,u_{v,i}\rangle+a_{\rho_i}}.
\]
The transformation \(m\mapsto(\langle m,u_{v,i}\rangle)_i\) is a lattice bijection. By Laurent uniqueness and the final assertion of Lemma 21.9.4, holomorphy of \(g_v\) on \(U_v\simeq\mathbb C^n\) forces \(c_m=0\) unless
\(\langle m,u_{v,i}\rangle+a_{\rho_i}\geq0\) for every \(i\). Every facet contains a vertex; imposing these inequalities at every vertex is therefore **equivalent**, not merely sufficient, to \(m\in P_D\). Conversely, each \(m\in P_D\cap M\) makes \(\chi^m s_D\) holomorphic on every \(U_v\), so the sections span. Distinct characters have distinct Laurent coefficients, proving linear independence.

For finiteness, the recession cone of \(P_D\) is \(\{y:\langle y,u_\rho\rangle\geq0\ \forall\rho\}\). This is also the recession cone of the original bounded polytope \(P\), whose defining inequalities have the **same** facet normals; it is \(\{0\}\). Thus \(P_D\), if nonempty, is bounded, and its lattice-point set is finite. Invariance of \(D\) under \(T\) defines the rational-function linearization. Under it \(s_D=1\) is invariant and \(\chi^m\) transforms by \(\chi^{-m}\), establishing the sign independently of translations.

**Canonical differential.** Let \(e_1,\ldots,e_n\) be any lattice basis. On \(T\), \(\Omega\) is nowhere zero and \(T\)-invariant. At any vertex \(v\), write \((w_i)=\big(\chi^{e_{v,i}}\big)\). The lattice change-of-basis matrix has determinant \(\pm1\), so
\[
 \Omega=\pm\frac{dw_1\wedge\cdots\wedge dw_n}{w_1\cdots w_n}
\quad\text{on }U_v.
\]
The numerator is a nowhere-zero holomorphic top form in the chart and the denominator has one simple zero along **each** boundary hyperplane. Hence the divisor of \(\Omega\) is exactly \(-\sum_\rho D_\rho\) on all charts; it has no additional components on the dense torus. Applying the proved general divisor-section formula with \(a_\rho=1\) gives the formula for sections of \(-K\). No vanishing theorem, Hironaka input, asymptotic section counting, multiplier ideal or excluded regularization is used.

**Integral one-dimensional signed check (including non-nef cases).** For \(X_P=\mathbb P^1\), normals \(u_0=1,\ u_\infty=-1\), an arbitrary integral divisor \(D=a_0D_0+a_\infty D_\infty\) has
\[
 P_D=[-a_0,a_\infty],\qquad h^0(\mathbb P^1,\mathcal O(D))
       =\max\{a_0+a_\infty+1,0\}.
\]
For example \(a_0=-1,a_\infty=3\), despite a negative boundary coefficient, the allowed characters are \(m=1,2,3\), giving three sections. For \(K=-D_0-D_\infty\) the interval is \([1,-1]\) and has no lattice points; for \(-K=D_0+D_\infty\) it is \([-1,1]\) and gives exactly three sections. These tests independently verify the inward-normal inequalities and canonical sign.

## Audit verdict, dependents, and precise scope

Theorems 21.8.3 and 21.9.5 and Propositions 21.9.2–3, Lemma 21.9.4 are **not refuted**. This is a constructive, conditional strengthening of the printed ample-polytope section formula to **every invariant Cartier divisor** on the same smooth complete toric variety, plus a direct nonzero meromorphic volume-form proof of the canonical boundary identity. It may support later divisor/Picard, anticanonical and section-growth discussions, but those downstream arguments are **not** certified here. It does **not** assert an analogous divisor basis for a non-smooth fan without handling its Cartier condition. The integrated chart and Laurent inputs are assumed as printed, not transitive-certified. No full section, chapter, build, test, formalization, canonicalization change or publication is claimed; excluded Demailly approximation and its dedicated Bergman/L2/OT/multiscale/positivity-loss programme are **deferred-by-user**, untouched.
