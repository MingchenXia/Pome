# Mathematical audit: sharp spherical logarithmic constants and nonpolar zero-dimensional Cantor sets

**Checkpoint:** 2026-10-23 15:54 Asia/Shanghai. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Pre-write review head:** e5936ebf56694e46cea49015f5466d1469e28ee1. Main README.md and AGENTS.md (eda69505b93b4782290d9cfac07c8651dedd17c5), documentation/proof-expansions.md (8b37e218c74d5a93637e0f092cf5f29cc338a94d), review-branch README.md and mathematical-audit/LATEST.md (4f19bd22d8c151ad84d2b37f70eded347b393171), and main ToC (c0c07abf4d8f7575b54cff2ec694fcf987f51cf8) were freshly read. There are 25 chapters and 747 inventory sections, **not 747 verified sections**.

**Actual new selected proof coverage:** §5.50.1–3 (raw extremal annulus test and plurifine limits); §5.51.1 (Cantor code, smooth nonpluripolar graph and slicewise energy); §5.57.1, 5.57.4, 5.57.7, 5.57.11 (sphere logarithms and integration/Grassmannian normalization). Internal §4.1.17 and §5.47.10 were checked only as precise upstream theorem links; their entire dependency chains remain conditional. None of these sections was completely certified. The Demailly *approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme* was **not** reopened; previous records retain deferred-by-user status.

## POME-SPHERE-LOG-HARMONIC-001

**Status:** verified conditional deduction; **severity:** low (strengthening, not an original false theorem). **Exact source:** docs/sections/real-currents-submersions-and-homotopies--averaging-complex-planes/index.html, blob 2245f2fee90247cc55a3b57b9b41e0af135abcd1. Lemma 5.57.1 source demailly-complex-geometry:B58E58A0, permanent tag F08E0D60DA23, lines 11–46; Equations 5.57.2/3 source labels A38ACD30/79B51C09, permanent tags 6A107C250306/F0FBE5A138FA (lines 12–21).

Let ξ be uniformly distributed on the unit sphere in C^n and ℓ_ξ(z)=⟨z,ξ⟩. For all n≥1, with H_0=0 and H_m=Σ_{j=1}^m 1/j, the constants in the printed lemma are **exactly**
\[
c_n=-H_{n-1},\qquad C_n=H_{n-1}.
\]
Indeed, put r=|z|²>0. The exact absolute logarithmic moment is
\[
\int |\log|\ell_\xi(z)|^2|\,d\sigma(\xi)=
\begin{cases}
-\log r+H_{n-1},&0<r\le1,\\
\log r-H_{n-1}+2\sum_{k=1}^{n-1}(-1)^{k+1}\binom{n-1}{k}r^{-k}/k,&r\ge1.
\end{cases}
\]
The sum is empty for n=1. In particular the constant in (5.57.3) is **sharp**: equality holds for every 0<|z|≤1.

**Proof.** By unitary invariance, |ℓ_ξ(z)|²=rS, where S=|ξ_1|². Normalize independent standard complex Gaussians G_1,...,G_n to obtain the uniform sphere distribution; Y_j=|G_j|² are independent mean-one exponentials. Conditioning on W=Σ_{j=2}^n Y_j gives P(S>u)=E(exp[-uW/(1-u)])=(1-u)^{n-1} for 0<u<1, also covering the deterministic n=1 case. Hence X=-log S≥0 satisfies P(X>t)=1-(1-e^{-t})^{n-1}. Layer-cake integration yields
\[
EX=\int_0^\infty [1-(1-e^{-t})^{n-1}]dt
=\int_0^1 \frac{1-(1-s)^{n-1}}s\,ds=H_{n-1}.
\]
Thus E log(rS)=log r-H_{n-1}. If a=log r≤0, a-X≤0 and E|a-X|=-a+H_{n-1}. For a≥0, |a-X|=a-X+2(X-a)_+, so
\[
E|a-X|=a-H_{n-1}+2\int_a^\infty[1-(1-e^{-t})^{n-1}]dt.
\]
Expand the finite binomial polynomial and integrate termwise to obtain the second branch. At a=0 both branches equal H_{n-1}. This proves optimality and integrability without any current regularization. QED.

