# Mobius boundary-exchange gate

Status: exact reduction proved and adversarially audited, 2026-08-04.  The
Björner topology is exact; only the proposed discrete-Morse interpretation of
the exchange pairs is pruned.  A deterministic sign-pairing target remains,
but currently has no independent RH leverage.

## 1. Exact collar identity

For every integer `N>=2`, let

```text
S_N = {m : N/2 < m <= N, m odd and squarefree}.
```

Then

```text
M(N) = sum_(m in S_N) mu(m).                         (1)
```

Indeed, split the squarefree terms in `M(N)` into odd and even terms.  Every
squarefree even integer is uniquely `2m` with `m` odd and squarefree, and
`mu(2m)=-mu(m)`.  Therefore

```text
M(N)
 = sum_(m<=N, m odd,sf) mu(m)
   - sum_(m<=N/2, m odd,sf) mu(m),
```

which is (1).  The lower endpoint is strict.

This is also exactly the homology collar in Björner's prime-factor complex

```text
Delta_N = {P(m) : m<=N and m squarefree}.
```

His Theorem 3.1 gives

```text
beta_k(Delta_N)
 = #{m in S_N : omega(m)=k+1},
```

and hence

```text
M(N) = sum_(k>=0) (-1)^(k+1) beta_k(Delta_N)
     = - reduced_chi(Delta_N).
```

See [Björner, *A cell complex in number
theory*](https://arxiv.org/abs/1101.5704), Theorems 3.1, 3.4, and 3.5.

## 2. The factorization-exchange graph

Color `m in S_N` by `omega(m) mod 2`.  Join `m,m'` when their prime-factor
sets have the form

```text
P(m)  = C union {p},
P(m') = C union {q,r},
```

where the three added primes are distinct.  Equivalently, in one orientation,

```text
m' = m q r / p.
```

Both endpoints are required to remain in `S_N`.  Every edge flips the Mobius
sign while preserving the logarithmic scale.  This avoids the density loss of
the earlier one-prime map `m -> pm`.

Let the two color-class sizes be `E,O`, let a matching have size `nu`, and let

```text
R = E+O-2 nu
```

be its total number of unmatched vertices.  Matched signs cancel, so

```text
|M(N)| = |E-O| <= R.                                (2)
```

Thus an explicitly constructed matching with

```text
R = O_epsilon(N^(1/2+epsilon))
```

would prove RH through the classical Mertens criterion.

## 3. The decisive audit: what (2) does not say

If a maximum matching saturates the smaller color class, then

```text
nu=min(E,O),   R=|E-O|=|M(N)|.
```

This is a cardinality identity, not an estimate.  Hall expansion can establish
saturation, but it cannot bound the difference `E-O`.  After saturation, an
RH-scale bound on the *minimum* unmatched count is exactly the RH-scale bound
on `M(N)` in different notation.

There is also no discrete-Morse cancellation here.  The two endpoints
`C union {p}` and `C union {q,r}` are incomparable faces, not a face and an
incident coface.  They therefore do not form a Forman Morse pair.  Björner's
collar elements count genuine Betti generators; pairing their alternating
signs can cancel the Euler sum numerically but cannot cancel the homology.
See [Forman, *Morse Theory for Cell
Complexes*](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/forman5.pdf).

The corrected conclusion is:

> The graph supplies a scale-preserving language for a sign-reversing
> involution.  It does not supply the missing estimate.  Only a deterministic
> rule whose exceptional set is bounded by an independent arithmetic argument
> would create new leverage.

## 4. Lightweight finite scout

The small-`N` script `src/mobius_boundary_exchange.py` uses a smallest-prime-factor
sieve, common-core hashing, and Hopcroft--Karp.  It explicitly verifies (1)
before reporting any graph data.

| `N` | vertices | even/odd `omega` | edges | isolated | max unmatched |
|---:|---:|---:|---:|---:|---:|
| 1,000 | 200 | 101/99 | 8,572 | 0 | 2 |
| 3,000 | 604 | 299/305 | 67,506 | 0 | 6 |
| 10,000 | 2,029 | 1,003/1,026 | 649,741 | 0 | 23 |
| 30,000 | 6,080 | 3,049/3,031 | 5,077,706 | 0 | 18 |

The smaller class is saturated at all four checkpoints, so the final column
is exactly `|M(N)|`.  This passes a connectivity test and nothing more.

A fixed value-ordered greedy rule was also tested without consulting which
color class is smaller.  On the grid `N=250,500,...,10000`, its excess over
`|M(N)|` was at most 6; at `N=6000`, for example, `M(N)=0` and the rule left 4
vertices.  This is an intriguing diagnostic, not asymptotic evidence.  A
remote positive-density obstruction can defeat every finite scan.

Reproduce the small checkpoints with

```text
python3 src/mobius_boundary_exchange.py 1000 3000 10000
```

The default deliberately stops at small `N`; the edge set becomes dense and
the script is not intended for record-scale Mertens computation.

## 5. Only defensible continuation

The next theorem must name a rule, not an optimizing matching:

```text
Construct Phi_N:S_N -> S_N union {unmatched}
```

such that

1. `Phi_N` is an involution on matched vertices;
2. every matched pair is a valid `p <-> qr` exchange;
3. the rule is defined from bounded/local factorization data, without using
   `M(N)`, global parity counts, or a maximum matching;
4. its exceptional set has an independently proved
   `O_epsilon(N^(1/2+epsilon))` bound.

The fail-fast version should first test lexicographic and multiscale exchange
rules for an explicit positive-density family of unmatched vertices.  If such
a family exists for every bounded-complexity rule in a clearly defined class,
prove that no-go theorem and close the branch.  Until the exception bound has
an arithmetic mechanism, this is an RH-strength reformulation rather than an
advance toward RH.

That follow-up has now been carried out for several broad classes.  Fixed
summable (in particular bounded-overlap) template dictionaries and bounded
dyadic-local exchanges leave positive-density obstruction families; standard
one-shot lexicographic rules suffer explicit core-fiber collisions.  See
`results/MOBIUS-STATIC-EXCHANGE-NOGO-2026-08.md`.  Only genuinely multiscale,
`N`-adaptive sequential allocation remains open.
