# Compact perturbations: the exact \(\mathrm{dd}^c\)-closed trace criterion

**Date:** 2026-11-07. **Finding:** `POME-COMPACT-TRACE-DDC-CRITERION-001`. **Classification:** low / **verified conditional deduction** (the smooth fixed-form criterion and its countermodel are proved below; the separately printed Bedford–Taylor lemma is not refuted). **Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Exact primary source and dependency anchors

- Primary: `docs/sections/bedford-taylor-products-and-local-capacity--local-energy-moments/index.html`, main blob `e619f7aa95f80ce11aa676193b054db3180e59d4`, physical lines **355–380**, in particular Lemma **7.11.18**, source `foundations-of-pluripotential-theory:7C182C45`, permanent tag `E1A777307E3D`. The printed proof uses the **closed** mixed Bedford–Taylor currents, their locality (Proposition 7.2.2) and symmetry (Theorem 7.3.7).
- Crosscheck: `docs/sections/torsion-and-the-variation-of-mass/index.html`, blob `9abec9685e33a1b40f9c0765381408eb52b325d3`, lines **14–30, 68–94, 99–128**. In particular integration-by-parts Lemma **11.1.2**, source `non-kahler-pluripotential-theory:7DC882C7`, permanent `3B0A8DD950AD`; the full-mass Chiose Theorem **11.1.7**, source `non-kahler-pluripotential-theory:5CD99CBA`, permanent `FB90FC741F25`.
- Crosscheck: `docs/sections/gauduchon-metrics-and-linear-mass--conservation-of-the-trace-mass/index.html`, blob `34af83ff391b5e5590cd9cb10ca4cd2b3faff02c`, physical lines **7–30**, Proposition **11.5.1**, source `non-kahler-pluripotential-theory:0D4A42C8`, permanent `828FAD1A35BF`.

## Statement, exact iff, and proof

Let \(\Omega\subset\mathbb C^n\) be open, \(n\ge2\), and let \(T\) be a fixed smooth real \((n-1,n-1)\)-form, with no **a priori** closedness condition. For every smooth strictly plurisubharmonic \(\psi\), every real \(h\in C_c^\infty(\Omega)\), and every sufficiently small real \(\varepsilon\), \(\psi_\varepsilon=\psi+\varepsilon h\) remains strictly plurisubharmonic. Its **relative trace-mass variation** is exactly
\[
 \int_\Omega \bigl(\mathrm{dd}^c\psi_\varepsilon-
              \mathrm{dd}^c\psi\bigr)\wedge T
 =\varepsilon\int_\Omega h\,\mathrm{dd}^cT. \tag{1}
\]
The integrals of the *difference* are finite even when either separate trace mass is infinite. Consequently the following are equivalent:

1. \(\mathrm{dd}^cT=0\) as a current;
2. the left side of (1) vanishes for every compactly supported smooth perturbation of **one** fixed strictly psh \(\psi\) for which both signs of small \(\varepsilon\) are allowed;
3. it vanishes for compactly supported smooth perturbations of **every** smooth strictly psh \(\psi\).

To prove (1), move the distributional operator \(\mathrm{dd}^c\) from the compactly supported test function \(h\) to \(T\); no \(dT=0\) hypothesis is needed. The implication (1) \(\Rightarrow\) (3) is immediate. For the converse, fix \(\psi(z)=\sum |z_j|^2\). Since \(\mathrm{dd}^c\psi\) is uniformly positive and \(\operatorname{supp}h\) is compact, both signs of sufficiently small \(\varepsilon\) preserve strict positivity. If all variations vanish, (1) says \(\langle\mathrm{dd}^cT,h\rangle=0\) for every real compactly supported \(h\). This is precisely \(\mathrm{dd}^cT=0\). No sequential compactness, regularization or limiting exchange is used.

## Explicit strictly positive Hermitian countermodel when the criterion fails

