# Sharpness of the bounded Monge–Ampère \(L^1\)-to-\(L^\infty\) stability exponent — 2026-10-29

**Pinned production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch:** `review/mathematical-audit`. This is a selected nonexcluded mathematical check, not a certification of the full comparison/domination machinery or the section. No source text, permanent tag, or published site is changed.

## POME-PRESMA-STABILITY-EXPONENT-SHARP-001

**Severity / status:** low / **verified conditional deduction** (a fully computed obstruction to strengthening the *printed* estimate; the printed theorem is **correct**). This result is not a counterexample to Theorem 15.4.1 because that theorem assumes the strictly smaller exponent.

**Integrated anchor:** `docs/sections/equations-with-prescribed-singularities--a-quantitative-stability-estimate/index.html`, main blob `f0c16c8d03d6175fd285bfbc1fc3a6af96cf6d8a`, physical lines **10–28** (hypotheses and exponent of Theorem **15.4.1**), **33–87** (printed proof and its \(q\downarrow1\) exponent), **93–107** (Corollary **15.4.3**). The theorem has source identifier `non-kahler-pluripotential-theory:D2BDFCB4` and permanent tag `72397EB33655`; the section tag is `B4FB50E0C9DE`. The current section states \(p>1\) and a smooth semipositive big \(\theta\). We take a strictly positive \(\theta\), a special admissible case.

**Claim.** For every complex dimension \(n\ge1\), every \(1<p<\infty\), and every
\[
\eta>\eta_*(n,p):=\frac{p-1}{np+p-1},
\]
there exist a **fixed** bounded \(\theta\)-psh \(u\) on \(X=\mathbf P^n\), normalized by \(\sup_Xu=0\), whose Monge–Ampère measure has a nonnegative \(L^p\) density \(f\), and a family of bounded \(\theta\)-psh \(v_\delta\le0\) such that
\[
\frac{\sup_X(v_\delta-u)_+}
 {\bigl(\int_X(v_\delta-u)_+\,dV\bigr)^\eta}\longrightarrow+\infty
 \qquad(\delta\downarrow0).
\]
In particular, even with the solution \(u\), the \(L^p\) density bound, and the \(L^\infty\) bound **fixed**, the stability theorem cannot hold with a universal exponent larger than \(\eta_*(n,p)\). It follows that the printed strict exponent range is optimal as a **supremum of permissible exponents**. This argument does **not** decide whether the endpoint \(\eta=\eta_*\) is valid under the printed assumptions.

### Construction and full calculation

Set \(\theta=\omega_{\mathrm{FS}}\), \(dV=\theta^n\) (a harmless positive normalization of the smooth volume form), and \(o=[1:0:\cdots:0]\). In its affine chart write \(z=(Z_1/Z_0,\ldots,Z_n/Z_0)\), \(r=|z|\), and
\[
g([Z])=\frac{|Z_0|^2}{\sum_{j=0}^n|Z_j|^2}=\frac1{1+r^2}.
\]
Choose an exponent
\[
\beta\in(2-2/p,\,2)
\quad\text{such that}\quad
\frac{\beta}{\beta+2n}<\eta.
\]
Such a \(\beta\) exists because \(\beta\mapsto\beta/(\beta+2n)\) is strictly increasing and
\[
\frac{2-2/p}{2-2/p+2n}=\frac{p-1}{np+p-1}.
\]
Let \(\chi\ge0\) be a smooth radial cutoff supported in a small affine ball and equal to \(1\) near \(o\). Fix sufficiently small \(\lambda,A>0\), and put
\[
u=-\lambda g+A\chi r^\beta
\]
(where the second term is extended by zero to \(X\)). Since \(\chi r^\beta\ge0\) and \(g(o)=1>g(x)\) for every \(x\ne o\), \(u\) has the **unique** global minimum \(u(o)=-\lambda\). By choosing \(A\) sufficiently small relative to \(\lambda\) and the cutoff support, \(u\le0\) everywhere; at the hyperplane \(Z_0=0\) it equals \(0\). Thus \(\sup_Xu=0\) and \(-\lambda\le u\le0\).

In the punctured chart, the complex Hessian of \(r^\beta=(\sum|z_j|^2)^{\beta/2}\) has, up to the fixed \(dd^c=(i/2\pi)\partial\bar\partial\) normalization, tangential eigenvalues \((\beta/2)r^{\beta-2}\) and radial eigenvalue \((\beta/2)^2r^{\beta-2}\). These are positive for \(\beta>0\). All possible negative parts of \(dd^c(\chi r^\beta)\) lie in the smooth compact cutoff annulus and are bounded below by \(-C\theta\). Also \(dd^cg\) is globally smooth. Taking \(\lambda,A\) small makes \(\theta+dd^cu\ge\tfrac12\theta\) as a current. In particular \(u\in\mathrm{PSH}(X,\theta)\cap C^0(X)\), with \(u\) smooth off \(o\).

