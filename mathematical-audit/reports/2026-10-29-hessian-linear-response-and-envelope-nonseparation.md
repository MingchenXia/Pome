# Parametric complex-Hessian response and continuum-sized nonseparation of ordinary types — 2026-10-29

## Provenance, exact scope, and excluded work

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. The preceding audit reviewed a different set of propositions; this is a direct new reading of the **nonexcluded** statements and proofs of §§8.8.1–3, followed by an **incremental** independent stress test of §18.10.1 (already sampled in an earlier audit). §8.1 retains its global assumptions: X is compact, connected and complex, the background omega is positive Hermitian, and **2 <= m < n**. We do not extend these Chapter 8 results to m=1 or m=n. No section's entire dependency chain, nor an entire chapter, is certified.

**Relevant source files:** 
- <code>docs/sections/complex-hessian-equations/index.html</code>, main blob <code>5331b937ccdaba51f1ec006d5e72dc84f7addfbf</code>, physical line 7 (chapter assumptions).
- <code>docs/sections/complex-hessian-equations--continuous-equations-and-regularity/index.html</code>, main blob <code>62cace2a2bdec93860bf4b5ba9cb4653b4ed2b50</code>, lines 10–22 (Prop. 8.8.1, source label <code>non-kahler-pluripotential-theory:3F168071</code>, permanent tag <code>5D1E62F09217</code>); lines 29–57 (Thm. 8.8.2, source label <code>non-kahler-pluripotential-theory:C1C0E328</code>, tag <code>3B8FDE2FF95D</code>); lines 64–92 (Thm. 8.8.3, source label <code>non-kahler-pluripotential-theory:8B2683EB</code>, tag <code>76376AD88152</code>).
- <code>docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--separation-and-mass/index.html</code>, main blob <code>8044189fa6f5eb3fb475e0712dd600adea39e98a</code>, lines 10–22 (Prop. 18.10.1, source label <code>non-kahler-pluripotential-theory:928A1A8E</code>, permanent tag <code>3B87EFC632CF</code>). Its topology is defined in <code>docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types/index.html</code>, main blob <code>c1b46f98d8d9354355e5b3968e4b3947463b6edf</code>, lines 13–19, 45–79.

**Exclusion:** We did not reopen Demailly approximation/regularization, its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss proof-completion programme, nor inspect §18.9's dyadic analytic approximation proof. Previously filed excluded findings remain **deferred-by-user**, not resolved or certified. Smooth implicit differentiation of an already smooth elliptic equation in §8.8 is not a reconstruction of that excluded programme.

## POME-HESSIAN-SMOOTH-LINEAR-RESPONSE-001

**Severity:** low. **Status:** verified conditional deduction; **printed Theorem 8.8.3 is correct as read**. This is an additional smooth-parameter response formula, conditional on the theorem's existence/regularity and standard compact elliptic Fredholm facts already used in Lemma 8.6.1. No false printed theorem or fully certified global PDE proof is alleged.

**Hypotheses.** Let s vary in an open real interval I and let \(f_s(x,t)\) be jointly smooth in \((s,x,t)\) on a neighborhood of \(I\times X\times[A,B]\). Assume the **same fixed constants** \(A<B\), \(\kappa>0\), and \(L<\infty\) work for all \(s\) in a neighborhood of a chosen \(s_0\):
\[
f_s(x,A)\leq0\leq f_s(x,B),\qquad
\kappa\leq\partial_t f_s(x,t)\leq L
\quad(A\leq t\leq B).
\]
Let \(w_s\) denote the unique smooth strictly admissible solution furnished by Theorem 8.8.3:
\[
H_m(w_s):=(\omega+dd^c w_s)^m\wedge\omega^{n-m}
=e^{f_s(x,w_s)}\,\omega^n.
\]

**Direct audit of the printed argument.** Proposition 8.8.1 gives the \(a^{-1}\)-Lipschitz dependence of a proper exponential Hessian equation on its prescribed continuous datum; its printed maximum-point proof has the correct direction. In Theorem 8.8.3, setting \(H_v=f_s(x,v)-av\) with \(a\geq L\), the barriers imply \(-aB\leq H_v\leq-aA\), and the map \(v\mapsto T_s(v)\) contracts by \(1-\kappa/a<1\). The fixed point satisfies the required equation. Theorem 8.8.2 and positivity of the right side make it smooth and strictly admissible. Those **exact steps** were directly checked, while the global a priori Hessian estimate, viscosity extension, and proof of the upstream smooth solvability lemma were only read as *conditional inputs*, not re-established.

