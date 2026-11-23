# 2026-11-24 — Gauduchon volume-test quotient gap, curvature pairs and convex-geodesic rotation

## Baseline and exact scope

- **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; no source-body, tag or canonicalization write.
- **Audit branch:** review/mathematical-audit; this is a documentation-only mathematical review.
- **New finding:** POME-GAUDUCHON-VOLUME-TEST-QUOTIENT-GAP-001 — **low / verified conditional deduction**, not a false printed theorem, not a proof repair. One new derived estimate with a three-regime sharp asymptotic.
- **Direct present-main reading:** all mathematical material in §12.14 (physical HTML lines 9–274, blob 4e892ab379abdfa3b6520671db344e94bbc7a51a), §12.17 (lines 14–263, blob 48b41a642dec5de37f73d9052ae13202ddb6d202), §9.17 (lines 20–174, blob 11789d8f51f81ec69de4fbb206c1186c73540b0e), and §9.20 (lines 16–218, blob 406faf6cf759c6aa6ed9b0cee3792ba6b5a85f65). Reading a whole current section is not certification of all its transitive dependencies or its historical first visit.
- **Partial nonexcluded review:** §12.15 (blob 440964738faf623f2e0942bbc7fd21d5f2a3ed69): density comparison (§12.15.1), smooth-mass criterion (§12.15.2), fixed-Gauduchon Hölder estimate and minimax (§12.15.4), critical-point criterion (§12.15.6) and boundary limit (lines 10–141), **except** the §12.15.4 step at physical line 81 invoking Theorem 5.32.1 and the excluded regularization programme. That dependency stays **deferred-by-user**, without a claimed verification or replacement.
- The Demailly regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion programme was not audited. §24.10 kernel questions were not registered as audited coverage.

## New finding: POME-GAUDUCHON-VOLUME-TEST-QUOTIENT-GAP-001

**Status:** low / verified conditional deduction; original §12.14.10 remains valid. **Source:** docs/sections/a-gauduchon-variational-volume--positive-volume-without-bigness/index.html, permanent §12.14 tag E4AB7B03C20D; Theorem 12.14.6 tag ECAB6BFB33FD, equation (12.14.1) tag 71973446DB97 at lines 22–26; Proposition 12.14.10 tag 0E9506DB4E70 and equation (12.14.11) at lines 169–193; proof and radial integrals at lines 198–235. **Affected dependents:** interpretation of the normalized volume-minimizing test family in §12.14.9–13 and comparison with the bigness threshold (§24.3.2); no theorem replacement is needed.

Let m≥2, n=m+1, t=(m−1)/m, B=P^m, and let ω and w be the unit-volume Fubini–Study forms on B and P¹ as printed in §12.14. Set a=x/t, θ=ω+aw, μ=ω^m∧w, and

\[
H(\varepsilon)=\int_B(a+\varepsilon)^{-1}\omega^m
=m\int_0^1\frac{x^{m-1}}{x/t+\varepsilon}\,dx,\quad
I(\varepsilon)=\int_B(a+\varepsilon)^{-2}\omega^m,\quad
J(\varepsilon)=\int_B(a+\varepsilon)^{-3}\omega^m.
\]

For the smooth balanced Gauduchon test g_ε from Proposition 12.14.10, let

\[
Q_\theta(g_\varepsilon)=
\frac{\int_X\theta\wedge g_\varepsilon^{n-1}}
{D_\mu(g_\varepsilon)},\qquad
F(\varepsilon)=H(\varepsilon)^{-1/n}.
\]

**Claim 1 (exact identity and strict monotonicity).** For all ε>0,

