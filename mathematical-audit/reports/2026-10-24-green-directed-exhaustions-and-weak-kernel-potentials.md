# Directed Green exhaustions and weakly convergent fundamental potentials

**Review date:** 2026-10-24 (Asia/Shanghai). **Current main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Status of both new findings:** low severity / **verified conditional deduction**, not a false theorem or a repair to published material. Both are direct consequences of the identified reading-edition inputs; those inputs have been checked at the indicated passages, but the entire upstream theory has NOT been certified.

**Scope / deliberate rotation.** First selected proof-level pass of previously inventory-only §§3.1 and 3.4. Exact integrated HTML paths, blobs and anchors:
- docs/sections/harmonic-functions-and-the-dirichlet-problem/index.html, blob fc02188d6e246a21aa07acd8bf6d3712761ba6e5; Theorem 3.1.7 (source 667A5C9D; permanent tag A60BA3B2DBFC; physical lines 135–142, derivative estimates in the following proof); Theorems 3.1.25, 3.1.27, 3.1.29 (source 6EC9A4AF/2949A188/3442F8BF; tags 537ACE84788C/8FE1B604CDA2/C1B72E118338; statement lines 512–514, 551–553, 589–591); Theorem 3.1.34 (source 497FD574, permanent tag 476CFD04AAC6, statement lines 671–695 and subsequent proof). The new exhaustion lemma uses the domain monotonicity, exhaustion, and derivative estimate, not the independent converse barrier result.
- docs/sections/subharmonic-functions/index.html, blob 3d06e9703f2eb184cf63a2c45524ed6acbeeebd2; Proposition 3.4.11 (source 45B5A1B8; permanent tag 1F52C5AF98EF; statement lines 186–192 and proof immediately afterward); Theorem 3.4.12 (source 7E2C1398; tag E76E281548A5; statement lines 218–239 and subsequent proof); Theorem 3.4.14 (source A2BCDB4A; tag F04DBD614238; statement lines 298–304 and proof afterward). Choquet selection / increasing envelopes (§§3.4.22–23, tags B37EED9280E3 and 1C986491E366) and removable polar sets (§3.4.27, tag 8B711E470600) were read for dependency boundaries only, not completely certified.

The ToC at docs/chapters/index.html on this main has 25 chapters and 747 sections. Those counts are a coverage *inventory*, not 747 verified mathematical sections. The user-excluded Demailly approximation/regularization, and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme, was not reopened; prior such notes remain deferred-by-user.

## POME-CLASS-GREEN-DIRECTED-EXHAUST-001

**Severity/status:** low / verified conditional deduction. **Proposed addition:** optional nonsequential corollary after Theorem 3.1.34, preserving that theorem, its source attribution and tag. **Affected dependents:** constructions of Green potentials by arbitrary increasing unions of regular domains; potential future uses of ordered families without a countable cofinal index subset. No printed theorem is false.

**Statement.** Let D be a bounded regular domain in Euclidean space of dimension d≥1. Let (D_i) indexed by a **directed set I** be an increasing family of bounded regular domains: i≤j implies D_i⊆D_j, and their union is D. For x in D, eventually x belongs to D_i. For every y≠x in D, with both points eventually in D_i,

    G_{D_i}(x,y) increases to G_D(x,y).

For each fixed x and each integer k≥0, the convergence is in C^k on every compact subset of D\{x}; equivalently it is C^∞_loc there. No countable cofinal subset of I is assumed or asserted.

**Proof.** Fix a compact exhaustion K_1⊂int(K_2)⊂... of D (possible since D⊂R^d is open and second countable). Each K_m is covered by the open sets D_i. Finitely many members cover K_m; since I is directed, some i'_m dominates their indices, so K_m⊂D_{i'_m}. Inductively pick i_m≥i_{m−1},i'_m, giving an increasing *auxiliary* chain D_{i_m} whose union is D. Theorem 3.1.34, applied to this actual sequence of regular domains, gives G_{D_{i_m}}(x,y)↑G_D(x,y) and C^∞ convergence off the pole.

For i≥i_m, monotonicity of the Green function for regular domains yields

    0≤G_D(x,y)−G_{D_i}(x,y)≤G_D(x,y)−G_{D_{i_m}}(x,y)

for y∈D_{i_m}\{x}, once x lies in that domain. The right-hand side tends to zero uniformly on each fixed compact subset away from x. It follows by the **definition of convergence of a net** that G_{D_i}(x,·)→G_D(x,·) uniformly on those compacta; no sequential subnet inference occurred.

To control derivatives, the difference h_i(y)=G_D(x,y)−G_{D_i}(x,y) is harmonic in y on all D_i: both Green functions have the same singular fundamental kernel at x, so the pole cancels (this includes d=1). Given compact L⊂D\{x}, choose finitely many balls B_a with L covered by their concentric half-balls and whose closed double balls lie in D, and fix m large enough that these closed balls lie in D_{i_m}. For i≥i_m, on each ball 0≤h_i≤h_{i_m} and h_{i_m}→0 uniformly, by the sequential exhaustion theorem already established. The interior harmonic derivative estimate of §3.1.7 then gives for every multi-index α a constant C_{L,α}, independent of i, such that

    sup_L |∂^α h_i| ≤ C_{L,α} max_a sup_{B_a} h_i
                       ≤ C_{L,α} max_a sup_{B_a} h_{i_m} →0

as m increases. Therefore the original net converges in each local C^k seminorm, which proves the assertion. The auxiliary sequence is a bounding device only; it is **not claimed cofinal** in I. QED.

