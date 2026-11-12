# Countable rooftops and finite intersection of zero sets for ordinary models

**Date:** 2026-11-13. **Finding ID:** \`POME-ROOFTOP-COUNTABLE-MODEL-FIP-001\`.
**Classification:** low; **verified conditional deduction**. No false printed
statement has been found here. This note is a new countable-family corollary,
not an audit certification of all of §13.23 or its prerequisites.

## Immutable reviewed source

- Production \`main\`: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- Integrated reading page:
  \`docs/sections/volumes-under-bounded-mass--rooftops-and-capacity-convergence/index.html\`,
  blob \`2b0162752e9800061002119630703701c814a2ec\`.
- Finite rooftop Lemma 13.23.1, source
  \`non-kahler-pluripotential-theory:126FCF2C\`, permanent
  \`2B568CD72F9D\`: physical lines 10–42 (hypotheses 11–15,
  finite-level argument 20–42).
- Proposition 13.23.2, source \`non-kahler-pluripotential-theory:06C3A6D1\`,
  permanent \`1542F41C8A51\`: lines 49–90 (context only).
- Theorem 13.23.3, source
  \`non-kahler-pluripotential-theory:0A2EE475\`, permanent
  \`7D5F8FB5CFAB\`: lines 97–160, especially the verified finite-rooftop
  ordinary-model argument in line 112 and normalized decreasing models
  in line 157.
- Chapter assumptions in
  \`docs/sections/volumes-under-bounded-mass/index.html\` line 20:
  connected compact complex \(X\) of dimension \(n\ge1\) with the bounded
  mass property and big smooth real \((1,1)\)-form \(\theta\), not necessarily
  closed. The restricted curve-background change from §13.28 is irrelevant.
  Ordinary envelope facts are taken in the normalization \(P_\theta[u]\le0\).

## Derived countable-family theorem

Let \(w\in\operatorname{PSH}(X,\theta)\) with
\(\delta=\underline{\operatorname{vol}}_\theta(w)>0\).
Let \((u_j)_{j\ge1}\) be **normalized ordinary models**, i.e.
\(P_\theta[u_j]=u_j\), so \(u_j\le0\) and \(\sup_Xu_j=0\).
Assume \(u_j\preceq w\) for every \(j\), and
\[
 \sigma:=\sum_{j=1}^\infty\bigl(U(w)-U(u_j)\bigr)<\delta.
 \tag{1}
\]
Here \(U\) is the upper singularity volume of the integrated §13.23.
Then the countable rooftop
\[
 p:=P_\theta(u_1,u_2,\ldots)
   :=\sup\{v\in\operatorname{PSH}(X,\theta):v\le u_j
             \text{ for every }j\}
\]
is a well-defined **nontrivial normalized ordinary model**, and
\[
 p=\inf_{N\ge1}p_N,\qquad
 p_N:=P_\theta(u_1,\ldots,u_N),\qquad
 \sup_Xp=0,\qquad P_\theta[p]=p.
 \tag{2}
\]
In particular the models have a nonempty **common zero set**:
\[
 \varnothing\ne\bigcap_{j\ge1}\{u_j=0\}.
 \tag{3}
\]
The same conclusion holds, without (1) or \(w\), whenever each finite
rooftop \(p_N\) is known independently to be nontrivial. Thus (1) is a
sufficient *finite-intersection criterion*, not an asserted optimal one.

### Proof

**(a) Finite noncollapse.** All the deficits in (1) are nonnegative by
the monotonicity of upper singularity volume under \(\preceq\).
Every finite partial sum is at most \(\sigma<\delta\). Applying precisely
Lemma 13.23.1 to \(u_1,\ldots,u_N,w\) proves \(p_N\not\equiv-\infty\).
The lemma is a conditional *internal prerequisite* here: its original
analytic contact and mass estimates are not certified afresh.

**(b) Each finite rooftop is an ordinary model.** Because every
\(u_j=P_\theta[u_j]\) and \(p_N\le u_j\), the monotonicity of the ordinary
singularity envelope implies
\[
 p_N\le P_\theta[p_N]\le P_\theta[u_j]=u_j
 \quad (1\le j\le N).
\]
The first inequality uses \(p_N\le0\) as an admissible candidate for its
own singularity envelope. The middle expression is itself
\(\theta\)-psh; it is below all finite obstacles and hence below their
largest common minorant \(p_N\). Consequently \(P_\theta[p_N]=p_N\).
This is the same **finite-rooftop argument** explicitly printed in the
proof of Theorem 13.23.3, line 112; no extra global regularity premise
is being inserted. Moreover every nontrivial ordinary envelope has
maximum zero. Indeed, if \(\sup_Xp_N=-\varepsilon<0\), then
\(p_N+\varepsilon/2\le0\) has the same singularity type and is admissible
for \(P_\theta[p_N]=p_N\), an impossibility.

**(c) Compact zero-set argument.** Set
\(K_N=\{x\in X:p_N(x)=0\}\). Since each \(p_N\) is upper semicontinuous,
nonpositive and has supremum zero on the compact \(X\), \(K_N\) is
nonempty and compact. As \(p_{N+1}\le p_N\), these sets are nested.
Compactness yields \(x_*\in\bigcap_{N\ge1}K_N\). Thus
\(p_N(x_*)=0\) for all \(N\), and because \(p_N\le u_j\le0\) when
\(N\ge j\), also \(u_j(x_*)=0\) for every \(j\). This proves (3).

**(d) Limit and model identity.** The decreasing pointwise limit
\(p=\lim_Np_N\) is not identically \(-\infty\), since \(p(x_*)=0\).
The standard decreasing-limit theorem for local psh functions, applied
after adding local smooth potentials of \(\theta\), shows that \(p\)
is \(\theta\)-psh (decreasing upper semicontinuous limits are
upper semicontinuous). Every competitor \(v\le u_j\) for all \(j\)
lies below each \(p_N\), hence below \(p\); conversely \(p\le u_j\)
for every \(j\). Therefore \(p\) is exactly the countable rooftop,
with supremum zero. As \(p\le u_j\), the same envelope monotonicity as
in (b) gives
\(p\le P_\theta[p]\le u_j\) for all \(j\). The just-proved maximality
then gives \(P_\theta[p]\le p\), hence \(P_\theta[p]=p\).
This completes (2) and the theorem. No sequential compactness has
been substituted for a directed-net argument: only the explicitly
countable monotone sequence \(p_N\) is involved.

## Sharp limitation of a naive countable extension

The **normalized ordinary-model** hypothesis cannot simply be omitted
from this argument. On \(X=\mathbf P^1\) with a positive Kähler form
\(\theta\) and \(w=0\), choose \(u_j\equiv-j\).
Every \(u_j\) is a bounded \(\theta\)-psh potential, \(u_j\preceq w\),
and all \(u_j\) have the **same singularity type** as \(w\).
Thus \(U(w)-U(u_j)=0\) for every \(j\), the series in (1) is zero, and
\(\underline{\operatorname{vol}}_\theta(w)=\int_X\theta>0\).
Each finite rooftop exists but is
\(P_\theta(u_1,\ldots,u_N)\equiv-N\); consequently
\(\inf_Np_N\equiv-\infty\).
The functions \(u_j\) are *not* normalized ordinary models:
\(P_\theta[u_j]=0\ne u_j\). This refutes a countable analogue of
Lemma 13.23.1 based on summable deficits alone. It does **not**
refute that printed lemma, whose hypothesis explicitly concerns a
**finite** family.

One cannot infer from the present proof either that the countable
rooftop has a positive lower volume or that the entire §13.23
analytic dependency chain is certified. Those stronger conclusions
would require separate arguments, not silent limiting of finite mass
inequalities.

## Classification and follow-up

- **Finding:** \`POME-ROOFTOP-COUNTABLE-MODEL-FIP-001\`.
- **Severity / status:** low / **verified conditional deduction**, with
  an explicit scope counterexample for **non-model** obstacles;
  no confirmed error in Lemma 13.23.1, Proposition 13.23.2 or
  Theorem 13.23.3.
- **Proposed correction:** optionally add the above countable-model
  corollary after Lemma 13.23.1; do **not** replace its finite-family
  statement by an unrestricted countable-family assertion.
- **Potential dependents:** §13.23.3's decreasing model rooftops;
  §13.22.7's model-completeness construction; §13.21.2's monotone
  model limits. The deduction does not certify any of these in full.
- **Genuine dependencies:** finite rooftop noncollapse
  (Lemma 13.23.1), ordinary-envelope monotonicity and fixed-point
  characterization (§13.19 and line 112 of §13.23.3), and the standard
  decreasing-limit theorem for psh functions. No cited historical
  attribution is reclassified as a proof input.
- **Scope:** no Demailly approximation/regularization, Bergman,
  \(L^2\), Ohsawa–Takegoshi, multiscale-atlas or positivity-loss
  proof-completion is reopened. Older notes on those topics remain
  **deferred-by-user**, not verified.
- **Verification performed:** explicit analytic proof and exact constant
  translation counterexample; inspection of integrated statement and
  relevant printed proof anchors. **No build, tests, CI, website
  publication, repository source edits or full-project theorem
  certification performed.**
