# Exact DH mass escape for decreasing model test curves on \(\mathbf P^1\)

**Finding:** \`POME-NA-DH-ESCAPING-TAIL-MASS-001\`  
**Date:** 2026-11-14. **Severity:** low. **Status:** **verified conditional deduction** (sharp necessity example for an explicit hypothesis; no false printed theorem).  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

## Integrated statements and immutable source anchors

- \`docs/sections/non-archimedean-pluripotential-theory/index.html\`, main blob \`8448d710690ebe1cc28040f9611d05c9d008a961\`, section tag \`1E9C5D0261FD\`: Definition **22.1.55** source \`sgpt:115B0C00\`, permanent \`9ADEFD2FF381\`, physical lines **904–912**; Theorem **22.1.56** source \`sgpt:420C36E9\`, permanent \`0AD7F80A793D\`, lines **916–997**, moment Eq. **22.1.57** source \`sgpt:097E0D17\` / permanent \`A51020D58E6F\`, lines **917–919**; Proposition **22.1.60** source \`sgpt:3E4F1C70\`, permanent \`492A145E9067\`, lines **1012–1091**, crucial mass condition Eq. **22.1.61** source \`sgpt:FF0788F7\` / permanent \`E10A583B2E40\`, lines **1019–1023**, convergence Eq. **22.1.62** source \`sgpt:969A6D8B\` / permanent \`636AFE1086C1\`, lines **1030–1033**.
- \`docs/sections/the-theory-of-okounkov-bodies--okounkov-test-curves/index.html\`, main blob \`20ff3089e62dd1c8349e8bcc077ec64605a9788b\`: Definition **19.6.18** source \`sgpt:09132002\`, permanent \`51940EF88F4F\`, physical lines **329–334**, and Proposition **19.6.19** source \`sgpt:DE3D564A\`, permanent \`F397AFA38927\`, lines **338–366**. We independently compute the one-dimensional Okounkov roof below, rather than treating weak convergence of moments as a black box.
- \`docs/sections/the-envelope-operators--multiplier-ideal-envelopes/index.html\`, main blob \`e37e0c4f6273acf41ee2e6d46d99ee5018bf78d5\`: \(\mathcal I\)-equivalence Proposition **16.6.2**, source \`sgpt:24D38FCD\`, permanent \`8769D844C274\`, lines **14–71**, and Definition **16.6.7**, source \`sgpt:E94E1B7\`, permanent \`E94E1B7F9193\`, lines **131–136**. The equivalence of all multiplier ideals and Lelong coefficients is used as an *existing internal input*, not reproved via excluded analytic regularization.
- The explicitly established \(u_a\) potentials and decreasing **\(P\)-model** test curves are reused solely as a *construction*, not recounted as a new result: \`mathematical-audit/reports/2026-11-14-test-curve-negative-infinity-infimum-witness.md\`, finding \`POME-TC-DECREASING-INF-NEGATIVE-INFTY-NONCOMMUTE-001\`. The new work is to check the **stronger \(\mathcal I\)-model requirement** and to calculate all the actual DH measures, Okounkov roofs, their lost tightness and moments.

## Exact finding

On normalized \(X=\mathbf P^1\), \(\int_X\omega_{\rm FS}=1\), fix \(0<c<1\). There exist decreasing genuine \(\mathcal I\)-model test curves \(\Gamma^j\in\mathrm{PSH}^{\rm NA}(X,\omega_{\rm FS})_{>0}\) and an \(\mathcal I\)-model limit \(\Gamma=\inf_j\Gamma^j\), each with maximum parameter \(0\), such that
\[
 \operatorname{vol}\Gamma^j=1,\quad \operatorname{vol}\Gamma=1-c,\qquad
 \boxed{\operatorname{DH}(\Gamma^j)
 =(1-c)\delta_0+\frac cj e^{t/j}\mathbf1_{t<0}\,dt,\quad
 \operatorname{DH}(\Gamma)=(1-c)\delta_0.}
\]
For every \(R>0\),
\[
 \operatorname{DH}(\Gamma^j)((-\infty,-R))
 =c e^{-R/j}\longrightarrow c.
\]
Thus a fixed positive fraction \(c\) of the mass **escapes to \(-\infty\)**; the sequence is not tight and does *not* converge weakly to \(\operatorname{DH}(\Gamma)\) as finite measures on \(\mathbb R\). It converges vaguely to that measure, and on the compactification \([-\infty,0]\) it converges weakly to \((1-c)\delta_0+c\delta_{-\infty}\). Its moments are exact:
\[
 \int_{\mathbb R} t^m\,d\operatorname{DH}(\Gamma^j)
 =c(-1)^m m!j^m,\qquad m\ge1.
\]
The strictly positive **uniform** lower bound \(\operatorname{vol}\Gamma^j_\tau\ge1-c>0\) for every finite \(t<0\) does *not* replace the **total-volume continuity** hypothesis (22.1.61). Therefore the printed Proposition 22.1.60(1) is correct and its extra hypothesis has genuine mathematical force.

## Full computation and proof

Put \(r=\log|z|^2\), \(F(r)=\log(1+e^r)\), \(r_a=\log(a/(1-a))\), \(H(a)=-a\log a-(1-a)\log(1-a)\), and for \(0<a<1\)
\[
 F_a(r)=
 \begin{cases}ar+H(a),&r\le r_a,\\ F(r),&r\ge r_a,\end{cases}
 \qquad u_a=F_a-F,\qquad u_0=0 .
\]
Use \(\mathrm{dd}^{\rm c}=\frac{i}{2\pi}\partial\bar\partial\). The pieces have matching value and derivative. Their convexity gives
\(\omega_{\rm FS}+\mathrm{dd}^{\rm c}u_a=a[0]+\mathbf1_{\{r>r_a\}}\omega_{\rm FS}\), with no circle atom. Hence \(\sup u_a=0\), its only pole is at \(0\), and its non-pluripolar mass equals \(1-a\). The earlier report supplies a complete elementary maximum-principle proof that \(u_a=P_{\omega_{\rm FS}}[u_a]\).

**Upgrade from \(P\)-model to \(\mathcal I\)-model.** Near \(0\), \(u_a=a\log|z|^2+O(1)\). The local integrability condition
\[
 |z|^{2q}e^{-ku_a}\in L^1_{\rm loc}
 \quad\Longleftrightarrow\quad q>ka-1
\]
gives \(\mathcal I(ku_a)_0=(z^{\lfloor ka\rfloor})\) for all positive integers \(k\); elsewhere the ideal is trivial. Any normalized \(\omega_{\rm FS}\)-psh competitor \(v\le0\) which is \(\mathcal I\)-equivalent to \(u_a\) has Lelong number \(\nu(v,0)=a\) by the already integrated Proposition 16.6.2. The function \(v+F(r)-ar\) extends subharmonically across \(0\) on \(r<r_a\), and its boundary value is at most \(H(a)\); by the subharmonic maximum principle \(v\le u_a\) there. Outside \(r<r_a\), \(v\le0=u_a\). Since \(u_a\) is itself a candidate in Definition 16.6.7, we get
\[
 P_{\omega_{\rm FS}}[u_a]_{\mathcal I}=u_a.
\]
Thus these are **\(\mathcal I\)-model** potentials, not merely \(P\)-model ones. For \(a=0\) the zero potential is likewise an \(\mathcal I\)-model.

Define for every integer \(j\ge1\)
\[
 \Gamma^j_t=u_{c e^{t/j}}\quad(t<0),\qquad
 \Gamma^j_t=-\infty\quad(t\ge0),\qquad
 \Gamma^j_{\max}=0 .
\]
The map \(a\mapsto u_a(z)\) is nonincreasing and concave, and \(t\mapsto c e^{t/j}\) is increasing and convex; composition is therefore nonincreasing and concave. Every finite slice is an \(\mathcal I\)-model of positive mass. The usc-regularized negative-infinity endpoint is \(0\). Thus the curves satisfy the actual \(\mathcal I\)-model requirements of §17.14.1, and \(\operatorname{vol}\Gamma^j=1\). For fixed \(t<0\), \(ce^{t/j}\uparrow c\), so \(\Gamma^j_t\downarrow u_c\); their decreasing infimum \(\Gamma\) has \(\Gamma_t=u_c\) for every \(t<0\) and \(\Gamma_{-\infty}=u_c\). The latter is also an \(\mathcal I\)-model. Consequently \(\operatorname{vol}\Gamma=1-c\). The positivity bound for each finite slice is exactly \(1-ce^{t/j}\ge1-c\).

**Direct one-dimensional Okounkov roof (no abstract DH continuity used).** Take the smooth flag on \(\mathbf P^1\) ending at \(0\); \(\omega_{\rm FS}\) represents \(\mathcal O(1)\). Because
\(\mathcal I(ku_a)_0=(z^{\lfloor ka\rfloor})\), the selected \(k\)-th graded series has exactly the vanishing orders
\(\lfloor ka\rfloor,\ldots,k\). Hence its normalized Okounkov body is the interval \([a,1]\), also for irrational \(a\) by taking the closure. For \(\Gamma^j\) the convex superlevels are
\[
 \Delta^j_t=[c e^{t/j},1]\quad(t<0),\qquad
 \Delta^j_{-\infty}=[0,1].
\]
The associated concave test function on \([0,1]\) is
\[
 G_j(x)=
 \begin{cases}
 j\log(x/c),&0<x<c,\\
 0,&c\le x\le1,\\
 -\infty,&x=0.
 \end{cases}
\]
For the limiting curve, \(\Delta_t=[c,1]\) for every \(t<0\), \(\Delta_{-\infty}=[c,1]\), and \(G(x)=0\) on \([c,1]\). This is precisely where the *underlying Okounkov convex body* ceases to be fixed. Since \(n=1\), the \(n!\) factor in Definition 22.1.55 is one. Pushing forward Lebesgue measure by \(G_j\), the part \([c,1]\) gives \((1-c)\delta_0\). On \((0,c)\), the inverse relation \(x=c e^{t/j}\), \(dx=(c/j)e^{t/j}dt\), gives the claimed exponential density. Similarly \(G\) gives \((1-c)\delta_0\). The calculation is therefore an *explicit measure identity* without a tacit exchange of weak limits or use of moment determinacy.

The tail formula is immediate by integration. For each fixed compactly supported continuous \(f\), the exponential part contributes at most \(c(1-e^{-R/j})\|f\|_\infty\) once \(\operatorname{supp}f\subset[-R,R]\), hence tends to zero. In contrast, its total mass is \(c\) for all \(j\), so testing with the bounded continuous function \(1\) rules out narrow convergence to the smaller limiting measure. If \(f\) extends continuously to the point \(-\infty\), substitution \(t=js\) and dominated convergence yield \(\int f(t)(c/j)e^{t/j}\mathbf1_{t<0}dt\to c f(-\infty)\), proving the compactified limit. Finally, with \(t=-js\), the Gamma integral gives
\(\int_{-\infty}^0 t^m(c/j)e^{t/j}dt=c(-1)^m j^m\int_0^\infty s^m e^{-s}ds=c(-1)^m m!j^m\). These moments also agree exactly with the extended-moment identity (22.1.57).

## Classification, correction and dependents

**Classification:** low / **verified conditional deduction**, with the cited integral-ideal/divisorial equivalence and the established reading-edition definition of partial Okounkov bodies as upstream inputs. The explicit curve, roof, distribution, tails and moments are fully computed. **No false theorem and no new proof gap are asserted.** This is not a second claim of discovering the negative-infinity endpoint phenomenon already recorded in \`POME-TC-DECREASING-INF-NEGATIVE-INFTY-NONCOMMUTE-001\`; the new and independently checked part is the \(\mathcal I\)-model admissibility plus *complete* spectral-law and non-tightness calculation in §22.1.

**Proposed correction:** none needed for the actual statement. An optional example directly after Proposition 22.1.60 could demonstrate why its total-volume condition must not be replaced by a uniform positive finite-slice mass lower bound; explicitly mention that this family violates (22.1.61), rather than suggesting it is a counterexample to the proposition. **Potential dependents:** all uses of decreasing non-Archimedean DH convergence or of the fixed-underlying-Okounkov-body condition in §§19.6, 22.1. The remaining general proofs of flag independence, model convergence and the full NA package are *not* certified. The excluded Demailly approximation/regularization, dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof programme remains **deferred-by-user**, not resolved or audited. No build, CI, publication or source edit is claimed.
