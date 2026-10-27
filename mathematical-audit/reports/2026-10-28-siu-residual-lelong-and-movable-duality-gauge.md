# Siu residual point Lelong numbers and a gauge for dual positive cones

Date: 2026-10-28. **Fresh reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Initial audit branch HEAD:** aa3e29c54e6dc51f099751ec4aecff64370d68ff.
**Scope:** selected current-reading proof passages in three previously inventory-only, nonexcluded sections, not certification of any entire section. The dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remains **deferred-by-user**, not reexamined or certified. Previously resolved, unresolved, and user-deferred entries are preserved.

## Immutable integrated reading anchors

1. **§6.40**, Siu decomposition in arbitrary bidimension: docs/sections/lelong-densities-generalized-masses-and-multiplicity--siu-decomposition-in-arbitrary-bidimension/index.html; main blob **76094d2efe4c1a0c306f19d592c1e11029a6a5d9**. Theorem 6.40.1, source **demailly-complex-geometry:15D6D8A1**, permanent tag **6A51F1CD4D5B**, lines **7–17**. Proposition 6.40.2, source **demailly-complex-geometry:BBDF9A97**, tag **5C624FF7D159**, lines **19–35**. Theorem 6.40.3, source **demailly-complex-geometry:FC32B122**, tag **9F8D9022476A**, lines **37–53**. Proposition 6.40.4, source **demailly-complex-geometry:5CB7F8B8**, tag **4357853E1FD2**, lines **55–99**.
2. **§6.49**, polynomial iterates and residual mass: docs/sections/polynomial-iterates-and-residual-mass/index.html; main blob **40c8aa7367e43ba39fca9bc1288b62aa3e9c78cc**. Proposition 6.49.1, source **isolated-plurisubharmonic-singularities:801F1DD0**, tag **CE621FA6CE58**, lines **10–50**. Corollary 6.49.2, source **isolated-plurisubharmonic-singularities:2E583758**, tag **A9F7692E230F**, lines **52–87**. Definition 6.49.3, source **isolated-plurisubharmonic-singularities:14E30FEA**, tag **54F98147B130**, lines **89–99**. Proposition 6.49.4, source **isolated-plurisubharmonic-singularities:737A0A7C**, tag **DDF1EA12A4BF**, lines **102–135**.
3. **§10.100**, dual positive cones: docs/sections/dual-positive-cones/index.html; main blob **9b0ff0ccb06e68d1cbc466d8b79df3ceb5f022f1**. Theorem 10.100.1, source **transcendental-positive-cones:5F09EB8A**, permanent tag **DF6FA97EF816**, lines **7–42**. Upstream approximation Theorem 13.32.3, tag **AD36F0CA2A0B**, is mentioned as a **conditional existing input only**; its dedicated regularization proof is not reopened.

## POME-SIU-RESIDUAL-POINT-LELONG-001

**Severity:** low. **Status:** verified conditional deduction. **Not** a false printed theorem or new gap. **Hypotheses:** a neighborhood of the origin in $\mathbb C^2$; $dd^c=i\partial\bar\partial/(2\pi)$; $u(z)=\log(|z_1|^2+|z_2|^2)$ and $T=dd^c u$. **Affected dependents:** §§6.40.2–4 and any canonicalization conflating a residual Siu current with zero pointwise Lelong numbers, or classical products with non-pluripolar products.

**Result:** the bidimension-one Siu decomposition of $T$ is purely residual, $R=T$, although $\nu(R,0)=1$. The current's coefficient measures have no atom at the origin, whereas its *classical* isolated-pole square is $\delta_0$ and its *non-pluripolar* square vanishes.

**Proof.** Outside the origin, $u$ is smooth, so $\nu(T,z)=0$; at zero the squared logarithmic normalization gives $\nu(T,0)=1$. Thus every nonempty positive Lelong level $E_c(T)$ equals the **point** $\{0\}$ for $0<c\leq1$; it contains no irreducible curve. By Theorem 6.40.3 there can be no one-dimensional Siu component, hence $R=T$. The local coefficients of $T$ grow as $O(|z|^{-2})$, integrably in real dimension four, and so $\mathbf 1_{\{0\}}T=0$: absence of a coefficient-measure atom does not imply zero density/Lelong number.

