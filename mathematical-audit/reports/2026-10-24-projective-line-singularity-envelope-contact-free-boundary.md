# 2026-10-24 audit: exact projective-line singularity envelope and its contact free boundary

**Reviewed current main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Starting review-branch head:** `db3212d649a3aa35bfffe2faa74bbf67e784a6fe` (preserved, not reset).
**Scope:** freshly read `main/AGENTS.md`, `main/documentation/proof-expansions.md`, current 25-chapter/747-section reader ToC, and `review/mathematical-audit/README.md`, `LATEST.md`, `SECTION_MATRIX.md`, and `LEDGER.md`. The 747 rows constitute an inventory, not verification. New selected mathematical reading is confined to §§16.20–16.21; §21.1 was checked only for conventions. No whole section certified.

## Permanent anchors and proof actually inspected

1. `docs/sections/envelopes-and-model-potentials--singularity-envelopes/index.html`, **main blob `8d55c95795ea2a0a3cf5cb81bd4abb4ba867a16a`**, physical lines **10–16** (Definition 16.21.1; Pome permanent tag `99168E437529`, source `foundations-of-pluripotential-theory:BF5AA585`), **19–59** (Proposition 16.21.2 and proof; permanent tag `037CA226D141`, source `92AD249D`), and **61–81** (Proposition 16.21.3 and proof; permanent tag `5ADA09DD223E`, source `38793463`). Section permanent tag `88E8C70208D8`, source `0D6D8695`.
2. `docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--contact-with-an-arbitrary-singular-potential/index.html`, **main blob `f64401a04bf44d21da59668ed415945c559de3ac`**, lines **42–109** (Theorem 16.20.2, including Steps 1–5; permanent tag `F6E7514B9542`, source `foundations-of-pluripotential-theory:F324B92D`), especially lines **104–106** (mixed polarization and contact-density argument); lines **111–125** (Corollary 16.20.4, tag `6EFE0C8DBCE3`, source `AF879DB1`). This is a selected examination of the polynomial and contact steps, **not** an independent validation of every cited BT/capacity/PDE theorem. The elementary smooth-majorant lemma 16.20.1 was read for context only and is *not* treated as Demailly approximation.
3. `docs/sections/convex-analysis-and-toric-potentials/index.html`, blob `e875ab348461c739ae3799c6906f8f13b9050ba7`, §21.1 conventions only: logarithmic coordinate `x=log|z|²`, the normalization of convex slopes, and the distinction between arbitrary volume and unit-normalized Fubini–Study volume. This is context, **not** a new §21.1 theorem review.

## POME-MODEL-P1-FREEBOUNDARY-EXACT-001

**Status:** `verified conditional deduction`. **Severity:** low (explanatory sharpness/model computation, **not** a false theorem or a repair).
**Precise hypotheses:** $X=\mathbb P^1$, $0<a<1$, normalized $\omega=dd^c\log(1+|z|^2)$ in $z=Z_1/Z_0$, and the Pome convention $dd^c=\frac{i}{2\pi}\partial\bar\partial$. Put
\[
u_a(z)=a\log\frac{|z|^2}{1+|z|^2},\quad
R_a^2=\frac{a}{1-a},\quad
h(a)=-a\log a-(1-a)\log(1-a).
\]
The function $u_a$ extends as an $\omega$-psh function on $\mathbb P^1$, with a unique pole at $z=0$, of Lelong number $a$, and with $\sup_Xu_a=0$.

**Exact envelope (not a guessed pointwise obstacle):**
\[
\boxed{
P_\omega[u_a](z)=w_a(z)=
\begin{cases}
a\log|z|^2+h(a)-\log(1+|z|^2),& |z|^2\le R_a^2,\\
0,& |z|^2\ge R_a^2.
\end{cases}}
\]
The two branches agree with equal first radial derivatives at $|z|^2=R_a^2$, so the formula is globally continuous outside its logarithmic pole and has no boundary-shell current.

### Direct proof of the envelope assertion

Write $x=\log|z|^2$, $F(x)=\log(1+e^x)$, (x_a=\log(a/(1-a))). Then $F'(x_a)=a$, and the supporting affine function $L(x)=ax+h(a)$ is tangent to $F$ at $x_a$; convexity gives $L\le F$. Thus $w_a=L-F\le0$ for $x\le x_a$ and $w_a=0$ for $x\ge x_a$. The function $H=w_a+F$ is affine on $(-∞,x_a]) and equal to (F) on ([x_a,∞)$. Its derivative is nondecreasing: it is $a$ to the left and $F'(x)\ge a$ to the right. Therefore $\omega+dd^cw_a\ge0$, including across the matching circle. Since $w_a-u_a$ is bounded on the compact sphere (the logarithmic terms cancel at 0), $w_a\preceq u_a$; hence $w_a$ is an admissible competitor for $P_\omega[u_a]$.

