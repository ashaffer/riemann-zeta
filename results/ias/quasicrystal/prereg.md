# PRE-REGISTRATION — the two-scale (incommensurate two-curve) quasicrystal test

Quasicrystal seat, IAS panel Round 1. Logged BEFORE the script was run.
Date: 2026-07-26. Script: `two_scale_test.py` (this directory). Budget: ≪ 30 CPU-min.

## Object

Γ_union = Γ_{E₁} ∪ Γ_{E₂} (multiset union of zero-ordinate sets), where
E₁: y² = x³ + x + 1 over F₅ (N₁ = 9, a = −3, wall 4·ln 5 = 6.4378) and
E₂: y² = x³ + x + 1 over F₇ (point count computed in-script by brute force;
hand count gives N₁ = 5, a = +3, wall 4·ln 7 = 7.7836). ln 7/ln 5 is
irrational: the union is a genuine two-frequency Fourier quasicrystal —
support = union of 4 arithmetic progressions on TWO incommensurate period
lattices, spectrum in ℤ·ln 5 + ℤ·ln 7 (dense). This is the minimal world in
which the program's "fifth obstruction" (ℚ-linear independence of the log
prime powers; PLAN-algebraic-geometry §1.4 item 4) is switched ON while
every other ζ feature (archimedean place, pole, growing density) stays OFF.

Instrument: frame form Q_L(φ) = Σ_{γ∈Γ}|φ̂(γ)|² on unit φ ∈ L²[−L/4, L/4],
orthonormal Legendre Galerkin (m = 48, 64), height truncation H = 2000
(H = 4000 at the two deepest L and for drift checks). Rayleigh–Ritz gives
λ_m ≥ λ_true(truncated Γ); truncation deletes positive rank-ones so biases
the value DOWN vs the full Γ. Positivity of a converged measured value is
therefore evidence (not proof) for the true form; flatness/decay comparisons
at matched settings are the real readout.

## Landau bookkeeping (the basis of the predictions)

Each curve alone: density ln q/π, individual wall L = 4 ln q (verified to
six digits by the AG seat). Union: density (ln 5 + ln 7)/π, predicted
combined wall L_w = 4·ln 35 = 14.2214. In the inter-wall regime
L ∈ (7.784, 14.221) each curve alone is PAST its wall (its own form has a
kernel); any positivity of the union is carried entirely by
incommensurability (Weyl equidistribution of one lattice's phase against
the other's Zak fibers).

## Pre-registered predictions

P-A (incommensurability sustains positivity). At L = 9.0 — both curves
individually past-wall by ≥ 1.2 — the union margin is strictly positive and
stable: m-drift (48→64) < 5% and H-drift (2000→4000) < 25%. Point estimate
(LOW confidence): λ ∈ [10⁻⁵, 10⁻²]. The positivity + stability claim is the
HIGH-confidence part.

P-B (the glide is restored by incommensurability). The single-curve margin
is a flat staircase between thresholds (AG-1, proved + measured). Union
thresholds near the test window: 2·2·ln 7 = 7.784 and 2·3·ln 5 = 9.657. On
the threshold-free interval L ∈ [8.0, 9.5], the union margin is STRICTLY
DECREASING with total drop ≥ 25%, while the single-curve control on a rung
interior is flat to < 1% at the same settings. I.e.: no archimedean place is
needed for a glide — incommensurability alone destroys the flat rungs.
(This refines PLAN-algebraic-geometry §1.3(iii): "no archimedean place ⇒ no
glide" is a statement about PERIODIC sets, not about function fields per se.)

P-C (decay toward the combined wall). λ decays monotonically (up to < 5%
instrument jitter) from L = 9.0 to L = 13.5, spanning ≥ 2 orders of
magnitude — OR bottoms out at the H-truncation floor, which must then be
exposed by the H = 2000 → 4000 drift at L = 13.5 exceeding 25%. Escape
hatch stated in advance: values below ~10⁻⁶ at H = 2000 are floor-suspect.

P-D (control / conventions oracle). Single E₁/F₅ at L = 5.0 and L = 6.0
(same rung interior): both equal (2 − 3/√5)·ln 5 = 1.0595883 to < 1% and to
each other to < 0.5%. If this fails, everything above is void until the
instrument is fixed (program law: bug until an oracle rules otherwise).

P-E (past-wall null). Union at L = 15.0 > L_w: measured value < 10% of the
L = 12.5 value and still falling with m — consistent with λ ≡ 0 past the
combined Landau wall (no converged positive residue).

## What each outcome means

- P-A + P-B + P-C as predicted: the two-frequency quasicrystal has a
  strictly-decreasing positive margin between the individual walls and the
  Landau wall — the minimal measured instance of "incommensurability buys
  completeness", the mechanism ζ needs at every scale. Feeds lemma QC-1 in
  the seat file; hands the renormalization seat a small-divisor observable.
- P-B fails (flat rungs persist): the union still fibers in some hidden way;
  QC-1(ii) dies; the glide really is archimedean-only. Report as a kill.
- P-A fails (collapse at L = 9): incommensurate unions of critical-ish APs
  are NOT complete much beyond the larger individual wall — Landau density
  is far from sufficient here; QC-1(i) dies as stated and the ζ-side moral
  inverts (incommensurability would be WEAKER than density bookkeeping
  suggests — a finding worth more than the confirmation).
