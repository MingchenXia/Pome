# POME-BT-SUBSOLUTION-MOMENT-SPECTRUM-001

- **Date:** 2026-11-21.
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **branch:** `review/mathematical-audit`.
- **Severity:** low.
- **Status:** **verified conditional deduction** (not a confirmed source error, not a verified independent upstream proof chain).
- **Primary anchors:** §7.11.2 `docs/sections/bedford-taylor-products-and-local-capacity--local-energy-moments/index.html`, source `foundations-of-pluripotential-theory:C2BB479D`, permanent `05F71889C324`, lines 25–91, particularly tail (7.11.3) lines 30–33; cube-average transfer §7.11.5, source `3263E506`, permanent `1151DF7B32E4`, lines 98–160. Section blob `e619f7aa95f80ce11aa676193b054db3180e59d4`.
- **Finding:** A finite measure \(\mu\le(dd^cw)^n\) with bounded psh \(w\) obeys for \(p\ge1\), \(N=n+p\), \(K=2^{n+p}(n+1)! (\mathrm{osc}_Bw)^n e_p(\varphi)\), \(\varphi\in\mathcal E_0(B)\),
  \[
  \int(-\varphi)^q\,d\mu\le\frac{N}{N-q}\mu(B)^{1-q/N}K^{q/N}\quad(0<q<N),
  \qquad\|-\varphi\|_{L^{N,\infty}(\mu)}\le K^{1/N}.
  \]
  For the actual compact-support cube averages \(\mu_j\), the strong \(q\)-moment estimate transfers with factor \(D_{n,q}\) for \(1\le q<N\). No weak endpoint transfer is claimed for \(\mu_j\).
- **Proof:** split the layer-cake integral at \(T=(K/\mu(B))^{1/N}\), using (7.11.3); use Proposition 7.11.5(2) cube average for transfer. Zero-mass/zero-energy cases are handled directly. The printed \(q=p\) case is recovered exactly.
- **Repair/proposal:** optional additional corollary after (7.11.4); **no change required** for the correctness of the source theorem.
- **Affected dependents:** weighted convergence / cube canonical approximants of §7.11 and the mixed-product arguments of §7.12; no new general existence assertion.
- **Open dependencies:** Błocki §7.4.5, BT §7.3, subsolution and cube-average hypotheses; nonexcluded dependency verification pending. All user-excluded analytic proof programmes remain **deferred-by-user**.
- **Full report:** [2026-11-21-bt-capacity-subsolution-moment-spectrum.md](../reports/2026-11-21-bt-capacity-subsolution-moment-spectrum.md).
