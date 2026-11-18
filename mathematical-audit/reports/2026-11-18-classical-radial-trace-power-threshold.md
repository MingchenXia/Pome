# 2026-11-18 — exact radial mixed-current traces and the top-degree weight threshold

**Finding:** `POME-CLASSICAL-RADIAL-TRACE-POWER-THRESHOLD-001` (low; **verified conditional deduction**). This is a new sharp model and not a false printed theorem, not a proof of the whole upstream dependency chain, and not a repair of any excluded regularization programme.

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Integrated reading file:** `docs/sections/classical-products-with-controlled-unbounded-loci--classical-products-with-compact-unbounded-loci/index.html`.
**Main blob:** `65666651048e9ada933a763b7d381766f8b43965`.
**Anchors:** Theorem 7.29.5, original source `demailly-complex-geometry:B0311B48`, permanent tag `8FBB0E4DE397`, physical lines 46–56 (hypotheses), 61–80 (bounded-collar construction and unweighted induction), 82–102 (weighted induction and weak-limit upper bound), 104–130 (reverse mass inequality); Lemma 7.29.1, original `demailly-complex-geometry:828A36D4`, permanent `438B9224299E`, lines 10–41. The section itself is `4BDD61F32BF5`. Its already recorded isolated-point Poincaré–Lelong example is lines 175–185. These are physical HTML lines at the pinned main, not source-book page numbers.

## Sharp mixed trace calculation

Fix an integer \(n\ge 1\) and the normalization \(dd^c=(i/2\pi)\partial\bar\partial\). On \(B_1\subset\mathbb C^n\) put
\[
 \omega_0=dd^c|z|^2,\qquad u(z)=\log |z|^2,\qquad
 M_q=(dd^cu)^q\wedge\omega_0^{n-q},\quad 0\le q\le n.
\]
These are **classical** products, retaining a possible pole mass, rather than non-pluripolar products. The unbounded locus of \(u\) is the compact set \(\{0\}\), and all potentials are bounded on a collar of the boundary of every centered ball. Consequently the stated hypotheses of Theorem 7.29.5 apply to the recursion, conditional on that theorem's upstream bounded-product continuity.

For each integer \(0\le q<n\), the *entire* positive measure, including its behavior at the origin, is
\[
 \boxed{M_q=\frac{n-q}{n}|z|^{-2q}\omega_0^n,\qquad M_q(\{0\})=0.}
\]
At the top degree,
\[
 \boxed{M_n=(dd^c\log|z|^2)^n=\delta_0.}
\]
These identities give the exact threshold for a positive power weight:
\[
 \boxed{\int_{B_R}|z|^{-2s}\,dM_q
  =\frac{n-q}{n-q-s}R^{2(n-q-s)}
 \quad(0<R\le1,\ 0\le q<n,\ 0\le s<n-q).}
\]
The integral is infinite when \(s\ge n-q\), and for \(q=n\) it is infinite for every \(s>0\). In particular
\[
 \boxed{\int_{B_1}(-\log|z|^2)\,dM_q=\frac1{n-q}\quad(q<n),}
\]
while \(uM_n\) is not a current: \(u(0)=-\infty\) on the unit atom.

### Complete calculation

Write \(r=|z|\). On \(\mathbb C^n\setminus\{0\}\), the complex Hessian of \(u\), measured relative to the Hessian of \(|z|^2\), has one radial eigenvalue zero and \(n-1\) tangential eigenvalues \(r^{-2}\). For any semipositive Hermitian endomorphism with eigenvalues \(\lambda_1,\ldots,\lambda_n\),
\[
 \frac{\beta^q\wedge\omega_0^{n-q}}{\omega_0^n}
   =\frac{e_q(\lambda_1,\ldots,\lambda_n)}{\binom nq}.
\]
Here \(e_q=\binom{n-1}{q}r^{-2q}\), proving the density off zero.

