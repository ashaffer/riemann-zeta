# PQR addendum: the small `E` defect, residue rotations, and associator

**Date:** 2026-08-30  
**Status:** exact arithmetic refinement of the curvature theorem; the final
rotation-rigidity theorem remains open; no zero-free strip and no proof of RH

## 0. Verdict

For a pointwise-clean same-side prime ratio shadow, put

```text
Q=2Y,                         d_ab=2p_ab-Q,
K_kji=d_ki-d_kj-d_ji,
E_kji=QK_kji-d_kj d_ji.                              (0.1)
```

Then

```text
E_kji=2(Qp_ki-2p_kj p_ji),
0<|E_kji|<<H=Y^2/B=Y^(16/33),
E_kji=2 (mod 4).                                     (0.2)
```

For every fixed middle vertex `j`, the full matrix
`(E_kji)_(k>j,i<j)` has **exact rank one**, with no carrier-width
restriction.  The proof is especially clean:

```text
E_kji=-d_kj d_ji (mod Q),
```

so every quadratic minor is divisible by `Q`, while its absolute value is
`O(H^2)=o(Q)`.

This strictly strengthens the conclusions extracted from the preceding
`K`-charge phase split.  It does not define a smaller input class than PQR:
all of these conclusions follow from the same transported-shadow hypothesis.
It also produces modular rotations and a global rank-two projective
completion.  The exact four-vertex associator is information-neutral: it is
an identity for arbitrary edge labels.  The projective normal form still
does not close PQR, because arbitrary `GL_2` chains can be long and the small
signed even defects do not have prime-factor uniqueness entry by entry.

## 1. Exact formula, size, parity, and gcd

Retain the hypotheses and notation of
`ZETA23-VIBE-PQR-ODD-CURVATURE-CHARGE-ADDENDUM-2026-08-30.md`:

```text
B=Y^(50/33),          delta=Y/B,          H=Y delta,
p_ab=Y exp[sigma omega(a_a-a_b)]+O(delta),
```

with distinct ordinary primes in the fixed shell of width `w=1/5`.

### Proposition 1.1

For every `k>j>i`,

```text
E_kji=2(Qp_ki-2p_kj p_ji).                           (1.1)
```

It satisfies

```text
2<=|E_kji|<<H,
v_2(E_kji)=1.                                        (1.2)
```

Moreover no shell prime occurring in its triangle divides `E_kji/2`, and

```text
gcd(E_kji/2,Q p_ki p_kj p_ji)=1.                    (1.3)
```

No fixed sign for `E_kji` follows.

#### Proof

Expanding `(0.1)` with `d_ab=2p_ab-Q` gives `(1.1)`.  At the decomposable
reference,

```text
d*_ki=Q[exp(sigma(x+y))-1],
d*_kj=Q[exp(sigma x)-1],
d*_ji=Q[exp(sigma y)-1],
K*=Q[exp(sigma x)-1][exp(sigma y)-1],
```

and therefore `QK*-d*_kj d*_ji=0`.  Each `d` and `K` has error `O(delta)`,
while all reference quantities are `O_w(Y)`.  Hence

```text
|E_kji|<<Y delta=H.                                  (1.4)
```

The quantity in parentheses in `(1.1)` is odd: `Qp_ki` is odd and
`2p_kj p_ji` is even.  Thus `E=2 (mod 4)`, proving nonvanishing and the
lower bound in `(1.2)`.

No shell prime divides `Q`.  Indeed, if `p|Q`, the odd integer `Q/p` would
lie in

```text
[2exp(-w),2exp(w)] subset (1,3)
```

at `w=1/5`, which contains no odd integer.  Reducing `E/2` modulo each of
`Q,p_ki,p_kj,p_ji`, and using global distinctness, now proves `(1.3)`.
The reference defect is zero, so the approximation itself supplies no sign;
parity supplies only nonvanishing.  QED

In particular

```text
gcd(E_kji,Q)=1,
E_kji in (Z/QZ)^x.                                   (1.5)
```

## 2. Exact rank one at every middle vertex

### Theorem 2.1 -- `E`-slice collapse

For each fixed `j`, every `2 x 2` minor of

```text
E^(j)=(E_kji)_(k>j,i<j)                              (2.1)
```

vanishes.  Since no entry is zero,

```text
rank_Q E^(j)=1                                      (2.2)
```

whenever the slice is nonempty.

#### Proof

From `(0.1)`,

```text
E_kji=-d_kj d_ji (mod Q).                            (2.3)
```

Thus for any two rows `k,l` and columns `i,h`,

```text
Q | E_kji E_ljh-E_kjh E_lji.                        (2.4)
```

By `(1.4)`, the absolute value of this determinant is `O(H^2)`.  But

```text
H^2=Y^(32/33)=o(Q).                                  (2.5)
```

