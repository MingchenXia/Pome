# Chapter-wide dimension scoping: correction of an earlier Gauduchon audit false positive

- **Stable correction ID:** `POME-GAUD-ROOT-SCOPE-AUDIT-RECLASS-001`.
- **Classification:** **medium / verified repair of an audit finding's classification**, **not** a mathematical source or proof repair. The earlier `POME-GAUDUCHON-N1-POSITIVE-ROOT-001` is **withdrawn as an in-scope confirmed error**, not silently removed.
- **Production main re-read:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Audit head before this correction:** `55d12a99b052762c0f0a9a2aede8636fbfcc75bf`.
- **Scope:** direct proof-level re-examination of §§11.3, 11.4 and 11.6, and a selected consistency check with §§12.2 and 12.11. No Demailly approximation/regularization or its excluded auxiliary programme.

## Exact current-main source anchors

| Current reading-edition path and main blob | Original source / permanent label and physical anchor | Mathematical content |
| --- | --- | --- |
| `docs/sections/conventions/index.html`; `ef778e54d8d7413242387e95c52269b3c7d42cae` | `non-kahler-pluripotential-theory:DE921263`, integrated source variant physical **line 123** | Default connected compact `X`, **`n>=1`**, subject to subsequent local assumptions. |
| `docs/sections/gauduchon-metrics-and-linear-mass/index.html`; `02d635e918120c4026c38d14119db9377eefe61f` | §11.3 source `non-kahler-pluripotential-theory:67BD8090`, permanent `1009E65ECC4C`, physical **line 7** | **“Throughout this chapter, ... `n>=2` unless a section specifies another setting.”** This is the missing prerequisite in the older audit. |
| `docs/sections/gauduchon-metrics-and-linear-mass--conformal-gauduchon-metrics/index.html`; `ecb4bf9e593dfb25f1644f0561d1aa65bf096b10` | Theorem 11.4.2 source `non-kahler-pluripotential-theory:F1B1A709`, permanent `3978AEB15BD7`, **lines 20–25**, proof **26–58** | The `rho^(1/(n-1))` construction is **within the stipulated `n>=2` setting**, not an accidental division by zero. |
| `docs/sections/gauduchon-metrics-and-linear-mass--the-gauduchon-criterion-for-positivity/index.html`; `6dd43b62800206fb0302fd4261372d7882e5170d` | §11.6 source `non-kahler-pluripotential-theory:8909D36D` / permanent `6029C37CE10F` **lines 23–30**; Theorem 11.6.1 source `:87DC00D0` / permanent `88BE3B63D9E5`, line **41** of proof | The positive `(n-1,n-1)` root claim and its spectral exponent belong to the standing **`n>=2`** case. |
| Same §11.6 blob | Lemma 11.6.3 source `non-kahler-pluripotential-theory:DC67F892` / permanent `91B8C8A3C10E`, **lines 104–117**, explicit `n=1` clause at **109** | This **lemma specifically** extends its conclusions to dimension one. The exception does *not* retroactively change the earlier theorem/root lemma's ambient hypothesis. |
| `docs/sections/a-gauduchon-variational-volume--the-quotient-and-the-smooth-equation/index.html`; `9ec67161d46b3ba20afa1b1c9a0c84f29322763e` | Theorem 12.2.3 source `non-kahler-pluripotential-theory:876DF057` / permanent `2DB664A6EFDF`, **lines 59–86** | Separately handles minimizer classification for `n>=2` and the curve case `n=1`, corroborating the intended dimensional split. |
| `docs/sections/a-gauduchon-variational-volume--nef-limits-and-nonattainment/index.html`; `086d12a65c46cfb68c7d6fe952266515ca04623b` | Theorem 12.11.1 `:F03E2CAC` / `9ECB2B21B601`, **lines 11–29**; Proposition 12.11.2 `:727E9DB2` / `854AAD5CF1CA`, **lines 42–50** | Selected independent check: monotone infimum/interchange and the positive-trace nonattainment mechanism do not require applying the root lemma at `n=1`. Previously partly reviewed, no whole-section certification. |

