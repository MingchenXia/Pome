# Direct audit: rooftop comparison and projective cohomology

**Date:** 2026-11-23. **Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Review branch:** `review/mathematical-audit`.

## Exact current-integrated coverage

- §13.23, entire mathematical text physical lines **7–160** in `docs/sections/volumes-under-bounded-mass--rooftops-and-capacity-convergence/index.html`, main blob `2b0162752e9800061002119630703701c814a2ec`. Lemma **13.23.1**, permanent tag `2B568CD72F9D`, statement lines 11–15 and proof 20–42; Proposition **13.23.2**, permanent tag `1542F41C8A51`, statement lines 50–52 and proof 58–90; Theorem **13.23.3**, permanent tag `7D5F8FB5CFAB`, statement lines 98–106 and proof 111–160.
- §10.50, entire mathematical text physical lines **7–88** in `docs/sections/hodge-theory-curvature-and-compact-vanishing--the-cohomology-of-spheres-and-projective-space/index.html`, main blob `a45ae3fefbf6746eca800f490163ac7ce2456c07`. Proposition **10.50.1**, tag `DD72F1B19307`, lines 11–27; Lemma **10.50.2**, tag `2E46F3014687`, lines 33–44; Theorem **10.50.3**, tag `558E1268EEED`, lines 49–88.
- Definition §13.22.1 and Eq. **13.22.2**, selected context only, `docs/sections/volumes-under-bounded-mass--cauchy-convergence-of-model-potentials/index.html`, blob `390f280e62ce8ba01de30f6b1ed52b4aa7fb10e4`, lines 7–27. Other dependencies listed below are not counted as new whole-section readings.

## POME-ROOFTOP-VOLUME-COMPARISON-LOCAL-HOLDER-001

**Severity:** low. **Status:** verified conditional deduction. **Not a false original theorem; not a full transitive proof certification.**

Use the compact-background volume notation of §§13.22–13.23: \(n=\dim_{\mathbb C}X\ge1\), \(U(w)=\overline{\mathrm{vol}}_\theta(w)\), \(M=U(V_\theta)>0\), and \(d_\theta(x,y)=2U(\max(x,y))-U(x)-U(y)\). In particular **\(d_\theta\) is a volume comparison, not a metric**. Let \(u,v\in\mathrm{PSH}(X,\theta)\), \(\delta=\underline{\mathrm{vol}}_\theta(u)>0\), and \(s=d_\theta(v,u)\). Fix \(a\in(0,1)\) satisfying \(2nMa<\delta\). If
\[
0<s<\tfrac12\delta a^n,\qquad t=\frac1a\left(\frac{2s}{\delta}\right)^{1/n}<1,
\]
then the rooftop \(p=P_\theta(v,u)\not\equiv-\infty\) and
\[
\boxed{0\le d_\theta(p,u)\le M[1-(1-t)^n]\le \frac{nM}{a}(2s/\delta)^{1/n},}
\]
\[
\boxed{0\le\underline{\mathrm{vol}}_\theta(u)-\underline{\mathrm{vol}}_\theta(p)
\le\delta[1-(1-t)^n]\le\frac{n\delta}{a}(2s/\delta)^{1/n}.}
\]
This gives an explicit margin-dependent local \(1/n\)-Hölder **upper modulus** for both quantities; no optimality or metric triangle inequality is claimed.

**Proof.** Set \(m=\max(u,v)\), \(b=(\delta/(2s))^{1/n}\). Then \(b>1\), \(b^ns=\delta/2<\delta\), and \(\underline{\mathrm{vol}}_\theta(m)\ge\delta\). Definition 13.22.1 shows that the two upper-volume deficits from \(m\) to \(u,v\) are each at most \(s\). Therefore Lemma 13.18.1 constructs stretching envelopes \(G=Q_b(v,m)\) and \(H=Q_b(u,m)\). With \(g=(1-a)m+aG\) and \(h=(1-a)m+aH\), the mass addition estimate used explicitly in §13.23.2, physical lines 68–77, gives
\[
2U(m)-U(g)-U(h)\le2[1-(1-a)^n]U(m)\le2nMa<\delta.
\]
Lemma 13.23.1 makes \(r=P_\theta(g,h)\) nontrivial. The defining stretching inequalities and \(r\le g,h\) imply, because \(t=(ab)^{-1}\),
\[
(1-t)m+tr\le u,\ v.
\]
Thus \(p\) has a nontrivial competitor. The volume monotonicity/addition argument at physical lines 83–89 of §13.23.2 yields, for either \(V=\underline{\mathrm{vol}}_\theta\) or \(V=U\),
\[
(1-t)^n V(u)\le(1-t)^nV(m)\le V(p)\le V(u).
\]
The lower-volume bound follows immediately. Since \(p\le u\), Eq. 13.22.2 gives \(d_\theta(p,u)=U(u)-U(p)\), bounded by \(M[1-(1-t)^n]\). Finally \(1-(1-t)^n\le nt\) on \([0,1]\). This proves both displayed estimates. \(\square\)

**Dependencies, status and correction:** The result relies on the currently printed §13.18.1 stretching construction, §13.23.1 finite-rooftop contact/deficit argument, and §13.23.2 mass-addition inequalities. Their full upstream Bedford–Taylor/non-pluripolar and monotone-volume chains have **not** been certified in this run. §13.23.3's monotone lower barriers also invoke §13.21.2, §16.28.6 and compact normalized model limits; no unproved interchanges of an arbitrary net with sequences are made here. Propose an optional quantitative corollary after §13.23.2; retain the printed theorem, all source tags and attribution. The downstream capacity and model-convergence results citing §13.23.2 may use the stronger quantitative input, but no downstream false statement is alleged. All upstream regularization-specific matters, if cited, remain **deferred-by-user**, not re-examined.

## Independent §10.50 mathematics review

- §10.50.1: a partition of unity constructs surjectivity of the restriction-difference map; the splitting need not commute with \(d\), whereas the short exact complex arrows do. Long-exact-sequence degree shifts and signs check.
- §10.50.2: punctured sphere Mayer–Vietoris gives \(H^1(S^1)=\mathbb C^2/\Delta\mathbb C\) and \(H^j(S^m)\simeq H^{j-1}(S^{m-1})\) for \(m\ge2,j\ge2\). The \(S^0\) component exception is explicitly handled.
- §10.50.3: the displayed deformation \([z_0:z']\mapsto[(1-t)z_0:z']\) stays inside \(\mathbb P^n\setminus\{[1:0:\cdots:0]\}\); the punctured affine-ball intersection computes the top degree. Positivity and Stokes prove \([\omega_{\rm FS}^k]\ne0\); normalization follows from \((n!/\pi^n)(\pi^n/n!)=1\). The Dolbeault identification is conditional on the already cited §§10.47.13 and 10.43.11, not independently re-proved here. The \(n=0\) case is treated separately.
- No newly confirmed theorem error, genuine duplicate, or counterexample in this section; no completely certified dependency chain.

**New actual scope:** two whole current direct mathematical readings, one selected §13.22 definition/equation check, one new conditional deduction, zero new confirmed errors, zero complete transitive certifications. Historical first visits unasserted. No software tests, build, GitHub Actions CI, source/body/registry/canonical-tag/main or production-site edits; all specified Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain deferred-by-user.