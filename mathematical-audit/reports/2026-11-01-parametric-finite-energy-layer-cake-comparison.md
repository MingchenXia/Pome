# 2026-11-01: A parametrized layer-cake comparison for relative Monge–Ampère energies

**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Status:** targeted independent mathematical audit, not a whole-section or transitive-dependency certification. **Excluded scope:** all Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof completion remain *deferred-by-user*; none was inspected or repaired in this increment.

## Finding POME-ENERGY-PARAMETRIC-LAYER-001 — low / verified conditional deduction

**Primary integrated location:** \`docs/sections/relative-energy-and-perron-segments--relative-monge-ampere-energy/index.html\`, main blob \`16fdcc4c6a6f0cc75e69ba267bd7da2b2d7922a1\`, Lemma **17.3.18**, source \`foundations-of-pluripotential-theory:FE22CA48\`, permanent tag \`620127F44043\`. Statement: physical **247–255**; its layer-cake set inclusion, full-mass comparison, and Tonelli argument: **258–281**, especially **261–279**.

**Hypotheses (the same as the printed lemma):** \`X\` is in the compact Kähler / big closed background setting of §17.3; \`φ\` is a positive-mass model potential; \`u∈E(X,θ,φ)\` has full relative mass, \`v∈PSH(X,θ)\` satisfies \`v≼φ\`, and \`γ:X→[-∞,+∞]\` is Borel with \`γ≥max(u,v)\`. Write \`μ_w=⟨(θ+dd^cw)^n⟩\`. Extended differences and null pluripolar pole sets have exactly the interpretation used in the original Lemma 17.3.18. Put
\[
 A=\int_X(\gamma-u)\,\mu_u,\qquad
 B=\int_X(\gamma-v)\,\mu_v,\qquad
 I=\int_X(\gamma-u)\,\mu_v
 \quad\in[0,+\infty].
\]

**New precise claim:** For every real \`a>0\`,
\[
 \boxed{I\ \le\ (1+a)\,A+(1+a^{-1})\,B.}\tag{*}
\]
Consequently, whenever \`A,B<∞\` (including either zero endpoint),
\[
 \boxed{I\ \le\ (\sqrt A+\sqrt B)^2
  =A+B+2\sqrt{AB}\ \le\ 2A+2B.}\tag{**}
\]
The intermediate inequality is strictly stronger than the printed coefficient-\`2\` estimate when \`A≠B\`, with difference \`(\sqrt A-\sqrt B)^2\` in the upper bounds. It is *not* asserted that (**) is the best possible bound for every admissible triple; its equality is achieved in the endpoint model below. The original lemma is **correct**, not a false theorem.

### Complete derivation of (*) and (**)

Fix \`a>0\` and \`t≥0\`. If both \`γ≤v+at\` and \`v≤u+t\`, then \`γ≤u+(1+a)t\`; hence the pointwise inclusion
\[
 \{\gamma>u+(1+a)t\}
 \ \subset\
 \{\gamma>v+at\}\ \cup\ \{v>u+t\}.
 \tag{1}
\]
All inequalities and level sets are restricted to the common finite locus as in the printed lemma; non-pluripolar Monge–Ampère measures give zero mass to the omitted pole sets. By the layer-cake identity and Tonelli for *nonnegative* extended Borel weights,
\[
 I=(1+a)\int_0^\infty
     \mu_v\bigl(\{\gamma>u+(1+a)t\}\bigr)\,dt.
\]
The first right-hand set in (1) contributes
\[
 (1+a)\int_0^\infty
     \mu_v(\{\gamma>v+at\})\,dt
      =\frac{1+a}{a}\,B=(1+a^{-1})B.
\]
For the second set, apply exactly the **full-relative-mass** case of Proposition 16.25.4 to \`u\` and \`v-t\` (constant translation preserves \`μ_v\` and the required singularity preorder). The mass defect cancels because \`u∈E(X,θ,φ)\`. Thus
\[
 \mu_v(\{v>u+t\})\le \mu_u(\{v>u+t\}).
 \tag{2}
\]
Consequently,
\[
 (1+a)\int_0^\infty \mu_v(\{v>u+t\})\,dt
 \le (1+a)\int_X(v-u)_+\,\mu_u
 \le(1+a)A,
\]
because \`γ≥v\`. Adding the two terms proves (*); no compactness, measure limit, approximation of \`γ\`, or integrability is silently assumed. When \`A,B>0\`, minimize \`aA+B/a\` at \`a=\sqrt{B/A}\` to obtain (**). If \`B=0\` take \`a↓0\`; if \`A=0\` take \`a↑∞\`; if both vanish, either limit gives \`I=0\`. Extended-infinite cases retain the universally valid bound (*), with the usual nonnegative extended-value conventions. This optimization uses scalar real arithmetic, *not* an interchange of a directed limit and an integral.

**Endpoint attainment:** Take any compact Kähler \`X\` with \`θ=ω>0\`, \`φ=0\`, \`u=-c\` for \`c>0\`, \`v=0\`, and \`γ=0\`. Then \`μ_u=μ_v=ω^n\`, and if \`m=\int_Xω^n\`, one has \`A=I=cm\`, \`B=0\`. The bound (**) reads \`cm≤cm\` and is an equality. Hence the coefficient of \`A\` in the \`B=0\` endpoint cannot be decreased. This explicit smooth test is separate from and does not certify non-pluripolar comparison in general.

**Comparison dependency actually inspected:** \`docs/sections/envelopes-and-model-potentials--singularity-constraints-and-relative-capacity/index.html\`, main blob \`4207ba03590b2988456f1df4da4123e1e572c8de\`, Proposition **16.25.4**, source \`foundations-of-pluripotential-theory:944C88B6\`, tag \`C32431185924\`, lines **75–99**. This proof invokes §13.8 mixed mass monotonicity, §16.21 model mass preservation, and plurifine locality; these are **upstream premises**, not independently recertified. The \`v\` side is *not* assumed to have full relative mass for inequality (2).

**Proposed documentation-only change:** Offer (*) and (**) as an optional corollary following Lemma 17.3.18, preserving the original coefficient-\`2\` statement, source attribution, hypotheses, permanent tags, and subsequent mixed finite-energy integrability consequence. Do not modify the integrated reading text. Possible dependent uses: the mixed-measure integrability part of Lemma 17.3.18, finite-energy cocycle Proposition **17.3.19** (main lines **286–325**, tag \`98BD01BE1363\`), and energy comparisons in §§17.3–17.9. No downstream error is asserted.

## Other genuinely inspected passages, without a new error verdict

- **§7.3:** \`docs/sections/bedford-taylor-products-and-local-capacity--decreasing-continuity-and-symmetry/index.html\`, blob \`96a9e39e85fab5774ebdac0c6d9d006338a4e42c\`, Lemma 7.3.4 (tag \`DE1E6EDC0B48\`, physical 74–89) and Theorem 7.3.7 (tag \`D87C13B3250A\`, physical 134–229), selected upper semicontinuity / common-collar / weighted-measure steps. The theorem is stated for **sequences**, and the local subsequence compactness argument was not extended to arbitrary nets here. These passages were historically reviewed, so **no first-time coverage** is claimed.
- **§17.3:** Lemma 17.3.18, its mixed full-mass/Tonelli integrability reduction (lines 281–282) and the precise finite-energy framework in Proposition 17.3.13 / Theorem 17.3.14 (149–215) and Proposition 17.3.19 (286–325) were independently checked as selected steps; not a full section certification.
- **§20.7:** \`docs/sections/meromorphic-sections-and-divisor-classes/index.html\`, blob \`d0c40d1e3f6f515eb13169ed1cd3fb447ca161c8\`, Proposition 20.7.3 source \`demailly-complex-geometry:00A05C89\`, tag \`ACC6D09EDDD9\`, physical 12–27: independently reread divisor cocycle, \`dd^c log|s|_h²=[div s]-c₁(L,h)\` sign and local principal-divisor prerequisites. The formula is consistent with \`O(1)\` on \`P¹\`, where for a section vanishing at \`z=0\`, \`dd^c log(|z|²/(1+|z|²))=δ_0-ω_FS\`. This §20.7 proof has **historical** coverage; it is only a cross-check, and no claim about non-Cartier Weil divisors on singular bases is made.

## Coverage, state and execution boundaries

The current actual table of contents still has **25 chapters and 747 numbered sections**. The only new mathematical deduction in this run is \`POME-ENERGY-PARAMETRIC-LAYER-001\`, at the unisolated parametric step of Lemma 17.3.18; all additional reads are explicitly partial or previously covered. **Zero complete mathematical sections certified.** No old finding is re-announced as new; no prior proof gap, external input, verified-but-unapplied repair, or deferred issue is silently closed. Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion remain **deferred-by-user**. No project tests, build, GitHub Actions, formal verification, website publication, source/body/canonicalization/permanent-tag edits or changes to production \`main\` were performed.
