# 2026-11-18 audit: exact quadratic energy gap for classical Green equilibrium

**Stable finding ID:** POME-CLASS-GREEN-EQUILIBRIUM-QUADRATIC-GAP-001  
**Classification:** low / **verified conditional deduction** (quantitative strengthening).  
**Verdict on printed results:** Propositions 4.2.11 and 4.2.12 are not refuted; this is *not* a confirmed error, proof repair, or whole-section certification.  
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Integrated file:** docs/sections/fine-topology-and-balayage/index.html; blob d4c8eed09391441b4b6d13e2fa402a60da70be0d.

## Precise anchors, provenance and hypotheses

* Proposition 4.2.11, source label **foundations-of-pluripotential-theory:0EBEB570**, permanent tag **2BC493B5F349**, physical lines **196–200**: finite Green energy is the squared \(L^2\) norm of a distributional gradient, and the signed finite-energy pairing is positive definite with Cauchy–Schwarz.
* Proposition 4.2.12, source label **foundations-of-pluripotential-theory:F837B7D4**, permanent tag **AF6AC1F168D7**, physical lines **259–264** (statement), **269–283** (proof): the equilibrium Riesz measure \(\lambda_K\), capacity \(m=C_B(K)\), and their exact mutual energy identities.
* Upstream context: Theorem 4.1.26 (permanent **E54414B74C32**) supplies the quasi-everywhere equilibrium potential equality; Theorem 4.1.17 (permanent **5B4ACD7E054D**) supplies nonpolar/finite-energy equivalence. Both appear in docs/sections/potentials-energy-and-capacity/index.html, blob 4962a7cd576a64cb47fa0955dcc80cf87c3da9d1. Their entire proof chains are *not* newly certified here.

Assume \(B\subset\mathbb R^d\), \(d\ge2\), is an open Euclidean ball and \(K\Subset B\) is a compact set of positive relative Green capacity \(m=C_B(K)>0\). Denote by \(I_B(\sigma,\eta)\) the symmetric Green energy pairing, and let
\[
\lambda_K=\Delta u_K,\qquad
\lambda_K(K)=m,\qquad
e_K=\frac{\lambda_K}{m}.
\]
The exact conclusions below concern **finite-energy** competitors: \(\tau\) is a positive probability supported on \(K\) with \(I_B(\tau)<\infty\). Signed tests \(\eta\) are finite signed measures with positive and negative parts of finite Green energy, as stipulated by Proposition 4.2.11. No assertion is made for signed distributions outside this energy class or for competitors of infinite energy.

## New exact energy-gap identity

**Claim.** For every such \(\tau\),
\[
\boxed{\quad
 I_B(\tau)-\frac1m
 = I_B(\tau-e_K)
 =\bigl\|\nabla G_B(\tau-e_K)\bigr\|^2_{L^2(B)}
 \quad}
\tag{A}
\]
and for every admissible signed test \(\eta\),
\[
\boxed{\quad
\left|I_B(\tau,\eta)-I_B(e_K,\eta)\right|
\le \sqrt{I_B(\tau)-m^{-1}}\,\sqrt{I_B(\eta)}.
\quad}
\tag{B}
\]
The coefficient \(1\) and the square-root scale in (B) are sharp within the class of positive competing probabilities.

**Proof of (A).** The printed proof of Proposition 4.2.12 obtains, using \(G_B\lambda_K=1\) quasi-everywhere on \(K\) and the fact that finite-energy measures do not charge polar sets,
\[
I_B(\lambda_K)=m,\qquad
I_B(\lambda_K,\tau)=1.
\tag{1}
\]
The identical equality with \(\tau=e_K\) also holds. Consequently,
\[
I_B(e_K)=\frac1m,\qquad
I_B(e_K,\tau)=\frac1m.
\tag{2}
\]
Expanding the finite signed energy gives
\[
\begin{aligned}
I_B(\tau-e_K)
 &= I_B(\tau)+I_B(e_K)-2I_B(\tau,e_K)\\
 &= I_B(\tau)-m^{-1}.
\end{aligned}
\]
Proposition 4.2.11 supplies the last equality in (A), since the positive and negative parts of \(\tau-e_K\) have finite energy. In particular the energy gap vanishes **only if** \(\tau=e_K\), by the positive-definiteness statement there. This recovers uniqueness without invoking a compactness argument.