For sufficiently large `Y`, the only multiple of `Q` in that range is zero.
Every quadratic minor therefore vanishes.  Proposition 1.1 makes each entry
nonzero, proving `(2.2)`.  QED

This proof uses both pieces of arithmetic.  Congruence alone gives only
rank one modulo `Q`; the strict inequality `H^2<Q` lifts it to characteristic
zero.

## 3. Integral factors and residue rotations

Choose a primitive integral rank-one factorization

```text
E_kji=g_j A^(j)_k B^(j)_i,                           (3.1)
```

with the row and column factor families primitive.  It can be normalized so
that

```text
v_2(g_j)=1,              A^(j)_k,B^(j)_i odd.        (3.2)
```

All factors in `(3.1)` are units modulo `Q`.  There is a unit
`lambda_j in (Z/QZ)^x` such that

```text
A^(j)_k=lambda_j d_kj                    (mod Q),
B^(j)_i=-(g_j lambda_j)^(-1)d_ji         (mod Q).    (3.3)
```

#### Proof

Integral rank-one factorization is standard after taking the content and
primitive row and column gcds.  Since every entry has 2-adic valuation one,
primitivity puts the sole factor two in `g_j`, proving `(3.2)`.  Equation
`(1.5)` makes every factor a unit modulo `Q`.

Compare `(3.1)` and `(2.3)` at a fixed anchor row and column.  Division by
units gives

```text
A^(j)_k/A^(j)_(k_0)=d_kj/d_(k_0,j)       (mod Q),
B^(j)_i/B^(j)_(i_0)=d_ji/d_(j,i_0)       (mod Q).
```

Absorbing the anchor ratio into `lambda_j` yields `(3.3)`.  QED

The rotations are injective on each incident prime family.  If two row
factors were congruent modulo `Q`, then `d_kj=d_lj (mod Q)`.  The fixed shell
has diameter less than `Q/2` at `w=1/5`, so
`d_kj-d_lj=2(p_kj-p_lj)` has absolute value less than `Q`; congruence would
force equality of the distinct primes.  The same holds for column factors.

Thus each middle vertex rotates all its incident prime residues into two
short exact factor families whose cross-products have magnitude `O(H)`.
This is stronger information than a single projective larger-sieve cut, but
the rotation `lambda_j` may change with `j`.

For reference, this information at one middle vertex gives only the crude
bound

```text
(# rows)(# columns)<<H.                              (3.4)
```

Indeed `(3.3)` makes the row factors distinct modulo `Q`, and hence distinct
as integers because each has magnitude `O(H)<Q`; likewise for the column
factors.  Their largest absolute values are therefore at least constant
multiples of the two cardinalities, while their cross-product in `(3.1)` is
`O(H)`.  This recovers `m<<H^(1/2)` at a central slice and no more.

## 4. The exact multiplicative associator

Put

```text
s_ab=2p_ab/Q=1+d_ab/Q,
e_kji=s_ki-s_kj s_ji=E_kji/Q^2.                     (4.1)
```

Associativity of multiplying three edge ratios gives:

### Proposition 4.1

For every `l>k>j>i`,

```text
Q E_lki+2p_lk E_kji
 =Q E_lji+2p_ji E_lkj.                              (4.2)
```

#### Proof

Expand `s_li` along the two bracketings:

```text
s_li=s_lk(s_kj s_ji+e_kji)+e_lki,
s_li=(s_lk s_kj+e_lkj)s_ji+e_lji.
```

Cancel the common triple product, substitute `(4.1)`, and multiply by `Q`.
QED

Modulo `Q`, `(4.2)` is consistent with the rotations `(3.3)`.  It supplies no
independent constraint, however.  For arbitrary edge labels the two sides
of its normalized form are identically

```text
e_lki+s_lk e_kji=e_lji+s_ji e_lkj
                     =s_li-s_lk s_kj s_ji.          (4.3)
```

The associator is therefore bookkeeping, not entropy.

### Theorem 4.2 -- global projective completion

Let `n>=4`, set `s_ii=1`, and suppose every fixed-middle defect matrix

```text
(s_ki-s_kj s_ji)_(k>j,i<j)
```

has rank at most one over a field.  If

```text
det [[s_(n-1,1),s_(n-1,2)],
     [s_(n,1),  s_(n,2)  ]] !=0,                    (4.4)
```

then there are row vectors `u_k` and column vectors `v_i` of dimension two
such that

```text
s_ki=u_k v_i,                 u_i v_i=1             (4.5)
```

for every `k>=i`.  Thus the ordered array has a global rank-two completion.

#### Proof

For each `j`, form the southwest cut

```text
B_j=(s_ki)_(k>=j,i<=j).
```

