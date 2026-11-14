# Three noncollinear point blowups: exact restricted ranks and the two volume walls

**Stable finding ID:** POME-RESVOL-NONCOLLINEAR-THREEPOINT-WALL-001  
**Date:** 2026-11-14 (Asia/Shanghai)  
**Severity/status:** low / **verified conditional deduction**. The cited printed theorem and proposition are not refuted.  
**Production main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Integrated reading edition:** docs/sections/divisorial-restricted-volumes/index.html  
**Integrated Git blob:** 8eb1127568e77d6d045098361c366ceeb846b909

## Source anchors, proof scope, and exclusions

- §20.8 section permanent tag 30E77D3CC0BE, under the subject B-divisors and restriction.
- Theorem 20.8.3: source label transcendental-positive-cones:42C59BDB, permanent tag 8DC7DAC31FB7, HTML physical lines **63–66** (differentiation of volume in a smooth divisorial direction); proof runs from physical line **72**. The full analytic proof is **not** re-certified here.
- Proposition 20.8.16: source label transcendental-positive-cones:682A1645, permanent tag 7ED04B77FCC6, physical lines **349–352**, proof lines **358–384** (numerical restricted volumes and positive-product pairing). Only the hypotheses and displayed identity are used to interpret the algebraic model; the regularization-containing proof, notably lines 335–344 and 361–363, was deliberately **not audited**.
- Lemma 20.8.1: source label transcendental-positive-cones:1E2C07C0, permanent tag 7E82D2724E2F, physical lines **10–25**, consulted for the restricted-volume convention **only**; the regularization step in line 17 is explicitly **excluded**.
- This is a *new three-noncollinear-point* model. The earlier two-point blowup and three-*collinear*-point calculations are retained as separate results, not replayed or counted as new findings.

## Exact statement

Let \(p_1=[1:0:0]\), \(p_2=[0:1:0]\), \(p_3=[0:0:1]\) be noncollinear points of \(\mathbf P^2\). Let
\[
X=\operatorname{Bl}_{p_1,p_2,p_3}\mathbf P^2,\quad
H=\pi^*c_1(\mathcal O_{\mathbf P^2}(1)),\quad E=E_1+E_2+E_3,
\quad D_t=H-tE.
\]
For integers \(d\ge1\), \(0\le r\le d\), write \(D_{d,r}=dH-rE\).
The exact global-section dimension is zero when \(3r>2d\). Otherwise
\[
h^0(X,\mathcal O_X(D_{d,r}))
=\binom{d+2}{2}-3\binom{r+1}{2}
+3\binom{\max(0,2r-d)}{2},                 \tag{A}
\]
with \(\binom{k}{2}=0\) for \(k<2\).
The exact restriction-image rank on *each exceptional curve* is
\[
\operatorname{rank}\bigl(H^0(X,D_{d,r})\to H^0(E_i,D_{d,r}|_{E_i})\bigr)
=\begin{cases}
r+1,&2r\le d,\\
2d-3r+1,&d<2r\le 4d/3,\\
0,&3r>2d.
\end{cases}                                                    \tag{B}
\]
In the middle line \(d<2r\le4d/3\) is precisely \(d/2<r\le2d/3\).

The numerical volume and the algebraic restricted volume of the big class \(D_t\) for \(0<t<2/3\) consequently obey
\[
\operatorname{vol}_X(D_t)=
\begin{cases}
1-3t^2,&0\le t\le1/2,\\
(2-3t)^2,&1/2\le t\le2/3,\\
0,&t\ge2/3,
\end{cases}\qquad
\operatorname{vol}_{X|E_i}(D_t)=
\begin{cases}
t,&0<t\le1/2,\\
2-3t,&1/2\le t<2/3.
\end{cases}                                                    \tag{C}
\]
The displayed volume function is \(C^1\) across the non-nef wall \(t=1/2\), with
\[
\frac{d}{dt}\operatorname{vol}_X(D_t)
=-2\sum_{i=1}^3\operatorname{vol}_{X|E_i}(D_t)
=\begin{cases}-6t,&0<t\le1/2,\\-6(2-3t),&1/2\le t<2/3.\end{cases} \tag{D}
\]
Thus the coefficient \(n=2\) in Theorem 20.8.3 is directly tested across a genuine fixed-component wall. This is **not** a proof of the general analytic differentiation theorem.

## Proof without analytic regularization

