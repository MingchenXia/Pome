# Hopf character bundles, separately smooth subharmonic peaks, and polynomial approximation — 2026-10-29

## Provenance, exact review scope, exclusions

**Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit-branch HEAD:** d470c2736f0beeec46fc6528f4efdd0d7bc7084f. All mathematical text below is about the integrated reading edition actually on the pinned main, not source-book numbering inferred by title.

**New selected proof-level review:** \`docs/sections/polynomial-approximation-and-a-separate-subharmonic-example/index.html\`, blob \`a4a17c61ef30efb6fc6e20f105baeca052bbed43\`, Proposition **3.7.1** source \`klimek-pluripotential-theory:01560C0B\`, tag \`6D285B395FD0\`, physical lines **7–19**; and the untagged accompanying polynomial-peak example, **lines 21–36**, containing section tag \`7AF53FD9F731\`. Checked the grid/Cauchy rational approximation, resolvent open/closed argument, connected complements of slit compacts, and the diagonal peak construction.

**Additional selected direct checking (previously contextual):** \`docs/sections/separate-harmonicity-and-subharmonicity/index.html\`, blob \`1d3c9ebe0d7093f0f069dc2b25b0a47f700f907a\`, Theorem **3.6.1**, source \`klimek-pluripotential-theory:F1182878\`, permanent tag \`58AAF98CC15E\`, lines **7–35**; Theorem **3.6.2**, source \`klimek-pluripotential-theory:BDD09117\`, tag \`95AFE3B73B3D\`, lines **49–93**. Checked the successive submean/upper-bound step and the Baire-strip/harmonic-continuation argument, but did not independently certify all subharmonic compactness and harmonic expansion inputs.

**Incremental direct proof reading (already selected in an earlier audit):** \`docs/sections/meromorphic-sections-and-divisor-classes/index.html\`, blob \`d0c40d1e3f6f515eb13169ed1cd3fb447ca161c8\`, Definition **20.7.2**, source \`demailly-complex-geometry:37374C87\`, tag \`F9B013D39957\`, lines **7–9**, and Proposition **20.7.3**, source \`demailly-complex-geometry:00A05C89\`, tag \`ACC6D09EDDD9\`, lines **12–28**. Examined the holomorphic frame convention, normalization \(\mathrm{dd}^c=\frac{i}{2\pi}\partial\bar\partial\), divisor/Picard exact-image clause and local cocycle cancellation. The prior elliptic-curve finding \`POME-DIVISOR-CHERN-NONPRINCIPAL-001\` is NOT being reclassified or repeated.

**Dependency only:** \`docs/sections/normal-spaces-and-tube-continuation--continuation-on-normal-complex-spaces/index.html\`, blob \`fa09a923ef076a99d638d038020ddd3b884afaa7\`, Theorem **9.38.5**, source \`demailly-complex-geometry:7716022D\`, tag \`F35BA7139EC4\`, physical lines **89–111**, meromorphic Hartogs across normal codimension-two loci; its Remmert–Stein input remains conditional. The scalar Hopf quotient is context only from section 23.1, tag \`142249962360\`, \`docs/sections/unbounded-mass-on-hopf-manifolds/index.html\`, blob \`f53618e8d808de21687ff9166971cb9302ea8cfb\`; none of its Monge–Ampère proofs was checked.

**Excluded by explicit user direction:** Demailly approximation and regularization and the dedicated Bergman/weighted-L2/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof programme were not opened, extended or reconstructed. Earlier notes on that programme remain **deferred-by-user**, neither resolved nor certified.

## POME-HOPF-CHAR-MEROMORPHIC-SECTIONS-001

**Severity low; status verified conditional deduction.** Proposition 20.7.3 is **correct**, including its assertion that the image of the divisor-to-Picard map consists of line bundles *admitting a componentwise nonzero meromorphic section*, not necessarily all line bundles. Here is a sharp explicit obstruction.

Let \(X=(\mathbb C^2\setminus\{0\})/\langle z\mapsto2z\rangle\), a compact scalar Hopf surface. For \(a\in\mathbb C^*\), define the holomorphic character line bundle
\[
L_a=((\mathbb C^2\setminus\{0\})\times\mathbb C)/((z,v)\sim(2z,av)).
\]
A meromorphic section lifts to a nonzero meromorphic \(f\) on \(\mathbb C^2\setminus\{0\}\) satisfying **\(f(2z)=af(z)\)**. Meromorphic Hartogs (Theorem 9.38.5, a *conditional* internal input) extends \(f\) across the origin. Write its meromorphic germ as \(P/Q\), where \(P,Q\) are nonzero holomorphic germs, and let \(P_p,Q_q\) denote their first nonzero homogeneous Taylor polynomials. Choose a complex direction \(\xi\) with \(P_p(\xi)Q_q(\xi)\ne0\). Along \(z=t\xi\),
\[
f(t\xi)=t^{p-q}\frac{P_p(\xi)}{Q_q(\xi)}(1+O(t)),\quad
a=\frac{f(2t\xi)}{f(t\xi)}\longrightarrow2^{p-q}.
\]
Consequently \(a\in2^{\mathbb Z}\). Conversely, for \(a=2^m\), \(m\in\mathbb Z\), the nonzero meromorphic function \(f(z)=z_1^m\) is equivariant and descends to a nonzero meromorphic section. Hence
\[
L_a\text{ admits a nonzero meromorphic section}\quad\Longleftrightarrow\quad a=2^m\ (m\in\mathbb Z).
\]
In particular **\(L_3\) is not isomorphic to \(\mathcal O(D)\) for any divisor \(D\)**: the exact image statement of Proposition 20.7.3 would supply a nonzero meromorphic section otherwise. This is a concrete instance where \(\operatorname{Div}(X)\to\operatorname{Pic}(X)\) is not surjective. It does not purport to classify the entire Hopf Picard group.

**Optional correction, not a body change:** add an explanatory Hopf example after §20.7.3 to warn against replacing an arbitrary holomorphic line bundle by a Cartier divisor. Preserve the original Proposition, Poincaré–Lelong normalization and source attribution. **Affected dependents:** careless identification of all holomorphic line-bundle classes with divisors or trace/b-divisor data. **Unverified dependency:** the general normal-space meromorphic Hartogs theorem's complete proof chain. No original theorem shown false.

## POME-SEPARATE-SMOOTH-SUBHARM-PEAK-001

**Severity low; status verified conditional deduction.** The printed §3.7 example already proves that a finite separately subharmonic function can fail to be jointly upper semicontinuous. We strengthen it by imposing smoothness on **every individual slice** and allowing arbitrarily prescribed diagonal peak growth. Theorem 3.6.1 remains correct with its locally integrable pointwise majorant.

Retain the printed compacts \(K_j\), points \(a_j=j^{-1}e^{i/(j+1)}\), and polynomials \(P_j\) from §3.7, lines 21–28. They satisfy \(0\in K_j\), every fixed \(z\in\mathbb C\) eventually belongs to \(K_j\), \(\|P_j\|_{K_j}<1/2\), and \(P_j(a_j)=j+1\). The polynomial interpolation follows by Proposition 3.7.1 applied to \(K_j\cup\{a_j\}\), whose complement is connected.

Put \(\eta(t)=e^{-1/t^2}\) for \(t>0\), \(\eta(t)=0\) otherwise, and define the smooth flat cutoff
\[
\beta(t)=\begin{cases}\int_0^t(t-s)\eta(s)\,ds,&t>0,\\0,&t\le0.\end{cases}
\]
Then \(\beta,\beta',\beta''\ge0\), \(\beta\in C^\infty(\mathbb R)\), \(\beta(t)=0\) for \(t\le0\), and \(\beta(t)>0\) for \(t>0\). For any prescribed numbers \(R_j>0\) tending to infinity, put
\[
c_j=\frac{\sqrt{R_j}}{\beta((j+1)^2-1)},\quad
b_j(z)=c_j\beta(|P_j(z)|^2-1),\quad
F(z,w)=\sum_{j\ge1}b_j(z)b_j(w).
\]
For every \(j\), \(b_j\) is smooth and subharmonic because
\[
\Delta\beta(|P_j|^2-1)=\beta'(|P_j|^2-1)\Delta|P_j|^2+
\beta''(|P_j|^2-1)|\nabla|P_j|^2|^2\ge0.
\]
For any fixed \(w\), all sufficiently large \(j\) have \(w\in K_j\), hence \(b_j(w)=0\). Thus \(F(\cdot,w)\) is a **finite sum of smooth subharmonic functions**, and likewise \(F(z,\cdot)\) for each fixed \(z\). The value \(F(z,w)\) is finite for every pair. Yet \(F(0,0)=0\), and for every \(j\),
\[
F(a_j,a_j)\ge b_j(a_j)^2=R_j\to+\infty,\qquad(a_j,a_j)\to(0,0).
\]
Consequently \(F\) is **not jointly locally bounded above, upper semicontinuous, or jointly subharmonic**. No *joint* \(C^\infty\) claim is made. Such an \(F\) cannot have the locally integrable pointwise majorant of Theorem 3.6.1, or the theorem would imply joint subharmonicity.

**Optional correction:** present the above smooth-slice strengthening as a supplement to the original §3.7 example without replacing its existing valid version. **Affected dependents:** any unwarranted promotion of separate smoothness/subharmonicity to joint upper regularity or subharmonicity. No Demailly, Bergman, L² or other excluded input occurs.

## POME-POLY-CONNECTED-COMPLEMENT-NECESSITY-001

**Severity low; status verified conditional deduction.** The *correct* Proposition 3.7.1 supplies sufficiency of connected complement for approximation of **functions holomorphic on a neighborhood** of a compact \(K\subset\mathbb C\). For this universal approximation property, the hypothesis is also necessary.

Indeed, if \(\mathbb C\setminus K\) is disconnected it has a bounded complementary component \(H\); choose \(a\in H\). The function \(f(z)=1/(z-a)\) is holomorphic near \(K\). If polynomials \(p_n\) converged uniformly to \(f\) on \(K\), the polynomials \(q_n(z)=(z-a)p_n(z)-1\) would converge uniformly to zero on \(K\). But \(\partial H\subset K\), so the maximum modulus principle on the bounded domain \(H\) would yield
\[
1=|q_n(a)|\le\sup_{\partial H}|q_n|\le\sup_K|q_n|\longrightarrow0,
\]
a contradiction. No smooth boundary or polynomial convexity assumption on \(H\) is required.

**Optional correction:** append this short converse after §3.7.1; do not remove the original connected-complement hypothesis or change the proposition's statement. **Affected dependents:** the \(K_j\cup\{a_j\}\) interpolation of the following example and any use of Mergelyan-type approximation. No false printed theorem is alleged.

## Coverage and unresolved ledger boundary

Newly proof-level inspected only selected passages in **§3.7** (previously contextual); deeper selected **Theorems 3.6.1–2**; incremental **§20.7.3**. Dependency-only **§9.38.5** and standing **§23.1** are not new coverage. Selected proof checks are **not** whole-section certifications, nor a verification of all external/internal inputs. Existing actual ToC inventory remains **25 chapters / 747 numbered sections / zero whole-section certifications**.

All prior confirmed errors, proof gaps, external dependencies, deferred items and historically distinct genuine variants remain unchanged. No changes to main, source material, mathematical body, registry, canonicalization, permanent tags, generated site, build, CI, or formalization. The only authorized changes are audit Markdown documentation on \`review/mathematical-audit\`.
