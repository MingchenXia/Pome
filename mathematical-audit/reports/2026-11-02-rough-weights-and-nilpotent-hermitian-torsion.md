# 2026-11-02 mathematical audit — a rough-weight obstruction and square-zero Hermitian torsion

**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Review branch before this report:** `7cc686f2d822a251fb5991663a8fcd5c8b794235`.
**Scope:** independent, selected proof-level checks of the *integrated reading edition* in §§13.7, 7.5 and 11.48. Neither entire section nor its full upstream proof chain is certified. This report does **not** inspect or extend the user-deferred Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale atlas, or positivity-loss programme.

## POME-NPP-ROUGH-WEIGHT-CIRCLE-001

**Severity/status:** low / **verified conditional deduction** (a sharpness example, **not** a false printed theorem).

**Exact integrated sources:**

- `docs/sections/non-pluripolar-products--capacity-convergence-and-loss-of-mass/index.html`, blob `d66813856cb813722806ab912afdfd4815d2da97`: Corollary **13.7.9**, source `data-tag=82DB3E57`, permanent tag `D73416504271`, physical lines **176–209**, especially the quasi-continuity hypothesis at 176, mass hypothesis at 180–184, and weighted continuity proof at 190–208. Theorem **13.7.5**, source `AB4EBE3B`, permanent `67C4F7EC316E`, lines 107–134. Example **13.7.6**, source `D5678E03`, permanent `ACAEA8D8BE87`, line 139.
- `docs/sections/bedford-taylor-products-and-local-capacity--quasi-continuity-and-convergence-in-capacity/index.html`, blob `464778b7ca6f1a456e36b24ecb4a0c93ab6948d3`: Definition **7.5.1**, source `CB3CE5F3`, permanent `A2CACA24130B`, line 11; weighted-continuity Theorem **7.5.8**, source `2B1AA42A`, permanent `42828E3BDDFA`, lines **172–185**.
- The normalization in these pages is \(\mathrm dd^{\mathrm c}=\frac{\mathrm i}{2\pi}\partial\bar\partial\); the Fubini–Study probability form is \(\omega_{\rm FS}=\mathrm dd^{\mathrm c}\log(1+|z|^2)\) on \(\mathbf P^1\).

**Question.** Can the limit weight's quasi-continuity in Corollary 13.7.9 be dropped while retaining bounded Borel weights, capacity convergence of those weights, uniform convergence of potentials, and *exact conservation of the total masses*? The answer is **no**.

**Fully explicit model and proof.** On \(X=\mathbf P^1\), in the affine coordinate \(z\), let
\[
 F_k(z)=\frac1k\log(1+|z|^{2k}),\quad
 F(z)=\log\max\{1,|z|^2\},\quad
 u_k=F_k-\log(1+|z|^2),\quad u=F-\log(1+|z|^2).
\]
The expressions \(u_k\) extend smoothly at infinity: for \(w=1/z\),
\[
 u_k(w)=k^{-1}\log(1+|w|^{2k})-\log(1+|w|^2).
\]
The function \(u\) is continuous on \(X\), including infinity, and
\[
0\le F_k-F\le (\log 2)/k
\]
globally (interpreting the difference via the displayed smooth potentials at infinity). Hence \(u_k\to u\) **uniformly**, in particular in local/extended capacity, with uniformly bounded potentials. The positive currents
\[
 T_k=\omega_{\rm FS}+\mathrm dd^{\mathrm c}u_k=\mathrm dd^{\mathrm c}F_k,\qquad
 T=\omega_{\rm FS}+\mathrm dd^{\mathrm c}u=\mathrm dd^{\mathrm c}F
\]
have locally bounded potentials and therefore coincide with their degree-one non-pluripolar products.

The explicit smooth probability densities are
\[
 T_k=\frac{k}{\pi}\frac{|z|^{2k-2}}{(1+|z|^{2k})^2}\,dx\,dy,
 \qquad T_k(\{|z|\le r\})=\frac{r^{2k}}{1+r^{2k}}.
\]
They are rotationally invariant, charge no circle, and converge weakly to the **normalized angular Haar probability** \(\mu_{S^1}\) on \(S^1=\{|z|=1\}\). Thus \(T=\mu_{S^1}\), and for every \(k\),
\[
 T_k(X)=T(X)=1,\qquad T_k(S^1)=0,\qquad T(S^1)=1.
\]
Set \(\chi_k=\chi=\mathbf1_{S^1}\). These are bounded nonnegative Borel weights, and \(\chi_k\to\chi\) in capacity *identically*. However,
\[
 \chi_k\langle T_k\rangle=0 \ \text{for every }k,\qquad
 \chi\langle T\rangle=T\ne0.
\]
Thus **even the weighted lower-semicontinuity inequality fails** if one drops only the quasi-continuity hypothesis on the limit weight, despite mass conservation and uniform potential convergence.

