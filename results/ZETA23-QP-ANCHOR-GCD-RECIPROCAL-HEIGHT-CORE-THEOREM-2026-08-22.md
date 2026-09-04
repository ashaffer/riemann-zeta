# QP high-completion tail: anchor-GCD reciprocal-height core theorem

**Date:** 2026-08-22  
**Verdict:** every *single* high partner with `m~K` has the sharp
`K^(2+o(1))` reciprocal-height mass, without any tangent, affine-line, or
parabolic hypothesis.  More generally, if all high partners of one anchor
use only `M` distinct shared rows, their entire restricted reciprocal-height
support has mass

```text
R_(gamma,K)<<M^2*q^o(1).                           (0.1)
```

Consequently the sharp high tail is proved whenever `M<=K*q^o(1)`, and a
strict improvement on the present `D^(5/4)` trace follows throughout

```text
M<=K*D^(1/8-epsilon).                              (0.2)
```

There is a second independent closed range.  For a fixed anchor, the color
determinant `k` determines the partner uniquely.  The whole low-determinant
range

```text
0<|k|<=D/K                                         (0.3)
```

satisfies the desired `D/K` high-completion tail by the second factorial
identity alone.

The exact defect identity

```text
e cross f=-k*h                                    (0.4)
```

shows that these statements preserve the actual mask and the primitive
height exactly.  It also shows the remaining obstruction precisely: many
high partners with `|k|>D/K` whose shared-row union is polynomially larger
than `K`.  No uniform four-cycle bound is claimed.

---

## 1. Exact anchor and defect coordinates

Fix an actual ordered color pair

```text
gamma=(c,d),              gcd(c,d)=1.              (1.1)
```

A neighboring row vertex is an ordered actual pair `x=(a,A)`.  If `b` is
the unique common carrier, subtraction of its two product residuals gives

```text
e_gamma(x)=a*c-A*d,              |e_gamma(x)|<<D. (1.2)
```

The map `x->e_gamma(x)` is injective.  Indeed, equal defects for `x,x'`
give

```text
c*(a-a')=d*(A-A').                               (1.3)
```

Coprimality makes `(a-a',A-A')` an integral multiple of `(d,c)`.  A
nonzero multiple cannot fit inside the project shell, whose diameter is
smaller than either coordinate.  Hence `x=x'`.

Let a second actual color pair be

```text
gamma'=(c',d'),       k=c*d'-c'*d !=0,             (1.4)
```

and put `f(x)=a*c'-A*d'`.  For three shared rows

```text
X=(x_1,x_2,x_3),
a=(a_1,a_2,a_3),       A=(A_1,A_2,A_3),
e=(e(x_1),e(x_2),e(x_3)),
f=(f(x_1),f(x_2),f(x_3)),                          (1.5)
```

bilinearity gives the exact identity

```text
e cross f
 =(c*a-d*A) cross (c'*a-d'*A)
 =-(c*d'-c'*d)*(a cross A)
 =-k*h.                                            (1.6)
```

If `h=t*h_0`, with `h_0` primitive and
`H(X)=||h_0||_infinity`, then

```text
content(e cross f)=|k|*t,
primitive(e cross f)=+-h_0.                        (1.7)
```

Thus neither the determinant `k` nor the raw content changes the primitive
height.  Any gain from a large `k` or large content must come from counting
how often that label occurs; it cannot come from replacing `H(X)` by the
raw cross-product size.

There is also partner uniqueness at fixed `k`.  Two solutions of

```text
c*d'-d*c'=k                                       (1.8)
```

differ by an integral multiple of `(c,d)`, too large to remain in the
shell.  Hence a fixed anchor has at most one actual partner for every
nonzero integer `k`.

---

## 2. A normalized-GCD reciprocal-height theorem

Let `Y` be any set of `N` primitive ordered shell pairs in one slope block,
so every nonzero pair determinant has modulus `O(D)`.  For a triple
`X={x,y,z}` put

```text
g_X=gcd(|det(x,y)|,|det(y,z)|,|det(z,x)|),
H(X)=max(|det(x,y)|,|det(y,z)|,|det(z,x)|)/g_X.    (2.1)
```

Then

```text
sum_({x,y,z} subset Y) 1/H(X)
 <<N^2*D^o(1).                                     (2.2)
```

Here is a self-contained proof.  Anchor `x` and write

```text
d_y=|det(x,y)|,        d_z=|det(x,z)|.              (2.3)
```

