# 2026-11-23 — Countable measure domination near a prescribed type, and projective symmetry/flux rotation

## Version, scope, and classification

- Reviewed current `main` commit: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. This report concerns its **integrated reading edition**, not merely original source titles.
- Entire current §15.24: `docs/sections/equations-with-prescribed-singularities--representing-measures-in-an-ordinary-type/index.html`, blob `124c7650d904ff9617e90fe5e283c98e72261ea5`, physical lines 5–132; section tag `2BB76C1E3909`, Proposition 15.24.1 tag `A46357C92C12`, inequality 15.24.3 tag `3F73A2DB6267`, Lemma 15.24.4 tag `F9088D3DDEBB`.
- Entire current §15.20: `docs/sections/equations-with-prescribed-singularities--symmetry-and-the-selected-projective-limit/index.html`, blob `5939b066b23315e66c9f8ec26a97677825fa2a16`, physical lines 5–240; section tag `457A6A4C41F4`, Proposition 15.20.1 `1750C7E75315`, Theorem 15.20.4 `72B88B8B1639`, Lemma 15.20.5 `5D3F7173CA27`, Proposition 15.20.8 `517F0BB04B80`.
- Selected nonexcluded Steps 2–3 of §15.25.1 only: `docs/sections/equations-with-prescribed-singularities--the-homogeneous-equation-with-a-holder-reference/index.html`, blob `0defdec5270db7ff34625b638c9ac2a31264ca4a`, Theorem tag `8CE230CD94D4`. Its upstream smoothing/approximation premise was **not** reviewed.
- One new **low / verified conditional deduction**; zero new confirmed printed theorem errors; zero complete transitive proof-chain certificates. Historical first-visit status remains unreconciled.

## POME-PRESCRIBED-TYPE-COUNTABLE-NEAR-REFERENCE-DOMINATION-001 — low / verified conditional deduction

**Claim (countably many measures, arbitrary ordinary-type proximity).** Assume exactly the hypotheses of Proposition 15.24.1: (X) compact, (	heta\ge0) a smooth big real ((1,1))-form, (arphi\in\mathrm{PSH}(X,\theta)), and (P_{\varepsilon\theta}(\varphi)\not\equiv-\infty) for some (0<\varepsilon<1). Let ((\mu_j)_{j\ge1}) be any countable family of finite non-pluripolar positive measures, and let (eta>0). Then there exists (\psi\in\mathrm{PSH}(X,\theta)) such that
[
\varphi-\eta\le\psi\le\varphi,\qquad
\mu_j\ll\mathrm{MA}^{\mathrm{ext}}_\theta(\psi)\quad\text{for every }j.
]
In fact, there are individual (f_j\ge0) with (f_j\in L^1(\mathrm{MA}^{\mathrm{ext}}_\theta(\psi))) and (\mu_j=f_j\mathrm{MA}^{\mathrm{ext}}_\theta(\psi)).

**Complete deduction from the stated internal inputs.** Write (m_j=\mu_j(X)<\infty), (\beta_j=2^{-j}/(1+m_j)>0), and (\mu=\sum_{j\ge1}\beta_j\mu_j). Then (\mu(X)\le1), (\mu) is finite and non-pluripolar, and (\mu_j\ll\mu) for each (j). If all measures vanish, choose (\psi=\varphi). Otherwise, run the actual construction in Proposition 15.24.1 for (\mu), retaining its entire sequence (q_k) of (\theta)-psh competitors satisfying (\varphi-C_k\le q_k\le\varphi), (C_k<\infty), and its verified null-set property (\mu\ll\sum_k\mathrm{MA}^{\mathrm{ext}}_\theta(q_k)) in the sense that common null sets are (\mu)-null. **The freedom to select the positive weights is the only additional step.** Put
[
t_k=\frac{\min\{1,\eta\}}{4}\,\frac{2^{-k}}{1+C_k}>0.
]
Then (T=\sum_k t_k<1) and (B=\sum_k t_k C_k<\eta). The finite sums
[
\psi_N=\sum_{k=1}^N t_k q_k+
\left(1-\sum_{k=1}^N t_k\right)\varphi
]
are decreasing (\theta)-psh potentials with (\varphi-B\le\psi_N\le\varphi). Their decreasing limit (\psi) is not identically (-\infty) and obeys (\varphi-\eta\le\psi\le\varphi), so it has the same ordinary singularity type.

