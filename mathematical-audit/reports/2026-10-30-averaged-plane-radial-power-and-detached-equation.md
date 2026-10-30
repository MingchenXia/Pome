# Averaged complex-plane currents: exact radial power thresholds and a detached equation permalink

**Date:** 30 October 2026 (Asia/Shanghai). **Production main examined:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Scope:** selected integrated §§5.57.4, 5.57.7, 5.57.11 and Equation 5.57.10, and its standalone tagged page. All other proof chains remain conditional. This is classical complex-plane/current calculus, **not** the expressly excluded Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale atlas or positivity-loss programme. Those earlier findings remain **deferred-by-user**, neither resolved nor certified.

## Pinned source and permanent-tag anchors

- Continuous reading edition: `docs/sections/real-currents-submersions-and-homotopies--averaging-complex-planes/index.html`, main blob `2245f2fee90247cc55a3b57b9b41e0af135abcd1`. Proposition **5.57.4**, source `demailly-complex-geometry:21A674FD`, permanent `522ECB915F74`, lines **50–84**; mass Equation **5.57.5**, source `demailly-complex-geometry:2619A79B`, permanent `9DCAA92A7418`, lines **55–58**. Lemma **5.57.7**, source `demailly-complex-geometry:BC8F6A45`, permanent `74F34FAD7C93`, lines **89–135**, and recursion Equation **5.57.8**, permanent `4EAEBCA3446D`, lines **90–94**. Theorem **5.57.11**, source `demailly-complex-geometry:5B5618BA`, permanent `AB7EED2588E5`, lines **139–152**, with Equation **5.57.12**, source `demailly-complex-geometry:ED2C06C1`, permanent `1642738DA5E8`, lines **140–145**.
- Broken integration: Equation **5.57.10**, source `demailly-complex-geometry:26C290A4`, permanent `128DDD633F87`. Its two-row display is in the continuous §5.57 page at **lines 109–116**; the detached partial-entry copy is at **line 155**, same blob. Standalone permalink `docs/tag/128DDD633F87/index.html`, main blob `5f4e5d378d3a85e96ed2480231274f0db774a7ec`, contains the partial formula following `<main id="content">`. Exact source identity—not a similarly numbered equation elsewhere—is used throughout.
- Baseline normalization: \(\mathrm{dd}^{\mathrm c}=(i/2\pi)\partial\bar\partial\), \(\beta=\mathrm{dd}^{\mathrm c}|z|^2\), \(\int_{B(0,r)}\beta^n=r^{2n}\), as fixed in the printed §5.57 passage.

## Finding POME-PLANE-RADIAL-POWER-THRESHOLD-001: exact radial coefficient mass and sharp weighted integrability

**Severity:** low. **Status:** **verified conditional deduction**, **not** a false printed theorem or a completed independent proof of its internal prerequisites. The old `POME-SPHERE-LOG-HARMONIC-001` computes the *sphere's random linear-functional logarithm* and its constant \(-H_{n-1}\). The present result instead computes the **radial trace density of averaged Grassmannian currents** and its all-power/logarithmic thresholds. It is mathematically distinct, and the old finding remains credited rather than relogged.

For \(n\ge1\), \(1\le q\le n\), let \(\nu_q\) be the invariant probability on the complex Grassmannian \(G(q,n)\), and
\[
 A_q=\int_{G(q,n)}[S]\,d\nu_q(S),\qquad \mu_q=A_q\wedge\beta^q.
\]
The printed Proposition 5.57.4 and Theorem 5.57.11 give \(A_q=(\mathrm{dd}^{\mathrm c}\log|z|^2)^{n-q}\) as the **classical recursive product**, and \(\mu_q(B(0,r))=r^{2q}\). One obtains the sharper **measure identity on \(\mathbb C^n\setminus\{0\}\)**:
\[
 \boxed{\quad A_q\wedge\beta^q
     =\frac{q}{n}|z|^{-2(n-q)}\beta^n.\quad}
\]
For \(q\ge1\), the printed ball formula also implies \(\mu_q(\{0\})=0\), so this density determines the whole measure. Its radial pushforward on \((0,\infty)\) is exactly
\[
 \boxed{\quad (|z|)_*\mu_q=2q\,r^{2q-1}\,dr.\quad}
\]
Consequently, for \(R>0\) and real \(\gamma\),
\[
 \int_{|z|<R}|z|^{-\gamma}\,A_q\wedge\beta^q
 =\begin{cases}
 \dfrac{2q}{2q-\gamma}R^{2q-\gamma},&\gamma<2q,\\[4pt]
 +\infty,&\gamma\ge 2q.
 \end{cases}
\]
The critical power exponent is **exactly \(2q\), independent of ambient \(n\)**. At this endpoint, for \(0<R\le1\) and real \(p\),
\[
 \int_{|z|<R}\frac{|z|^{-2q}}{[\log(e/|z|)]^p}\,
 A_q\wedge\beta^q
 =\begin{cases}
 \dfrac{2q}{p-1}[\log(e/R)]^{1-p},&p>1,\\[4pt]
 +\infty,&p\le1.
 \end{cases}
\]
The endpoint \(q=n\) gives \(A_n=1\) and the ordinary Euclidean \(\beta^n\) mass. The excluded \(q=0\) would instead yield \(\mu_0=\delta_0\), not an absolutely continuous radial density. These endpoints cannot be conflated.

