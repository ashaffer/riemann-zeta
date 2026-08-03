# Combined reserve-symbol scan

Status: numerical diagnostic, not a positivity proof.

The tested symbol for a support step `a -> b` is

`Re ψ(1/4 + iπξ) - log π - Σ_new 2 Λ(n)/√n cos(2π log(n) ξ)`.

This is the archimedean multiplier plus the exact activation-defect symbol
minus the activation shell mass.

## Fixed-width steps fail

For steps of width `0.1`, the number and total weight of newly activated prime
powers grow rapidly. By support near `a = 4`, individual shells contain about
50--60 prime powers and total weights around 15--18. The combined symbol was
still strongly negative at sampled frequencies as large as `ξ = 12`.

Thus a fixed-width propagation scheme is not credible under this estimate.
Archimedean growth is logarithmic, while a fixed logarithmic support slab
contains exponentially increasing arithmetic weight.

## Event-driven steps remain plausible at high frequency

Crossing one prime-power threshold at a time changes the picture. Scanning all
465 prime powers through `exp(8)`, with `ξ` sampled in `[0,12]` at spacing
`0.01`, found:

- the largest last-negative frequency was approximately `4.18`, for `n = 11`;
- every sampled single-event symbol was positive for `ξ >= 5`;
- among `n >= 100`, the largest last-negative frequency was approximately
  `2.39`.

This suggests a potentially uniform high-frequency estimate for event-driven
activation, with a conservative candidate cutoff near `|ξ| = 5`.

## Consequence for the roadmap

The propagation scale should follow individual prime-power activation events,
not fixed support increments. Prime-shift defects may control the high-frequency
sector uniformly on that scale. The decisive remaining problem is the bounded
low-frequency sector, where the defect symbol vanishes at zero and the pole
term must be combined with the archimedean form without assuming positivity.

Reproduce with:

```text
python3 src/combined_reserve_scan.py --stop 4 --step 0.1
python3 src/combined_reserve_scan.py --stop 4 --event
```
