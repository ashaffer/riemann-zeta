# Exact central-residue polynomial for proportional-order mollifiers

Status: **exact finite residue and annihilator identities proved; the generic
high-order amplification shortcut is closed.  No zero-free strip or RH proof
is claimed.**

Date: 2026-08-09.

This note continues
[`HIGH-ORDER-MOLLIFIER-SHIFT-AUDIT.md`](HIGH-ORDER-MOLLIFIER-SHIFT-AUDIT.md).
It resolves the first symbolic task left there and strengthens the obstruction:
not only does the order-`k` Mellin transform create a central pole at `w=1`,
but the exact operator that annihilates its full residue polynomial also
removes the entire apparent high-order amplification of a target zero.

## 1. Local form at the central pole

For the logarithmic mollifier of order `k`, the Mellin transform contains

```text
H_(t,k)(w)
 = k! / [(w-1)^(k+1) zeta(w-1/2+it)].                   (1.1)
```

Multiplication by the original first-order auxiliary factor supplies only
`(w-1)^2`.  After separating the target-zero denominator and all other factors,
the central part of the shifted contour has the form

```text
k! x^w R_t(w) / (w-1)^(k-1),                            (1.2)
```

where `R_t` is analytic at `w=1`.

Put

```text
L=log x,
z=w-1,
R_t(1+z)=sum_(j>=0) r_j(t) z^j.                         (1.3)
```

Then (1.2) becomes

```text
k! x exp(Lz)
  [sum_(j>=0) r_j(t)z^j] / z^(k-1).                    (1.4)
```

## 2. Exact residue polynomial

For `k>=2`, coefficient extraction at `z=0` gives

```text
Res_(w=1) (1.2)
 = k! x sum_(j=0)^(k-2)
     r_j(t) L^(k-2-j)/(k-2-j)!.                         (2.1)
```

Thus the complete central residue is

```text
x P_(k-2,t)(log x),                                     (2.2)
```

where `P_(k-2,t)` has degree at most `k-2`.

The first cases are

```text
k=1:  no central pole,

k=2:  2! x r_0,

k=3:  3! x [r_0 L+r_1],

k=4:  4! x [r_0 L^2/2+r_1 L+r_2].                      (2.3)
```

No asymptotic theorem is used here; (2.1) is a finite Taylor-coefficient
identity.

## 3. The exact annihilator

Let

```text
A = d/dL - 1.                                            (3.1)
```

For every polynomial `P`,

```text
A[e^L P(L)] = e^L P'(L).                                (3.2)
```

Consequently

```text
A^(k-1)[x P_(k-2,t)(log x)] = 0.                        (3.3)
```

So `A^(k-1)` annihilates the complete central residue, independently of its
coefficients.

Now consider the naively isolated target carrier.  Suppressing analytic
factors that are nonzero at the target, its high-order part is

```text
e^(w_rho L)/(w_rho-1)^(k-1).                            (3.4)
```

But

```text
A[e^(w_rho L)] = (w_rho-1)e^(w_rho L),                  (3.5)
```

and therefore

```text
A^(k-1)
 [e^(w_rho L)/(w_rho-1)^(k-1)]
 = e^(w_rho L).                                         (3.6)
```

Equation (3.6) is the exact repayment law:

> annihilating the full central polynomial removes exactly the
> `(w_rho-1)^(-(k-1))` factor responsible for the apparent proportional-order
> target amplification.

This conclusion does not depend on Stirling approximation or an exponent
comparison.

## 4. Partial annihilation gives no hidden gain

After `j` applications of `A`, the central polynomial degree falls from
`k-2` to at most `k-2-j`, while the target factor changes from

```text
(w_rho-1)^(-(k-1))
```

to

```text
(w_rho-1)^(j-k+1).                                      (4.1)
```

Thus every degree of generic center removal consumes one degree of target
amplification.  Full center removal at `j=k-1` leaves factor one; applying
more derivatives attenuates the target.

There is no intermediate choice that both kills the entire generic center
and retains a negative power of `w_rho-1`.

## 5. Finite-difference version and support cost

The scale-discrete analogue is

```text
A_h f(L)=f(L+h)-e^h f(L).                               (5.1)
```

For the center,

```text
A_h[e^L P(L)]
 =e^(L+h)[P(L+h)-P(L)],                                 (5.2)
```

so `A_h^(k-1)` kills every center polynomial of degree at most `k-2`.

On the target carrier it contributes

```text
[e^(w_rho h)-e^h]^(k-1)
 =(e^h)^(k-1)[e^((w_rho-1)h)-1]^(k-1).                 (5.3)
```

After the derivative normalization `h^(-(k-1))`, the small-`h` limit of
(5.3) is precisely `(w_rho-1)^(k-1)`, again repaying the target denominator.
Without that normalization the target is suppressed.

Moreover, `k-1` forward shifts use logarithmic scale support `(k-1)h`.  When
`k` is proportional to `L`, fixed `h` incurs linear scale support.  Shrinking
`h` to keep support sublinear introduces the same normalization cost.  This
matches the repository's earlier high-order scale-filter obstruction from a
second, exact residue calculation.

## 6. Consequence for the zero-free-strip program

The proportional-order mollifier remains useful as a diagnostic and as a
coefficient regularizer, but it cannot be inserted into the first-order
Bettin--Gonek detector as a generic free amplifier.

The route now has only two logically valid possibilities:

1. **Retain the center.**  Estimate the completed combination of the target
   carrier, `x P_(k-2,t)(log x)`, and the remaining contour before taking
   absolute values.
2. **Use arithmetic structure.**  Find a relation tying the Taylor
   coefficients `r_j(t)` to the Möbius-weighted critical-line moment so that
   cancellation is stronger than generic polynomial annihilation.

A coefficient-blind differential or finite-difference operator is now closed:
it either leaves part of the center or repays the entire high-order target
gain.

The more promising active zero-free-strip target therefore remains the signed
long-mollifier twisted-moment remainder in
[`LONG-MOLLIFIER-TWISTED-MOMENT-REDUCTION.md`](LONG-MOLLIFIER-TWISTED-MOMENT-REDUCTION.md),
where the main aggregate is already at natural scale and the Möbius signs,
cutoff kernel, and rational twists are retained jointly.

## 7. Reproducibility

The exact rational coefficient ledger and tests are in

```text
src/high_order_mellin_center.py
src/test_high_order_mellin_center.py.
```

They verify:

- formula (2.1) for arbitrary rational Taylor prefixes;
- annihilation of every central polynomial after `k-1` shifted derivatives;
- exact target-factor repayment for rational nonzero `w_rho-1`;
- the one-for-one partial-annihilation tradeoff (4.1).

The result is finite algebra.  It does not certify the analytic hypotheses
needed to derive (1.2) from a complete zeta contour, which remain those stated
in the parent audit.
