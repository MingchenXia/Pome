# Distributional Hessians: canonical C¹,¹ representatives and sharp C⁰-to-C¹ stability

**Date:** 2026-10-25 (Asia/Shanghai). **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting audit head:** `129bd677b54aa15fd3c6c53bacaa696facc3f950`. **Scope:** selected, direct proof-level review of integrated §§2.8.1–5 and crosschecks of §§2.9.2, 2.9.4–6, 2.9.10–12, 2.9.19, 2.9.22, 2.9.24, 2.9.26–28. This is a review of basic distribution and Fourier analysis, not of the user-deferred Demailly approximation programme.

**Exact integrated sources.** `docs/sections/measures-and-distributions--densities-and-differentiation-of-integrals/index.html`, main blob `1b600ca8444edebc8e05e300cb86ae371e9f8535`: Lemma **2.8.1**, source `foundations-of-pluripotential-theory-43819F13`, permanent tag **9790D3B21542**, lines 10–46; Corollary **2.8.2**, permanent tag **D30ED2659FC7**, lines 54–75; Lebesgue differentiation Theorem **2.8.3**, tag **CF98893DE93E**, lines 79–117; cube Poincaré Lemma **2.8.4**, tag **CAAD90CD1576**, lines 124–142; Proposition **2.8.5**, source `foundations-of-pluripotential-theory-B959E3ED`, tag **B412D7DC28A3**, statement lines 146–151, proof lines 154–226, especially Hessian estimates 159–181 and Lebesgue-point expansion 183–217. Relevant elementary inputs: §2.5.1 and §2.5.3 convolution of distributions; §2.7.4 Arzelà–Ascoli.

`docs/sections/fourier-analysis-and-incidence-of-complex-lines/index.html`, main blob `b2366d2a9604cc6f39cf45ced697905978dff8ab`: Fourier/Plancherel §2.9.2–6, lines 35–203; Calderón–Zygmund and Hessian multiplier §§2.9.10–12, lines 215–381; projective incidence §§2.9.19, 2.9.22, 2.9.24, 2.9.26–28, lines 637–918. This latter section already has earlier substantive audit IDs `POME-FOURIER-PROJ-001`, `POME-FOURIER-INC-001`, and `POME-INCIDENCE-LINES-MASS-001`; they are **not** re-registered as new findings.

## POME-DISTRIBUTIONAL-HESSIAN-REP-001

**Severity:** low. **Status:** verified conditional deduction (strengthening of a correct proposition, **not** a false theorem). **Affected statements:** Proposition 2.8.5 and potential internal citations requiring a continuous representative; no change required in the existing statement or tags.