The values `d_y` are distinct on each fixed sign branch.  Equality with
sign would make `y-z` or `y+z` an integral multiple of primitive `x`; shell
positivity excludes the second case and shell diameter excludes a nonzero
multiple in the first.  Splitting signs costs only a constant.

For the anchored triple,

```text
1/H(x,y,z)
 <=gcd(d_y,d_z)/max(d_y,d_z)
 <=gcd(d_y,d_z)/sqrt(d_y*d_z).                    (2.4)
```

The normalized GCD matrix on integers at most `O(D)` has operator norm
`D^o(1)`.  One elementary bound suffices.  Since

```text
gcd(m,n)=sum_(ell|m, ell|n) phi(ell),              (2.5)
```

Cauchy--Schwarz gives, for arbitrary coefficients `v_n`,

```text
sum_(m,n) gcd(m,n)/sqrt(m*n) v_m conjugate(v_n)
 <=log(2D)*max_(n<=O(D)) sum_(ell|n) phi(ell)/ell
       *sum_n |v_n|^2
 <<D^o(1)*sum_n |v_n|^2.                           (2.6)
```

Applying (2.6) to the indicator of the distinct determinant set in (2.3)
shows that all triples containing one fixed `x` contribute
`O(ND^o(1))`.  Sum over `x`; every unordered triple is counted three times.
This proves (2.2).

This theorem includes the consecutive tangent fixture, but is much more
general: the correct `N^2` reciprocal-height scale holds for every subset
of primitive shell rows, not only for an affine packet.

---

## 3. The shared-row core theorem

Return to a fixed anchor `gamma`.  For every high partner put

```text
S_(gamma')=N(gamma) intersect N(gamma'),
K<=|S_(gamma')|<2K,                                (3.1)
```

and let

```text
U_(gamma,K)=union_(gamma') S_(gamma'),
M=|U_(gamma,K)|.                                   (3.2)
```

After the already certified packet deletion, the restricted triple support
`X_(gamma,K)` is a subset of the triples from `U_(gamma,K)`.  Equation
(2.2) therefore proves

```text
R_(gamma,K)
 =sum_(X in X_(gamma,K))1/H(X)
 <<M^2*q^o(1).                                     (3.3)
```

Insert this into the proved singleton-safe factorial reduction

```text
W_K(z)<<D*R_K/K^3*q^o(1)||z||_2^4.                (3.4)
```

If `M=K*R`, then

```text
W_(K,core)(z)
 <<(D/K)*R^2*q^o(1)||z||_2^4.                     (3.5)
```

Hence `R=q^o(1)` proves the sharp high tail.  At the critical
`K=D^(5/16)`, multiplying (3.5) by `m(C)~K` gives completed trace exponent

```text
1+2*log_D R.                                       (3.6)
```

The present uniform exponent is `5/4`, so every core range

```text
R<=D^(1/8-epsilon)                                 (3.7)
```

gives a strict power improvement.  This is (0.2).

For one fixed high partner, `M<2K`; thus (3.3) proves

```text
sum_(X subset N(gamma) intersect N(gamma'))1/H(X)
 <<K^2*q^o(1)                                      (3.8)
```

uniformly.  The missing power never occurs inside one partner fibre.  It is
entirely a cross-partner union problem.

---

## 4. The low-color-determinant tail is closed

Restrict the high partners of `gamma` to

```text
0<|k(gamma,gamma')|<=L.                            (4.1)
```

Partner uniqueness from (1.8) leaves `O(L)` partners.  Since every one has
`m<2K`, the anchored second factorial row sum is

```text
F_(2,K,L)(gamma)
 =sum_(gamma') binom(m(gamma,gamma'),2)
 <<L*K^2.                                          (4.2)
```

For

```text
L<=D/K,                                            (4.3)
```

this is `O(DK)`, exactly the sufficient singleton-safe estimate `(AF_2)`.
Consequently

```text
W_(K, |k|<=D/K)(z)
 <<D/K*q^o(1)||z||_2^4.                            (4.4)
```

At the critical multiplicity `K=D^(5/16)`, every color determinant through

```text
|k|<=D^(11/16)                                     (4.5)
```

is therefore finished.  The anisotropic endpoint with `|k|~D` remains.

---

## 5. Fixed primitive normals at large height

The defect coordinate also gives a local normal theorem.  Fix one primitive
`h_0 in Z^3`, `||h_0||_infinity=H<=D`.  Every anchor triple with this normal
satisfies

