# `LTRAD_full`: expanded actual-prime finite audit

**Date:** 2026-08-28  
**Verdict:** the useful exponent regime was not tested nonvacuously, because
its premise is absent by an exact prime-count ceiling at every accessible
scale.  Expanded actual-prime computations found finite constant-one
violations only in the opposite regime `d_dir>c_rad`.  No sampled violation
reaches the useful `c_rad>d_dir` wedge, and no asymptotic conclusion follows
either way.

The observed directional extrema scale approximately like `N^-1/2` over the
small center grid, whereas the full-band radial radii have effective exponents
near `1/4`.  At the selected adverse centers this gives `E roughly R^2`, but
that mnemonic is not center-stable: the effective power ranges from about
`1.93` to `2.43` in the expanded tables, and reaches about `3.2` in the
smallest earlier base-center row.  This is a description of the
preasymptotic laboratory, not evidence for a uniform power law or for the rare
`E>=N^-.001` event required by the proposed strip adapter.

The exponent-frontier replay is
`src/qp_ltrad_full_numeric_audit.py`; unit tests are in
`src/test_qp_ltrad_full_numeric_audit.py`.

---

## 1. What a finite violation means

At one actual half-integer center, let the floating/guarded brackets be

```text
E_lower <= E <= E_upper,
R_lower <= r_+(H_Y;S_Y) <= R_upper.
```

To avoid the reversed positional notation used in older reports, write the
radial conclusion exponent as `c_rad` and the directional premise exponent
as `d_dir`.  For the constant-one finite implication

```text
LTRAD_full(c_rad,d_dir):
E>=N^-d_dir ==> r_+(H_Y;S_Y)>=N^-c_rad,
```

the brackets prove its premise whenever

```text
d_dir >= d_min := -log(E_lower)/log N,
```

and prove failure of its conclusion whenever

```text
c_rad < c_max := -log(R_upper)/log N.
```

Thus the definite finite-violation rectangle is

```text
d_dir>=d_min,  0<c_rad<c_max.                       (1.1)
```

This is only a floating diagnostic.  The validation-grid gap is guarded by
the exact derivative estimates in `qp_radialization_lab.py`, but HiGHS and
the cosine evaluations are not interval-certified.  More importantly, a
finite constant-one violation does not refute a theorem with asymptotic
onset, fixed constants, or `N^o(1)` slack.

---

## 2. Expanded base-center run

The original lab stopped at `N=1800`.  The same actual prime-power shell and
full band were run at larger base centers, with coarser but still analytically
guarded phase meshes.

| `N` | prime powers / primes | full radius bracket | arbitrary-interval `E` | `d_min` | `c_max` | effective `E=R^lambda` |
|---:|---:|---:|---:|---:|---:|---:|
| 2400 | 132 / 126 | [.169388,.170241] | .0135677 | .55248 | .22748 | 2.43 |
| 3000 | 151 / 148 | [.160979,.163755] | .0123112 | .54922 | .22599 | 2.42 |
| 4000 | 195 / 191 | [.144626,.147080] | .0111062 | .54259 | .23110 | 2.34 |

Every violation rectangle (1.1) lies strictly in `d_dir>c_rad`.  In
particular, none intersects `c_rad>d_dir`.

---

## 3. Center scan and the most adverse sampled rows

For `Y/N` in the grid `1.0,1.2,...,2.4`, the largest sampled directional
values were:

| `N` | winning sampled `Y/N` | `E` | `sqrt(N) E` | `d_min` |
|---:|---:|---:|---:|---:|
| 600 | 2.2 | .0367288 | .900 | .51653 |
| 1000 | 2.4 | .0308950 | .977 | .50337 |
| 1800 | 2.4 | .0231748 | .983 | .50226 |
| 3000 | 2.2 | .017758 | .973 | .50346 |

This small grid is strikingly consistent with `E asymp N^-1/2`, the scale
expected for an extreme of largely incoherent prime phases over polynomially
many effective trials.  It is not an asymptotic fit and does not constrain an
exceptional event forced by a hypothetical zero.

