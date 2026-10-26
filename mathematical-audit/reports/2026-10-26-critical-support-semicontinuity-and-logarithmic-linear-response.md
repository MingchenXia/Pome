# 2026-10-26 — critical supporting probabilities and linear response of a logarithmic product model

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit base:** `336e7987e04aacf0e430e060d50a641e7e20255f`. **Scope:** first selected integrated proof-level inspection of §§11.44–11.45 (not entire-section certification). Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programme are **deferred-by-user**, neither inspected nor certified here. No underlying theorem, source, proof registry, canonical tag or published page is edited.

## POME-CRITICAL-SUPPORT-UHC-001

**Severity:** low. **Status:** verified conditional deduction; no false printed theorem or confirmed gap. **Proposal:** optionally state the density-integrability and upper-hemicontinuity corollary immediately after Proposition 11.44.9. **Dependents:** the supporting-probability normalization in Theorem 11.44.2 and comparison of critical scalars when right-hand densities vary. The result does not claim lower hemicontinuity of the entire face of supporting probabilities.

**Integrated sources:**
- `docs/sections/normalization-and-weak-adjoint-measures--selection-by-a-vanishing-exponential-parameter/index.html`, **main blob** `aaa0a6363ade7e865aeea7ab43b7770748fedbaa`; §11.44, source book `non-kahler-pluripotential-theory`, section permanent tag `DB96849B14F8`.
- Eq. 11.44.1 (permanent `CC5ED4480663`), physical lines 13–20: critical-scalar transform \(\kappa_f\) and \(\mathcal P_f\).
- Proposition 11.44.5 (permanent `91FDE4AB5C22`, source tag `84EE34F5`), lines 49–80: the lattice norm \(N\), with \(1<q<p\), \(\ell=nq\), and its \(L^\ell\)-Lipschitz constant \(C_q\).
- Proposition 11.44.9 (permanent `AD91D203DE64`, source tag `260BBDC7`), lines 89–170, especially equations 11.44.8/10, permanent tags `75A33AC0E5F0`/`829BF6353639`: positive norming duals and \(d\nu=A^{-1}a\eta\,dV\).
- Theorem 11.44.2 (permanent `3F95A960C6FA`), lines 24–41 and proof Steps 1–5 at lines 272–311, inspected specifically for the use of supporting measures and one-sided weak limits.

**Precisely qualified consequence.** Let \(X\) be compact of complex dimension \(n\), \(\theta\) a smooth big real \((1,1)\)-form, \(dV\) the positive smooth reference volume, and \(1<q<p<\infty\). Fix nonzero \(f\ge0\) in \(L^p(dV)\), and consider nonzero \(f_j\ge0\) in \(L^p(dV)\) such that \(f_j\to f\) in \(L^q\). Then:

1. For each \(M>0\), the critical support functionals converge **uniformly for \(\|r\|_\infty\le M\)**:
   \[
   \sup_{\|r\|_\infty\le M}|\kappa_{f_j}(r)-\kappa_f(r)|
   \le \frac{2nC_q}{A}\bigl(e^{2M/n}+1\bigr)
   \|f_j-f\|_q^{1/n}
   \quad\text{for all sufficiently large }j,
   \]
   where \(a=f^{1/n}\), \(A=N(a)=c(f)^{-1/n}>0\), and \(C_q\) is the printed norm bound.
2. If \(\nu_j\in\mathcal P_{f_j}\) and \(\nu_j\rightharpoonup\nu\) along any subsequence, then \(\nu\in\mathcal P_f\). This is **upper hemicontinuity**, not a Hausdorff-convergence or lower-hemicontinuity assertion.
3. For any fixed \(f\in L^p\) and \(1<q<p\), every \(\nu\in\mathcal P_f\) has a density \(h=d\nu/dV\) in \(L^r\), where
   \[
   \frac1r=1-\frac1{nq}+\frac1{np},
   \qquad
   r=\frac{npq}{npq-p+q}>1,
   \qquad
   \|h\|_r\le C_q A^{-1}\|f\|_p^{1/n}.
   \]
   If also \(\sup_j\|f_j\|_p<\infty\), these bounds apply uniformly to the entire union of \(\mathcal P_{f_j}\) for sufficiently large \(j\).

