# 2026-11-04 — Exact rank and bidegree boundaries of weak-exhaustion semipositive vanishing

**Finding:** \`POME-VANISH-POSRANK-BOUNDARY-SHARP-001\`  
**Severity / status:** **low / verified conditional deduction**. The printed theorem is **not refuted or repaired**; the deduction is an independent sharpness model.  
**Reviewed production \`main\`:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Integrated reading page:** \`docs/sections/hodge-theory-curvature-and-compact-vanishing--semipositive-line-bundle-vanishing-on-weak-exhaustions/index.html\`; exact main blob \`d3dfb60754a1df99aa6c283d0c54d96fa5a5fa01\`.  
**Source and permanent label:** Theorem **10.52.1**, \`demailly-complex-geometry:8601427A\`, permanent tag \`A46DE8D5D789\`, physical HTML lines **7–10**. Context-only curvature scalar bound Equation **10.52.3**, source \`demailly-complex-geometry:E34CD770\`, permanent \`C7EBF8BB029C\`, lines **41–44**. Section permanent tag \`D6A8ACD1845D\`.  
**Actual new coverage:** first direct **geometric countermodel to two unprinted weakenings** of §10.52.1, in previously inventory-only §10.52. The analytic weighted-estimate proof, \`6.27.12\` and \`9.50.3\` are **not reviewed** here. No whole theorem chain or mathematical section is certified.

## Statement and exactly what is being tested

The printed Theorem 10.52.1 assumes a weakly pseudoconvex Kähler complex manifold of dimension \`n\`, and a smooth Hermitian line bundle with semipositive curvature having at least \`n-s+1\` strictly positive eigenvalues **at every point**, for \`1 ≤ s ≤ n\`. It concludes
\[
H^{a,b}_{\bar\partial}(X,L)=0 \quad (a+b\ge n+s).
\]
The present model independently proves that neither (i) replacing \`a+b≥n+s\` by \`a+b≥n+s-1\`, nor (ii) allowing only \`n-s\` strictly positive eigenvalues while keeping the original threshold, is valid in this generality.

## Explicit fixed-manifold family (all dimensions and endpoints)

Let \(E=\mathbb C/(\mathbb Z+\mathrm i\mathbb Z)\) and \(X=E^n\), with its product flat Kähler form \(\omega\). The canonical bundle \(K_X\) is holomorphically trivialized by
\(\Omega=dz_1\wedge\cdots\wedge dz_n\).
Choose a degree-one holomorphic line bundle \(A=\mathcal O_E(p)\). Riemann–Roch on the elliptic curve gives a nonzero holomorphic section \(s\). Equip \(A\) with a smooth metric of strictly positive Chern curvature, which is possible since its degree is positive: adjust an arbitrary curvature representative to a positive constant multiple of the flat area form by solving the mean-zero scalar Poisson equation on \(E\).

For every integer \(0\le r\le n\) set
\[
L_r=\bigotimes_{j=1}^r\operatorname{pr}_j^*A,\qquad L_0=\mathcal O_X,
\]
with the product Hermitian metric. Its curvature is the sum of the positive pullbacks on the first \(r\) factors and zero on the other \(n-r\) factors. Therefore its ordered curvature eigenvalues have **exactly \(r\) strictly positive entries at every point**, and the others vanish. This is an everywhere-semipositive metric, not a varying-rank or pointwise-only construction. Compact \(X\) is connected, Kähler and weakly pseudoconvex (a constant smooth PSH function is a proper exhaustion on a compact space).

Write \(t=n-r\), \(S=\prod_{j=1}^r\operatorname{pr}_j^*s\) (with \(S=1\) if \(r=0\)), and
\[
\gamma_r=S\,\Omega\wedge d\bar z_{r+1}\wedge\cdots\wedge d\bar z_n
\in \mathcal A^{n,t}(X,L_r).
\]
It is smooth and \(\bar\partial_{L_r}\)-closed: \(S\) is holomorphic, \(\Omega\) is holomorphic and the anti-holomorphic coordinate one-forms are closed. It represents a **nonzero** Dolbeault class:
\[
\boxed{H^{n,n-r}_{\bar\partial}(E^n,L_r)\ne0.}
\]

Here is an argument not relying on a Künneth theorem. If \(t=0\), the nonzero \((n,0)\) form cannot be \(\bar\partial\)-exact for degree reasons. If \(t>0\), assume \(\gamma_r=\bar\partial_{L_r}\eta\) with \(\eta\) of type \((n,t-1)\). Choose \(p\in E^r\) with \(S(p)\ne0\). Contract both sides by the \(r\) global holomorphic constant vector fields \(\partial/\partial z_1,\ldots,\partial/\partial z_r\), then restrict to the holomorphic slice \(\{p\}\times E^t\). Holomorphic contraction commutes with \(\bar\partial\) up to the fixed standard graded sign; the restriction of \(L_r\) to this slice is a constant one-dimensional vector space. The alleged exactness would imply that the nonzero constant multiple
\[
S(p)\, dz_{r+1}\wedge\cdots\wedge dz_n\wedge
d\bar z_{r+1}\wedge\cdots\wedge d\bar z_n
\]
is \(\bar\partial\)-exact on \(E^t\). Its integral is nonzero. On \((t,t-1)\) forms the \(\partial\)-term vanishes by degree, so an exact top \(\bar\partial\)-form is \(d\)-exact; Stokes' theorem forces its integral to vanish. Contradiction. For \(r=0\) the same argument applies with no contractions and \(p\) omitted.

## Sharpness of both hypotheses

Fix arbitrary \(n\ge1\) and \(1\le s\le n\).

1. **Degree bound is optimal.** Set \(r=n-s+1\), so \(t=s-1\). The positive-eigenvalue hypothesis of Theorem 10.52.1 is met *with equality*, but
   \[
   H^{n,s-1}_{\bar\partial}(X,L_{n-s+1})\ne0,
   \qquad n+(s-1)=n+s-1.
   \]
   Thus vanishing one total degree earlier is false, including at \(s=1\) and \(s=n\).

2. **Number of strictly positive directions is optimal.** Set \(r=n-s\), so \(t=s\). Now the positive-eigenvalue count misses the printed hypothesis by **exactly one**, and
   \[
   H^{n,s}_{\bar\partial}(X,L_{n-s})\ne0,
   \qquad n+s=n+s.
   \]
   Hence removing one positive direction while retaining the printed degree bound is false. When \(s=n\), this is the trivial bundle and its top Dolbeault class; when \(s=1\), this is an \(n-1\)-positive line bundle and a nonzero \((n,1)\) class.

Both constructions have smooth semipositive curvature of constant rank on a *single fixed manifold* \(E^n\). There is no singular metric, approximation, non-pluripolar mass or limit interchange.

## Mathematical classification, correction and dependents

**Status:** verified conditional deduction, **not** confirmed error, not a proof gap, and not a completed analytic proof of the printed theorem. The proof above requires only the elementary elliptic-curve degree-one section and positive-metric facts (or their standard Riemann–Roch/Poisson proofs), the global torus forms and Stokes. These are unrelated to the excluded Demailly regularization/OT/Bergman programme. The original weighted-\(L^2\) vanishing proof remains **unexamined and uncertified**, so no dependency status is changed.

**Suggested patch (proposed only):** add the two sharply quantified \(E^n\) examples after Theorem 10.52.1; retain its statement, attribution, permanent tags, coefficient conventions and analytic proof unchanged. **Affected dependents:** there is no known false downstream theorem in the integrated reading edition; *any future* extension dropping one eigenvalue or shifting the threshold by one would contradict these explicit classes. No body/source/registry/tag mutation was performed.

**Actual coverage:** one theorem's hypotheses and sharpness model in §10.52; Equation 10.52.3 inspected only to locate the stated algebraic rank mechanism, not its entire proof or its analytic prerequisites. The 25-chapter / 747-numbered-section ToC is unchanged; no mathematical section is certified in full.
