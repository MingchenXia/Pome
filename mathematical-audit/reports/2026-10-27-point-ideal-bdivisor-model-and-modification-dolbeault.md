# Mathematical audit — the point ideal, the first Cartier model, and modification Dolbeault classes (2026-10-27)

- **Pinned published main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Starting audit head:** `1352f713ef37704dabde09d82995ac7849d48e2d`.
- **Scope:** first direct selected proof review of §§20.4.11, 20.4.14–15, 20.4.18 and §10.91.1–2; §20.4.17 and the analytic-resolution hypothesis are used only as stated inputs, **not** re-proved. The dedicated Demailly approximation/regularization and Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme is excluded by the author and remains **deferred-by-user**, not certified.
- **New finding:** one low-severity **verified conditional deduction**, not a false printed theorem or a certified resolution of any historical issue. The algebraic blowup and Poincaré–Lelong calculations below are explicit and require no excluded approximation proof.

## POME-POINT-IDEAL-BDIVISOR-NONBASE-CARTIER-001

**Status:** verified conditional deduction. **Severity:** low. **Correction:** optional worked example following Theorem 20.4.18, with a cross-reference to Proposition 10.91.1; no change to a statement, source, tag or canonicalization is requested.

**Pinned primary sources and exact reader anchors:**

1. `docs/sections/divisorial-currents-on-compact-modifications/index.html`, Git blob `79d6e21f9d3784bf3761846f77f90ad075253644`: Definition **20.4.11**, source `non-kahler-pluripotential-theory:DDEBA3E8`, permanent `6EC6FB71DCF4`, lines **208–220**; self-trace §**20.4.13** source `non-kahler-pluripotential-theory:9A3BEEA2`, permanent `F45AA1F2A651`, lines **252–263**; Lemma **20.4.14**, source `non-kahler-pluripotential-theory:8A6E9683`, permanent `691315D9AA1C`, lines **267–285**; Theorem **20.4.15**, source `non-kahler-pluripotential-theory:29CD462A`, permanent `25F4A4E3755D`, lines **289–311**; Theorem **20.4.18**, source `non-kahler-pluripotential-theory:BA4B812E`, permanent `0AD88DBD3706`, lines **340–363**.
2. `docs/sections/one-point-curvature-positivity-and-vanishing--one-point-positivity-and-modification-descent/index.html`, Git blob `95b3f78a729e01664c4a24d3ef8aa96143ead523`: Proposition **10.91.1**, source `demailly-complex-geometry:CAB0AEA4`, permanent `35E27213FA56`, lines **8–44**; Theorem **10.91.2**, source `demailly-complex-geometry:156BC1D4`, permanent `8532D3ED47E8`, lines **46–74**. Smooth/current Dolbeault comparison and the Kähler vanishing result cited there remain conditional inputs, not newly certified.

**Hypotheses and explicit construction.** On \(X=\mathbb P^2\), let \(p=[1:0:0]\), let \(\omega_{\rm FS}\) be the Chern form of \(\mathcal O(1)\) normalized by \(\int_{\mathbb P^1}\omega_{\rm FS}=1\), and let \(s_1=Z_1,s_2=Z_2\) be the global coordinate sections. Define a globally well-defined quasi-psh potential
\[
 \varphi=\log\!\bigl(|s_1|_{\rm FS}^2+|s_2|_{\rm FS}^2\bigr),\qquad
 T=\omega_{\rm FS}+dd^c\varphi\ge 0 .
\]
In the affine chart \(Z_0=1\), with \(x=Z_1/Z_0\), \(y=Z_2/Z_0\), the metric-weight cancellation gives exactly
\[
 T=dd^c\log(|x|^2+|y|^2).
\]
This current has analytic singularities of rational coefficient \(1\) at the isolated point \(p\) and has no generic divisorial Lelong coefficients on \(X\). In particular \(N_X(T)=0\) and \(\mathbb D(T)_X=\{\omega_{\rm FS}\}_{\rm BC}\).

