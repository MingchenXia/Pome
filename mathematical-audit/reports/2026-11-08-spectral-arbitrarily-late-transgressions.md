# Arbitrarily late nonzero differentials in finite first-quadrant double complexes

**Finding:** POME-SPECTRAL-SHARP-LATE-TRANSGRESSION-001.  
**Class:** low / **verified conditional deduction**; no printed theorem is refuted.  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Integrated reading edition:** docs/sections/spectral-sequences-support-and-cup-products--filtered-complexes-and-spectral-sequences/index.html; Git blob **2d26dcf0ea764f1d8823bae057dc951063053a50**.

**Precise sources and anchors:** Theorem 10.54.2, **demailly-complex-geometry:311B37F9**, permanent tag **E83B7568FE4B**, physical lines 23–41; Theorem 10.54.6, **demailly-complex-geometry:F23F5EAE**, permanent tag **C060D8E63B4F**, lines 114–139; Theorem 10.54.7, **demailly-complex-geometry:B32921E0**, permanent tag **BD1FDFF09B89**, lines 141–160. The finite-filtration and page-stabilization argument of Theorem 10.54.3 was checked in the intervening lines. The source name refers to complex geometry, *not* to the owner-excluded approximation/regularization proof programme.

## Statement and scope

For every integer $r\ge3$, there exists a bounded first-quadrant double complex $K_r^{p,q}$ of **finite free abelian groups**, with anticommuting horizontal and vertical differentials, such that:

1. Its column spectral sequence has only two nonzero groups on every page $E_1,E_2,\ldots,E_r$:
   $$
   E_s^{0,r-1}\cong\mathbb Z,\qquad E_s^{r,0}\cong\mathbb Z
   \quad(1\le s\le r).
   $$
   All differentials $d_s$ with $s<r$ vanish, but
   $$
   d_r:E_r^{0,r-1}\longrightarrow E_r^{r,0}
       \quad\text{is multiplication by }(-1)^{r-1}.
   $$
2. The total complex is **acyclic**, hence $E_{r+1}=0$.
3. For all $2\le s\le r$, the top-edge map $H^{r-1}(\operatorname{Tot}K_r)\to E_s^{0,r-1}$ is **not surjective**, and the bottom-edge map $E_s^{r,0}\to H^r(\operatorname{Tot}K_r)$ is **not injective**. Both maps still exist, exactly as asserted in Theorem 10.54.7.
4. The source total degree is optimal: every nonzero differential $d_r$ in any first-quadrant cohomological spectral sequence originates in total degree at least $r-1$, and this model realizes degree $r-1$.

The result is a uniform construction for **all $r\ge3$**, distinct from the earlier isolated $d_2$ calculation **POME-SPECTRAL-D2-ZIGZAG-001**, which remains valid and unchanged.

## Explicit integral bicomplex and full proof

Fix $r\ge3$ and let all unlisted components be zero. Take a copy of $\mathbb Z$ with generator $a_j$ in bidegree $(j,r-1-j)$ for every $0\le j\le r-1$, and a copy with generator $b_j$ in bidegree $(j+1,r-1-j)$ for every $0\le j\le r-1$. Thus
$$
a_j\in K_r^{j,r-1-j},\qquad
b_j\in K_r^{j+1,r-1-j}
\qquad(0\le j\le r-1).
$$

Define
$$
d_h a_j=b_j\quad(0\le j\le r-1),\qquad
d_v a_0=0,\qquad
d_v a_j=b_{j-1}\quad(1\le j\le r-1),
$$
and put $d_hb_j=d_vb_j=0$ for every $j$. Every $a_j$ has total degree $r-1$, every $b_j$ has total degree $r$, and all components lie in the first quadrant. Since *both composites* $d_hd_v$ and $d_vd_h$ vanish (they land in generators $b_j$ on which all differentials vanish), the actual anticommutation convention
$$
d_h^2=d_v^2=0,\qquad d_hd_v+d_vd_h=0
$$
of Theorem 10.54.6 holds over $\mathbb Z$ without a sign convention change.

The column filtration of $\operatorname{Tot}K_r$ has first page the vertical cohomology. Each intermediate column $j=1,\ldots,r-1$ contains the vertical two-term **isomorphism**
$$
\mathbb Z a_j\xrightarrow{d_v}\mathbb Z b_{j-1}.
$$
Only $a_0$ in column $0$ and $b_{r-1}$ in column $r$ remain, giving
$$
E_1^{0,r-1}=\mathbb Z[a_0],\qquad
E_1^{r,0}=\mathbb Z[b_{r-1}],
$$
with every other $E_1^{p,q}=0$. A page-$s$ differential has bidegree $(s,1-s)$. For $s<r$, the only possible arrow out of $(0,r-1)$ lands in $(s,r-s)$, whose $E_1$-group is zero. There is no other nonzero source. Inductively $d_s=0$ and $E_{s+1}=E_s$ for $1\le s<r$.

