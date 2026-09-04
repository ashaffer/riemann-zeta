# QP Bezout two-diamond tagged trace and projective-norm audit

**Date:** 2026-08-25  
**Verdict:** the Bezout two-diamond normal form is exact and useful, but it
does **not** turn the remaining zero-tag trace into a legal scalar
Blomer--Pascadi bilinear form.  It is a pair of unimodular relabelings, so it
preserves the partner tag, the incidence singular values, and the zero-tag
factorial mass exactly.  The second physical row remains a genuinely joint
centre--partner mask.

There is one positive local result.  In the principal adjacent chart the
second hard-window diamond restores a positive-definite ellipse and leaves
only `O(D)` determinant cells, rather than the determinant-only `D^2`
relaxation.  This is the correct local mechanism.  What is missing globally
is a vector/Carleson theorem that assembles the moving Bezout charts while
retaining their actual-prime row selectors.

A new exact method witness quantifies the scalarization loss.  On a literal
four-hard-window principal chart of effective side `p~sqrt(D)`, a Paley
difference row mask has zero-tag factorial mass of the sharp size `D*K`, but
its projective/nuclear norm is larger than its Hilbert--Schmidt norm by
`asymp sqrt(p)=D^(1/4)`.  Thus termwise reduction to scalar bilinear forms can
spend the entire missing power before any Kloosterman saving is used.

The Paley witness uses a selected **integer** row mask, not the actual
prime-power mask, and its points lie in a coherent affine chart.  It is
therefore a theorem-method obstruction, not a counterexample to the
post-peel four-cycle bound.

## 1. Lossless two-diamond coordinates

Fix the primitive anchor `gamma=(c,C)` and choose

```text
c*u-C*v=1.
```

The exact token maps are

```text
(b,B) <-> P=(delta,n),
delta=c*b-C*B,
(d,E) <-> R=(h,m),
h=C*d-c*E.
```

They are unimodular bijections of `Z^2`.  For the symmetric integral form

```text
K=(-2uv, cu+Cv; cu+Cv, -2cC),        det K=-1,
```

one has exactly

```text
det(P,R)=b*d-B*E,
P^T K R=b*d+B*E.                                    (1.1)
```

Consequently the two hard windows with row `x` are equivalent to one exact
diamond

```text
|4x P^T K R-q^3|+4x|det(P,R)|<=qD.                 (1.2)
```

The first edge from `P` to the fixed anchor is the same diamond with
`R=(0,1)` and row `a`.  No actual node has been copied, completed, or
projected in (1.1)--(1.2).

The Gram identity in these coordinates is

```text
(P^T K R)^2-(P^T K P)(R^T K R)=det(P,R)^2.         (1.3)
```

But (1.3) is exactly the physical factorization

```text
(bd+BE)^2-4bB dE=(bd-BE)^2.                        (1.4)
```

It creates no extra divisor equation.

## 2. Why the zero tag survives unchanged

For a fixed anchor let `M(P,R)` be the selected common-neighbour incidence
matrix and let

```text
d_R=sum_P M(P,R).
```

The tagged factorial quantity is

```text
F_2=sum_R d_R(d_R-1).                               (2.1)
```

Changing physical pairs to Bezout tokens only permutes the rows and columns
of `M`.  Therefore it preserves, exactly,

```text
all d_R,
F_2,
rank(M),
every singular value of M,
||M||_F and ||M||_* .                               (2.2)
```

In convolution language, (2.1) is still the `tag difference =0` slice.
The token map does not turn it into a full-vector convolution, and summing
over the tag still inserts the forbidden cross-partner pairs.

## 3. Exact scalar projective-norm witness

Let `p=3 (mod 4)` be prime and put

```text
W_(i,j)=1_(i-j is a nonzero quadratic residue mod p).
```

Every row and column has degree

```text
K=(p-1)/2.                                           (3.1)
```

Hence its zero-tag factorial mass is

```text
sum_j K(K-1)=p*K*(K-1) asymp p^3.                  (3.2)
```

The matrix is circulant.  The quadratic Gauss-sum evaluation gives the
singular values exactly:

```text
(p-1)/2                         once,
sqrt(p+1)/2                     p-1 times.          (3.3)
```

In particular it has full rank and

```text
||W||_F^2=p(p-1)/2,
||W||_*=(p-1)/2+(p-1)sqrt(p+1)/2,
||W||_*/||W||_F >sqrt((p^2-1)/(2p))
                 >sqrt((p-1)/2).                   (3.4)
```

The nuclear norm is the minimum of

```text
sum_j ||alpha_j||_2 ||beta_j||_2
```

over scalar rank-one decompositions
`W=sum_j alpha_j beta_j^*`.  Thus any argument which makes the joint mask
legal for a scalar bilinear theorem by triangle-summing rank-one pieces pays
at least `asymp sqrt(p)` relative to its Hilbert--Schmidt normalization on
this mask.

