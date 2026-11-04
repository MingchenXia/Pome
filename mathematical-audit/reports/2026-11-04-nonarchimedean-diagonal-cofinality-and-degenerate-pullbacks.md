# Non-Archimedean inverse limits: the Kähler diagonal and the semipositive boundary

**Date:** 2026-11-04. **Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Scope:** selected integrated proof at §22.1.14–19 and the exact statement (not a reproof) of §16.4.4. This is a new argument-level inspection of early §22.1; §22.1 was already partly audited elsewhere, and no whole section is certified.

## Stable source anchors

- `docs/sections/non-archimedean-pluripotential-theory/index.html`, blob `8448d710690ebe1cc28040f9611d05c9d008a961`: Definition **22.1.14**, source `sgpt:5A9D4C43`, permanent `CCAAC9DA4E2F`, physical lines **256–264**.
- Same file: Proposition **22.1.15**, source `sgpt:176139CE`, permanent `3943AA7119C5`, and Equation **22.1.16**, source `sgpt:40CA45E4`, permanent `29D3530031C6`, physical lines **268–308**, especially compatibility requirements **280–304**.
- Same file: Proposition **22.1.17**, source `sgpt:D30D14E9`, permanent `817C1BB3E570`, Equation **22.1.18**, source `sgpt:14615434`, permanent `258B0F2A2F95`, physical lines **312–319** (including the source footnote that the enlarged indexing poset is *not* directed).
- Same file: Corollary **22.1.19**, source `sgpt:93D7BBCD`, permanent `347399E47277`, physical lines **323–337**.
- Upstream proposition **16.4.4**, source `sgpt:DE839E2D`, permanent `048490BEAC8C`, published reading entry `docs/tag/048490BEAC8C/index.html`, blob `9e66a1fbda45995c256b709f91a6c505e6a15717`. Its decreasing-net mass/divisorial-continuity assertion was read as a *stated dependency*, not mathematically re-certified.

## Finding POME-NA-DIAGONAL-KAHLER-COFINALITY-001

**Severity:** low. **Status:** verified conditional deduction; no false original statement. **Affected theorem:** Proposition 22.1.15, whose printed proof presents an inverse by the half-diagonal.

Write `K` for the collection of Kähler forms. All comparisons of forms in this report are pointwise. The indexing order in the reading edition is the reverse of the usual form order, and the transition maps run from `theta+a` to `theta+b` when `b >= a`. Consider any compatible two-parameter family
`B(a,b) in PSH^NA(X,theta+a+b)_{>0}`, with separate transitions in the two variables exactly as displayed in the three compatibility bullets at lines 280–296.

**Claim (precise cofinal-diagonal statement).** The family `C(e)=B(e/2,e/2)` for `e in K` is a compatible one-parameter family and uniquely determines the entire two-parameter family. Conversely any one-parameter compatible family determines the two-parameter family through `B(a,b)=C(a+b)`. In particular the proposed inverse in line 304 of the reading edition is correct under its stated compatibility of the transition maps.

**Proof.** For every finite collection of Kähler forms `a_1,...,a_r`, choose a fixed Kähler form `rho`. Compactness of `X` and strict positivity give `delta>0` such that `delta rho <= a_j` for all `j`. Consequently the diagonal subsystem `{(delta rho,delta rho)}` is cofinal in `K x K` for the reverse form order: for any `(a,b)`, one can choose `kappa` with `kappa <= a,b`. These inequalities also imply `kappa <= (a+b)/2`.

The prescribed transitions in each coordinate commute: starting at `B(kappa,kappa)`, adding `a-kappa` in the first coordinate and then `b-kappa` in the second gives `B(a,b)`; the opposite path gives the same component by the two compatibility conditions. Taking `e=a+b`, the two coordinate transitions from `B(kappa,kappa)` to `B(e/2,e/2)` give `C(e)`. Both paths increase the total background from `theta+2kappa` to `theta+a+b`. Functoriality of the `I`-envelope transition map (the already cited Proposition 17.14.6, *conditional internal input*) makes their resulting values equal. Thus `B(a,b)=C(a+b)` for every `a,b`. In the other direction, `C(e)=B(e/2,e/2)` plainly preserves transitions because each of the two half-parameters increases when `e` increases. These constructions are mutually inverse. The argument works for arbitrary indexed families and never extracts a sequence or interchanges limits. QED.

This formal argument does **not** independently verify analytic existence, uniqueness or functoriality of `I`-envelopes: those are internal hypotheses of the cited construction. It verifies the missing explicit index-category portion of Proposition 22.1.15, not the entire Non-Archimedean theorem.

