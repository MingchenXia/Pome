# Magnetic Landau levels: a sharp Riesz bound from midpoint convexity

**Audit date:** 2026-11-06. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (not modified).
**Integrated reading edition:** `docs/sections/magnetic-models-and-spectral-localization/index.html`;
blob `ee89de7d23cc96a8546c736ac7d068546b126f3a`, physical lines **5–7, 31–54, 59–70, 76–79, 85–109**.

**Stable provenance (source: `demailly-complex-geometry`):**
equation 2.24.4 source `4EE24E32`, permanent tag `6919A4A3FD8F` (lines 31–35);
equation 2.24.5 source `E2C26C03`, permanent `72E6618A3A3C` (lines 38–45);
Lemma 2.24.6 source `2FD17158`, permanent `0F14CB3D46F3` (lines 49–70);
bound 2.24.7 source `3A39A2CF`, permanent `DD3B970F19C7` (lines 49–54).
Proposition 2.24.8, permanent `C554004EA447`, lines 76–109, was checked solely for its direct use of the spectral densities and is **not** certified.

## Findings

**POME-MAGNETIC-MIDPOINT-RIESZ-CONVEX-ORDER-001** — severity **low**; status
**verified conditional deduction** (from the integrated explicitly normalized
spectral measures). The printed inequality (2.24.7) is correct; its Riesz-mean
constant can be made precise, uniformly in *all* magnetic field magnitudes,
without a field-dependent argument. No printed theorem is refuted.

For `b>0`, the integrated definition is
[
 mu_b=rac b{2pi}sum_{pgeq0}delta_{(2p+1)b},
 qquad mu_0=rac{dt}{4pi}quad	ext{on }[0,infty).
]
For any nonnegative convex function (arphi) for which the following integrals
are defined (in particular for nonnegative compactly supported convex
functions), the elementary midpoint inequality on
(I_p=[2pb,2(p+1)b]) gives
[
 rac b{2pi}arphi((2p+1)b)
  leq rac1{4pi}int_{I_p}arphi(t),dt.
]
Sum over `p`. Thus (intarphi,dmu_bleqintarphi,dmu_0).
For a field vector (mathbf b=(b_1,ldots,b_n)), apply this inequality one
coordinate at a time to
(G_E(t_1,ldots,t_n)=(E-t_1-cdots-t_n)_+).
This is nonnegative and convex in **each** coordinate. Tonelli's theorem,
or finitely many active Landau levels plus compactly supported free
integrals, justifies each replacement:
[
 r_{mathbf b}(E)
 =int G_E,dmu_{b_1}cdots dmu_{b_n}
  leq int G_E,dmu_0^{otimes n}
 =oxed{rac{(E_+)^{n+1}}{(4pi)^n(n+1)!}}. 	ag{A}
]
The last equality follows from the convolution density
(mu_0^{*n}(dt)=t^{n-1}dt/((4pi)^n(n-1)!)).
At (mathbf b=0), (A) is equality for every `E`; hence its coefficient
is **optimal** uniformly in (mathbf b). Note that this proves only a
sharpening of the **Riesz** bound in (2.24.7), not its counting-function
bound, and depends on the correct spectral normalization in (2.24.4).

In one magnetic pair the discrepancy is **exact**. For `E>=0`, `b>0`,
write (x=E/(2b)) and (m=lfloor x+1/2floor) (the upper nearest integer
at a tie). The contributing levels have indices `0,...,m-1`, where
an endpoint term can be zero. Consequently
[
 r_b(E)=rac{b}{2pi}sum_{p=0}^{m-1}(E-(2p+1)b)
       =rac{b}{2pi}(mE-bm^2)
       =rac{E^2}{8pi}-rac{b^2}{2pi}(x-m)^2 .
]
As (m) is a nearest nonnegative integer to (xge0),
[
 oxed{0le r_0(E)-r_b(E)
    =rac{b^2}{2pi}operatorname{dist}
        left(rac{E}{2b},mathbb Z_{ge0}ight)^2
    lerac{b^2}{8pi}}. 	ag{B}
]
For `E<=0`, both means vanish. The endpoint constant in (B) is attained
at every odd Landau energy (E=(2k+1)b), and gives a uniform-in-`E`
`O(b^2)` zero-field limit for the one-pair Riesz mean.
All factors of (2) and (pi) are fixed by the *printed*
(mu_b,mu_0), not a convention imported from another source.

**POME-MAGNETIC-COUNTING-FREE-BOUND-FAIL-001** — severity **low**;
status **verified conditional deduction** (counterexample to an *unprinted*
over-strengthening, **not** to any assertion in Pome). It is incorrect to
replace the counting bound in (2.24.7) by the free-field coefficient.
For `n=1` and (E=(1+epsilon)b), (0<epsilon<1),
[
 
u_b(E)=rac b{2pi}
  > rac{(1+epsilon)b}{4pi}=
u_0(E).
]
The reason is that (tmapsto{f1}_{[0,E)}(t)) is not convex; the preceding
midpoint argument applies to the integrated Riesz kernel ((E-t)_+), not
to a sharp spectral cutoff. More precisely,
(r_b'(E^-)=
u_b(E)), whereas
(r_b'(E^+)=mu_b([0,E])).
The derivatives differ by the Landau atom at (E), consistent with
the strict interval used in equation 2.24.5.

## Audit consequences and limits

The stronger coefficient in (A) is suitable as a **proposed optional
mathematical clarification** adjacent to Lemma 2.24.6, but no edits to
the theorem, canonical registry, or published reading edition are
authorized by this audit. Keep `C_n` for (
u_{mathbf b}):
the free-field coefficient is false even for one pair.
The direct dependent Proposition 2.24.8 uses both (r_{mathbf b})
and (
u_{mathbf b}) in its Dirichlet localization error estimate
(lines 89–109); (A) may improve the *Riesz* term, but does not improve
the counting term by the same argument. Further dependent references
elsewhere in the repository have **not** been exhaustively searched.

The spectral-density identification and oscillator completeness in
Lemma 2.24.6 were read but not independently reconstructed in this
increment; the deductions above are complete once equations 2.24.4–5
are accepted. The general Dirichlet spectral localization proof,
the `Q`-form lemma, boundary-layer estimates and transitive
dependencies remain **unverified**. No whole section is certified.
This work does not touch the owner's excluded Demailly
approximation/regularization or Bergman, weighted-`L^2`,
Ohsawa–Takegoshi, multiscale-atlas, positivity-loss proof programme.

**Reproducible limited arithmetic check:** independently evaluated
the finite-level sum and identity (B), after multiplication by (pi),
at 18 exact rational pairs ((b,E)) with no floating-point arithmetic.
This is a sanity check, not a test or verification of the general
theorem, the build, CI or the published site.
