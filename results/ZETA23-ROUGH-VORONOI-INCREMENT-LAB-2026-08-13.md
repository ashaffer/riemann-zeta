# Rough-Voronoi dyadic-increment lab

**Date:** 2026-08-13  
**Status:** exact finite residue/Fourier instrument; numerical evidence only.

## Object measured

For

```text
R_P={n in [Y,2Y]:P^-(n)>P}
```

with prime shell barriers, let `nu_P` be the endpoint-trapezoid (Voronoi)
mass measure.  The tool computes the exact integral residue vector of

```text
Delta_(P,q)=2(nu_(2P)-nu_P) mod q
```

and its primitive finite Fourier transform.  This is the same dyadic
rough-measure increment obtained by telescoping the SPF stages `P<p<=2P`
before using Cauchy or the large sieve.  It is a **whole-shell surrogate**
for the actual curvature-block vector `Delta_(I,P)`, not that localized
vector itself.  The factor `2` is only the repository's integral twice-mass
convention; the Fourier ledger restores the factor `1/2`.  Consequently its
Fourier fields are in actual-mass normalization, while a raw twice-mass
`L2` norm or correlation energy must be divided by `4` or `16`, respectively,
before comparison with the analytic `L2/L4` hypotheses.

Implementation:

- `src/rough_voronoi_increment_lab.py`
- `src/test_rough_voronoi_increment_lab.py`

The code certifies total-mass cancellation and the exact finite `L2` and
`L4` Parseval identities on every row.

## Scale scan

The automatic scan used prime moduli in

```text
Y^(1537/10000)<=q<=Y^(31/125)
```

and dyadic roughness thresholds starting just above `q`.  The displayed run
exhausted the prime moduli in that range and produced 25 rows through
`Y=10^6`.  If `M(Y,q,P)` denotes the largest primitive Fourier
coefficient divided by the shell length, the diagnostic quantity below is
`q M`.

| `Y` | rows | max `q M` | median `q M` | min empirical `-log(M)/log(Y)` |
|---:|---:|---:|---:|---:|
| `10,000` | 2 | `.209335763` | `.174302040` | `.344531643` |
| `30,000` | 4 | `.200895041` | `.168921314` | `.312592157` |
| `100,000` | 5 | `.199317128` | `.132250692` | `.341615118` |
| `300,000` | 6 | `.219824481` | `.131463803` | `.310257259` |
| `1,000,000` | 8 | `.218415813` | `.128048747` | `.283684768` |

Thus the worst observed coefficient is below `.220/q` after normalization.
The quantity `q M` varies less than the displayed empirical power in this
small experiment, but the moduli are tiny and the sample does not
statistically distinguish `q^(-1)` from nearby profiles.

## Interpretation boundary

The scan is compatible with the conjectural `q^(-1)` profile predicted by
the complete finite-wheel model.  It is not evidence for the localized
theorem at the required strength: its interval has length `asymp Y`, whereas
the target vectors live on curvature blocks of length `H=Y^h` with `q` as
large as `H`; it samples only prime moduli, only early roughness bands with
`P<=Y^.248`, and not the full post-`q` tail.  It therefore does **not** prove
a uniform profile on growing intervals, does not cover a height-selected
varying-modulus theorem, and does not supply the selector-stable `L2/L4`
power estimate needed by the antenna.  Numerical stability cannot replace
control of a single exceptional primitive numerator.

The exact theorem target remains the weighted residue-dispersion bound in
`ZETA23-WEIGHTED-ROUGH-TRANSITION-RESIDUE-DISPERSION-GATE-2026-08-13.md`.

## Reproduction

```bash
python3 src/test_rough_voronoi_increment_lab.py
python3 src/rough_voronoi_increment_lab.py \
  --scales 10000,30000,100000,300000,1000000 \
  --exhaustive-q --output /tmp/rough_increment_full.json
```

No zero-free strip is claimed.
