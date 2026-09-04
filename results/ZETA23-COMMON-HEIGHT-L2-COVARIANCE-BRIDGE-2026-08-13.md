# Common-height physical `L2` covariance bridge

**Date:** 2026-08-13  
**Verdict:** exact reduction; the arithmetic covariance input remains open.

Let

```text
B_I(t)=sum_P hat(Delta^t_(I,P))(a_I(t))
```

be the bands-first selected coefficient from the common-height `CH4` target,
with the taper, exact residual logarithmic phase, crossing band, and boundary
transport already included in `Delta`.  The signed measures before and after
the telescope each have block mass `O(H_I)`, hence

```text
|B_I(t)| <= C H_I.                                      (1.1)
```

Therefore

```text
sum_I |B_I|^4/H_I^3
 <= C^2/H_min sum_I |B_I|^2.                            (1.2)
```

Throughout the full aperture `t<=Y^(50/33)`, the curvature blocks satisfy

```text
H_min=Y^(8/33+o(1)).                                    (1.3)
```

More generally, suppose the selected physical covariance theorem has exponent
`lambda`:

```text
sup_t sum_I |B_I(t)|^2 << Y^(lambda+o(1)).             (CL2_lambda)
```

implies

```text
sup_t sum_I |B_I(t)|^4/H_I^3 << Y^(lambda-8/33+o(1)).  (1.4)
```

For the hostile bill `kappa=.01974048259`, this proves `CH4` whenever

```text
lambda < 1+8/33-4kappa = 1.163462... .                 (1.5)
```

The clean benchmark `lambda=1` proves `CH4` for every fixed

```text
0 < delta < 2/33-kappa = .040865577... .                (1.6)
```

This `CL2` is not the already-falsified arbitrary-selector residue-energy
bound.  It evaluates only the coefficient chosen by one common height and
combines all dyadic bands before squaring.

## The diagonal is already below the frontier

After the audited long-terminal-edge deletion, every prime gap is at most
`G=Y^(797/5000+o(1))`.  Every rough set in the telescope contains the shell
primes, so its gaps are no larger.  Each of the two positive endpoint
Voronoi measures has total mass `O(Y)` and atom mass `O(G)`.  With bounded
taper and bounded block overlap,

```text
sum_(I,n) |d_(I,t)(n)|^2 << Y G Y^o
                              =Y^(1.1594+o(1)).       (1.7)
```

This is below the closing covariance frontier by

```text
(1+8/33-4kappa)-(1+.1594)=.004062312... .             (1.8)
```

Thus it is enough to prove only the signed off-diagonal estimate

```text
Re sum_I sum_(n!=m in I)
 d_(I,t)(n) conjugate(d_(I,t)(m)) exp(i t log(n/m))
 <<Y^(1.1594+o(1)).                                    (OD2)
```

Together with (1.7), `(OD2)` proves `CH4` for every fixed

```text
0<delta<(8/33-4kappa-.1594)/4=.001015578... .          (1.9)
```

If

```text
B_I(t)=sum_(n in I) d_(I,t)(n) exp(i t log n),
```

then the exact remaining input is the short-shift covariance estimate

```text
sum_I sum_(n,m in I)
 d_(I,t)(n) conjugate(d_(I,t)(m)) exp(i t log(n/m))
 <<Y^(lambda+o(1)),  lambda<1.163462... .               (1.10)
```

Here `d_(I,t)` is the actual q-first rough-to-prime transport coefficient and
depends on the common-height selector.  No modulus average, maximum over
numerators, or coefficient-free gap-energy estimate may replace `(OD2)`.

The reduction is exact; `(OD2)` is not proved here.  Its advantage is strategic:
it replaces a fourth-correlation theorem by a selected short-shift covariance
theorem.  The clean `lambda=1` benchmark has margin exceeding `.16`; the
already-proved diagonal-scale reduction leaves the smaller but still positive
margin `.004062312...` before the fourth power.
