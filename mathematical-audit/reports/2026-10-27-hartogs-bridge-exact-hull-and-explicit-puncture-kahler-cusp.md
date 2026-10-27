# 2026-10-27 — Exact Hartogs-bridge holomorphic hull and an explicit finite-volume complete Kähler cusp

**Reviewed reading-edition main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch before this work:** de4c9e61443ae6d23e794c739688e877a38c653c. **Scope:** new selected proof inspection in §§9.30, 9.31, and 10.82. No entire section, cited analytic solvability result, or entire dependency chain is certified. This audit does **not** address the user-deferred Demailly approximation/regularization or dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas, or positivity-loss proof-completion programmes. Such previous work remains **deferred-by-user**, neither corrected nor certified.

## POME-HARTOGS-BRIDGE-EXACT-HULL-001

**Status:** verified conditional deduction; **severity:** low; **printed Proposition 9.30.1 is not disproved**.

**Exact integrated source:** docs/sections/separation-strict-exhaustions-and-coverings--local-separation-without-global-separation/index.html, main blob c4037b237429e2c1269bd7beebded6644dc206c9, section 9.30 tag 4CC893698BCD, Proposition 9.30.1, source label demailly-complex-geometry:61281B36, permanent tag 774E0C4C33DB, lines 10–62. In particular, the gluing and Hausdorff analysis is at lines 21–43, the global holomorphic-function algebra at 45–53, and the noncompact-hull witness at 55–62.

**Precise claim (additional, not already printed).** In the glued Hausdorff Riemann domain $X$ of Proposition 9.30.1, let $\pi:X\to\Delta^2$ be the local biholomorphism, and let $K$ be the circle in the $H$ chart with $z=3/4$ and $|w|=7/8$. Its full holomorphic hull is exactly
\[
 \widehat K_{\mathcal O(X)}
 = \pi^{-1}\bigl(\{(3/4,w):|w|\le 7/8\}\bigr).
\]
This equality counts **both** points above any $(3/4,w)$ in the negative overlap $U_-$; it is a set equality in $X$, not in the base $\Delta^2$. In particular the hull is noncompact even though its image is contained in a compact closed disk in $\Delta^2$.

**Proof.** Proposition 9.30.1 proves that every $f\in\mathcal O(X)$ is uniquely $F\circ\pi$ for $F\in\mathcal O(\Delta^2)$; its proof of this algebra is directly inspected in the cited lines. If $x$ is in the hull, taking the global function $z-3/4$ (which vanishes on $K$) forces $\pi_1(x)=3/4$. Taking the global function $w$ then gives $|\pi_2(x)|\le 7/8$. Conversely, for $\pi(x)=(3/4,w)$ with $|w|\le 7/8$, the one-variable maximum-modulus principle applied to $F(3/4,\cdot)$ gives
\[
 |f(x)|=|F(3/4,w)|\le\max_{|\zeta|=7/8}|F(3/4,\zeta)|=\sup_K|f|.
\]
Thus $x$ lies in the hull. This also handles the noninjective fibers without any illicit descent of compactness.

**Concrete noncompactness and sharpness.** For integers $j\ge2$ the $B$-chart points $x_j$ with $\pi(x_j)=(3/4,i(1-1/j)/8)$ lie in the displayed hull. Their coordinate images tend to $(3/4,i/8)\notin\pi(X)$ (this point is on the boundary of the open rectangle $E$, outside $H$). A compact hull would have compact, hence closed, image in the Hausdorff bidisc, which is impossible. This strengthens the existing noncompactness witness from membership alone to an exact complete hull computation. Both copies over $U_-$ occur because only $U_+$ is identified in the construction. The original proposition needs no correction.

**Suggested addition / affected dependents:** optional explicit formula after the final paragraph of the proof of Proposition 9.30.1, with a warning that holomorphic convexity cannot be recovered from base compactness when a local biholomorphism is nonproper. Related: global separation versus local separation and Stein criteria in §§9.25–9.32. The one-variable identity and maximum principles are the only standard analytic inputs used here.

## POME-PUNCTURE-KAHLER-FINITE-CUSP-001

**Status:** verified conditional deduction (explicit independent proof of the metric-existence instance); **severity:** low; **the printed Theorem 9.31.1 and Example 9.31.2 are not disproved**.

**Exact integrated source:** docs/sections/separation-strict-exhaustions-and-coverings--complete-kahler-metrics-on-regular-open-sets/index.html, main blob 3faaef942f4822127e09c63a463d654d346696c2, section tag 34A39DF5C65F. Theorem 9.31.1: demailly-complex-geometry:232F4B65, tag 214C6B3DF885, lines 7–22. Example 9.31.2: demailly-complex-geometry:12510407, tag D80B90CDCDA1, lines 25–42.

**Claim.** For every $n\ge1$, $\mathbb C^n\setminus\{0\}$ carries an **explicit** complete Kähler metric whose volume in a sufficiently small punctured ball is finite. The metric can equal the Euclidean Kähler metric outside a fixed small ball. For $n\ge2$ this refines the metric-existence part of Example 9.31.2 and simultaneously supplies the expected counterexample to dropping the **regular-open** hypothesis of Theorem 9.31.1, since $\operatorname{Int}\overline{\mathbb C^n\setminus\{0\}}=\mathbb C^n$. The nonpseudoconvexity for $n\ge2$ is established by the separate Hartogs proof printed at lines 34–40.

