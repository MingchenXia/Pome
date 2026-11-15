# Multipair magnetic Riesz means: a monotone zero-field envelope and a sharp two-pair defect

**Finding:** POME-MAGNETIC-MULTIPAIR-MIDPOINT-DEFECT-001  
**Classification:** low / verified conditional deduction. No printed theorem refuted; not a complete certification of the surrounding section or of its downstream spectral applications.  
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272 (2026-11-15).  
**Integrated reading edition:** docs/sections/magnetic-models-and-spectral-localization/index.html, main blob ee89de7d23cc96a8546c736ac7d068546b126f3a.

## Precise source anchors

- Formula **2.24.4**, defining the one-pair positive measures, integrated physical lines **31–35**, source label **demailly-complex-geometry-4EE24E32**, permanent tag **6919A4A3FD8F**.
- Formula **2.24.5**, defining convolution measures, distribution functions and Riesz means, lines **38–45**, source label **demailly-complex-geometry-E2C26C03**, permanent tag **72E6618A3A3C**.
- Lemma **2.24.6**, constant-field magnetic spectral measure and continuity, lines **49–71**, source label **demailly-complex-geometry-2FD17158**, permanent tag **0F14CB3D46F3**. Its uniform local mass estimate **(2.24.7)** occupies lines **50–54**, permanent tag **DD3B970F19C7**.
- Proposition **2.24.8**, Dirichlet first Riesz-mean asymptotics, physical lines **76–110**, source label **demailly-complex-geometry-7DBC83A8**, permanent tag **C554004EA447**. Its localization inequality **(2.24.10)** occupies lines **94–109**, permanent tag **B6FBF3F18EA3**.
- Prior audit **POME-LANDAU-RIESZ-MIDPOINT-001**, report 2026-10-27-magnetic-riesz-rates-and-nuclear-banach-rigidity.md, has already established the *single-pair* exact midpoint defect. It is a reused input, **not** a newly discovered finding or rerun test.

## New mathematical conclusion

Let \(n\ge2\), \(\mathbf b=(b_1,\ldots,b_n)\in[0,\infty)^n\), and use *exactly* the normalizations of (2.24.4)–(2.24.5):

\[
\mu_b=\frac{b}{2\pi}\sum_{p\ge0}\delta_{(2p+1)b}
\quad(b>0),\qquad
d\mu_0(t)=\frac{\mathbf 1_{t\ge0}\,dt}{4\pi},
\]
\[
r_{\mathbf b}(E)=\int_{\sum t_j\le E}(E-\sum t_j)
\,d\mu_{b_1}(t_1)\cdots d\mu_{b_n}(t_n).
\]

Then, **for every** \(E\ge0\) and every nonnegative field vector, including field-rank changes and unbounded \(b_j\),

\[
\boxed{\quad
0\le r_{\mathbf0}(E)-r_{\mathbf b}(E)
\le \frac{E^{\,n-1}}{8\pi(2\pi)^{n-1}}
\sum_{j=1}^n b_j^2,\qquad
r_{\mathbf0}(E)=\frac{E^{n+1}}{(4\pi)^n(n+1)!}.
\quad}
\]

Both Riesz means vanish for \(E\le0\). This gives a *monotone zero-field upper envelope* and an explicit global quadratic upper modulus that are not asserted by the printed qualitative continuity lemma. The coefficient in this **general** upper bound is not claimed optimal.

In the new two-pair case \(\mathbf b=(b,0)\), \(b>0\), define for \(E\ge0\)
\(x=E/(2b)\), \(N=\max\{0,\lceil x-\tfrac12\rceil\}\), and \(\delta=N-x\in[-1/2,1/2]\). There is the **exact oscillatory identity**

\[
\boxed{\quad
r_{(0,0)}(E)-r_{(b,0)}(E)
=\frac{b^2E}{96\pi^2}
+\frac{b^3}{48\pi^2}(\delta-4\delta^3).
\quad}
\]

Consequently,

\[
\left|
r_{(0,0)}(E)-r_{(b,0)}(E)-\frac{b^2E}{96\pi^2}
\right|
\le\frac{b^3}{144\sqrt3\,\pi^2}.
\]

For **each fixed \(E>0\)** the normalized defect therefore satisfies

\[
\lim_{b\downarrow0}
\frac{r_{(0,0)}(E)-r_{(b,0)}(E)}{b^2}
=\frac{E}{96\pi^2}>0.
\]

Thus the global quadratic power in the magnetic field is **sharp already in complex dimension two** (even when only one magnetic pair is nonzero); neither the general numerical coefficient nor a higher-rank optimal coefficient is asserted.

## Complete proof of the general comparison

Partition \([0,\infty)\) into intervals \(I_p=[2pb,2(p+1)b]\), \(b>0\). For any convex nonnegative \(h\) with finite integrals, Jensen's inequality on each cell gives

\[
\frac1{4\pi}\int_{I_p}h(t)\,dt
\ge \frac{b}{2\pi}\,h((2p+1)b).
\]