**Proposed optional edit:** replace the terse surjectivity closure at lines 301–307 with the two-path comparison through any `kappa <= a,b`; retain source attribution and permanent tags unchanged.

## Finding POME-NA-SEMIPOSITIVE-NONCOFINALITY-001

**Severity:** low, but important as a proof-scope guard. **Status:** verified conditional deduction (counterexample to an *unprinted indexing shortcut*), **not** a disproof or a confirmed gap in Proposition 22.1.17. **Affected dependencies:** Proposition 22.1.17, its Equation 22.1.18 and Corollary 22.1.19.

Proposition 22.1.17 also uses the much larger index class `S` of *smooth closed semipositive* (1,1)-forms with `int_X eta^n>0`. It cannot be proved merely by the cofinal Kähler-diagonal argument above.

**Explicit counterexample to the needed cofinality.** Let `X=P^1`, let `omega_FS` be the Fubini–Study form, and choose a smooth nonnegative function `f` which is nonzero somewhere and vanishes at a point `p`. Then `eta=f omega_FS` is a smooth **closed** semipositive (1,1)-form: closedness is automatic on the real two-dimensional manifold `P^1`. Its total volume `int_X eta>0`, so `eta in S`. But there is **no** Kähler form `kappa` with `kappa<=eta`, since evaluating at `p` would give the contradiction `0<kappa_p<=eta_p=0`. Therefore `K` is not cofinal in `S` for the inverse-system order used in §22.1.

The obstruction also occurs in the precise geometric situation of Corollary 22.1.19. Let `pi:Y=Bl_p(P^2)->P^2` be the blowup of a point. The smooth closed semipositive form `eta=pi^*omega_FS` has
`int_Y eta^2=int_{P^2}omega_FS^2>0`,
yet `eta` vanishes in every tangent direction to the exceptional curve. Again no Kähler form on `Y` can be pointwise bounded above by `eta`. The pullback of a Kähler form under a modification therefore produces exactly the non-cofinality relevant to the stated birational invariance.

**Logical consequence, precisely delimited.** The proof of Proposition 22.1.15 by cofinal diagonal is sound on the strictly Kähler indexing set. It does *not* by itself identify the additional semipositive positive-volume inverse limit appearing in Proposition 22.1.17. That latter equivalence requires genuine analytic **extension to a degenerate background**, not just categorical cofinality: one must reconstruct compatible positive-volume model components at `theta+eta` from the family at the Kähler perturbations `theta+eta+epsilon rho`, and justify compatibility, uniqueness and preserved volume. The reading edition cites Proposition 16.4.4 exactly at line 312; it states a decreasing-*net* envelope/mass convergence result, so this is a relevant, nonexcluded *internal* input. Its full application to all model test-curve components is not verified in this focused pass. **No false theorem and no confirmed failure of the stated proof is claimed.**

**Proposed editorial clarification:** immediately after the line-312 reference, explicitly say that the semipositive extension is an analytic continuity argument, because the Kähler subposet is not cofinal. Specify why the reconstructed test curves remain `I`-model with positive volume in the big class `theta+eta`, and cite the exact compatibility/mass lemma supplying each step. Do not silently replace a net by a sequence. An alternative is to prove a separate extension lemma before Proposition 22.1.17.

## Coverage, dependencies, and nonclaims

- **Actually reviewed now:** full printed compatibility clauses and diagonal formula of §§22.1.14–15; the sentence of proof and index-domain quantifier in §22.1.17; the pullback statement of §22.1.19; statement (not proof certification) of §16.4.4. The other ~100 statements in §22.1, including previously audited §22.1.86–89, are outside this increment.
- **Conditional upstream inputs:** functoriality of `I`-model transitions (17.14.6); decreasing-net envelopes, mass and singularity behavior (16.4.4). Internal compatibility is used exactly as printed; neither result has been independently certified here.
- **Downstream:** §22.1.19 needs the semipositive boundary stage since exceptional tangents make `pi^*omega` degenerate. Nothing here certifies birational invariance independently.
- **Inventory:** 25 chapters, 747 numbered current ToC sections, zero wholly mathematically certified sections. Both current findings are additive; prior confirmed errors, open gaps, genuine duplicates and separate proposed repairs retain their old statuses.
- **User-deferred scope untouched:** Demailly approximation/regularization, dedicated Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion remain **deferred-by-user**, not resolved or reexamined.
- **Verification performed:** reading-edition and cited entry inspection, categorical argument and two explicit geometric countermodels. **Not performed:** local project build, test suite, CI, Lean/formal verification, publication, or edits of source/body/registry/permanent tags.
