# Nonproper Monge–Ampère mass: every complex dimension at least two, linear boundary flux, and the compactification bridge

Date: 2026-11-09. Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
New stable findings: **POME-FB-ALLDIM-LINEAR-FLUX-001** (low; verified conditional deduction); **POME-FB-COMPACT-MASS-BRIDGE-001** (low; verified repair proposed only, *not* a demonstrated gap in the printed theorem).

## Exact integrated reading-edition targets and provenance

1. Proposition 16.43.1: docs/sections/boundary-flux-and-nonproper-mass-comparison/index.html, blob b9a79bd1d3254676b65d10031e314a2de1d5a0c4, physical lines 8–39, source klimek-pluripotential-theory:ED092E5C, permanent tag A9104D666EA7. The Stokes argument is at lines 29–38. Corollary 16.43.2: same file, lines 43–51, source klimek-pluripotential-theory:C328B16E, permanent BD99C3A4D1ED.
2. Theorem 9.22.2, existence of a proper smoothly bounded Fatou–Bieberbach domain in complex dimension two: docs/sections/a-smooth-boundary-for-a-proper-biholomorphic-image/index.html, blob 1279ba00791fa992f753ddd35a63cfc0fa36973f, physical lines 49–92; source klimek-pluripotential-theory:BDF5266C, permanent CE10A564601F. This existence theorem is used as a **stated internal input**, not transitively certified here.
3. Proposition 16.35.5, the *local sign calculation* for the outward boundary orientation: docs/sections/polynomial-families-and-equilibrium-null-obstacles/index.html, blob 568257f81e9f31491e0cdde36ba8efb357423cd7, lines 81–92; source klimek-pluripotential-theory:5DEAA8D5, permanent 6F70A6B34439.
4. Proposition 13.5.1, cohomological invariance of top mass on a compact complex manifold: docs/sections/non-pluripolar-products--global-finiteness-and-bounded-cohomological-mass/index.html, blob 943517743538820940559eae8469ce98ecf5fcd5, lines 10–29; source foundations-of-pluripotential-theory:4EE18BE1, permanent 06A36B9354A5. **Its compactness hypothesis matters:** see the explicit bridge below.

## Finding POME-FB-ALLDIM-LINEAR-FLUX-001: proof and exact scope

**Status:** low / verified conditional deduction, conditional *only* on the existence result of printed Theorem 9.22.2. **Neither printed Proposition 16.43.1 nor Corollary 16.43.2 is false.**

**Claim.** For every integer \(n\geq2\) there are smooth strictly plurisubharmonic positive functions \(u_\epsilon,v\) on \(\mathbb C^n\), for all sufficiently small \(\epsilon>0\), such that
\[
 \tfrac12\leq u_\epsilon\leq v,\qquad
 \|u_\epsilon-v\|_{L^\infty(\mathbb C^n)}\leq\epsilon\|\psi\|_\infty,\qquad
 (u_\epsilon-v)(z)\longrightarrow0\quad(|z|\to\infty),
\]
and their finite **classical** Monge–Ampère total masses satisfy
\[
  \int_{\mathbb C^n}(dd^c u_\epsilon)^n
   -\int_{\mathbb C^n}(dd^c v)^n
   = n\,\mathcal A\,\epsilon +O(\epsilon^2),
  \qquad \mathcal A>0.
\]
In particular the reversed strict inequality holds for all sufficiently small \(\epsilon>0\), in *every* complex dimension \(n\geq2\). There are constants \(c,C>0\) (depending on a fixed patch and cutoff, not on \(\epsilon\)) such that \(c\epsilon\leq\) the displayed mass difference \(\leq C\epsilon\).

