# Product-pole smooth Monge–Ampère limits at competing scales

Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Date: 2026-11-26.
Finding **POME-BT-PRODUCT-POLE-COMPETING-SCALES-001**, low / verified deduction (not a printed error). This is an elementary local counterexample calculation about the scope of unbounded Bedford–Taylor products, not the excluded Demailly approximation or its proof programme.

## Exact source and coverage

- docs/sections/unbounded-potentials-and-dependence-on-regularization/index.html, blob 431e66dcee4efdf3c4aac592aaee1490156da2b9. Entire mathematical lines 7–145. Example 7.23.1, source 6E737739, permanent 20D8C7C9B243, lines 8–41; Proposition 7.23.2, source 80EFAB5F, permanent EC436652E435, lines 46–133; Example 7.23.3, source 8EC23CC0, permanent C89C030AFB89, lines 138–145. 
- docs/sections/normal-spaces-and-tube-continuation/index.html, blob 01a93b78d1e2085f407db1f6f073445e3738383b, §9.37 tag ACBDBFF87246, line 5 heading and links only.
- docs/sections/analytic-tensor-products-and-proper-direct-images/index.html, blob 58b0ad0bb555f9f4cc99b3f7562474e8d9325659, §9.40 tag 00CF0B1E94F5, line 5 heading and links only.
- Both heading-only sections have no mathematical body to certify. Earlier historical coverage is unreconciled. The main section is marked direct conditional, not transitive.

## Result

For n >= 2, let F(z)=product z_i and let positive decreasing sequences e_j,d_j tend to zero. Put
\[
a_j=\log(|F|^2+d_j),\quad b_j=\sum_i\log(|z_i|^2+e_j),
\quad u_j=(1-t)a_j+t b_j,\quad 0\le t\le1.
\]
These are smooth PSH decreasing to the same u=sum log|z_i|² (including the pole set; endpoints interpreted separately). Write q_j=d_j/e_j^{n-1}. If q_j tends to lambda in [0,+infty], the vague top-product limit is
\[
n!t^n\delta_0+n!(1-t)t^{n-1}\sum_{k=1}^n \iota_{k*}\sigma_\lambda.
\]
Here iota_k embeds C as the kth coordinate axis. For lambda=0, sigma_0=delta_0; for lambda=+infty, sigma_infty=0 (vague mass escape); for finite positive lambda, sigma_lambda is the law of sqrt(lambda) W_0 / product_{i=1}^{n-1}|W_i|, where the W_i are independent with probability density 1/[pi(1+|w|²)^2] with respect to planar area. In particular this axis measure is a nonatomic probability for positive finite lambda. In the finite cases the convergence is also narrow.

### Proof

Let A_j=dd^c a_j and B_j=dd^c b_j. The rank-one calculation of lines 22–28 gives A_j²=0. The coordinate forms in B_j square to zero. Thus
\[
(dd^c u_j)^n=t^n B_j^n+n(1-t)t^{n-1} A_j\wedge B_j^{n-1}.
\]
With the section's dd^c normalization, write mu_s=dd^c log(|z|²+s), a probability density s/[pi(|z|²+s)^2]. Then B_j^n=n! tensor_i mu_{e_j}, converging narrowly to n! delta_0. The mixed term is (n-1)! times a sum over missing coordinates k. In a summand the n-1 other coordinates have independent laws mu_{e_j}; since their forms already occupy those complex directions, only the kth diagonal Hessian entry of A_j contributes. Off the null set where one of the other coordinates is zero, fixing those coordinates gives the conditional law mu_{d_j/product_{i!=k}|z_i|²} in coordinate k. This proves the exact mixed-measure representation by Fubini, with no Jacobian omitted. The exceptional coordinate-zero set is Lebesgue-null for every j; the smooth integrands carry no mass there.

Couple all j using independent W_i with law mu_1. The coordinates other than k are sqrt(e_j)W_i, and the remaining coordinate is sqrt(q_j)W_0/product_{i!=k}|W_i|. Almost surely all W_i are finite and nonzero. If lambda is finite, the random vectors converge almost surely to the described axis vector, and dominated convergence for bounded continuous tests gives narrow convergence. If lambda is infinite, their norm tends to infinity almost surely; dominated convergence for compactly supported tests gives vague convergence to zero. The coefficients above follow from the binomial expansion and (n-1)! factor. This proof needs neither a monotone convergence theorem for unbounded Monge–Ampère products nor regularization of general potentials.

For example choose e_j=1/j and d_j=e_j^n. Then lambda=0, and the atomic mass is
\[
n!\,[t^n+n(1-t)t^{n-1}].
\]
The bracket runs continuously and monotonically from zero to one (derivative n(n-1)t^{n-2}(1-t)). Hence **every multiple c delta_0 with 0<=c<=n!** arises as a limit of smooth decreasing approximations of this fixed u. At critical scaling d_j=e_j^{n-1}, interior t gives positive diffuse axis mass as well as the atom, whereas at supercritical ratio q_j→infty the mixed mass escapes to infinity. For t in (0,1) in this last case the limit cannot be narrow: each total mass equals n![t^n+n(1-t)t^{n-1}], strictly larger than the limiting mass n!t^n. These are explicit counterexamples to uniqueness even within smooth decreasing approximants and distinguish vague from narrow convergence. No classification of all possible limits is asserted.

## Rest of section: proof checks

Example 7.23.1: verified the scalar Hessian rank, one-dimensional probability normalization and n! coefficient. Proposition 7.23.2: differentiating L=-log|y| gives L_y=-1/(2y) and L_{y bar y}=0 away from y=0, yielding exactly the matrix in lines 61–69 and determinant (1-2|x|²)/(16|y|² L). Its normalized Hessian has minimum eigenvalue at least 1-|x|²-|x|>1/2 on the given disk. The squared weighted gradient is (|x|²+(1-|x|²)²)sqrt(L), so the printed gradient upper bound holds. Adding |z'|²-2 preserves the gradient bound and U<-1. For f_j, both derivative signs are positive and the printed 9κ bound implies H_{U-f_j(U)}>=H_U/2. The two extensions across y=0 use the removable-set theorem for PSH locally upper bounded off an analytic hypersurface (an internal input, not re-proved here). The resulting exact cone decomposition, positivity and multilinearity imply the comparison of measures on the fixed compact K; Fatou off y=0 and the divergent integral ∫dr/(r log(1/r)) give contradiction. In fact the same proof excludes any positive scalar diagonal extension monotone under addition of PSH functions, not only multilinear extensions; this is an immediate observation, not a separate finding. Example 7.23.3: dd^c log|z| has smooth Hessian rank n-1 away from 0, strict truncation discards the boundary sphere, and the classical isolated-point mass 2^{-n} uses the earlier radial isolated-point theorem (§7.18); not independently certified in this run. The local bounded BT product and its locality remain internal inputs.

No new printed errors or demonstrated proof gaps. Proposed addition: append the competing-scale formula to Example 7.23.1; no change to the statement or permanent tags. Affected downstream scope: examples of unbounded products, the classical vs non-pluripolar distinction, and convergence terminology. No downstream theorem is refuted. Ledger search for section/pole/coordinate-axis terms found no matching earlier competing-scale result; not a claim of exhaustive historical deduplication. No tests, builds, CI, source or website changes. All user-excluded programmes remain deferred-by-user; no approximation theorem for general potentials was pursued.
