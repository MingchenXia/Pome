# 2026-11-12 — Disconnected-component obstruction to the common Monge–Ampère normalization scalar

**Stable finding:** POME-MA-DISCONNECTED-COMPONENT-SCALAR-001  
**Classification:** **high / confirmed error (missing connectedness in the integrated chapter scope)**.  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Status boundary:** the statements below fail *as printed when a compact complex manifold is allowed to be disconnected*. This does **not** disprove the intended connected-manifold Tosatti–Weinkove theorem, and this audit does not independently certify its full proof.

## Precisely reviewed integrated text

- Chapter 1 convention: `docs/sections/conventions/index.html`, blob `ef778e54d8d7413242387e95c52269b3c7d42cae`, physical lines 17–25: a **domain** is connected, while a **complex manifold** is only assumed paracompact. Thus connectedness of a complex manifold is not a global convention.
- Chapter 14 initial scope: `docs/sections/smooth-monge-ampere-equations/index.html`, blob `e35eb98bdc1c62c4938155964945f4d6495b4ee4`, lines 7–17: “Throughout this chapter” specifies the Hermitian form and smooth volume form, but does not say that \(X\) is connected (or explicitly compact). Equation 14.1.1: original source `non-kahler-pluripotential-theory:2BED92DC`, permanent tag `C5FA7F078BB6`, lines 9–14.
- `docs/sections/smooth-monge-ampere-equations--scalar-bounds-and-uniqueness/index.html`, blob `3f96829e18befc845df40c6d4bca13c977ae9cea`: Theorem 14.2.1 (original `non-kahler-pluripotential-theory:3EE16849`, permanent `F33DA8C9DF9F`, lines 10–15), Proposition 14.2.4 (original `:E26E18C6`, permanent `366AA2E61158`, lines 49–65).
- `docs/sections/smooth-monge-ampere-equations--the-potential-bound-from-weighted-integration/index.html`, blob `f774b702e65736ce8a23847dbb3409c6b31b0211`: Theorem 14.3.5 (original `non-kahler-pluripotential-theory:C569075E`, permanent `EEF74F1DEBB8`, lines 107–149). The final appeal to Theorem 5.25.2 is at lines 143–149.
- `docs/sections/smooth-monge-ampere-equations--the-linearized-equation-and-smooth-dependence/index.html`, blob `2f9ebecbd5bd079eb8573b4bb97df0fb5ab1bdfb`: Proposition 14.4.1 (original `non-kahler-pluripotential-theory:E0953F19`, permanent `2AD3CD874EA4`, lines 19–38), with claimed invertibility at lines 32–38.
- `docs/sections/smooth-monge-ampere-equations--the-continuity-method/index.html`, blob `81d74e60560d2241c9e3cc0dacf583d080b8bdd8`: proof of Theorem 14.2.1, lines 9–26.
- The contrast is explicit in `docs/sections/plurisubharmonic-functions-and-singularities--plurisubharmonic-potentials/index.html`, blob `bf6e5ca74ac04a3d79565bb58bda8d968a68be68`, line 7: **Chapter 5**, not Chapter 14, declares \(X\) a connected compact complex manifold. Theorem 5.25.2 itself, original `non-kahler-pluripotential-theory:D9A05B95`, permanent `FC59B7D406A3`, `docs/sections/plurisubharmonic-functions-and-singularities--normalized-compactness/index.html` blob `d7ff8eafea43197c77de4bfd335bed0764ab4f69`, lines 31–51, invokes connectedness of the finite coordinate-ball intersection graph at line 47.

## Complete counterexamples, all dimensions

Fix any integer \(n\geq1\). Let \(Y=(\mathbb P^1)^n\), with its product Kähler form \(\omega_Y=\sum_{j=1}^n\mathrm{pr}_j^*\omega_{\mathrm{FS}}\), and let \(X=Y_1\sqcup Y_2\) be two disjoint copies. On each component set \(\omega=\omega_Y\), \(\mathrm dV=\omega_Y^n\). This is a compact (but disconnected) complex manifold with smooth Hermitian form and positive smooth volume form.

