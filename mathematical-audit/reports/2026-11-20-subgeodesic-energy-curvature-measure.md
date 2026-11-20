# 2026-11-20 — Whole-section audit of §17.8: curvature of the energy of bounded subgeodesics

**Finding:** POME-GEO-SUBGEODESIC-ENERGY-CURVATURE-001
**Severity/status:** low / **verified conditional deduction** from the explicitly identified printed integration-by-parts and non-pluripolar fiber identities. This is neither a counterexample to the printed theorem nor certification of the complete upstream proof graph.
**Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Integrated reading-edition file:** `docs/sections/relative-energy-and-perron-segments--energy-along-weak-geodesics/index.html` (blob `8d9b7af925289346c96df751c67049e90c9dfe1d`); **all mathematical lines 7–112** directly examined.
**Stable source/permanent labels:** section original `foundations-of-pluripotential-theory:DE08DDE4`, reader section tag `0753F06C3AFA`; Lemma 17.8.1 original `9DEC569D`, permanent `950F051CF55A`, lines 11–38; Lemma 17.8.2 original `B2CECD86`, permanent `3D0F1309E327`, lines 43–54; Theorem 17.8.3 original `907171A2`, permanent `678A18D6D406`, lines 59–112; equation (17.8.4) original `DD6D5F8C`, permanent `2B3BEF6C25C1`, lines 88–90.

## Statement of the audit-only deduction

Let $X$ be a compact Kähler $n$-fold, $\theta$ a smooth closed real $(1,1)$-form, $\phi\in\operatorname{PSH}(X,\theta)$ a reference model potential with finite non-pluripolar mass
\[
m=\int_X\langle(\theta+dd^c\phi)^n\rangle.
\]
Let $A=\{e^{-1}<|z|<1\}$ and let $U$ be $p_1^*\theta$-plurisubharmonic on $X\times A$, with
\[
p_1^*\phi-C\leq U\leq p_1^*\phi+C\quad\text{on }X\times A
\tag{A}
\]
in the extended-valued sense for some finite constant $C$. Write $U_z(x)=U(x,z)$ and
\[
L=p_1^*\theta+dd^c U\geq0,\qquad
\mu_U=\langle L^{n+1}\rangle.
\]
The slice energies are finite, and **as currents on $A$** one has the exact positive curvature identity
\[
\boxed{
dd^c_z\big(E_\theta^\phi(U_z)\big)
=\frac1{n+1}(p_2)_*\mu_U .
}
\tag{1}
\]
The top non-pluripolar measure $\mu_U$ is locally finite by the compact-extension argument below. In particular the energy on the annulus has a subharmonic representative; its harmonicity is equivalent to $\mu_U=0$ on $X\times A$ (positivity of $\mu_U$ prevents cancellation under $p_2$).

If moreover $U(x,z)=V_{-\log|z|}(x)$ is rotation invariant, put
$f(t)=E_\theta^\phi(V_t)$ for $0<t<1$. Each $t\mapsto V_t(x)-\phi(x)$ is convex on the common finite locus and bounded by $C$; the uniform interior chord-slope bound together with Proposition 17.3.9 makes $f$ continuous and locally Lipschitz. For the map $\tau(x,z)=-\log|z|$, the distributional second derivative is the **positive Radon measure**
\[
\boxed{
f''=\frac{2}{n+1}\,\tau_*\mu_U
}
\quad\text{on }(0,1).
\tag{2}
\]
Here the pushforward integrates over all $x\in X$ and all angular variables; no area-form normalization is left implicit. Consequently $f$ is convex, and it is affine on an interval $I$ **if and only if** $\mu_U$ vanishes on $X\times\tau^{-1}(I)$. It is strictly convex on $(0,1)$ if the measure charges every nonempty open parameter band. These are statements about the **top non-pluripolar measure**, not about local maximality without extra hypotheses.

## Proof, including the normalization

