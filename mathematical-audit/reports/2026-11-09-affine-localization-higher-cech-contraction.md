# Affine localization Čech contraction in every positive degree

**Finding:** POME-AFFINE-CECH-ALL-DEGREES-001 — **low / verified conditional deduction**. The printed Proposition 9.58.3 is correct; this is an additional, self-contained higher-degree consequence, **not** a repair of a false theorem and **not** a certification of arbitrary sheaf cohomology.

## Pinned reading-edition target

Production main: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

- \`docs/sections/finite-type-algebraic-models-and-analytic-structure-sheaves--finite-type-models-and-nilpotent-structure/index.html\`, blob \`96eb7c1f6ee63ce6d222ed3f608a242a0a64b7f0\` (physical lines 11–61).
- Theorem 9.58.2: source \`demailly-complex-geometry:3F3FF286\`, permanent tag \`36502A11961A\`, physical lines 11–32. We use its maximal-ideal/Nullstellensatz clause to recognize a finite principal-open cover.
- Proposition 9.58.3: source \`demailly-complex-geometry:5EF3B92E\`, permanent tag \`72F3ADBDFF9A\`, physical lines 34–61; the proof of the degree-zero sheaf gluing assertion is in lines 42–59. The new result concerns *positive* Čech degrees, not asserted in the printed proposition.
- §9.59 is a possible application to closed subschemes and products; it was not reverified in this pass.

## Exact statement and independent proof

Let \(A\) be **any commutative ring**, possibly nonreduced or containing zero divisors. Take finitely many elements \(t_1,\ldots,t_s\) such that \((t_1,\ldots,t_s)=A\). For \(I=(i_0,\ldots,i_q)\), write \(t_I=\prod_{j=0}^q t_{i_j}\), and let
\[
  C^q=\prod_{1\le i_0<\cdots<i_q\le s} A_{t_I}
\]
with the usual alternating Čech differential and the localization restriction maps. Then
\[
     H^q(C^\bullet)=0 \qquad \text{for every integer }q\ge1.
\]
For a finite-type algebra over an algebraically closed field, the condition that the \(D(t_i)\) cover \(\operatorname{Spm}A\) is equivalent to \((t_i)=A\): otherwise a maximal ideal contains all the \(t_i\). The Čech modules above are *exactly* the sections supplied by Proposition 9.58.3 on the corresponding multiple intersections.

**Proof.** Fix \(q\ge1\) and a \(q\)-cocycle \(c=(c_I)\), extended antisymmetrically to arbitrary ordered lists (zero for a repeated index). For each ordered \(q\)-tuple \(J=(j_1,\ldots,j_q)\) and \(i\), the element \(c_{iJ}\) lies in \(A_{t_i t_J}\). Since this is a localization of \(A_{t_J}\) at \(t_i\), some power \(t_i^{N_0}c_{iJ}\) is represented by an element \(d_{iJ}\in A_{t_J}\). Finitely many tuples occur, so \(N_0\) can be chosen uniformly.

For a tuple \(I=(i_0,\ldots,i_q)\), the cocycle relation on \(A_{t_i t_I}\) reads
\[
  \sum_{r=0}^q(-1)^r c_{i,I\setminus i_r}=c_I.
\]
Consequently
\[
 e_{iI}:=\sum_{r=0}^q(-1)^r d_{i,I\setminus i_r}-t_i^{N_0}c_I\in A_{t_I}
\]
vanishes **after** inverting \(t_i\). It need not yet vanish in \(A_{t_I}\) if \(t_i\) is a zero divisor. By the defining property of localization there is \(M_{iI}\) with \(t_i^{M_{iI}}e_{iI}=0\) already in \(A_{t_I}\). Choose one \(M\) working for the finitely many pairs \((i,I)\), set \(N=N_0+M\), and replace \(d_{iJ}\) by \(t_i^M d_{iJ}\). We now have the **exact identity in \(A_{t_I}\)**:
\[
   \sum_{r=0}^q(-1)^r d_{i,I\setminus i_r}=t_i^N c_I.
\]

Because \((t_1,\ldots,t_s)=A\), the powers also generate the unit ideal: \((t_1^N,\ldots,t_s^N)=A\) (expand a sufficiently large power of \(\sum a_it_i=1\), or exclude maximal ideals). Choose \(a_i\in A\) with \(\sum_i a_it_i^N=1\). Define
\[
   b_J=\sum_{i=1}^s a_i d_{iJ}\in A_{t_J}
   \qquad (|J|=q).
\]
Then in every \(A_{t_I}\),
\[
  (\delta b)_I
    =\sum_i a_i\sum_{r=0}^q(-1)^r d_{i,I\setminus i_r}
    =\sum_i a_it_i^N c_I=c_I.
\]
Thus \(c=\delta b\). This proves all positive-degree Čech acyclicity, with **no** reduction, domain, smoothness, Noetherianity or characteristic assumption. The explicit extra step annihilating the \(e_{iI}\) is essential: identities only valid after localization cannot simply be asserted in \(A_{t_I}\) when there are zero divisors.

**Concrete nilpotent check.** In \(A=k[x,\varepsilon]/(\varepsilon^2)\), \(D(x)\) and \(D(1-x)\) cover \(\operatorname{Spm}A\), since \(x+(1-x)=1\). The Čech 1-cocycle
\[
 c_{12}=\frac{\varepsilon}{x(1-x)}\in A_{x(1-x)}
\]
is the coboundary of \(b_1=-\varepsilon/x\in A_x\) and \(b_2=\varepsilon/(1-x)\in A_{1-x}\), as \(b_2-b_1=c_{12}\). The construction does not discard the nonzero nilpotent \(\varepsilon\).

## Classification, limits, and proposed integration

- **Severity/status:** low / **verified conditional deduction**. Neither Theorem 9.58.2 nor Proposition 9.58.3 is false; there is no demonstrated gap in their printed degree-zero arguments.
- **Precise novelty:** an explicit contracting coboundary in **every positive degree** for finite principal covers of the localization structure sheaf, including zero-divisor torsion clearance. This is different from the earlier point-supported-sheaf Čech calculation \`POME-POINT-SHEAF-FINITE-CECH-ACYC-001\` in §10.78 and from Proposition 9.58.3's printed gluing proof.
- **Proposed addition:** an optional separately tagged lemma/remark after Proposition 9.58.3 giving the higher Čech contraction; preserve all original source labels, authorship, historical attribution, and permanent tags.
- **Affected possible dependents:** affine chart and closed-subspace calculations in §9.59 and local analytic/algebraic model comparisons in §9.60 **if** they require finite-principal-cover Čech exactness. No statement there is claimed repaired or proved by this observation alone.
- **Open boundary:** exactness of this *specific Čech complex* is not, without an additional comparison/acyclic-cover theorem, a proof of arbitrary sheaf-cohomology vanishing. No broader Cartan/Serre, projective, or analytic vanishing statement has been verified.
- The user-excluded Demailly regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-gluing and positivity-loss programme remains **deferred-by-user**, neither solved nor revisited. This proof is entirely elementary commutative algebra and does not enter that programme.

## Actual coverage and verification

A new, direct mathematical review of the *higher-degree localization consequence* of §9.58.3, together with its printed degree-zero proof, nullstellensatz cover criterion and source/permanent identifiers. §9.58 had been previously sampled, so **zero first-visited numbered sections**; §9.59 only an affected-dependent note, **not** re-audited. Actual main ToC / matrix: **25 chapters, 747 numbered sections, zero completely certified sections**. No full upstream project verification. No builds, tests, Actions, website publishing, source changes, registry changes or tag changes performed.
