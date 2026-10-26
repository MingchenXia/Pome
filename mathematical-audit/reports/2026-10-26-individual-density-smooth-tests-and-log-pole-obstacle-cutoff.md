# 2026-10-26 — Essential local density floors and an explicit logarithmic-obstacle cutoff

**Reviewed main commit:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch at start:** f3f9ec6a391336765c096b0a5c029b7b48762fdd.  
**Classification:** selected proof-level review, **not** certification of an entire section, an existence theorem, or the entire dependency graph.

This session first directly read the current integrated mathematical statements and proofs in §15.28 (individual integrable right-hand-side densities) and §16.44 (obstacle-envelope pointwise trace estimate). The supporting proofs in §§15.27.1 and 16.15.7 were consulted for their exact hypotheses, not certified transitively. Neither finding refutes a printed theorem. All source references below are to **main**, not to a previous source manuscript.

## POME-SMOOTH-TEST-LOCAL-FLOOR-001

**Severity:** low. **Status:** verified conditional deduction (new exact quantitative corollary).  
**Integrated source:** \`docs/sections/equations-with-prescribed-singularities--subsolutions-for-an-individual-density/index.html\`, blob \`9262e6b9fd8929cbdd3f75bacbe2a532839d1dbe\`, §15.28.8 tag \`A89D44842BA5\` (lines 143–153), Theorem 15.28.9 tag \`4AC87EC7D266\` (lines 155–216, especially Step 4, lines 209–216). Comparison and homogeneity are Lemma 15.27.1, tag \`CE5CA1071A3C\`, \`docs/sections/equations-with-prescribed-singularities--lower-mass-and-solvability-for-all-measures/index.html\`, blob \`fc7d4f24f72d9b6ec898eedc961b789e65ef3e25\`, lines 26–58. The normalization that \(\mathrm dV\) is a **probability** volume form is explicit at line 7 of the latter file (and §15.1, \`docs/sections/equations-with-prescribed-singularities/index.html\`, blob \`a638ee4e9afd9b284c28aef989076a4874b028aa\`, line 7).

### Statement and proof

Let \(X\) be a connected compact complex manifold, \(h\) a Hermitian background for which the positive scalars \(c_h(g)\) of the existing continuous \(L^p\) Monge–Ampère solutions are defined. Let \(\mathrm dV\) be the fixed smooth **probability** volume, and suppose a probability density \(f\in L^1(\mathrm dV)\) satisfies \(f\ge c>0\) almost everywhere and

\[
\operatorname*{ess\,inf}_{x\in U} f(x)=c
\quad\text{for every nonempty open }U\subset X
\]

(with the essential infimum taken against \(\mathrm dV\)). Define the existing smooth-test threshold

\[
C_h^{\mathrm{sm}}(f)=
\inf_{\substack{g\in C^\infty(X),\,g>0\\ \int_Xg\,\mathrm dV=1}}
c_h(g)\left\|\frac{g}{f}\right\|_{L^\infty}.
\]

Then the exact value is

\[
\boxed{C_h^{\mathrm{sm}}(f)=\frac{c_h(1)}{c}.}
\]

In particular, \(C_h^{\mathrm{sm}}(f)\) is insensitive to arbitrary integrable upward excursions of \(f\) that preserve this common local essential floor. No assumption \(v_-(h)=0\) is needed for the identity.

**Proof.** Fix a smooth positive probability density \(g\), and write \(R=\|g/f\|_\infty<\infty\). Then \(g\le Rf\) almost everywhere. If some \(x_0\in X\) had \(g(x_0)>Rc\), there would be \(\varepsilon>0\) and a nonempty open neighborhood \(U\) of \(x_0\) on which \(g>R(c+\varepsilon)\). By the local essential-floor hypothesis, \(\{x\in U:f(x)<c+\varepsilon\}\) has positive volume, a contradiction. Consequently \(g\le Rc\) pointwise. Lemma 15.27.1 gives the order reversal and scalar homogeneity

\[
c_h(g)\ge c_h(Rc)=\frac{c_h(1)}{Rc}.
\]

Thus \(R\,c_h(g)\ge c_h(1)/c\). Conversely, the constant density \(g\equiv1\) is smooth and is a probability density because \(\mathrm dV(X)=1\). The hypothesis implies \(\operatorname*{ess\,inf}_X f=c\), whence \(\|1/f\|_\infty=1/c\). This test realizes equality. \(\square\)

The proof of Theorem 15.28.9 constructs exactly this local-floor phenomenon for \(f=(1+Q)/M\), with \(c=1/M\). Its existing conclusion \(C_h^{\mathrm{sm}}(f)=M c_h(1)\) is the special case of the formula. In the zero-lower-mass example the *distinct* genuine subsolution threshold is \(b_h(f)=0\): this must not be conflated with \(C_h^{\mathrm{sm}}(f)>0\).

**Proposed change:** optional general corollary immediately after §15.28.8 or after Theorem 15.28.9; retain the theorem's explicit nowhere-dense construction and its attribution. **Affected dependents:** the smooth-test comparison in §15.28.8–9 and interpretations of the individual-density threshold; no amendment of §15.28.4 (attainment of a lower-bound subsolution) or any claim of an exact Monge–Ampère solution. Existence/strict domination and scalar comparisons are internal inputs not independently proved in this session.

## POME-OBSTACLE-SCALAR-CUTOFF-001

**Severity:** low. **Status:** verified repair (explicit missing calculation supplied for a valid proof step; not a confirmed false assertion).  
**Integrated source:** \`docs/sections/pointwise-estimates-for-obstacle-envelopes/index.html\`, blob \`0afeba79adffb86326ca094ab25ce13daf6b2285\`, Lemma 16.44.1, permanent tag \`8281BE55D0D3\`, statement lines 8–12, trace argument lines 17–24, logarithmic-obstacle cutoff lines 26–33. **Internal input checked:** \`docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--penalized-equations-and-metric-laplacian-envelopes/index.html\`, blob \`a8e758f43a4c55592ce5bf1864248c6e05881698\`, Lemma 16.15.7 tag \`EA811ACFD26E\` (from line 149), its maximum principle (16.15.10), tag \`905710F73D03\` (line 190); penalized solution existence and its uniform convergence to the envelope are retained as **conditional internal inputs**.

The existing proof of Lemma 16.44.1 requests, but does not explicitly construct, smooth functions \(\psi_R\) satisfying

\[
\psi\le\psi_R\le\max(\psi,-R),\qquad
dd^c\psi_R\ge-C\kappa,\qquad
\psi_R=\psi\text{ eventually on compact sets off the logarithmic poles}.
\]

This can be supplied *without* any Demailly approximation, Bergman, \(L^2\), Ohsawa–Takegoshi, or multiscale argument: it is a one-variable convex composition.

### Complete elementary cutoff and obstacle comparison

Choose a smooth nondecreasing \(\chi:\mathbb R\to[0,1]\) equal to \(0\) on \((-\infty,-1]\) and \(1\) on \([0,\infty)\), and for each \(R>0\) set

\[
F_R(t)=-R+\int_{-R}^{t}\chi(s+R)\,\mathrm ds,\qquad
\psi_R=F_R(\psi).
\]

Then \(F'_R\in[0,1]\) and \(F''_R\ge0\); \(F_R(t)=t\) for \(t\ge-R\), and \(F_R\) is constant on \((-\infty,-R-1]\). Direct integration shows

\[
t\le F_R(t)\le\max(t,-R)
\quad(t\in\mathbb R).
\]

The logarithmic pole set is \(\{\psi=-\infty\}\). Upper semicontinuity of \(\psi\) implies that near any point of this set, \(\psi<-R-1\); hence the composition extends smoothly there as a locally constant function. Away from the pole set, \(\psi\) is smooth. Thus \(\psi_R\) is smooth globally. Off the poles, the exact chain rule gives

\[
dd^c\psi_R=F_R'(\psi)\,dd^c\psi+
F_R''(\psi)\,d\psi\wedge d^c\psi\ge-C\kappa;
\]

both sides are smooth everywhere, so the inequality extends across the poles. If \(K\) is compact away from the pole set, \(\min_K\psi>-\infty\), so \(\psi_R=\psi\) on \(K\) for all large \(R\).

Now write \(f=g-\psi\), \(v=P_\kappa(f)\), \(f_R=g-\psi_R\), and \(m_0=\inf_Z f>-\infty\). Since \(v\) is globally bounded (as argued in the integrated proof), choose

\[
R>\max\bigl\{\sup_Z(v-g),\,m_0-\min_Zg\bigr\}
\]

and also large enough that \(\psi(x_0)\ge-R\) at a minimum point \(x_0\) of \(f\) (which lies off the pole set). On \(\{\psi<-R\}\), \(f_R\ge g+R\ge m_0\); elsewhere \(f_R=f\ge m_0\), while \(f_R(x_0)=f(x_0)=m_0\). Therefore

\[
\min_Z f_R=\inf_Z f=m_0.
\]

The inequality \(R>\sup(v-g)\), together with \(v\le f\), implies \(v\le g-\max(\psi,-R)\le f_R\). On the other hand, \(f_R\le f\), so monotonicity and admissibility yield the *exact envelope identity*

\[
P_\kappa(f_R)=v.
\]

Moreover \(dd^cf_R\le dd^cg+C\kappa\), hence \(\sup_Z\Delta_\kappa f_R\le\sup_Z\Delta_\kappa g+Cm\). Applying the smooth-obstacle estimate to \(f_R\) and using \(f_R=f\) eventually on any fixed compact \(K\Subset Z\setminus\{\psi=-\infty\}\) yields precisely the stated pointwise distributional upper bound there, with the *unchanged* minimum \(m_0\) and the constant \((C+1)m+\sup\Delta_\kappa g\).

For completeness, the smooth-obstacle trace bound itself follows directly from the maximum principle already printed in §16.15.7: for \(Q_\beta=\log H_\beta-Aa_\beta\) and \(B=m+\sup\Delta_\kappa f\), \(H_\beta(x_\beta)\le2B\) at a maximum, hence
\[
H_\beta(x)\le2B\,\exp(A(a_\beta(x)-\min_Z f)).
\]
Uniform convergence \(a_\beta\to v\), and \(v\le f\), pass this upper bound to the distributional trace \(m+\Delta_\kappa v\). This only crosschecks the claimed maximum-principle use; it does not independently certify the penalized PDE existence or uniform convergence.

**Proposed change:** replace the phrase requesting an unspecified smooth cutoff in Lemma 16.44.1 by this short convex-composition construction, including the exact \(\min f_R=\inf f\) check. **Affected dependents:** obstacle-envelope contact and pointwise density bounds using the logarithmic-divisor version of §16.44.1. The stated lemma remains correct as checked; no source mathematical body was edited.

## Coverage and exclusions

- **New first selected proof-level:** §15.28, directly reading its threshold definition (15.28.1–2), Lemma 15.28.3, Theorem 15.28.4, Proposition 15.28.6–7, smooth-test discussion §15.28.8, and Theorem 15.28.9 including its full nowhere-dense and Markov-tail construction. In particular, *subsolution attainment does not imply exact equation, finite mass, or capacity convergence*.
- **New first selected proof-level:** §16.44, its entire single integrated Lemma 16.44.1, the variable trace estimate, and logarithmic-obstacle reduction. Supporting §15.27.1, §16.15.7 and §15.1 were consulted only; no entire section or dependency graph certified.
- **No new confirmed false theorem.** The first finding is a conditional strengthening; the second makes an implicit elementary proof step self-contained. No old ledger status changed.
- **Author exclusion honored:** all Demailly approximation/regularization and the dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion programme remain **deferred-by-user**, not reopened or marked resolved. The one-variable convex cutoff here is independent of that programme.
- No project tests, builds, CI, formal verification, publication, or main/source/registry/canonicalization/tag edits were performed.
