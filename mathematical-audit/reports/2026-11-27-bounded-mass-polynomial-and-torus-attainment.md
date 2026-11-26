# 2026-11-27 — bounded Hermitian mass polynomial and torus endpoint attainment

Main reviewed: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit parent: 8f8c3b47dcc2b70ae8778161754b947072c2018e. English notes only; no source, registry, permanent tag, site, build or CI changes.

## Scope and anchors

* §11.1, docs/sections/torsion-and-the-variation-of-mass/index.html, blob 9abec9685e33a1b40f9c0765381408eb52b325d3, physical mathematical lines 7–329. Whole direct review of nonexcluded arguments; the global regularization input in line 147 (5.32.1) and final smooth-to-bounded comparison reference in line 329 are recorded without reopening them. Lemmas 11.1.2–3 (15–51), binomial mass expansion (69–92), polarization (100–145), first variation and surface specialization (162–196), torus example (214–239), comparison (244–294) and background order bound (301–325) checked. Stokes signs, pure-bidegree closedness, degree n exactness, complexified local Hessian span, n=2 degree exception, determinant order, and strict margin after dividing by C all agree with the printed assumptions. No printed false statement identified. Historical partial review of this section, including the 2026-11-17 smooth interval finding, is retained, not re-counted.
* §11.3, docs/sections/gauduchon-metrics-and-linear-mass/index.html, blob 02d635e918120c4026c38d14119db9377eefe61f, lines 7–19, complete introductory exposition only. Conserved pairing follows by distributional duality, even for unbounded quasi-PSH u in L1. Duality and attainment claims are previews of later sections, not separately certified here.
* §12.34, docs/sections/a-gauduchon-variational-volume--current-tests-for-smooth-positivity/index.html, blob 4cf9e352c0d94c34ccaed0e41948a095fcfa8213, selected lines 7–65: Theorem 12.34.1 (source DC850E04, permanent FC99385C18B8) and Proposition 12.34.2 (source 39289E45, permanent 635FE1D11798). The Hahn–Banach proof correctly separates an affine space from an open cone without needing the affine space to be closed. Scaling the linear directions forces annihilation of dd^c C-infinity; scaling the positive cone gives positivity and the nonpositive theta pairing. Normalizing the nonzero positive functional gives the contradiction. Applying to theta-ah correctly computes the open interval of feasible bounds and the nef criterion. The determinant-measure conclusion is conditional on the variational infimum formula 12.7.2 and continuity 12.11.1: its estimate epsilon >= lambda(theta+epsilon h) D_mu(T) implies D_mu(T)=0; no unjustified inference about analytic support. Later flow proof not counted as reviewed. The older matrix status was legacy-unreconciled, not evidence of a historical first visit.
* Selected dependencies: §5.27.1 (source theorem permanent 8B1218AE4FDC; blob ddb2ac8d9de27a22152872e07e5e787d138a790e, lines 7–15); §5.28.1–2 (blob e2ba89b51376ba0296846221109c664a0c29b2c3, lines 7–46; permanent C87F0ACE9C76 and 3EDAB69A7289); §7.2.1–3 (blob 18bd2395f3b76941b2c677079c09eb6accc5a9cb, lines 7–75, in particular the recursive definition permanent 254CDCCCAB5E and product rule EDF346A35F76). §1.1 lines 105–130: X compact connected by default; dd^c=i/(2pi) partial bar-partial; no factorial in masses. The local Bedford–Taylor inputs are used as established statements, not transitively certified.

## POME-HERM-BOUNDED-MASS-POLYNOMIAL-001

Severity low; verified conditional shorter proof, not a source error. Theorem 11.1.5 (source D4902E5B, permanent 2B3316345A4A; lines 69–92) and Theorem 11.1.7 (source 5CD99CBA, permanent FB90FC741F25; lines 100–148).

Claim: if u is any bounded quasi-PSH function on X, not necessarily omega-PSH, the signed mixed products of §5.28 give the same identity as (11.1.6):

    int_X (omega+dd^c u)^n
      = int_X omega^n
        + sum_{k=1}^{n-1} binom(n,k)
          int_X u (dd^c u)^{k-1} wedge dd^c(omega^{n-k}).

Proof: on a small chart choose a smooth q so that p=u+q is PSH. Put A=dd^c p and Q=dd^c q. For j>=0 write C_j=(A-Q)^j using the finite local BT expansion. Each summand is a closed order-zero current (A powers are BT products, Q smooth closed). The overlap independence in 5.28.2 glues these to global closed signed order-zero currents C_j. C_0=1. By the local recursive definition 7.2.1, dd^c(p A^l)=A^{l+1}; wedging with smooth closed Q powers commutes with dd^c. Also dd^c(q C_j)=Q wedge C_j by the smooth Leibniz rule for a closed pure-bidegree current. Subtraction yields, locally and hence globally,

    dd^c(u C_j) = (A-Q) wedge C_j = C_{j+1}

where the middle expression means precisely the finite BT expansion, not an unrestricted multiplication of distributions. Bounded Borel u times C_j is well-defined and of order zero. Consequently current duality on the compact manifold gives, for k=1,...,n,

    int_X C_k wedge omega^{n-k}
      = <dd^c(u C_{k-1}), omega^{n-k}>
      = <u C_{k-1}, dd^c(omega^{n-k})>.

