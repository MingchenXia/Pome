# 2026-11-01 — exact polarized Monge–Ampère pushforward for log-sum-exp and a rooftop corner

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Stable finding:** POME-LEGENDRE-POLARIZED-SOFTMAX-001 — **low / verified conditional deduction**, not a false printed theorem or a production repair. The proof below is complete for the stated local model **conditional only on the previously established locally bounded Bedford–Taylor mixed-product monotone-continuity and Chern–Levine–Nirenberg bounds**. It is not a verification of the general Kiselman minimum principle or of the full Lemma 17.18.1.

## Integrated reading-edition evidence

The exact primary file on main is
docs/sections/partial-legendre-transforms-and-monge-ampere-mass/index.html,
blob **5d989cf765f5471ce1e2278ef39e2c69979eeb92**;
§17.18 section source **transcendental-positive-cones:17B5480E**, permanent tag **12D395D414C1** (lines 5–10);
Lemma **17.18.1**, source **transcendental-positive-cones:676C0E65**, permanent tag **C12669D1EC3D**, lines **13–23**;
the Schur-complement and angular normalization proof is at **28–40**, bounded psh interpolation at **45–60**, noncompact-fiber control at **60–62**.
The local normalization is dd^c=(i/2π)∂∂̄, y=log|τ|², with d^c y=d arg(τ)/(2π), whose circle integral is one.

For independent rotation only, §10.76 was **first opened directly** at
docs/sections/compact-curves-periods-and-complex-tori/index.html,
main blob **f19750ab7bab07f32873dcd297f2332b3f461129**,
physical lines **4–6**, section permanent tag **2B25FAC99DE6**.
It contains *only a subject-navigation list to §§10.77–10.81*, with no proposition or proof to certify. This is a structural inventory update only, not mathematical coverage of those five child sections.

## Exact two-endpoint identity

Let U be an open subset of C^n (n≥1), and φ,ψ be **locally bounded plurisubharmonic functions** on U. For each real t>0 put

\[
u_t(z,\tau)=\frac1t\log\!\left(e^{t\varphi(z)}
                +|\tau|^{2t}e^{t\psi(z)}\right),
\qquad (z,\tau)\in U\times\mathbb C^* .
\]

This is locally bounded psh: the log-sum-exp function is convex and increasing in each real argument, hence its composition with the two psh arguments φ and ψ+log|τ|² is psh. The partial Legendre transforms, with the conventions of §17.18, are precisely

\[
\widehat u_{t,\lambda}=
(1-\lambda)\varphi+\lambda\psi
-\frac{\lambda\log\lambda+(1-\lambda)\log(1-\lambda)}t
\quad (0\le\lambda\le1),
\]

with the endpoint values defined by continuity, and are identically minus infinity for λ outside [0,1]. The entropy term is a z-independent constant and has zero dd^c. Consequently there is the **temperature-independent Radon-measure identity**

\[
\boxed{\quad
(\pi_U)_*(dd^c u_t)^{\,n+1}
=\sum_{k=0}^{n}(dd^c\varphi)^{n-k}\wedge(dd^c\psi)^k.
\quad} \tag{A}
\]

**Every coefficient is exactly one**, not a binomial coefficient. In particular the right side is independent of t>0. The pushforward is defined on compactly supported nonnegative tests via integration over the full noncompact C* fiber; the proof establishes local finiteness and prevents loss of mass at either end of that fiber.

Moreover, the pointwise decreasing limit as t→∞ is

\[
u_\infty(z,\tau)=\max\{\varphi(z),\psi(z)+\log|\tau|^2\}.
\]

The same pushforward identity (A) holds with u_t replaced by u_∞. This is an explicit **polarization by one logarithmic fiber** of the mixed Bedford–Taylor masses, including the nonsmooth rooftop corner.

## Self-contained computation in the smooth case

First suppose φ,ψ are smooth psh. Write y=log|τ|² and

\[
s=\frac{e^{t(\psi+y)}}{e^{t\varphi}+e^{t(\psi+y)}}\in(0,1).
\]
Then \(\partial_yu_t=s\), \(\partial_{yy}u_t=t s(1-s)>0\), and
\[
\partial_y s=t s(1-s),\quad
(u_t)_{iy}=t s(1-s)(\psi_i-\varphi_i).
\]
The z-Hessian is
\[
(u_t)_{i\bar j}=(1-s)\varphi_{i\bar j}+s\psi_{i\bar j}
 +t s(1-s)(\psi_i-\varphi_i)(\psi_{\bar j}-\varphi_{\bar j}).
\]
Its Schur complement with respect to the y direction is exactly
\((1-s)\partial\bar\partial\varphi+s\partial\bar\partial\psi\).
Using the normalized angular form from §17.18 gives
\[
(dd^c u_t)^{n+1}
=(n+1)\,\partial_y s\,dy\wedge
  \frac{d\arg\tau}{2\pi}\wedge
  \big((1-s)dd^c\varphi+s\,dd^c\psi\big)^n.
\]
For each fixed z, s increases bijectively from 0 to 1 as y runs from -∞ to ∞. Therefore the integral over the fiber equals
\[
(n+1)\int_0^1\sum_{k=0}^n\binom nk
 (1-s)^{n-k}s^k
 (dd^c\varphi)^{n-k}\wedge(dd^c\psi)^k\,ds.
\]
The elementary beta identity
\[
(n+1)\binom nk\int_0^1(1-s)^{n-k}s^k\,ds
=(n+1)\frac{n!}{k!(n-k)!}
\frac{k!(n-k)!}{(n+1)!}=1
\]
proves (A). No asserted independence of coefficients relies on a formal interchange of a limiting operation.