Full radial brackets were recomputed at the first three adverse centers:

| `N,Y` | full radius bracket | `c_max` | effective `E=R^lambda` |
|---:|---:|---:|---:|
| 600,1320.5 | [.209809,.210604] | .24352 | 2.12 |
| 1000,2400.5 | [.169408,.169703] | .25677 | 1.96 |
| 1800,4320.5 | [.141128,.142240] | .26019 | 1.93 |

Changing either endpoint of the tight displayed radius brackets changes the
reported powers only in the last few hundredths; changing the center has a
much larger effect.  Thus `E roughly R^2` is robust to bracket-endpoint choice
on the adverse rows, but not to center choice.

Again `d_min>c_max` in every row.  These rows do give, for example, a finite
constant-one violation of `LTRAD_full(.20,.60)`: at `N=1000,Y=2400.5`,

```text
E >= .030895 > 1000^(-.60)=.015849,
r_+ <= .169703 < 1000^(-.20)=.251189.
```

This is not a counterexample to the target pair and has no asymptotic force.
It merely confirms that an unrestricted claim for arbitrary exponent pairs
would already be false at small actual-prime scales.

---

## 4. The target premise is exactly unavailable

At `N=1000,Y=2400.5`, the deliberately weak useful benchmark
`c_rad=.0189,d_dir=.001` has

```text
observed E / N^(-d_dir)        = .03111,
prime-count ceiling / N^-d_dir = .12687,
R_upper / N^(-c_rad)           = .19337.
```

The conclusion would fail at this finite center, but the premise is
impossible even before phases are considered: for every interval,

```text
E <= (# shell primes)/N = .126 < N^(-.001)=.9931.
```

The same obstruction applies to `d=.019`, whose threshold is about `.877`.
This is structural, not a failure to search enough heights.

For calibration only, the prime number theorem model gives

```text
# shell primes / N
  approximately 2 (Y/N) sinh(.2) / log Y.
```

At the largest allowed center ratio `Y/N=2 exp(.2)`, this count first matches
`N^(1-d)/N` at approximately

```text
d=.019: log10 N = 130.93,
d=.001: log10 N = 3967.99.
```

At the base center the corresponding values are about `155.16` and
`4400.80`.  These are PNT-model crossover estimates, not rigorous prime-count
thresholds.  They explain why direct numerical testing of the useful premise
is not a realistic program.

---

## 5. Transverse-return check

The calibrated broad-interval transverse LP was also extended:

| `N` | broad mass `E` | probability depth `D` | transverse bracket `s_v` |
|---:|---:|---:|---:|
| 1200 | .0180642 | .33870 | [.3580,.3630] |
| 1800 | .0140059 | .30745 | [.2855,.2987] |
| 2400 | .0135677 | .33227 | [.2411,.3148] |

The last upper bracket is loose at the coarser exchange mesh.  The lower
endpoints are legal finite-pool transverse returns (up to reported LP
residuals), so the calibrated residual is not visibly trapped at these
scales.  These witnesses again have `E` of effective exponent about `.55`,
not the target `.001`.

---

## 6. Disposition

```text
expanded actual-prime base-center run through N=4000:       DONE;
allowed-center directional grid through N=3000:             DONE;
useful d_dir=.001 or d_dir=.019 premise tested nonvacuously:  NO;
finite constant-one violations with d_dir>c_rad:              FOUND;
finite violation in the useful c_rad>d_dir wedge:             NOT FOUND;
adverse-center small-scale mnemonic:                         E roughly R^2;
uniform center-stable E-versus-R power law:                  NOT OBSERVED;
asymptotic actual-prime LTRAD_full(c_rad,d_dir):              OPEN;
QP-to-strip or uniform strip:                                NOT PROVED.
```

Replay tests:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_ltrad_full_numeric_audit.py \
  src/test_qp_radialization_lab.py \
  src/test_qp_transverse_sharpness_lab.py \
  src/test_qp_ltrad_hereditary_gate.py
```

The focused run reports `24 passed`.
