# Strong quantitative stability of product weak adjoints

Date: 2026-11-26. Production main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Prior audit branch head: 13b685e167fa33c8fdd1ad781de2aa046ceb0af9.

## Finding POME-PRODUCT-ADJOINT-L2-LIPSCHITZ-001

Severity: low. Status: **verified conditional deduction**, not a false printed theorem or demonstrated proof gap. Proposed correction: add the following stronger conclusion to Proposition 11.45.18 as an optional corollary, retaining the original statement. No production changes.

### Anchors and assumptions

Integrated file: `docs/sections/normalization-and-weak-adjoint-measures--selection-for-logarithmic-models-on-products/index.html`, blob f0b92ec93b3184a6af1c804b07bd3454b957d6bc.
Theorem 11.45.16 (permanent tag 23BDF62163E8), lines 303–355; Proposition 11.45.18 (132C5E1825BF), lines 360–395. Lemma 11.45.15 (85744C3971DC), lines 269–298, is the continuous-potential resolvent input. The hypotheses are precisely those of Proposition 11.45.18: two projective lines, mass-one Fubini–Study forms \(\omega_1,\omega_2\), \(dW=\omega_1\wedge\omega_2\), continuous positive \(A(x)\) with integral \(a>0\), smooth positive \(b(x)\), and \(\Omega=A\omega_1+b\omega_2\). Smooth positive residuals \(\Omega_j=\eta+dd^cw_j\) converge uniformly to \(\Omega\). Their normalized smooth adjoint weights satisfy \(dd^c(\rho_j\Omega_j)=0\), \(\int\rho_j\Omega_j^2=1\). We use their existence from Theorem 11.4.2 exactly as the printed proof does.

Write \(\epsilon_j=\|\Omega_j-\Omega\|_{C^0}\) in the fixed product metric, \(p_j=\rho_j\Omega_j^2/dW\), \(p=A/a\), \(\rho=1/(2ab)\). There is a constant \(C\) depending only on the limiting positive \(A,b\) and the fixed metric such that, for all sufficiently small \(\epsilon_j\),
\[
 \|p_j-p\|_{L^2(dW)}+
 \|\rho_j-\rho\|_{L^2(dW)}+
 \|\rho_j\Omega_j-\rho\Omega\|_{L^2(dW)}
 \le C\epsilon_j .
\]
The last norm is the coefficient norm induced by the fixed product metric. In particular the probability convergence holds in total variation, with no derivatives of the metric perturbation in the estimate. The result is valid for an arbitrary directed net of such smooth residuals converging uniformly.

### Proof

Use the printed Laplacian convention \(\Delta_i\) of the unit round sphere (mass-one area measure). For smooth real \(h\), put \(Lh=A^{-1}\Delta_1h+b^{-1}\Delta_2h\), \(c(x)=A(x)/b(x)\), \(g=A Lh\). Decompose \(h=\sum_k h_k(x)e_k(y)\), \(g=\sum_k g_k(x)e_k(y)\) in an orthonormal real spherical harmonic basis in the second variable, with \(-\Delta_2e_k=\lambda_k e_k\). Then
\[
 (\Delta_1-\lambda_k c)h_k=g_k .
\]
Integration by parts against \(h_k\) gives, for \(\lambda_k>0\), \(\lambda_k\min c\|h_k\|_2^2\le |\langle g_k,h_k\rangle|\le\|g_k\|_2\|h_k\|_2\). For the zero mode the inequality \(\lambda_k\|h_k\|_2\le(\min c)^{-1}\|g_k\|_2\) is automatic. Parseval therefore yields \(\|\Delta_2h\|_2\le(\min c)^{-1}\|g\|_2\), and the equation yields \(\|\Delta_1h\|_2\le\|g\|_2+\|c\|_\infty\|\Delta_2h\|_2\). The integrated real Hessian identity on the round product is
\[
 \|\nabla^2 h\|_2^2=\|(\Delta_1+\Delta_2)h\|_2^2-\int\operatorname{Ric}(\nabla h,\nabla h)dW.
\]
It follows by integrating the divergence of the Hessian against the gradient and commuting covariant derivatives, whose commutator contributes Ricci. The volume normalization is a constant multiple of Riemannian volume and does not affect the identity. Ricci is nonnegative. The complex Hessian is a fixed linear projection, up to the fixed \(dd^c\) normalization, of the real Hessian on this Kähler product. Thus
\[
 \|dd^ch\|_2\le C_0\|Lh\|_2.
\]
No regularity of derivatives of \(A\) or \(b\) enters this estimate.

