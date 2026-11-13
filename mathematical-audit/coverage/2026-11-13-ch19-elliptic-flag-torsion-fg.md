# Exact coverage — 2026-11-13 / elliptic flag valuation semigroups

**Pinned main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; table of contents 25 chapters / 747 numbered sections. Audit branch: `review/mathematical-audit`. This session tests a nonexcluded example, not the general theorem chain.

| Scope | Exact main blob and locator | Actual work | Limit |
|---|---|---|---|
| §19.9.1 and Lemma 19.9.2 | `docs/sections/flags-convex-bodies-and-section-growth/index.html` blob `83557f0e15275253661fe679c75407e6636d497c`, lines 12–54; Lemma source `non-kahler-pluripotential-theory:EAA5A841`, permanent `2B103C3B777A` | Explicit all-degree genus-one vanishing-order filtration, equality `#valuations = h0 = md` and the arithmetic jump at the top vanishing order | Lemma's general proof read as contextual input; no full §19.9 verification |
| Definition 19.7.26 | `docs/sections/almost-semigroups/index.html` blob `33898b2963ad0f8b7e30bf414276642f60925b74`, lines 393–398; source `sgpt:56C14254`, permanent `0270FA2C03BD` | Direct degree-one cone slice computed as `[0,d]`, full group lattice checked; exact finite-generation iff torsion proved independently | No general §19.7 saturation/counting inputs certified |
| Definitions 19.3.2, 19.3.5 | `docs/sections/the-theory-of-okounkov-bodies--flags-and-valuations/index.html` blob `9190d2ae0d3e51ca0ca965000cb9b5b2ec965c85`, lines 8–14, 50–56; sources `sgpt:D3CA5409`, `sgpt:8623A0C4`; permanent `F1312787FCC5`, `46E1CFFE3502` | Flag (Esupset{p}) fits the printed smooth/admissible flag definitions | No new higher-dimensional flag trace theorem certification |
| Theorem 19.9.3 | §19.9 blob above, lines 55–61; source `non-kahler-pluripotential-theory:36D35BB7`, permanent `EA8340BC8D54` | Statement-only compatibility with exact bound `k<=dm` | Not a new proof of the general bound |

**Coverage delta:** 0 new first-visited numbered sections; 0 fully certified numbered sections; new independent conditional explicit model and finite-generation equivalence on already partly inspected §§19.3, 19.7, 19.9. The genus-one Riemann–Roch/Serre-duality dimension formula is named as the model's unreviewed standard input. [Full dated proof](../reports/2026-11-13-elliptic-flag-semigroup-torsion-finite-generation.md) · [classified ledger](../ledger/2026-11-13-elliptic-flag-torsion-fg.md).

**Scope exclusions:** user-deferred Demailly approximation/regularization, dedicated Bergman/L²/OT, multiscale charts and positivity-loss proof programme not visited or certified. No main/source/tag/registry/canonicalization edits, tests, CI or site publication.
