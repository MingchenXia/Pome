# Contracting Hopf quotients: smooth topology from a Lyapunov cross-section

**Finding:** `POME-HOPF-CONTRACTION-LYAPUNOV-S3S1-001`  
**Date:** 2026-11-19  
**Severity / status:** low / **verified conditional deduction** (a stronger topological conclusion, **not** an error in the printed theorem).  
**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated HTML:** `docs/sections/contracting-hopf-quotients/index.html`, blob `d09d9bac3785b78b557ff5178ad7a52b34b20dac`.  
**Stable source / permanent tag:** Theorem 23.3.3, `demailly-complex-geometry:371996B7` / `D81E3145A1B4` (lines 8–22); iteration equation 23.3.4, `demailly-complex-geometry:F5EE64FF` / `436562DE848D` (lines 29–32). Full printed proof at lines 24–53. The section has two headings and this one proof-bearing theorem; mathematical contents at lines 5–53 were directly read.

## Statement and distinction from existing reports

In either case of Theorem 23.3.3 — diagonal contractions with `0<|lambda_1|<=|lambda_2|<1`, or triangular maps
\[
 F(z_1,z_2)=(\lambda z_1,\lambda z_2+z_1^p),\qquad 0<|\lambda|<1,\ p\ge1,
\]
the compact complex quotient \(X_F=(\mathbb C^2\setminus\{0\})/\langle F\rangle\) is **smoothly diffeomorphic to \(S^3\times S^1\)**. In particular,
\[
H^j(X_F;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&j=0,1,3,4,\\
0,&j=2\text{ or }j>4,
\end{cases}
\qquad
b_2(X_F)=0,\quad\chi(X_F)=0,\quad\pi_2(X_F)=0.
\]
Hence \(X_F\) admits **no symplectic form**, a strictly stronger obstruction than the printed non-Kähler conclusion. This finding is the smooth **Lyapunov-cross-section** argument and integral topology, **not** a reclassification of automorphism groups, the previously noted polynomial conjugacy for \(p>1\), or the already printed \(\pi_1=\mathbb Z\) statement. Prior audit results remain in place.

## 1. Linear contractions: an explicit global product

Let \(A\in GL_2(\mathbb C)\) have all eigenvalues of modulus strictly less than one and suppose \(A=e^L\) for a complex matrix logarithm \(L\) all of whose eigenvalues have strictly negative real parts. Such an \(L\) exists in the two linear cases under consideration:

* For \(A=\operatorname{diag}(\lambda_1,\lambda_2)\), choose \(L=\operatorname{diag}(\log\lambda_1,\log\lambda_2)\), with any complex logarithm of each eigenvalue.
* For the triangular \(p=1\) case \(A=\lambda I+N\), \(N=\left(\begin{smallmatrix}0&0\\1&0\end{smallmatrix}\right)\), \(N^2=0\). Take
  \[
  L=(\log\lambda)I+\lambda^{-1}N.
  \]
  Since \(\exp(\lambda^{-1}N)=I+\lambda^{-1}N\), we have \(e^L=A\), and both eigenvalues of \(L\) are \(\log\lambda\), with negative real part.

The semigroup \(e^{tL}\) converges exponentially to zero, up to a polynomial factor, as \(t\to+\infty\). Define the Hermitian matrix
\[
Q=\int_0^\infty (e^{tL})^*e^{tL}\,dt.
\]
The integral converges, and \(Q\) is positive definite because for every \(v\ne0\) its quadratic form integrates the strictly positive function \(\|e^{tL}v\|^2\). Differentiating under the integral gives the **exact Lyapunov identity**
\[
L^*Q+QL=\int_0^\infty \frac{d}{dt}\bigl((e^{tL})^*e^{tL}\bigr)\,dt=-I.
\]
Thus, for \(z\ne0\),
\[
\frac{d}{dt}\|e^{tL}z\|_Q^2
=\langle(L^*Q+QL)e^{tL}z,e^{tL}z\rangle
=-\|e^{tL}z\|_{\rm Eucl}^2<0.
\tag{1}
\]
Moreover, \(\|e^{tL}z\|_Q\to0\) as \(t\to+\infty\). As \(t\to-\infty\) it tends to infinity: since \(\|e^{sL}\|\to0\) as \(s\to+\infty\), the inequality
\(\|z\|\le\|e^{sL}\|\|e^{-sL}z\|\) forces \(\|e^{-sL}z\|\to\infty\), and the Euclidean and \(Q\)-norms are equivalent.

Put \(S_Q^3=\{z:\|z\|_Q=1\}\), a smooth ellipsoidal three-sphere. For each \(z\ne0\), equation (1) and the endpoint limits give a **unique** real \(t\) with
\(\|e^{-tL}z\|_Q=1\), and \(\xi=e^{-tL}z\in S_Q^3\). Hence
\[
\Phi:S_Q^3\times\mathbb R\longrightarrow\mathbb C^2\setminus\{0\},
\quad(\xi,t)\longmapsto e^{tL}\xi
\tag{2}
\]
is bijective. Equation (1) makes the level crossing transverse, so the implicit function theorem makes its inverse smooth; (2) is a diffeomorphism. It intertwines the deck action exactly:
\[
A\Phi(\xi,t)=e^{(t+1)L}\xi=\Phi(\xi,t+1).
\]
Consequently
\[
(\mathbb C^2\setminus\{0\})/\langle A\rangle
\cong_{\mathrm{diff}} S_Q^3\times(\mathbb R/\mathbb Z)
\cong_{\mathrm{diff}} S^3\times S^1.
\tag{3}
\]
There is no implicit claim that the diffeomorphism is holomorphic.

## 2. Nonlinear triangular contractions

For \(p>1\), \(|\lambda|<1\) implies \(\lambda-\lambda^p\ne0\). Define the globally invertible triangular polynomial map
\[
H(z_1,z_2)=\bigl(z_1,z_2+c z_1^p\bigr),\qquad
c=(\lambda-\lambda^p)^{-1}.
\]
Its inverse is \(H^{-1}(w_1,w_2)=(w_1,w_2-cw_1^p)\), and direct substitution yields
\[
H\circ F=(\lambda I)\circ H
\quad\text{since }1+c\lambda^p=\lambda c.
\tag{4}
\]
The map fixes the origin and therefore restricts to a biholomorphism of the punctured planes intertwining the \(\mathbb Z\)-actions. Thus \(X_F\) is actually **biholomorphic** to the scalar Hopf surface \(X_{\lambda I}\); by (3) it is diffeomorphic to \(S^3\times S^1\).

Equation (4) is used here as a reduction step. Its existence and the distinct \(p=1\) behavior were already touched upon in previous Hopf automorphism audit notes and are **not counted as new findings**.

## 3. Cohomology and the stronger obstruction

The integral cohomology of \(S^3\) and \(S^1\) is torsion free, so the elementary product/Künneth calculation gives
\[
H^*(X_F;\mathbb Z)=H^*(S^3\times S^1;\mathbb Z)
\]
as graded rings. Let \(a\in H^1\) and \(b\in H^3\) be the standard generators. Then \(a\smile b\) generates \(H^4\), and \(H^2=0\).

If a compact oriented real four-manifold admits a symplectic form \(\Omega\), then \(\int\Omega^2>0\) with its symplectic orientation. But here \(H^2_{\rm dR}=0\), so any closed two-form has the form \(\Omega=d\alpha\); Stokes implies
\[
\int_{X_F}\Omega^2=\int_{X_F}d(\alpha\wedge\Omega)=0,
\]
a contradiction. Thus **no symplectic structure exists** on these smooth quotients, in particular no Kähler structure. This proof does not need the printed Hodge-parity input at Theorem 10.47.13.

## 4. Direct audit of the printed proof

The printed Theorem 23.3.3 is **not refuted**. Its calculation of \(F^k\), including \(k\lambda^{k-1}\) at \(p=1\) and the bounded geometric sum for \(p>1\), is correct (lines 27–34). The weighted norm at lines 36–42 indeed contracts because \(a^{-1}<1-|\lambda|\). Uniform contraction on compacta, freeness and finite-intersection proper discontinuity are correctly sequenced (line 44). The compact annulus \(\overline B\setminus F(B)\) surjects onto the quotient (line 46); no boundary regularity assumption is tacitly used. The covering and fundamental-group argument (lines 48–50) yields \(\mathbb Z\) as claimed. Finally, the Hodge-theoretic parity argument is correctly applied **only after** compactness has been established.

The stronger proof above checks the topology without upgrading any unverified upstream assertion to a full dependency-chain certificate. No new confirmed error or independent gap in the printed §23.3 theorem was found.

**Proposed correction (audit-only):** append an optional remark after Theorem 23.3.3 stating that \(X_F\cong_{\rm diff}S^3\times S^1\), with the Lyapunov sphere cross-section construction and \(b_2=0\) symplectic obstruction. Preserve the original statement, source attribution, permanent tags, and the existing proofs. In any discussion of distinct complex types, explicitly avoid presenting the \(p>1\) triangular family as a new holomorphic type, because (4) already conjugates it to the scalar case.

**Affected dependents:** results that use §23.3.3 only for \(\pi_1\), \(b_1\), compactness, or non-Kählerness remain correct. The new \(H^2=0\) and no-symplectic statement can strengthen the hypotheses checks in Hopf/LCK and cohomological comparisons (§23.2, §19.9), but neither section is thereby certified. The separate general Hopf mass estimates of §23.1 are unaffected.

**Coverage:** full direct reading of the current §23.3 mathematical text, lines 5–53, its one theorem and proof; **+1 whole-section direct audit**, +0 newly certified upstream chains. Historical first-visit status **unreconciled**: previous §23.3 partial audit notes exist. The current actual chapter inventory remains 25 chapters / 747 sections, not 747 verified sections. No builds, tests, CI, main/source/registry/tag or website changes. Demailly approximation/regularization and the dedicated Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**, not certified. The source label here names a *Hopf quotient theorem*, not any excluded regularization result.
