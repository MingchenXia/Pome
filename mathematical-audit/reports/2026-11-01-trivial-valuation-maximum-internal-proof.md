# 2026-11-01: an internal trivial-valuation maximum principle, with independent Hessian and Okounkov proof checks

**Pinned production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Audit branch:** `review/mathematical-audit`. **Scope:** nonexcluded mathematics only. Demailly approximation/regularization, the dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme is strictly **deferred-by-user**, not reviewed or resolved in this pass.

## POME-NA-TRIVIAL-VALUATION-MAX-001

**Severity:** low. **Status:** **verified repair of a specific external proof step**, proposed for later review; **not** an independently certified proof of the whole lemma, the NA comparison theorem, or the global construction of psh metrics.

**Source and permanent anchors.** Production reading edition `docs/sections/non-archimedean-pluripotential-theory/index.html`, blob `8448d710690ebe1cc28040f9611d05c9d008a961`:
- §22.1.70, generically finite Fubini–Study formula, lines 1173–1185, source section `sgpt:178E4884`, section tag `3CE1C3E79114`; its **legacy displayed equation number 13.37** was already reported as `POME-NA-FS-STALE-EQUATION-LABEL-001` and is **not a new finding**.
- Definition 22.1.71, source `sgpt:DAC17F2D`, permanent `EEADED50AAC3`, line 1189: psh functions are pointwise **decreasing directed-net** limits of rational generically finite Fubini–Study functions, allowing varying line bundles `L_i`.
- Lemma 22.1.116, source `sgpt:657B916D`, permanent `1861C279EAB7`, lines 1814–1842, especially the first proof paragraph at line 1833, which cites the external BJ22 Lemma 1.4(i) maximum principle to identify conditions (1) and (2).

**Exact claim.** Let `Y` be an irreducible closed subvariety of the projective `X`, and let `v_{Y,triv}` be the trivial valuation of `C(Y)`, considered as a point of `Y^An`. For every `\phi\in PSH(L^An)`, in the precise sense of Definition 22.1.71, and every valuation/semivaluation `v\in Y^An`,
```math
\phi(v)\le \phi(v_{Y,\mathrm{triv}}).
```
The inequality is in the extended real numbers and includes the case when both sides are `-infinity`. In particular,
```math
\phi(v_{Y,\mathrm{triv}})>-\infty
\quad\Longleftrightarrow\quad
\phi|_{Y^{\mathrm{An}}}\not\equiv-\infty.
```
The right-hand implication is immediate because the trivial valuation itself belongs to the domain; the other implication follows from the inequality.

**Proof, without the cited BJ22 maximum principle.** First take one generically finite rational Fubini–Study function
```math
\phi_i(v)=\frac1{m_i}\max_{1\le j\le N_i}
\{\lambda_{ij}-v(s_{ij})\},
\qquad s_{ij}\in H^0(X,L_i^{m_i})\setminus\{0\}.
```
Set `J_i(Y)=\{j:s_{ij}|_Y\not\equiv0\}`. For `j\notin J_i(Y)`, the restricted section is identically zero, so its logarithmic norm equals `-infinity` at *every* point of `Y^An`; that term never contributes. For `j\in J_i(Y)`, choose a local regular trivialization near the center of `v` on `Y`. The restricted section is a regular local function, and a valuation with center on `Y` is nonnegative on the local ring, hence `v(s_{ij}|_Y)\ge0`. Transition functions are units and have valuation zero, so this inequality is independent of the chosen frame. At the generic trivial valuation `v_{Y,triv}`, the same nonzero rational section has valuation zero. Therefore
```math
\phi_i(v)
=\frac1{m_i}\max_{j\in J_i(Y)}
 \bigl(\lambda_{ij}-v(s_{ij}|_Y)\bigr)
\le\frac1{m_i}\max_{j\in J_i(Y)}\lambda_{ij}
=\phi_i(v_{Y,\mathrm{triv}}).
```
If `J_i(Y)` is empty, both sides are `-infinity` by convention, so the same inequality holds. This argument uses no positivity of `L_i`, only the regularity of its global sections and the valuation convention `\log|s|(v)=-v(s)` printed at §22.1.70.

