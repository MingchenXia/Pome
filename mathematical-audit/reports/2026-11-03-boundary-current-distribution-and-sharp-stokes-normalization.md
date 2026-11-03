# Boundary level currents, distributional jump, and sharp Stokes normalization

Date: 2026-11-03. Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit-only review branch, with no amendment to the reading edition.

## Source and status

**POME-BOUNDARY-FLUX-SURFACE-DISTRIBUTION-001 — low / verified conditional deduction.** This is a new direct proof-level audit of the **previously unreviewed Proposition 16.35.5**, together with the boundary term (only) of Proposition 16.43.1. Neither printed proposition is refuted; no defect in their displayed boundary orientation or coefficient is found.

- Integrated main path: docs/sections/polynomial-families-and-equilibrium-null-obstacles/index.html, blob 568257f81e9f31491e0cdde36ba8efb357423cd7. **Proposition 16.35.5:** physical lines 81–90; source label klimek-pluripotential-theory:5DEAA8D5; permanent tag 6F70A6B34439. Section tag 53525C2A2232.
- Integrated main path: docs/sections/boundary-flux-and-nonproper-mass-comparison/index.html, blob b9a79bd1d3254676b65d10031e314a2de1d5a0c4. **Proposition 16.43.1:** physical lines 8–10 and 17–38, especially Stokes identity at 30–36; source label klimek-pluripotential-theory:ED092E5C; permanent tag A9104D666EA7. Section tag C4C1E68A8EDC.
- Normalization: the standing convention is \(dd^c=\frac{i}{2\pi}\partial\bar\partial\), \(d^c=\frac{i}{4\pi}(\bar\partial-\partial)\). The integrated text explicitly records \(d^c(-y_n)=dx_n/(4\pi)\) at §16.35.5 line 88. This audit verifies the associated boundary coefficient rather than presuming Euclidean conventions without the factor \(2\pi\).

## Precise new deduction

Let \(g\in C^1(U,\mathbf R)\), with \(G=\{g<0\}\Subset U\) and \(g^{-1}(0)=\partial G\) a regular compact hypersurface. Define the positive \((1,1)\)-current in Proposition 16.35.5 by
\[
T_g(\alpha)=\int_{\partial G}d^c g\wedge\alpha,
\]
for compactly supported smooth \((n-1,n-1)\)-forms \(\alpha\). Let
\[
\beta=dd^c|z|^2=\frac1\pi\sum_{j=1}^n dx_j\wedge dy_j.
\]
Then the **exact trace identity**, not just positivity, is
\[
\boxed{\quad T_g\!\left(\frac{\beta^{n-1}}{(n-1)!}\right)
=\frac1{4\pi^n}\int_{\partial G}|\nabla g|\,d\mathcal H^{2n-1}.\quad} \tag{1}
\]
Here the notation on the left permits the non-compactly supported constant form because \(T_g\) is compactly supported.

If in addition \(g\in C^2\), then as distribution-valued \((1,1)\)-forms
\[
\boxed{\quad T_g=dd^c(-g)_++\mathbf1_G\,dd^c g
=\delta(g)\,dg\wedge d^c g
=\frac{i}{2\pi}\delta(g)\,\partial g\wedge\bar\partial g.\quad} \tag{2}
\]
The \(\delta(g)\) terms are defined by coarea along the regular zero hypersurface. Formula (2) does **not** say that \((-g)_+\) is PSH or that \(T_g\) is closed; neither claim is generally justified.

Finally, any positive \(C^1\) function \(h\) gives another defining function \(\widetilde g=hg\) with the same negative domain and
\[
\boxed{\qquad T_{\widetilde g}=h|_{\partial G}\,T_g.\qquad} \tag{3}
\]
Thus the current is positive, but its normalization is a first-order property of the **chosen defining function**, not an intrinsic hypersurface measure.

## Complete proof of the new identities

