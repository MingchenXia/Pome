# Full direct §13.12 audit and a smooth setwise-convergence obstruction

**Date:** 2026-11-19  
**Finding ID:** POME-CAP-C1-SMOOTH-SETWISE-FAIL-001  
**Classification:** low / **verified conditional deduction** (sharp boundary of a proposed strengthening; no false printed theorem).  
**Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Integrated reading-edition file:** docs/sections/non-pluripolar-products--quasi-continuous-functions/index.html  
**Exact integrated blob:** 110ec8727eca146a1304cfd43fdbeb4eebf96290  
**Review branch:** review/mathematical-audit

## Actual direct reading and source anchors

The complete integrated §13.12 text (physical lines 7–116, eight numbered entries) was read directly. The following are *source* labels and distinct permanent reader tags; the numbers are current reader locators rather than imported source numbering.

| Reader item | Source label / permanent tag | Exact integrated physical lines | Direct check |
| --- | --- | --- | --- |
| Definition 13.12.1 | sgpt:9B23E7DB / C96BE5099B6A | 9–16 | Big-class capacity, admissible obstacle bounds, Borel sets |
| Theorem 13.12.2 | sgpt:731F5229 / C5C10F2AB708 | 18–27 | Four Kähler-capacity inequalities, directions and composition of moduli; proof expansion sgpt:thm:comp_capa |
| Definition 13.12.3 | sgpt:A6D559E2 / BA13EE505D9B | 29–42 | Borel/quasi-continuity, finite continuous representative off small open capacity, polar modification |
| Theorem 13.12.4 | sgpt:BE8E66B3 / 9F9E57CC1422 | 43–57 | Zero capacity vs pluripolarity and the need for capacitability; proof expansion sgpt:thm:pp_cap |
| Example 13.12.5 | sgpt:22E9858D / 472C675FCEA8 | 58–67 | Difference of qpsh functions, extended values at common poles |
| Definition 13.12.6 | sgpt:ECF23FD9 / F7490AE48EAC | 68–76 | Order-based inequalities for directed nets, local vs global capacity |
| Proposition 13.12.7 | sgpt:606EEC85 / D56D6D4A5E94 | 77–99 | Monotone-net proof, finite-intersection argument, countable Choquet selection and Dini, and the sharp proper-open-set counterexample; replacement proof sgpt:prop:mono_psh_cap |
| Theorem 13.12.8 | sgpt:B4CE255F / 272876B00528 | 100–116 | Uniformly bounded qpsh factors and weights, quasi-continuous limit, local Bedford–Taylor reduction, weak-current conclusion; replacement proof sgpt:thm:loc_conv_cap |

The source text in §13.12.7 is the current corrected **local** statement on proper open subsets. It must not be recanonicalized as a global-capacity theorem. The §13.12.7 counterexample is a smooth monotone family with annular escape; it is distinct from the **fixed Borel-set** construction below. No step of the excluded Demailly regularization programme was opened.

Direct proof checks: a positive modulus composed in the correct direction remains continuous at zero; the increasing *net* argument uses a countable Choquet subfamily plus domination by sufficiently large original indices, **not** a purported countable cofinal subnet; the decreasing net uses compactness of directed decreasing closed sets. In §13.12.8, local coordinate reductions use a smooth quadratic correction and finite product expansion; each expanded term is a signed smooth coefficient multiplying a bounded Bedford–Taylor product. Reconstructing the globally stated weak convergence relies on compactly supported tests. No new false statement or self-contained proof defect was established. Earlier 2026-10-25 selected §13.12 coverage is preserved, rather than recounted as a new first visit.

## New precise boundary: even C¹ convergence of smooth potentials does not imply setwise measure convergence

