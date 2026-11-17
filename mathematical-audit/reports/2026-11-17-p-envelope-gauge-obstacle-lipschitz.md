# Smooth gauge changes of P-envelopes: exact obstacle covariance and sharp bounds

**Date:** 2026-11-17. **Finding:** POME-PENV-GAUGE-OBSTACLE-SHARP-001.  
**Classification:** low / verified conditional deduction. **No error in the printed proposition.** This is a quantitatively sharp refinement of Proposition 16.3.8, not a new proof of all of Chapter 16.

## Precise integrated source and scope

- Reviewed production main commit: b6933b772f41b45918f7e25ed1afbbb1fd892272.
- Section 16.2 standing assumptions: docs/sections/the-envelope-operators--p-envelopes/index.html; blob 912f81b3bccf3e1ead96fd18005261a708dfcb4e; source sgpt:189A8E0C; section permanent A6FA63C034E6; physical line 7: connected compact Kähler manifold.
- Section 16.3 integrated file: docs/sections/the-envelope-operators--p-envelopes--rooftop-operator-and-the-definition-of-the-p-envelope/index.html; blob 97681f31628eb362950837daaadde67d10507a2f.
- Definition 16.3.4, source sgpt:15C6153F / permanent 395DB7860949; defining formula (16.3.5), source sgpt:E4924BB8 / permanent 7E001B03F24A, physical lines 79–85.
- Proposition 16.3.8, source sgpt:EBC14D0B / permanent EF5AC4B19C4D, physical lines 108–133: invariance of *singularity type* under \(\theta'=\theta+dd^cg\), \(\varphi'=\varphi-g\); existing proof uses boundedness of \(g\).
- Definition 16.7.1, source sgpt:410CBDE6 / permanent 3E4D57445698, defines \(u\preceq v\) iff \(u\le v+C\). Only the definition is used; no additional regularity theorem is invoked.

## Exact claim

Let \(X\) be connected compact Kähler, \(\theta\) smooth closed real \((1,1)\)-form with a nonempty \(\mathrm{PSH}(X,\theta)\), \(\varphi\in\mathrm{PSH}(X,\theta)\), and \(g,h\in C^\infty(X,\mathbb R)\). Define the obstacle-constrained singularity envelope
\[
Q_\theta(g;\varphi)=
\left(\sup\{\psi\in\mathrm{PSH}(X,\theta):
             \psi\le g,\ \psi\preceq\varphi\}\right)^* .
\]
The competitor set is nonempty, since \(\varphi-C\le \min(g,h)\) for a sufficiently large constant \(C\). All envelopes below use upper-semicontinuous regularization.