Use the convention \(\mathrm{dd}^c=\frac{i}{2\pi}\partial\bar\partial\), set \(\beta_j=\mathrm{dd}^c|z_j|^2\), and work on the unit ball \(\Omega=B\subset\mathbb C^n\). Consider the strictly positive Hermitian form
\[
 \omega=\beta_1+(1+|z_1|^2)\beta_2+\sum_{j=3}^{n}\beta_j.
\]
Write \(a=1+|z_1|^2\). The identity
\[
 \omega^{n-1}
  =(n-1)!\sum_{j=1}^n
     \left(\prod_{k\ne j}a_k\right)
     \beta_1\wedge\cdots\wedge\widehat{\beta_j}
                    \wedge\cdots\wedge\beta_n,
 \qquad (a_1,a_2,a_3,\ldots)=(1,a,1,\ldots)
\]
implies
\[
 \boxed{\ \mathrm{dd}^c(\omega^{n-1})
       =(n-1)!\,\beta_1\wedge\cdots\wedge\beta_n\ne0.\ } \tag{2}
\]
Indeed, only the term omitting \(\beta_1\) contributes after applying \(\mathrm{dd}^c\): every other nonconstant coefficient is multiplied by an existing \(\beta_1\), so its Hessian wedge is zero. In particular \(\omega\) is **not** Gauduchon.

Choose any nonzero \(h\in C_c^\infty(B)\), \(h\ge0\), and set \(\omega_\varepsilon=\omega+\varepsilon\mathrm{dd}^ch\). This is positive for sufficiently small \(|\varepsilon|\), and (1)–(2) yield the **exact**, not merely asymptotic, trace variation
\[
 \int_B\omega_\varepsilon\wedge\omega^{n-1}
 -\int_B\omega^n
   =\varepsilon(n-1)!\int_B h\,
                    \beta_1\wedge\cdots\wedge\beta_n .
 \tag{3}
\]
For positive \(\varepsilon\) the right side is strictly positive. Moreover, differentiating the polynomial top Monge–Ampère mass at zero gives
\[
 \left.\frac{d}{d\varepsilon}\right|_{\varepsilon=0}
   \int_B\omega_\varepsilon^n
 =n!\int_B h\,\beta_1\wedge\cdots\wedge\beta_n>0. \tag{4}
\]
This establishes a nonzero first variation of the Hermitian top mass as well; equation (4) is **not** an exact finite-\(\varepsilon\) formula for that top mass.

## Classification, limits, and dependent checks

The printed **Lemma 7.11.18 is correct**: its \((\mathrm{dd}^c\varphi)^n\) and \((\mathrm{dd}^c\psi)^n\) are built from **closed** positive currents, and the mixed-current telescope admits a compactly supported primitive \(R=(\varphi-\psi)\sum_{k=0}^{n-1}S_k\). The cutoff in physical lines 374–380 makes \(\int\mathrm{dd}^cR=0\). There is no hidden assumption of compactness of \(\Omega\), only compactness of the difference support. Our countermodel uses a **nonclosed Hermitian background**; it is not a counterexample to that lemma. No source theorem is classified as false.

The exact criterion above supplies a guard against replacing the printed **closed** Bedford–Taylor factors by an arbitrary smooth positive \((n-1,n-1)\)-form. It agrees with Proposition 11.5.1: the Gauduchon condition \(\mathrm{dd}^c\gamma^{n-1}=0\) is exactly the local infinitesimal trace-mass conservation condition. It does **not** by itself imply that the entire nonlinear Hermitian Monge–Ampère mass is invariant in dimension \(n\ge3\): Theorem 11.1.7 requires the higher-power conditions \(\mathrm{dd}^c(\omega^j)=0\) for all \(1\le j\le n-1\).

**Proposed action:** retain all printed statements and their permanent tags; record the iff (1) and countermodel (2)–(4) only as a cross-reference caution for prospective extensions of §7.11.18 and for downstream mixed-mass and Hermitian comparison arguments. No currently printed dependent is established false. Bedford–Taylor locality/symmetry and the full Hermitian nonlinear chain are referenced only for semantic comparison, not newly certified by this smooth calculation.

**Actual coverage:** direct selected verification of §7.11.18's compact-support telescope and smooth fixed-form contrast, plus crosschecks §11.1.2/.5/.7 and §11.5.1; **no complete mathematical section** certified. Existing unresolved/external/deferred findings unchanged. Demailly approximation/regularization and its dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale and positivity-loss programme remain **deferred-by-user**. No tests, builds, CI, formal verification, source edits or publication.