The witness embeds in the principal token chart with

```text
gamma=(M,M+1),
b_i=M-A_i,       B_i=M-A_i-1,
d_j=M+s_j,       E_j=M+s_j+1,
a_i=M+A_i,       x_ij=M+A_i-s_j.                  (3.5)
```

Choose `A_i=10p+i`, `s_j=30p+j` and retain precisely the rows for which
`i-j` is a nonzero square modulo `p`.  Every one of the four triples in
(3.5) has centered offset sum zero, so its product error is quadratic in
`p`.  The executable fixture chooses the literal critical parameters

```text
D=floor(q^(16/33))>=20000p^2,       D^2<q,
```

and verifies all four inequalities

```text
|8abc-q^3|<=qD.                                      (3.6)
```

All eight displayed coordinates occupy disjoint bands, and every physical
pair is primitive.  With `p~sqrt(D)` equations (3.1)--(3.4) become

```text
K~sqrt(D),
F_2~D*K,
projective/Hilbert cost ~D^(1/4).                   (3.7)
```

Thus this is sharp at the desired tagged-trace scale while being maximally
unfriendly to scalar rank-one decomposition.

## 4. Blomer--Pascadi does not absorb that loss

Blomer--Pascadi Theorem 1.1 applies to

```text
sum_(m,n) alpha_m beta_n S(am,n;c)                  (4.1)
```

for two scalar interval sequences and one complete fixed-modulus
Kloosterman kernel.  It does not accept a joint matrix coefficient
`W(m,n)`, a zero-tag mixed norm, or a moving family of kernels indexed by
the physical partner.

At the optimistic shell interface `c~q`, `N=D=q^(16/33)`, its weakest
relative saving is

```text
q^(-19/1056)=D^(-19/512).                           (4.2)
```

The favorable scalar local ledger has only

```text
D^(-3/512)                                           (4.3)
```

of headroom beyond its required saving.  The legal scalarization cost in
(3.7) can be `D^(1/4)`, overwhelmingly larger than (4.3).  Even in the
unrealistic global ledger with four independent, lossless applications,
the total saving is only

```text
D^(-19/128),
```

which already leaves `D^(13/128)` of the original `D^(1/4)` gap before any
joint-mask, Fourier-block, zero-tag, or moving-modulus loss is paid.

Relative to the project's newer `D^(9/8)` bound, the numerical ledger is
less negative but the applicability verdict is unchanged.  Four completely
independent gains would save `D^(19/128)`, exceeding the remaining
`D^(1/8)` by only

```text
D^(3/128).                                           (4.4)
```

Thus even this optimistic recombination can afford only `D^(3/128)` of
total conversion loss.  The exact Paley scalarization cost `D^(1/4)` is
still larger by `D^(29/128)`.  Moreover Blomer--Pascadi's own fourth moment
has already been spent proving one scalar operator estimate, so four
independent uses are not supplied by Theorem 1.1.

Fourier-expanding the difference selector in (3.5) does not repair this.
For the Paley selector all nonzero Fourier coefficients have the same
Gauss-size; absolute summation is another realization of the
`sqrt(p)=D^(1/4)` cost.  A Hilbert-valued tensorization is free only when all
coordinates see the same fixed scalar kernel and the output remains an
`ell^2` vector.  Here the zero-tag trace sums the diagonal coordinates back
to a scalar positive mass, while the physical modulus/numerator and row
completion change with the outer tag.

## 5. Exact conclusion

```text
Bezout token maps are lossless and unimodular:          PROVED;
middle difference and sum are det(P,R), P^T K R:        PROVED;
two hard windows equal one exact diamond:               PROVED;
token Gram identity supplies a new divisor condition:   NO;
tokenization changes the zero-tag slice:                 NO;
principal hard chart has O(D) ellipse capacity:          PROVED LOCALLY;
Paley zero-tag mass is of target order D*K:              PROVED;
Paley scalar projective loss is D^(1/4):                 PROVED;
Paley fixture satisfies four literal hard windows:       PROVED;
Paley fixture is an actual-prime counterexample:         NO;
scalar Blomer--Pascadi yields the zero-tag mixed norm:    NO;
mask-sensitive vector/Carleson BP extension:             OPEN;
generic post-peel tagged-trace theorem:                  OPEN;
sharp four-cycle bound:                                  NOT PROVED.
```

The new exact artifacts are

```text
src/qp_tagged_trace_projective_barrier.py
src/test_qp_tagged_trace_projective_barrier.py
```

Focused verification:

```text
python3 -m pytest -q \
  src/test_qp_tagged_trace_projective_barrier.py \
  src/test_qp_four_completion_bezout_token.py
# 11 passed
```

Primary theorem audited: Blomer--Pascadi, *Bilinear forms with Kloosterman
sums via quadratic characters*, Theorem 1.1,
<https://arxiv.org/abs/2607.24311>.
