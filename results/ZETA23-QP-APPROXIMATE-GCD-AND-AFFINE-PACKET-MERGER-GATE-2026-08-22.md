# QP common carriers: approximate GCD and the affine-packet merger gate

**Date:** 2026-08-22  
**Verdict:** the common-carrier problem is exactly a two-input **general
approximate common divisor** problem, but the rigorous Howgrave--Graham
radius is much smaller than the project width.  The tempting
`D < sqrt(q)` threshold belongs to the partial problem with one known exact
multiple and therefore does not apply here.

There is a useful new inverse statement.  At the project scale, all short
color chords, and hence all `sqrt(D)`-scale affine/Hankel packets, have one
common primitive direction.  The proof is the elementary but decisive
inequality

```text
D^(3/2)=q^(8/11)=o(q).
```

Thus several genuinely different coherent tangent directions cannot coexist
for one fixed coprime row pair.  This still does not prove the desired
common-neighbor bound: a set of isolated modular lifts, with no two points in
one short chord, evades the merger theorem.  Controlling that sparse remainder
is a sub-square-root reciprocal-distribution problem.

No four-cycle estimate is claimed here.

---

## 1. Exact interval and GCD formulation

Fix shell constants `0<alpha<beta` with

```text
beta/alpha<2,                 beta-alpha<alpha,
```

as in the project shell, and let the retained hard core be

```text
|8*a*b*c-q^3| <= E,           E=C*q*D,              (1.1)
alpha*q <= a,b,c <= beta*q.
```

For a fixed row `a`, put

```text
X_a=q^3/(8*a),
I_a=[(q^3-E)/(8*a),(q^3+E)/(8*a)].                  (1.2)
```

Then

```text
length(I_a)=E/(4*a) <= C*D/(4*alpha)=O(D).          (1.3)
```

Suppose distinct actual prime-power rows `a,a'` have a common carrier `b`,
with colors `c,d`.  Set

```text
n=b*c in I_a,                 m=b*d in I_a'.        (1.4)
```

The shell contains at most one power of each prime base.  Hence distinct
shell nodes are coprime.  Also `c!=d`: otherwise subtraction of the two
residuals would give

```text
8*b*|a'-a|*c <= 2E,
```

whose left side is `>>q^2` and right side is `O(qD)=o(q^2)`.  Therefore

```text
gcd(c,d)=1,                   gcd(n,m)=b.            (1.5)
```

Since `length(I_a)=O(D)<b`, a fixed `b` supports at most one `n`, and
similarly at most one `m`.  If

```text
A=floor(X_a),                 A'=floor(X_a'),
```

then every common carrier gives unique errors `x,y`, with

```text
|x|+|y|=O(D),
b | A+x,                      b | A'+y,              (1.6)
b asyp q,                     A,A' asyp q^2.
```

This is precisely a two-input general approximate-common-divisor instance.

There is also an exact residual coordinate.  Put

```text
h=a'*d-a*c.
```

If `r=8abc-q^3` and `r'=8a'bd-q^3`, then

```text
r'-r=8*b*h,                  |h|=O(D).               (1.7)
```

For a fixed `h`, the color pair is unique.  Indeed, two pairs with the same
`h` obey

```text
a'*(d-d_1)=a*(c-c_1).
```

Since `gcd(a,a')=1`, the integer `a'` divides `c-c_1`; but the shell diameter
is smaller than `a'`.  Thus `c=c_1` and `d=d_1`.  In particular the elementary
bound is only

```text
number of common carriers = O(D).                   (1.8)
```

The project width has the slightly stronger property

```text
2*(beta-alpha)<alpha.                               (1.9)
```

Indeed, for `alpha=e^(-.2)/2` and `beta=e^(.2)/2`, (1.9) is equivalent
to `2*(e^.4-1)<1`.

---

## 2. Why the Coppersmith square-root slogan does not close the problem

Let `N` denote the size of the two known inputs in (1.6), so `N asyp q^2`,
and let the unknown common divisor have size

```text
b asyp q=N^(1/2).                                   (2.1)
```

For the **partial** approximate-GCD problem, one is given a known exact
multiple of `b`.  Howgrave--Graham's one-error theorem reaches

```text
N^(beta^2),       beta=1/2,
```

which is `N^(1/4)=sqrt(q)`.  Since

```text
D=q^(16/33)<q^(1/2),
```