Conversely let $v\in\mathrm{PSH}(X,\omega)$ satisfy $v\le0$ and $v\preceq u_a$. On the punctured disc $0<|z|<R_a$ the function
\[
G(z)=v(z)+\log(1+|z|^2)-a\log|z|^2-h(a)
\]
is subharmonic: $v+\log(1+|z|^2)$ is subharmonic and $a\log|z|^2+h(a)$ is harmonic off 0. Because $v\le u_a+C$, near 0,
\[
G(z)\le (1-a)\log(1+|z|^2)+C-h(a),
\]
which is bounded above. The removable-singularity theorem extends $G$ subharmonically across 0. On $|z|=R_a$, the tangent relation $F(x_a)=ax_a+h(a)$ and $v\le0$ give $\limsup G\le0$. The subharmonic maximum principle gives $G\le0$ on the whole disc, i.e. $v\le w_a$ there. Outside the disc $w_a=0\ge v$. Thus every competitor is below $w_a$; taking the usc envelope proves the displayed equality. This comparison uses no Demailly-type approximation and no compactness-of-sequences shortcut.

### Curvature, non-pluripolar mass, exact contact and discrepancy

Distributionally,
\[
\omega+dd^cu_a=(1-a)\omega+a[0],\qquad
\omega+dd^cw_a=a[0]+\mathbf1_{\{|z|\ge R_a\}}\omega .
\]
Here ([0]) is the unit Dirac mass, by the Poincaré–Lelong normalization; the equality for $w_a$ has **no measure supported on the matching circle**, since both value and first radial derivative match. Non-pluripolar products in complex dimension one discard the Dirac mass at a logarithmic pole, yielding
\[
\boxed{\mu_{u_a}=(1-a)\omega,\qquad
\mu_{w_a}=\mathbf1_{\{|z|\ge R_a\}}\omega.}
\]
The normalized Fubini–Study radial mass is
\[
\int_{\{|z|\le R\}}\omega=\frac{R^2}{1+R^2}.
\]
Consequently $int_{|z|\le R_a}\omega=a$ and $int_{|z|\ge R_a}\omega=1-a$, so
\[
\int_X\mu_{u_a}=\int_X\mu_{w_a}=1-a.
\]
Moreover $V_\omega=0$, the contact set ${w_a=V_\omega}={|z|\ge R_a}$, and therefore
\[
\boxed{\mu_{w_a}=\mathbf1_{\{w_a=V_\omega\}}\mu_{V_\omega}},
\]
**equality** in the domination of Proposition 16.21.3 on this example. The unprojected $u_a$ has diffuse mass on both sides of the free boundary, and yet the envelope has exactly the same total mass. Specifically,
\[
\boxed{\|\mu_{w_a}-\mu_{u_a}\|_{\rm TV}
=(1-a)\,a+a\,(1-a)=2a(1-a).}
\]
The total-variation convention here is the mass of the absolute signed measure, without an additional factor (1/2); it reaches (1/2) at $a=1/2$. This explicitly separates preservation of **total** non-pluripolar mass from preservation of the **measure**. It does not contradict Proposition 16.21.2(3), which asserts only the former.

### Verification of the relevant printed steps and boundaries

- Proposition 16.21.2(2): each rooftop approximant is bounded above by $V_\theta$ and has the original singularity type by Proposition 16.11.7; the two competitor families have the same supremum. The special example has a *strictly larger* normalized envelope $w_a\ge u_a$ and confirms why taking the supremum matters.
- Proposition 16.21.2(3): the mixed-mass passage explicitly uses Corollaries 13.8.8–9. The concrete one-dimensional mass identity above is **independent** of certifying those general mixed-mass continuity theorems.
- Proposition 16.21.3: ${u+k\le V_\theta}\downarrow\{u=-\infty}$ and the non-pluripolar measure of (u) does not charge that pole set. The printed limit to a fixed dominating measure is compatible with the model, where equality holds.
- Theorem 16.20.2, Step 4 (main HTML physical line 104): for $lambda_j>0$ and $E=\cap_j{u_j=f_j}$, the scalar restricted identity is a measure-valued homogeneous polynomial in the $lambda_j$, and the $lambda_1\cdots\lambda_n$ coefficient is (n!) times the desired mixed wedge. Step 5 (line 106) uses the fact that weak Hessians of $W^{2,p}$ functions agreeing on a measurable set agree there a.e.; it is conditional on the established regular-envelope theorem and weak-Hessian locality. **No new gap or false theorem has been established by these selected checks.**

**Affected dependents / proposed action:** Proposition 16.21.2(3), Proposition 16.21.3, the mass/contact discussion in §§16.20–16.22, and toric intuition in §21.1. The proposed amendment is an **optional explanatory example**, not a correction of the source theorem, proof registry, reading text, or tags. Do not conflate equal total mass with equal distributions. No existing canonical duplicate or permanent-tag conflict was found in these passages.

**Excluded/deferred:** All dedicated Demailly approximation/regularization, Bergman, $L^2$, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion work remains `deferred-by-user`, not reopened, proved, resolved or certified. The elementary subharmonic removable-singularity/maximality proof above is unrelated to that programme. Resolution/principalization and historical attribution remain unchanged.

**What was and was not executed:** The displayed Fubini–Study integration, tangency derivative, maximum-principle comparison and measure calculation were derived explicitly. No independent symbolic/numerical script, project test/build, CI, website publication, formalization check, merge, PR/issue creation, or source/body/registry/canonicalization/permanent-tag/main modification was executed. This is a **selected** review of two sections, not an assertion that their entire dependency chains or the 747-section collection are verified.
