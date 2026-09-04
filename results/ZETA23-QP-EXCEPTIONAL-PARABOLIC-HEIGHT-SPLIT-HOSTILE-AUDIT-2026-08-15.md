# QP exceptional-parabolic height split: hostile audit

**Date:** 2026-08-15  
**Audited artifact:**
`ZETA23-QP-EXCEPTIONAL-PARABOLIC-HEIGHT-SPLIT-AND-SCALED-ADDITIVITY-2026-08-15.md`  
**Verdict:** **PASS**, with the scope restricted to the exceptional rational
two-plane sector.

The proved bound is

```text
Q_exceptional(z) << D^(11/8) q^o(1) ||z||_2^4.     (0.1)
```

It is not a global fourth-trace estimate.  In particular, generic rank-three
difference lattices are outside the parabolic inverse theorem.

## 1. The primitive height is the correct quadratic height

After fixing the denominator congruence of one parabolic chart, its integral
product matrices are

```text
M(n)=M0+n M1+n^2 M2.
```

Because the polynomial is integer-valued on the reparametrized progression,
`2M2` is integral.  Writing `2M2=g e`, with `e` primitive rank one, gives
`g!=0` and

```text
||M2||_infinity >= ||e||_infinity/2.
```

Thus no denominator or nonprimitive carrier-slope factor weakens the
quadratic coefficient.  If `h=||e||_infinity`, one product-matrix entry is a
quadratic of leading coefficient at least `h/2` inside an interval of length
`O(D)`.  Consequently a chart has

```text
m_ch << 1+sqrt(D/h).                               (1.1)
```

For three or more parameters, the pinned common-level polynomial is
constant identically, so its quadratic coefficient says exactly that `e`
kills the signed color matrix.  The rank-one fixed-relation theorem therefore
applies with no mismatch between the geometric and color-relation heights.

## 2. The high/low sum and its exact stopping point

Split at chart length `M`.  Low charts cost

```text
Q_low << M D q^o(1),                               (2.1)
```

using the global determinant-layer color mass.  A high chart has primitive
height `h<<H=D/M^2`.  Primitive rank-one `2 by 2` matrices of height at most
`H` number `H^2 q^o(1)`.  On one dyadic height block, (1.1) and the proved
fixed-relation color bound `sqrt(D)q^o(1)` give

```text
Q_high << D H^(3/2) q^o(1)
       = D^(5/2) M^(-3) q^o(1).                    (2.2)
```

Balancing (2.1) and (2.2) gives

```text
M=D^(3/8),              Q_low+Q_high<<D^(11/8+o(1)). (2.3)
```

At the critical scale, the scalar inputs can all saturate simultaneously:

```text
relation height cutoff       D^(1/4),
number of directions         D^(1/2),
color mass per direction     D^(1/2),
chart length                 D^(3/8).
```

Their product is `D^(11/8)`.  Hence the fixed-relation theorem, direction
count, and determinant-layer mass alone cannot prove the target `D` bound.
A further cross-direction operator merger or actual-carrier incidence saving
is required.

## 3. Actual primes do not restore ordinary additivity at color level

There is an exact prime-color witness at the active determinant scale:

```text
q=166013,
C=(93607,87383;79229,73961),
r=(11,13),                 s=(14,15).
```

All four entries of `C` are prime and lie in the project width-`0.2` shell
about `q/2`.  Direct integer calculation gives

```text
r1*s1*c11-r1*s2*c12-r2*s1*c21+r2*s2*c22 = 0,
det C                                                   = -380,
c11+c22-c12-c21                                        = 956.
```

Also `380=O(q^(16/33))`.  Thus actual prime support, a short unequal-slope
rank-one relation, and the active determinant range do **not** imply raw
additivity or equal carrier slopes.  This witness concerns colors only; it
does not construct an actual-prime affine carrier chart.

The Cilleruelo--Garaev modular-hyperbola idea likewise gives only a
fixed-color statement after fixing two projective numerator variables.
Summing those variables restores the missing polynomial direction count.
The determinant-divisor/thin-strip argument already proves the legitimate
fixed-color conclusion (`q^o(1)` small primitive directions), but it does not
merge directions used by different colors.

```text
primitive chart-height inequality:                  PASS;
exceptional parabolic D^(11/8) weighted sum:         PASS;
prime support forces raw additivity/equal slopes:    FALSE;
actual-prime affine-chart counterexample:            NOT CONSTRUCTED;
generic rank-three sector:                           NOT COVERED;
full four-cycle D^(1+o):                             OPEN.
```

Exact replay is in `src/qp_four_cycle_parabolic_global_audit.py` and
`src/test_qp_four_cycle_parabolic_global_audit.py`.
