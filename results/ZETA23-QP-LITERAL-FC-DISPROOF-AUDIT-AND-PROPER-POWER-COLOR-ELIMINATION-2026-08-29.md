# QP literal four-cycle: disproof audit and proper-power color elimination

**Date:** 2026-08-29

## Verdict

No legal asymptotic counterexample to the literal positive hard-window
four-cycle estimate was found.  In particular, the known multilevel tangent
fixture is not such a counterexample: it violates a factorial completion-pair
form, whereas its direct positive source has size only `D^(3/4+o(1))`.

There is, however, one new exact reduction.  Up to logarithmic loss, a
counterexample may be assumed to have its coefficient vector supported on
ordinary primes.  Coefficients on proper prime powers satisfy the sharp
four-cycle bound automatically.  Proper prime powers may still occur in the
two unweighted carrier coordinates; the reduction does not remove them.

The surviving counterexample profile is therefore very narrow: it must be
all-distinct and block-odd, use ordinary-prime coefficient colors, have
recurrent completion matrices and high transverse defect fans, and spread
over polynomially many genuinely different secants/planes.  One isolated
affine or Hankel packet cannot violate the estimate.  No theorem presently
rules out the required approximate, multi-direction packet reuse on the
actual prime-power mask, so this audit does not prove the four-cycle bound.

## 1. Literal target

Let `q` tend through odd primes, let

```text
Y=q/2,
S_q={p^j: Y exp(-w)<p^j<Y exp(w)},
0<w<(log 2)/3,
D=q^(16/33+o(1)),
```

and put

```text
kappa(a,b,c)=1_(a,b,c in S_q) 1_(|8abc-q^3|<=qD),
A_z(a,b)=sum_c z_c kappa(a,b,c).
```

The literal positive endpoint is

```text
F_+(z)=tr((A_|z|^* A_|z|)^2)
      =sum_C m(C)|z_c11 z_c12 z_c21 z_c22|
      <<D q^o(1)||z||_2^4.                            (1.1)
```

Here `m(C)` is the number of physical completion occurrences of the oriented
color matrix `C`.  There is no factor `m(C)^2` in (1.1).

## 2. Fixed-exponent proper-power colors have no generic rectangle

For `j>=1`, let `S_q^(j)` be the nodes in `S_q` of the form `p^j`, with `p`
prime.  The representation is unique.  Suppose a nondegenerate physical
rectangle has all four colors in one fixed class `S_q^(j)`, `j>=2`:

```text
c_rs=p_rs^j.
```

Put

```text
k=c11*c22-c12*c21
 =(p11*p22)^j-(p12*p21)^j=X^j-Z^j.                  (2.1)
```

The exact residual determinant identity gives, uniformly on the fixed
shell,

```text
|k|<<D.                                               (2.2)
```

If `X=Z`, unique factorization gives

```text
{p11,p22}={p12,p21}.
```

One pairing makes the two colors in each row equal; the other makes the two
colors in each column equal.  Pair uniqueness then forces `b1=b2` or
`a1=a2`, contrary to nondegeneracy.  Thus the zero case is impossible.  If
`X!=Z`, then

```text
|X^j-Z^j|
 =|X-Z| sum_(r=0)^(j-1) X^(j-1-r) Z^r
 >=j min(X,Z)^(j-1)
 >>_w q^(2-2/j)
 >=c_w q.                                             (2.3)
```

Since `D=q^(16/33+o(1))=o(q)`, (2.2) and (2.3) are incompatible for all
sufficiently large `q`.  Hence a fixed proper-power exponent class supports
no nondegenerate color rectangle at all.

For completeness, its trace bound is direct.  Put

```text
R_a=sum_b |A_(z^(j))(a,b)|^2.
```

Pair uniqueness gives `R_a<=||z^(j)||_2^2`, while the maximum color degree
`Delta<<Dq^o(1)` gives

```text
sum_a R_a<=Delta||z^(j)||_2^2.
```

Thus the repeated-row part is at most
`Delta||z^(j)||_2^4`; the repeated-column part has the same bound.  Since
there are no other nonzero trace terms,

```text
||A_(z^(j))||_S4^4<<D q^o(1)||z^(j)||_2^4,
j>=2.                                                 (2.4)
```

## 3. Removing all proper-power coefficient colors

Decompose

```text
z=sum_(j>=1) z^(j),
supp z^(j) subset S_q^(j).
```

Only `O(log q)` exponent classes occur.  By linearity and the Schatten
triangle inequality,

```text
||sum_(j>=2) A_(z^(j))||_S4
 <=sum_(j>=2)||A_(z^(j))||_S4
 <<D^(1/4)q^o(1) sum_(j>=2)||z^(j)||_2
 <<D^(1/4)q^o(1)||z||_2.                              (3.1)
```

The logarithmic Cauchy loss is absorbed by `q^o(1)`.  Thus

