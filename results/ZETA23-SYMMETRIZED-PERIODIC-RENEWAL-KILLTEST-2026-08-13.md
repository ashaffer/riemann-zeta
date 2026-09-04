# Symmetrized periodic-renewal kill test

**Date:** 2026-08-13
**Status:** exact theorem in a sieved-Cramer model; Hardy--Littlewood scope
audit; no claim about actual primes.

## Verdict

The strongest exactly computable periodic renewal model does **not** predict
a polylogarithmic obstruction.  At a prime modulus

```text
q=Y^b,        .1537 < b <= .1594,
```

the systematic nonprincipal predecessor/successor mode is uniformly
`O(q^-1)`, and is generically `O((q log Y)^-1)`.  Its random fluctuation is at
most `Y^(-1/2+o(1))`.  Both are far below `Y^(-kappa)`, where
`kappa=.0180303234`.

This is a decisive **model verdict**, not the missing actual-prime theorem:
the route survives the prime-modulus and fixed-auxiliary-wheel
sieved-Cramer mechanisms tested here.  A
failure for actual primes would have to come from gap--residue coherence that
is absent from the periodic renewal model, most plausibly anomalous mass on
gaps comparable with `q`.

## 1. Exact periodic theorem

Let `q` be prime.  Independently mark each integer not divisible by `q` with
probability `p`; multiples of `q` are never marked.  This is Kim's modified
Cramer model with sieve modulus `q`, frozen on a block so that

```text
p=(q/(q-1))/log Y = (1+o(1))/log Y.                  (1.1)
```

Write the unsieved points in one period as `u_i=i`, `1<=i<=m=q-1`, and
extend by `u_(i+m)=u_i+q`.  Put

```text
D_i^+(k)=u_(i+k)-u_i,       D_i^-(k)=u_i-u_(i-k),
z=1-p,                      omega=e_q(r).
```

The expected symmetrized Voronoi-cell Fourier mass per physical unit is
exactly

```text
A_(q,p)(r)
 =p^2/(2q) sum_(i=1)^m omega^i sum_(k>=1) z^(k-1)
                         [D_i^+(k)+D_i^-(k)].         (1.2)
```

Indeed, `p^2 z^(k-1)` is exactly the probability that `u_i` and `u_(i+k)`
are consecutive marked points.  The two distances in (1.2) are the outgoing
and incoming half-cell masses.  Thus (1.2) is a stationary mass-transport
identity, with no heuristic independence inserted after the model is
defined.

For `k=am+h`, `0<=h<m`, one has

```text
D_i^+(k)=aq+h+1_(h>0)1_(i>m-h),
D_i^-(k)=aq+h+1_(h>0)1_(i<=h).                       (1.3)
```

At a nonzero frequency, the DFT of the two boundary indicators is

```text
2 Re sum_(j=1)^h omega^j.                             (1.4)
```

Equations (1.2)--(1.4) reduce the expectation to a finite geometric
expression.  There is a cleaner exact resolvent form.  Conditional on `u_i`
being marked, the expected number of candidate steps to either neighbor is
`1/p`.  The expected numbers of deleted multiples of `q` crossed to the
right and left are respectively

```text
z^(m-i)/(1-z^m),             z^(i-1)/(1-z^m).
```

Consequently the expected cell mass carried by residue `i`, divided by the
physical period `q`, is exactly

```text
s_i=1/q+p[z^(m-i)+z^(i-1)]/[2q(1-z^m)].             (1.4a)
```

This also audits the normalization directly:

```text
sum_(i=1)^m s_i=(q-1)/q+1/q=1.                      (1.4b)
```

Taking the DFT of (1.4a) gives

```text
A_(q,p)(r)
 =-1/q + p/[q(1-z^m)] Re[(omega-z^m)/(1-z omega)]
 =-1/q + p/q Re[omega/(1-z omega)] + R_(q,p)(r),     (1.5)

R_(q,p)(r)
 =p z^m/[q(1-z^m)] Re[(omega-1)/(1-z omega)].        (1.6)
```

