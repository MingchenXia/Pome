# Ordered logarithmic data: two-slope sharp stability in the Hermitian Hessian equation

**Date:** 2026-11-15  
**Finding:** **POME-HESS-ORDERED-LOGDATA-TWO-SLOPE-001**  
**Severity/status:** **low / verified conditional deduction**. The printed Proposition 8.13.12 and Theorem 8.13.10 are **not** disproved; the following is a more informative *conditional* corollary, not an applied production repair or certification of their analytic prerequisites.  
**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (not modified).

## Integrated anchors, hypotheses and dependence

- \`docs/sections/complex-hessian-equations--hessian-mass-and-global-comparison/index.html\`, main blob \`580d3bc2b10ebd01d880b2a31fc6930436570aac\` (physical lines).
- Theorem **8.13.10** (lines **281–303**), source \`non-kahler-pluripotential-theory:98425BFC\`, permanent tag \`A532C77D7D0C\`: if \(\mathbf1_{\{a<b\}}H_m(a)\le c\mathbf1_{\{a<b\}}H_m(b)\) with \(c<1\), then \(a\ge b\) everywhere. This is explicitly **assumed** in the new corollary, not transitively recertified.
- Proposition **8.13.12** (lines **330–353**), source \`non-kahler-pluripotential-theory:3FE616D3\`, permanent tag \`FBE7E9A6BE5E\`: \(L^\infty(\nu)\)-stability of bounded admissible solutions under the lower slope bound \(\partial_t f\ge\kappa>0\). Its proof compares the original values in \([A,B]\), not the shifted comparison potential.
- Corollary **8.13.13** (lines **355–365**), source \`non-kahler-pluripotential-theory:126D8F14\`, permanent tag \`5460C4009B01\`: downstream smooth/bounded uniqueness, conditional on PDE existence and smooth-to-bounded identification.
- Global scope: compact complex \(n\)-fold with a smooth positive Hermitian \(\omega\), \(2\le m<n\); \(H_m(w)=(\omega+dd^cw)^m\wedge\omega^{n-m}\). The complete bounded Hessian theory, canonical representatives, and non-Kähler domination theorem remain conditional internal dependencies. There is **no** engagement with the user-excluded Demailly regularization/Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programme.

## New order-interval assertion

Fix \(0<\kappa\le\Lambda<\infty\), and let \(f\) be smooth near \(X\times[A,B]\) with
\[
\kappa\le\partial_t f(x,t)\le\Lambda.
\]
Let \(u,v\) be bounded admissible potentials with actual canonical values in \([A,B]\), satisfying for one fixed finite positive Radon measure \(\nu\)
\[
H_m(u)=e^{f(x,u)+h_1}\nu,\qquad
H_m(v)=e^{f(x,v)+h_2}\nu.
\]
Assume the bounded Borel data obey
\[
0\le a\le h_1-h_2\le b<\infty\quad\nu\text{-a.e.}
\]
Then **pointwise on all of \(X\)**,
\[
\boxed{\qquad v-\frac b\kappa\ \le u\ \le v-\frac a\Lambda.\qquad} \tag{1}
\]
In particular, \(h_1\ge h_2\) \(\nu\)-a.e. implies the **order-reversing data comparison** \(u\le v\), even when the data are merely Borel and \(\nu\) is singular. The result is stronger than the unsigned stability estimate of Proposition 8.13.12: it separates the lower and upper slopes and preserves the sign of the perturbation. It does not assert existence for arbitrary \(\nu,h_i\).

### Complete conditional proof of (1)

The Hessian measure is invariant under adding constants. All identities below are identities of measures restricted to Borel sets; no absolutely continuous density of \(\nu\), open-set assumption or interchange of singular limits is used.

**Lower bound.** Fix \(\delta>0\), set \(w=v-b/\kappa-\delta\), and \(E=\{u<w\}\). On \(E\), the *actual* values \(u,v\) belong to \([A,B]\) and
\[
f(x,v)-f(x,u)\ge\kappa(v-u) >b+\kappa\delta.
\]
The upper bound \(h_1-h_2\le b\), valid \(\nu\)-almost everywhere, gives on \(E\)
\[
H_m(u)=e^{f(x,u)+h_1-h_2-f(x,v)}H_m(v)
\le e^{-\kappa\delta}H_m(w).
\]
Theorem 8.13.10 applied to \(u,w\) gives \(u\ge w\) everywhere. Let \(\delta\downarrow0\).

**Upper bound when \(a>0\).** Choose \(0<\delta<a/\Lambda\), put \(w=v-a/\Lambda+\delta\) and \(E=\{w<u\}\). If \(u<v\) on \(E\), then
\[
f(x,u)-f(x,v)\ge-\Lambda(v-u)>-a+\Lambda\delta.
\]
If \(u\ge v\), the left side is nonnegative, which is also strictly greater than \(-a+\Lambda\delta\). Thus everywhere on \(E\),
\[
f(x,u)-f(x,v)+h_1-h_2\ge\Lambda\delta
\quad \nu\text{-a.e.},
\]
and
\[
H_m(w)=H_m(v)\le e^{-\Lambda\delta}H_m(u)
\quad\text{on }E.
\]
Apply Theorem 8.13.10 to \(w,u\), obtaining \(w\ge u\) everywhere; let \(\delta\downarrow0\). For \(a=0\), use \(w=v+\delta\) and \(\partial_t f\ge\kappa\) to get the same conclusion with \(e^{-\kappa\delta}\).

The shifted comparison potentials \(w\) need **not** remain in \([A,B]\): only the originally prescribed \(u,v\) are evaluated inside \(f\), exactly as required in printed Proposition 8.13.12. This is essential to avoid silently strengthening its hypotheses.

### Both slope coefficients are independently optimal

Take any compact Hermitian \(X\) in the allowed dimension range, set \(\nu=\omega^n\), \(v=0\), \(h_2=0\), and choose a constant \(d>0\) with \([-d/\kappa,0]\subset[A,B]\). All constant potentials have \(H_m(\mathrm{constant})=\omega^n\).

- For \(f(x,t)=\kappa t\), \(h_1=d\) and \(u=-d/\kappa\), the lower bound \(u=v-b/\kappa\) is attained with \(a=b=d\), even if an available upper derivative bound \(\Lambda>\kappa\) is specified.
- For \(f(x,t)=\Lambda t\), \(h_1=d\) and \(u=-d/\Lambda\), the upper bound \(u=v-a/\Lambda\) is attained with \(a=b=d\), even if a smaller valid lower derivative bound \(\kappa<\Lambda\) is specified.

Both are exact solutions, not approximations. Therefore the factors \(1/\kappa\) and \(1/\Lambda\) in their respective sides of (1) cannot be uniformly improved under these hypotheses.

## Disposition and affected dependents

The new deduction can be added as an optional corollary after Proposition 8.13.12, with the **same** Hermitian normalization, the two derivative bounds, and the condition \(0\le a\le h_1-h_2\le b\) stated explicitly. Corollary 8.13.13 and other proper-equation uniqueness/stability uses may exploit its one-sided ordering. The existing Theorem 8.13.10 remains a conditional analytic input; no printed statement is false and no source, registry, canonicalization, permanent-tag or historical-attribution alteration is proposed. Distinct from \`POME-HESS-ONESIDED-MEASURE-001\` (2026-10-21; measure-residual bounds) and \`POME-HESS-TORSION-RECURRENCE-RESOLVENT-001\` (2026-11-12; torsion recursion): the present argument concerns **ordered logarithmic forcing data** and the two endpoint slopes of \(f\).

**Exact new coverage:** direct reread of the integrated §8.13.10 domination conclusion and its proof (lines 281–303); full reread of Proposition 8.13.12 hypotheses and proof (lines 330–353); Corollary 8.13.13 (lines 355–365) as downstream context. All were in the previously partly reviewed §8.13, so **+0 first-visited numbered sections / +0 complete-section certifications**. Current ToC remains **25 chapters / 747 numbered sections**; all other analytic dependencies and other sections are unverified unless individually recorded. The excluded programme remains **deferred-by-user**, never resolved or certified. No project build, tests, CI or website publication were performed.
