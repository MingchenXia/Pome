# Test-curve Choquet selection: invalid dead slices and a precise rational-slice repair

**Audit date:** 30 October 2026 (Asia/Shanghai). **Pinned production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit-only branch:** `review/mathematical-audit`. **Scope:** a new proof-level check of §17.15.20–31 (increasing nets, finite joins, and countable reduction), crosschecked with §17.12.1–6 and §5.14.3; independent first selected checks of the Hessian-capacity/locality passages in §§8.11–8.12. No chapter or complete dependency chain is certified.

## Finding POME-TC-CHOQUET-DEAD-SLICES-001

**Severity:** low to medium (invalid invocation of a prerequisite, but a local exact correction is available). **Status:** **proof gap** in the printed proof of Proposition 17.15.31; **not a counterexample to its statement**. The repair below is a **verified conditional repair**, proposed but **not integrated**. It depends on the existing Choquet selection result §5.14.3 and on the test-curve continuity statement §17.12.5; their entire transitive proof graphs have not been recertified. In particular, the separate earlier `POME-CHOQUET-TOPOLOGICAL-REPAIR-001` already proposes an internal proof of the **different** foundational Choquet lemma and is **not** being relogged.

### Exact integrated anchors and hypotheses

- Main file `docs/sections/test-curves--operations-on-test-curves/index.html`, **blob `3da617be8f58713f764d49ba22f49b803149a5e8`**, Proposition **17.15.31**, source `sgpt:6B576942`, permanent tag **`4B67ABC0083D`**, physical lines **662–713**; the invalid family inclusion is at **680–684**, the consequent application and selection at **686–704**, and the final mass-continuity argument at **705–713**. Definition 17.15.25, source `sgpt:BD3ECA71`, permanent `FA768FFB9E17`, lines **591–614**; finite join Corollary 17.15.17, permanent `C8D1BA787705`, and increasing-supremum Proposition 17.15.22, source `sgpt:7C36CCDA`, permanent `88665EBBD399`, lines **529–565**.
- Main file `docs/sections/test-curves--the-notion-of-test-curves/index.html`, **blob `6dfdfc2b5e599eb3a19a9558a9c963e79df71dc7`**: Definition **17.12.1**, source `sgpt:ECCF19D5`, permanent `C8399F09D86D`, lines **10–36**; Remark **17.12.3**, source `sgpt:FCDC9660`, permanent `3D73AB2E32CB`, lines **42–47**; Equation **17.12.5**, source `sgpt:07C41068`, permanent `5EFADBE6069E`, lines **71–79**; Lemma **17.12.6**, permanent `348ACDBCB24E`, lines **82–105**.
- Main file `docs/sections/plurisubharmonic-functions--properties-of-plurisubharmonic-functions/index.html`, **blob `e7d871122eca3eb7416ab8a993063cdc8d3987f3`**, Choquet Proposition **5.14.3**, source `sgpt:BAE53833`, permanent `1D624ECF05E9`, lines **48–59**. That proposition requires a **nonempty family of actual psh functions** locally uniformly bounded above; it is not stated for an arbitrary family containing identically `-infinity` slices.

The standing hypotheses of §17.15 are: connected compact Kähler `X`; a smooth real closed `theta` in a big class; a nonempty collection `(Gamma^i)_{i in I}` of positive-mass test curves; and `M:=sup_i Gamma^i_max<infinity`. By §17.12.3, each curve is extended by **identically `-infinity` for every `tau>Gamma_max`**, while its value **at** `tau=Gamma_max` is the indicated decreasing limit in `PSH(X,theta)`. These are different endpoint cases.

### Exact failure of the printed proof step

At lines 680–684 the proof applies §5.14.3, for **each rational `q<M`**, to the purported family
```text
{ (bigvee_{j in J} Gamma^j)_q : J in Fin(I) } subset PSH(X,theta).
```
That displayed **set inclusion is false** whenever the family contains a finite subset `J` with `max_{j in J} Gamma^j_max<q`: its join is a test curve whose `q`-slice, by the stated extension convention, is identically `-infinity`, which is not a member of the psh family required by §5.14.3. The global condition `q<M` guarantees **some** live finite joins, not that **every** finite join is live.

A concrete counterexample to this *proof assertion* uses `X=P^1`, `theta=omega_FS`, and the simple normalized model test curves `Gamma^b_tau=0` for `tau<b`, extended as in §17.12.3, with `b=0` and `b=2`. Each is legitimate (the zero potential is a positive-mass model, with a constant decreasing/concave profile below its terminal parameter). Let `I={0,2}`, so `M=2`, and choose the rational `q=1`. The singleton `J={0}` belongs to `Fin(I)`, but
```text
(bigvee_{j in {0}} Gamma^j)_1 = Gamma^0_1 = -infinity,
```
while the singleton `J={2}` has `q`-slice `0`. Thus the printed family is *not* a subset of `PSH(X,theta)`. No false conclusion of Proposition 17.15.31 follows: its countability assertion is true in this two-element example, and the failure is solely the unqualified prerequisite invocation.

### Complete local correction of this step and the final reduction

