# Event-window old/collar cross-ratio experiment

Status: encouraging arithmetic-side numerical evidence, not a certified
operator inequality.

## Quantity tested

For consecutive prime-power support thresholds, the script constructs smooth
compact polynomial-bump bases for the old interval and the two boundary
collars. It evaluates the arithmetic Weil matrix using the exact pole vectors
and the Fourier multiplier

`Re ψ(1/4+iπξ) - log π - Σ_active 2Λ(n)/√n cos(2π log(n) ξ)`.

No zeta zeros or RH assumption enter the calculation.

For positive old and collar blocks `A,D` and cross block `C`, it computes

`||A^(-1/2) C D^(-1/2)||`.

The sharp Schur condition is that this ratio be at most one.

## Results

| scan | events | old degree | collar degree per side | worst ratio |
|---|---:|---:|---:|---:|
| support `<=2` | 23 | 8 | 4 | `0.114` |
| refined support `<=2` | 23 | 12 | 6 | `0.149` |
| support `<=3` | 97 | 8 | 4 | `0.160` |
| support `<=4` | 464 | 8 | 4 | `0.188` |

No tested old or collar block had a negative eigenvalue. The ratio distribution
through support four had median about `0.103`, 99th percentile about `0.168`,
and maximum about `0.188`.

This is the first numerical evidence in the program for a substantial margin
in the genuinely decisive relative cross estimate.

## Important caveat

The support-three and support-four scans use a fixed Fourier cutoff. Very thin
collars have frequency scale `1/(b-a)`, so their computed smallest eigenvalues
eventually collapse toward zero because positive high-frequency energy is
omitted. The smooth old basis has far less high-frequency mass, suggesting
that restoring the tail should principally increase the collar diagonal and
reduce the normalized ratio, but this has not been interval-certified.

The evidence therefore supports, but does not prove, a uniform leakage margin.
The next analytic target is a scale-adapted uncertainty estimate that captures
the omitted collar tail and bounds the old--collar cross by the same energy.

## Artifacts

- `src/event_cross_ratio.py`
- `results/event-cross-ratios.csv`
- `results/event-cross-ratios-refined.csv`
- `results/event-cross-ratios-support3.csv`
- `results/event-cross-ratios-support4.csv`
