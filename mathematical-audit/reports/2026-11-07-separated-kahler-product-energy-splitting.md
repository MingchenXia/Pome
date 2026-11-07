# Exact Aubin–Mabuchi energy splitting for separated Kähler factors

**Finding:** `POME-ENERGY-PRODUCT-TENSOR-SPLITTING-001`  
**Review date:** 2026-11-07  
**Classification:** low / **verified conditional deduction**; the printed statements inspected below are **not** refuted.  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Scope:** a new, narrowly delimited consequence of the integrated reading-edition statements in §§13.6 and 17.3, not a certification of either section or of their transitive dependencies.

## Exact integrated anchors

- `docs/sections/non-pluripolar-products--fiber-integration-and-modifications/index.html`, main blob `9954a43d90d5cae8ef744968636d7a5912348fce`: Corollary 13.6.1, original `foundations-of-pluripotential-theory:BAE2819F`, permanent `BEC54934FC2C`, **physical lines 10–30** (weighted fiber identity); Proposition 13.6.3, original `foundations-of-pluripotential-theory:3F4A3A88`, permanent `0811FFDF15B7`, **physical lines 35–55** (modification naturality, read for scope only).
- `docs/sections/relative-energy-and-perron-segments--relative-monge-ampere-energy/index.html`, main blob `16fdcc4c6a6f0cc75e69ba267bd7da2b2d7922a1`: Definition 17.3.2, original `foundations-of-pluripotential-theory:582D55DC`, permanent `240EF1DE5889`, **physical lines 31–38**, including formula 17.3.3, permanent `F19AAFA93177`; Proposition 17.3.4, original `foundations-of-pluripotential-theory:44639882`, permanent `9086ABF36774`, **physical lines 41–53**, with first-variation formula 17.3.5, permanent `46190A7C1B2F`; its polynomial/BT integration-by-parts proof, **physical lines 55–90**.
- The current ToC, `docs/index.html`, main blob `68e66f6b30cdaaee887dc3c91580cdd0a38d8801`, locates §§13.6 and 17.3 in chapters 13 and 17 respectively.

The only substantive inputs used are bounded Bedford–Taylor multilinearity and its compact Kähler mass invariance, plus the stated internal energy first-variation formula. They are **dependencies**, not re-proved from first principles here; no Demailly approximation/regularization or associated Bergman, weighted `L^2`, Ohsawa–Takegoshi, multiscale, or positivity-loss argument is used or examined.

## The precise new deduction

Let \((X,\theta)\) and \((Z,\gamma)\) be compact Kähler manifolds of complex dimensions \(r,m\geq1\). Put \(N=r+m\),
\[
  V_X=\int_X\theta^r>0,\qquad V_Z=\int_Z\gamma^m>0,\qquad
  \Theta=p_X^*\theta+p_Z^*\gamma.
\]
For **bounded** \(\theta\)-psh functions \(u\) on \(X\) and **bounded** \(\gamma\)-psh functions \(v\) on \(Z\), let
\(U=p_X^*u+p_Z^*v\), a bounded \(\Theta\)-psh function. Use the **unnormalized** relative Aubin–Mabuchi energy \(E_\theta^0\) of Definition 17.3.2 with reference \(0\) (and similarly for \(\gamma,\Theta\)). All three zero references are models since the backgrounds are Kähler.

Then the exact identity, with **no asymptotic error**, is
\[
  \boxed{\;
  E_\Theta^0(U)
    = {N\choose r}\bigl(V_Z E_\theta^0(u)+V_X E_\gamma^0(v)\bigr).
  \;}
  \tag{A}
\]
No normalization \(\sup u=\sup v=0\) is required. The binomial coefficient is essential: the top-degree volume on \(X\times Z\) is \({N\choose r}V_XV_Z\), not \(V_XV_Z\).

More generally, for any two pairs \((u_0,v_0)\), \((u_1,v_1)\) with each component bounded and psh with respect to its fixed Kähler background, putting \(U_i=p_X^*u_i+p_Z^*v_i\) gives
\[
 E_\Theta^0(U_1)-E_\Theta^0(U_0)
 ={N\choose r}\left[
 V_Z\bigl(E_\theta^0(u_1)-E_\theta^0(u_0)\bigr)
 +V_X\bigl(E_\gamma^0(v_1)-E_\gamma^0(v_0)\bigr)
 \right]. \tag{B}
\]

### Proof, including Bedford–Taylor and normalization checks

