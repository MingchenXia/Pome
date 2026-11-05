# Exact minimizing geodesics from proper approximate midpoints, and a complete nonproper countermodel

Date: 2026-11-05. Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Finding: **POME-METRIC-PROPER-APPROX-MIDPOINT-GEODESIC-001**.
Severity: low. Classification: **verified conditional deduction** (a stronger consequence of correct printed results, not a false theorem, not a complete audit of their full dependency chain).

## Pinning and actual mathematical scope

- Current reading-edition section: docs/sections/metric-completeness-and-compact-balls/index.html, main blob **4ad63fec32bfa9a18a12a5dbb009445a43693c86**.
- Approximate-midpoint axiom (Equation 2.22.2): physical lines **7–14**; source **demailly-complex-geometry:4BF7D568**, permanent **D0F673E1134B**.
- Dyadic approximation (Lemma 2.22.3): lines **17–35**; source **demailly-complex-geometry:B621C59E**, permanent **3B383470A6A3**.
- Complete approximate-midpoint spaces are length spaces (Proposition 2.22.4): lines **39–55**; source **demailly-complex-geometry:AC512055**, permanent **EB12C0B326CA**.
- Properness equivalence (Theorem 2.22.5): lines **59–83**; source **demailly-complex-geometry:7217AFA4**, permanent **883E85712A41**.
- Internal properness input: Lemma 9.28.1, docs/sections/separation-strict-exhaustions-and-coverings--strictly-plurisubharmonic-exhaustions-on-coverings/index.html, main blob **ef92b5dc5bb4c143345621ea60ca52f3ca7d1872**, lines **13–25**; source **demailly-complex-geometry:83A0D387**, permanent **9DBBB1BAE0CF**.
- Crosscheck only: Arzelà–Ascoli Proposition 2.7.4 in docs/sections/measures-and-distributions--nets-and-compactness/index.html, main blob **7e4a226a48f88a97b3db1a8dd7d8582c909aeea1**, lines **71–89**, source **foundations-of-pluripotential-theory:C7F49DCE**, permanent **2963E35FB0D3**. The proof below does not require this proposition.
- Separately checked the net compactness Proposition 2.7.1, Tychonoff Lemma 2.7.2 and bounded-measure Theorem 2.7.3 at physical lines **13–67** in that section for consistency of net and positivity conventions. In particular, Theorem 2.7.3 does not quantify over signed measures: positivity is explicitly fixed in §2.2, physical line **7**, in docs/sections/measures-and-distributions--radon-measures-and-integration/index.html, blob **f0086e0d7fa46b8d1756eebb839b0ba14e663863**. These crosschecks are **not** a claim to certify all of §2.7 or the Riesz representation theorem.

## Strengthening: proper approximate-midpoint spaces are geodesic

**Claim.** Let $(E,d)$ be a finite-valued metric space satisfying
\[
\inf_{z\in E}\max\{d(x,z),d(y,z)\}=\tfrac12d(x,y)\qquad(x,y\in E),
\]
and suppose every closed bounded ball is compact. Then for every $x,y\in E$ there is a map
\[
\gamma:[0,1]\longrightarrow E,\qquad
d(\gamma(s),\gamma(t))=|s-t|\,d(x,y),\quad
\gamma(0)=x,\quad\gamma(1)=y.
\]
In particular, **complete and locally compact approximate-midpoint spaces admit distance-realizing constant-speed geodesics**, strengthening the printed conclusion that they are length spaces.

**Proof.** Put $r=d(x,y)$. For $r=0$, use the constant curve. If $r>0$, choose for each $m\ge1$ a point $z_m$ for which
\[
d(x,z_m)\le r/2+1/m,\qquad d(z_m,y)\le r/2+1/m.
\]
The $z_m$ lie in the compact ball $\overline B(x,r/2+1)$; choose a convergent subsequence with limit $z$. Passing to the limit yields both distances at most $r/2$, while the triangle inequality yields their sum at least $r$. Thus
\[
d(x,z)=d(z,y)=r/2.
\]
**Every pair has an exact midpoint.** This conclusion uses properness essentially, not sequential compactness of an arbitrary nonmetrizable space: the ball is a **compact metric** subspace.

