# 2026-11-23: torus rigidity, Kummer boundary classes, and semipositive metric extension

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272
**Review branch before this run:** 5a0ed5a47646164b3c32ed162210b73f6a39affa
**Status:** a complete *direct mathematical reading* of current §§10.26–10.28, plus selected nonexcluded checks from §10.29. This is **not** a transitive verification of all internal references, and is not a claim about earlier first-ever coverage.
**Excluded by user:** Demailly approximation/regularization, dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof programmes; any such old notes remain **deferred-by-user**, not resolved.

## New finding — POME-TORUS-NONRIGID-FLAT-COLLAPSE-ORDER-001

- **Severity / status:** low / **verified conditional deduction** (a sharp *order* within the explicit printed model; **NOT** a false theorem or a proof gap).
- **Location:** \`docs/sections/bott-chern-classes-and-singular-loci--rigid-boundary-classes-on-a-torus/index.html\`, Example **10.26.3**, permanent tag **87A3AA3B13FD**, physical lines **87–112**, especially model 90–99 and determinant/diameter calculation 102–111. Main blob \`0cd2a46d5f5aaceb809c5ef13b9a717c422a7212\`.
- **Hypotheses:** the square complex torus \(X=(\mathbb C/(\mathbb Z+i\mathbb Z))^2\), flat form
  \[
  \beta_t=\frac{i}{2}\big((t\,dz_1+dz_2)\wedge(t\,d\bar z_1+d\bar z_2)+t^2dz_2\wedge d\bar z_2\big),\qquad t>0,
  \]
  and Riemannian convention \(g_t(v,w)=\beta_t(v,Jw)\).
- **Claim (deduction, not a replacement of the original example):**
  \[
  \boxed{\left(\frac{2}{\pi^2}\right)^{1/4}t\ \leq\ \operatorname{diam}(X,g_t)\ \leq\ t.}
  \]
  Thus the collapse in the **nonrigid** limiting class of Example 10.26.3 has the **exact linear order** \(\Theta(t)\), not merely an unspecified rate. The constant in the lower bound is universal and explicit; no optimality of that particular numeric constant is claimed.
- **Full proof:** The coefficient Hermitian matrix in Example 10.26.3 is
  \[
  H_t=\begin{pmatrix}t^2&t\\ t&1+t^2\end{pmatrix},\qquad \det H_t=t^4.
  \]
  Because the standard square complex torus has real coordinate fundamental domain of volume one, its Riemannian density is \(\det H_t\), so
  \[
  \operatorname{Vol}_{g_t}(X)=\int_X\beta_t^2/2=t^4.
  \]
  Let \(D_t=\operatorname{diam}(X,g_t)\) and fix \(p\in X\). Every point lies at distance at most \(D_t\) from \(p\). Since the metric is flat, the exponential map on the tangent-space Euclidean ball of radius \(D_t\) is surjective onto \(X\), a local isometry, and its image's volume cannot exceed the source ball volume (counting overlaps only decreases the image volume). In four real dimensions that source volume is \((\pi^2/2)D_t^4\). Hence \(t^4\le(\pi^2/2)D_t^4\), giving the claimed lower bound. The upper bound \(D_t\le t\) is the directly checked Gaussian-integer rounding argument at physical lines 102–111 of the original example. Therefore both exponents match.
- **Affected dependents / interpretation:** strengthens the specific boundary-collapse countermodel of §10.26.3. It does **not** alter the equivalence of rigidity, kernel-density and collapse for fixed positive perturbations \(\theta+t\kappa\) in Theorem **10.26.1** (tag **9A07C571BD3F**), and does **not** claim a general rate for arbitrary Kähler paths, nor a theorem about an arbitrary torus, nor a new characterization of nonrigid classes.
- **Proposed correction:** optional audit-only quantitative remark after Example 10.26.3; no source, registry, tag, or reading-edition body edit is authorized here.

## Direct checks of the integrated reading edition

### §10.26, complete current text (physical lines 7–114; blob \`0cd2a46d5f5aaceb809c5ef13b9a717c422a7212\`)

- Theorem **10.26.1** (tag **9A07C571BD3F**): verified the kernel Fourier argument: positivity and vanishing total coefficient mass force \(D_v^2u+D_{Jv}^2u=0\); density kills every nonzero character. The opposite direction uses a character trivial on \(K\), whose real cosine gives a bounded \(dd^c\) perturbation supported in the positive complement.
- For collapse with a **fixed translation-invariant** \(\kappa\), a finite \(\delta\)-net from the dense kernel yields \(D_t\le\sqrt t R+C\delta\); a quotient character obstructs collapse otherwise. No unjustified sequential compactness is used.
- Example **10.26.2**: integral characters of the square torus annihilate \(K_a=\{(z,az)\}\) precisely when \(m_1+am_2=n_1+an_2=0\). The periods \(1,-a\) establish the irrational cohomology ray when \(a\notin\mathbb Q\).
- Example **10.26.3**: checked positivity \(\det H_t=t^4>0\), smooth convergence to \(\theta_0\), Gaussian-integer upper estimate, and semipositive nonrigid cosine variation. The new lower rate is independent of the printed proof.

### §10.27, complete current text (physical lines 7–79; blob \`9ad1ad9323c3c53e9c1faec36877f911ac5f8b76\`)

- Lemma **10.27.1**: local involution on the blowup is \((u,v)\mapsto(-u,v)\); quotient coordinates \(s=u^2,v\) have overlap \(s'=v^2s\), giving the \(\mathcal O_{\mathbb P^1}(-2)\) normal line. Checked the normal positivity of \(dd^c(c\rho^2)\) and tangential correction via \(dd^cq_v\), without claiming Hironaka as a new result.
- Proposition **10.27.2**: checked \(h(y_1)dx_1\wedge dy_1\) is invariant and vanishes near quotient singularities; \(f''=4\pi(h_1-h_2)\) matches the project's \(dd^c=(i/2\pi)\partial\bar\partial\) convention. Evenness and mean zero give the local constancy needed to descend the potential across exceptional curves. Periods \(1,a\) on translated integer two-cycles show nonzero irrational de Rham ray; square-zero and nonrigid representatives follow. No new printed error confirmed.

### §10.28, complete current text (physical lines 7–254; blob \`26a2089355aa80701c7c20923660a0c9363e7a65\`)

- Lemma **10.28.1**: checked four point centers, linear initial terms of \(F_1=x(z-ty)\), \(F_2=y(z-tx)\), basepoint freeness on \(t\ne0\), \(L_t^2=0\), and \(K_{X_t}\cdot L_t=-2\), which excludes adjoint sections by nefness.
- Lemma **10.28.2**: central decomposition \(2L_0=A+\ell\); cubic generators with the stated exceptional multiplicities give the half-divisor metric \(h_0\).
- Lemmas **10.28.3**, **10.28.8**: conic equation \(F_1-aF_2=z(x-ay)+t(a-1)xy\) degenerates to \(\ell+q_a\); \(q_a\) has \(L_0\)-degree one. The blowup chart \(z=1,x=r,y=rs\) gives \(1-as+t(a-1)rs=0\), transverse in \(s\) for \(a\ne0\).
- Theorem **10.28.4**: the degree-zero curvature on nearby compact conics is zero for almost every parameter. Lemma **10.28.6** supplies the *central-slice* harmonicity, rather than asserting unwarranted continuity of restrictions. Its degree-one curvature at \(p_a\) requires logarithmic coefficient one, contradicting the half-divisor lower bound.
- Theorem **10.28.9** and Corollary **10.28.10**: checked that fiberwise harmonicity leads to a base \(\mathcal O_{\mathbb P^1}(1)\) metric, and that a homogeneous psh weight \(V(F_1,F_2)\) extends across the common zero with value \(-\infty\); this is an elementary psh extension, **not** the excluded Demailly regularization programme. The necessity uses equality almost everywhere of psh representatives, not an unjustified pointwise subtraction at polar sets.

### §10.29, **selected-only** contextual checks (main blob \`8846df97111fa26289cd5e0cb4fd8f8a1fc5a035\`)

Checked Theorem **10.29.4** at physical lines approximately 70–111 (Liouville on complex leaves, density of real translations, convexity of transverse potentials); Proposition **10.29.10** at lines 165–265 (Gauduchon \(\omega^2\) cancellation, indefinite mixed derivative, mass normalization, \(P=1-\partial_1g,Q=1-\partial_2g\) bounds); and Proposition **10.29.14** at lines 280–303 (averaging and convex/concave \(h(y)\) contradiction). These are **not** an entire §10.29 audit or independent proofs of all cited analytic theorems.

## Findings and dependency classification

- **New confirmed theorem errors:** 0.
- **New proof gaps:** 0 confirmed; no new candidate asserted.
- **New quantitative finding:** one, \`POME-TORUS-NONRIGID-FLAT-COLLAPSE-ORDER-001\`, status **verified conditional deduction**; baseline printed statement remains correct.
- **Genuine duplication:** none newly confirmed; the Kummer nonrigidity and torus rigidity are different examples with genuinely distinct hypotheses (their irrational classes behave differently).
- **External / outstanding chains:** §20.4.10 for Bott–Chern potential representation; positivity and psh restriction on families; §5.24.3 and §5.24.7 for equality/extension of psh weights; classical Kähler-ness of the Kummer resolution, and §10.29's Siu, Skoda and unit-group inputs. None independently transitive-certified. The elementary \(4\)-ball volume deduction itself uses only the explicit constant flat metric.
- **User-deferred:** Demailly approximation/regularization and the named Bergman, L², Ohsawa–Takegoshi, multiscale atlas, positivity-loss proof completion programmes; left untouched and uncertified.

**Coverage delta:** +3 entire present-main mathematical sections directly read (§§10.26–10.28), +1 **selected** §10.29, +1 new quantitative conditional deduction, +0 confirmed false theorems, +0 certified complete upstream dependency chains. Historical first visits remain unreconciled; existing 747 section identities and all old records are preserved. No tests, build, CI, production publication, or source/registry/tag edits were performed.