Fix an arbitrary relatively compact concentric annulus $A_0\Subset A$ and a larger annulus $A_0\Subset A_1\Subset A$. The proof of Theorem 17.8.3, Step 1 (integrated lines 68–78), requires only the uniform comparison (A), not the Perron maximality of $U$: choose the smooth cutoff $q$ on $\mathbb P^1$ equal to $-C-2$ on $A_0$ and $C+2$ near $\partial A_1$, and choose $B$ so that $B\omega_{\mathrm{FS}}+dd^cq\geq0$. Put
\[
Y=X\times\mathbb P^1,\quad \Theta=p_1^*\theta+Bp_2^*\omega_{\mathrm{FS}},
\quad\Phi=p_1^*\phi.
\]
Set $W=\max\{U,\Phi+q\}$ on $X\times A_1$ and $W=\Phi+q$ elsewhere. The inequalities (A) ensure the formulas agree on a collar and give $W=U$ on $X\times A_0$; $W$ is globally $\Theta$-psh, with $W-\Phi$ bounded. Thus every current below has globally defined locally finite non-pluripolar mixed products on compact $Y$. In particular this verifies local finiteness of $\mu_U$ on $X\times A_0$, hence on $X\times A$.

Put $T=\Theta+dd^cW$, $R=\Theta+dd^c\Phi$ and
\[
H=\frac1{n+1}(p_2)_*
  \bigg[(W-\Phi)\sum_{j=0}^n\langle T^j\wedge R^{n-j}\rangle\bigg].
\]
Printed equation (17.8.4), obtained by the bounded-difference integration-by-parts Theorem 17.2.5 and telescoping, states
\[
dd^cH=\frac1{n+1}(p_2)_*
       \big(\langle T^{n+1}\rangle-\langle R^{n+1}\rangle\big).
\tag{3}
\]
Printed Corollary 13.6.1 identifies $H$ on $A_0$ with the distribution induced by $z\mapsto E_\theta^\phi(U_z)$. The local slice mass is $m$, since all $U_z$ have bounded difference from $\phi$.

Write $\beta=p_2^*\omega_{\mathrm{FS}}$ and $L_\phi=p_1^*(\theta+dd^c\phi)$. On $A_0$, $T=L+B\beta$ and $R=L_\phi+B\beta$. Multilinearity, $\beta^2=0$, and smooth-factor compatibility give
\[
\langle T^{n+1}\rangle
  =\langle L^{n+1}\rangle+(n+1)B\beta\wedge\langle L^n\rangle,
\quad
\langle R^{n+1}\rangle
  =(n+1)B\beta\wedge\langle L_\phi^n\rangle.
\tag{4}
\]
The omitted $\langle L_\phi^{n+1}\rangle$ vanishes because it is pulled back from the $n$-fold $X$ (the truncation justification appears in printed Step 3, lines 101–103). Corollary 13.6.1, this time with difference weight replaced by $1$, gives *for both $U_z$ and $\phi$*
\[
(p_2)_*\big(\beta\wedge\langle L^n\rangle\big)
=m\omega_{\mathrm{FS}}
=(p_2)_*\big(\beta\wedge\langle L_\phi^n\rangle\big).
\tag{5}
\]
Thus the two $B$-terms in (3) cancel **exactly**, even when $U$ is not maximal. Restrict (3) to $A_0$ and combine (4)–(5) to obtain (1). Since $A_0$ was arbitrary, (1) holds on all of $A$. Positivity of $\mu_U$ proves both subharmonicity and the harmonicity criterion; if $(p_2)_*\mu_U=0$, then $\mu_U$ has zero mass over every relatively compact subannulus, and so vanishes.

