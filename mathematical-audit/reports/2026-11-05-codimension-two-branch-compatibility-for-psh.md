# Codimension-two PSH upper bounds do not imply extension on a reduced non-unibranch space

- **Date:** 2026-11-05.
- **Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Stable ID:** `POME-REDUCED-CODIM2-PSH-NONDESCENT-001`.
- **Status:** **verified conditional deduction** (complete explicit counterexample to an **unprinted strengthening**, not a false theorem).
- **Severity:** low (hypothesis-boundary clarification); no production proof or theorem is being marked erroneous.
- **Actual mathematical coverage:** newly checked Definition 9.9.1, Lemma 9.9.2(2), Proposition 9.9.4's exact codimension hypothesis, and the *necessity* of the unibranch hypothesis in the codimension-two clause of Theorem 9.10.14, by a completely explicit two-dimensional analytic-space model. These are selected checks, not certification of either section.

## Source and reading-edition anchors

1. `docs/sections/complex-spaces-and-modifications--plurisubharmonic-functions-on-reduced-spaces/index.html`, blob `d9d8091b530c9843e5a725b49af2400936aeaa3a` on the reviewed `main`: Definition **9.9.1**, physical line **11**, source label `foundations-of-pluripotential-theory:025047FB`, permanent tag `7A62ADAFC2A7`; Lemma **9.9.2**, lines **19–41**, source `foundations-of-pluripotential-theory:45AEDF34`, permanent `83D4170FB2B3`; Proposition **9.9.4**, lines **63–89**, source `foundations-of-pluripotential-theory:A6674849`, permanent `B43080BD49F3`.
2. `docs/sections/pluripotential-theory-on-unibranch-spaces/index.html`, blob `6edfa6b19fa7cdbaf0c2665389fa7b3ca338cdf4`: Theorem **9.10.14 (Grauert–Remmert)**, lines **140–156**, source `sgpt:EEFC0C9A`, permanent `C69D2F0ABA4F`. Its existing footnote (physical line **155**) already gives a **one-dimensional**, hence codimension-*one*, two-branch warning. The present calculation strengthens the obstruction to codimension **two on every irreducible branch**. Theorem **9.10.5**, lines **39–69**, supplies connected fibers in the unibranch case (context only).
3. The chapter's actual current table of contents places these in §§9.9 and 9.10. No manuscript/source, permanent tag, reader locator or attribution is altered.

## Exact model and statement

Write coordinates on `\mathbb C^4` as `(z_1,z_2,w_1,w_2)` and let

```math
P_z=\{w_1=w_2=0\},\quad P_w=\{z_1=z_2=0\},\quad
X=P_z\cup P_w,\quad A=P_z\cap P_w=\{0\}.
```

The ideal `(w_1,w_2)\cap(z_1,z_2)` is radical, so `X` is a **reduced**, pure two-dimensional complex analytic space with exactly two smooth irreducible components. The singleton `A` is analytic and has complex codimension **two in each irreducible branch at its sole point**; thus it satisfies the **precise** hypothesis of Proposition 9.9.4.

For arbitrary `a,b\in\mathbb R`, define `u_{a,b}:X\setminus A\to\mathbb R` by

```math
u_{a,b}|_{P_z\setminus\{0\}}=a,\qquad
u_{a,b}|_{P_w\setminus\{0\}}=b.
```

Because `P_z\setminus A` and `P_w\setminus A` are disjoint open complex submanifolds of `X\setminus A`, these constant functions are locally plurisubharmonic under Definition 9.9.1. Both components carry finite values, so they also satisfy the nontriviality convention of `\mathrm{PSH}(X\setminus A)`. Moreover, `u_{a,b}` is *globally bounded* between `\min(a,b)` and `\max(a,b)`. In particular, the upper-bound conclusion of Proposition 9.9.4 is satisfied in the strongest possible way.

**Claim.** There exists a locally plurisubharmonic extension `U:X\to[-\infty,+\infty)` of `u_{a,b}` **if and only if** `a=b`.

### Complete proof

If `a=b=c`, the constant `U=c` is a globally ambient plurisubharmonic extension.

Conversely, suppose `U` is a locally plurisubharmonic extension. Consider two holomorphic discs through the common origin,

```math
\gamma_z(t)=(t,0,0,0),\qquad
\gamma_w(t)=(0,0,t,0),\qquad |t|<\epsilon.
```

By Lemma 9.9.2(2), each pullback `U\circ\gamma_z`, `U\circ\gamma_w` is subharmonic (or identically `-\infty`) on a disc. The first equals `a` on the punctured disc; the second equals `b` there. For a subharmonic function `v` equal to a finite constant `c` outside the center, upper semicontinuity gives `v(0)\ge c` and the submean inequality on every centered circle gives `v(0)\le c`; thus **`v(0)=c`**. Neither pullback can be identically `-\infty`, because its punctured values are finite. Consequently `U(0)=a` and simultaneously `U(0)=b`, forcing `a=b`.

In particular, when `a<b`, assigning `U(0)=b` produces an *upper semicontinuous* extension of the bounded function. But its pullback along `\gamma_z` violates the submean inequality, so upper semicontinuity and boundedness do **not** suffice for ambient local plurisubharmonic extension on this space.

The normalization of `X` is the disjoint union `P_z\sqcup P_w`. Each constant extends uniquely as a PSH function on its smooth normalization component, but the two resulting values at the distinct points of the normalization fiber over `0` are `a` and `b`. They **fail to descend** exactly when `a\ne b`. This identifies the branch-compatibility obstruction, independently of any approximation argument.

## Mathematical classification and dependencies

- **Correct original propositions:** Proposition 9.9.4 asserts only a local **upper bound**, not removal of the singular set; Definition 9.9.1 and Lemma 9.9.2(2) are consistent with the model. Theorem 9.10.14 requires **unibranchness** and is also not contradicted because this `X` is not unibranch at `0`.
- **New information versus the printed footnote:** the existing §9.10.14 footnote has two copies of `\mathbb C` crossing at a point, where the omitted point has *codimension one*. Here the omitted set has **codimension two on both two-dimensional branches**, so even the stronger codimension hypothesis of the theorem cannot replace unibranchness. The exact `a=b` criterion and normalization-fiber explanation are supplied.
- **Used dependencies:** only the local embedded PSH definition and its disc-pullback implication; the latter can also be proved immediately by restricting an ambient PSH extension. No Demailly regularization, Bergman argument, weighted `L^2`, OT, multiscale atlas or positivity-loss programme is used.
- **Affected dependents:** any proposed extension of §9.10.14 to arbitrary **reduced** spaces under a codimension-two hypothesis, or an attempted implication “§9.9.4 upper boundedness => removable PSH singularity”, would be false. There is **no identified invalid printed dependent**.
- **Proposed optional patch (not applied):** after Proposition 9.9.4, insert a warning that a local upper bound is not a removable-singularity theorem on arbitrary reduced complex spaces; cite the two-plane model and retain the historical attribution to Grauert–Remmert and the existing §9.10.14 footnote. Do not weaken the printed unibranch condition.
- **Still open:** the full general proof of Proposition 9.9.4 via finite projections, the Fornaess–Narasimhan disc criterion, Grauert–Remmert existence on arbitrary unibranch spaces, and all other mathematical statements in §§9.9–9.10. No complete section has been certified.

No builds, CI, formal checks, source changes, registry edits, website publication or tests are claimed.
