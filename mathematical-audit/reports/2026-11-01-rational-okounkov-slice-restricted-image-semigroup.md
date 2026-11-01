# Rational interior Okounkov slices from actual restricted-image graded series

**Date:** 2026-11-01. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch:** review/mathematical-audit. **Finding:** POME-OKO-RATIONAL-IMAGE-SEMIGROUP-001 — low / **verified conditional deduction** (a complete elementary algebraic-semigroup statement; transcendental transfer NOT verified). **Disposition:** propose a carefully qualified algebraic replacement, NOT a repair applied to the production theorem.

## Exact integrated anchors and provenance

- **Algebraic Okounkov body:** Definition 19.4.8, source \(\mathrm{sgpt}:\mathrm{32C6E06F}\), permanent tag **0114DCC2E021**, at \(\mathrm{docs/sections/the-theory-of-okounkov-bodies--algebraic-partial-okounkov-bodies/index.html}\), main blob **c661e264cab0995a2a344453039940028feff8e0**, lines **112–117**. Its graded valuation semigroup and degree convention appear in Proposition 19.4.7, source **sgpt:32BC1D4A**, permanent **632B1323B741**, lines **58–107**.
- **Multiplicativity and closed-convex-hull convention:** §19.9.5, source **non-kahler-pluripotential-theory:B9A34270**, permanent **E9A3FA804369**, at \(\mathrm{docs/sections/flags-convex-bodies-and-section-growth/index.html}\), blob **83557f0e15275253661fe679c75407e6636d497c**, lines **105–132**, in particular the semigroup statement at **119** and definition at **128**.
- **Printed problematic complete-restriction clause:** Theorem 19.5.4(5), source theorem **sgpt:CE657E18**, permanent **E839B4A35A2A**, fifth clause source **sgpt:F0C64B11**, permanent **111D84FB6B1C**, at \(\mathrm{docs/sections/the-theory-of-okounkov-bodies--transcendental-partial-okounkov-bodies/index.html}\), blob **a53c6b2f80c3775e9d646f57808425823ec4a4ac**, lines **20–52**, especially **44–49**. Its \([DRWNXZ]\) attribution is historical and remains intact.
- Previously established **POME-OKO-SLICE-FALSE-001 (high / confirmed theorem-clause error / unresolved)** and the specific blowup-family **POME-OKO-AMPLE-SLICE-THRESHOLD-001** are *not* registered again. The present result replaces their *model-only* image-series observation by an abstract semigroup theorem with a proof.

## Statement — rational interior slicing of an arbitrary graded valuation semigroup

Let \(X\) be an integral smooth projective variety, \(Y_\bullet=(X\supset Y_1\supset\cdots\supset Y_n)\) a smooth admissible flag with \(Y_1\) an effective Cartier divisor, \(L\) a line bundle, and \(W_\bullet\) a graded subalgebra of \(\bigoplus_{m\ge0}H^0(X,L^m)\) with at least one nonzero positive-degree piece. For a nonzero homogeneous section \(s\), write \(\nu(s)=(\nu_1(s),\ldots,\nu_n(s))\). Set
\[
S=\left\{\nu(s)/m:m\ge1,\ 0\ne s\in W_m\right\},\quad
\Delta=\overline{\operatorname{conv}}(S),\quad
a=\inf_{x\in S}x_1,\quad b=\sup_{x\in S}x_1.
\]
The integrated §19.9 assumptions bound these ratios when its graded-algebra hypotheses hold. Suppose \(a<t<b\) with \(t\in\mathbb Q\). For integers \(m\) divisible by the denominator of \(t\), let
\[
R^{[t]}_m=\operatorname{im}\left(
  \{s\in W_m:\nu_1(s)\ge mt\}
  \xrightarrow{\;s\mapsto (s/s_{Y_1}^{mt})|_{Y_1}\;}
  H^0\!\left(Y_1,(L^m(-mtY_1))|_{Y_1}\right)\right).
\]
Here the expression using \(s_{Y_1}\) means the canonical Cartier-divisor factorization; it is globally defined as a section of \(L^m(-mtY_1)\). The images form a multiplicative graded series over the divisible degrees. Write \(\Delta_{Y_\bullet|Y_1}(R^{[t]}_\bullet)\) for its closed convex hull of residual valuations divided by the *original* degree \(m\). Then
\[
\boxed{\quad
\{y\in\mathbb R^{n-1}:(t,y)\in\Delta\}
   =\Delta_{Y_\bullet|Y_1}(R^{[t]}_\bullet).
\quad}
\]
In fact the set of normalized **individual** section valuation vectors with first coordinate exactly \(t\) is already dense in the left-hand slice. For \(W_m=H^0(X,L^m)\), this is the image of the *global restriction map*, not the full section space on \(Y_1\). No ampleness or projective normality assumption is needed beyond the stated boundedness and nonempty interior first-coordinate interval.

## Complete proof

**(1) The image semigroup is the exact first-order slice.** If \(\nu_1(s)>mt\), division by the Cartier equation produces a section still vanishing along \(Y_1\); its restriction is zero. If \(\nu_1(s)=mt\), the restriction is nonzero and its valuation in the induced \(Y_1\)-flag is exactly \((\nu_2(s),\ldots,\nu_n(s))\). Conversely every nonzero element of the image comes from a section with \(\nu_1(s)=mt\). Because \(X\) is integral and flag valuations are additive under multiplication, images in degrees \(m,k\) multiply to images in degree \(m+k\), and normalized residual valuations are precisely
\[
S_t=\left\{(\nu_2(s),\ldots,\nu_n(s))/m:
     m\ge1,\ \nu_1(s)/m=t,\ 0\ne s\in W_m\right\}.
\]
Thus \(\Delta_{Y_\bullet|Y_1}(R^{[t]}_\bullet)=\overline{\operatorname{conv}} S_t\).