```text
||A_(z_proper)||_S4^4<<D q^o(1)||z||_2^4.             (3.2)
```

Consequently it is enough to prove (1.1) for `z` supported on ordinary
primes.  Equivalently, any fixed-power violation of (1.1) has a
fixed-power ordinary-prime coefficient component.  This statement does not
project the two matrix-index roles onto primes.

## 4. Why the existing hostile fixtures do not disprove (1.1)

### 4.1 Repeated Latin blocks

The abstract construction with `L` disjoint `L by L` blocks, the same `L`
Latin colors, and `D=L^2` has fourth trace `D^(3/2)`.  It obeys degree and
pair-uniqueness axioms but not the cubic product window.  An exact integer
multiplicative realization has ambient logarithm `Omega(L log L)`, so it
only gives `L=q^o(1)`; no polynomial-size actual-prime realization is known.

### 4.2 One affine/Hankel packet

For a tangent/Hankel patch of width `W<<sqrt(D)` and coefficient squared
mass `x`, convolution and Frobenius bounds give

```text
tr((H^*H)^2)<<W^2 x^2<<D x^2.                        (4.1)
```

This remains true after taking an arbitrary sparse prime submask.  A single
affine packet can saturate but cannot violate (1.1).

If row/column-disjoint packets `P_nu` each satisfy (4.1), and any coefficient
color belongs to at most `mu` packets, then, writing `x_nu` for its squared
mass in `P_nu`,

```text
sum_nu x_nu<=mu,
sum_nu x_nu^2<=mu,
sum_nu F(P_nu)<<D mu.                                 (4.2)
```

Thus a packet-built polynomial violation requires polynomial weighted color
reuse together with row/column orthogonality.  Exact factorized reuse is
divisor-type, and the exact prime-power translation grid is excluded by
unique factorization.  Approximate reuse across varying directions is not
excluded.

### 4.3 Multilevel tangent reuse

In the full-integer fixture with parameter `L`,

```text
D asymp L^2,
# color matrices asymp L^2,
m(C) asymp L,
w(C)=1/(16L^(3/2))
```

for the displayed spiked unit vector.  Its factorial off-diagonal lift is
`asymp L^(5/2)=D^(5/4)`, but the direct source in (1.1) is only

```text
sum_C m(C)w(C) asymp L^(3/2)=D^(3/4).                 (4.3)
```

It therefore gives no literal-FC excess.  This is exactly why completion
pair forms must carry reciprocal multiplicity when used to represent the
direct source.

## 5. Tightest necessary profile for a genuine counterexample

Combining the proved reductions in the project, a fixed-power violation of
(1.1) must satisfy all of the following after subpower losses.

1. All eight displayed rectangle nodes are distinct; repeated-node,
   permutation, square, and opposite-color-equality sectors are `O(Dq^o)`.
2. The coefficient vector is supported on ordinary primes, by Sections 2--3.
3. The mass is block-odd.  The Rademacher-even residual-label sector is
   `O(Dq^o)`.
4. It is not coefficient-diffuse beyond `M=D^2`; that range is already
   closed by the support-sensitive randomized bound.
5. At the critical support `M=D^(15/8)`, it contains transverse endpoint
   fibres with more than `D^(7/8)` distinct nonzero defects.  Endpoint gaps
   at most `D^(3/8)` are closed.
6. It has recurrent color matrices: polynomial excess forces positive mass
   on `m(C)>=3`, and if `F/W=lambda>=8`, then

   ```text
   sum_C (m(C))_4 w(C)>=lambda^3 F/256.               (5.1)
   ```

7. It cannot be carried by one dominant affine line or one rational
   completion plane per high-multiplicity color; those sectors have the
   sharp `D/K` tail.  Its completions must spread over polynomially many
   one-/two-point secants or moving planes.
8. If modeled as coherent blocks, it must realize polynomially many
   row/column-orthogonal blocks with polynomial reuse of the same weighted
   ordinary-prime colors.  One local translation collar and every known
   exact factorized family fail this requirement.

No known actual-prime-power family meets this profile.  Conversely, the
current rigidity theorems only eliminate exact or pointwise coherent prime
shadows; they do not bound sparse approximate multi-direction reuse.

## 6. Binary ledger

```text
literal source is m(C)w(C), not m(C)^2w(C):        EXACT;
multilevel factorial fixture disproves literal FC: NO;
fixed-exponent proper-power coefficient sector:    O(Dq^o), PROVED;
reduction to ordinary-prime coefficient support:   PROVED;
single affine/Hankel packet counterexample:         IMPOSSIBLE;
exact prime-power translation-grid counterexample: IMPOSSIBLE;
abstract repeated-block counterexample:             EXISTS, NONPHYSICAL;
approximate multi-direction actual-prime reuse:     NOT RULED OUT;
actual-prime-power q^delta FC counterexample:       NOT FOUND;
sharp literal four-cycle theorem:                   OPEN.
```
