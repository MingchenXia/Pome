# A small-resolution degree obstruction for the threefold quadric cone

**Date:** 2026-11-07. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Finding:** POME-NODE-SMALL-RESOLUTION-DEGREE-001. **Severity:** low. **Status:** verified conditional deduction; the printed propositions and example are **correct**, not false theorems. The explicitly constructed resolution and degree calculation below are proved directly. This is an additional geometric audit, not a certification of the entire section or a reconstruction of the full local analytic class group.

**Pinned integrated reading text.** <code>docs/sections/analytic-cycles-and-cartier-cycles/index.html</code>, production main blob <code>d4817ac64b1365bd967d42cd474fec169f992e28</code>, physical lines 28–45 (Proposition 20.6.4, source <code>demailly-complex-geometry:BD1D45B4</code>, permanent tag <code>AA96C35C8290</code>) and 46–75 (Example 20.6.5 and its integrated rank-one proof, source <code>demailly-complex-geometry:E054C396</code>, permanent <code>0C462992AB3A</code>). The cycle definition Proposition 20.6.3 (source <code>demailly-complex-geometry:02B65FA7</code>, permanent <code>FD8966432506</code>) is context at lines 12–27. These are current Pome locators, not source-book theorem numbers.

## Precise new geometric computation

Let
\[
 X=\{(x,y,z,w)\in\mathbb C^4:xy+zw=0\},\qquad
 A=\{x=z=0\}\cap X,\quad B=\{x=w=0\}\cap X.
\]
Both A and B are irreducible effective Weil divisors on the reduced threefold X. The singular locus of X is exactly the origin. The previously audited four-ruling calculation, POME-CYCLE-FOURRULING-CARTIER-001, already established the non-torsion class of A using rank-one semi-invariants; **do not record that class-group statement a second time as a novel discovery**. The genuinely new item here is an explicit **proper small resolution**, its exceptional normal bundle, and the **opposite degrees of the two strict transforms on its contracted curve**.

Use the rank-one matrix
\[
 M=\begin{pmatrix}x&z\\-w&y\end{pmatrix},\qquad\det M=xy+zw.
\]
Introduce a column-image direction \([s:t]\in\mathbb P^1\), and set
\[
Y=\{(M,[s:t])\in X\times\mathbb P^1:\ tx+sw=0,\ tz-sy=0\}.
\]
On the chart \(s=1\), put \(q=t/s\), \(u=x\), \(v=z\). The equations give
\[
 (x,y,z,w)=(u,qv,v,-qu),\quad [s:t]=[1:q].
\]
On the chart \(t=1\), put \(r=s/t\), \(U=-w\), \(V=y\). They give
\[
 (x,y,z,w)=(rU,V,rV,-U),\quad [s:t]=[r:1].
\]
The overlap transitions are
\[
r=q^{-1},\qquad U=qu,\qquad V=qv.
\]
These are exactly the fiber-coordinate transitions for the tautological line \(\mathcal O_{\mathbb P^1}(-1)\), twice. Therefore
\[
Y\simeq\operatorname{Tot}\bigl(\mathcal O_{\mathbb P^1}(-1)
 \oplus\mathcal O_{\mathbb P^1}(-1)\bigr)
\]
as a smooth complex threefold. Both displayed charts are affine three-spaces, independently checking smoothness and \(\det M=0\). The morphism \(\pi:Y\to X\) is proper because Y is closed in \(X\times\mathbb P^1\) and \(\mathbb P^1\) is compact. For every nonzero rank-one M, its column image line is unique, and the inverse is holomorphic on the open sets where an individual column is nonzero. Hence \(\pi\) is an isomorphism over \(X\setminus\{0\}\). Its exceptional fiber \(E=\pi^{-1}(0)\) is the zero section \(\mathbb P^1\), **codimension two** in Y; there is no exceptional divisor. Its normal bundle is
\[
N_{E/Y}\simeq\mathcal O_{\mathbb P^1}(-1)^{\oplus2}.
\]
No general resolution theorem or analytic approximation is used for this explicit example.

