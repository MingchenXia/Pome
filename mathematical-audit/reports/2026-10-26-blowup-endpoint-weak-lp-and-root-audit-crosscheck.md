# 2026-10-26 — The sharp weak endpoint for blowup pushforward densities; independent density-root crosschecks

**Actual checkpoint (UTC):** 2026-10-25T17:04:42.882Z. **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Pre-write audit head:** `6fc009d70378c952fb5567bbf9420994453deeab`. **Scope:** targeted direct review of the integrated §§15.23.2/.5/.10 and §15.24.1/.4, plus selected rechecking of §§15.32.1/.4–.6/.9/.11. No section or upstream existence theorem is certified in full.

**Excluded at the author's direction:** the entire dedicated Demailly approximation/regularization/Bergman/`L²`/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme. Any appearance of a dependent existence or Hölder theorem below is *recorded only*, not reopened; old notes remain **deferred-by-user**, not resolved.

## POME-BLOWUP-WEAK-ENDPOINT-001

**Status:** **verified conditional deduction**, low severity. **The printed theorem is correct, not a false theorem.** This is an optional precise endpoint supplement to the existing strict (L^s) statement.

**Exact current-source anchors:** `docs/sections/equations-with-prescribed-singularities--minimal-singularities-on-blowups/index.html`, main blob `884c20eb0ab2b613129a84232e9b6688f3aba993`. Section setup lines 10–17; Proposition **15.23.2**, source label `non-kahler-pluripotential-theory-7C4F9B6C`, permanent tag `E42F32DA29D8`, lines 20–56; Theorem **15.23.5**, source label `non-kahler-pluripotential-theory-3D393512`, tag `66FFA0C36433`, lines 60–90; exponent Equation **15.23.7**, tag `7E7FF8A6A54E`, lines 67–70; Jacobian computation Equation **15.23.8**, tag `2BE1216FD9F5`, lines 77–85. The iterated-blowup Theorem **15.23.10**, label `non-kahler-pluripotential-theory-5971231E`, tag `37D35D78F0C6`, lines 102–121, was inspected *only* for the iteration boundary.

**Claim with hypotheses and endpoint convention.** Let (pi:X=mathrm{Bl}_Z Y	o Y) be the blowup of a compact smooth complex (n)-fold (Y) along a **smooth center (Z) of complex codimension (rge2)**. Fix a smooth positive volume form (mu) on (X) and a smooth positive volume form (v) on (Y) (take (v=h^n) in the printed theorem). If (1<p<infty), (fge0) lies in (L^p(X,mu)), and
[
pi_*(fmu)=Fv,qquad s_*=rac{rp}{(r-1)p+1},
]
then (F) has the **endpoint weak-(L^{s_*})** bound
[
oxed{sup_{t>0} t,v({F>t})^{1/s_*}
       le C_{pi,mu,v,p},|f|_{L^p(X,mu)}.}
]
This is an ordinary measure-theoretic pushforward estimate and uses **no** Monge–Ampère existence, regularization, or Hölder-continuity result. It does not assert strong (L^{s_*}).

