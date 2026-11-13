# Extremal-degree rigidity for projective hyperplane star configurations

**Date:** 2026-11-13  
**Stable finding:** POME-STAR-EXTREMAL-RIGIDITY-001  
**Severity:** low  
**Status:** verified conditional deduction (new strengthening; **not** a false source theorem)  
**Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272

## Exact integrated targets

- docs/sections/projective-vanishing-degree-configurations/index.html, main blob 8c1603d341f3dc45bf5c7124e396e9f1e8eb235c, Theorem **9.69.2**, source label **demailly-complex-geometry:84AEA91E**, permanent tag **FB7CD3CDDE23**, physical lines **7–17** (hypotheses/conclusion) and **19–43** (printed proof), in particular the restriction to a hyperplane (22–30), factor divisibility (24), and multiplicity recursion (32–40).
- docs/sections/entire-function-growth-and-algebraic-zero-sets--refined-bounds-for-simultaneous-vanishing-orders/index.html, blob 8ff4e22eede7fe72ba7bbceeb221ef8b2ed20cf7, Definition **9.56.1**, source **demailly-complex-geometry:4C4F1642**, permanent tag **145E38D5855C**, physical lines **10–20**.

These are current **integrated reading-edition** statements, not inferred from earlier source numbering.

## New statement

Let \(n\ge1\), \(N\ge n\), and let \(H_1,\ldots,H_N\subset\mathbf P^n\) be hyperplanes in exactly the general position of Theorem 9.69.2, with distinct linear equations \(\ell_i\). Let \(S\) be the set of their \(n\)-fold intersections, \(P=\prod_i\ell_i\), and let \(\omega_t(S)\) have the meaning of Definition 9.56.1. Define the **vector space at the minimum degree**
\[
W_t(S)=\{F\in H^0(\mathbf P^n,\mathcal O(\omega_t(S))):
             \operatorname{ord}_pF\ge t\text{ for every }p\in S\}.
\]
The zero form is included in \(W_t(S)\), while \(\omega_t\) is defined using a nonzero form.

**Rigidity:** If \(N>n\), then for every integer \(q\ge1\),
\[
\boxed{W_{qn}(S)=\mathbf C P^q.}
\]
If also \(n\ge2\), then the **complete one-dimensionality criterion** is
\[
\boxed{\dim_{\mathbf C}W_t(S)=1\quad\Longleftrightarrow\quad n\mid t.}
\]

**Sharp boundary:** If \(N=n\), then \(S\) is one point, \(\omega_t(S)=t\), and
\[
\dim_{\mathbf C}W_t(S)=\binom{t+n-1}{n-1}.
\]
For \(n=1\), the minimum-degree form is unique up to scalar for all \(N\ge1,t\ge1\).

## Proof

**(1) Multiples of \(n\).** If \(n=1\), the set \(S\) consists of \(N\) distinct points on \(\mathbf P^1\). Any degree-\(Nt\) homogeneous polynomial vanishing to order at least \(t\) at all these points is divisible by every \(\ell_i^t\), hence is \(cP^t\).

Suppose now \(n\ge2\), \(N>n\) and \(q\ge1\). Exactly \(n\) hyperplanes pass through every point of \(S\), so \(P^q\) vanishes there to order \(qn\) and has degree \(qN\). The printed numerical bound in Theorem 9.69.2 gives
\[
\omega_{qn}(S)\ge \frac{N(qn)}n=qN;
\]
therefore \(\omega_{qn}(S)=qN\).

Take any nonzero \(F\in W_{qn}(S)\). If some \(\ell_i\) did not divide \(F\), its restriction to \(H_i\simeq\mathbf P^{n-1}\) would be a **nonzero** polynomial of degree \(qN\), vanishing to order at least \(qn\) at all \((n-1)\)-fold intersection points of the other \(N-1\) hyperplanes. Apply the **printed** Theorem 9.69.2 in dimension \(n-1\):
\[
qN\ge\frac{(N-1)qn}{n-1}
     =qN+\frac{q(N-n)}{n-1}>qN,
\]
a contradiction. Hence every \(\ell_i\) divides \(F\). As the \(\ell_i\) are pairwise nonassociate prime polynomials, their product \(P\) divides \(F\).

