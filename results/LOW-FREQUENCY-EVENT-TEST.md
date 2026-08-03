# Low-frequency event test

Status: numerical obstruction to a proposed sufficient mechanism; not a
counterexample to RH.

## 1. High-frequency certificate

For a single prime-power activation, RHBridge now proves the combined symbol
is nonnegative on `|ξ| >= 5`, conditional only on two narrow, independently
certifiable numerical facts:

- `2 Λ(n)/sqrt(n) <= 3/2` for every prime power;
- the archimedean multiplier at `ξ = 5` is at least `3/2`.

Digamma monotonicity then makes the estimate uniform outside the band.

## 2. Low-frequency finite model

For every prime-power event `n` at support `a = log(n)/2`, the script
`src/low_frequency_event_operator.py` forms the Galerkin matrix on the first
Legendre modes for

`pole + integral_(|ξ|<=5) [A(ξ) - 2Λ(n)/sqrt(n) cos(2π log(n) ξ)] |F(ξ)|² dξ`.

The pole term uses the exact rank-two vectors `exp(±x/2)`. Fourier and physical
integrals use independent Gauss--Legendre quadrature.

## 3. Outcome

At degree 20, scanning 465 prime powers through support `4` found a negative
lowest eigenvalue at every event. The worst sampled event was near `n = 2971`,
`a = 3.99833`, with eigenvalue approximately `-49.1` after refined quadrature.

Convergence checks at degrees 12--28 gave:

| event | degree 12 | degree 28 |
|---|---:|---:|
| `n=2` | `-2.83e-6` | `-3.93e-6` |
| `n=11` | `-1.78808` | `-1.78820` |
| `n=2971` | `-49.10485` | `-49.10490` |

The negative values are stable enough to reject separate positivity of the
low-frequency block as a research strategy. They are not counterexamples to
the full Weil form: the omitted positive high-frequency contribution can
compensate them.

## 4. Structural simplification and revised target

A stronger exact observation emerged during the test. Any prime power newly
activated beyond an old support `a` has `log(n) >= 2a`; hence its translate has
zero overlap with `[-a,a]`. RHBridge now proves that the activation loss on the
embedded old block is identically zero. Old-block positivity therefore
propagates exactly; only collar and old--collar cross interactions remain.

The separately-positive low-block strategy is abandoned. The viable successor
is a coupled uncertainty estimate: negative low-frequency collar energy must
be controlled by its unavoidable positive high-frequency energy, together
with the pole term and relative cross estimate.

Artifacts:

- `results/low-frequency-events.csv`
- `results/low-frequency-worst-witness.npz`
