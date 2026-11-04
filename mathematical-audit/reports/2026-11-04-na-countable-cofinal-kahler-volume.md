# 2026-11-04 — A countable cofinal Kähler scale for the analytic non-Archimedean inverse limit

**Finding:** `POME-NA-KAHLER-INDEX-COFINAL-001` — **low / verified conditional deduction**. The printed definition and volume assertion are correct; this is an explicit, internally conditional proof of the index-set reduction and of the monotonicity sentence, **not** a new theorem error or a certification of the entire analytic theory.

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Integrated reading edition:** `docs/sections/non-archimedean-pluripotential-theory/index.html` (blob `8448d710690ebe1cc28040f9611d05c9d008a961`), physical lines **25–47, 64–80, 118–136, 141–169**. Definition **22.1.2** source `sgpt:B01CC65A`, permanent `657951EB240B`; transition equation **22.1.3** source `sgpt:93C71D7B`, permanent `A99876729E5F`; Proposition **22.1.5** source `sgpt:5BA764A5`, permanent `B80F3474DB2F`; Definition **22.1.7** source `sgpt:6F37B588`, permanent `A92D6DFAC0CF`; Lemma **22.1.9** source `sgpt:DA29B884`, permanent `587EEDE88F4F`. Cross-check: Proposition **16.3.9**, source `sgpt:9640EC28`, permanent `E58386609911`, in `docs/tag/E58386609911/index.html` (blob `1e68b2ecc01c81a0765c77e31144ee4c2e43a6cd`); and Proposition **17.14.6** `sgpt:3F2306F9`, permanent `BF40FB71C62C` (tag-page blob `559287fe06ae6302d5197b18ecd5e3dbb235cb2a`). Source labels are provenance, not replacements for their current reader locators.

## Claim A: cofinality and exact reconstruction

Let `X` be a connected **compact** Kähler manifold of positive complex dimension, `theta` a smooth real closed representative of a pseudo-effective class, and `omega_*` **any fixed Kähler form**. Put `omega_k=omega_*/k`, `k=1,2,...`. The order in §22.1 is deliberately reversed: `eta preceq eta'` means `eta >= eta'` pointwise. The chain satisfies `omega_k preceq omega_(k+1)`.

For every Kähler form `eta`, the continuous minimum eigenvalue of `eta` relative to `omega_*` is positive at each point of compact `X`; its global minimum `c_eta>0`. For any integer `k>1/c_eta`, one has `eta >= omega_*/k`, i.e. `eta preceq omega_k`. Thus the **countable chain is cofinal in the actual directed set of all Kähler forms**. There is no extraction of a cofinal subsequence from an arbitrary net, no sequential compactness assertion, and no assumption that Kähler forms lie in one cohomology class.

Write `A_eta = PSH^NA(X,theta+eta)_{>0}` and, whenever `eta>=xi`, write `T_(eta,xi):A_xi -> A_eta` for the transition map `P_(theta+eta)[·]_I` of Eq. 22.1.3. The compatibility identity printed at lines 39–43 says `T_(zeta,eta) T_(eta,xi)=T_(zeta,xi)` when `zeta>=eta>=xi`.

Restrict any full compatible family `(Gamma^eta)_eta` to `Gamma_k=Gamma^(omega_k)`. Conversely, given a compatible sequence `(Gamma_k)_k` with `Gamma_k = T_(omega_k,omega_l)(Gamma_l)` for `l>=k`, define its coordinate at any Kähler form `eta` by
```text
Gamma^eta := T_(eta,omega_k)(Gamma_k), for any k such that omega_k <= eta.
```
For two such choices `k,k'`, take `l>=k,k'`; then `omega_l <= omega_k,omega_k' <= eta` and the printed composition identity gives both formulas equal to `T_(eta,omega_l)(Gamma_l)`. If `eta>=xi`, choose `k` with `omega_k <= xi`; compatibility gives `T_(eta,xi)(Gamma^xi)=Gamma^eta`. The constructions are inverse. Consequently, **as sets (without additional topology claims)**,
```text
lim_{eta in Kah(X)} A_eta   ~=   lim_{k>=1} A_(omega_*/k).
```
This is valid even when `{theta}` is merely pseudo-effective rather than big: all input spaces and maps are exactly the ones in Definition 22.1.2. It is a statement about the existing transition system; it does not independently reconstruct the internal `I`-envelope maps or prove their full well-definedness.

