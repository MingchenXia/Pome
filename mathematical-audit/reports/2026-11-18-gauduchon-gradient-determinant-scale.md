# Quantitative determinant-scale gradient barrier for the Gauduchon matrix

**Date:** 2026-11-18. **Finding:** `POME-GAUD-GRADIENT-DETERMINANT-SCALE-001` (**low / verified conditional deduction**). **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Status of printed Lemma 14.15.1, Theorem 14.15.2, and Proposition 14.16.1:** no counterexample or incorrect printed implication found; their upstream chains are *not* certified here. This note adds a precise, independent quantitative consequence of the rescaling argument. It does **not** repeat the previously recorded `POME-GAUD-LIOUVILLE-MAXIMALITY-NECESSARY-001` radial countermodel (2026-11-04).

## Integrated reading-edition anchors

| Role | Current integrated HTML and blob | Stable source / permanent tag; physical lines |
| --- | --- | --- |
| Cone, viscosity maximality, stability and comparison | `docs/sections/smooth-monge-ampere-equations--a-liouville-theorem-for-the-limiting-cone/index.html`, `2a5f42ad68db1f5091a0c2e0c5a29e2c3887cdec` | `non-kahler-pluripotential-theory:D0FAF6CD` / `6E3495B1A225` (Lemma 14.15.1, lines 31–47); `non-kahler-pluripotential-theory:7A4BB576` / `AC61FE141521` (Theorem 14.15.2, lines 51–154) |
| Fixed-background matrix decomposition | `docs/sections/smooth-monge-ampere-equations--the-matrix-structure-of-the-gauduchon-equation/index.html`, `6e1faedde219b856c0bf5ecaf566403ae999772e` | Equation 14.13.1, permanent `D281466AD7B7` (lines 16–35; dependency context only) |
| Original gradient blowup | `docs/sections/smooth-monge-ampere-equations--the-gradient-bound-by-rescaling/index.html`, `4081db05fb0a989451c4e536f8e285501c399e81` | `non-kahler-pluripotential-theory:6B4FF351` / `EFE7268223F4` (Proposition 14.16.1, lines 13–19); equation tag `977E6E7B264D` (lines 15–17); normalized determinant equation tag `3DCC81BE4D1E` (lines 51–66); entire argument lines 24–73 |

## New conditional quantitative statement

Let \(n\ge 2\), and fix the smooth compact Hermitian geometric data \((X,\gamma,\gamma_0)\) used in (14.13.1). Write
\[
Q_u=Q_0+P_\gamma\bigl(\mathrm i\partial\bar\partial (u/(2\pi))\bigr)+Z(\partial(u/(2\pi))) ,
\qquad
P_\gamma(H)=\frac{(\operatorname{tr}_\gamma H)I-H}{n-1}.
\]
The map \(Z\) is a fixed real-linear first-order expression with smooth coefficients. For prescribed constants \(B,K>0\), consider **any** smooth real functions \(u\) for which
\[
\|u\|_{L^\infty(X)}\le B,\qquad Q_u>0,\qquad
\|dd^c u\|_{L^\infty(X,\gamma)}
\le K\bigl(1+ A(u)^2\bigr),
\qquad A(u):=\sup_X|\partial u|_\gamma.
\]
Set \(D(u):=\sup_X\det_\gamma Q_u\), a finite positive number. **There exists a constant \(C=C(X,\gamma,\gamma_0,B,K)>0\), independent of \(u\) and of the prescribed right-hand side, such that**
\[
\boxed{\displaystyle A(u)\le C\bigl(1+D(u)^{1/(2n)}\bigr).}\tag{*}
\]
For actual Gauduchon solutions satisfying (14.13.1), this reads
\[
\sup_X|\partial u|_\gamma
\le C\left(1+\exp\left(\frac{n-1}{2n}\sup_X(F+b)\right)\right).
\]
Only an upper bound on the determinant enters this *conditional* gradient estimate. In contrast, the printed Proposition 14.16.1 uses an a priori \(C^0\) bound on \(F\) and a separate bound on \(b\) to secure a fixed determinant bound. The new formulation isolates the precise scale of this input and does **not** assert the independent \(C^0\) bounds for \(u,b\).

### Complete proof of (*)

Suppose that no such uniform \(C\) exists. Choose a sequence \(u_j\) with \(A_j=A(u_j)\), \(D_j=D(u_j)\) and
\[
\frac{A_j}{1+D_j^{1/(2n)}}\longrightarrow\infty.
\]
In particular \(A_j\to\infty\) and \(D_j/A_j^{2n}\to0\). Let \(x_j\) maximize \(|\partial u_j|_\gamma\). Pass to a subsequence lying in one fixed bounded-geometry coordinate chart; perform uniformly controlled complex-linear changes so that \(\gamma(x_j)=I\). On balls of radii comparable to \(A_j\), set \(v_j(z)=u_j(x_j+z/A_j)\). The \(C^0\) bound gives \(|v_j|\le B\); gradient maximality gives local uniform Lipschitz bounds and \(|\partial v_j(0)|=1\). The assumed complex-Hessian estimate gives uniform local bounds on \(\partial\bar\partial v_j\), including after scaling by \(A_j^{-2}\).