**Proof that the missing hypothesis really fails.** On \(D=B(0,2)\), put \(M=\log5\). The psh functions \(F_k/M-1\) and \(F/M-1\) lie in \([-1,0]\) on \(D\). Therefore, by the very definition of Bedford–Taylor relative capacity, for every Borel \(E\subset D\),
\[
 T_k(E)\le M\operatorname{Cap}_D(E),\qquad
 T(E)\le M\operatorname{Cap}_D(E).
\]
The capacity of \(S^1\) is positive: the admissible psh function
\[
 h(z)=\max\{-1,\,\log|z|^2/\log4-1\}\quad(z\in D)
\]
satisfies \(\mathrm dd^{\mathrm c}h=(\log4)^{-1}\mu_{S^1}\), so
\(\operatorname{Cap}_D(S^1)\ge1/\log4\).

Suppose \(\mathbf1_{S^1}\) were quasi-continuous. Choose the compact disk \(K=\overline{B(0,3/2)}\) and an open \(G\subset D\) with \(\operatorname{Cap}_D(G)<1/(4M)\) on whose complement in \(K\) the indicator is continuous. Then \(A=S^1\setminus G\) is compact and \(T(A)>3/4\). At every \(x\in A\), relative continuity and the value \(1\) give a small ordinary open ball \(U_x\subset\operatorname{Int}K\) satisfying \(U_x\setminus S^1\subset G\). By compactness, finitely many such balls cover \(A\); their union \(U\) is open, \(\mu_{S^1}(U)>3/4\), and \(U\setminus S^1\subset G\). Since \(T_k(S^1)=0\), for all \(k\),
\[
 T_k(U)=T_k(U\setminus S^1)\le T_k(G)<1/4.
\]
The open-set Portmanteau inequality for the already proved weak convergence \(T_k\rightharpoonup T\) gives
\(T(U)\le\liminf_kT_k(U)\le1/4\), a contradiction. Hence \(\chi\) **is not quasi-continuous**.

**Classification/consequence.** The printed Corollary 13.7.9 and Theorem 7.5.8 keep the correct quasi-continuity hypothesis and are **not shown false**. Unlike the printed Example 13.7.6, this example loses **no** total non-pluripolar mass: it isolates the *weight* obstruction. Proposed optional editorial insertion: present this circle/Haar example after Corollary 13.7.9, without changing any original hypotheses. Affected downstream uses: weighted non-pluripolar convergence and any argument that attempts to test a varying measure against arbitrary merely Borel indicator weights.

## POME-HERM-TORSION-NILPOTENT-GAP-001

**Severity/status:** low / **verified conditional deduction** (a strict improvement of a printed sufficient inequality, **not** a theorem repair or certification).

**Exact integrated sources:**

- `docs/sections/hermitian-torsion-and-the-bochner-identity/index.html`, blob `4656b430de6ec989ef121eca550afda0be407222`: Definition/equation **11.48.2**, line 17; \(T_\omega\) equation **11.48.13**, source `D2AA9D04`, permanent `DBCAF8FF0340`, lines **103–108**; Bochner identity Theorem **11.48.15**, source `72367915`, permanent `E96E372480D4`, lines 155–197; vanishing Corollary **11.48.20**, source `B37247AF`, permanent `222BB53B613A`, lines **205–222**; torsion bound Corollary **11.48.21**, source `7E456199`, permanent `5029210C26BC`, lines **227–244**, especially the estimate at 237–240.
- Existing §11.48 equation-alias and double-prime rendering defects already recorded elsewhere remain separate; no new editorial rendering defect is registered here.