Now write `\phi=\inf_{i\in I}\phi_i` pointwise using Definition 22.1.71. The displayed inequality holds **for every** index `i`; taking infima of both sides gives
```math
\phi(v)=\inf_i\phi_i(v)
\le\inf_i\phi_i(v_{Y,\mathrm{triv}})
=\phi(v_{Y,\mathrm{triv}}).
```
This directly handles the **original arbitrary directed net**, including approximants on varying `L_i`. There is no appeal to a sequential compactness theorem or interchange of two limiting operations. This proves precisely the maximum-principle step required by (1) \(\Leftrightarrow\) (2) of Lemma 22.1.116.

**Dependency boundary and proposed action.** The algebraic proof above starts from the *integrated* Definition 22.1.71 and Fubini–Study valuation convention; no additional external BJ22 maximum principle, BJ22 decreasing-sequence theorem 22.1.75, or regularization theorem is required for this **specific step**. When applying it to `\Gamma^{An}` in Lemma 22.1.116, the identification `\Gamma^{An}\in PSH(L^{An})` continues to depend on the earlier comparison/bijection Theorem 22.1.111 (source `sgpt:0558A92C`, permanent `9B811DBD89E3`, lines 1678–1722), **not certified in this pass**. The separate implication (1) \(\Leftrightarrow\) (3) at lines 1835–1841, involving generic Lelong numbers and the nontrivial trace condition, is **not repaired or recertified here**. Proposed future source/body patch: replace only the invoked maximum-principle step at line 1833 with the finite-max/net proof above, while preserving BJ22 historical attribution elsewhere. No production source, registry, permanent tag or published documentation was altered.

**Affected dependents:** Theorem 22.1.113 (`sgpt:331B39A3`, permanent `D613676A36CA`), which cites Lemma 22.1.116 at lines 1742 and 1762 in its restriction/analytification argument. This repair does not certify the other steps of Theorem 22.1.113.

## Independent fresh coverage without a new error claim

**Complex Hessian equations §8.3, previously unreviewed proof segment:** directly inspected
`docs/sections/complex-hessian-equations--liouville-and-gradient-estimates/index.html`, main blob `74cda06ad4bf75ab5fcba6e841c9ad4aa9424981`, Lemma 8.3.1 (`non-kahler-pluripotential-theory:88E13750`, permanent `89F810E43B3E`, lines 19–30), bounded-Lipschitz maximal Liouville Theorem 8.3.2 (source `:32D9A170`, permanent `96D01E7C4F0F`, lines 33–107), and gradient Proposition 8.3.3 (source `:A456C079`, permanent `B863BB49A505`, lines 112–153). Checked the directions of the lower-test comparison, the `m<n` cone slice identity, the `v^2` nonnegative-subharmonic argument, and the rescaled Hessian-density power `R_j^{-2m}`; these **selected steps did not reveal a confirmed error**. The full induction, external scalar elliptic estimates and all upstream cone facts are **not independently certified**. No new theorem or repair ID is assigned to this contextual inspection.

**Okounkov almost semigroups §19.7, previously unreviewed selected passage:** directly inspected `docs/sections/almost-semigroups/index.html`, main blob `33898b2963ad0f8b7e30bf414276642f60925b74`: Lemma 19.7.29 (`sgpt:688D7503`, permanent `B63FC87B8DDF`, lines 477–525) and Theorem 19.7.32 (`sgpt:ED83BFDD`, permanent `1551B679B8B7`, lines 535–658). Checked the positive-volume requirement for decreasing intersections, nested cone-slice identity, compact Hausdorff subsequence argument and the use of **sequences** (not general nets) for the stated metric completion. The foundational semigroup metric and volume lemmas 19.2.5, 19.7.19, 19.7.25–27 remain conditional inputs; no claim that the whole extension theorem was proved anew.

**Coverage discipline:** this report adds a **new internal proof of one externally quoted step** in §22.1.116 and selected new line-level inspections in §8.3 and §19.7.29/.32, rather than claiming three complete sections. Current actual ToC: **25 chapters, 747 numbered sections, zero fully mathematically certified sections**. Existing ledger errors, proof gaps, external inputs, deferred-by-user entries, and all previous source/tag conventions remain unchanged. No builds, CI, formalization checks, website publication, source integration or tests were run.
