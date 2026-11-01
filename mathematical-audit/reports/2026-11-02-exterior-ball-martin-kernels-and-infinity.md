# Exact Martin compactification of an exterior ball (2026-11-02)

**Finding:** `POME-MART-EXTERIOR-BALL-INFINITY-001`  
**Severity / status:** low — **verified conditional deduction** (new explicit model calculation; **not** a false source theorem, proof gap, globally certified theorem, or applied production patch).  
**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Review branch:** `review/mathematical-audit`.

## Precise integrated-reading anchors

- `docs/sections/green-energy-and-martin-boundaries/index.html`, blob `976a90f2a5eba299658f73a1eee8b9d3fef8020f`: Lemma **4.5.8**, source `classical-potential-theory:AB110663`, permanent tag `D878F27BAB16`, physical lines **94–106**, evaluation compactification; Theorem **4.5.9**, source `classical-potential-theory:1677A9F0`, tag `9D6B5CF5E0CF`, **109–122**, Martin normalization, harmonic boundary kernels and metrizability; Theorem **4.5.12**, source `classical-potential-theory:57D18B4C`, tag `6736FBE7368C`, **165–186**, minimal Martin kernels and representing measures; Theorem **4.5.13**, source `classical-potential-theory:854603A2`, tag `0E65F552B1A6`, **189–214**, ball boundary kernels and their minimality. This audit only uses the **ball** part of 4.5.13 as an established internal conditional input; it does not replay the earlier audit of the general Martin representation construction.
- `docs/sections/perron-theory-and-fine-boundary-limits/index.html`, blob `4bc2fb9317e2b6f6bb5b2d90208c677da8275eba`: Theorem **4.4.11**, source `classical-potential-theory:07EA9CB6`, tag `E16C09608A00`, lines **122–148**, exterior Kelvin/Poisson formula and the **distinct** Helms interior-infinity convention.
- Additional **structural recheck** (previously inventoried, not new first coverage): `docs/sections/the-envelope-operators--p-envelopes/index.html`, blob `912f81b3bccf3e1ead96fd18005261a708dfcb4e`, §**16.2** section source `sgpt:189A8E0C`, tag `A6FA63C034E6`, lines **5–9**. This is an introductory navigation/overview page without a standalone theorem proof, **not** mathematical proof-level coverage; actual §§16.3–16.5 retain their prior matrix statuses.

## Statement (exact explicit model)

Let \(d\ge2\), \(R>0\), \(\Omega=\mathbb R^d\setminus\overline{B(0,R)}\), and \(a\in\Omega\) be the reference point used to normalize the Martin kernel. The **complete Martin compactification** of the ordinary Euclidean Greenian domain \(\Omega\) is its closure in the one-point compactification of \(\mathbb R^d\). Consequently
\[
\Delta=\partial B(0,R)\ \sqcup\ \{\infty\},\qquad \Delta_1=\Delta.
\]
Every displayed boundary kernel below has value one at \(a\). For each finite boundary point \(\zeta\in\partial B(0,R)\),
\[
  K_\zeta(x)=
  \frac{(|x|^2-R^2)\,|a-\zeta|^d}
       {(|a|^2-R^2)\,|x-\zeta|^d},
  \qquad x\in\Omega.
\tag{1}
\]
The additional **minimal** Martin kernel at the exterior end is
\[
 K_\infty(x)=
 \begin{cases}
 \displaystyle\frac{\log(|x|/R)}{\log(|a|/R)}, &d=2,\\[6pt]
 \displaystyle\frac{1-(R/|x|)^{d-2}}{1-(R/|a|)^{d-2}}, &d\ge3.
 \end{cases}
\tag{2}
\]
In particular, for \(d\ge3\), \(K_\infty\) is bounded and tends to a positive constant at Euclidean infinity; for \(d=2\), \(K_\infty\) grows logarithmically. The two cases are **not** interchangeable through the formal substitution \(d=2\) in \(1-(R/|x|)^{d-2}\).

