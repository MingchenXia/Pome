# Sharp local \(L^p\) removability across coordinate strata of complete Reinhardt domains

**Finding:** POME-REINHARDT-LP-AXIS-REMOVABILITY-001  
**Date:** 2026-11-12  
**Classification:** low / **verified conditional deduction** (with a sharp counterexample to an *unclaimed strengthening*, not a printed false theorem).  
**Production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (read freshly this session).  
**Integrated reading page:** \`docs/sections/reinhardt-domains-and-logarithmic-convexity/index.html\`, blob \`51d14c9874a7f3ec3a4886644749db8ddb82d923\`; **section 9.62** (permanent tag \`C236D3977F38\`).  
**Precise anchors:** Lemma 9.62.3, source \`demailly-complex-geometry:C667FC59\`, permanent \`9179B3F88EE7\`, physical lines **38–69**; its domain definition (9.62.4), source \`demailly-complex-geometry:5E4E8360\`, permanent \`591389D2112E\`, lines **40–43**; Theorem 9.62.6, source \`demailly-complex-geometry:463F81C1\`, permanent \`2A0C2847FC1E\`, physical lines **86–112**. Proposition 9.62.2 (\`demailly-complex-geometry:D34443BE\`, permanent \`B7A5F2850576\`, lines **16–36**) was read for the distinction between the punctured Reinhardt domain and its coordinate completion.

## Precisely new result

Let \(n\ge1\), let \(D\subset\mathbb R^n\) be any nonempty **open convex coordinatewise downward-closed** set, and define
\[
 U=\widetilde\Omega_D
 =\{z\in\mathbb C^n:\exists x\in D,\ |z_j|\le e^{x_j}\text{ for all }j\},\qquad
 U^\times=U\cap(\mathbb C^*)^n=\Omega_D^*.
\]
The elementary geometric identification \(U^\times=\Omega_D^*\), the openness of \(U\), and inclusion of its coordinate strata are exactly the assertions checked in the proof of Lemma 9.62.3.

**Theorem (sharp axis-removability threshold).** Suppose \(f\in\mathcal O(U^\times)\), \(p\ge2\), and
\[
 \int_{K\cap U^\times}|f|^p\,dV_{2n}<\infty
 \quad\text{for each compact }K\Subset U.
\]
Then \(f\) admits a **unique** extension \(F\in\mathcal O(U)\). Its \(|F|^p\) is locally integrable and the extension does not change any of the above integrals. The lower bound \(p\ge2\) is optimal **for every such \(D\)**: if \(0<p<2\), the holomorphic function \(f(z)=z_1^{-1}\) on \(U^\times\) is locally \(L^p\) on \(U\) but cannot extend holomorphically across the origin.

This conclusion is not stated in 9.62.3 or 9.62.6. In particular, the previously established pseudoconvexity of \(U\) does **not**, by itself, make arbitrary holomorphic functions on \(U^\times\) extendible: the \(L^p\) hypothesis is essential.

## Full local proof, including the borderline exponent

**One-variable coefficient estimate.** Let \(h\) be holomorphic on \(\Delta_R^*=\{0<|z|<R\}\) and \(h\in L^p(\Delta_R)\) for some \(p\ge2\). For \(m\ge1\), its Laurent coefficient is
\[
 a_{-m}=\frac{1}{2\pi i}\int_{|z|=r}h(z)z^{m-1}\,dz
 =\frac{r^m}{2\pi}\int_0^{2\pi}h(re^{it})e^{imt}\,dt
 \quad(0<r<R).
\]
Since \(p\ge1\), Hölder's inequality gives
\[
 \frac{1}{2\pi}\int_0^{2\pi}|h(re^{it})|^p\,dt
 \ge |a_{-m}|^p r^{-mp}.
\]
Hence, if \(a_{-m}\ne0\),
\[
 \int_{|z|<R_0}|h|^p\,dA
 \ge 2\pi|a_{-m}|^p\int_0^{R_0}r^{1-mp}\,dr=+\infty
 \quad (0<R_0<R),
\]
because \(mp\ge2\). All negative Laurent coefficients therefore vanish and \(h\) extends holomorphically across \(0\). This calculation explicitly includes the logarithmically divergent case \(m=1,p=2\).

**Joint extension without a sequential compactness shortcut.** Fix \(a\in U\). Because \(U\) is open, choose a closed polydisc \(Q\Subset U\) centered at \(a\) and, if \(a_j\ne0\), shrink its \(j\)-th radius so that no zero occurs in that coordinate. Write \(I=\{j:a_j=0\}\), so on the interior \(Q^\circ\) the original domain is the product of punctured discs in the coordinates \(I\) and ordinary discs in the others. Fix \(j\in I\) and denote the remaining variables by \(w\). Tonelli's theorem gives \(f(\cdot,w)\in L^p\) on the punctured \(z_j\)-disc for **almost every** \(w\) in the corresponding product of nonzero-coordinate discs. The one-variable estimate kills all its negative Laurent coefficients for almost every such \(w\).

For each \(m\ge1\), the Laurent coefficient
\[
 a_{-m}(w)=\frac{1}{2\pi i}\int_{|z_j|=\rho}
              f(z_j,w)z_j^{m-1}\,dz_j
\]
is holomorphic in \(w\) on that connected product; it vanishes a.e., hence identically by continuity (indeed holomorphy). Consequently the Cauchy integral
\[
 F_j(z_j,w)=\frac{1}{2\pi i}\int_{|\zeta|=\rho}
 \frac{f(\zeta,w)}{\zeta-z_j}\,d\zeta,\qquad |z_j|<\rho,
\]
is jointly holomorphic and agrees with \(f\) wherever \(z_j\ne0\). Varying \(\rho\) extends across the entire \(j\)-axis slice of \(Q^\circ\). The extension agrees a.e. with \(f\), so it retains the same local \(L^p\) property. Repeat for the **finite** set \(I\); after removing all coordinate punctures one obtains a holomorphic extension on \(Q^\circ\). Local extensions agree on nonempty open intersections of \(U^\times\) with overlapping polydiscs, hence agree everywhere on overlaps by the identity theorem. They glue to \(F\in\mathcal O(U)\). The dense set \(U^\times\) guarantees uniqueness. Adding measure-zero coordinate hyperplanes changes no local integrals.

There is no use of Demailly approximation/regularization, \(L^2\) solution operators, Ohsawa–Takegoshi extension, Bergman kernels, or a positivity-loss argument. The elementary integrability condition with exponent \(2\) happens to involve \(L^2\) as a **function space**; it is not the excluded dedicated \(L^2\) proof-completion programme.

**Sharpness on every allowed domain.** The same Lemma 9.62.3 shows \(0\in U^\circ\). Let \(f=z_1^{-1}\) on \(U^\times\). For every compact \(K\Subset U\), a finite covering by polydiscs gives
\[
 \int_{K\cap U^\times}|f|^p\,dV_{2n}<\infty
 \quad\Longleftrightarrow\quad p<2,
\]
using \(\int_0^\epsilon r^{1-p}\,dr<\infty\) precisely for \(p<2\). Since any neighborhood of zero contains points with all coordinates nonzero and arbitrarily small \(z_1\), no holomorphic extension exists.

More generally, for the Laurent monomial \(z^\alpha=\prod z_j^{\alpha_j}\), \(\alpha\in\mathbb Z^n\), on \(U^\times\), local \(L^p\) integrability **at the origin** holds exactly when
\[
 p(-\alpha_j)<2\quad\text{for every coordinate with }\alpha_j<0.
\]
This follows by Fubini from the nonnegative product integral; equality is logarithmically divergent. The formula is a sharp family of independent checks on the exponent and coordinate-stratum quantifiers.

## Scope and dependency classification

- **Source statements:** Lemma 9.62.3 and Theorem 9.62.6 remain **not refuted**. The present theorem is a new, verified conditional deduction about their coordinate completion \(U\).
- **Internal dependency:** the identification and openness of \(U^\times\subset U\) are taken from the printed proof of Lemma 9.62.3; their specific geometry was reread. All analytic extension steps above are elementary and explicitly proved.
- **Missing obligations:** this is **not** a complete independent verification of Proposition 9.62.2, all convex-exhaustion prerequisites or Theorem 9.62.6's general pseudoconvexity argument. No general singular-extension theorem is certified.
- **Correction proposal:** no source correction. If useful, add a separate corollary after §9.62.3 stating the precise \(p\ge2\) conclusion with the \(z_1^{-1}\) sharpness example; preserve all existing permanent tags and canonical versions.
- **Affected dependents:** any future argument using axis completion \(\Omega_D^*\subset\widetilde\Omega_D\) to extend \(L^p\)-integrable holomorphic coefficients. Unqualified holomorphic extension is **false**, even when the completion is pseudoconvex.
- **Audit coverage:** §9.62 was previously partially sampled. **Zero new first-visited numbered sections, zero newly fully certified sections.** Current ToC: **25 chapters, 747 numbered sections**. Existing unresolved/candidate/error ledger entries unaffected.
- **Deferred-by-user:** the Demailly approximation/regularization and dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion programme remains deferred, neither resolved nor audited.
- **Operational verification:** directly read the main HTML and branch documentation/coverage; performed the symbolic proof above. **No mathematical formalization, project tests, builds, CI or website publication**.
