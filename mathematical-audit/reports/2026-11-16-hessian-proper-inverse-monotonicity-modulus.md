# Exact inverse-monotonicity modulus for bounded complex Hessian equations

**Finding:** POME-HESS-PROPER-INVERSE-MODULUS-001  
**Date:** 2026-11-16  
**Status:** verified conditional deduction (low); **no false printed theorem and no certified analytic upstream chain**.  
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Integrated reader file:** docs/sections/complex-hessian-equations--hessian-mass-and-global-comparison/index.html  
**Blob:** 580d3bc2b10ebd01d880b2a31fc6930436570aac.  
**Stable anchors:** Theorem 8.13.10, source non-kahler-pluripotential-theory:98425BFC, permanent A532C77D7D0C, physical lines 281–303; Corollary 8.13.11, source :B7B86F6A, permanent 6BFB2EB67A74, lines 305–325; Proposition 8.13.12, source :3FE616D3, permanent FBE7E9A6BE5E, lines 330–353. The admissible-cone convention in §8.2 lines 5–16 is context.

## Statement and hypotheses

Work on the compact Hermitian manifold and with the admissibility and complex Hessian measure H_m of Chapter 8, in the range of its comparison theorem. Let A<B, L=B-A, and let f:X×[A,B]→ℝ be a bounded Borel function, nondecreasing in its second argument at every x. For 0≤s≤L define its **uniform strict-increase modulus**

\[
\Delta_f(s)=\inf_{\substack{x\in X\\A\le t\le B-s}}
                \bigl(f(x,t+s)-f(x,t)\bigr).
\]

Then Δ_f(0)=0, Δ_f is nonnegative and nondecreasing. Let ν be a finite positive Radon measure; let h_1,h_2 be bounded ν-measurable real functions, and suppose bounded admissible u,v with values in [A,B] solve

\[
H_m(u)=e^{f(x,u)+h_1}\nu,\qquad
H_m(v)=e^{f(x,v)+h_2}\nu.
\]

Put K=||h_1-h_2||_{L^\infty(\nu)} and define

\[
R_f(K)=\sup\{s\in[0,L]:\Delta_f(s)\le K\}.
\]

**Conclusion.** Independently of smoothness or a positive derivative lower bound for f,

\[
\boxed{\quad\|u-v\|_{L^\infty(X)}\le R_f(K).\quad}
\]

In particular, if Δ_f(s)>0 for every s>0, then K=0 implies u=v. This does not assert existence for Borel f.

For f(x,t)=t^{2q+1} on a symmetric interval [-R,R], q≥1, exact minimization yields

\[
\Delta_f(s)=\frac{s^{2q+1}}{2^{2q}}\quad (0\le s\le2R),
\quad
\boxed{\ \|u-v\|_\infty\le
\min\{2R,(2^{2q}K)^{1/(2q+1)}\}.\ }
\]

The exponent and **numerical coefficient** 2^{2q/(2q+1)} are optimal across this class. In particular, cubic properness f(t)=t³ has sharp universal error modulus (4K)^{1/3}, despite inf f'(t)=0 on [-R,R]. Hence the strictly positive differential lower bound κ in printed Proposition 8.13.12 is sufficient for *Lipschitz* stability, but is not necessary for uniqueness or for an exact (generally Hölder) stability estimate.

## Proof

1. For s_2≥s_1≥0, every pair (x,t) admissible for s_2 is admissible for s_1, and monotonicity gives
   f(x,t+s_2)-f(x,t)≥f(x,t+s_1)-f(x,t)≥Δ_f(s_1).
   Thus Δ_f is nondecreasing, even without continuity of f.

