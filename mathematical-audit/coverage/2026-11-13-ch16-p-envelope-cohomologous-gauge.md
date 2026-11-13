# 2026-11-13 — precise selected proof coverage: §16.3 cohomologous P-envelope gauges

- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated path:** `docs/sections/the-envelope-operators--p-envelopes--rooftop-operator-and-the-definition-of-the-p-envelope/index.html`; blob `97681f31628eb362950837daaadde67d10507a2f`.
- **Previously sampled section:** §16.3, permanent `1BFD41225C11`, original `sgpt:6215ED06`.
- **Direct statement and proof inspected:** Definition 16.3.4 `sgpt:15C6153F` / `395DB7860949` at physical lines 79–85; equation 16.3.5 `sgpt:E4924BB8` / `7E001B03F24A` at 81–84; Proposition 16.3.8 `sgpt:EBC14D0B` / `EF5AC4B19C4D` at 108–131. The bounded-difference preorder was crosschecked at the §16.3 pointer to §16.7.1 (physical line 79) solely for the needed convention, not as an independent certification of §16.7.
- **New verification:** two-sided interval comparison for normalized P-envelopes when `theta' = theta+dd^c g`, and a Kähler/small-smooth-gauge example attaining both endpoints. This identifies the exact sign/normalization constants and avoids undefined differences at common poles. Finding `POME-PENVELOPE-GAUGE-SHARP-OSC-001`.
- **Not reviewed:** other substantive §16.3 proofs; upstream full PSH envelope compactness and non-pluripolar mass arguments; §16.8 entire preorder theory.
- **Inventory accounting:** 0 newly first-visited numbered sections; 0 fully verified numbered sections; existing current collection inventory 25 chapters / 747 numbered sections.
- **Scope exclusion:** no Demailly approximation/regularization or dedicated Bergman/L2/OT/multiscale/positivity-loss proof-completion work; these remain deferred-by-user.
- **Operations:** audit Markdown only, no production/source/registry/permanent-tag modifications, no tests/build/CI/website publication.
