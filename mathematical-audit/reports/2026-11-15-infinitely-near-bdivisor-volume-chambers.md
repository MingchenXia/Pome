# 2026-11-15 — Two infinitely near toric blowups: exact b-divisor volume chambers

**Finding:** `POME-BDIV-INFINITELYNEAR-VOLUME-CHAMBERS-001` — **low / verified conditional deduction**. This is a new, independent two-stage *infinitely near* point construction, not the previously recorded distinct-point blowup or movable-point example. The original b-divisor definitions and the cited toric mass theorem are **not refuted**. The section-count calculation below is self-contained; identification of algebraic section volume with the analytic class volume uses the stated internal toric theorem and is **conditional on that theorem**, not a certification of its prerequisites.

## Exact production anchors and status

Main commit `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Integrated file `docs/sections/the-theory-of-b-divisors/index.html`, blob `4a793dfd462badcb351f54a36cb030cde14a399b`. Directly compared Proposition 20.1.2 (source `sgpt:03364441`, permanent `7E1DC3BE93AF`, lines 29–35), equation 20.1.3 (`sgpt:6EAD3F58` / `73D0C455ED1D`, lines 31–34), Definition 20.1.5 (`sgpt:2A98D289` / `178D74F44C30`, lines 39–53), Definition 20.1.6 (`sgpt:0B20B6FE` / `E6F6681E7170`, lines 56–63), Definition 20.1.10 (`sgpt:2D01378B` / `908967DFB37E`, lines 123–125), and the **distinct** Example 20.1.9 (`sgpt:048A0D73` / `7AF528B0FB3B`, lines 100–120).

Cross-checked the only internal analytic-volume input: Theorem 21.13.45 and equation 21.13.47, `docs/sections/toric-pluripotential-theory-on-big-line-bundles/index.html`, blob `d77d383b4bee977cca473ea43627ee7ac449cfda`, source `sgpt:7CCE1B26` / permanent `1293B87EF09F` (Theorem, lines 753–764), and source `sgpt:86272700` / permanent `82B62A741230` (equation, lines 759–762). The theorem states that the maximal-envelope analytic mass of a big toric line bundle equals (2!) times the area of its character polytope. **Its proof is not recertified here**; no regularization or Bergman/L²/OT argument has been opened.

## Exact statement

Start with (X_0=mathbf P^2), and blow up the torus-fixed point (p=[1:0:0]), obtaining (X_1) with exceptional curve (F). Blow up the torus-fixed point (qin F) corresponding to the tangent direction (y=0) in affine coordinates (x=Z_1/Z_0, y=Z_2/Z_0). Denote the resulting smooth projective toric surface by (X_2), the strict first exceptional curve by (F'), the second exceptional curve by (E_2), and set
[
H=pi^*mathcal O_{mathbf P^2}(1),qquad E_1=pi_2^*F=F'+E_2.
]
Here (E_1) is the **total pullback**, not the strict transform. For rational (a,bge0) with (a+b<1), let
[
D_{a,b}=H-aE_1-bE_2,qquad
mathbb D_{a,b}=	ext{the Cartier b-divisor over }X_0	ext{ determined by }(X_2,D_{a,b}).
]
Then (D_{a,b}) is big, and its **exact** section-volume and, assuming the internal toric mass identity, analytic class and Cartier-b-divisor volume are
[
oxed{quad
operatorname{vol}(mathbb D_{a,b})=operatorname{vol}_{X_2}(D_{a,b})
=egin{cases}
1-a^2-b^2,&0le ble a, a+b<1,\
1-rac12(a+b)^2,&0le a<b, a+b<1.
end{cases}quad}
	ag{A}
]
Moreover (D_{a,b}) is nef **if and only if** (ble a) in this parameter range. In the other chamber, its explicit Zariski decomposition is
[
D_{a,b}=P_{a,b}+N_{a,b},qquad
N_{a,b}=rac{b-a}{2}F',quad
P_{a,b}=D_{a,b}-N_{a,b},quad P_{a,b}	ext{ nef},quad P_{a,b}cdot F'=0.
	ag{B}
]
Thus (operatorname{vol}(D_{a,b})-D_{a,b}^{,2}=(b-a)^2/2>0) when (b>a). The positive-part distinction is essential; no such equality with (D^2) is asserted for general big non-nef divisors.

## Complete elementary section-count proof

In the first blowup chart (x=u, y=uv), the point (q) is (u=v=0). In a second blowup chart (u=s, v=st), one has (x=s, y=s^2t). A monomial (x^iy^j) consequently has order (i+j) on (F') and order (i+2j) on (E_2). Since the *total* (E_1=F'+E_2) has coefficient one on each, a polynomial of degree at most (m), viewed as a section of (mathcal O_{mathbf P^2}(m)), defines a section of (mD_{a,b}) exactly when each supported monomial satisfies
[
i,jge0,qquad i+jle m,qquad i+jge ma,qquad i+2jge m(a+b).
	ag{C}
]
Here (m) is divisible by the denominators of (a,b). No cancellation among distinct monomials can alter either divisorial order: their respective lowest coefficients are distinct Laurent monomials in a generic coordinate along the exceptional curve. Hence (h^0(X_2,mD_{a,b})) is **exactly** the number of lattice points in the polygon (C).

Scale (i,j) by (m). The ambient triangle (i,jge0, i+jle1) has area (1/2); because (a+b<1), the excluded region lies wholly below its sloping edge. If (ble a), the excluded polygon has ordered vertices
[
(0,0), (a+b,0), (a-b,b), (0,a)
]
and area ((a^2+b^2)/2). If (b>a), the inequality (i+2jge a+b) already implies (i+jge(a+b)/2>a). The excluded triangle has vertices ((0,0),(a+b,0),(0,(a+b)/2)) and area ((a+b)^2/4). For a fixed rational polygon, elementary unit-cell counting gives (#(mQcapmathbf Z^2)=m^2operatorname{area}(Q)+O(m)) along divisible (m). Therefore
[
lim_{substack{m	oinfty\m a,mbinmathbf Z}}rac{2}{m^2}h^0(X_2,mD_{a,b})
=1-2operatorname{area}(	ext{excluded region}),
]
which is (A) **as an algebraic section-volume calculation without any analytic approximation premise**.

## Intersection and nefness check

In the orthogonal total-transform basis (H,E_1,E_2), the intersection matrix is (operatorname{diag}(1,-1,-1)). In particular ((F')^2=(E_1-E_2)^2=-2), (F'cdot E_2=1), and (D_{a,b}cdot F'=a-b). The five invariant curves are (F'), (E_2), the twice-proper-transformed tangent line (L=H-E_1-E_2), the other coordinate line through (p) of class (H-E_1), and the line at infinity of class (H). Their intersections with (D_{a,b}) are, in order,
[
a-b,quad b,quad 1-a-b,quad 1-a,quad1.
]
Nefness of a divisor on a smooth complete toric surface is equivalent to nonnegative intersections with all invariant curves; in this explicit surface the assertion also follows by decomposing effective curve classes using the same five rays. Thus (D) is nef precisely for (ble a).

For (b>a), put (t=(b-a)/2). Then (P=D-tF') has intersections with the five invariant curves
[
0,quad (a+b)/2,quad 1-a-b,quad1-(a+b)/2,quad1,
]
all nonnegative. Also (Pcdot F'=0) and (N=tF'ge0), proving (B). Direct bilinearity yields
[
D^2=1-a^2-b^2,qquad P^2=D^2+rac{(b-a)^2}{2}=1-rac{(a+b)^2}{2},
]
in exact agreement with the independent lattice-point count.

On any further model dominating (X_2), the Cartier b-divisor trace is a pullback of (D); (H^0) and its section-volume are unchanged by a proper birational pullback to a normal model (projection formula and (g_*mathcal O=mathcal O)). Such models are cofinal among models over (X_0) by existence of common resolutions. The internal toric volume formula at 21.13.45 then identifies these fixed section volumes with the analytic volumes entering Definition 20.1.6. No interchange of an arbitrary sequence with the **directed** modification net is used.

## A reproducible rational instance and affected dependents

Take (a=1/5, b=2/5). The root trace on (X_0) is (H), with volume (1). The realization (D) has (D^2=4/5) but
[
operatorname{vol}mathbb D=operatorname{vol}_{X_2}(D)=41/50.
]
Indeed for every (m=10k), (C) gives **exactly**
[
h^0(X_2,10kD)=41k^2+12k+1.
]
The order of the first exceptional class at the second blowup is what changes the chamber wall to (a=b). Treating (E_1) as its strict transform would give incorrect vanishing thresholds and the wrong volume.

**Affected context:** Definitions 20.1.5/.6/.10 and their model/root distinction; the *illustrative* use of the volume net in Lemma 20.1.7; the normalization in 21.13.45/.47. No printed statement is declared false and no original dependency repaired. The superficially similar Example 20.1.9 studies a **moving sequence of distinct points** and upper semicontinuity, not the fixed infinitely near model and its non-nef volume chambers. The previously audited distinct-point restricted-volume and toric lattice-free examples are also different.

**Proposed optional source-side addition, NOT APPLIED:** append this two-chamber example after 20.1.10, retaining all printed tags and historical attributions, to warn that (operatorname{vol}mathbb D) can be strictly less than root volume while exceeding the self-intersection of a big non-nef realization. The algebraic computation is complete; analytic identification relies on 21.13.45 (not newly certified). The generic analytic proof of b-divisor nefness and its regularization-dependent stages is entirely **deferred-by-user**.

**Coverage:** new direct example-level proof audit in **previously partially visited** §§20.1 and 21.13; newly first-visited numbered sections **0**, fully certified sections **0**. The current main ToC has **25 chapters and 747 sections**. A short rational check was run locally (five parameter pairs, 14 exact Ehrhart identities); no project build, test suite, GitHub Actions, formal verification, or website publication. No main, body, source, registry, permanent tag, or canonicalization edits.
