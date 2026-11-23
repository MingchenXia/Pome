# Direct audit of Gauduchon trace topology, smooth normalization, and unibranch descent — 2026-11-23

**Reviewed main SHA:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Audit-only branch:** \`review/mathematical-audit\`. Examined the current integrated reading-edition HTML rather than merely the source chapter headings. The full current mathematical text of §§11.31 and 14.18 was read directly; §9.10 was selectively rechecked as a different subject (its principal arguments had been examined on 2026-11-22). Historical first-visit claims remain **LEGACY-UNRECONCILED**. This report contains two **verified conditional deductions**, not false printed theorems, complete transitive verification, or new canonicalization defects.

## POME-GAUDUCHON-SURFACE-SCALAR-KL-001 — exact Kullback–Leibler interpretation on Gauduchon surfaces

**Severity/status:** low / **verified conditional deduction**. The smooth existence, uniqueness, and adjoint-measure facts are taken from existing §14.10–14.13 and §14.18, not independently certified here. In particular, do **not** relog the preexisting \`POME-GAUD-ADJOINT-GRADIENT-MONO-001\` general monotonicity/Bregman finding: **only the surface relative-entropy identification** below is new.

**Anchors:** \`docs/sections/smooth-monge-ampere-equations--normalization-for-the-gauduchon-equation/index.html\`, main blob \`07303e817cd642d6f34b8ff2c1b876a4b299c4ac\`; Theorem **14.18.2**, source \`non-kahler-pluripotential-theory:67056566\`, permanent tag **F90961841CA0**, mathematical lines **22–62**; Example **14.18.3**, source \`non-kahler-pluripotential-theory:D7692D79\`, tag **8AC1A3B0F2AF**, lines **69–77**. The normalization \(\mu_F^\gamma=e^F\gamma^2/\int_Xe^F\gamma^2\) and scalar formula in line 75 are essential.

**Claim (under the section's compact connected surface and smooth solvability assumptions):** Let \(F,G\in C^\infty(X,\mathbb R)\), \(H=G-F\), and let \(b_\gamma\) be the smooth Gauduchon scalar of §14.18. If \(\gamma_0\) is the Gauduchon surface form in Example 14.18.3, put
\[
Z_F=\int_X e^F\gamma^2,\qquad \mu_F^\gamma=\frac{e^F\gamma^2}{Z_F}.
\]
Then the **oriented concavity gap** satisfies the *exact* identity
\[
\boxed{\ b_\gamma(F)-\int_XH\,d\mu_F^\gamma-b_\gamma(G)
=\mathrm{KL}(\mu_F^\gamma\Vert\mu_G^\gamma)
=\log\!\int_Xe^H\,d\mu_F^\gamma-\int_XH\,d\mu_F^\gamma.\ }
\]
In particular it is nonnegative, and zero if and only if \(G-F\) is constant (the smooth measures have strictly positive densities). Reversing \(F,G\) and adding yields the symmetrized identity
\[
\boxed{\ \int_XH\,d(\mu_G^\gamma-\mu_F^\gamma)
=\mathrm{KL}(\mu_F^\gamma\Vert\mu_G^\gamma)
+\mathrm{KL}(\mu_G^\gamma\Vert\mu_F^\gamma).\ }
\]

**Complete algebraic proof:** Example 14.18.3 gives \(b_\gamma(F)=C-\log Z_F\), \(C=\log\int_X\gamma_0^2\), and Theorem 14.18.2 gives \(Db_\gamma(F)[H]=-\int H\,d\mu_F^\gamma\). The density ratio is
\[
\log\frac{d\mu_F^\gamma}{d\mu_G^\gamma}
=\log(Z_G/Z_F)-H,\qquad Z_G/Z_F=\int_Xe^H\,d\mu_F^\gamma.
\]
Integrating the logarithm against \(\mu_F^\gamma\) yields the claimed formula. Gibbs/Jensen inequality yields nonnegativity, with equality precisely when \(e^H\) is almost everywhere constant and hence \(H\) is constant by smoothness and full support. For the reversed gap, replace \(H\) by \(-H\) and subtract the two first variations; all logarithmic partition-function terms cancel. This proof does not differentiate a singular family or infer continuity from finite \(L^p\) convergence of logarithmic densities. **Scope:** smooth surface case only; no extension to the general Gauduchon ansatz, weak solutions, or arbitrary Hermitian dimension is claimed.

**Proposed optional correction/addition:** an independent corollary after Example 14.18.3 identifying the signed Bregman gap with relative entropy, preserving Theorem 14.18.2, its tags and historical attribution. **Potential dependents:** stability and identifiability of smooth surface normalization, convex duality of probability densities, monotonicity of adjoint probabilities. These applications remain conditional on the existing smooth PDE results.

## POME-GAUDUCHON-TRACE-CROSS-METRIC-HOLDER-001 — cross-background trace metrics are quantitatively bi-Hölder

**Severity/status:** low / **verified conditional deduction**, not a printed theorem error. The resulting exponent is a universal *sufficient* modulus; it is **not** claimed optimal for a fixed pair of backgrounds (the identical-background map is Lipschitz).

**Anchors:** \`docs/sections/gauduchon-traces-and-the-topology-of-potentials/index.html\`, main blob \`1516feb665870be31c5be159edb6c2cf1898db8c\`; Theorem **11.31.2**, source \`non-kahler-pluripotential-theory:8C0421FB\`, permanent tag **160CE026081B**, lines **32–62**; Corollary **11.31.6**, source \`non-kahler-pluripotential-theory:7FBCB410\`, tag **AA6333BC6B20**, lines **94–115**; Proposition **11.31.7**, source \`non-kahler-pluripotential-theory:5B0B54B7\`, tag **56D7737A1AF0**, lines **120–157**.

**Claim:** Fix \(X,\theta,dV\) and the same compact normalized convex potential space \(\mathcal K^0_{\theta,dV}\) from §11.31. Let \((\gamma_1,d_1),(\gamma_2,d_2)\) be two admissible Gauduchon-background/Riemannian-distance choices, and let \(D_i\) denote their bounded-Lipschitz trace metrics. Then there are finite \(A,B>0\), depending on these fixed choices, such that for every pair \(u,v\in\mathcal K^0_{\theta,dV}\),
\[
\boxed{\ D_2(u,v)\le A D_1(u,v)^{1/2},\qquad
D_1(u,v)\le B D_2(u,v)^{1/2}.\ }
\]
Equivalently, the canonical identification of the two compact **trace-measure images** \(T_{\gamma_2}\circ T_{\gamma_1}^{-1}\) and its inverse have the displayed \(1/2\)-Hölder moduli when each image carries its bounded-Lipschitz metric. This strengthens the bare uniform equivalence (uniform continuity in both directions) of §11.31.6, but makes no sharpness claim.

**Proof:** Proposition 11.31.7 gives constants \(C_i\ge1\) such that for \(w=u-v\),
\[
C_i^{-1}\|w\|_{L^1}\le D_i(u,v)\le C_i\|w\|_{L^1}^{1/2}.
\]
Use \(\|w\|_{L^1}\le C_1D_1(u,v)\) in the upper estimate for \(D_2\) to obtain \(D_2\le C_2 C_1^{1/2}D_1^{1/2}\); reverse the roles for the other inequality. The zero-total-trace-mass singleton case also satisfies both trivially. As Theorem 11.31.2 is an injective homeomorphism onto each image, conjugating this estimate produces the measure-image formulation. No algebraic identification of distinct trace measures is silently made: the map is specifically \(T_{\gamma_2}\circ T_{\gamma_1}^{-1}\).

**Proposed optional addition:** record a cross-background quantitative corollary to Proposition 11.31.7, retaining its original source labels and tags. **Potential dependents:** quantitative comparison of Gauduchon trace topologies and compactness arguments with changing fixed auxiliary metrics. The constants need not remain uniform if the backgrounds degenerate.

## Direct reading and hypothesis/dependency audit

### §11.31 — entire present-main mathematical section directly read

- **Trace map (§11.31.1–4, lines 20–92):** checked \(Af=(dd^cf\wedge\gamma^{n-1})/dV\), adjoint compatibility \(A^*1=0\) from Gauduchon, fixed total mass, and why injectivity requires elliptic regularity, componentwise maximum principle and the mean-zero normalization. The image criterion needs positivity of the *full* reconstructed \((1,1)\)-current, not merely nonnegativity of its trace measure; the curve special case is correctly separated.
- **Metric (§11.31.5–8, lines 94–179):** checked that the common-mass bounded-Lipschitz metric metrizes weak convergence by finite uniform nets (Arzelà–Ascoli), and that a compact homeomorphism gives uniform continuity but **not** by itself a bi-Lipschitz comparison. Examined the \(W^{2,p}\), \(p>2n\), inverse-adjoint estimate and mollification at scale \(\varepsilon\), including the signed measure bound \(2M\). For Example 11.31.8, \(\dd^c(\cos(2\pi kx)/(2\pi k^2))=-\tfrac12\cos(2\pi kx)\eta\), consistent with \(dd^c=(i/2\pi)\partial\bar\partial\), so the reported \(k^{-1}\) versus \(k^{-2}\) scales and the sharp \(1/2\) exponent have the correct signs and normalization. This example's original sharpness is **not** relogged as a new discovery.
- **Continuous potentials (§11.31.9–11, lines 181–262):** checked integration by parts \(\int dv\wedge d^cv\wedge G=-\int v\,dd^cv\wedge G\), the \(2CM\|a-b\|_\infty\) variation bound, the positive matrix-measure Cauchy–Schwarz step, and the *order of limits* in the joint \(u_j,G_j\) convergence: first \(j\to\infty\) for a fixed smooth approximant \(a_k\), then \(k\to\infty\). The proof uses smooth approximants from §5.42.5; this is **recorded as an upstream input only**, not independently validated or expanded as an approximation programme. No transitive theorem certification.

### §14.18 — entire present-main mathematical section directly read

- **Smoothness Lemma 14.18.1 (lines 9–18):** checked dependence on the Hölder-space implicit function theorem and normalized scalar/potential linearization, rather than asserting independent elliptic regularity.
- **Adjoint variation Theorem 14.18.2 (lines 22–62):** checked the \(\frac1{n-1}\log\det_\gamma Q_u\) coefficient, the negative sign and \(1/(n-1)\) in the squared logarithmic derivative, the fact that \(\operatorname{tr}[(Q^{-1}\dot Q)^2]\ge0\) because the matrix is similar to a Hermitian one, and that the adjoint measure is integrated at a fixed time (not silently differentiated). The general Bregman consequence was **already present** under \`POME-GAUD-ADJOINT-GRADIENT-MONO-001\` and has **not** been counted again.
- **Surface Example 14.18.3 (lines 69–77):** checked \(dd^c\gamma_0=0\) implies conservation of \(\int(\gamma_0+dd^cu)^2\), yielding the explicit \(-\log\int e^F\gamma^2\) dependence, from which the *new* relative-entropy identification is proved above. The final mention of future \(L^p\) weak solvability is not treated as an already verified theorem.

### §9.10 — selected recheck only, previous core coverage preserved

\`docs/sections/pluripotential-theory-on-unibranch-spaces/index.html\`, main blob \`6edfa6b19fa7cdbaf0c2665389fa7b3ca338cdf4\`: Zariski connected fibers, source \`sgpt:AFDCC00F\`, permanent tag **E707851D5DBA**, lines **39–66**; extension theorem \`sgpt:EEFC0C9A\`, tag **C69D2F0ABA4F**, lines **140–211**; pullback bijection \`sgpt:D36D019A\`, tag **2DA8FD7B7A99**, lines **216–230**. The proof passes to a finite ramified disk cover and descends subharmonicity; neither a sequential compactness assumption nor a global 1-to-1 lift without ramification is introduced. The Hironaka domination exception is an explicitly quoted permitted external input. The last general extension catalogue in §9.10 remains **dependency-only**, not a new whole-section certificate; all references to the user-excluded regularization programme stay deferred-by-user.

## Ledger/status and boundaries

**This session:** 2 newly entire direct mathematical sections (§11.31, §14.18); 1 selected recheck (§9.10, previously core-reviewed); 2 new **low / verified conditional deductions**; **0 confirmed new false printed theorems, 0 proof gaps promoted to confirmed, 0 complete transitive proof-chain certificates**. The 747-section register is maintained; no historical first-visit count inferred.

**Unresolved / external dependencies (not certified):** §§5.25.2 and 5.24.3 compactness/representative uniqueness; Fredholm and elliptic \(W^{2,p}\) inverse-adjoint estimates for the Gauduchon trace; §5.42.5 smooth approximation quoted, not inspected; §14.10.1 smooth solvability and implicit linearization, §14.12 adjoint kernel, §14.13 determinant formula; §9.10.4 excellence/GAGA, §9.10.13 Fornaess–Narasimhan and the quoted analytic connectedness facts. These remain external/dependency notes rather than confirmed gaps. **Deferred-by-user, neither resolved nor certified:** Demailly approximation/regularization and the dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes.

Only proposed optional additions are given. No source/body/registry/canonicalization/tag edits, main changes, PR merge, site publication, tests, full build or CI occurred in this audit.