The k=n term vanishes because dd^c 1=0. Each integral is finite: coefficient measures are finite on compact X, u bounded and the test form smooth. Expanding (omega+dd^c u)^n by 5.28.2 proves the claim. There is no passage to a global approximating sequence and no hidden integration by parts involving products of two arbitrary measure coefficients.

In particular, the lower-power dd^c identities of Chiose imply the bounded mass invariance directly. Conversely bounded invariance implies smooth strict invariance as in the printed proof. Thus the original Step 3 is valid conditional on its cited input, but it can be replaced by the preceding direct argument. The excluded regularization theorem 5.32.1 is not proved, reviewed, certified or otherwise reopened. This replacement uses ordinary local BT current algebra only. Affected dependents: 11.1.7 bounded equivalence and the bounded comparison application at line 294 (still conditional on 14.25.3); it does not prove the unrelated equality between upper mass suprema of 13.14.15 in general non-invariant backgrounds.

## POME-HERM-TORUS-BOUNDED-ENDPOINT-ATTAINMENT-001

Severity low; verified conditional deduction, not a printed error. Example 11.1.12, source 028A9E19, permanent F336FEED9D87, lines 214–239, and the surface formula 11.1.10 (permanent 2C05FFD39C6D, lines 185–196). The prior 2026-11-17 audit proved the smooth strict open interval (2B,6B); it is not repeated as a new result.

Use the exact printed background on X=E^2: beta_j=i/(2pi) dz_j wedge dbar z_j, omega=beta_1+b(x_1) beta_2, b(x)=2+cos(2pi x), and B=int beta_1 wedge beta_2. For any bounded omega-PSH u let T=omega+dd^c u >=0. By the previous identity, or directly by the degree-two recursion,

    M(u)=int omega^2+2 int dd^c u wedge omega
        =2 int b(x_1) T wedge beta_2.

Indeed int dd^c u wedge beta_1=0 by duality, beta_2^2=0, and omega^2=2b beta_1 wedge beta_2. The positive measure T wedge beta_2 has total mass B since beta_2 is closed. Its pushforward under x_1:X->R/Z, divided by B, is a probability measure nu. Therefore

    M(u)=2B int b dnu ∈ [2B,6B].

Equality at the upper (lower) endpoint requires and is equivalent to nu being carried by x_1=0 (respectively x_1=1/2), because these are the unique maximizer/minimizer of b on the circle. There is no claim that every circle probability measure is realized by a bounded potential in higher-dimensional analogues.

In this example every point mass delta_a is realized explicitly. Let t be the fractional part of x_1-a and set u_a=2t(1-t), a periodic continuous Lipschitz function. Its distributional second derivative in the circle variable is -4 dx+4 delta_a: on (0,1) the second derivative is -4 and the derivative jumps from -2 to 2 at the seam. By the printed normalization dd^c f=(f''/4) beta_1, interpreted as a distribution in x_1 with Haar measure in the other coordinates,

    omega+dd^c u_a = delta_a beta_1 + b beta_2 >=0,

where delta_a beta_1 denotes the positive coefficient current supported on the real hypersurface x_1=a (not an integration current over a complex divisor). Locally u_a plus a smooth quadratic is PSH: its distributional complex Hessian is positive after that correction and it is continuous. Hence u_a is a bounded admissible potential with nu=delta_a. Its mass is 2B b(a). Varying a realizes the entire closed interval, including both endpoints; no limit of Monge–Ampere products is used.

Moreover for a fixed 0<=epsilon<1, requiring T>=epsilon omega is equivalent to w=u/(1-epsilon) being omega-PSH, since T=epsilon omega+(1-epsilon)(omega+dd^c w). On a surface M is affine in the potential by the degree-two mass formula, so its exact range under this current margin is

    [2B(1+epsilon), 2B(3-epsilon)].

Both endpoints are attained by (1-epsilon)u_a. At epsilon=1 the condition is dd^c u>=0, so compactness forces u constant and the interval collapses to 4B. In contrast to the earlier smooth strict interval, bounded potentials with a *positive current margin* can attain the new restricted endpoints (but not the original 2B or 6B). The formula also gives an exact loss of 2B epsilon from each unrestricted extreme. These assertions concern only this explicit surface background; no general mass attainment or continuity principle is inferred.

Affected dependents: concrete sharp mass/comparison examples of 11.1.12, 11.1.16–18; the latter remain correct. Any use of bounded endpoint attainment should state the bounded-current rather than smooth strict domain.

## Status and remaining gaps

Two new conditional deductions, one being a proposed shorter proof of a correct theorem. Zero newly confirmed printed errors or demonstrated proof gaps; zero complete upstream proof-chain certifications. The prior smooth range is not counted again. The local Bedford–Taylor construction, the general determinant duality/volume continuity inputs, and the rest of §12.34 have not been transitively certified. All Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain deferred-by-user, not resolved. No tests, builds, CI or publication. The current actual ToC in docs/chapters/index.html contains 747 distinct section numbers; compared with the existing matrix, all 747 were present, no duplicate.