**Construction, including properness and boundary regularity.** Let \(F_2:\mathbb C^2\overset{\sim}{\to}\Omega_2\subsetneq\mathbb C^2\) be supplied by Theorem 9.22.2, with \(\partial\Omega_2\) smooth. For \(n>2\) put \(\Omega_n=\Omega_2\times\mathbb C^{n-2}\), \(F_n=F_2\times\operatorname{id}_{\mathbb C^{n-2}}\); for \(n=2\) use \(\Omega_2,F_2\). Then \(F_n\) is biholomorphic, \(\Omega_n\subsetneq\mathbb C^n\) is a domain, and \(\partial\Omega_n=\partial\Omega_2\times\mathbb C^{n-2}\) is smooth. The product **is unbounded**; no relative-compactness hypothesis is inserted.

Choose a bounded coordinate ball \(U\) meeting the boundary, a smooth defining function \(r\) on \(U\), negative in \(U\cap\Omega_n\) with \(dr\ne0\) at the boundary, and a smooth nonnegative cutoff \(\chi\) compactly supported in \(U\), positive on a relatively open part of \(\partial\Omega_n\cap U\). Put \(\psi=\chi r\) on \(U\) and zero outside \(U\). Then \(\psi\in C_c^\infty(\mathbb C^n)\), \(\psi\leq0\) on \(\Omega_n\), and \(\psi|_{\partial\Omega_n}=0\).

Let
\[
 \gamma(w)=\tfrac12\log(1+|w|^2),\quad
 \omega=dd^c\gamma,\quad \xi=dd^c\psi,\quad
 v=1+\gamma\circ F_n,\quad
 u_\epsilon=1+(\gamma+\epsilon\psi)\circ F_n.
\]
The fixed strictly positive form \(\omega\) has a uniform positive least eigenvalue on \(\operatorname{supp}\psi\); hence \(\omega+\epsilon\xi>0\) for sufficiently small \(\epsilon>0\). If also \(\epsilon\|\psi\|_\infty<1/2\), the pointwise inequalities and the uniform \(L^\infty\) difference estimate follow. To verify the **limit at source infinity**, for each \(a>0\) the set
\[
 K_a=\{w\in\overline{\Omega_n}\cap\operatorname{supp}\psi:|\psi(w)|\geq a\}
\]
is compact and disjoint from \(\partial\Omega_n\), since \(\psi\) vanishes there; thus \(K_a\Subset\Omega_n\), and \(F_n^{-1}(K_a)\) is compact in \(\mathbb C^n\). Therefore \(\psi\circ F_n\to0\) outside source compacts. This is stronger than a merely pointwise claim along an unspecified sequence.

**Exact finite polynomial and positive first variation.** As \(\xi\) is compactly supported, all the following integrals are finite, and by the binomial formula
\[
 \Delta_n(\epsilon):=\int_{\Omega_n}[(\omega+\epsilon\xi)^n-\omega^n]
    =\sum_{k=1}^{n}\binom nk\epsilon^k
         \int_{\Omega_n}\xi^k\wedge\omega^{n-k}.
\]
Since \(\omega\) is closed, \(\xi=dd^c\psi=d(d^c\psi)\), and \(\psi\) is supported in \(U\), the locally applied outward Stokes formula gives
\[
 \mathcal A:=\int_{\Omega_n}\xi\wedge\omega^{n-1}
   =\int_{\partial\Omega_n\cap U}d^c\psi\wedge\omega^{n-1}
   =\int_{\partial\Omega_n\cap U}\chi\,d^c r\wedge\omega^{n-1}>0.
\]
The positivity is the **local outward-normal calculation** in the proof of 16.35.5. Its theorem statement assumes relatively compact \(G\), whereas \(\Omega_n\) is not relatively compact; we use only the calculation on a bounded boundary chart with cutoff and no artificial-boundary contribution. The strictly positive form \(\omega\) makes the tangential boundary density strictly positive wherever \(\chi>0\). It follows that
\[
 \Delta_n(\epsilon)=n\mathcal A\epsilon+
    \sum_{k=2}^{n}\binom nk\epsilon^k
                  \int_{\Omega_n}\xi^k\wedge\omega^{n-k}
 =n\mathcal A\epsilon+O(\epsilon^2).
\]
For small enough positive \(\epsilon\), the remainder has absolute value at most \(\tfrac12n\mathcal A\epsilon\). Thus, for example, \(\tfrac12n\mathcal A\epsilon\leq\Delta_n(\epsilon)\leq\tfrac32n\mathcal A\epsilon\). A biholomorphic change of variables identifies \(\Delta_n(\epsilon)\) with the difference of the two entire-source top masses.

