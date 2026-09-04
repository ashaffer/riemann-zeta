# QP four-cycle: weighted `q^2` principal polar closure

**Date:** 2026-08-24  
**Verdict:** the coarse principal/logarithmic channel is power-small for the
coefficient-normalized fourth-trace problem.  The primitive cross-block
square function remains open, so the sharp four-cycle theorem is not proved.

## 1. Why the unweighted audit saw a large mode

Put `p0=q/2` and `x_p=log(p/p0)`.  Every physical triple satisfies

```text
x_a+x_b+x_c=log(1+rho/q^3)=O(D/q^2).                 (1.1)
```

For the unweighted triangle adjacency `T`,

```text
x^* T x
 =sum_{tau={a,b,c}} (|x_a+x_b+x_c|^2
                       -|x_a|^2-|x_b|^2-|x_c|^2).    (1.2)
```

Thus the logarithmic vector is a genuine negative coarse mode whenever the
triangle degrees are reasonably regular.  Subtracting only the constant
vector is not the right unweighted selected-BDH theorem.

This mode is the physical manifestation of the principal character in the
exact conductor-`q^2` decomposition.  It is a smooth multiplicative Hankel
polar channel, not primitive residual dispersion.

## 2. The weighted carry operator pays `D/q`

For the four-cycle problem let `z` be the color coefficient vector and let
`P_c^0` denote the coarse color layer cut out by

```text
W((8abc-q^3)/q^2).                                      (2.1)
```

The exact principal coefficient is `2D/q` up to harmless endpoint factors,
so

```text
A_(z,0)=(2D/q) sum_c z_c P_c^0.                        (2.2)
```

Because all variables are in fixed proportional `q`-shells, (2.1) has the
following elementary properties:

* for fixed `(a,c)`, the admissible interval for `b` has length `O(1)`;
* for fixed `(a,b)`, the admissible interval for `c` has length `O(1)`;
* consequently `P_c^0` has `O(1)` row and column degree and `O(q^(1+o(1)))`
  entries;
* every matrix cell belongs to only `O(1)` coarse color layers.

Schur and Cauchy therefore give, after absorbing constants and `q^o(1)`,

```text
||A_(z,0)||op
   <= (D/q)||z||1
   <= D/q^(1/2) ||z||2,                                (2.3)

||A_(z,0)||HS^2
   <= D^2/q ||z||2^2.                                  (2.4)
```

Using `||A||S4^4<=||A||op^2||A||HS^2`,

```text
||A_(z,0)||S4^4
   <= D^4/q^2 q^o(1)||z||2^4
   = D^(-1/8+o(1))||z||2^4,                            (2.5)
```

because `q=D^(33/16+o(1))`.

Thus the entire coarse principal continuum—including the logarithmic mode
in (1.2)—is far below the desired `D^(1+o(1))` fourth-trace budget.  The
earlier `O(D)` Schur obstruction concerned the **unweighted** carrier matrix
and does not transfer to normalized arbitrary color coefficients.

## 3. What remains

After (2.5), the conductor-`q^2` decomposition leaves the primitive residual
packets.  In physical language these are the ordered `q`-width residual
triangle matchings.  Their scalar square-function budget is exactly `D`, but
the required mask-stable estimate for their cross-Gram is still open.

```text
coarse principal/logarithmic polar in weighted FC: CLOSED;
primitive ordered-block vector square function:     OPEN;
post-peeling mask compatibility:                     OPEN;
best unconditional global fourth trace:             D^(9/8+o(1));
sharp D^(1+o(1)) four-cycle bound:                   NOT PROVED.
```

Finite ledger and tests:

```text
src/qp_q2_principal_weighted_fc.py
src/test_qp_q2_principal_weighted_fc.py
```
