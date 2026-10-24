# Circle-local-system monodromy, integral torsion, and the sheaf/Čech comparison

**Audit date:** 2026-10-24 (Asia/Shanghai). **Main SHA read afresh:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting review-branch head:** 819f23618f6aaa89d7e4bae734e86636e118edb1.

**Scope.** This is a first selected proof-level pass over the current *integrated reading edition* in §§10.43–10.44, 10.67, and 10.70, not a certification of all four sections or their transitive analytic/topological inputs. The dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme is **deferred-by-user** and was not examined. The occurrence of an author/book identifier in the unrelated sheaf-theoretic source provenance is not a reason to reopen that excluded programme.

## Finding POME-CIRCLE-LOCAL-MONODROMY-001

**Status:** verified conditional deduction. **Severity:** low (useful exact computation, no false printed theorem or missing proof alleged). **Proposed change:** optional worked proposition, after the local-system comparison; no proposed change to a theorem's hypotheses, permanent tag, historical attribution, or canonicalization.

**Precise prerequisites and integrated anchors:**

1. Proposition 10.70.1, source label **demailly-complex-geometry-5E45D1E2**, permanent tag **3CBF93FB0039**, §10.70 HTML lines **8–32**: equivalence of locally constant module sheaves and monodromy representations, with endpoint transport conventions. Theorem 10.70.3, source label **demailly-complex-geometry-223C7EB2**, tag **9E4C37619D42**, lines **72–103**, supplies local-system singular/sheaf comparison on manifolds. Exact path: docs/sections/spectral-sequences-support-and-cup-products--local-systems-and-a-singular-comparison-with-supports/index.html; blob **66ca556aac90cacad01dec69e61943398c888865**.
2. Theorem 10.43.16, source **demailly-complex-geometry-B5A98C8B**, permanent tag **678E4157C53F**, §10.43 HTML lines **296–313**: an acyclic open cover computes sheaf cohomology by Čech cohomology. Proposition 10.43.2, source **demailly-complex-geometry-5021AB5D**, tag **64E16AF43980**, lines **41–56**, describes the direct image of a local system under a finite covering. Exact path: docs/sections/sheaf-cohomology-and-acyclic-resolutions--sheaves-resolutions-and-cohomology/index.html; blob **7a67c86dfb218e1846f0735a8f24f57b65f431fd**.
3. Theorem 10.44.12, source **demailly-complex-geometry-8EC5A774**, tag **E83248AB1E9D**, §10.44 HTML lines **163–196**, identifies global Čech and sheaf cohomology on paracompact spaces. Proposition 10.44.14, source **demailly-complex-geometry-AE979C9C**, tag **54F5489B5EF9**, lines **200–224**, proves the integral homotopy equivalence between full and alternating Čech complexes. Exact path: docs/sections/sheaf-cohomology-and-acyclic-resolutions--soft-sheaves-and-paracompact-comparison/index.html; blob **c40db93edfa6c8a63b15001ecb40837fa321d6a8**.
4. Lemma 10.67.4 and Corollary 10.67.5 (free modules and cyclic torsion over a PID), plus the chosen termwise-flat Künneth convention of Theorem 10.67.7, source label **demailly-complex-geometry-018C5C2F**, tag **669128A0733C**, §10.67 HTML lines **142–210**. Exact path: docs/sections/spectral-sequences-support-and-cup-products--algebraic-tensor-products-and-universal-coefficients/index.html; blob **fc7abc376ab34a4f6436d92820088f13f1bf69f9**. This is a normalization and torsion crosscheck, not an assertion that the full unbounded Künneth proof has been independently certified.

### Statement and proof

Let \(R\) be a commutative ring with identity, let \(L\) be an \(R\)-module and let \(T\in\operatorname{Aut}_R(L)\). Let \(\mathcal L_T\) denote the locally constant sheaf on the oriented circle \(S^1\) whose monodromy, after choosing a base fiber, is \(T\). Then

