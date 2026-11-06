# Arbitrary directed nets in the capacity/mass convergence theorem

**Finding:** `POME-NPP-CAPACITY-ARBITRARY-NET-TRANSFER-001`. **Severity:** low. **Status:** verified conditional deduction (not a reported false theorem, not an independent proof of the underlying sequential convergence results). **Date:** 2026-11-06.

## Version, exact integrated anchors and scope

Production `main` reviewed: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Main integrated file: `docs/sections/non-pluripolar-products--capacity-convergence-and-loss-of-mass/index.html`, Git blob `d66813856cb813722806ab912afdfd4815d2da97`. Theorem **13.7.5**, source `foundations-of-pluripotential-theory:AB4EBE3B`, permanent tag `67C4F7EC316E`, physical lines **106–134**; Corollary **13.7.9**, source `foundations-of-pluripotential-theory:82DB3E57`, permanent `D73416504271`, lines **175–209**; the explicitly net-valued Proposition **13.7.8**, source `foundations-of-pluripotential-theory:8CF7A9C6`, permanent `4B60F7F33590`, lines **147–170**. Supporting precise definition **7.5.5**, source `foundations-of-pluripotential-theory:F3E0CD1A`, permanent `DAD5D0809372`, `docs/sections/bedford-taylor-products-and-local-capacity--quasi-continuity-and-convergence-in-capacity/index.html`, blob `464778b7ca6f1a456e36b24ecb4a0c93ab6948d3`, lines **83–89**. The sequential bounded-product input is Theorem **7.5.8** (same file, lines **172–189**).

Only the statements and arguments needed for the following *logical sequential-to-net transfer* were checked. This does not independently certify the Bedford–Taylor continuity theorem, the sequential non-pluripolar proof, its local finiteness hypotheses, or any entire section.

## Precise strengthening of the printed statements

Let `I` be **any directed set**, not necessarily containing a countable cofinal subset. Replace the sequence index `k` in the hypotheses of Theorem 13.7.5 by `a in I`. Keep the same fixed smooth forms `theta_j`, positive currents `T_{j,a}=theta_j+dd^c u_{j,a}`, and limits `T_j`, and suppose each potential converges to `u_j` **locally in extended capacity as a net** in the finite-chart sense of Definition 13.7.2. Write

```text
R_a = <T_{1,a} ∧ ... ∧ T_{p,a}>,    R = <T_1 ∧ ... ∧ T_p>.
```

For every smooth strongly positive test `eta`, one has the net lower bound

```text
liminf_(a in I) ∫_X R_a ∧ eta >= ∫_X R ∧ eta.
```

If also

```text
limsup_(a in I) ∫_X R_a ∧ omega^(n-p) <= ∫_X R ∧ omega^(n-p),
```

then **`R_a -> R` weakly as a net of currents**. For the weighted version, take any Borel `0<=chi_a,chi<=A` with `chi` quasi-continuous and `chi_a -> chi` locally in ordinary capacity as a net. Then

```text
liminf_(a in I) ∫_X chi_a R_a ∧ eta >= ∫_X chi R ∧ eta,
```

and the same mass hypothesis implies **`chi_a R_a -> chi R` weakly as currents**, and as Radon measures if `p=n`. The existing local lower bounds transfer as well **provided the local product finiteness and common local upper bounds in the original local theorem hold on an eventual tail of the net**. No assumption of first-countability of the directed index set or a countable cofinal subnet is made.

This is a conditional extension of the *already stated sequential* Theorem 13.7.5 and Corollary 13.7.9. It should not be mistaken for a proof of those underlying theorems, or for any reversal of the mass assumption.

## Proof: countably many convergence tests, not a cofinal sequence

**Countable error tests.** On a compact `X`, choose the finite bounded-image chart cover appearing in Definition 13.7.2. For each chart choose a compact exhaustion `K_{l,m}` with `K_{l,m} subset int K_{l,m+1}`. For each potential index `j` and each `l,m`, consider the nonnegative number

```text
e_{j,l,m}(a)
 = Cap^*_{D_l}(z_l(K_{l,m} ∩ { d_*(u_{j,a}+h_{j,l}, u_j+h_{j,l}) > 1/m })).
```

For weighted convergence add the two capacity errors of the upper and lower difference sets at threshold `1/m` for `chi_a-chi`, as in Definition 7.5.5. Every such number tends to zero **in the directed-net sense** by the assumptions. The collection of these tests is countable because the atlas is finite, the number of potentials finite, and `m` ranges over positive integers. For any fixed `m`, the estimate at threshold `1/m` implies the corresponding estimate at every larger threshold, and every compact subset of a chart lies in some `K_{l,m}`.