For an independently checkable normalization put $u_\varepsilon=\log(|z|^2+\varepsilon)$. The complex Hessian has tangential eigenvalue $(|z|^2+\varepsilon)^{-1}$ and radial eigenvalue $\varepsilon(|z|^2+\varepsilon)^{-2}$, hence determinant $\varepsilon(|z|^2+\varepsilon)^{-3}$. With the stated $dd^c$ convention this gives
\[
(dd^c u_\varepsilon)^2=
\frac{2\varepsilon}{\pi^2(|z|^2+\varepsilon)^3}\,dV_{\mathbb R^4}.
\]
Its total mass, computed using the area $2\pi^2$ of the unit three-sphere, is
\[
4\varepsilon\int_0^\infty\frac{r^3\,dr}{(r^2+\varepsilon)^3}
=4\varepsilon\frac1{4\varepsilon}=1.
\]
For every fixed radius $a>0$ the mass outside $B_a$ tends to zero as $\varepsilon\downarrow0$, so the top forms converge to $\delta_0$; this agrees with the classical decreasing isolated-pole product invoked in Proposition 6.40.4 for $q=2$, $F_1=z_1$, $F_2=z_2$, $\gamma_1=\gamma_2=1$. On $\mathbb C^2\setminus\{0\}$ the Hessian of $u$ has rank one. Every non-pluripolar truncation discards the pole and has zero square on its retained open set. Therefore $\langle T^2\rangle=0$. For $q=1$ Proposition 6.40.4 instead has no codimension-one component, consistent with the purely residual $T$.

**Disposition:** optional example following Theorem 6.40.3 / Proposition 6.40.4, retaining both products as distinct mathematical entries. This is a static local pole model, not a rediscovery of the printed iterated-polynomial construction in §6.49. No body or registry patch was applied.

## POME-MOVABLE-DUAL-THRESHOLD-GAUGE-001

**Severity:** low. **Status:** verified conditional deduction **assuming Theorem 10.100.1**; neither a false theorem nor certification of its upstream analytic approximation. **Hypotheses:** connected compact Kähler $X$, dimension $n\geq1$, fixed Kähler class $\omega$, arbitrary $\xi\in H^{1,1}(X,\mathbb R)$, and pseudoeffective cone $\mathcal E$. **Affected dependents:** numerical detection of pseudoeffectivity using single-power witnesses and positive-cone duality in §10.100.

Let
\[
\tau_\omega(\xi)=\inf\{t\geq0:\xi+t\omega\in\mathcal E\}.
\]
The closed-cone duality $\mathcal E=C^*$ in Theorem 10.100.1 immediately gives the exact gauge
\[
\boxed{\displaystyle
\tau_\omega(\xi)=
\max\!\left(0,\sup_{\substack{\mu:Y\to X\ \mathrm{modification}\\
\kappa\ \mathrm{K\ddot ahler\ on}\ Y}}
-\frac{\xi\cdot\mu_*(\kappa^{n-1})}
{\omega\cdot\mu_*(\kappa^{n-1})}\right).}
\]
Every denominator is strictly positive: $\mu^*\omega$ is semipositive and strictly positive on the nonempty isomorphism locus, while $\kappa^{n-1}$ is strictly positive. Being in $C^*$ is equivalent to having nonnegative pairing against **every generating single power**, since finite nonnegative combinations and their limits impose no additional inequalities. For each generator, $(\xi+t\omega)\cdot g\geq0$ is equivalent to $t\geq-\xi\cdot g/(\omega\cdot g)$; intersect with $t\geq0$. Finiteness follows because sufficiently large $t$ makes $\xi+t\omega$ Kähler. No sequential-compactness claim or limit interchange is needed.

