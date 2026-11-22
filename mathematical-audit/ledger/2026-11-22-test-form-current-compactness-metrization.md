# POME-TESTFORMS-POINTWISE-BOUNDED-WEAK-COMPACT-METRIZABLE-001

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Severity:** low. **Status:** verified conditional deduction, NOT a source-theorem error, proof gap, or complete transitive proof certificate.

**Exact file:** docs/sections/test-form-topology-and-compactness-of-currents/index.html, main blob 420522ce2f3e4d8a8cbc3d8a3c1bb270d62ece4b, physical lines 11–40, 48–70 and 95–129.

**Stable source labels/permanent tags:** Theorem 2.10.5 demailly-complex-geometry:6DD9E811 / 423C948D346B; Proposition 2.10.2 E541977A / BC76137F21A7; Proposition 2.10.3 1DAD97D6 / 257A408A0F68; equation (2.10.6) tag 73EE691E4241.

**Hypotheses:** M smooth, Hausdorff, second-countable; \(0\le p\le\dim M\); A a pointwise-bounded subset of currents \(\mathcal D'_p(M)\).

**Precise claim:** The full weak closure K of A is compact and metrizable. A countable dense family of tests \(\varphi_j\) yields
\[
d_K(S,T)=\sum_{j=1}^\infty 2^{-j}\min\{1,|(S-T)(\varphi_j)|\}.
\]
Every sequence in A has a weakly convergent subsequence. The unrestricted dual is not asserted to be metrizable.

**Complete new mathematical step:** Each fixed-compact test-form Fréchet space is separable, as a subspace of the countable product of separable coefficient-derivative \(C(Q)\) spaces. A countable union of countable fixed-support dense subsets is dense in the actual test-form locally convex topology, since each fixed-support inclusion is continuous and the spaces exhaust all tests. By the printed Theorem 2.10.5, K is compact and all its elements are continuous currents. Evaluation on the countable dense set is continuous and injective into \(\mathbb C^{\mathbb N}\); compact-to-Hausdorff implies that it is a homeomorphism onto a compact metrizable subspace. Only then infer sequential compactness. The example \(\partial_x^j\delta_j\to0\) on \(\mathbb R\) shows there is no common global support/order hypothesis to add.

**Proposed correction:** none needed; optional corollary after Theorem 2.10.5. **Potential dependents:** §§5.19, 5.63, 11.22, provided their families satisfy pointwise boundedness. **Unresolved:** transitive upstream compactness/separability details have not all been independently certified.

[Full proof and cross-chapter coverage](../reports/2026-11-22-test-form-current-compactness-metrization-rotation.md). User-excluded regularization/Bergman/L²/OT/multiscale/positivity-loss work stays **deferred-by-user**.