The quotient \(F/P\) has degree \((q-1)N\) and vanishes to order at least \((q-1)n\) at all points of \(S\). By induction on \(q\), with the base \(q=0\) given by constants, \(F/P=cP^{q-1}\), hence \(F=cP^q\). This proves the first boxed equality without appealing to any external interpolation theorem.

**(2) Nonmultiples of \(n\).** Let \(n\ge2\), \(N>n\), and \(t=qn+r\), \(q\ge0\), \(1\le r<n\). The exact initial-degree formula
\[
\omega_t(S)=t+(N-n)\lceil t/n\rceil=qN+(N-n+r)
\]
was **already established in the historical audit** (POME-STAR-SYMBOLIC-EXACT-001); it is supporting input, **not recounted as a new finding**. It also follows from the integrated restriction/divisibility induction: if one \(\ell_i\nmid F\), restrict to \(H_i\) and use
\[
D\ge t+(N-n)\lceil t/(n-1)\rceil
 \ge t+(N-n)\lceil t/n\rceil.
\]
If every \(\ell_i\mid F\), remove \(P\), lowering the degree by \(N\) and the vanishing order by \(n\); when \(t\le n\), simply \(D\ge N\ge t+N-n\). The base case \(n=1\) is root counting, and products of \(P^q\) with \(N-n+r\) distinct \(\ell_i\) attain this bound.

Choose two different subsets \(J,J'\subset\{1,\ldots,N\}\), both of size \(N-n+r\). Such choices exist because \(1\le N-n+r\le N-1\). The forms
\[
F_J=P^q\prod_{j\in J}\ell_j,\qquad
F_{J'}=P^q\prod_{j\in J'}\ell_j
\]
have **minimum degree**, and each vanishes at every point of \(S\) to order at least \(qn+r\): of the \(n\) incident hyperplanes, at least \(r\) belong to \(J\). Unique factorization shows the two forms are not scalar multiples. Consequently \(\dim W_t(S)\ge2\). With part (1), this proves the second boxed equivalence.

**(3) Boundary \(N=n\).** The \(n\) hyperplanes intersect at a single point \(p\). Choose homogeneous coordinates with \(p=[1:0:\cdots:0]\). A homogeneous form of degree \(t\) vanishes at \(p\) to order \(t\) if and only if it is a homogeneous polynomial of degree \(t\) in \(x_1,\ldots,x_n\). The number of monomials is \(\binom{t+n-1}{n-1}\); \(\omega_t=t\). In particular, for \(n\ge2\) this dimension exceeds one for every \(t\ge1\), whereas for \(n=1\) it equals one. This establishes the sharp scope of the rigidity statement.

## Classification and dependency ledger

- **Original theorem:** Theorem 9.69.2 is correct on the inspected hypotheses; the result here is a **strict strengthening**, not an error report or a complete-project certificate.
- **New contribution:** one-dimensionality classification of the entire minimum-degree linear system (not just the numerical minimum \(\omega_t\) or asymptotic \(\Omega\)). In particular the unique extremal form for \(t=qn\) is the \(q\)-th power of the product of all hyperplane equations.
- **External mathematical inputs:** none beyond elementary polynomial UFD arithmetic, vanishing orders and the printed projective restriction argument. No approximation/regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale, or positivity-loss proof programme is used.
- **Potential dependents:** later statements involving symbolic powers and extremal sections of hyperplane arrangements. A short corollary after 9.69.2 is optional; **no correction is required**.
- **Actual scope:** checked source statement/proof 9.69.2 and definition 9.56.1. Section 9.69 was already partially visited; **+0 first numbered-section visits, +0 whole-section certifications**. Main ToC: **25 chapters, 747 numbered sections**. No build, tests, CI, publishing, main/source/registry/canonicalization/tag edits. The user-excluded Demailly programme remains **deferred-by-user**.
