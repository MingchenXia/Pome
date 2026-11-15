# Effective stable base loci for integral big toric divisors, including lattice-free degree one

**Finding ID:** `POME-TORIC-BIG-LATTICEFREE-STABLE-BASE-EFFECTIVE-001`  
**Date:** 2026-11-15  
**Classification:** low / **verified conditional deduction**. The printed Proposition 21.13.8 and Corollary 21.13.10 are **correct** under their usual base-locus conventions. This note is neither a correction to them nor a certification of the entire section.  
**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated reading file:** `docs/sections/toric-pluripotential-theory-on-big-line-bundles/index.html`; main blob `d77d383b4bee977cca473ea43627ee7ac449cfda`.

## Actual source anchors and mathematical inputs

- Section 21.13.1, source `sgpt:BBB50B1C`, permanent `E05D6993D0C8`, lines 24–38: smooth projective toric $X$, integral $T$-invariant big divisor $D$, and character/cocharacter lattices $M,N$.
- Equation 21.13.2, source `sgpt:995BC664`, permanent `2A3462C0F498`, lines 38–45:
  $P_D=\{m\in M_{\mathbb R}:\langle m,u_\rho\rangle\ge-a_\rho\ \forall\rho\in\Sigma(1)\}$.
- Equation 21.13.7, source `sgpt:38C140E1`, permanent `498E343E626C`, lines 100–107: $Q_\tau=P_D\cap\bigcap_{\rho\in\tau(1)}\{\langle m,u_\rho\rangle=-a_\rho\}$.
- Proposition 21.13.8, source `sgpt:7A4E8461`, permanent `111BC1BBBDE6`, lines 110–139 (especially character decomposition, lines 124–135). Its condition 21.13.9 has source `sgpt:A9A97BFB`, permanent `0AA0B0B933FC`, lines 112–116.
- Corollary 21.13.10, source `sgpt:2D4B45AE`, permanent `0D3DB05576E8`, lines 142–163; its empty-face criterion 21.13.11 has source `sgpt:2CB22C04`, permanent `7480F81CDDBD`, lines 155–159.

The character-section decomposition $H^0(X,\mathcal O_X(kD))=\bigoplus_{m\in kP_D\cap M}\mathbb C\chi^m$ is the standard toric input already stated at 21.13.8. The argument below does not use approximation/regularization or any dedicated Bergman, $L^2$, or Ohsawa–Takegoshi machinery.

## A finite, effective stabilization theorem

Let $D$ be an integral torus-invariant big divisor on a smooth projective toric variety of dimension $n$. Let $q$ be any positive integer such that $qv\in M$ for **every vertex** $v$ of $P_D$ (for instance the least common multiple of their coordinate denominators in a lattice basis). Then, as reduced closed sets,
\[
  \boxed{\operatorname{Bs}|qD|=\mathbf B(D)
  :=\bigcap_{k\ge1}\operatorname{Bs}|kD|.}
\]
The equality also holds with $q$ replaced by any positive multiple of $q$. No basepoint-freeness or nefness assumption is needed.

**Proof.** At the torus orbit $O(\tau)$, the toric monomial $\chi^m$, viewed as a section of $kD$, is nonvanishing exactly when
\[
 \langle m,u_\rho\rangle=-ka_\rho\quad\text{for all }\rho\in\tau(1).
\]
Indeed its divisor is $\sum_\rho(ka_\rho+\langle m,u_\rho\rangle)D_\rho$, with all coefficients nonnegative. A linear combination is nonzero at some orbit point only if at least one constituent monomial is nonzero there; conversely any such monomial proves the point is not in the base locus. Hence
\[
 O(\tau)\not\subseteq\operatorname{Bs}|kD|
 \quad\Longleftrightarrow\quad
 Q_\tau\cap \tfrac1kM\neq\varnothing. \tag{A}
\]
The set $Q_\tau$ is a (possibly empty) face of the compact polytope $P_D$. If $Q_\tau\neq\varnothing$, it contains a vertex $v$ of $P_D$. Since $qv\in M$, (A) applies for $k=q$ and every positive multiple of $q$. If $Q_\tau=\varnothing$, (A) fails for every $k$; that orbit is contained in the stable base locus. Therefore both loci have exactly the same intersections with every torus orbit and so are equal as reduced sets. $\square$

A completely explicit (possibly nonminimal) denominator bound comes from the defining integral facet normals: take the least common multiple of the absolute nonzero determinants of all linearly independent $n$-tuples of ray generators, or any multiple of this integer. By Cramer's rule every vertex denominator divides one such determinant. The all-vertex denominator $q$ is generally sharper; this note makes **no claim of minimality** of the stabilization index.

## Big but without sections in degrees one and two

Here is a smooth projective **surface** example illustrating why the distinction between ordinary and stable base loci is essential, even in the toric setting.