\[
\boxed{
H^0(S^1,\mathcal L_T)\cong\ker(T-I),\qquad
H^1(S^1,\mathcal L_T)\cong\operatorname{coker}(T-I),\qquad
H^j(S^1,\mathcal L_T)=0\quad(j\ge2).
}
\]

The identifications are \(R\)-linear and natural under maps of pairs \((L,T)\to(L',T')\) intertwining the monodromy. An arbitrary change of base-fiber identification conjugates \(T\), and does not alter the isomorphism types. No assumption of finite generation, a field coefficient, or a simply connected base is made.

**Proof.** Choose two proper open arcs \(U,V\) covering \(S^1\), each contractible and connected, whose intersection is the disjoint union \(A\sqcup B\) of two contractible arcs. After transporting a chosen fiber trivialization along \(U\) and \(V\), the restriction maps on the first intersection component can be taken to be identities; on the second, their difference is the action of \(T\), or \(T^{-1}\) if the chosen orientation is reversed. The open sets \(U,V,A,B\) are acyclic for \(\mathcal L_T\): they are unions of contractible intervals with constant coefficient systems, using the local-system comparison and singular prism contraction from §10.70.2–3. The acyclic-cover theorem 10.43.16 therefore applies *to this specific two-arc cover*, not only to the global Čech direct limit.

The alternating Čech cochain groups are
\[
C^0=L\oplus L,\qquad C^1=L\oplus L,\qquad C^j=0\ (j\ge2).
\]
With compatible choices of trivializations and of the sign of the Čech differential, the only nonzero differential is
\[
d:L\oplus L\longrightarrow L\oplus L,\qquad
d(a,b)=(b-a,\ b-Ta).
\]
This is legitimate for arbitrary \(R\)-modules: there is no division, no averaging over sheets, and no finite-rank hypothesis. The kernel satisfies \(b=a=Ta\), so \(\ker d\cong\ker(T-I)\). To calculate the cokernel, make the invertible change of input coordinates \(b=a+c\) and the invertible change of output coordinates \((x,y)\mapsto(x,y-x)\). The displayed differential becomes
\[
(a,c)\longmapsto \bigl(c,(I-T)a\bigr).
\]
The first summand is an isomorphism, so the cokernel is \(L/(I-T)L\), canonically isomorphic to \(L/(T-I)L\). No positive Čech degrees above one survive. Proposition 10.44.14 identifies this computation with the full ordered-tuple convention used throughout Pome. The conclusion follows from Theorem 10.43.16. The same formula can alternatively be transported through the natural §10.70.3 singular/sheaf comparison. \(\square\)

### Integral tests that matter for the surrounding cohomology

**Torsion in cohomology despite free stalks.** Take \(R=\mathbb Z\), \(L=\mathbb Z^2\) and
\[
T_m=\begin{pmatrix}1&m\\0&1\end{pmatrix},\qquad m\ge2.
\]
This lies in \(\mathrm{GL}_2(\mathbb Z)\), and \((T_m-I)(a,b)=(mb,0)\). Consequently
\[
H^0(S^1,\mathcal L_{T_m})=\mathbb Z(1,0),\qquad
H^1(S^1,\mathcal L_{T_m})\cong\mathbb Z\oplus\mathbb Z/m\mathbb Z.
\]
Thus a locally free rank-two integral local system can have nonzero torsion in degree-one cohomology. This warns against replacing integral coefficient calculations with real or rational de Rham computations and silently discarding torsion. For \(L=\mathbb Z\) and \(T=-1\), one gets \(H^0=0,\ H^1=\mathbb Z/2\mathbb Z\); after extending coefficients to \(\mathbb R\), \(T-I=-2\) becomes invertible and both groups vanish.

