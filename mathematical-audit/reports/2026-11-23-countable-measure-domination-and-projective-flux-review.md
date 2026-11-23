# 2026-11-23 — Countable near-reference measure domination and projective flux review

## Version and exact scope

Reviewed main commit: b6933b772f41b45918f7e25ed1afbbb1fd892272.

- Entire current §15.24: docs/sections/equations-with-prescribed-singularities--representing-measures-in-an-ordinary-type/index.html; blob 124c7650d904ff9617e90fe5e283c98e72261ea5; physical mathematical lines 5–132; section tag 2BB76C1E3909; Proposition 15.24.1 permanent tag A46357C92C12, source label non-kahler-pluripotential-theory-2AFB7920; Equation 15.24.3 tag 3F73A2DB6267; Lemma 15.24.4 tag F9088D3DDEBB.
- Entire current §15.20: docs/sections/equations-with-prescribed-singularities--symmetry-and-the-selected-projective-limit/index.html; blob 5939b066b23315e66c9f8ec26a97677825fa2a16; physical mathematical lines 5–240; section tag 457A6A4C41F4; Proposition 15.20.1 tag 1750C7E75315; Theorem 15.20.4 tag 72B88B8B1639; Lemma 15.20.5 tag 5D3F7173CA27; Proposition 15.20.8 tag 517F0BB04B80.
- Selected nonexcluded Steps 2–3 of §15.25.1: docs/sections/equations-with-prescribed-singularities--the-homogeneous-equation-with-a-holder-reference/index.html; blob 0defdec5270db7ff34625b638c9ac2a31264ca4a; Theorem tag 8CE230CD94D4. Its smoothing/approximation premise was **not** audited.

Totals: two complete current sections, one selected; one new low / verified conditional deduction; zero new confirmed printed errors; zero complete transitive proof-chain certificates. Historical first-visit status remains unreconciled.

## POME-PRESCRIBED-TYPE-COUNTABLE-NEAR-REFERENCE-DOMINATION-001

**Severity and status:** low / verified conditional deduction; *not* an original theorem error.

**Statement.** Under exactly the hypotheses of Proposition 15.24.1—\(X\) compact, \(\theta\ge0\) a smooth big real \((1,1)\)-form, \(\varphi\in\operatorname{PSH}(X,\theta)\), and \(P_{\varepsilon\theta}(\varphi)\not\equiv-\infty\) for some \(0<\varepsilon<1\)—let \((\mu_j)_{j\ge1}\) be any countable family of finite non-pluripolar positive measures. For every \(\eta>0\), a *single* \(\psi\in\operatorname{PSH}(X,\theta)\) exists with

\[
\varphi-\eta\le\psi\le\varphi,\qquad
\mu_j\ll\operatorname{MA}^{\mathrm{ext}}_\theta(\psi)
\quad\text{for every }j.
\]

Indeed each \(\mu_j=f_j\operatorname{MA}^{\mathrm{ext}}_\theta(\psi)\), with nonnegative \(f_j\in L^1(\operatorname{MA}^{\mathrm{ext}}_\theta(\psi))\). There is no assertion of bounded densities.

**Proof.** Write \(m_j=\mu_j(X)<\infty\) and aggregate

\[
\beta_j=\frac{2^{-j}}{1+m_j}>0,\qquad
\mu=\sum_{j\ge1}\beta_j\mu_j.
\]

Then \(\mu(X)\le1\), the aggregate is non-pluripolar, and \(\mu_j\ll\mu\) for all \(j\). If all are zero, use \(\psi=\varphi\). Otherwise apply *the explicit construction* of Proposition 15.24.1 to \(\mu\), not just its bare conclusion. Physical lines 27–80 provide countably many \(\theta\)-psh competitors \(q_k\) and finite \(C_k\ge0\) with

\[
\varphi-C_k\le q_k\le\varphi;
\quad
\left[\operatorname{MA}^{\mathrm{ext}}_\theta(q_k)(E)=0\
\text{for every }k\right]\Longrightarrow\mu(E)=0.
\]

The positive weights in that construction are arbitrary subject to summability. Choose

\[
t_k=\frac{\min\{1,\eta\}}4\,
\frac{2^{-k}}{1+C_k}.
\]

Then \(T=\sum_k t_k<1\) and \(B=\sum_k t_k C_k<\eta\). The finite sums from lines 81–98 are

\[
\psi_N=\sum_{k=1}^N t_kq_k+
\left(1-\sum_{k=1}^N t_k\right)\varphi.
\]