The local Euclidean Laplacians of the \(v_j\) are therefore uniformly bounded. Interior \(W^{2,p}\) estimates for the Euclidean Laplacian, using \(|v_j|\le B\), hold for every finite \(p\). For \(p>2n\), compact Sobolev embedding and a diagonal subsequence yield \(v_j\to v\) in \(C^1_{\mathrm{loc}}(\mathbb C^n)\), with \(v\) bounded and globally Lipschitz and \(|\partial v(0)|=1\).

In the moving unitary frames of the printed proof, the *exact* (14.13.1) decomposition gives, uniformly on each fixed ball,
\[
A_j^{-2}Q_{u_j}
=P_n\bigl(H(v_j)/(2\pi)\bigr)+o(1).
\]
Indeed the smooth background is \(O(A_j^{-2})\), the fixed first-order torsion term is \(O(A_j^{-1})\), and the scaled metric tends smoothly to the identity. Positivity \(Q_{u_j}>0\) yields \(P_n(H(v))\ge0\) distributionally. Further,
\[
0<\det(A_j^{-2}Q_{u_j})\le D_j/A_j^{2n}\longrightarrow0
\]
uniformly on fixed balls. If a smooth \(h\) touched \(v\) from below with \(P_n(H(h))>0\), subtracting a small quadratic makes the contact strict. Local uniform convergence produces nearby interior contacts with \(v_j\); their complex Hessians dominate that of the perturbed \(h\). Positivity preservation by \(P_n\) then forces \(A_j^{-2}Q_{u_j}\ge cI>0\) there, contradicting the vanishing determinant bound. Hence \(v\) is *maximal* for the cone as well as admissible. Theorem 14.15.2 makes this bounded globally Lipschitz (v) constant, contrary to \(|\partial v(0)|=1\). This proves (*).

The proof uses no quantitative Liouville constant and accordingly establishes the existence, **not an explicit numerical value**, of \(C\). It does not claim any estimate if the \(L^\infty\) or the stated Hessian-to-gradient bound is removed.

## Direct audit of the printed proofs

**§14.15 (whole section, direct argument):** Verified the comparison perturbation \(h+\delta(|z|^2-R^2)\) and locally uniform stability in Lemma 14.15.1 (31–47); for Theorem 14.15.2, checked the (n=2) plurisubharmonic base, exact \(P_n(H\oplus0)\) block reduction (58–66), normalized bounded-subharmonic averages of \(v,v^2\) (68–86), weak directional derivative limit (89–98), the negation/compactness quantifiers yielding (14.15.5) (100–113), the Lipschitz annular estimate and kernel positivity (115–145), and bounded comparison domain \(D'=\{v<h\}\) (147–154). No unproved passage from a general directed net to a sequence was used in this reviewed proof. The previously documented explicit **nonmaximal** radial admissible function is not a new result of this run and is not reclassified.

**§14.16 (whole section, direct argument):** Verified the blowup normalization, uniform local \(C^1\) compactness from bounded rescaled complex Laplacians, the precise \(O(A_j^{-2})/O(A_j^{-1})\) background/torsion contributions, the unitary determinant comparison, strict lower test and contradiction (24–69), and the final conditional invocation of the second-derivative estimate (73). The new proof above identifies exactly which piece of the printed \(C^0\) density hypothesis is used at the blowup stage.

**Scope and upstream:** Theorem 14.15.2 uses bounded-psh Liouville (internal §5.24.5), subharmonic mean monotonicity, Arzelà–Ascoli and standard local elliptic \(W^{2,p}\) compactness; the §14.16 argument uses (14.13.1), the fixed geometric coefficients, and conditional Hessian bound from §14.14. These upstream chains are crosschecked only where cited, not certified end to end. In particular, the printed Cauchy/elliptic estimate, the Gauduchon continuity method, and the non-Kähler existence theorem are not being declared proved. None of the excluded Demailly-regularization/Bergman/dedicated L²/Ohsawa–Takegoshi/multiscale/positivity-loss programmes was opened.

## Classification and proposed change

- **Severity/status:** low / **verified conditional deduction**; printed results are **not false** and no new gap is asserted. The estimate is unconditional under its explicitly stated matrix, boundedness, positivity and Hessian assumptions, but depends on the already printed cone Liouville theorem for its proof.
- **Proposed (not applied) source improvement:** optional lemma after Proposition 14.16.1 stating (*) and its determinant-right-hand-side form; keep the original stronger-uniform-data formulation. No canonical tags, source files or integrated body are changed in this audit branch.
- **Affected dependents:** §14.16.1 gradient control, the subsequent §14.17 existence strategy if one seeks estimates with nonuniform (F+b). This note supplies no new a priori bound on (u), (b) or the Hessian itself.
- **Verification performed:** symbolic hand calculation of the matrix scaling and logical contradiction, direct full reading of §§14.15–14.16 and (14.13.1). No builds, runtime tests, CI, website publication or theorem-prover checks performed.
