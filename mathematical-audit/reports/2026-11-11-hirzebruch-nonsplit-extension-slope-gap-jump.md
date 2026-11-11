# Exact slope-gap jumping locus for nonsplit Hirzebruch extensions

**Finding:** POME-HIRZ-EXT-SLOPE-JUMP-001  
**Date:** 2026-11-11  
**Classification:** low / verified conditional deduction (the printed Proposition 11.14.1 remains correct; this is not a counterexample or a repair)  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Audit branch:** review/mathematical-audit

## Exact integrated anchors and provenance

- Main: docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--stable-extensions-approaching-the-split-comparison-bundle/index.html; blob SHA 03559e82ef17c97d04258775312d994ec217e376.
- Proposition 11.14.1: source label non-kahler-pluripotential-theory:D386B065, permanent tag A195B6162A49, physical lines 25–86. In particular, the extension space and dimension appear at lines 40–49, the three slopes at lines 52–55, the divisor analysis at lines 57–74, and the exceptional e=0 injection at lines 74–85.
- Main: docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--ample-comparison-quotients-on-hirzebruch-surfaces/index.html; blob SHA 6d836a2ed19f76c26311025602fb44a56713e390.
- Lemma 11.13.1: source label non-kahler-pluripotential-theory:9A9AA541, permanent tag 8FE2AABC7334, physical lines 26–51; ruling, intersection conventions, and effective cone in physical lines 12–38.
- Proposition 11.14.3, source label non-kahler-pluripotential-theory:E4134CA1, permanent tag 7215288BDF53, physical lines 111–135: family degeneration context only; its deformation argument is not re-certified here.

## Statement of the additional exact result

Let X=F_e for an integer e>=0, with negative section S, ruling fiber f, and the exact line bundles and polarization of Proposition 11.14.1:

\[
L_1=\mathcal O_X(5S-f),\qquad
L_2=\mathcal O_X(-S+(12e+5)f),\qquad
P=4S+(12e+3)f.
\]

Put F=L_1\otimes L_2^{-1} and W=Ext^1_X(L_2,L_1)=H^1(X,F); its dimension is N=105e+35. For a nonzero extension class alpha, let V_alpha be the corresponding nonsplit rank-two vector bundle. Define its rank-one slope margin by

\[
\Delta_P(V_\alpha)=\mu_P(V_\alpha)-
\sup\{\mu_P(M):M\subset V_\alpha\text{ coherent, torsion-free, rank one}\}.
\]

For each a in the ruling base P^1, let s_a be a nonzero section of O_X(f) cutting out the fiber F_a=pi^{-1}(a), and define

\[
K_a=\ker\left(
H^1(X,F)\xrightarrow{\cdot s_a}H^1(X,F(f))
\right).
\]

Then the following statements are exact:

1. Each K_a has complex dimension seven; for distinct a,b one has K_a intersect K_b = {0}.
2. The set Z of projective nonsplit extension classes [alpha] in P(W) for which alpha belongs to at least one K_a is a closed irreducible algebraic subset of dimension **7**, hence of codimension **105e+27** in P(W).
3. For every nonzero alpha,

\[
\boxed{\quad
\Delta_P(V_\alpha)=
\begin{cases}
1,&[\alpha]\in Z,\\
3,&[\alpha]\notin Z.
\end{cases}
\quad}
\]

Thus a general nonsplit class has slope margin exactly 3, while there are special nonsplit classes with the **sharp universal** margin 1. The split bundle E_0=L_1\oplus L_2 instead has margin -3. These claims apply to **all** rank-one coherent subsheaves, not only subbundles with locally free quotient.

## Proof

**1. Reduction to line bundles and the divisor degree.**
As in the printed proposition, the double dual of a rank-one torsion-free subsheaf M is a line bundle and the inclusion M -> V extends across the finite set where M is not locally free. The extension preserves c_1 and therefore slope. Write m=mu_P(V)=40e+14. The printed intersection calculation gives mu_P(L_1)=m-3, mu_P(L_2)=m+3, S.P=8e+3 and f.P=4. The distinguished subbundle L_1 therefore proves Delta_P(V)<=3.

For any line subbundle M -> V, if the composite to L_2 is zero then mu_P(M)<=m-3. Otherwise the composite has effective zero divisor D and M=L_2(-D), so mu_P(M)=m+3-D.P. The case D=0 would split the nonzero extension and is impossible. Since every effective D has class aS+bf with nonnegative integers a,b, a possible slope strictly greater than m-3 requires D.P<6. For e>=1 the only possibility is D=f (degree 4); for e=0 the two possibilities are D=f (degree 4) and D=S (degree 3). The latter is impossible for every nonsplit extension, because the map H^1(O(6S-6f)) -> H^1(O(7S-6f)) induced by any nonzero section of O(S) is injective by the first-factor H^0(P^1,O(6)) -> H^0(P^1,O(7)) injection and Kunneth, exactly as checked in the printed proof. Thus there is **no** rank-one slope strictly between m-3 and m-1 and no slope at least m; the only possible improvement over the L_1 bound is a lift of L_2(-f), which has slope m-1.