**Independent new derivation.** At a fixed parameter \(s\), define the nonlinear map on \(C^{k+2,\alpha}(X)\) in a neighborhood of \(w_s\) inside the open admissible cone,
\[
\mathscr F(s,u)
=\log\!\left(\frac{H_m(u)}{\omega^n}\right)-f_s(x,u).
\]
Its derivative in the potential is
\[
(D_u\mathscr F)_{(s,w_s)}\xi
=L_{w_s}\xi-q_s\xi,\qquad
q_s(x)=\partial_t f_s(x,w_s(x))\geq\kappa,
\]
where, with \(\omega_{w_s}=\omega+dd^c w_s\),
\[
L_{w_s}\xi
=\frac{m\,dd^c\xi\wedge\omega_{w_s}^{m-1}
                  \wedge\omega^{n-m}}{H_m(w_s)}.
\]
Strict admissibility makes the principal coefficients of \(L_{w_s}\) positive definite. The operator \(L_{w_s}-q_s\) has trivial kernel by the maximum principle; standard elliptic Fredholm theory on compact X (the same type of input explicitly used in §8.6.1, lines 23–29 of the entry tagged <code>8B310CC2C1A1</code>) yields invertibility between the stated Hölder spaces. The implicit-function theorem now supplies a smooth local solution branch through \(w_{s_0}\). The constant-barrier maximum argument places each nearby solution in \([A,B]\); uniqueness in Theorem 8.8.3 identifies it with the specified \(w_s\). Thus the solutions are \(C^1\) in \(s\), indeed smoothly dependent locally in Hölder spaces.

Differentiating the equation **with the background form fixed** gives the response identity
\[
\boxed{(L_{w_s}-q_s)\dot w_s
       =\partial_s f_s(x,w_s).}
\]
At a positive maximum of \(\dot w_s\), \(L_{w_s}\dot w_s\leq0\); at a negative minimum, \(L_{w_s}\dot w_s\geq0\). Applying the two inequalities with \(q_s\geq\kappa\) proves
\[
\boxed{\|\dot w_s\|_{L^\infty(X)}
 \leq\frac{\|\partial_s f_s(\cdot,w_s)\|_\infty}{\kappa}.}
\]
Moreover, if \(\partial_s f_s\geq0\), then \(\dot w_s\leq0\). This order reversal matches the direction of the printed maximum principle and does not depend on Kähler closedness. Sharpness is obtained by \(f_s(x,t)=t+s c\), with \(c\) a real constant and common barriers chosen to contain \(w_s=-sc\) for the relevant parameter interval. Since \(H_m(-sc)=\omega^n\), the response is \(\dot w_s=-c\) and the bound is attained with \(\kappa=1\).

**Not a duplicate:** The earlier ID <code>POME-HESS-ONESIDED-MEASURE-001</code> addressed zero-order comparisons with *measure residual inequalities* for bounded solutions in §8.13. The present finding is the **derivative/operator identity, smooth parameter dependence, and sign** for the §8.8.3 solution map. The \(1/\kappa\) constant by itself is not counted as a new discovery or as an independent verification of §8.13. Recommended optional corollary after §8.8.3, preserving its permanent tag and history. Dependents include perturbative Hessian equations, data paths, and comparison of smooth intermediate-degree solutions. The entire a priori PDE chain remains conditional.

## POME-ORDINARY-TYPE-UNCOUTABLE-FIBER-001

**Severity:** low. **Status:** verified conditional deduction; **printed Proposition 18.10.1 is correct**. This proves a stronger explicit statement than its single non-\(T_0\) pair. Section 18.10 had already received selected attention, so this is **incremental** coverage, not a newly opened section or a new confirmed topology defect.

