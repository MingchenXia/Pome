# Quadratic jet by subharmonic circle means; duplicated Gauduchon second-variation equation

Date: 2026-10-29. **Reviewed production main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. Audit-only branch: <code>review/mathematical-audit</code>. Scope: selected integrated reading-edition passages, not a chapter or whole-section certification. All dedicated Demailly regularization/approximation, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion is **deferred-by-user** and not reviewed here.

## POME-SCHWARZ-QUADRATIC-JET-MEAN-001

**Status:** verified repair (self-contained replacement of the *local quadratic-jet step only*). **Severity:** low. **Printed Proposition 9.17.1 is not asserted false or incompletely proved.**

**Integrated source and anchors.** Main file <code>docs/sections/schwarz-estimates-and-invariant-distances/index.html</code>, blob <code>11789d8f51f81ec69de4fbb206c1186c73540b0e</code>, physical lines 19–51, especially 32–43. Source <code>klimek-pluripotential-theory:9FEF0D81</code>, permanent tag <code>10AFB6AB7732</code>; section §9.17, statement Proposition 9.17.1. The text invokes planar removable subharmonic singularities and nonthin radial segments to eliminate pure second-order terms of a function of the form <code>v=exp(h)</code>. The second input can be eliminated by a short circle-mean argument.

**Hypotheses and exact claim.** Let <code>D ⊂ C^n</code> be bounded, <code>a ∈ D</code>, let <code>h</code> be negative plurisubharmonic with <code>h(a)=-∞</code>, and put <code>v=exp(h)</code>. Assume <code>v</code> is C² near <code>a</code>. For every complex direction <code>ξ</code>, the second real Taylor polynomial of <code>v(a+z)</code> restricted to the line <code>z=ζξ</code> has no harmonic quadratic component <code>Re(Bζ²)</code>. Hence the full second jet contains no pure holomorphic/antiholomorphic quadratic terms, and for every holomorphic curve <code>F(0)=a</code>, <code>F'(0)=ξ</code>,
\[
v(F(\zeta))=\mathcal L_v(a;\xi)|\zeta|^2+o(|\zeta|^2).
\]

**Complete elementary argument.** Since <code>v ≥ 0</code> and <code>v(a)=0</code>, the assumed differentiability makes <code>a</code> a minimum, so <code>dv(a)=0</code> and <code>v(a+z)=O(|z|²)</code>. Fix a nonzero direction <code>ξ</code> and write <code>f(ζ)=v(a+ζξ)</code>. On the punctured disc,
\[
w(\zeta):=\frac{f(\zeta)}{|\zeta|^2}
=\exp\!\big(h(a+\zeta\xi)-2\log|\zeta|\big).
\]
The exponent is subharmonic because <code>log|ζ|</code> is harmonic off zero; the increasing convex exponential preserves subharmonicity. The Taylor estimate makes <code>w</code> bounded above near zero. The removable-singularity theorem for subharmonic functions extends <code>w</code> to zero with <code>w(0)=limsup_{\zeta\to0}w(\zeta)</code>, a finite number.

The C² real Taylor polynomial along this line gives
\[
w(re^{it})=A+\operatorname{Re}(Be^{2it})+o(1)
\quad(r\downarrow0),
\]
uniformly in <code>t</code>. Denote the continuous limit by <code>L(t)</code>. Upper semicontinuity of the extended <code>w</code> gives <code>L(t) ≤ w(0)</code> for all <code>t</code>. Subharmonic sub-mean and upper semicontinuity give, respectively,
\[
w(0)\le\frac1{2\pi}\int_0^{2\pi}w(re^{it})\,dt
\le w(0)+o(1).
\]
Taking the limit yields <code>A=w(0)</code>. Thus the continuous nonnegative function <code>w(0)-L(t)</code> has integral zero and is identically zero. It follows that <code>B=0</code>. Applying this for every complex direction and polarizing removes the pure second-order terms of the full real Taylor polynomial. The displayed holomorphic-curve asymptotic follows because <code>F(ζ)=a+ζξ+O(|ζ|²)</code>.

This replaces precisely the **nonthin-segment** invocation in the selected quadratic-jet step without reopening any excluded approximation programme. The surrounding Green-envelope comparison, leafwise maximum principle, planar subharmonic removal, and canonical Green-function existence retain their own assumptions and are **not** transitively certified.

**Proposed change.** Optional separately reviewable proof-only replacement of the nonthin-segment paragraph by the circle-mean proof, preserving source attribution and permanent tag. Do not alter source body or main automatically. **Affected dependents:** the Levi-form comparison and equality-rigidity argument within Proposition 9.17.1, plus interpretations of Green/invariant-distance second jets in §9.17.

## POME-GAUD-SECONDVAR-EQ-ALIAS-NESTED-001

**Status:** confirmed error (**reading-edition equation integration/markup**, not a false mathematical proposition). **Severity:** medium.

