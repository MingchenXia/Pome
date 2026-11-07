# Arbitrarily late first nonzero differentials in finite first-quadrant double complexes

**Finding:** `POME-SPECTRAL-SHARP-LATE-TRANSGRESSION-001`  
**Class:** low / **verified conditional deduction**; *no printed theorem is refuted*.  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated reading-edition file:** `docs/sections/spectral-sequences-support-and-cup-products--filtered-complexes-and-spectral-sequences/index.html`, blob `2d26dcf0ea764f1d8823bae057dc951063053a50`.  
**Source/permanent labels:** Theorem 10.54.2, source `demailly-complex-geometry:311B37F9`, permanent `E83B7568FE4B`, physical lines **23–41**; Theorem 10.54.6, source `demailly-complex-geometry:F23F5EAE`, permanent `C060D8E63B4F`, lines **114–139**; Theorem 10.54.7, source `demailly-complex-geometry:B32921E0`, permanent `BD1FDFF09B89`, lines **141–160**. The finite-filtration comparison and collapse conditions of Theorem 10.54.3 were also checked in the integrated passage preceding line 114. These are *spectral-sequence* statements from a complex-geometry source; no part of the owner-excluded Demailly approximation programme was opened.

## Exact statement and hypotheses

For **each integer** (r\ge 3), there exists a bounded, first-quadrant double complex (K_r^{p,q}) of **finite free abelian groups**, with anticommuting horizontal and vertical differentials, such that:

1. Its column spectral sequence has exactly two nonzero groups on pages (E_1, E_2,\ldots,E_r):
   [
   E_s^{0,r-1}\cong\mathbb Z,\qquad E_s^{r,0}\cong\mathbb Z\quad(1\le s\le r).
   ]
   Every (d_s) for (s<r) vanishes, but (d_r:E_r^{0,r-1}\to E_r^{r,0}) is multiplication by ((-1)^{r-1}).
2. The **total complex is acyclic**. Thus (E_{r+1}=0), even though the preceding (r-1) pages have not changed.
3. For each (2\le s\le r), the actual top-edge map (H^{r-1}(\mathrm{Tot}K_r)\to E_s^{0,r-1}) is not surjective, and the bottom-edge map (E_s^{r,0}\to H^r(\mathrm{Tot}K_r)) is not injective. This does **not** contradict Theorem 10.54.7, which only asserts existence/naturality of these edge maps.
4. The total-degree threshold is sharp: in *every* first-quadrant cohomological spectral sequence a nonzero (d_r) requires a source of total degree at least (r-1); the constructed source has exactly that degree.

This is a **new uniform-in-r construction**, not the previously logged four-term **nonzero (d_2)** example `POME-SPECTRAL-D2-ZIGZAG-001`.

## Complete integral construction and proof

Fix (r\ge3). Let all unspecified components be zero and take one copy of (mathbb Z) in each of
[
 a_j\in K_r^{j,r-1-j}\quad(0\le j\le r-1),\qquad
 b_j\in K_r^{j+1,r-1-j}\quad(0\le j\le r-1).
]
The symbols name free generators. Prescribe
[
 d_h a_j=b_j\quad(0\le j\le r-1),\qquad
 d_v a_0=0,\quad d_v a_j=b_{j-1}\quad(1\le j\le r-1),
]
and set both differentials to zero on every (b_j). Every (a_j) has total degree (r-1) and every (b_j) has total degree (r). Both (d_h) and (d_v) square to zero; each composite (d_hd_v) and (d_vd_h) is identically zero. Thus the **anticommutation** convention (d_hd_v+d_vd_h=0) of the actual Theorem 10.54.6 holds integrally, without a hidden sign conversion.

For the column filtration, (E_1) is vertical cohomology. In each intermediate column (j=1,\ldots,r-1), the vertical pair (a_j\mapsto b_{j-1}) is an isomorphism, hence acyclic. The two unmatched generators are (a_0\in K^{0,r-1}) and (b_{r-1}\in K^{r,0}). There are therefore exactly the two displayed (E_1) groups. A differential (d_s) has bidegree ((s,1-s)). For (s<r), its target from ((0,r-1)) is ((s,r-s)), a vacant term on the page; no other possible differential survives. Consequently (E_1=E_2=\cdots=E_r) as bigraded groups.