**2. Lifting criterion.**
The nonzero section s_a gives the inclusion L_2(-f) -> L_2 with quotient on the ruling fiber F_a. This inclusion lifts to V_alpha if and only if the pullback of the extension class alpha to Ext^1(L_2(-f),L_1)=H^1(F(f)) is zero. This is precisely alpha in K_a. Since the composite to L_2 is injective as a map of sheaves, every lift is injective. Therefore the slope margin is one exactly on the union of the nonzero K_a; if no such lift exists, the L_1 subbundle achieves the maximal slope m-3 and the margin is three.

**3. Dimension of every K_a.**
Put d_i=12e+6+ie for 0<=i<=6, so all d_i>=6. The verified formula in Lemma 11.13.1 gives

\[
\pi_*F=\bigoplus_{i=0}^6\mathcal O_{\mathbb P^1}(-d_i),
\quad R^1\pi_*F=0,
\quad
\pi_*F(f)=\bigoplus_{i=0}^6\mathcal O_{\mathbb P^1}(-d_i+1).
\]

In particular H^0(X,F(f))=0. The exact sequence 0 -> F --s_a--> F(f) -> F(f)|_{F_a} -> 0 and F(f)|_{F_a}=O_{P^1}(6) give

\[
K_a\simeq H^0(F_a,\mathcal O_{F_a}(6)),\qquad \dim K_a=7.
\]

Equivalently, on each of the seven direct summands, multiplication by s_a induces a map H^1(P^1,O(-d_i)) -> H^1(P^1,O(-d_i+1)) with one-dimensional kernel.

**4. Distinct ruling fibers and the jumping locus.**
By Serre duality on the base, H^1(P^1,O(-d_i)) is dual to H^0(P^1,O(d_i-2)). The one-dimensional kernel just described is the line spanned by point evaluation at a, because the dual multiplication map has image consisting of sections divisible by s_a. Evaluations at distinct a,b are linearly independent since d_i-2>=4. The seven-summand decomposition therefore gives K_a intersect K_b={0} for a!=b.

The K_a vary algebraically as a rank-seven subbundle K of the constant vector bundle W tensor O_{P^1}. Its projective bundle P(K) is irreducible projective of dimension 1+6=7. The natural morphism P(K) -> P(W) is proper, and distinct fibers have disjoint images, so its fibers are zero-dimensional. Its image Z is therefore closed, irreducible and of dimension seven. Since dim P(W)=N-1=105e+34, its codimension is 105e+27.

**5. Split endpoint.**
For alpha=0, E_0=L_1 direct-sum L_2. Every rank-one subsheaf maps nontrivially to at least one summand and so has slope <=mu_P(L_2)=m+3; the summand L_2 attains equality. Thus Delta_P(E_0)=m-(m+3)=-3. Combined with the nonsplit dichotomy, the degeneration E_t in Proposition 11.14.3 has a genuine jump in maximum rank-one slope at t=0, even though its Dolbeault operators converge smoothly.

## Scope, severity, correction, dependents

- **Status:** verified conditional deduction. The established integrated Proposition 11.14.1 is *not* false; its proof of stability is strengthened by the exact optimization and a closed jumping-locus calculation. There is no source/body correction required.
- **Internal inputs:** Lemma 11.13.1 (ruling direct images and effective cone), Proposition 11.14.1 (basic stable-extension geometry and e=0 no-lift case), and the standard long exact sequence and Serre duality on P^1. These are mathematically justified in the displayed calculations; this audit does **not** independently certify every upstream theorem in the book.
- **Dependents:** Proposition 11.14.3 and Theorem 11.15.5 can use the exact slope-margin distinction if a quantitative extension stability estimate is desired. The latter's separate Walter prioritary-stack irreducibility input remains an **external dependency** and is not resolved here.
- **Proposed addition (not applied):** optional remark after Proposition 11.14.1 recording the slope-margin dichotomy and the codimension-105e+27 exceptional projective extension locus.
- **Exact coverage:** new proof of the classification for Proposition 11.14.1 and Lemma 11.13.1; Proposition 11.14.3 and Theorem 11.15.5 are context only. Both numbered sections were previously selected for mathematical review: **0 first section visits, 0 entire-section certifications**. Current main inventory: **25 chapters, 747 numbered sections**.
- **User-deferred scope:** Demailly approximation/regularization and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion program remain **deferred-by-user**, neither reopened nor certified.
- **Operations:** audit Markdown only, review/mathematical-audit; no edits to main, sources, registry, permanent tags, CI, build or publication.