This exact remainder is much smaller than the coefficient-blind absolute
tail bound.  Since

```text
|Re[(omega-1)/(1-z omega)]|
 =(1+z)(1-Re omega)/[p^2+2z(1-Re omega)]
 <=(1+z)/(2z),
```

one has, uniformly in every nonzero `r`,

```text
|R_(q,p)(r)|
 <=p(1+z)z^(q-2)/[2q(1-z^(q-1))].                  (1.6a)
```

In particular `R=o(q^-1)` whenever `pq->infinity`.  This implication is
uniform: `z^(q-1)<=exp(-p(q-1))`, while the remaining factor in (1.6a) is
`o(1)`.  A previous coefficient-blind tail estimate was too crude to prove
this assertion when `pq` grows slowly; the exact resolvent (1.6) is what
justifies it.

Total cell mass is one.  Therefore the principal character contributes the
Ramanujan term `-1/(q-1)`.  After removing it, (1.5) gives

```text
A_np(r)
 =1/[q(q-1)] + p/q Re[omega/(1-(1-p)omega)] + R,     (1.7)
```

and

```text
p/|1-(1-p)omega| <=1.                                (1.8)
```

Consequently, whenever `pq -> infinity`, uniformly in every reduced `r`,

```text
|A_np(r)| <=(1+o(1))/q.                              (1.9)
```

If `r/q` stays away from zero and one, (1.7) improves to
`O(p/q)=O((q log Y)^-1)`.  The selected numerator cannot be assumed generic,
so (1.9), with saving exponent `b`, is the correct uniform model verdict.

### 1.1 Adjoining a fixed auxiliary sieve wheel

The conclusion is not an artifact of sieving only by `q`.  Let `P` be fixed,
`(P,q)=1`, and mark the units modulo `Pq`.  Couple this model to the model
which marks all units modulo `P` with the same probability.  The latter has
a `P`-periodic expected cell-mass profile.  Because multiplication by `P`
permutes the residues modulo `q`, its nonzero `q`-Fourier mode vanishes
exactly over a period `Pq`.

There are `phi(P)` additional candidate sites in the `P` wheel per period
`Pq`: the sites divisible by `q`.  Starting from the `Pq` process, insert
these sites one at a time, with independent mark probability `p`.  Inserting
a marked site between its nearest marked neighbors changes the total
variation of the Voronoi cell-mass measure by at most the sum of the two
neighbor distances.  For fixed `P`, the deterministic gaps between
candidate sites in either wheel are `O_P(1)` once `q` is large.  The expected
sum of the neighbor distances is therefore `O_P(p^-1)`.  After multiplication
by the insertion probability `p`, each candidate insertion costs `O_P(1)`
in expected total variation.  Earlier insertions can only shorten the
neighbor distances, so no separate interaction term is needed.

The expected full additive mode of the `Pq` process is consequently
`O_P(q^-1)` after division by the physical period `Pq`.  Its total mass is
one, so its principal `q`-character contribution is still `-1/(q-1)`.
Removing that term proves

```text
A_np(Pq;r)=O_P(q^-1).                                (1.10)
```

Thus every fixed finite auxiliary wheel preserves the `q^-1` verdict.  The
checker independently compares the exact period-resolvent formula with its
defining renewal series and evaluates it for `P=2,6,30`.
This does not claim uniformity for a wheel `P=P(Y)` growing arbitrarily fast;
the constants in the candidate-gap and coupling bounds depend on `P`.  A
growing wheel is a different model and needs its own stabilization ledger.

## 2. Why the fixed-modulus expansion is misleading here

For fixed `q` and `p->0`, exact expansion of (1.2) gives

```text
A_np(r)=O_(q,r)(p^2).                                 (2.1)
```

