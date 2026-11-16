# Fixed-data large-parameter asymptotics for the smooth Hermitian exponential Monge–Ampère equation

**Date:** 2026-11-17. **Finding ID:** \`POME-SMOOTH-EXP-LARGE-LAMBDA-RESOLVENT-001\`.  
**Severity:** low. **Status:** **verified conditional deduction** (not a false printed theorem and not an independent proof of global smooth existence).  
**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Integrated reading-edition file:** \`docs/sections/smooth-monge-ampere-equations--the-smooth-exponential-equation/index.html\`, blob \`1de4acc3150f79f4275f8aa507d2c044edb32d8f\`.  
**Source labels / permanent tags:** Proposition 14.7.1 = \`non-kahler-pluripotential-theory:CF8EC5AE\` / \`C52E44D9C563\`; Theorem 14.7.2 = \`non-kahler-pluripotential-theory:793E5FA5\` / \`97F5C96646CC\`. Section tag \`A4D09B787D84\`.  
**Direct physical-line anchors in the integrated HTML:** comparison statement 10–15 and proof 18–22; smooth existence, uniqueness and extremal bounds 26–40; continuation, invertibility and elliptic-estimate dependencies 42–51. The obstacle-scaling discussion 54–61 is **context only and explicitly outside the scope** of the fixed-data result.

## Statement and scope

Let \(X\) be a compact complex \(n\)-fold, let \(\omega\) be a smooth positive Hermitian \((1,1)\)-form, and let \(F\in C^\infty(X,\mathbb R)\) be **fixed independently of** \(\lambda>0\). Let \(u_\lambda\) be the unique smooth admissible solution furnished by printed Theorem 14.7.2:
\[
\log\frac{(\omega+dd^c u_\lambda)^n}{\omega^n}=\lambda u_\lambda+F,\qquad \omega+dd^c u_\lambda>0.
\tag{1}
\]
Use Pome's \(dd^c=\frac{i}{2\pi}\partial\bar\partial\) and write
\(L_\omega f=\operatorname{tr}_\omega dd^c f\),
\(A_f=\omega^{-1}dd^c f\).
Then, as \(\lambda\to+\infty\),
\[
\boxed{\displaystyle
u_\lambda=-\frac F\lambda-\frac{L_\omega F}{\lambda^2}
-\frac{L_\omega^2 F+\frac12\operatorname{tr}(A_F^2)}{\lambda^3}
+O_{C^0}(\lambda^{-4}).}
\tag{2}
\]
More generally, there are canonically recursively defined smooth functions \(a_j\), depending only on \(F,\omega\), such that for every integer \(N\ge1\),
\[
\left\|u_\lambda-\sum_{j=1}^{N}\lambda^{-j}a_j\right\|_{C^0(X)}
\le C_N\lambda^{-(N+1)}
\quad (\lambda\ge\lambda_N).
\tag{3}
\]
This is a **uniform asymptotic expansion on the original parameter**, with no subsequence extraction. It does **not** claim \(C^k\) remainder estimates; each comparison barrier is smooth, but the estimate is in \(C^0\). It uses no Demailly approximation, Bergman kernels, \(L^2\) extension, multiscale atlas or positivity-loss procedure.

The comparison also yields, for smooth fixed \(F,G\) and the **same** \(\lambda>0\),
\[
-\frac{\sup_X(G-F)}{\lambda}
\le u_\lambda(G)-u_\lambda(F)
\le-\frac{\inf_X(G-F)}{\lambda}.
\tag{4}
\]
On connected \(X\), if \(G-F\) is nonconstant, both pointwise inequalities are strict. For a constant perturbation \(G=F+c\), equality is attained: \(u_\lambda(F+c)=u_\lambda(F)-c/\lambda\), so the coefficient \(1/\lambda\) is sharp.

## Direct proof: comparison and order reversal

The printed Proposition 14.7.1, whose entire statement/proof is at the lines above, applies to the *same* density \(F\). A constant translate \(u_\lambda(F)+c\) leaves the Hermitian form unchanged and changes the right-hand logarithm by \(\lambda c\). With
\(m=\inf_X(G-F)\), \(M=\sup_X(G-F)\), the functions
\(u_\lambda(F)-M/\lambda\) and \(u_\lambda(F)-m/\lambda\) are respectively a subsolution and a supersolution for the data \(G\). The printed comparison gives (4), without any differentiability of the solution operator in the data.

For the strict assertion on a connected manifold set \(w=u_\lambda(G)-u_\lambda(F)\). Every interpolated form
\(\omega_{u_\lambda(F)+tw}=(1-t)\omega_{u_\lambda(F)}+t\omega_{u_\lambda(G)}\) is positive, so
\[
(B-\lambda)w=G-F,\qquad
B\phi=\int_0^1\operatorname{tr}_{\omega_{u_\lambda(F)+tw}}dd^c\phi\,dt.
\]
The operator \(B\) is smooth, uniformly elliptic, and has no zero-order term. The nonnegative-source comparison applied to
\(w+m/\lambda\) (whose image under \(B-\lambda\) equals \(G-F-m\ge0\)) yields \(w\le-m/\lambda\), with equality anywhere only if \(G-F-m\equiv0\) on that connected component, by the strong maximum principle. Apply the minimum principle to \(w+M/\lambda\) analogously. No strictness across disconnected components is asserted.

## Full expansion from scalar barriers

Put \(\varepsilon=\lambda^{-1}\). Define \(a_1=-F\). Given \(a_1,\ldots,a_r\), put \(A_j=\omega^{-1}dd^c a_j\) and define the next coefficient **pointwise as the formal power-series coefficient**
\[
a_{r+1}=
[\varepsilon^r]\,
\operatorname{tr}\log\!\left(I+\sum_{j=1}^r\varepsilon^j A_j\right),
\qquad r\ge1.
\tag{5}
\]
The logarithm is only a finite **formal** polynomial through order \(r\); it is unambiguous even though the matrices need not commute. For every fixed finite order, the corresponding ordinary real logarithmic determinant is smooth near \(\varepsilon=0\), uniformly in \(x\in X\). Consequently
\[
a_2=-L_\omega F,\qquad
a_3=-L_\omega^2F-\tfrac12\operatorname{tr}(A_F^2).
\]

Fix \(N\), write \(h_N(\varepsilon)=\sum_{j=1}^N\varepsilon^j a_j\).
Compactness and smoothness give \(\omega+dd^c h_N(\varepsilon)>0\) for all sufficiently small positive \(\varepsilon\). By (5), the coefficients through order \(\varepsilon^{N-1}\) of
\[
R_N(\varepsilon,x):=
\log\frac{(\omega+dd^c h_N(\varepsilon))^n}{\omega^n}
-\varepsilon^{-1}h_N(\varepsilon)-F
\]
vanish identically, hence
\[
\|R_N(\varepsilon,\cdot)\|_\infty\le C_N\varepsilon^N.
\tag{6}
\]
The constant shifts \(h_N^\pm=h_N\pm C_N\varepsilon^{N+1}\) preserve **exactly the same positive** \((1,1)\)-form and have residuals
\(R_N\mp C_N\varepsilon^N\).
Thus \(h_N^-\) is a subsolution and \(h_N^+\) is a supersolution for (1). Proposition 14.7.1 proves
\(h_N^-\le u_{\varepsilon^{-1}}\le h_N^+\), giving (3) directly.
For \(N=3\) this yields (2), without using Schauder estimates at large \(\lambda\), any compactness argument for the family, or an interchange of limits.

The argument presupposes the **existence of the smooth solutions** in printed Theorem 14.7.2 (whose continuity proof invokes 14.5.5, 14.5.8 and elliptic theory); it does not independently certify that PDE existence proof. The fixed-\(F\) hypothesis is essential: substituting the obstacle family \(F=-\lambda f\) from lines 54–61 destroys the small \(\varepsilon\)-barrier expansion, so (2)–(3) give no new obstacle-envelope result.

## Normalization and sharpness checks

On the flat elliptic curve \(X=\mathbb C/(\mathbb Z+i\mathbb Z)\), take
\(\omega=(i/2)dz\wedge d\bar z\), \(F(z)=\cos(2\pi\,\Re z)\).
The stated \(dd^c\) normalization gives
\[
L_\omega=\frac1{4\pi}(\partial_x^2+\partial_y^2),\quad
L_\omega F=-\pi F,\quad L_\omega^2F=\pi^2F.
\]
As \(n=1\), \(\operatorname{tr}(A_F^2)=\pi^2 F^2\). Hence
\[
u_\lambda=-\lambda^{-1}F+
\lambda^{-2}\pi F-
\lambda^{-3}\pi^2(F+\tfrac12F^2)+O_{C^0}(\lambda^{-4}).
\tag{7}
\]
The second and third coefficients are nonzero. Thus the stated remainder orders for the first and second truncations cannot, in general, be improved by one power. The constant-data case gives the exact solution \(u_\lambda\equiv-F/\lambda\) and saturates the comparison Lipschitz constant. These are algebraic normalization/model checks, not a full numerical test or project build.

## Audit conclusion and proposed addition

**No confirmed error in Proposition 14.7.1 or Theorem 14.7.2.** The finding is a new, completely proved **conditional consequence** of their smooth existence/comparison conclusions. It distinguishes exact fixed-data large-\(\lambda\) asymptotics from the already-studied obstacle-penalty regime. A possible separately reviewable source/body patch is an optional corollary after Theorem 14.7.2 recording (2)–(4) and the recurrence (5); **no mathematical body, registry, canonical label, permanent tag, website or main-branch change is made**.

**Affected dependents:** direct quantitative use of §14.7.1–2; the obstacle statement at §14.7 physical lines 54–61 / §16.28.2 is explicitly **not** covered. The Fredholm, Schauder and fully nonlinear a-priori inputs of §14.5/§14.7 remain unverified dependencies, not silently promoted to certified results. Demailly approximation and its dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss programme remain **deferred-by-user**, not resolved.

**Coverage change:** §14.7 had already received selected proof-level attention in \`SECTION_MATRIX.md\`; this run re-read its entire two displayed statements/proofs and added the independent scalar-barrier computation. **New first-visited numbered sections: 0. Entire-section or transitive theorem certifications: 0.** The current main-generated table of contents was independently counted as 25 chapters and 747 unique numbered sections.
