# Two-point blowup: exact restricted section ranks and the nef/non-Kähler wall

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272 (2 November 2026).
**Stable finding:** **POME-RESTVOL-TWOPOINT-NULL-WALL-001**.
**Severity and status:** low; **verified conditional deduction**, not a false printed theorem or a repair of an existing proof.
**Actual selected coverage:** additional concrete proof-level test of Proposition 20.8.16, Lemmas 20.8.13–15, and Theorem 10.99.8; geometric crosscheck of the non-nef/non-Kähler distinctions in §§10.12–10.13. These sections had already been partially reviewed. Neither their full proofs nor any excluded approximation dependency is certified.

## Precise integrated anchors

- Main file **docs/sections/divisorial-restricted-volumes/index.html**, blob **8eb1127568e77d6d045098361c366ceeb846b909**; Lemma **20.8.13**, source **transcendental-positive-cones:A47ADAF8**, permanent **DA69AEE4E88A**, physical lines **291–302**; Lemma **20.8.14**, source **transcendental-positive-cones:54BBE5DC**, permanent **B50F0B700160**, lines **305–325**; Lemma **20.8.15**, source **transcendental-positive-cones:04719031**, permanent **41D346BEA9CE**, lines **326–347**; Proposition **20.8.16**, source **transcendental-positive-cones:682A1645**, permanent **7ED04B77FCC6**, lines **349–383**.
- Main file **docs/sections/variations-of-the-volume/index.html**, blob **0b744b6432968b1320d63f5ebe67246108bb3ecf**; Theorem **10.99.8**, source **transcendental-positive-cones:0FF4E50C**, permanent **BF3A71BBF47B**, physical lines **135–152**, particularly derivative Eq. **10.99.9**, permanent **0F43ABDC6E3C**.
- Section **10.13**, main **docs/sections/bott-chern-classes-and-singular-loci--the-non-kahler-locus/index.html**, blob **180b31064ee7ac3e71e9d802e698573aa464337c**, Theorem **10.13.2** (source **transcendental-positive-cones:4861F30D**, permanent **7B5F62BF9296**, line **29**) is a *contextual statement only*. We do not use any part of its excluded regularization programme.

## Exact algebraic model

Let \(\pi:S=\operatorname{Bl}_{p_1,p_2}\mathbf P^2\to\mathbf P^2\) blow up the distinct points
\(p_1=[1:0:0]\) and \(p_2=[0:1:0]\). Put
\(H=\pi^*c_1(\mathcal O_{\mathbf P^2}(1))\),
\(E_1,E_2\) the two exceptional curves, and
\(L=H-E_1-E_2\), the strict transform of the line \(z=0\).
The intersections are \(H^2=1\), \(H E_i=0\),
\(E_i^2=-1\), \(E_1E_2=0\), and \(L^2=-1\).
Fix \(0<a<1\) and set
\[
D_a=H-a(E_1+E_2),\qquad Q=2H-E_1-E_2.
\]
The complete linear system of conics through the two distinct points is basepoint-free on \(S\), so \(Q\) is nef and big, \(Q^2=2\), and \(Q\cdot L=0\).

**Exact finite-degree ranks.** For every positive integer \(m\) put \(k=\lceil ma\rceil\) and
\(\mathscr L_m=\mathcal O_S(mH-kE_1-kE_2)=\mathcal O_S(\lfloor mD_a\rfloor)\). Then
\[
h^0(S,\mathscr L_m)=
\begin{cases}
\binom{m+2}{2}-2\binom{k+1}{2},&2k\le m,\\
(m-k+1)^2,&2k\ge m .
\end{cases} \tag{1}
\]
At equality both expressions agree. More strongly, the ranks of the *actual images of the restriction maps*, not the full spaces of sections on the curves, are
\[
\begin{aligned}
r_m(L)&=\dim\operatorname{im}\bigl(H^0(S,\mathscr L_m)\to H^0(L,\mathscr L_m|_L)\bigr)
       =\max(m-2k+1,0),\\
r_m(E_1)&=r_m(E_2)=\min(k,m-k)+1.
\end{aligned} \tag{2}
\]

