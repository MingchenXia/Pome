# Mathematical audit: reducibility in null foliations and cotangent tensors over rationally connected fibers

**Date:** 2026-10-28 (Asia/Shanghai).
**Pinned current production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Starting audit branch:** \`a75651e5fdedfb2aee64a6f344715ab19d9072ad\`.
**Scope:** only the integrated reading edition at the specified physical lines. No source publication, canonicalization, Demailly approximation/regularization, dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss work is attempted.

## POME-NULL-ALPHA-REDUCIBILITY-001

**Severity:** low. **Status:** verified conditional deduction (an exact countermodel to a *hypothesis-deleted extension*, not an error in the printed proposition).

**Reading locus:** \`docs/sections/integral-leaves-of-constant-rank-null-distributions/index.html\`, main blob \`564667ab5d008b0ffa1d29f5b7ecc578c19d2f04\`, physical lines 83–107, especially Proposition **7.15.4**, source \`klimek-pluripotential-theory:3B18B0CF\`, permanent tag \`992E9692EF3B\`. The printed independent warning, Example **7.15.5** (source \`klimek-pluripotential-theory:D21B8572\`, permanent tag \`849194DD5398\`), appears at lines 114–120 and removes *semipositivity of β*, not reducibility of α. The complex-kernel calculation is in Theorem **7.15.3**, source \`klimek-pluripotential-theory:FB2152E8\`, tag \`8FE75D79B9CA\`, lines 50–79.

**Verified countermodel.** On \(\mathbb C^3\), consider the constant complex \((1,1)\)-form and real semipositive \((1,1)\)-form
\[
 \alpha=\frac{i}{2}\,dz_1\wedge d\bar z_2,\qquad
 \beta=\frac{i}{2}\,dz_3\wedge d\bar z_3.
\]
Both are smooth and closed. Take \(p=q=1\). The three exterior-power tests in Proposition 7.15.4 **all** hold:
\[
 \alpha\wedge\beta\ne0,\qquad \alpha^2=0,\qquad
 \alpha\wedge\beta^2=0.
\]
Moreover \(\beta\) is semipositive, and the numerical bounds \(p+q\le n\) hold. Nevertheless, for a real tangent vector \(v\), the contraction \(i_v\alpha\) vanishes exactly when its complex \(z_1\)- and \(z_2\)-components vanish, whereas \(i_v\beta=0\) exactly when its \(z_3\)-component vanishes. Their common real kernel is therefore \(\{0\}\), of complex dimension **0**, not the would-be \(n-p-q=1\).

Equivalently, for the coefficient matrix \(A=(a_{jk})^{\mathsf T}\) of \(\alpha\), \(\operatorname{rank}A=1\), while
\[
 \ker A\cap\ker A^*=\mathbb C e_3,
 \qquad \ker B=\mathbb C e_1\oplus\mathbb C e_2,
 \qquad \ker A\cap\ker A^*\cap\ker B=\{0\}.
\]
The essential failure is \(\ker A\ne\ker A^*\); a rank-one non-reducible complex form need not have a complex kernel of codimension one. Thus the **reducibility of α is essential independently of the semipositivity of β**. This supplements, and must not be conflated with, the different β-indefiniteness countermodel already printed as Example 7.15.5.

**Disposition/dependents:** retain all hypotheses, Theorem 7.15.3, Proposition 7.15.4 and Example 7.15.5 unchanged. An optional two-sided hypothesis-necessity remark can be proposed separately, citing the new constant-form model. No theorem is false and no complete Frobenius/CR proof chain has been certified. The linear-algebra computation itself has no external proof dependency.

## POME-MRC-PROJECTIVE-CURVE-COTENSOR-001

**Severity:** low. **Status:** verified conditional deduction (complete elementary result for a nontrivial family of MRC quotients; **not** a solution of the unrestricted open question).

**Reading locus:** \`docs/sections/questions-on-relative-canonical-classes-and-cotangent-tensors/index.html\`, main blob \`7b2763d35ab776a5bb0a17a34e8a2e6b3546358f\`, physical lines 5, 8–12. **Question 24.12.2**, source \`cao-paun-foliations:54F33ABF\`, permanent tag \`2C2AE81C4020\`, asks whether, for the maximal rationally connected quotient \(q:X\dashrightarrow Q\), a pseudoeffective line bundle \(L\hookrightarrow(\Omega_X^1)^{\otimes m}\) satisfies \(\nu(X,L)\le\nu(Q,K_Q)\). Adjacent **Conjecture 24.12.1** has source \`cao-paun-foliations:026DF33E\` and tag \`3E0B91E5DF69\`; it is not used or resolved.

**Verified product case.** Fix \(r\ge1\), a smooth connected projective curve \(C\) of genus \(g\ge1\), and
\[
 X=\mathbb P^r\times C,\qquad q=\operatorname{pr}_C,\qquad m\ge1.
\]
Then \(q\) is the MRC quotient: the fibers \(\mathbb P^r\) are rationally connected and every holomorphic map \(\mathbb P^1\to C\) is constant by Riemann–Hurwitz (the case \(g=1\) included). Let \(L\) be pseudoeffective and admit a nonzero sheaf morphism, in particular any injection,
\[
 L\longrightarrow(\Omega_X^1)^{\otimes m}.
\]
We prove that \(L=q^*M\) for some \(M\in\operatorname{Pic}(C)\), that
\[
 0\le\deg M\le m(2g-2),
\]
and that for \(g=1\), necessarily \(M\simeq\mathcal O_C\). Consequently the question's numerical-dimension inequality is **true** for this entire product family, with equality attained.

**Proof.** By the projective-bundle Picard formula, write
\[
 L=\operatorname{pr}_1^*\mathcal O_{\mathbb P^r}(a)\otimes q^*M,\quad a\in\mathbb Z.
\]
For completeness, this Picard splitting follows from the integral Künneth decomposition of \(H^2(\mathbb P^r\times C,\mathbb Z)\), the vanishing of \(H^1(\mathbb P^r,\mathcal O)\), and the exponential exact sequence: a line bundle with zero degree on every projective fiber, made trivial on one \(\{p\}\times C\), has both vanishing \(c_1\) and a trivial class in \(\mathrm{Pic}^0\). Test a positive current representing the pseudoeffective class \(c_1(L)\) against the smooth semipositive forms \(H^{r-1}\wedge q^*\omega_C\) and \(H^r\), where \(H=\operatorname{pr}_1^*\omega_{\mathrm{FS}}\). This gives, respectively, \(a\ge0\) and \(\deg M\ge0\).

On any line \(\ell\subset\mathbb P^r\) there is a splitting
\[
 \Omega^1_{\mathbb P^r}|_\ell
 \simeq\mathcal O_\ell(-2)\oplus\mathcal O_\ell(-1)^{\oplus(r-1)}
\]
(the conormal exact sequence splits because \(H^1(\ell,\mathcal O_\ell(1))=0\)); for \(r=1\) only \(\mathcal O(-2)\) occurs. The cotangent of the product splits as
\[
 \Omega_X^1=\operatorname{pr}_1^*\Omega_{\mathbb P^r}^1
 \oplus q^*K_C.
\]
Restrict a putative nonzero morphism to a projective fiber where it is not identically zero, and then to a line through a point where it is nonzero. Every summand of \((\Omega_X^1)^{\otimes m}\) restricts to a line bundle of **nonpositive** degree, strictly negative if at least one tensor factor comes from \(\Omega_{\mathbb P^r}^1\). Since \(a\ge0\), nonvanishing forces \(a=0\). Moreover, all components involving at least one \(\mathbb P^r\)-cotangent factor vanish identically: their restriction to each line has no sections. The map therefore factors through the pure \(q^*K_C^{\otimes m}\) summand and gives
\[
 0\ne H^0\bigl(C,K_C^{\otimes m}\otimes M^{-1}\bigr).
\]
Thus \(\deg(K_C^{\otimes m}\otimes M^{-1})\ge0\), hence \(0\le\deg M\le m(2g-2)\). If \(g=1\) this forces degree zero, and the nonzero section of \(M^{-1}\) has no zeros, so \(M\) is trivial. If \(g\ge2\), then \(\nu(X,L)\le1=\nu(C,K_C)\); if \(g=1\), then \(\nu(X,L)=0=\nu(C,K_C)\). Equality occurs for \(g\ge2\) with \(L=q^*K_C\) and \(m=1\), and for \(g=1\) with \(L=\mathcal O_X\), using a nowhere-vanishing holomorphic 1-form from \(C\).

**Disposition/dependents:** The question remains open in its stated generality. This calculation supplies a rigorous positive model in arbitrary rationally connected fiber dimension, including the rigid elliptic-base endpoint; it does **not** claim a new proof of global MRC quotient theory, conjectural relative canonical pseudoeffectivity, or any regularization programme. Optional placement is a separately reviewed example below Question 24.12.2, with the open status and original attribution retained. Standard Euler/conormal, projective-bundle Picard, and curve facts are explicitly exposed above rather than hidden as a borrowed deep analytic theorem.

## Coverage and unchanged limits

- **§7.15:** this run directly checked Proposition 7.15.4's displayed proof (physical lines 83–107) against a complex nonreducible form, and contrasted the already printed Example 7.15.5. This **extends an already contextually sampled section**; it is not first coverage of a complete section.
- **§24.12:** the formerly inventory-only new section received its **first** targeted question/hypothesis review (physical lines 5–12), followed by a fully computed projective-fibration model. This is a question-case proof, not certification of an open conjecture.
- Crosschecked §19.10.1 (semipositive section-growth asymptotic) and §22.1.109 (net-limit minimax) for prior scope and duplication. Existing findings \`POME-SEMIPOS-TORSION-OSCILLATION-001\` and \`POME-NA-MINIMAX-001\` remain unchanged; neither is repackaged as new progress.
- Current chapter index inventory remains **25 chapters / 747 distinct section IDs**, with **zero entire sections certified**. Existing resolved/unresolved/deferred statuses are preserved. No tests, builds, CI, browser validation, formalization, original-source changes, production-main changes, tag changes, merges or publication performed.
- Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain expressly **deferred-by-user**, not resolved or reopened.