This is the model counterpart of Kim's result: the outgoing prime-running
bias is `R_Q(q,a)/log Y`, the reverse bias has the opposite sign, and the
predecessor/successor average cancels it.  But the constant in (2.1) grows
with `q`.  The fixed-`q` series ceases to be uniform at `pq asyp 1`; resumming
the exact renewal expression in the repository's regime `pq->infinity`
produces (1.7), not a bare `(log Y)^-2` term.

Thus an argument of the form

```text
fixed-q remainder O_q((log Y)^-2)
    => growing-q polylogarithmic obstruction
```

is invalid.  The two limits do not commute.

## 3. Random fluctuation in the model

Changing one Bernoulli mark can only split or merge the cell between its
nearest marked neighbors.  Those two renewal distances have geometric
second moments `O(p^-2)`.  Efron--Stein therefore gives, for a physical block
of length `Y`, the deliberately crude uniform estimate

```text
Var(A_sample(r)) <<1/(Y p^2).                         (3.1)
```

With `p asyp 1/log Y`,

```text
A_sample(r)-A_(q,p)(r)=O_P(Y^-1/2 log Y).             (3.2)
```

This is much smaller than both the required `Y^-kappa` and the systematic
`q^-1` scale.  Sharper renewal-reward variance gives a square-root-log
instead of a full log, but it is unnecessary for the verdict.

## 4. Hardy--Littlewood literature scope

Lemke Oliver--Soundararajan's consecutive-residue conjecture is stated for
**fixed** `q`.  Its coefficients already contain `phi(q) log q`; its error
term has no uniformity allowing `q=Y^b`.  Substituting a growing modulus into
that displayed fixed-modulus expansion is therefore not a justified model
calculation.  It also counts transitions rather than their gap-weighted
Voronoi marginals.

Their symmetric formula is still structurally informative: forward/reverse
antisymmetric bias disappears, while local sieve effects depending on the
endpoint difference remain.  In the periodic renewal calculation those
effects are exactly the two boundary indicators in (1.3).  Only a proportion
`O(g/q)` of starting residues see a multiple of `q` inside a gap `g`; after
the no-prime-interior probability is included, their fully resummed Fourier
response is (1.7), of `q^-1` size.  A Hardy--Littlewood model with typical
`g asyp log Y=o(q)` therefore has the same qualitative verdict.  This last
sentence is a model inference, not a published uniform Hardy--Littlewood
theorem.

Kim explicitly leaves a Hardy--Littlewood refinement of prime-running
functions for future work.  No primary source located supplies the required
actual-prime, gap-weighted, growing-modulus estimate.

## 5. Fail-fast disposition

```text
polylog-sized nonprincipal model main term:          NO
uniform periodic-renewal systematic term:            O(q^-1)
target exponent supplied by model:                   b >= .1537
required exponent:                                   kappa=.0180303234
model margin:                                        >=.1356696766
actual-prime selected-frequency theorem:             OPEN
```

The model test clears rather than kills the route.  It sharply identifies
what a definitive empirical or theoretical falsification must exhibit:
actual-prime symmetric cell mass at one selected `q,r` of size at least
`Y^-kappa`, despite the renewal prediction `Y^-b`.  Ordinary prime-running
bias is not enough, because its first term is antisymmetric and cancels.

## Primary sources

- J. Kim, [*Prime Running Functions*](https://arxiv.org/abs/2006.13355),
  especially Theorems 4.3, 4.5, 4.6 and the reversed model discussion.
- R. J. Lemke Oliver and K. Soundararajan,
  [*Unexpected biases in the distribution of consecutive primes*](https://arxiv.org/abs/1603.03720),
  especially the fixed-modulus Main Conjecture and symmetric formula (1.2).
- A. Granville, [*Harald Cramer and the distribution of prime numbers*](https://doi.org/10.1080/03461238.1995.10413946),
  for the small-prime-sieved correction to the original Cramer model.

## Reproduction

```bash
python3 results/verify_zeta23_sym_renewal_model_killtest.py
```
