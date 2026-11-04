# Unique boundary measure, vague recovery and atomic boundary mass in half-space Poisson representation (2026-11-05)

**Stable finding ID:** \`POME-HARM-HALFSPACE-VAGUE-BOUNDARY-UNIQUENESS-001\`.  
**Severity/status:** low / **verified conditional deduction**. The printed theorems are **not** false; this is an additional uniqueness and boundary-recovery theorem, not a repair or a complete dependency certification.  
**Production main reviewed:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Integrated file:** \`docs/sections/kelvin-transforms-and-half-space-potentials/index.html\`, main Git blob \`f2615a5393af724c3996978212162f94911ff9d9\`.  
**Current ToC:** Chapter 3, §3.2 “Kelvin transforms and half-space potentials”, section tag \`9728BD930155\`.  
**Exact source labels / permanent tags / physical HTML anchors:** Theorem 3.2.6 \`classical-potential-theory:1C8A330A\` / \`6BC86EEF03A9\`, lines **64–75**; Eq. 3.2.7 \`:C0A46F1A\` / \`F3ED29BBAD39\`, lines **66–68**; weighted measure Eq. 3.2.8 \`:358F89A3\` / \`8F7C774A9D89\`, lines **70–73**. Its proof of existence and kernel transformation occupies lines **80–131**. Theorem 3.2.12 \`:BB6DAC3F\` / \`9ADD2DF19642\`, lines **140–145**; Poisson normalization Eq. 3.2.13 \`:E7E82020\` / \`AB2849CD8791\`, lines **151–165**; boundary-tail estimate lines **168–180**. Independently inspected the Kelvin cancellation at Theorem 3.2.2, \`:B1AA5815\` / \`97BA27062B9F\`, lines **16–49**.

## 1. Precise new statement

Let \`d>=2\`, \`H=R^{d-1} x (0,infinity)\`, and \`kappa_d=2/s_{d-1}\`. Assume the **exact** hypotheses of the integrated Theorem 3.2.6: \`h\` is nonnegative harmonic on \`H\`, and its representation is
\[
h(x,t)=ct+\int_{\mathbb R^{d-1}}P_t(x-z)\,d\nu(z),\qquad
P_t(v)=\kappa_d\,\frac{t}{(|v|^2+t^2)^{d/2}},
\]
where \`c>=0\`, \`nu\` is a positive Radon measure and
\[
I(\nu):=\int_{\mathbb R^{d-1}}(1+|z|^2)^{-d/2}\,d\nu(z)<\infty.
\tag{A}
\]

**New conclusions (unique boundary data and sharp point-mass readout):**

1. **Vague boundary recovery.** For every \(\varphi\in C_c(\mathbb R^{d-1})\),
   \[
     \boxed{\lim_{t\downarrow0}\int_{\mathbb R^{d-1}}
                      \varphi(x)h(x,t)\,dx=\int\varphi\,d\nu.}
     \tag{B}
   \]
   Here the limit is over **all real** \`t>0\`, not just a sequence. The measures \`h(x,t)dx\` are only locally finite, not asserted to have uniformly bounded *global* mass.
2. **Atom extraction.** For every \(z_0\in\mathbb R^{d-1}\),
   \[
      \boxed{\lim_{t\downarrow0}t^{d-1}h(z_0,t)
               =\frac2{s_{d-1}}\nu(\{z_0\}).}
      \tag{C}
   \]
   Hence atomic weights are pointwise recoverable even if \(\nu\) has infinite total mass.
3. **Uniqueness.** The representing pair \((c,\nu)\) is unique in the printed class. Equation (B) determines \(\nu\); subtracting its Poisson integral at any interior point determines \`c\`. In fact the *intrinsic vertical-slope formula* \(c=\lim_{T\to\infty}h(x,T)/T\) was **already established** in \`POME-HARM-HALFSPACE-CONE-GROWTH-SHARP-001\` (2026-11-02), and is deliberately **not** counted as a new finding here.

The original Theorem 3.2.6 asserts *existence*, not uniqueness or (B)–(C). Both the theorem and Theorem 3.2.12 remain correct.

## 2. Complete proof of vague boundary recovery

The integrated Eq. 3.2.13 proves \(\int_{\mathbb R^{d-1}}P_t(v)\,dv=1\) for every \`t>0\`. The explicit kernel also gives, for any fixed \(\delta>0\),
\[
 \int_{|v|\ge\delta}P_t(v)\,dv
 \le C_d\,t/\delta,\quad 0<t\le1.
 \tag{D}
\]
For a bounded uniformly continuous compactly supported \(\varphi\), (D) implies
\[
 \int\varphi(x)P_t(x-z)\,dx\longrightarrow\varphi(z)
 \quad\text{for every }z
 \tag{E}
\]
(the convergence is in fact uniform in \`z\`). We must **not** apply dominated convergence against a potentially infinite \(\nu\) using only the trivial bound \(\|\varphi\|_\infty\).

Choose \`R>=1\` such that \(\mathrm{supp}\varphi\subset B_R(0)\). For \(|z|\ge 2R+2\), \(0<t\le1\), and \(|x|\le R\) one has \(|x-z|\ge|z|/2\), so
\[
\left|\int\varphi(x)P_t(x-z)\,dx\right|
\le C_{d,\varphi,R}\,t\,|z|^{-d}
\le C'_{\varphi,R}(1+|z|^2)^{-d/2}.
\tag{F}
\]
For \(|z|<2R+2\), kernel positivity and normalization give the bound \(\|\varphi\|_\infty\), which is also bounded by a constant times \((1+|z|^2)^{-d/2}\) on this fixed ball. Consequently, for **all** \`z\` and \`0<t<=1\`,
\[
 \left|\int\varphi(x)P_t(x-z)\,dx\right|
 \le C_{\varphi}(1+|z|^2)^{-d/2}.
\tag{G}
\]
This is an integrable majorant by (A). Equation (G) also justifies absolute Fubini for the compactly supported test. Thus, by (E) and dominated convergence,
\[
\int\varphi(x)(P_t*\nu)(x)\,dx
=\int\left(\int\varphi(x)P_t(x-z)\,dx\right)d\nu(z)
\to\int\varphi\,d\nu.
\]
The \`ct\` summand contributes \(ct\int\varphi\,dx\to0\). This proves (B) for arbitrary \(\varphi\in C_c\), by the same domination, without treating infinite \(\nu\) as a finite measure.

## 3. Complete proof of the atom formula

Fix \(z_0\) and multiply the representation by \(t^{d-1}\):
\[
 t^{d-1}h(z_0,t)
 =c\,t^d+\kappa_d\int
 \frac{t^d}{(|z-z_0|^2+t^2)^{d/2}}\,d\nu(z).
 \tag{H}
\]
On \(|z-z_0|\le1\), the integrand in (H) is bounded by \`1\` and tends pointwise to \(\mathbf1_{\{z_0\}}(z)\). The measure of this fixed ball is finite (Radon), so dominated convergence gives its contribution \(\nu(\{z_0\})\).

On \(|z-z_0|>1\) and \`t<=1\`, its integrand is bounded by \(t^d|z-z_0|^{-d}\). The integral of \(|z-z_0|^{-d}\) over this outer set is finite: it is bounded on the bounded part (where \(\nu\) is finite), and at infinity it is comparable to the integrable weight from (A). This contribution is therefore \`O(t^d)\to0\`. Also \(ct^d\to0\). Equation (C) follows. In particular, it is **not** legitimate to apply a global \(\nu\)-dominated convergence argument using the constant bound \`1\` if \(\nu(\mathbb R^{d-1})=\infty\).

## 4. Independent inspection of the integrated proof and a normalization model

**Kelvin computation, not a separate new finding.** In Theorem 3.2.2 translate the inversion center to zero, put \(r=|x|\), \(Q=I-2xx^{\mathsf T}/r^2\), \(T(x)=\rho^2x/r^2\), \(w=\rho^{d-2}r^{2-d}\). Direct differentiation gives \(DT=\rho^2r^{-2}Q\), \(\Delta T_j=-2(d-2)\rho^2x_j/r^4\), \(\Delta w=0\), and \(Qx=-x\). The cross-gradient term from \(\Delta(wu\circ T)\) cancels the \(\Delta T\)-term, leaving \((\rho/r)^{d+2}(\Delta u)\circ T\). This also works at \`d=2\` since both cross terms then vanish. The signs/exponents in Eq. 3.2.3 (lines 17–49) pass this independent selected algebraic check; this does **not** certify every preceding harmonic-analysis dependency.

**Infinite-mass normalization check.** Choose \(\nu=dz\), Lebesgue measure on \(\mathbb R^{d-1}\). Then (A) is finite, despite \(\nu(\mathbb R^{d-1})=\infty\), and Eq. 3.2.13 gives \(P_t*\nu\equiv1\), \`c=0\`. Formula (B) recovers \`dz\` from \(h\equiv1\); formula (C) correctly gives zero at every point. This confirms the need to keep the weighted Radon class rather than silently imposing finite total boundary mass.

## 5. Status, proposed correction and coverage limits

- **Status:** \`POME-HARM-HALFSPACE-VAGUE-BOUNDARY-UNIQUENESS-001\` — low / **verified conditional deduction**, no false printed theorem, no proof gap established, no external dependency introduced. This proof uses the integrated half-space representation (Theorem 3.2.6) and the elementary Poisson normalization/tail bound in §3.2.12 as internal inputs; its general existence proof and ball-measure selection are **not** transitively certified.
- **Proposed patch, not applied:** append a corollary **after** Theorem 3.2.6 giving (B), (C) and uniqueness. Keep the source attribution, variants, equation identifiers and permanent tags intact. Do not redefine boundary data by pointwise values of a density where \(\nu\) may be singular.
- **Affected downstream arguments to check:** uniqueness of half-space harmonic boundary traces, boundary atoms or singular measures, identification of the Martin point at infinity versus finite boundary traces, and any claim that convergence in (B) holds in *global total variation* or with unbounded test functions. No particular downstream theorem is alleged false without reading its actual proof.
- **Actual mathematical coverage:** new selected **§3.2.2 Kelvin algebraic identity** and **§3.2.6 Poisson boundary-measure uniqueness and atomic recovery**, crosscheck of **§3.2.12 normalization/tail estimate**; no complete §3.2 or chapter-3 certification. §3.2.6 had previously been sampled for *large-height conical growth*, a mathematically distinct issue. No old heat-kernel or separate-subharmonic findings were repeated.
- **Exclusions respected:** no Demailly approximation/regularization; no dedicated Bergman, weighted \`L^2\`, Ohsawa–Takegoshi, multiscale-atlas or positivity-loss programme. Older records in this area stay **deferred-by-user**, not certified or resolved. No build, tests, CI, formal verification, main/source/body/registry/tag mutation or publication.