## Locally bounded data: both tails and the rooftop endpoint

On any pair K⊂⊂K'⊂⊂U, choose decreasing smooth psh approximants φ_j↓φ and ψ_j↓ψ on a common neighborhood of K' (local convolution), uniformly bounded on K'. Their mixed Bedford–Taylor measures on K have a uniform mass bound C_K by the local mixed-mass estimate. The differences ψ_j−φ_j are uniformly bounded in absolute value by M_K there. For t≥1 and R>M_K, the logistic variable s obeys
\[
y>R\Longrightarrow 1-s\le e^{-(R-M_K)},\qquad
y<-R\Longrightarrow s\le e^{-(R-M_K)}.
\]
For the smooth approximants the preceding differential formula, positivity and change of variable give, for any fixed nonnegative test supported in K, a bound
\[
\int_{K\times\{|y|>R\}}(dd^c u_{t,j})^{n+1}
\ \le\ 2(n+1)C_K\,e^{-(R-M_K)},
\tag{B}
\]
uniformly in j and t≥1. We may enlarge K slightly to handle compactly supported tests and then let its enlargement shrink; no boundary mass assertion is needed. In particular (B) rules out escaping fiber mass, with a rate uniform across the smooth approximation **and** the large-temperature limit.

For a fixed t, u_{t,j} decreases locally to u_t on every compact cylinder. Locally bounded Bedford–Taylor monotone continuity gives weak convergence of its top measures on those cylinders, while the uniform tail bound passes the pushforward across all y. The mixed products on the right of (A) converge by the same Bedford–Taylor continuity. Thus (A) holds for locally bounded φ,ψ. Since \(u_t\downarrow u_\infty\) as \(t\to\infty\), apply compact-cylinder Bedford–Taylor continuity once again, and invoke the same uniform estimate (B) for t≥1 to obtain the formula for u_∞. This proves both identities as local Radon measures.

The uniform bound for all t≥1 is intentional: no theorem about arbitrary simultaneous non-pluripolar or singular limit interchanges is asserted. For θ-psh endpoints in a **smooth closed** background one may add a local potential of θ and repeat the local identity with θ+dd^cφ and θ+dd^cψ, but no global singular/non-pluripolar extension is claimed in this report.

## Numerical/algebraic normalization crosschecks and disposition

For φ=ψ, all n+1 mixed terms coincide and (A) reads \((n+1)(dd^c\varphi)^n\), matching the direct product \(u_t=\varphi+t^{-1}\log(1+|\tau|^{2t})\). For n=1 it reads \(dd^c\varphi+dd^c\psi\), with no extra factor two. An **independent exact SymPy beta-integral check for n=1,...,7** returned coefficient one for each k; this is not a project test or formal verification.

**Status:** POME-LEGENDRE-POLARIZED-SOFTMAX-001 — low / **verified conditional deduction**, not a confirmed error, not a certified full lemma, and not a production fix. Its mathematical scope is the explicitly locally bounded two-endpoint family and the max limit. Optional action is an example/corollary after Lemma 17.18.1; retain source and permanent tags and original attribution. Potential dependents are the mass normalization in §17.18 and mixed-product identities of §7.3/§7.5. The broader Kiselman/Legendre correspondence, global non-pluripolar statement, and all upstream Bedford–Taylor proofs remain outside this local certification.

**Actual coverage:** additional selected proof-level inspection of §17.18.1 with a new family and limit; it was **already sampled in 2026-10-23** (the prior logistic coefficient-(n+1) test is not counted again). First structural reading of §10.76 only, no mathematical assertion there. No entire mathematical section certified; collection remains **25 actual chapters / 747 ToC sections / zero fully certified sections**. All historical ledger findings remain unchanged. All user-excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss work stays **deferred-by-user**, not touched or certified. Only audit Markdown is proposed; no main/source/proof-registry/canonicalization/tag/CI/build/formalization/site/publication changes.