**Proof of (B) and net stability.** Apply the Cauchy–Schwarz inequality of Proposition 4.2.11 to \(\tau-e_K\) and \(\eta\). For any two competitors \(\tau,\nu\), the gradient realization or the triangle inequality yields
\[
I_B(\tau-\nu)^{1/2}
\le
\bigl(I_B(\tau)-m^{-1}\bigr)^{1/2}
+
\bigl(I_B(\nu)-m^{-1}\bigr)^{1/2}.
\tag{3}
\]
For an *arbitrary directed net* \((\tau_\alpha)\) of finite-energy probabilities supported on the same \(K\), if \(I_B(\tau_\alpha)\to m^{-1}\), then
\(I_B(\tau_\alpha-e_K)\to0\) **on the original net**. The conclusion is convergence in the Green energy seminorm (a norm by positive definiteness), not an unsupported claim of total-variation convergence or convergence in every weak topology. In particular no sequential compactness, subnet selection or interchange of limits is needed.

The algebraic equality (A) also holds for a finite signed *mass-one* measure \(\tau\) supported on \(K\) whose positive and negative parts have finite energy, because both parts ignore polar sets and (1) extends by linearity. The variational minimality statement continues to be asserted for positive probabilities only.

## Sharp positive-probability example

Take \(d=3\), \(B=B(0,2)\), and \(K=\{x\in\mathbb R^3:|x|=1\}\). Let \(e\) be normalized spherical area probability. The Newton kernel singularity \(c|x-y|^{-1}\) is integrable on \(K\times K\) (surface dimension two), and the regular Dirichlet Green correction is bounded on \(K\times K\); hence \(I_B(e)<\infty\) and \(m>0\). The ball and sphere are rotation invariant, so by the *uniqueness* already stated in Proposition 4.2.12, \(e=e_K\).

Let \(h(x)=x_1\) on the sphere. Then \(\int_Kh\,de=0\), \(|h|\le1\), and \(\nu=h\,e\) is a nonzero signed finite-energy measure of total mass zero. In particular \(I_B(\nu)>0\) by Proposition 4.2.11. For any real \(|t|\le1\), let
\[
 d\tau_t=(1+t h)\,de .
\]
This is a **positive probability** supported on \(K\). Bilinearity and (A) imply the exact identities
\[
 I_B(\tau_t)-m^{-1}=t^2 I_B(\nu),
 \qquad
 I_B(\tau_t-e_K,\nu)=t I_B(\nu).
\tag{4}
\]
For the admissible signed test \(\eta=\nu\), (B) is an equality for every \(t\), so the factor \(1\) cannot be reduced and a universal error scale smaller than the square root of the energy gap is impossible for energy-linear tests. This does not assert sharpness for total-variation distance or any stronger topology.

## Dependency ledger and affected conclusions

**Status:** verified conditional deduction. No incorrect printed theorem is identified. The direct new work is the precise orthogonal energy projection identity (A), its signed-dual stability bound (B), original-net convergence and the explicit sharp *positive* perturbation (4). Hypotheses for competitors and signed tests are retained exactly.

**Conditional upstream inputs:** Proposition 4.2.11 (gradient identity, positive definiteness, Cauchy–Schwarz), Proposition 4.2.12 (quasi-everywhere potential equality and \(\lambda_K\) mass identity), plus finite-energy measures' polar-null property. These were checked as integrated statements and relevant proof passages, not independently derived from the beginning of distribution/potential theory.

**Affected dependents / suggested correction:** Add an optional corollary after Proposition 4.2.12 stating (A)–(B) and the original-net energy stability. This would quantitatively strengthen the energy minimization discussion and provide a ready-made estimate for compact reduction and sweeping in later parts of §4.2 (not a claim that their entire chains are now certified). Preserve the source attribution, alternative valid formulations, canonical labels and permanent tags. No production source or canonicalization patch was made.

**Actual coverage this session:** Newly checked proof arithmetic/functional-analytic deduction in §4.2.11–12, with a targeted contextual check of §4.1.17/.26. This section had already been partially audited: **0 new first-visited numbered sections; 0 entire sections fully certified**. The current reading edition's inventory is **25 chapters, 747 numbered sections**. The separately prohibited Demailly approximation/regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programmes are explicitly **deferred-by-user**, neither resolved nor revisited. No build, tests, GitHub Actions, website publication, source editing or formal mathematical verification was performed.
