# Classification ledger — 2026-11-04 — Okounkov flag corrections and nested resolutions

**Main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Primary integrated reading:** docs/sections/the-theory-of-okounkov-bodies--flags-and-valuations/index.html, blob 9190d2ae0d3e51ca0ca965000cb9b5b2ec965c85.
[Detailed independent coordinate proof and exact source anchors](../reports/2026-11-04-okounkov-flag-birational-matrices-and-resolution-audit.md).

| Stable ID | Severity; status | Exactly checked | Decision / proposed action |
| --- | --- | --- | --- |
| POME-OKO-FLAG-TWO-BLOWUPS-001 | low; **verified conditional deduction** | Definition 19.3.12, source sgpt:E615C683 / permanent E494C67EB4B8, lines 161–179; Eq. 19.3.13 sgpt:827D77FC / 63511F34173E; Prop. 19.3.14 sgpt:DD7439A2 / D094DD00A592, lines 183–236; Prop. 19.3.17 sgpt:6A0E92BC / 8D2910CD1CEC and Eq. 19.3.18 sgpt:E051E414 / 1C158885A628, lines 241–305 | For a flag line and point on P², blowups at the flag point and its strict-transform intersection yield right-hand upper transvections [[1,1],[0,1]] twice, hence [[1,2],[0,1]]. Direct exact verification for arbitrary nonzero rational function germs, not arbitrary positive currents. Original propositions **not** refuted. |
| POME-OKO-FLAG-NESTED-RESOLUTION-001 | medium; **candidate** proof gap | Theorem 19.3.19, sgpt:44C3D868 / B00AB5301F7A, lines 311–332, especially 323–331; dependency Theorem 9.10.8, permanent 3CD8BF9158DD | Independently resolved pairs do not **automatically** have asserted compatible embeddings; specify a simultaneous ambient Hironaka embedded resolution and preserve the previously smooth subflags. Existence theorem not refuted. Potentially affects §19.3.20/22 and §19.4.7 conditionally. |
| POME-OKO-FLAG-TRACE-INPUT-001 | low; **candidate** notation/type error | Paragraph lines 176–179 following Eq. 19.3.13; source context sgpt:E615C683 / E494C67EB4B8; §20.2 ambient trace definition | The argument to Tr_W1 is already restricted to W1, not an ambient current. Clarify Tr_W1 of the ambient divisor or state an identity-trace convention; no false valuation statement proven. |
| POME-OKO-FLAG-PRINTED-LABEL-001 | low; **confirmed error** (editorial locator only) | Untagged displayed identity within Prop. 19.3.14, sgpt:DD7439A2 / D094DD00A592, lines 183–188 | Reader label "10.14" does not match §19.3; use generated current reader locator or unnumbered formula while retaining source provenance. Mathematical identity not refuted. |

**Unchanged:** previous §19.4.7 POME-OKO-FLAG-ON-MODEL-001 and every other confirmed error, proof gap, external dependency, verified repair and genuine duplication keep their previous status. No full mathematical-section certification; actual ToC 25 chapters / 747 numbered sections. Explicitly excluded Demailly approximation/regularization and Bergman/weighted-L²/OT/multiscale/positivity-loss work remains **deferred-by-user**.

Only new audit Markdown files; no original body/source/registry/permanent-tag/main modification, tests, build, CI or publication.