**Self-contained construction and exact eigenvalues.** Write $r=|z|>0$, $L=\log(1/r^2)$, and for $0<r<r_0<e^{-2}$ let
\[
 \psi(z)=-\log L=-\log(-\log|z|^2).
\]
Set $t=\log r^2$, so $\psi'(t)=-1/t=1/L>0$ and $\psi''(t)=1/t^2=1/L^2>0$. Consequently
\[
 i\partial\bar\partial\psi
 =\frac1L\,i\partial\bar\partial\log r^2+
   \frac1{L^2}\,i\partial\log r^2\wedge\bar\partial\log r^2 .
\]
Relative to $\omega_{\mathrm{eucl}}=i\sum_j dz_j\wedge d\bar z_j$, its complex Hessian has one radial eigenvalue $1/(r^2L^2)$ and $n-1$ tangential eigenvalues $1/(r^2L)$. In particular it is positive for $z\ne0$; no approximation or $L^2$ existence theorem is being used.

Take a smooth radial cutoff $\chi=1$ on $r\le r_0$, $\chi=0$ on $r\ge2r_0$. The real $(1,1)$-form $i\partial\bar\partial(\chi\psi)$ has a finite lower eigenvalue bound on the compact transition annulus, and is semipositive where $\chi=1$ and zero where $\chi=0$. For sufficiently small fixed $\lambda>0$,
\[
 \omega_\lambda=\omega_{\mathrm{eucl}}+\lambda i\partial\bar\partial(\chi\psi)>0
\]
globally on $\mathbb C^n\setminus\{0\}$. It is closed because it is the Euclidean closed form plus an exact $i\partial\bar\partial$ term. It equals $\omega_{\mathrm{eucl}}$ outside $2r_0$.

**Completeness.** Near $0$ its radial Riemannian metric dominates a positive multiple of $dr^2/(r^2L^2)$, hence the length of any curve tending to $0$ dominates a positive multiple of the total variation of $\log L$. Since $\log L\to\infty$ as $r\to0$, such a curve has infinite length. Curves escaping to infinity also have infinite length since the metric equals the Euclidean metric there. Smooth local equivalence on compact annuli then gives metric completeness.

**Finite local volume.** Near $0$ the determinant of $\omega_\lambda$ relative to the Euclidean form is exactly
\[
 \left(1+\frac{\lambda}{r^2L^2}\right)
 \left(1+\frac{\lambda}{r^2L}\right)^{n-1}
 \sim\lambda^n r^{-2n}L^{-(n+1)} .
\]
After multiplication by polar Euclidean volume $r^{2n-1}dr\,dS$, this has locally finite integral because
\[
 \int_0^{r_0}\frac{dr}{r(\log(1/r^2))^{n+1}}
 =\frac{(\log(1/r_0^2))^{-n}}{2n}<\infty .
\]
The metric thus has a complete, finite-volume cusp at the missing point. No statement of finite **total** volume at Euclidean infinity is intended.

**Dependencies / correction proposal.** The proof of Theorem 9.31.1 uses the internal division Corollary 6.28.14 and the Cartan–Thullen equivalences at lines 14–20; we checked its quantifier and the elementary positive-distance radial-integrability calculation but **did not reopen the separate L²/division proof**. The current Example 9.31.2 uses Lemma 6.28.11 for metric existence; this elementary displayed construction can optionally be added as an alternative proof **of that concrete instance only**, not as a certification of 6.28.11 or its broader programme. No proof-body edit is made here. Dependents include the regular-open qualification of 9.31.1 and the holomorphic-convexity/separation discussion at 9.29–9.32.

## Independent selected crosscheck: symbols, stars, and nonflat connections

**Source:** docs/sections/symbols-exterior-algebra-and-bundle-adjoints/index.html, main blob 95b25dd98d1678d1130be1b6dbd3f18c3c084ce8, section tag A91D152909BF. Subheading 10.82.1 permanent tag 5ADADD15BE60, symbol proof lines 5–21 (shared Proposition 2.17.2); Proposition 10.82.2 source label demailly-complex-geometry:A161E98B, tag 3765CBF9B2B4, lines 23–35.

Checked the covector transformation and principal-symbol composition by the repeated Leibniz rule in lines 11–18, the adjoint sign on 1-forms, the Hodge square $*^2=(-1)^{k(d-k)}$, and the anticommutator $\iota_v(\theta\wedge u)+\theta\wedge\iota_vu=\theta(v)u$ which yields scalar principal symbol $|\xi|^2I$ for $\Delta_D$. In particular, nonflatness does not affect the principal symbol: on the trivial Hermitian line over $\mathbb R^2$, the unitary connection $D=d+i x\,dy$ has $D^2=i\,dx\wedge dy\ne0$ even though $\Delta_D$ still has scalar leading term $-\partial_x^2-\partial_y^2$. The printed qualification requiring flatness only for the **complex/cohomology** interpretation is correct. This is a new selected check, **not a third new finding**, and it does not certify the cited global Hodge comparison.

## Coverage and integrity

Exactly three previously inventory-only ToC rows, §§9.30, 9.31 and 10.82, have been examined at the stated integrated paragraphs; **747 unique current section identifiers are preserved**. No whole section is fully certified. No newly confirmed false theorem. No source manuscript, canonicalization, registry, permanent tag, main branch, website, CI or build is changed. Deferred-by-user exclusions are not treated as repaired, independently verified, or silently reactivated.
