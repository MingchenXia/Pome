# Project-wide mathematical audit — 2026-11-01 — central blowup intersection test and detached restricted-volume equations

**Production main pinned:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Previous audit head at session start:** `24d9621ee95c3e5022154fd3924013ec689a92ad`. **Scope:** nonexcluded intersection/restriction mathematics and bounded Bedford–Taylor capacity-measure comparison only. No approximation/regularization or Bergman/L²/OT proof-programme work was undertaken. Such historical notes remain **deferred-by-user**, not certified.

## POME-DIVVOL-ORPHAN-EQS-001 — low / confirmed error (reading-edition display and canonicalization only)

**Evidence:** `docs/sections/divisorial-restricted-volumes/index.html`, main blob `8eb1127568e77d6d045098361c366ceeb846b909`. The intact *grouped* equations **(20.8.4)–(20.8.7)** occur at physical lines **117–120** in Theorem **20.8.3** (source `transcendental-positive-cones:42C59BDB`; permanent `8DC7DAC31FB7`). The same three formulas (20.8.5), (20.8.6), (20.8.7) are rendered **again**, outside that group, in three standalone reading chunks on **physical line 237**, each of which inserts a LaTeX `align` environment *inside* `aligned` *inside* display math. This is invalid nesting and repeats hard-coded equation numbers.

**Three independently preserved source/permanent label pairs:**

| Duplicated equation | Source label | Permanent tag | Standalone tag-page blob |
| --- | --- | --- | --- |
| 20.8.5 | `transcendental-positive-cones:694584D3` | `9788B3886ACF` | `docs/tag/9788B3886ACF/index.html` blob `d034e4609c8abc172c02b33e77c21d3b9607713f` |
| 20.8.6 | `transcendental-positive-cones:B14C7F7D` | `8B17E6C92508` | `docs/tag/8B17E6C92508/index.html` blob `f9c88ade5f1b4f817772ceb379fdd9fa3ac756b6` |
| 20.8.7 | `transcendental-positive-cones:104018FE` | `6394FCEF80E1` | `docs/tag/6394FCEF80E1/index.html` blob `cb2c5c655a20a557f19486ca52b0362e33b916b9` |

All three tag pages also contain the nested `aligned/align` sequence; they are not merely misplaced hyperlinks on the section page. This defect is **not a counterexample to the volume formulas or Theorem 20.8.3**. It is separate from prior orphan-equation findings in other sections and must not be conflated with them.

**Proposed repair, NOT applied:** in a separately reviewed reading/canonicalization patch, preserve the grouped formulas and all three source labels, independent permanent permalinks and provenance, but make the independent tag pages link to the corresponding grouped equation rows rather than emitting a second malformed and hard-numbered display. Verify responsive rendering and anchor destinations before publication. The current audit branch contains no published HTML or registry edits. **Affected:** equation navigation, reader mathematical display, cross-reference stability for Theorem 20.8.3, Eqs. 20.8.5–7.

## POME-DIVVOL-P2CENTRAL-FIBER-001 — low / verified conditional deduction (exact ample model, not a complete theorem proof)

**The mathematical test:** Theorem **20.8.3**, same source/permanent labels as above, physical lines **63–68** and the proof's volume equations **117–140, 157–160, 227–233**. The proof invokes substantial Legendre, non-pluripolar and restricted-mass inputs, which are **not certified here**. We independently test *all* of its central-fiber formulas and the derivative in a fully explicit algebraic situation.

Take (X=\mathbb P^2), (Y=H\simeq\mathbb P^1) a hyperplane, (\alpha=aH), with (0<c<a), (b>c+1). On (M=\operatorname{Bl}_{Y\times\{0\}}(\mathbb P^2\times\mathbb P^1)) let (A,B) be the pullbacks of the hyperplane class and base-point class and let (E) be the exceptional divisor. Let (F=X'+E=B) be the total central fiber and (\beta=aA+bB-cE). This is an ample toric class when (a,b>c>0): the star subdivision truncates the normal crossing intersection of the (A)- and (B)-facets by a distance (c), strictly less than both widths (alternatively check the torus-invariant curve intersections). Thus its volume and its ample restrictions are ordinary intersection numbers. The strict transform (X'\simeq\mathbb P^2).

