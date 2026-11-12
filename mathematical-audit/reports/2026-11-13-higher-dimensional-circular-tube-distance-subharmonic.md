# Higher-dimensional circular-tube obstruction to the planar subharmonic-distance convexity theorem

**Checkpoint:** 2026-11-13. **Stable finding ID:** POME-DIST-HIGHERDIM-CIRCLE-TUBE-SUBHARMONIC-001.  
**Status:** **verified conditional deduction** (the explicit counterexample and its proof are unconditional; the classification refers to the attempted higher-dimensional extension, not the correctly stated planar propositions). **Severity:** low (sharp hypothesis-boundary illustration; **no printed theorem is refuted**).

**Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Integrated reading edition:** docs/sections/planar-boundary-distance-and-convexity/index.html, blob 25fd0fd57d3e51f9224a25341ace77584b2a1a2a.  
**Section:** §3.9, *Planar boundary distance and convexity*, permanent section tag B2AAD3B5B63F.  
**Main anchor:** Proposition 3.9.2, source label klimek-pluripotential-theory:219D9DEC, permanent tag 59D258340230, physical HTML lines **37–87**: its hypothesis and conclusion explicitly concern \(\mathbb R^2\), a nonempty proper closed set \(F\), and subharmonicity of \(d_F\) on a **connected open neighborhood containing \(F\)**. The proof at lines **60–70**, especially **68**, uses that the Hessian of the distance has one zero eigenvalue and nonnegative trace **in dimension two**; only then is the Hessian positive semidefinite.  
**Context:** Proposition 3.9.3, source klimek-pluripotential-theory:366D2F88, permanent tag BBEB233BF8A4, same file lines **91–107**, also explicitly planar and dependent on Proposition 3.9.2. Proposition 3.9.1, source klimek-pluripotential-theory:79D31B13, permanent tag 964B6728E795, lines **7–33**, is a different statement about \(-d_{\partial D}\) on planar domains and is **not** the target of this example.

## Claim: the precise dimension-two boundary is essential

For every integer \(m\ge 3\), every \(R>0\), and every \(0<\varepsilon<R/2\), set
\[
F_R=\{(R\cos\theta,R\sin\theta,0,\ldots,0):
                    0\le\theta<2\pi\}\subset\mathbb R^m,
\qquad
G_\varepsilon=\{x\in\mathbb R^m:d_F(x)<\varepsilon\}.
\]
Then \(F_R\) is compact, closed, proper, **connected, smooth and not convex**. The open set \(G_\varepsilon\) is a connected tubular neighborhood containing the **entire** \(F_R\). Nevertheless \(d_F=\operatorname{dist}(\cdot,F_R)\) is continuous and **strictly subharmonic in distributions on \(G_\varepsilon\)**.

Consequently the straightforward variant of Proposition 3.9.2 obtained by replacing \(\mathbb R^2\) with \(\mathbb R^m\), \(m\ge3\), is false even when the neighborhood is connected and the closed set is a smooth connected compact curve. The actual printed, dimension-two Proposition 3.9.2 is unaffected.

## Complete calculation and distributional proof

Write \(x=(x_1,x_2,w)\), \(w\in\mathbb R^{m-2}\), and
\[
r=(x_1^2+x_2^2)^{1/2},\qquad s=r-R,\qquad
d_F(x)=\bigl(s^2+|w|^2\bigr)^{1/2}.
\tag{1}
\]
The distance formula follows by minimizing
\[
|x-(R\cos\theta,R\sin\theta,0)|^2
=r^2+R^2-2Rr\cos(\theta-\arg(x_1+ix_2))+|w|^2.
\]
On \(G_\varepsilon\), \(r>R-\varepsilon>0\); therefore this minimization gives (1) without an axis ambiguity. Also
\[
G_\varepsilon=\{(r,\theta,w):(r-R)^2+|w|^2<\varepsilon^2,\ r>0\}
\simeq S^1\times B_{\varepsilon}^{m-1},
\]
hence connected.

Away from \(F_R\), put \(d=d_F>0\). Because \(d\) is independent of \(\theta\), the cylindrical Euclidean Laplacian is
\[
\Delta_{\mathbb R^m}d
=\left(\partial_s^2+\Delta_w\right)
     (s^2+|w|^2)^{1/2}
+\frac1r\partial_r d.
\]
The normal variables \((s,w)\) have dimension \(m-1\). Their radial distance has Laplacian \((m-2)/d\), while \(\partial_r d=s/d\). Thus
\[
\boxed{\Delta d
=\frac{m-2}{d}+\frac{s}{rd}
=\frac{m-2+s/r}{d}
\ge \frac{m-2-\varepsilon/(R-\varepsilon)}d>0.}
\tag{2}
\]
The final strict inequality uses \(\varepsilon<R/2\) and \(m\ge3\). For \(m=3\), (2) becomes
\[
\Delta d=\frac{2r-R}{rd}>0.
\tag{3}
\]
This proves ordinary strict subharmonicity on \(G_\varepsilon\setminus F_R\), but the absence of a negative distributional contribution on \(F_R\) must still be justified.