The sign argument in §10.100.1, lines 23–37, independently gives for $\xi\notin\mathcal E$, $t_0=\tau_\omega(\xi)>0$ and $\gamma_\varepsilon=P(\xi+(t_0+\varepsilon)\omega)$:
\[
\frac{\xi\cdot\gamma_\varepsilon}{\omega\cdot\gamma_\varepsilon}
\leq-t_0+(n-1)\varepsilon.
\]
For $n>1$ choosing $0<\varepsilon\leq t_0/(4(n-1))$ gives a ratio at most $-3t_0/4$, and an actual sufficiently late single-power approximant has ratio below $-t_0/2$. **Only the approximation step** uses the existing Theorem 13.32.3, taken as a black box and not audited here. For $n=1$ the empty product gives the exact ratio $-t_0$.

**Independent example:** for $X=\mathbb P^1\times\mathbb P^1$, let $H_1,H_2$ be the fiber classes with $H_1^2=H_2^2=0$, $H_1H_2=1$, and take $\omega=H_1+H_2$, $\xi=-H_1+H_2$. The pseudoeffective cone is $\{aH_1+bH_2:a,b\geq0\}$, so $\tau_\omega(\xi)=1$. With $\mu=\mathrm{id}$ and $\kappa=aH_1+bH_2$ for $a,b>0$,
\[
-\frac{\xi\cdot\kappa}{\omega\cdot\kappa}
=\frac{b-a}{a+b}\longrightarrow1\qquad(b/a\to\infty).
\]
The supremum is sharp but **not attained** by a strictly Kähler $\kappa$ on this identity model. This is an elementary independent test of the gauge and of the supremum quantifier.

**Disposition:** optional exact threshold corollary following Theorem 10.100.1; preserve its source label and attribution. The corollary is proved *conditional on* the printed cone theorem, not an independent proof of it.

## Other directly checked passages, no new finding IDs

- **§6.40.1–4:** the level-set dimension reduction, countable generic-level complement, normal-support dimension principle, uniqueness by coefficient restriction, and the argument using increasing finite sums bounded by $T$ were read. The latter does not interchange an infinite-series Lelong limit. Analytic level-set theorem 6.39.11 and normal support theorem 5.56.3 remain noncertified upstream. The two log-sum potentials in 6.40.4 differ by an amount in $[0,\log N]$; the radial $q=1,2$ checks agree with their different products.
- **§6.49.1–4:** $\det DF_\varepsilon=-zw$, and for $\varepsilon\ne0$ the branch images are exactly $\{\alpha=0\}$ and $\{\beta^2=2\varepsilon^2\alpha\}$ (for $\varepsilon=0$, $\{\alpha\beta=0\}$). Counting the two nested square roots verifies the displayed local degree $(1+\mathbf1_{\{w=0\}})(1+\mathbf1_{\{z=0\}})$ and $e(F_\varepsilon,0)=4$. For iterates, degree $4^j$ and scaling $2^{-j}$ are consistent with the printed $(dd^cp_j)^2=\delta_0$ and $\nu(p_j,0)=2^{-j}$. The global weighted projection formula and classical decreasing continuity remain separate conditional inputs; this is not a new version of the old mass-arithmetic audit.
- **§10.100.1:** checked the finite-dimensional bipolar argument, positivity of the test denominator, $n=1$ empty-power convention and the **direction** of the volume-derivative estimate. The cone theorem as a whole remains dependent on its already stated analytic ingredients, including the user-excluded approximation input, which was not reopened.

## Coverage and ledger disposition

Exactly **three** prior inventory-only ToC rows (**§§6.40, 6.49, 10.100**) are now marked **selected bounded proof inspection**. All **747** unique numbered ToC IDs are retained; **zero** complete sections or chapters certified. Two low verified conditional deductions; **no newly confirmed false printed theorem** and no completed source-text repair. Existing unresolved, resolved, external and deferred statuses are unchanged. No build, test suite, formal verification, GitHub Actions CI, main/source/body/tag/registry/canonicalization or website publication.