The normal bundle of (Y\times\{0\}) in (\mathbb P^2\times\mathbb P^1) is (N\simeq\mathcal O_{\mathbb P^1}(1)\oplus\mathcal O_{\mathbb P^1}). Write (h=A|_E), (\zeta=c_1(\mathcal O_{\mathbb P(N)}(1))) **in the lines convention**. Then (E|_E=-\zeta), (h^2=0), (\zeta^2=-h\zeta), and (\int_E h\zeta=1). Consequently
[
 A^2B=1,\quad AE^2=-1,\quad BE^2=0,\quad E^3=-1,
]
where the other degree-three terms except (A^2B) vanish. The sign (E^3=-1) follows directly from (E|_E=-\zeta) and (\zeta^2=-h\zeta), avoiding a convention-dependent pushforward formula. Therefore
[
 \operatorname{Vol}(\beta)=\beta^3=3a^2b-3ac^2+c^3.
]
This agrees **exactly** with the right side of the printed (20.8.4):
[
 3\left[(b-c)a^2+\int_0^c(a-t)^2\,dt\right]
 =3a^2b-3ac^2+c^3.
]
Moreover (\beta|_{X'}=(a-c)H) and (\beta|_E=ah+c\zeta), so the two central restricted volumes are
[
 \operatorname{Vol}_{M|X'}(\beta)=(a-c)^2,
 \qquad
 \operatorname{Vol}_{M|E}(\beta)=(ah+c\zeta)^2=2ac-c^2
   =2\int_0^c(a-t)\,dt.
]
These match (20.8.6) and (20.8.7); the generic-fiber restricted volume is (a^2), matching (20.8.5). Their sum is **exactly** (a^2=\operatorname{Vol}(\alpha)), matching (20.8.8). Replacing (b) by (b-1) computes (\operatorname{Vol}(\beta)-\operatorname{Vol}(\beta-F)=3a^2), as used in lines 157–160. Finally (\operatorname{Vol}(aH+tH)=(a+t)^2), hence the derivative is (2a=2\operatorname{Vol}_{X|Y}(aH)), exactly the (n=2) case of Theorem 20.8.3.

At the integral point (a=2,b=3,c=1), the test gives (\operatorname{Vol}(\beta)=31), (\operatorname{Vol}(\beta-F)=19), central restricted volumes **1 and 3**, total **4**, and derivative **4**. All values are nonnegative and agree with the printed normalizations.

**Decision:** a **complete independent intersection calculation for this ample model only**, not a certification of the theorem for arbitrary big classes, arbitrary divisors, analytic regularization, or arbitrary non-pluripolar products. The printed volume theorem is not shown false and requires no mathematical correction. **Dependents:** Theorem 20.8.3, grouped formulas (20.8.4)–(20.8.8), its derivative normalization. Suggested optional note: the elementary blowup computation as a consistency check; retain original attribution and permanent tags.

## Separate genuinely new selected passage: local energy/capacity continuity

Directly inspected `docs/sections/bedford-taylor-products-and-local-capacity--local-energy-moments/index.html`, main blob `e619f7aa95f80ce11aa676193b054db3180e59d4`:

- **Lemma 7.11.18**, source `foundations-of-pluripotential-theory:7C182C45`, permanent `E1A777307E3D`, physical lines **355–381**: the compactly supported telescoping current and cutoff-Stokes identity justify equality of the two locally bounded Bedford–Taylor total masses, provided the existing product symmetry and locality are available.
- **Lemma 7.11.19**, source `foundations-of-pluripotential-theory:2F603F4B`, permanent `546063653198`, lines **385–423**: equality of total masses after level truncation, the precise Chebyshev (T^{-p}) tail, and the factor-two total variation bound were checked as local deductions, conditional on the previous lemma and bounded BT locality.
- **Lemma 7.11.27**, source `foundations-of-pluripotential-theory:CA871C5F`, permanent `A2369B2DB317`, lines **556–606**: the common compact support gives tightness, the Portmanteau inequality on open sets transfers the uniform capacity modulus, a Tietze extension yields fixed quasi-continuous-weight convergence, and an (L^1) small-bad-capacity estimate transfers it to varying bounded weights. The level-set limit explicitly requires (\nu(\{f=c\})=0); this hypothesis was retained. No new adjudicated error in these selected steps and no complete proof-chain certification.

This passage is *new incremental selected coverage*, not a claim of first §7.11 contact or entire-section verification; earlier §7.11.2/.5/.9/.30/.33/.38 audits remain in place. The explicit regularization-dependent steps inside §20.8.1/.2 were noted as dependencies and **not** audited.

## Tracking and limitations

Coverage remains **25 current ToC chapters, 747 numbered sections, zero fully mathematically certified sections**. This run inspected specified proof steps and one independent ample blowup model, **not** the entire project. All older confirmed errors, gaps, external inputs, open/closed ledger dispositions and user-deferred approximation work are preserved. The three malformed tag-page payloads were read for comparison; **none** were edited. No project tests, build, formalization, CI, publication, production-main, source, canonical registry, or permanent-tag changes. Existing PR #9 is already merged/closed; no new PR or issue is necessary for these audit-only notes.
