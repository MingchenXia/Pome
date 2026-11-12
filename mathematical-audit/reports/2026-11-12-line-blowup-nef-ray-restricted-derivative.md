# Exact nef ray and restricted intersections on the blowup of a line in \(\mathbf P^3\)

**Finding:** POME-BC-LINE-BLOWUP-NEF-RAY-RESTRICTED-DERIVATIVE-001  
**Status:** verified conditional deduction  
**Severity:** low — quantitative sign and normalization boundary check, not an error in the printed example  
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272 (2026-11-12 audit snapshot).

## Scope and exact source anchors

Integrated reading edition: docs/sections/bott-chern-classes-and-singular-loci--divisorial-traces-with-bounded-remainder/index.html, main blob 336833c05262c42310ca72254358088739b2ca27.

- Example 10.17.10, original source non-kahler-pluripotential-theory:88E1D2A0, permanent tag 5E3AD3C523AC, physical lines 145–150: the blowup of \(\mathbf P^3\) along a line, the exceptional ruled surface, the zero restricted invariant on \(E\), and the positive degree on one section.
- Lemma 10.17.3, original source non-kahler-pluripotential-theory:3EFD2D7A, permanent 21B7909B2B52, lines 30–61, especially the bounded-residual top intersection identity (10.17.4), original source D4A37A0B, permanent 477AB76A3ADC, lines 32–60.
- Theorem 10.17.6, original source non-kahler-pluripotential-theory:3EFBC646, permanent 2D52D521F2D7, lines 74–90: invariance of the trace mass under resolution.
- This new calculation checks a *one-parameter* family on the same explicit threefold and is **not** a proof of general resolution-independence, the general nef restricted-volume theorem, or the general null-locus theorem.

## Statement and complete intersection calculation

Let \(\mu:X=\mathrm{Bl}_L\mathbf P^3\to\mathbf P^3\) be the blowup of the line \(L=\{Z_2=Z_3=0\}\). Let \(H=\mu^*c_1(\mathcal O_{\mathbf P^3}(1))\) and \(E\) be the exceptional divisor. The projection \([Z_0:Z_1:Z_2:Z_3]\dashrightarrow[Z_2:Z_3]\) extends to a morphism \(p:X\to\mathbf P^1\), and \(H-E=p^*c_1(\mathcal O_{\mathbf P^1}(1))\).

The exceptional surface is \(E\simeq\mathbf P^1_s\times\mathbf P^1_d\), where \(s\) is the point of the center and \(d\) the normal direction. Set \(a=\mathrm{pr}_s^*c_1(\mathcal O(1))\), \(b=\mathrm{pr}_d^*c_1(\mathcal O(1))\) on \(E\). Then
\[
H|_E=a,\quad (H-E)|_E=b,\quad E|_E=a-b,\quad a^2=b^2=0,\quad \int_E ab=1. \tag{1}
\]
For clarity about the sign: since \(N_{L/\mathbf P^3}=\mathcal O_L(1)^{\oplus2}\), the normal line of \(E\) in \(X\) is its tautological *subline* \(\mathcal O_E(-1)=\mathcal O_E(1,-1)\), not \(\mathcal O_E(-1,-1)\). Equivalently, the two resolved maps \(\mu,p\) restrict to the two projections on \(E\); this implies \(E|_E=H|_E-(H-E)|_E=a-b\) without invoking a projectivization convention.

Consequently the entire intersection table is
\[
H^3=1,\quad H^2E=0,\quad HE^2=-1,\quad E^3=-2. \tag{2}
\]
The signs in (2) follow from restriction to \(E\): \(\int_E a^2=0\), \(\int_E a(a-b)=-1\), and \(\int_E(a-b)^2=-2\).

For \(0\le t\le1\) let \(A_t=H-tE=(1-t)H+t(H-E)\). Both summands are pullbacks of hyperplane classes, so \(A_t\) is nef throughout the closed interval. Since \(X\) is the incidence hypersurface in \(\mathbf P^3\times\mathbf P^1\) and \((\mu,p)\) is an embedding, the positive combination is a Kähler class for \(0<t<1\); \(A_1=p^*c_1(\mathcal O(1))\) is nef but not big.

Expanding (2) proves the exact polynomial
\[
\boxed{\int_X A_t^3=1-3t^2+2t^3=(1-t)^2(1+2t).} \tag{3}
\]
On the exceptional divisor, \(A_t|_E=(1-t)a+tb\), hence
\[
\boxed{\int_E(A_t|_E)^2=2t(1-t).} \tag{4}
\]
For the section \(Y=\mathbf P^1_s\times\{d_0\}\) and the ruling fiber \(F=\{s_0\}\times\mathbf P^1_d\),
\[
\boxed{\int_Y A_t=1-t,\qquad \int_F A_t=t.} \tag{5}
\]
For these nef smooth classes the restricted invariants in the sense of the printed example agree with the respective intersection numbers by the nef intersection/trace-mass identification quoted in the reading edition. In particular at \(t=0\), (4) gives \(\mathcal R(A_0;E)=0\), while (5) gives \(\mathcal R(A_0;Y)=1\), reproducing precisely Example 10.17.10. For \(0<t<1\), (4) is positive; for \(t=1\), it vanishes again, while the fiber still has degree one.

Differentiating (3) and comparing to (4) yields the exact moving intersection identity
\[
\boxed{\frac{d}{dt}\int_X A_t^3=-3\int_E(A_t|_E)^2=-6t(1-t).} \tag{6}
\]
The first equality is also a direct multilinear expansion, \(d(A_t^3)/dt=-3A_t^2E\). It is a separate sign crosscheck: incorrectly assigning \(E^3=+2\) would violate both (3) at \(t=1\) and (6).

## Interpretation, dependencies, and limits

This gives a completely explicit restricted-mass transition in a fixed projective threefold: the exceptional surface has zero restricted intersection at both nef endpoints, positive restricted intersection strictly between them, and different ruling curves detect opposite endpoints. The ambient top intersection has a **quadratic** zero at the non-big endpoint \(t=1\), consistent with numerical dimension one of \(A_1\).

Equations (1)–(6), the nef claim, and the direct positivity for \(0<t<1\) follow from the displayed blowup and intersection calculation without any singular potential regularization. Interpreting the intersections as the *general* restricted invariant uses the internal nef trace/intersection identification of §§10.16–10.17, **not independently certified here**. No general non-pluripolar convergence, resolution-invariance, or theorem of positivity is certified by the model. No source theorem is refuted; no edit of the mathematical body is proposed.

**Deduplication:** Example 10.17.10 already contains the isolated \(t=0\) values. This finding only records the new entire \(A_t\)-ray, the correct \(E^3=-2\) intersection table, the endpoint/section/fiber formulas, and the moving derivative identity. It does not refile the existing example or previous normal-crossing mixed mass models.

**Affected dependent statements to check when used:** Example 10.17.10, Lemma 10.17.3/(10.17.4) for nef trace mass, and any use of a restricted-intersection derivative in the nearby divisorial-volume discussion. The general statements remain conditional rather than certified.

**Out of scope:** Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain deferred-by-user; prior notes are neither resolved nor validated here.
