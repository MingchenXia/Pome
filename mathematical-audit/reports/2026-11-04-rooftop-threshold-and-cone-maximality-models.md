# Mathematical audit: an exact divisorial rooftop threshold and a strict-admissibility Liouville boundary

**Date:** 2026-11-04. **Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Audit branch:** \`review/mathematical-audit\`. **Scope:** two independent, explicit new boundary calculations in chapters 16 and 14. This report does not certify the general analytic proof chains or any entire section. No changes to production statements, source, registries or permanent tags are proposed as completed repairs.

## POME-ROOF-EXTRAPOLATION-DIVISOR-THRESHOLD-001

**Classification:** low / **verified conditional deduction** (not a false theorem or repaired proof gap).

**Precise source:** Theorem **16.26.1**, original \`foundations-of-pluripotential-theory:459ECABA\`, permanent \`64513E83F854\`, integrated \`docs/sections/envelopes-and-model-potentials--quantitative-rooftop-extrapolation/index.html\`, main blob \`c40b40892fd37beb63802fb6cb253269fb59bd20\`, **physical lines 7, 10–19, 24–49**. Its mass-preserving singularity-envelope dependency is Proposition **16.21.2**, original \`foundations-of-pluripotential-theory:92AD249D\`, permanent \`037CA226D141\`, at \`docs/sections/envelopes-and-model-potentials--singularity-envelopes/index.html\`, main blob \`8d55c95795ea2a0a3cf5cb81bd4abb4ba867a16a\`, physical lines 19–end. The earlier sufficient extrapolation is Theorem **16.22.4**, original \`:37CAA8E0\`, permanent \`FCFA7EB59B34\`, at \`docs/sections/envelopes-and-model-potentials--extrapolation-and-model-singularities/index.html\`, blob \`17191d65c793e508c1785dd617ddb1dbc5f5d213\`, lines 97 onward. The Borel and quasi-everywhere obstacle conventions are in Definition **16.25.1**, original \`:4CF5DB90\`, permanent \`3558A6E66BA8\`, at \`docs/sections/envelopes-and-model-potentials--singularity-constraints-and-relative-capacity/index.html\`, blob \`4207ba03590b2988456f1df4da4123e1e572c8de\`, lines 10–16.

### An exact family in every complex dimension

Let \(X=(\mathbb P^1)^n\), \(n\ge 1\), with \(\omega_j\) the pullback from the \(j\)-th factor of the Fubini–Study form normalized by \(\int_{\mathbb P^1}\omega_{\mathrm{FS}}=1\), and put \(\theta=\sum_{j=1}^n\omega_j\). Fix \(p\in\mathbb P^1\) and a section \(s\) of \(\mathcal O_{\mathbb P^1}(1)\) vanishing once at \(p\), scaled so \(|s|_{\mathrm{FS}}\le1\) everywhere. Write
\[
q=\log |s|_{\mathrm{FS}}^2\circ\mathrm{pr}_1\le0,\qquad
D=\{p\}\times(\mathbb P^1)^{n-1}.
\]
With \(dd^c=\tfrac{i}{2\pi}\partial\bar\partial\), the Poincaré–Lelong identity yields \(dd^cq=[D]-\omega_1\). For each \(0\le b\le1\), let \(u_b=bq\), interpreted as zero for \(b=0\), so
\[
\theta_{u_b}=(1-b)\omega_1+\sum_{j=2}^n\omega_j+b[D]\ge0.
\]
The non-pluripolar top product discards the divisor-supported terms. Since \(\omega_j^2=0\) and \(\int_X\omega_1\wedge\cdots\wedge\omega_n=1\),
\[
M(u_b):=\int_X\langle\theta_{u_b}^n\rangle
=\int_{X\setminus D}\Bigl((1-b)\omega_1+\sum_{j=2}^n\omega_j\Bigr)^n
=n!(1-b).
\]
This calculation also holds at \(b=1\) (zero non-pluripolar top mass), and can be checked directly from truncation away from \(D\); no regularization or weighted \(L^2\) arguments are involved.

Choose \(0\le c<b<1\), let \(u=u_b\), \(v=u_c\), and let \(a>1\). Because \(q\le0\), \(u_b\le u_c\), and thus \(P_\theta[u_b]\le P_\theta[u_c]\) by inclusion of singularity-envelope competitor classes. The obstacle, off its polar set, is exactly
\[
a u_b+(1-a)u_c=dq,\qquad d=c+a(b-c).
\]
For \(d\le1\), \(dq\) is itself \(\theta\)-psh and is a competitor dominated by the same obstacle. By definition, **the envelope is exactly** \(P_\theta(dq)=dq\), independently of the obstacle's arbitrary Borel values on \(D\). Its non-pluripolar mass is
\[
M(P_\theta(dq))=n!(1-d) \quad (d\le1).
\]

For \(d>1\), the envelope's competitor family is **empty**. Indeed, suppose a nontrivial \(h\in\mathrm{PSH}(X,\theta)\) satisfies \(h\le dq\) quasi-everywhere. On a generic vertical fiber \(F_y=\mathbb P^1\times\{y\}\), \(h|_{F_y}\not\equiv-\infty\), its restriction is \(\omega_{\mathrm{FS}}\)-subharmonic, and the inequality outside a polar subset of that fiber forces its Lelong number at \(p\) to be at least \(d\). But \(\omega_{\mathrm{FS}}+dd^c(h|_{F_y})\) is a positive measure of total mass \(1\), so no atom can exceed \(1\). This contradiction shows \(P_\theta(dq)\equiv-\infty\) for \(d>1\). The generic-fiber restriction step uses only local integrability/Fubini and the one-dimensional Riesz mass identity; it is not an application of the excluded approximation programme.

Consequently, in this entire explicit family the rooftop envelope has **strictly positive mass if and only if**
\[
\boxed{c+a(b-c)<1,\quad\text{i.e.}\quad a<\frac{1-c}{b-c}.}
\]
At equality the envelope exists but its non-pluripolar top mass is zero; above equality there is no competitor at all. The printed hypothesis of Theorem 16.26.1 reduces exactly to
\[
a^n(b-c)<1-c.
\]
For \(n=1\) it is the **sharp exact threshold**. For \(n\ge2\) it is **strictly stronger than necessary** in this family; this does not invalidate a sufficient theorem.

For a concrete rational check, choose \(b=3/5\), \(c=1/5\), \(a=3/2\). Then \(d=4/5\), so \(P_\theta(dq)=dq\) has the strictly positive mass \(n!/5\), but the printed numerical premise fails for every \(n\ge2\), because \(a^n(b-c)\ge(9/4)(2/5)=9/10>4/5=1-c\). Conversely, \(a=2\) is exactly the zero-mass boundary \(d=1\); when \(a>2\), the competitor family is empty.

**Disposition and dependents:** Theorem 16.26.1 is **correct as stated** and its proof is **not repaired**. The model independently certifies the role of the positive-mass conclusion and distinguishes a sufficient \(a^n\) mass-gap estimate from necessity. Proposed optional addition after Theorem 16.26.1: the \(X=(\mathbb P^1)^n\) calculation with its \(n=1\) sharpness and higher-dimensional non-necessity. It may inform later uses of quantitative rooftop extrapolation (not audited transitively); no canonical label or source theorem should be replaced.

## POME-GAUD-LIOUVILLE-MAXIMALITY-NECESSARY-001

**Classification:** low / **verified conditional deduction** (not a counterexample to the printed theorem).

**Precise source:** cone definition and maximality test in §**14.15**, original \`non-kahler-pluripotential-theory:5C496399\`, section permanent \`D4DE203BE3BF\`, and Theorem **14.15.2**, original \`non-kahler-pluripotential-theory:7A4BB576\`, permanent \`AC61FE141521\`, at \`docs/sections/smooth-monge-ampere-equations--a-liouville-theorem-for-the-limiting-cone/index.html\`, main blob \`2a5f42ad68db1f5091a0c2e0c5a29e2c3887cdec\`, **physical lines 13–28, 51–58**. Related printed comparison Lemma **14.15.1**, original \`:D0FAF6CD\`, permanent \`6E3495B1A225\`, lines **31–46**, is statement/context only here.

The theorem concludes that bounded globally Lipschitz functions on \(\mathbb C^n\) **maximal** for the cone \(P_n(H)=((\mathrm{tr}H)I-H)/(n-1)\ge0\) are constant. The word *maximal* is indispensable already for smooth functions when \(n\ge3\): define
\[
v_n(z)=-(1+|z|^2)^{-(n-2)},\qquad n\ge3.
\]
It is \(C^\infty\), nonconstant, \(-1\le v_n<0\), and globally Lipschitz because
\(|\nabla v_n|=2(n-2)|z|(1+|z|^2)^{-(n-1)}\)
is bounded. Put \(s=|z|^2\), \(f(s)=-(1+s)^{-(n-2)}\), so
\[
H(v_n)=f'(s)I+f''(s)zz^*,\quad
f'(s)=(n-2)(1+s)^{-(n-1)},\quad
f''(s)=-(n-2)(n-1)(1+s)^{-n}.
\]
In the complex radial direction \(z\), the eigenvalue of \(P_n(H(v_n))\) is \(f'(s)>0\); in its \(n-1\) orthogonal complex directions it is
\[
f'(s)+\frac{s f''(s)}{n-1}=(n-2)(1+s)^{-n}>0.
\]
The formula also extends to \(z=0\). Thus \(P_n(H(v_n))\) is **positive definite at every finite point**, so \(v_n\) is strictly admissible. It cannot be maximal: the smooth test \(h=v_n\) touches \(v_n\) from below everywhere and has strictly positive \(P_n(H(h))\), violating the printed maximality definition. It supplies a sharper elementary warning than bounded subharmonicity alone: even smooth, globally Lipschitz, bounded cone-admissible functions need not be constant in \(n\ge3\). For \(n=2\) the cone is the usual psh cone and bounded admissible functions are already constant; hence the dimensional restriction is essential to this example.

**Disposition and dependents:** Theorem 14.15.2 is **not false** and its maximality hypothesis is precisely what excludes the example. Optional addition immediately after the theorem: \(v_n\) as a self-contained reason that admissibility cannot replace maximality in the induction/gradient blow-up scheme of §14.16. No claim is made to verify the entire induction, energy alternative, viscosity stability, or rescaling proof chain.

## Coverage and exclusions

New proof/model scrutiny: one exact sharp-threshold family attached to §16.26.1 (a section previously sampled in a separate audit), and one globally explicit strict cone-admissible model testing the *maximality* hypothesis in §14.15.2 (also previously sampled). Cross-read only: the named statements in §§16.21, 16.22 and 16.25, and the definition/comparison in §14.15.1. **No entire new mathematical section or transitive source-proof chain is certified.** The actual table of contents remains **25 chapters / 747 numbered sections / zero fully certified mathematical sections**. All previous confirmed errors, proof gaps, external inputs, duplicates and verified repairs retain their existing statuses. **Demailly approximation/regularization and its dedicated Bergman, weighted-\(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain deferred-by-user, NOT resolved or certified.** No builds, tests, CI, automatic publication, main/source/tag/registry modifications or PR creation were performed.
