# 2026-10-30 — Entire-function rigidity of a Stein open union and sharp abstract Hölder interpolation

## Scope and immutable source

Reviewed production main: **b6933b772f41b45918f7e25ed1afbbb1fd892272**. This report documents only audit proposals, not a change to the integrated reading edition. All source labels below refer to the integrated edition at that commit. Two new stable findings are **low / verified conditional deduction**; neither asserts that a printed theorem is false. No complete mathematical section, full dependency chain, or project-wide correctness is certified.

The first new selected proof inspection of the previously inventory-only §§15.5 and 15.6 is **restricted to the elementary stability-to-regularity algebra after taking the stated smoothing and stability estimates as conditional inputs**. In particular, nothing here reads, extends, repairs, replays or certifies the user's excluded Demailly approximation/regularization and its dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes. The quoted smoothing lemmas remain **deferred-by-user**, not resolved.

## POME-STEIN-UNION-ENTIRE-ALGEBRA-001

**Severity and status:** low; **verified conditional deduction** (in fact a direct proof from the displayed algebraic model); not a false printed theorem, proof gap or new canonical duplicate.

**Stable location:** [§9.27 integrated reading page](../../docs/sections/separation-strict-exhaustions-and-coverings--an-increasing-union-of-affine-stein-surfaces/index.html), main blob **26b2e856fc24b04616b0840caec5c688cc045ffa**, section tag **E65337AF838D**, Example 9.27.1 source label **demailly-complex-geometry:BBFF78A8** (HTML environment id demailly-complex-geometry-BBFF78A8), permanent tag **F00C66A8D202**, physical lines **8–12** for the statement and embeddings, **18–30** for the open-union construction, and **32–46** for the coordinate projection and its missing limit point. The earlier finding **POME-STEIN-UNION-NO-PSH-EXHAUST-001** proves a different, maximum-principle obstruction; it remains unchanged.

### Precise stronger conclusion

Set \(a_j=1/j\), \(p_\nu(z)=\prod_{j=1}^\nu(z-a_j)\), and
\[
X_\nu=\{(z,w,t)\in\mathbb C^3:wt=p_\nu(z)\},
\quad
j_\nu(z,w,t)=(z,w,t(z-a_{\nu+1})).
\]
Write \(X=\varinjlim X_\nu\), with its specified open-complex-manifold union, and \(\pi=(z,w):X\to\mathbb C^2\). Then
\[
\boxed{\pi^*:\mathcal O(\mathbb C^2)\ \xrightarrow{\ \sim\ }\ \mathcal O(X)}
\]
is an isomorphism of unital complex algebras. For **every** compact \(K\subset X\),
\[
\boxed{\widehat K_X^{\mathcal O(X)}
=\pi^{-1}\!\left(\widehat{\pi(K)}_{\mathrm{poly},\,\mathbb C^2}\right).}
\]
For each \(j\), if \(x_j\in\pi^{-1}(a_j,0)\), the hull of the **single point** \(K_j=\{x_j\}\) is exactly
\[
\widehat{K_j}_X=\pi^{-1}(a_j,0)\simeq\mathbb C.
\]
Consequently global holomorphic functions fail to distinguish even two points on the same zero fiber, and the holomorphic hull of a singleton is noncompact. This is substantially stronger and geometrically different from the noncompact hull of the special circle used in the printed example.

### Proof of the algebra isomorphism

On \(w\neq0\), \(\pi\) is the biholomorphism
\[
\pi^{-1}(\mathbb C\times\mathbb C^*)\simeq\mathbb C\times\mathbb C^*
\]
explicit in the original proof. Take \(f\in\mathcal O(X)\) and denote its restriction in these coordinates by \(F\in\mathcal O(\mathbb C\times\mathbb C^*)\). Fix \(r>0\). For each integer \(m\in\mathbb Z\), its Laurent coefficient
\[
c_m(z)=\frac1{2\pi i}\int_{|w|=r}F(z,w)\,w^{-m-1}\,dw
\]
is entire in \(z\), by holomorphic differentiation under a fixed contour. In stage \(X_j\), the curve
\[
\ell_j:\mathbb C\longrightarrow X_j,\qquad w\longmapsto(a_j,w,0)
\]
is holomorphic, because \(p_j(a_j)=0\). On \(w\neq0\), this curve is the unique point above \((a_j,w)\). Hence \(F(a_j,w)=f(\ell_j(w))\) extends **entirely in \(w\)**. Every negative Laurent coefficient \(c_m(a_j)\), \(m<0\), therefore vanishes.