Sum over \(p\). Apply with \(h(t)=(E-s-t)_+\), which is convex and supported in \([0,E-s]\) whenever \(s<E\). Tonelli's theorem applies throughout because all measures and integrands are nonnegative. Thus **replacing one magnetic pair by a zero pair cannot decrease** the convolution Riesz mean. Replacing coordinates successively proves \(r_{\mathbf b}(E)\le r_{\mathbf0}(E)\), with no regularization or limiting interchange.

For \(u>0\), the prior *single-pair* arithmetic can be recovered without any external theorem: if \(N=\max\{0,\lceil (u/b-1)/2\rceil\}\), summing the first \(N\) odd integers gives
\[
r_b^{(1)}(u)=\frac{b}{2\pi}(Nu-bN^2),
\qquad
r_0^{(1)}(u)=\frac{u^2}{8\pi},
\]
\[
0\le r_0^{(1)}(u)-r_b^{(1)}(u)
=\frac{b^2}{2\pi}\left(N-\frac{u}{2b}\right)^2
\le\frac{b^2}{8\pi}.
\]
The difference vanishes for \(u\le0\); when \(b=0\) it is identically zero. This paragraph verifies the exact normalization but **does not re-register** the earlier one-pair finding.

For a fixed coordinate \(j\), integrate this bound with \(u=E-\sum_{i\ne j}t_i\) against the product of the other measures. Its contribution to a telescoping replacement is at most
\[
\frac{b_j^2}{8\pi}
\prod_{i\ne j}\mu_{b_i}([0,E)).
\]
The uniform one-pair counting estimate in Lemma 2.24.6 says \(\mu_b([0,E))\le E/(2\pi)\) for \(b>0\); for \(b=0\) the stronger \(E/(4\pi)\) holds. Therefore each replacement is bounded by
\(b_j^2 E^{n-1}/[8\pi(2\pi)^{n-1}]\).
Summing over \(j\) yields the displayed upper estimate. Finally the \(n\)-fold convolution of the \(n\) zero-field densities has density \(t^{n-1}/[(4\pi)^n(n-1)!]\) on \([0,\infty)\). Integrating \((E-t)\) over \([0,E]\) gives the stated polynomial for \(r_{\mathbf0}\).

## Complete proof of the two-pair identity

With one zero field, direct integration of its continuous measure gives
\[
r_{(b,0)}(E)
=\frac{b}{16\pi^2}\sum_{p\ge0}
(E-(2p+1)b)_+^2,\qquad
r_{(0,0)}(E)=\frac{E^3}{96\pi^2}.
\]
The number of positive terms is \(N\) as above, including the strict-threshold convention of (2.24.5). The finite odd-square identity
\(\sum_{p=0}^{N-1}(2p+1)^2=N(4N^2-1)/3\)
implies
\[
r_{(b,0)}(E)
=\frac b{16\pi^2}
\left(NE^2-2bEN^2+\frac{b^2N(4N^2-1)}3\right).
\]
Substitute \(E=2bx\) and \(N=x+\delta\) and expand; this gives exactly the boxed formula. On \([-1/2,1/2]\), the cubic \(f(\delta)=\delta-4\delta^3\) has extrema \(\pm1/(3\sqrt3)\), attained at \(\delta=\pm1/\sqrt{12}\), establishing the quantitative remainder and positive limiting coefficient. This calculation uses finite polynomial sums only.

## Status, correction and dependencies

**Severity:** low. **Status:** verified conditional deduction, **not** confirmed error or a claim that the original Lemma 2.24.6 / Proposition 2.24.8 is false. The proposed change is an *optional* source/body corollary for later independent review, **not** an edit to main. Downstream dependencies: the field-rank-continuity part of Lemma 2.24.6, uniform magnetic Riesz estimates and semiclassical comparison surrounding Proposition 2.24.8; no global holomorphic Morse inequality is certified here. The proof treats only the stated constant-field model and uses the printed density formulas and elementary convexity/finite sums. Completeness of the oscillator mode decomposition and the general magnetic spectral theorem remain earlier internal inputs, not transitively certified by this calculation.

## Actual performed checks and coverage

- Freshly read main, AGENTS.md, documentation/proof-expansions.md, branch LATEST.md and README.md, and current table-of-contents/coverage inventory; reviewed fixed main blob and the exact integrated physical lines above.
- A standalone **exact-rational** finite arithmetic check was run: n=2 and n=3 model values with zero/nonzero fields and a separate set of 240 exact two-pair oscillation identities. It passed. It is supportive finite testing, **not** a project build, formal proof or global verification. Reproducible source: checks/check_magnetic_multipair_midpoint.py.
- §2.24 was **already partly inspected** on 2026-10-27: newly first-visited numbered sections **0**; entire-section certifications **0**; actual project ToC **25 chapters / 747 numbered sections**. Other chapter 2 results, general analytic prerequisites and all downstream spectral results remain unverified.
- All user-excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programmes remain **deferred-by-user**, neither resolved nor certified. No source, canonicalization, permanent tags, main, publication, CI or GitHub Actions changes.
