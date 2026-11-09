# 2026-11-09 — classical Green kernel under discrete-polar deletion

| Finding ID | Status | Severity | Printed theorem? | Exact anchor | Follow-up |
| --- | --- | --- | --- | --- | --- |
| POME-GREEN-PUNCTURE-INVARIANCE-001 | verified conditional deduction | low | Theorems 3.5.5, 3.5.6, 3.5.12 remain correct | Main b6933b772f41b45918f7e25ed1afbbb1fd892272; docs/sections/green-functions-and-potentials/index.html, blob 63c74d1c4a0958633b42903a0e3a4526f42b7588; source/permanent classical-potential-theory:772DDE67/F3C6870EA9A8 lines 38–57, classical-potential-theory:093A6B54/9E37095B7A8A lines 60–83, classical-potential-theory:1DF5E8AD/9CF388990FE4 lines 155–172 | Proposed tagged Example after 3.5.12; preserve hypotheses and all source tags |

For every Greenian \(\Omega\subset\mathbb R^d\), \(d\ge2\), and relatively closed discrete \(A\), \(G_{\Omega\setminus A}=G_\Omega\) on the smaller domain. This uses a fully written radial-barrier proof of bounded harmonic removability followed by minimality. In \(D^*\subset\mathbb C\), the kernel tends to \(\log(1/|a|)>0\) at the removed point and \(G_{D^*}1(z)=\pi(1-|z|^2)/2\) tends to \(\pi/2\). Therefore **Greenianity alone does not imply boundary decay for bounded potentials**; the explicit one-pole decay assumption of Theorem 3.5.12 is genuinely needed.

**Not the same finding as** POME-PLANAR-GREEN-POLAR-BOUNDARY-SPIKE-001 (which tests the upper semicontinuous regularization of a logarithmic polynomial envelope). Full proof: [report](../reports/2026-11-09-green-kernel-closed-discrete-deletion.md). Precise sampled statements: [coverage](../coverage/2026-11-09-ch3-green-discrete-deletion.md).

No existing finding changed status; no excluded regularization programme reopened. Zero complete-section certifications; no test suite, build, CI or website publication.
