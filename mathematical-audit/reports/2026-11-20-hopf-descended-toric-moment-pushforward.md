# 20 November 2026 — §21.14 direct reading: Hopf-fiber toric curvature and exact moment measure

**Finding:** \`POME-HOPF-DESCENDED-TORIC-MOMENT-PUSHFORWARD-001\`. **Status:** verified conditional deduction. **Severity:** low. This is **not a false printed theorem**, not an independent repair, and not a certificate for all upstream proofs. The formula concerns *arbitrary smooth, strictly positive torus-invariant base curvatures*, unlike the earlier \`POME-TORIC-GUILLEMIN-MOMENT-STRATA-DH-001\` (specific Guillemin reference on a compact toric variety), and unlike \`POME-HOPF-TORIC-SUBGRAD-LOCALIZATION-001\` (quantitative inverse localization).

## Fixed source, anchors and dependency scope

- Production \`main\`: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- Complete integrated §21.14 mathematical reading: \`docs/sections/hopf-fibrations-and-toric-potentials/index.html\`, blob \`0e83de13efbd70dfddc64a8eed40baed2d4359c5\`, physical mathematical lines **7–201**.
- Hopf fiber form conventions and normalization: §21.14 lines **16–19**, permanent section tag \`23660BEC4C1F\`; selected actual upstream \`docs/sections/holomorphic-sections-and-hermitian-mass/index.html\`, blob \`5f00431e7986d899dc833c89175686b75f09371d\`, §19.8.12 lines **291–320**, permanent subsection \`82379C382500\`. This is a selected input check, not a whole §19.8 review.
- Theorem **21.14.2**, source \`non-kahler-pluripotential-theory:6F65FF2F\`, permanent \`DCED1F266D4F\`, lines **23–44**, reviewed as a fiber-Fubini and homogeneous-section argument only. This does **not** reopen Demailly approximation or the user-excluded dedicated Bergman/L²/OT proof-completion programme; no new Bergman estimates are attempted.
- Theorem **21.14.4**, source \`non-kahler-pluripotential-theory:8A7CCCFA\`, permanent \`94243AEE3360\`, statement lines **62–74**, integrated proof **79–107**.
- Equation **21.14.5**, source \`non-kahler-pluripotential-theory:59DC9EFD\`, permanent \`D50C510DA3A9\`, lines **114–139**.
- Proposition **21.14.8**, source \`non-kahler-pluripotential-theory:7515BE71\`, permanent \`F23340CADBE0\`, statement **166–170**, proof **175–201**.
- The general continuous base equation in §14.25.2 and the extended non-pluripolar construction in §13.14.3 remain **conditional external-to-this-run internal dependencies**, not freshly transitively certified. Their proof programmes were not reopened.

## Exact strengthened measure identity (smooth positive case)

Let \(n\ge2\), \(m=n-1\), \(X_n=(\mathbf C^n\setminus\{0\})/\langle z\mapsto e^{-1}z\rangle\), and let \(\pi:X_n\to\mathbf P^m\) be projectivization. Use exactly the source convention
\[
\alpha=\pi^*\sigma,\qquad \zeta=ds\wedge d^cs,\qquad
\zeta^2=0,\qquad \int_{\pi^{-1}(y)}\zeta=2,\qquad
dd^c=\frac{i}{2\pi}\partial\bar\partial.
\]
Take **any real \(k>0\)** and any smooth torus-invariant \(v\) with
\(B=k\sigma+dd^cv>0\) on \(\mathbf P^m\). Put
\[
\omega_k=k\alpha+\zeta,\quad u=\pi^*v,\quad
\eta=\omega_k+dd^cu=\pi^*B+\zeta>0.
\]
The standard case in Theorem 21.14.4 is \(k=1\) and \(\omega_1=\omega\).

On the dense projective torus \(z_n\neq0\), \(z_i\neq0\), set \(w_i=z_i/z_n\),
\(x_i=\log|w_i|^2\), \(\theta_i=\arg w_i\) for \(i=1,\dots,m\), and
\[
f(x)=k\log(1+e^{x_1}+\cdots+e^{x_m})+
v([e^{x_1/2}:\cdots:e^{x_m/2}:1]).
\]
Let \(p_i=\partial f/\partial x_i\), and let
\[
\Delta_k^\circ=\{(p_1,\dots,p_m):p_i>0,\ \sum_{i=1}^m p_i<k\}.
\]
Proposition 21.14.8, including its proved coercivity and strict transverse
convexity, says \(p=\nabla f:\mathbf R^m\to\Delta_k^\circ\) is bijective.
Since \(D^2f>0\), the inverse function theorem upgrades this to a global
smooth diffeomorphism. Define \(\mu_k\) by \(p\) on the dense projective
torus; its values on the coordinate divisors (of zero smooth curvature
volume) do not affect the measure identity.

**Exact base pushforward:**
\[
\boxed{(\mu_k)_*\frac{B^m}{m!}
=\mathbf1_{\Delta_k}\,dp_1\cdots dp_m.} \tag{1}
\]
**Exact Hopf pushforward:**
\[
\boxed{(\mu_k\circ\pi)_*(\eta^n)
=2n\,m!\,\mathbf1_{\Delta_k}\,dp_1\cdots dp_m.} \tag{2}
\]
The measure \(dp\) is the ordinary \(m\)-coordinate Lebesgue measure in the
affine hyperplane \(\sum_{i=1}^n p_i=k\), **not** the induced
\(\mathbf R^n\) Euclidean hypersurface measure (which would introduce a
factor \(\sqrt n\)). In particular,
\[
\boxed{\int_{\mathbf P^m}B^m=k^m,\qquad
\int_{X_n}\eta^n=2n\,k^m.} \tag{3}
\]
For \(k=1\) this recovers \(2n\) in Theorem 21.14.4 but (2) gives the
**entire moment distribution**, not merely its total mass.

### Direct proof and all factors

Because \(dd^c=(i/2\pi)\partial\bar\partial\), and
\(dw_i/w_i=\tfrac12dx_i+i\,d\theta_i\), one has
\[
B=dd^cf
=\frac1{2\pi}\sum_{i,j=1}^m
f_{ij}\,dx_i\wedge d\theta_j
\quad\text{on the dense torus}.
\]
The orientation implicit in the positive top power gives
\[
\frac{B^m}{m!}
=\det(D^2f)\,dx_1\cdots dx_m
\,\frac{d\theta_1\cdots d\theta_m}{(2\pi)^m}.
\]
Integrate the angles, then use the **global diffeomorphism**
\(p=\nabla f\) and the real Jacobian \(dp=\det D^2f\,dx\).
The coordinate divisor has zero mass for the smooth form \(B^m\), proving
(1), including measure normalization and no boundary atoms.

The identity \(\zeta^2=0\), \(\dim_{\mathbf C}\mathbf P^m=m\), and
\(\pi^*B^{m+1}=0\) imply
\[
\eta^n=(\pi^*B+\zeta)^n
=n\,\pi^*(B^m)\wedge\zeta.
\]
For every nonnegative Borel \(\varphi\) on \(\Delta_k\), the *given* fiber
integral of \(\zeta\) equals \(2\); hence
\[
\int_{X_n}\varphi(\mu_k\circ\pi)\eta^n
=2n\int_{\mathbf P^m}\varphi(\mu_k)B^m
=2n\,m!\int_{\Delta_k}\varphi(p)\,dp.
\]
This proves (2). Since the affine simplex has volume \(k^m/m!\), (3)
follows. Check: for \(n=2\), the Hopf density is \(4\,dp\) on an interval
of length \(k\); for \(n=3\), it is \(12\,dp_1dp_2\) on a triangle of area
\(k^2/2\), giving \(6k^2\). These are arithmetic cross-checks performed
in this proof, not claimed software tests.

### Applicability and proposed use

(1)–(2) require **smooth strictly positive toric base curvature**.
They do not assert a measure-preserving diffeomorphism for a singular
potential, a non-strict semipositive metric, or an arbitrary non-toric
metric. An optional audit-only-to-production proposed remark after
Proposition 21.14.8 could state (1)–(2), with the chosen affine-Lebesgue
normalization and proof above. Do **not** modify source bodies,
canonicalization, tags, or publication automatically.

**Affected dependents:** interpretation of §21.14.4 and §21.14.8;
comparison with the mass bound for fiberwise constant potentials and the
unbounded fiber-varying mass constructions in §23.1; comparison to the
specific Guillemin reference pushforward in §21.10. No original theorem
is invalidated.

## Direct mathematical checks across §21.14

- **Lines 7–19:** verified compatibility of \(\omega=\alpha+\zeta\), its
  Gauduchon probability volume \(dV=\omega^n/(2n)=\tfrac12\alpha^m\zeta\),
  and fiber mass \(2\), against the actual §19.8.12 source.
- **Lines 21–44:** checked the actual homogeneous-section correspondence,
  base-pullback weights, Fubini equality for nonnegative (possibly
  nonintegrable) section norms, and the orthonormal-basis consequence.
  Underlying separate holomorphic Hartogs and multiplier-ideal results
  are reused, not independently re-proved. No Bergman approximation
  analysis is attempted.
- **Lines 47–107:** checked the positivity equivalence using
  \(\pi_*[(\omega+dd^cu)\wedge\zeta]=2(\sigma+dd^cv)\),
  the bounded Bedford–Taylor expansion, truncation indicators and
  increasing extended-measure limit, and the factor \(2n\). This does
  not certify all upstream bounded-BT or extended-MA results.
- **Lines 111–139:** verified the descended \(L^p\) base equation has
  factor \(c/(2n)\), that integrating gives
  \(c=2n/\int f\sigma^m\), and that uniqueness/existence is conditional
  on the cited base Monge–Ampère theorems. No full nonlinear PDE proof
  is claimed.
- **Lines 141–201:** checked \(F(x+t\mathbf1)=F(x)+kt\),
  the Hessian congruence, \(\sum F_i=k\), nonnegative component slopes
  via one-sided convexity, coercivity on the quotient \(H\), and the
  strict-convexity uniqueness. The older §21.14 subgradient inverse
  *localization* result was **not** reclassified as new.
- **Finding separation:** no new confirmed false printed statement,
  genuine duplication, or independently certified complete upstream
  chain was found in this reading. A conditional strengthened identity
  is not a repair of an incorrect theorem.

## Coverage, exclusions, and reproducibility

- **New direct coverage:** one current **whole §21.14** reading, physical
  mathematical lines **7–201**; one **selected upstream** §19.8.12
  lines **291–320**. Already logged historic partial §21.14 and the
  existing §21.10 result remain intact; no historical first-visit
  increment is asserted.
- **Complete transitive proof-chain certificates:** **zero**.
- **Deferred-by-user:** all Demailly approximation/regularization and
  its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas and
  positivity-loss proof-completion programmes; no deferred item is
  marked resolved.
- **Not run:** build, tests, CI, website publication, source edits or
  automatic canonicalization. This report is an audit Markdown finding
  only.
