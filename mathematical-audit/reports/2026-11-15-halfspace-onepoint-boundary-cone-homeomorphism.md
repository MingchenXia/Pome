# The positive half-space harmonic cone is the measure cone of a compactified boundary

- **Stable ID:** \`POME-HALFSPACE-MARTIN-ONEPOINT-WEAKSTAR-001\`.
- **Date:** 2026-11-15.
- **Severity/status:** **low / verified conditional deduction**; neither a false theorem nor a claim to have completed an upstream proof. The printed Theorems 3.2.2, 3.2.6 and 3.2.12 remain correct on the passages checked.
- **Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; current numbered ToC has 25 chapters and 747 sections.
- **Integrated file:** \`docs/sections/kelvin-transforms-and-half-space-potentials/index.html\`, blob \`f2615a5393af724c3996978212162f94911ff9d9\`.
- **Stable anchors:** section §3.2 \`9728BD930155\`; Theorem 3.2.2 original \`classical-potential-theory:B1AA5815\`, permanent \`97BA27062B9F\`, lines 16–22 and inversion computation lines 27–48; Theorem 3.2.6 original \`classical-potential-theory:1C8A330A\`, permanent \`6BC86EEF03A9\`, lines 64–75; Equation 3.2.7 original \`C0A46F1A\`, permanent \`F3ED29BBAD39\`, lines 66–68; weighted hypothesis Equation 3.2.8 original \`358F89A3\`, permanent \`8F7C774A9D89\`, lines 70–73; ball Poisson derivation and inversion, lines 80–123, particularly 95–97 and 102–123. Theorem 3.2.12 original \`BB6DAC3F\`, permanent \`9ADD2DF19642\`, lines 140–145; normalization equation original \`E7E82020\`, permanent \`AB2849CD8791\`, lines 153–164.
- **Previous, distinct increments:** [2026-11-02 conical high-altitude growth](2026-11-02-half-space-growth-cones-and-escaping-boundary-mass.md) and [2026-11-07 bounded \`L^\infty\` Poisson isometry](2026-11-07-halfspace-bounded-harmonic-poisson-isometry.md). Neither proves the full positive-cone weak-* identification below.

## Precise assertion

Fix an integer \(d\ge2\), \(H=\mathbb R^{d-1}\times(0,\infty)\), \(s=s_{d-1}\), and write \(e=e_d\).
Put \(a=-e\), \(b=-e/2\), \(B=B(b,1/2)\), \(S=\partial B\), and
\[
T(x)=a+\frac{x-a}{|x-a|^2},\qquad
W(z)=(1+|z|^2)^{-d/2},\quad z\in\mathbb R^{d-1}.
\]
The map \(z\mapsto T((z,0))\) identifies \(\mathbb R^{d-1}\) with \(S\setminus\{a\}\), adding **one point at infinity**, \(a\). Denote by \(\mathscr H_+(H)\) the cone of all nonnegative harmonic functions on \(H\), with the compact-open \(C^\infty\) topology. Denote by \(\mathcal M_+(S)\) the finite positive Borel measures on \(S\), with their weak-* topology against \(C(S)\).

**Theorem (conditional on printed positive half-space representation).** The assignment
\[
\begin{aligned}
 h(x',t)&=ct+\frac{2t}{s}
 \int_{\mathbb R^{d-1}}(|x'-z|^2+t^2)^{-d/2}\,d\nu(z),\\
 \mu_h&=\frac{s}{2}c\,\delta_a+
  (T|_{\mathbb R^{d-1}\times\{0\}})_*(W\nu)
\end{aligned}
\tag{1}
\]
is a **unique, additive, positively homogeneous bijection and homeomorphism**
\[
(\mathscr H_+(H),C^\infty_{\rm loc})\ \simeq\
(\mathcal M_+(S),\sigma(\mathcal M(S),C(S))).
\tag{2}
\]
Here \(c\ge0\), \(\nu\) is a positive Radon measure, and \(\int W\,d\nu<\infty\), exactly as in Theorem 3.2.6; \(\nu\) need not have finite unweighted mass. In particular, (2) holds for **arbitrary convergent nets**, not just sequences. At \(x_*=(0,1)\),
\[
\boxed{\ \mu_h(S)=\frac{s}{2}h(x_*)\ }.
\tag{3}
\]
The coefficients \(c\) and the weighted measures \(W\nu\), **taken separately**, are not continuous under this topology: boundary mass can escape horizontally and become the \(ct\) term. This distinction is essential, rather than a proof defect in Theorem 3.2.6.

## Proof

### 1. Exact compactification and mass normalization

Theorem 3.2.6 gives existence of a pair \((c,\nu)\) with \(\int W\,d\nu<\infty\). Thus (1) defines a finite positive measure on compact \(S\). At \(x_*=(0,1)\) the Poisson kernel is \((2/s)W(z)\), so
\[
h(x_*)=c+\frac{2}{s}\int W\,d\nu,
\]
which gives (3).

The exact inversion identities displayed in the integrated proof (physical lines 102–123) yield the ball Poisson formula
\[
h(x)=|x-a|^{2-d}\int_S
\frac{\frac14-|T(x)-b|^2}{(s/2)|T(x)-\zeta|^d}
\,d\mu_h(\zeta).
\tag{4}
\]
Indeed, if \(\zeta=T((z,0))\), the boundary kernel in (4) multiplied by \(|x-a|^{2-d}\) equals
\[
\frac{2t}{s}\frac{|(z,0)-a|^d}{|x-(z,0)|^d},
\]
and \(W(z)=|(z,0)-a|^{-d}\), giving precisely the integral in (1). At the exceptional boundary point \(a\), the corresponding kernel is exactly \((2/s)t\), and its mass \((s/2)c\) gives \(ct\). The same formula defines a smooth nonnegative harmonic \(h\) from **every** finite positive \(\mu\) on \(S\), by the ordinary ball Poisson kernel and Kelvin transform. This establishes surjectivity onto the positive harmonic cone, conditional on the established interior harmonicity and ball Poisson formula in §3.2.

### 2. Uniqueness of the entire representing measure

Let \(v(q)=|q-a|^{2-d}h(T(q))\), \(q\in B\). Its representation (4) is \(v(q)=\int_SP_B(q,\zeta)d\mu_h(\zeta)\).
For \(\varphi\in C(S)\) and \(0<r<1\) let \(q_r(\eta)=b+r(\eta-b)\). The spherical Poisson kernels obey
\[
\int_S\varphi(\eta)v(q_r(\eta))\,dS(\eta)
 =\int_S(P_r\varphi)(\zeta)\,d\mu_h(\zeta),
\tag{5}
\]
where \(P_r\varphi\to\varphi\) **uniformly** on \(S\). This is the standard elementary approximate-identity argument: \(P_r\) has total mass one by the ball Poisson formula, its positive mass concentrates uniformly near the diagonal, and \(\varphi\) is uniformly continuous on compact \(S\). The identity follows from Fubini (finite \(\mu_h\)) and the rotational symmetry \(|q_r(\eta)-\zeta|=|q_r(\zeta)-\eta|\). Thus
\[
\int_S\varphi\,d\mu_h=
\lim_{r\uparrow1}\int_S\varphi(\eta)v(q_r(\eta))\,dS(\eta)
\tag{6}
\]
depends only on \(h\). Consequently \(\mu_h\) is unique. Its atom at \(a\) recovers \(c=(2/s)\mu_h(\{a\})\), and the restriction to \(S\setminus\{a\}\), pulled back and multiplied by \(W^{-1}\), recovers \(\nu\). Therefore the original positive half-space pair is uniquely determined; the printed theorem asserted existence but did not require this stronger topological uniqueness.

### 3. Weak-* convergence implies smooth compact-open convergence

For \(x\in H,\zeta\in S\) denote by \(K(x,\zeta)\) the smooth kernel in (4). For every compact \(K_0\Subset H\) and every multi-index \(\alpha\), \(\partial_x^\alpha K(x,\zeta)\) is jointly continuous, hence bounded and uniformly continuous on \(K_0\times S\). If \(\mu_i\to\mu\) weak-*, their masses are bounded and
\[
\partial^\alpha h_i(x)=
\int_S\partial^\alpha_xK(x,\zeta)d\mu_i(\zeta)
 \longrightarrow
\int_S\partial^\alpha_xK(x,\zeta)d\mu(\zeta).
\]
The convergence is **uniform for \(x\in K_0\)**: use a finite uniform-continuity net of kernel test functions in the supremum norm on \(S\), together with the common mass bound. This argument works for arbitrary directed nets, and proves \(C^\infty_{\rm loc}\) convergence.

### 4. Smooth compact-open convergence implies weak-* convergence, including nets

Suppose \(h_i\to h\) in \(C^\infty_{\rm loc}\). By (3), \(\mu_i(S)=(s/2)h_i(x_*)\to(s/2)h(x_*)\); in particular the net is eventually contained in a fixed bounded subset of \(\mathcal M_+(S)\). On compact \(S\), such a set is weak-* compact (Banach–Alaoglu and positivity).

If \(\mu_i\not\to\mu_h\), take a weak-* neighbourhood \(U\) of \(\mu_h\) and a subnet eventually outside \(U\). The complement of \(U\) is closed; weak-* compactness gives a further convergent subnet with limit \(\widetilde\mu\notin U\). Step 3 shows its harmonic images converge locally smoothly to \(h_{\widetilde\mu}\), whereas the original images converge to \(h\). Hence \(h_{\widetilde\mu}=h\), so Step 2 forces \(\widetilde\mu=\mu_h\in U\), contradiction. This proves the claimed inverse continuity for **nets** without assuming sequential compactness of an arbitrary starting net.

### 5. Exact escaping-mass example: why the infinity atom cannot be discarded

Fix \(c>0\) and any sequence \(|z_j|\to\infty\). Put
\[
c_j=0,\qquad
\nu_j=\frac{s}{2}c(1+|z_j|^2)^{d/2}\delta_{z_j}.
\]
Each \(\nu_j\) satisfies the **exact** weighted hypothesis, with \(\int W\,d\nu_j=(s/2)c\); it has no \(ct\) term. Yet
\[
\mu_j=\frac{s}{2}c\,\delta_{T((z_j,0))}
\ \xrightarrow{\,w^*\,}\ \frac{s}{2}c\,\delta_a,
\]
and its harmonic function is
\[
h_j(x',t)
=c\,t\left(\frac{1+|z_j|^2}{|x'-z_j|^2+t^2}\right)^{d/2}
\ \xrightarrow{\,C^\infty_{\rm loc}\,}\ ct.
\tag{7}
\]
The last limit follows directly by differentiating the rational factor on each compact subset of \(H\), where the denominator divided by \(|z_j|^2\) tends uniformly to one and its nonconstant derivatives tend to zero. On the other hand \(W\nu_j=(s/2)c\,\delta_{z_j}\to0\) **vaguely** on \(\mathbb R^{d-1}\), and all \(c_j=0\). Thus vague convergence of the finite-boundary measures plus convergence of \(c_j\) is **not** enough to recover the harmonic limit: the compactification tracks precisely the missing mass at infinity.

## Disposition, dependencies and precise coverage

This is a verified conditional deduction, **not** a correction to an incorrect statement. The proof independently establishes the uniqueness, compactification, net convergence and escape model once the positive ball/half-space harmonic representation and Kelvin/Poisson identities printed in §3.2 are accepted. The existence of the ball representation in Theorem 3.2.6 (lines 80–100) and the general validity of the compact Laplacian/Poisson background were **not transitively reverified**. No Hironaka input, Demailly approximation/regularization, or dedicated Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, positivity-loss proof-completion programme is used.

**Proposed optional separately reviewable patch:** add a corollary after Theorem 3.2.6 identifying the unique representing pair and the compactified weak-* topology; explicitly distinguish \(C^\infty_{\rm loc}\) stability from coefficientwise convergence. Preserve original source attribution, permanent tags, and distinct versions. **Potential dependents:** positive harmonic compactness, noncompact boundary Poisson limits, uniqueness of half-space representation, and the bounded \(L^\infty\) trace result at Theorem 3.2.12. No identified printed dependent theorem has been disproved.

**Coverage delta:** directly read and checked displayed §§3.2.2/.6/.12 at their named physical lines, with a new proof of the positive-cone topology. §3.2 was **previously partly audited**; **0 newly first-visited sections and 0 fully certified sections**. Current ToC remains 25 chapters / 747 numbered sections. Audit-only documentation: no mathematical-body, source, registry, canonicalization, permanent-tag, GitHub Actions CI, build, site or publication changes.