**Claim.** Let \(\Omega\subset\mathbb R^d\) be open, and let \(T\in\mathcal D'(\Omega;\mathbb R)\) be a real **distribution**, with no assumed pointwise representative. Suppose all second distributional partial derivatives satisfy
\[
\partial_a\partial_b T=A_{ab}\in L^\infty_{\rm loc}(\Omega).
\]
Then there is a **unique** \(F\in C^{1,1}_{\rm loc}(\Omega)\) representing \(T\) as a distribution. Moreover, if \(V\subset\Omega\) is convex and
\[
\|A(x)\|_{\mathrm{op}}\le M\quad\text{a.e. on }V,
\]
then
\[
\operatorname{Lip}(\nabla F|_V)\le M,\qquad
|F(y)-F(x)-\nabla F(x)\cdot(y-x)|\le\frac M2|y-x|^2
\quad(x,y\in V).
\]
Both constants are optimal. The original coordinatewise bound \(|A_{ab}|\le C\) gives \(M\le dC\), and the printed constant \(dC\) is itself optimal for the coordinatewise hypothesis.

**Proof.** Commutation of distribution derivatives shows \(A_{ab}=A_{ba}\) almost everywhere. On a ball \(B(x_0,3R)\Subset\Omega\) take a standard nonnegative compactly supported Euclidean mollifier \(\rho_\varepsilon\); \(T_\varepsilon=T*\rho_\varepsilon\) tends to \(T\) in distributions on \(B(x_0,2R)\). For sufficiently small \(\varepsilon\), the Hessian of \(T_\varepsilon\) equals \(A*\rho_\varepsilon\). On \(B(x_0,2R)\), its operator norm is at most the essential operator norm of \(A\) on the larger ball, by the triangle inequality for integrals of matrices. Call this finite bound \(M_0\). Write on \(B(x_0,R)\)
\[
T_\varepsilon(x)=a_\varepsilon+b_\varepsilon\cdot(x-x_0)+R_\varepsilon(x),
\quad a_\varepsilon=T_\varepsilon(x_0),\quad
b_\varepsilon=\nabla T_\varepsilon(x_0).
\]
Taylor's integral remainder gives
\[
|R_\varepsilon(x)|\le\tfrac12M_0|x-x_0|^2,\quad
|\nabla R_\varepsilon(x)|\le M_0|x-x_0|.
\]
It is crucial not to infer a bound for \(a_\varepsilon,b_\varepsilon\) from the Hessian bound alone: affine functions have zero Hessian. Instead, choose a smooth compactly supported radial test function \(\eta\) in \(B(x_0,R)\) with integral one. Its first moments about \(x_0\) vanish. Put \(\zeta_j=-\partial_j\eta\). Integration by parts gives
\[
\int\zeta_j=0,\qquad
\int(x-x_0)_k\zeta_j(x)\,dx=\delta_{jk}.
\]
Consequently
\[
\langle T_\varepsilon,\eta\rangle
=a_\varepsilon+\int R_\varepsilon\eta,\qquad
\langle T_\varepsilon,\zeta_j\rangle
=(b_\varepsilon)_j+\int R_\varepsilon\zeta_j.
\]
All pairings on the left converge, while the remainder integrals are uniformly bounded. Thus \(a_\varepsilon\) and \(b_\varepsilon\) are uniformly bounded. The families \(T_\varepsilon\) and \(\nabla T_\varepsilon\) are therefore bounded and equicontinuous on each smaller closed ball; the gradients are equi-Lipschitz. Arzelà–Ascoli and the fundamental theorem of calculus yield a subsequence converging in \(C^1\) there. Its limit represents \(T\), since the mollifications converge distributionally. Any two such continuous representatives agree everywhere because they determine the same distribution. This uniqueness glues the representatives over a countable ball cover of \(\Omega\), and shows \(F\in C^{1,1}_{\rm loc}(\Omega)\).

Now assume the operator-norm bound \(M\) on a convex \(V\). For any fixed \(x,y\in V\), their closed segment has positive distance from \(\mathbb R^d\setminus V\); sufficiently small mollifiers preserve the Hessian bound \(M\) on that segment. Integrating the mollified Hessians along the segment and taking the established local \(C^1\) limit gives \(|\nabla F(y)-\nabla F(x)|\le M|y-x|\); a second integration gives the stated quadratic remainder. The model \(F(x)=\tfrac M2(e\cdot x)^2\) for a unit vector \(e\) attains these constants. For the coordinatewise hypothesis, \(F(x)=\tfrac C2(x_1+\cdots+x_d)^2\) has \(A_{ab}=C\), while the gradient difference along \(e=d^{-1/2}(1,\ldots,1)\) is exactly \(dC\) times the displacement. \(\square\)

**Proposed disposition.** Optional corollary after Proposition 2.8.5: remove prior continuity when the input is given as a distribution, explicitly state the canonical representative and matrix-norm variant. No source/body/registry mutation is proposed in this audit branch. This proof is entirely elementary and does not rely on the excluded approximation programme.

## POME-DISTRIBUTIONAL-C0C1-MODULUS-001

**Severity:** low. **Status:** verified conditional deduction (quantitative stability of the correct Proposition 2.8.5). **Dependents:** potential passages passing from uniformly convergent families with bounded Hessians to convergent first derivatives; does not certify such uses if their hypotheses differ.

**Claim.** Let \(B\subset\mathbb R^d\) be an open ball, let \(K\Subset B\), and choose \(r>0\) with \(\operatorname{dist}(K,\partial B)\ge r\). Suppose \(f,g\in C^{1,1}(B)\) are real, with \(\|D^2 f\|_{\mathrm{op}},\|D^2g\|_{\mathrm{op}}\le M\) almost everywhere, and put \(\delta=\|f-g\|_{L^\infty(B)}<\infty\). Then
\[
\boxed{\quad
\|\nabla f-\nabla g\|_{L^\infty(K)}
\le \inf_{0<t<r}\left(\frac\delta t+Mt\right).
\quad}
\]
In particular, if \(M>0\) and \(\delta<Mr^2\), then \(\|\nabla f-\nabla g\|_{L^\infty(K)}\le2\sqrt{M\delta}\). The **exponent** \(1/2\) cannot be improved even for smooth functions on a fixed ball. Consequently any **directed net** \(f_i\) with common Hessian bound \(M\) and \(f_i\to f\) uniformly on \(B\) converges to \(f\) in \(C^1\) on compact subsets of \(B\); the limit remains \(C^{1,1}\) with the same bound. The same statement holds if the potentials are first supplied as distributions and replaced by the unique representatives above.

**Proof.** Put \(h=f-g\). The Hessian of \(h\) has operator norm at most \(2M\) almost everywhere. For \(x\in K\), a unit vector \(e\) and \(0<t<r\), both \(x\pm te\in B\). The fundamental theorem of calculus with Lipschitz derivative yields
\[
|h(x\pm te)-h(x)\mp t\,\partial_eh(x)|\le Mt^2.
\]
Subtracting the expansions and using \(|h|\le\delta\) gives
\[
2t|\partial_eh(x)|\le2\delta+2Mt^2,
\quad |\partial_eh(x)|\le\delta/t+Mt.
\]
Take the supremum over unit \(e\), points \(x\in K\), then the infimum over \(t\). For \(t=\sqrt{\delta/M}<r\) one obtains the square-root estimate. With fixed \(M>0\), consider \(f_\delta(x)=\delta\sin(\sqrt{M/\delta}\,x_1)\), \(g=0\), on a ball containing the origin. Then \(\|f_\delta\|_\infty\le\delta\), \(\|D^2 f_\delta\|_{\mathrm{op}}\le M\) and \(|\nabla f_\delta(0)|=\sqrt{M\delta}\), proving optimality of the exponent (not claiming the displayed coefficient 2 is optimal). For a uniformly converging directed net, the pairwise \(\delta_{ij}\to0\) in the product directed order, so the estimate makes the gradients Cauchy in each compact sup norm, **without extracting a sequence**. The limits satisfy the fundamental-theorem-of-calculus identity and preserve the common Lipschitz gradient bound. \(\square\)

**Proposed disposition.** Optional quantitative lemma after §2.8.5, useful for weak-to-strong arguments with common Hessian bounds. Preserve the original Proposition 2.8.5 and all permanent tags.

## Other genuinely inspected arguments and limits

In §2.8, the dyadic conditional-average orthogonality and measure extension in Lemma 2.8.1 (lines 26–46), positive/negative distribution splitting in Corollary 2.8.2 (69–75), maximal-cube proof of Lebesgue differentiation (89–117), and the cube Poincaré/Fubini factor (134–142) are compatible with their stated hypotheses. In §2.9, the Fourier sign \(-\xi_a\xi_b/|\xi|^2\) for \(T_{ab}(-\Delta v)\), heat-kernel limiting argument (245–293), weak-(1,1)/strong-\(L^p\) interpolation (307–380), Riesz Fourier constant (135–170) and complex-hyperplane averaging normalization (792–848) were directly crosschecked against the printed formulas; no new confirmed mathematical defect resulted. The earlier Fourier projection/incidence IDs remain unchanged and were not claimed again as new progress.

This report does **not** certify any entire section, all distributions/measure dependencies, the higher-dimensional weak-type singular integral theorem in all its applications, or the full project. The user-deferred Demailly approximation/regularization and dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remains **deferred-by-user**, not reopened, resolved or certified. No Python/JS test, full build, CI, formal verification, site publication, main/source/registry/tag edit, or automatic PR merge was performed.
