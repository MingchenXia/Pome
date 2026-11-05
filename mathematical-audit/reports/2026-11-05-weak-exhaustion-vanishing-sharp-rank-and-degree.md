# Audit report — sharp rank and bidegree in semipositive vanishing; a corrupted second derivative

**Date:** 2026-11-05. **Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (read freshly). **Review-only branch:** `review/mathematical-audit`. **Actual newly audited current-ToC section:** §10.52, *Semipositive line-bundle vanishing on weak exhaustions*. **Integrated reading edition:** `docs/sections/hodge-theory-curvature-and-compact-vanishing--semipositive-line-bundle-vanishing-on-weak-exhaustions/index.html`, main blob `d3dfb60754a1df99aa6c283d0c54d96fa5a5fa01`, 103 physical HTML lines. **Theorem 10.52.1:** original source `demailly-complex-geometry:8601427A`, permanent tag `A46DE8D5D789`, statement lines 8–12, proof lines 17–90. Equations 10.52.2, 10.52.3 and 10.52.4 are displayed at lines 28–30, 41–43 and 68–70 respectively.

The owner-excluded Demailly *approximation/regularization*, dedicated Bergman, weighted-L²/Ohsawa–Takegoshi approximation, multiscale-atlas and positivity-loss programme was **not** audited or reopened. This note concerns an elementary independent sharpness model for a **vanishing theorem**, not its analytic proof; the printed analytic chain, including Lemma 9.50.3 and the metric/exhaustion inputs, remains **unverified here**.

## POME-WEAK-EXHAUSTION-RANK-DEGREE-SHARP-001

**Severity:** low. **Status:** verified conditional deduction (the only background inputs are standard complex projective-space coordinates and holomorphic forms; no conclusion of the printed theorem is refuted). **Statement:** Both numerical inequalities in Theorem 10.52.1 are **individually sharp** already among compact Kähler manifolds with a smooth semipositive Hermitian line bundle:

1. With exactly `n-s+1` positive curvature eigenvalues, one cannot replace the vanishing range `a+b >= n+s` by `a+b >= n+s-1`.
2. Keeping the vanishing range `a+b >= n+s`, one cannot weaken `at least n-s+1 positive eigenvalues` to `at least n-s positive eigenvalues`.

These examples work **for every** `n>=1` and `1<=s<=n`, including the boundary cases `s=1` and `s=n`.

### An explicit family exhibiting the two sharp thresholds

For every integer `0<=r<=n`, put `q=n-r` and take
\[
 X_r=\mathbb P^r\times E^q,\qquad
 L_r=\operatorname{pr}_1^*\mathcal O_{\mathbb P^r}(r+1),
 \qquad E=\mathbb C/(\mathbb Z+\mathrm i\mathbb Z).
\]
Here `\mathbb P^0` is a point and `E^0` a point. Use the product of a Fubini–Study form and a flat Kähler form, and the Fubini–Study Hermitian metric on `\mathcal O(r+1)`. Its curvature is `(r+1)\omega_{\rm FS}` on `\mathbb P^r` and zero on `E^q`. Therefore it is smooth semipositive with **exactly `r` strictly positive eigenvalues at every point** (rank zero when `r=0`). The manifold is compact Kähler, hence has a smooth PSH exhaustion (a constant exhaustion is proper on a compact manifold).

The canonical bundle of `\mathbb P^r` is `\mathcal O(-r-1)`. This identity can be checked directly on projective coordinate charts using the transition determinant of `d(Z_i/Z_j)`; equivalently, the homogeneous expression
\[
  \sum_{j=0}^{r}(-1)^j Z_j\,dZ_0\wedge\cdots
  \wedge\widehat{dZ_j}\wedge\cdots\wedge dZ_r
\]
induces a nowhere-zero holomorphic `\mathcal O(r+1)`-valued top form. For `r=0` take the constant section `1`. The canonical bundle of the complex torus `E^q` is trivial, with top form `\eta=dz_1\wedge\cdots\wedge dz_q` (use `1` if `q=0`). Hence
\[
 K_{X_r}\otimes L_r\simeq\mathcal O_{X_r}
\]
and there is a nowhere-vanishing holomorphic **`L_r`-valued `(n,0)` form** `\Omega`.

For `q>0`, set `\beta=d\bar z_1\wedge\cdots\wedge d\bar z_q` on `E^q` and pull it back to `X_r`. The `L_r`-valued `(n,q)` form
\[
  g=\Omega\wedge\beta
\]
is smooth and `\bar\partial`-closed. It is **not** `\bar\partial`-exact: if `g=\bar\partial U`, dividing by the nowhere-zero `\Omega` gives `\beta=\bar\partial(\Omega^{-1}U)`. Restrict the resulting scalar `(0,q-1)` form to any holomorphic fiber `\{p\}\times E^q`; then `\beta` would be `\bar\partial`-exact there. Wedging with the holomorphic top form `\eta` and integrating over the compact torus gives zero by Stokes, contradicting
\[
  \int_{E^q}\beta\wedge\eta\ne0
\]
(the integrand is a nonzero constant multiple of the flat volume form). If `q=0`, the nowhere-vanishing holomorphic `L_n`-valued `(n,0)` form `\Omega` already represents a nonzero class, since there are no forms of bidegree `(n,-1)`. Thus, in **every** case,
\[
  \boxed{H_{\bar\partial}^{n,n-r}(X_r,L_r)\ne0.}
\]
This argument uses only projective transition functions, holomorphic coordinate forms, pullbacks and Stokes; it does **not** require a Dolbeault–Künneth theorem, a vanishing theorem or any of the owner-excluded regularization/Bergman/L²/OT programmes.