Recursively assign exact midpoints to every dyadic interval, keeping all earlier assignments. The resulting $a:D\to E$ for the dyadic numbers $D\subset[0,1]$ has $a(0)=x$, $a(1)=y$, and adjacent stage-$n$ values separated by exactly $r2^{-n}$. Hence the triangle inequality gives
\[
d(a(s),a(t))\le r|s-t|\quad(s,t\in D).
\]
Taking $s=0$ and $t=1$ and inserting an arbitrary $u\in D$ implies
$r\le d(x,a(u))+d(a(u),y)\le ru+r(1-u)=r$.
Consequently $d(x,a(u))=ru$. For $s<t$ the reverse triangle inequality now gives
\[
d(a(s),a(t))\ge d(x,a(t))-d(x,a(s))=r(t-s).
\]
Therefore $a$ is **exactly** a scaled isometry on $D$. Properness implies completeness (the easy direction of printed Theorem 2.22.5, also immediate from compactness of the ball containing any Cauchy sequence). Thus $a$ extends uniquely by Cauchy limits to the asserted isometry $\gamma$ on all of $[0,1]$. Its length is precisely $r$. $\square$

The only imported mathematical step for the second, complete-and-locally-compact formulation is the existing properness implication in Theorem 2.22.5 (with internal dependency Lemma 9.28.1). The first, proper formulation above is directly proved and needs no Arzelà–Ascoli, external Hopf–Rinow theorem, or regularization.

## Sharpness: completeness and approximate midpoints do not imply a minimizer without local compactness

Form a metric graph $G$ from countably many disjoint closed intervals $I_n=[0,1+1/n]$ by identifying all left endpoints to a vertex $p$ and all right endpoints to a vertex $q$. Give the quotient the **path-length metric**. Every path from $p$ to $q$ crosses a complete edge, while the lengths of the edges decrease to $1$. Hence
\[
d(p,q)=\inf_{n\ge1}(1+1/n)=1,
\]
but **no path of length $1$ exists**. For a precise crossing argument, take the first hitting time of $q$ and the last preceding hitting time of $p$ for any continuous path from $p$ to $q. Between them the image avoids both vertices and thus lies in one connected edge interior, connecting both ends; its length is at least $1+1/n>1$ for that edge.

The graph is a length metric space by construction, and hence has approximate midpoints by the directly checked Proposition 2.22.4. It is also **complete**. If a Cauchy sequence has a subsequence approaching either of the two vertices, the whole sequence converges to that vertex (passing to a further subsequence if necessary). Otherwise its distances to both vertices are eventually bounded below by some $\delta>0$. Points on distinct edge interiors with that bound are separated by at least $2\delta$, since every connecting path must pass through $p$ or $q$. The Cauchy sequence is therefore eventually contained in one fixed compact edge, and converges.

However $G$ is **not locally compact** at $p$: for any sufficiently small $t>0$, the points at arclength $t$ from $p$ in the different edges are pairwise at distance $2t$. They all lie in $\overline B(p,2t)$, which is not totally bounded. This gives a complete, connected length space with approximate midpoints but no minimizing segment. It shows why the printed last sentence of §2.22 (the axiom alone does not ensure an attaining curve) cannot be strengthened without properness or comparable compactness.

Other hypothesis boundaries can be checked independently: $(0,1)$ with Euclidean distance is locally compact and has exact midpoints but is incomplete and its closed ball $\overline B(1/2,1/2)=(0,1)$ is noncompact. An infinite discrete space with distance $1$ between distinct points is complete and locally compact but fails the approximate-midpoint axiom, and its unit closed ball is not compact.

## Proof-chain check, status and proposed treatment

The exact dyadic recurrence printed in Lemma 2.22.3 is compatible with its strict $L>d(x,y)$ assumption; no midpoint is assumed in its proof. Proposition 2.22.4 uses completeness exactly when extending the dyadic Lipschitz map. Theorem 2.22.5 correctly invokes the **previously stated and proved internal** Lemma 9.28.1; it does not presuppose a minimizing curve in that lemma. Its converse requires no midpoint axiom. These checked local steps are consistent.

**Classification:** verified conditional deduction (low), NOT a confirmed error, proof gap, duplicate, or claim of complete verification of §2.22/§9.28. Suggested *proposed only* textual addendum after Theorem 2.22.5: “Under the equivalent conditions, any two points admit a distance-realizing constant-speed geodesic; properness upgrades approximate midpoints to exact midpoints, then dyadic interpolation gives the geodesic.” Retain original attribution and permanent tags. No body/source/registry change in this audit.

**Affected dependents:** geometric uses of the length/properness equivalence, Riemannian completeness and covering arguments around §9.28; a new geodesic consequence may be cited after editorial review but is not needed to justify any printed theorem. Earlier ledger findings remain unchanged. Demailly approximation/regularization and its dedicated Bergman, weighted-$L^2$, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work remain **deferred-by-user**.

**Coverage limit:** selective statement/proof checks in §§2.22.2–5, §2.7.1–4 and 9.28.1; none of the three whole numbered sections or their transitive dependencies is certified. Current established project navigation: 25 chapters, 747 numbered sections, zero whole-section mathematical certifications. No tests, builds, CI, formal proof check or website publication performed.
