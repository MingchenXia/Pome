# 2026-11-12 classified ledger: line blowup nef ray

- **Stable ID:** POME-BC-LINE-BLOWUP-NEF-RAY-RESTRICTED-DERIVATIVE-001
- **Severity / status:** low / verified conditional deduction. No confirmed printed error or source patch.
- **Main snapshot:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Integrated source:** docs/sections/bott-chern-classes-and-singular-loci--divisorial-traces-with-bounded-remainder/index.html, blob 336833c05262c42310ca72254358088739b2ca27.
- **Anchors:** Example 10.17.10 source non-kahler-pluripotential-theory:88E1D2A0 / permanent 5E3AD3C523AC, physical 145–150; Lemma 10.17.3 source :3EFD2D7A / permanent 21B7909B2B52, 30–61; Eq.10.17.4 source :D4A37A0B / permanent 477AB76A3ADC, 32–60.
- **Hypotheses:** \(X=\mathrm{Bl}_{\mathbf P^1}\mathbf P^3\), \(H=\mu^*c_1(\mathcal O(1))\), exceptional \(E\), \(0\le t\le1\), \(A_t=H-tE\).
- **New verified computation:** \(H^3=1,H^2E=0,HE^2=-1,E^3=-2\); \(A_t^3=(1-t)^2(1+2t)\); \((A_t|_E)^2=2t(1-t)\); \(A_t\cdot Y=1-t\), \(A_t\cdot F=t\); \(\frac d{dt}A_t^3=-3(A_t|_E)^2\). \(A_t\) nef throughout; Kähler for \(0<t<1\).
- **Correction:** none needed to the printed example. Retain the correct \(\mathcal O_E(E)=\mathcal O(1,-1)\) sign in future computations.
- **Conditional upstream:** equality of the general trace/restricted invariant with nef intersection is as stated internally in §§10.16–10.17, not independently proved for arbitrary classes. No proof of general resolution invariance.
- **Duplicates avoided:** previously printed \(t=0\) facts not claimed as new; previous SNC mixed NPP and unrelated blowup-point formulas not refiled.
- **Affected dependents:** Example 10.17.10, Eq.10.17.4 and nef restricted-mass/volume computations using the blowup.
- **Deferred-by-user:** all dedicated Demailly approximation/regularization, Bergman, L², OT, multiscale atlas, positivity-loss work remains deferred, not resolved.
- **Full report:** reports/2026-11-12-line-blowup-nef-ray-restricted-derivative.md.