The function \(d\) is 1-Lipschitz. In tubular coordinates \((\theta,s,w)\) the volume element is
\(r\,d\theta\,ds\,dw\). Therefore \(d^{-1}\in L^1_{\rm loc}(G_\varepsilon)\): the radial integral in \(m-1\) normal dimensions is bounded by a multiple of
\(\int_0^{\varepsilon_0}t^{m-3}\,dt<\infty\). The hypersurface \(S_\delta=\{d=\delta\}\), \(0<\delta<\varepsilon\), is parametrized by
\[
(\theta,v)\longmapsto
((R+\delta v_1)\cos\theta,(R+\delta v_1)\sin\theta,
\delta v_2,\ldots,\delta v_{m-1}),
\qquad v\in S^{m-2}.
\]
Its surface element is \((R+\delta v_1)\delta^{m-2}\,d\theta\,d\sigma(v)\), and symmetry in \(v_1\) gives
\[
\mathcal H^{m-1}(S_\delta)
=2\pi R\,|S^{m-2}|\,\delta^{m-2}\longrightarrow0.
\tag{4}
\]
For every \(\varphi\in C_c^\infty(G_\varepsilon)\), apply Green's formula in \(\{d>\delta\}\cap\operatorname{supp}\varphi\), using a smooth interior cutoff if necessary. Since \(|\nabla d|=1\) away from \(F_R\) and \(d=\delta\) on \(S_\delta\), all interface terms are bounded by
\[
\left(\|\varphi\|_\infty
      +\delta\|\nabla\varphi\|_\infty\right)
\mathcal H^{m-1}(S_\delta)\to0.
\]
By (4) and the local \(L^1\)-integrability of the right-hand side of (2), sending \(\delta\downarrow0\) yields the exact distributional identity
\[
\langle\Delta d,\varphi\rangle
=\int_{G_\varepsilon\setminus F_R}
\frac{m-2+(r-R)/r}{d}\,\varphi(x)\,dx.
\tag{5}
\]
There is **no residual negative or signed measure** supported on the circle. For \(\varphi\ge0\), (2)–(5) imply \(\langle\Delta d,\varphi\rangle\ge0\), strictly positive for nonzero nonnegative tests on the tube. Because \(d\) is continuous, this is equivalent to subharmonicity on \(G_\varepsilon\). The argument uses neither an unproved regularity statement across the circle nor any excluded approximation or \(L^2\)-estimate programme.

## Planar contrast and dependence check

On the same circle \(F_R\subset\mathbb R^2\), a small annular neighborhood has
\[
d_F(r)=|r-R|,\qquad
\Delta d_F=-1/r<0\quad\text{when }R-\varepsilon<r<R.
\]
Thus in the **planar** normal dimension one, no such subharmonic tubular example exists; this is consistent with the printed theorem. The essential linear algebra in its proof is exact: when \(m=2\), a real symmetric \(2\times2\) Hessian satisfying \(H\nabla d=0\), \(|\nabla d|=1\) and \(\operatorname{tr}H\ge0\) has its sole remaining eigenvalue nonnegative. In \(m\ge3\), the \(m-1\) eigenvalues perpendicular to \(\nabla d\) can have mixed signs despite nonnegative sum; (2) exhibits their compensating trace in an explicit smooth geometry.

**Classification:** verified direct, nonexcluded **scope counterexample to a hypothetical higher-dimensional version**; severity low; no incorrect original theorem, proof gap, circular dependency, or duplicate claimed. Proposition 3.9.3 uses the correct planar input, so no printed downstream conclusion is declared false.

**Proposed optional editorial correction (not applied):** add an independent dimension-warning remark following Proposition 3.9.2, quoting (1)–(3) and the distributional justification, while retaining the existing \(\mathbb R^2\) hypotheses, historical attribution, labels and permanent tags. Any future higher-dimensional distance-convexity statement must require stronger geometric or matrix-positivity assumptions than \(\Delta d_F\ge0\).

**Actual coverage:** selected direct reading of §3.9.2 (hypotheses, Hessian/eikonal and connectedness argument at lines 43–78) and contextual comparison with §§3.9.1/3, plus complete new m-dimensional model proof. §3.9 was already partially sampled (2026-10-22, 2026-10-23, 2026-10-31): **0 newly first-visited numbered sections, 0 whole-section certifications**. The actual main ToC has 25 chapters / 747 numbered sections; this remains inventory rather than verification. Existing §3.9 slab rigidity finding is different and not re-logged. The owner-excluded Demailly approximation/regularization and dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion findings remain **deferred-by-user**, not resolved or certified. No production source, registry, canonicalization, tag, test, build, CI or website alteration is authorized or performed in this audit note.