**Correction proposal and affected dependents:** optional exact-constant corollary immediately following Lemma 5.57.1; preserve its tag and history. Improves the explicit Fubini coefficient bound (5.57.10), and the plane-average estimates used in §§5.57.4–11. This does not independently certify those downstream current theorems.

## POME-SMOOTH-NONPOLAR-CANTOR-CAPACITY-001

**Status:** verified conditional deduction; **severity:** low (not a counterexample to the printed theorem). **Exact source:** docs/sections/smooth-curves-which-are-not-pluripolar/index.html, blob 46a19f83fb124ff5a683a25b26660c1c6a24f56e; Theorem 5.51.1 source klimek-pluripotential-theory:F3192D90, permanent tag 283A0A00F1E4, lines 8–69. The digit/separation construction is lines 20–31, smooth graph lines 32–53, the transverse Cantor measure lines 54–61, and the iterative slicing/Josefson step lines 62–69.

Take exactly the printed frozen-bit Cantor slices C_a⊂[0,1] with Q=2^{n+1}+1 (n≥2), and C'={Σ_{k≥1} a_k 10^{-k²}: a_k∈{0,1}}. Use classical *planar logarithmic* capacity cap_log(K)=exp[-inf_{μ∈P(K)}∬log(1/|x-y|)dμ(x)dμ(y)], **not** Pome's relative Green capacity C_B. Then
\[
\boxed{\operatorname{cap}_{\log}(C_a)\ge Q^{-2}
\quad\text{for every frozen array }a,\qquad
\operatorname{cap}_{\log}(C')\ge(2\cdot10^6)^{-1},\qquad
\dim_H C'=0.}
\]

**Proof.** For the printed cylinder probability μ_a on C_a, conditional on any fixed first code, the first differing bit is at index k with probability 2^{-k}; the printed digit separation gives |x-y|≥Q^{-k}. Thus I(μ_a)≤log Q Σ_{k≥1}k2^{-k}=2log Q, which proves the first uniform capacity bound. On C', the transverse first difference at k has distance at least 10^{-k²}/2. With its cylinder probability ν, I(ν)≤Σ_{k≥1}2^{-k}(k²log10+log2)=6log10+log2; exponentiate for the second bound. Finally at level k the first k bits cover C' by 2^k intervals of length at most Σ_{j>k}10^{-j²}≤2·10^{-(k+1)²}. For every s>0 the total s-dimensional content ≤2^k(2·10^{-(k+1)²})^s tends to zero, so dim_H C'=0. These quantitative conclusions need only the elementary cylinder calculation, not Josefson. The original construction uses internal Pome Theorem 4.1.17 (tag 5B4ACD7E054D, planar finite-energy nonpolarity) and Theorem 5.47.10 (tag 1822741C4B07, Josefson), both linked in the proof and retained with attribution. QED.

**Correction proposal and dependents:** optional separate quantitative remark after Theorem 5.51.1; preserve its existing proof and provenance. Theorem 5.51.1 is not false; this makes explicit why dimension-zero transverse sets still support the nonpluripolar slicing argument.

## Additional checked proof boundaries

In §5.50 (docs/sections/plurithin-annuli-and-plurifine-limits/index.html, blob 69642722f934c7ed0acc637ffa79a551da4aceef), Theorem 5.50.1 tag 0313727814DD, lines 11–27, uses raw relative extremals and a decreasing PSH series finite at a; Theorem 5.50.2 tag 8289C8DFE8FE, lines 28–53, uses a plurifine diagonal; Theorem 5.50.3 tag E34D223CA44D, lines 54–70, glues only after strict barrier separation. Selected steps are consistent **conditional on the independently stated plurithin amplification input**, whose full proof was not certified this session. §5.57 coefficient integration/Grassmannian identification similarly relies on unreviewed upstream current calculus. No newly confirmed original false mathematical theorem. Do not treat the ordinary Demailly geometry source attribution for the sphere lemma as authorizing review of the separately excluded approximation programme.

One small local exact-rational consistency script checks 239 harmonic/binomial, Cantor energy-series and finite digit-separation identities. It does not prove the analytic theorems or validate full builds. No project tests, full build, CI, publishing, website or main/source/registry/permanent-tag changes, formal verification, branch reset, PR or merge occurred in this audit.