**Independent proof of the additional formulas.** On the punctured space, at any \(z\ne0\), the Hermitian matrix of \(\mathrm{dd}^{\mathrm c}\log|z|^2\) relative to \(\beta\) has eigenvalues \(0,|z|^{-2},\ldots,|z|^{-2}\), with \(n-1\) nonzero eigenvalues. The elementary wedge/symmetric-polynomial identity therefore yields
\[
 \frac{(\mathrm{dd}^{\mathrm c}\log|z|^2)^{n-q}\wedge\beta^q}{\beta^n}
 =\frac{\binom{n-1}{n-q}}{\binom n{n-q}}\,|z|^{-2(n-q)}
 =\frac qn|z|^{-2(n-q)}.
\]
The printed mass identity \(\mu_q(B_r)=r^{2q}\) makes \(\mu_q(\{0\})=0\) by continuity from above as \(r\downarrow0\), since \(\mu_q\) is locally finite. Differentiating that distribution function—or using \(\int_{B_r}\beta^n=r^{2n}\) with the density—gives radial shell mass \(2q r^{2q-1}dr\). Elementary one-variable integration proves all the displayed moment formulas. At \(\gamma=2q\), substitute \(t=\log(e/r)\) into \(2q\int_0^R dr/[r(\log(e/r))^p]\); the threshold is \(p>1\) with the stated exact value. These are ordinary positive-measure integrations; no interchange of unrelated singular limits and no regularization theorem is used.

**Disposition and dependents.** The printed statements are consistent; the result is an optional self-contained quantitative corollary following Proposition 5.57.4 or Theorem 5.57.11, not a proposed correction of a false assertion. It gives a sharp power-weight upgrade of the printed \(\log|z|^2\) coefficient-integrability argument, relevant to §5.57.7's Fubini/current recursion, §5.57.11's isolated top-product mass and the classical-product comparison at §7.31.2. The original internal Poincaré–Lelong, unitary averaging and current-calculus premises have **not** all been transitively certified.

## Finding POME-PLANE-ALIGN-DETACHED-001: the tagged Equation 5.57.10 is split and its permalink is malformed

**Severity:** medium (reader-visible mathematical content and stable cross-reference). **Status:** **confirmed integration/canonicalization error**, **not** a false mathematical inequality or theorem. This is a new tagged-instance defect. A previously logged similar nesting bug in §12.4.3 is a separate prior finding and is **not** being re-registered.

The continuous section's proof at lines 109–116 contains the correct two-row joint estimate beginning with a double integral of \(|\log|\ell_\xi(z)|^2|\) and ending with the integrable radial bound. However, its first displayed copy is wrapped in `<div class="equation numbered-equation">` with the **literal equation label `277`**, without the canonical permanent-tag wrapper, despite an internal `\tag{5.57.10}`. At line 155 the same source label `26C290A4` becomes a detached equation entry containing **only the second/right-hand inequality row**. That second fragment is wrapped as `\[\begin{aligned}\begin{align} ... \tag{5.57.10} \end{align}\end{aligned}\]`: incompatible nested display alignment. The independent tagged page at `docs/tag/128DDD633F87/index.html` contains only this malformed, missing-left-hand-side fragment. The proof's link to Equation 5.57.10 consequently points to an incomplete (and structurally invalid) formula even though the surrounding proof text contains the intended correct full estimate.

**Precise proposed reviewable repair (not applied to production):** retain both full rows as **one** tagged \(\mathrm{5.57.10}\) display in the continuous reading edition; attach the existing source label `demailly-complex-geometry:26C290A4`, original logical label, and permanent tag `128DDD633F87` to the whole estimate. Generate the standalone equation permalink from that complete two-row expression, not the detached RHS, and eliminate the stray `277` label/second partial reading step. Avoid changing upstream source labels, provenance, unrelated canonical entries or mathematical content. Re-run rendering/numbering/link checks in a separately authorized production PR; they were **not** run in this audit. Dependents: the proof of Lemma 5.57.7 at lines 109–135, the Equation 5.57.10 citation at lines 115–116, its permalinks/search results, and downstream Theorem 5.57.11's recursive current identity. No theorem is thereby disproved.

## Coverage and checks actually performed

Selected new check of §5.57.4's Grassmannian mass and coefficient-integrability proof, §5.57.7's Fubini bound and displayed equation, §5.57.11's classical recursive statement, plus the **actual** isolated Equation 5.57.10 tag page. Prior selected checks of §5.57.1 and the spherical \(-H_{n-1}\) moment remain historical and are **not** claimed as new. The new density and sharp moments follow from direct linear-algebra and one-dimensional integral calculations, conditional on the current's printed plane-average identities. No entire section, chapter, or upstream proof chain certified. Current inventory: **25 chapters / 747 numbered ToC sections / 0 entirely certified mathematical sections**. Previous confirmed errors, proof gaps, external dependencies and **deferred-by-user** exclusions are unchanged.

Only English audit Markdown is proposed for the review branch. No production/main/source/body/registry/canonicalization/permanent-tag/site modifications; no builds, MathJax browser rendering, CI, publication, or formal verification claimed.
