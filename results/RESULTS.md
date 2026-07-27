# Measured results (July 26, 2026) — regression targets

Float pipeline (double precision, Galerkin m ≤ 101, Rayleigh–Ritz one-sided) unless
noted. A reproduction matching these numbers is a pass; a mismatch is a bug until an
independent oracle rules otherwise.

## Oracles (certified identities)
| object | window | LHS = RHS | diff |
|---|---|---|---|
| ζ | Gaussian on γ₃, dps 30 | 2.0007024351181021364 | −1.5e−29 |
| ζ | off-resonance t₀=18.5 | 0.0832884717025448 | −8.9e−30 |
| χ mod 3 | Gaussian on 2nd zero | first zero 8.0397372 | −5.8e−22 |
| χ mod 4 | Gaussian on 2nd zero | first zero 6.0209489 | −1.6e−22 |

## Zero-side instruments
- Census [100, 30000]: 35,644 found vs 35,643.63 predicted.
- Record close pair: t = 17143.7865, gap 0.0353 (norm 0.0445), interior max|Z| = 0.00215.
- Classic Lehmer pair: t = 7005.0629, gap 0.0377, bump 0.00397. Typical local max|Z| ≈ 2.36.
- GUE small-gap counts (norm gap < .10/.15/.20/.30): 25/90/215/707 vs predicted 38/128/299/971.
- Davenport–Heilbronn off-line zero: 0.808517182457 + 85.6993484854i (|f| ≈ 6e−26, FE partner 1.5e−24).

## Prime-side instruments (ζ never evaluated)
- Equal loudness at X=10⁶: line heights 13.79/13.26/13.08/12.90/13.13 vs log X = 13.82; floor ≈ 0.8.
- Rogue scan t∈[10,300]: 138 lines vs ≈139 zeros; ratios 1.209±0.133 vs 1.200; max 1.526 ⇒ β < 0.604.
- Mertens: max |M(n)|/√n = 0.4722 on [10³,10⁷]; M(10⁷) = 1037. Redheffer det = M(n) verified (n=50,100,150).

## Margin ladder (ζ)
- Deficits without newest prime (windows 2/3/4/5/7): −0.41/−0.40/−0.61/−0.59/−0.18; rescues → ~1e−6 (m=41).
- Escalation: L=1.75 margin 3.775→3.442e−5 (m 41→101, converged ≈3.4e−5);
  L=2.19: 1.44e−6→1.18e−7; L=3.85: 8.4e−7→3.3e−8 (threshold collapse).
- Threshold exponent (p=3 boundary): λ ∝ d^κ, κ ≈ 0.4 (resolution-limited, biased low).
- Safety factor rescue/deficit at L=1.55…3.20: 2.39, 1.45, 1.27, 1.05, 1.06, 1.03.
- Cascade #eig<1e−2 at same L: 1, 2, 2, 3, 5, 7; bottom-3 principal angle vs landscape: ~20° → 90° at L≈2.4.
- Keyhole (L=3.2, m=61): bottom eigs 2.4e−7, 1.8e−6, 6.0e−6, 1.7e−5, 5.6e−5;
  vector-1 suppression at the 7 zeros: 0.0006/0.0041/0.0002/0.0031/0.0033/0.0037/0.0054;
  nodes 14.135, 21.020, 25.010, 30.410, 32.910, 37.515 vs true 14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862.
