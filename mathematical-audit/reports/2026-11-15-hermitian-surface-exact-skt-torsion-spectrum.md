# Exact SKT torsion spectrum in complex dimension two (2026-11-15)

**New stable finding:** POME-HERM-SKT-SURFACE-EXACT-TORSION-SPECTRUM-001 — **low / verified conditional deduction**; the printed Corollary 11.48.21 is correct but its norm estimate is nonoptimal on Hermitian surfaces. This is not the previously registered 2026-10-25 equation-alias/double-prime integration problem.

**Reviewed main commit:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Integrated reading-edition path:** docs/sections/hermitian-torsion-and-the-bochner-identity/index.html; Git blob 4656b430de6ec989ef121eca550afda0be407222.  
**Section:** 11.48, permanent section tag C9B4C5E646B1; source book demailly-complex-geometry.  
**Direct source/permanent anchors:** introductory Chern/exterior conventions, physical lines 5–20, source entry demailly-complex-geometry:2EE4DD59 / permanent 527E14D109BB; Lemma 11.48.9, source demailly-complex-geometry:28FD7941 / permanent A9F492A7F5C3, physical lines 97–154; torsion term (11.48.13), source demailly-complex-geometry:D2AA9D04 / permanent DBCAF8FF0340, lines 103–107; Theorem 11.48.15, source demailly-complex-geometry:72367915 / permanent E96E372480D4, lines 155–203; Corollary 11.48.20, source demailly-complex-geometry:B37247AF / permanent 222BB53B613A, lines 205–226; Corollary 11.48.21, source demailly-complex-geometry:7E456199 / permanent 5029210C26BC, lines 227–244 (especially the first-order estimate at lines 236–243).

## New exact assertion

Let $(X,\omega)$ be a Hermitian complex surface and write $a=\partial\omega\wedge$ for the degree-three exterior multiplication in (11.48.2). At any point put $r=|\partial\omega|_\omega$. Then the pointwise nonnegative Hermitian operator
\[
 Q:=aa^*+a^*a
\]
on the full complex exterior algebra is **exactly**
\[
 Q=r^2 P,\qquad P^2=P=P^*,\qquad \operatorname{rank}_{\mathbb C}P=4
 \quad (r>0).
\]
Here $P$ is explicitly the orthogonal projector onto the sum of the subspaces having either none or all of the three one-forms in a normalized decomposable representation of $\partial\omega$.

More precisely, with $P_{p,q}$ denoting its restriction to $\Lambda^{p,q}$, the nonzero bidegree blocks, for $r>0$, are:

| Bidegree | Spectrum of $Q|_{\Lambda^{p,q}}$ |
| --- | --- |
| $(0,0)$, $(2,2)$ | $\{r^2\}$ |
| $(0,1)$, $(2,1)$ | $\{0,r^2\}$ |
| All other $(p,q)$ | $\{0\}$ (with multiplicities $\binom{2}{p}\binom{2}{q}$) |

In particular,
\[
 0\le Q\le |\partial\omega|_\omega^2 I
\]
is a **sharp** full-algebra estimate: equality holds pointwise on scalar forms when $\partial\omega\ne0$. The bound is zero in all bidegrees $(1,q)$, as well as $(0,2)$ and $(2,0)$.

If in addition the surface is **pluriclosed** ($\partial\bar\partial\omega=0$), then (11.48.13) becomes $T_\omega=-Q$. Therefore the following sharper conditional variant of the *sufficient* vanishing criterion in Corollary 11.48.21 holds:
\[
 [\mathrm i\Theta,\Lambda]\ge bI,\qquad
 b>\sup_X|\partial\omega|_\omega^2
 \quad\Longrightarrow\quad
 [\mathrm i\Theta,\Lambda]+T_\omega>0.
\]
The printed surface threshold is $b>2N\sup|\partial\omega|^2=4\sup|\partial\omega|^2$ since $N=2\binom 22=2$. The coefficient **1** above is optimal for a bidegree-uniform *pointwise torsion bound*, not asserted to be the optimal global vanishing threshold on every bundle. In bidegrees $(1,q)$, $(0,2)$, $(2,0)$ the torsion term itself vanishes identically under the pluriclosed hypothesis, so any strict uniform positivity of the curvature commutator suffices. On $(0,1)$ and $(2,1)$ one may sharpen further by checking positivity of the anisotropic operator $[\mathrm i\Theta,\Lambda]-r^2P_{p,q}$ rather than using a scalar $b$.

## Complete pointwise proof

