# Iterated-logarithm endpoint for unibranch curve equations and the four-ruling Cartier lattice of a threefold node

**Date:** 2026-10-31. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Status:** two new low-severity, verified conditional deductions; no printed theorem or question is declared false. **Scope:** two selected proof/model inspections, not a whole-section or transitive theorem certification.

The current production reader, not unintegrated source numbering, is the object of review. The Demailly approximation/regularization programme and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss work are **deferred-by-user**. Nothing below depends on re-opening them.

## POME-UNI-LOGLOG-ORDTYPE-001 — the second logarithmic integrability threshold

**Severity:** low. **Status:** verified conditional deduction; original Theorem 9.11.60 remains correct. This is the boundary line with exponent gamma=2 and an additional iterated logarithm, not the earlier gamma>2 theorem or the already registered Dini estimate POME-UNI-LOG-DINI-001.

**Pinned text:** docs/sections/potentials-and-equations-on-unibranch-spaces/index.html, main blob fa1475ba7cd3b71cf195e91c45b5719b517bb0ae, subsection 9.11.59, physical lines 1019–1039; Theorem 9.11.60 (source non-kahler-pluripotential-theory:267B655B, permanent E80960D59FB4), lines 1040–1102; Equation 9.11.61 (source 36F6A4FF, permanent 7B4446B6082E), lines 1054–1062; Equation 9.11.62 (source 00151FF8, permanent BA74C8891A07), lines 1079–1083. Dependent Problem 24.11.1 (source non-kahler-pluripotential-theory:A6F8C69E, permanent A63319B4B931) is in docs/sections/problems-in-hermitian-pluripotential-theory--equations-on-singular-spaces/index.html, blob 95fe41df613a9b40e64fdd1f5992492e2add31f1, physical lines 13–28.

**New claim, including quantifiers.** Retain precisely the compact unibranch curve / elliptic normalization, background, fixed logarithmic type, and mass data of 9.11.50–60. On a sufficiently small flat coordinate disk centered at a chosen normalization point q, put
\[
r=|z|,\quad t=\log(1/r)>e,\quad
f_{\eta}(z)=C_0\,r^{-2}t^{-2}(\log t)^{-\eta},\qquad C_0>0,\quad \eta\in\mathbb R.
\]
Extend the density smoothly and positively off that disk, and define
\[
F_{\eta}=\int_E f_{\eta}\beta_0,\quad c_{\eta}=M/F_{\eta},
\quad \nu_{\eta}=\pi_*(f_{\eta}\beta_0)
\]
with the printed conventions \(\beta_0=dA/V\) and \(M=H-A>0\). **Every real eta gives an L1 density, but no eta gives any Lp density for p>1.** The equation \(\mathrm{MA}^{\mathrm{ext}}_{X,h}(u)=c\nu_{\eta}\), \(c>0\), has a solution in the fixed *ordinary* singularity type of \(\psi\) **if and only if \(\eta>1\)**; then necessarily \(c=c_{\eta}\), and normalized uniqueness follows from the compact-curve harmonic-difference argument. For \(\eta\le1\) the constructed extended-mass solution of mass M remains in the same *multiplier-ideal* type but not the ordinary type; no positive c solves the equation in that ordinary type. In the good regime the residual is continuous on the normalization but not Holder of any positive exponent.