this looks perfect.  But neither `A` nor `A'` in (1.6) is divisible by `b`;
only the candidate-dependent perturbations `A+x` and `A'+y` are.  There is no
known exact multiple to which the partial theorem can be applied.

The applicable result is the two-input **general** approximate-GCD theorem.
For two inputs, Howgrave--Graham's sharper exponent is

```text
f(beta)=1-beta/2-sqrt(1-beta-beta^2/2).              (2.2)
```

At `beta=1/2`,

```text
f(1/2)=3/4-sqrt(3/8)=0.137627... .                  (2.3)
```

Thus its rigorous radius, expressed in `q`, is only

```text
N^f=q^(2f)=q^(3/2-sqrt(3/2))=q^0.275255... .        (2.4)
```

The project width is

```text
D=q^(16/33)=q^0.484848... .                         (2.5)
```

Consequently the known rigorous general-ACD theorem misses by a large power.
The asymptotic multivariate bound in Cohn--Heninger is weaker still in the
two-input case.  Their discussion also makes explicit that multivariate
extensions generally need an algebraic-independence hypothesis; see
[Cohn--Heninger, *Approximate common divisors via lattices*](https://arxiv.org/abs/1108.2714).

One may fix `n` in (1.4) and then use it as an exact multiple, but summing over
the `O(D)` possible integers `n` loses the whole desired saving.  A successful
lattice proof would therefore need a genuinely batched/list-size theorem,
not the standard one-root partial-ACD theorem.

---

## 3. Exact modular-lift form of the unresolved remainder

Equation (1.7) gives

```text
a*c == -h (mod a').                                 (3.1)
```

Let `abar` be the inverse of `a` modulo `a'`.  Then

```text
c == -abar*h (mod a').                              (3.2)
```

Because the color shell has length smaller than `a'`, each `h` has at most
one lift `c(h)` into the shell.  Once this lift exists,

```text
d(h)=(a*c(h)+h)/a'                                  (3.3)
```

is forced, and the interval `I_a`, whose length is smaller than `c(h)`,
forces at most one carrier `b(h)`.

Hence the desired estimate is exactly a statement that among `O(D)`
consecutive values of `h`, at most `sqrt(D) q^o(1)` of the modular lifts
`c(h)` also pass the reciprocal/product window

```text
b(h)*c(h) in I_a                                    (3.4)
```

and the prime-power masks.  This is the actual anti-aliasing problem.  A
completion estimate at modulus `a' asyp q` naturally pays a square-root
`q^(1/2)`, while the `h` interval has length only

```text
D=q^(1/2-1/66).                                     (3.5)
```

The gap is exactly the previously observed `1/66` sub-square-root gap.

---

## 4. A proved primitive-direction merger

The following elementary lemma is useful independently of any analytic
estimate.

> **Short-direction uniqueness lemma.**  Let `a,a'` be coprime positive
> integers.  Suppose two primitive positive pairs `(v,w)` and `(v',w')`
> satisfy
>
> ```text
> max(v,w,v',w') <= L,
> |a'*w-a*v| <= H,              |a'*w'-a*v'| <= H.
> ```
>
> If `2*L*H<a'`, then `(v,w)=(v',w')`.

Indeed, if `e=a'w-av` and `e'=a'w'-av'`, then

```text
a'*(v*w'-v'*w)=v*e'-v'*e.                           (4.1)
```

The right side has modulus below `a'`, so the integer determinant vanishes.
The two positive primitive pairs are therefore equal.

Apply this to common-neighbor colors.  For two neighbors `i,j`, put

```text
Delta c=c_i-c_j,                Delta d=d_i-d_j.
```

Then

```text
a'*Delta d-a*Delta c=h_i-h_j=O(D).                  (4.2)
```

After dividing `(Delta c,Delta d)` by its gcd, every color chord of
coordinate size `O(sqrt(D))` gives a primitive pair with

```text
L=O(sqrt(D)),                   H=O(D).              (4.3)
```

At the project scale,

```text
L*H=O(D^(3/2))=O(q^(24/33))=O(q^(8/11))=o(q).       (4.4)
```

Since `a' asyp q`, (4.1) proves:

> **Fixed-row packet merger.**  For one fixed coprime row pair, all
> `sqrt(D)`-scale color chords are parallel to one primitive rational
> direction.  Every connected component of the graph formed by these short
> chords lies on an affine line, and all nontrivial components have the same
> direction.

This is stronger than merely extracting one dense packet: distinct coherent
tangent directions cannot coexist.

There is a complementary inverse statement which does not assume that the
chord is short.  Let the common neighbors be indexed by `i`, with residual
coordinates `h_i` and colors `(c_i,d_i)`.  If

```text
h_i-h_j=h_k-h_l,                                    (4.5)
```

then

```text
a'*[(d_i-d_j)-(d_k-d_l)]
 =a*[(c_i-c_j)-(c_k-c_l)].                          (4.6)
```

Coprimality makes `a'` divide the second bracket.  Its modulus is at most
twice the shell diameter, which is smaller than `a'` by (1.9).  Therefore

```text
c_i-c_j=c_k-c_l,              d_i-d_j=d_k-d_l.      (4.7)
```

Thus the map

```text
h_i -> (c_i,d_i)                                    (4.8)
```

is a Freiman 2-isomorphism on the common-neighbor set: equal residual
differences are exactly equal color chords.

If there are `M` common neighbors, their nonzero ordered residual differences
occupy only `O(D)` integer values.  Hence one nonzero difference occurs at
least

```text
>>M*(M-1)/D                                         (4.9)
```

times.  By (4.7), all these pairs use one identical color translation
`(Delta c,Delta d)`.  For a fixed residual difference, the pairs form
disjoint arithmetic chains, and (4.7) sends every chain to an affine color
chain with that same direction.

Consequently

```text
M >= sqrt(D)*q^epsilon
```

forces a fixed-direction affine/Hankel translation family of size
`>>q^(2*epsilon)`.  This is a rigorous power-excess inverse theorem.  It does
not say that the family is one long chain: it may consist of many isolated
one-edge chains.  Merging those parallel sparse chains is exactly the
remaining global packet problem.

---

## 5. One affine packet has the sharp square-root cap

Suppose a literal affine packet has consecutive parameter values

```text
b_t=b_0+u*t,       c_t=c_0-v*t,       d_t=d_0-w*t,
t=0,...,T-1,       u,v,w positive.                    (5.1)
```

Then

```text
b_t*c_t=b_0*c_0+(u*c_0-v*b_0)*t-u*v*t^2.            (5.2)
```

The range of a quadratic sequence with second difference `-2uv` on `T`
consecutive integers is `>>uv*(T-1)^2`.  If all products in (5.2) lie in one
interval of length `O(D)`, then

```text
u*v*(T-1)^2 << D.                                   (5.3)
```

In particular

```text
T << sqrt(D)+1.                                     (5.4)
```

The second product gives the analogous estimate with `uw`.  Thus the square
root is the exact curvature scale of a merged affine/Hankel packet.

It is sharp already in the integer model.  For `T asyp sqrt(D)`, the points

```text
b_t=L+t,             c_t=L-t,             d_t=L-1-t
```

obey

```text
b_t*c_t=L^2-t^2,
b_t*d_t=L*(L-1)-t-t^2,
gcd(c_t,d_t)=1.                                      (5.5)
```

Both product families lie in intervals of length `O(D)`.  Moreover their
centers have the exact linked ratio corresponding to the coprime rows
`a=L-1,a'=L`.  Prime-power masks may thin this packet by logarithms, but not
by a power on the basis of geometry alone.

---

## 6. What remains

The merger lemma closes every already-detected coherent packet and shows
that all such packets use one primitive direction.  It does **not** imply
that every large common-neighbor set contains enough short chords.  A set of
one or two points on each of many separated modular lifts can avoid all
affine components while still having cardinality larger than `sqrt(D)`.

The exact remaining theorem is therefore one of the following equivalent
forms.

```text
(i)  a list-size theorem for the special linked two-input general-ACD
     instance (1.6) at error q^(16/33);

(ii) a sub-square-root distribution theorem for the lifted reciprocal
     sequence (3.2)--(3.4);

(iii) an inverse theorem showing that >sqrt(D) q^o admissible lifts force
      enough short chords to enter the unique affine/Hankel direction.
```

Current status:

```text
exact short-interval/GCD reduction:                 PROVED;
fixed residual h injective:                         PROVED;
standard partial-ACD sqrt(q) theorem applicable:    NO (no exact multiple);
general two-input ACD theorem reaches project D:    NO;
all short packet directions merge:                  PROVED;
one affine packet has O(sqrt(D)) points:             PROVED;
sparse modular-lift remainder:                       OPEN;
uniform common-neighbor sqrt(D) q^o bound:           NOT PROVED.
```
