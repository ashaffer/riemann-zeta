# Finite Ramanujan null-gauge and joint-Schur gate

Status: exact all-nonzero finite completion, optimized coefficient ledger,
vanishing center Schur complement, primitive solution-lattice formula, and
theta-completion fail-fast theorem proved; 2026-08-07.  The construction does
not give a new zero-free strip or prove RH.

## 1. Verdict

The joint Gram calculation proposed after R81 has a clean answer, but not the
coercive answer we hoped for.

1. The finite Ramanujan Mertens zero mode is **coordinate-dependent**.  On an
   active range below `Y`, a normalized cloud of prime moduli `Y<p<=2Y`
   moves it exactly into nonzero integer and reduced-rational modes.
2. The move costs only `O(log^5 Y)` in the same
   `sum phi(q)|h_q|^2` ledger as the original finite expansion.  No power
   bound for Mertens is used.
3. Equivalently, the full augmented Gram matrix has an exact null vector and
   the center Schur complement is **zero**.  A proposed positive uniform
   center floor is therefore false.
4. This does not estimate the completed energy.  The prime cloud is a
   coherent Farey direction at moduli `p asymp Y`; it synthesizes a vector of
   natural energy `asymp Y` from a logarithmic coefficient ledger.  Generic
   frame, large-sieve, or off-axis Wright bounds overcharge it or omit the
   sectors in which the null identity closes.
5. Completing the new prime-prime reciprocal phase in `theta` gives an exact
   sampling identity.  The result is the original shifted Ramanujan
   correlation; after restoring its diagonal, the native upper-half
   top-prime packet is the centered prime-indicator covariance.  Thus
   standalone theta completion is an invertible rewrite, not new
   cancellation.
6. A short-cell version lowers the auxiliary moduli to
   `Q gg H log Y`, but scalar recombination loses `Y/H`, sharply, and the
   joint coefficient is outside current separable Kloosterman theorems.

The new theorem is still useful: it removes the misleading claim that a bare
Mertens coefficient must be estimated separately.  The exact obstruction is
now a gauge-invariant, arithmetic-vector-specific major-arc correlation.

```text
finite completed Ramanujan field
  -> explicit Mertens zero coefficient                   COORDINATE ARTIFACT
  -> all-nonzero prime-cloud gauge, polylog ledger       THEOREM
  -> positive center Schur floor                         FALSE (exactly zero)
  -> generic nonzero-mode/frame power                    FALSE
  -> theta-only completion                               CLOSED (returns primes)
  -> full gauge-invariant major-arc power                OPEN.             (1.1)
```

## 2. The finite completed field

Let `Y` be a sufficiently large positive integer.  Let `T` denote any linear
compact R71 window map whose active integer support lies in `1<=n<=Y`.  Put
`N=2Y` and

```text
h_q=LambdaHat_N(q),
z=h_1-1=-R(N),
A=T(sum_n delta_n),
C=T(dt),
O_1=A-C,
B_q=T(sum_n c_q(n)delta_n),       q>=2.                 (2.1)
```

Proposition 3.3 of R81 gives exactly

```text
D=T(sum_n Lambda(n)delta_n-dt)
 =z C+h_1 O_1+sum_(2<=q<=N)h_q B_q.                    (2.2)
```

Poisson summation gives

```text
O_1=T(sum_(a in Z-{0})e(at)dt),
B_q=T(sum_((a,q)=1,a in Z)e(at/q)dt),     q>=2.         (2.3)
```

Thus `O_1` and every `B_q` already consist only of nonzero additive
frequencies.  The sole displayed zero frequency in (2.2) is `zC`.

## 3. Exact finite null gauge

### Theorem 3.1 (all-nonzero finite completion)

Let

```text
P_Y={p prime:Y<p<=2Y},
S_Y=sum_(p in P_Y)1/(p-1),
w_p=1/[(p-1)S_Y].                                      (3.1)
```

