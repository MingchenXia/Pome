# 2026-10-27 — A noncompact-base obstruction to a uniform Finsler polar margin; normal-current support

**Reviewed repository:** MingchenXia/Pome. **Current \`main\`:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Review branch before this run:** \`bde22f904afce4cde92892d88ffb6a494d36d691\`. All anchors below are to the actual *integrated reading-edition HTML on this main commit*; physical line numbers are one-based. This is a selected proof audit, not certification of any complete section or its transitive dependencies.

**Scope:** This run did **not** inspect or extend Demailly psh approximation/regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale atlases, or positivity-loss proof completion. Their prior ledger entries remain *deferred-by-user*. In particular, the later smoothing step cited in §11.12.6 was not reopened.

## POME-FINSLER-POLAR-GLOBAL-MARGIN-001 — medium; confirmed error **under the unqualified printed standalone hypotheses**

**Statement and exact source.** \`docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--polar-norms-of-semipositive-finsler-metrics/index.html\`, blob \`9d8c639c4460719360048213e58aa08138dd1a71\`; §11.12 heading (tag \`C40892E1279D\`) and local setup lines 5–16; **Lemma 11.12.3**, source article \`non-kahler-pluripotential-theory-86EFA793\`, permanent tag \`BD7ECB0F942E\`, line 102–106, proof lines 111–141 (especially line 112, which calls the unit sphere bundle *compact*, and line 128, which uses a uniform lower bound). Corollary 11.12.6, source permanent tag \`3DE300A9B2AD\`, lines 146–153, is a downstream use.

The subsection only says that \(E\to X\) is a holomorphic bundle of positive rank; it does not explicitly require \(X\) compact. Lemma 11.12.3 then asserts a **single constant** \(c>0\) valid over every \(x\in X\) for any smooth positive degree-two homogeneous \(G\), such that
\[
Q(x,\xi)-c|\xi|_{k^*}^2
\quad\text{is convex on }E_x^*.
\]
This global conclusion is false for arbitrary noncompact \(X\). The *compact-base reading* of the lemma is correct: the issue is a missing/ambiguous global quantifier, **not** a counterexample on a compact base. If the intended source has a chapter-wide standing compactness convention, make it explicit in this standalone reading section instead of marking the intended compact theorem false.

**Complete counterexample under the displayed hypotheses.** Take \(X=\mathbf C\), \(E=X\times\mathbf C\), \(k(z,v)=|v|^2\), and
\[
G(z,v)=e^{\operatorname{Re}z}|v|^2.
\]
It is smooth, strictly positive off the zero section, homogeneous of degree two, and continuously zero at the zero section. Its vertical complex Hessian is \(e^{\operatorname{Re}z}>0\). Moreover, the Kobayashi curvature convention of lines 19–25 gives \(\mathcal K_G=0\), since \(\operatorname{Re}z\) is pluriharmonic. Thus the counterexample even satisfies the additional semipositive-curvature hypothesis of the preceding Proposition 11.12.2. Polarization is explicit:
\[
Q(z,\xi)=\max_{v\ne0}\frac{|\xi v|^2}{e^{\operatorname{Re}z}|v|^2}
=e^{-\operatorname{Re}z}|\xi|^2.
\]
For any proposed \(c>0\), choose real \(z\) sufficiently large that \(e^{-\operatorname{Re}z}<c\). Then \(Q(z,\xi)-c|\xi|^2\) is a *strictly negative* quadratic form in the real fiber variable, hence not convex. No uniform \(c>0\) exists.

**Verified precise repair, including the noncompact case.** State: *For each relatively compact open \(U\Subset X\), there is \(c_U>0\) such that \(Q(x,\cdot)-c_U|\cdot|_{k^*}^2\) is convex for every \(x\in U\). If \(X\) is compact, one may choose a single \(c>0\) on all of \(X\).* Here is the complete fiberwise proof, independent of the later smoothing programme.

On the compact unit sphere bundle above \(\overline U\), positivity of \(G\) supplies \(G(x,v)\ge a_U|v|_k^2\), while its real vertical Hessian has a uniform upper bound \(D_v^2G\le 2L_U k\), for finite positive \(L_U\). Degree-two homogeneity propagates these bounds to all nonzero vectors; the extension across \(v=0\) is \(C^1\) with zero differential. Integrating the Hessian bound, splitting any segment through zero, yields
\[
G(x,v+w)\le G(x,v)+d_vG(x,v)[w]+L_U|w|_k^2 .
\]
Complex homogeneity along each line, including optimization over its complex scalar, yields the exact identity
\[
Q(x,\xi)=\max_{v\in E_x}\bigl(2\operatorname{Re}\xi(v)-G(x,v)\bigr).
\]
Coercivity gives a maximizer \(v_0\) at \(\xi_0\), and differentiability gives \(d_vG(x,v_0)=2\operatorname{Re}\xi_0\) (also for \(\xi_0=v_0=0\)). For any \(\eta\in E_x^*\), test the objective at \(v_0+w\) and maximize in \(w\):
\[
Q(x,\xi_0+\eta)\ge Q(x,\xi_0)+2\operatorname{Re}\eta(v_0)
+\sup_w\bigl(2\operatorname{Re}\eta(w)-L_U|w|_k^2\bigr)
=Q(x,\xi_0)+2\operatorname{Re}\eta(v_0)+L_U^{-1}|\eta|_{k^*}^2.
\]
After subtracting \(L_U^{-1}|\xi_0+\eta|^2\), this produces an affine global supporting function to \(Q-L_U^{-1}|\xi|^2\) at every \(\xi_0\), hence convexity. Take \(c_U=L_U^{-1}\). For compact \(X\) the same sphere-bundle argument works with \(U=X\), as intended by printed lines 112 and 128.

**Impact/disposition.** The printed lemma needs explicit *compact base* or the corrected *locally uniform* version. Corollary 11.12.6 uses only **local** strong convexity of the polar squared norm on the total bundle, so this repair supplies its needed convexity input without a global \(c\) on a noncompact base. It does **not** certify the subsequent smoothing theorem, or the hypotheses of Corollary 11.12.7. Preserve the original stable tags, source provenance and attribution; propose a separate body patch/PR, with **no mathematical source edit in this audit branch**.

## Independent selected checks (no new confirmed defects)

1. **Tautological Levi/curvature bridge (§11.11).** \`docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--strict-positivity-from-the-tautological-metric/index.html\`, blob \`6f9d5aa919f3b4de1626f1b32cee6064393fff7c\`. Lemma 11.11.1, permanent tag \`40D29F4EF95B\`, lines 20–39, has the correct Schur-square formula \(H(\mathcal L\varphi(u)+|t/\lambda+\partial\varphi(u)|^2)\) and strictness equivalence; Proposition 11.11.2, tag \`68260DAF47D2\`, lines 47–60, correctly extracts a positive metric from an ample tautological dual under the stated geometric setup. Its compact-base bound in line 59 is locally available even without compactness, but this observation does not change the §11.12.3 global failure.

2. **Stokes for \(C^1\) submanifolds (§5.55).** \`docs/sections/real-currents-submersions-and-homotopies--integration-over-real-submanifolds/index.html\`, blob \`09cf11ebb628e7a198bbe84befd8d5c68ead5854\`; Proposition 5.55.1, source \`demailly-complex-geometry-25F759A0\`, permanent tag \`E09F702EB680\`, lines 8–41. The convention \(dT(\alpha)=(-1)^{\deg T+1}T(d\alpha)\), together with \(\deg[Z]=m-p\) and outward-normal-first boundary orientation, does indeed give
\[
d[Z]=(-1)^{m-p+1}[\partial Z].
\]
The proof does not illegally differentiate \(F^*\alpha\) for a merely \(C^1\) parameterization: it passes through smooth \(C^1\)-convergent approximating charts on fixed compact parameter regions, then passes to the limit in both test integrals. This is a check of the displayed argument, not a claim to certify all current theory.

3. **Normal currents on \(C^1\) supports (§5.56).** \`docs/sections/real-currents-submersions-and-homotopies--normal-currents-supported-on-a-differentiable-submanifold/index.html\`, blob \`f89355e610fd1711a2397855116df4d1325d58df\`; Lemma 5.56.1, tag \`A6C399681838\`, lines 23–71, and Theorem 5.56.3, source \`demailly-complex-geometry-F657BA8F\`, tag \`D47CED9844B5\`, lines 75–109; examples lines 113–128. The sign conversion \(d(F_*T)=(-1)^{a-b}F_*(dT)\) is consistent with the dimension-\(p\) boundary operator. The normality assumption is used twice, not just for convenience: both the current and its boundary must be order-zero measures to justify \(hT=0\), \(h\partial T=0\) for \(C^1\) defining functions. The conormal annihilation then eliminates every normal-index coefficient after a \(C^1\) graph flattening. The printed derivative-of-Dirac counterexamples correctly show why normality cannot simply be removed. No new defect established.

## Coverage, dependencies, changes

The previously inventory-only **§§5.55–5.56 and 11.11–11.12** receive *selected theorem/proof-level* coverage as delimited above, **four** ToC rows upgraded; no full-section certifications. §11.3 was used only for chapter context, and its row remains inventory-only. No claim is made about the full Finsler curvature/global smoothing theories or their external inputs. The candidate/confirmed global-quantifier issue is distinguished from a failure of the compact-base theorem. Existing deferred-by-user and unresolved entries are preserved. No tests, build, CI, website publication, formal verification, main/source/registry/canonicalization/permanent-tag edits, PR merge or PR creation.