## Why the old 'confirmed error' does not exist in the stated domain

The prior dated report `reports/2026-11-10-gauduchon-dim1-positive-root.md` interpreted §11.6's strictly-positive complementary-form root claim as quantifying over all `n>=1`, taking the **nearby Lemma 11.6.3's explicit curve extension** as evidence that the preceding root paragraph covered curves. But §11.3, **the containing subject introduction**, restricts the entire chapter to `n>=2` unless a particular section or assertion gives an override. No such override applies to §11.6's pre-theorem positive-root paragraph or Theorem 11.6.1. The extension is explicitly attached only to Lemma 11.6.3.

The old examples at hypothetical `n=1` remain **correct calculations**: for a positive `(0,0)` form `Gamma=2` there is no positive `(1,1)` form `gamma` with `gamma^0=2`; `Gamma=1` has nonunique roots; `1/(n-1)` would be undefined. They refute **an unstated extension**, not the printed assertion under its actual inherited hypothesis. Consequently the finding `POME-GAUDUCHON-N1-POSITIVE-ROOT-001` is a **false positive**, not a source error, and its suggested mandatory text patch must be withdrawn. Its independent Poisson proof of the curve criterion remains a mathematically valid *optional extension*, not a repair of a published defect.

For completeness, the actual `n>=2` positive-matrix root step can be checked directly. In an oriented unitary frame write `G>0` for the Hermitian complementary-minor matrix of the positive `(n-1,n-1)` form, using the same wedge normalization as the reading edition. The `(n-1)`-power operation on a positive `(1,1)` matrix `A` becomes `G=adj(A)=det(A)A^{-1}`. For `n>=2`, set
```text
d = (det G)^(1/(n-1)),       A = d G^(-1).
det A = d,                  adj(A) = d(d^(-1)G) = G.
```
The positive `(n-1)`-st root is unique because `det G=(det A)^(n-1)`, and the inverse and positive determinant root depend smoothly on `G`. This **checks this finite-dimensional proof step**, not the full global Hahn–Banach/Fredholm or complex-current chain.

The same scope prevents a spurious error report against Theorem 11.4.2: the displayed conformal factor `rho^(1/(n-1))` is only asserted with the inherited `n>=2` premise. On curves, all Hermitian forms are Gauduchon, and the constant positive `rho` solves `dd^c rho=0`; the conformal-root parameterization need not be invoked.

## Verification boundaries and action

- **Previous classification changed:** `POME-GAUDUCHON-N1-POSITIVE-ROOT-001`: **withdraw its "confirmed error" status**, retaining the original report and hypothetical dimension-one calculations as a dated, explicitly superseded audit trail. **New ID** `POME-GAUD-ROOT-SCOPE-AUDIT-RECLASS-001` is a **verified audit correction**, not an additional confirmed theorem error.
- **Original mathematical statements and proofs remain unchanged.** No source-body patch, registry/canonicalization edit, tag change, build, CI, website publication or formal verification has been performed. An optional explanatory cross-reference to §11.3 would be *editorial*, not a mathematically necessary repair.
- **No transitive certification:** the general `n>=2` Hahn–Banach/Fredholm current construction, Theorem 11.4.2, downstream §11.7 or the global nonlinear theorem behind §12.2.3 were not fully re-proved.
- **Coverage:** §§11.3, 11.4, 11.6 and 12.11 were already partly visited; §12.2 was used for precise hypothesis comparison. **0 first proof-level numbered-section visits, 0 whole-section mathematical certifications**. Current inventory remains **25 chapters / 747 numbered sections**.
- **User-deferred scope unchanged:** Demailly regularization/approximation and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion are still `deferred-by-user`, neither reopened nor certified.

**Suggested audit disposition:** display this correction next to the original finding, treat that original as **superseded / non-defect** in all future active-error summaries, and count no production error for the `n=1` root countermodels.