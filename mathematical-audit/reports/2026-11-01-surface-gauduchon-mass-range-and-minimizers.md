# Surface Gauduchon volume ranges and exact optimizer dichotomy

Date: 2026-11-01. Reviewed main SHA: b6933b772f41b45918f7e25ed1afbbb1fd892272.

Finding: **POME-GAUD-SURFACE-VOLUME-RANGE-OPTIMIZERS-001 — low / verified conditional deduction**. No false theorem or completed production repair is asserted.

## Exact integrated anchors and prior work

- Proposition 12.15.2, source non-kahler-pluripotential-theory:F87A9477, permanent D26C76DEC922: docs/sections/a-gauduchon-variational-volume--varying-the-probability-measure/index.html, main blob 440964738faf623f2e0942bbc7fd21d5f2a3ed69, physical lines 33–49. Its smooth normalized equation identifies the set of smooth measure-volumes with the set of smooth strictly positive potential masses. The pluriclosed surface special case is mentioned at line 54.
- Proposition 12.15.6, source non-kahler-pluripotential-theory:6834DDEA, permanent 87CB9377C0BB, same path and blob, lines 98–118. Its first variation and Gauduchon-minimizer characterization were directly inspected. Equation 12.15.5 has permanent tag AE720210AADD (lines 69–72).
- Theorem 12.2.3, source non-kahler-pluripotential-theory:876DF057, permanent 2DB664A6EFDF: docs/sections/a-gauduchon-variational-volume--the-quotient-and-the-smooth-equation/index.html, main blob 9ec67161d46b3ba20afa1b1c9a0c84f29322763e, lines 49–80. Its smooth equation and equality-case minimizers are *internal conditional inputs*, not independently certified here; it cites smooth existence Theorem 14.2.1.
- The earlier finding POME-GAUD-SURFACE-MASS-PLURICLOSED-001 (source non-kahler-pluripotential-theory:538AA05F, permanent 881C26425D7A, §12.1) already established the affine Stokes mass formula below. That earlier identity is not registered again as a new discovery.

**User exclusion honored:** The regularization-of-bounded-potentials passage at §12.15.4, line 81, is NOT inspected or invoked. No Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss programme is reopened.

## A precise interval alternative on compact complex surfaces

Let \(X\) be a connected compact complex surface and \(\omega\) a smooth Hermitian form. Define
\[
 {\cal A}_\omega=\{v\in C^\infty(X,\mathbb R):\Omega_v=\omega+dd^cv>0\},\quad
 M(v)=\int_X\Omega_v^2,\quad I_\omega=M({\cal A}_\omega).
\]
The admissible set is nonempty (zero belongs), convex, and open in the smooth \(C^2\)-topology by compact strict positivity. The already-checked Stokes formula is
\[
 M(v)=\int_X\omega^2+2\int_X v\,dd^c\omega. \tag{1}
\]
Indeed \((dd^cv)^2=dd^c(v\,dd^cv)\), and integration by parts gives \(\int\omega\wedge dd^cv=\int v\,dd^c\omega\).

**New range assertion:** If \(dd^c\omega=0\), \(I_\omega=\{\int\omega^2\}\). If \(dd^c\omega\ne0\), \(I_\omega\) is a nonempty *nondegenerate open interval* contained in \((0,+\infty)\); neither its infimum nor a finite supremum is attained by any admissible potential. Every mass in that interval has both a smaller and a larger attainable mass.

**Proof.** If \(dd^c\omega\ne0\), choose smooth real \(f\) with
\[
 c=2\int_X f\,dd^c\omega>0.
\]
For any admissible \(v\), compact strict positivity of \(\Omega_v\) allows \(v+tf\) for every sufficiently small signed \(t\), and (1) gives the *exact* formula
\[
 M(v+tf)=M(v)+ct. \tag{2}
\]
Hence every point of \(I_\omega\) is interior. Since \({\cal A}_\omega\) is convex and \(M\) affine, \(I_\omega\) is an interval; (2) proves it is nondegenerate, open, and has no attained endpoints. Positivity of \(\Omega_v^2\) gives \(I_\omega\subset(0,\infty)\). This does NOT classify the finite/infinite endpoints.

**Smooth probability-measure volume consequence (conditional on the integrated smooth equation).** For every \(v\in{\cal A}_\omega\), put \(\mu_v=\Omega_v^2/M(v)\); this is a smooth positive probability measure and Proposition 12.15.2 gives \({\cal V}_{\mu_v}(\omega)=M(v)\). Conversely Theorem 12.2.3 supplies for every such \(\mu\) a smooth admissible solution whose mass equals \({\cal V}_{\mu}(\omega)\). Thus the set of smooth measure-volumes is **exactly** \(I_\omega\). If \(dd^c\omega\ne0\), for *each* smooth \(\mu\) there exist smooth probabilities \(\mu_-,\mu_+\) for which
\[
 {\cal V}_{\mu_-}(\omega)<{\cal V}_{\mu}(\omega)<{\cal V}_{\mu_+}(\omega).
 \tag{3}
\]
Construct them from the signed perturbations \(v\pm tf\) of the normalized solution \(v\) as above. This uses neither the nonsmooth masses \(v_\pm(\omega)\) nor the excluded regularization step.

