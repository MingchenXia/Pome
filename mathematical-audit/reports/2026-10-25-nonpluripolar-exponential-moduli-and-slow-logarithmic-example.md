# 2026-10-25 — exponential damping against non-pluripolar measures: capacity-controlled moduli and a logarithmically slow fixed example

**Reviewed integrated main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit branch:** e5cd7f073f0a34a5ceab7fd0e89c561a646d3145. **Session started:** 2026-10-25 14:53 Asia/Shanghai. This audit explicitly **excludes** the entire Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme. Historical notes remain deferred-by-user, not resolved.

## Pinned integrated evidence and actual scope

1. **§5.44.5 (vanishing exponents), permanent tag D260E972F57C, internal reader label 1D86C745**, source non-kahler-pluripotential-theory. Main file: docs/sections/plurisubharmonic-functions-and-singularities--integration-against-non-pluripolar-measures/index.html, blob 15c449ab02d6f8df98edfa07f5286af7ac8e72d1, physical lines **48–86**. The qualitative non-pluripolar measure conclusion is proved by sublevel capacity splitting in lines 65–78; the more quantitative \(L^p\) result explicitly assumes \(p>1\) in line 56, with Hölder in lines 80–86. Related selected proof passages inspected: §§5.44.2 (11–30), 5.44.4 (37–43), 5.44.7 (92–165), 5.44.10 (174–199), 5.44.12 (215–263). No transitive certification is claimed.
2. **§5.29.2**, permanent tag 5CEF121C5391; **Eq. 5.29.4**, tag 3EF8F920CDD3. Main file: docs/sections/plurisubharmonic-functions-and-singularities--hermitian-capacity/index.html, blob 77a9098e9bb922425d11c5b04d8927a3997ad44e, lines **36–77** (display at **41–44**). The integrated result supplies the uniform bound \(\operatorname{Cap}_\omega(\{v<-t\})\le C_0/t\) for normalized \(\omega\)-psh potentials and \(t>1\).
3. **§5.25.1**, tag 45B3FA75B7BD, lines 14–26; **§5.25.2**, tag FC59B7D406A3, lines 32–51; **§5.25.3**, tag 0AD144F69807, lines 57–63. Main file: docs/sections/plurisubharmonic-functions-and-singularities--normalized-compactness/index.html, blob d7ff8eafea43197c77de4bfd335bed0764ab4f69. Directly checked the moving-point submean upper bound, the finite connected chart-cover propagation, and the decreasing-limit \(L^1\) argument.
4. **§5.26.2**, tag 88C7A8DCE36E, lines 18–41, main file docs/sections/plurisubharmonic-functions-and-singularities--uniform-exponential-integrability/index.html, blob d961c0412577bb6abdb8455efc44e2f35760c55c. Inspected the dyadic weighted-sum contradiction and its monotone \(L^1\) step; the separate qualitative Skoda theorem for one quasi-psh potential was treated as an unverified prerequisite.
5. **§5.22 standing assumptions**, docs/sections/plurisubharmonic-functions-and-singularities--plurisubharmonic-potentials/index.html, main blob 1b0067104a17b95c283a89791721bb9b04edad39, physical line 7: the section assumes connected compact \(X\), smooth real backgrounds and a Hermitian form. Dependency context only.

Both new findings below are **low severity / verified conditional deduction** from the printed inputs, not errors in the original theorems.

## POME-CAP-DOM-EXP-MODULUS-001 — quantitative modulus from Hermitian capacity domination

**Hypotheses.** Suppose \(X\) is connected compact complex, \(\omega\) is Hermitian, and a finite positive measure \(\mu\) satisfies
$$
  \mu(E)\le A\,\operatorname{Cap}_\omega(E)^\gamma
  \quad\text{for every Borel }E\subseteq X,\qquad A<\infty,\ \gamma>0.
$$
Then a constant depending only on the displayed fixed data satisfies, **uniformly over** \(v\in\operatorname{PSH}(X,\omega)\) with \(\sup_Xv=0\), for \(0<\lambda\le\frac12\),
$$
 \boxed{\int_X(1-e^{\lambda v})\,d\mu
 \le C
 \begin{cases}
 \lambda^\gamma,&0<\gamma<1,\\
 \lambda(1+|\log\lambda|),&\gamma=1,\\
 \lambda,&\gamma>1.
 \end{cases}}
$$

**Proof.** Put \(T=-v\ge0\), allowing \(T=+\infty\) on a pole. The measure vanishes on pluripolar sets by the assumed domination. By Tonelli,
$$
  I_\lambda:=\int_X(1-e^{-\lambda T})\,d\mu
    =\lambda\int_0^\infty e^{-\lambda t}\,\mu(T>t)\,dt.
$$
The checked Eq. 5.29.4 gives \(\mu(T>t)\le D t^{-\gamma}\) for \(t>1\), where \(D=AC_0^\gamma\), while \(\mu(T>t)\le M:=\mu(X)\) holds for all \(t>0\). Hence
$$
 I_\lambda\le \lambda M
 +\lambda D\int_1^{1/\lambda}t^{-\gamma}\,dt
 +\lambda D\int_{1/\lambda}^\infty e^{-\lambda t}t^{-\gamma}\,dt.