**Monomial ideal and dimension.** A degree-\(d\) homogeneous polynomial vanishes to order at least \(r\) at \(p_1\) precisely when every occurring monomial \(x^ay^bz^c\), \(a+b+c=d\), has \(b+c\ge r\), or equivalently \(a\le d-r\). Applying the analogous conditions at the other two coordinate points gives the *exact* monomial basis
\[
\{x^ay^bz^c:\ a+b+c=d,\quad a,b,c\in\mathbf Z_{\ge0},
\quad \max(a,b,c)\le d-r\}.                         \tag{E}
\]
The set is empty exactly when \(d>3(d-r)\), i.e. \(3r>2d\). For \(3r\le2d\), start with \(\binom{d+2}{2}\) triples and subtract the three caps \(a\ge d-r+1\), etc., each of cardinality \(\binom{r+1}{2}\). A pair of caps has \(\binom{2r-d}{2}\) triples when \(2r-d\ge2\); there are three pairs. A triple intersection is impossible in this range. Inclusion–exclusion proves (A), including the finite-degree boundary cases.

**Exceptional restriction ranks.** In the affine chart \(x\ne0\) at \(p_1\), the exceptional homogeneous coordinates are \([y:z]\). Restriction to \(E_1\) retains precisely the leading homogeneous order-\(r\) terms: in (E), these have \(a=d-r\), \(b+c=r\). The other two base-point conditions give \(b,c\le d-r\). Thus \(b\) ranges over the integers
\[
\max(0,2r-d)\ \le b\le\ \min(r,d-r).
\]
Different such monomials restrict to independent sections of \(\mathcal O_{E_1}(r)\). Counting the interval proves (B). The same argument applies to \(E_2,E_3\). **No assumed asymptotic surjectivity of a jet map is used.**

**Asymptotics and fixed parts.** For a real \(t\), take \(r_d=\lceil dt\rceil\) (or multiples of the denominator for rational \(t\)). Formula (A), divided by \(d^2/2\), tends to the displayed two positive pieces in (C). For \(t>2/3\), the spaces are eventually zero. Formula (B), divided by \(d\), gives the restricted ranks in (C); the limits are unchanged by rounding.

For \(r>d/2\), every monomial in (E) satisfies \(a,b,c\ge k:=2r-d\). Therefore \((xyz)^k\) divides *every* admissible polynomial. These factors correspond to the three strict transforms of the coordinate lines through pairs of the blown-up points, and the residual linear system is exactly
\[
D_{d,r}-k(L_{12}+L_{13}+L_{23})
=(2d-3r)(2H-E), \qquad L_{ij}=H-E_i-E_j.            \tag{F}
\]
The conics through the three coordinate vertices are generated by \(xy,xz,yz\), whose strict transforms have no common zero on the blowup; hence \(|2H-E|\) is basepoint-free. Formula (F) explicitly locates the non-nef wall, without using Zariski-decomposition existence as an external black box. For \(0<r<d/2\), \(D_{d,r}=(d-2r)H+r(2H-E)\) is a positive combination of the two indicated globally generated classes. In each regime the generic point of every \(E_i\) is outside the fixed locus; in fact its restricted moving degree is strictly positive for \(0<t<2/3\). The standard projective identification of restricted volume with asymptotic restriction rank, and of this rank with the numerical restricted mass in Proposition 20.8.16, is the **explicitly isolated upstream analytic/algebraic identification** in (C).

**Derivative and exact normalization.** Differentiating both elementary polynomials in (C) gives (D), with the same value \(-3\) at \(t=1/2\). Because \(\frac{d}{dt}D_t=-\sum_i E_i\), this is the coefficient-two prediction of the printed divisorial differentiation statement in dimension two. Both the volume and each restricted volume vanish at the pseudo-effective boundary \(t=2/3\); the derivative formula is asserted only inside the big range.

## Reproducible small check and verification limits

The accompanying text-only Python check enumerates all monomials and restriction orders for \(1\le d\le35\), \(0\le r\le d\), and compares with (A) and (B): **665 integer pairs**, all assertions passed in this audit session. This is a finite combinatorial check, not a project test suite, build, CI run, or analytic theorem verifier.

**Status:** low / verified conditional deduction; the finite-degree formulas and their asymptotics are complete. The identification with analytic non-pluripolar restricted masses remains conditional on the existing Pome restricted-volume statements. No general restricted-volume theorem is fully certified; no false printed theorem has been found here. The Demailly approximation/regularization and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain **deferred-by-user**, neither reopened nor marked solved. No production HTML, source bodies, registry, tags, main, CI or published site is to be changed.