Let \(p:Y\to\mathbb P^1\) be the bundle projection. The strict transform of A is
\[
\widetilde A=p^{-1}([0:1]).
\]
Indeed, in the \(s=1\) chart the equations \(x=z=0\) force \(u=v=0\), just the exceptional curve; in the \(t=1\) chart they read \(rU=rV=0\), whose divisorial branch away from E is \(r=0\). Thus \(\widetilde A\) is a smooth Cartier divisor and meets E transversally in the single point \([0:1]\). It is the zero divisor of the pullback of the standard section \(s\) of \(\mathcal O_{\mathbb P^1}(1)\), and consequently
\[
\mathcal O_Y(\widetilde A)=p^*\mathcal O_{\mathbb P^1}(1),
\qquad \boxed{\deg_E\mathcal O_Y(\widetilde A)=+1}.
\]

Similarly, the strict transform \(\widetilde B\) is given by \(u=0\) on \(s=1\) and by \(U=0\) on \(t=1\); both equations define one smooth divisor. In the first chart \(x=u\), whereas in the second \(x=rU\). Hence as *Cartier divisors on Y*
\[
\operatorname{div}_Y(x)=\widetilde A+\widetilde B.
\]
Since a principal divisor has trivial associated line bundle,
\[
\boxed{\deg_E\mathcal O_Y(\widetilde B)=-1}.
\]
This also checks the coefficient-one decomposition \(\operatorname{div}_X(x)=A+B\) on the regular locus of X; neither A nor B individually needs to descend as a Cartier divisor at the vertex.

## The degree obstruction (independent of the earlier C-star proof)

Suppose \(mA\) were locally Cartier near the origin for some nonzero integer m. By the local Cartier-cycle definition in Proposition 20.6.4, it is the divisor of a meromorphic function f on a sufficiently small neighborhood of the origin. Pull back f under the proper bimeromorphic \(\pi\). Over \(Y\setminus E\) its divisor is \(m\widetilde A\). Since E has codimension two in the smooth Y, it cannot carry any additional codimension-one component of \(\operatorname{div}_Y(f\circ\pi)\). Thus, near E,
\[
\operatorname{div}_Y(f\circ\pi)=m\widetilde A.
\]
The left side is principal, so its associated line bundle restricts trivially to the contracted curve E. The right side restricts to \(\mathcal O_{\mathbb P^1}(m)\), of nonzero degree m. This contradiction proves that **no nonzero integral multiple of A is Cartier at the vertex**, now by an intrinsic curve-degree obstruction. The same reasoning applies to B with degree \(-m\).

More generally, for any divisor locally pulled back from a Cartier divisor on X, its associated line bundle restricts trivially to E, because the map \(E\to X\) is constant. The displayed \(\pm1\) degrees distinguish the strict transforms of A and B from such pullbacks. This is a geometric refinement and independent check of the older four-ruling Cartier lattice, not a new assertion that the entire analytic local class group has been determined.

## Finding classification, dependencies, and proposed correction

**Classification:** POME-NODE-SMALL-RESOLUTION-DEGREE-001 — low / verified conditional deduction. All explicit charts, properness, fibers, normal bundle, strict transforms, and degree calculations are directly justified above. The only standard background is the elementary divisor-line-bundle correspondence on a smooth complex manifold and \(\deg\mathcal O_{\mathbb P^1}(m)=m\). Proposition 20.6.4 supplies the precise Cartier-cycle convention. No regularization, Bergman kernel, weighted L2, Ohsawa–Takegoshi theorem, multiscale atlas, or positivity-loss estimate is used.

**Affected dependents:** Example 20.6.5 (a second obstruction proof), Proposition 20.6.4 (Cartier/Weil distinction); potentially the reader's interpretation of modification traces and Cartier b-divisors in Chapter 20, but no downstream b-divisor statement has been certified by this argument. The old finding POME-CYCLE-FOURRULING-CARTIER-001 retains its status and scope.

**Proposed optional reading addition, not applied:** after Example 20.6.5, a short remark can display the proper small resolution \(Y=\operatorname{Tot}(\mathcal O(-1)^{\oplus2})\), the contracted curve, and the degree \(+1\) of \(\widetilde A\) on E. Keep both the original rank-one proof and its source attribution, stable tag, and statement unchanged. Do **not** infer ordinary pullback of non-Cartier Weil divisors on X.

**Coverage boundary:** first new *method* in already sampled §20.6; only the pinned lines and the explicit model are reviewed. No full Proposition 20.6.3/4 dependency-chain verification, complete section certification, analytic local class-group calculation, project build/test, CI, or publication claim. The current inventory remains **25 chapters / 747 numbered sections / zero whole mathematical-section certifications**. All earlier resolved/unresolved/deferred entries remain intact, with the user's excluded programme still **deferred-by-user**.