## All smooth Gauduchon-quotient minimizers

For a smooth Gauduchon metric \(\gamma\) on \(X\), let
\[
 Q_\omega(\gamma)=\frac{\int_X\omega\wedge\gamma}
              {(\int_X\gamma^2)^{1/2}},\qquad
 \mu_\gamma=\frac{\gamma^2}{\int_X\gamma^2}.
\]
Recall from Theorem 12.2.3 the fixed-density quotient
\(\lambda_\mu(\omega)=\inf_{\eta\ {\rm Gauduchon}}\int\omega\wedge\eta/D_\mu(\eta)\),
where \(D_\mu(\eta)=\int(\mu/\eta^2)^{1/2}\eta^2\).
Hölder, for **every** Gauduchon \(\eta\), gives
\[
 D_{\mu_\gamma}(\eta)\le(\int_X\eta^2)^{1/2},
\]
with equality at \(\eta=\gamma\). The numerator is positive. Therefore
\[
 \inf_\eta Q_\omega(\eta)\le
 \lambda_{\mu_\gamma}(\omega)\le Q_\omega(\gamma). \tag{4}
\]

**If \(dd^c\omega\ne0\), the infimum of \(Q_\omega\) is not attained.**
Indeed, if \(\gamma_0\) minimizes \(Q_\omega\), (4) forces
\(\lambda_{\mu_{\gamma_0}}(\omega)=Q_\omega(\gamma_0)\).
By the *smooth* equality case of Theorem 12.2.3, \(\gamma_0\) is conformal to a smooth normalized solution \(\Omega=\omega+dd^cu>0\), with
\(\Omega^2=c_\omega(\mu_{\gamma_0})\,\mu_{\gamma_0}
 =c_\omega(\mu_{\gamma_0})\gamma_0^2/\int_X\gamma_0^2\).
The conformal factor must be **constant**, since the volume-form ratio is constant and positive in complex dimension two. Hence \(\Omega\) is a constant multiple of the Gauduchon metric \(\gamma_0\), so \(dd^c\Omega=0\). But \(dd^c\Omega=dd^c\omega\ne0\), contradiction. No assertion that the unattained infimum is positive or zero is required.

**If \(dd^c\omega=0\), the minimizers are precisely**
\[
 \underset{\gamma\ {\rm Gauduchon}}{\operatorname{argmin}}\,Q_\omega(\gamma)
   =\{a(\omega+dd^cv):a>0,\ v\in{\cal A}_\omega\},
 \qquad
 \min_\gamma Q_\omega(\gamma)=\left(\int_X\omega^2\right)^{1/2}. \tag{5}
\]
Proof: write \(M_0=\int\omega^2\). Formula (1) and smooth normalized solvability imply
\(\lambda_{\mu_\gamma}(\omega)=\sqrt{M_0}\) for each \(\gamma\).
Then (4) gives \(Q_\omega(\gamma)\ge\sqrt{M_0}\).
Every \(\Omega_v>0\) is Gauduchon because \(dd^c\Omega_v=dd^c\omega=0\);
Stokes gives \(\int\omega\wedge\Omega_v=\int\Omega_v^2=M_0\), so
\(Q_\omega(\Omega_v)=\sqrt{M_0}\), as does every positive constant multiple.
Conversely, if \(\gamma\) attains this value, equality in (4) makes it a minimizer of its fixed-density quotient. Theorem 12.2.3 again makes it conformal to the corresponding normalized \(\Omega=\omega+dd^cu\), and proportionality of their volume forms makes the conformal factor constant. Thus every minimizer is of the stated form. This proves (5).

## Verdict, proposed correction, and actual coverage

**Severity/status:** low / verified conditional deduction. The affine mass-range proof is elementary and complete; the complete quotient-minimizer classification is a correct deduction **conditional on the existing smooth elliptic equation and quotient equality case**, which were checked only as statements and selected proof steps, not completely independently re-proved. No theorem has been falsified or repaired in production.

**New versus old:** previous POME-GAUD-SURFACE-MASS-PLURICLOSED-001 already gives equation (1) and its constant-mass criterion. The **new** content is the open range and strict two-sided realization, and the exact Gauduchon quotient attainment/nonattainment classification, obtained without the excluded nonsmooth approximation theorem. Proposed optional surface corollary following Proposition 12.15.6, preserving the original history, source labels, numbered clauses, and permanent tags.

**Affected dependents:** smooth fixed-density and Gauduchon variational arguments §§12.2–12.6 and §§12.15–12.16, and surface mass comparisons in §§11.1–11.4. These are not claimed reviewed. **Actually examined:** first new selected proof-level pass of Proposition 12.15.6 (lines 98–118) and direct smooth-only realization of Proposition 12.15.2 and Theorem 12.2.3, plus consistency of the quotient. §12.15 was previously partially examined, so this is incremental, not first section coverage or a complete chain certificate.

Current main table of contents: **25 chapters, 747 numbered sections, zero whole mathematical sections certified**. Older errors/gaps/dependencies remain at their previous statuses. Demailly regularization and all dedicated excluded proof programmes remain **deferred-by-user**, never resolved; no source/reader/registry/tag/main/site/build/CI/formalization change has been made or requested in this finding.
