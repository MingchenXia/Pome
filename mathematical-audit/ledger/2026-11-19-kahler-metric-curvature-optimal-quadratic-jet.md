# 2026-11-19 — Kähler metric quadratic-jet minimax ledger

- **ID:** \`POME-KAHLER-METRIC-QUADRATIC-JET-MINIMAX-001\`.
- **Status:** **verified conditional deduction** / **low severity**. No confirmed original error, proof gap, genuine duplicate, complete source repair or full upstream chain is claimed.
- **Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Integrated file:** \`docs/sections/kahler-normal-coordinate-jets/index.html\` (blob \`4fd58352bd134c2715fc4cbf1e0074a42a7e0657\`), physical lines **7–77**.
- **Source/permanent anchors:** Theorem 10.94.2 \`demailly-complex-geometry:07136048\` / **\`64B6971EF741\`**, lines 10–29, 31–77. Equation 10.94.3 \`demailly-complex-geometry:159ABCDF\` / **\`F8EFB833957C\`**, lines 15–22; equation 10.94.4 \`demailly-complex-geometry:9390894A\` / **\`89C5EDFA346C\`**, lines 24–27; cubic-coordinate equation tag **\`9F6B4FD758C3\`**, lines 49–62.
- **Hypotheses:** smooth Kähler metric, \(n\ge1\), point \(p\), holomorphic germs with \(g(0)=I,dg(0)=0\); unscaled Chern curvature, Hermitian operator norm in unitary normal frame. No claim for non-Kähler metrics.
- **Finding:** In all such charts, the quadratic metric deviation satisfies \(\mathcal D(z)\ge\kappa_p=\max_{|v|=1}\|\sum C_{j\bar k l\bar m}v_j\bar v_k\|_{\mathrm{op}}\), with **equality attained** in the cubic normal chart of Theorem 10.94.2. Phase averaging destroys arbitrary \((2,0)+(0,2)\) coordinate artifacts and leaves the mixed curvature term. Equivalently \(g=I+O(|z|^3)\) at \(p\) iff \(\Theta(p)=0\). On \(\mathbb P^1\) Fubini–Study gives the sharp nonzero value \(\kappa_p=2\).
- **Full justification:** [anchored English proof](../reports/2026-11-19-kahler-metric-curvature-optimal-quadratic-jet.md); uses the original cubic-coordinate result as an internal premise.
- **Proposed correction:** optional separate corollary after printed Theorem 10.94.2, **not** a correction of an erroneous printed assertion and **not** an edit to its existing body/tag.
- **Affected dependents:** interpretation of normalized metric jets, curvature coefficient bounds; downstream §10.95 not certified.
- **Prior work distinct:** \`POME-KAHLER-QUARTIC-POTENTIAL-001\` concerns the coefficient of a local potential, **not** the infimum of operator-norm metric distortions over holomorphic charts; not counted again.
- **Unresolved:** the cited internal first-order normal-coordinate lemma \`B12EA9BB1DC1\` and other complete transitive chains remain unverified in this run.
- **Deferred-by-user:** the Demailly regularization, dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi, multiscale and positivity-loss programmes remain deferred, not resolved or certified.
