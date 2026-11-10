# Audit: exact central-fiber Hilbert ranks in every projective dimension

**Date:** 2026-11-10. **Finding:** **POME-DIVVOL-CENTRAL-HILBERT-GLUING-001**.
**Status:** verified conditional deduction. **Severity:** low. The printed theorem and formulas are **not claimed false**.

## Pinned reading-edition location

Production main: **b6933b772f41b45918f7e25ed1afbbb1fd892272**.
Integrated file: **docs/sections/divisorial-restricted-volumes/index.html**, Git blob **8eb1127568e77d6d045098361c366ceeb846b909**.
Theorem **20.8.3**: source **transcendental-positive-cones:42C59BDB**, permanent **8DC7DAC31FB7**, physical lines **64–69**; its deformation to the normal cone is introduced at **lines 72–93**. Grouped volume equations **20.8.4–20.8.7**: source **transcendental-positive-cones:94BE9453**, permanent **419BFB5D9AD7**, physical lines **115–120**. Central conservation equation **20.8.8**: source **transcendental-positive-cones:80713735**, permanent **93C6922E83B2**, lines **136–141**. In particular the three restricted-volume terms have individual entry tags **9788B3886ACF** (20.8.5), **8B17E6C92508** (20.8.6), and **6394FCEF80E1** (20.8.7). The printed analytic proof is much broader; this note verifies an independent algebraic family, and **does not examine or certify** its regularization-dependent passages.

## Exact finite-degree construction

Fix an integer \(n\geq1\), integers \(A,B,C\) with \(0<C<\min(A,B)\), and \(X=\mathbb P^n\) with \(H=\{x_0=0\}\). Let \(F_0=\{\tau=0\}\subset\mathbb P^1\) and
\[
W=\operatorname{Bl}_{H\times F_0}(\mathbb P^n\times\mathbb P^1),\qquad
L=A\,p_X^*H+B\,p_{\mathbb P^1}^*[\mathrm{pt}]-C E .
\]
The center is the smooth complete intersection of local equations \(x_0=0,\tau=0\). From the two elementary blowup charts (the Rees algebra of the ideal \((x_0,\tau)\)), sections of \(kL\) are exactly bihomogeneous polynomials of bidegree \((kA,kB)\) in the \(kC\)-th ideal power. For monomials
\(x_0^i x_1^{a_1}\cdots x_n^{a_n}t_0^j t_1^{kB-j}\), with \(i+\sum_{\ell\geq1}a_\ell=kA\), this is the **exact** condition
\[
 i+j\geq kC,\qquad 0\leq i\leq kA,\quad 0\leq j\leq kB .
\]
Thus for every integer \(k\geq1\),
\[
\boxed{h^0(W,kL)
=(kB+1)\binom{kA+n}{n}
-\sum_{i=0}^{kC-1}(kC-i)\binom{kA-i+n-1}{n-1}.}\tag{1}
\]
No smooth-approximation, Bergman, multiplier-ideal or non-pluripolar limit is used.

## Four simultaneous restricted-rank computations

Write \(X'\) for the strict transform of the zero fiber; the blowup of \(X\) along its Cartier hyperplane \(H\) is \(X\) itself. Restriction of a section to \(X'\) keeps precisely the terms with \(j=0\), \(i\geq kC\), after dividing the prescribed exceptional factor. Consequently
\[
\boxed{\dim\operatorname{im}[H^0(W,kL)\to H^0(X',kL|_{X'})]
=\binom{k(A-C)+n}{n}.}\tag{2}
\]
For any nonzero fiber \(X_\tau\), the term \(j=kB\) permits every degree-\(kA\) monomial, because \(B>C\), so
\[
\boxed{\dim\operatorname{im}[H^0(W,kL)\to H^0(X_\tau,kL|_{X_\tau})]
=\binom{kA+n}{n}.}\tag{3}
\]
On \(E=\mathbb P_H(\mathcal O_H(1)\oplus\mathcal O_H)\), the initial normal form has \(i+j=kC\). The torus characters with different \(i\) and remaining \(x_\ell\)-monomials are independent on the two blowup charts. Each is realized by a global section because \(B>C\), giving
\[
\boxed{\begin{aligned}
\dim\operatorname{im}[H^0(W,kL)\to H^0(E,kL|_E)]
&=\sum_{i=0}^{kC}\binom{kA-i+n-1}{n-1}\\
&=\binom{kA+n}{n}-\binom{k(A-C)+n-1}{n}.
\end{aligned}}\tag{4}
\]
These are ranks of **actual restriction maps**, not merely counts of intrinsic sections or an appeal to numerical equivalence.