**Exact algebraic improvement.** Write \(a=\partial\omega\wedge\) on the complete Hermitian exterior algebra (with the bundle \(E\) tensored by its identity). The wedge multiplier has **odd total degree three**. For every three-form \(\alpha\), \(\alpha\wedge\alpha=0\), so
\[
a^2=0,\qquad (a^*)^2=0.
\]
On the finite-dimensional Hermitian exterior fibre let \(P=a^*a\) and \(Q=aa^*\). These are nonnegative self-adjoint and satisfy
\[
PQ=a^*(a^2)a^*=0,\qquad QP=a((a^*)^2)a=0.
\]
Consequently their supports are orthogonal and
\[
\|aa^*+a^*a\|_{\mathrm{op}}
=\max\{\|aa^*\|_{\mathrm{op}},\|a^*a\|_{\mathrm{op}}\}
=\|a\|_{\mathrm{op}}^2.
\]
If \(\partial\bar\partial\omega=0\), the exact printed equation 11.48.13 gives
\[
T_\omega=-(aa^*+a^*a)\ \ge\
-\|a\|_{\mathrm{op}}^2 I.
\]
The printed proof's already justified monomial estimate is
\(\|a\|_{\mathrm{op}}\le\sqrt N\,|\partial\omega|_\omega\) with \(N=n\binom n2\).
Thus the coefficient **\(2N\) in its sufficient torsion estimate can be improved to \(N\)**:
\[
\boxed{T_\omega\ \ge\ -N|\partial\omega|_\omega^2I.}
\]
For any fixed bidegree and Hermitian holomorphic vector bundle \(E\), \([\mathrm i\Theta,\Lambda]\ge bI\) and
\[
 \boxed{b>N\sup_X|\partial\omega|_\omega^2}
\]
suffice for precisely the vanishing and minimum-norm smooth solvability conclusions of Corollaries 11.48.20–21, provided \(X\) is compact and \(\partial\bar\partial\omega=0\). An even more intrinsic sufficient condition is \(b>\sup_X\|\partial\omega\wedge\|_{\mathrm{op}}^2\). This uses **only** the already printed Bochner identity and finite-dimensional exterior algebra.

**Exact complex-surface constant.** In complex dimension \(n=2\), at an \(\omega\)-unitary point,
\[
 \partial\omega=\theta_1\wedge\theta_2\wedge
 (c_1\bar\theta_1+c_2\bar\theta_2).
\]
Exterior multiplication by this form can act nontrivially only from bidegrees \((0,0)\) to \((2,1)\) and \((0,1)\) to \((2,2)\); the norm of both blocks is
\(\sqrt{|c_1|^2+|c_2|^2}=|\partial\omega|_\omega\). Hence
\[
 \|a\|_{\mathrm{op}}=|\partial\omega|_\omega,\quad
 \boxed{T_\omega\ge-|\partial\omega|_\omega^2I\quad(n=2).}
\]
Equality of this **pointwise full-exterior** estimate is attained on scalar \(0\)-forms, since \(a^*1=0\) and \(\|a1\|^2=|\partial\omega|^2\). Accordingly \(b>\sup_X|\partial\omega|_\omega^2\) is a valid dimension-two sufficient hypothesis. The sharpness here concerns the operator estimate, **not** a necessary-and-sufficient geometric cohomology criterion in a fixed bidegree.

**Classification/consequence.** The printed Corollary 11.48.21 is **correct but non-optimal** in its stated sufficient constant. A proposed optional, separately reviewable insertion would mention the square-zero argument and stronger \(N\) (respectively \(1\) for \(n=2\)) threshold, leaving the existing statement and permanent tags unchanged. Affected dependents are the stated Hermitian Bochner/cohomology vanishing and \(\bar\partial\)-solvability applications; no Demailly/weighted-L² proof-completion is attempted or needed.

## Coverage, provenance, and boundaries

These are **two new selective proof/model checks** in **previously partly sampled** §§13.7 and 11.48, plus a supporting targeted crosscheck of §7.5.1/.8. No section is upgraded to whole-proof-chain certification. The previously reported §13.7 directed-net extension, §11.48 equation defects, and all other ledger items retain their existing status. There are **25 chapters / 747 numbered sections / zero fully mathematically certified sections** in the current main ToC. This run made no production main, source repository, registry/canonicalization, permanent tag, CI, build, formalization, or website changes. No software tests or build were run; the calculations above are direct mathematical checks and an explicit probability/capacity computation.

**Suggested subsequent rotation (not covered here):** take a genuinely unreviewed nonexcluded passage in a different chapter and verify its exact integrated proof and hypotheses; in particular avoid overcounting repeated work in §§13.7 and 11.48.
