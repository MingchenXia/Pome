# Infinite divisorial trace on a fixed projective surface: oscillatory finite-level mass

**Finding ID:** POME-BDIV-INFINITE-DYADIC-TRACE-RATE-001  
**Date:** 2026-11-03  
**Severity / status:** low / verified conditional deduction (explicit model, not a false printed theorem).  
**Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

## Reading-edition anchors and scope

- Main file: docs/sections/divisorial-currents-on-compact-modifications/index.html, blob 79d6e21f9d3784bf3761846f77f90ad075253644.
- Theorem 20.4.2: source label **non-kahler-pluripotential-theory:E6DD8E29**, permanent tag **A67FA9DFB4BC**, physical lines **50–82**. The finite divisor definition occurs at lines **35–43**, the countable-series construction and dominated-convergence argument at **78–82**, and dyadic monotonicity at **60, 82**. Equation 20.4.3: source **non-kahler-pluripotential-theory:CDEF0DCA**, permanent **B7771456202C**, lines **52–56**.
- Premise crosscheck only: Theorem 20.3.2 and Eq. 20.3.3, source **non-kahler-pluripotential-theory:BF417B5C** and **:2D477734**, permanent **7CD874C73EC9** and **66AFB7F7397B**; docs/sections/restriction-and-intrinsic-trace-data/index.html, blob dbc3b722ceacb8232fe4c7b711e5ad98b0708f06, physical lines **35–51**.
- This is the first *direct infinite-divisor finite-level multiplier-ideal rate* check of Theorem 20.4.2. It does **not** certify the theorem for arbitrary currents, arbitrary models, or any approximation/principalization dependency. Previous §20.3 curve atomic tests and §13.24 countable-positive-current valuation-tail tests are distinct; neither established the entire fixed-model integer-index rate below.

## Exact global model

Work on \(Y=X=\mathbf P^2\) with normalized Fubini–Study form \(\omega\), \(\int_Y\omega^2=1\), and \(dd^c=\tfrac{i}{2\pi}\partial\bar\partial\). In homogeneous coordinates \(Z=[Z_0:Z_1:Z_2]\), for \(j\geq1\) let
\[
 \ell_j(Z)=\frac{Z_0-j^{-1}Z_1}{\sqrt{1+j^{-2}}},\qquad
 L_j=\{\ell_j=0\},\qquad a_j=2^{-j}.
\]
These lines are distinct and all pass through \(p=[0:0:1]\). Their only limiting line in the pencil is \(L_\infty=\{Z_0=0\}\), which is distinct from each \(L_j\). Put
\[
 u([Z])=\sum_{j\geq1}a_j\log\frac{|\ell_j(Z)|^2}{\|Z\|^2},
 \qquad T=\omega+dd^c u .
\]
Every summand is nonpositive and belongs to \(\operatorname{PSH}(Y,\omega)\) after adjusting the background by its coefficient. Its \(L^1(\omega^2)\) norm is the same finite number for every \(j\), by unitary invariance of \(\omega\) and the normalization of the linear forms. Hence \(\sum a_j\| \log(|\ell_j|^2/\|Z\|^2)\|_{L^1}<\infty\), so the decreasing series is a genuine quasi-psh \(L^1\) potential rather than \(-\infty\). Poincaré–Lelong and continuity of distributional derivatives give
\[
 T=\sum_{j\geq1}a_j[L_j]\geq0,\qquad
 \int_Y T\wedge\omega=\sum_{j\geq1}a_j=1 .
\]
Its generic Lelong number on \(Y\) is zero, as required in §20.4. At a generic point of \(L_j\) away from \(p\), all other \(L_i\) miss a sufficiently small neighborhood: the slope \(1/j\) is isolated among the slopes \(1/i\), with sole accumulation at zero. There the sum of the other logarithms converges smoothly and
\[
 u=a_j\log|z_1|^2+O(1).
\]
At a generic point of any other irreducible divisor, including \(L_\infty\), the generic divisorial Lelong number of \(T\) is zero. One may see this without assuming locally bounded remainders near \(L_\infty\): normalized local Lelong masses of individual hyperplane currents are bounded by a common constant, and their weighted sum has summable weights, so dominated convergence yields
\(\nu(T,x)=\sum_j a_j\mathbf1_{L_j}(x)\).
Consequently the only nonzero coefficients of the self-trace current on the **identity model** are precisely the \(a_j\) on \(L_j\).

