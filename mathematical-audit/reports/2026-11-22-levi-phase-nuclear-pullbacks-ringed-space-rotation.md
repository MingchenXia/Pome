# 2026-11-22 — Levi-flat foliation regularity, relative nuclear maps, and ringed-space reductions

## Immutable audit scope and classification

- Reviewed \`main\`: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- Audit branch: \`review/mathematical-audit\`; this is an audit-only document, not a correction merged into the reading edition.
- **Complete current integrated direct mathematical readings:** §§9.63 (lines 7–68), 9.68 (7–64), 9.64 (7–61). The last is a full recheck of already partly audited material, **not** a historically new discovery.
- **Full repeat readings, not new coverage:** §§17.8 (7–112), 17.9 (7–75), 9.59 (7–47), 9.60 (7–60), 9.77 (7–19). Prior geodesic, Proj, monomial-curve, and Fujiki-deformation findings are not re-entered.
- **Selected-only, not complete:** §20.8.13–14 (physical lines 291–322; only the nonexcluded volume/Siu/decomposition and differentiation steps), §20.1.5–14 (lines 40–179). There is no claim to have proved the long restricted-volume construction, whose other steps cite the user-excluded programme.
- New classified mathematical result: **POME-LEVI-PHASE-CAUCHY-ESTIMATE-001** — **low / verified conditional deduction**, *not* a false printed theorem or a repair of a broken proof. No newly confirmed source error or new external dependency is asserted.
- No fully transitive theorem-chain certification. No build, project tests, CI, publication, source/body/registry, or permanent-tag edit.

## 1. A quantitative form of the fixed-torus phase reconstruction

**Stable anchor:** integrated \`docs/sections/levi-foliations-and-boundary-regularity/index.html\`, main blob \`8c022608e6bb846204f1eb000ef2d4d873183441\`, physical lines **8–18**; Lemma **9.63.2**, source \`demailly-complex-geometry:1E6C08BD\`, permanent \`6F469AB373C2\`; equation **9.63.3**, permanent \`F5B6ECCA47FD\`. Downstream Theorem **9.63.4**, source \`demailly-complex-geometry:B87F9D00\`, permanent \`A6B15EBA6E91\`, lines **24–68**.

Fix \`m >= 1\`, positive radii \`r=(r_1,...,r_m)\`, and \`0 <= rho_nu < r_nu\`. Let \`J\Subset I\` be a compact interval and \`0 <= j <= l\`. Let \`H_1,H_2\` satisfy the exact hypotheses of Lemma 9.63.2 on the same polydisc and interval. Set
\[
b_\nu(\zeta,t)=\operatorname{Im}H_\nu(\zeta,t),\qquad
a_\nu(t)=\operatorname{Re}H_\nu(0,t).
\]
For every multi-index \(\alpha\in\mathbb N^m\), define
\[
A_{\alpha,\rho,r}:=
\prod_{h=1}^m\frac{\alpha_h!\,r_h}{(r_h-\rho_h)^{\alpha_h+1}}.
\]
Then the following **explicit interior stability bound** holds:
\[
\boxed{
\begin{aligned}
&\sup_{(z,t)\in \overline{P_\rho}\times J}
 \left|\partial_z^\alpha\partial_t^j(H_1-H_2)(z,t)\right|\\
&\quad\leq
\mathbf 1_{\alpha=0}\,\|\partial_t^j(a_1-a_2)\|_{C^0(J)}
+\left(2A_{\alpha,\rho,r}+\mathbf1_{\alpha=0}\right)
 \|\partial_t^j(b_1-b_2)\|_{C^0(\mathbb T_r\times J)}.
\end{aligned}}
\tag{A}
\]
In particular, the passage from the torus imaginary part and the center real normalization to any fixed collection of interior holomorphic/transverse derivatives is Lipschitz in these data. It **does not** claim uniform control up to \(\partial P_r\), a boundary derivative estimate, or stability of the Levi foliations under perturbation of their defining hypersurfaces.

**Complete direct proof.** The printed equation 9.63.3, applied separately to each \(H_\nu\), gives
\[
H_1-H_2=(a_1-a_2)
+i\,\mathrm{avg}_{\mathbb T_r}
\left[\left(2\prod_{h=1}^m\frac{\zeta_h}{\zeta_h-z_h}-1\right)(b_1-b_2)\right].
\]
The torus is fixed. The assumed \(C^l\) transverse regularity permits \(j\) differentiations under the integral for \(j\leq l\). Holomorphic differentiation of the kernel gives the *exact* factorization
\[
\partial_z^\alpha\prod_h\frac{\zeta_h}{\zeta_h-z_h}
=\prod_h\frac{\alpha_h!\,\zeta_h}{(\zeta_h-z_h)^{\alpha_h+1}}.
\]
On \(|z_h|\leq\rho_h\), \(|\zeta_h|=r_h\), its modulus is bounded by \(A_{\alpha,\rho,r}\). The \(-1\) term and the \(a_1-a_2\) term differentiate to zero when \(\alpha\ne0\). For \(\alpha=0\), use \(|2K-1|\leq 2|K|+1\). The normalized average has operator norm at most one in \(C^0\); triangle inequality proves (A), with no limiting interchange. Every assertion holds for the original arbitrary real parameter interval and any compact \(J\Subset I\).

**Status and effect.** This is a **verified conditional deduction** from the printed fixed-torus identity and its exact hypotheses. Lemma 9.63.2 and Theorem 9.63.4 were **not** found false. The explicit seminorm constant can be quoted after Lemma 9.63.2 when quantifying the transverse \(C^{k-1}\) control of \(\log h_t\) in Theorem 9.63.4. The theorem's independent Levi-bracket/Frobenius input, Proposition 9.34.1, is *not* transitively certified here. Source attribution is preserved.

## 2. Direct full review — §9.63

Physical lines 24–68 of the integrated file were read against Lemma 9.63.2. The proof starts with a \(C^{k-1}\) complex-leaf Frobenius chart, normalizes the transverse curve at \(z=0\), and obtains the exact scalar identity
\[
2\operatorname{Re}(p\,h_t)=0,\quad
p=-\tfrac12(\varphi_u+i),\quad
\operatorname{Im}\log h_t=-\tfrac\pi2-\arg p.
\]
The sign of this phase formula agrees with the branch where \(h_t(0,0)=1\) and \(p(0,0)=-i/2\). Also \(\operatorname{Re}\log h_t(0,t)=\log|1+i\varphi_u(0,t)|\). Lemma 9.63.2 supplies all \(C^{k-1}\) transverse derivatives on an interior fixed torus; integrating \(h_t\) then restores \(C^k\) regularity of the plaque map. The inverse follows from \(\operatorname{Re}h_t>1/2\) near the base point. No new error was established. The earlier Levi-bracket equivalence is a specifically identified, uncertified upstream internal dependency.

## 3. Direct full review — §9.68

**Exact file:** \`docs/sections/relative-nuclear-maps-and-composition/index.html\`, blob \`b426cb8cb38d4c1b66611ac9f8cb87b35406aca9\`, mathematical lines **7–64**. Proposition **9.68.1**, source \`demailly-complex-geometry:FCE8E21F\`, permanent \`DB4C2E622157\`, lines **11–26**. Example **9.68.2**, source \`demailly-complex-geometry:E95AA863\`, permanent \`FECBDA82D7CC\`, lines **31–64**.

Rechecked that the pullback \(\{(s,m):u(s)=p(m)\}\) of the open module surjection \(p:M\to E\) is a closed Fréchet submodule; the projection onto \(S\) is an open surjection by the explicit neighborhood calculation. Nuclearity of this pullback is used **only** when both \(S\) and \(M\) are nuclear, not for an arbitrary Fréchet pullback. In the example, the square-zero ideal \(B=\ell^2\) has the key obstruction: a nonzero character component of an \(A\)-linear map \(\xi:N\to A\) from a nuclear module \(N\) would provide a complemented closed copy of \(B\) inside \(N\). The resulting failure of arbitrary precomposition is therefore consistent with the stated nuclear-source qualification. No new counterexample to Proposition 9.68.1 was found, and the nuclear permanence Theorem 2.13.3 remains a conditional internal input.

## 4. Ringed-space reductions and selected divisorial checks

**Entire current §9.64**: \`docs/sections/ringed-spaces-and-reductions/index.html\`, blob \`a84cbf2134702a33dc53c3de30ff097d9cfa1c1f\`, lines **7–61**. Proposition 9.64.2 source \`demailly-complex-geometry:A616BEB2\` / permanent \`ADC46EC60E54\`, and Proposition 9.64.3 source \`demailly-complex-geometry:29A82276\` / permanent \`16DE5782FC00\`. Checked the local nilradical sheaf, the distinction between locally nilpotent germs and a globally nilpotent section, and the residue-value kernel inclusion \(\mathcal N_X\subset\ker e_X\). The one-point reduced but not strongly reduced local-ring example is consistent. This does **not** re-enter the previously recorded strong-reduction coreflection deduction as a new finding.

**Selected §20.8 only**: \`docs/sections/divisorial-restricted-volumes/index.html\`, blob \`8eb1127568e77d6d045098361c366ceeb846b909\`. Read Lemma 20.8.13, source \`transcendental-positive-cones:A47ADAF8\` / permanent \`DA69AEE4E88A\`, **lines 291–301**, and nonexcluded parts of Lemma 20.8.14, source \`transcendental-positive-cones:54BBE5DC\` / permanent \`B50F0B700160\`, **lines 306–322**. For 20.8.13, pushing forward a positive current in \(\mu^*\alpha+t[F]\) and pulling back a current in \(\alpha\) preserve absolutely continuous top mass on the common isomorphism locus; the exceptional set has zero Lebesgue mass. Hence the volume is constant in \(t\ge0\), and the zero directional derivative gives \(\langle(\mu^*\alpha)^{n-1}\rangle\cdot[F]=0\), *conditional on* the internal full gradient Theorem 10.99.8. The finite-divisor-support justification of 20.8.14 refers to an excluded approximation input and has been **recorded as deferred-by-user, not rechecked, proved, or certified**. In particular **§20.8 is not marked completely reviewed**.

A comparison-only reading of the nonexcluded definitions and volume net in §20.1, blob \`4a793dfd462badcb351f54a36cb030cde14a399b\`, lines 40–179, did not revisit its excluded approximation proof; the previously recorded moving-point blowup findings were not repeated.

## Remaining risks, classification, and proposed action

- **Verified conditional deduction:** \`POME-LEVI-PHASE-CAUCHY-ESTIMATE-001\` (low). Optional separately reviewable text-only corollary after Lemma 9.63.2; no direct source edit.
- **Uncertified internal inputs, not new source errors:** §9.34.1 Levi-bracket/Frobenius, §2.13.3 nuclear stability, §10.99.8 big-class volume differentiability, and the stated current/volume assumptions.
- **Deferred-by-user:** all Demailly regularization/approximation and dedicated Bergman/L²/OT/multiscale-atlas/positivity-loss proof programmes. Existing historical audit notes remain intact, with no resolution or certification inferred.
- **Duplicates deliberately avoided:** the prior §9.59 Proj/Veronese, §9.60 analytic monomial curve, §17.8 energy-curvature, §17.9 geodesic extrema, §9.64 strong-reduction coreflection, §9.77 Fujiki input, and §20.1 moving-point volume findings.

Only **two current direct whole-section reviews (§§9.63, 9.68)** are added to the matrix's previously unreconciled rows; §9.64 is a full current reread, §20.8 a selected-only increment. The 25-chapter / 747-section table of contents is unchanged. No tests, builds, or full mathematical verification are claimed.
