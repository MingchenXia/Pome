# Classical Green energy: spherical-shell Gram matrix and the sharp polynomial accumulation threshold

**Audit date:** 2026-10-31. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Stable finding ID:** **POME-GREEN-SHELL-GRAM-THRESHOLD-001**.  
**Severity/status:** **low / verified conditional deduction**. The printed Green-energy theorem and signed-incompleteness example are mathematically correct; the new result is an exact all-pairs Gram identity, an if-and-only-if Cauchy criterion for *arbitrary* nested shells, and a sharp polynomial-scale threshold and convergence rate. It is **not** a false-theorem finding, a new proof defect, a certification of the entire Green/Martin theory, or a repetition of the original geometric-radius counterexample.

## Pinned integrated statements and scope

- **Main reading edition:** <code>docs/sections/green-energy-and-martin-boundaries/index.html</code>, main blob **976a90f2a5eba299658f73a1eee8b9d3fef8020f**, physically numbered HTML lines **8–14, 17–43, 47–68 and 70–73**. The section label/permanent tag is **8D29421CAE4C**.
- **§4.5.1**, source heading <code>classical-potential-theory:5FDF1F52</code>, permanent tag **57DD989B07A4** (lines 8–14): sign convention for the nonnegative Green kernel and the signed energy pairing.
- **Theorem 4.5.2**, source <code>classical-potential-theory:AEA69819</code>, permanent tag **CC3D1AD9179B** (lines **17–43**): positive definiteness and Cauchy–Schwarz for signed finite-energy Radon measures. Used as an **internal conditional input**, not transitively certified.
- **Theorem 4.5.4**, source <code>classical-potential-theory:5FB19CB2</code>, permanent tag **CE0D5F4DF7B2** (lines **47–68**): completeness of the *positive* energy cone, as distinct from its signed span.
- **Example 4.5.5**, source <code>classical-potential-theory:898691BF</code>, permanent tag **61A5D2A82793** (lines **70–73**, especially line **72**): the original geometric-radius Newtonian shell construction proving incompleteness of the signed energy space. The example is **correct**.
- **Theorem 4.5.6**, source <code>classical-potential-theory:9D70EB64</code>, permanent tag **B15EFD960FD5** (lines **77–87**): consulted for the positive-cone projection distinction only; not independently reproved here.

This report does **not** re-register the existing findings **POME-MARTIN-GREEN-002**, which already verifies the *particular* geometric shell example, **POME-GREEN-ENERGY-WEAK-NONSTRONG-SPHERES-001**, which treats a different **positive** shell sequence, or **POME-GREEN-SPHERE-SWEEP-ESCAPE-001**, which treats spherical balayage. The mathematical increment below is the exact Gram law and **all-sequence sharp threshold**.

## Exact Gram theorem for spherical shells

Work on \(\Omega=\mathbb R^3\), with the Newtonian Green normalization \(G(x,y)=|x-y|^{-1}\), which is precisely the normalization of Example 4.5.5. Write \(\sigma_r\) for normalized surface area probability on the sphere \(S_r=\{|x|=r\}\). Let

\[
0<r_2<r_3<\cdots<1,\qquad r_j\uparrow1,\qquad
\delta_j:=\frac1{r_j}-1>0,\qquad
\lambda_j:=\sigma_{r_j}-\sigma_1.
\]

All finite linear combinations of the \(\lambda_j\) are signed finite-energy Radon measures. Newton's shell identity gives

\[
G\sigma_r(x)=\frac1{\max(|x|,r)},\qquad
I(\sigma_r,\sigma_s)=\frac1{\max(r,s)}.
\]

Hence for **every** \(j,k\ge2\),

\[
\boxed{\qquad I(\lambda_j,\lambda_k)
=\frac1{\max(r_j,r_k)}-1
=\delta_{\max(j,k)}=\min(\delta_j,\delta_k).\qquad}
\]

The equality is a genuine **positive-definite Gram identity**, not merely a bound on individual summand norms. In particular, for integers \(2\le n\le m\),

\[
\boxed{\qquad
\left\|\sum_{j=n}^m\lambda_j\right\|_I^2
=\sum_{j=n}^{m}\bigl(2(j-n)+1\bigr)\delta_j.
\qquad}                                                    \tag{1}
\]

Indeed, in the double sum over \([n,m]^2\), precisely \(2(j-n)+1\) ordered pairs have \(\max(k,l)=j\).

### Exact convergence criterion

Writing \(S_m=\sum_{j=2}^{m}\lambda_j\) in the **signed pre-Hilbert energy space**, the partial sums are norm-Cauchy **if and only if**

\[
\boxed{\qquad \sum_{j=2}^{\infty}j\left(\frac1{r_j}-1\right)<\infty.\qquad} \tag{2}
\]

For sufficiency, (1) implies

\[
\sup_{m\ge n}\|S_m-S_{n-1}\|_I^2
\le 2\sum_{j=n}^{\infty}j\delta_j\longrightarrow0.
\]

Conversely, if \(S_m\) is norm-Cauchy, choose one \(n\) sufficiently large that all \(\|S_m-S_{n-1}\|_I^2\), \(m\ge n\), are bounded. Monotonicity of the nonnegative right side of (1) forces
\(\sum_{j=n}^{\infty}(2(j-n)+1)\delta_j<\infty\). Since its coefficients are eventually comparable to \(j\), (2) follows. No compactness, limiting exchange of signed measures, or summability of individual norms is assumed.

A useful equivalent expression, obtained by telescoping the minimum kernel, is

