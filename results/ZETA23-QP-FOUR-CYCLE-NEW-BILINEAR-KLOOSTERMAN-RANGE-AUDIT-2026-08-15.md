# QP four-cycle: August 2026 bilinear Kloosterman range audit

**Date:** 2026-08-15  
**Verdict:** none of the checked theorems by itself proves the four-cycle
bound.  Mohammadi's
small-box theorem has the closer phase, but the QP carrier condition is a
one-variable reciprocal graph rather than two independent boxes.  The
Milićević--Qin--Wu theorem accepts arbitrary `ell^2` coefficients and, in an
optimistic modulus-`q`, length-`D` model, gives the explicit saving
`q^(-1/275+epsilon)`.  Its kernel is a **complete normalized Kloosterman
sum**, however, not the incomplete reciprocal-carrier graph; and even that
optimistic saving is far smaller than the factor `D=q^(16/33+o(1))` needed
to turn a `D^2` completion count into the four-cycle scale.

No QP, strip, or full `(FC)` theorem is asserted here.

---

## 1. Exact QP input

For fixed coprime actual-shell rows `a1!=a2`, the local common-neighbor
problem has the exact parametrization

```text
c(v) == inverse(a1)*v (mod a2),                 |v|<<D,
distance(q^3/(8*a1*c(v)), S)<<D/q,              D=q^(16/33+o(1)). (1.1)
```

The shell lift `c(v)` is unique, and then the carrier `b(v)` is unique.  So
the required object is a weighted count on the graph

```text
v -> c(v) -> b(v) approximately q^3/(8*a1*c(v)).       (1.2)
```

It is not initially a bilinear sum over two independent intervals.  With
arbitrary color coefficients, the weight attached to `v` also depends on
the lifted prime powers `c(v),b(v)`.

---

## 2. Mohammadi: the phase matches, the variables do not