For an **actual filtered representative**, put
[
 c=\sum_{j=0}^{r-1}(-1)^j a_j\in F^0\mathrm{Tot}^{r-1}K_r.
]
A direct cancellation gives
[
 Dc=\sum_{j=0}^{r-1}(-1)^jb_j+
       \sum_{j=1}^{r-1}(-1)^j b_{j-1}
   =(-1)^{r-1}b_{r-1}\in F^r\mathrm{Tot}^{r}K_r.
]
Thus (c\in Z_r^{0,r-1}), reduces to (a_0) in the zeroth associated-graded column, and by the **printed representative rule** in Theorem 10.54.2,
[
 d_r[a_0]=(-1)^{r-1}[b_{r-1}].
]
The target class is nonzero on (E_r), so (d_r) is an isomorphism. The next page is zero by Theorem 10.54.2.

Independently of spectral convergence, the total complex consists only of
[
 0\longrightarrow \mathrm{Tot}^{r-1}K_r\xrightarrow{D}
 \mathrm{Tot}^{r}K_r\longrightarrow0 .
]
With columns ordered (a_0,\ldots,a_{r-1}) and rows (b_0,\ldots,b_{r-1}), its integer matrix is
[
 D_{ij}=\delta_{ij}+\delta_{i,j-1},\qquad 0\le i,j\le r-1.
]
This is upper bidiagonal with every diagonal entry (1), so (\det D=1). Hence (D\in\mathrm{GL}_r(\mathbb Z)) and the total complex has **zero cohomology in every degree**. This also proves that no torsion or completion issue is concealed in the spectral computation.

Finally any first-quadrant nonzero (d_r:E_r^{p,q}\to E_r^{p+r,q-r+1}) has target second index (q-r+1\ge0), forcing (q\ge r-1) and source total degree (p+q\ge r-1). Our ((0,r-1)\to(r,0)) differential attains equality. Since total cohomology is zero, the top-edge map (0\to\mathbb Z) and bottom-edge map (\mathbb Z\to0) on every (2\le s\le r) have respectively non-surjective and non-injective behavior. Both maps remain exactly as asserted in the original theorem.

## Mathematical classification, impact, and limits

**Severity:** low. **Status:** verified conditional deduction, with a fully elementary independent integral construction; published Theorems 10.54.2, 10.54.3, 10.54.6 and 10.54.7 are **not false**. No original proof gap is alleged. This model shows the hypothesis "degenerates at (E_2)" cannot be inferred from first-quadrant boundedness, (E_2)-page stability for an arbitrarily long finite interval, or the existence of natural edge maps. The proven per-degree total convergence remains intact.

**Proposed editorial addition (not applied):** after Theorem 10.54.7, insert the all-(r) double-complex model, or at least a note that the edge maps are not generally mono-/epimorphisms and that arbitrarily late first differentials occur even for bounded complexes of finite free modules. Preserve both theorem source attributions and permanent tags.

**Potential downstream audit targets:** the spectral-sequence comparisons in `docs/sections/spectral-sequences-support-and-cup-products--hypercohomology-and-direct-image-spectral-sequences/index.html` (§10.55) and `docs/sections/general-complex-cohomology-and-modifications--the-frolicher-filtration/index.html` (§10.84), but **no error is asserted in those sections without checking their exact hypotheses**. The construction is an abstract double complex; it is **not** claimed to arise from the Dolbeault complex of any compact complex manifold.

**Coverage:** new *selected* proof-level verification of §10.54.6–7 and all-(r) transgression sharpness in a section previously sampled for (d_2). Exactly **zero** newly first-visited ToC sections and **zero** whole mathematical sections certified; the actual current navigation remains **25 chapters / 747 numbered sections**. No project tests, build, GitHub Actions, formal verification, or website deployment were run. The Demailly approximation/regularization and dedicated Bergman, weighted (L^2), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remains **deferred-by-user**.
