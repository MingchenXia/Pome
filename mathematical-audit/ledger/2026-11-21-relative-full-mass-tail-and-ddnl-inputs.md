# Findings: relative energy tails and prescribed-mass solvability

**2026-11-21. Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Scope:** complete current §§16.5 and 11.9; prior §§11.5 and 11.7 selectively rechecked, not new findings.

## POME-RELENERGY-HALF-LEVEL-TAIL-REPAIR-001

- **Status/severity:** low / verified repair (a local proof-step clarification); **printed Proposition 16.5.30 and its conclusion are not false**.
- **Source:** integrated `docs/sections/the-envelope-operators--p-envelopes--relative-full-mass-classes/index.html`, blob `9c17814a07f78694a858dc941e6a76d2f3cc989f`; Proposition 16.5.30 source `sgpt:ABE17BA7` / permanent `4280CB108A7E` at physical line 545; equation 16.5.35 source `sgpt:653816BA` / permanent `F913F2DBE96C` lines 592–621, especially line 618.
- **Hypotheses:** \(\varphi\in\mathcal E^1(X,\theta;\phi)\), \(\varphi\le\phi\), finite \(\mu=\theta_\varphi^n\), \(A=\phi-\varphi\ge0\) with \(A\in L^1(\mu)\).
- **Issue:** the displayed limiting estimate uses the smaller set \(\{A\ge C\}\) to conclude a half-threshold tail decay. No valid direct fixed-\(C\) inequality justifies this with that smaller set (take \(A=3C/4\) on a unit-mass space). The **limiting conclusion itself is true**.
- **Verified replacement:** \(0\le C\mu\{A\ge C/2\}\le2\int_{\{A\ge C/2\}}A\,d\mu\to0\). Insert this before concluding (16.5.35), retaining the original theorem and source tags.
- **Dependents:** finite-energy cocycle and §16.5.36–.59 energy/rooftop arguments; correctness remains conditional on separately established non-pluripolar locality/comparison. Source-only patch proposed, not applied.

## POME-RELATIVE-FULL-MASS-DDNL-SOLVABILITY-EXTERNAL-001

- **Status/severity:** medium / genuine external dependency, **not** printed error.
- **Source:** same integrated blob; Theorem 16.5.8 source `sgpt:4D0318F8`, permanent `6F1A42885C28`, line 140; Theorem 16.5.9 source `sgpt:5A0069A8`, permanent `0E437FB98B97`, lines 147–157; explicit external proof input **DDNL19log**, line 157.
- **Hypotheses:** big smooth closed real \((1,1)\) background \(\theta\), positive-mass model \(\phi\), non-pluripolar data of the prescribed total mass for Theorem 16.5.8, or positive non-pluripolar data and exponential coefficient \(\lambda>0\) for 16.5.9.
- **Missing internal step:** internally deriving these full relative-mass existence/uniqueness and exponential comparison statements in exactly this generality is not supplied; the external citation must be retained, not mistaken for an error.
- **Dependents:** §16.5 Lemma 16.5.40 source `sgpt:E3FA9734` / permanent `4C2A27A8F97A` and finite-energy rooftop closure in Proposition 16.5.49, plus subsequent energy operations.
- **Proposed handling:** retain and explicitly classify this as unresolved external mathematical input; no completion of any deferred Demailly-related programme.

**Excluded scope:** Demailly approximation/regularization, dedicated Bergman/L2/OT/multiscale/positivity-loss completion deferred-by-user, not certified. **Audited:** §§16.5 and 11.9 complete current direct reads, +0 full upstream-chain certificates. [Proof and section detail](../reports/2026-11-21-relative-full-mass-tail-proof-and-convex-norms.md).