## Derivation of every boundary kernel

Use inversion in the radius-\(R\) sphere
\[
 I(x)=\frac{R^2x}{|x|^2}.
\]
It maps \(\Omega\) to \(B(0,R)\setminus\{0\}\) and fixes the sphere pointwise. The puncture \(0\) is polar in dimensions \(d\ge2\), so the punctured ball and the ball have the same Dirichlet Green kernel. Kelvin covariance, checked also by its **fundamental-singularity coefficient** at the pole, gives, for \(d\ge3\),
\[
 G_\Omega(x,y)=
 \left(\frac{R}{|x|}\right)^{d-2}
 \left(\frac{R}{|y|}\right)^{d-2}
 G_B(Ix,Iy).
\tag{3}
\]
For \(d=2\), conformal invariance yields (3) with both prefactors equal to one. The factors at \(y\) cancel in
\(G_\Omega(y,x)/G_\Omega(y,a)\).
By the construction before Theorem 4.5.9, the auxiliary potential \(b(y)=G_\Omega(y,a)\) outside a compact subset of \(\Omega\); hence this **same** ratio computes every Martin boundary limit.

When \(y\to\infty\), \(Iy\to0\). Using
\[
 G_B(z,0)=
 \begin{cases}
 c_2\log(R/|z|),&d=2,\\
 c_d\bigl(|z|^{2-d}-R^{2-d}\bigr),&d\ge3
 \end{cases}
\]
in (3), and then normalizing at \(a\), yields (2) exactly; the convention-dependent constants \(c_d\) cancel.

When \(y\to\zeta\in\partial B_R\), the ball Green quotient tends to the ratio of the inward normal derivatives, i.e. to the ball Poisson-kernel quotient. This follows directly by differentiating the **explicit smooth spherical Green formula** at the boundary (or by its elementary one-sided Taylor expansion), with locally uniform remainder for \(x\) in compact subsets of \(\Omega\). Since
\[
 |Ix-\zeta|=(R/|x|)|x-\zeta|,\qquad
 R^2-|Ix|^2=\frac{R^2}{|x|^2}(|x|^2-R^2),
\]
Kelvin transformation of the unnormalized ball Poisson density
\((R^2-|z|^2)/|z-\zeta|^d\) is precisely
\((|x|^2-R^2)/|x-\zeta|^d\). This gives (1), including the correct \(d=2\) normalization.

The formulas are positive and harmonic in \(x\in\Omega\), and each equals one at \(a\). Distinct finite \(\zeta\) give nonproportional boundary singularities, and \(K_\infty\) cannot equal a finite-boundary kernel: as \(x\to\zeta\) from within \(\Omega\), \(K_\zeta(x)\) diverges whereas \(K_\infty(x)\to0\). The ordinary one-point closure
\[
 \overline\Omega^{\,\sharp}=
 \{x\in\mathbb R^d:|x|\ge R\}\cup\{\infty\}
\]
is compact. Equations (1)–(3), with the interior Green kernels and their pole singularities, define a **continuous injective** extension from this closure to the evaluation compactification of Lemma 4.5.8: near sphere points or infinity the quotients converge **locally uniformly in the kernel's test variable**, not merely at a chosen sequence of test points. Its image contains the dense embedded \(\Omega\) and is compact, so it is all of \(M\). A compact-to-Hausdorff continuous bijection is a homeomorphism. This proves both completeness of the boundary list and the claimed topology, without assuming sequential compactness for an arbitrary initial net.

## Minimality, including the point at infinity

