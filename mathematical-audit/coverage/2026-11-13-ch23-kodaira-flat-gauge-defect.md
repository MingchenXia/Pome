# Exact incremental coverage — 2026-11-13 — §23.2.53

**Main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Actual main ToC:** 25 chapters, 747 numbered sections, inventory `docs/chapters/index.html` blob c0c07abf4d8f7575b54cff2ec694fcf987f51cf8.
**Integrated section:** `docs/sections/locally-conformally-kahler-geometry/index.html`, blob 6ebf8e604b45d3eb748037af506145273ca3875d. No production modifications.
**Coverage status:** genuinely new proof steps inside previously partly reviewed §23.2; **0 newly first-visited numbered sections, 0 fully certified sections**. Old unresolved and deferred findings retain their classifications.

| Reader locus | Stable source label / permanent tag | Physical lines | Actual mathematical check | Unverified dependencies |
| --- | --- | --- | --- | --- |
| Definition 23.2.2, Lee convention | `non-kahler-pluripotential-theory:FE5EDE37` / 48F6C713AFE3 | 22–28 | \(d\omega=\lambda\wedge\omega\) sign and strict Lee period | General LCK theory not certified |
| Proposition 23.2.7 | `:F551F544` / 11EBB7AD1165 | 98–127 | Uses printed \(q=0\) iff Gauduchon for particular explicit metrics | No new general proposition certification |
| Theorem 23.2.47 | `:C87CCD5B` / C4981F6B1F78 | 785–889 | Exact reported \(S^-\)-versus-\(q\) formula crosschecked for statement relevance only | Full Bianchi/Bochner argument remains conditional |
| Example 23.2.53, compact Kodaira quotient and Vaisman metric | `:F3D1120B` / E37387C4675B | 906–951 | Direct coframe, \(\lambda_1=-e^4+f'e^1\), \(C=1-f''>0\), \(d\omega_1=\lambda_1\wedge\omega_1\), parallel Lee dual for *every* periodic \(f\) | Compact nilmanifold and holomorphic volume checked in printed quotient |
| Example 23.2.53, flat conformal metric | same source/permanent | 953–982 | All-dimensional conformal-factor uniqueness on this surface; \(h=C^{-1/2}\), \(\omega^2/2=e^{1234}\), exact \(q=-((1-f'')^{-1/2})''\), \(q=0\) exactly when \(f\) constant | No regularization/PDE existence |
| Additional high-frequency Fourier family (not printed) | finding POME-KODAIRA-FLAT-GAUDUCHON-FREQUENCY-001 | [report](../reports/2026-11-13-kodaira-flat-gauge-periodic-defect.md) | \(f_k=a(2\pi k)^{-2}\cos(2\pi kx)\), \(0<a<1\), fixed Lee class, fixed volume, uniform \(C^0\) metrics, \(\|q_k\|_2^2=(2\pi k)^4J(a)>0\) | Optional \(\|S^-\|_2\) conclusion requires Theorem 23.2.47 conditionally |

**Finding status:** low / verified conditional deduction. Printed Example 23.2.53 and Theorem 23.2.47 remain correct as far as this selected check reaches. Documentation corollary only proposed; no source/body/tag/registry edit.

**Scope exclusion:** Demailly approximation/regularization and its dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme is **deferred-by-user**, neither investigated nor certified.

[Complete proof](../reports/2026-11-13-kodaira-flat-gauge-periodic-defect.md) · [classification](../ledger/2026-11-13-kodaira-flat-gauge-periodic-defect.md).
