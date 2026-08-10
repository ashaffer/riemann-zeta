# Blomer--Pascadi Kloosterman saving as a conditional strip gate

Status: **exact exponent conversion proved; compatibility with the completed
long-mollifier reciprocity remainder is OPEN. This note does not prove a new
zero-free strip or RH.**

Date: 2026-08-09.

This note records a concrete graduated target for the active reciprocity
branch. Blomer and Pascadi's 2026 bilinear Kloosterman theorem supplies a
power saving of `c^(-1/32)` in the critical square-root range. If—and only if—the
completed long-mollifier reciprocity remainder can be reduced to their
bilinear form without losing that saving, the exponent would support the
uniform symmetric strip

```text
1/64 <= Re(rho) <= 63/64.                               (0.1)
```

No such reduction is claimed here.

## 1. The external bilinear theorem

Let `c` be a positive integer, let the two integer intervals have lengths at
most `N<=c`, and let `alpha_m,beta_n` be arbitrary complex sequences. Blomer
and Pascadi prove

```text
sum_(m,n; (m,n,c)=1)
 alpha_m beta_n S(am,n;c)

<< ||alpha||_2 ||beta||_2 c^(1+o(1))
 [ N^(1/8)c^(-3/32)
  +N^(5/16)c^(-3/16)
  +N^(2/3)c^(-7/18) ].                                  (1.1)
```

For full initial intervals the coprimality condition can be removed. The
result applies to arbitrary moduli.

At

```text
N=c^(1/2),                                               (1.2)
```

the three exponents in (1.1) are

```text
31/32, 31/32, 17/18.                                    (1.3)
```

The trivial bilinear exponent is `1`, so the net critical saving is

```text
delta_K=1/32.                                            (1.4)
```

## 2. Long-mollifier exponent conversion

The absolute reciprocity-error barrier isolated in
[`LONG-MOLLIFIER-PRIME-RECIPROCITY-STRESS.md`](LONG-MOLLIFIER-PRIME-RECIPROCITY-STRESS.md)
has scale

```text
Y^(2+o(1))                                               (2.1)
```

after the cutoff average. The long-mollifier target is

```text
T Y T^epsilon.                                           (2.2)
```

Suppose a completed transformation gave a **net** power saving `Y^(-delta)`
for the entire signed remainder, including all dyadic pieces, local factors,
transform errors, and cutoff losses. Then (2.1) would become

```text
Y^(2-delta+o(1)).                                        (2.3)
```

With

```text
Y=T^theta,                                               (2.4)
```

comparison with (2.2) requires

```text
theta(2-delta) <= 1+theta,

theta(1-delta) <= 1.                                    (2.5)
```

Hence the largest admissible nominal mollifier length is

```text
theta_max=1/(1-delta).                                   (2.6)
```

The averaged long-mollifier criterion would then give

```text
right zero boundary
 =(theta_max+1)/(2 theta_max)
 =1-delta/2,                                             (2.7)

symmetric strip width
 =(theta_max-1)/(2 theta_max)
 =delta/2.                                               (2.8)
```

Thus a net remainder saving of `Y^(-delta)` converts exactly into strip width
`delta/2`.

## 3. The critical `1/32` gate

Substituting `delta=1/32` into (2.6)--(2.8) gives

```text
theta_max=32/31,                                         (3.1)

Re(rho)<=63/64,                                          (3.2)

1/64<=Re(rho)<=63/64                                    (3.3)
```

by functional-equation symmetry.

This is a meaningful intermediate milestone: the required nominal
mollifier overlength is only

```text
Y=T^(32/31),                                             (3.4)
```

not an arbitrarily long mollifier.

## 4. Why (3.3) is not yet a theorem

The squarefree reciprocity work has exposed a centered sieve kernel in the
variables `re-1` and `re+1`, but it has not produced a Kloosterman bilinear
form satisfying every hypothesis of (1.1). The following compatibility steps
remain load-bearing.

### 4.1 Modulus identification

One must identify a modulus `c` in the completed dual expression and prove
that all gcd and conductor factors are retained correctly. The current
squarefree character kernel is not itself a Kloosterman sum.

