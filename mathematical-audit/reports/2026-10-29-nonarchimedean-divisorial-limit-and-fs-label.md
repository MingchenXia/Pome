# 2026-10-29 — Divisorial-pointwise versus full Berkovich pointwise limits; an unremapped Fubini–Study equation label

## Provenance, scope, and status

Production `main` reviewed: `b6933b772f41b45918f7e25ed1afbbb1fd892272` (not modified). Audit branch: `review/mathematical-audit`. Integrated reading file: `docs/sections/non-archimedean-pluripotential-theory/index.html`, production blob `8448d710690ebe1cc28040f9611d05c9d008a961`. This is **selected direct mathematical review only** of §22.1.66–76, physical HTML lines 1102–1215. It does not certify any whole section, Boucksom–Jonsson's external theorems, or the conjecture. No Demailly approximation, regularization, Bergman, L², Ohsawa–Takegoshi, multiscale atlas, or positivity-loss proof was examined.

The stable section entry is `618C84432CDA` (heading §22.1.66), followed by `3CE1C3E79114` (§22.1.70); source book `sgpt`. Relevant permanent tags: valuation Definition 22.1.67 `433FF564E9A3` (source `sgpt-5735BD72`, line 1108); Fubini–Study function formula immediately before Definition 22.1.71, lines 1178–1185; Definition 22.1.71 `EEADED50AAC3` (source `sgpt-DAC17F2D`, line 1189); divisorial-determination Theorem 22.1.72 `0DAB63894803` (line 1194); closure Proposition 22.1.73 `8E1FC46DBC87` (line 1199); approximation Theorem 22.1.75 `6B2CF0C2744A` (line 1209); and envelope Conjecture 22.1.76 `95739E70234B` (line 1214).

## POME-NA-DIV-POINTWISE-NONUSC-001

**Severity:** low. **Status:** verified conditional deduction (a new explicit example); **no printed theorem is false**.

**Claim.** On the smooth projective line, a **monotone increasing sequence of rational generically finite Fubini–Study metrics on a fixed ample line bundle**, uniformly bounded above by a continuous Fubini–Study metric, can converge to that upper metric at every divisorial valuation while its raw pointwise limit on the whole Berkovich analytification fails to be upper semicontinuous and fails to equal that metric at a closed-support semivaluation. Thus the topology on `PSH(L^An)` declared in line 1193 really is divisorial-pointwise; it cannot silently be replaced by raw pointwise convergence on all of `X^An`. This is consistent with the precise statement of Conjecture 22.1.76 and does **not** disprove it.

**Proof.** Let `X=P^1_C`, `L=O(1)`, and use homogeneous sections `Z_0,Z_1`. A local frame of `L` identifies the following expressions with ordinary real functions, with all displayed identities independent of the choice of frame:
```tex
\Phi=\max\{\log|Z_0|,\log|Z_1|\},
\qquad
\Phi_m=\frac1m\max\{\log|Z_0^m|,\log|Z_0Z_1^{m-1}|\}
       =\left(1-\frac1m\right)\Phi+\frac1m\log|Z_0|,
\quad m\ge2.
```
Each `Phi_m` is an element of `H^gf_Q(L^An)` by the actual definition at lines 1178–1185: the two nonzero homogeneous sections have degree `m`, all weights are rational (zero), and they have no common zero on the generic point. Likewise `Phi` is a basepoint-free rational Fubini–Study metric. Since `log|Z_0|<=Phi` everywhere, `Phi_m<=Phi_{m+1}<=Phi`, including the extended-value convention when `log|Z_0|=-infinity`. For any `v in X^div` with support `X`, every nonzero rational section has **finite** valuation, whence
```tex
\lim_{m\to\infty}\Phi_m(v)=\Phi(v).
```
Thus `Phi_m` converges to `Phi` in the exact **divisorial-pointwise topology** declared before Theorem 22.1.72.