**(A) Exact gauge transformation.** With \(\theta'=\theta+dd^cg\), \(\varphi'=\varphi-g\),
\[
\boxed{Q_\theta(g;\varphi)=g+P_{\theta'}[\varphi-g].}
\]
This is an exact identity of upper-semicontinuous extended-valued functions, not merely equivalence of singularity types.

**(B) Order-Lipschitz dependence on the obstacle.** If \(\delta=\|g-h\|_{C^0(X)}\), then
\[
\boxed{Q_\theta(h;\varphi)-\delta\le Q_\theta(g;\varphi)
               \le Q_\theta(h;\varphi)+\delta.}
\]
In particular, writing \(m=\min_Xg\), \(M=\max_Xg\), one has
\[
\boxed{P_\theta[\varphi]+m\le
 g+P_{\theta'}[\varphi-g]\le P_\theta[\varphi]+M.}
\]
These are inequalities in the extended-real order: at a polar point both sides may equal \(-\infty\). They should NOT be restated using an undefined pointwise subtraction of two \(-\infty\) values.

**(C) Simultaneous sharpness, and no constant-valued gauge correction.** On \(X=\mathbb P^1\), let \(\theta=\omega_{\mathrm{FS}}>0\), \(\varphi=0\), and choose any nonconstant smooth real \(h\) on \(X\). For a sufficiently small \(\varepsilon>0\), \(g=\varepsilon h\) satisfies \(\theta'=\theta+dd^cg>0\). Then
\[
 P_\theta[0]=0,\quad P_{\theta'}[-g]=0,\quad
 Q_\theta(g;0)=g.
\]
Consequently the bounds in (B) attain equality at minimum and maximum points of \(g\), respectively; neither universal constant \(m\) nor \(M\) can be improved. Moreover, the tempting strengthened identity
\(P_{\theta'}[\varphi-g]=P_\theta[\varphi]-g+c\)
for a constant \(c\) fails as soon as \(g\) is nonconstant, even when both forms are Kähler and the input potential has minimal singularities.

## Complete proof of the new statements

For (A), the bijection \(\psi\mapsto\psi-g\) sends \(\mathrm{PSH}(X,\theta)\) onto \(\mathrm{PSH}(X,\theta')\), because
\(\theta'+dd^c(\psi-g)=\theta+dd^c\psi\).
The ordinary singularity comparison is unchanged:
\(\psi\preceq\varphi\) iff \(\psi-g\preceq\varphi-g\), directly from Definition 16.7.1. Finally \(\psi\le g\) iff \(\psi-g\le0\). Therefore the candidate families agree after this bijection. Upper regularization commutes with addition of a continuous function \(g\), yielding (A).

For (B), \(g\le h+\delta\). Every \(\theta\)-psh candidate \(\psi\le g\) has \(\psi-\delta\le h\) and unchanged singularity preorder. It follows that \(\psi\le Q_\theta(h;\varphi)+\delta\). Take the supremum and its upper-semicontinuous regularization. Interchange \(g,h\) for the opposite inequality. For constant obstacles, translating every candidate establishes \(Q_\theta(c;\varphi)=P_\theta[\varphi]+c\) exactly. Since \(m\le g\le M\), monotonicity of candidates proves the displayed bound; alternatively use (B) twice.

For (C), \(\omega_{\mathrm{FS}}\) is positive, and \(dd^ch\) is a bounded smooth real \((1,1)\)-form on the compact manifold, so \(\omega_{\mathrm{FS}}+\varepsilon dd^ch>0\) for sufficiently small \(\varepsilon\). If \(\eta\) is a smooth Kähler form and \(\chi\) is a bounded \(\eta\)-psh potential, every \(\eta\)-psh candidate for \(P_\eta[\chi]\) is \(\le0\), whereas \(0\) itself is a candidate because \(0\preceq\chi\) (boundedness of \(\chi\)). Hence \(P_\eta[\chi]=0\). Apply this first to \((\eta,\chi)=(\theta,0)\), then to \((\theta',-g)\). Identity (A) gives \(Q_\theta(g;0)=g\) and shows sharpness at both extrema. If an additive-constant identity held, it would imply \(0=-g+c\), contradictory to nonconstancy.

## Mathematical and dependency classification

- **Status:** verified conditional deduction, **not** confirmed error, genuine duplication, or complete verification of Section 16.3.
- **Printed Proposition 16.3.8:** correct. Its equivalence \(\sim\) cannot be strengthened to a fixed additive-constant *function identity* after transporting the potential by \(-g\).
- **Inputs actually used:** the defining candidate families, Definition 16.7.1, elementary \(\theta\)-psh inequalities and USC regularization under continuous addition, compactness to bound \(g\), plus the elementary Kähler positivity perturbation in the sharpness test. No Demailly regularization, Bergman/L2/OT, approximation, or mass-continuity theorem is involved.
- **Suggested optional exposition:** after Proposition 16.3.8, state the exact obstacle covariance and sharp comparison above; make clear that the correct assertion is a two-sided *order* bound, not an identity modulo a scalar. No production-text change made.
- **Affected dependents to audit, not alleged errors:** Section 16.4 (background variation), §16.7 (ordinary singularity preorder), subsequent energy and metric comparisons where a smooth change of representative is used. No claim about global \(d_S\) estimates or Monge–Ampère mass under a varying obstacle is made.
- **Prior audit findings:** unchanged. User-excluded Demailly regularization/approximation and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain **deferred-by-user**, not resolved or certified.

## Coverage accounting

- Newly inspected *mathematical* substatements: §16.3.4 defining candidate family, §16.3.8 change-of-background proof and precise sharp strengthening, §16.7.1 preorder definition; §16.2 standing compact Kähler assumption checked.
- §16.3 already had partial substantive audit; §16.2 is only a standing-assumptions/heading page. **First-time fully proof-reviewed numbered sections: 0. Complete-section certifications: 0.** The full theorem chains of §§16.3/16.4/16.7 remain open.
- Current main ToC freshly read: **25 chapters, 747 numbered sections**.
- Audit note only: no CI, build, publication, source-body, registry, canonicalization, or permanent-tag changes.
