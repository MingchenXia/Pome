# Ledger — 2026-11-17 directed positive-volume semigroup nets

| Finding ID | Severity | Classification | Precise scope | Result and remaining dependency |
| --- | --- | --- | --- | --- |
| `POME-OKO-DIRECTED-SG-POSVOL-NET-001` | low | **verified conditional deduction** | `docs/sections/almost-semigroups/index.html` (main `b6933b772f41b45918f7e25ed1afbbb1fd892272`, blob `33898b2963ad0f8b7e30bf414276642f60925b74`); Lemma 19.7.29 tag `B63FC87B8DDF`, lines 477–525; Definition 19.7.26 tag `0270FA2C03BD`, lines 393–396; cited Lemmas 19.7.19/27 and Theorem 19.7.20 | Decreasing **arbitrary directed net** in \(\mathcal S'(C)\) with \(\inf_i \mathrm{vol}(S_i)>0\) converges in \(d_{\rm sg}\) to the saturated semigroup of the intersected cones; exact distance equals the convex-body volume deficit. The convex compactness/net argument and full-lattice property are proved. Original sequence lemma correct. The printed KK12/lattice-counting theorem is an identified input for the general semigroup volume identification, **not independently certified**. |

**Proposed optional correction/strengthening (not applied):** Add the directed-net statement after Lemma 19.7.29, retaining all original hypothesis, historical attribution, permanent tags and the sequence version. Its use in the positive-volume closure of almost semigroups and continuous \(\Delta\) mapping is limited to monotone nets; Theorem 19.7.32 is not recertified.

**Previously recorded items left untouched:** older sharp Okounkov-body Hölder modulus, zero-volume boundary countermodels, and convex slice endpoint-gap entries. No earlier proof gap, confirmed error, candidate, or external dependency is reclassified by this addition. The separate Demailly approximation/regularization and its dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale and positivity-loss programmes remain **deferred-by-user**.

**Coverage:** existing partly sampled §19.7, selected new argument around 19.7.29 only; **0 first visits, 0 completely verified sections**, global inventory 25 chapters/747 sections (not independently recounted in this pass). No project tests, build, CI or publication.

[Complete source-anchored proof](../reports/2026-11-17-directed-decreasing-almost-semigroup-nets.md) · [Coverage delta](../coverage/2026-11-17-ch19-directed-net-semigroups.md)