To prove **there is no hidden pole atom when \(q<n\)**, set \(u_\varepsilon=\log(r^2+\varepsilon^2)\), a smooth psh function decreasing to \(u\). Its Hessian eigenvalues are
\[
 \lambda_{\mathrm{tan}}=(r^2+\varepsilon^2)^{-1}
 \quad\text{(multiplicity \(n-1\))},\qquad
 \lambda_{\mathrm{rad}}=\frac{\varepsilon^2}{(r^2+\varepsilon^2)^2}.
\]
For \(0<r\) each eigenvalue lies in \([0,r^{-2}]\). Therefore, for \(q<n\), the mixed smooth density is bounded by \(r^{-2q}\omega_0^n\), locally integrable near \(0\), and converges pointwise away from \(0\) to the displayed density. Dominated convergence establishes the complete measure limit without an atom. The current recursion and its bounded decreasing continuity identify this limit with \(M_q\); the calculation itself uses only explicit smooth Hessians and ordinary local Bedford–Taylor continuity, not Demailly approximation.

For \(q=n\), the smooth determinant is
\[
 (dd^cu_\varepsilon)^n
  =\frac{\varepsilon^2}{(r^2+\varepsilon^2)^{n+1}}\omega_0^n.
\]
Since \(\omega_0^n=n!\pi^{-n}dV_{\mathbb R^{2n}}\), radial integration gives total mass
\[
 \frac{2n!}{(n-1)!}\int_0^\infty
   \frac{\varepsilon^2r^{2n-1}}{(r^2+\varepsilon^2)^{n+1}}\,dr
 =n\int_0^\infty \frac{t^{n-1}}{(1+t)^{n+1}}\,dt=1.
\]
Its mass outside every fixed ball about zero tends to zero; therefore its weak limit is precisely \(\delta_0\).

For \(q<n\), normalized polar coordinates give
\[
 \omega_0^n=2n\,r^{2n-1}dr\,d\sigma,\qquad
 dM_q=2(n-q)r^{2(n-q)-1}dr\,d\sigma,
\]
where \(d\sigma\) is probability measure on the unit sphere. Integrating \(r^{-2s}\) proves the stated threshold. Substituting \(-\log r^2\), and using \(\int_0^1r^{a-1}(-\log r)\,dr=a^{-2}\), gives exactly \(1/(n-q)\).

## Comparison with the integrated theorem and earlier audit

Theorem 7.29.5 explicitly allows a further unbounded psh weight only when there are \(r\le p-1\) Hessian factors. The model \(T=1\) (bidimension \((n,n)\)) shows that **the restriction cannot be extended universally to \(r=p\)**: at \(q=p=n\), the top classical Monge–Ampère current is \(\delta_0\), against which \(\log|z|^2\) is not integrable. Below top degree the exact logarithmic moment and the power-test critical exponent \(s=n-q\) quantify the available integrability. No published theorem is false; this is a verified conditional deduction and an optimality boundary.

The prior 2026-10-25 report already proved the Hausdorff-incidence exponent sharp and confirmed the *reading-edition* malformed duplicate of equation 7.29.3, and already noted the \(n=1\) top-degree Dirac obstruction. Those findings remain unchanged and are **not recounted as new**. What is newly established here is the full all-dimensional mixed trace law, the absence of residual atoms for every \(q<n\), and the exact moment/power integrability formula for all \(q\).

**Proposed optional text-only correction (not applied to source):** after the final §7.29 note, state the all-dimensional mixed trace example and the sharp obstruction at \(r=p\). Preserve the source attribution, permanent tags, and the distinct classical/non-pluripolar conventions. **Affected dependents:** Theorem 7.29.5 and its bounded-collar recursion; users of the product/weight integrability range in §§7.28–7.31. This does not supply a proof of their upstream premises.

**Audit boundary:** Only the displayed theorem steps in lines 46–130 and the independent smooth radial calculation were checked. The local convolution/smooth-collar construction at lines 64–68 was noted as an upstream analytical step but **not reviewed as a regularization programme**; all Demailly approximation/regularization, dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work remains **deferred-by-user**, not repaired or certified. No tests, builds or CI ran, and no canonical/source/website edits were made.

**Coverage delta:** §7.29 was already partly reviewed. **+0 first-visited numbered sections, +0 completed entire-section direct certifications, +0 completed transitive dependency chains; +1 independently proved theorem-level quantitative model.** The freshly inspected main navigation contains 25 chapters and 747 numbered sections.
