# Dense divisorial poles, strict Lelong semicontinuity, and conformal capacity of ellipses — 2026-10-29

**Pinned production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Review branch:** \`review/mathematical-audit\`. This report audits selected integrated reading-edition arguments; it is not an assertion of complete theorem-chain verification. Source attributions, tags, and distinct versions are preserved. Demailly approximation/regularization and its dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion programme are **deferred-by-user**, not examined or certified here.

## A. Countably dense divisors do not invalidate the finite-mass domination criterion

**Stable finding ID:** \`POME-DENSE-DIVISOR-LOCI-DOMINATION-001\`. **Severity/status:** low / **verified conditional deduction** (explicit model and direct proof, conditional on the printed divisorial-removal lemma, not a new false theorem).

**Integrated anchor:** \`docs/sections/plurisubharmonic-functions-and-singularities--lelong-numbers-and-divisorial-estimates/index.html\`, main blob \`483b94209054b7a076757be189afb887fc37c7cf\`. Lemma **5.38.1**, source \`non-kahler-pluripotential-theory:71AD1E73\`, permanent tag \`3AA98220C897\`, physical lines **14–35**; Lemma **5.38.5**, source \`non-kahler-pluripotential-theory:F5990C9E\`, permanent tag \`65C35F77CB06\`, physical lines **90–118**; Corollary **5.38.6**, source \`non-kahler-pluripotential-theory:8089ED26\`, permanent tag \`F5277854ECB3\`, physical lines **119–134**. This section was recorded as inventory-only in the prior coverage matrix.

**Exact hypotheses being tested:** The printed Lemma 5.38.5 permits a *countable* family of distinct prime divisors with positive coefficients, provided their integration-current series has finite mass; it does **not** assume locally finite support. The ambient compact complex manifold is connected and a reference quasi-psh potential \`v\` satisfies \`dd^c v=S-\beta\` for a smooth real form \`\beta\`.

Take \`X=P^1\times P^1\`, and write \`\pi_1\` for the first projection. Normalize the Fubini–Study form \`\omega\` on \`P^1\` by \`\int_{P^1}\omega=1\`, using the project convention \`dd^c=(i/2\pi)\partial\bar\partial\`. Choose pairwise distinct points \`p_j\` forming a dense subset of \`P^1\`, set \`c_j=2^{-j}\`, and put \`D_j=\{p_j\}\times P^1\`. For homogeneous coordinates \`p=[p_0:p_1]\`, \`z=[z_0:z_1]\` define the globally defined quasi-psh weight
\[
 q_p(z)=\log\frac{|p_0z_1-p_1z_0|^2}
 {(|p_0|^2+|p_1|^2)(|z_0|^2+|z_1|^2)}\leq0.
\]
Poincaré–Lelong in the stated normalization gives \`dd^c q_p=[p]-\omega\`. Because the round \`SU(2)\` action is transitive and preserves \`\omega\`, \`\|q_p\|_{L^1(\omega)}\` is the same finite constant for every \`p\`. Thus
\[
 Q=\sum_{j=1}^{\infty}2^{-j}q_{p_j}
\]
is an \`L^1\` limit of a decreasing sequence of quasi-psh functions with the **common** lower bound \`dd^c Q_N\geq-\omega\`; it is not identically \`-\infty\`. Distributionally
\[
 \omega+dd^cQ=\sum_{j\geq1}2^{-j}[p_j].
\]
Let \`v=\pi_1^*Q\`, \`\beta=\pi_1^*\omega\`, and \`S=\sum 2^{-j}[D_j]\`. Then \`dd^c v=S-\beta\`. Relative to the product Kähler form \`\Omega=\pi_1^*\omega+\pi_2^*\omega\`, the total mass is
\[
 \int_X S\wedge\Omega=\sum_{j\geq1}2^{-j}=1.
\]
Yet \`\bigcup_jD_j\` is dense in \`X\`; the family is not locally finite, and the pole set of \`v\` contains every \`D_j\`. Moreover the generic Lelong number along \`D_j\` is exactly \`2^{-j}\`, by restriction of the positive current \`S\` to its divisorial component.

To verify the delicate implication in the printed lemma *without a hidden separation hypothesis*, take any \`a\in QPSH(X)\` with \`\nu(a,D_j)\geq 2^{-j}\` for **every** \`j\`. Choose a smooth Hermitian form \`\Lambda\` with \`\Lambda+dd^ca\geq0\`. For each \`N\`, Lemma 5.38.1 (which explicitly allows nonclosed smooth background forms) implies
\[
 \Lambda+dd^ca-\sum_{j=1}^N2^{-j}[D_j]\geq0.
\]
All currents are locally finite and the partial sums converge weakly to \`S\`; the cone of positive currents is weakly closed, so \`\Lambda+dd^ca-S\geq0\`. Hence \`dd^c(a-v)\geq\beta-\Lambda\` as distributions. After a local smooth correction, \`a-v\` has a plurisubharmonic representative. Compactness makes that quasi-psh representative bounded **above**, yielding \`a\leq v+C\` almost everywhere and, by the established quasi-psh comparison of §5.24.3, everywhere in the usual extended-valued sense. The reverse ordinary-to-Lelong implication is immediate from monotonicity of generic Lelong numbers. The intervening ideal-domination clauses are those already printed in §§5.33 and 5.37 and are not independently recertified here.

**Conclusion / action:** The countable, non-locally-finite hypothesis in Lemma 5.38.5 passes an explicit dense-divisor stress test. **Do not add a spurious local-finiteness assumption.** An optional internal example could document the sharp distinction between locally finite divisors and a finite-mass current with dense support. This selected implication relies on the established local divisorial-removal theorem (with its Siu-decomposition input) and the quasi-psh inequality extension; their complete upstream proofs were not audited. **Affected dependents:** Corollary 5.38.6, ordinary-versus-ideal singularity-type comparisons, finite-mass divisorial constructions.

## B. Strictness of upper semicontinuity of Lelong numbers at a fixed point

**Stable finding ID:** \`POME-MOVING-POINT-LELONG-STRICT-LIMSUP-001\`. **Severity/status:** low / **verified conditional deduction**, not an error in the printed inequality.

**Integrated anchor:** same \`docs/sections/plurisubharmonic-functions-and-singularities--lelong-numbers-and-divisorial-estimates/index.html\`, same main blob; **Lemma 5.38.7**, source \`non-kahler-pluripotential-theory:D9AC87CF\`, permanent tag \`E04E4D6C502E\`, physical lines **135–149**; use also **Lemma 5.38.8**, source \`non-kahler-pluripotential-theory:519C12FA\`, tag \`1792691862B8\`, lines **150–178**, for the stated common compact curvature/Lelong framework.

The printed assertion is
\[
 u_j\longrightarrow u\ \mathrm{in}\ L^1_{\mathrm{loc}},
 \quad dd^c u_j,\ dd^c u\geq-\beta
 \ \Longrightarrow\ 
 \nu(u,x)\geq\limsup_j\nu(u_j,x)
 \quad\text{for fixed }x.
\]
It cannot generally be strengthened to equality even for globally normalized, analytic divisorial weights on \`P^1\` with the same curvature lower bound and constant total curvature mass. Fix \`p\in P^1\` and distinct \`p_j\ne p\` converging to \`p\`, and take \`u_j=q_{p_j}\`, \`u=q_p\` as in part A. These satisfy \`\sup u_j=\sup u=0\` and
\[
 dd^c u_j=[p_j]-\omega,\qquad dd^cu=[p]-\omega.
\]
Rotations in \`SU(2)\` sending \`p\` to \`p_j\` can be chosen to tend to the identity; continuity of their action on \`L^1(P^1,\omega)\` proves \`u_j\to u\` in \`L^1\`. At the fixed point \`p\`, \`u_j\` is smooth nearby (for each fixed \`j\`), so \`\nu(u_j,p)=0\`; however \`\nu(u,p)=1\`. Thus
\[
 1=\nu(u,p)>0=\limsup_{j\to\infty}\nu(u_j,p).
\]
As a related topological check, \`[p_j]\rightharpoonup[p]\` while \`\|[p_j]-[p]\|_{\mathrm{TV}}=2\` for all \`j\`, so the argument uses neither total-variation convergence nor regularization. The printed Lemma 5.38.7 remains **correct**; its one-sided inequality is optimal. No uniformity in the moving point is being asserted.

**Action / dependents:** Optional example following §5.38.7, with fixed-point quantifiers intact. Useful for statements about moving exceptional loci and Lelong limits, but not a new positivity or approximation theorem.

## C. Exact conformal logarithmic capacity and equilibrium law for filled ellipses

**Stable finding ID:** \`POME-PLANAR-ELLIPSE-GREEN-CAPACITY-001\`. **Severity/status:** low / **verified conditional deduction**, not a false theorem.

**Integrated anchor:** \`docs/sections/planar-green-functions-and-conformal-maps/index.html\`, main blob \`bfee348bb5f4bbfaa4515e5c9333789a13dae861\`, Proposition **3.8.2**, source \`klimek-pluripotential-theory:886FBC1A\`, permanent tag \`3F05222ECC9E\`, physical lines **54–70**. The Riemann mapping and exterior minimality conventions in §3.8.1–2 were checked only where used; earlier audit treatments of the level-set capacity, polar exceptional boundary points, and Joukowski *real-cube* estimates are distinct and are **not** re-registered as new findings.

Let
\[
 K_{a,b}=\bigl\{x+iy:x^2/a^2+y^2/b^2\leq1\bigr\},
 \qquad a>b>0,
\]
and write \`c=(a+b)/2\`, \`\kappa=(a-b)/(a+b)\in(0,1)\`. The Laurent polynomial
\[
 F(w)=c\left(w+\frac{\kappa}{w}\right)
\]
is conformal from \`\{|w|>1\}\` onto \`\mathbb C\setminus K_{a,b}\`. Indeed,
\[
 F(e^{it})=a\cos t+ib\sin t,\qquad
 F(w_1)-F(w_2)=c(w_1-w_2)\left(1-\frac{\kappa}{w_1w_2}\right).
\]
For \`|w_i|\geq1\`, the second factor is never zero; \`F'(w)=c(1-\kappa/w^2)\ne0\` outside the closed unit disk. The simple Jordan boundary and behavior at infinity establish the claimed onto image. Therefore \`G(z)=\log|F^{-1}(z)|\` is positive harmonic outside the ellipse, continuous with zero boundary value, bounded near the finite boundary, and has logarithmic growth. Its asymptotic
\[
 G(z)=\log|z|-\log c+o(1)\qquad(z\to\infty)
\]
identifies it with \`V_{K_{a,b}}^*\` by the minimality/uniqueness clause of Proposition 3.8.2 and gives the **exact logarithmic capacity**
\[
 \operatorname{cap}(K_{a,b})=\frac{a+b}{2}.
\]
It also identifies the equilibrium probability measure, in the \`\Delta\log|z|=2\pi\delta_0\` convention:
\[
 \mu_{K_{a,b}}=F_*\left(\frac{dt}{2\pi}\bigg|_{|w|=1}\right).
\]
To see the latter, the distributional normal-flux jump of the continuous function \`G\` extended by zero across its smooth boundary is \`(2\pi)^{-1}\Delta G\`; conformal invariance of flux transports the exterior \`(2\pi)^{-1}\Delta\log|w|\` boundary flux (harmonic measure at infinity) to the ellipse. As \`b\downarrow0\` at fixed \`a\`, the boundary parametrization becomes \`a\cos t\`; thus the equilibrium laws converge weakly to the arcsine law \`dx/(\pi\sqrt{a^2-x^2})\` on \`[-a,a]\`, and the capacities tend to \`a/2\`. This degeneration is a consistency check, not a claim of uniform boundary smoothness at \`b=0\`.

**Action / dependents:** Optional sharp example following §3.8.2, preserving its historical attribution and conventions. Useful for planar Green functions, classical capacity, and convex examples; no modification of the printed proposition and no duplicate/canonicalization recommendation.

## Coverage, statuses and limits

This run **first directly inspected nonexcluded selected statements and proof steps §5.38.1, .5–.8** (including the finite-to-countable current limit), and **incrementally checked §3.8.2** via a conformal-model proof. It did **not** audit §5.38.9 onward: local Bergman estimates there belong to the user-deferred dedicated scope. Sections §5.24, §5.33, §5.37, and §10.4 are **dependency/context only**, not newly certified. The original inventory remains **25 chapters / 747 distinct numbered table-of-contents sections / zero certified complete sections**. The three IDs above are new conditional deductions/explicit stress tests; none is a new confirmed error, an unconditional repair, or a proof of all upstream inputs. No prior ledger item is closed or reclassified, and no source text, registry, permanent tags, main, published website, CI, or formalization is changed.