**Boundary/limitations.** The bounded regularity of D and every D_i is part of the statement; it is not enough to replace regularity by arbitrary open sets and quote the printed theorem without defining the generalized Green kernel. The proof is conditional on the printed domain monotonicity and sequential exhaustion theorem §3.1.34 and the internal harmonic estimates of §3.1.7. It does not establish the whole Martin-boundary theory or a universal criterion for regularity.

## POME-CLASS-POTENTIAL-WEAK-L1-001

**Severity/status:** low / verified conditional deduction plus a sharp counterexample to an *unclaimed stronger continuity principle*. **Proposed addition:** optional corollary after Proposition 3.4.11 / Theorem 3.4.14, distinguishing L1 convergence from pointwise convergence. **Affected dependents:** Riesz-potential approximations and continuity when distributions of compactly supported positive charges vary; relevant in §3.4 and potentially §4.1. This is not a counterexample to Proposition 3.4.11.

**Statement.** Let L⊂R^d be compact. Let ν_i, indexed by an arbitrary directed set, be finite positive Borel measures supported in L and converging weakly on C(L) to a finite positive measure ν. Define p_i=E_d*ν_i and p=E_d*ν with the fundamental solution E_d of Proposition 3.1.13 (source 571B3697, tag F8A69601BB8C), so Δp_i=ν_i, Δp=ν by Proposition 3.4.11. Then

    p_i → p in L1_loc(R^d).

If K⊂R^d\L is compact, all derivatives of p_i converge uniformly on K to those of p; i.e., p_i→p in C^∞_loc(R^d\L).

**Proof, including net topology.** Weak convergence against the constant 1 on the compact L implies that ν_i(L) is eventually bounded by a common M. Fix any compact K⊂R^d. Translation continuity of the locally integrable kernel E_d implies that

    Φ : L → L1(K),       Φ(y)=[x↦E_d(x−y)]|_K

is norm-continuous. Indeed, K−L is compact and the L1_loc translation theorem applied to a neighborhood of K−L gives ||Φ(y)−Φ(y')||_{L1(K)}→0 as y'→y. The image Φ(L) is compact in L1(K).

For ε>0, choose finitely many points y_1,...,y_N∈L and a continuous partition of unity θ_1,...,θ_N on L supported in sufficiently small neighborhoods of those points so that uniformly for y∈L,

    ||Φ(y)−Σ_a θ_a(y)Φ(y_a)||_{L1(K)}<ε.

This is a finite-dimensional uniform approximation, not a convergence theorem about sequences of measures. The potential p_i represents the Banach-space integral ∫_L Φ(y)dν_i(y), by Fubini's theorem and the bound

    ∫_L ||Φ(y)||_{L1(K)} dν_i(y)
      ≤ ν_i(L) ∫_{K−L} |E_d(z)|dz < ∞.

The same holds for p. Thus, by the triangle inequality,

    ||p_i−p||_{L1(K)}
      ≤ ε(ν_i(L)+ν(L))
        + Σ_a |∫_L θ_a d(ν_i−ν)| ||Φ(y_a)||_{L1(K)}.

The finite sum tends to zero along the **original net**, by its weak convergence. Taking limsup, then ε↓0, proves L1(K) convergence and hence L1_loc convergence. When K is disjoint from L, all x-derivatives ∂_x^αE_d(x−y) are jointly continuous on K×L. Applying the same finite-rank argument in C(K) to these derivatives, for each α, gives uniform convergence of ∂^αp_i to ∂^αp on K. QED.

**Why pointwise convergence is not automatic.** In d=2 take

    ν_j=(2π/j)δ_{exp(−j)e_1},  j≥1,       ν=0.

These are positive compactly supported measures in the closed unit ball, converging weakly to zero because their total masses tend to zero. However E_2(z)=(1/(2π))log|z|, hence for every j,

    (E_2*ν_j)(0)=(2π/j)·(−j/(2π))=−1,

whereas E_2*ν(0)=0. Thus the L1_loc result cannot be strengthened to **pointwise convergence at every point** without additional hypotheses. The example has no conflict with distributional convergence or the original Riesz decomposition.

## Selected proof checks and limits

1. **§3.1** Read the integrated proofs for Perron lifting / harmonic envelope (§§3.1.24–25), the positive linear boundary operator (§3.1.27), the regular-barrier implication (§3.1.29), and positivity, uniqueness, domain monotonicity and regular exhaustion (§3.1.34). The new net result depends specifically on the last theorem and the interior estimates, not a global classification of regular boundaries. No confirmed false theorem or demonstrated gap from these selected passages.
2. **§3.4** Checked the compact-kernel integrability and Fubini computation of Proposition 3.4.11, positivity and canonical distributional representatives in §3.4.12, the localized Riesz split in §3.4.14; also inspected the Choquet selection argument and the polar-removability construction for hypothesis checks. The new weak-measure result is an independent Banach-valued finite-rank argument; it neither silently invokes regularization nor claims pointwise convergence.
3. **Dependency status:** real harmonic interior estimates, local integrability of E_d and distributional fundamental-solution normalization are explicit internal inputs. Their use is not an unproved external citation; no Hironaka premise is needed. None of the full §§3.1 or 3.4, or their transitive dependencies, is mathematically certified.
4. **Reproducibility:** the d=2 atom example can be verified by the symbolic identities mass(ν_j)=2π/j→0 and (2π/j)(log(e^(−j))/(2π))=−1. The main conclusions are analytic proofs; no numerical test, project test/build, formal proof checker, CI, website publication or source/registry/canonicalization/permanent-tag/main edit was performed.

**Persistent disposition:** statuses are verified conditional deductions, not resolved former defects. All earlier excluded-work notes remain deferred-by-user; they are not reclassified. Keep previous findings and attribution history intact.