As \(r\downarrow0\), the determinant of \(\theta+dd^cu\) relative to \(dV\) is asymptotic to a positive constant times \(r^{n(\beta-2)}\); its bounded smooth background terms do not affect the leading power because \(\beta<2\). By the Bedford–Taylor noncharging of pluripolar sets for **bounded** psh potentials, the Monge–Ampère measure has no point mass at \(o\). Its density \(f\) is smooth away from \(o\), and
\[
f^p\,dV\asymp r^{np(\beta-2)+2n-1}\,dr\,d\sigma
\qquad(r\downarrow0).
\]
The integral is finite precisely when \(np(\beta-2)+2n>0\), i.e. \(\beta>2-2/p\), as chosen. Thus \(f\in L^p(dV)\) with **one finite norm independent of \(\delta\)**. This step uses only the bounded Bedford–Taylor product, not approximation/regularization.

For \(0<\delta<\lambda\), define
\[
v_\delta=\max\{u,-\lambda+\delta\}.
\]
Both \(u\) and the constant \(-\lambda+\delta\) are \(\theta\)-psh because \(\theta\ge0\); their maximum is also \(\theta\)-psh. Moreover \(-\lambda\le u\le v_\delta\le0\). At \(o\), \(v_\delta(o)-u(o)=\delta\), and everywhere the difference is at most \(\delta\), so
\[
\sup_X(v_\delta-u)_+=\delta.
\]

Near \(o\), where \(\chi=1\),
\[
u(z)+\lambda=A r^\beta+\frac{\lambda r^2}{1+r^2}.
\]
Since \(0<\beta<2\), the second term is \(o(r^\beta)\). The uniqueness of the minimum and compactness show that, for small \(\delta\), the support of \((v_\delta-u)_+\) is contained in this chart. Let \(J(0)>0\) denote the density of \(dV\) at \(o\) relative to Euclidean \(2n\)-volume. Scaling \(z=(\delta/A)^{1/\beta}y\) and using dominated convergence gives the **exact leading asymptotic**
\[
\begin{split}
I_\delta
&:=\int_X(v_\delta-u)_+\,dV\\
&\sim
J(0)\,\operatorname{Vol}(B^{2n}_1)
\,\frac{\beta}{2n+\beta}\,A^{-2n/\beta}
\,\delta^{1+2n/\beta}.
\end{split}
\]
Indeed, the radial Euclidean integral is
\( |\mathbb S^{2n-1}|\int_0^1(1-r^\beta)r^{2n-1}\,dr
=\operatorname{Vol}(B^{2n}_1)\beta/(2n+\beta)\).
Consequently
\[
\frac{\sup_X(v_\delta-u)_+}{I_\delta^\eta}
\asymp \delta^{\,1-\eta(1+2n/\beta)}
\longrightarrow+\infty,
\]
because \(\eta>\beta/(\beta+2n)\). This disproves the proposed **stronger** exponent while leaving the original estimate intact.

**Bounded-density endpoint diagnostic.** With \(\beta=2\), the same construction is smooth, \(f\in L^\infty\), and \(u+\lambda=(A+\lambda)r^2+O(r^4)\) at \(o\). Then \(I_\delta\asymp\delta^{n+1}\) and \(\sup(v_\delta-u)=\delta\). Thus even for a fixed smooth strictly positive density the exponent cannot exceed \(1/(n+1)\), matching \(\lim_{p\to\infty}\eta_*(n,p)\). This does not assert that the printed finite-\(p\) theorem includes \(p=\infty\).

### Classification, action and dependents

- **Classification:** sharpness of a correct theorem / **verified conditional deduction**; not a false statement, not a proof gap, not an endpoint counterexample, not a new numerical test, and not a full proof of Theorem 15.4.1.
- **Proposed correction:** **none** to the printed theorem. An optional self-contained sharpness remark can be added through a separately reviewable source/reading-edition PR if desired; the audit branch contains documentation only.
- **Affected dependents:** Corollary 15.4.3 inherits the same upper limit on universal powers when used with a fixed reference solution; later regularity statements such as §§15.5–15.6 cite Theorem 15.4.1, but their dedicated Demailly/Chern-connection approximation argument is **deferred-by-user** and is not inspected or certified. No source labels, historical attribution, or other versions are to be merged on the strength of this example.

**Coverage:** selected direct re-examination of the current integrated **Theorem 15.4.1** (hypotheses, dimension, exponent, \(q\downarrow1\) proof passage), with only statement-level comparison to Corollary **15.4.3** and its named later dependents. The actual project-wide matrix remains **25 chapters, 747 numbered table-of-contents sections, zero completely certified sections**. All historical errors, open proof gaps, external-input records, and the entire user-deferred approximation/regularization/Bergman/weighted-\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss programme retain their previous statuses. No build, CI, formalization, source, website, or publication action was performed.
