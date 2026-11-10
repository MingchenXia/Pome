> **AUDIT CORRECTION (2026-11-10, `POME-GAUD-ROOT-SCOPE-AUDIT-RECLASS-001`):** The former `POME-GAUDUCHON-N1-POSITIVE-ROOT-001` was **incorrectly classified as a confirmed source error**. §11.3, line 7, supplies the standing `n>=2` hypothesis governing §§11.4/11.6; §11.6.3 alone explicitly extends its lemma to `n=1`. The counterexamples in the original note concern an **unasserted extension**, not the printed root statement. The original mathematical note remains below as superseded historical material, **not an active confirmed error**. [Full correction](../reports/2026-11-10-gauduchon-chapter-scope-reclassification.md). No production patch is required.

---

# The one-dimensional exception to the positive Gauduchon-root assertion

- **Finding:** `POME-GAUDUCHON-N1-POSITIVE-ROOT-001`
- **Classification:** **low / confirmed error (auxiliary assertion; not a false theorem)**.
- **Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated reading edition:** `docs/sections/gauduchon-metrics-and-linear-mass--the-gauduchon-criterion-for-positivity/index.html`, blob `6dd43b62800206fb0302fd4261372d7882e5170d`.
- **Precise anchor:** §11.6, physical lines **23–30**: unqualified claim that every smooth strictly positive `(n-1,n-1)` form has a **unique** positive `(1,1)` root, and formula with exponent `1/(n-1)`. The following proof of Theorem 11.6.1 appeals to this claim at physical line **41**.
- **Stable provenance:** §11.6 source `non-kahler-pluripotential-theory:8909D36D`, section permanent tag `6029C37CE10F`; Theorem 11.6.1 source `non-kahler-pluripotential-theory:87DC00D0`, permanent tag `88BE3B63D9E5` (physical lines **10–19, 34–79**). For scope and dependents, Corollary 11.6.2 source/permanent `non-kahler-pluripotential-theory:EAE0F4AE/F83E15A1F529` (lines **84–98**), and Lemma 11.6.3 `non-kahler-pluripotential-theory:DC67F892/91B8C8A3C10E` (lines **104–117**, explicitly including `n=1`). Chapter 11 actual ToC §11.6 title: *The Gauduchon criterion for positivity*.

## Confirmed false auxiliary assertion

The reading edition allows complex dimension `n=1`; the nearby Lemma 11.6.3 explicitly discusses that case. On any connected compact Riemann surface `X`, a smooth strictly positive `(n-1,n-1)=(0,0)` form is a smooth positive real function. Take `Gamma=2`. It is strictly positive and `dd^c Gamma=0`. Nevertheless, for **every** positive Hermitian `(1,1)` form `gamma` we have `gamma^(n-1)=gamma^0=1`, not `2`. Hence existence of the asserted root fails.

For `Gamma=1` the opposite defect occurs: `gamma^0=1` for **every** positive Hermitian `gamma`, so uniqueness fails. The displayed eigenvalue formula `lambda_i=(prod_j g_j)^(1/(n-1))/g_i` is undefined at `n=1`. This is a literal counterexample to the unqualified explanatory claim in lines 23–30, **not** a counterexample to Theorem 11.6.1, Corollary 11.6.2, or Lemma 11.6.3.

For `n>=2`, the adjugate/determinant positive-matrix root construction is well-defined and the stated root uniqueness is valid. No change to that case is proposed.

## Independent dimension-one repair of the theorem's exact missing bridge

Let `X` be a **connected compact Riemann surface** and `theta` a smooth real `(1,1)` form. Condition (ii) of Theorem 11.6.1 is simply
`int_X theta >= 0`: every positive Hermitian metric `gamma` is Gauduchon in dimension one and `gamma^0=1`. On the other hand, if `u` is `theta`-psh, positivity of `theta+dd^c u` and Stokes give `int_X theta>=0`. This is necessity.

For sufficiency, choose a smooth strictly positive `omega` and put
`a=(int_X theta)/(int_X omega)>=0`. Since `int_X (theta-a omega)=0`, the compact connected surface Poisson equation has a smooth real solution `f`, unique up to constant, of
`dd^c f=theta-a omega`. This follows directly by writing both sides in units of `omega`, using the scalar elliptic Laplacian and its constants-only kernel/cokernel (equivalently, the mean-zero Fredholm alternative already used at §11.6, lines 55–66). With `u=-f`,
`theta+dd^c u=a omega>=0`. Thus Theorem 11.6.1 **is true for n=1**, despite the false root assertion.

Alternatively, retain the existing Hahn–Banach proof with a separate `n=1` sentence: a smooth `dd^c`-closed `(0,0)` form on connected compact `X` is a **constant** `c`, and if it is strictly positive then `c>0`. Every such `Gamma=c` is a positive **scalar multiple**, not the zeroth power of a metric. The hypothesis `int_X theta>=0` implies `ell(c)=c int_X theta>=0` on the positive cone `E`, which is **exactly** what the extension argument needs. The current construction then goes through unchanged. For `n>=2` use the original unique positive root formula.

At `n=1` the dependent threshold is explicitly
`kappa_omega(theta)=(int_X theta)/(int_X omega)`, and **every** Gauduchon metric attains the displayed infimum: its ratio does not depend on `gamma`. Moreover `theta-kappa_omega(theta)omega=dd^c f`, consistent with the last paragraph of §11.6. Thus the proposed repair preserves Corollary 11.6.2 and Lemma 11.6.3 verbatim.

## Proposed source-body correction (NOT APPLIED)

Replace the start of the positive-root paragraph, lines 23–30, by:
> If `n>=2`, every smooth strictly positive `(n-1,n-1)` form has a unique smooth strictly positive `(1,1)` root; the following eigenvalue formula proves this. If `n=1`, the positive `dd^c`-closed `(0,0)` tests are exactly the positive constants; their nonnegative `theta`-pairings are equivalent to `int_X theta>=0`. This is enough for the separation proof, without a root.

Keep the `n>=2` spectral formula, the provenance/attribution, permanent tags and the theorem statement. This is a **proposed** edit only; no mathematical body or permanent tag has been changed in this audit. The dimension-one fix is independently justified above and requires no user-deferred regularization/Bergman/L²/OT/multiscale/positivity-loss programme.

## Exact scope and unresolved inputs

- **Newly checked:** the full displayed hypotheses of Theorem 11.6.1, root paragraph, the exact use of the root at line 41, the scalar dimension-one Poisson repair, the dependent threshold statement and explicit `n=1` clause of Lemma 11.6.3. A direct elementary counterexample certifies the auxiliary assertion as false.
- **Not claimed:** an independent proof of the general `n>=2` Hahn–Banach/Fredholm current construction or the global proof chain from §11.4.2/§11.5.1/§5.22.2; no formal verification, tests, build, or entire §11.6 certification.
- **Affected dependents:** only the proof bridge from Gauduchon tests to positive `dd^c`-closed tests for `n=1` in Theorem 11.6.1, subsequently invoked by Corollary 11.6.2 and applications of the generalized Lamari criterion in dimension one. The printed main theorems remain correct.
- **Prior audit coverage:** §11.6 was already selected in earlier audit work (including smooth-minimizer tests); this report adds a *new* checked claim, **not** a first visit. Full-section certifications remain zero.
- **Deferred:** all user-excluded Demailly approximation/regularization and dedicated Bergman, weighted-L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion investigations stay `deferred-by-user`, not resolved.
