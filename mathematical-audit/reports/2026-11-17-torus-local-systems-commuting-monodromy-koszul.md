# Commuting monodromy on a two-torus: an integral Koszul cochain test

**Date:** 2026-11-17  
**Finding:** `POME-TORUS-LOCAL-PAIR-KOSZUL-TORSION-001`  
**Severity/status:** low / **verified conditional deduction**, not a false printed theorem, not a proof repair, and not an independent certification of the topological comparison inputs.  
**Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`  
**Primary integrated path:** `docs/sections/sheaf-cohomology-and-acyclic-resolutions--sheaves-resolutions-and-cohomology/index.html`, blob `7a67c86dfb218e1846f0735a8f24f57b65f431fd`; §10.43 Theorem **10.43.16**, source label `demailly-complex-geometry:B5A98C8B`, permanent tag `678E4157C53F`, physical lines **296–310**, with double-complex Lemma **10.43.15** source `demailly-complex-geometry:40652A02`, permanent tag `9D23E3CA1553`, physical lines **282–290**.  
**Supporting integrated path:** `docs/sections/spectral-sequences-support-and-cup-products--local-systems-and-a-singular-comparison-with-supports/index.html`, blob `66ca556aac90cacad01dec69e61943398c888865`; Theorem **10.70.3**, source `demailly-complex-geometry:223C7EB2`, permanent tag `9E4C37619D42`, physical lines approximately **72–103** (local-system singular/sheaf comparison).  
**Earlier distinct result:** `POME-CIRCLE-LOCAL-MONODROMY-001` concerns *one* circle and a single automorphism, not two commuting automorphisms or higher-degree torsion. This note explicitly builds on it without counting it as a new result.

## Exact statement

Let (R) be a commutative ring with identity, (L) an arbitrary (R)-module (no finite generation, projectivity, flatness or characteristic assumption), and (A,B\in\operatorname{Aut}_R(L)) with (AB=BA). Let (ℒ_{A,B}) be the locally constant sheaf on (T^2=\mathbb R^2/\mathbb Z^2) whose monodromies around the two oriented basic loops are (A,B). Put (P=A-I, Q=B-I). Then sheaf cohomology is computed by the explicit complex
\[
0\longrightarrow L\xrightarrow{\ d^0\ } L\oplus L\xrightarrow{\ d^1\ }L\longrightarrow0,
\quad d^0(v)=(Pv,Qv),\qquad d^1(x,y)=Qx-Py.
\]
In particular
\[
\begin{aligned}
H^0(T^2,\mathcal L_{A,B})&=\ker P\cap\ker Q,\\
H^1(T^2,\mathcal L_{A,B})&=
 \frac{\{(x,y)\in L^2:Qx=Py\}}
 {\{(Pv,Qv):v\in L\}},\\
H^2(T^2,\mathcal L_{A,B})&=L/(PL+QL),\\
H^j(T^2,\mathcal L_{A,B})&=0\quad(j>2).
\end{aligned}
\]
All formulas are natural in (R)-linear maps of modules intertwining both monodromies. The displayed (d^1\) sign depends on an orientation choice for the square and has no effect on the cohomology.

## Proof by finite Čech reduction, without flatness or averaging

Cover each factor (S^1) by two connected contractible arcs (U_0,U_1) with (U_0\cap U_1) the disjoint union of two contractible arcs. The four rectangles (U_i\times U_j) cover (T^2). Every nonempty finite intersection is a disjoint union of contractible rectangles; (ℒ_{A,B}) is constant on each rectangle. Such intersections are acyclic by the local-system comparison Theorem 10.70.3 and elementary contraction. The acyclic-cover theorem 10.43.16 consequently computes sheaf cohomology by Čech cochains of this concrete cover.

Equivalently, apply two-open Mayer–Vietoris in each circle factor. The resulting finite rectangular Čech double complex has bidegrees (0\le p,q\le1) and (R)-module sizes (L^4,L^8,L^4) in total degrees (0,1,2). Its horizontal differential on each pair of one-circle 0-cochains is
\[
d_A(a,b)=(b-a,b-Aa).
\]
The vertical differential is the analogous (d_B); their actions commute because (AB=BA). Their totalization uses the sign ((-1)^p) as in §10.43.15. This description may also be obtained by contracting the extra ordered Čech summands in the ordinary four-rectangle Čech complex; the contraction is the usual finite indexed-Čech row contraction of §10.43.14–15, so it does not assume a general Čech/sheaf equality for arbitrary spaces.

Make the *invertible* input change ((a,b)\mapsto(a,c=b-a)) and the *invertible* output change ((x,y)\mapsto(x,y-x)). The differential becomes
\[
(a,c)\longmapsto(c,(I-A)a).
\]
It splits into an identity two-term contractible summand and the reduced two-term complex (L\xrightarrow{I-A}L). All changes are built from (I,A), hence commute with the vertical (B)-operators; they can be made simultaneously in the rectangular bicomplex. Contract the identity summand, then apply the same reduction vertically using (B). The surviving total complex has ranks (L,L^2,L), with differentials (A-I,B-I) and (Qx-Py) after harmless degreewise signs, exactly as displayed. The identity
\[
d^1d^0(v)=Q Pv-P Qv=0
\]
uses precisely (AB=BA). Taking kernels and cokernels gives the four formulas. This is a finite algebraic reduction of finite products of (L), so no tensor exactness, division, subsequence, or derived inverse limit is hidden. □

## Tests of the hypotheses and the integral torsion

1. If (A-I) is invertible on (L), all four cohomology groups vanish. Indeed (H^0=H^2=0); given a 1-cocycle ((x,y)), subtract (d^0(P^{-1}x)). The remaining pair is ((0,y-QP^{-1}x)); commutativity and (d^1=0) imply (P(y-QP^{-1}x)=0), hence it is zero. The same holds if (B-I) is invertible. For a field this applies whenever one scalar monodromy is not 1.
2. Over the **integers**, take (L=\mathbb Z^2), (m\ge2),
\[
 A_m=\begin{pmatrix}1&m\\0&1\end{pmatrix},\qquad B=I.
\]
Then (P(a,b)=(mb,0),\ Q=0). Direct computation gives
\[
H^0\simeq\mathbb Z,\qquad
H^1\simeq\mathbb Z^2\oplus\mathbb Z/m,\qquad
H^2\simeq\mathbb Z\oplus\mathbb Z/m.
\]
Thus integral torsion occurs in **both** degrees 1 and 2 for a locally free rank-two integral local system. Replacing coefficients by (\mathbb R) erases that torsion; a de Rham rank-only check cannot certify the integral answer. The free ranks satisfy (1-2+1=0=\chi(T^2)\operatorname{rank}L).
3. **Commutativity is essential:** formally (d^1d^0=(B-I)(A-I)-(A-I)(B-I)=BA-AB). Noncommuting (A,B) do not even define a representation of (\pi_1(T^2)=\mathbb Z^2), nor the asserted complex.

## Classification, proposed addition, and dependency limit

The printed Theorems 10.43.16 and 10.70.3 are **not refuted**. This is a concrete generalization of the earlier one-circle computation using *two commuting monodromies* and a new integral degree-two obstruction. Proposed optional addition: a worked two-torus local-system cohomology example near the §§10.43/10.70 comparisons; do not replace or merge existing statements. Affected interpretive dependents are calculations using local-system cohomology, Čech covers, integral coefficient torsion, and product spaces; no faulty dependent theorem is claimed.

**Uncertified upstream inputs:** the full correctness of the printed general sheaf/Čech comparison 10.43.16 and local-system singular/sheaf comparison 10.70.3 is inherited, not re-proved here. The finite Čech algebra is checked directly; no whole section or chapter receives a complete transitive certificate. Historical attribution remains unchanged. User-excluded Demailly approximation/regularization and its dedicated Bergman, (L^2), Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss programme remain **deferred-by-user** and were not examined. No project build, tests, CI, or site publication was performed.