Subtract `s_kj` times row `j` from every row `k>j`.  The transformed matrix
has pivot row ending in `1` and lower block `[E^(j) | 0]`.  Consequently

```text
rank(B_j)=1+rank(E^(j))<=2.                          (4.6)
```

The anchor `(4.4)` makes columns one and two independent on every suffix
ending in rows `n-1,n`.  Take `v_1=(1,0)^T`, `v_2=(0,1)^T`, and put

```text
u_k=(s_k1,s_k2)                  (k>=2).
```

For `3<=i<n`, every column `i` in `(4.6)` is the unique linear combination
of columns one and two on rows `i,...,n`; put those two coefficients into
`v_i`.  The combination includes row `i`, so it also gives
`u_i v_i=s_ii=1`.  Take `u_1=(1,0)`, and choose the final `v_n` from the one
remaining equation `u_n v_n=1`.  This proves `(4.5)`.  QED

In the prime shadow, `(4.4)` cannot vanish: after clearing `Q`, vanishing
would equate two products of four globally distinct primes, contrary to
unique factorization.  Conversely, `(4.5)` gives exactly

```text
e_kji=det(u_k,u_j) det(v_i,v_j),                    (4.7)
```

so all defect slices have rank at most one.  Equations `(4.5)--(4.7)` are
therefore the correct projective normal form for the full prime system, not
merely a source of countermodels.

## 5. What this does not classify

The following shortcuts are invalid.

1. `E` has no forced sign.  Its reference is exactly zero, so the sign is a
   rounding/transport datum.
2. Rank-one `E` slices do not imply `E=0`; parity proves the opposite.
3. A small rank-one integer matrix need not have prime entries or disjoint
   factor support.  UFD therefore does not give the factorial argument used
   in tensor SR2PF.
4. The associator is a tautology for every edge system and cannot stabilize
   anything.
5. The global rank-two completion is not a size bound.  No proof yet reduces
   all projective coordinates to one constant ratio or unipotent tangent
   orbit.

There is a broad exact algebraic family inside the normal form.  Over any
field, choose two-vectors `u_i,v_i` with

```text
u_i^T v_i=1,
s_ki=u_k^T v_i.                                     (5.1)
```

Then the `2 x 2` determinant identity gives

```text
s_ki-s_kj s_ji
 =det(u_k,u_j)det(v_i,v_j),                          (5.2)
```

up to the fixed orientation convention.  Thus every defect slice has rank
one, while arbitrary sequences of projective vectors give nonautonomous
rotations; the associator holds identically.  The specializations
`s_ki=r_k/r_i` and `s_ki=1+c(x_k-x_i)` recover respectively the zero-defect
ratio model and a nonzero tangent model.

Arbitrary `G_i in GL_2` give such systems by taking

```text
u_i=e_1^T G_i,                 v_i=G_i^(-1)e_1.     (5.3)
```

These are formal algebraic families, not asymptotic distinct-prime PQR
counterexamples: they do not impose the nonzero parity, short height, prime
gcd law, or modular rotations proved above.  They show exactly why those
arithmetic inputs must enter the remaining theorem.

## 6. Exact remaining theorem

The PQR gate now has the following sharper arithmetic interface.

> **Rotating small-defect rigidity (`RSDR`).**  Let a complete ordered graph
> of distinct same-side shell primes satisfy the PQR approximation.  For
> its global projective completion `(4.5)`, use the determinant factors
> `(4.7)`, short nonzero integer height `|E|<<H`, parity, the residue
> rotations `(3.3)`, and the prime gcd law `(1.3)` to prove either
>
> 1. `m<<(log Y)^C`; or
> 2. a long constant-rotation or unipotent-transfer subsystem, together with
>    an adapter theorem placing it under PHR2 or tensor SR2PF.

This theorem is open.  The scalar count from distinct short factors gives
at best `m^2<<H`, hence `m<<Y^(8/33)`, which is far above
`m=Y^(.0179+o(1))`.  The missing gain must come from prime and short-height
rigidity of the global projective configuration, not from one slice or from
the tautological associator.

In particular, modular constancy alone is not the adapter in output 2: it
does not by itself give an exact rational recurrence or a full Cartesian
all-cut prime tensor.

```text
exact E formula and |E|<<Y^(16/33):                  PROVED
E=2 mod 4, nonzero, edge/Q gcd law:                   PROVED
every fixed-middle E slice has exact rank one:         PROVED
primitive factors and modular residue rotations:       PROVED
four-vertex multiplicative associator:                 PROVED
associator as an independent constraint:                FALSE
global rank-two projective completion:                  PROVED
uniform sign of E:                                    FALSE/UNAVAILABLE
rotation stabilization or entropy growth:             OPEN
RSDR, PQR, and PQR+G:                                 OPEN
uniform zero-free strip:                              NOT PROVED
RH:                                                   NOT PROVED
```
