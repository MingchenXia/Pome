# Generalized Lelong-mass level atoms and a projective-line Legendre-ray energy check

**Date:** 2026-10-29. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Destination:** review/mathematical-audit. **Scope:** selected new nonexcluded proof/model checks only, not certificates for whole sections or their upstream dependency chains. No production/source/tag/registry change is made in this report.

## POME-GENLELONG-LEVEL-JUMP-001 — sharp open/closed boundary mass (low; verified conditional deduction)

**Integrated anchors.** Section 6.34, *Weights and generalized Lelong masses*, source family **demailly-complex-geometry** (the generalized-mass subject, NOT Demailly approximation). Main file: **docs/sections/lelong-densities-generalized-masses-and-multiplicity--weights-and-generalized-lelong-masses/index.html**, blob **3bfe070c28159bff5f2e90a3f8d8ba695bde26e4**. Theorem 6.34.2: source label **demailly-complex-geometry-9E365A7F**, permanent tag **57F9C2832703**, physical lines 33–57; equation 6.34.3 permanent **E50D452944E2**. Proposition 6.34.5 source **demailly-complex-geometry-A74A20C0**, permanent **E1AA7F10EA92**, lines 65–89; equation 6.34.7 permanent **2B06A37CFD8E**, lines 69–72. Theorem 6.34.8 source **demailly-complex-geometry-2FE26534**, permanent **D75AE58A4C84**, physical lines 92–108; equation 6.34.9 permanent **F3579EFF0991**, lines 93–96.

**Standing hypotheses checked.** The normalization is $dd^c=(i/2\pi)\partial\bar\partial$. The weight is plurisubharmonic and extended-continuous ($e^\varphi$ continuous); only the *support-relative* closed low sublevels $S\cap\{\varphi\le R\}$ need be compact. With a closed positive current $T$ of bidimension $(p,p)$, the level mass $M_T(\varphi,r)$ is measured on the **open** sublevel $\{\varphi<r\}$, and the right limit includes its boundary atom. The fixed-weight statement (6.34.9) allows $p=0$. The distinct varying-weight statement assumes locally uniform convergence of $e^{\varphi_j}$ and retains a **right-closed level** upper estimate.

**Model A: an exact sharp fixed-weight example for (6.34.9).** Work on $\mathbb C$ with $p=0$, let $\varphi(w)=|w|^2$, $T=\delta_1$, and $T_j=\delta_{1-1/j}$ for integers $j\ge2$. All currents are positive and closed in top bidegree, and their supports lie in the same compact closed disk $S=\{|w|\le2\}$. Clearly $T_j\rightharpoonup T$, and $\varphi$ is continuous and strictly psh; support-relative semi-exhaustion holds. At the level $r=1$, theorem 6.34.2 itself says $M_T(\varphi,r)=T(\{\varphi<r\})$ because $p=0$. Direct calculation gives
$$
M_T(\varphi,1)=0,\qquad M_{T_j}(\varphi,1)=1\quad(j\ge2),\qquad M_T(\varphi,1+)=1.
$$
Thus the upper endpoint in the printed fixed-weight inequality (6.34.9) is *attained* and cannot be replaced by the open-level limit at a level carrying boundary mass. No false statement is inferred.

**Model B: positive-degree boundary mass under locally uniform varying weights.** Work on $\mathbb C^2$ with coordinates $(w,z)$ and take the integration current $T=[\{z=0\}]$, of bidimension $(1,1)$, with support $S=\{z=0\}$. Put
$$
\varphi(w,z)=\max\{0,\log|w|^2\},\qquad
\varphi_j=\varphi-\frac1j,\qquad T_j=T.
$$
Here $\varphi$ and every $\varphi_j$ are continuous psh; by convention $\max\{0,\log0\}=0$. Further, $e^{\varphi_j}=e^{-1/j}\max\{1,|w|^2\}$ converges locally uniformly to $e^\varphi$. For every finite $R\ge0$, $S\cap\{\varphi\le R\}=\{z=0,\ |w|\le e^{R/2}\}$ is compact, although the ambient sublevels are not relatively compact. The same holds for each shifted weight. Restriction to the support gives
$$
T\wedge dd^c\varphi
  =[\{z=0\}]\wedge dd^c_w\max\{0,\log|w|^2\}
  =\text{normalized angular probability on }\{|w|=1,z=0\}.
$$
To check the normalization without a reference, on the $w$-line the radial flux of $dd^c\max\{0,\log|w|^2\}$ through a circle of radius $R$ is $(R/2)\partial_R\max\{0,2\log R\}$, hence is zero for $R<1$ and one for $R>1$. There is no interior or exterior Laplacian density, so the entire probability mass lies on the unit circle, exactly where $\varphi=0$.

The potential is bounded near this circle, so the bounded Bedford–Taylor current product gives the classical mass; the truncation definition in Theorem 6.34.2 agrees. Consequently,
$$
M_T(\varphi,0)=0,\qquad M_T(\varphi,0+)=1,\qquad
M_{T_j}(\varphi_j,0)=M_{T_j}(\varphi_j,0+)=1
\quad(j\ge1).
$$
The equality for shifted weights follows also from $dd^c\varphi_j=dd^c\varphi$: their open zero sublevels contain the entire unit circle. Therefore locally uniform convergence of the exponentiated weights does **not** imply convergence of the open-level masses at a boundary atom, even for a fixed positive-degree current. The varying-weight *right-level* estimate of Theorem 6.34.8 is exactly compatible with the model, $1\le M_T(\varphi,0+)=1$.

