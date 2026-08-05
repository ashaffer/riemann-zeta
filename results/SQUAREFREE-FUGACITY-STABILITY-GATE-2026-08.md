# Squarefree fugacity stability gate

Status: real-rooted route exactly falsified; Hurwitz half-plane route survives
finite tests but is quantitatively insufficient, 2026-08-04.  No RH claim is
made.

## 1. Singular-endpoint construction

Define

```text
P_N(z) = sum_(n<=N) mu(n)^2 z^omega(n)
       = sum_k a_k(N) z^k.
```

All coefficients are positive integers, while

```text
P_N(-1)=M(N),
P_N(1)=#{n<=N:n squarefree} ~ 6N/pi^2.
```

This packages the singular Selberg--Delange endpoint `z=-1` into a finite
polynomial.  Unlike the nearby functions `mu^2(n)z^omega(n)`, evaluation at
`-1` retains the exact Mobius cancellation.

## 2. Exact real-rootedness falsifier

The first small counterexample found is already `N=114`:

```text
P_114(z)=1+30z+32z^2+9z^3.
```

The coefficients are independently checkable: there are 30 primes, 32
squarefree semiprimes, and the nine squarefree triples
`30,42,66,70,78,102,105,110,114`; the first four-prime product is 210.
Its exact cubic discriminant is `-28139`, so it has one real root and one
nonreal conjugate pair.  At `N=113`, by contrast, the discriminant is `63040`
and all three roots are real.  Thus the negative-real Lee--Yang route fails at
a tiny, exactly checkable truncation.  An exact Sturm scan through every
smaller cutoff identified `N=114` as the first failure; that minimality claim
is computer-checked, while the counterexample itself is hand-checkable.

For a larger independent checkpoint, at `N=10000` exact sieving gives

```text
P_10000(z)
 = 1 + 1229 z + 2600 z^2 + 1800 z^3 + 429 z^4 + 24 z^5.
```

Its exact discriminant is

```text
-322712393061871347291,
```

and an exact Sturm count gives three real roots.  Hence `P_N` is not always
real-rooted and its
coefficients do not form the hoped-for Polya-frequency/independent-spin cone.
This kills that Lee--Yang route with a finite exact counterexample.

## 3. Hurwitz stability is a different, weaker question

The cubic counterexample at `N=114` is nevertheless exactly Hurwitz stable:
`32*30>9*1`.  The first five Routh--Hurwitz minors at `N=10000` are

```text
429,
709800,
1619303907,
1988859514911,
1988859514911.
```

They are all positive, so every root has negative real part at this
checkpoint.  Additional exploratory numerical scans found no early Hurwitz
violation, but no all-cutoff scan artifact is retained in this repository and
no range claim is used here.  Pakianathan--Winfree's prime-log quota complex has this polynomial as
its squarefree face enumerator, up to the usual dimension shift, but does not
study its zero geometry
([primary source](https://arxiv.org/abs/1104.4324)).  The literature search
found no source asserting its Hurwitz stability.

More importantly, Hurwitz stability alone cannot imply an RH-scale bound.
Write the roots as `rho_j`.  Then

```text
|M(N)| / P_N(1)
 = product_j |(1+rho_j)/(1-rho_j)|.                 (1)
```

If `Re rho_j<0`, every factor in (1) is below one.  This yields only

```text
|M(N)| < P_N(1) asymp N,
```

which is essentially trivial.  Stable positive-coefficient polynomials can
have the ratio in (1) arbitrarily close to one.  For example, `(1+z/A)^d` has
every root at `-A`, but its ratio is `((A-1)/(A+1))^d`, which tends to one when
`A` grows faster than `d`.

The actual RH-strength root statement is the accumulated displacement bound

```text
sum_j log |(1+rho_j)/(1-rho_j)|
 <= -(1/2-epsilon) log N + O_epsilon(1).            (2)
```

Together with `P_N(1)=O(N)`, (2) implies
`M(N)=O_epsilon(N^(1/2+epsilon))`.  But (2), not half-plane stability, contains
the cancellation theorem.

## 4. Reproduction and classification

The standard-library scout computes coefficients and exact integer Hurwitz
minors.  If SymPy is installed it also performs the exact discriminant and
real-root count:

```text
python3 src/squarefree_fugacity_stability.py 113 114 10000 --sympy
python3 src/squarefree_fugacity_stability.py --first-nonreal 114
```

Classification:

- all-real-negative roots: **pruned exactly** at `N=114`;
- uniform Hurwitz stability: **open but insufficient by itself**;
- quantitative product bound (2): **valid RH-sufficient target, with no
  independent mechanism yet**.

A worthwhile continuation must either find a recurrence/interlacing law that
forces (2), or quickly produce an `N` with a right-half-plane root and close
even the qualitative stability curiosity.  Merely extending the numerical
Hurwitz scan is not useful RH progress.
