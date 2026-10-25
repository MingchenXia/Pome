# 2026-10-25 — sharp Hölder Monge–Ampère ball mass and logarithmic cost of smooth density bounds

## Revision, scope, and exact reading anchors

Reviewed immutable \`main\` commit: **b6933b772f41b45918f7e25ed1afbbb1fd892272**. The audit branch started this pass at **be465808e940d7f97ccc520bbfcfb4d114e5db6d**. Both findings below are **low severity / verified conditional deductions**, not false theorems and not certifications of their complete upstream theories.

Directly inspected the *integrated reading-edition* statements and proofs, at this main revision:

- \`docs/sections/smooth-monge-ampere-equations--the-potential-bound-from-weighted-integration/index.html\` (blob \`f774b702e65736ce8a23847dbb3409c6b31b0211\`): Lemma 14.3.1, tag \`E2F31793530D\`, lines 11–28; Lemma 14.3.2, tag \`D570CDA4FA55\`, lines 33–103 (including weighted mixed-mass recurrence, equations 14.3.3–4); Theorem 14.3.5, tag \`EEF74F1DEBB8\`, stable source label \`non-kahler-pluripotential-theory-C569075E\`, lines 108–150 (Moser iteration and normalization). The separate quantitative family below pertains to the dependence on the parameter \(\Lambda\), not to an alleged failure of the proof.
- \`docs/sections/smooth-monge-ampere-equations--second-derivatives-and-ellipticity/index.html\` (blob \`fe3df283b6431886676aa704c588a7dc88aade37\`): Lemma 14.5.1, tag \`BC4847C0CD7D\`, lines 26–121, including the torsion square completion; Theorem 14.5.5, tag \`A61645907A4D\`, lines 126–187, including the ellipticity maximum-principle step. Selected algebra checked for contextual consistency only: neither the whole section nor its regularity chain is certified.
- \`docs/sections/equations-with-prescribed-singularities--singular-measures-on-shrinking-spheres/index.html\` (blob \`354dfdf5224fac8896103ec09aa5936351021914\`): spherical probability and weights, equation 15.26.1, tag \`938F2C76C18A\`, lines 10–23; Proposition 15.26.2, tag \`8F3C95237950\`, stable source label \`non-kahler-pluripotential-theory-92442012\`, lines 27–65; downstream Corollary 15.26.3 and Theorem 15.26.4, tags \`AB5B44EC4BDD\` and \`6076D6F3256C\`, lines 70–103 (dependency-only read). The downstream Hölder/reference existence theorems are not re-proved.
- \`docs/sections/plurisubharmonic-functions-and-singularities--local-products-and-capacity/index.html\` (blob \`ddb2ac8d9de27a22152872e07e5e787d138a790e\`): Lemma 5.27.25, tag \`3242D4BA1F13\`, stable source label \`non-kahler-pluripotential-theory-961DE4FB\`, lines 518–527, giving the normalized Monge–Ampère measure of the spherical radial maximum. Its proof in the tag reading page was checked for normalization, but the full Bedford–Taylor calculus remains an upstream input.

The previous \`POME-SPHERE-MA-NORM-001\` and \`POME-SPHERE-HOLDER-SHARP-001\` from 2026-10-18 concern specifically the normalization and sharp regularity of the *original* exponent \(1/2\) construction. They are **not** re-registered. The full range of exponents, the universal small-ball mass theorem, and its sharpness are different statements.

The user-excluded Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain **deferred-by-user**. No proof from those programmes is used here.

## POME-SMOOTH-MA-LOG-COST-001 — fixed-background logarithmic lower bound

**Status:** verified conditional deduction (the concrete calculation is independent); **severity:** low. **Printed target:** Theorem 14.3.5, tag \`EEF74F1DEBB8\`. The printed theorem is correct. **Proposed edit:** optional sharpness remark after the theorem; no change to hypotheses, permanent tags, proof registry or source.

**Claim.** For every complex dimension \(n\geq1\), there is a *single fixed compact Kähler* \(n\)-fold \((X,\omega)\) such that any function \(C_\Lambda\) bounding all the normalized smooth potentials in Theorem 14.3.5 must satisfy
\[
 C_\Lambda\geq\log\Lambda\qquad (\Lambda\geq1).
\]
Thus not even on a fixed Kähler background can its density-dependent sup-norm constant have sublogarithmic growth as \(\Lambda\to\infty\).

**Complete calculation.** On \(\mathbb P^1\), let
\[
 \omega_{\mathrm{FS}}=dd^c\log(1+|z|^2),
 \qquad u_\epsilon(z)=\log\frac{|z|^2+\epsilon}{1+|z|^2},
 \qquad 0<\epsilon\leq1,
\]
with the project-wide convention \(dd^c=\frac{i}{2\pi}\partial\bar\partial\). The logarithmic quotient extends smoothly across \(z=\infty\), with \(u_\epsilon(\infty)=0\), while \(u_\epsilon(0)=\log\epsilon\). Thus
\[
 \sup_{\mathbb P^1}u_\epsilon=0,\qquad
 \|u_\epsilon\|_\infty=\log(1/\epsilon).
\]
Writing \(x=|z|^2\), direct differentiation gives
\[
 \omega_{\mathrm{FS}}+dd^c u_\epsilon
 =dd^c\log(x+\epsilon)
 =q_\epsilon(x)\,\omega_{\mathrm{FS}},\qquad
 q_\epsilon(x)=\frac{\epsilon(1+x)^2}{(x+\epsilon)^2},
\]
and
\[
 q'_\epsilon(x)=\frac{2\epsilon(\epsilon-1)(1+x)}{(x+\epsilon)^3}\leq0.
\]
It follows that \(0<q_\epsilon(x)\leq1/\epsilon\), with exact maximum \(q_\epsilon(0)=1/\epsilon\). At infinity use \(w=1/z\): the numerator's local curvature potential becomes \(\log(1+\epsilon|w|^2)\), so the form is strictly positive and smooth there as well.

For \(n\geq2\), take
\[
 X=\mathbb P^1\times\mathbb P^{n-1},\quad
 \omega=p_1^*\omega_{\mathrm{FS}}+p_2^*\omega_{\mathrm{FS},n-1},\quad
 U_\epsilon=p_1^*u_\epsilon.
\]
Only the first factor changes. Multilinearity and dimension imply
\[
 \frac{(\omega+dd^c U_\epsilon)^n}{\omega^n}
 =q_\epsilon\circ p_1\leq\epsilon^{-1},\qquad
 \|U_\epsilon\|_\infty=\log(1/\epsilon).
\]
For \(n=1\), use the first factor alone. Set \(\epsilon=\Lambda^{-1}\). This proves the claimed lower bound for the *same fixed* \(\omega\), and every \(\Lambda\geq1\). The smooth admissible family has no singularities and requires no approximation theorem.

**Dependencies/impact.** No printed theorem is false and no proof gap is asserted. The example gives a quantitative restriction on possible constants in §14.3.5 and its uses in continuity-method bounds. The connectedness, determinant and positivity hypotheses are all satisfied.

## POME-HOLDER-BALL-MASS-EXPONENT-001 — sharp \(r^{n\alpha}\) decay, including singular shells

**Status:** verified conditional deduction; **severity:** low. **Printed targets:** Proposition 15.26.2 (tag \`8F3C95237950\`) and local spherical Lemma 5.27.25 (tag \`3242D4BA1F13\`). The printed original \(\alpha=1/2\) proposition remains correct. **Proposed edit:** optional stand-alone local sharpness statement and a general-exponent remark, without altering the original normalizations.

**Universal local upper estimate.** Let \(h\) be any smooth Hermitian metric on an \(n\)-dimensional complex manifold, \(u\in\mathrm{PSH}(X,h)\cap C^{0,\alpha}(X)\), \(0<\alpha\leq1\), and \(p\in X\). In a sufficiently small fixed coordinate ball, there is a constant \(C\), depending on the chart, \(h\) and the Hölder norm of \(u\), such that
\[
 \boxed{\quad \mathrm{MA}_h(u)(B(p,r))\leq C\,r^{n\alpha}\quad(0<r<r_0).\quad}
\]
Here \(B(p,r)\) denotes the coordinate Euclidean ball. To prove it even when \(h\) is not closed, choose \(A>0\) on the chart such that \(A\,dd^c|z|^2\geq h\), and put \(v=u+A|z|^2\). Then \(v\) is locally psh and
\[
 dd^cv\geq h+dd^cu\geq0.
\]
The bounded Bedford–Taylor mixed-product positivity gives \(\mathrm{MA}_h(u)\leq(dd^cv)^n\) locally. Since \(|v(z)-v(0)|\leq L'|z|^\alpha\), for \(r\) sufficiently small the rescaled psh function
\[
 v_r(\zeta)=\frac{v(r\zeta)-v(0)}{r^\alpha},\qquad |\zeta|<2,
\]
has a bound independent of \(r\). The fixed nested-ball Chern–Levine–Nirenberg estimate gives \(\int_{|\zeta|<1}(dd^cv_r)^n\leq C\). Under holomorphic dilation,
\[
 \int_{|z|<r}(dd^cv)^n
 =r^{n\alpha}\int_{|\zeta|<1}(dd^cv_r)^n,
\]
proving the bound. This step uses only the established bounded local Bedford–Taylor product/CLN estimate, not the excluded global regularization programme.

**Sharpness for every exponent, including \(\alpha=1\).** In \(\mathbb C^n\), put \(f(z)=|z|^\alpha\). For \(t=|z|^2>0\), the complex Hessian of \(f=t^{\alpha/2}\) has one radial eigenvalue \((\alpha/2)^2t^{\alpha/2-1}\) and \(n-1\) tangential eigenvalues \((\alpha/2)t^{\alpha/2-1}\). Consequently, with the stated \(dd^c\) convention,
\[
 \det(f_{i\bar j})=(\alpha/2)^{n+1}|z|^{n\alpha-2n},
 \qquad
 \boxed{\ \int_{B(0,r)}(dd^c|z|^\alpha)^n
       =(\alpha/2)^n r^{n\alpha}.\ }
\]
The product has no point mass at the origin: boundedness and the preceding universal estimate show its ball masses tend to zero. The explicit density on the punctured ball, integrated in \(2n\)-dimensional polar coordinates, gives the displayed identity. For any compact Hermitian \(X\), multiply \(|z|^\alpha\) by a cutoff equal to one near \(p\), extend by zero, and scale by a sufficiently small \(\delta>0\). Away from \(p\) the negative part of the Hessian is smooth and bounded; near \(p\) the radial Hessian is positive. Hence the global \(h\)-psh Hölder potential \(U\) satisfies \(h+dd^cU\geq h/2\) and
\[
 \mathrm{MA}_h(U)(B(p,r))\geq
 \delta^n(\alpha/2)^n r^{n\alpha}
\]
for all small \(r\). Together with the upper estimate this proves that the exponent \(n\alpha\) is **optimal** on every compact Hermitian background.

**Singular-shell realization for every \(0<\alpha<1\).** Retain exactly the cutoff \(\chi\), radii \(r_j=r_0\,2^{-j}\), functions \(\psi_j\) and common curvature bound \(dd^c\psi_j\geq-Kh\) from the *printed* proof of Proposition 15.26.2, lines 35–48. Replace only the weights by
\[
 Z_\alpha=2K\sum_{j\geq1}r_j^\alpha,\quad
 d_{j,\alpha}=r_j^\alpha/Z_\alpha,\quad
 S_{n\alpha}=\sum_{j\geq1}r_j^{n\alpha},\quad
 \rho_\alpha=S_{n\alpha}^{-1}\sum_{j\geq1}r_j^{n\alpha}\sigma_j.
\]
Then \(\sum_jd_{j,\alpha}=1/(2K)\), so the uniformly convergent series \(U_\alpha=\sum_jd_{j,\alpha}\psi_j\) satisfies \(h+dd^cU_\alpha\geq h/2\). For two inner-ball points at distance \(t\), the same radial logarithmic comparison in original line 53 gives
\[
 |\psi_j(z)-\psi_j(z')|\leq2\log(1+t/r_j).
\]
Split the sum at \(r_j=t\): the large-radius contribution is bounded by
\(Ct\sum_{r_j\geq t}r_j^{\alpha-1}\leq C_\alpha t^\alpha\), and the smaller-radius contribution by
\(C\sum_{r_j<t}r_j^\alpha\log(1+t/r_j)\leq C_\alpha t^\alpha\).
The transition annulus is one fixed smooth function. Thus \(U_\alpha\in C^{0,\alpha}(X)\). Lemma 5.27.25 and positive mixed products, exactly as in original lines 58–64, yield
\[
 \mathrm{MA}_h(U_\alpha)\geq\sum_jd_{j,\alpha}^n\sigma_j
 =\frac{S_{n\alpha}}{Z_\alpha^n}\rho_\alpha.
\]
In particular, the Monge–Ampère measure has a nonzero singular component supported on countably many spheres, and for all sufficiently small \(r\),
\[
 \mathrm{MA}_h(U_\alpha)(B(p,r))\geq
 Z_\alpha^{-n}\sum_{r_j<r}r_j^{n\alpha}
 \geq c_\alpha r^{n\alpha}.
\]
The matching upper bound is the universal local estimate proved above. Subtracting \(\sup_X U_\alpha\) changes none of these conclusions. Each \(\sigma_j\) and hence \(\rho_\alpha\) ignores pluripolar sets by Lemma 5.27.25.

**Dependencies/limits.** This does not prove all bounded Bedford–Taylor/CLN facts anew, all Hermitian existence results, or the downstream statements 15.26.3–4; those stay conditional on their original prerequisites. It does not claim that the *entire* MA measure is singular, or that every admissible density has a smooth or bounded solution. The prior exponent-\(1/2\) sharpness ID remains independent; the new finding establishes the universal local exponent, its exact smooth radial model and the whole singular-shell \(\alpha\)-family.

## Coverage, verification, and disposition

First selected proof-level coverage: §§14.3, 14.5, and 15.26 (specified paragraphs above). §5.27.25 is an incremental local normalization crosscheck; §15.24.1 and §15.25.1 were consulted only to identify the downstream representative/subsolution dependencies, **not** audited or certified. No complete section, chapter or project is certified. The user-excluded approximation material was not replayed. The two exact derivative/eigenvalue calculations were independently checked algebraically; no project tests, build, GitHub Actions CI, formalization, publication or source/body/registry/tag/main edit was performed.

**Proposed text-only next step:** if adopted later via a separately reviewable content PR, insert the first finding as a quantitative example after §14.3.5 and the second as a local sharpness observation alongside §15.26.2. Retain all provenance, labels and old statements unchanged. Review further nonexcluded sections rather than expanding the excluded regularization dependencies.