Define \(L_jh=2\Omega_j\wedge dd^ch/\Omega_j^2\). Uniform positivity for late indices and the elementary inverse-matrix identity \(M^{-1}-N^{-1}=M^{-1}(N-M)N^{-1}\) give
\[
 \|(L-L_j)h\|_2\le C_1\epsilon_j\|dd^ch\|_2
 \le C_2\epsilon_j\|Lh\|_2 .
\]
By distributional Stokes, \(\int L_jh\,p_jdW=0\) and \(\int Lh\,p\,dW=0\). Hence
\[
 |\langle Lh,p_j-p\rangle|\le C_2\epsilon_j\|Lh\|_2\|p_j\|_2 .
\]

The closure in real \(L^2(dW)\) of the range \(L(C^\infty)\) is exactly the orthogonal complement of \(p\). To see this, any element \(q\) orthogonal to that range defines a finite *signed* invariant measure \(q\,dW\). The harmonic-mode proof in lines 332–344 of Theorem 11.45.16 applies verbatim to signed measures: all nonconstant second-variable modes vanish by the signed-measure Lemma 11.45.15, and the zero mode is a constant multiple of \(\omega_1\). Testing with continuous products after multiplying by \(A\) gives \(q\,dW=C A\,dW\). No positivity or probability normalization was used in those steps. Conversely \(p\) is invariant. Hilbert orthogonality proves the range closure without an elliptic surjectivity assumption.

Let \(r_j\) be the orthogonal projection of \(p_j-p\) onto \(p^\perp\). Density of the range and the preceding estimate imply \(\|r_j\|_2\le C_2\epsilon_j\|p_j\|_2\). Write \(p_j-p=r_j+t_jp\). Integrating and using the probability normalizations gives \(t_j=-\int r_jdW\), so \(|t_j|\le\|r_j\|_2\) since \(dW(X)=1\). Consequently
\[
 \|p_j-p\|_2\le C_3\epsilon_j(\|p\|_2+\|p_j-p\|_2).
\]
For \(C_3\epsilon_j\le1/2\), absorption gives \(\|p_j-p\|_2\le 2 C_3\|p\|_2\epsilon_j\). This is an estimate for each residual individually, not an inference from sequential compactness.

Finally \(D_j=\Omega_j^2/dW\) and \(D=\Omega^2/dW\) have a uniform positive lower bound and \(\|D_j-D\|_\infty=O(\epsilon_j)\). Use \(\rho_j=p_j/D_j\), \(\rho=p/D\) to obtain the weight estimate; multiply by the uniformly bounded forms to obtain the current coefficient estimate. Cauchy–Schwarz converts the probability estimate to total variation.

The linear order for the probability is optimal: choose smooth \(A=a\) constant, and a nonzero smooth mean-zero \(f(x)\). By the mass-zero Green inversion used in lines 394–395, take a smooth \(w\) with \(dd^cw=f\omega_1\). For \(\Omega_t=(a+tf)\omega_1+b\omega_2\), \(|t|\) small, the explicit normalized adjoint is \(\rho_t=1/(2ab)\), \(p_t=(a+tf)/a\), by the same closed weighted-form computation as in Theorem 11.45.16. Thus \(\|p_t-p\|_2=|t|\|f\|_2/a\) and \(\|p_t-p\|_1=|t|\|f\|_1/a\) while \(\|\Omega_t-\Omega\|_{C^0}=|t|\|f\omega_1\|_{C^0}\).

