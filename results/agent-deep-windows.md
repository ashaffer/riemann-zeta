# Deep windows and the bend: the envelope law past L = 4.2 — final report

**Session: July 26, 2026 (deep-windows agent). Status: FINAL.** Data:
`agent-deep-windows/runs.csv` (this session's 20+ runs) +
`agent-deep-windows/priors.csv` (recorded anchors used); complete fit output:
`agent-deep-windows/fit_report.txt` (regenerate: `python3 fit_law.py`);
stopping-height readouts: `python3 stopping_height.py`. The L=5.50
discriminator ladder was still landing its last rungs at close; its section
below states exactly what is measured and what is extrapolated.

## Task

Extend the measured envelope law **ln λ_min(L) ≈ 10.2 − 1.755·e^{L/2}(L/2+4)**
to deeper windows (L = 4.60, 4.75, stretch 5.00), refine the flagged deep
points (L = 4.25, 4.50), refit, and settle the bend question. Coordinator
addenda: the L = 5.50 Connes/Groskin discriminator (agent-prior-art.md §7.2);
the numerical-analysis creep de-bias (PLAN-numerical-analysis.md Lemma 1)
reported in parallel with raw fits; the w(L) stopping-height protocol
(PLAN-differential-geometry.md Round 2 (c)) with its three hypotheses; the
harmonic-analysis T1′ two-horizon consistency test (PLAN-harmonic-analysis.md
Round 2); and the synthesis' correction of this report's interim overclaim
(SYNTHESIS.md §1.2 item 1) — adopted, see "Convergence honesty".

## Instrument, anchors, discipline

`src/spectral_margins.py` (`spectral_form`/`spectral_lam_min`), driven
unmodified by `agent-deep-windows/run_window.py`. **Every λ is a
Rayleigh–Ritz upper bound**; nested bases ⇒ fixed-L ladders monotone
non-increasing in m — **PASS at every L, no violations**. All m ≤ 184 share
identical 192-point GL x/u rules (exact on polynomial overlap factors;
analytic-factor error ~10^{−271}), so decrements are pure basis effects.
Bottom-gap λ₂/λ₁ ≥ 3.6×10³ at every deep rung — no level-crossing artifacts.

Regression anchors: `spectral_form(2.485, 24)` at dps 50/40 →
**3.8688156e-10, PASS to all printed digits** (10.9 s). Expensive anchor
(4.25/112 → 5.5489577e-35) not rerun (permitted); confirmed by monotonicity
(this session's 128/144/160 rungs descend below it).

Calibration: (4.60, 112, 75/65) → 375 s solo; assembly ~m², solve < 100 s
to m=176; co-tenant load stretched wall clocks ~2.2x mid-session. ≤ 3
concurrent single-threaded workers throughout; two session restarts and one
lane-kill absorbed by re-reading runs.csv and relaunching only missing rungs.
Precision: solve dps with 10^{−(dps−5)} ≥ 100x below predicted λ (75/65 at
L ≤ 4.75, 90/80 at 5.00, 100/90 at 5.50); assembly = solve+10; every
eigenvalue ≥ 15 orders above the solver floor.

## Run table (all completed runs this session; RR upper bounds)

| L | m | dps | λ_min | asm+solve s |
|---|---|---|---|---|
| 3.555 | 96 | 50/40 | 2.1399593e-22 | 340+12 |
| 3.555 | 112 | 50/40 | 2.1266806e-22 | 457+18 |
| 4.025 | 96 | 50/40 | 2.0887707e-30 | 713+16 |
| 4.025 | 112 | 50/40 | 2.0269885e-30 | 560+23 |
| 4.25 | 128 | 75/65 | 5.4302903e-35 | 1080+84 |
| 4.25 | 144 | 75/65 | 5.2588983e-35 | 735+40 |
| 4.25 | 160 | 75/65 | 5.2331605e-35 | 869+58 |
| 4.50 | 128 | 75/65 | 8.9731803e-41 | 1053+48 |
| 4.50 | 144 | 75/65 | 8.1342193e-41 | 1639+60 |
| 4.50 | 160 | 75/65 | 7.9244886e-41 | 1902+55 |
| 4.60 | 112 | 75/65 | 2.2124424e-42 | 361+14 |
| 4.60 | 128 | 75/65 | 3.0769156e-43 | 990+98 |
| 4.60 | 144 | 75/65 | 2.3639344e-43 | 1515+95 |
| 4.60 | 160 | 75/65 | [landing at close; see runs.csv] | |
| 4.75 | 128 | 75/65 | 1.4880410e-46 | 1018+36 |
| 4.75 | 144 | 75/65 | 2.0404476e-47 | 1071+44 |
| 4.75 | 160 | 75/65 | 1.8636609e-47 | 1344+74 |
| 5.00 | 144 | 90/80 | 2.9413204e-53 | 678+40 |
| 5.00 | 160 | 90/80 | [landing at close] | |
| 5.00 | 176 | 90/80 | 7.0075134e-55 | 1073+73 |
| 5.50 | 152 | 100/90 | 1.9853755e-64 | 824+49 |
| 5.50 | 168 | 100/90 | [queued at close] | |
| 5.50 | 184 | 100/90 | [landing at close] | |

Scheduled-not-run: 4.75/176 (luxury); 5.50/200 (4x node-regime cost; the
equal-step triple 152/168/184 was run instead — same budget, extrapolable);
2.996/80+96 (best-converged old window). CPU total ≈ 7 h of the 6–10 h
budget including in-flight rungs.

## Convergence honesty (interim overclaim, corrected)

The interim version of this report said "convergence bias is excluded" from
Aitken plateaus at L=4.25/4.60. SYNTHESIS.md called the overclaim, and this
session's own m=144 row at L=4.25 proved it: the decrement INCREASED past
the quoted plateau (staircase descent). All statements below distinguish
hard upper bounds, model-tested extrapolations, and model-contested ones.

## Ladders and the extrapolation-model tests

- **L=3.555**: 2.1774/2.1400/2.1267e-22 (m=80/96/112), r=0.355; Aitken
  2.119e-22 ≈ creep 2.062e-22 (3%).
- **L=4.025**: 2.7922/2.0888/2.0270e-30, r=0.088; Aitken 2.021e-30; creep
  floor 1.727e-30. The recorded fifth solid window was 38% above its own
  refinement.
- **L=4.25**: 7.5202/5.5490/5.4303/5.2589/**5.2332e-35** (m=96..160).
  Decrements 1.971/0.119/0.171/0.026 — a **staircase** (d₃ > d₂), then
  re-collapse (d₄/d₃ = 0.150). 4-pt test at m=144: geometric predicted
  5.4231, creep 5.3408, measured 5.2589 — **both models failed low** there;
  the m=160 rung then re-flattened. Last-triple Aitken 5.229e-35;
  staircase-aware bracket **[≈5.1e-35, 5.2332e-35]**.
- **L=4.50** (cleanest): 12.448/8.9732/8.1342/**7.9245e-41** (m=112..160),
  ratios 0.241/0.250 — stable geometric. 4-pt test at m=160: geometric
  7.9317e-41 (**+0.09%**), creep 7.4805e-41 (−5.6%): **geometric confirmed,
  creep rejected**. Aitken limit **7.855e-41**; creep limit 6.37e-41.
- **L=4.60**: 22.124/3.0769/**2.3639e-43** (m=112..144), r=0.037; Aitken
  **2.336e-43**; creep model extrapolates NEGATIVE here (self-inconsistent —
  its C is plunge-contaminated, outside the model's own post-plunge regime).
  m=160 plateau-check landing at close.
- **L=4.75**: 14.880/2.0404/**1.8637e-47** (m=128..160), r=0.014; Aitken
  **1.861e-47**; creep floor 5.51e-48. The Fuchs-form prediction of this
  limit (1.87e-47) was registered from the 4.25/4.50/4.60 data BEFORE the
  m=144/160 runs: measured landed within **0.4%**.
- **L=5.00**: 2.9413e-53 → 7.0075e-55 (m=144→176), 42x/32-in-m — deep
  plunge, unconverged (mid-point landing at close).
- **L=5.50**: 1.9854e-64 (m=152) — first rung, deep plunge (see below).

## The refit (raw AND creep-de-biased, per instruction)

3-param family ln λ = A − b·e^{L/2}(L/2+c0); parameter-degenerate — compare
predictions/residuals, not constants:

| fit | data | (A, b, c0) |
|---|---|---|
| F0 | four original windows, best values | (10.57, 1.659, 4.38) — canonical, ±2% |
| F1b | five solid windows, converged limits | (11.84, 1.305, 6.21) — ±10% structured |
| F2 | + deep raw UBs | b drifts to ≈0.94 — the bias artifact NA predicted |
| F4 | + deep geometric limits | b ≈ 1.0, residuals still structured |
| F6 | + deep creep-model limits | see fit_report.txt (creep invalid at 4.60) |

**Deep residuals vs F1b** (best mid-range refit; +: above law; nats):

| L | raw UB | geometric | creep-de-biased |
|---|---|---|---|
| 4.25 | +0.27 | +0.27 (staircase bracket +0.24..+0.27) | +0.03 |
| 4.50 | +0.54 | **+0.32** (model-tested) | +0.32 (but model rejected at this L) |
| 4.60 | +0.75 | **+0.73** | n/a (negative — model breaks) |
| 4.75 | +0.97 | **+0.97** | −0.25 |
| 5.00 | +1.90 | unconverged | — |

Vs the CANONICAL constants the same rows read +0.87/+1.53/+1.92/+2.49/+4.08:
**the published law underpredicts every deep window under every reading.**

**Raw/geometric verdict: (ii) systematic upward bend** — geometric-limit
residuals grow monotonically to ~7x F1b's own residual band, with the
corrected deep form (below) fitting at the few-percent level.
**Creep-de-biased verdict: (i)-relative** — de-biased points scatter ±0.35
around F1b (no bend beyond refitted constants) — but the creep model **lost
its only head-to-head test** (4.50), **breaks at 4.60**, and its C is
plunge-contaminated at deep L by its own regime condition. **The two
verdicts disagree; that disagreement is a finding.** The evidence
preponderance (model test 1–0, internal consistency, the blind 4.75
prediction) favors the geometric reading and verdict (ii).

**The corrected deep functional form** (Fuchs/prolate), fit on the four
extrapolated deep limits (4.25 last-triple, 4.50, 4.60, 4.75):

    ln λ ≈ A′ − b′·e^{L/2} + p·(L/2)
    free (4 pts, 1 dof):  b′ = 12.729 = 1.013·4π,  p = 6.5, resid ≤ 2.8%
    p = 4.5 (Fuchs n=4):  b′ = 12.521 = 0.996·4π,  resid ≤ 3.4%
    b′ = 4π fixed:        p = 4.93,                resid ≤ 3.2%
    pairwise slopes (p=4.5 gauge): 12.53 / 12.42 / 12.58  (4π = 12.566)

The canonical law's local slope 1.755(L/2+5) crosses 4π at **L = 4.32** —
where the deviations begin. The mid-range (L/2+4) log-factor is
pre-asymptotic; past c = e^{L/2} ≈ 8.7 the decay rate saturates at the
universal prolate rate **4π per unit c**.

## The w(L) stopping-height protocol (DG Round 2 (c)) — executed, scalar part

Three hypotheses (per the protocol's own honing): **drift** (no bend),
**abrupt saturation** (w jumps to w∞ = 1.2785 = root of e^w(w−1)=1), **smooth
cap** (slope pinned at 4π, w continuous). The protocol warns: *w-levels
separate only abrupt saturation* (drift and smooth-cap differ by ≤ 0.003 in w
at reachable L); drift-vs-cap needs the shape test.

Primary estimator w_E2 (action matching, A = 11.5, band A ∈ [11.1, 11.9];
`stopping_height.py`):

| L | λ used (top-m) | w_E2 | A-band | gate (Δw ≤ 0.01) |
|---|---|---|---|---|
| 1.750 | 3.144e-05 | 1.1437 | ±0.007 | — |
| 2.485 | 3.568e-10 | 1.1647 | ±0.005 | calibration: drift ref 1.147±0.02 → +0.018, **PASS** |
| 2.996 | 4.227e-15 | 1.1803 | ±0.004 | calibration: drift ref 1.167 → +0.013, **PASS** |
| 3.555 | 2.127e-22 | 1.1970 | ±0.003 | PASS |
| 4.025 | 2.027e-30 | 1.2087 | ±0.002 | PASS |
| 4.250 | 5.233e-35 | 1.2136 | ±0.002 | PASS (refs: drift 1.212, cap 1.214) |
| 4.500 | 7.924e-41 | 1.2192 | ±0.002 | PASS (drift 1.220, cap 1.220) |
| 4.600 | 2.364e-43 | 1.2211 | ±0.002 | PASS |
| 4.750 | 1.864e-47 | 1.2243 | ±0.001 | PASS (drift 1.229, cap 1.227) |
| 5.000 | 7.008e-55 | 1.2282 | ±0.001 | **FAIL (0.012)** → verdict U at 5.00 |
| 5.500 | 1.985e-64 | 1.1861 | ±0.001 | unconverged (plunge) |

- **Convergence gate**: PASS at every L in 3.555–4.75; FAIL at 5.00
  (verdict U there, pending its mid-rung) — the protocol's bias diagnostic
  doing its job.
- **Level test** (converged L): w_E2(4.75) = 1.224 ∈ [1.20, 1.25] →
  **level-non-discriminating, exactly as pre-computed for both drift and
  smooth cap; B_abrupt is EXCLUDED** (would require ≥ 1.26).
- **Shape test (Step 5.3)**: the specified y(x) envelope test needs the
  minimizer VECTORS (not stored by these runs; extraction assigned to the DG
  seat in SYNTHESIS §7). **Not run here.** The scalar analog — secant slopes
  dE/dc in the p=4.5 gauge between converged deep limits — reads
  12.53/12.42/12.58 against: smooth-cap 12.566; drift(1.755, 4)
  13.12/13.23/13.31; drift(1.51, 5.04) 12.93/13.02/13.16. Measured slopes
  sit ON the cap (−1.1%..+0.1%) and 3–6% BELOW both drift members, with
  residual RR bias bounded ≤ 0.5% of slope (gates passed at all four
  endpoints). **The scalar shape evidence favors B_smooth (smooth cap)**;
  the formal B_smooth verdict per protocol awaits DG's vector-level y(x)
  break test.

## The T1′ two-horizon consistency test (HA Round 2) — PASS

T1′ requires every stopping height strictly inside (e·T*, e²·T*), i.e.
w ∈ (1, 2). Measured: all eleven w_E2 values lie in **[1.144, 1.228]** —
strictly inside both horizons at every window. Margins: lower (w − 1) from
**+0.144** (L=1.75, the tightest) rising to +0.228 (L=5.00); upper (2 − w)
from +0.856 down to **+0.772**; the A-band moves w by ≤ 0.008, never
approaching either endpoint. In T/T* units: T_s/T* ∈ [3.14, 3.41] ⊂
(2.72, 7.39). The deep values approach C4's e^{w∞} = 3.59·T* from below and
nothing crosses it. **T1′ survives its first falsifiable pass against
measured data, at all support lengths, with ≥ 0.14 nats to spare.**

## The L=5.50 rung and the Connes/Groskin tension (status: honest)

Measured at close: **m=152 → 1.9854e-64** (dps 100/90, 873 s), deep in the
plunge; m=168/184 were landing/queued at close (runs.csv is authoritative).
Status: **descending upper bound, NOT converged, NOT adjudicating by
itself.** Predictions at L=5.50 for the record: canonical law 9.0e-77
(log₁₀ = −76.05); Fuchs-form fits (this session, all variants) **1.9–2.6e-73
(log₁₀ ≈ −72.6 ± 0.1)**; calibrated comparator (anchors c=11 → −49,
c=100 → −530) **−73.6**. The corrected law and the comparator now agree
within ~1 decade at this depth; the canonical law sits 2.4–3.4 decades
below both. Trend extrapolation (LABELED EXTRAPOLATION: from the m=152
point and the plunge-phase pattern of the 4.75/5.00 ladders, whose rungs
fell 7–42x per 16–32 in m before flattening ~1 decade under the second
rung): the L=5.50 limit is expected in **10^{-72}–10^{-75}** — consistent
with both the Fuchs form and the comparator; discriminating against the
canonical −76.05 needs m ≳ 200 or the finished triple's Aitken.

**The c=100 statement (the original §7.2 tension).** Extrapolating the
measured corrected law to CvS c = 100: free/fixp45/fix4pi variants give
**log₁₀ λ(c=100) = −527.7 to −529.0**, against Connes/Groskin ≈ −530
(Groskin Aitken −536.8/−533.7) and against the old law's −656. **The
126-decade tension is resolved as prior-art §7.2's option (ii): the
(L/2+4) log-factor was a mid-range description; with the measured 4π cap
the two programs' predictions coincide to ~0.5% of the exponent.**

## Forecast: the 13-window (L = 5.13–5.50; thresholds 5.130 / 5.545)

| model | L=5.13 | 5.20 | 5.30 | 5.40 | 5.50 |
|---|---|---|---|---|---|
| canonical law | 2.4e-61 | 5.0e-64 | 4.9e-68 | 2.8e-72 | 9.0e-77 |
| F1 (solid-window refit) | 3.1e-60 | 8.5e-63 | 1.2e-66 | 1.0e-70 | 5.2e-75 |
| **Fuchs-form (recommended)** | **2.4e-59** | **8.5e-62** | **1.9e-65** | **2.6e-69** | **2.3e-73** |
| comparator (calibrated) | 2.5e-60 | — | 2.0e-66 | — | 2.5e-74 |

Recommended forecast: the Fuchs-form band (spread across variants ~1.3x);
its L=5.50 value is directly testable by finishing the m=152/168/184 ladder
plus one m ≈ 200–216 rung.

## One-paragraph verdict

**Bend: YES — the envelope law bends upward past L ≈ 4.3, at high
confidence on the raw/geometric reading and by preponderance overall.** The
converged deep ladders sit 1.4–2.6x above the best possible 3-parameter
refit (7x its residual band) and 2.4–7x above the published constants; the
deviation onset coincides with the exactly-computable crossover (L = 4.32)
where the old law's local slope reaches 4π; the deep decay rate is measured
at b′ = 4π to 0.4–1.3% three independent ways (free fit, constrained fit,
pairwise slopes); and the corrected form blind-predicted the L=4.75 limit
to 0.4%. Of the protocol's three hypotheses, **abrupt saturation is
excluded** (level test: w = 1.224 < 1.26), and the **smooth-cap hypothesis
is favored over drift** by the scalar shape evidence (secant slopes on the
cap, 3–6% below both drift-family members, against ≤ 0.5% bias headroom) —
formal B_smooth certification awaits the DG seat's vector-level shape test,
and the creep-de-biased reading (which would flatten the bend onto refitted
constants) is contradicted by its own 4-pt test failure at L=4.50 and its
negative extrapolation at L=4.60. Consistency dividends: every measured
stopping height lies strictly inside T1′'s two horizons (margins ≥ 0.14),
and the corrected law closes the 126-decade Connes/Groskin gap at c=100 to
~0.5% of the exponent — the program's own envelope now extrapolates onto
the frontier's prolate asymptotics.

## Downstream notes

- ENVELOPE.md must be revised before distribution: present the crossover at
  L≈4.32 to the 4π cap; cite Connes §6.4/Fuchs per agent-prior-art.md §7.3.
- Old-window refits should use this session's extended ladders
  (3.555 → 2.119e-22, 4.025 → 2.021e-30).
- Next measurements: DG vector shape test at 4.50/4.75 (B_smooth formal);
  finish 5.50 (m=168/184 + one ≥ 200 rung); m=176/192 at 4.25 (staircase
  closure); interval-certify one deep rung (4.50/m=160) past 1e-20.