**Proof.** A homogeneous monomial \(x^iy^jz^\ell\) of degree \(m\) vanishes to order
\(m-i\) at \(p_1\) and \(m-j\) at \(p_2\). Hence it gives a section of \(\mathscr L_m\)
exactly if \(i,j,\ell\ge0\), \(i+j+\ell=m\), and \(i,j\le m-k\). The surviving monomials are linearly independent and exhaust the global sections, which are homogeneous polynomials with the prescribed two multiplicities.

When \(2k\le m\), the excluded monomial corners \(i>m-k\) and \(j>m-k\) are disjoint and each contains \(\binom{k+1}{2}\) monomials. When \(2k\ge m\), the entire rectangle \(0\le i,j\le m-k\) lies below \(i+j\le m\). This proves (1).

Restriction to \(L=\{z=0\}\) retains exactly the monomials with \(\ell=0\);
their exponents satisfy \(k\le i,j\le m-k\), \(i+j=m\), giving \(r_m(L)\).
The restriction to \(E_1\) is the degree-\(k\) leading homogeneous part at \(p_1\), namely terms with \(j+\ell=k\), \(i=m-k\). The second-point condition requires
\(\ell\ge\max(0,2k-m)\); there are \(\min(k,m-k)+1\) distinct monomials.
The same argument holds for \(E_2\). This proves (2), with *no* saturation of the image to complete restricted sections.

Furthermore the smallest \(\ell\) among surviving monomials is
\(\max(2k-m,0)\). Thus \(L\) has fixed multiplicity
\[
\operatorname{ord}_L|\mathscr L_m|=\max(2k-m,0). \tag{3}
\]
For \(2k>m\), division by \(z^{2k-m}\) leaves the complete conic-through-two-points series in degree \(m-k\), with no further fixed divisor.

## Volume, wall, and three restricted volumes

Taking \(\lim_{m\to\infty}(2!/m^2)\) of (1), including irrational \(a\) through the floors already built into \(\mathscr L_m\), yields the exact algebraic volume
\[
\operatorname{Vol}(D_a)=
\begin{cases}
1-2a^2,&0<a\le\tfrac12,\\
2(1-a)^2,&\tfrac12\le a<1.
\end{cases} \tag{4}
\]
The classical restricted volumes obtained from the *image ranks* (2), after dividing by \(m\), are
\[
\boxed{
\operatorname{vol}_{S|L}(D_a)=(1-2a)_+,\qquad
\operatorname{vol}_{S|E_1}(D_a)=\operatorname{vol}_{S|E_2}(D_a)=\min(a,1-a).
} \tag{5}
\]
These are direct finite-dimensional section calculations, requiring neither positive-current regularization nor an identification with the numerical/transcendental restricted volume of Proposition 20.8.16.

To check the positive-product and gradient normalization without assuming a Zariski decomposition theorem, allow the three independent parameters
\(D_{A,b_1,b_2}=AH-b_1E_1-b_2E_2\), with \(A>b_i>0\).
The same monomial polygon gives
\[
\operatorname{Vol}(D_{A,b_1,b_2})=
\begin{cases}
A^2-b_1^2-b_2^2,&b_1+b_2\le A,\\
2(A-b_1)(A-b_2),&b_1+b_2\ge A .
\end{cases} \tag{6}
\]
The first derivatives from both sides coincide at the wall. Differentiating
(6) and applying **Theorem 10.99.8 as an internal, not independently
certified, input** yields
\[
\langle D_a\rangle=P_a=
\begin{cases}
D_a,&a\le\tfrac12,\\
(1-a)Q,&a\ge\tfrac12.
\end{cases}
\quad
D_a=P_a+(2a-1)_+[L]. \tag{7}
\]
Indeed \(\partial_A\operatorname{Vol}=2\langle D\rangle\cdot H\) and
\(\partial_{b_i}\operatorname{Vol}=-2\langle D\rangle\cdot E_i\);
the three intersection pairings determine a class in \(H^{1,1}(S,\mathbf R)\).
Equation (7) and the intersections immediately reproduce (5) as
\(\langle D_a\rangle\cdot L\) and \(\langle D_a\rangle\cdot E_i\),
*conditional on* the printed derivative theorem and restricted-product
identification. It is an independent crosscheck of all coefficients and
signs; it is **not a new proof of Proposition 20.8.16**.