\[
\boxed{Q_\theta(g_\varepsilon)
=n^{1/n}\big(F(\varepsilon)-\varepsilon F'(\varepsilon)\big),\qquad
\frac{d}{d\varepsilon}Q_\theta(g_\varepsilon)>0.}
\]

In particular Q_θ(g_ε)>λ_μ(θ)=n^{1/n}, while Q_θ(g_ε) decreases to this optimum as ε↓0.

**Claim 2 (three sharp leading orders).** With ε↓0 and positive constants as given,

\[
\boxed{
\frac{Q_\theta(g_\varepsilon)}{n^{1/n}}-1
\sim
\begin{cases}
\varepsilon/6,&m=2\quad(n=3),\\
(2/9)\varepsilon^2\log(1/\varepsilon),&m=3\quad(n=4),\\
C_m\varepsilon^2,&m\ge4\quad(n\ge5),
\end{cases}}
\]

where

\[
I_0=\frac{(m-1)^2}{m(m-2)},\qquad
J_0=\frac{(m-1)^3}{m^2(m-3)},\qquad
C_m=\frac{J_0}{m+1}-\frac{m+2}{2(m+1)^2}I_0^2>0
\quad (m\ge4).
\]

These are asymptotics for **this specific prescribed family** and fixed μ, not universal rates for all Gauduchon minimizing sequences.

### Proof

The numerator and determinant denominator printed in equation (12.14.11) are

\[
\int_X\theta\wedge g_\varepsilon^{m}
=\frac{n-\varepsilon I/H}{M_\varepsilon},\qquad
D_\mu(g_\varepsilon)
=\frac{(n/H)^{m/n}H}{M_\varepsilon}.
\]

Cancel M_ε. Since H'=-I and F'=I H^{-1/n-1}/n, the quotient simplifies exactly to n^{1/n}(F−εF'). Differentiating H again gives H''=2J. Thus

\[
F''=\frac1n H^{-1/n-2}
\Big((1+1/n)I^2-2HJ\Big).
\]

Cauchy–Schwarz for the probability measure ω^m gives I²≤HJ. Since n>1 and H,J>0, the bracket is strictly negative and F''<0. Consequently

\[
Q_\theta'(g_\varepsilon)=-n^{1/n}\varepsilon F''(\varepsilon)>0,\qquad
\frac{Q_\theta(g_\varepsilon)}{n^{1/n}}-1
=-\int_0^\varepsilon sF''(s)\,ds.
\]

Here H(0)=1 by the radial identity (12.14.5), and εF'(ε)→0; for m=2, F'=O(log(1/ε)), while for m≥3 it is bounded. The integral identity follows by first integrating from δ>0 and then letting δ↓0.

For m=2, t=1/2 and radial integration gives J(ε)∼1/(4ε). Because H→1 and I=O(log(1/ε)), we obtain F''(ε)∼−1/(6ε). Integrating −sF'' produces ε/6.

For m=3, t=2/3 and J(ε)∼3t³log(1/ε)=(8/9)log(1/ε). Since I(ε) stays bounded, n=4 and F''(ε)∼−(4/9)log(1/ε). Since \(\int_0^\varepsilon s\log(1/s)\,ds\sim\tfrac12\varepsilon^2\log(1/\varepsilon)\), the quotient gap is (2/9)ε²log(1/ε).

For m≥4, dominated convergence gives I(0)=m t²/(m−2)=I₀ and J(0)=m t³/(m−3)=J₀. The formula for F''(0) yields the displayed C_m and a quadratic remainder. Its positivity follows either from F''(0)<0 or directly from I₀²≤H(0)J₀=J₀.

No smooth approximation theorem, Bergman construction, L² estimate or external positivity-loss lemma enters this proof. The claim is conditional only on the specific smooth test family and normalization already supplied in §12.14; it does not certify the full upstream construction.

## Other nonexcluded mathematical checks

1. **§12.14:** checked the radial probability normalization H(0)=1 (lines 45–53), the distribution-function inequalities x^m≤q_ε^m≤x^{m−1} (lines 77–95), the nonbigness obstruction using closed horizontal test forms (lines 121–129), the balanced test T_ε=γ_ε^m and Stokes/AGM quotient (lines 131–157), both normalized-current limits (lines 198–274). The printed statements were not contradicted. In particular the n=3 logarithmic divergence of I_ε and n≥4 finite I_0 must not be conflated with the new quotient-gap asymptotics.
2. **§12.17:** checked the bounded cubic mass expansion (Lemma 12.17.2, tag 3BBBC535BFA2; lines 18–53); invariant determinant density under h↔g (Lemma 12.17.4, tag 73E13B1F9B7A; lines 59–77); split curvature dd^c e=−Q/(2π) and dd^c(g²)=0 (Theorem 12.17.7, tag 7EC7E0C62DF9; lines 83–134); the primitive-pair opposite sign (Proposition 12.17.9, tag A60EEF389BCA); the elliptic-fiber area factors 4πlog(1/ρ) and 8π² Im τ (Propositions 12.17.11 and 12.17.14). No new printed error confirmed; local uses of bounded BT products and endpoint current determinants remain upstream dependencies.
3. **§9.17:** checked Schwarz–Pick sign/distance bounds, the construction of one disc through two points by a thin complex rectangle, Green-versus-Carathéodory/Kobayashi inequalities, and the bounded-domain separation step. Source propositions 9.17.1–5, tags 10AFB6AB7732, 6BCDD3D7DD27, 75C57846C83D, F0CC92394671 and 32C365095F79; physical lines 20–174. The planar nonthin-segment input in 9.17.1 has not been independently transitively verified.
4. **§9.20:** checked the Hardy factorization/boundary-value route, supporting covector and interpolation extremality, strongly convex boundary derivative estimate, stationary lift, convex exhaustion and normal-family retraction. Source 9.20.2–5, tags 415609592B60, 5DE7AB27F999, E378BBBF406D, 7264782B9A80; physical lines 16–204. The global Lempert retraction invokes §§9.18.1–2; its full upstream chain is not certified.
5. **§12.15 (nonexcluded portion only):** checked Hölder density comparison in §12.15.1, scalar/mass equivalence §12.15.2 (tag D26C76DEC922), fixed-Gauduchon minimax formula (12.15.5, tag B6CA5669E402), and the minimizer ⇒ Gauduchon first-variation step (§12.15.6, tag 87CB9377C0BB). **Do not mark the equality of bounded and smooth mass extrema in §12.15.4 as fully certified:** line 81 invokes the user-deferred Theorem 5.32.1. Other steps were considered conditionally, without exploring the excluded premise.

## Finding disposition and remaining gaps

- New: **one low / verified conditional deduction**, POME-GAUDUCHON-VOLUME-TEST-QUOTIENT-GAP-001; no source correction necessary.
- New confirmed false statements: **zero**. New proof gaps registered: **zero**. Full transitive proof chains certified: **zero**.
- Deferred by user, not resolved: all dedicated Demailly regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof programmes; note §12.15.4's cited dependency only.
- Follow-up candidates outside the excluded scope: source proof of §§9.18.1–2 for the geodesic retract, invariant determinant measure and endpoint current bound from §§12.7/12.9, and §12.14's currents/AGM argument on the degeneracy locus if independent transitive verification is needed.
- The previously withdrawn eight disconnected/noncompact countermodels are **not** reinstated: global connected/compact §1.1 convention governs those claims.
- This run performed no build, tests, Actions CI, publication, main/source/body/registry/tag changes, PR merge or issue creation.
