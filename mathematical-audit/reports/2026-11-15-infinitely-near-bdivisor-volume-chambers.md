# 2026-11-15 — Two infinitely near toric blowups: exact b-divisor volume chambers

**Finding:** POME-BDIV-INFINITELYNEAR-VOLUME-CHAMBERS-001 — **low / verified conditional deduction**. This is an independent fixed *infinitely near* point construction, not an audit of a moving-point or a two-independent-point example. No printed theorem is refuted. The section-count calculation below is complete and elementary. Identifying it with Pome's *analytic* volume of a big toric class uses the existing internal Theorem 21.13.45, which is **not** transitively certified here.

## Pinned main, sources and anchors

Main SHA: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

- \`docs/sections/the-theory-of-b-divisors/index.html\`, blob \`4a793dfd462badcb351f54a36cb030cde14a399b\`: Proposition 20.1.2, source \`sgpt:03364441\`, permanent \`7E1DC3BE93AF\`, physical lines 29–35; Eq. 20.1.3, \`sgpt:6EAD3F58\` / \`73D0C455ED1D\`, lines 31–34; Definition 20.1.5, \`sgpt:2A98D289\` / \`178D74F44C30\`, lines 39–53; Definition 20.1.6, \`sgpt:0B20B6FE\` / \`E6F6681E7170\`, lines 56–63; Definition 20.1.10, \`sgpt:2D01378B\` / \`908967DFB37E\`, lines 123–125. The different moving-point Example 20.1.9 is \`sgpt:048A0D73\` / \`7AF528B0FB3B\`, lines 100–120.
- \`docs/sections/toric-pluripotential-theory-on-big-line-bundles/index.html\`, blob \`d77d383b4bee977cca473ea43627ee7ac449cfda\`: Theorem 21.13.45, source \`sgpt:7CCE1B26\` / permanent \`1293B87EF09F\`, physical lines 753–764; its Eq. 21.13.47, \`sgpt:86272700\` / \`82B62A741230\`, lines 759–762. The equation identifies maximal-envelope mass with \(2!\) times the character-polytope area in the surface case. Its proof is an **existing internal conditional input** here, not a freshly verified theorem.

## Statement

On \(X_0=\mathbf P^2\), use affine coordinates \(x=Z_1/Z_0\), \(y=Z_2/Z_0\) at the torus-fixed point \(p=[1:0:0]\). Blow up \(p\), then blow up the torus-fixed point \(q\) of the first exceptional divisor corresponding to the tangent direction \(y=0\). Let \(X_2\) be the resulting smooth projective toric surface and \(\pi:X_2\to X_0\) the composite.

Let \(H=\pi^*[\mathcal O_{\mathbf P^2}(1)]\). Write \(E_2\) for the second exceptional curve, \(F'\) for the strict transform of the first exceptional curve, and **\(E_1=F'+E_2\) for its total pullback**. For \(a,b\in\mathbf Q_{\ge0}\) and \(a+b<1\), set \(D_{a,b}=H-aE_1-bE_2\). Denote by \(\mathbb D_{a,b}\) its Cartier b-divisor closure over \(X_0\).

The algebraic section volume, and conditionally upon the cited toric mass identity the analytic class/b-divisor volume, are
\[
\boxed{\operatorname{vol}\mathbb D_{a,b}=\operatorname{vol}_{X_2}(D_{a,b})=
\begin{cases}
1-a^2-b^2,& b\le a,\\
1-(a+b)^2/2,& b>a.
\end{cases}}
\tag{1}
\]
All these classes are big. They are nef exactly when \(b\le a\). When \(b>a\), their explicit surface Zariski decomposition is
\[
D_{a,b}=P+N,\qquad
N=\frac{b-a}{2}F',\qquad P=D_{a,b}-N\text{ nef},\qquad
P\cdot F'=0,
\tag{2}
\]
and \(\operatorname{vol}_{X_2}(D_{a,b})-D_{a,b}^2=(b-a)^2/2>0\).

## Complete section-count proof; no regularization argument

Take an integer \(m\ge1\) divisible by the denominators of \(a,b\). The affine monomials \(x^iy^j\) with \(i,j\ge0\), \(i+j\le m\), form a basis of the degree-\(m\) homogeneous polynomial sections of \(\mathcal O_{\mathbf P^2}(m)\).

In the first blowup chart \(x=u\), \(y=uv\); in the second chart near \(q=(u,v)=(0,0)\), put \(u=s\), \(v=st\). Therefore \(x=s\), \(y=s^2t\). The valuation of \(x^iy^j\) at the first strict exceptional curve is \(i+j\), while its valuation at the second exceptional curve is \(i+2j\). Because the divisor \(E_1\) is the *total* pullback, it has coefficient one on **both** exceptional curves. Consequently a monomial section of \(mD_{a,b}\) exists exactly if
\[
i,j\ge0,\quad i+j\le m,\quad
i+j\ge ma,\quad i+2j\ge m(a+b).
\tag{3}
\]
These conditions apply term-by-term to any polynomial: monomials with the same vanishing order have distinct residual monomial characters along the generic exceptional curve and cannot cancel identically. Thus \(h^0(X_2,mD_{a,b})\) is **exactly** the lattice-point count in (3), not only an upper bound.

Normalize \(i,j\) by \(m\). The full degree triangle \(T=\{u,v\ge0:u+v\le1\}\) has area \(1/2\). For \(c=a+b<1\), the excluded region lies below the sloping edge. If \(b\le a\), the excluded polygon has vertices in cyclic order
\[
(0,0),\quad(c,0),\quad(a-b,b),\quad(0,a).
\]
The shoelace formula gives area \((a^2+b^2)/2\). If \(b>a\), the condition \(u+2v\ge c\) implies \(u+v\ge c/2>a\), so the constraint \(u+v\ge a\) is redundant. The excluded triangle is \((0,0),(c,0),(0,c/2)\), of area \(c^2/4\). For any fixed rational polygon \(Q\), covering its boundary by \(O(m)\) grid cells gives \(\#(mQ\cap\mathbf Z^2)=m^2\operatorname{area}(Q)+O(m)\) along integer dilations. Hence
\[
\lim_{\substack{m\to\infty\\ma,mb\in\mathbf Z}}
\frac{2h^0(X_2,mD_{a,b})}{m^2}
=1-2\operatorname{area}(T\setminus Q),
\]
which proves (1) **for section volume**. The two cases agree continuously at \(a=b\). The strict \(a+b<1\) ensures positive area, hence bigness.

## Nefness, negative part, and the b-divisor net

The total-transform classes \(H,E_1,E_2\) have intersection matrix \(\operatorname{diag}(1,-1,-1)\), so \((F')^2=(E_1-E_2)^2=-2\), \(F'\cdot E_2=1\), and \(D_{a,b}\cdot F'=a-b\). The five torus-invariant irreducible curves have classes
\[
F'=E_1-E_2,\quad E_2,\quad
L=H-E_1-E_2,\quad H-E_1,\quad H.
\]
Their intersections with \(D_{a,b}\), in order, are
\[
a-b,\quad b,\quad1-a-b,\quad1-a,\quad1.
\]
On a complete toric surface, nonnegative intersection with invariant curves characterizes nefness. These five values prove the nef criterion.

For \(b>a\), put \(t=(b-a)/2\), \(P=D-tF'\). Its five intersections, in the same order, are
\[
0,\quad (a+b)/2,\quad1-a-b,\quad1-(a+b)/2,\quad1.
\]
Thus \(P\) is nef, \(N=tF'\) effective, and \(P\cdot N=0\); (2) follows. Since \(D^2=1-a^2-b^2\) and \(N^2=-(b-a)^2/2\), the identity \(P^2=D^2+(b-a)^2/2\) matches the **independently counted** volume in (1). This cross-check does not assume an unproved identification of volume with the intersection number of a non-nef class.

On the base \(X_0\), the Cartier b-divisor root is \(H\), of volume \(1\). On models dominating \(X_2\), its trace is a pullback of \(D\). These models form a cofinal system among modifications of \(X_0\) by the existence of common resolutions, and the spaces of sections are unchanged under proper birational pullback to normal models (\(g_*\mathcal O=\mathcal O\), projection formula). Thus its **section-volume** has the same fixed value on the cofinal system. Applying the already printed big-toric analytic-volume theorem 21.13.45 to the toric realization identifies the analytic volume used in Definition 20.1.6 with the polygon volume. No sequential compactness or unproved interchange of limiting operations is being used.

## Exact finite-level arithmetic and limitations

At \(a=1/5\), \(b=2/5\), the root volume is \(1\), \(D^2=4/5\), but \(\operatorname{vol}_{X_2}(D)=41/50\). The polytope has the single effective constraint \(i+2j\ge 3m/5\). At **every** \(m=10k\), a direct arithmetic sum gives
\[
h^0(X_2,10kD)=41k^2+12k+1.
\]
Indeed there are \((10k+1)(10k+2)/2\) monomials in total and \(3k(3k+1)\) excluded by \(i+2j<6k\). Their difference is the displayed polynomial. The exact small-check script also tests five rational parameter pairs and 14 finite-level identities; no numerical optimization is used to infer coefficients.

**Status:** *verified conditional deduction*, low severity. The original Proposition 20.1.2 and Definitions 20.1.5/.6/.10 are correct in this model. In particular the result **does not** change Example 20.1.9, which concerns moving blowup centers and upper semicontinuity rather than fixed infinitely near points. The analytical toric mass theorem 21.13.45 and the general b-divisor-current nefness theorem 20.1.15 are **not fully certified** by this calculation. The latter's regularization-dependent steps are outside user-authorized scope and remain **deferred-by-user**.

**Proposed optional correction/addition (not applied):** insert a separate two-chamber, infinitely-near blowup illustration after Definition 20.1.10, retaining the source/permanent tags and historical attribution, to prevent confusion between root volume, realization self-intersection, and actual big non-nef b-divisor volume.

**Precise coverage:** first direct proof-level inspection of this particular chamber model within **previously partially visited** §§20.1 and 21.13. Newly first-visited numbered sections: **0**. Entirely certified sections: **0**. Current main ToC: **25 chapters, 747 numbered sections**. No source/main/registry/canonicalization/tag/website changes; no project build, test suite, GitHub Actions, or formal verification. All user-excluded Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale-atlas/positivity-loss programmes remain **deferred-by-user**, not resolved.