Start with the fan of $\mathbb P^1\times\mathbb P^1$, and perform successive star subdivisions in the first and third quadrants to obtain the cyclically ordered rays
\[
\begin{gathered}
(1,0),(2,1),(1,1),(1,2),(0,1),(-1,0),\\
(-2,-1),(-3,-2),(-1,-1),(-2,-3),(-1,-2),(0,-1).
\end{gathered}
\]
Adjacent primitive generators have determinant $+1$, including the last-to-first pair, so the complete fan is smooth. It is projective because these subdivisions are torus-equivariant blowups of the projective surface $\mathbb P^1\times\mathbb P^1$.

Assign the integral Cartier divisor $D=\sum a_uD_u$ by
\[
 a_{(2,1)}=a_{(1,2)}=-1,\quad
 a_{(-3,-2)}=a_{(-2,-3)}=2,\quad
 a_{(1,0)}=a_{(0,1)}=0,
\]
and $a_u=100$ on all six remaining rays. Every invariant Weil divisor on this smooth toric surface is Cartier. The six operative inequalities and the redundancy of the large coefficients give **exactly**
\[
 P_D=\{(x,y):x\ge0,\ y\ge0,\ 2x+y\ge1,\ x+2y\ge1,\
                   3x+2y\le2,\ 2x+3y\le2\}. \tag{B}
\]
Its four vertices, in cyclic order, are
\[
  (1/3,1/3),\quad(1/2,1/4),\quad(2/5,2/5),\quad(1/4,1/2).
\]
The shoelace formula gives $\operatorname{area}(P_D)=1/60>0$. Thus $D$ is big: lattice-point counting in the positive-area rational polygon gives quadratically many sections of $kD$ for large $k$ (equivalently, $\operatorname{vol}(D)=2!\operatorname{area}(P_D)=1/30$).

Nevertheless $P_D\cap\mathbb Z^2=\varnothing$. In fact $2P_D\cap\mathbb Z^2=\varnothing$: both coordinates of an integer point of $2P_D$ lie in $\{0,1\}$, but $(0,0),(1,0),(0,1)$ violate a lower inequality and $(1,1)$ violates an upper one. Thus
\[
 H^0(X,\mathcal O_X(D))=H^0(X,\mathcal O_X(2D))=0,
 \quad\operatorname{Bs}|D|=\operatorname{Bs}|2D|=X.
\]
Yet $(1,1)\in 3P_D\cap M$, so $H^0(X,\mathcal O_X(3D))\neq0$ and $\mathbf B(D)\ne X$. For this $P_D$, the vertex-denominator theorem applies with $q=\operatorname{lcm}(3,4,5)=60$, and yields
\[
 \operatorname{Bs}|60D|=\mathbf B(D)\subsetneq X.
\]
In particular, a big integral divisor need not be effective in its first (or even second) degree. The nonemptiness of $P_D$ as a real polytope cannot be silently replaced by $P_D\cap M\ne\varnothing$.

**Quantifier safeguard for the printed proposition.** In Proposition 21.13.8 the condition is **for each** $m\in P_D\cap M$ there is a ray with positive coefficient. If that lattice-point set is empty, this universal quantification is vacuous even for the zero cone $\tau=\{0\}$; then $V(\tau)=X$ is correctly included in the base locus. Excluding the zero cone by incorrectly reversing quantifiers would create a false special case. The printed Proposition 21.13.8 and Corollary 21.13.10 do **not** make that mistake.

## Classification, implications, and limits

- **Status:** verified conditional deduction; no false theorem, and no claimed repair of a missing proof. The finite stabilization follows from printed character decompositions and rational-polytope geometry, with the complete elementary argument above.
- **Severity:** low (useful effective strengthening and empty-degree guard).
- **Proposed correction:** optional addendum after Corollary 21.13.10 recording the finite denominator bound and the distinction $P_D\ne\varnothing$ versus $P_D\cap M\ne\varnothing$; retain the correct original statement and attribution.
- **Affected dependents to watch:** any later argument replacing a stable base locus by a single linear-series base locus, or assuming degree-one characters for an integral big divisor, especially toric valuation/Okounkov arguments in §§21.13.31ff. No such downstream statement is classified as false by this note.
- **Coverage:** new proof-level examination of 21.13.8 and 21.13.10 and its toric section conventions, within §21.13 previously partially visited for other statements on 2026-10-21. **+0 newly first-visited numbered sections; +0 complete-section certifications.** Current table of contents: 25 chapters and 747 numbered sections. §§21.13.21ff and the section's analytic proof chains are **not** certified here.
- **Independent small check:** `mathematical-audit/checks/check_toric_big_lattice_free.py` verifies all adjacent ray determinants, exact polygon area, and integer points in degrees 1, 2, 3 using rational arithmetic; it is not a project test suite or proof of the general lemma.
- **Excluded scope:** Demailly approximation/regularization and dedicated Bergman, $L^2$, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work remain **deferred-by-user, not certified**. No production changes, build, CI or publication.
