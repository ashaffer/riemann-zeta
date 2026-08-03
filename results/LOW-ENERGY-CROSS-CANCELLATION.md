# Low-energy old-sector cross cancellation

Status: the sector reduction is proved in Lean; the combined-kernel
cancellation has strong numerical evidence but is not yet an operator proof.

## Corrected experiment

The earlier event scan used a small smooth-bump old basis.  At larger support
that basis misses the extremely low-energy old modes.  The new script obtains
the lowest generalized eigenvectors from the high-precision x-kernel hat
matrix, embeds them into the next event window, and computes their collar
coupling as three separate pieces:

`pole cross + archimedean cross - prime cross`.

No zeta zeros or RH assumption are used.

For the first three event windows at old dimension 61, the ground-mode data
are:

| event | old eigenvalue | normalized total ratio | cancellation factor |
|---:|---:|---:|---:|
| 0 | `3.60e-5` | `0.759` | `3.31e-3` |
| 1 | `3.69e-7` | `0.292` | `1.01e-4` |
| 2 | `2.46e-7` | `0.147` | `4.27e-5` |

Here the cancellation factor is the collar-dual norm of the combined cross
row divided by the sum of the three component dual norms.  At the tight first
event it is stable as the old dimension rises:

| old dimension | normalized ratio | cancellation factor |
|---:|---:|---:|
| 41 | `0.745` | `3.40e-3` |
| 61 | `0.759` | `3.31e-3` |
| 81 | `0.772` | `3.28e-3` |

This is evidence for real combined-kernel cancellation, not a Fourier-cutoff
artifact.  It is three-way cancellation involving the pole term; describing
it as solely prime--archimedean cancellation would be inaccurate.

## Proved sector isolation

Fix a threshold `mu`.  If an old vector satisfies

`Q(old) >= mu ||old||^2`,

the collar satisfies `Q(v) >= d ||v||^2`, the ordinary cross estimate is
`|B(old,v)| <= c ||old|| ||v||`, and `c^2 <= mu d`, then Lean proves

`B(old,v)^2 <= Q(old) Q(v)`.

Thus ordinary estimates handle the high-energy sector.  Only vectors below
the threshold require a cancellation theorem.  The next analytic target is a
low-sector rigidity statement: low Weil energy must force the three cross
functionals to satisfy their observed near-linear dependence.

Artifacts:

- `src/low_energy_cross_cancellation.py`
- `results/low-energy-cross-cancellation.csv`
- `results/low-energy-cross-cancellation-refined.csv`
- `RHBridge/LowEnergySector.lean`