$$
The final term is bounded by \(D\lambda^\gamma\int_1^\infty e^{-s}s^{-\gamma}ds\). The middle integral is \(O(\lambda^\gamma)\) if \(0<\gamma<1\), \(O(\lambda\log(1/\lambda))\) if \(\gamma=1\), and \(O(\lambda)\) if \(\gamma>1\). Together with the first term this proves all three claims without selecting sequences or interchanging unjustified limits. \(\square\)

**Proposed addition and dependents.** This can appear as an optional quantitative corollary after §5.44.5. Any downstream claim of a uniform rate from capacity domination may use the corresponding case. These bounds are *not claimed optimal* over the entire class of measures satisfying that capacity condition.

## POME-NONPOLAR-SLOW-EXP-001 — an absolutely continuous measure with exact slow asymptotic

**Hypotheses and construction.** Work on \(X=\mathbb P^1\) with the normalized Fubini–Study form \(\omega_{\mathrm{FS}}=dd^c\log(1+|z|^2)\) on the affine chart. For \(0<a<1\) define
$$
 v_a(z)=a\log\frac{|z|^2}{1+|z|^2},
 \qquad \omega_{\mathrm{FS}}+dd^c v_a
 =(1-a)\omega_{\mathrm{FS}}+a[0]\ge0,
 \qquad \sup_{\mathbb P^1}v_a=0.
$$
Set \(t=-\log|z|\) on \(0<|z|<e^{-e}\) and push forward
$$
   d\mu=\frac{dt}{t(\log t)^2}\,
         \frac{d\vartheta}{2\pi},
   \qquad e\le t<\infty,\quad
   0\le\vartheta<2\pi,\qquad z=e^{-t+i\vartheta}.
$$
Give the measure zero mass elsewhere. Since \(\int_e^\infty dt/[t(\log t)^2]=1\), this is a probability measure. It is **absolutely continuous with respect to Euclidean area** on the punctured chart and has **zero atom at \(z=0\)**, so it charges no pluripolar set.

**Exact conclusion.**
$$
 \boxed{\lim_{\lambda\downarrow0}\log(1/\lambda)
 \int_{\mathbb P^1}(1-e^{\lambda v_a})\,d\mu=1.}
$$
In particular, no estimate \(O(\lambda^\delta)\), for any fixed \(\delta>0\), follows from finite non-pluripolarity alone, even with *one fixed* normalized psh potential and *one fixed* non-pluripolar measure.

**Proof.** Let \(L=1/\lambda\). On the support of \(\mu\),
$$
 -v_a(e^{-t+i\vartheta})
   =a\bigl(2t+\log(1+e^{-2t})\bigr),
$$
whence
$$
 I_\lambda=\int_e^\infty
  \left(1-\exp[-a\lambda(2t+\log(1+e^{-2t}))]\right)
  \frac{dt}{t(\log t)^2}.
$$
On \(e\le t\le L\), use \(1-e^{-x}\le x\) and \(2t+\log(1+e^{-2t})\le3t\), giving
$$
 \int_e^L(\cdots)\,\frac{dt}{t(\log t)^2}
 \le3a\lambda\int_e^L\frac{dt}{(\log t)^2}
 =O((\log L)^{-2}).
$$
The last bound follows by splitting at \(\sqrt L\): the initial interval has length \(O(\sqrt L)\) and the second has integrand \(O((\log L)^{-2})\). For \(t\ge L\), bounding the factor by 1 leaves exactly \(\int_L^\infty dt/[t(\log t)^2]=1/\log L\). Thus \(\limsup_{L\to\infty}(\log L)I_{1/L}\le1\).

Conversely, fix \(M>1\). On \(t\ge ML\), the factor is at least \(1-e^{-2aM}\), and hence
$$
 I_{1/L}\ge
 (1-e^{-2aM})\int_{ML}^\infty\frac{dt}{t(\log t)^2}
 =\frac{1-e^{-2aM}}{\log(ML)}.
$$
It follows that \(\liminf_{L\to\infty}(\log L)I_{1/L}\ge1-e^{-2aM}\). Sending \(M\to\infty\) proves the stated limit. \(\square\)

**Proposed addition and dependents.** This is an optional counterexample to the *unprinted quantitative strengthening*, not to §5.44.5 itself. If a dependent argument needs polynomial decay against an arbitrary finite non-pluripolar measure, it must add capacity domination, density integrability or another quantitative hypothesis. The printed linear rate for \(L^p\) densities (\(p>1\)) is unaffected.

## Limitations and status ledger

No false theorem or new missing-proof claim is established here. The §5.44.5 qualitative capacity splitting is compatible with both deductions; the §5.25 normalization argument uses connectedness as stipulated in §5.22; the §5.26 dyadic-sum proof requires the independent qualitative Skoda integrability premise. Cegrell's fixed-measure convergence, the bounded Hermitian torsion-current limiting calculus used elsewhere in §5.44 and other upstream analytic inputs are **not** independently certified. The Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss programme remains entirely **deferred-by-user**, not reopened under prerequisite checking. No full section or project verification, tests, build, CI, publication or change to main/source bodies/permanent tags/registries occurred.