**Finite covering crosscheck.** Let \(f:S^1\to S^1\) be the connected covering of degree \(q\ge1\). By Proposition 10.43.2 the sheaf \(f_*\underline{\mathbb Z}\) has fiber \(\mathbb Z^q\) and cyclic permutation monodromy \(P\). The \(P\)-invariants are the constant-coordinate vectors, hence \(\mathbb Z\). Summation of coordinates annihilates \((P-I)\mathbb Z^q\). Conversely any integer vector of sum zero is an integral sum of consecutive differences \(e_i-e_{i+1}\), all in \((P-I)\mathbb Z^q\). Thus the coinvariants are also \(\mathbb Z\), giving
\[
H^j(S^1,f_*\underline{\mathbb Z})=
\begin{cases}\mathbb Z,&j=0,1,\\0,&j\ge2.\end{cases}
\]
More generally, a permutation action with \(c\) orbits has \(\mathbb Z^c\) in degrees zero and one. The calculation is an exact integral check of the sheet-permutation transition law; it does **not** assert that arbitrary proper direct images are acyclic.

**Determinant test.** For a finite-rank integral \(L=\mathbb Z^r\) with \(T\in\mathrm{GL}_r(\mathbb Z)\) and \(\det(T-I)\ne0\), \(H^0=0\) and \(H^1\) is a finite group of order \(|\det(T-I)|\). This follows from the integer Smith diagonalization described in §10.67.4; no claim is made when the determinant is zero.

### Actual proof-level coverage and limitations

* §10.43: directly checked the local-homeomorphism/stalk argument and inverse-image/direct-image direction in Props. .1–2, exact-sequence boundary and five-lemma convention in Lemma .3, Godement stalk contraction in Thm. .5, section long-exact and flabby acyclicity in Thm. .7, horizontal double-complex elimination and the degree-one injectivity/acyclic-cover clauses in Thm. .16. §10.43.11's distributional Dolbeault exactness was *read* but its analytic local-exactness prerequisite was **not** re-proved.
* §10.44: directly checked shrinking/locally finite closed pasting, soft-lifting and acyclicity clauses (.2, .4, .7–9); focused on componentwise refinement lifting in Lemma .11, the compatibility of Čech/Godement connecting morphisms in Thm. .12, and the integer (factorial-free) homotopy onto alternating cochains in Prop. .14. No complete proof-chain certification is claimed.
* §10.67: read the Tor-flat-resolution and PID normalization (Lemmas .2–4, Cor. .5), the degreewise free cone replacement, direct-sum unbounded totalization, Künneth injection/splitting argument in Thm. .7 and the \(E_2\) comparison/non-convergence caveat in Prop. .11. The reviewed statements distinguish naturality from nonnatural splitting; their remaining infinite-complex dependencies are not marked certified. Nothing here uses the excluded analytic approximation programme.
* §10.70: checked the monodromy quotient/conjugation conventions in Prop. .1, finite barycentric subdivision and local-coefficient transport in Lemma .2, and selected Čech/sheaf comparison, supported-kernel and cup-product passage in Thm. .3. Compatibility with cup products was **not** independently certified back through §10.58.3.
* No identified *false* statement, confirmed proof gap or genuine mathematical duplicate in these selected passages. This finding is explicitly a **conditional corollary** of the specified internal theorems, not certification of all of those theorems.

**Proposed insertion:** a worked local-system example after Proposition 10.70.1 or Theorem 10.70.3, citing the precise internal §10.43–10.44 Čech calculation, followed by the integral unipotent example. This would help the downstream spectral-sequence, coefficient-change and supported-cohomology discussions. No production source, integrated reader, canonical registry, or permanent tag was modified.

**Actions and validation:** Current main and audit branch were read; mathematical identities above were proved directly from the printed differential and by integral row operations. No project build, tests, CI, formalization, numerical experiment, website publication, merge or automatic PR operation was performed. The 747 ToC section rows are a *coverage inventory*, not a set of certified results. All previously logged findings, including historical investigations of §§10.26–10.29, retain their previous statuses; the dedicated excluded approximation programme remains **deferred-by-user**.
