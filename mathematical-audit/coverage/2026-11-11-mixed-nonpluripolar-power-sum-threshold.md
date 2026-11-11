# Exact coverage — 2026-11-11 — mixed NPP two-power threshold

**Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Review branch:** `review/mathematical-audit`.

**Direct reading:** `docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html`, blob `81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c`. Selected Lemma 13.2.2 and cutoff trace criterion (lines 34–52, source/permanent `foundations-of-pluripotential-theory:CE1D6DA5/D59675D9F6D8`); Proposition 13.2.6 (lines 80–125, `:E82F0D73/7F7123F92478`); Example 13.2.9 (lines 151–165, `:2F8E45A2/6F4C920FEDCA`). Supporting statement/normalization checks: §13.3.1, main `docs/sections/non-pluripolar-products--closedness-and-cutoff-gradients/index.html`, blob `f781fa61bd20944c7c4798e0e0984cfb81ef069f`, lines 10–47 (context **only**); Eq. 7.2.4 and `dd^c` convention (previously pinned source).

**New review:** computed polarized mixed Hessian, checked strict positivity and polar extension for unequal power exponents; integrated exact cylinder measure to obtain the **sharp mixed parameter sum threshold `a+b<1`**, including the case of a finite mixed wedge and an infinite diagonal square. [Finding and proof](../reports/2026-11-11-mixed-nonpluripolar-power-sum-threshold.md). No new false theorem; original statements intact. The **prior diagonal threshold** stays independently registered and is not claimed as new.

**Count:** §13.2 already had previous selected proof review, so **0 newly first-visited numbered sections**; **0 fully mathematically certified sections**. The actual chapter matrix remains **25 chapters / 747 distinct numbered sections**. §13.3 is context-only. Unreviewed other portions of §13.2 and upstream bounded BT/regularity not certified. No software tests/builds, CI, main/source/site edits.

**Deferral:** The owner's Demailly regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remains **deferred-by-user**; its earlier files are neither completed nor certified.