```text
h_0 dot (e_1,e_2,e_3)=0.                           (5.1)
```

The injectivity of (1.2) embeds these triples into the integer points of
the plane (5.1) in a box of side `O(D)`.  A primitive plane of height `H`
has

```text
O(D^2/H+D)                                         (5.2)
```

such points.  This follows directly by solving modulo a largest coordinate
of `h_0`; the associated two-dimensional congruence lattice has index `H`.
Thus one fixed-normal block has reciprocal-height mass

```text
<<D^2/H^2+D/H.                                     (5.3)
```

In particular, for

```text
H>=D/K,                                            (5.4)
```

one fixed normal costs only `O(K^2+K)`, at the desired scale.  The same is
true for `q^o(1)` occupied normal labels.  What remains is a polynomial
family of varying normals or the low-height range `H<D/K`; summing (5.3)
naively over all primitive normals is not legitimate.

---

## 6. Exact unimodular quotient form of the residual

The defect coordinates admit a useful two-dimensional normal form.  Put

```text
g=(d,c)
```

and choose one Bezout complement `s=(u,v)` with

```text
det(g,s)=d*v-c*u=1.                                (6.1)
```

Every anchor row and every partner color pair have unique expansions

```text
x=(a,A)=m*g-e*s,
g'=(d',c')=n*g-k*s,                                (6.2)
```

where

```text
e=det(x,g)=a*c-A*d,
k=c*d'-c'*d.                                      (6.3)
```

Their second defect is exactly

```text
f=det(x,g')=e*n-m*k.                               (6.4)
```

For fixed `e`, the shell contains at most one `m`, because varying `m` by
one translates `x` by the shell-sized primitive vector `g`.  For fixed
`k`, the shell similarly contains at most one `n`; this is partner
uniqueness again.  Thus the residual incidence is a restriction of

```text
|e*n(k)-m(e)*k|<<D                                (6.5)
```

between two one-dimensional integer graphs.  The original prime-power
conditions on `x,g'` and on the unique reciprocal carrier are retained
pointwise.  No rectangular completion has occurred.

Formula (6.5) explains both the progress and the remaining difficulty.  A
single partner is one vertical fibre and is handled by Section 2; small
`k` has too few fibres and is handled by Section 4.  The unresolved family
is a large-`k` determinant graph between the two actual rounding masks.
A positive completion of either graph to a box permits the known regular
incidence countermodels, so the next input must be a mask-sensitive large
sieve for (6.5), not an unweighted determinant count.

---

## 7. Hostile summation audit

The new estimates do not by themselves prove the uniform tail.

* Summing (3.8) over `P` partners loses `P`.  The reciprocal-height support
  is a union, so overlap can help, but arbitrary addition of the individual
  bounds is too expensive.
* If `P<=D/K`, the second factorial estimate already closes, regardless of
  height.  Hence a residual anchor must have more than `D/K` high partners.
* If their shared-row union has `M<=Kq^o(1)`, Section 3 closes.  Hence a
  residual anchor must also spread over polynomially more than `K` rows.
* Section 4 removes every partner with `|k|<=D/K`.  The residual determinants
  are all large.
* Large raw content in (1.7) is not automatically favorable: it cancels
  when the primitive height is formed.  A content split needs an additional
  multiplicity theorem before it yields a saving.
* Section 5 closes `q^o(1)` large-height normal labels, not a polynomial
  collection.  A positive union bound over labels recreates the original
  square-function loss.

Thus any remaining counterconfiguration must simultaneously have

```text
more than D/K high partners per anchor;
all partner determinants |k|>D/K;
a shared-row union M>K*q^Omega(1);
polynomially many primitive normal labels;
no dominant affine/Hankel packet.                  (6.1)
```

This is a substantially narrower scattered family, but its exclusion is
still open.

```text
defect cross identity e cross f=-k h:              PROVED;
single-partner reciprocal-height K^2:              PROVED;
M-row union reciprocal-height M^2:                 PROVED;
common-core sharp tail M<=K q^o:                   PROVED;
common-core strict five-fourths improvement:       PROVED;
low determinant |k|<=D/K high tail:                PROVED;
fixed-normal H>=D/K block:                         PROVED;
large-content union saving:                        NOT PROVED;
high-k, large-union, varying-normal tail:           OPEN;
uniform four-cycle bound:                          OPEN.
```

Exact finite replay and exponent checks are in
`src/qp_anchor_gcd_reciprocal_height.py` and its test module.