Then `sum_p w_p=1`, and on the active range

```text
B_p=-A,             p in P_Y,                           (3.2)
C=-O_1-sum_(p in P_Y)w_p B_p.                           (3.3)
```

Consequently (2.2) has the exact representation

```text
D=O_1+sum_(2<=q<=N) htilde_q B_q,                       (3.4)

htilde_p=h_p-z w_p,             p in P_Y,
htilde_q=h_q,                   q notin P_Y.            (3.5)
```

For uniform notation below, set `htilde_1=1`.

Every mode in (3.4) has nonzero additive frequency.  Moreover,

```text
1+sum_(2<=q<=N)phi(q)|htilde_q|^2 <<log^5 Y.            (3.6)
```

#### Proof

For `p>Y` and `n<=Y`, the prime Ramanujan sum is

```text
c_p(n)=p 1_(p|n)-1=-1.                                 (3.7)
```

This proves (3.2).  Since `A=C+O_1`, averaging (3.2) with weights of sum one
proves (3.3).  Substitute (3.3) into (2.2).  The integer-mode coefficient is

```text
h_1-z=1,                                                (3.8)
```

and (3.4)--(3.5) follow.

The inverse-totient weights uniquely minimize the adjustment ledger:

```text
min_(sum w_p=1) sum_p(p-1)|w_p|^2=1/S_Y.               (3.9)
```

The PNT gives

```text
S_Y~log(2)/log Y.                                      (3.10)
```

The elementary estimate

```text
|z|<=1+sum_(d<=N)log(d)/d <<log^2 N                    (3.11)
```

and R81's original ledger then give

```text
sum_q phi(q)|htilde_q|^2
 <<sum_q phi(q)|h_q|^2+|z|^2/S_Y
 <<log^5 Y.                                             (3.12)
```

For these top primes, `h_p=log(p)/p`; also

```text
|z w_p|<<log^3(Y)/Y.                                   (3.13)
```

This proves the theorem.

The exact formal-prime-log reconstruction is exercised by
[`ramanujan_null_gauge_probe.py`](../src/ramanujan_null_gauge_probe.py).

### Literature status

