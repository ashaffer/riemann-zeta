# Common-height rough `L4`: final fail-fast card

**Date:** 2026-08-13  
**Binary verdict:** **LIVE** for the actual rough/common-height theorem;
**FALSIFIED** only for a coefficient-blind abstract node-class theorem with a
fixed power margin.

No actual-prime or SPF-rough countermodel was found.  The semiprime diagonal,
additive-energy inequalities, and the finite selector laboratory do not
contradict the small-positive-margin `L4` estimate needed for closure.

## 1. Weakest correctly normalized closing theorem

Fix one legal common height `t`.  Let `I` run over its curvature blocks, with
length `H_I` and

```text
sum_I H_I << Y.
```

Let `a_I(t)/q_I(t)` be the reduced rational selected on `I`.  In actual-mass
normalization, let `c_(I,P)(n)` be the atomic coefficient of the exact dyadic
rough-Voronoi increment in band `P`.  Include the crossing band, when present,
as `nu_(2P)-nu_(q_I)`; every post-`q_I` stage must occur exactly once.

Put every physical weight into the vector before taking a moment.  Thus

```text
Delta_(I,P)^t(r)
 =sum_(n in I, n=r mod q_I) W_(I,t)(n)c_(I,P)(n),    (1.1)
```

where `W_(I,t)` contains the tent or smooth taper, the original smooth
amplitude, and the exact residual chirp after the carrier
`e_(q_I)(a_I n)` is removed.  The vector may be complex.  Define

```text
D_(I,P)(t)=sum_(r mod q_I) Delta_(I,P)^t(r)e_(q_I)(a_I r),
B_I(t)=sum_P D_(I,P)(t).                             (1.2)
```

The weakest natural `L4` theorem which closes the retained post-`q` tail is,
for some fixed `delta>0`,

```text
sup_(legal t) sum_I |B_I(t)|^4/H_I^3
   << Y^(1-4 kappa-4 delta+o(1)),                    (CH4)

kappa=0.01974048259....
```

Indeed, weighted Holder gives exactly

```text
sum_I |B_I(t)|
 <=(sum_I H_I)^(3/4)
   (sum_I |B_I(t)|^4/H_I^3)^(1/4)
 <<Y^(1-kappa-delta+o(1)).                           (1.3)
```

`(CH4)` asks only for the numerator actually selected by the one common
height, and it combines the dyadic bands before the fourth power.  It does
not ask for arbitrary blockwise selectors, a maximum over numerators, or an
all-frequency moment.  Among the `L4` formulations currently on the table,
this is therefore the logically weakest sufficient one.

Any boundary, discarded-edge, or continuum-transfer term not included in
`W_(I,t)c_(I,P)` still needs a uniform aggregate `L1` bound
`<<Y^(1-kappa-delta_E)` for some `delta_E>0`.  There is no extra taper loss
when the taper and residual phase are included in (1.1).

## 2. Stronger moment interfaces

Combine vectors before taking a moment:

```text
Delta_I^t=sum_P Delta_(I,P)^t.
```

For

```text
C_Delta(s)=sum_r Delta(r) conjugate(Delta(r+s)),
M_4^*(Delta;q)=sum_((a,q)=1)|Delta_hat(a)|^4,
```

the exact complex identities are

```text
sum_(a mod q)|Delta_hat(a)|^4
 =q sum_s |C_Delta(s)|^2,                            (2.1)

M_4^*(Delta;q)
 =sum_(s,u) C_Delta(s) conjugate(C_Delta(u))
               c_q(u-s),                            (2.2)
```

where `c_q` is the Ramanujan sum.  Consequently either of

```text
sup_t sum_I H_I^-3 M_4^*(Delta_I^t;q_I)
 <<Y^(1-4kappa-4delta+o(1)),                         (2.3)

sup_t sum_I (q_I/H_I^3)sum_s|C_(Delta_I^t)(s)|^2
 <<Y^(1-4kappa-4delta+o(1))                          (2.4)
```

implies `(CH4)`.  Equation (2.3) is stronger than the selected-mode theorem;
(2.4) is stronger again because it includes imprimitive frequencies.

If a proof is available only band by band, then

```text
|sum_P D_(I,P)|^4 <=L_I^3 sum_P |D_(I,P)|^4,
L_I=O(log Y).                                        (2.5)
```

Thus the corresponding bandwise selected, primitive, or full-frequency
estimate also suffices, with only `Y^o(1)` loss.  Combining bands first is
strictly preferable: it preserves the cross-band covariance supplied by the
exact rough-measure telescope.

## 3. Why the semiprime diagonal does not kill `L4`

At the arbitrary-selector injective endpoint `q=H+O(1)`, let `N_(I,P)` be
the retained balanced-semiprime deletion count.  The hard-block argument
gives

