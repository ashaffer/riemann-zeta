# Random-sieve resonance capacity

Status: a fundamentally different density notion survives its first gate,
2026-08-01.

Assume hypothetically that `rho=beta+i gamma` is a zero of zeta with
`1/2<beta<1`.  Choose a parameter

`1-beta < a < 1`,

and independently select each prime `p` with probability

`theta_p = p^(-a)`.

Let `P` be the random selected set and retain integers having no prime factor
in `P`.  Define the restricted Möbius function

`mu_P(n) = mu(n) 1_((n, product(P))=1)`,

where the indicator means that no selected prime divides `n`.

## 1. The retained integers have positive ordinary density

Since

`E sum_(p in P) 1/p = sum_p p^(-a-1) < infinity`,

the random sum is finite almost surely.  Hence

`delta_P = product_(p in P) (1-1/p) > 0`

almost surely.  Unlike a primorial multiple channel, this construction has not
collapsed onto a zero-density subset.

## 2. The hypothetical pole survives almost surely

For `Re(s)>1`, Euler products give

`F_P(s) = sum_n mu_P(n)n^(-s)`

`       = zeta(s)^(-1) product_(p in P) (1-p^(-s))^(-1)`.

For every `sigma>1-a`,

`E sum_(p in P) p^(-sigma) = sum_p p^(-a-sigma) < infinity`.

Thus the selected-prime Euler product converges absolutely, locally uniformly,
and to a nonzero analytic function on `Re(s)>1-a`, almost surely.  Because
`beta>1-a`, it is analytic and nonzero in a neighborhood of `rho`.
Consequently `F_P` has a pole at `rho` of exactly the same order as
`1/zeta`, for almost every random sieve.

This proves infinite-depth resonance propagation through a continuum of
positive-density multiplicative restrictions.

## 3. The branching entropy has positive multiplicative-scale rate

Up to primes `p<=y`, the selector entropy is

`H_y = sum_(p<=y) h(p^(-a))`,

where `h(t)=-t log t-(1-t)log(1-t)`.  Let the expected logarithmic dilation
cost be

`C_y = E log product_(p<=y, p in P) p`

`    = sum_(p<=y) p^(-a) log p`.

Since `h(p^(-a)) = a p^(-a) log p + O(p^(-a))`, the prime number theorem
gives

`H_y/C_y -> a > 0`,

while both quantities diverge on the scale `y^(1-a)`.  The construction
therefore has positive entropy per unit of its *typical logarithmic
multiplicative cost*, even though it has zero entropy relative to the maximal
primorial cost `theta(y)~y`.

This is the appropriate nonuniform density: sparse random exclusions, not
uniform mass on all primorial branches.

## 4. What this does and does not prove

This is a genuine improvement over the failed primorial tree:

- the retained integer set has positive natural density;
- the selector has unbounded entropy at positive multiplicative-scale rate;
- the off-line resonance survives almost surely with a nonzero random Euler
  multiplier.

It does not yet contradict known cancellation theorems.  The different
restricted functions are strongly correlated, and their random Euler
multipliers have finite local variation.  Almost-all short-interval estimates
allow a normalized resonance of size `X^(beta-1)`.

The next load-bearing gate is an ensemble inverse theorem:

> Can one convert the common pole across this positive-entropy family of
> positive-density random sieves into mutually independent information or
> orthogonal energy growing like `H_y`?

If the pole signal occupies only a finite-dimensional common mode, entropy is
irrelevant and the path is pruned.  If its Walsh components carry energy at a
positive rate, an entropy-decrement or large-sieve contradiction becomes
plausible.

## Subsequent gate result

The first alternative occurs.  Because `2 beta>1`, the primewise pole
increments are square-summable for every selector probability bounded by one.
The Euler-residue martingale has finite total `L2`/Walsh energy and its tail
energy vanishes, even while selector entropy diverges.  See
`RANDOM-SIEVE-WALSH-BARRIER.md`.  The propagation theorem remains valid, but
the entropy-amplification program is pruned in every quadratic formulation.