**Nonexistence of a single scalar for arbitrary \(F\).** Set \(F|_{Y_1}=0\) and \(F|_{Y_2}=\log2\); \(F\) is smooth. If a pair \((u,b)\) solved (14.1.1), integration on each component would give
\[
\int_{Y_i}(\omega+dd^cu)^n
=e^b\int_{Y_i}e^F\omega^n.
\]
Since \(\omega\) is closed, the left side equals \(V:=\int_Y\omega_Y^n>0\) on **each** component. Indeed, with \(\omega_t=\omega+tdd^cu\),
\[
\frac{\mathrm d}{\mathrm dt}\int_{Y_i}\omega_t^n
=n\int_{Y_i}dd^cu\wedge\omega_t^{n-1}
=n\int_{Y_i}d(d^cu\wedge\omega_t^{n-1})=0
\]
by Stokes and \(d\omega_t=0\). The equations are simultaneously \(V=e^bV\) and \(V=2e^bV\), a contradiction. Thus **the existence assertion of Theorem 14.2.1 fails under its unqualified integrated chapter scope, for every \(n\ge1\)**.

**Failure of normalized uniqueness.** Instead take \(F=0\). For every \(A\ge0\), let \(u_A=0\) on \(Y_1\) and \(u_A=-A\) on \(Y_2\). Then \(dd^cu_A=0\), \(b=0\), the equation holds, \(\omega_{u_A}=\omega>0\), and \(\sup_Xu_A=0\). Distinct \(A\)'s yield distinct normalized solutions: Theorem 14.2.1's uniqueness fails. Moreover \(u_A-u_B\) is **locally** constant but not globally constant for \(A\ne B\), contradicting the literal conclusion of Proposition 14.2.4 (whose maximum-principle proof only gives componentwise constancy).

**Failure of the uniform potential bound.** In the same \(F=0\) family, \((\omega+dd^cu_A)^n=\omega^n\le 1\cdot\omega^n\), while \(\|u_A\|_\infty=A\to\infty\). Thus Theorem 14.3.5's conclusion is false without connectedness. The proof's final application of Theorem 5.25.2 is invalid outside that theorem's Chapter 5 connected setting.

**Failure of the claimed linear inverse.** Proposition 14.4.1 normalizes by \(\int_Xu\,dV=0\), and its derivative in \((u,b)\) is \((v,a)\mapsto L_uv-a\). Write \(V_i=\int_{Y_i}dV\). Choose \(v|_{Y_1}=V_2\) and \(v|_{Y_2}=-V_1\). Then \(v\not\equiv0\), \(\int_Xv\,dV=0\), \(dd^cv=0\), and \(L_uv=0\). Hence \((v,0)\) is in the kernel, so the asserted Banach inverse **does not exist** on the printed disconnected scope. There are also two independent componentwise adjoint compatibility conditions but only one scalar \(a\). The proof of Theorem 14.2.1 in §14.6 consequently cannot claim openness for this scope: for the first example, the path \(F_t=tF\) is solvable at \(t=0\) and unsolvable for every \(t>0\).

## Scope, classification, proposed correction, and dependents

The counterexamples require **no** Demailly approximation, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale atlas, or positivity-loss argument. They use only smooth Kähler forms, locally constant potentials and Stokes' theorem. They are not counterexamples on a connected compact manifold. The defect is an **omitted hypothesis in the integrated reading edition**, not a claim that the intended connected theorem is false, nor merely a gap in an otherwise universally valid proof.

**Proposed source/reading patch (not applied):** add at the start of §14.1 a chapter-wide statement such as “Throughout this chapter, \(X\) is a connected compact complex manifold of dimension \(n\ge1\), unless otherwise stated.” Audit each later special setting for compatibility. Alternatively state connectedness separately in Theorem 14.2.1, Proposition 14.2.4, Theorem 14.3.5, and Proposition 14.4.1 with downstream propagation. If disconnected \(X\) is desired, introduce separate scalars \(b_i\) and normalizations per component; a common \(b\) is not generally possible, and global \(\sup_Xu=0\) does not eliminate independent componentwise constants.

**Directly affected:** 14.2.1 existence/uniqueness, 14.2.4 global-constant conclusion, 14.3.5 global \(C^0\) bound, 14.4.1 claimed inverse/smooth single-valued solution, and the openness/closedness proof in §14.6. **Potential further dependents** using these results (later scalar variation and continuity) require individual scope checks; they are not hereby declared false on connected manifolds. This is distinct from the older SGPT disconnected-normalization finding because these are Chapter 14's coupled smooth Hermitian Monge–Ampère existence/normalization statements with a **componentwise integral obstruction** to one scalar.

**Coverage:** selected integrated proof-level inspection in §§14.1–14.4 and §14.6, plus only convention/Chapter 5 hypotheses as supporting crosschecks. All of those numbered Chapter 14 sections were previously partially visited in the audit; this session adds **0 first proof-level numbered-section visits and 0 whole-section mathematical certifications**. Current actual ToC: **25 chapters, 747 numbered sections**. No statements in excluded regularization material were audited. User-deferred notes stay **deferred-by-user**, not resolved or certified.
