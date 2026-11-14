# A single continuous admissible potential whose higher Hessian powers charge Sobolev-polar strata

**Finding:** POME-HESS-DIAGONAL-HIGHER-CODIM-001  
**Date:** 2026-11-14  
**Status:** **verified conditional deduction**; **severity:** low (sharpness/extension, **not** a refutation of the reading edition).  
**Reviewed production \`main\`:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`  
**Scope:** current printed Chapter 8, **connected compact complex** \(X\) of dimension \(n\), Hermitian \(\omega>0\), and \(2\le m<n\) (§8.1, physical line 7). This is *not* the \(m=n\) or \(m=1\) theory.

## Precise anchored source interfaces

- \`docs/sections/complex-hessian-equations/index.html\`, main blob \`5331b937ccdaba51f1ec006d5e72dc84f7addfbf\`, §8.1 permanent tag \`CFD38285654D\`, line 7: \(2\le m<n\).
- \`docs/sections/complex-hessian-equations--bounded-potentials-and-recursive-hessian-currents/index.html\`, main blob \`117b866408974cdf706bf305df75e35e1b8affde\`, §8.9, lines 36–56 and 83–115: recursive \(D_p\), positive shifted \(Q_p\). Original source \`non-kahler-pluripotential-theory:61CC9D08\`, permanent tag \`846671D5582A\` (Theorem 8.9.6, lines 96–115); formula (8.9.5) permanent tag \`17FA1BFF2491\`, lines 83–87.
- \`docs/sections/complex-hessian-equations--sobolev-capacity-and-two-hessian-factors/index.html\`, main blob \`25f25433cb9b17de6715a5b05f8b3c15b95a18cd\`, Lemma 8.10.6 original \`non-kahler-pluripotential-theory:350D7B3A\`, permanent \`2A6BE9847309\`, lines 185–205; Example 8.10.7 original \`non-kahler-pluripotential-theory:36B886BE\`, permanent \`AEB4F2397BBF\`, lines 209–246. The example uses **two distinct coordinate potentials**; it does not establish the **diagonal \(p\)-fold** assertion below.
- \`docs/sections/complex-hessian-equations--local-capacities-and-decreasing-products/index.html\`, main blob \`115d285f6b1f76d284463c396e7e87db2b9dbdc3\`, Theorem 8.11.12 original \`non-kahler-pluripotential-theory:B227378C\`, permanent \`C044CD1C65C4\`, lines 281–293: joint decreasing-product identification and weak convergence, used **conditionally** below.

## Exact diagonal statement

For every integer \(p\) with \(2\le p\le m\), **on every** \(X,\omega\) satisfying the preceding hypotheses, there is a *single* globally bounded continuous, even globally \(\omega\)-plurisubharmonic, admissible function \(u\), and a compact coordinate subset \(E\), such that
\[
 \operatorname{Cap}_1(E)=0,\qquad
 \bigl(Q_p(\underbrace{u,\ldots,u}_{p})\wedge\omega^{m-p}\bigr)(E)>0.
\]
Thus no bound \(Q_p(u,\ldots,u)\wedge\omega^{m-p}(F)\le C\,\operatorname{Cap}_1(F)^\gamma\) with \(\gamma>0\), valid for **all** Borel \(F\), holds even for a *single repeated continuous potential*, in any Hessian degree \(p\ge2\).

More precisely, choose a holomorphic coordinate box with \(z_j=x_j+\mathrm i y_j\) for \(1\le j\le n\), a nonnegative smooth cutoff \(\chi\) equal to one on a smaller box, and \(a>0\) sufficiently small. Put
\[
 u=a\chi\sum_{j=1}^p|x_j|\quad\text{(zero outside the chart)},\qquad
 \alpha_j=\frac{\mathrm i}{4\pi}\,\mathrm dz_j\wedge\mathrm d\bar z_j .
\]
Inside the box where \(\chi=1\), for any compact \(E\) lying in
\(\Sigma_p=\{x_1=\cdots=x_p=0\}\) and having nonempty relative interior,
\[
 \boxed{\left.
 Q_p(u,\ldots,u)\wedge\omega^{m-p}
 \right|_E
 =
 \left.
 p!a^p
 \biggl(\prod_{j=1}^p\delta_{\{x_j=0\}}\biggr)
 \alpha_1\wedge\cdots\wedge\alpha_p\wedge\omega^{n-p}
 \right|_E.}
\]
Here a product of one-dimensional Dirac measures means the transverse tensor product with ordinary Lebesgue measure in the remaining real coordinates. The right-hand side has strictly positive mass on \(E\). This restriction identity is stronger than a bare positivity assertion; it does **not** claim that the entire shifted product is concentrated on \(\Sigma_p\).

## Complete local calculation and global construction

1. **Uniform global positivity.** Let \(g_\varepsilon(t)=\sqrt{t^2+\varepsilon^2}\), \(0<\varepsilon\le1\), and set \(u_\varepsilon=a\chi\sum_{j=1}^p g_\varepsilon(x_j)\). Since \(g_\varepsilon''\ge0\), \(g_\varepsilon\) and \(g_\varepsilon'\) are uniformly bounded on the fixed compact cutoff support, the product rule gives
   \[
   \mathrm{dd}^{\mathrm c}\Bigl(\chi\sum_jg_\varepsilon(x_j)\Bigr)\ge -C\omega
   \]
   for one \(C\) independent of \(\varepsilon\). The nonnegative principal terms are \(\chi\,\mathrm{dd}^{\mathrm c}g_\varepsilon(x_j)\); every cross/cutoff derivative is uniformly bounded. Choose \(0<a<(2C)^{-1}\). Then \(\omega+\mathrm{dd}^{\mathrm c}u_\varepsilon\ge\omega/2\) globally. The smooth \(u_\varepsilon\) decrease to the bounded continuous \(u\), so \(u\) is globally \(\omega\)-psh (hence \(m\)-admissible). This elementary absolute-value mollification is **not** Demailly regularization and invokes no dedicated excluded programme.

2. **Exact local product.** With the Pome normalization \(\mathrm{dd}^{\mathrm c}=\frac{\mathrm i}{2\pi}\partial\bar\partial\), on \(\{\chi=1\}\)
   \[
   \mathrm{dd}^{\mathrm c}u_\varepsilon
     =\frac a2\sum_{j=1}^p g_\varepsilon''(x_j)\alpha_j,
   \qquad
   g_\varepsilon''(t)=\frac{\varepsilon^2}{(t^2+\varepsilon^2)^{3/2}},
   \qquad
   g_\varepsilon''(t)\,\mathrm dt\rightharpoonup2\delta_0.
   \]
   Each \(\alpha_j^2=0\). Therefore
   \[
   (\mathrm{dd}^{\mathrm c}u_\varepsilon)^p
      =p!\left(\frac a2\right)^p
       \prod_{j=1}^p g_\varepsilon''(x_j)\,
          \alpha_1\wedge\cdots\wedge\alpha_p
      \rightharpoonup
       p!a^p\prod_{j=1}^p\delta_{\{x_j=0\}}\,
          \alpha_1\wedge\cdots\wedge\alpha_p.
   \]
   To justify tensor-product convergence without an illicit interchange of limits, test against a compactly supported continuous coefficient; first use uniform continuity on a compact box and the one-dimensional probability approximate identities \(g_\varepsilon''/2\); the mass outside any prescribed transverse neighborhood tends to zero. This proves convergence directly in all \(p\) coordinates simultaneously.

3. **Identify the integrated product.** Formula (8.9.5) and the joint weak continuity asserted in Theorem 8.11.12 identify, locally,
   \[
   Q_p(u,\ldots,u)\wedge\omega^{m-p}
   =(\omega+\mathrm{dd}^{\mathrm c}u)^p\wedge\omega^{n-p}.
   \]
   The right side is understood via the just-computed smooth decreasing products, not by a priori multiplying arbitrary singular currents. Expanding the smooth powers, each term of degree \(q<p\) in \(\mathrm{dd}^{\mathrm c}u_\varepsilon\) tends to a sum of product measures supported on intersections of only \(q\) different real hyperplanes \(x_j=0\). Each such measure is absolutely continuous in at least one remaining transverse \(x_\ell\), hence assigns **zero** mass to \(E\subset\Sigma_p\). The \(q=p\) term has the displayed strictly positive restriction density. No general convergence of masses *of closed sets* is inferred from weak convergence alone: the explicit tensor-product limit identifies the entire limiting measures before restricting to \(E\).

4. **Zero Sobolev capacity.** The stratum \(\Sigma_p\) is a smooth real codimension-\(p\) submanifold. Since \(p\ge2\), \(E\) is also contained in the smooth real codimension-two submanifold \(\{x_1=x_2=0\}\) inside the chart. Lemma 8.10.6 gives \(\operatorname{Cap}_1(E)=0\). Strict positivity of \(\omega\) and of the wedge \(\alpha_1\cdots\alpha_p\wedge\omega^{n-p}\), evaluated on the complementary coordinates, gives the strictly positive mass. The claimed failure of every positive power capacity bound follows immediately.

The *coordinate/tensor-product proof* is complete. **Transitive certification of the Pome global current identification is not claimed**: §8.11.12, §8.9.6, and their Hermitian-capacity and decreasing-approximation prerequisites remain internal dependencies. If a future audit changes that calculus, the local calculation remains a valid Bedford–Taylor model but the Pome-specific notation \(Q_p\) must be rechecked.

## Classification and implications

- **Severity:** low. **Status:** verified conditional deduction, not confirmed error, not proof gap, not duplicate.
- **Novelty relative to existing §8.10.7:** one and the same globally continuous \(\omega\)-psh potential appears in *every* factor; any \(p\in[2,m]\), with exact \(p!\) transverse mass, rather than two distinct potentials only at \(p=2\).
- **Affected dependent statements:** §8.10.7 sharpness narrative; §8.11 capacity hierarchy; §8.11.13–14 use \(c_m^*\), not \(\operatorname{Cap}_1\), and are **not** contradicted. No source/theorem/registry/canonicalization edit is authorized in this audit.
- **Proposed optional correction:** add a remark after Example 8.10.7 stating the diagonal all-degree strengthening and cite the elementary local calculation. Do not broaden the first-Hessian \(\operatorname{Cap}_1\) domination.
- **Unresolved/deferred:** general Hessian current chain and full proof-level audit outside the anchored passages remain unresolved; Demailly approximation/regularization and the dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale atlas and positivity-loss programme remain **deferred-by-user**, neither resolved nor certified.
- **Actions:** audit Markdown only. No source edits, build, tests, GitHub Actions, or website publication. No new first-visited numbered section or complete-section certification is claimed.
