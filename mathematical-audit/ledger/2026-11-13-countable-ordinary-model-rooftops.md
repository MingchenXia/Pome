# Classified audit ledger — 2026-11-13 — countable ordinary-model rooftops

- **ID:** `POME-ROOFTOP-COUNTABLE-MODEL-FIP-001`.
- **Status:** **verified conditional deduction**; **severity low**.
- **Source:** production main `b6933b772f41b45918f7e25ed1afbbb1fd892272`,
  `docs/sections/volumes-under-bounded-mass--rooftops-and-capacity-convergence/index.html`
  (blob `2b0162752e9800061002119630703701c814a2ec`), Lemma 13.23.1
  `non-kahler-pluripotential-theory:126FCF2C` /
  `2B568CD72F9D`, lines 10–42; Theorem 13.23.3
  `non-kahler-pluripotential-theory:0A2EE475` /
  `7D5F8FB5CFAB`, especially 112 and 157.
- **Content:** for countably many normalized ordinary models
  \(u_j\preceq w\), if
  \(\sum_j[U(w)-U(u_j)]<
    \underline{\operatorname{vol}}_\theta(w)\),
  finite rooftops are nontrivial ordinary models with supremum zero;
  their nested zero sets have a common point; their decreasing limit
  is the normalized ordinary-model countable rooftop.
- **Limitation:** the bounded \(\theta\)-psh constants \(u_j=-j\)
  on \(\mathbf P^1\) have **zero** deficits but finite rooftops \(-N\)
  collapsing to \(-\infty\); they are not ordinary models. The printed
  *finite* Lemma 13.23.1 is correct.
- **Dependencies:** Lemma 13.23.1 and ordinary envelope monotonicity;
  decreasing-psh limit. **No certification** of the prerequisite
  contact/mass argument or positive-volume persistence of the limit.
- **Proposal:** optional separate countable-model corollary; no source
  statement, canonicalization, registry or permanent-tag edits.
- **Affected:** potential applications to §§13.21–13.23; no downstream
  theorem is declared repaired or fully proved.
- **Complete justification:** [dated report](../reports/2026-11-13-countable-ordinary-model-rooftops.md).
- **Coverage:** [exact matrix row](../coverage/2026-11-13-ch13-countable-model-rooftops.md).
- **Excluded programme:** Demailly approximation/regularization and
  dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale and
  positivity-loss work remain **deferred-by-user**.
