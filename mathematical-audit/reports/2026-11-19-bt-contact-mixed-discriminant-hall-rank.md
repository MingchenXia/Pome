# Mixed Bedford–Taylor contact density: exact Hall–Rado rank criterion

**2026-11-19. Baseline main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Integrated file:** \`docs/sections/bedford-taylor-products-and-local-capacity--bounded-complex-hessians-and-contact-sets/index.html\`, blob \`e2697dc465a2b639120974188eaeb6c446ed8071\`. Directly reviewed **all mathematical lines 7–138** (section permanent tag \`FB1768F3514F\`): Lemma 7.13.1, \`foundations-of-pluripotential-theory:B80A5A22\` / \`8736729F21D9\` lines 14–43; Lemma 7.13.2, \`0CFF4F56/D57C89462C1B\` lines 48–83; Proposition 7.13.3, \`AF82FB9E/C006456D2AFC\` lines 91–101; Proposition 7.13.4, \`D9CC767A/1466731348C1\` lines 109–134; manifold application line 138.

**Finding POME-BT-CONTACT-MIXED-DISCRIMINANT-HALL-RANK-001: low / verified conditional deduction.** This is a new *exact support/positivity test* for the already printed mixed-density contact formula, not a counterexample or proof repair. The 2026-11-10 \`POME-BT-CRITICAL-LN-HESSIAN-CONTACT-001\` is a different, previously recorded *integrability-hypothesis* extension; it is not repeated here.

## Statement

Let \(\Omega\subset\mathbb C^n\) be open. For \(1\le j\le n\), let \(u_j\) be continuous plurisubharmonic with locally essentially bounded complex Hessian \(A_j=(\partial_a\bar\partial_b u_j)\). Let real \(v_j\in W^{2,1}_{\mathrm{loc}}(\Omega)\) have weak complex Hessian \(B_j\), and put \(E=\bigcap_j\{u_j=v_j\}\) with Borel representatives. By Proposition 7.13.3, \(B_j=A_j\succeq0\) **almost everywhere on \(E\)**. Proposition 7.13.4 states

\[
\mathbf1_E\,dd^cu_1\wedge\cdots\wedge dd^cu_n
=\frac{n!}{\pi^n}\mathbf1_ED(B_1,\ldots,B_n)\,dV_{2n}.
\]

The right side has **strictly positive density at almost every \(z\in E\) if and only if**

\[
\boxed{\operatorname{rank}\left(\sum_{j\in I}B_j(z)\right)\ge |I|
\quad\text{for every nonempty }I\subset\{1,\ldots,n\}.}\tag{H}
\]

If (H) fails a.e. on a Borel subset \(F\subseteq E\), the mixed product gives \(F\) zero mass. The result is valid for arbitrary \(W^{2,1}\) obstacles because positivity is asserted only on \(E\), not outside it. It is unaffected by modifying the obstacle representatives on null sets.

## Independent finite-dimensional proof

For each positive-semidefinite Hermitian \(B_j\), choose a spectral Gram decomposition
\(B_j=\sum_{a=1}^{r_j}v_{ja}v_{ja}^{*}\), with the \(v_{ja}\) spanning \(V_j=\operatorname{Im}B_j\). Cauchy–Binet applied to the determinant polynomial \(\det(\sum_jt_jB_j)\) shows that its \(t_1\cdots t_n\) coefficient equals
\(\sum_{a_1,\dots,a_n}|\det(v_{1a_1},\dots,v_{na_n})|^2\).
Under the **printed** convention, the same coefficient equals \(n!D(B_1,\dots,B_n)\). Therefore

\[
\boxed{D(B_1,\ldots,B_n)=\frac1{n!}\sum_{a_1,\ldots,a_n}
|\det(v_{1a_1},\ldots,v_{na_n})|^2.}\tag{G}
\]

In particular \(D>0\) precisely if some linearly independent vectors can be selected, one from each \(V_j\). The forward implication follows from a nonzero summand of (G). Conversely, expand the determinant of independent selected vectors in the spectral spanning families; multilinearity produces a nonzero determinant summand of (G).

For completeness, prove the corresponding **Hall–Rado subspace criterion** without any external combinatorial dependency. For \(m\) subspaces \(V_1,\ldots,V_m\), independent representatives exist iff \(\dim(\sum_{i\in I}V_i)\ge|I|\) for every nonempty \(I\). Necessity is immediate. Induct on \(m\). If some proper nonempty \(I\) is tight, let \(W=\sum_{i\in I}V_i\), so \(\dim W=|I|\). Inductively select independent representatives for \(I\); for every \(J\subseteq I^c\), the images of \(V_j\) in the quotient by \(W\) span a space of dimension
\(\dim(W+\sum_{j\in J}V_j)-\dim W\ge |I|+|J|-|I|=|J|\).
Select representatives in the quotient by induction and lift them. If there is no such tight proper \(I\), every nonempty proper \(I\) has \(\dim\sum_{i\in I}V_i\ge |I|+1\). Pick any nonzero \(w_m\in V_m\). In the quotient by \(\mathbb Cw_m\), every nonempty \(J\subseteq\{1,\ldots,m-1\}\) has image dimension at least \(|J|\), since taking a one-dimensional quotient loses at most one dimension. Apply induction to choose independent representatives in the quotient and lift them; together with \(w_m\) they are independent. The case \(m=1\) is immediate. This proves (H), with no assumption that individual \(B_j\) have full rank.

The coincidence and density equalities from Proposition 7.13.4 then prove the stated measure result. No net interchange or unproved convergence of mixed determinants is used.

## Opposite sharp examples and normalization

On a polydisc in \(\mathbb C^2\), take \(u_1=v_1=|z_1|^2\), \(u_2=v_2=|z_2|^2\). Both Hessian matrices have rank **one**, but their images span \(\mathbb C^2\), \(D=1/2\), and
\(dd^cu_1\wedge dd^cu_2=\pi^{-2}dV_4>0\).
In contrast, \(u_1=v_1=u_2=v_2=|z_1|^2\) violates (H) for \(I=\{1,2\}\) and gives a zero mixed product. Thus “all individual Hessians are singular” is **not** a sufficient zero-mass criterion. The normalization is \(dd^c=(i/2\pi)\partial\bar\partial\); the \(n!\) in the printed formula is essential.

## Direct printed-proof checks

1. **7.13.1, lines 20–42:** the bounded-derivative \(W^{1,1}\) chain rule follows by mollification, \(L^1\) derivative convergence and dominated convergence. The shrinking cutoff \(\Phi_\varepsilon\) proves that the weak gradient vanishes a.e. on a measurable zero set; applying this to each first derivative gives second-order coincidence modulo a finite union of null sets.
2. **7.13.2, lines 54–82:** local integration by parts first gives \(L^2\) gradient Cauchy convergence. For compactly supported smooth \(v\), the exact identity \(\sum_{a,b}\|\partial_{ab}v\|_2^2=\|\Delta v\|_2^2\) gives second derivatives of cut-off mollifications. This is a **local** \(W^{2,2}\) conclusion, not a global boundary regularity claim.
3. **7.13.3, lines 91–101:** apply the coincidence lemma to \(f-g\in W^{2,1}_{loc}\). Equality holds **almost everywhere on** the contact set, not pointwise at each contact.
4. **7.13.4, lines 123–133:** coefficient comparison gives the exact \(n!D\) factor; bounded Hessian entries and local \(L^1\) convergence of their mollifications yield local \(L^1\) convergence of their determinant polynomials, while Bedford–Taylor products converge weakly. Replacing matrices on \(E\) uses the preceding contact lemma. No total-variation convergence of arbitrary approximants is asserted.
5. **Manifold clause, line 138:** apply the test to the **locally psh representatives after adding smooth local potentials**, not to arbitrary nonclosed background forms.

No new **confirmed printed error, independent proof gap, or genuine duplicate** was found. The cited Sobolev/mollification/Bedford–Taylor upstream results were inspected only as dependency interfaces, and are not fully transitively certified.

**Proposed correction/application:** optionally add (G)–(H) as a separate corollary after Proposition 7.13.4 (not a repair). The affected dependents are §16.10 contact measures and any mixed-envelope arguments claiming strictly positive contact density: those arguments must check the subset rank condition. No source text, registry, tags, canonicalization or production website was changed.

**Coverage:** +1 entire direct section reading (§7.13), +0 complete transitive dependency chains; prior partial audits retained, no first-visit claim. Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion are **deferred-by-user**, not resolved/certified. No tests, builds, CI or browser checks were run.
