# Classified finding — 2026-11-11 — monomial generic sheet degree

**Stable ID:** POME-CYCLE-MONOMIAL-FINITE-MAP-GCD-001. **Severity:** low. **Status:** verified conditional deduction. **Original theorem status:** correct in checked scope; no claimed source repair.
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Integrated source:** docs/sections/divisors-and-logarithmic-limits-on-analytic-cycles/index.html, blob dae567406b2030e550664ca57b1fe77911d956d4.

**Anchors:** Lemma 20.5.3, source demailly-complex-geometry:FF68839A / permanent 323D5DA3E240 (lines 27–59); Theorem 20.5.5, source demailly-complex-geometry:D58680EB / permanent F1C928146DBC (lines 64–127); equation 20.5.9 tag 74331B0B45F1 (104–116); Example .11 permanent FF4839E28893 (line 155).

**Exact hypotheses/conclusions:** \(p,q,m,n\ge1\), \(\gcd(p,q)=1\), \(F(x,y)=(x^m,y^n)\), \(D=\{y^p=x^q\}\), \(d=\gcd(pm,qn)\), \(L=mn/d\). Then \(F_*[D]=d[B]\), \(F^*[B]=\sum_{\zeta^L=1}[D_\zeta]\), each \(F_*[D_\zeta]=d[B]\), and \(F_*F^*[B]=mn[B]\). Local divisor orders are \(pma+qnb=d(Pa+Qb)\). Complete algebraic and current-model arguments are in [the dated proof](../reports/2026-11-11-monomial-finite-map-curve-sheet-gcd.md).

**Missing upstream general certifications:** internal proper current pushforward (§20.5.3), analytic-cycle Poincaré–Lelong (§20.5.5). Their exact statements were read; they were *not* proved in full here. No false theorem, missing proof, or new genuine duplication established.

**Proposed correction:** none to the correct source. Guard against substituting ambient degree \(mn\) for individual curve-image degree \(d\); relevant to §§20.4, 20.6, 20.8.

**Exact coverage:** [§20.5 selected passages](../coverage/2026-11-11-ch20-monomial-finite-map-sheet-gcd.md); +0 first mathematical-section visits, +0 complete certifications, 25 chapters / 747 sections. Previous cycle intersection/collision findings not repeated. All excluded Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss work stays **deferred-by-user**.