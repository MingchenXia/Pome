# Strict mixed-discriminant equality and rigidity of smooth Kähler Hessians

**Date:** 2026-11-08. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Review branch at start:** 7e4c3f4df2f09e42824b0d3bd0fb9f6bfc293d11. **Finding:** POME-BT-MIXED-EQUALITY-KAHLER-RIGIDITY-001, **low / verified conditional deduction**. This is not a counterexample to the printed statements and not a completion of the full Bedford–Taylor dependency graph.

## Production reading edition and stable anchors

- Section 7.8, docs/sections/bedford-taylor-products-and-local-capacity--density-lower-bounds-and-mixed-products/index.html, **main blob 0284d93a0ac26e28746e95afda5e6875f9feaba3**. Its local normalization is $\eta=dd^c|z|^2$ and $(dd^c u)^n=\det\mathcal H(u)\,\eta^n$ for smooth $u$, physical lines **7–16**. Lemma **7.8.6**, source **foundations-of-pluripotential-theory:1BCDB7A0**, permanent tag **91F43DBA51F0**, physical lines **215–245**, includes the normalized mixed-discriminant inequality and reverse Cauchy–Schwarz step. Corollary **7.8.8**, source **foundations-of-pluripotential-theory:88AEA1CD**, permanent tag **142C8110B540**, lines **249–282**, is the locally bounded mixed Bedford–Taylor lower bound (no equality claim). The auxiliary determinant definition occurs at lines **210–213**.
- Section 5.3, docs/sections/complex-differential-forms-and-positive-currents--currents-and-positivity/index.html, **main blob deba65cba51b4275b523879202e6254db0db2b5c**. Lemma **5.3.4**, source **foundations-of-pluripotential-theory:36DBF0BE**, permanent tag **8907196C3513**, physical lines **179–222** proves that, with strictly positive definite fixed matrices in the other slots, $q(M,N)=D(M,N,A_3,\ldots,A_n)$ has signature $(1,n^2-1)$ and its restriction to the $q$-orthogonal hyperplane of any positive definite $H$ is negative definite. The proof at lines **193–221** was read independently for its strict nondegeneracy and normalization. Lemma **5.3.3**, source **foundations-of-pluripotential-theory:11CB40EC**, permanent tag **3D25BAD0C21E**, lines **127–176**, fixes the mixed-discriminant convention.
- Prior nearby result **POME-BT-SURFACE-MINKOWSKI-ANISOTROPY-001** checks a *pairwise, complex-dimension-two, exact spectral defect*. **POME-BT-FINITE-MINKOWSKI-001** checks a *nonnegative lower bound*. Neither is presented here as new. The new work concerns the **full n-linear strict equality condition in every dimension n >= 2** and the additional **global differential rigidity** from closedness of smooth Kähler forms.

## Theorem A: strict equality in the mixed discriminant

Let $n\ge 2$ and let $A_1,\ldots,A_n$ be **positive definite** Hermitian $n\times n$ matrices. Under the reading edition's normalization

\[
D(A_1,\ldots,A_n)\ge\prod_{i=1}^n(\det A_i)^{1/n},
\]

**equality holds if and only if all the $A_i$ are positive scalar multiples of one matrix.** For $n=1$ there is only one matrix, so the equality statement has no rigidity content. The positive-definiteness assumption cannot be dropped for this iff characterization.

**Complete derivation from the inspected internal signature lemma.**
Normalize $B_i=(\det A_i)^{-1/n}A_i$; then $\det B_i=1$. Assume the displayed lower-bound inequality is an equality, so $D(B_1,\ldots,B_n)=1$. Fix two indices $i\ne j$ and regard the remaining $n-2$ positive definite matrices as fixed slots of
$q(X,Y)=D(X,Y,B_{k_3},\ldots,B_{k_n})$.
By Lemma 5.3.4, $q$ has precisely one positive direction, and its restriction to the $q$-orthogonal complement of the positive definite $B_j$ is **negative definite**. Its reverse Cauchy–Schwarz inequality is
\[
q(X,Y)^2\ge q(X,X)q(Y,Y)
\quad (X,Y>0).
\]
Here $q(B_i,B_j)=1$. Applying the same Lemma 7.8.6 to tuples with the first two entries repeated yields
\[
q(B_i,B_i)\ge1,\qquad q(B_j,B_j)\ge1.
\]
Consequently
\[
1=q(B_i,B_j)^2\ge q(B_i,B_i)q(B_j,B_j)\ge1.
\]
Let $c=q(B_i,B_j)/q(B_j,B_j)>0$ and $M=B_i-cB_j$. Then $q(M,B_j)=0$ and
\[
q(M,M)=q(B_i,B_i)-\frac{q(B_i,B_j)^2}{q(B_j,B_j)}=0.
\]
Strict negative definiteness on this orthogonal hyperplane forces $M=0$. Thus $B_i=cB_j$, and $\det B_i=\det B_j=1$ forces $c=1$. Every pair coincides; therefore all original $A_i$ are positive scalar multiples. Conversely, if $A_i=c_i A$ with $c_i>0$, multilinearity and $D(A,\ldots,A)=\det A$ give equality. This is a strictness upgrade of the **already printed and correct** Lemma 7.8.6, not a repaired statement.

**Why positive definiteness matters.** In dimension 3, let
$A_1=A_2=\operatorname{diag}(1,0,0)$ and
$A_3=\operatorname{diag}(0,1,0)$.
Then each pure determinant and the mixed discriminant vanish (two factors have the same one-dimensional range), so equality holds although $A_3$ is not proportional to $A_1$. There is no assertion of proportionality for general semipositive matrices.