At a boundary point, a unitary affine coordinate change and multiplication of the defining function by a *positive constant at that point* arrange \(dg=-q\,dy_n\), \(q=|\nabla g|>0\), while \(G\) lies on the \(y_n>0\) side to first order. Hence \(d^c g=q\,dx_n/(4\pi)\) on the tangent hyperplane. The outward boundary orientation is \(dx_n\wedge dx_1\wedge dy_1\wedge\cdots\wedge dx_{n-1}\wedge dy_{n-1}\). Restricting \(\beta^{n-1}/(n-1)!\) gives precisely \(\pi^{-(n-1)}\bigwedge_{j<n}dx_j\wedge dy_j\) in the term that survives the wedge with \(dx_n\). This gives \(q/(4\pi^n)\) times Euclidean hypersurface volume. Unitary changes preserve both norms and orientations. Integrating yields (1), with no differentiability beyond \(C^1\).

For \(C^2\) data, the distributional derivative of the characteristic function is \(d\mathbf1_G=-\delta(g)\,dg\). Since \(d^c(-g)_+=-\mathbf1_G\,d^c g\), the product rule gives
\[
dd^c(-g)_+=\delta(g)\,dg\wedge d^c g-\mathbf1_G\,dd^c g.
\]
The coarea definition of \(\delta(g)\,dg\) matches the outward orientation, hence the first equality in (2) coincides with the source's boundary integral. Expanding \(d=\partial+\bar\partial\) and \(d^c\) gives \(dg\wedge d^c g=\frac{i}{2\pi}\partial g\wedge\bar\partial g\), visibly semipositive, proving the remaining equalities and an alternative positivity argument. For (3), restrict \(d^c(hg)=h\,d^c g+g\,d^ch\) to \(g=0\); only the first term remains.

## Exact unit-ball / Stokes test

For \(G=B_R\subset\mathbf C^n\) and \(g(z)=|z|^2-R^2\), the Euclidean sphere has area \(2\pi^nR^{2n-1}/(n-1)!\), and \(|\nabla g|=2R\). Equation (1) gives
\[
T_g\!\left(\frac{\beta^{n-1}}{(n-1)!}\right)
=\frac{R^{2n}}{(n-1)!},\qquad
\int_{\partial B_R}d^cg\wedge\beta^{n-1}=R^{2n}.
\]
Independently, \(\int_{B_R}\beta^n=R^{2n}\), checking the Stokes boundary orientation.

For \(\epsilon>-1\), set \(\beta_\epsilon=(1+\epsilon)\beta=\beta+\epsilon\,dd^c g\). Direct integration and the precise polynomial Stokes identity yield **the same expression**:
\[
\begin{aligned}
\int_{B_R}(\beta_\epsilon^n-\beta^n)
&=((1+\epsilon)^n-1)R^{2n}\\
&=\epsilon\int_{\partial B_R}d^cg\wedge
\sum_{j=0}^{n-1}\beta_\epsilon^j\wedge\beta^{n-1-j}\\
&=\epsilon R^{2n}\sum_{j=0}^{n-1}(1+\epsilon)^j.
\end{aligned}
\]
This independently checks **both** the lack of an extra \(n!\) and the sign of the boundary term in §16.43.1, lines 30–36. The test is a local smooth-ball model, **not** an assertion that the global nonproper-domain construction in §16.43.1 has been proved.

## Assessment and dependencies

**Severity:** low. **Status:** verified conditional deduction from the source's \(C^1\) regular-level assumptions, with the additional \(C^2\) hypothesis explicitly imposed for (2). The printed propositions' boundary sign and \(2\pi\)-normalization survive this check; there is **no confirmed theorem error** and **no body repair**. The test does not establish the existence of the proper Fatou–Bieberbach domain invoked by §16.43.1, global full Monge–Ampère mass \(2^{-n}\), or any upstream approximation argument.

**Suggested reviewable enhancement, not performed:** after §16.35.5, mention the \(C^2\) distributional formula (2) and the exact trace coefficient (1), clarifying dependence on the defining function. The boundary-flux term in §16.43.1 is an **affected mathematical dependent**; its local Stokes coefficient has been verified, while its other dependencies remain unverified. Keep original attribution, source labels and permanent tags unchanged. The earlier withdrawn §16.35.3 polar-hypothesis false positive remains withdrawn, not reopened.

**Actual incremental coverage:** previously unsampled §16.35.5 at its entire displayed proof and §16.43.1's boundary Stokes passage only; no full §16.35 or §16.43 mathematical certification. No Demailly approximation/regularization, Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss work was attempted. All such records remain deferred-by-user. No build, source edit, project tests, formalization, CI, or site publication.