- Weyl staircase (#eig<1e−3): 1,1,1,2,2,3,3,3,4,4,5,6,6,6 over L = 1.50…3.45.

## Mechanism law
- 8/8 sign predictions; first-order effect −2Λ(p)χ(p)p^{−1/2}ψ_min(log p).
- Pole flip (ζ, L=1.70): ψ_min(log 2) = +0.106 pole-free → −0.200 with pole;
  prime-2 effect −0.126 → +0.131.

## Dirichlet family
- Cartography |D|≤2000: min L(1): D=−163 (0.2461), −427, −907 | D=1133 (0.2742), 437, 1253.
  Chowla proximity: −1411 (0.0239), 1592 (0.0323), −1012 (0.0487), −1227 (0.0670). No negatives.
- Conductor coasting L*: q=3: 1.66; q=4: 2.44; q=5: 1.84; q=8: 2.69; q=7, q=11: > 6.
- Sign ledger q=7, L=4.04: arch +0.238; +2 → −0.584; +2,3 → −0.092; full → +0.00158.
- Production hunt |D|≤10⁵ (60,786 characters): min L(½) = +0.00180 at D=14693 (triple-adjudicated
  0.001798/0.001798/0.00179796); records <0.02: 13340 (0.00361), 60357, 90461, −37427, 37901, −28963, −17923.
- Small-value CDF exponent (band [3e4,1e5], 10,633 chars, smallest 250): 1.50 (symplectic 3/2).
- D=14693: γ₁ = 0.0232 (5.7% of mean spacing 0.405); comparator D=14696: L(½)=1.73, γ₁=0.683 (169%).

## Pipeline pathology log (the discipline's record)
1. Trapezoid archimedean quadrature (1.5% deficit) → fake pre-threshold negativity of the ζ
   Weil form (fake RH disproof). Caught by the zero-side oracle (+3.292e−3) and hp pieces (+3.295e−3).
2. Kronecker symbol, even-discriminant branch → L(½, χ₉₀₈) = −0.04 (fake GRH disproof).
   Caught by simultaneous mod-4 oracle failure.
3. Lentz continued-fraction seed → L(½, χ₁₄₆₉₃) = −0.00086 (fake GRH disproof).
   Caught by regression anchors; fixed value +0.00180 confirmed three ways.
Rate: one convincing fake catastrophe per scaling step; three for three caught.
4. (Day two) A containment TEST comparing 1e-64-wide interval enclosures at
   15-digit ambient precision manufactured a phantom 6e-19 discrepancy between
   the two independent archimedean implementations. Caught by component-wise
   adjudication; methods agreed to 24+ digits. Test artifact, not pipeline.
5. (Day three) The m=12 Lean certificate's BRIDGE was false as stated: the
   generator converted 220-bit interval endpoints through mp.mpf at ambient
   dps 15, so the emitted integers carried ~1.46e-17 error against a stated
   delta = 1e-20 (the kernel theorem itself, being about mRat, was never
   wrong). Invisible to all five per-artifact validation layers; caught by the
   CERTIFICATE-COHERENCE ORACLE proposed by the category-theory expert
   (nested certificates at the same L must agree on overlapping blocks to
   their combined rounding budget). Repaired same day: 60-dps conversion,
   full integer chain regenerated and exactly re-verified, coherence now
   PASSES at 5.00e-25 absolute (budget 5e-25 + 5e-29), Lean rebuilt green,
   axioms re-audited. Generator patched; coherence check adopted as a
   standing oracle for all future certificate emissions.
Updated rate: five convincing catastrophes, five caught — two of them by
oracles that did not exist when the error was made. The discipline's lesson
stands: every new validation layer finds the class of error the previous
layers were structurally blind to.

---

# July 25, 2026 — independent verification + the hp margin ladder (second working day)

Fresh environment, fresh session (Claude Code). Dates: the sections above self-date
to July 26, 2026; the machine clock on the day of the original runs and of this
verification read July 25, 2026. Kept as written; noted for the record.

## Verification of everything above (this repo's code, rerun)
- Oracles: ζ on γ₃ at dps 30: both sides 2.0007024351181021347, diff −1.3e−29
  (recorded LHS above ends …21364: 18th-digit transcription drift, identity intact);
  off-resonance diff −8.9e−30; demo settings −4.3e−19 / −5.6e−17 / −2.2e−16. PASS.
- Census [100, 30000]: 35,644 vs 35,643.63; GUE counts 25/90/215/707 vs 38/128/299/971. PASS exact.
- Close pairs: 17143.7865 / gap 0.0353 / bump 0.00215; 7005.0629 / 0.0377 / 0.00397. PASS.
  Scoping correction: by NORMALIZED gap the classic pair is the tighter one
  (0.0421 vs 0.0445); t = 17143.79 is the record of this scan by absolute gap and
  interior ascent only, and far closer pairs are known at large height (Odlyzko-line
  computations). "Record" must always carry the scan-range qualifier.
- DH zero, keyhole eigenvalues/suppressions/nodes, pole flip (ψ_min +0.106→−0.200,
  prime-2 −0.126→+0.131), q=7 ledger (+0.238/−0.584/−0.092/+0.00158), cartography
  leaders, margin escalation anchors (1.75: 3.7750→3.4420e−5; 2.485: →6.7797e−8;
  3.85: →3.2227e−8): all PASS to printed digits.
- Keyhole disclosure: the bottom vector also has nodes at 7.640 and 13.655 that are
  NOT zero ordinates; the documented node list is the in-band matching subset.
- Chowla hunt |D| ≤ 1e5 rerun end-to-end (126 s): min 0.00179796 at D = 14693; the
  top-8 record order reproduces. Fully independent check (fresh Jacobi/Kronecker,
  mpmath Hurwitz row sum, no repo code): L(½, χ₁₄₆₉₃) = 0.00179796153084. PASS.
- Deficit anchors: interpretation pinned as window TOPS with newest prime excluded
  (float m=41): −0.414 for p=2 (matches −0.41); −0.457 / −0.242 / −0.606 / −0.370
  for 3/4/5/7 — sign and magnitude reproduce; exact doc values evidently used
  unrecorded (L, m, exclusion) conventions. Anchor the p=2 value going forward.
- Repo fix: gue_gap_counts used np.trapezoid (numpy ≥ 2 only); now falls back to
  np.trapz. Environment: python 3.12.3, numpy 1.26.4, mpmath 1.2.1.

## hp margin ladder (src/hp_margins.py — x-space kernel; no Simpson, no R-truncation)
- Float arch-matrix error, measured: max entry 4.08e−7 (R = 3000 truncation);
  resulting λ_min bias: stable +0.7–0.9e−9 at every (L, m) tested. The float
  ladder was real Galerkin data with a now-measured error budget.
- p=2 window: L=1.75 hp ladder m=41/61/81/101/121:
  3.77498 / 3.59685 / 3.50265 / 3.44205 / 3.39895 e−5; Richardson (1/m, 1/m²)
  brackets the basis limit at 3.18–3.30e−5. First rung of f(p), beyond quadrature
  doubt. L=1.79: 2.01496e−5 at m=121; limit est. 1.88–1.95e−5.
- p=3 window: L=2.485 hp ladder m=41/61/81/101/121/161/201:
  1.39741e−6 / 4.13636e−7 / 1.52570e−7 / 6.71035e−8 / 3.45007e−8 / 1.24514e−8 /
  5.57117e−9 — stable m^{−3.6} descent, no plateau above 5.6e−9. At m=121:
  n=4 window 2.13832e−8 (L=2.996), p=5 1.47005e−8 (L=3.555), p=7 1.68169e−8 (L=4.025).
  Verdict on §2.8: the near-coincidence at m=101 was neither float noise nor a flat
  envelope — it is a shared genuine basis transient; true interior margins for
  p ≥ 3 lie below 5.6e−9 (Rayleigh–Ritz upper bound), beyond hat-basis reach.
- Threshold approach, p=3 boundary, hp m=81: d = 0.100/0.050/0.025/0.007/0.002 →
  4.070 / 2.541 / 2.057 / 1.744 / 1.712 e−7. The small-d flattening is the m=81
  basis floor (m-ladder at L=2.19: 1.436e−6 / 3.819e−7 / 1.746e−7 / 1.168e−7 at
  m=41/61/81/101, still descending). κ raw 0.49–0.68 (floor-biased LOW);
  floor-subtracted 1.3–1.5. The float-era κ ≈ 0.4 was mostly floor.
- Zero-side inequality on the L=1.75 minimizer: 2Σ_{first 60 γ}|φ̂(γ)|² = 3.6207e−5
  ≤ Q(φ) = 3.7750e−5 (96% captured; the deficit is the γ⁻⁴ hat tail).

## Day two, second session — the spectral ladder, the family port, and the first certificates

### The spectral (Legendre) basis and the operator-level margins (src/spectral_margins.py)
- Basis: orthonormal Legendre on [-L/4, L/4]; Gram = I; overlaps exact (Gauss-Legendre
  on polynomials); same x-space archimedean kernel; parity split S_kj = 0 for k+j odd.
- L=1.75: m=8..48 -> 4.13301/3.24836/3.18972/3.17791/3.16043/3.15316/3.15192/3.14680/
  3.14389e-5. Passes below the hat wall by m=16 and below the hat-only Richardson
  bracket [3.18,3.30]e-5 by m=24 (that extrapolation underestimated its residual —
  corrected in hp_margins docstring). Upper bound f(2) <= 3.1439e-5, limit ~ 3.12-3.14e-5.
- L=2.485 (p=3 window): m=12..64 -> 7.5308e-8, 4.4677e-9, 5.9239e-10, 3.86882e-10,
  3.74714e-10, 3.66564e-10, 3.61910e-10, 3.59571e-10, 3.56788e-10.
  Plunge-then-creep (originally attributed to interior kinks at +-(a - log p)
  from the prime shifts; REVISED 2026-07-26: the pre-registered kink-enrichment
  experiment REFUTED the corner-kink mechanism — snap enrichment does not beat
  plain refinement — the creep is a log-regularized truncation-jump effect,
  Theta(A_L/(m ln m)); see results/experts/PLAN-numerical-analysis.md).
  Tail extrapolation: **f(3) ~ 3.49-3.50e-10**; hard upper bound 3.5679e-10 (m=64).
  Hats at m=201 were still 15x above this.
- Zero-side inequality at (2.485, m=48): 2 SUM_{60} |phihat(gamma)|^2 = 3.10471e-10
  <= Q(phi) = 3.59571e-10 (86%): explicit formula and eigenvalue agree at the tenth
  decimal with no shared code.
- **The measured f(p) ladder** (mid-window operator margins, spectral, Rayleigh-Ritz
  upper bounds at the deepest m):
  | window | L | lam_min (operator est.) | upper bound (deepest m) |
  |---|---|---|---|
  | p=2 | 1.750 | ~3.13e-5 | 3.1439e-5 (m=48) |
  | p=3 | 2.485 | ~3.50e-10 | 3.5679e-10 (m=64) |
  | n=4 | 2.996 | ~4.2e-15 | 4.2265e-15 (m=64) |
  | p=5 | 3.555 | ~2.1e-22 | 2.1774e-22 (m=80) |
  | p=7 | 4.025 | ~1-3e-30 | 2.7922e-30 (m=80, still descending) |
- **The empirical margin law.** A two-parameter fit to the first three windows,
  ln lam ~ a - c e^{L/2}, anticipated the deeper windows but with c drifting
  (10.70/11.24/11.62 per segment). The three-parameter refinement
  **ln lam_min(L) ~ 10.2 - 1.755 e^{L/2} (L/2 + 4.0)**
  (exponent proportional to (T*/2pi)(ln(T*/2pi)+4) at the Nyquist height
  T* = 2 pi e^{L/2}) fits all four solid windows to <1% in the exponent, and then
  survived three tests: interpolation at L=2.30 (never fit: predicted 1.03e-8,
  measured 9.72e-9, 6%), the threshold band (predicted 6.0e-8 at L=2.1942,
  measured 5.77e-8, 4%), and extrapolation to the p=7 window (forecast 1.3e-30
  logged before the m=64/80 runs; measured upper bound 2.79e-30, still
  descending toward it). A constant-toll-per-zero model misfits by 20x.
- **The threshold non-collapse (major reinterpretation of the July 26 2.7).**
  Spectral d-ladder at the p=3 boundary (m=48; m=64 drift 0.35%):
  d = 0.100/0.050/0.025/0.012/0.007/0.003 ->
  2.8216e-7 / 1.3496e-7 / 8.4541e-8 / 6.6549e-8 / 6.1350e-8 / 5.7887e-8.
  The operator margin does NOT collapse at the threshold: it flattens to
  ~5.77e-8, exactly on the smooth law. The hat-era "zero-slack at thresholds,
  lam ~ d^kappa" was the hat basis's own transient, not the form's behaviour.
  At operator level there is no local knife-edge at prime-power thresholds:
  one smooth super-exponential envelope covers windows and thresholds alike.
  (The deficit/rescue ledger — arch+pole alone fails, the newest prime rescues —
  is untouched: that is about the form WITHOUT the needed prime.)

### The family port (hp_margins.py now conductor-aware)
- hp_form(q, D, parity, prime_set) with the odd kernel e^{-3u/2}/(1-e^{-2u}), psi(3/4),
  conductor term log(q/pi), no pole. Zeta path regression: 3.77497984e-5 unchanged.
- q=7 sign ledger at L=4.04, m=41, hp: arch +0.23805387; +2 -> -0.5844069;
  +2,3 -> -0.092107573; full -> +0.0015755882. Matches the float ledger to all its
  digits — the sign ledger is now beyond quadrature doubt.

### The first interval certificates (src/certified_margins.py — M1 first rungs)
- Method: exact-rational hat autocorrelation cubics (Fraction arithmetic), Bernoulli-
  series kernel with rigorous geometric tails (|c_j| <= 4 e^{(2-s)pi}/pi^j), interval
  constants for psi(1/4), psi(3/4), interval Cholesky (lower) + interval Rayleigh
  (upper), mpmath.iv at 220 bits. Trust base: iv elementary-function enclosures.
- Sanity: iv enclosures (widths 1e-63..1e-65) contain the hp tanh-sinh diagonals at
  every k tested. (A first version of this test compared at ambient 15-digit
  precision and manufactured a fake 6e-19 discrepancy — diagnosed as a test
  artifact, the two independent methods agree to 24+ digits. Fake-catastrophe
  counter: four for four caught.)
- **CERTIFIED enclosures (hat basis, m=41):**
  | form | L | certified |
  |---|---|---|
  | zeta | 7/4 | 3.77497970e-5 < lam_min <= 3.77497984e-5 |
  | zeta | 219/100 | 1.43609370e-6 < lam_min <= 1.43609382e-6 |
  | zeta | 497/200 | 1.39740560e-6 < lam_min <= 1.39740567e-6 |
  | chi_{-7}, full primes | 101/25 | 1.57558810e-3 < lam_min <= 1.57558821e-3 |
  First interval-certified window positivities of the program, including the first
  certified family window; ~4 s each.

### LMFDB / literature status of D = 14693 (diligence item closed as far as public sources go)
- LMFDB HAS the character (14693.b, Conrey chi_14693(14692,.), even, primitive,
  conductor 14693) but serves NO L-function for it: /L/Character/Dirichlet/14693/14692
  and /L/1/14693/... both 404; the lfunc_lfunctions API returns empty at that
  conductor. LMFDB's Dirichlet L-function data does not reach q = 14693.
- No published smallest-|L(1/2)| tables over fundamental discriminants located.
  The value is recoverable by anyone with lcalc/Rubinstein-type sweeps, so the claim
  stays "record of our scan, not of mathematics" — but as of 2026-07-25 no public
  source listing it was found.

## Day two, third session — spectral certificates, the family law, and the note

### Certified spectral rungs (src/certified_spectral.py)
- Machinery: unnormalized Legendre basis (Gram = diag(2a/(2k+1)) exact rational);
  the shifted overlaps are UNIVERSAL exact-rational polynomials F_kj(v) (computed
  once in Fractions, cached, L-independent); no hinges; kernel via exact rational
  moments + Bernoulli series with rigorous tails; pole via the all-positive
  modified-spherical-Bessel series; interval Cholesky + interval Rayleigh.
- Cross-check: exact F polynomials vs the GL overlap engine: exact agreement.
- **CERTIFIED (adds to the hat certificates above):**
  | form | L | basis | certified |
  |---|---|---|---|
  | zeta | 497/200 | Legendre m=24 | 3.86870000e-10 < lam_min <= 3.86881560e-10 |
  | zeta | 749/250 | Legendre m=48 | 4.34600000e-15 < lam_min <= 4.34621580e-15 |
  | zeta | 711/200 | Legendre m=40 | 1.79970000e-20 < lam_min <= 1.79972291e-20 |
  The certified ladder now spans 3.8e-5 down to 1.8e-20 — fifteen orders of
  certified window positivity. (Development note: an off-by-one power ladder in
  the H coefficients produced a grossly wrong matrix on first assembly and was
  caught before any claim by the interval Rayleigh check returning an impossible
  negative upper bound.)

### The family envelope law (q = 3, 5, 7; spectral basis; deepest m per point)
- q=3 (D=-3, odd):  L=3: 4.1094e-5 (m=32) | L=4: 7.1100e-10 (m=40) |
  L=5: 3.0714e-18 (m=80) | L=6: 2.5363e-31 (m=96, descending)
- q=5 (D=+5, even): L=3: 2.1269e-3 (m=32) | L=4: 2.0447e-6 (m=40) |
  L=5: 2.0940e-11 (m=48) | L=6: 8.0463e-20 (m=72, descending)
- q=7 (D=-7, odd):  L=4.04: 1.3055e-3 (m=32) | L=5: 7.5699e-7 (m=40) |
  L=6: 1.7659e-12 (m=64) | L=7: 3.1802e-22 (m=96, descending)
- **Universality**: slopes d(ln lam)/d(e^{L/2}/q) = -11.3/-12.1/-11.4 (q=3),
  -12.0/-12.0/-12.3 (q=5), -11.2/-11.5/-12.1 (q=7) vs zeta's -10.7/-11.2/-11.6
  per unit e^{L/2}: the decay rate is one constant b ~ 11-12 in the family
  Nyquist height T*_chi = (2 pi / q) e^{L/2}; conductor, parity, and the pole
  move only the offset. (All deep values are Rayleigh-Ritz upper bounds, so the
  bias is one-sided and the true deep slopes are, if anything, steeper.)
- Cross-basis note: q=7 at L=4.04 — operator margin 1.3055e-3 vs the hat m=41
  Galerkin value 1.5756e-3 (hats 17% high at that m, as elsewhere).

### The note
- ENVELOPE.md drafted at repository root: self-contained summary of the law,
  its validations, the certified rungs, the family universality, caveats, and a
  short cover-email draft. NOT sent anywhere; for the owner to review.

## Day two, fourth session — the law survives everything we threw at it

### Deep extrapolation (two+ windows beyond the fit; dps 70 assembly / 60 solve)
- L=4.25 (n=8 window): spectral m=96: 7.5202e-35 -> m=112: 5.5490e-35, vs law
  prediction 2.2e-35 — within 2.5x at the 1e-35 scale and still descending
  toward it (see figure).
- L=4.50 (n=9 window, THREE windows beyond the fit): m=112: 1.2448e-40 vs law
  prediction 1.7e-41 — within a factor 7 at the 1e-40 scale, m=112 not yet
  converged (Rayleigh-Ritz upper bound, descending). The law is now tested
  over ~35 orders of magnitude, from 3e-5 to 1e-40. Both deep extrapolations
  land ABOVE the law and descend toward it with m — consistent with pure
  convergence bias; a mild upward bend of the true envelope beyond L ~ 4.2
  cannot yet be excluded and is the natural next discriminating measurement.

### The threshold glide (continuity across 2 log 3; spectral m=48)
- L = 2log3 + dL for dL = -0.030..+0.100: 9.3089e-8 / 7.0134e-8 / 5.9542e-8 /
  5.6383e-8 / 5.4861e-8 / 5.1566e-8 / 4.3827e-8 / 3.4203e-8 / 2.0557e-8 / 1.0245e-8.
  Across the threshold itself (dL = -0.001 -> +0.001): ratio 0.973 measured vs
  0.968 predicted by the law's local slope. The margin GLIDES; the rescue is
  invisible in the full form. The knife-edge is dead at operator level.

### The mechanism experiment (src/model_zeros.py): the law is DENSITY, not arithmetic
- The form equals the frame form of exponentials at the zero ordinates; we
  recomputed the frame bound with the ordinates replaced by (i) the smooth
  Riemann-von Mangoldt staircase (right density, perfectly rigid), (ii) Poisson
  arrivals through the same density (right density, clumpy).
- Validation: frame(true zeros, Gcut=180/300/420) = 1.102/2.346/2.690e-10 rising
  toward the form value 3.5957e-10 from below, as the identity demands.
- At fixed Gcut=420, m=48:            true      |   smooth    |  poisson
    L=2.485:                       2.68972e-10  | 2.75124e-10 | 2.89509e-12
    L=2.996:                       2.71352e-15  | 3.17610e-15 | 2.97052e-17
    L=3.555:                       9.90930e-22  | 1.57685e-22 | 8.94928e-23
- **Verdict**: the smooth staircase MATCHES the true zeros (within truncation
  uncertainty); Poisson costs 1.5-2 orders; all three share the decay slope.
  The envelope's decay constant is a functional of N(T) alone — prolate/
  Landau-Widom territory — local statistics enter only the offset, and the true
  zeros sit at the maximally-rigid offset (echoing the below-GUE small-gap
  counts of 2.1). A Hilbert-Polya candidate is constrained by this data through
  its counting function and rigidity class; nothing finer is visible here.

### Family refinements + a spectral family certificate
- q=3, L=5: 3.0714e-18 (m=80, 3% drift — converged-ish); q=3, L=6: 2.5363e-31
  (m=96); q=7, L=7: 3.1802e-22 (m=96). Slopes updated in the section above.
- chi_{-7}, L=5, spectral m=40: **CERTIFIED 7.56900000e-7 < lam_min <=
  7.56991097e-7** (kernel series N=900 for 2a=2.5; 83 s).

### The figure
- results/figures/envelope_law.png: (a) the zeta law with fitted/interpolated/
  threshold/extrapolated points, (b) the four-L-function universality collapse,
  (c) the threshold glide. Palette validated (dataviz six-checks: ALL PASS).

## Day two, fifth session — from measurements to theorems

### Theorem 1 (the Glide Theorem; THEOREMS.md, complete proof)
- lam(L) is NON-INCREASING in L (zero-extension argument — the new primes cannot
  see short-support test functions), and continuous with explicit modulus
  C(l0,l1) (log 1/h)^{-1/2} on compacts — in particular continuous ACROSS every
  prime-power threshold: the knife-edge is now dead by proof, not only by
  measurement. Key self-contained ingredient (Lemma A): via Gauss's integral and
  a Frullani evaluation,
    psi(1/4) + (1/2) log(1+4r^2) <= Re psi(1/4+ir/2)
                                 <= psi(1/4) + (1/2) log(1+4r^2) + 8,
  and |r d/dr Re psi(1/4+ir/2)| <= 2 + pi/2. (Numerically checked: slack in
  [0.136, 2.842], derivative max 2.078.)
- Supporting lemmas with explicit constants: log-weighted energy bound for
  near-minimizers; non-concentration on short intervals (mass <= C/log(1/eps));
  autocorrelation translation modulus C/log(1/Delta); entering-prime edge bound
  (C/log(1/eps))^{1/2}.

### Theorem 2 (machine-checked window of Weil positivity; lean/weilcert)
- **Lean 4 + mathlib, kernel-verified, axioms [propext, Classical.choice,
  Quot.sound] only** (no native_decide, no sorry, no floats):
  every rational 12x12 matrix entrywise within 1e-20 of the explicit mRat
  (= aInt/10^24) has strictly positive quadratic form
  (WeilCert.weil_window_positive). Certificate: integer congruence
  c^2 B = W^T diag(g) W (B = 10^24 mRat - 120000 I), Winv W = f I, g > 0,
  all reduced by the kernel; perturbation via an exact Q Cauchy-Schwarz bound.
  Integer sizes: A <= 24 digits, W <= 101, g <= 1226, c,f ~ 602. Build ~10 s.
- Bridge Proposition (computer-assisted; trust base mpmath.iv, stated):
  the truncated Weil matrix of zeta at L = 497/200 in the unnormalized Legendre
  basis m = 12 lies in that entrywise ball (enclosure widths <= 5e-60, rounding
  <= 5e-25). Corollary: Weil positivity holds, formally verified modulo the
  stated bridge, on an explicit 12-dim test space whose window requires BOTH
  primes 2 and 3 (arch+pole alone has deficit -0.41 there).
- To our knowledge the first kernel-checked positivity window in the
  Weil-positivity program (pending literature check, as always).
- Verification instructions + axiom audit: lean/README-verify.md;
  data regeneration: lean/make_certificate.py.

## Diligence executed (July 25)
- Every post-cutoff citation and event in PROGRAM.md verified real: arXiv:2607.02828
  (Groskin), 2606.09096 (Suzuki), 2602.04022 (Connes), 2605.20695; the Jacobian
  counterexample (Alpöge crediting Claude, July 19–20) and the unit-distance
  disproof (OpenAI model, May 20) both happened.
- NOVELTY KILL — keyhole: arXiv:2605.20224 (Groskin, May 2026) already recovers
  Riemann zeros from the ground state of the truncated Weil form — 307–329 digits
  at cutoff c=100 — via Fourier–Mellin zeros of the CCM rank-one operator. §2.13
  stands as full-pipeline validation of THIS instrument, not as discovery.
- D = 14693 is fundamental (7·2099, ≡ 1 mod 4). Whether it appears in existing
  small-central-value tables (LMFDB, Rubinstein-era) remains UNCHECKED.


## Day three, part 2 (July 26 evening): the bend is REAL — the 4pi cap

Deep-window campaign final (results/agent-deep-windows.md; ladders to m=176,
every rung an RR upper bound, monotone nested bases, no violations):

- **VERDICT: the envelope law bends upward past L ~ 4.3.** Converged deep
  limits (L = 4.25/4.50/4.60/4.75) sit 1.4-2.6x above the best 3-parameter
  refit (7x its residual band). The deep decay rate saturates at the
  universal prolate rate **4pi per unit c = e^{L/2}**, measured to 0.4-1.3%
  three independent ways; the corrected Fuchs-form law
  ln lam ~ A' - 4pi e^{L/2} + p(L/2) blind-predicted the L=4.75 limit to
  0.4%. Onset exactly computable: the old law's local slope crosses 4pi at
  L = 4.32, where deviations begin.
- **Stopping-height protocol (DG Round 2)**: abrupt saturation EXCLUDED
  (w(4.75) = 1.224 < 1.26); scalar shape test favors SMOOTH CAP over drift
  (secant slopes on 4pi, 3-6% below drift, bias headroom <= 0.5%). Formal
  B_smooth certification awaits the vector-level shape test (DG seat).
- **T1' two-horizon consistency (HA Round 2): PASS** — all eleven measured
  stopping heights strictly inside (e T*, e^2 T*), lower margin >= +0.144.
- **Connes/Groskin 126-decade tension RESOLVED**: corrected law at CvS
  c = 100 gives log10 lam in [-529.0, -527.7] vs their ~ -530 (old chart:
  -656). Option (ii) of agent-prior-art.md par. 7.2 — the (L/2+4) log-factor
  was mid-range only. ENVELOPE.md updated (4pi-cap section + resolution).
- The creep-de-biased reading (which would have flattened the bend) lost its
  only pre-registered head-to-head test (L=4.50: geometric +0.09%, creep
  -5.6%) and self-invalidates at L=4.60 (negative extrapolation).
- L=5.50 discriminator: m=152 -> 1.9854e-64, descending, unconverged;
  expected limit 1e-72..1e-75 (extrapolation, labeled); m=168/184 rungs and
  a 5.00 midpoint were still landing at close (runs.csv authoritative).
- Convergence-honesty note: the interim "bias excluded" overclaim was
  corrected (SYNTHESIS.md called it; the L=4.25 staircase proved it right).


## Day three, part 3 (July 26 night): the top target is kernel-checked

Pipeline completion in ONE day for the panel's #1 target: T1(i) killed by
counterexample (Round 2) -> restated as two-horizon T1' -> paper-proved with
all constants explicit (results/experts/T1PRIME.md, onset gap resolved:
bites at every window, unconditional zeta hard caps 13.1->7.7 T*) -> passed
its first data test (eleven measured stopping heights strictly inside
(e, e^2) T*) -> KERNEL-CHECKED: HardHorizon.hard_horizon (Theorem 1,
staircase form, full multiplicity) + HardHorizon.zero_desert (Corollary 2,
strictly stronger than the paper form) in lean/glide/Glide/HardHorizon.lean —
1461 lines, 36 declarations, zero sorry, every theorem on exactly
[propext, Classical.choice, Quot.sound] (independently re-audited by the
coordinator). This is the program's first ANALYTIC formal theorem (mathlib's
Jensen formula instantiated; differentiation under the integral; Holder);
the certificate artifacts now have an analytic sibling. Formalization
by-catch: the paper's "radius selection optional in Lean" claim was FALSE
(Real.log junk value at boundary zeros, a < 1/2) — caught and repaired in
session 1; an analyticOrderAt translation lemma identified as a mathlib gap
worth upstreaming. Remaining: Corollary 1 needs RvM/S(T) in mathlib (months,
external, exactly as the paper's gap-map priced it).

Same evening, FULLINF composite (results/experts/FULLINF.md): F4 certified
class-restricted full-infimum bound >= 1.56e-5 at L=7/4 over an
infinite-dimensional basis-independent class (certification runs m=96/192
in flight); F5 wall theorem — the UNRESTRICTED infimum is provably beyond
the whole split template (a-priori regularity of near-minimizers is the
named missing mathematics); F6 basis no-go — prolate upgrade now
theorem-forced. DG vector-level shape test pre-registered and running.
