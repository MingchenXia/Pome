# 2026-11-22: Hopf radial period monodromy, Hermitian torsion display, flat twists, and involutivity

## Baseline and exact scope
- Reviewed **main**: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; pre-write audit branch: \`a4b3ec7fc37d52be4d33b6f45d577fe6f105917d\`.
- Fully read current integrated mathematics (not a certificate of upstream inputs):
  - \`docs/sections/hermitian-torsion-and-the-bochner-identity/index.html\`, blob \`4656b430de6ec989ef121eca550afda0be407222\`, physical lines **6–247**, §11.48.1–21, primary source \`demailly-complex-geometry\`. Read only the displayed Hermitian operator identities and their already-integrated arguments; **no** excluded regularization or dedicated Bergman/L²/OT/atlas/positivity-loss completion.
  - \`docs/sections/euler-characteristics-under-flat-twists/index.html\`, blob \`99c65b6051fef34b6ec0b8822c973ab5470bb30a\`, mathematical lines **5–18**, §10.103.1, \`cao-paun-foliations\`.
  - \`docs/sections/tensor-products-and-involutivity/index.html\`, blob \`b0939c7452c9ef74f49bd7751c8c728c251199d4\`, mathematical lines **5–45**, §§10.107.1–2, \`cao-paun-foliations\`.
- **Selected only**, NOT a full-section review: \`docs/sections/locally-conformally-kahler-geometry/index.html\`, blob \`6ebf8e604b45d3eb748037af506145273ca3875d\`, physical lines **594–777**, §§23.2.35–45 (\`non-kahler-pluripotential-theory\`), radial scalar Hopf metrics.
- The actual current ToC has **747 sections in 25 chapters**; three complete current readings and one selected passage here. No historical first visit or fully certified transitive proof chain is asserted.

## POME-HOPF-RADIAL-PERIOD-MONODROMY-001
**Severity: low. Status: verified conditional deduction.** Not a false statement or an identified gap in the printed Theorem 23.2.41. Stable source/permanent identifiers: eq. §23.2.38 \`0452243D80CF\`, eq. §23.2.39 \`9A128F70476F\`, Lemma §23.2.40 \`1D02D96B9AF2\`, Theorem §23.2.41 \`C4C3411B46C3\`. Physical lines **625–711**.

Let \`m=n-1>=1\`, \`F(r)>0\` be smooth and 2-periodic, and \`k<0\`. Let \`C=C_{F,k}>0\` be the unique 2-periodic solution (Theorem 23.2.41) of
\[
 C'=kC^{1-m}+FC^{-m},\qquad
 L(k,F)=k\int_0^2 C^{-m}\,dr=-\int_0^2 FC^{-m-1}\,dr<0.
\]
Consider the time-two flow map \`P(c;k,F)\`, sending an initial value \`C(0)=c\` to \`C(2)\`, near the unique periodic initial value. Its derivative at the periodic solution is **exactly**
\[
 \boxed{\partial_c P(C(0);k,F)=\exp(L(k,F))\in(0,1).}
\]
Consequently the positive periodic solution depends smoothly on \`k\` and on every smooth finite-dimensional family of positive periodic inputs \`F\`; there is no unit Floquet multiplier. Put \`H=\partial_k C\`. Then
\[
 \boxed{(C^m H)'=kH+C,\qquad
 H(r)=C(r)^{-m}\int_{-\infty}^{r}
 C(s)\exp\!\left(\int_s^r kC(t)^{-m}dt\right)ds>0.}
\]
In particular the period is **smooth with strictly positive derivative**
\[
 \boxed{\partial_kL(k,F)=
 \int_0^2\!\left(C^{-m}-mkC^{-m-1}H\right)dr>0.}
\]
With the endpoint ranges already established in §23.2.41, \`k\mapsto L(k,F)\` is a smooth increasing diffeomorphism from \`(-\infty,0)\` to \`(-\infty,0)\`. Thus the unique radial Gauduchon metric with prescribed positive volume profile and negative Lee period varies smoothly under smooth families of both data. This is a **conditional strengthening** of the existing uniqueness/existence theorem, with no claim about arbitrary nonradial metrics.

**Proof.** The variational equation for the initial condition is \`J'=b_C(r,C)J\`, where \`b=kC^{1-m}+FC^{-m}\`. Direct differentiation gives
\[
 b_C=(1-m)kC^{-m}-mFC^{-m-1}
    =kC^{-m}-mC'/C.
\]
Since \`C(2)=C(0)\`, integrating over one period yields \`\int_0^2b_C=L(k,F)\`, hence the first boxed identity. Since \`e^L-1\ne0\`, the implicit function theorem applied to \`P(c;k,F)-c=0\` provides smooth periodic initial data for smooth parameter families; standard smooth ODE dependence then provides the asserted periodic \`C\`.

Differentiate \`C^mC'=kC+F\` in \`k\`; this gives \`(C^mH)'=kH+C\`. For \`Y=C^mH\`, the coefficient of its homogeneous equation is \`kC^{-m}<0\` and periodic, with multiplier \`e^L<1\`. Thus its unique periodic solution equals the displayed convergent whole-past variation-of-constants integral, whose integrand is everywhere positive. Therefore \`H>0\`. Differentiate \`L=k\int C^{-m}\` to obtain the third boxed identity; both terms are positive because \`k<0\` and \`H>0\`. The inverse-function assertion follows, and smooth dependence on a varying target period is another application of the one-dimensional implicit function theorem. No unproved interchange of net limits occurs: these are classical finite-dimensional parameter derivatives of smooth periodic ODE solutions.

For completeness, an input perturbation \`F+\varepsilon G\` at fixed \`k\` has \`Z=\partial_\varepsilon C|_0\` satisfying \`(C^mZ)'=kZ+G\`; the same positive periodic Green kernel shows \`G\ge0\implies Z\ge0\`. This is a local order-preserving response at fixed \`k\`, **not** an asserted fixed-Lee-period comparison.

**Affected dependents:** §23.2.41 (strengthened smooth dependence), §§23.2.43–45 (radial potential and non-Vaisman family). No source/body patch needed; optional note after Theorem 23.2.41. This relies only on the printed smooth ODE and its already established existence, not on a complete upstream global proof certificate.

## POME-HERMITIAN-TORSION-DOUBLEPRIME-GLYPH-001
**Severity: low. Status: confirmed error (formula transcription only, NOT a false Hermitian identity).** In the current integrated reading edition \`docs/sections/hermitian-torsion-and-the-bochner-identity/index.html\`:
- Physical **line 27**, equation (11.48.5), permanent combined equation tag \`8C926C4A6B4A\`, displays \`\delta ”\` (Greek delta followed by the U+201D RIGHT DOUBLE QUOTATION MARK) where the formal \`(0,1)\` adjoint must be \`\delta ''\`.
- Physical **line 162**, equation (11.48.18), permanent combined tag \`2F5B471E480A\`, displays \`\Delta ”\` where it must be \`\Delta ''\`.
- Both incorrect tokens occur a **second time** in standalone linked equation chunks on physical **line 247**, tags \`1E5D7A00D2DA\` and \`CC4EDB6E65CB\`. A direct exact-text check found **two** occurrences of each malformed token in this blob.

The correct operator identities are
\[
 [\Lambda,D']=i(\delta''+\bar\tau^*),\qquad
 \Delta_\tau=\Delta'_\tau+\Delta''.
\]
This follows from the operator definitions at §11.48 lines 7–20, the first two lines of (11.48.5), and the expansion and proof of (11.48.18) at lines 185–188. The U+201D glyph is not the notation for a double-prime. Proposed **separately reviewable presentation patch**: replace precisely the two instances of \`\delta ”\` with \`\delta ''\` and both instances of \`\Delta ”\` with \`\Delta ''\` in the generator/source of the continuous and standalone equation renderings; preserve all permanent tags and historical attribution. This is a display/transcription issue; **none** of Theorems 11.48.3 or 11.48.15 is thereby shown false. Affected readers of the torsion commutator identities and of the Bochner decomposition; downstream L² proof-completion was **not** reopened.

## Independent cross-chapter checks

**§10.103.1, permanent \`E897B72A71BA\`, lines 8–18.** The equality \`\chi(\mathcal H\otimes\rho)=\chi(\mathcal H)\` for coherent \`H\` on smooth projective \`Z\` and \`\rho\in\operatorname{Pic}^0(Z)\` uses finite locally free resolutions, additivity of Euler characteristic and constancy of the Dolbeault Fredholm index along a path of topologically trivial holomorphic line bundles. The argument correctly distinguishes invariance of the **alternating sum** from invariance of individual \`h^q\`; no new error established. The general local regularity/resolution and elliptic-index inputs are not claimed here as independently certified.

**§10.107.1–2, permanent \`BB9ADDF87BD1\` and \`1BF160484066\`, lines 11–45.** The reflexive tensor maximal-slope equality is explicitly **conditional** on the Kähler/movable tensor-semistability theorem attributed to Ou and Toma; this external input is already recorded in \`proofs/open-dependencies.json\` under \`movable-tensor-semistability\` and is **not** relogged as a newly discovered gap. The filtration proof treats codimension-two reflexive extensions and the corollary uses the \`q=2\` exterior power only for semistable \`G\`. The printed \`O(1)\oplus O(-1)\` example correctly rejects the unqualified maximal-exterior-slope identity. Historical credits retained. No new confirmed mathematical error here.

## Audit boundaries and status
- **New findings:** one verified conditional deduction; one confirmed transcription error. **Original false theorems found: zero. Complete upstream proof chains certified: zero.**
- Deferred-by-user material (Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas, positivity-loss completion programme) remains **deferred, not solved or certified**.
- No source, registry, permanent-tag, \`main\`, CI, GitHub Actions, build, test suite, or website publication was changed or run.
