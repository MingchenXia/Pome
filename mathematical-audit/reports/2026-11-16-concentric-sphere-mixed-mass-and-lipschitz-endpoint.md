# 2026-11-16 — exact concentric-sphere Bedford–Taylor masses and the Lipschitz shell endpoint

## Scope, revision, and immutable reading anchors

**Finding ID:** POME-SPHERE-NESTED-MASS-CRITICAL-LIPSCHITZ-001. **Severity:** low. **Status:** verified conditional deduction, not a confirmed error, not a complete upstream proof certification. **Source theorem remains correct:** Proposition 15.26.2 only asserts the existence of some positive domination constant and one \(C^{0,1/2}\) potential; neither assertion is disproved. The results below improve the *quantitative lower bound* for its **same** potential and construct a different, **Lipschitz** potential for a different shell probability. They are not source/body edits.

Reviewed immutable **main** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; targeted actual integrated reading files:

1. \`docs/sections/equations-with-prescribed-singularities--singular-measures-on-shrinking-spheres/index.html\`, blob \`354dfdf5224fac8896103ec09aa5936351021914\`; Eq. **15.26.1**, original \`non-kahler-pluripotential-theory:4C0F3404\`, permanent tag \`938F2C76C18A\`, physical lines **10–23**; Proposition **15.26.2**, original \`non-kahler-pluripotential-theory:92442012\`, permanent \`8F3C95237950\`, statement lines **26–30**, construction and proof lines **33–65** (especially curvature 36–48, radial Hölder estimate 50–56, diagonal mass inequality 58–64). Corollary **15.26.3** (\`non-kahler-pluripotential-theory:BBB972F3\` / \`AB5B44EC4BDD\`, lines **69–80**) and Theorem **15.26.4** (\`non-kahler-pluripotential-theory:7EBE40DC\` / \`6076D6F3256C\`, lines **84–99**) read only for dependency consequences.
2. \`docs/sections/plurisubharmonic-functions-and-singularities--local-products-and-capacity/index.html\`, blob \`ddb2ac8d9de27a22152872e07e5e787d138a790e\`; Lemma **5.27.25**, original \`non-kahler-pluripotential-theory:961DE4FB\`, permanent \`3242D4BA1F13\`, physical lines **518–527** and its immediately following radial computation; the normalized spherical identity and the underlying radial Stokes flux were read and compared with the present multi-shell computation.

Previous ledger IDs \`POME-SPHERE-MA-NORM-001\`, \`POME-SPHERE-HOLDER-SHARP-001\`, and \`POME-HOLDER-BALL-MASS-EXPONENT-001\` remain distinct. They establish the individual sphere normalization and universal power bounds / \(\alpha<1\) shell existence. **This report's new assertion is the exact nonlinear *interaction mass* between all concentric shells and its original-\(1/2\) improved constant; it also proves the previously unaddressed globally Lipschitz (\(\alpha=1\)) *singular-shell* endpoint and its failure of differentiability.** It neither re-registers those earlier statements nor claims a stronger universal estimate than their established \(r^{n\alpha}\) bound.

## Exact all-shell measure: a sharper constant for the printed potential

Work in the coordinate ball where the cutoff \(\chi=1\). Fix \(n\ge2\), \(r_j=r_0 2^{-j}\) and a positive exponent \(a>0\), with
\[
 Z_a=2K\sum_{j\ge1}r_j^a,\qquad d_{j,a}=\frac{r_j^a}{Z_a},
 \qquad
 \phi_a(z)=\sum_{j\ge1} d_{j,a}\log\max\{|z|^2,r_j^2\}.
\]
The series is uniformly convergent on the closed inner ball because
\(\sum_j r_j^a(1+|\log r_j|)<\infty\). Each summand is bounded psh there; so is the limit. The project convention is \(dd^c=\frac{i}{2\pi}\partial\bar\partial\); \(\sigma_j\) is the **probability** surface measure on \(|z|=r_j\). Define
\[
 q_a=(2^a-1)^{-1},\qquad
 C_{n,a}=(1+q_a)^n-q_a^n.
\]
Then **the entire pure local Bedford–Taylor measure**, including every interaction term, is
\[
 \boxed{\quad (dd^c\phi_a)^n
   = C_{n,a}\sum_{j\ge1}d_{j,a}^{\,n}\,\sigma_j\quad}
 \tag{A}
\]
on the inner ball, with **no mass at the origin, between spheres, or in its remaining smooth radial annuli**.

**Proof.** Set \(t=\log|z|^2,\ t_j=\log r_j^2\). The continuous convex profile
\(g_a(t)=\sum_jd_{j,a}\max\{t,t_j\}\) has derivative, on the interval
\(t_{j+1}<t<t_j\),
\[
 g_a'(t)=\sum_{k>j}d_{k,a}
  =q_a d_{j,a},
\]
and across \(t=t_j\) its derivative increases by exactly \(d_{j,a}\). On the outermost annulus \(t>t_1\) its slope is \(\sum_jd_{j,a}\), while \(g_a'(t)\to0\) as \(t\to-\infty\).

The **same radial Stokes identity explicitly computed in the proof of Lemma 5.27.25** applies to any bounded radial psh function \(g(\log|z|^2)\) with a convex nondecreasing profile: the cumulative mass inside a radius away from the support of \(g''\) is \((g'(\log R^2))^n\), provided the limiting inner slope is zero. In the smooth-profile case this follows by expanding
\[
 (dd^c g(t))^n
  =n(g')^{n-1}g''\,dt\wedge d^ct\wedge(dd^ct)^{n-1}
\]
and integrating the normalized angular flux \(1\) from the proof of Lemma 5.27.25. For the present countably piecewise-affine profile, take finite inner-truncated sums (replace the omitted \(\max(t,t_j)\) by the constants \(t_j\)), followed by the elementary convex-profile smoothing of that same lemma, and use bounded Bedford–Taylor monotone convergence / uniform bounded-potential convergence. No **Demailly** approximation or global regularization theorem is invoked. This yields the Stieltjes mass \(d((g_a')^n)\). Its jumps are
\[
 (q_ad_{j,a}+d_{j,a})^n-(q_ad_{j,a})^n
  =C_{n,a}d_{j,a}^n.
\]
Rotational invariance makes each jump the corresponding multiple of normalized \(\sigma_j\). On open gaps \(g_a''=0\), so the top product vanishes; at the origin the cumulative mass is \(\lim_{t\to-\infty}(g_a'(t))^n=0\). This proves (A). As a consistency check, the total mass equals
\[
 C_{n,a}\sum_jd_{j,a}^n
 =\Big(\sum_jd_{j,a}\Big)^n,
\]
by the geometric-series identity
\(C_{n,a}=(2^{an}-1)/(2^a-1)^n\).

For **the original printed exponent** \(a=1/2\), \(q_{1/2}=1+\sqrt2\) and hence
\[
 C_{n,1/2}=(2+\sqrt2)^n-(1+\sqrt2)^n>1 \quad(n\ge2).
\]
The full global cutoff series \(u_0=\sum_jd_{j,1/2}\psi_j\) from original lines 36–48 satisfies \(h+dd^cu_0\ge h/2\), and on the inner ball \(u_0=\phi_{1/2}\). By positivity and mixed Bedford–Taylor products,
\[
 (h+dd^cu_0)^n \ge (dd^cu_0)^n
  = C_{n,1/2}\frac{S_n}{Z^n}\rho .
\]
The measure on the right is supported strictly in the inner ball, so this inequality holds **globally on \(X\)**. Thus in the original Proposition 15.26.2 the **same constructed** \(u_\rho\) permits the larger explicit witness
\[
 \boxed{k_{\rm improved}
       =\big((2+\sqrt2)^n-(1+\sqrt2)^n\big)\,S_n/Z^n.}\tag{B}
\]
The previous printed \(k=S_n/Z^n\) is valid but neglects positive off-diagonal shell interactions. **No claim is made that (B) is the globally optimal constant**, since background and mixed-current terms can further contribute.

## New critical singular-shell endpoint: a globally Lipschitz potential

Keep the **same** cutoff \(\chi\), background \(h\), common \(K\) and dyadic radii, but set
\[
 Z_1=2K\sum_{j\ge1}r_j,\quad
 d_{j,1}=r_j/Z_1,\quad
 u_1=\sum_{j\ge1}d_{j,1}\psi_j,\quad
 \rho_1=\frac{\sum_{j\ge1}r_j^n\sigma_j}
                {\sum_{j\ge1}r_j^n}.
\]
The curvature bound of original lines 36–48 still gives
\(h+dd^cu_1\ge h/2\). The series converges uniformly, and outside the smaller ball all summands have the same smooth cutoff expression; hence \(u_1\) is smooth away from the nested-shell region.

Inside that region write \(U(R)=\sum_jd_{j,1}\log\max(R^2,r_j^2)\).
For \(r_{j+1}<R<r_j\),
\[
 U'(R)=\frac2R\sum_{k>j}d_{k,1}
       =\frac{2r_j}{Z_1R}\le\frac4{Z_1},
\]
and for \(R>r_1\) the same bound follows from
\(\sum_{k\ge1}r_k=r_0=2r_1\). The function is continuous at each shell and at \(R=0\); integrating the a.e. derivative shows it is **globally radial Lipschitz** in the small ball, with the patch smooth elsewhere. The \(\sup_X=0\) normalization does not change this. In contrast, the termwise estimate \(t\sum_{r_j\ge t}r_j^{a-1}\) used for \(a<1\) gives a spurious \(t\log(1/t)\) loss when \(a=1\); the **joint radial slope** is essential at this endpoint.

It is **not differentiable at the center**. Indeed for every \(j\),
\[
 \frac{U(r_j)-U(0)}{r_j}
 =\frac2{Z_1}\sum_{\ell\ge1}2^{-\ell}\ell\log2
 =\frac{4\log2}{Z_1}>0.
\]
A differentiable radial real function at the origin must have zero derivative (opposite radial directions have the same values), contradicting these positive difference quotients.

Formula (A) for \(a=1\) gives the **exact pure local mass**
\[
 (dd^cu_1)^n=(2^n-1)Z_1^{-n}\sum_{j\ge1}r_j^n\sigma_j,
\]
so, globally,
\[
 \boxed{\ (h+dd^cu_1)^n\ge
 (2^n-1)\frac{\sum_jr_j^n}{Z_1^n}\,\rho_1.\ }\tag{C}
\]
The probability \(\rho_1\) is singular with respect to smooth volume and does not charge pluripolar sets (the individual spherical non-pluripolarity in Lemma 5.27.25 and countable additivity). Thus **every compact Hermitian background in the printed setup admits a Lipschitz, non-\(C^1\) strictly \(h\)-psh potential whose Monge–Ampère measure dominates an explicit singular probability supported on infinitely many shrinking spheres**. This is stronger at the regularity endpoint than the printed one-half-Hölder construction and is distinct from the previously audited *single smooth radial* endpoint \(|z|\).

## Status, consequences, and exclusions

- **Classification:** \`POME-SPHERE-NESTED-MASS-CRITICAL-LIPSCHITZ-001\` — **low / verified conditional deduction**. The radial calculation and regularity estimates are explicit; using \`5.27.25\` and standard bounded Bedford–Taylor continuity is a declared **internal dependency**, not a certification of their complete upstream proofs. The original Proposition 15.26.2 is **true**; the earlier coefficient was simply conservative.
- **Correction proposed, not applied:** append an optional quantitative remark to §15.26.2 giving (B), and an independent \(\alpha=1\) singular-shell endpoint proposition (C). Preserve the existing statement, source label, permanent tags, history and every previous audit entry.
- **Dependents:** The reference domination hypothesis of Corollary 15.26.3 and Theorem 15.26.4 also holds for \(\rho_1\), so their **conditional** solvability consequences extend to bounded nonzero densities \(d\nu/d\rho_1\). This does **not** prove the existence theorems \`15.25.1\` or \`15.10.1\` and does not establish uniqueness for their homogeneous equations.
- **Exact coverage:** new interaction/endpoint derivation against §15.26 Eq.1, Proposition .2, its lines 36–64, plus the radial proof of §5.27.25; downstream §§15.26.3–4 contextual only. Both sections were **previously partly visited**, so **0 first-visited sections, 0 whole-section certificates** (current 25 chapters / 747 numbered sections).
- **Out of scope:** Demailly approximation/regularization and the dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion programme remain **deferred-by-user**, neither resolved nor certified. No changes to main, text bodies, proof registries, permanent tags, CI or published site are proposed or carried out in this audit report.
