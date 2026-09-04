# QP four-cycle: small-height primitive-slope rigidity

**Date:** 2026-08-15  
**Verdict:** a high-multiplicity parabolic chart has only divisor-many
primitive directions for each fixed color matrix.  This follows from an
exact determinant-divisor identity and a two-dimensional thin-strip
argument; no modular-hyperbola theorem is needed.  At the QP scale,

```text
chart multiplicity m >= D^(1/4)
  ==> primitive direction height <= O(sqrt(D))
  ==> O(tau(|det C|))=q^o(1) primitive slope pairs.       (0.1)
```

This is a fixed-color classification.  It does not reduce the number of
different slope relations used by different colors and therefore does not,
by itself, improve the proved exceptional-sector `D^(11/8+o(1))` mass.

## 1. Exact divisor identity

Let

```text
C=(c11,c12;c21,c22),       k=det C!=0,              (1.1)
```

and let `r=(r1,r2)`, `s=(s1,s2)` be primitive integral vectors satisfying
the parabolic common-level relation

```text
c11 r1s1-c12 r1s2-c21 r2s1+c22 r2s2=0.             (1.2)
```

Put

```text
T=(c21,-c22;c11,-c12),       det T=k.               (1.3)
```

Equation (1.2) and the primitivity of `r` give a nonzero integer `eta` with

```text
T s=eta r.                                          (1.4)
```

Applying the adjugate of `T` gives

```text
k s=eta adj(T)r.                                    (1.5)
```

Since `s` is primitive, `eta` divides `k`.  This is the primitive version
of the normalized-gap identity `h*l=-det(C)g_r g_s`.

## 2. The thin-strip lemma

Fix one signed divisor `eta` of `k` and suppose

```text
||r||_infinity, ||s||_infinity <=B.                 (2.1)
```

Every possible `s` belongs to the symmetric convex body

```text
R_eta={x: ||x||_infinity<=B, ||T x||_infinity<=|eta|B}. (2.2)
```

Choose the longer row of `T`; its Euclidean norm is `N`.  Intersecting the
side-`2B` square with the corresponding strip gives

```text
area(R_eta)<=4 sqrt(2)|eta|B^2/N.                   (2.3)
```

If

```text
8 eta^2 B^4<N^2,                                   (2.4)
```

then this area is below two.  A symmetric convex body containing two
linearly independent integral vectors contains their centrally symmetric
diamond, whose area is at least two.  Hence all integral vectors in
`R_eta` are collinear.  It contains at most two primitive vectors, `s0`
and `-s0`, and (1.4) then determines `r`.

There are at most `2 tau(|k|)` signed choices for `eta`.  Thus (2.4) for
all of them gives at most `4 tau(|k|)` oriented primitive slope pairs (and
no more rank-one matrix directions after quotienting simultaneous sign).

In the project shell `N>>q`, `|k|<<D`.  If `B<<sqrt(D)`, the left-to-right
ratio in (2.4) is

```text
O(D^4/q^2)=O((D^2/q)^2)=q^(-2/33+o(1)),             (2.5)
```

so the certificate holds for all sufficiently large `q`.

## 3. Bridge from chart length

On an integral parabolic chart,

```text
M(n)=M0+nM1+n^2M2.                                  (3.1)
```

Integer-valuedness gives `2M2=g e`, where `g` is a nonzero integer and `e`
is a primitive rank-one integral matrix.  If `h=||e||_infinity`, one entry
has quadratic coefficient at least `h/2`.  Since that entry remains in a
product interval of length `O(D)`, a chart containing `m` integral
parameters obeys

```text
h<<D/m^2.                                           (3.2)
```

Factor `e=r s^T` with both factors primitive.  Each component of `r` and
`s` is at most `h` in magnitude.  Thus `m>=D^(1/4)` gives
`B<<sqrt(D)`, and Sections 1--2 prove (0.1).  Fixed denominators and sparse
parameter congruences cause no loss: after reparametrizing the progression,
they only multiply the quadratic coefficient.

## 4. Why Cilleruelo--Garaev does not directly give a global gain

Reducing (1.2) modulo `c11` and assuming the required inverses exist gives

```text
(c22 r2-c12 r1)(c22 s2-c21 s1)
  =c12 c21 r1s1                         (mod c11).  (4.1)
```

For fixed `r1,s1`, this is a shifted modular hyperbola in the two short
variables `r2,s2`.  When `c11` is prime and the right side is nonzero,
Cilleruelo--Garaev indeed gives `P^o(1)` points in a side-`P` box for
`P<c11^(1/4)`.

That theorem does not apply to the desired union as stated:

* `c11` is a varying prime power, not necessarily a prime modulus;
* without fixing `r1,s1`, the projective slope variables are ratios of
  short integers rather than elements of ordinary intervals;
* summing the fixed-`r1,s1` estimate naively restores a `P^2` loss.

The exact strip proof avoids all three issues and establishes the legitimate
fixed-color conclusion.  What it does not establish is a global
fixed-direction operator merger or a bound for the generic rank-three
completion branch.

```text
determinant-divisor identity eta|det(C):             PROVED;
two-independent-slope exclusion for B<<sqrt(D):      PROVED;
fixed-color primitive slope count q^o(1):            PROVED;
global direction count improvement:                  NOT PROVED;
generic rank-three branch:                            NOT COVERED;
full four-cycle bound:                                OPEN.
```

The exact identities and the integer area certificate are replayed in
`src/qp_four_cycle_small_slope_rigidity.py` and its tests.