The volume is \(C^{1,1}\) but not \(C^2\) at \(a=\tfrac12\):
the first derivative is \(-4a\) on the left and \(-4(1-a)\) on
the right, with common value \(-2\) at the wall; one-sided
second derivatives are \(-4\) and \(+4\).
This two-point chamber crossing is mathematically distinct from the
previously recorded one-exceptional-curve example
**POME-VOL-C11-NONC2-BLOWUP-001**, which has its wall at a pure
pullback class. We do **not** register that earlier example again.

## The subtle locus distinction at the wall

The divisor \(Q\) is basepoint-free and has null curve \(L\).
For \(0<a<1/2\), \(D_a=(1-2a)H+aQ\) is ample (the two nef
systems have no common contracted curve, and \(D_a^2>0\));
the non-nef and non-Kähler loci are both empty.

At \(a=1/2\), \(D_{1/2}=\tfrac12Q\) is **big, nef and semiample**.
In particular its divisorial minimal multiplicities vanish and
\(E_{\mathrm{nn}}(D_{1/2})=\varnothing\), but
\(D_{1/2}\cdot L=0\) and \(L\subset E_{\mathrm{nK}}(D_{1/2})\).
For the converse inclusion, choose a small \(\delta>0\);
\(\tfrac12Q-\delta L\) is ample, and a smooth Kähler representative
plus \(\delta[L]\) gives a Kähler current with singular set contained
in \(L\). A Kähler current smooth near the generic point of \(L\)
would yield strictly positive restriction mass on \(L\), contradicting
the zero cohomological intersection. Therefore
\[
E_{\mathrm{nn}}(D_{1/2})=\varnothing,\qquad
E_{\mathrm{nK}}(D_{1/2})=L. \tag{8}
\]

For \(1/2<a<1\), (3) shows that the asymptotic divisorial fixed
multiplicity along \(L\) is \(2a-1>0\), with basepoint-free residual
positive part \((1-a)Q\). Thus both non-nef and non-Kähler loci equal
\(L\). The same small-\(\delta\) construction using
\((1-a)Q-\delta L\) provides the strict Kähler current smooth off
\(L\). This distinction also explains why the vanishing restricted
mass in (5) is correctly governed by the **non-Kähler** locus, not
by the **non-nef** locus: at \(a=1/2\), the latter is empty.

The ampleness statements here can be checked by the explicit toric
polygon or the projective surface ampleness criterion. This is an
elementary surface-model verification, not a proof of the full analytic
non-Kähler locus theorem in an arbitrary Kähler class.

## Classification, dependents, and change proposal

**Result:** **POME-RESTVOL-TWOPOINT-NULL-WALL-001** —
**low / verified conditional deduction**. No new false theorem,
confirmed proof gap, genuine duplicate, or completed regularization
repair is asserted. Formulas (1)–(6), including the exact two-point
restricted-section ranks, are independently proved algebraically.
The positive-product and numerical restricted-mass identifications
in (7) use Theorem 10.99.8 and Proposition 20.8.16 **conditionally**.
The geometric null/non-nef distinction (8) is verified in the explicit
semiample blowup model only.

**Suggested reviewable correction:** optionally add the finite-degree
rank formulas (1)–(2) and the wall example (4)–(8) after
Proposition 20.8.16, with a cross-reference at §10.99.8.
Do not alter the current theorem statements, permanent tags,
canonicalization, registry or historical attributions. It clarifies
dependencies in §§10.12–10.14 and §20.8 and prevents confusing
the non-nef locus with the restricted-volume zero locus.

**Verification performed:** manual independent monomial enumeration,
fixed-divisor valuation and polynomial differentiation. No symbolic
test, project tests, site build, CI, formalization, source manuscript
change, or publication was performed. **Entire-section certifications:
zero** (25 chapters; 747 actual numbered ToC sections). Existing
finding statuses are unchanged. Demailly approximation/regularization
and dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and
positivity-loss proof programmes remain **deferred-by-user** and were
not audited or reopened.