[Mohammadi, Theorem 1](https://arxiv.org/abs/2608.01203) treats, over
`F_(p^n)`,

```text
sum_(x in B1) sum_(y in B2) alpha(x) beta(y)
 psi(A*x*y+B*(x*y)^(-1)),                         (2.1)
```

for coordinate boxes and pointwise bounded **separable** weights.  It gives
a relative `p^(-delta(epsilon))` saving when

```text
|B1|*|B2| >= (p^n)^(1/2+epsilon).                 (2.2)
```

For `n=1` and two hypothetical length-`D` intervals, the size condition is
comfortably satisfied:

```text
D^2=p^(32/33+o(1)),
32/33-1/2=31/66.                                  (2.3)
```

But the square-root decomposition naturally suggested by the desired
degree bound would have two boxes of length `sqrt(D)`, whose product is

```text
D=p^(16/33+o(1))=p^(1/2-1/66+o(1));               (2.4)
```

this misses (2.2), rather than meeting it.

More fundamentally, (1.1) has only the short variable `v`; its reciprocal
carrier is determined, not independently summed.  Taking one box to be a
singleton puts (2.1) below (2.2).  Introducing `b` as an independent
variable requires a delta constraint enforcing `b=b(v)`; Fourier completion
of that delta adds a frequency sum and destroys the two-factor separable
form in (2.1).  The arbitrary prime-power weights inherited from `z` are
also joint weights on that graph, not `alpha(x)beta(y)` on full boxes.

There is a second scope mismatch for nonprime shell nodes.  Congruence in
(1.1) is in the ring `Z/(p^j)Z` when `a2=p^j`; the field `F_(p^j)` in (2.1)
has the same cardinality but different multiplication and inversion.  The
theorem can be compared directly only to the prime-row subcase `n=1`.

Finally, the theorem states only an unspecified positive
`delta(epsilon)`.  Even if a legal two-length-`D` reduction were found, its
statement alone would not supply the relative `D^(-1)=q^(-16/33)` saving
needed to reduce a generic `D^2` count to `D`.

Thus Mohammadi is a genuinely relevant phase theorem, but it does not apply
to the present rank-one reciprocal graph with the required quantitative
strength.

---

## 3. Milićević--Qin--Wu: exact optimistic exponent ledger

[Milićević--Qin--Wu, Theorem 1.1](https://arxiv.org/abs/2511.07550) bounds

```text
sum_(m<=M) sum_(n<=N) alpha_m beta_n Kl_2(cmn;q),         (3.1)
```

where

```text
Kl_2(t;q)=q^(-1/2) sum_(x mod q)^* e_q(t*x+inverse(x)),   (3.2)
```

and the two coefficient sequences are arbitrary in `ell^2`.  Under

```text
M<=N*q^(1/4),       M^(7/5)*N<q^(3/2),       M*N<=q^(5/4), (3.3)
```

the multiplier beyond the trivial normalized scale is

```text
M^(-1/2)q^(1/6)
 +M^(-3/25)N^(-3/10)q^(1/5)
 +(MN)^(-3/16)q^(11/64).                            (3.4)
```

Give the theorem every optimistic advantage: use modulus comparable with
the shell scale `q`, and take `M=N=D=q^(16/33)`.  Conditions (3.3) hold,
with margins

```text
3/2-(12/5)*(16/33)=37/110,
5/4-2*(16/33)=37/132.                               (3.5)
```

The three terms in (3.4) then save respectively

```text
q^(-5/66),             q^(-1/275),             q^(-7/704). (3.6)
```

Hence the sum is dominated by the rigorous but small saving
`q^(-1/275+epsilon)`.  This is consistent with the paper's balanced
nontriviality threshold `M=N>>q^(10/21+delta)`, since

```text
16/33-10/21=2/231.                                  (3.7)
```

At the square-root target lengths `M=N=sqrt(D)=q^(8/33)`, the first term in
(3.4) is instead `q^(1/22)` and the theorem is not nontrivial.  If the
natural modulus is retained as `Q=q^3`, length `D=Q^(16/99)` is much farther
below the balanced threshold.

The decisive issue is again the kernel.  Formula (3.2) contains a complete
sum over an internal unit `x`.  Formula (1.1) is an incomplete short graph
of affine lifts and reciprocal carriers; it has no such complete internal
average.  Completing the `v` interval does not yield (3.1) with two free
coefficient sequences: the carrier-shell detector and `z` weights remain
coupled to the same lift.  No exact reduction from `(FC)` or (1.1) to (3.1)
is presently available.

Even ignoring this kernel mismatch, `q^(-1/275)` does not replace the
missing factor `D=q^(16/33)`.  It could become a modest exponent gain only
after a new reduction that loses no additional powers and requires merely
some cancellation, not the full square-root degree theorem.

---

## 4. Blomer--Pascadi: the exponent now clears the numerical gap

[Blomer--Pascadi, Theorem 1.1](https://arxiv.org/abs/2607.24311) proves for
an arbitrary modulus `c`, intervals `I,J` of common maximum length `N`,
arbitrary separated `ell^2` coefficients, and a unit `a mod c`,

```text
sum_(m in I,n in J;(mn,c)=1) alpha_m beta_n S(am,n;c)
 <<||alpha||_2 ||beta||_2 c^(1+o(1))
   [N^(1/8)c^(-3/32)+N^(5/16)c^(-3/16)
                         +N^(2/3)c^(-7/18)].       (4.1)
```

Relative to the Weil/Cauchy scale
`||alpha||_2||beta||_2 N c^(1/2)`, the three factors are

```text
c^(13/32)N^(-7/8),
c^(5/16)N^(-11/16),
c^(1/9)N^(-1/3).                                  (4.2)
```

The result is nontrivial throughout
`c^(13/28+epsilon)<N<c^(7/12-epsilon)`.  Thus, if an exact reduction to
one balanced form with `c asymp q` and `N=D=q^(16/33)` were available, the
range margin would be

```text
16/33-13/28=19/924.                                (4.3)
```

More importantly, the three active savings in (4.2) would be

```text
q^(-19/1056),       q^(-1/48),       q^(-5/99).   (4.4)
```

The first dominates.  It is stronger than the numerical square-root
shortfall `q^(-1/66)` by

```text
19/1056-1/66=1/352.                                (4.5)
```

This is a materially different verdict from the earlier MQW audit: the new
theorem has enough exponent **conditional on a lossless balanced
Kloosterman reduction**.

That reduction is not presently in the QP argument.  The exact common-row
form remains

```text
v -> c(v) -> b(v),                 |v|<<D,          (4.6)
```

a one-variable reciprocal graph.  Formula (4.1) has two independent
interval variables and a complete internal unit sum

```text
S(am,n;c)=sum_(x mod c)^* e_c(amx+n inverse(x)).    (4.7)
```

Completing the reciprocal variable in (4.6) creates a dual frequency, but
the carrier-shell detector and arbitrary prime-power `z` weights remain
joint functions of the same lift; they have not been factored as
`alpha_m beta_n`.  Nor is the new `x` average in (4.7) already present.
Taking one interval to be a singleton forfeits (4.3)--(4.4).  The positive
fixed-color completion count also has no oscillatory phase until a Fourier
completion is introduced, and its zero frequency must be bounded
separately.

The modulus issue is less severe than for the finite-field small-box
theorem: Blomer--Pascadi is uniform for arbitrary integer `c`, so it can in
principle accept an actual prime-power row modulus.  The remaining mismatch
is the kernel and separated-coefficient structure, not merely the range.
Variation of that modulus across row pairs would still require a further
summation argument.

### Shen does not reach the active power scale

[Shen, Theorem 1](https://arxiv.org/abs/2607.06575) treats a Lehmer/incomplete
reciprocal problem for a prime modulus, but requires

```text
N >= q^(1/2) exp(-(log q)^(1/2-2 delta)),           (4.8)
```

and gives logarithmic rather than fixed-power penetration below the square
root.  Our length

```text
D=q^(1/2-1/66)=q^(1/2)exp(-(log q)/66)              (4.9)
```

is asymptotically much shorter than (4.8).  Shen therefore does not cover
the active range.

---

## 5. Binary range verdict

```text
Mohammadi phase Axy+B/(xy) relevant:                 YES;
QP variables form two independent boxes:            NO;
Mohammadi sqrt(D)-by-sqrt(D) threshold met:           NO, misses by q^(1/66);
Mohammadi theorem supplies full D saving:             NOT STATED;
MQW accepts arbitrary separated ell^2 coefficients:  YES;
MQW applies optimistically at M=N=D, modulus q:       YES;
optimistic MQW relative saving:                       q^(-1/275+epsilon);
MQW applies nontrivially at M=N=sqrt(D):              NO;
QP reciprocal graph is a complete Kl_2 kernel:        NO;
BP applies numerically at balanced M=N=D, modulus q:  YES;
BP active relative saving:                            q^(-19/1056+o(1));
BP saving exceeds the 1/66 shortfall:                 YES, margin 1/352;
exact QP-to-BP separated-kernel reduction:            NOT PROVED;
Shen reaches D=q^(1/2-1/66):                          NO;
new papers prove the four-cycle bound:                NO.
```

The smallest theorem still matching the problem is now sharper: either an
exact factorization of the weighted reciprocal carrier into balanced
Blomer--Pascadi forms with total loss `<q^(1/352)`, or a direct weighted
incomplete reciprocal-graph estimate of the same strength, uniform in the
actual prime-power coefficients.