**Assessment, correction and dependents.** Theorems 6.34.2 and 6.34.8 and formula 6.34.7 remain **correct** under their printed hypotheses. The models justify preserving the strict/open and closed/right-level distinction and the support-relative compactness hypothesis in any downstream generalized-Lelong-number comparison or weak-limit argument. Proposed change: optionally add a short boundary-atom example after Theorem 6.34.8; do **not** replace the right limit by the open-level mass. Model A is explicitly the fixed-weight sharpness test; Model B pertains to the separately printed varying-weight clause. No regularization argument or general existence theorem is certified.

## POME-RWN-LOGISTIC-RAY-ENERGY-001 — uniform moment law and exact energy slope (low; verified conditional deduction)

**Integrated anchors.** Section 17.17, *Test curves and Legendre duality*, main **docs/sections/test-curves-and-legendre-duality/index.html**, blob **704ed205a974fe18e2dc502b13ceaf382b4af4b3**. Explicit test curve equation 17.17.10: source **non-kahler-pluripotential-theory-CB283DA0**, permanent **3B7363400CA2**, lines 198–202. Proposition 17.17.11: source **non-kahler-pluripotential-theory-42E4DFA8**, permanent **377F0AD20B28**, lines 206–239. Ray equation 17.17.12: source **non-kahler-pluripotential-theory-1A6C8986**, permanent **9BA75154C113**, lines 208–210. For energy context only, Theorem 17.8.3 permanent **678A18D6D406**, in **docs/sections/relative-energy-and-perron-segments--energy-along-weak-geodesics/index.html**, blob **8d9b7af925289346c96df751c67049e90c9dfe1d**, line 59 onward. This is an **increment** to an already partially reviewed §17.17, not first-time coverage of that section or an independent verification of the Perron correspondence.

**Model and calculation.** On $X=\mathbb P^1$ use the printed mass-one Fubini–Study form $\omega=dd^c\log(1+|z|^2)$ and the exact printed smooth ray, extended by $U_0=0$:
$$
U_t(z)=\log\frac{1+e^t|z|^2}{1+|z|^2},\qquad
\omega_t=\omega+dd^cU_t=dd^c\log(1+e^t|z|^2),\qquad t\ge0.
$$
For its velocity (the toric moment coordinate)
$$
m_t(z)=\dot U_t(z)=\frac{e^t|z|^2}{1+e^t|z|^2}\in[0,1],
$$
with values $m_t(0)=0$ and $m_t(\infty)=1$, the pushforward of the smooth Monge–Ampère probability **is exactly uniform Lebesgue measure**:
$$
(m_t)_*\omega_t=\mathbf1_{[0,1]}(s)\,ds.
$$
Indeed, writing $a=e^t$ and $r=|z|$, angular integration under the stated $dd^c$ normalization gives
$$
\int_{|z|\in dr}\omega_t=\frac{2ar}{(1+ar^2)^2}\,dr
=d\left(\frac{ar^2}{1+ar^2}\right)=dm_t.
$$
The two endpoints have zero $\omega_t$ mass. Therefore for every real $q>-1$,
$$
\int_{\mathbb P^1}m_t^q\,\omega_t=\int_0^1s^qds=\frac1{q+1}.
$$
In particular the mean moment is $1/2$, its second moment is $1/3$, and
$\int_{\mathbb P^1}\ddot U_t\,\omega_t
=\int_0^1s(1-s)\,ds=1/6$.

The dimension-one Aubin–Mabuchi energy relative to zero, in the printed mass-one convention, is
$$
E(U)=\tfrac12\int_{\mathbb P^1}U(\omega+\omega_U),\qquad E(0)=0.
$$
For this **smooth** ray, differentiation and ordinary compact Kähler integration by parts give
$$
\frac{d}{dt}E(U_t)
=\int_{\mathbb P^1}\dot U_t\,\omega_t
=\frac12.
$$
Since $U_0=0$, the **exact** identity is
$$
\boxed{E(U_t)=t/2\quad(t\ge0).}
$$
As a separate consistency check, differentiating once more gives
$\frac{d^2E}{dt^2}=\int\ddot U_t\omega_t+\int\dot U_t\,dd^c\dot U_t=1/6-1/6=0$,
where the negative term follows by Stokes from the exact first-moment identity. This does **not** infer geodesic maximality solely from affine energy: Proposition 17.17.11 supplies the independent correspondence statement, which this calculation does not reprove.

**Assessment, correction and dependents.** Proposition 17.17.11 and the printed ray (17.17.12) are **correct** in this independent normalization/moment test. The new scalar moment law is a conditional quantitative corollary and an explicit smooth check on the §17.8 energy convention; it neither duplicates the earlier Hopf higher-dimensional simplex integration nor resolves any general geodesic/Perron external dependency. Proposed change: optional moment-and-energy remark adjacent to Proposition 17.17.11, with all original source attribution and permanent tags retained. No theorem/body/registry edit is made by this audit.

## Exact coverage and unresolved scope

New selected mathematical inspection: **§6.34.2/.5/.8**, with support-relative conditions, original generalized-level formulas, open/closed portmanteau step and the two explicit examples above. Incremental selected check: **§17.17.10–12**, plus smooth dimension-one Stokes normalization; **§17.8.3** used only as comparison/dependency context. The table-of-contents category **§6.42** was opened but is only an introductory convention page here, not a proof review. No complete section, full theorem-chain, complete project build, CI, publication, or formal verification is claimed.

Current main inventory is **25 chapters / 747 numbered ToC sections / zero complete-section certifications**. Existing confirmed errors, unresolved gaps, conditional repairs, and actual external dependencies are unchanged. The entire Demailly approximation/regularization programme and dedicated Bergman, $L^2$, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion research remain **deferred-by-user**, neither inspected nor certified here. The mere source-family name “demailly-complex-geometry” on §6.34 does not make its independent generalized-Lelong-mass statements part of the excluded approximation programme.