2. Fix s∈(0,L] with Δ_f(s)>K and let E_s={v+s<u}. On E_s the **actual** values u,v belong to [A,B], so v+s≤u≤B. Pointwise monotonicity and the defining infimum give f(x,u)-f(x,v)≥Δ_f(s). Since h_2-h_1≤K ν-almost everywhere, restriction of the two measure equations yields
   \[
   \mathbf1_{E_s}H_m(v+s)=\mathbf1_{E_s}H_m(v)
   \le e^{K-\Delta_f(s)}\mathbf1_{E_s}H_m(u).
   \]
   The coefficient c=e^{K-Δ_f(s)} lies in (0,1). Apply **exactly** Theorem 8.13.10 to the bounded admissible pair (v+s,u), invoking constant-invariance of H_m. It yields v+s≥u on all of X, including any non-open/contact-set subtleties. The shifted potential need not belong to [A,B]: f was evaluated only at u and v.

3. Exchange u,v to obtain |u-v|≤s. Since Δ_f is nondecreasing, every s>R_f(K) has Δ_f(s)>K. If R_f(K)<L, pass s↓R_f(K) from above; if R_f(K)=L, |u-v|≤L is immediate from the range assumption. This proves the uniform estimate without assuming continuity of Δ_f. When K=0 and Δ_f(s)>0 for every s>0, R_f(0)=0, giving uniqueness.

4. For f(t)=t^{2q+1}, the derivative of g_s(t)=(t+s)^{2q+1}-t^{2q+1} with respect to t is
   (2q+1)[(t+s)^{2q}-t^{2q}]. It is negative for t<-s/2 and positive for t>-s/2. The point -s/2 lies in [-R,R-s] for 0≤s≤2R. Consequently the exact minimum is
   g_s(-s/2)=s^{2q+1}/2^{2q}; inversion gives the stated bound.

5. **Sharpness and no hidden PDE construction.** On any compact Hermitian X, constants are admissible and H_m(c)=ω^n. Set ν=ω^n, u=s/2, v=-s/2 with 0<s≤2R, h_1=-(s/2)^{2q+1}, h_2=(s/2)^{2q+1}. Both equations hold identically. Here K=s^{2q+1}/2^{2q} and ||u-v||∞=s. Thus equality is achieved and neither the exponent nor its coefficient can be improved. For q=1 the identity
   \[
   (t+s)^3-t^3-\frac{s^3}{4}
      =3s(t+s/2)^2\ge0
   \]
   is an independent exact algebraic check.

## Audit classification / impacts

This is an **additional conditional deduction** from the already printed strict measure domination Theorem 8.13.10, not an error in Theorem 8.13.10 or Proposition 8.13.12 and not a replacement of the latter's sharp Lipschitz statement. The recently recorded two-slope result POME-HESS-ORDERED-LOGDATA-TWO-SLOPE-001 assumes κ>0 and derives order-sensitive linear bounds; it does **not** cover this κ=0 sharp inverse-modulus regime. The proof does not reopen or invoke any Demailly approximation, Bergman, L², Ohsawa–Takegoshi, multiscale or positivity-loss completion programme.

**Upstream status:** Theorem 8.13.10 depends on 8.13.8, 8.13.7 and the bounded-Hessian current/locality framework (§§8.11–8.12); this run read the integrated comparison and torsion-recursion proof passages (physical lines 173–303) but did not independently certify analytic smooth-approximation, decreasing convergence or the whole comparison dependency graph. Thus the deduction is conditional on the printed comparison theorem. All previously classified proof gaps remain unchanged. Hironaka is not used.

**Proposed manuscript enhancement:** append this as a clearly labeled conditional corollary to §8.13.12, if desired, without altering its hypotheses or permanent tags. It also gives a natural error modulus for strictly monotone nonlinearities with vanishing derivative, relevant to proper-equation uniqueness and stability.

**Exact coverage delta:** Direct new hypothesis-level review of §8.13.10 and Proposition 8.13.12 (lines 281–303 and 330–353), plus their torsion comparison chain at lines 173–273 as conditional context. §8.13 was previously partially reviewed: **0 new first-visited numbered sections, 0 fully certified sections**. The existing generated ToC inventory is 25 chapters / 747 numbered active sections; this run did not recompute the complete inventory independently. No project build, formal verification, CI or site publication.
