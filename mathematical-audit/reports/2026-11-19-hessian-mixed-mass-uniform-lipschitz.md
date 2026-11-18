# Uniform Lipschitz continuity of bounded Hermitian mixed Hessian total mass

**Date:** 2026-11-19  
**Finding ID:** POME-HESS-MIXED-MASS-UNIFORM-LIPSCHITZ-001  
**Classification:** low / **verified conditional deduction**. This is an additional consequence of the printed bounded-current calculus, not an error in the existing theorems and not a complete independent certification of their upstream proofs.  
**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`  
**Scope:** §8.12.4 and §§8.13.1, 8.13.4–5, with the precise auxiliary bounds in §§8.9 and 8.11. The other results in §§8.12–8.13 were read for compatibility, but this report does **not** claim full direct-section certification.

## Statement

Retain the standing hypotheses of Chapter 8: \(X\) is a compact connected complex \(n\)-fold with a fixed smooth positive Hermitian \((1,1)\)-form \(\omega\), and \(2\le m<n\). The potentials below are bounded \(\omega\)-\(m\)-admissible functions with their canonical upper-semicontinuous pointwise representatives.

For a list \(\mathbf t=(t_1,\ldots,t_m)\), let
\[
\mathcal M_m(\mathbf t)=\int_X Q_m(t_1,\ldots,t_m)
\]
be the mixed Hessian total mass in §8.13.1. Given any two lists \(\mathbf t,\mathbf s\) satisfying
\[
\max_i\{\|t_i\|_{L^\infty(X)},\|s_i\|_{L^\infty(X)}\}\le B,
\qquad B\ge0,
\]
there exists a constant \(C=C(X,\omega,m,n)>0\), **independent of \(B\) and of the potentials**, such that
\[
\boxed{\;
|\mathcal M_m(\mathbf t)-\mathcal M_m(\mathbf s)|
 \le C(1+B)^{m-1}\sum_{i=1}^m\|t_i-s_i\|_{L^\infty(X)}.
\;}
\tag{1}
\]
In particular, for \(H_m(t)=Q_m(t,\ldots,t)\),
\[
\boxed{\;
\left|\int_X H_m(t)-\int_X H_m(s)\right|
\le Cm(1+B)^{m-1}\|t-s\|_{L^\infty(X)}.
\;}
\tag{2}
\]
Thus uniform convergence of uniformly bounded admissible **nonmonotone** lists implies convergence of their **total mixed masses**. No weak convergence of the full measures under arbitrary nonmonotone perturbations is asserted.

The power one of the sup-norm difference is optimal whenever the first torsion variation does not vanish. The displayed polynomial dependence on \(B\) is an established upper bound, **not** asserted to be optimal.

## Exact telescoping identity

Set
\[
\mathbf a^{(j)}=(t_1,\ldots,t_j,s_{j+1},\ldots,s_m),
\quad 0\le j\le m,
\]
and for \(1\le j\le m\) define the \((n-1,n-1)\)-current
\[
T_j=R_{m-1}(t_1,\ldots,t_{j-1},s_{j+1},\ldots,s_m)
       \wedge\omega^{n-m}.
\]
The following is an **exact** identity for bounded admissible lists:
\[
\boxed{\quad
\mathcal M_m(\mathbf t)-\mathcal M_m(\mathbf s)
=\sum_{j=1}^m\int_X(t_j-s_j)\,\mathrm{dd}^{\mathrm c}T_j .
\quad}
\tag{3}
\]
Every term on the right uses the bounded **canonical** difference against the signed Radon measure \(\mathrm{dd}^{\mathrm c}T_j\); it does **not** interpret a product of an unbounded distribution with a merely Borel function.

For smooth lists, the telescoping polynomial identity is
\[
Q_m(\mathbf a^{(j)})-Q_m(\mathbf a^{(j-1)})
=\mathrm{dd}^{\mathrm c}(t_j-s_j)\wedge T_j.
\]
Integrating on compact \(X\) and using Stokes/integration by parts yields (3).

For arbitrary bounded admissible endpoints, select separately the globally smooth decreasing admissible approximations provided by §8.6.6. For each approximation index the smooth identity holds. By Theorem 8.11.12 the corresponding positive mixed measures converge weakly, so the integrals on the left converge. By Lemma 8.12.4 the signed torsion measures \(\mathrm{dd}^{\mathrm c}T_j^{(k)}\) converge **even when weighted** by a continuous function of finitely many bounded decreasing admissible approximants. Apply it to the two-variable function \(F(x,y)=x-y\). Consequently each right-hand integral converges to the right-hand side of (3). The differences \(t_j^{(k)}-s_j^{(k)}\) need not decrease; assuming their monotonicity would be an invalid shortcut. No exchange of unrelated iterated limits is used.

## Uniform torsion variation

The shifted current \(R_{m-1}\) is the finite subset expansion in (8.9.5):
\[
R_{m-1}(\mathbf v)=
\sum_{I\subseteq\{1,\ldots,m-1\}}
\omega^{m-1-|I|}\wedge D_I(\mathbf v).
\]
For every \(p<m\), Proposition 8.9.3 gives on compact coordinate sets \(K\Subset U\)
\[
\|D_p(v_{i_1},\ldots,v_{i_p})\|_K
\le C_{K,U,\omega,p}(1+B)^p .
\]
The torsion formula in Lemma 8.12.4 (ultimately Proposition 8.9.7) expresses \(\mathrm{dd}^{\mathrm c}T_j\) as a **finite** sum of fixed smooth metric-derivative forms wedged with shifted currents of degrees at most \(m-1\). In particular, the potentially nonclosed background contributions of degree \(m-1\) must be retained; there is no assumed identity \(\mathrm{dd}^{\mathrm c}\omega^q=0\). Expanding these shifted currents over their subsets bounds every coefficient variation by \(C_{K,U}(1+B)^{m-1}\). A finite coordinate cover and its subordinate cutoff functions therefore give
\[
\boxed{\quad
|\mathrm{dd}^{\mathrm c}T_j|(X)
\le C(X,\omega,m,n)(1+B)^{m-1},
\qquad 1\le j\le m .
\quad}\tag{4}
\]
Combining (3) with (4) proves (1), and choosing both lists diagonally proves (2). The result remains valid without any Gauduchon or Kähler condition; if the background powers are \(\mathrm{dd}^{\mathrm c}\)-closed as in Theorem 8.13.4, the total masses are exactly constant and the left side vanishes.

## Sharpness of the perturbation exponent (existing source model)

The already printed Example 8.13.5 supplies a sharpness check without inventing a new example. On its Hermitian complex torus, with \(u_t=t\cos(2\pi x_1)\), \(|t|<\pi^{-2}\),
\[
\|u_t-u_0\|_\infty=|t|,\qquad
\int_XH_m(u_t)-\int_XH_m(0)
=-\frac{m\pi^2n!}{2n}B_n\,t,\quad B_n>0.
\]
Thus the mass difference is a **nonzero constant times** the uniform distance. A general \(o(\|u-v\|_\infty)\) modulus, or a Hölder exponent \(>1\), is false even for smooth strictly admissible potentials on a fixed background. This reuses the printed computation; it is **not** a separately discovered torus counterexample.

## Audited anchors, dependencies, proposed addition, and effect

| Role | Exact integrated reader path on main | Stable source label; permanent reader tag | Physical HTML lines |
| --- | --- | --- | --- |
| Raw coefficient estimate and canonical recursion | \`docs/sections/complex-hessian-equations--bounded-potentials-and-recursive-hessian-currents/index.html\` (blob \`117b866408974cdf706bf305df75e35e1b8affde\`) | \`non-kahler-pluripotential-theory:354EA0C7\`; \`EB2FA13CDDE0\` (§8.9.3); (8.9.5) \`17FA1BFF2491\` | 36–115, especially 47–78, 83–103 |
| Torsion identities | same §8.9 file | \`non-kahler-pluripotential-theory:633FD461\`; \`26EFAEC0B76D\` (§8.9.7) | 123–147 |
| Weighted torsion measure convergence | \`docs/sections/complex-hessian-equations--locality-and-maxima-of-bounded-potentials/index.html\` (blob \`8750df56019c14e16704607ca20fa8b90f137fb0\`) | \`non-kahler-pluripotential-theory:5AEBD34D\`; \`3A8C156268BF\` (§8.12.4) | 96–110 |
| Mixed total-mass definition/integration | \`docs/sections/complex-hessian-equations--hessian-mass-and-global-comparison/index.html\` (blob \`580d3bc2b10ebd01d880b2a31fc6930436570aac\`) | \`non-kahler-pluripotential-theory:A6052F07\`; \`69692CE9985B\` (§8.13.1) | 10–38 |
| Constant-mass special case | same §8.13 file | \`non-kahler-pluripotential-theory:776C8B26\`; \`53F870DE5980\` (§8.13.4) | 69–121 |
| Optimal order, existing example | same §8.13 file | \`non-kahler-pluripotential-theory:870AB319\`; \`0DB9D80DE230\` (§8.13.5) | 128–150 |
| Joint decreasing convergence, auxiliary only | \`docs/sections/complex-hessian-equations--local-capacities-and-decreasing-products/index.html\` (blob \`115d285f6b1f76d284463c396e7e87db2b9dbdc3\`) | §8.11.12 tag \`C044CD1C65C4\` | 281–295 |

**Verified direct steps:** polynomial telescoping for smooth lists; Stokes sign; weighted passage for canonical nonmonotone differences under separate decreasing approximants; the uniform order-\((1+B)^{m-1}\) torsion-variation bound; and linear-order sharpness using the pre-existing smooth formula.

**Open dependencies:** the general global decreasing smooth admissible approximation (§8.6.6), recursive coefficient estimates (§8.9.3), capacity/quasicontinuity and weighted decreasing convergence (§8.11.10–12), and the general integrated-product existence are used **as stated** and have not been independently certified in full. This report is therefore a **verified conditional deduction**, not an unconditional proof from first principles. The excluded Demailly approximation/regularization and its Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss programme remains **deferred-by-user**, neither reopened nor certified. An appearance of the word "approximation" in the separate Chapter 8 Hessian-input chain is not an authorization to audit that excluded programme.

**Proposed source change (not executed):** add (1)–(3) after §8.13.1, citing §§8.9.3, 8.11.12 and 8.12.4. This is a new uniform-topology stability lemma, not a correction to an erroneous original theorem. Potential readers include §§8.13.3–4 (total-mass corrections), §8.13.8 (modified comparison) and the bounded equation theory; no downstream theorem is claimed false or fully reverified.

**Coverage accounting:** direct proof-level review targeted §§8.12.4 and 8.13.1, with specific auxiliary steps above. Neither §8.12 nor §8.13 is declared newly **entirely certified**, no first-visit credit is asserted, and **zero** complete upstream dependency chains were certified. No source/body/registry/permanent-tag/main/site modifications, tests, builds, CI or publication are part of this report.