**Integrated source and anchors.** Main <code>docs/sections/a-gauduchon-variational-volume--second-variation-on-background-classes/index.html</code>, blob <code>4992f82c6e84918ead47a972eab7e3238a147655</code>. The full two-row equation is at physical lines **22–29** of Proposition 12.4.1, source <code>non-kahler-pluripotential-theory:C55D0CC4</code>, permanent tag <code>67FDDBC10DBD</code>. The first row (12.4.2) is source tag <code>86F8F24F</code>, permanent tag <code>E544AEC2FDDB</code>; the second (12.4.3) is source tag <code>3217D224</code>, permanent tag <code>88A03DC67E97</code>. The proof refers correctly to these tags at lines **43–54**.

**Exact defect and reproducible three-page check.** The complete, mathematically correct, two-row <code>\begin{align} ... \tag{12.4.2}\\ ... \tag{12.4.3}\end{align}</code> occurs once in the proposition. The section then appends a **second, terminal-row-only** source-variant chunk at physical line **79**, representing equation (12.4.3) as
\[
\texttt{\textbackslash[ \textbackslash begin\{aligned\}\textbackslash begin\{align\} ... \textbackslash tag\{12.4.3\} \textbackslash end\{align\}\textbackslash end\{aligned\} \textbackslash]},
\]
i.e. an illegal nested display environment <code>\begin{aligned}\begin{align}</code>. The standalone page <code>docs/tag/88A03DC67E97/index.html</code> (blob <code>9b5b21b413f54aad1ee4cce5aa959ddb08e3d8a2</code>) repeats only this malformed fragment. The complete (12.4.2) page <code>docs/tag/E544AEC2FDDB/index.html</code> (blob <code>0d46362e01f32a8c40f467205cc6bacf226cb958</code>) contains the correct two-row align display.

A deterministic, read-only text check of these three **actual main blobs** returned: continuous section = two occurrences of <code>\tag{12.4.3}</code>, nested align present, complete align present; tag (12.4.3) = one occurrence, nested align present, no complete align; tag (12.4.2) = one occurrence, no nested align, complete align present. This directly witnesses duplicated mathematical display and invalid MathJax/TeX structure, without claiming to have run a browser or a project build.

**Mathematical control check.** With <code>A_χ=Ω^{-1}(χ+dd^c u̇)</code> and <code>tr A_χ=nλ̇/λ</code>, twice differentiating the printed fixed-density Monge–Ampère equation gives
\[
\operatorname{tr}_\Omega(dd^c\ddot u)-\operatorname{tr}(A_\chi^2)
=n\big(\ddot\lambda/\lambda-(\dot\lambda/\lambda)^2\big).
\]
The adjoint probability kills the integral of <code>tr_Ω(dd^c ü)</code>, proving (12.4.3). Using <code>||A_χ-rI||²=tr(A_χ²)-nr²</code> for <code>r=λ̇/λ</code> yields (12.4.2). The signs and normalization of the *intended proposition* are consistent; the upstream smooth solution/adjoint-probability existence is conditional. This is therefore a **confirmed rendering/integration error**, not a theorem counterexample or a complete analytic theorem proof.

**Proposed correction.** In a separately reviewed source-to-reading registry patch, associate each permanent equation tag with its canonical row in the single full aligned display; do not emit a duplicate detached row in the continuous section. Give the standalone (12.4.3) permalink a legal standalone rendering (or an anchored, uniquely accessible view of the full display) rather than nesting <code>align</code> inside <code>aligned</code>. Preserve tags, statement order, full two-row identity and original historical attribution. Do not modify main/site/source/registry/permanent tags directly in this audit.

**Affected dependents:** the permanent (12.4.3) equation permalink, §12.4 continuous section, proof links within Proposition 12.4.1, and the Hessian-metric interpretation §12.6. This is a **new location of a previously recognized general alias-splitting pattern**, distinct from the earlier §6 and §14 equation identities; not a new mathematical duplication or a claim that the underlying formula fails.

## Exact coverage and limitations

- **New selected proof-level check:** only the quadratic-jet removal step and immediate Levi consequence of §9.17.1.
- **Incremental selected audit:** §12.4.1–4, the adjoint integration and equation alias/standalone/continuous representation; previous second-variation checks were not claimed as new mathematics.
- **First navigation inspection, not proof review:** §§9.33 (subject page linking §§9.34–36) and 10.42 (subject page linking §§10.43–44). These two section pages contain no theorem/proof bodies. Inventory rows become navigation-only, not verified.
- The original **25 chapters, 747 distinct numbered sections and zero complete-section certifications** are preserved; no earlier ledger item is closed. All dedicated excluded approximation/regularization and Bergman/L²/OT/multiscale/positivity-loss tasks stay **deferred-by-user**, neither solved nor reopened.
- No compilation, browser rendering, CI, formalization, repository source editing, automatic merge, or site publication was performed. This report and ledger changes are review-only Markdown notes on the audit branch.