**Direct local calculation.** Write \(k=4\pi C_0/V\) and \(w_{\eta}(t)=t^{-2}(\log t)^{-\eta}\). For fixed \(t_0>e\) set
\[
Q_{\eta}(t)=\int_t^\infty w_{\eta}(s)\,ds,\qquad
P_{\eta}(t)=-k\int_{t_0}^{t}Q_{\eta}(u)\,du.
\]
All these tails converge, for every real eta. Exact differentiation gives
\(P'_{\eta}=-k Q_{\eta}\) and \(P''_{\eta}=k w_{\eta}\). With the printed normalization \(dd^c=i\partial\bar\partial/(2\pi)\), the radial Laplacian is \(dd^cP_{\eta}=P''_{\eta}(t)dA/(4\pi r^2)=f_{\eta}\beta_0\). The enclosed flux is
\[
-\tfrac12P'_{\eta}(t)=\frac{k}{2}Q_{\eta}(t)
\longrightarrow0,
\]
so the distributional extension creates **no Dirac mass at q**. Also \(P_{\eta}(t)=o(t)\); it is locally integrable and has Lelong number zero. These assertions do not rely on any psh regularization, L2 estimate, or extension theorem.

An elementary integration by parts yields
\[
Q_{\eta}(t)=\frac{1+O(1/\log t)}{t(\log t)^\eta}.
\]
Consequently the *sharp* alternatives, with nonzero leading coefficients, are
\[
\begin{array}{ll}
\eta>1:&
P_{\eta}(\infty)-P_{\eta}(t)
\sim \dfrac{k}{\eta-1}(\log t)^{1-\eta},\\[4pt]
\eta=1:&
P_{\eta}(t)\sim-k\log\log t,\\[4pt]
\eta<1:&
P_{\eta}(t)\sim-\dfrac{k}{1-\eta}(\log t)^{1-\eta}.
\end{array}
\]
In particular \(P_\eta\) is bounded at q exactly when eta>1. The positive density has total local mass proportional to
\(\int^\infty t^{-2}(\log t)^{-\eta}dt<\infty\), for all eta, while its p-th power has local integral comparable to
\(\int^\infty e^{2(p-1)t}t^{-2p}(\log t)^{-\eta p}dt=\infty\), for every p>1. For eta>1 the residual decay is exactly of order \([\log\log(1/r)]^{1-\eta}\), slower than every \(r^\alpha\).

**Global deduction and its conditional boundary.** Just as in the actual proof of 9.11.60, take a cutoff chi equal to one near q, put \(L=c_{\eta}\chi P_{\eta}\), and solve the *smooth* zero-integral correction
\[
\rho\beta_0=(c_{\eta}f_{\eta}-M)\beta_0-dd^cL
\]
on the elliptic normalization. The printed Green inverse in Lemma 9.11.51 gives a smooth R, and \(U=\Psi+L+R\) satisfies
\[
\beta+dd^cU=c_{\eta}f_{\eta}\beta_0+\sum_j a_j\delta_{q_j}.
\]
The same disk-lifting/descent and non-pluripolar mass mechanism in 9.11.54/60 supplies the corresponding equation on the unibranch curve. This global step is **conditional on those printed normalization/descent and fixed-mass lemmas**, not a new verification of their entire prerequisites. The ordinary type holds exactly when \(L+R\) is bounded, i.e. eta>1. The compact-curve mass forces any solution in the type to have c=c_eta, and the difference of two lifted distributions with the same right-hand side is harmonic on the connected compact normalization, hence constant. When eta<=1 this contradicts bounded equivalence to Psi. The correction is o(log r) at q, so all monomial-integrability thresholds, including borderline nonintegrability, stay unchanged: the fixed logarithmic poles and this correction have the same multiplier ideals at each positive weight, as in the already printed Lemma 5.37.18. This is **not** ordinary-type equivalence.

**Proposed addition and dependents.** Optional short endpoint remark after Theorem 9.11.60: at gamma=2 an extra factor \((\log t)^{-\eta}\) restores the bounded ordinary type precisely for eta>1; explain the critical triple-log divergence at eta=1. This sharpens the integrability examples and informs Problem 24.11.1 but gives no general L1 theorem, no higher-dimensional Hermitian solution, and no proof of every resolution/descent prerequisite. Keep the established source history and all permanent tags.

## POME-CYCLE-FOURRULING-CARTIER-001 — complete integral relation among the four coordinate rulings

**Severity:** low. **Status:** verified conditional deduction (the algebraic calculation is complete relative to the printed analytic-cycle and smooth local-factoriality statements). It **extends**, rather than restates, existing POME-CYCLE-QUADRIC-CARTIER-LATTICE-001: that older ID treated only two of the four coordinate prime divisors.

**Pinned text:** docs/sections/analytic-cycles-and-cartier-cycles/index.html, main blob d4817ac64b1365bd967d42cd474fec169f992e28. Definition 20.6.2 (source demailly-complex-geometry:AFD209B1, permanent BE0C86A8DD65), lines 7–11; Proposition 20.6.3 (source 02B65FA7, permanent FD8966432506), lines 13–27; Proposition 20.6.4 (source BD1D45B4, permanent AA96C35C8290), lines 29–45; Example 20.6.5 (source E054C396, permanent 0C462992AB3A), lines 47–78.

**Exact result.** On the threefold node germ \(X=\{xy+zw=0\}\subset\mathbb C^4\), define four distinct irreducible Weil divisors
\[
A=(x,z),\quad B=(x,w),\quad C=(y,z),\quad D=(y,w).
\]
For arbitrary integers alpha,beta,gamma,delta, the germ
\[
T=\alpha A+\beta B+\gamma C+\delta D
\]
is Cartier at the origin **if and only if**
\[
\boxed{\alpha+\delta=\beta+\gamma}.
\]
When this holds, an explicit meromorphic local equation is
\[
\boxed{f=x^{\alpha-\gamma}z^{\gamma}w^{\delta}},
\]
allowing negative exponents. Thus the subgroup of the local Weil/Cartier class quotient generated by these four rulings is infinite cyclic; their classes obey \([B]=[C]=-[A]\) and \([D]=[A]\). This last assertion concerns the subgroup *generated by these four divisors*, **not** a computation of the entire analytic local divisor class group.

**Proof of necessity.** Use the printed surjective rank-one parametrization
\[
F(a,b,c,d)=(ac,bd,ad,-bc).
\]
Its inverse image of the singular origin is \(\{a=b=0\}\cup\{c=d=0\}\), of codimension two. Everywhere else F is a submersion onto the smooth locus, and the generic reduced pullbacks of \(A,B,C,D\) are exactly the coordinate hypersurfaces \(a=0,c=0,d=0,b=0\), respectively. If the cycle T is Cartier, Definition/Proposition 20.6.4 gives a meromorphic germ f on X with \(\operatorname{div}(f)=T\). The pullback is a meromorphic germ on smooth \(\mathbb C^4\) having precisely those four coordinate divisorial orders; no additional prime hypersurface can hide in the codimension-two inverse image of the origin. Local smooth-factoriality, already proved using the internal Noetherian/local-prime-equation results in Example 20.6.5, gives
\[
f\circ F=a^\alpha c^\beta d^\gamma b^\delta u,\qquad u(0)\ne0
\]
with u holomorphic and invertible. For every \(s\in\mathbb C^*\), the gauge change
\((a,b,c,d)\mapsto(sa,sb,s^{-1}c,s^{-1}d)\) fixes F, but multiplies the monomial by \(s^{\alpha+\delta-\beta-\gamma}\). After cancelling this monomial, evaluation of the unit identity at the origin forces \(s^{\alpha+\delta-\beta-\gamma}=1\) for all s. The integer exponent is therefore zero.

**Proof of sufficiency and primitivity.** On the regular locus, with the local divisor conventions in Proposition 20.6.4,
\[
\operatorname{div}(x)=A+B,\quad
\operatorname{div}(z)=A+C,\quad
\operatorname{div}(w)=B+D,\quad
\operatorname{div}(y)=C+D.
\]
Consequently the above explicit f has coefficients
\((\alpha,\,\alpha-\gamma+\delta,\,\gamma,\,\delta)\), exactly T under the displayed relation. The valuation matrix with columns div(x),div(y),div(z),div(w) has rank 3 and primitive left null vector \((1,-1,-1,1)\). The three columns div(x),div(z),div(w) already span the full integer kernel: if alpha+delta=beta+gamma, T equals
\((\alpha-\gamma)\operatorname{div}(x)+\gamma\operatorname{div}(z)+\delta\operatorname{div}(w)\). Hence the quotient is Z with generator [A]; **no torsion** occurs in this four-ruling subgroup.

**Independent arithmetic check actually run:** SymPy computed rank 3, primitive left kernel (1,-1,-1,1), and four maximal 3x3 minors of the (x,z,w) column matrix \((-1,-1,1,1)\); four signed integer coefficient quadruples were reconstructed exactly using \(x^{\alpha-\gamma}z^\gamma w^\delta\). This checks the displayed lattice arithmetic only; it is neither a project build nor formal mathematical verification.

**Proposed addition and dependents.** An optional four-ruling table after Example 20.6.5 makes the exact Cartier obstruction and its primitive (non-Q-Cartier) class explicit, preserving the existing two-ruling audit ID, original statement and historical attribution. The directly affected reading contexts are Proposition 20.6.4 and divisorial local computations in section 20.7. The general sheaf axioms of Proposition 20.6.3, normality of arbitrary singularities, and the full analytic class group were not re-certified.

## Precise coverage and remaining boundaries

New proof/model steps checked: §9.11.59–60's local radial Laplacian, zero-atom flux, global smooth-correction construction **conditionally**, and explicit singularity-type quantifiers against Problem §24.11.1; independently §20.6.2–5's four-coordinate pullback and principal divisor lattice. Previous §9.11.60 Dini and §20.6.5 two-ruling findings were read solely to avoid duplication, not entered as new accomplishments. **25 chapters, 747 current ToC sections, zero complete mathematical-section certifications**. No project tests, build, CI, formal verification, source/registry/permanent-tag modifications, main update, or website publication. All historical confirmed errors, proof gaps, unresolved external inputs, and user-deferred work retain their original statuses.
