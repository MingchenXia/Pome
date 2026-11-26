# Non-pluripolar products: positive cohomological defect currents

Date: 2026-11-27. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit parent: 8e263410359bda8ee00f73a290a13bbe93f5d7cb.

## POME-NPP-TRUNCATION-COHOMOLOGICAL-DEFECT-001

Low / verified conditional deduction (not an error in the printed theorem; no novelty claim outside this audit).

Anchors: docs/sections/non-pluripolar-products--global-finiteness-and-bounded-cohomological-mass/index.html, blob 943517743538820940559eae8469ce98ecf5fcd5. Proposition 13.5.1 (06A36B9354A5), lines 11–27; Theorem 13.5.4 (source A00627D3, permanent 3783DE0B4D00), lines 85–119; equation 13.5.5 (896BDD434F7F). Multilinearity 13.2.6 (7F7123F92478). The common truncation identity on G_k is at line 118.

**Claim.** With the hypotheses and notation of 13.5.4, let A_j=T_j+C omega, tau_j=theta_j+C omega, and P_I denote the non-pluripolar product of the T_j with j in I, with P_empty=1. There is a closed positive (p,p)-current D such that

    [D] = product_j [tau_j] - [<A_1 wedge ... wedge A_p>].

In particular, if all theta_j are semipositive, one can take C=0, and the cohomological defect of the mixed NPP is represented by a positive closed current, not merely nonnegative after integration against omega^(n-p). For arbitrary theta_j, the stronger bound for every smooth closed strongly positive (n-p,n-p)-form eta is

    integral P_{1,...,p} wedge eta
      <= integral product_j tau_j wedge eta
         - sum_{I proper subset of {1,...,p}}
              C^(p-|I|) integral P_I wedge omega^(p-|I|) wedge eta.

At C=0 omit terms with positive exponent (no empty-product ambiguity). This retains the exact contribution of every lower-degree NPP rather than dropping all the additional positive terms, as is sufficient for (13.5.5).

**Proof.** Put G_k=intersection_j {phi_j > -k} and B_k=product_j (tau_j+dd^c max(phi_j,-k)). The tau_j are semipositive, so these are bounded Bedford–Taylor products of closed positive currents. Proposition 13.5.1 fixes their pairings with every smooth closed complementary form and in particular their trace masses against omega^(n-p). By compactness for positive currents of uniformly bounded mass on compact X, choose a weakly convergent subsequence B_{k_l} with k_l increasing to infinity (one may extract from the integer sequence of truncations; no arbitrary directed net is assumed sequentially compact). Denote its closed positive limit by B. Proposition 13.5.1 and weak convergence against smooth closed forms give [B]=product_j[tau_j].

By the exact common-level identity of line 118, 1_{G_k} B_k = 1_{G_k} P_A, where P_A=<A_1 wedge ... wedge A_p>. The latter restrictions tend weakly to P_A: their scalar trace measures increase to the trace of P_A, since its mass on the union of the pole sets is zero. For any smooth test form, its absolute pairing with the positive tail current is controlled by a fixed constant times that tail's trace mass. Thus the restrictions converge, even in coefficient total variation in finitely many compact charts. Since B_k-1_{G_k}B_k is positive, its subsequential limit D=B-P_A is positive. It is closed because B and P_A are closed; subtracting their classes gives the claim. This does not assert that B is unique, or that D is supported on a closed analytic pole set. No limit of moving-set indicators was interchanged with the weak limit of B_k.

By multilinearity, P_A=sum_I C^(p-|I|) P_I wedge omega^(p-|I|), including the smooth empty term. Pair the positive D with eta and rearrange. In degree one C cancels entirely. In degree two and eta=omega^(n-2), write delta_j=int (theta_j-P_{j}) wedge omega^(n-1). The estimate reads

    int <T_1 wedge T_2> wedge omega^(n-2)
       <= int theta_1 wedge theta_2 wedge omega^(n-2)
          + C(delta_1+delta_2).

The degree-one argument gives delta_j>=0 independently of the shift.

Sharpness of the semipositive cohomological inequality: for T_j smooth semipositive one may use phi_j=0 and D=0. A strictly positive defect occurs on P^n with theta_j=omega_FS, normalized integral omega_FS^n=1, T_1=[H], and T_2=...=T_p=omega_FS. Since <[H]>=0 and the remaining factors are smooth, P_{1,...,p}=0. The defect class is [omega_FS]^p and the common truncation products have trace mass one. This uses only Poincare–Lelong and the degree-one NPP example/linearity.

**Status and downstream:** retain 13.5.4–5 unchanged; optionally insert the claim after line 118. It strengthens the mass-control step but does not certify mixed mass comparison in 13.8 or any existence theorem. Dependencies: bounded BT recursion/locality, 13.2.2/6, 13.3.1 closedness, 13.5.1, and positive-current weak compactness; not independently transitively certified. No regularization input needed for this deduction.

## Actual coverage

- Whole direct conditional §13.5, mathematical lines 7–215 (same blob as above; previous status HISTORIC-PARTIAL-REPORTED). Checked bounded Stokes telescoping, 13.5.2 local identity (13.5.3, 81F1166426A9), signs from d(BR), the weighted continuity with fixed B and dominated convergence, global finite trace via truncations, and mixed lower bounds. 13.5.8–11 previously reviewed in the finite-mixture report of 2026-11-17; not a new finding. At line 213 of 13.5.11, clarify that equality at endpoints refers to the weighted AM–GM inequality, not the subsequent bound by f+g; no false theorem or proof gap recorded. Extended nonnegative densities can be replaced on nu-null sets by finite values, so no 0 times infinity convention affects the measure assertion.
- Repeat direct §13.12, mathematical lines 7–111, docs/sections/non-pluripolar-products--quasi-continuous-functions/index.html, blob 110ec8727eca146a1304cfd43fdbeb4eebf96290. Checked replacement proof of 13.12.7 (D56D6D4A5E94): finite intersection property for decreasing nets and Choquet extraction plus Dini for increasing nets; local qualification retained. Checked 13.12.8 (source B4CE255F, permanent 272876B00528) weighted local capacity proof, open exceptional-set budgets, null modification and smooth-form expansion. This is repeat-only (historic full reported, 2026-11-19); no new coverage or claim of upstream certification. The capacity comparisons, outer regularity, Choquet selection and weighted BT continuity remain conditional on the referenced results. The proof expansion for 13.12.2 invokes comparison with Kähler capacity; this was not independently reproved.
- Current chapter 13 TOC checked: 32 numbered sections, matrix has all 32; matrix overall has 747 distinct numbered rows. No fresh whole-project TOC comparison or full proof-chain certification.
- No newly confirmed false statements, no newly demonstrated proof gaps. One conditional deduction; one new whole direct current review relative to recorded partial status, one full repeat. Historical first visit not asserted. Demailly approximation/regularization and all dedicated associated programmes remain deferred-by-user, not certified or reopened. No build, tests, CI, publication, or source/registry changes.