**Proof.** Put \(a_j=f_j^{1/n}\), \(d_j=\|a_j-a\|_{nq}\). By the scalar inequality \(|x^{1/n}-y^{1/n}|^n\le |x-y|\) for \(x,y\ge0\),
\(d_j\le\|f_j-f\|_q^{1/n}\). The lattice-norm Lipschitz estimate implies
\(|N(a_j)-A|\le C_qd_j\). For \(\|r\|_\infty\le M\),
\[
|N(a_je^{r/n})-N(ae^{r/n})|\le C_qe^{M/n}d_j.
\]
Lattice monotonicity and homogeneity give
\(e^{-M/n}N(a_j)\le N(a_je^{r/n})\le e^{M/n}N(a_j)\), and similarly with \(a\). For large \(j\), \(N(a_j)\ge A/2\). Applying \(|\log x-\log y|\le |x-y|/\min(x,y)\) twice to the printed identity
\(\kappa_f(r)=n\log(N(ae^{r/n})/A)\) yields the displayed constant. If \(\nu_j\) converges weakly, pass to the limit in \(\int r\,d\nu_j\le\kappa_{f_j}(r)\) for every \(r\in C(X)\). This gives \(\nu\in\mathcal P_f\).

Finally the printed dual representation gives \(h=A^{-1}a\eta\) with \(\|\eta\|_{(nq)'}\le C_q\). Hölder between \(a\in L^{np}\) and \(\eta\in L^{(nq)'}\) gives the claimed exponent and norm. For varying \(f_j\), substitute \(A_j=N(a_j)\ge A/2\), yielding the uniform statement. No concentration or claim about convergence of an individually selected extreme supporting measure follows from these estimates.

**Verification limits:** The lattice-norm property and dual representation are *conditional inputs* from the printed Propositions 11.44.5/9, rather than independently re-proved through their noncompact analytic ancestors. Their displayed Hölder, convexity, and weak-dual passages were checked. This does not certify the entire exponential Monge–Ampère existence chain.

## POME-LOGMODEL-FIRST-ORDER-001

**Severity:** low. **Status:** verified conditional deduction; not a repair or a false-theorem claim. **Proposal:** optional quantitative fixed-data addendum after Theorem 11.45.9. **Dependents:** the normalization scalar, residual Green potential and selected fixed-background limit of §11.45. The claim is **for fixed data only**, not for arbitrary varying \(a_j,d_j,b_j,H_j\).

**Integrated sources:**
- `docs/sections/normalization-and-weak-adjoint-measures--selection-for-logarithmic-models-on-products/index.html`, **main blob** `f0b92ec93b3184a6af1c804b07bd3454b957d6bc`; §11.45 permanent tag `A167FA614566`, source book `non-kahler-pluripotential-theory`.
- Proposition 11.45.3 (permanent `DA11AEC1C7C7`, source tag `79CC743A`), lines 26–70, defines the logarithmic reference and continuous residual.
- Theorem 11.45.9 (permanent `72A7418012F7`, source tag `01FA98A6`), lines 108–142 and proof lines 147–218, in particular fixed-point density, derivative and uniform contraction at lines 152–170, exact potential equation 11.45.11 (permanent `9E6339686644`) at lines 172–185, and centering scalar at lines 205–217.
- Lemma 11.45.4 (permanent `688DA0FB893F`), lines 76–103, is used conditionally only to identify the contraction solution with the greatest ordinary-type solution; its global existence dependencies are not certified here.

**Quantitative fixed-data refinement.** Retain the hypotheses and notation of §11.45, but fix \(a,d,b,H\) and let \(\sigma\downarrow0\). All integrals in the following formulas are over \(\mathbb P^1\) with \(\omega_1\). Write
\[
m=\int H,\quad \psi=d\log\ell,\quad A_0=\frac{aH}{m},
\quad w_0=G*(A_0-a),\quad t=\psi+w_0,\quad
J=\frac1m\int Ht.
\]
Define the continuous mean-zero function
\[
w_1=G*\bigl[A_0(t-J)\bigr],
\qquad \int A_0(t-J)=0,
\]
and the finite scalar
\[
K_1=\frac1m\int Hw_1+
\frac1{2m}\int Ht^2-\frac12J^2.
\]
For the fixed-point residual \(w_\sigma\) and its normalizer
\(Z_\sigma=\int H e^{\sigma(\psi+w_\sigma)}\), one has
\[
\boxed{\|w_\sigma-w_0-\sigma w_1\|_{C^0}=O(\sigma^2)},\qquad
\boxed{\frac1\sigma\log\frac{Z_\sigma}{m}
=J+\sigma K_1+O(\sigma^2).}
\]
Consequently, writing \(c_0=a/m\) and \(s_\sigma\) for the printed greatest ordinary-type solution,
\[
\boxed{
s_\sigma-\frac{\log c_0}{\sigma}
=\psi+w_0-J+\sigma(w_1-K_1)+O(\sigma^2).
}
\]
Here the error is **uniform after subtracting the common logarithmic pole \(\psi\)**, hence is an ordinary continuous residual extension across the divisor \(D\); it is not a claim that the singular potentials themselves are bounded. The normalization scalar \(c_\sigma=e^{\sigma\sup_Xs_\sigma}\) also satisfies
\[
\boxed{c_\sigma=c_0\bigl(1+\sigma(S_0-J)+O(\sigma^2)\bigr),}
\quad S_0=\sup_X(\psi+w_0).
\]