Let `p=[0:1]`, and let `x_p in X^An` denote the semivaluation with support the reduced closed subvariety `{p}`. In the `Z_1` frame, `log|Z_0|(x_p)=-infinity` while `log|Z_1|(x_p)=0`. Hence
```tex
\Phi_m(x_p)=-\infty\quad(\forall m),\qquad \Phi(x_p)=0.
```
The raw pointwise limit `Psi=lim_m Phi_m` on **all** of `X^An` therefore differs from `Phi` at `x_p`. More decisively, put `v_t=t ord_p`, a divisorial valuation for positive rational `t`. In the affine coordinate `z=Z_0/Z_1`, `|z|(v_t)=e^{-t}`, while any polynomial with nonzero constant term has norm one; hence `v_t -> x_p` in the Berkovich topology as `t -> infinity` through positive rationals. But
```tex
\Psi(v_t)=\Phi(v_t)=\max\{-t,0\}=0
\quad\text{and}\quad \Psi(x_p)=-\infty.
```
So `Psi` is **not** upper semicontinuous at `x_p`. There is no issue with the upper semicontinuity of each individual `Phi_m`: at fixed `m`, `Phi_m(v_t)=-t/m -> -infinity`. The failure arises solely from interchanging the two limiting operations `m -> infinity` and `t -> infinity`. This establishes the example without invoking a compactness or regularization theorem.

**Proposed action and dependents.** Optional explanatory counterexample after the topology statement preceding Theorem 22.1.72 or near Conjecture 22.1.76, with all existing tags retained. This guards §22.1.71–76 and downstream NA-envelope uses against confusing pointwise convergence on divisorial valuations with pointwise convergence on all semivaluations. It gives **no** complete proof of the external BJ22 determination/approximation theorems or of the envelope conjecture.

## POME-NA-FS-STALE-EQUATION-LABEL-001

**Severity:** medium (reader numbering/permalink integrity); **status:** confirmed error **in the integrated reading edition only**, not a false formula or theorem.

**Exact evidence.** In the same production HTML blob, at physical lines 1178–1185, the Fubini–Study definition displays
```html
<div class="equation numbered-equation">
<span class="equation-label">13.37</span>
<div>\begin{equation}  \phi =\frac{1}{m}\max _ j \{ \log |s_ j|+\lambda _ j\} . \end{equation}</div>
</div>
```
The literal `13.37` is the **old source-style number**, not a reader locator in §22.1. It has no `data-tag`, no link, and no stable equation-anchor span, unlike the properly generated numbered Eq. 22.1.68 (lines 1156–1159) and Eq. 22.1.69 (lines 1166–1169). A direct inspection of all `<span class="equation-label">...</span>` instances in this section yielded this single unlinked literal label. This contradicts `AGENTS.md`'s current-Pome-number and permanent-tag policy. The displayed mathematical expression itself is correct under the given section convention.

**Proposed correction.** In a separately reviewable renderer/integration patch, determine whether this source equation has a legitimate permanent equation tag. If yes, generate its proper §22.1 reader number, stable link and tag using the established mapping; if not, render it as **unnumbered** rather than hard-code the obsolete `13.37`. Retain source provenance and all other permanent tags. Do not hand-edit the published `docs/` output or mathematical registry during this audit. Affected readers: Fubini–Study formula adjacent to Definition 22.1.71, cross-reference consistency and generated equation/pagination navigation. This is an **unresolved proposed renderer repair**, not a completed patch.

## Additional false-positive excluded during review

The exact wording of line 1143, namely `U^An` consisting of semivaluations whose **support meets** the Zariski open `U`, is **not** an error and must not be replaced by a center-in-`U` criterion. For example, on `P^1`, the valuation `ord_infinity` has support all of `P^1` and thus belongs to the analytification of the affine chart `A^1` although its center on the projective compactification is infinity. It evaluates the affine coordinate `z` to `|z|=e>1`, an allowed (non-unit-disk) Berkovich point over the trivially valued field. This agrees with Boucksom–Jonsson, *Global pluripotential theory over a trivially valued field* (2022), §1.1.2, and is **not** an audit finding. Historical attribution is retained.

## Precise coverage, outstanding work, and change boundary

Checked the integrated definitions and model computations §22.1.66–76 (lines 1102–1215) at the specific anchors above, independently proved the Fubini–Study model limit and counterexample, and checked the single stale formula label. Proposition 22.1.73/.74 and Theorems 22.1.72/.75 were read at statement level, **not** re-proved; no full Berkovich/BJ theory, non-Archimedean Monge–Ampère operator, or full §22.1 chapter is certified. Prior §22.1.88 left-tail recursion error, its repair proposals, the original external dependencies, and every pre-existing audit finding retain their exact historical statuses. Across the project the matrix retains **25 chapters, 747 numbered ToC sections, zero complete-section certificates**. Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss programme remain **deferred-by-user**, neither resolved nor reopened. No source text, body, registry, canonical tag, main, website, GitHub Action, or formalization state was changed. No test suite, build, CI or deployment was run.