Choose a unitary $(1,0)$-coframe $(e_1,e_2)$ and its conjugate $(\bar e_1,\bar e_2)$. Since $\Lambda^{2,0}$ has complex dimension one, *every* $(2,1)$-form has the form
\[
 \partial\omega=e_1\wedge e_2\wedge
       (b_1\bar e_1+b_2\bar e_2).
\]
The two monomials are orthonormal in the conventions at lines 5–20 and 236–240, so $r^2=|b_1|^2+|b_2|^2$. For $r>0$ let $v=(b_1\bar e_1+b_2\bar e_2)/r$; choose $\sigma$ to complete $(v,\sigma)$ to a unitary $(0,1)$-coframe. We may thus write
\[
 a=r\,\varepsilon_{e_1}\varepsilon_{e_2}\varepsilon_v,
\]
where $\varepsilon_\zeta$ denotes exterior multiplication by the unit one-form $\zeta$. We never need to change the Chern connection or to assume that the coframe extends holomorphically.

For a monomial basis vector in
$\Lambda^*\langle e_1,e_2,v,\sigma\rangle$, record the occupancy of the three distinct generators $e_1,e_2,v$.
If none is occupied, $a$ sends it isometrically (up to a unit sign) times $r$ to the monomial with all three occupied; $a^*$ annihilates it. If all are occupied, $a^*$ sends it back isometrically times $r$ and $a$ annihilates it. If one or two of the three are occupied, both $a$ and $a^*$ annihilate that monomial, since respectively an exterior factor would be repeated or at least one contraction factor is absent.

Consequently $aa^*+a^*a$ acts by $r^2$ on precisely the 'none' and 'all' occupancy subspaces, and by zero on all other occupancy subspaces. The fourth generator $\sigma$ may be absent or present, giving two orthogonal basis vectors for each of the 'none' and 'all' cases: rank four in total. This proves the projector formula and $Q^2=r^2Q$. Tracking holomorphic and antiholomorphic degrees yields exactly the bidegree table. The case $r=0$ is immediate with $Q=0$.

For a pluriclosed surface the first term of the displayed formula (11.48.13) vanishes identically; note that this uses $\partial\bar\partial\omega=0$ and does **not** claim that $d\omega=0$. We get $T_\omega=-r^2P$ and $T_\omega\ge-r^2I$. The sharper strict positivity condition follows algebraically, and the cohomology vanishing / smooth primitive statement then follows **conditionally on the printed Hermitian Bochner identity and Corollary 11.48.20**, whose transitive global analytic proof chain is not certified here. This checks no Demailly approximation, Bergman, Ohsawa–Takegoshi, multiscale gluing or positivity-loss argument.

## Reproducible finite-dimensional check

The accompanying standard-library script checks the complete $16\times16$ exterior matrix for $b_1=3$, $b_2=4$, hence $r^2=25$. It verifies $Q^2=25Q$, $\operatorname{tr}Q=100$ (rank four), bidegree block invariance, and the claimed traces. It was executed locally and printed:

PASS: Q^2=25Q; rank(Q)=4; bidegree traces exact

This finite rational arithmetic check is only a consistency check; the occupancy argument above is the proof for arbitrary complex coefficients. No project test suite, site build, CI, browser verification or formal mathematical certification was run.

## Classification, action, dependencies, scope

**Status/severity:** low / verified conditional deduction. The printed Corollary 11.48.21 is **correct**, with an unnecessarily weak but safe estimate. The exact pointwise linear-algebra statement is proved. The proposed strengthened vanishing conclusion is conditional on the already printed Theorem 11.48.15, Corollary 11.48.20 and their elliptic/Hodge dependencies; it is not a verified replacement for the entire section.

**Proposed optional source patch only (not applied):** add a surface-specific note after Corollary 11.48.21 with the projector calculation and coefficient-one condition, preserving the existing dimension-independent bound, historical attribution, source and permanent tags. No correction to registry, canonicalization or published body is authorized by this audit.

**Affected dependents:** the quantitative sufficient criterion in §11.48.21 and applications requiring Hermitian torsion loss under a pluriclosed surface hypothesis. The previously confirmed rendering/typography findings POME-HERM-BOCHNER-EQUATION-ALIASES-001 and POME-HERM-BOCHNER-DOUBLEPRIME-001 are unchanged and neither resolved nor newly claimed.

**Actual coverage:** directly reviewed the displayed torsion operator and Hermitian vanishing argument at the line anchors above. §11.48 was already proof-level visited on 2026-10-25, so **0 newly first-visited numbered sections and 0 fully certified sections**. The main table of contents remains 25 chapters / 747 numbered sections. All user-excluded Demailly regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof-completion work remains **deferred-by-user** (not resolved). Only audit notes and the small check are proposed for the review branch.