For the angular normalization take $z=re^{i\vartheta}$, $t=-\log r$. Pome uses $dd^c=(i/2\pi)\partial\bar\partial$, hence for a smooth radial $f$,
\[
dd^c_z f(-\log|z|)
=\frac{f''(t)}{4\pi}\frac{dx\wedge dy}{r^2}
=\frac{f''(t)}{4\pi}\,d\vartheta\wedge dt.
\]
This formula extends to distributional $f''$ by mollification in the $t$-variable. Integrating over a full $2\pi$ angular circle gives
\[
\tau_*(dd^c_z f(-\log|z|))=\tfrac12 f''.
\]
Push (1) forward by $\tau$ to obtain (2) with the **factor $2/(n+1)$**. No curvature sign is changed by $t=-\log r$ because the second derivative brings two minus signs.

**Independent scalar calibration.** If $h$ is smooth subharmonic and bounded on compact subannuli and $U(x,z)=\phi(x)+h(z)$ (with global boundedness if using (A)), then
\[
E_\theta^\phi(U_z)=m h(z),\qquad
\mu_U=(n+1)p_1^*\langle(\theta+dd^c\phi)^n\rangle\wedge p_2^*(dd^c h).
\]
Both sides of (1) equal $m\,dd^c h$. For $h(z)=c(-\log|z|)^2$, $c\geq0$, formula (2) reads $f''=2cm$ exactly. This independently fixes the potential $n+1$, $2\pi$, and radial normalization factors.

## Direct reading and boundaries of certification

- **Lemma 17.8.1, 11–38:** checked the decreasing Bedford–Taylor Dirichlet replacements, the cutoff weight on the plurifine set, weighted capacity limit, and zero top NPP measure. The logical direction is maximal $\Rightarrow$ zero NPP. The **converse is false for unbounded psh** and was already logged in earlier `POME-MAX-NPP-ZERO-NONCONVERSE-001`; it is **not** logged again.
- **Lemma 17.8.2, 43–54:** checked the $\Gamma$-invariant Perron argument, boundary gluing, uniform upper bound and preservation of endpoint data under the regularized upper envelope. No false printed assertion identified. Its Choquet-envelope and psh pasting inputs are not re-proved here.
- **Theorem 17.8.3, 59–112:** read all five steps: projective gluing, product-current integration by parts, maximality/vanishing, the radial Laplacian normalization and endpoint continuity, followed by monotone energy limits. The new formula (1) uses the *un-cancelled positive top product* in Step 3 for **arbitrary bounded subgeodesics**. The displayed theorem remains correct, and this audit does not replace its full proof.
- **Selected prerequisite statements:** Theorem 17.2.5 (integrated `docs/sections/relative-energy-and-perron-segments--integration-by-parts-for-bounded-differences/index.html`, blob `5779ef1a17a52e02052c7485a7aa04adf606aace`, from line 155), Corollary 13.6.1 (integrated `docs/sections/non-pluripolar-products--fiber-integration-and-modifications/index.html`, blob `9954a43d90d5cae8ef744968636d7a5912348fce`, lines 11–30, tag `BEC54934FC2C`), and the energy definition in §17.3.2 (blob `16fdcc4c6a6f0cc75e69ba267bd7da2b2d7922a1`, lines 32–37). This is **selected dependency inspection, not complete upstream transitive proof certification**.

**Affected dependents / proposed action:** audit-only optional corollary to equation (17.8.4), explaining the nonnegative curvature measure for bounded subgeodesics and its exact vanishing criterion; relevant to §§17.7–17.9 and later geodesic-energy uses. Do **not** infer maximality for unbounded potentials from $\mu_U=0$. The printed theorem is **not** false, no new independent proof gap has been confirmed, and no body/registry/tag change is authorized by this report.

**Coverage delta:** +1 entire current mathematical section (§17.8) directly reviewed, +3 selected prerequisite statements inspected, +0 complete upstream proof chains. §17.8 had earlier selected visits; no historical first-visit claim. Existing open and resolved ledger entries remain unchanged.

**Scope and workflow:** user-excluded Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme were **not** opened; previous notes stay **deferred-by-user**, not resolved/certified. No build, test, CI, main/source, permanent-tag, registry or published-site modification.