To compute the *actual* $r$-th page differential using the printed filtered representatives, put
$$
c=\sum_{j=0}^{r-1}(-1)^j a_j\in
F^0\operatorname{Tot}^{r-1}K_r.
$$
The two sums telescope:
$$
Dc=\sum_{j=0}^{r-1}(-1)^jb_j+
\sum_{j=1}^{r-1}(-1)^jb_{j-1}
=(-1)^{r-1}b_{r-1}\in
F^r\operatorname{Tot}^{r}K_r.
$$
Thus $c\in Z_r^{0,r-1}$, while its class modulo $F^1$ is exactly $a_0$. The rule $d_r[x]=[Dx]$ in Theorem 10.54.2 now gives
$$
\boxed{d_r[a_0]=(-1)^{r-1}[b_{r-1}].}
$$
The target is a nonzero integral generator, so this is an **isomorphism**, and $E_{r+1}=0$.

An *independent* verification of total acyclicity avoids any appeal to spectral convergence. The total complex has just the degrees $r-1$ and $r$:
$$
0\longrightarrow
\operatorname{Tot}^{r-1}K_r\xrightarrow{D}
\operatorname{Tot}^{r}K_r\longrightarrow0.
$$
In the ordered free bases $(a_0,\ldots,a_{r-1})$ and $(b_0,\ldots,b_{r-1})$ its differential is the upper bidiagonal integer matrix
$$
D_{ij}=\delta_{ij}+\delta_{i,j-1},
\qquad 0\le i,j\le r-1.
$$
Every diagonal entry is $1$, so $\det D=1$; thus $D\in\mathrm{GL}_r(\mathbb Z)$. In particular **all total cohomology vanishes integrally**, not merely rationally. The calculation has no completion, torsion, extension or limiting assumption.

For any first-quadrant spectral sequence, if
$$
d_r:E_r^{p,q}\longrightarrow E_r^{p+r,q-r+1}
$$
is nonzero, its target must satisfy $q-r+1\ge0$. Hence $q\ge r-1$ and source total degree $p+q\ge r-1$. The constructed $d_r:E_r^{0,r-1}\to E_r^{r,0}$ attains equality.

Finally $H^{r-1}(\operatorname{Tot}K_r)=H^r(\operatorname{Tot}K_r)=0$. For $2\le s\le r$, Theorem 10.54.7's maps specialize to $0\to\mathbb Z$ and $\mathbb Z\to0$, respectively. Neither is an isomorphism; the former is not surjective and the latter is not injective. The printed result claims neither stronger property, so **it remains correct**.

## Classification, possible note, dependents and boundaries

**Severity:** low. **Status:** verified conditional deduction (indeed an elementary integral proof with no new external mathematical input). This is a *sharp limitation of tempting unprinted strengthening*, **not a confirmed false theorem, missing proof, or repair**. Specifically, first-quadrant boundedness, the finite-page stabilization $E_2=\cdots=E_r$, and the mere existence of edge maps do *not* imply $E_2$ degeneration, nor injectivity/surjectivity of the edge maps. The precise convergence and five-term exact-sequence statements printed in §§10.54.2–7 remain intact.

**Proposed optional clarification (not applied to production):** add the all-$r$ model, or an abbreviated note after Theorem 10.54.7, retaining permanent tags and historical attribution. Downstream spectral-sequence applications deserving separate hypothesis checks include §10.55 (hypercohomology/direct images) and §10.84 (Frölicher filtration), **but this audit has not found or alleged an error in those sections**. The abstract bicomplex is not claimed to be realized as a Dolbeault double complex of a compact complex manifold.

**Exact coverage:** new selected proof-level reading of the already-partly-reviewed §10.54, not a first visit; **0** newly first-visited ToC sections and **0** complete mathematical-section certifications. Current actual inventory: **25 chapters / 747 numbered sections**. The Demailly approximation/regularization and dedicated Bergman, weighted $L^2$, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remains **deferred-by-user**. No build, tests, CI, formal verification, website publishing, source/registry/tag edits or production-main changes were made.
