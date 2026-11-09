# Gauduchon derivative: cofactor inversion and quantitative stability (2026-11-09)

**Stable finding:** \`POME-GAUD-DERIVATIVE-COFACTOR-STABILITY-001\`  
**Classification:** low / **verified conditional deduction** (no false printed statement, no claim of full upstream verification).  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Primary integrated reading edition:** \`docs/sections/a-gauduchon-variational-volume--recovering-a-positive-class-from-its-gauduchon-derivative/index.html\`, blob \`829d10abfa8f92c7c77fde66704adb6486ccdc93\`, section tag \`9141861B4F50\`; Proposition 12.5.1, source \`non-kahler-pluripotential-theory:765CFEAC\`, permanent tag \`4BBB232A044C\`, physical lines 22–43, especially formulas at 23–25 and proof at 32–35. Section setup and derivative representation are at lines 7–19.

**Other integrated inputs directly crosschecked:** Theorem 12.2.3, \`docs/sections/a-gauduchon-variational-volume--the-quotient-and-the-smooth-equation/index.html\`, blob \`9ec67161d46b3ba20afa1b1c9a0c84f29322763e\`, source \`non-kahler-pluripotential-theory:876DF057\`, permanent \`2DB664A6EFDF\`, starting physical line 59; Proposition 12.3.2, \`docs/sections/a-gauduchon-variational-volume--the-equality-case-of-concavity-and-the-first-variation/index.html\`, blob \`d94e3fc055b0642a86495c27ad8f5af6f24f17d1\`, source \`non-kahler-pluripotential-theory:6D3F0AB8\`, permanent \`94AFD9E43DE0\`, starting line 34. Their general elliptic existence/smooth-dependence proofs are **inputs, not certified** in this note.

## Exact claim and hypotheses

Let \((X,\omega_0)\) be compact Hermitian of complex dimension \(n\ge2\), let \(\mu=\rho\,\omega_0^n\) with a smooth strictly positive function \(\rho\), and choose \(\theta\in\mathscr P\) in the precise setting of §§12.2–12.5. Put
\[
 \lambda=\lambda_\mu(\theta)>0,\qquad
 \Xi=\frac{\gamma_\theta^{\,n-1}}{D_\mu(\gamma_\theta)}.
\]
Here \(\Xi\) is the positive \((n-1,n-1)\)-form representing \((d\lambda_\mu)_\theta\), **not** a normalized \((1,1)\)-form. At each point, in a unitary frame for \(\omega_0\), define the positive Hermitian matrix \(B=B_\Xi\) by the **wedge normalization**
\[
 \boxed{\quad
 \Xi\wedge\eta
 =\frac1n\operatorname{tr}(B H_\eta)\,\omega_0^n
 \quad\text{for every real }(1,1)\text{-form }\eta ,
 \quad}
\]
where \(H_\eta\) is the Hermitian coefficient matrix of \(\eta\) in that frame. This definition fixes all factorial and cofactor conventions; under a unitary change of frame, \(B\) changes by unitary conjugation.

**Pointwise reconstruction, eliminating the positive \((n-1)\)-st root:**
\[
 \boxed{\quad H_{\Omega_\theta}
   =\lambda\,\rho^{1/n}\,(\det B)^{1/n} B^{-1}.\quad} \tag{A}
\]
In particular, \(\det H_{\Omega_\theta}=\lambda^n\rho\) and \(\Omega_\theta^n=\lambda^n\mu\). Formula (A) is a direct, quantitative reformulation of the correct Proposition 12.5.1, **conditional** on its differentiated and normalized Gauduchon solution setup.

Write \(\mathcal R(B)=(\det B)^{1/n}B^{-1}\). If two such derivative matrices \(B_1,B_2\) satisfy the *uniform pointwise ellipticity bounds*
\[
 0<a I\le B_i(x)\le bI \qquad(i=1,2;\ x\in X),
\]
then, with the operator norm relative to \(\omega_0\),
\[
 \boxed{\;
 \|\Omega_1-\Omega_2\|_{C^0(\omega_0)}
 \le \|\rho\|_\infty^{1/n}
 \left[\frac ba|\lambda_1-\lambda_2|
 +\frac{2b}{a^2}\max(\lambda_1,\lambda_2)
       \|B_1-B_2\|_{C^0(\omega_0)}\right].
 \;} \tag{B}
\]
Thus, on ellipticity-bounded sets, **the inverse map from value plus first derivative to the solution metric is explicitly locally Lipschitz in \(C^0\)**. This is *one-sided inverse stability*, not an assertion that \(\theta\mapsto d\lambda_\mu\) is locally bi-Lipschitz or that its PDE dependencies have been independently proved.

## Complete algebraic proof

Let \(A=H_{\widehat\gamma}\), where Proposition 12.5.1 defines \(\widehat\gamma^{n-1}=\Xi\) and \(D_\mu(\widehat\gamma)=1\). Diagonalizing \(A\) in a unitary frame, the standard wedge identity for any Hermitian \(H\) is
\[
 \widehat\gamma^{n-1}\wedge\eta
 =\frac1n\det(A)\operatorname{tr}(A^{-1}H)\,\omega_0^n .
\]
For a general (not necessarily diagonal) \(A\), this follows by unitary conjugation; for a diagonal \(A\) it follows by expanding the wedge and keeping only the matching missing-index terms. Comparing with the definition of \(B\) gives
\[
 B=(\det A)A^{-1},\qquad
 \det B=(\det A)^{n-1},\qquad
 A=(\det B)^{1/(n-1)}B^{-1}.
\]
Proposition 12.5.1 gives
\[
 \Omega_\theta
 =\lambda\,(\mu/\widehat\gamma^n)^{1/n}\widehat\gamma ,
\]
so its matrix is \(\lambda(\rho/\det A)^{1/n}A\).
Substituting the two identities above yields (A). In particular \(\det \mathcal R(B)=1\), without a missing \(n!\) or an erroneous power of \(\rho\).

For stability, differentiating on the open positive-definite Hermitian cone gives, for Hermitian \(H\),
\[
 D\mathcal R_B[H]
 =(\det B)^{1/n}
 \left(\frac1n\operatorname{tr}(B^{-1}H)B^{-1}
          -B^{-1}HB^{-1}\right).
\]
On \(aI\le B\le bI\), we have
\[
 (\det B)^{1/n}\le b,\quad
 \|B^{-1}\|\le a^{-1},\quad
 \frac1n|\operatorname{tr}(B^{-1}H)|\le a^{-1}\|H\|,
\]
hence \(\|D\mathcal R_B[H]\|\le2ba^{-2}\|H\|\). The segment joining \(B_1\) to \(B_2\) remains in the same closed ellipticity interval, so integration along that segment proves
\(\|\mathcal R(B_1)-\mathcal R(B_2)\|\le2ba^{-2}\|B_1-B_2\|\).
Moreover \(\|\mathcal R(B_i)\|\le b/a\). Expanding the difference of the two copies of (A), applying these bounds and taking suprema proves (B). No limiting operation on currents, regularization, compactness theorem, or unproved PDE estimate is used in this *finite-dimensional matrix calculation*.

Sanity check: if \(B=I\) and \(\mu=\omega_0^n\), then (A) gives \(\Omega_\theta=\lambda\omega_0\). For any scalar \(c>0\), \(\mathcal R(cB)=\mathcal R(B)\), as required by the fact that the derivative alone determines a metric only up to its scalar volume normalization.

## Status and proposed placement

- **Verified conditional deduction, low severity.** The printed Proposition 12.5.1 is **not** false. Formula (A) refines the inverse construction and (B) supplies a stability bound absent from the selected printed passage.
- **Suggested patch only:** add a short coordinate-free/locally unitary *Remark* after Proposition 12.5.1 stating the wedge-normalized cofactor matrix and (A), optionally the ellipticity-bounded estimate (B). Preserve the original statement, proof, history, source labels and permanent tags. **No source/reading-edition patch is made in this audit branch.**
- **Affected dependencies:** §§12.2.3, 12.3.2 and 12.5.1 (assumed as printed); potentially quantitative reconstruction arguments in §12.6. No downstream statement has been shown false or fully certified. Uniform ellipticity is an explicit assumption on the compared *derivative matrices*, not automatically obtained from \(\theta\in\mathscr P\) with a universal constant.
- **Exclusions respected:** no Demailly approximation/regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale atlas, or positivity-loss proof programme was invoked or opened; previous notes on these remain **deferred-by-user**, never resolved or certified.
- **Coverage:** new explicit cofactor/stability subcalculation in previously partly examined §12.5; §§12.2 and 12.3 dependency statements only; **zero new first-visited numbered sections, zero complete mathematical-section certifications**. Main table of contents remains 25 chapters and 747 sections; no build/CI/test/formal proof or publication is asserted.