\[
\left\|\sum_{j=n}^m\lambda_j\right\|_I^2
=\sum_{l=n}^m(\delta_l-\delta_{l+1})(l-n+1)^2
+\delta_{m+1}(m-n+1)^2.
\]

This second identity exhibits the discrete quadratic energy of the cumulative shell counts.

## Sharp polynomial-radius threshold and rate

Fix \(p>0\), set for \(j\ge2\)

\[
r_j=1-j^{-p},\qquad
\delta_j=\frac1{j^p-1}.
\]

Then \(\delta_j\sim j^{-p}\), so (2) is satisfied **if and only if \(p>2\)**. Thus the signed shell partial sums are energy-Cauchy precisely for \(p>2\); for \(p=2\) the positive tail sum in (1) diverges logarithmically, while for \(0<p<2\) it diverges with a power as \(m\to\infty\), for any fixed \(n\).

For every \(p>2\) the squared *abstract-completion* tail norm has the exact asymptotic

\[
\boxed{\qquad
\lim_{n\to\infty}n^{p-2}
\lim_{m\to\infty}\left\|\sum_{j=n}^m\lambda_j\right\|_I^2
=\frac{2}{(p-1)(p-2)}.
\qquad}                                                     \tag{3}
\]

To prove it, write \(j=n+k\) in (1); the difference between
\(\delta_j=(j^p-1)^{-1}\) and \(j^{-p}\) contributes \(O(n^{2-2p})\) to the infinite sum, negligible compared with \(n^{2-p}\). The leading term is the ordinary one-dimensional Riemann sum

\[
n^{p-2}\sum_{k\ge0}(2k+1)(n+k)^{-p}
\longrightarrow 2\int_0^\infty\frac{t\,dt}{(1+t)^p}
=\frac2{(p-1)(p-2)}.
\]

An elementary tail majorant \(C(1+t)^{1-p}\), integrable exactly for \(p>2\), justifies the infinite-interval Riemann-sum passage. In particular the formal tail norm is asymptotic to
\(\sqrt{2/((p-1)(p-2))}\,n^{1-p/2}\).

The **already printed** geometric choice \(r_j=1-4^{-j}\) is the separate special case \(\delta_j=(4^j-1)^{-1}\). Formula (1) refines that old example with the new exact rate

\[
\lim_{n\to\infty}4^n
\lim_{m\to\infty}\left\|\sum_{j=n}^m\lambda_j\right\|_I^2
=\sum_{k=0}^{\infty}(2k+1)4^{-k}=\frac{20}{9},
\]

but the old **existence of a signed incompleteness example** is not presented as a new finding.

## Why the Cauchy vector is not a signed Radon measure

For *every* shell family as above with infinitely many distinct \(r_j\uparrow1\), suppose that \(S_m\) had a signed finite-energy **Radon-measure** limit \(\lambda\). For \(q\in C_c^\infty(B(0,1))\), Theorem 4.5.2's representation \(q=G(-\Delta q/(4\pi)\,dx)\), paired with signed-energy Cauchy–Schwarz, implies \(\int q\,dS_m\to\int q\,d\lambda\). Since only finitely many of the shells \(\sigma_{r_j}\) meet each fixed compactly supported \(q\), and the negative \(\sigma_1\) lies on the boundary, it follows that

\[
\lambda|_{B(0,1)}=\sum_{j=2}^{\infty}\sigma_{r_j}
\]

as positive locally finite Radon measures on the **open** unit ball. Yet the compact **closed** ball \(\overline B(0,1)\subset\mathbb R^3\) contains infinitely many distinct unit-mass spheres. The positive variation of \(\lambda\) on this compact set would be infinite, contradicting the Radon property of a signed finite-energy measure.

Consequently, for each \(p>2\), the polynomial family yields a Cauchy sequence with the sharp rate (3), **but without a signed energy-measure limit**. The symbol “infinite tail” in (3) denotes the **real limit of finite energy norms**, or an element of the *abstract Hilbert completion*, **not** an improperly presumed signed Radon measure. This is compatible with Theorem 4.5.4: the **positive** cone \(\mathcal E^+\) is complete, whereas its **signed span** \(\mathcal E\) need not be.

## Verification, disposition, dependencies and affected results

The optional editorial addition is a short corollary after Example 4.5.5 recording the exact Gram identity (1), the sharp criterion (2), and the polynomial threshold and rate (3). **No original mathematical statement or proof is declared false, no repair is required, and no canonical source/permanent tag is to be changed.** Potential dependents include §4.5.4's positive-vs-signed energy convergence distinction, §4.5.6's positive-cone projections, and interpretations of energy topology under mass concentration; these dependents are **not** independently certified.

**Independent reproducible check actually executed:** 16 exact rational comparisons between the Gram double sum and the closed weighted sum (1), for \(p=1,2,3,5\) and four finite index blocks; all passed. The companion standard-library script reproduces these identities. It does **not** numerically certify the asymptotics, completeness, or any project source theorem.

**Precise new mathematical coverage:** the actual §4.5.5 shell construction and its all-pairs Newtonian energy, plus §4.5.2's compact-test signed-pairing convention and §4.5.4's positive/signed completion distinction. §4.5.6 was checked only as context, and §§4.5.8–13 (Martin boundary) were inspected as background without a new full proof certification. The wider matrix remains **25 chapters / 747 numbered ToC sections / zero complete mathematical-section certifications**. Prior confirmed errors, proof gaps, external dependencies, genuine duplicates, proposed repairs and their statuses are unchanged.

**Deferred-by-user, never re-opened:** Demailly approximation/regularization and dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes. This is a notes-only audit, not a project build, CI run, source/body edit, publication, or formal verification.