## Finding POME-FB-COMPACT-MASS-BRIDGE-001: complete compactification argument

**Status:** low / verified repair proposed only (a self-contained clarification of the last step at 16.43 physical line 38, **not** a false assertion or a demonstrated substantial proof gap). The printed argument invokes compact-manifold Proposition 13.5.1 to assign full-space masses to potentials defined on *noncompact* \(\mathbb C^n\). The missing **written bridge** is as follows.

Write \(\omega_{\rm FS}=dd^c\log(1+|w|^2)\) on the standard affine chart of \(\mathbb P^n\), in the printed convention \(dd^c=\frac{i}{2\pi}\partial\bar\partial\), with \(\int_{\mathbb P^n}\omega_{\rm FS}^n=1\). Because \(\psi\) has compact support in this affine chart, its extension \(\widetilde\psi\) by zero to a neighborhood of the hyperplane at infinity is a globally smooth real function on \(\mathbb P^n\). The two positive forms on the compactification are
\[
 \tfrac12\omega_{\rm FS},
 \qquad \tfrac12\omega_{\rm FS}+\epsilon dd^c\widetilde\psi,
\]
whose restrictions are \(\omega,\omega+\epsilon\xi\). Since the omitted hyperplane has real codimension two and both forms are smooth,
\[
 \int_{\mathbb C^n}(dd^c\gamma)^n
 =\int_{\mathbb C^n}(dd^c(\gamma+\epsilon\psi))^n
 =\int_{\mathbb P^n}(\tfrac12\omega_{\rm FS})^n
 =2^{-n}.
\]
The middle equality follows directly from compact Stokes/cohomological Proposition 13.5.1, applied to the *globally defined bounded/smooth potential* \(\epsilon\widetilde\psi\). Positivity of both densities implies their integrals over the open subdomain \(\Omega_n\) are finite, at most \(2^{-n}\). Only after this step do we pull them back by \(F_n\). This also prevents the illegitimate use of compact Stokes directly on noncompact \(\mathbb C^n\) without boundary control.

**Proposed reading-edition amendment (NOT applied):** after Corollary 16.43.2, add a remark that its conclusion holds for every \(n\geq2\) via the product domain and that the difference has positive linear first variation. In the proof of Proposition 16.43.1, add the one-sentence projective-compactification explanation above before the reference to 13.5.1. Retain both statements, their hypotheses, source attribution, permanent tags, and the existing orientation lemma. No source/body/registry edits are made here.

## Dependency boundary and exact reviewed coverage

New calculation: the full compactly supported binomial expansion, local Stokes coefficient and positivity, projective mass bridge, and the dimension-\(n\) product construction. The actual existence proof of Theorem 9.22.2 was opened and read, but its long iterative polynomial-shear convergence and all its upstream inputs were **not independently certified**; the result is used as an internal conditional premise. The boundary orientation of Proposition 16.35.5 was directly checked; its global relatively-compact statement is *not* misapplied. Proposition 13.5.1 was checked at its compact hypothesis and its exact integral identity; its general locally bounded-current proof was not fully certified.

The sections 16.43 and 9.22 were previously partly visited. This is a **new selected argument, zero new first-visited numbered sections, zero complete mathematical-section certifications**; the actual current contents remain 25 chapters and 747 numbered sections. No claim is made about arbitrary noncompact Monge–Ampère convergence, unknown univalent maps, or a false printed theorem. Excluded Demailly approximation/regularization and the dedicated Bergman/weighted-L2/Ohsawa–Takegoshi/multiscale/positivity-loss program remain **deferred-by-user**, neither resolved nor reopened. No code/test suite, build, Actions CI, formalization, or website publication was performed.