At each generic point of \(L_j\), the one-variable local-integrability condition
\[
 |z_1|^{2q}\exp(-m u)\in L^1_{\mathrm{loc}}
 \quad\Longleftrightarrow\quad q\geq\lfloor ma_j\rfloor
\]
shows directly that
\(\operatorname{ord}_{L_j}\mathcal I(mu)=\lfloor m2^{-j}\rfloor\).
All other divisorial generic orders on the identity model vanish; no assertion is made about exceptional divisors on blowups of \(p\). Thus the exact finite-level currents of Theorem 20.4.2 are
\[
 \boxed{\
 D_{m,Y}=\frac1m\sum_{j\geq1}\lfloor m2^{-j}\rfloor[L_j],
 \qquad S_Y(u;Y)=\sum_{j\geq1}2^{-j}[L_j].\
 }
\]
The first sum is **finite for each \(m\)** even though the limiting current has infinitely many nonzero divisorial coefficients. Its trace-mass error in the fixed Gauduchon metric \(\omega\) is exactly
\[
 \boxed{\
 e_m=\int_Y(S_Y-D_{m,Y})\wedge\omega
    =1-\frac1m\sum_{j\geq1}\lfloor m2^{-j}\rfloor.\
 }
\]

## Two sharply different integer subsequences

For \(m=2^k\) (\(k\geq1\)), the floor is \(2^{k-j}\) for \(j\leq k\) and zero otherwise. Therefore
\[
 D_{2^k,Y}=\sum_{j=1}^k2^{-j}[L_j],
 \qquad e_{2^k}=\sum_{j>k}2^{-j}=2^{-k}=\frac1m .
\]
In particular, these dyadic currents increase, and their tail masses are explicit, as the printed theorem asserts.

For \(m=2^k-1\) (\(k\geq2\)),
\(\lfloor m2^{-j}\rfloor=2^{k-j}-1\) for \(1\leq j\leq k\) and is zero for \(j>k\). Hence
\[
 \sum_{j\geq1}\lfloor m2^{-j}\rfloor=(2^k-1)-k=m-k,
 \qquad
 \boxed{\ e_{2^k-1}=\frac{k}{2^k-1}
              =\frac{\log_2(m+1)}m.\ }
\]
Thus **no estimate \(e_m\leq C(u,Y,\omega)/m\) holds for all positive integers \(m\)** even for this one fixed positive current on \(\mathbf P^2\). A direct bound for all \(m\geq1\), with \(k=\lfloor\log_2m\rfloor\), is
\[
 0\leq e_m<
 \frac{k}{m}+\sum_{j>k}2^{-j}
 \leq\frac{k+2}{m}.
\]
The order \((\log m)/m\) along \(m=2^k-1\) is therefore sharp for this example. The integer sequence of currents need not be increasing: the \(L_1\)-coefficient falls from \(1/2\) in \(D_4\) to \(2/5\) in \(D_5\). The theorem carefully asserts increasingness only for the dyadic subsequence. For any fixed smooth \((1,1)\) test form \(\eta\), positivity bounds
\(|\langle S_Y-D_{m,Y},\eta\rangle|\leq C_\eta e_m\), confirming weak convergence without exchanging unrelated limits.

## Classification, implications, and boundaries

The original Theorem 20.4.2 is **not false**: the construction satisfies its hypotheses, finite-level dominance, convergence and dyadic monotonicity. The new finding is a **verified conditional deduction / quantitative obstruction**: a natural \(O(1/m)\) strengthening of *all-integer* trace-mass convergence is wrong when infinitely many prime divisors contribute, although a sparse dyadic subsequence can have that rate. The example independently tests countability, infinite-to-finite truncation, fixed-model trace normalization and the precise non-monotone integer quantifiers, not just a preexisting one-atom floor calculation.

**Suggested addition (not edited in production):** after Theorem 20.4.2, note that convergence has no unconditional \(C/m\) rate for the full integer sequence; cite the projective line-pencils model above. Any future rate statement for Theorem 20.4.2, or downstream use of its convergence in Theorems 20.4.5/20.4.15, must explicitly impose a quantitative distribution assumption on divisorial coefficients or restrict the index family. **No current dependent theorem was shown false.** All analytic-approximation/regularization, Bergman, weighted \(L^2\), OT, multiscale or positivity-loss material is excluded/deferred-by-user and was not investigated here.

**Verification performed:** exact local integrability at generic divisorial points, full-series \(L^1\) convergence, Poincaré–Lelong, trace-mass normalization, and both floor-sum identities. No project build, formal verification, CI, web publication, or full proof-chain certification.