Consider the flat elliptic curve
\[
E=\mathbf C/(\mathbf Z+i\mathbf Z),\qquad
\theta=dx\wedge dy=\frac{i}{2}dz\wedge d\bar z,\qquad
\int_E\theta=1.
\]
Pome uses \(dd^c=\frac{i}{2\pi}\partial\bar\partial\). Therefore for a smooth real function
\[
dd^c f=\frac{\Delta f}{4\pi}\,dx\wedge dy. \tag{1}
\]

Fix \(0<\varepsilon<1\) (take \(\varepsilon=1/4\)), and a nonnegative \(h\in C_c^\infty((0,1))\) with \(\int_0^1h=1\). Set \(\delta_j=2^{-j-6}\). On the circle \(\mathbf R/\mathbf Z\) define a smooth nonnegative \(1/j\)-periodic density by
\[
\rho_j(x)=\sum_{k=0}^{j-1}\frac1{\delta_j}
h\left(\frac{jx-k}{\delta_j}\right),\qquad 0\le x<1,
\tag{2}
\]
extended periodically; the supports of the summands do not meet endpoints. It has mean one:
\[
\int_0^1\rho_j(x)\,dx=1,\qquad
|\operatorname{supp}\rho_j|\le\delta_j. \tag{3}
\]

Let \(q_j(t)=(1-\varepsilon)\bigl(\delta_j^{-1}h(t/\delta_j)-1\bigr)\), for \(t\in[0,1]\), extended smoothly and periodically. Its mean is zero and its \(L^1([0,1])\) norm is at most \(2(1-\varepsilon)\), **uniformly in \(j\)**. Solve the periodic ordinary differential equation
\[
v_j''=4\pi q_j,\qquad \int_0^1v_j=0.
\tag{4}
\]
There is a unique periodic solution with zero mean, and direct integration yields
\[
\|v_j'\|_\infty\le16\pi(1-\varepsilon),\qquad
\|v_j\|_\infty\le16\pi(1-\varepsilon). \tag{5}
\]
Indeed, write \(H_j(t)=\int_0^tq_j\), choose
\(v_j'=4\pi(H_j-\int_0^1H_j)\), then integrate and subtract the mean. The bounds follow from \(\|H_j\|_\infty\le\|q_j\|_1\).

The smooth global functions
\[
u_j(x+iy)=j^{-2}v_j(jx)
\tag{6}
\]
then satisfy
\[
\|u_j\|_\infty=O(j^{-2}),\qquad
\|du_j\|_\infty=O(j^{-1}), \tag{7}
\]
and equations (1), (2) and (4) give the exact identity
\[
\boxed{\quad\mu_j:=\theta+dd^cu_j
=\bigl[\varepsilon+(1-\varepsilon)\rho_j(x)\bigr]\theta
\ge\varepsilon\theta.\quad} \tag{8}
\]
Thus every \(u_j\) is smooth and strictly \(\theta\)-psh, globally uniformly bounded, and tends to zero even in \(C^1\). In particular the §13.12.6 capacity exceptional sets are eventually empty for every positive threshold: \(u_j\to0\) **globally in capacity**. The weights \(\chi_j\equiv\chi\equiv1\) are uniformly bounded and continuous, so **all** conditions of printed Theorem 13.12.8 hold with \(p=1\).

The positive probability measures \(\mu_j\) converge weakly to \(\theta\). More explicitly, for every continuous \(F(x,y)\),
\[
\int_E F\rho_j\,d\theta
=\frac1j\sum_{k=0}^{j-1}\int_0^1\!\!\int_0^1
h(s)F\left(\frac{k+\delta_js}{j},y\right)\,ds\,dy
\longrightarrow\int_E F\,d\theta. \tag{9}
\]
Uniform continuity of \(F\) makes this a uniform-in-\(s\) Riemann-sum argument; no singular-current limit is interchanged.

Nevertheless, put
\[
A=\left(\bigcup_{j\ge1}\operatorname{supp}\rho_j\right)
\times(\mathbf R/\mathbf Z)\subset E. \tag{10}
\]
This is a **single fixed Borel set**, not a varying test set. By (3),
\[
\theta(A)\le\sum_{j\ge1}\delta_j=\frac1{64},
\qquad
\mu_j(A)\ge1-\varepsilon=\frac34
\quad\hbox{for every }j. \tag{11}
\]
Hence
\[
\boxed{\quad\mu_j\rightharpoonup\theta
\text{ but }\mu_j(A)\not\longrightarrow\theta(A).\quad} \tag{12}
\]
In particular, there is **no setwise convergence** and therefore no total-variation convergence. This failure occurs despite smoothness, a common strict positive lower bound on the densities, \(C^1\)-small potentials and globally trivial capacity exceptional sets. The **upper** density bounds are not uniform, as \(\max\rho_j\asymp\delta_j^{-1}\).

### Exact guard distinguishing the defect

If, in addition, all \(\mu_j\) and the weak limit \(\mu\) were dominated by a common \(M\theta\), weak convergence of the measures on compact \(E\) **would** imply setwise convergence: for any Borel \(B\), approximate \(1_B\) in \(L^1(\theta)\) by continuous functions \(f_m\). Uniform domination bounds both \(|\int(1_B-f_m)d\mu_j|\) and the corresponding limit error by \(M\|1_B-f_m\|_{L^1(\theta)}\). First let \(j\to\infty\), then \(m\to\infty\). Thus the failure in (12) is specifically an absence of uniform integrability of the **densities**, not a failure of capacity convergence or of the printed theorem.

This is distinct from the old POME-BT-UNIFORM-BL-SQRT-SHARP-001 oscillatory cosine model, where the densities are uniformly bounded (hence setwise convergence **does** hold), and from the singular moving-fiber/non-TV examples. It is also distinct from POME-CAP-WEIGHT-UNIFORM-BOUND-SHARP-001 (unbounded **weights**, not unbounded smooth MA densities).

## Diagnosis, proposed correction, dependents, status

- **Classification/severity:** **low / verified conditional deduction**. The **explicit smooth countermodel (1)–(12) is independently proved**; the status is conditional only for treating the general printed §13.12.8 weak-convergence theorem as an internal input. This is **not** a claim that §13.12.8 is false.
- **Proposed optional clarification:** after §13.12.8, stress that its conclusion is *weak convergence on compactly supported continuous test forms*, **not setwise or total-variation convergence**. If an application needs convergence on every fixed Borel set, supply an independent uniform domination or uniform-integrability argument for the measures. The uniform \(L^\infty(\theta)\) domination argument above is sufficient on compact \(E\), not claimed necessary or general for arbitrary singular \(X,\theta\).
- **Potential dependents:** applications that replace a continuous test by an indicator, treat weak convergence as convergence over arbitrary Borel sets, or infer total variation from convergence of smooth psh potentials. The countermodel rules out those upgrades even in dimension one.
- **External/unverified inputs:** comparison with Kähler/coordinate capacities and local Bedford–Taylor zero-capacity and weighted continuity results in §§7.5, 13.12.2/4 and their earlier internal dependencies. Historical citations (Lu21, GZ17) are retained as attribution; none was silently certified or erased. No regularization proof was reopened.
- **Deduplication:** 2026-10-25 selected §13.12.8 and uniform-weight sharpness, and the 2026-11-14 local BL/TV oscillation model remain separate existing findings. The new point is failure of **setwise** convergence for a *fixed* Borel set under *global smooth \(C^1\) potential convergence and uniform positive lower densities*.
- **Actual scope:** all eight entries and current proof replacements in §13.12 directly read; **+0 newly visited sections / +1 whole-section direct reading / +0 fully certified upstream chains**. The maintained current table-of-contents inventory is 25 chapters / 747 numbered sections. No scripts, builds, tests, CI, production source/body/registry/tag modifications or website publication were performed. Every excluded Demailly/Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss item remains **deferred-by-user**, not resolved.
