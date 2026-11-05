# Exact hyperplane deformation-to-normal-cone volume check

2026-11-05. Finding **POME-DNC-HYPERPLANE-CENTRAL-MASS-001**; severity **low**; status **verified conditional deduction**. Reviewed `main` `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

**Integrated source:** `docs/sections/divisorial-restricted-volumes/index.html`, blob `8eb1127568e77d6d045098361c366ceeb846b909`. Theorem 20.8.3 `transcendental-positive-cones:42C59BDB`, permanent tag `8DC7DAC31FB7`, physical HTML 64–79. Volume identities (20.8.4)–(20.8.7) lines 115–134; conservation (20.8.8) lines 136–143; total-volume difference 157–160; derivative 227–233.

## Complete independent computation in every dimension

Take n>=2, X=P^n, Y=P^(n-1) a hyperplane, alpha=aH, a>0, H^n=1. Blow up W=Bl_(Y×{0})(X×P^1), with classes A=p_1^*H, B=p_2^*[pt] and exceptional divisor E. Let beta=aA+bB-cE, with b>1 and sufficiently small 0<c<min(a,b-1). Both beta and beta-B are ample (small exceptional perturbations of ample product classes). Their analytic and restricted volumes therefore equal their top intersection numbers.

The center has normal bundle N=O_Y(1)⊕O_Y. In the **lines** convention E=P_Y(N), put h=H|Y and xi=c_1(O_E(1)). The exceptional normal bundle is O_E(-1), hence E|E=-xi, while xi^2+h xi=0 and int_E h^(n-1)xi=1. Consequently int_W A^nB=1, B^2=0, and for every 2<=j<=n+1 one has int_W A^(n+1-j)E^j=-1; any top intersection containing both B and E vanishes. The exceptional minus sign comes from (-xi)^(j-1) restricted to E and xi^j=(-h)^(j-1)xi.

Expanding:
```
Vol(beta)
 = (n+1)b a^n - Σ_(j=2)^(n+1) binom(n+1,j)a^(n+1-j)(-c)^j
 = (n+1)(b-c)a^n+a^(n+1)-(a-c)^(n+1)
 = (n+1)[(b-c)Vol(alpha)+∫_0^c Vol(alpha-t[Y])dt].
```
This verifies (20.8.4), including its n+1 factor and exceptional sign. Every noncentral fiber W_tau=P^n has beta|W_tau=aH, so its restricted volume is a^n, verifying (20.8.5). The strict central transform X'=P^n has B|X'=0, E|X'=H, hence beta|X'=(a-c)H and Vol_(W|X')(beta)=(a-c)^n: (20.8.6).

On E, beta|E=ah+c xi. The relation xi^2=-h xi gives
```
Vol_(W|E)(beta)
 = ∫_E(ah+c xi)^n
 = Σ_(j=1)^n binom(n,j)a^(n-j)c^j(-1)^(j-1)
 = a^n-(a-c)^n
 = n∫_0^c(a-t)^(n-1)dt
 = n∫_0^c Vol_(X|Y)(alpha-t[Y])dt.
```
Thus (20.8.7) holds, and adding its mass to (a-c)^n gives Vol(alpha)=a^n as required in (20.8.8). Replacing b by b-1 yields the exact base difference Vol(beta)-Vol(beta-B)=(n+1)a^n, as printed at line 160. Finally d/dt Vol(alpha+t[Y])|0=n a^(n-1)=n Vol_(X|Y)(alpha), verifying the model of Theorem 20.8.3. In n=2 the formulas reduce to Vol(beta)=3ba²-3ac²+c³, central masses (a-c)² and 2ac-c².

## Classification and boundary

The printed theorem is **not false**. This is a proof-complete intersection-number model and normalization test, **not** full verification of the general big-class theorem. Its general analytic Legendre-transform, envelope, contact-set, and non-pluripolar limiting steps (especially source lines 99–225) have not been verified. Any analytic proof relying on Demailly-type approximation is explicitly **deferred-by-user**, not resolved or reopened. Retain this all-n model as a regression test for the derivative and formulas (20.8.4)–(20.8.8), including their dependents. No source/body/registry/permanent-tag change is proposed.

Current exact ToC: 25 chapters, 747 numbered sections, zero complete mathematical-section certifications. No tests, builds, GitHub Actions, formal verification or website publication were run.