For each rational `q<M` define
```text
Fin_q(I) = { nonempty finite J subset I : b_J := max_{j in J} Gamma^j_max >= q }.
```
This family is **nonempty**, since `q<M` gives an index with terminal parameter strictly greater than `q`. For every `J in Fin_q(I)`, the finite join `Gamma^J := bigvee_{j in J} Gamma^j` has terminal parameter `b_J>=q`. If `q<b_J`, its `q`-slice lies in `PSH(X,theta)` by the test-curve definition. If `q=b_J`, the slice also lies in `PSH(X,theta)` by **the endpoint clause of Remark 17.12.3**. All those slices are bounded above by zero (including endpoint limits), so Choquet's lemma applies to this **nonempty, uniformly upper-bounded family** (using local smooth `theta`-potentials to pass from quasi-psh to psh in charts).

The omitted finite subsets, those with `b_J<q`, contribute identically `-infinity`. They have **no effect** on the upper semicontinuous regularized supremum. Accordingly the original equality on line 689 follows with a countable selected subfamily `J'_q subset Fin_q(I)`. Retain the printed countable union
```text
I' = union_{q rational, q<M} union_{J in J'_q} J.
```
Monotonicity of finite joins gives equality of the resulting `q`-slices for every rational `q<M`. The selected family has the **same terminal supremum** `M`: otherwise, if `M':=sup_{i in I'}Gamma^i_max<M`, choose a rational `q` with `M'<q<M`. Then the selected supremum has `q`-slice identically `-infinity`, but the full family has a live positive-mass test-curve slice, contradiction.

There is also a shorter replacement for the final mass-continuity step. With both terminal suprema equal to `M` and equality on all rational slices, choose for any real `tau<M` a rational sequence `q_k ↑ tau`. The **already printed** left-continuity identity Eq. **17.12.5** gives, as equality of normalized psh potentials,
```text
Gamma_tau = inf_k Gamma_{q_k} = inf_k Gamma'_{q_k} = Gamma'_tau.
```
This proves the complete test-curve identity **without** an additional appeal here to §16.8.7 or to continuity of the nonlinear Monge–Ampère mass §17.12.9. The last shortcut is conditional on §17.12.5, which the reading edition supplies; its proof chain has not been newly certified.

**Recommended source-safe patch:** at lines 680–686 replace `Fin(I)` by `Fin_q(I)` with the definition, nonemptiness, endpoint `q=b_J` explanation, and the observation that discarded joins equal `-infinity`; optionally replace lines 704–713 with the rational left-continuity argument. Preserve the permanent tag/source label and the original attributed results. This should be submitted as a separately reviewable source/reading-edition patch; this audit does **not** edit production.

**Dependents and risk:** §17.15.25–31 countable envelope constructions; test-curve operations and subsequent §17.15.32–35 identities, §17.17 Legendre/test-curve constructions, and §22.1 non-Archimedean uses **to the extent they invoke** the countable reduction. This is a proof gap with an explicit valid local repair, **not a disproof of Choquet selection**, not a certified theorem-level patch in `main`.

## Independent breadth check: §§8.11–8.12 (no additional error asserted)

Directly sampled `docs/sections/complex-hessian-equations--local-capacities-and-decreasing-products/index.html` (main blob `115d285f6b1f76d284463c396e7e87db2b9dbdc3`), Lemma **8.11.1** lines **20–47** (bounded local mixed masses and gradient), Lemma **8.11.4** source `non-kahler-pluripotential-theory:E67F97DC`, permanent `9AF7CFAD9A0B`, lines **75–115** (weighted Hermitian torsion/Cauchy–Schwarz), and selected steps of Proposition **8.11.6**, Lemma **8.11.11**, Theorem **8.11.12**. Compared `docs/sections/complex-hessian-equations--locality-and-maxima-of-bounded-potentials/index.html` (main blob `8750df56019c14e16704607ca20fa8b90f137fb0`), the strict-max locality **8.12.1**, contact-set inequality **8.12.2**, and bounded positive-mass argument **8.12.5**, to locate their capacity and weighted-limit prerequisites.

A tempting objection to Lemma 8.11.4 is the exponent `omega^(n-q-2)` at `q=m-1`. **This is not an error under the actual chapter hypotheses.** The current Chapter 8 introduction, `docs/sections/complex-hessian-equations/index.html`, main blob `5331b937ccdaba51f1ec006d5e72dc84f7addfbf`, **line 7**, fixes **`2 <= m < n`**, so `q <= m-1 <= n-2` and `n-q-2 >= 0`. The hypothetical `m=n` negative-power objection would ignore an explicit standing hypothesis and must **not** be logged as a defect. These were **selected proof-step inspections**, not complete certifications of the Hessian current construction or all mass/capacity convergence arguments.

## Scope, disposition and exclusions

This pass newly inspected **selected §17.15.20/.22/.25/.28/.31 and §§17.12.1/.3/.5/.6** plus the indicated first **§§8.11–8.12** proof steps, and crosschecked §5.14.3's actual invocation. It does not assert complete proof verification of any entire section. **25 current chapters / 747 numbered ToC sections / zero full mathematical section certifications**. Prior ledger statuses, external dependencies and historical notes remain unchanged. In particular, the complete Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**, untouched here. No production main, original sources, reading body, registry, canonical tags, CI, build, website or formalization changes were made.