**Complete proof.** Write (W=d(pi_*mu)/dv) off (Z), which suffices as (v(Z)=mu(E)=0). In the standard blowup chart with transverse complex normal coordinates ((z,w)), the map is ((z,w)mapsto(z,zw)) and its complex Jacobian is (z^{r-1}); directions tangent to (Z) contribute bounded smooth factors. Finitely many bounded projective-coordinate charts cover each exceptional fiber. Hence, in a compact tubular neighborhood of (Z),
[
0le W(y)le C,operatorname{dist}(y,Z)^{-2(r-1)}.
]
It is bounded away from this neighborhood. Tubular normal-coordinate volume estimates in real codimension (2r) therefore give, for all sufficiently large (t),
[
v({W>t})le C t^{-r/(r-1)}.
]
The layer-cake identity, splitting (int_A W,dv) at (tasymp v(A)^{-(r-1)/r}), proves for every measurable (Asubset Y)
[
pi_*mu(A)=int_A W,dvle C,v(A)^{1/r};
]
enlarge (C) to accommodate larger sets. For (p'=p/(p-1)), Hölder on (pi^{-1}(A)) yields
[
int_A F,dv=int_{pi^{-1}(A)} f,dmu
 le|f|_{L^p(mu)},mu(pi^{-1}(A))^{1/p'}
 le C|f|_p,v(A)^{1/(rp')}.
]
Take (A={F>t}). Since (t,v(A)leint_A F,dv), and
[
1-rac1{rp'}=rac{(r-1)p+1}{rp}=rac1{s_*},
]
we obtain the boxed bound. The same argument works with either target volume (h^n) or any comparable smooth volume form.

**Sharpness, including failure of the strong endpoint.** Fix an adapted chart over a small relatively compact part of (Z), and restrict the angular (w)-coordinates to a nonempty bounded open set. With a nonnegative cutoff supported there, set near (z=0)
[
f(z,w,y)asymp |z|^{-2/p}igl(log(e/|z|)igr)^{-eta},
qquad rac1p<etalerac1{s_*}.
]
The interval is nonempty since (s_*<p) for (rge2,p>1). The local upstairs (L^p) radial integral is
[
int_0^arepsilon rac{dt}{t,(log(e/t))^{eta p}}<infty.
]
Off the exceptional divisor, the downstairs density on the corresponding positive-angular-measure normal cone satisfies
[
Fasymp |z|^{-2(r-1+1/p)}igl(log(e/|z|)igr)^{-eta}.
]
The change-of-variables formula in the printed (15.23.8) gives at (s=s_*)
[
int F^{s_*}dv gtrsimint_0^arepsilonrac{dt}{t,(log(e/t))^{eta s_*}}
=infty,
]
because (s_*(r-1+1/p)=r) and (eta s_*le1). Thus **strong** (L^{s_*}) fails for a legitimate nonnegative (L^p) datum. For every (s'>s_*), restricting to normal annuli with radius comparable to (t) shows (F
otin L^{s',infty}): the quantity (F_{mathrm{level}}cdot v(	ext{annulus})^{1/s'}) grows as (t^{-2r/s_*+2r/s'}(log(e/t))^{-eta}). The weak-(L^{s_*}) exponent is optimal.

**Disposition and affected dependents.** Add an optional endpoint Lorentz-space corollary to the *pushforward density* paragraph of Theorem 15.23.5, preserving the original strict (L^s) estimate, all labels, and historical attribution. This alone gives no endpoint (L^infty)/Hölder estimate for the target Monge–Ampère equation; do not infer one. The multistage exponent in Theorem 15.23.10 is only a context comparison: a weak endpoint for an iterated composite is **not** asserted without a separate distortion analysis. Strict comparison and existence inputs of Theorem 15.23.5, including its cited regularization-dependent steps, are not verified here.

## Additional actual proof checks — not newly discovered results

- **§15.23, main blob above:** re-derived the divisor metric sign in Proposition 15.23.2:
  (	heta+dd^c((c+delta)L'-csigma)=pi^*h+(c+delta)[E]-deltaTheta'_E) when (L'=L+sigma,Theta'_E=Theta_E-dd^csigma). Distinguished the divisor current from the smooth Jacobian density in Theorem 15.23.5 and the total-transform statement in Theorem 15.23.10. Did **not** certify the full distributional descent/proper-pushforward current argument, its Hölder PDE input, or the full iterated blowup case.
- **§15.24, first selected proof-level pass:** `docs/sections/equations-with-prescribed-singularities--representing-measures-in-an-ordinary-type/index.html`, blob `124c7650d904ff9617e90fe5e283c98e72261ea5`, Proposition **15.24.1**, source `non-kahler-pluripotential-theory` entry tag `A46357C92C12`, lines 10–114, and Lemma **15.24.4** tag `F9088D3DDEBB`, lines 118–129. Checked the inequalities (q_{i,m}learphi), the decreasing weighted convex combination, the fixed-(k) mixed-mass domination, and the role of (sigma)-finiteness in Radon–Nikodym. Local domination Lemma 5.27.10, extended-product theorem 13.14.3 and the global strict-potential input remain **conditional**, not independently certified here.
- **§15.32, incremental only:** `docs/sections/equations-with-prescribed-singularities--stability-of-the-subsolution-threshold/index.html`, blob `903ae0ce7173604063a833295dd94e971b18fd72`: Theorem **15.32.1** tag `D988D47D5E0E` (11–29), Propositions **15.32.4–.6** tags `D697A55DE07C`, `4C06D1B94BD1`, `C926F63790E3` (40–129), Proposition **15.32.9** tag `2210D4123A64` (196–231), and factor-root Proposition **15.32.11** tag `7A2CC1A3258E` (248–281) checked selectively for normalization, truncations, topology and completeness. **No new net-convergence result** is claimed: the previous `POME-SUBSOL-ROOT-NET-DOMCONV-001` already proves the arbitrary-directed-net extension, with a quantitative split, in `2026-10-24-root-net-dominated-convergence-and-determinant-squared-gap.md`. We neither repeat nor promote it as new progress.

## Unresolved / deferred / verification boundary

The new weak-endpoint estimate is a complete local geometric/measure-theoretic deduction. It does not establish the full analytic solution assertion of Theorem 15.23.5, the full classification of positive currents for a sequence of blowups, the (sigma)-finiteness or local Bedford–Taylor assertions used in §15.24, or all Gauduchon duality claims of §15.32. Those retain their earlier conditional/unreviewed statuses. Neither `main`, generated mathematical source HTML, proof registry, permanent tags, canonicalization, CI, website publication nor mathematical formalization was modified. Only the durable audit notes are proposed for the review branch.