## Claim B: a precise proof of decreasing volume and reduction of its limit

Fix a full compatible `Gamma`. For comparable Kähler forms `eta>=xi`, put `u=Gamma^(theta+xi)_{-infinity}`, `T=theta+xi+dd^c u >=0`, and `v=eta-xi >=0` (a smooth semipositive closed form). Proposition 22.1.5 identifies the more-positive-class endpoint with `P_(theta+eta)[u]`. Its total non-pluripolar mass agrees with that of `u` computed in class `theta+eta` by Proposition 16.3.9. Hence, with standard non-pluripolar-product notation,
```text
V_eta = integral_X <(T+v)^n>
      = sum_{j=0}^n binom(n,j) integral_X <T^j> wedge v^(n-j)
      >= integral_X <T^n> = V_xi.
```
The inequality uses *only* positivity and multilinearity of mixed non-pluripolar products with smooth positive factors (the internally cited Proposition 13.11.4). It does not exchange a limiting operation with a wedge product. This proves the decreasing-net assertion immediately after Definition 22.1.7 **conditional on the stated upstream propositions** and also identifies precisely the step otherwise omitted there. There is no claim to have reverified those upstream non-pluripolar-product constructions.

A decreasing nonnegative real net over a directed set converges to its infimum. By cofinality,
```text
vol(Gamma) = inf_{eta in Kah(X)} V_eta
           = inf_{k>=1} V_(omega_*/k)
           = lim_{k->infinity} V_(omega_*/k).
```
In particular the value is independent of the chosen fixed Kähler form `omega_*`; this is **cofinality**, not an assertion that an arbitrary net has a convergent subsequence.

## Why compactness is substantive

On the noncompact complex line, with `omega_* = i dz wedge dbar(z)` (up to a positive constant), the form `eta = exp(-|z|^2) omega_*` is Kähler but is not bounded below by `omega_*/k` for any integer `k`. Thus this particular cofinal-chain reduction is **not justified without compactness**, which the printed theorem correctly assumes.

## Disposition and affected uses

- **Status:** low / **verified conditional deduction**; Definitions 22.1.2 and 22.1.7 and Proposition 22.1.5 are not refuted. The reduction is a direct order-theoretic theorem assuming the source-stated transition maps and their compatibility; the mass monotonicity invokes the existing non-pluripolar multilinearity and mass preservation.
- **Suggested addition (proposal only):** after Definition 22.1.2 note that every fixed positive Kähler form yields a countable cofinal scale `omega_*/k`, and explain its inverse-limit restriction/reconstruction. After Definition 22.1.7 insert the displayed mixed-mass expansion as justification of `decreasing`. Do **not** replace the original net definition: retain it as the intrinsic, choice-free formulation.
- **Dependents examined:** Definition 22.1.7 (volume); Proposition 22.1.8 (comparison with a positive-mass class); Lemma 22.1.9 (mixed-volume expansion). Their full independent analytic proof chains remain **unverified**, as do Proposition 16.3.9 and all prerequisites to non-pluripolar multilinearity. No regularization, Bergman, weighted-`L^2`, Ohsawa–Takegoshi, multiscale or positivity-loss programme was reopened.
- **Coverage discipline:** newly examined **§22.1.2–3, 22.1.5, 22.1.7–9**, with dependency-only crosschecks **§17.14.6 and §16.3.9**. Not all of §22.1, Chapter 22 or the project was verified; no software tests or website builds were performed.
