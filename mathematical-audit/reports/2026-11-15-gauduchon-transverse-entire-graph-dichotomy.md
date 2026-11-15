# The transverse Gauduchon test for entire graph germs on the projective plane

**Date:** 2026-11-15  
**Finding:** **POME-GAUD-TRANSVERSE-ENTIRE-GRAPH-DICHOTOMY-001**  
**Severity/status:** **low / verified conditional deduction**. The printed Theorem 11.8.1 and Proposition 11.8.2 are correct as used here. This is a new explicit local-versus-global dichotomy, conditional on their stated Lamari/Siu/compactness inputs, **not** a source correction or a transitive certification of those analytic theorems.  
**Reviewed main SHA:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (unchanged).

## Exact reading-edition anchors and dependency ledger

- **Actual ToC:** Chapter 11, §11.8 *Transverse concentration of Gauduchon tests*, within 25 chapters and 747 numbered sections.
- **Integrated main file:** \`docs/sections/gauduchon-metrics-and-linear-mass--transverse-concentration-of-gauduchon-tests/index.html\`; blob \`93c2b63848b752f3ef660c1bcd599d0be1bc1e40\`.
- **§11.8 setup (physical lines 5–22):** normalized smooth positive \(dd^c\)-closed \((n-1,n-1)\) tests, a product chart \((z,\zeta)\), a compactly supported cut-off \(\chi\), normalized planar kernel \(p\), the positive form \(B_\delta\), and \(C_\delta=\sup_\Theta\int B_\delta\wedge\Theta\). Section source label \`non-kahler-pluripotential-theory:22A7F863\`; section permanent tag \`959649DAC54D\`.
- **Theorem 11.8.1 (physical lines 25–53):** source \`non-kahler-pluripotential-theory:8F4DC027\`, permanent \`B0762464DCDC\`. Bounded \(C_{\delta_j}\) on some \(\delta_j\downarrow0\) forces a global analytic hypersurface containing the inner graph. Its proof invokes the generalized Lamari criterion (Theorem 11.6.1, source \`non-kahler-pluripotential-theory:87DC00D0\`, permanent \`88BE3B63D9E5\`), compactness of normalized quasi-psh potentials (Theorem 5.25.2, source \`D9A05B95\`, permanent \`FC59B7D406A3\`), and the Siu analyticity theorem (Theorem 5.34.2, source \`86D804B1\`, permanent \`E911F3E2C8E9\`). These upstream results were **not independently recertified** this run.
- **Proposition 11.8.2 (physical lines 55–81):** source \`non-kahler-pluripotential-theory:79BF143E\`, permanent \`26C9605156BE\`. An effective Cartier divisor agreeing with the local \(\zeta=0\) hypersurface with multiplicity one on the full cut-off chart gives a uniform \(C_\delta\) bound. The full-chart condition is essential and is verified, not dropped, below.
- **Contextual §11.7** \`docs/sections/gauduchon-metrics-and-linear-mass--compactness-and-duality-of-gauduchon-currents/index.html\` blob \`31d17f258f2ff178bf52be3d3f92d5a995878d3a\`, Proposition 11.7.1 source \`non-kahler-pluripotential-theory:C21ACA47\`, permanent \`155386134D9E\`. Its normalized compact cone is used only as in the printed §11.8 argument.

## New exact dichotomy

Let \(X=\mathbf P^2\) with **any** fixed smooth Hermitian form \(\omega>0\). On the affine chart \([1:z:w]\), fix an **entire function** \(f:\mathbf C\to\mathbf C\), relatively compact disks \(U'\Subset U\Subset\mathbf C\), a smooth \(0\le\chi\le1\) compactly supported in \(U\) with \(\chi=1\) on \(U'\), and a sufficiently small radius \(r>0\). The coordinates
\[
(z,\zeta)\longmapsto[1:z:f(z)+\zeta],\qquad (z,\zeta)\in U\times\Delta_r,
\]
are a biholomorphic product chart. Use precisely §11.8's normalization
\[
\sigma_\zeta=\frac{i}{2\pi}d\zeta\wedge d\bar\zeta,\quad
B_\delta=\chi(z)\delta^{-2}p(\zeta/\delta)\sigma_\zeta,\quad
\int_{\mathbf C}p\,\sigma_\zeta=1,\quad
C_\delta(f)=\sup_{\Theta\in\mathcal T_\omega}\int_XB_\delta\wedge\Theta
\]
for \(0<\delta<r\), with \(p\in C_c^\infty(\Delta_1)\), \(p\ge0\).

**Proposition (new conditional deduction).**
\[
\boxed{\quad\sup_{0<\delta<\delta_0}C_\delta(f)<\infty
\quad\Longleftrightarrow\quad
f\in\mathbf C[z].\quad}
\]
More precisely, if \(f\) is a polynomial then the numbers \(C_\delta(f)\) are uniformly bounded for all sufficiently small \(\delta\). If \(f\) is an entire **nonpolynomial** function, then
\[
\lim_{\delta\downarrow0}C_\delta(f)=+\infty .
\]
The statement concerns a **fixed** \(\chi,p,\omega\) as above; it is not a dimension-free rate, nor a general quantitative estimate for the Lelong-level-set theorem.

### Direct proof: polynomial graph

If \(f(z)=\sum_{j=0}^d a_jz^j\), put \(m=\max(1,d)\). The degree-\(m\) homogeneous polynomial
\[
Q(Z_0,Z_1,Z_2)
=Z_0^{m-1}Z_2-\sum_{j=0}^d a_jZ_1^j Z_0^{m-j}
\]
defines an effective Cartier divisor \(D\subset\mathbf P^2\). On the **entire affine chart** \(Z_0\ne0\), its equation is exactly \(w-f(z)=\zeta\), with multiplicity one. Thus it has *no additional local branches* on the chosen product chart, including the support of \(\chi\), and satisfies the full hypothesis of Proposition 11.8.2.

For completeness, take a smooth metric on \(\mathcal O(D)\) whose local frame has norm one near \(\operatorname{supp}\chi\times\{|\zeta|\le\delta_0\}\). If \(s\) is the canonical section and \(\psi_\delta=\log(|s|_h^2+\delta^2)\), the fixed-metric lower bound \(dd^c\psi_\delta\ge-C\omega\) is uniform in \(\delta\). On this flat-frame neighborhood the **exact** \(dd^c=i(2\pi)^{-1}\partial\bar\partial\) normalization gives
\[
dd^c\psi_\delta
=\frac{\delta^2}{(|\zeta|^2+\delta^2)^2}\sigma_\zeta
\ge\frac1{4\delta^2}\sigma_\zeta
\quad (|\zeta|\le\delta).
\]
Let \(P=\|p\|_\infty\) and \(0<\epsilon\le(2C)^{-1}\). Then
\(\omega+\epsilon dd^c\psi_\delta\ge\epsilon B_\delta/(4P)\) globally, and Stokes against any normalized \(dd^c\)-closed \(\Theta\) yields
\[
1=\int_X(\omega+\epsilon dd^c\psi_\delta)\wedge\Theta
\ge\frac{\epsilon}{4P}\int_XB_\delta\wedge\Theta .
\]
Therefore \(C_\delta(f)\le4P/\epsilon\), uniformly. This independently checks the key sign, constant and divisor-localization step in the printed Proposition 11.8.2.

### Elementary projective-closure lemma for a nonpolynomial entire graph

Write
\[
\Gamma_f=\{[1:z:f(z)]:z\in\mathbf C\}\subset\mathbf P^2,\qquad
L_\infty=\{Z_0=0\}.
\]
**Claim:** If \(f\) is entire and not a polynomial, then the ordinary topological closure \(\overline{\Gamma_f}\) contains **every point of \(L_\infty\)**.

For \(|z|>R>0\) put \(g(z)=f(z)/z\). It is holomorphic on the exterior disk and has an **essential** singularity at infinity: if it were meromorphic there, then \(f\) would have at most a pole at infinity and, being entire on \(\mathbf C\), would be a polynomial.

Fix \(a\in\mathbf C\). If there were **no** sequence \(z_k\to\infty\) with \(g(z_k)\to a\), then for some \(R_a,\eta>0\) one would have \(|g(z)-a|\ge\eta\) for \(|z|>R_a\). The bounded holomorphic function \(h=1/(g-a)\) would extend holomorphically across infinity. If \(h(\infty)\ne0\), \(g\) would extend holomorphically there; if \(h(\infty)=0\), \(g\) would have a pole of finite order there. Either contradicts essentiality. Hence there are \(z_k\to\infty\) with \(g(z_k)\to a\), and
\[
[1:z_k:f(z_k)]=[1/z_k:1:g(z_k)]
\longrightarrow[0:1:a].
\]
Finally \(g\) is unbounded near infinity (otherwise the singularity would be removable), so some \(z_k\to\infty\) have \(|g(z_k)|\to\infty\), giving \([0:0:1]\). These points exhaust \(L_\infty\). No Chow theorem, algebraicity of compact analytic sets, or unproved degree theorem enters this lemma; only elementary isolated-singularity theory in one complex variable.

### Direct proof: nonpolynomial graph

If \(C_\delta(f)\not\to+\infty\), there exists \(\delta_j\downarrow0\) and \(M<\infty\) with \(C_{\delta_j}(f)\le M\). Theorem 11.8.1 (its **specific** Lamari/\(L^1\)/Siu argument, rather than any sequence-compactness shortcut) gives a global analytic hypersurface containing the inner open graph \(\{[1:z:f(z)]:z\in U'\}\). Taking an irreducible component \(D_0\) whose intersection with this connected graph contains an open subset, we obtain an **irreducible compact analytic curve** \(D_0\subset\mathbf P^2\) containing that open graph.

The preimage of \(D_0\) under the entire holomorphic map \(z\mapsto[1:z:f(z)]\) is an analytic subset of connected \(\mathbf C\) containing an open set, hence equals \(\mathbf C\). Thus \(\Gamma_f\subset D_0\). Closedness and the projective-closure lemma show \(L_\infty\subset D_0\). But a one-dimensional irreducible analytic curve cannot contain a *distinct* one-dimensional irreducible analytic curve properly. Hence \(D_0=L_\infty\), impossible because \(\Gamma_f\subset\{Z_0\ne0\}\). This contradiction proves the claimed divergence.

Equivalently, for the explicit pair \(f(z)=z\) and \(f(z)=e^z\), **on the same projective plane with the same type of Gauduchon tests**, the first transverse concentration supremum stays bounded and the second diverges. The phenomenon is controlled by the extendability of the **local germ**, not by whether the ambient projective manifold happens to possess other divisors.

## Audit disposition and exact coverage

**No false printed theorem and no newly demonstrated proof gap.** Theorem 11.8.1's three essential stages (global Lamari potential, distributional transverse limit and Siu level-set global component) were reread at lines 29–53, and Proposition 11.8.2's full-chart Cartier hypothesis, curvature bound and \(4P/\epsilon\) coefficient at lines 55–81 were reread and used. The new argument is an optional illustrative corollary immediately after Proposition 11.8.2; retain all historical attribution and existing stable tags. Affected dependents are the §11.7 normalized dual cone and §11.8 divisor-versus-transverse-concentration interpretation; no source, registry, canonicalization or publication modification is authorized.

**Coverage:** §11.8 had a selected 2026-10-22 audit already, so **0 newly first-visited numbered sections, 0 fully certified sections**. The actual ToC remains **25 chapters / 747 numbered sections**. This is a new explicit global-extensibility stress test, not a replay of the earlier §11.7 torus support-face or §11.8 basic divisor example. Lamari, quasi-psh compactness and Siu analyticity are recorded as **conditional internal/external inputs**, not certified here. No project tests, builds, CI or publication were run. Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain **deferred-by-user** and were not entered, checked, or resolved.
