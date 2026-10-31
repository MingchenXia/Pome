# Two independent positive exact rays on the Calabi–Eckmann threefold

**Audit date:** 2026-11-01. **Production main inspected:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Verdict:** no false printed theorem found. One new explicit, independently justified **low / verified conditional deduction**; ordinary topology and positivity conventions are the only inputs. No regularization, Bergman, \(L^2\), or extension work.

## Source and exact reading-edition anchors

- The main reading-edition file is \`docs/sections/locally-conformally-kahler-geometry/index.html\`, Git blob **\`6ebf8e604b45d3eb748037af506145273ca3875d\`**.
- **Proposition 23.2.59:** source \`non-kahler-pluripotential-theory:F88B67B6\`, permanent tag **\`EBFA309383E5\`**, lines **1054–1080**. Its proof depends on generalized Lamari duality, Theorem 11.6.1, and Poincaré duality. We checked the image/annihilator and openness arguments locally, not the entire Lamari theorem.
- **Theorem 23.2.60:** source \`non-kahler-pluripotential-theory:B41AA0AF\`, permanent **\`DB27896B9A96\`**, lines **1082–1113**. The finite-dimensional separation direction was checked, including the case \(W_X=0\).
- **Proposition 23.2.69:** source \`non-kahler-pluripotential-theory:40B2088A\`, permanent **\`4CCB765ECCA2\`**, lines **1238–1274**. The differential sign and Fréchet-cone separation were checked as specified below, without re-certifying the de Rham theorem for currents.
- **Corollary 23.2.70:** source \`non-kahler-pluripotential-theory:811BE385\`, permanent **\`86E2247D209D\`**, lines **1280–1305**; its numbered mass inequality has source \`8F1CE001\`, permanent **\`24F2C25D4A8F\`**, lines **1282–1285**.
- **Example 23.2.72:** source \`non-kahler-pluripotential-theory:3C406D0A\`, permanent **\`1EE117A3B0B0\`**, lines **1307–1357**, particularly quotient construction **1318–1338**, holomorphic projection and positive exact form **1340–1354**.

## POME-CE-TWORAY-EXACT-CONE-001 — low / verified conditional deduction

**Claim (a strict strengthening of the model calculation, not a correction to the printed example).**
Let \(X\) be the threefold constructed in Example 23.2.72:
\[
 \widetilde X=(\mathbb C^2\setminus\{0\})^2,\qquad
 t\cdot(z,w)=(e^t z,e^{it}w),\qquad X=\widetilde X/\mathbb C.
\]
Write \(p=(p_1,p_2):X\to\mathbb P^1\times\mathbb P^1\), and take the positive Fubini–Study form \(\omega_{\rm FS}\) on \(\mathbb P^1\). Define
\[
 \alpha_1=p_1^*\omega_{\rm FS},\qquad
 \alpha_2=p_2^*\omega_{\rm FS}.
\]
Then \(\alpha_1,\alpha_2\) are **linearly independent real smooth, closed, semipositive \((1,1)\)-forms**, each a **nonzero de Rham-exact current**. Consequently the cone
\[
 \mathcal Q=\{s\alpha_1+t\alpha_2:s,t\geq0\}
\]
is a two-dimensional pointed cone of positive, de Rham-exact currents.

For **every** Hermitian form \(h\) on \(X\), put
\[
 m_i=\int_X\alpha_i\wedge h^2>0.
\]
Every current \(T_{s,t}=s\alpha_1+t\alpha_2\in\mathcal Q\) has
\[
 [T_{s,t}]_{\rm dR}=0,\qquad
 \int_X T_{s,t}\wedge h^2=s\,m_1+t\,m_2.
\]
In particular, the positive-current fiber of the single de Rham class \(0\) has **unbounded trace mass**, contains two independent positive rays, and cannot be weakly relatively compact. This demonstrates simultaneously that the strongly Gauduchon mass estimate of Corollary 23.2.70 cannot hold without its existence hypothesis, and that the *closed, line-free de Rham image of the pseudoeffective cone by itself* is not a converse criterion: here the image is \(\{0\}\), although no strongly Gauduchon metric exists.

**Proof.**
The quotient action and slice in Example 23.2.72, lines 1318–1335, give a diffeomorphism \(X\simeq S^3\times S^3\). This also follows directly: for \(t=a+ib\), the action changes the two norms by \(e^a\) and \(e^{-b}\), so there is a unique \(a,b\) placing each orbit on \(S^3\times S^3\); freeness and properness are checked in the printed proof. The product CW structure of two 3-spheres has no cells in degree two, hence \(H^2_{\rm dR}(X;\mathbb R)=0\). Both \(\alpha_i\) are closed pullbacks of smooth Kähler forms, and thus de Rham exact.

The map \(p\) is a holomorphic submersion, as shown in lines 1340–1346. At any \(x\in X\), choose complex tangent vectors whose \(dp\)-images have arbitrary nonzero first-factor and zero second-factor components. Evaluating a real linear relation \(a\alpha_1+b\alpha_2=0\) on such a vector and its complex structure gives \(a=0\). Interchanging factors gives \(b=0\). Moreover, each nonzero semipositive \(\alpha_i\) has strictly positive trace against any \(h^2\) at every point, so \(m_i>0\). Mass is a continuous weak-current functional on the compact \(X\); the family \(k\alpha_1\), \(k\to\infty\), is not even weakly bounded. Finally, \(H^2_{\rm dR}(X)=0\) makes the image cone \(\{0\}\). Proposition 23.2.69, or directly Stokes against a closed form with positive \((2,2)\)-part, excludes strongly Gauduchon metrics in the presence of \(\alpha_1\ne0\). QED.

**What is and is not being claimed.** Independence is proved for the *differential forms/current rays*; this report does **not** claim that \(\{\alpha_1\},\{\alpha_2\}\) are linearly independent in Bott–Chern cohomology. Both are nonzero Bott–Chern classes because a positive nonzero \(dd^c\)-exact current would pair to zero with every Gauduchon metric. The original Corollary 23.2.70 remains correct; its positive-direction proof is not contradicted. The original Example 23.2.72 already gives one nonzero exact positive form; the independent **two-ray** structure, exact mass formula, and failure of a converse to closed/pointed image are the new deductions here. No theorem about arbitrary compact complex manifolds is inferred.

**Local sign/duality crosscheck.**
If a strongly Gauduchon \(\gamma\) has a closed extension \(\Theta=\gamma^{n-1}+\beta+\overline\beta\), then \(\partial(\gamma^{n-1})=-\bar\partial\beta\), \(\bar\partial(\gamma^{n-1})=-\partial\bar\beta\). The printed \(d^c=i(\bar\partial-\partial)/(4\pi)\) yields
\[
 d^c(\gamma^{n-1})=\frac{i}{4\pi}(\bar\partial\beta-\partial\bar\beta)
 =d\!\left(\frac{i}{4\pi}(\beta-\bar\beta)\right).
\]
Thus the exactness sign in the proof of Proposition 23.2.69, lines 1245–1251, is correct. The Hahn–Banach converse uses the actual Fréchet continuous dual of smooth \((2n-2)\)-forms and nonzero positive exact \((1,1)\)-currents; that functional-analytic and de Rham input is noted rather than globally certified. Theorem 23.2.60 uses a nonzero separator only modulo \(K_X\), as required. No new proof gap or false statement was established in these selected steps.

## Status, proposed editorial action, dependencies, coverage

**Status:** verified conditional deduction; **severity:** low. Optionally add a two-ray sharpness paragraph to Example 23.2.72 or a remark after Corollary 23.2.70, **preserving original labels, historical attribution and proof**. No production patch has been applied.

**Relevant dependents:** differentiating strong Gauduchon from \(0\in\operatorname{LG}(X)\); the cohomological mass and weak compactness claims of §23.2.70; possible interpretations of the de Rham image of the pseudoeffective cone. The proof assumes only the explicitly constructed quotient, elementary cohomology of \(S^3\times S^3\), positivity of Fubini–Study pullbacks, and the signed \(d^c\) convention; the general Lamari and Fréchet duality chain has not been independently certified.

**New selected mathematical coverage:** the *second independent pullback form* and two-parameter mass family in §23.2.72, and local checks of §23.2.59/.60/.69/.70. These latter theorems were **historically sampled** (in particular \`POME-LG-SG-DUAL-001\`), so this is not their first review or complete certification. No other chapter, whole section, or source version was exhaustively reviewed.

**Repository-wide certification remains:** 25 actual chapters, 747 numbered ToC sections, **zero fully mathematically certified sections**. All previously unresolved/resolved findings are preserved. User-excluded Demailly approximation/regularization and dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work remains **deferred-by-user**, neither resolved nor restarted.

**Checks actually performed:** direct exact reading-edition formula/proof/hypothesis comparison and the displayed elementary geometric/cohomological argument. **Not performed:** numerical tests, Python/JS suites, complete build, CI, formal verification, website publishing, edits to production main, tags, source bodies or canonicalization.