### 4.2 Critical lengths

The transformed variables must be dyadically arranged with both relevant
lengths comparable to `sqrt(c)`. Outside that range, the saving from (1.1) is
the maximum of three different exponent terms and may be smaller or zero.

### 4.3 Sequence norms

The `L2` norms of the transformed Moebius, divisor, cutoff, and AFE sequences
must be evaluated without losing a compensating power. A saving in the
operator norm is useless if normalization or completion costs `Y^(1/32)`.

### 4.4 Coprimality and zero frequencies

The condition `(m,n,c)=1`, or the special full-interval exception, must match
the actual transformed ranges. Ramanujan/zero-frequency sectors must be
removed and evaluated separately rather than hidden in an error term.

### 4.5 All moduli and terminal smoothing

The theorem is strong enough for arbitrary moduli, but the completed
reciprocity expression includes a modulus sum, terminal cutoff, and local
corrections depending on `re+/-1`. The gain must survive summation over all
of those pieces.

### 4.6 Signed transform error

The prime reciprocity stress test showed that the published pointwise
reciprocity error, summed absolutely, already returns the `theta=1` barrier.
The bilinear estimate must act on an exact or signed completed transform; it
cannot simply be appended after the same triangle inequality.

## 5. Exact theorem card for the next reduction

A sufficient new theorem would have the following shape.

### Conditional completed Kloosterman reduction

For one fixed smooth time weight and for `Y=T^(32/31)`, decompose the signed
long-mollifier remainder into `T^o(1)` dyadic forms

```text
R(T,Y)=sum_j C_j(T,Y)+O(TY T^epsilon),                   (5.1)
```

where every `C_j` is transformed into

```text
sum_(m in I_j, n in J_j)
 alpha_(j,m) beta_(j,n) S(a_j m,n;c_j),                 (5.2)
```

with

```text
|I_j|,|J_j| <= N_j,
N_j=c_j^(1/2+o(1)),                                      (5.3)
```

and the total normalization satisfies

```text
sum_j ||alpha_j||_2 ||beta_j||_2 c_j^(1+o(1))
 <=Y^2 T^o(1).                                           (5.4)
```

All completion, noncoprime, and zero-frequency terms must already be included
in (5.1). Applying (1.1) would then give

```text
R(T,Y)<<Y^(2-1/32)T^o(1)<=TY T^o(1),                    (5.5)
```

which would yield (3.3) through the long-mollifier criterion.

The actual challenge is proving (5.1)--(5.4), not the arithmetic in Section 2.

## 6. Other length ranges

Write

```text
N=c^nu.                                                  (6.1)
```

The three exponents in (1.1) are

```text
E_1(nu)=1+nu/8-3/32,
E_2(nu)=1+5nu/16-3/16,
E_3(nu)=1+2nu/3-7/18.                                   (6.2)
```

The trivial exponent is

```text
E_triv(nu)=min(1,nu+1/2).                               (6.3)
```

Thus the available saving at that dyadic length is

```text
delta(nu)
 =max(0,E_triv(nu)-max(E_1(nu),E_2(nu),E_3(nu))).        (6.4)
```

A complete reduction must use the minimum saving over every dyadic block that
contributes at power scale. Blocks outside the nontrivial range cannot be
silently discarded.

## 7. Reproducibility

The exact exponent arithmetic is implemented in

```text
src/kloosterman_strip_gate.py
src/test_kloosterman_strip_gate.py.
```

The tests verify:

1. the three critical exponents (1.3);
2. the exact `1/32` saving;
3. `theta_max=32/31`;
4. strip width `1/64` and right boundary `63/64`;
5. the equality of the remainder and target exponents at the gate;
6. the general identity `strip width=delta/2`.

The tests do not verify the missing completed reduction (5.1)--(5.4).

## 8. Primary source

- V. Blomer and A. Pascadi, *Bilinear forms with Kloosterman sums via
  quadratic characters*, arXiv:2607.24311, Theorem 1.1. The paper proves the
  bound for all moduli and records the critical `c^(-1/32)` saving.