Since \(a_j\to0\) inside the complex \(z\)-plane, the one-variable identity theorem gives \(c_m\equiv0\) on \(\mathbb C\) for every \(m<0\). Thus the Laurent expansion has no negative terms. For each compact set in \(z\) and \(0\leq |w|\leq r'<r\), the positive-power series \(\sum_{m\geq0}c_m(z)w^m\) converges normally by the Cauchy bounds on the fixed circle \(|w|=r\). It is jointly holomorphic across \(w=0\). As \(r>0\) was arbitrary and these continuations agree with \(F\) on \(w\neq0\), they glue to a unique \(\widetilde F\in\mathcal O(\mathbb C^2)\).

The holomorphic functions \(f\) and \(\widetilde F\circ\pi\) agree on the dense open set \(w\neq0\); they agree everywhere by continuity (or the identity theorem). Injectivity of \(\pi^*\) follows because \(\pi(X)\) contains \(\mathbb C\times\mathbb C^*\). Thus \(\pi^*\) is an isomorphism.

### Hulls and precise fibers

By that isomorphism, the defining inequalities of the holomorphic hull of \(K\) are **exactly** the inequalities for all entire \(G\) on \(\mathbb C^2\) evaluated on \(\pi(K)\). Entire Taylor polynomials converge uniformly on compact subsets of \(\mathbb C^2\), so testing all entire functions or all polynomials produces the same hull; this proves the displayed formula.

At \(z=a_j,w=0\), every stage \(X_\nu\), \(\nu\geq j\), has all \(t\in\mathbb C\), and the embedding to the next stage multiplies \(t\) by \(a_j-a_{\nu+1}\neq0\). Hence the direct-limit fiber is the entire affine line, and already the stage-\(j\) fiber surjects onto it. The polynomial hull of the singleton \(\{(a_j,0)\}\) in \(\mathbb C^2\) is itself, since the two coordinate functions separate any other point. Its inverse image is therefore precisely the affine line. This independently proves failure of holomorphic convexity and of global point separation.

### Sharpness of the accumulation mechanism

The finite accumulation of \(a_j\) is indispensable to the preceding **algebra** argument, not merely an incidental convenience. Replace \(a_j=1/j\) by \(a_j=j\), retaining the same equations and open embeddings. For each \(\nu\) the quotient \(h_\nu(z)=\sin(\pi z)/p_\nu(z)\) is entire: the zeros \(1,\ldots,\nu\) are simple. Define on \(X_\nu\)
\[
f_\nu(z,w,t)=t\,h_\nu(z).
\]
Since \(h_{\nu+1}(z)(z-(\nu+1))=h_\nu(z)\), the \(f_\nu\) are compatible with \(j_\nu\) and define \(f\in\mathcal O(\varinjlim X_\nu)\). On \(w\neq0\),
\[
f(z,w)=\frac{\sin(\pi z)}w,
\]
which cannot be the restriction of an entire function on \(\mathbb C^2\) (fix any noninteger \(z\)). In particular, on a zero fiber \(z=j\) the function is a nonzero scalar multiple of \(t\), so these fibers **are** separated by a global holomorphic function. No assertion about convexity of this modified union is needed.

**Suggested correction/addition, not applied:** add an optional corollary of Example 9.27.1 identifying \(\mathcal O(X)\) and its singleton hulls, and explaining that the accumulating zero fibers cause the loss of holomorphic functions. Preserve the original example, its provenance and permanent tags.

**Affected discussion:** §9.26 local/global separation and convexity (Theorem 9.26.1, source demailly-complex-geometry:57C45FF9, tag C1041DBBD4EC; main blob c04701d0358d43a3a3f1aed61e7cdd2a48305417, physical lines 7–14, 19–32), and the **different** Hartogs-bridge model §9.30 (Proposition 9.30.1, source demailly-complex-geometry:61281B36, tag 774E0C4C33DB; main blob c4037b237429e2c1269bd7beebded6644dc206c9, physical lines 10–15 and 45–61). The previously logged POME-HARTOGS-BRIDGE-EXACT-HULL-001 concerns §9.30, **not** the Stein union here.

## POME-HOLDER-ABSTRACT-SMOOTHING-OPT-001

**Severity/status:** low / **verified conditional deduction**, sharpening the interpretation of a proof step; not a counterexample to either printed Hölder theorem and **not** a certification of the excluded regularization inputs.

**First direct selected integrated anchors:** [§15.5 reading edition](../../docs/sections/equations-with-prescribed-singularities--holder-continuity-from-bounded-stability/index.html), main blob **6a5a19947ef5767f9828fa2230e6f251db21d743**, section tag **BDF9BACE965B**: Theorem 15.5.1 source **non-kahler-pluripotential-theory:CA85850B**, tag **CA29182325B0**, statement physical lines **11–19**, conditional stability-to-smoothing passage **24–88**; Theorem 15.5.4 source **non-kahler-pluripotential-theory:1B17D9EF**, tag **56C5E320D330**, lines **98–106**, conditional arithmetic **111–166**. [§15.6 reading edition](../../docs/sections/equations-with-prescribed-singularities--local-continuity-in-a-semipositive-big-background/index.html), main blob **222db429ecdbb24a04be5a0fc5039299e216b937**, section tag **FF4EC5CCEA0B**: Theorem 15.6.1 source **non-kahler-pluripotential-theory:E9203C4F**, tag **02C5F4AFC7FF**, lines **10–18**, post-input proof **23–76**, modulus caveat **81**.

### Abstract implication and optimality, independent of regularization

Let \(0<q<1\), and let \(v\) be bounded on a Euclidean interval with smooth approximants \(v_s\) for \(0<s<s_0\), obeying for one fixed \(C\)
\[
\|v_s-v\|_\infty\leq Cs^q,\qquad
\|\nabla v_s\|_\infty\leq C/s.
\]
For \(x,y\) close enough that their joining segment stays in the interval,
\[
|v(x)-v(y)|\leq2Cs^q+C|x-y|/s.
\]
Choosing \(s=|x-y|^{1/(1+q)}\) proves \(v\in C^{0,q/(1+q)}_{\mathrm{loc}}\). This terminal exponent **cannot be improved using only these two estimates**.

To prove sharpness fix \(\beta=q/(1+q)\), a smooth compactly supported cutoff \(\chi\) equal to one near zero, and \(v(x)=\chi(x)|x|^\beta\). It is bounded and globally \(\beta\)-Hölder, but fails to be \(\beta'\)-Hölder at zero for every \(\beta'>\beta\). Take a nonnegative smooth compactly supported probability mollifier \(\rho\), set \(h=s^{1+q}\), and put \(v_s=\rho_h*v\). The Hölder estimate gives
\[
\|v_s-v\|_\infty\leq C h^\beta=Cs^q.
\]
Using \(\int\rho_h'=0\) and changing variables,
\[
|v_s'(x)|=\left|\int\rho_h'(y)[v(x-y)-v(x)]\,dy\right|
\leq C h^{\beta-1}=C s^{-1},
\]
because \((1+q)\beta=q\) and \((1+q)(\beta-1)=-1\).
Thus both quantitative input estimates hold **exactly at the claimed order**, yet no greater Hölder exponent holds for \(v\).

This is an **abstract approximation boundary**, not a claim that the sharp exponent for the actual Monge–Ampère solution class equals this value. Stronger structural information about the special averages, the equation or the density could give more regularity.

### The printed exponent algebra, conditional on its named inputs

In Theorem 15.5.1 let \(0<\eta<(p-1)/(np+p-1)\), and set \(q=2\eta\). The printed proof obtains the two conditional bounds above with \(s=a\delta\), after using the stability estimate and the transform. The terminal exponent is
\[
\frac{2\eta}{1+2\eta},
\quad\text{whose limiting supremum is}\quad
\frac{2(p-1)}{np+3(p-1)}.
\]
The numerical implication and the strict endpoint convention are consistent with lines 28–88. In Theorem 15.5.4 the declared intermediate exponents are
\[
\eta=\frac{2\alpha}{\alpha+2n},\quad
\gamma=\frac1{6n+1},\quad q=\frac{\eta\gamma}{2}
=\frac{\alpha}{(\alpha+2n)(6n+1)}.
\]
Hence \(q/(1+q)=\alpha/((\alpha+2n)(6n+1)+\alpha)\), **exactly** the stated exponent. The curvature rescaling identity in line 134 is also algebraically consistent: if \(\omega+dd^cF\geq-\varepsilon\omega\), then
\[
\omega+dd^c((1-\varepsilon)F)
\geq[1-(1-\varepsilon)(1+\varepsilon)]\omega
=\varepsilon^2\omega.
\]
These are checks of the printed **deductions from their premises**, not proofs of the regularization or the weighted estimates.

For Theorem 15.6.1, assume just the post-input local estimates on \(\{\rho\geq-M\}\):
\[
\|R_{a_M\delta}u-u\|_\infty
\leq C_M\bigl(\delta^\alpha+\epsilon(\delta)\bigr),
\quad \|\nabla R_{a_M\delta}u\|_\infty\leq C_M/\delta,
\quad \epsilon(\delta)\to0.
\]
On each compact subset of the locus where \(\rho\) is locally bounded, a slightly larger compact coordinate neighborhood permits the segment argument, giving the **conditional** modulus
\[
\omega_{u,K}(d)\leq
C_K\inf_{0<\delta<\delta_0}
\left(\delta^\alpha+\epsilon(\delta)+\frac d\delta\right).
\]
The right side tends to zero: first choose \(\delta\) with the first two terms small, then choose \(d\ll\delta\). Without a power bound on \(\epsilon\), these inequalities alone give no fixed power modulus. This agrees with the last paragraph of §15.6 and does **not** solve the missing power-rate question.

**Proposed optional addition:** a short abstract interpolation remark after §15.5, making explicit the optimality of the final *two-estimate* step only. No alteration of Theorems 15.5.1, 15.5.4 or 15.6.1 or their exponents is justified by this audit.

**Exact unresolved/deferred boundary:** the Chern-connection averaging, transforms, weighted estimates and all regularization-related Lemmas 5.42.1/2/4/8/10 are expressly **deferred-by-user**. The stability estimates quoted from §§14.19, 15.4, capacity domination and other internal analytic inputs have not been transitively reverified. Neither theorems nor their proof chains are thereby certified. No unproved premise is relabeled a confirmed proof gap merely because it was not examined.

## Actual coverage, exclusions and execution record

- **New selected nonexcluded proof-level coverage:** §§15.5.1, 15.5.4, 15.6.1 **only after their smoothing and stability premises**: algebra of curvature rescaling, exponent arithmetic, the elementary two-estimate interpolation, and the conditional modulus on compact subsets. This is the first such direct record in previously inventory-only matrix rows §§15.5–15.6.
- **Incremental model-level coverage of a previously reviewed section:** §9.27 Example 9.27.1: entire global holomorphic-function algebra, exact hulls of arbitrary compact sets and singleton fibers, and the nonaccumulating-integers sharpness contrast. Prior §9.27 non-psh-exhaustion result and §9.30 bridge hull result were deliberately **not** duplicated. The §9.26 and §9.30 statements were reread solely for comparison.
- **Not checked:** the excluded programme, full proofs of any cited smoothing, \(L^2\), Bergman or extension theorem, external analytic inputs, full entire sections or chapters, full repository tests/build, browser rendering, GitHub Actions CI, publication and formal proof verification.
- The actual current section inventory remains **25 chapters, 747 distinct numbered table-of-contents sections, zero entirely certified mathematical sections**. Preserve every earlier error, gap, candidate, external dependency and deferred-by-user status. This report proposes no changes to production main, original source material, canonicalization data, equations or permanent tags.