**Hypotheses and explicit family.** Retain the compact Hermitian-background ordinary types \(\mathfrak S(X,\omega)=\mathrm{PSH}(X,\omega)/\sim\), where equivalence means bounded difference (§18.8, lines 13–19). Use the small cutoff logarithmic pole \(w\leq0\) at a point \(p\), with \(\omega+dd^cw\geq0\), constructed in the printed proof of §18.10.1. For every real \(0<\alpha<1\), set
\[
\chi_\alpha(s)=1-(1-s)^\alpha,\qquad
u_\alpha=\chi_\alpha(w),\qquad s\leq0.
\]
The derivatives are
\[
\chi_\alpha'(s)=\alpha(1-s)^{\alpha-1}\in(0,\alpha],
\qquad
\chi_\alpha''(s)=\alpha(1-\alpha)(1-s)^{\alpha-2}\geq0.
\]
Consequently the ordinary convex-increasing composition rule yields
\[
\omega+dd^cu_\alpha
=(1-\chi_\alpha'(w))\omega
 +\chi_\alpha'(w)(\omega+dd^cw)
 +\chi_\alpha''(w)\frac{i}{2\pi}\partial w\wedge\bar\partial w
\geq0
\]
away from the pole. The inequality extends across the isolated pole in the usual psh/distributional sense, so \(u_\alpha\in\mathrm{PSH}(X,\omega)\). This is elementary convex composition, not any Demailly approximation programme.

Near \(p\), \(w(z)=c\log|z|^2+O(1)\) for some \(c>0\), and hence
\[
u_\alpha(z)=-\bigl(c|\log|z|^2|\bigr)^\alpha(1+o(1)).
\]
For every \(t>0\), \(e^{-tu_\alpha}\) is locally integrable: for each small \(\varepsilon>0\), \(t\,T^\alpha=o(T)\) as \(T=-\log|z|^2\to\infty\), so \(e^{-tu_\alpha}\leq C_\varepsilon |z|^{-2\varepsilon}\), integrable after choosing \(\varepsilon<n\). Thus \(\mathcal I(tu_\alpha)=\mathcal O_X\) at every positive weight, and the ideal envelope is zero.

For any \(0<\delta\leq1\), the function
\[
\delta s-\chi_\alpha(s)=\delta s-1+(1-s)^\alpha
\]
is bounded above on \(s\leq0\), as it tends to \(-\infty\) for \(s\to-\infty\). Therefore \(\delta w\preceq u_\alpha\), and \(\delta w\leq0\) is a valid \(\omega\)-psh competitor for \(P_\omega[u_\alpha]\). Letting \(\delta\downarrow0\) on \(X\setminus\{p\}\) and using the upper-semicontinuous envelope gives
\[
\boxed{P_\omega[u_\alpha]=0
       =P_\omega[u_\alpha]_{\mathcal I}
       \qquad\text{for every }0<\alpha<1.}
\]
For \(0<\alpha<\beta<1\), \(u_\beta-u_\alpha\to-\infty\) at \(p\), so their difference is **not bounded**: \([u_\alpha]\ne[u_\beta]\) in the ordinary class space. But Proposition 18.10.1, or directly all the uniformity's coordinates and controlled ideal relations in Proposition 18.8.4 (lines 45–79), give **identical neighborhoods** to all \([u_\alpha]\) and \([0]\). The non-\(T_0\) fiber of the zero ordinary envelope therefore has at least continuum cardinality:
\[
\boxed{\left|\{[u]:P_\omega[u]=0\}\right|
       \ \geq\ |\,(0,1)\,|.}
\]
This does not claim an exact cardinality for the whole type space or a new failure beyond the published non-\(T_0\) conclusion.

**Recommended action/dependents.** Optional explicit one-parameter strengthening of the printed §18.10.1 example, carefully marked as *different ordinary types with the same topological indistinguishability class*, not a failure of the proposition. Useful for quotient constructions, analytic-closure interpretations, and avoiding incorrect claims of uniqueness of a representative from its envelope. Historical non-\(T_0\) and polar-curvature findings are not duplicated or reclassified; §18.9's excluded dyadic construction was not inspected.

## Exact coverage and outstanding boundaries

**New direct selected nonexcluded proof-level coverage:** §8.8.1, §8.8.2 and §8.8.3: verified the logic of the uniform \(a^{-1}\) comparison, contraction barriers and fixed point, and derived the distinct linear-response identity. The Hessian \(C^2\) estimate, smooth approximation proof §8.6.2, viscosity extension §8.5.4, and full global solvability chain remain *unverified conditional inputs*; no entire §8.8 certification.

**Incremental selected coverage:** §18.10.1: independently checked convex composition, all positive multiplier weights, ordinary-envelope competitors, and distinct classes for a continuum family. §18.8.1–4 was read only to fix the precise topology and equivalence relation; §18.4.4 is a cited input and was not recertified. The section's separate mass comparison (§18.10, lines 26–35) was *not reaudited*. No entire §18.10 certification.

**Excluded:** The Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss completion programme remains **deferred-by-user**, not resolved; no attempt was made to revisit it through its prerequisites. No main/source/reading body, registry, canonicalization, tags, website, publication, CI, build, or formalization action. Retain the existing actual table of contents of **25 chapters and 747 numbered sections**; **zero complete sections or chapters certified**.

**Conclusion:** Two low-severity **verified conditional deductions**. No newly established false theorem, proof gap, genuine duplicate, or completed repair. Preserve all earlier statuses.