**(2) Fix the first coordinate without losing limit points.** By \(a<t<b\), choose \(x^-,x^+\in S\) with \(x^-_1<t<x^+_1\). For any \(x=(t,y)\in\Delta\), choose \(z_j\in\operatorname{conv} S\) with \(z_j\to x\). If \(z_{j,1}>t\), replace \(z_j\) by \((1-\lambda_j)z_j+\lambda_jx^-\), where \(\lambda_j=(z_{j,1}-t)/(z_{j,1}-x^-_1)\). If \(z_{j,1}<t\), use \(x^+\) with the analogous coefficient. All coefficients are between zero and one for large \(j\) and tend to zero. The adjusted vectors \(z'_j\) remain in \(\operatorname{conv}S\), have first coordinate **exactly** \(t\), and satisfy \(z'_j\to x\). Therefore
\[
\Delta\cap\{x_1=t\}
=\overline{\operatorname{conv}S\cap\{x_1=t\}},
\]
where the convex-hull intersection on the right is taken before closure. This step uses a genuine two-sided interior condition and makes no unjustified boundary-slice claim.

**(3) Rationalize finite convex combinations while retaining the exact slice.** Write an adjusted \(z'\in\operatorname{conv}S\) as \(\sum_{i=1}^r\lambda_i x_i\), \(x_i=\nu(s_i)/m_i\), \(\lambda_i\ge0\), \(\sum_i\lambda_i=1\), \(\sum_i\lambda_i(x_i)_1=t\). All \((x_i)_1\) and \(t\) are rational. The coefficient polytope
\[
P=\{\lambda_i\ge0:\ \sum_i\lambda_i=1,\ \sum_i\lambda_i(x_i)_1=t\}
\]
is a nonempty bounded **rational polytope**, hence its rational points are dense in it (its vertices solve rational systems, and their convex combinations are dense). Approximate \(\lambda\) by \(\lambda^{(q)}\in P\cap\mathbb Q^r\). The resulting weighted averages still have first coordinate exactly \(t\).

**(4) Realize each rational combination by a single product section.** For rational \(\lambda_i^{(q)}\), choose \(M>0\) such that \(k_i=M\lambda_i^{(q)}/m_i\) are all nonnegative integers. Then \(s=\prod_i s_i^{k_i}\in W_M\setminus\{0\}\), since \(X\) is integral and \(W_\bullet\) is a graded algebra. One has \(\sum_i k_im_i=M\), and multiplicativity gives
\[
\frac{\nu(s)}M=\sum_i\lambda_i^{(q)}\frac{\nu(s_i)}{m_i}.
\]
Its first coordinate is exactly \(t\); thus every such rational combination belongs to the single-section slice \(S_t\). Taking first the rational approximation and then the \(j\to\infty\) approximation proves \(\Delta\cap\{x_1=t\}=\overline{S\cap\{x_1=t\}}\). Combining with (1) proves the boxed equality.

**(5) Why the printed full-restriction expression cannot be substituted.** The complete linear series \(H^0(Y_1,(L^m(-mtY_1))|_{Y_1})\) can strictly contain \(R^{[t]}_m\). Discarding the actual image loses vanishing restrictions inherited from the ambient variety. The earlier explicitly computed blowup of \(\mathbb P^2\) demonstrates the strict difference; it is not repeated as a new result here. This proof works for the image graded series for every rational interior \(t\), not just in that model.

## Boundaries, status, dependents, proposed correction

- **Verified scope:** the rational-interior algebraic section-semigroup assertion, with full elementary proof. The argument does not establish a formula at \(t=a\), \(t=b\), or for an irrational \(t\) without separately specifying the limiting series. It does not establish the correspondence between analytic positive-current bodies and these section bodies, nor a general transcendental trace/restriction theorem.
- **Status:** POME-OKO-RATIONAL-IMAGE-SEMIGROUP-001 — **low / verified conditional deduction**. Printed Theorem 19.5.4(5) remains **high / confirmed theorem-clause error / unresolved**; the other clauses are unaffected. This is a valid algebraic replacement, **not** a complete repair of the analytic theorem and **not** an applied production patch.
- **Proposed correction:** insert an optional independently proved algebraic proposition after §19.9.5 or as a note attached to §19.4.8, explicitly using the *image* graded series. For §19.5.4(5), separately qualify the analytic restriction theory and prove any required algebraic–transcendental identification before changing its asserted equality; retain the original \([DRWNXZ]\) historical attribution.
- **Affected dependents:** algebraic Okounkov flags §§19.3–19.4, graded series §19.9, the unresolved analytic slice clause §19.5.4(5), possible restricted-series interpretation of §§19.8 and 20.8. This does **not** certify any of those complete sections or earlier dependencies.
- **Additional direct inventory in this session:** §24.12.1 (Conjecture) and §24.12.2 (Question) at \(\mathrm{docs/sections/questions-on-relative-canonical-classes-and-cotangent-tensors/index.html}\), blob **7b2763d35ab776a5bb0a17a34e8a2e6b3546358f**, lines **8–12**, source **cao-paun-foliations:026DF33E / 54F33ABF**, tags **3E0B91E5DF69 / 2C2AE81C4020**. These are **open questions**, not proven theorems or new proof-level coverage; no conjecture resolved.
- **Audit scope:** selected new algebraic argument and source anchors only. Existing 25 chapters / 747 numbered sections / zero complete mathematical-section certifications remain unchanged. User-deferred Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof-completion are **not examined**, **not resolved**, **not certified**. No build, test, CI, formal proof or site publication performed.