**Exact three-matrix model, distinct from the prior surface computation.**
For $t>0$, put
\[
A_1=\operatorname{diag}(t,1,1),\quad
A_2=\operatorname{diag}(1,t,1),\quad
A_3=\operatorname{diag}(1,1,t).
\]
Each determinant is $t$. The coefficient-of-$x_1x_2x_3$ formula for $D$ is the normalized permanent of the 3 by 3 diagonal coefficient matrix: among the six permutations, one contributes $t^3$, three contribute $t$, and two contribute $1$. Hence
\[
D(A_1,A_2,A_3)-t
=\frac{t^3+3t+2}{6}-t
=\frac{(t-1)^2(t+2)}6.
\]
It is strictly positive for $t\ne1$ and zero for $t=1$, explicitly testing full three-factor equality without relying on two-factor polarizations.

## Theorem B: rigidity for smooth strictly PSH potentials

Let $\Omega\subset\mathbb C^n$, $n\ge2$, be **connected** and open. Let $u_1,\ldots,u_n\in C^3(\Omega,\mathbb R)$ be strictly plurisubharmonic, with positive definite complex Hessian matrices everywhere. Put $\omega_i=dd^c u_i$, $\eta=dd^c|z|^2$, and
$f_i=(\omega_i^n/\eta^n)>0$.

Then the smooth measure identity
\[
\boxed{\quad
\omega_1\wedge\cdots\wedge\omega_n
=\left(\prod_{i=1}^n f_i^{1/n}\right)\eta^n
\quad}
\]
holds on all of $\Omega$ **if and only if** there are positive *constants* $c_2,\ldots,c_n$ such that
\[
\omega_i=c_i\omega_1
\quad\text{on }\Omega\quad(i=2,\ldots,n).
\]
Equivalently $u_i-c_i u_1$ is pluriharmonic on $\Omega$, without claiming it is globally the real part of a single-valued holomorphic function.

**Proof.** The density of the left side is the mixed discriminant $D(\mathcal H(u_1),\ldots,\mathcal H(u_n))$ (compare Corollary 7.8.8, physical lines 269–280), while $f_i=\det\mathcal H(u_i)$. Since these densities are continuous, equality as measures implies pointwise equality. Theorem A gives smooth positive functions $a_i$ such that $\omega_i=a_i\omega_1$. Their regularity is at least $C^1$, since $u_i\in C^3$ and $\omega_1$ is positive definite (one can take the ratio of any nonzero Hermitian diagonal coefficient). All $\omega_i$ are closed because they are $dd^c$-exact. Thus
\[
0=d\omega_i=d(a_i\omega_1)=da_i\wedge\omega_1.
\]
For $n\ge2$, wedge with $\omega_1^{n-2}$ to obtain
$da_i\wedge\omega_1^{n-1}=0$. The map
$\Lambda^1_{\mathbb R}\to\Lambda^{2n-1}_{\mathbb R}$,
$\xi\mapsto\xi\wedge\omega_1^{n-1}$, is an isomorphism for a nondegenerate real two-form: in Darboux coordinates this follows by writing its symplectic paired basis and checking the nonzero images of every basis covector. Thus $da_i=0$. Connectedness makes $a_i=c_i>0$ constant. The converse is immediate from multilinearity and $D(A,\ldots,A)=\det A$; and $dd^c(u_i-c_i u_1)=0$ is the pluriharmonicity criterion.

The same conclusion is only componentwise constant on a disconnected domain. In dimension one the exterior differential $da\wedge\omega$ vanishes for degree reasons and does not force $a$ constant: e.g. $u_1=|z|^2$ and $u_2=|z|^2+|z|^4$ on a disk have nonconstant ratio of complex Hessians, whereas any one-factor mixed inequality is an identity. In degenerate and merely locally bounded Bedford–Taylor settings, neither the smooth proportionality conclusion nor the distributional wedge step above is asserted.

## Classification, affected dependents, and scope

**Finding POME-BT-MIXED-EQUALITY-KAHLER-RIGIDITY-001. Severity: low. Status: verified conditional deduction.** Theorems A and B are fully justified *from the directly inspected internal mixed-discriminant/signature statements* under their explicit strict-smooth hypotheses; the entire dependency chain of Lemma 5.3.4 and the bounded Bedford–Taylor comparison theorem is **not** separately certified. No printed theorem is false, and there is no claimed repair of a missing proof. Optional proposed amendment: a separate smooth equality-case remark after §7.8.8, preserving the source attribution, both original theorem statements, the permanent tags, and all legitimate semipositive versions. Potential downstream *interpretive* dependents are the equality cases of the mixed density estimates in §7.8, the local smooth models for §7.9, and mixed-energy/Hessian comparisons elsewhere; no downstream printed result is declared invalid.

**Coverage actually performed this run:** the exact proof of Lemma 7.8.6 (including the reverse Cauchy–Schwarz and minimizing-tuple argument), the statement and smooth coefficient comparison in Corollary 7.8.8, and the signature proof of Lemma 5.3.4 (including its induction/nondegeneracy). §7.8 and §5.3 had previously been only partially audited, so **no first-visit credit and no entire-section certificate**; the current ToC has 25 chapters and 747 numbered sections. No project build, tests, formal verification, CI, main/source edits or website publication were performed. The Demailly approximation/regularization and its dedicated Bergman, weighted-$L^2$, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programme remain **deferred-by-user** and were not visited.