**Bad-index selection.** Suppose a scalar consequence fails for the net: either the asserted liminf is too small, or a real test of the asserted weak convergence stays at distance greater than some `epsilon>0` on a cofinal set. In either case there is a **cofinal bad subset** `B subset I`: for every `a_0 in I` a bad `a>=a_0` exists. For each positive integer `N`, directedness and convergence provide an index `c_N` such that for **all** `a>=c_N`, each test with `j,l,m<=N` has capacity error less than `1/N`. In the weighted case include its finitely many weight tests with `l,m<=N`. If testing a convergence conclusion under the mass-limsup hypothesis, also require at that stage that

```text
∫_X R_a ∧ omega^(n-p) <= ∫_X R ∧ omega^(n-p) + 1/N.
```

Choose inductively `a_N in B` above both `c_N` and `a_{N-1}` (and above any other finitely many imposed stages). This uses **cofinality of B**, *not* cofinality of `(a_N)` in `I`. By construction, for each fixed `j,l,m`, the capacity error along `a_N` tends to zero, and the weight errors do likewise. Since a countable family of compact exhaustions and positive thresholds determines local capacity convergence, the **sequence** `u_{j,a_N}` satisfies the exact sequential extended-capacity hypotheses of Theorem 13.7.5; in the weighted case `chi_{a_N}` satisfies the hypotheses of Corollary 13.7.9. (The fixed positive currents are finite globally by the same finiteness input as in the printed theorem.) Any required mass-limsup bound holds along this sequence by the chosen `1/N` bound.

**Contradictions.** If the net lower inequality fails, fix a strongly positive test `eta` and select `B={a: integral_a < integral_limit-epsilon}`; the extracted sequence contradicts the **sequential** lower inequality. If the weak current convergence fails, choose a smooth test form `eta` witnessing failure, and extract with `B={a: |<R_a-R,eta>|>epsilon}`; sequential Theorem 13.7.5, under the extracted mass bound, forces this difference to zero. If weighted weak convergence fails, repeat with `chi_a R_a` and Corollary 13.7.9. For the top-degree Radon assertion, take the continuous test function witnessing failed Radon weak convergence; the sequential Radon conclusion contradicts its bad-index condition. The weighted lower bound follows exactly as the unweighted one, using the sequential weighted corollary. Local lower bounds require only a countable compact exhaustion inside the chosen local coordinate neighborhood; if the original local theorem asks for a common upper bound, choose `a_N` beyond the tail where that bound holds.

All claims follow. **No step claims that the extracted sequence is a subnet of the directed net.** It is an *increasing sequence of selected indices*, sufficient solely because the printed theorems apply to **any sequence** satisfying their stated convergence conditions. Equivalently, this is a cofinal-violation/diagonal contradiction principle for a countable family of capacity seminorm tests.

## Dependencies, limitations and proposed editorial addition

- **Used, not re-proved:** sequential Theorem 13.7.5, sequential Corollary 13.7.9, Definition 13.7.2/Definition 7.5.5, local coordinate comparison Lemma 13.7.1, and the existing finiteness/existence assumptions for the products. The proof does not treat Demailly regularization or any owner-excluded Bergman/L2/OT/atlas/positivity-loss programme.
- **Not asserted:** direct compactness of an arbitrary net by sequential compactness; uniform tightness of unbounded local products absent the hypotheses; convergence when mass genuinely drops; weak convergence against all bounded measurable tests; or a full independent proof of the sequential inputs.
- **Proposed text only (not production edit):** after the weighted corollary, note that its conclusions and those of Theorem 13.7.5 hold for arbitrary directed nets, and insert the countable exhaustion/cofinal-bad-index proof above. The extension helps subsequent net-valued envelope and model-potential arguments use the exact hypotheses rather than postulating countable cofinality.
- **Affected dependents for checking, not certified:** later uses of convergence in capacity and non-pluripolar mass in Chapters 13, 16 and 17. A separate dependency audit is necessary before declaring any particular downstream argument repaired.

**Classification:** low / verified conditional deduction. The printed statements are sequential and remain correct **conditional on their sequential proofs**. No confirmed error or unverified replacement of the underlying capacity-continuity result is reported. Nothing in the user-deferred approximation/regularization programme is touched.
