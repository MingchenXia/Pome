# Isolated plurisubharmonic singularities

The source `isolated-plurisubharmonic-singularities` tracks
`Gerby-Literature/main` through
`contributions/isolated-plurisubharmonic-singularities.tex`. It adapts
Li–Xia's isolated-pole construction and the supporting mathematics selected
for the shared reference. `ISOLATED_PSH_SOURCE_DIR` can point to the same
clean Literature checkout as the Helms, Klimek, Demailly and positive-cone
supplements. Source registration enables an export; it does not establish
publication.

The four selected proof packets cover explicit polynomial iterates and
their finite-stage mass and Lelong number; the decreasing cutoff
construction and its zero-Lelong witness; separated maximum products and
the higher-dimensional examples; and finite logarithmic thresholds,
radial regularity and asymmetry. Their subject placement is:

| Subject | Shared chapter |
| --- | --- |
| Polynomial iterates and residual mass | Lelong numbers, multiplier ideals, and regularization |
| Isolated singularities with zero Lelong number | Lelong numbers, multiplier ideals, and regularization |
| Separated maximum Monge–Ampère products | Local Monge–Ampère theory and capacity |
| Radial growth and residual mass | Lelong numbers, multiplier ideals, and regularization |

The general separated-product theorem and its higher-dimensional
counterexample corollary belong to different subjects. The reviewed
source layout assigns their complete statement boundaries separately.
The chapter and section configuration generates all reader numbers;
source labels and permanent tags do not depend on those numbers.

Major attribution joins the existing
`history--nonlinear-products-and-mass` section of the project history,
preserving the earlier source coverage. The source bibliography is
deduplicated with the shared references. Mathematical entries reuse the
existing isolated-pole continuity, logarithmic model mass, projection and
Lelong results instead of repeating those general theorems. No per-entry
Sources paragraphs are required.

The strict adapter is an exact copy of
`integrations/S0076/isolated-plurisubharmonic-singularities.py.in` in the
Literature repository. Its SHA256 is
`4f0d0e42f0d7cd07f4f3bbbd3b6f1758276251e199013ec3156d9f3e722bf246`.
It reads `integrations/S0076/source-manifest.json` and permits only the
selected contribution, four portable proof fragments, bibliography,
canonical reference map, section layout and project history. Every
selected file is checked against its manifest hash. Each proof requires
separate accepted root and independent review bindings for the exact
original proof hash, together with its portable transformation. Canonical
reference consumers and all subject boundaries must also be reviewed.
Retained papers, private reconstruction notes and unrelated source files
are outside this export graph.

The supplement uses Pome's convention
`dd^c=i/(2pi) partial barpartial`. Its potentials are twice the paper's
potentials, so the squared maximum-logarithm has unit residual mass. The
measure retains its isolated-pole atom; it is the classical
Monge–Ampère product. Global polynomial properness is used before
restricting the resulting identities to the bidisc.

Before publication, run the ordinary clean-source exports, the Python and
JavaScript checks, the complete eight-source collection build and its
numbering and link checks. Browser verification must cover all new formal
statements and actual proof links, all eight source indexes and
representatives, every new mathematical subject, history and bibliography,
and desktop/mobile equation, citation, tag and footnote behavior. Existing
Kelvin, Bedford–Taylor, Klimek Green-function and Demailly Morse-row checks
remain regressions. The shared renderer, reading styles and earlier source
payloads are not changed by this activation.
