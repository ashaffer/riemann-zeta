# Local rough-Voronoi selector lab: hostile audit

**Date:** 2026-08-13  
**Binary verdict:** **PASS AFTER PATCH** as an exact finite diagnostic;
**NO ASYMPTOTIC CLOSURE**.

## Exact object and normalization

Let the permanent shell barriers be the first and last primes in `[Y,2Y]`.
For `nu_z` the endpoint-trapezoid measure on

```text
{barriers} union {n:P^-(n)>z},
```

the program forms the actual-mass signed increment

```text
Delta_P=nu_(2P)-nu_P.
```

Complete post-`q` bands `P>=q` use the precomputed increment. For
`P<q<=2P`, the exact q-first increment is `nu_(2P)-nu_q`, not `Delta_P`;
this unique crossing band is now computed and included. The threshold ladder includes
the terminal band whose upper cutoff reaches every possible least prime
factor in the shell. The rational selector enforces exactly

```text
Y^(1537/10000)<q<=min(H,Y^(33/133)).
```

At center `x`, let

```text
w(n)=max(0,1-|n-x|/H),
delta(r)=sum_(n=r mod q) w(n) Delta_P({n}).           (1.1)
```

Here `H=Y/sqrt(T)` is the tent half-width, its support diameter is `2H`, and
the normalization is `H`, the continuum integral of the tent. The stored
twice-mass convention is divided by two before (1.1). The two reported
coefficients are exactly

```text
D_P(a/q)=sum_r delta(r) exp(+2*pi*i*a*r/q),
L_P(T)=sum_n w(n) Delta_P({n}) exp(+i*T*log(n/x)).   (1.2)
```

The signs agree. Removing the constant logarithmic phase does not affect
magnitudes or coherent sums over `P`. No claim is made that the two phases
are uniformly close: logarithmic curvature is order one across this tent.

For every row the code also computes, in actual mass,

```text
E2=sum_r |delta(r)|^2,
C(s)=sum_r delta(r) conjugate(delta(r+s)),
E4=sum_s |C(s)|^2.                                  (1.3)
```

The independently tested identities and the two analytic target summands are

```text
sum_a |D_P(a/q)|^2=q E2,        target L2=(q/H) E2,
sum_a |D_P(a/q)|^4=q E4,        target L4=(q/H^3) E4. (1.4)
```

## Defects patched

1. Forced composite endpoints `Y,2Y` were replaced by permanent prime
   barriers, and every tent is certified to lie between them.
2. The condition `q>Y^beta` now uses `q>floor(Y^beta)`. The previous
   `ceil` plus strict inequality could omit one legal integer denominator.
3. The geometric cutoff ladder previously could stop before the terminal
   SPF band. It now stops only after `2P>=floor(sqrt(2Y))`.
4. Precomputed `nu_(2P)-nu_P` rows with `P<q` are excluded. The unique
   crossing band is computed separately as `nu_(2P)-nu_q`.
5. Both the reduced frequency numerator `a mod q` and the lifted numerator
   approximating `T/(2*pi*x)` are serialized, so the Dirichlet certificate
   is reconstructible.
6. Complex rational/log components and the exact `L2/L4` ledgers in (1.4)
   were added. The selected Fourier coefficient reconstructed from the
   residue vector agrees to at most `4.50e-14` in the full scan.
7. The selector now enforces the live upper cap `q<=Y^(33/133)`. The old
   scan searched all the way to `H` and its lower-height rows were outside
   the sole target whenever `H>Y^(33/133)`.

## Finite scan

The schema-v4 scan has 233 selected blocks and 1483 complete-or-crossing rows for

```text
Y=10^4,3*10^4,10^5,3*10^5,10^6,
T=Y^.85,Y^1,Y^1.2,Y^1.5.
```

All block certificates pass. No in-range selector was found at `T=Y^.85`
among the deterministic probes, and only 9 were found at `Y=10^4,T=Y`;
the other 14 parameter pairs filled all 16 requested blocks. Absence from
this finite search is not a theorem that such a selector cannot occur.

For each sampled block, the table coherently sums the complex rows over all
complete `P>=q` bands and reports the empirical 90th percentile of
`Y^kappa |sum_P D_P|/H` and its true-log analogue. The last two columns are
only representative projections: `(Y/H)` times the sampled mean target
summand in (1.4), divided by `Y^(1-2kappa)` or `Y^(1-4kappa)`.

| `Y=10^6`, height exponent | `H` | median `q/H` | rational p90 | log p90 | projected L2 ratio | projected L4 ratio |
|---:|---:|---:|---:|---:|---:|---:|
| `1.0` | `1000` | `.0190` | `.2471` | `.2428` | `.3428` | `.00382` |
| `1.2` | `251` | `.0657` | `.3700` | `.3692` | `1.264` | `.0459` |
| `1.5` | `31` | `.4677` | `.9506` | `.9397` | `6.259` | `2.598` |

Across the five scales, the projected L2 ratio lies in `.327--.533` at
height exponent `1`, `.993--1.264` at exponent `1.2`, and `5.56--8.65` at
exponent `1.5`. This is consistent with the exact physical-diagonal
obstruction becoming acute only as `q/H` reaches block scale. The
corresponding projected L4 ranges are `.00382--.0257`, `.0452--.165`, and
`2.60--8.57`: `L4` is much less taxed through exponent `1.2`, but the top
finite-height rows emphatically do not demonstrate closure. The exact
common-height `L4` estimate remains open.

These projections are deterministic, tiny-sample diagnostics, not estimates
with statistical error bars. They include the exact crossing band, use finite tents
and at most 16 selected centers per parameter pair, and extrapolate a sampled
selected-block mean to all `Y/H` possible blocks even when most probes have
no in-range denominator. Neither a ratio below one nor agreement between
the rational and logarithmic columns proves a power saving.

## Companion analytic audit

The new hard-block counterexample to the arbitrary-selector `L2` hypothesis
passes hostile audit. At the top scale `H=Y^(33/133)`, take a range-legal
`q=floor(H)` and blocks of `q` consecutive sites. Residues are injective;
every retained semiprime `pr` with

```text
Y^.30<p<=Y^.31,  r prime,  Y<pr<=2Y
```

contributes a distinct negative atom of mass at least one in exactly one
post-`q` band. PNT gives `>>Y/log Y` such atoms, while the audited long-edge
and crossing-edge losses are `o(Y/log Y)`. Hence the `L2` left side is
`>>Y/log Y`, contradicting `Y^(1-2kappa+o(1))`.

The scope is strict. This refutes the range-uniform frozen hard-block
theorem. It does not show that one common height selects those denominators
on the required blocks, and it does not by itself transfer the lower bound
through an arbitrary tent taper. Its diagonal lower bound also does not
contradict the `L4` target.

## Reproduction

```bash
PYTHONPATH=src python3 -m unittest -v \
  src/test_local_rough_voronoi_selector_lab.py
PYTHONPATH=src python3 src/local_rough_voronoi_selector_lab.py \
  --scales 10000,30000,100000,300000,1000000 \
  --height-exponents 0.85,1.0,1.2,1.5 --block-samples 16 \
  --output /tmp/local_rough_voronoi_selector.json
python3 results/verify_zeta23_local_rough_voronoi_selector_lab.py \
  --json /tmp/local_rough_voronoi_selector.json
```

No zero-free strip is claimed.
