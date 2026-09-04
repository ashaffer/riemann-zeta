# Eratosthenes deletion and curvature-charge tool

## Verdict

There is an exact way to replace the nonlinear consecutive-prime-gap
statistic by a telescoping sum indexed by the least prime factors of deleted
composites.  This does not prove the required cancellation, but it escapes
the black-box cousin-prime formulation: the new coefficients are explicit
local deletion charges with a multiplicative stage label.

The reproducible implementation is
[`src/prime_gap_sieve_deletion.py`](../src/prime_gap_sieve_deletion.py), with
regression test
[`src/test_prime_gap_sieve_deletion.py`](../src/test_prime_gap_sieve_deletion.py).

## 1. Exact deletion identity

For a finite ordered set `S` and arbitrary complex data `f`, define

```text
T(S;f)=1/2 sum_(x<y consecutive in S) (y-x)(f(x)+f(y)).       (1.1)
```

Let `l<x<r` be consecutive active points and delete `x`.  Direct
subtraction gives

```text
T(S\{x};f)-T(S;f)
 =1/2[(r-x)f(l)+(x-l)f(r)-(r-l)f(x)].                         (1.2)
```

Start with every integer in `[L,R]`, retain the endpoints, and delete each
interior composite in increasing least-prime-factor stages.  If `D_p(f)` is
the sum of (1.2) during the stage `p`, then

```text
T({endpoints and primes};f)-T({all integers};f)=sum_p D_p(f). (1.3)
```

The total of a stage is independent of the order chosen inside that stage:
it is the difference of `T` immediately after and before the complete
stage.  Thus (1.3) is an algebraic theorem, not a probabilistic model.

## 2. Curvature cancellation is local and exact

For `f(n)=exp(i theta n)`, write `A=x-l`, `B=r-x`.  Equation (1.2) becomes

```text
D_x(theta)=f(x)/2 [B exp(-i theta A)+A exp(i theta B)-(A+B)].  (2.1)
```

The constant and linear Taylor terms cancel identically.  Consequently

```text
|D_x(theta)|
 <=min(A+B, theta^2*A*B*(A+B)/4).                            (2.2)
```

This recovers the third-gap-moment mechanism at low frequency.  At a
rational near-pole the first bound is the relevant one, so a proof must use
cancellation between deletion charges rather than a coefficientwise
estimate.

## 3. Why this is a genuinely different target

The direct `g=4` remainder is a selected Fourier sum over cousin-prime
pairs.  In (1.3), the same final statistic is instead the sum of stages in
which a composite `n=p*m` is deleted when its least prime factor `p` is
introduced.  The label `p` exposes multiplicative structure that is absent
from the terminal prime-pair coefficient.

The exact successor problem is therefore replaced by the following
two-scale question.

> Choose a sieve split `z`.  Prove selected-frequency cancellation for the
> early periodic-wheel stages `p<=z`, and a bilinear or dispersion estimate
> for the late least-prime-factor charges `p>z`, uniformly after summing the
> two pieces at the same height.

Neither ordinary Vaughan applied to the terminal prime sum nor a bound on
the absolute square function `sum_p |D_p|^2` is sufficient: the target is
the signed pointwise sum in (1.3).

## 4. Reproducible finite check

For `[100000,200000]`, `q=419`, `a=105`, the program gives the
endpoint-augmented finite mode (both displayed endpoints are composite):

```text
normalized final mode          0.00312925668336
exact deletion identity error  1.78e-12
```

Individual least-prime-factor stages are larger than the final mode and
cancel strongly.  This finite observation is diagnostic only; it is not an
asymptotic estimate and cousin-prime infinitude is not assumed.

## 5. Truth boundary

Proved here:

1. the exact deletion identity (1.2)--(1.3);
2. the curvature bound (2.2);
3. a deterministic implementation for rational and logarithmic phases.

Not proved:

1. a power bound for the signed stage sum;
2. uniform localization of a growing wheel to every curvature block;
3. the prime antenna, QP, or a zero-free strip.

The new live object is a **selected sieve-stage martingale/dispersion
estimate**, not another ordinary-prime exponential sum.
