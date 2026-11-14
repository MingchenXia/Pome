# Ledger: three noncollinear point blowup wall

**ID:** POME-RESVOL-NONCOLLINEAR-THREEPOINT-WALL-001  
**2026-11-14; main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Severity:** low. **Status:** verified conditional deduction; no false theorem or complete analytic repair asserted.

**Exact source:** docs/sections/divisorial-restricted-volumes/index.html, blob 8eb1127568e77d6d045098361c366ceeb846b909; section permanent 30E77D3CC0BE. Theorem 20.8.3 source transcendental-positive-cones:42C59BDB / permanent 8DC7DAC31FB7, lines 63–66. Proposition 20.8.16 source transcendental-positive-cones:682A1645 / permanent 7ED04B77FCC6, lines 349–352. Lemma 20.8.1 source transcendental-positive-cones:1E2C07C0 / permanent 7E82D2724E2F, lines 10–25, convention-only.

**Hypotheses:** blowup of P2 at three *noncollinear coordinate points*; real class H-t(E1+E2+E3), 0<t<2/3; restriction divisor E_i. The algebraic formulas require only finite-degree monomial ideal membership; interpreting restricted ranks as analytic restricted masses uses the upstream identification in §20.8.

**New verified statement:** global sections are exactly monomials of total degree d with each exponent <=d-r. The exceptional restriction rank is r+1 below the half-degree wall, then 2d-3r+1 up to r=2d/3. Volume is 1-3t² below t=1/2, (2-3t)² above, zero after t=2/3; E_i restricted volume is t below, 2-3t above. The C1 derivative is -2 times the sum of the three restricted volumes. Explicit fixed factors (xyz)^(2r-d) account for the wall.

**Disposition / proposed optional addendum:** add the finite-degree three-point model and normalization to §20.8, as a separately reviewable production patch only. There is no production edit in this audit. **Affected comparisons:** §20.8.3 derivative coefficient 2 and §20.8.16 restricted-volume interpretation, plus §19 algebraic section-count conventions. Neither theorem is refuted; their general analytic proof chains remain uncertified.

**Distinct from prior work:** the existing 2026-11-02 two-point model and 2026-11-07 three-*collinear*-point wall, and 2026-11-10 central deformation counts, remain separate findings. No earlier finding is resolved, reopened or replaced here.

**Deferred-by-user:** all Demailly regularization/approximation and dedicated Bergman/L2/OT/multiscale/positivity-loss proof completion. **Unresolved upstream:** general analytic identification and global differentiability proof, not reviewed here. Exact selected coverage in the companion coverage file. 