For \(s,t\in[0,1]\), let \(\theta_{su}=\theta+s\,dd^cu\), \(\gamma_{tv}=\gamma+t\,dd^cv\), and \(U_{s,t}=s\,p_X^*u+t\,p_Z^*v\). Local boundedness gives the ordinary Bedford–Taylor products; their defining multilinearity and the independent-variable product charts yield
\[
  \bigl(\Theta+dd^c U_{s,t}\bigr)^N
   =\sum_{k=0}^{N}{N\choose k}p_X^*\theta_{su}^{\,k}
                         \wedge p_Z^*\gamma_{tv}^{\,N-k}
   ={N\choose r}\,p_X^*\theta_{su}^{\,r}\wedge p_Z^*\gamma_{tv}^{\,m}. \tag{C}
\]
Terms with \(k>r\) or \(N-k>m\) vanish **for bidegree reasons**, not through a limit/interchange claim. The remaining product measure is a genuine product measure, as can be verified on rectangular compactly supported tests via the bounded local fiber formula underlying Corollary 13.6.1, then by a monotone class argument. All local potentials are bounded, so no pole-set cutoffs or arbitrary reordering of truncation limits is needed.

Each factor has constant top mass:
\[
 \int_X\theta_{su}^r=V_X,\qquad \int_Z\gamma_{tv}^m=V_Z. \tag{D}
\]
This is the standard internal bounded BT compact Kähler mass assertion (equivalently, the bounded-same-singularity special case of the mass invariance used in the current reading edition). We do **not** invoke any new smooth approximation argument.

Hold \(t\) fixed and differentiate the **two-parameter** energy using the first-variation identity of Proposition 17.3.4 in the \(X\)-direction. Equations (C)–(D), positivity and product Fubini give
\[
 \frac{\partial}{\partial s} E_\Theta^0(U_{s,t})
 ={N\choose r} V_Z\int_X u\,\theta_{su}^r
 ={N\choose r}V_Z \frac{d}{ds}E_\theta^0(su).
 \tag{E}
\]
Similarly,
\[
 \frac{\partial}{\partial t} E_\Theta^0(U_{s,t})
 ={N\choose r}V_X \frac{d}{dt}E_\gamma^0(tv). \tag{F}
\]
There are **no mixed derivatives**: for bounded psh functions the energies in these affine parameters are polynomials obtained from finite mixed BT measures, and (E) and (F) imply \(\partial_s\partial_t E_\Theta^0(U_{s,t})=0\). Since all three reference energies vanish at the zero potential, integration along the two edges of the unit square proves (A), and subtraction proves (B).

A completely explicit scalar check guards the normalization: put \(u=c\), \(v=d\) constant. Formula (A) gives \({N\choose r} V_XV_Z(c+d)\), exactly the expected constant-shift energy \((c+d)\int_{X\times Z}\Theta^N\). In complex dimension \(r=m=1\), the factor is **2**, not 1.

### Why the scope matters

1. Formula (C) assumes the **separated sum** \(U(x,z)=u(x)+v(z)\). Arbitrary \(W\in\mathrm{PSH}(X\times Z,\Theta)\) with genuine mixed \((x,z)\) curvature has additional terms; its energy need not split.
2. The proof assumes **closed Kähler backgrounds**, hence (D). The general nonclosed Hermitian mass variation analyzed elsewhere in the audit rules out extending (A) to arbitrary Hermitian backgrounds by the same argument.
3. The proof is restricted to **bounded** potentials. No assertion is made for arbitrary singular type envelopes, relative finite-energy completions, or zero-volume factors; further work would need carefully justified non-pluripolar product/tail passages. In particular, (A) does **not** independently certify Corollary 13.6.1 or Proposition 17.3.4.
4. This is a verified conditional **consequence** of correct printed statements, **not** a confirmed error, not a repaired missing proof, and not a full section certification.

**Affected dependent statements to check subsequently:** product examples or separable rays invoking the relative energy of §§17.3–17.9, fiber-integrated constructions in §13.6, and products in §22.1 where normalizations may differ. No production replacement is required. For reuse, state (A) with the Kähler/bounded/separated hypotheses and the \({N\choose r}\) coefficient.

**Coverage and execution:** new selected proof-level cross-check of §17.3.2/.4 and the bounded-fiber normalization of §13.6.1; §13.6.3 was compared for scope, not re-proved. Both sections already had partial audit coverage; **zero new first-visit sections and zero whole-section certifications**. No tests, builds, CI, browser checks, formalization or publication were run for this mathematical deduction. Current inventory remains 25 chapters, 747 numbered sections, 0 fully certified mathematical sections. Older findings remain at their prior statuses, and the user-excluded Demailly programme remains **deferred-by-user**, not resolved.