This is restricted to the product limit and smooth approximating adjoints (or L² densities already known to be invariant). It does not establish general weak-adjoint uniqueness or regularity for arbitrary continuous Hermitian metrics. The previously recorded POME-HERM-ADJOINT-C0-LP-LIPSCHITZ-001 uses a general p>2n Fredholm premise and yields L^{p'} stability; the present elementary separated coercivity gives L² here without that Fredholm premise. POME-CRITICAL-SUPPORT-UHC-001 and POME-LOGMODEL-FIRST-ORDER-001 remain earlier findings, not new results. This spectral calculation is unrelated to the deferred Demailly approximation and its dedicated L² proof-completion programme.

## Direct coverage and checks

All four sections below were read at the pinned main. “Whole direct conditional” denotes direct reading of the complete mathematical passage, not certification of all dependencies. Legacy first-visit status is not claimed.

- §11.36: `docs/sections/normalization-and-weak-adjoint-measures--bounded-measurable-densities-and-stability/index.html`, blob 9c045c6e7a5bc4f0830874030c18dad0cafae905, lines 7–55; Theorem 11.36.1 tag 99653D7759E2. Uniformly bounded approximation, dual-value supremum over measurable tests, weak L¹ compactness and uniform-integrability splitting correctly allow moving test and measure. Conditional on §§11.33.5, 11.35.2, 11.35.4. Prior all-net stability result not recounted.
- §11.42: `docs/sections/normalization-and-weak-adjoint-measures--the-mass-determined-by-the-functional/index.html`, blob 9766d5ddf698ae153a6ba635ab9933d471356d67, lines 7–79; Theorem 11.42.1 tag 1DCF668EBCCF, Examples 11.42.3/.4 tags C6588E30CFF6/0B7F3ACBCCC4. Checked integrating fixed ordinary-type mass, sign of log scalar and support, hyperplane coefficient and multiplier ideal floor, alternating point-pole example, and nonclosed residual form. Existence and prescribed-type uniqueness (explicit external closed-big-class input in §25.6), envelope type and non-pluripolar mass invariance remain dependencies, not certifications.
- §11.44: `docs/sections/normalization-and-weak-adjoint-measures--selection-by-a-vanishing-exponential-parameter/index.html`, blob aaa0a6363ade7e865aeea7ab43b7770748fedbaa, lines 7–316; Theorem 11.44.2 tag 3F95A960C6FA, Propositions 11.44.5/.9 tags 91FDE4AB5C22/AD91D203DE64, Lemmas 11.44.15/.19 tags FA5BBA96CCC3/0E0F3A0EC129. Checked root-density lattice norm triangle, positive norming extension on the zero locus, exponent moment bound, scalar centering, forcing-probability sign, monotone continuous approximation of -lambda s, portmanteau via truncation from below, and final greatestness and sup normalization. Conditional on named comparison, mixed-product, moment, existence and compactness inputs (§§15.13–17, 5.28.9, 5.26.2, 5.25.2, 5.24.3). Any regularization inputs in these chains remain deferred-by-user.
- §11.45: pinned path/blob above, lines 7–443; Proposition 11.45.3 DA11AEC1C7C7, Lemma 11.45.4 688DA0FB893F, Theorem 11.45.9 72A7418012F7, Corollary 11.45.13 86F268014BE0, Lemma 11.45.15 85744C3971DC, Theorem 11.45.16 23BDF62163E8, Proposition 11.45.18 132C5E1825BF, Example 11.45.19 3C22B09DCF87. Checked tangent slope and matching at the radial interface, no circle atom, removal of divisor, contraction constants, Green kernel normalization and logarithmic tails, scalar centering for varying data, critical coefficient comparison, signed resolvent uniqueness, linearization and weak limits, height moment 5/24, and the explicit pole-filling example. Conditional on divisorial removal, local product, greatest-subsolution existence/uniqueness, capacity bound and Gauduchon inputs cited there. The elementary explicit pole-filling example is a counterexample about adjoints, not a reopening of regularization. The new deduction affects only Proposition 11.45.18 and its potential use in the weak-adjoint problem; no conclusion for the general conjecture §24.7.1.

Matrix comparison: extracted actual section numbers from the current main docs/index.html ToC; 747 numbers, exactly 747 distinct matrix row numbers, empty differences. No production files modified. No tests, builds or CI run. Zero new confirmed printed errors, zero demonstrated gaps, zero complete upstream certificates; one new conditional deduction. The entire excluded programme remains deferred-by-user, not resolved or certified.