An additional exact, finite-degree gluing defect is
\[
\boxed{r_{X'}(k)+r_E(k)-r_{X_\tau}(k)
=\binom{k(A-C)+n-1}{n-1}.}\tag{5}
\]
The right-hand side is the dimension of \(H^0(H,\mathcal O_H(k(A-C)))\), precisely the common-intersection trace on \(X'\cap E=H\). In particular, summing the two central *finite-degree* ranks without subtracting the interface trace would be false; the extra term is of order \(k^{n-1}\), so it disappears in the normalized leading degree \(k^n/n!\). This is stronger information than the printed leading-volume conservation identity.

## Leading coefficients and normalization

The section-growth definition of algebraic volume, (1) and Riemann sums yield
\[
\begin{aligned}
\operatorname{vol}_{\rm alg}(W,L)
&=(n+1) B A^n-n(n+1)\int_0^C(C-s)(A-s)^{n-1}\,ds\\
&=(n+1)\left((B-C)A^n+\int_0^C(A-s)^n\,ds\right).
\end{aligned}\tag{6}
\]
The last identity follows by integrating
\(n(C-s)(A-s)^{n-1}\) by parts; the boundary term is \(CA^n\).
Similarly (2)–(4), with the **restricted image** definition and normalization \(n!/k^n\), give
\[
\boxed{\begin{aligned}
\operatorname{vol}_{W|X_\tau}(L)&=A^n\quad(\tau\ne0),\\
\operatorname{vol}_{W|X'}(L)&=(A-C)^n,\\
\operatorname{vol}_{W|E}(L)&=A^n-(A-C)^n
=n\int_0^C(A-t)^{n-1}dt.
\end{aligned}}\tag{7}
\]
Hence central mass conservation holds **in every \(n\ge1\)**:
\[
\operatorname{vol}_{W|X'}(L)+\operatorname{vol}_{W|E}(L)=A^n.
\]
Finally \(\operatorname{vol}_{\mathbb P^n}(AH+tH)=(A+t)^n\) yields the printed derivative \(nA^{n-1}=n\operatorname{vol}_{X|H}(AH)\). At \(n=1\) the two central components have degrees \(A-C\) and \(C\), providing the edge-case check.

For a reproducible finite-degree check take \((n,A,B,C,k)=(3,4,5,2,1)\): (1) gives \(170\) global sections; generic-fiber rank \(35\), central ranks \(10\) and \(31\), and interface rank \(6\). Thus \(10+31-35=6\). The volume from (6) is \(1008\), while the three restricted volumes are \(64,8,56\).

## Status, boundaries, and correction proposal

This is a **verified conditional deduction** for the smooth projective toric test family, not a proof of Theorem 20.8.3 for arbitrary big real classes. The algebraic section/image-rank formulas (1)–(5) are elementary and self-contained. Interpreting the resulting algebraic volumes as the *analytic* big-class/non-pluripolar volumes in the printed general theorem uses the project's projective algebraic/analytic volume comparison, which is **not transitively certified here**. No conclusion about regularization, non-Kähler loci, a general Legendre-envelope interchange or complete \(X'\)/\(E\) analytic restriction proof is drawn.

**Suggested optional text-only addition to a future separately reviewable source patch:** after (20.8.8), include the finite-degree gluing identity (5) as a projective-space check; the interface rank clarifies why conservation is an asymptotic equality rather than an uncorrected finite-level sum. Keep the original historical attribution, section labels and permanent tags unchanged. The previous **POME-DIVVOL-P2CENTRAL-FIBER-001** already checked the \(n=2\) leading intersection numbers; the genuinely new content here is the **arbitrary-dimensional all-\(k\) monomial rank computation and codimension-one gluing correction**, not another registration of its \(n=2\) arithmetic.