**Proof.** The Green kernel has \(C_2:=\sup_x\|G(x,\cdot)\|_{L^2(\omega_1)}<\infty\) by rotation invariance and square-integrability of the logarithmic singularity. Every fixed finite moment of \(|\psi|=d|\log\ell|\) is finite. Thus \(\|G*F\|_\infty\le C_2\|F\|_2\), also for the weighted logarithmic densities below.

The printed fixed-point map is
\[
T_\sigma(w)=G*\left[\frac{aHe^{\sigma(\psi+w)}}{\int He^{\sigma(\psi+w)}}-a\right]
\]
on a fixed uniformly bounded mean-zero ball. Its printed Lipschitz constant is \(O(\sigma)\) there. Since \(\psi\le0\), for bounded \(w\), the estimate
\(|e^{\sigma(\psi+w)}-1|\le C\sigma(|\psi|+1)\)
holds for \(\sigma\in(0,1]\). This gives
\(\|T_\sigma(w_0)-w_0\|_\infty=O(\sigma)\), and contraction gives
\(\|w_\sigma-w_0\|_\infty=O(\sigma)\).

Uniformly for those \(\sigma\), Taylor's remainder is bounded by
\(C\sigma^2(|\psi|+1)^2\) in \(L^2\) (the exponential is bounded above because \(\psi\le0\) and \(w_\sigma\) is bounded). Since \(w_\sigma=w_0+O(\sigma)\),
\[
e^{\sigma(\psi+w_\sigma)}
=1+\sigma t+O_{L^2}(\sigma^2),\qquad
Z_\sigma=m+\sigma\int Ht+O(\sigma^2).
\]
Therefore the density in \(T_\sigma\) is
\(A_0+\sigma A_0(t-J)+O_{L^2}(\sigma^2)\);
convolution with \(G\) proves the first boxed expansion. Taylor's third-order remainder is bounded in \(L^1\) by \(C\sigma^3(|\psi|+1)^3\), so after substituting \(w_\sigma=w_0+\sigma w_1+O(\sigma^2)\),
\[
Z_\sigma=m+\sigma\int Ht+
\sigma^2\left(\int Hw_1+\frac12\int Ht^2\right)
+O(\sigma^3).
\]
Expanding the logarithm gives the second boxed formula and its explicit \(K_1\). The exact identity (11.45.11) is
\(s_\sigma=\psi+w_\sigma+\sigma^{-1}\log(a/Z_\sigma)\), so subtracting \(\sigma^{-1}\log(a/m)\) yields the residual expansion. Finally \(S_\sigma=\sup_X(\psi+w_\sigma)=S_0+O(\sigma)\), since \(\psi\) is fixed and \(\|w_\sigma-w_0\|_\infty=O(\sigma)\). Apply the printed exact formula \(c_\sigma=ae^{\sigma S_\sigma}/Z_\sigma\).

**Verification limits:** This is a direct Green-kernel and uniform-contraction argument for the *fixed public model*. It does not open the excluded Demailly/multiscale/Bergman/OT programme, nor does it imply uniform first-order rates when the underlying data vary without an explicit rate. Existence/identification of the greatest global ordinary-type solution stays conditional on the printed Lemma 11.45.4 and its independent dependencies.

## Coverage and disposition

Selected proof-level, first audit: §11.44 Proposition 11.44.5 and 11.44.9, equations 11.44.1/8/10, Step 1 and weak-dual steps of Theorem 11.44.2; §11.45 Proposition 11.45.3 (notation), Lemma 11.45.4 (statement and reduction only), Theorem 11.45.9 fixed-point and centering steps 108–218. Neither full section nor upstream analytic existence is certified. The excluded regularization programme remains **deferred-by-user**, not resolved. No mathematical-body/registry/canonicalization edits, no tests/build/CI/formal verification/site publication.