### Apply the family to the printed theorem's two thresholds

- **Sharp bidegree with the printed curvature rank.** Set `r=n-s+1` (so `q=s-1`). The curvature has the **required** `n-s+1` positive eigenvalues, but
  \[
   H_{\bar\partial}^{n,s-1}(X_r,L_r)\ne0,
   \qquad n+(s-1)=n+s-1.
  \]
  Therefore the printed cutoff `a+b>=n+s` cannot be decreased even by one. At `s=1`, this is `X=\mathbb P^n`, `L=\mathcal O(n+1)`, with a nonzero holomorphic `L`-valued top form.

- **Sharp positivity count at the printed cutoff.** Set `r=n-s` (so `q=s`). The curvature has **one fewer positive eigenvalue** than the printed hypothesis, and
  \[
   H_{\bar\partial}^{n,s}(X_r,L_r)\ne0,
   \qquad n+s=n+s.
  \]
  Thus allowing only `n-s` positive eigenvalues makes the claimed vanishing false right at its threshold. When `s=n`, this is simply the flat complex torus `E^n` with trivial `L`, whose top Dolbeault group is nonzero.

Both implications are **counterexamples to hypothetical strengthened theorems, NOT counterexamples to Theorem 10.52.1**. The printed curvature and degree bounds are mutually consistent and, numerically, optimal. The general proof of the theorem is not thereby verified.

### Affected dependents and proposed action

Record this family as an optional sharpness remark following Theorem 10.52.1, preserving its hypothesis, conclusion, source attribution and permanent tag. It is relevant to any later attempt to weaken the strict eigenvalue count or the high-bidegree threshold in §10.52; **no existing dependent is known to assert such a false strengthening**. No statement, source registry or canonicalization change was made.

## POME-WEAK-EXHAUSTION-RHO-GLYPH-001

**Severity:** low. **Status:** confirmed **reader-body/editorial error**; **not a mathematical counterexample or a demonstrated failure of the vanishing proof**. In the displayed calculation of `\partial\bar\partial\alpha` (integrated theorem proof, physical HTML line **57**) the term `((\rho')^2-\rho ”)` contains a literal right double-quotation mark (U+201D) after `\rho`, where the second derivative `\rho''` is required. This is a **newly inspected §10.52 occurrence**, distinct from the previously logged §11.48 double-prime corruptions. It is not classified as a new project-wide cause or as a proof of additional glyph failures.

The correct identity, obtained by two direct applications of the chain rule and `\partial\omega=\bar\partial\omega=0`, is
\[
 \partial\bar\partial\big(e^{-\rho(\psi)}\omega\big)
 =e^{-\rho(\psi)}
 \Bigl(\big((\rho'(\psi))^2-\rho''(\psi)\big)
       \partial\psi\wedge\bar\partial\psi
       -\rho'(\psi)\partial\bar\partial\psi\Bigr)\wedge\omega.
\]
The printed surrounding estimates, in particular Equation 10.52.4 at lines 68–70, already involve `\rho''` as an ordinary positive second derivative; the character is therefore transcription corruption, not an independent operator. **Proposed correction:** replace only that glyph occurrence with `\rho''` in a separately reviewed production-reading-source patch; preserve labels and the mathematical statement, and inspect rendering at the exact tagged page. No source/HTML/site repair was performed in this audit branch.

## Scope, conditional inputs, and open work

The actual **new** proof audit is restricted to the displayed vanishing hypotheses and proof structure in §10.52 (statement 8–12; metric and curvature algebra 17–46; torsion derivative formula 48–73; completeness/L² closure 75–89). The sharpness proof is fully elementary modulo basic projective coordinate changes and Stokes, which are explicitly outlined. The **general** analytic theorem's Hodge–Bochner identities, global choice of weights, completeness criterion, torsion bounds, and global `\bar\partial` solvability cited from internal §10.33.6, §11.48.13, §6.26.3, §6.27.12 and §9.50.3 remain unverified by this run. These citations are dependencies, **not automatically proof gaps**. The glyph fix is editorial, and the degree/rank sharpness family is a correct independent model; neither certifies the whole section.

Current actual ToC (read from production `docs/index.html`): **25 chapters, 747 numbered sections, zero complete mathematical-section certificates**. Existing error, gap, external, genuine-duplication, verified-repair and **deferred-by-user** records are preserved. In particular, excluded Demailly approximation/regularization and its dedicated Bergman, weighted L², OT, multiscale-atlas and positivity-loss completion remain **deferred-by-user**, not resolved or certified. Only new audit Markdown on `review/mathematical-audit`; no main, source, canonicalization, permanent-tag, build, tests, CI or website publication changes.