```text
||Delta_(I,P)||_2^2 >=N_(I,P),
|C_(Delta_(I,P))(0)|^2>=N_(I,P)^2.                  (3.1)
```

There are `>>Y/log Y` centers across `Y/H` blocks and `Y^o(1)` bands.
Cauchy therefore forces only

```text
sum_(I,P) (q/H^3)sum_s|C_(Delta_(I,P))(s)|^2
 >>Y/H times a polylogarithmic loss
 =Y^(1-h-o(1)).                                      (3.2)
```

At the shallow endpoint `h=33/133`, this is exponent
`.751879...`, while the closing allowance at `delta=0` is

```text
1-4kappa=.92103806964....                            (3.3)
```

The margin is `.169158...`; the companion range `h>=1/2` has still more
room.  For the full-frequency theorem, (3.2) merely caps a possible saving
at

```text
delta <=h/4-kappa=.042289...                         (3.4)
```

on the shallow endpoint.  It does not rule out the arbitrarily small fixed
`delta>0` needed for closure.  Moreover (3.1) gives no lower bound at the
single selected primitive numerator: Fourier energy can avoid that mode,
and for composite `q` it can also lie at imprimitive modes.  The hard-block
argument has not been transferred through every smooth taper or realized by
one common height, so even (3.2) retains its stated scope.

No stronger universal additive-energy lower bound follows from the same
data.  Cauchy/Parseval reproduces the `C(0)` floor in (3.1); endpoint positive
atoms can cancel off-diagonal correlations, so a negative-center-only energy
cannot be inserted into the signed increment.

## 4. Exact common-height integer witness: what it does and does not refute

The exact-log odd-integer construction in
`ZETA23-COMMON-HEIGHT-MAXIMAL-INCIDENCE-FAIL-FAST-2026-08-13.md` adapts from
its older bill to the present `kappa`.  Keep

```text
b=39/250=.156,       a=1-b=.844,
h=(1+b)/2=.578,      t_0=2*pi*Y^a,
```

and select every `Y^kappa`-th one-turn gap.  Raising `kappa` to
`.01974048259` only decreases the selected-gap count.  The checker verifies
all strict requirements: low-denominator separation, positive global and
per-block counts, the Gafni--Tao tail envelope, the gap-square and cached
third-gap-moment bounds, rounding, small-mesh, local Peano, and continuum
errors.

At that single common height, on essentially every block the physical charge
has size

```text
|B_I(t_0)| asyp H_I Y^-kappa.                        (4.1)
```

Hence

```text
sum_I |B_I(t_0)|^4/H_I^3
 asyp sum_I H_I Y^(-4kappa)
 asyp Y^(1-4kappa).                                  (4.2)
```

This saturates `delta=0` and refutes every claim that common-height
incidence, geometry, integrality, and the present unsigned ledgers alone
force `(CH4)` with a fixed `delta>0`.

It is **not** an SPF rough set and not the primes.  It does not realize the
dyadic coefficients `c_(I,P)` in (1.1).  Therefore it is not a counterexample
to `(CH4)` for actual rough-Voronoi increments; it identifies the arithmetic
content an eventual proof must use.  No exact same-height SPF-rough or
actual-prime countermodel is currently known.

## 5. Finite laboratory boundary

The localized selector lab computes exact actual-mass tent vectors, uses one
height to choose its block denominators, combines complete bands coherently,
and certifies (2.1).  At `Y=10^6` its top sampled height has projected `L4`
ratio `2.559`, so the data give no empirical warrant for assuming a power
saving.

They also do not falsify one.  The scan is finite, uses at most sixteen
selected centers per parameter pair, omits the crossing band, and cannot
turn an order-one projected ratio into an asymptotic lower bound.  The
whole-shell rough-increment lab is even farther from `(CH4)` because it has
no curvature localization or one-height varying-modulus selector.

## 6. Final truth boundary

```text
actual rough/common-height selected (CH4):           LIVE
actual-prime or SPF-rough counterexample:             NONE
semiprime diagonal falsifies small-margin L4:         FALSE
universal abstract node-class fixed-margin L4:        FALSIFIED
abstract witness at current kappa:                    VERIFIED
delta=0 abstract bound:                               SATURATED, NOT REFUTED
finite lab gives an asymptotic verdict:               FALSE
bands-first selected normalization:                   EXACT / WEAKEST
primitive and full correlation identities:           EXACT
post-q tail or zero-free strip:                       NOT PROVED
```

## 7. Reproduction

```bash
python3 src/test_rough_common_height_l4_gate.py
python3 results/verify_zeta23_common_height_rough_l4_gate.py
```

The checker verifies both fourth-moment identities for complex tapered
vectors, band and weighted-block Holder, the exact exponent transfer, the
diagonal margins, and every strict exponent condition needed to adapt the
one-height integer witness to the current `kappa`.