The underlying null identity is known.  Remark 2 of the
[Coppola--Ghidelli preprint](https://arxiv.org/abs/2005.14666), specializing
the exotic class of its Proposition 2, gives

```text
sum_(K>=0)c_(p^K)(n)=0.                                (3.14)
```

When `p` does not divide `n`, its surviving face is exactly
`c_1(n)+c_p(n)=0`.  It is an element of their Ramanujan `0`-cloud; this
report calls its scale-adapted use a null gauge.

The scale-adapted insertion of this `0`-cloud element into the completed finite
von Mangoldt expansion, the inverse-totient optimization (3.9), and the
resulting all-nonzero polylogarithmic ledger are new within this repository.
No literature search establishes a novelty claim beyond that.

## 4. The exact joint Schur complement

Let `B` synthesize the columns

```text
(O_1,B_2,...,B_N),                                      (4.1)
```

and set `H=B*B`.  Equation (3.3) says

```text
C=B u,
u=(-1,0,...,-w_p,...,0).                               (4.2)
```

The augmented Gram matrix is

```text
Gamma=[ <C,C>   C*B ]
      [ B*C      H  ].                                  (4.3)
```

Because `C` belongs to the range of `B`, its Moore--Penrose Schur complement
is exactly

```text
<C,C>-(B*C)* H^dagger (B*C)=0.                         (4.4)
```

The corresponding null vector is `(1,-u)`.  If

```text
b=(h_1,h_2,...,h_N),                                   (4.5)
```

then

```text
D=B(b+z u),
||D||^2=(b+z u)*H(b+z u),                              (4.6)
```

and `b+zu` is precisely the coefficient vector in (3.4)--(3.5).

This kills the proposed coercivity route.  Completing the square does not
force a power estimate for `R(N)`; the correct full Gram absorbs `R(N)` into
an exact null direction.  It also does not upper-bound (4.6): the residual is
the original completed prime discrepancy.

## 5. Why a generic frame estimate is impossible

The same null cloud is a deterministic counterexample to the proposed
coefficient-ledger shortcut.  It satisfies

```text
sum_p w_p B_p=-A,
sum_p(p-1)|w_p|^2=1/S_Y asymp log Y.                   (5.1)
```

Consequently the squared weighted synthesis norm, equivalently the largest
generalized Gram eigenvalue, satisfies the exact lower bound

```text
||B W^(-1/2)||_op^2>=S_Y||A||^2,                       (5.2)
```

where `W` has prime-cloud diagonal entries `p-1`.  More sharply, (3.3)
represents the continuum vector using only nonzero modes and coefficient
ledger `1+1/S_Y`, so

```text
||B W^(-1/2)||_op^2>=||C||^2/[1+1/S_Y].                (5.3)
```

For the full safe convolution map, the continuum vector is exactly

```text
C(r)=exp(r/2)Vhat(1/2),
||C||_(L2(psi))^2=|Vhat(1/2)|^2 integral psi(r)e^r dr. (5.4)
```

For a fixed nondegenerate window on `r=log Y+O(1)`, this is `asymp Y`.
Therefore no uniform statement covering these admissible windows of the form

```text
all frequencies nonzero + polylog coefficient ledger
  => Y^(1-eta) energy                                  (5.5)
```

can be true for any fixed positive `eta`.

The standard large sieve predicts the same failure.  Farey frequencies of
order `Q` have spacing `delta asymp Q^(-2)`, so the sharp generic cost is
`Y+Q^2`.  At `Q asymp Y` this is `Y^2`, losing a full power relative to the
structured identity.  See
[Montgomery--Vaughan's Hilbert inequality](https://doi.org/10.1112/jlms/s2-8.1.73),
their [large-sieve paper](https://doi.org/10.1112/S0025579300004708), and
[Moitra's sharp conditioning threshold](https://doi.org/10.1145/2746539.2746561).

This is not merely a weak known inequality.  The full prime cloud is
perfectly coherent on the active integers.  A useful theorem must recognize
the specific completed coefficient vector and be invariant under the null
gauge; an arbitrary-vector frame bound cannot supply a power.

There is also an immediate scale failure in the current R81--Wright ledger.
The global gauge has modulus exponent one.  Substituting that exponent into
the favorable `1/40-11A/40` budget is already negative.  Wright's current
off-axis theorem cannot be applied to (3.4) as a completed estimate.

## 6. Primitive solution-lattice simplification

Although it does not prove a bound, (3.4) improves the exact lattice
bookkeeping.  Its complete energy is

```text
sum_(q_1,q_2<=N) htilde_(q_1) conjugate(htilde_(q_2))
 sum_(a,b!=0;(a,q_1)=(b,q_2)=1)
 Lhat(-a/q_1,b/q_2).                                   (6.1)
```

Write

```text
q_1=gm, q_2=gn, (m,n)=1, theta=an-bm.                 (6.2)
```

Then primitivity forces

```text
(theta,mn)=1.                                          (6.3)
```

In particular:

1. `theta=0` implies `m=n=1`, hence `q_1=q_2` and `a=b`.
   The determinant-zero sector is the genuine equal-frequency diagonal, not
   a cross-denominator family.
2. A zero numerator is primitive only for denominator one.  Thus the only
   punctured axes introduced by completing the solution lattice are the
   `q_1=1` or `q_2=1` axes.
3. For common factor `g>1`, the remaining conditions
   `(a,g)=(b,g)=1` give a periodic mask in the solution parameter.  Fourier
   expansion of that mask produces fractional dual shifts.  These are not
   directly Wright's integer-dual-variable form.

The simplification of the diagonal and axes is real.  It does not remove the
`q=1` prime--continuum axes or the dual-zero mode; those are precisely where
the null gauge reappears after the reciprocal-phase transformation.

## 7. Exact theta completion returns the prime correlation

The most promising attempted use of the cloud was to complete the reciprocal
phase in `theta` before estimating it.  The following identity kills that
shortcut exactly.

### Theorem 7.1 (prime-pair theta sampling identity)

Let `p` and `p'` be distinct primes, let `r` be the inverse of `p'` modulo
`p`, and put

```text
F_j(u)=L(u+j,u),
A_theta(j)=integral F_j(u)e(theta u/(pp'))du.           (7.1)
```

Then

```text
sum_((theta,pp')=1)
 e(j theta r/p) A_theta(j)
 =sum_(k in Z)c_p(k+j)c_(p')(k)L(k+j,k).               (7.2)
```

#### Proof

Move (7.1) inside the `theta` sum.  With `M=pp'` and
`beta=jrp'`, primitive Poisson summation gives

```text
sum_((theta,M)=1)e(theta[u+beta]/M)
 =sum_(ell in Z)c_M(ell)delta(u+beta-ell).              (7.3)
```

Therefore the left side of (7.2) is

```text
sum_ell c_(pp')(ell)F_j(ell-beta).                      (7.4)
```

Set `k=ell-beta`.  Since `beta=0 (mod p')` and
`beta=j (mod p)`, multiplicativity of Ramanujan sums turns (7.4) into the
right side of (7.2).

An equivalent one-sided completion is

```text
p' sum_l F_j(lp')c_p(j+lp')
-p  sum_k F_j(kp-j)
+   sum_k F_j(k-j).                                    (7.5)
```

Thus the hoped-for isolated factor `c_p(j)=-1` does not occur.  It is
replaced by shifted Ramanujan factors and two full-size sampling corrections.

On a physical shell `u asymp Y`, the effective theta length is

```text
T_theta asymp pp'/Y.                                   (7.6)
```

When `p,p' asymp Y`, this is one residue period.  The amplitude changes by
at most its a priori `O(1)` scale across that period, with no uniform `o(1)`
freezing error.  The exact sampling identity, rather than a lower bound on
that variation, is the decisive obstruction.

For `j=0`, (7.2) is

```text
sum_k c_p(k)c_(p')(k)L(k,k),                            (7.7)
```

which expands into four natural-scale divisibility samples.  More generally,
(7.2) literally reconstructs the original shifted physical correlation.

For the native top-prime coefficients at cutoff `N`,

```text
h_p=log(p)/p,                 N/2<p<=N.                 (7.8)
```

Writing `H_N=sum_(N/2<p<=N)log(p)/p=log 2+o(1)`, one has on
`N/2<n<=N`

```text
sum_(N/2<p<=N)h_p c_p(n)
 =log(n)1_(n prime)-H_N.                                (7.9)
```

Formula (7.9) is a separate native upper-half packet diagnostic; its integers
lie outside the active `n<=Y=N/2` range of the null gauge in Theorem 3.1.
After adjoining the equal-prime diagonal omitted by Theorem 7.1, summing
(7.2) over that native packet reconstructs the full shifted covariance of the
centered prime indicator.

On the actual active range of Theorem 3.1, every top-prime block is instead
the same constant sequence `c_p(n)=-1`, and

```text
sum_(Y<p<=2Y)htilde_p c_p(n)=z-H_(2Y).                 (7.10)
```

Theta completion then reconstructs the coherent integer-comb/continuum null
packet.  In either regime it loops back to the physical correlation it was
meant to estimate; it does not create a saving.

## 8. Local modulus-lowering gauge

There is a rigorous local version, but its exponent ledger fails with current
inputs.  Let `J` contain `H` consecutive integers in `[Y,2Y]`.  A prime
`p in [Q,2Q]` is good if it divides no integer of `J`.  The bad primes obey

```text
Q^(#bad)<=product_(n in J)n<=(2Y)^H,
#bad<=H log(2Y)/log Q.                                  (8.1)
```

Thus `Q=C H log(2Y)` with a sufficiently large fixed `C` leaves
`asymp Q/log Q` good primes.  On `J`, every good prime again satisfies

```text
c_p(n)=-1.                                              (8.2)
```

The inverse-totient local cloud moves the zero coefficient into those moduli
at cost

```text
asymp |R(N)|^2 log Q.                                   (8.3)
```

This lowers the auxiliary modulus from `Y` to `H log Y`.  It does not create
local cancellation.  For any two good primes,

```text
sum_(n in J)c_p(n)c_(p')(n)=H,                          (8.4)
```

so the cloud is perfectly coherent and its restricted synthesis norm loses
`H/log Q`.

There are `M asymp Y/H` cells.  Applying a scalar theorem cell by cell and
then recombining loses `M`; the positive broad R71 kernel makes this loss
sharp for the continuum packet.  If `H=Y^theta` and a per-cell theorem is
normalized as a `Y^(-delta_cell(theta))` saving, it must satisfy

```text
delta_cell(theta)>1-theta                              (8.5)
```

before modulus or amplitude costs.  The precise translation of Wright's
native `1/40` into `delta_cell` has not been established.  Qualitatively, a
large enough `theta` to repay scalar recombination makes
`Q=Y^(theta+o(1))` incompatible with the favorable small-denominator regime.

Keeping all cells jointly avoids writing Cauchy's inequality, but produces a
cell-by-modulus matrix of coefficients and dense cross-cell terms.  Wright's
current theorem accepts separable sequences, not this tensor-valued
completion.  Also, the original finite expansion still contains its large
denominators; the local gauge alone does not compress the whole prime field
to `q<=Q`.

Short-interval Ramanujan expansions with `q>2H` are studied by
[Coppola--Laporta](https://arxiv.org/abs/1312.5701).  The closest structural
analogue is Heath-Brown's
[delta method](https://doi.org/10.1515/crll.1996.481.149): exact rational
completion in its standard quadratic-form application has a zero dual vector
supplying the main term.

## 9. What remains

The Mertens scalar is no longer a logically separate gate.  A correct
finite-coordinate statement of the remaining estimate is

```text
(b+zu)*[
 H_(theta=0)+H_(j=0)+H_(axes)+H_(j theta!=0)
](b+zu)
 <<Y^(1-2eta+o(1)),       0<eta<=1/2 fixed.              (9.1)
```

Every block in (9.1) must use the same gauge representative, and the result
must be invariant under the null moves (3.3).  Wright currently controls only
a native nonzero reciprocal-phase form, not this sum.

Equation (9.1) is still fixed-strip-strength.  The exact null gauge and
theta identity show why three apparently cheaper formulations fail:

1. center coercivity fails because its Schur complement is zero;
2. coefficient-norm control fails on the continuum null packet; and
3. complete theta orthogonality returns the centered prime covariance.

The only plausible continuation within this architecture is a
**sector-aware nullspace optimization**: find a polylogarithmic representative
for which the non-Wright block is independently small and all remaining
moduli lie in a theorem's admissible range.  The global and local gauges in
this note do not meet those two requirements.  Any proposed version should
first be tested against the continuum counterexample (5.4) and the exact
sampling identity (7.2).

## 10. Reproduction and nonclaims

Run

```text
PYTHONPATH=src python3 src/ramanujan_null_gauge_probe.py \
  --active-limit 24
PYTHONPATH=src python3 -m pytest -q \
  src/test_ramanujan_null_gauge_probe.py
```

The probe checks the finite null relation and modified von Mangoldt
reconstruction in exact rational/formal-log arithmetic.  It does not certify
the PNT asymptotic, an operator norm, a Kloosterman estimate, a zero-free
region, or RH.  The analytic identities in Sections 4--8 should receive
independent specialist review before any external novelty claim.