They are decreasing \(\theta\)-psh functions, as \(q_k\le\varphi\), and \(\varphi-B\le\psi_N\le\varphi\). Their nontrivial decreasing limit \(\psi\) obeys \(\varphi-\eta\le\psi\le\varphi\) and has precisely the original ordinary singularity type.

For fixed \(k\), splitting off the summand gives \(\psi=t_kq_k+(1-t_k)w_k\) with \(w_k\in\operatorname{PSH}(X,\theta)\) of the same type. Positivity of mixed non-pluripolar products on the common finite locus, with the finite-truncation exhaustion of physical lines 99–105, yields

\[
\operatorname{MA}^{\mathrm{ext}}_\theta(\psi)
\ge t_k^n\operatorname{MA}^{\mathrm{ext}}_\theta(q_k).
\]

Every null set for the left-hand measure is therefore null for every right-hand measure, hence for \(\mu\) and every \(\mu_j\). The \(\sigma\)-finiteness theorem §13.14.3 explicitly invoked by the printed proof at line 107 permits Radon–Nikodym, giving

\[
\int_X f_j\,\operatorname{MA}^{\mathrm{ext}}_\theta(\psi)
=\mu_j(X)<\infty.
\]

This is a complete deduction *conditional on the printed internal prerequisites*, not a new construction of local representations or a certified full upstream proof chain. It gives neither a common \(L^\infty\) bound for \(f_j\), nor finite mass of \(\operatorname{MA}^{\mathrm{ext}}_\theta(\psi)\), nor a solution of an equation.

**Correction and dependents.** No correction to Proposition 15.24.1 is required. An optional strengthening could be proposed in a separately reviewable PR; audit notes alone do not modify source, registry or permanent tags. A potential dependent is the general-measure discussion at §15.37. The stronger bounded-density input of §15.10.1, and the Hölder-reference hypothesis of §15.25.1, **do not follow** from this statement.

## Independent checks of §15.20

**Symmetry and normalized limits (lines 11–28).** If a biholomorphism \(g\) preserves both \(\omega\) and \(f\,dV\), the pullback \(u_\lambda\circ g\) satisfies the same positive-exponent equation. Its uniqueness implies invariance; subtracting the global supremum and passing to a uniform cluster limit retain invariance. The compactness/uniqueness argument for the selected projective solution does not interchange uncontrolled limits. General Chapter 14 normalization/connectedness inputs remain separate already-recorded qualifications; the actual projective model is connected.

**No-jump radial flux (lines 79–132).** Let

\[
A(r,s)=(x(r)+s)(y(r)-s),\qquad
\Phi(r,s)=\int_0^s A(r,t)\,dt.
\]

An admissible upward jump \(h_-<h_+\), with both endpoints in \([-x(r_0),y(r_0)]\) and \(x(r_0)+y(r_0)>0\), would create an atom

\[
\Phi(r_0,h_+)-\Phi(r_0,h_-)
=\int_{h_-}^{h_+}(x(r_0)+s)(y(r_0)-s)\,ds>0.
\]

The prescribed radial measure has no atom; hence such jumps cannot occur. The lack of jumps alone does not rule out a singular-continuous derivative. That requires the remaining positive-distribution structure and the flux identity. We did not independently re-prove the upstream Bedford–Taylor continuity theorem.

**Projective ends (lines 155–183).** With \(a=\sigma+h\), the exterior equation is \(a(1-a)a'=\sigma(1-\sigma)\sigma'\). Define

\[
J(t)=\frac{t^2}2-\frac{t^3}3,\qquad
J'(t)=t(1-t)>0\quad(0<t<1).
\]

Boundedness of the potential forces \(a_\infty=1\), so integration constants match and strict monotonicity yields \(a=\sigma\), \(h=0\) on this end. This is conditional on the strict-interior and flux steps in the printed proof.

**Non-\(C^2\) band (lines 190–234).** At the transition \(r=t_*\in(0,1)\), the one-sided derivatives of the radial slope satisfy \(h_\lambda'(t_*-)=-z_0(t_*)<0\) and \(h_\lambda'(t_*+)=-p'(t_*)>0\). They are unequal, preventing \(C^2\) regularity. The submersion \(r\) transfers this to every point of the hypersurface. A smooth correction \(\rho\) cannot remove the jump. No new printed statement error was found.

## Actual audit limits

The local-to-global representation §5.27.10, \(\sigma\)-finite extended-mass §13.14.3, §14.26 projective model, and the nonexcluded elliptic/capacity inputs require separate certification. This report does **not** claim full proofs of them. The full §15.25 was **not** reviewed.

Demailly approximation/regularization and the dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain **deferred-by-user**, not resolved or certified. No tests, builds, CI, main/source/body/registry/permanent-tag/website changes, merges or publication.