For each fixed (k), the same tail decomposition as lines 97–104 of the source proof writes (\psi=t_kq_k+(1-t_k)w_k), with (w_k\in\mathrm{PSH}(X,\theta)) of the same ordinary type. Positivity of non-pluripolar mixed products on the common finite locus (and exhaustion by bounded truncations) yields
[
\mathrm{MA}^{\mathrm{ext}}_\theta(\psi)
\ge t_k^n\mathrm{MA}^{\mathrm{ext}}_\theta(q_k).
]
Consequently (\mu\ll\mathrm{MA}^{\mathrm{ext}}_\theta(\psi)), and therefore every (\mu_j\ll\mathrm{MA}^{\mathrm{ext}}_\theta(\psi)). The \(\sigma\)-finiteness input in §13.14.3, used by the printed proof at line 107, gives the individual Radon–Nikodym densities and
[
\int_X f_j\,\mathrm{MA}^{\mathrm{ext}}_\theta(\psi)=\mu_j(X)<\infty.
]
This uses no new regularization argument. In particular, it does **not** produce bounded densities, a finite mass of the reference measure, uniform \(L^1\) bounds over the family, or a solution of any Monge–Ampère equation.

**Status and dependents.** Verified *conditional* on the exact internal local-representation, mixed-product positivity, and sigma-finiteness premises of the printed Proposition 15.24.1; those upstream chains are not certified here. The proposition is not false, and no source/registry patch is necessary. This sharpened interface may be useful for the general-measure representation input at §15.37 and capacity-dominated existence discussions, but does not satisfy the stronger bounded-density hypothesis of §15.10.1. Theorem 15.25.1 uses a Hölder reference and must not be inferred from this claim.

## Independent cross-checks in the symmetry/flux chapter (§15.20)

1. **Symmetry under positive exponent, lines 11–28.** Pulling back the equation by a biholomorphism preserving both the Hermitian form and (f\,dV) gives the same equation. Given the printed uniqueness premise, (u_\lambda\circ g=u_\lambda). Supremum normalization and any uniform cluster limit retain that symmetry. A compactness/uniqueness selection argument does not interchange uncontrolled limits.
2. **Radial flux and no-jump mechanism, lines 79–132.** With (A(r,s)=(x+s)(y-s)), (\Phi(r,s)=\int_0^s A(r,t)dt), a positive upward jump of (h=G') inside ([-x,y]) would create the strictly positive atomic flux
[
\Phi(r_0,h_+)-\Phi(r_0,h_-)
=\int_{h_-}^{h_+}(x(r_0)+s)(y(r_0)-s)ds>0.
]
This contradicts the absolutely continuous prescribed radial density. It does not by itself eliminate a singular-continuous derivative: the remaining positivity and the flux identity must be used, as in the printed argument. This is a check of the given proof, **not** an independent full Bedford–Taylor continuity proof.
3. **Outer branch uniqueness, lines 155–183.** On (r\ge2), (a=\sigma+h) satisfies (a(1-a)a'=\sigma(1-\sigma)\sigma'). The primitive (J(t)=t^2/2-t^3/3) has (J'(t)=t(1-t)>0) on ((0,1)). Boundedness rules out a limiting (a_\infty<1); the integration constant is therefore zero, yielding (a=\sigma), hence (h=0) on this end, conditional on the already proved strict positivity and flux identity.
4. **Band non-(C^2) result, lines 190–234.** The two slopes at (t_*), (-z_0(t_*)<0) and (-p'(t_*)>0), differ. This is a genuine obstruction to (C^2) across (r=t_*), and the submersion (r) transports it to the projective hypersurface. A smooth correction (\rho) cannot remove the jump.

These checks find no new printed mathematical error. The connectedness-sensitive general existence and normalization inputs from Chapter 14 remain a **separate upstream qualification** (already audited); the explicit projective example is connected. The smooth-approximation input of §15.25 Step 1 remains **deferred-by-user** where it concerns the excluded regularization programme; only the subsequent measure inequalities and limiting logic were read.

## Coverage, correction policy, remaining work

- Two complete current mathematical sections directly read: §§15.20, 15.24. Selected nonexcluded §15.25 Steps 2–3; no claim of full §15.25 review.
- One new low conditional deduction, no new confirmed printed errors or local proof gaps, no complete transitive upstream certification.
- Future high-priority work: certify §15.24's internal local-measure theorem §5.27.10 and sigma-finiteness §13.14.3 **without** reopening excluded regularization; inspect the bounded-reference comparison step in §15.25 only outside the forbidden programme; independently assess §15.20's §14.26 projective model.
- Demailly approximation/regularization, Bergman, (L^2), Ohsawa–Takegoshi, multiscale atlases, and positivity-loss proof-completion projects remain **deferred-by-user**, neither resolved nor certified.
- No build, tests, CI, manuscript/source/body/registry/canonicalization/tag/main/website changes, PR merge or publication.