The Kelvin transform of a positive harmonic function \(h\) on \(\Omega\) is
\[
 (\mathcal Kh)(z)=(R/|z|)^{d-2}h(Iz),
\]
interpreted as \(h(Iz)\) in dimension two. Suppose \(0\le h\le K_\zeta\), for a fixed \(\zeta\in\partial B_R\). Then \(\mathcal Kh\) is positive harmonic on \(B_R\setminus\{0\}\), dominated by a **constant multiple of the ball Poisson kernel** at \(\zeta\). The latter is bounded near \(0\), so the harmonic removable-singularity theorem extends \(\mathcal Kh\) across \(0\). The already printed ball minimality argument in Theorem 4.5.13 forces \(\mathcal Kh=c\mathcal K K_\zeta\), and hence \(h=cK_\zeta\).

Now suppose \(0\le h\le K_\infty\). Its Kelvin transform is positive harmonic on the punctured ball, is bounded above by a constant multiple of the *ball Green pole* at \(0\), and tends to zero on the sphere. Bôcher's isolated-pole decomposition (the same elementary input used in Theorem 4.4.11) gives
\[
 \mathcal Kh(z)=
 \begin{cases}
 c\log(R/|z|)+u(z),&d=2,\\
 c|z|^{2-d}+u(z),&d\ge3,
 \end{cases}
\]
where \(c\ge0\) and \(u\) is harmonic on the **full** ball. The domination by the ball Green pole forces continuous zero boundary data for \(\mathcal Kh\). Therefore \(u\) has the corresponding **constant** sphere limit (zero if \(d=2\), \(-cR^{2-d}\) otherwise), so uniqueness of the bounded harmonic solution of the ball Dirichlet problem makes \(u\) that constant. Thus \(\mathcal Kh\) is a scalar multiple of \(G_B(\cdot,0)\) and \(h=c'K_\infty\). This proves **minimality** of the extra point for **every \(d\ge2\)**; no assertion that mere topological boundary points are automatically minimal is being made.

## Helms's different infinity convention

The exterior-end Martin boundary point in §4.5 must **not** be identified with the **interior** point at infinity in the compactified exterior theory of Theorem 4.4.11. For \(d\ge3\), the ordinary exterior harmonic function \(K_\infty\) has **zero sphere boundary data** and a **strictly positive finite infinity limit**. Its boundary mean is \(m=0\) while its infinity value is \(\alpha>0\); by the exact hypothesis in 4.4.11, it therefore **fails the additional Helms harmonicity condition at interior infinity**. For \(d=2\), \(K_\infty\) is unbounded and the finite-limit clause of 4.4.11 does not apply. This is a distinction of domain and boundary conventions, **not** a contradiction between two source theorems.

## Classification and action

- **Status:** verified conditional deduction, **low**. The calculations independently verify all normalizations and the Kelvin endpoint, **conditional** on the integrated ordinary ball Green/Poisson formula, the ball minimality statement (4.5.13) and the internally used Bôcher/removability facts. They do **not** certify the full Martin representation theorem (4.5.12), all sweeping lemmas, or the Helms compactified theory.
- **No confirmed original theorem error or newly confirmed proof gap.** The general historical issue `POME-MART-SWEEP-PROJECTIVE-001` remains a distinct **previous** ledger item; it is not reopened or reclassified.
- **Proposed production correction:** optional explicit example following Theorem 4.5.13 with formulas (1)–(2), the extra minimal point and the Helms/ordinary distinction. This is a **proposal only**, not an edit to any source, reader, tag, registry or published site.
- **Affected dependents:** classical potential §§4.4–4.5 (Perron/Martin kernels and exterior harmonic data), and any later application treating Euclidean infinity as either Martin boundary or Helms interior. No additional dependent statement is declared false.
- **Coverage accuracy:** selected new proof-level model/limit/minimality audit of 4.5.8–9 and 4.5.12–13, partly previously sampled; §16.2 revisited as previously inventoried structural-only. **25 chapters / 747 numbered ToC sections / zero entirely mathematically certified sections**. All user-deferred Demailly approximation/regularization and dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale and positivity-loss proof programmes retain `deferred-by-user` status. No builds, tests, CI, formalization, website publication or main/source changes.
