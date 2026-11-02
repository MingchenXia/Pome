# 2026-11-02 — Zero-Lelong polar restrictions versus trace and divisorial valuation

**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (not edited). **Stable finding:** \`POME-TRACE-SUBLOG-POINTWISE-001\`. **Severity:** low. **Status:** verified conditional deduction / explicit boundary example; **not** a false source theorem, an independently certified trace-existence theorem, or an applied correction. This model is different from previous non-pluripolar zero-Lelong Monge–Ampère mass examples. The exact distinction here concerns *ordinary restriction versus an equisingular trace* and the trivial valuation of a subvariety.

## Precisely inspected integrated anchors

- \`docs/sections/the-trace-operator/index.html\`, main Git blob \`1f3a3e4f0317a308b43bd3df53dda84c5f3fa50a\`: Definition **20.2.6** (source \`sgpt:DC6538A0\`, permanent \`ADF6E265888F\`, physical lines **224–231**); Example **20.2.9** (source \`sgpt:11E79380\`, permanent \`75F5F5ACD2FA\`, line **250**); Definition **20.2.10** (source \`sgpt:4261C2F9\`, permanent \`5239E9ADD0FF\`, lines **254–260**); Proposition **20.2.12** (source \`sgpt:18696C0F\`, permanent \`B293F74D2022\`, lines **272–305**, with the *separate* assumption that the pointwise restriction is not identically \`-infinity\`).
- \`docs/sections/non-archimedean-pluripotential-theory/index.html\`, main blob \`8448d710690ebe1cc28040f9611d05c9d008a961\`: Definition **22.1.79** (source \`sgpt:322D4668\`, permanent \`322D4668B967\`, lines **1224–1239**); Theorem **22.1.113** (source \`sgpt:331B39A3\`, permanent \`D613676A36CA\`, lines **1732–1810**, statement/dependency inspection only); Lemma **22.1.116** (source \`sgpt:657B916D\`, permanent \`1861C279EAB7\`, lines **1815–1842**, including its explicit \`0\` versus \`-infinity\` valuation dichotomy at **1835–1838**).
- \`docs/index.html\` on that same main was checked for actual section placements and ToC identity; tags identify statements, not changing source numbers. The non-Archimedean result's upstream bijection and the general existence/independence of equisingular traces are **conditional existing inputs**, not re-proved.

## Explicit compact-projective model

Let \`X = P^1\`, let \`Y = {p}\` be a point, and choose a coordinate \`z\` at \`p\`. Fix \`0<alpha<1\`. For \`0<|z|<epsilon\`, set
\[
t=-\log |z|^2,\qquad u(z)=-t^\alpha.
\]
Choose \`epsilon\` sufficiently small and extend \`u\` across the complement of a smaller coordinate disk by a smooth cutoff. The resulting upper-semicontinuous function on \`X\` is quasi-psh: on the punctured small disk it is subharmonic, and away from \`p\` its real Hessian is bounded below; adding a sufficiently large positive multiple of \`omega_FS\` compensates the latter. It tends to \`-infinity\` at \`p\` and is not identically \`-infinity\` on \`X\`.

Using Pome's \`dd^c = (i/2pi) partial barpartial\` and \`dd^c log|z|^2 = delta_p\`, write \`s=log|z|^2\` and \`f(s)=-(-s)^alpha\`. Then
\[
f'(s)=\alpha(-s)^{\alpha-1}>0,\qquad
f''(s)=\alpha(1-\alpha)(-s)^{\alpha-2}>0
\]
for sufficiently negative \`s\`. Hence \`dd^c u\` is positive off \`p\`. Stokes' formula on a punctured disk and the absence of an atom (the inward slope tends to zero) yield the **exact small-disk curvature mass**
\[
\int_{|z|<r}dd^c u
=\alpha(-\log r^2)^{\alpha-1}\longrightarrow 0
\quad (r\downarrow0).
\]
Equivalently, the Lelong number at \`p\` is \`nu(u,p)=lim_{r->0}u(r)/log r^2=0\`, while the **ordinary restriction is \`u|_Y = -infinity\`**.

Moreover, every positive integer \`m\` satisfies \`I(mu)_p=O_{X,p}\`. Indeed the local weight is \`exp(-mu)=exp(m t^alpha)\`, and polar area measure becomes a constant multiple of \`exp(-t)dt\`; thus
\[
\int_{|z|<r}e^{-mu}\,dA
=\pi\int_{-\log r^2}^{\infty}e^{m t^\alpha-t}\,dt<\infty.
\]
The conclusion is insensitive to conventional fixed factors in the exponent, since \`t^\alpha=o(t)\`. Thus the singularity is **polar in its pointwise restriction but invisible to all its positive-integral multiplier-ideal tests and to its divisorial Lelong number**.

## Audit consequence and correct interpretation

The example verifies that the hypothesis \`nu(phi,Y)=0\` used in Definition **20.2.6** is **not** a disguised assertion \`phi|_Y != -infinity\`; the additional ordinary-restriction hypothesis in Proposition **20.2.12** is logically independent. At a zero-dimensional target, Example **20.2.9** expressly allows a finite constant trace despite \`u(p)=-infinity\`. No attempt was made to reconstruct its quasi-equisingular approximants: their existence and convergence are treated as the **printed conditional inputs**, without entering the author-excluded approximation/Bergman/L2/Ohsawa–Takegoshi programme.

In Lemma **22.1.116**, the expression at \`v_{Y,triv}\` is **not a point evaluation of the original complex potential on \`Y\`**. Its proof uses a zero/positive generic-Lelong valuation dichotomy for the components of a non-Archimedean test curve; the zero-Lelong side can equal \`0\` despite \`u|_Y=-infinity\`. Therefore the nontrivial-restriction condition and analytified trace in Theorem **22.1.113** must not be silently replaced by naive pointwise restriction. The model does **not** assert that an arbitrary non-model quasi-psh \`u\` itself defines a model non-Archimedean test curve.

**Proposed non-invasive addition:** after Example 20.2.9, optionally give the sublogarithmic \`-(-log|z|^2)^alpha\` example and explicitly distinguish ordinary restriction, trace and the trivial-valuation test. Retain the existing hypotheses, historical attribution, stable source labels and permanent tags. No theorem repair is indicated.

**Potential affected dependents:** the scope of Proposition 20.2.12, compatibility Theorem 22.1.113, condition Lemma 22.1.116, and applications to trace on singular spaces. No downstream theorem has been shown false and no general trace or comparison proof is certified.

**Actual scope:** new selected statement/hypothesis-level inspection in previously sampled §§20.2 and 22.1, with independent local potential-theoretic calculation on \`P^1\`; **not** first whole-section coverage. The current ToC contains **25 chapters and 747 numbered sections, zero entire mathematical-section certifications**. Previous confirmed errors, proof gaps and external-dependency statuses are preserved. Demailly approximation/regularization and dedicated Bergman, \`L^2\`, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof completion remain **deferred-by-user**. No original/source, registry, canonicalization, main, tags, CI, tests, build, formal verification or published \`docs/\` files were changed.