Blow up \(p\), \(\pi:\widetilde X=\operatorname{Bl}_p\mathbb P^2\to X\), with exceptional curve \(E\simeq\mathbb P^1\). The rational map \([Z_0:Z_1:Z_2]\dashrightarrow[Z_1:Z_2]\) resolves into a holomorphic map \(f:\widetilde X\to\mathbb P^1\), restricting to an isomorphism on \(E\). In one blowup chart \(x=t,\ y=tv\), Poincaré–Lelong, in Pome's \(dd^c=(i/2\pi)\partial\bar\partial\) normalization, gives
\[
 \pi^*T=dd^c\log\!\bigl(|t|^2(1+|v|^2)\bigr)
       =[E]+dd^c\log(1+|v|^2)
       =[E]+f^*\omega_{{\rm FS},\mathbb P^1}.
\]
The other blowup chart gives the same current identity. The residual \(R=f^*\omega_{{\rm FS},\mathbb P^1}\) is **smooth, closed and semipositive** everywhere; this directly verifies nefness here, without using the smoothing input cited in §20.4.17. There are no further divisorial singularities. Thus
\[
 N_{\widetilde X}(T)=[E],\qquad
 \mathbb D(T)_{\widetilde X}=\{R\}_{\rm BC}
 =\pi^*\{\omega_{{\rm FS},\mathbb P^2}\}_{\rm BC}-\{[E]\}_{\rm BC}.
\]
For every model above \(\widetilde X\), pullback of \(R\) remains smooth semipositive, so \(\widetilde X\) is an **explicit nef Cartier realization** of \(\mathbb D(T)\), consistently with Theorem 20.4.18.

**Why the original base is not a Cartier realization.** Because \(\pi|_E\) is constant, the restriction to \(E\) of every smooth form pulled back from \(X\) vanishes. But \(f|_E\) is an isomorphism, so
\[
 \int_E R=\int_{\mathbb P^1}\omega_{\rm FS}=1
 \quad\text{while}\quad
 \int_E\pi^*\omega_{{\rm FS},\mathbb P^2}=0.
\]
These are well-defined cohomological pairings because both forms are closed. Consequently \(\mathbb D(T)_{\widetilde X}\ne\pi^*\mathbb D(T)_X\): the b-divisor is Cartier **on the blowup, not already on its base**. In Theorem 20.4.26 language the discrepancy for this first blowup is exactly \(E_\pi=E\).

**Separate Dolbeault consequence, with a precise limit of the assertion.** The same example makes the injection in Proposition 10.91.1 **strict** for \((p,q)=(1,1)\), \(F=\mathcal O\). Indeed \(R\) represents a \(\bar\partial\)-closed \((1,1)\)-class upstairs with \(\int_E R=1\). Any class of the form \(\pi^*[\alpha]\), \([\alpha]\in H^{1,1}_{\bar\partial}(X)\), integrates to zero over \(E\), because pullback of a smooth representative restricts to zero there and integration over the compact curve annihilates \(\bar\partial\)-exact \((1,1)\)-forms. Thus \([R]\notin\operatorname{im}\pi^*\). The printed result states a split injection, **not** surjectivity, so there is no error.

**Dependencies and affected results.** The local blowup chart, Poincaré–Lelong normalization, elementary positivity of Fubini–Study curvature and the explicit map \(f\) suffice for the computation. Using Definition 20.4.11 and Theorems 20.4.15/18 to phrase it as a b-divisor is conditional on their existing internal foundations; the demonstration does not audit or certify every trace-envelope input. Proposition 10.91.1 uses smooth/current Dolbeault comparison upstream; strictness is independently witnessed by integrating an actual smooth closed form. No claim is made about the map in other degrees or with arbitrary coefficients. This example prevents the mistaken strengthening “analytic singularities imply a nef Cartier realization already on \(X\)” and the mistaken strengthening “modifications preserve all Dolbeault groups isomorphically.”

## Other selected proof checks, with no new error

- **§20.4.14–15:** checked generic Lelong coefficient identification, finite/pushforward compatibility, and additivity of positive currents on the explicit blowup model. The self-trace limiting multiplier-ideal inequality is treated as an existing independent input, **not** reproved. In the example the coefficient computations come from the actual analytic ideal \((Z_1,Z_2)\), avoiding approximation.
- **§10.91.1–2:** checked the bundle-valued current pushforward formula, the degree-one change-of-variables left inverse, and the rank-at-most-\(m\) curvature pullback reasoning at critical points; strict positivity survives on a nonempty biholomorphic open set. The cohomological comparison and Kähler vanishing premises were not independently re-proved. There is **no new confirmed false theorem**.

**Coverage matrix:** exactly two rows received selected-scope updates: §20.4 (newly checked .11/.14–15/.18 passages on top of earlier selected .20/.22/.24 checks) and §10.91 (previously inventory-only, now selected .1–2). No whole section or chapter was certified; all **747** table-of-contents section identifiers, previous statuses and deferred-by-user items remain unchanged. No source, body, permanent tags, proof registry, CI, test/build, formal verification, or published site was touched.
