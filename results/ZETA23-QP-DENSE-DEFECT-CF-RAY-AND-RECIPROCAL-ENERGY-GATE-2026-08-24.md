# QP dense defects: the unique continued-fraction ray and the reciprocal-energy gate

**Date:** 2026-08-24  
**Binary verdict:** a canonical low-height packet ray is proved, but a dense
fan is not forced to occupy it.  After that ray is peeled, the exact remaining
statement is a packet-free additive-energy bound of size `D^(5/2+o(1))`.
That energy theorem would imply the desired `D^(7/8+o(1))` fan bound, but it
is not proved here.

This audit works in the residual pointwise sector

```text
D=q^(16/33+o(1)),       x,y,a,b,v asymp q,
w_x,w_y>D^(73/64),      x<y,      gcd(x,y)=1.          (0.1)
```

The conclusions below use only the actual shell-width hypothesis

```text
2 diam(S)<min(S),                                      (0.2)
```

the exact defect equation, and the two product bands.  They therefore retain
the physical carrier and do not complete the selected mask to a box.

---

## 1. Exact dense-defect model

Let `K` be a set of `H` distinct defects in an interval of length `O(D)`.
For each `k in K`, suppose there is one actual wedge

```text
P_k=(k,a_k,b_k,v_k)
```

with

```text
x*a_k-y*b_k=k,                                        (1.1)
|a_k*v_k-C_x|<<D,          C_x=T/x,
|b_k*v_k-C_y|<<D,          C_y=T/y.                   (1.2)
```

The product bands in `(1.2)` are just the reciprocal windows written in
integral coordinates: `|C_x/a_k-v_k|<<D/q`, and similarly for `b_k`.
Fixed-defect completion and carrier uniqueness makes `k -> P_k` injective.
Each completion projection is injective as well: if two `a` values agree,
then their defect difference is a multiple of `y`, but it also has size
`O(D)<y`; the two defects therefore agree.  The same argument applies to
`b` modulo `x`.

### Lemma 1.1 (exact paired Freiman two-isomorphism)

For `k_i in K`,

```text
k_1-k_2=k_3-k_4
 iff
(a_1-a_2,b_1-b_2)=(a_3-a_4,b_3-b_4).                (1.3)
```

**Proof.**  The forward implication gives

```text
x*((a_1-a_2)-(a_3-a_4))
 =y*((b_1-b_2)-(b_3-b_4)).                            (1.4)
```

Since `(x,y)=1`, the two parenthesized integers are respectively multiples
of `y` and `x`.  Their absolute values are strictly below `y` and `x` by
`(0.2)`, so both vanish.  The reverse implication follows from `(1.1)`.
`square`

Thus `k -> (a_k,b_k)` is an exact Freiman two-isomorphism.  In fact each
single coordinate projection is an exact Freiman two-isomorphism as well.
For example, if `a_1-a_2=a_3-a_4`, then `(1.1)` makes

```text
(k_1-k_2)-(k_3-k_4)
 =-y*((b_1-b_2)-(b_3-b_4)).                              (1.5)
```

The left side is `O(D)<y`, so both sides vanish.  The `b`-projection is
symmetric.  Consequently, for `A={a_k:k in K}`,

```text
E^+(A)=E^+(K)
       =sum_d r_K(d)^2
       >>H^4/D.                                       (1.6)
```

Here Cauchy was applied to `sum_d r_K(d)=H^2` and
`|K-K|<<D`.  If

```text
H=D^(7/8+eta),                                        (1.7)
```

then

```text
E^+(A)>>D^(5/2+4*eta).                                (1.8)
```

Thus `D^(5/2)` is not a guessed energy scale: it is exactly the scale forced
at the open fan threshold.

---

## 2. What dense differences prove

Order the defects.  At least half of the adjacent gaps have size
`O(D/H)`.  Pigeonholing those integral gaps proves that one nonzero `d`
satisfies

```text
0<d<<D/H,
# {k:k,k+d in K and adjacent in K} >>H^2/D.            (2.1)
```

By Lemma 1.1, all these pairs have one exact completion translation

```text
(a_(k+d)-a_k,b_(k+d)-b_k)=(s,r),
x*s-y*r=d.                                             (2.2)
```

At `(1.7)`, the two sizes are

```text
d<<D^(1/8-eta),       L:=# chords >>D^(3/4+2*eta).     (2.3)
```

This recovers the popular affine rank-two plane, now with a small defect
increment.  It does not yet give a carrier packet.

Let

```text
t_k=v_(k+d)-v_k.                                       (2.4)
```

From `(1.2)`,

```text
t_k=-C_x*s/[a_k*(a_k+s)]+O(D/q).                       (2.5)
```

On a fixed shell the main term in `(2.5)` is monotone in `a_k`, has total
range `O(1+|s|)`, and has derivative of size `asymp |s|/q`.  It follows that

```text
max_t # {k:t_k=t} >>L/(1+|s|),                         (2.6)
# {k:t_k=t} <<1+D/|s|             for every fixed t.   (2.7)
```

In particular, if the popular chord has `|s|<=sqrt(D)`, then at the critical
threshold at least

```text
D^(1/4+2*eta)                                          (2.8)
```

of its edges have one identical full translation `(d,s,r,t)`.  This is a
canonical family of parallel affine secants.  Equations `(2.6)--(2.8)` do
**not** say that three of the points lie on one occupied line: all the edges
may be disjoint two-point secants.

That distinction is real.  A set of `D^(7/8)` defects can be chosen inside
an interval with no three-term progression, so defect density and additive
energy alone cannot turn the popular chords into a recurrent carrier line.
The reciprocal/product arithmetic has to do that work.

---

## 3. The continued-fraction lattice

Put `u=x^(-1) (mod y)` and define

```text
Lambda={(d,s) in Z^2:s ==u*d (mod y)}.                 (3.1)
```

This is a determinant-`y` lattice.  If `z_i=(d_i,s_i)` are two of its
vectors, then

```text
det(z_1,z_2)=d_1*s_2-d_2*s_1 ==0 (mod y).              (3.2)
```

Hence the following elementary lemma is exact.

### Lemma 3.1 (one low rectangle, one rational ray)

If

```text
|d_i|<=R,       |s_i|<=S,       2*R*S<y,               (3.3)
```

then any two nonzero `z_i in Lambda` are collinear.  Indeed, `(3.2)` is a
multiple of `y`, while `(3.3)` makes its absolute value smaller than `y`.
Thus every lattice vector in the rectangle is an integral multiple of one
primitive continued-fraction ray.

The terminology is literal.  Write a nonzero lattice vector as
`s=u*d-m*y`.  Whenever `2|d*s|<y`,

```text
|u/y-m/d|=|s|/(|d|*y)<1/(2d^2).                        (3.4)
```

After reducing `m/d`, Legendre's criterion makes it a convergent of the
endpoint rotation `u/y`.  In particular every packet vector from Section 4
has this property because `|d*s|<<D^(3/2)=o(y)`.

There is also a literal continued-fraction certificate for a carrier chord.
Dividing `(2.5)` by `s` gives

```text
|t_k/s+C_x/[a_k*(a_k+s)]| <<D/(q*|s|).                (3.5)
```

For a sufficiently small fixed `c`, if `|s|<=c*q/D`, the right side is
less than `1/(2s^2)`.  After reducing `t_k/s`, Legendre's criterion says
that it is a convergent to the displayed reciprocal slope.  This is the
precise range in which a short completion chord is a continued-fraction
secant rather than merely a modular lift.

Density does not force this range.  Placing `H` points in an `a`-interval of
length `asymp q` guarantees only

```text
min_(i!=j)|a_i-a_j| <<q/H.                             (3.6)
```

At `H=D^(7/8)`,

```text
q/H=D^(19/16),          q/D=D^(17/16).                 (3.7)
```

Thus elementary spacing misses the continued-fraction scale by exactly
`D^(1/8)`.  Equivalently, the shell has `asymp D` cells of width `q/D`, and
a `D^(7/8)`-point fan can put at most one point in every used cell.

---

## 4. Unique completion ray for every genuine packet

The previous section did not assume that a packet exists.  If a genuine
packet does exist, its completion direction is canonical.

Consider `T_p>=3` actual wedge points on one affine line

```text
(k,a,b,v)=(k_0,a_0,b_0,v_0)
          +n*(d_0,p_a,p_b,-p_v),                      (4.1)
```

where the direction is integral.  On either real component of the line's
intersection with a product band, two occupied parameters are separated by
at least the number of intervening occupied lattice parameters.  One of the
two components contains at least `ceil(T_p/2)` points.  The standard
quadratic-curvature argument therefore gives

```text
p_a*p_v*T_p^2<<D,       p_b*p_v*T_p^2<<D.             (4.2)
```

All coordinates stay in one fixed positive shell, so a chord of the
reciprocal graph has `p_a asymp p_b asymp p_v`.  Therefore

```text
|p_a|+|p_b|+|p_v|<<sqrt(D).                            (4.3)
```

The defect coordinate in `(4.1)` satisfies

```text
d_0=x*p_a-y*p_b,       |d_0|<<D.                       (4.4)
```

Thus `(d_0,p_a)` belongs to `Lambda` and lies in the rectangle

```text
|d_0|<<D,       |p_a|<<sqrt(D).                        (4.5)
```

For two packet directions in one fixed endpoint fan, `(3.2)` and `(4.5)`
give

```text
|d_0*p_a'-d_0'*p_a|<<D^(3/2)=o(q)<y.                  (4.6)
```

The determinant is a multiple of `y`, so it is zero.  We have proved:

> **Unique-CF-ray packet lemma.**  Every genuine three-or-more-point
> affine/Hankel packet in a fixed endpoint fan has its completion vector
> `(d_0,p_a,p_b)` on one primitive continued-fraction ray.  The packet can
> therefore be labeled and removed at the incidence level before any Gram
> matrix or dyadic codegree layer is formed.

The margin in `(4.6)` is large:

```text
q/D^(3/2)=D^(9/16+o(1)).                               (4.7)
```

This lemma pins the completion ray, not automatically the carrier slope
`p_v`.  Different full packet directions over that ray must still be merged
with the existing fixed-direction theorem or controlled by a packet
Carleson estimate.  The lemma also does not force a dense fan to meet the
ray.

### 4.1 A reciprocal three-progression becomes a genuine packet

There is an exact converse at low completion step.  Suppose one completion
coordinate `a_0,a_1,a_2` forms an arithmetic progression.  The coordinate
Freiman isomorphism above shows that the defects and the other completion
coordinate form progressions too, so

```text
a_i=a_0+i*s,          b_i=b_0+i*r,             i=0,1,2.                (4.8)
```

Write `v_i=C_x/a_i+epsilon_i`, with `|epsilon_i|<<D/q`.  Directly,

```text
v_0-2*v_1+v_2
 =2*C_x*s^2/[a_0*(a_0+s)*(a_0+2*s)]+O(D/q).                          (4.9)
```

The left side is an integer.  Since `C_x asymp q^2` and `a_i asymp q`,
there is a shell-dependent `c>0` such that `|s|<=c*sqrt(q)` makes the
absolute value of the right side smaller than one.  Hence

```text
v_0-2*v_1+v_2=0.                                                        (4.10)
```

Thus `(k_i,a_i,b_i,v_i)` are three points of one genuine affine packet, not
merely a completion progression.  There is also a useful gap consequence.
Writing `v_i=v_0+i*t`, the second difference of `a_i*v_i` is `2*s*t`.
The product bands make it `O(D)`, while `(1.2)` gives `|t| asymp |s|` once
`|s|` exceeds a shell-dependent constant.  Therefore

```text
|s|<<sqrt(D).                                                            (4.11)
```

In particular, for suitable shell-dependent constants `C,c>0`, no occupied
completion three-progression can have

```text
C*sqrt(D)<|s|<=c*sqrt(q)=c*D^(33/32+o(1)).                              (4.12)
```

Every occupied completion three-progression below the upper endpoint of that
forbidden band is already on the canonical ray and is eligible for packet
peeling.  This still does not prove that a dense fan contains a recurrence: a
popular difference may be a matching of isolated two-point chords.

---

## 5. Exact ledger at the inverse-step endpoint

Write `w=D^beta`.  In the wrapped regime, the defect chart has

```text
J<<w*D/q=D^(beta-17/16)       branches,
M=q/w=D^(33/16-beta)          natural branch length.   (5.1)
```

At the proved pointwise endpoint `beta=73/64` and the open fan threshold,

```text
J=D^(5/64),       M=D^(59/64),
H/J=D^(51/64),    D/H=D^(8/64),
H^2/D=D^(48/64).                                    (5.2)
```

Thus every branch still has density `D^(-1/8)` on average.  A popular
within-branch defect gap has raw completion displacement at least
`w=D^(73/64)`, whereas it occurs only `D^(48/64)` times.  Its possible
carrier differences occupy an interval of length `O(wd)`.  Even at `d=1`
the alphabet is larger than the number of chords by

```text
D^(73/64-48/64)=D^(25/64).                             (5.3)
```

More generally, for `H=D^(7/8+eta)` with the maximal possible
`eta<=1/8`, the crude fixed-carrier recurrence exponent is

```text
3/4+2*eta-73/64<=-9/64.                                (5.4)
```

So dense differences cannot force a repeated carrier translation anywhere
in the allowed fan range unless a genuine modular near-return makes `s`
much smaller than the raw inverse step.  Equations `(3.6)--(3.7)` explain
why elementary spacing cannot force that near-return.

---

## 6. The exact open theorem after packet peeling

Let `P_0` be a subfamily of the wedges `(1.1)--(1.2)` after every actual
three-or-more-point affine line `(4.1)` has been assigned to its canonical
packet label and removed.  Put

```text
A_0={a:(k,a,b,v) in P_0}.                              (6.1)
```

The minimal remaining statement is:

> **Packet-free reciprocal-projection energy theorem (open).**  Uniformly
> in the actual mask and the fixed endpoints,
>
> ```text
> E^+(A_0)<<D^(5/2)*q^o(1).                            (PFRE)
> ```

If the peeled packets carry at least half of a fan, the unique-CF-ray lemma
gives a canonical incidence-level packet certificate.  Otherwise the
remainder has `|P_0|>>H`, and Lemma 1.1 plus `(PFRE)` gives

```text
H^4/D<<D^(5/2)*q^o(1),
H<<D^(7/8)*q^o(1).                                     (6.2)
```

Combined with the existing fixed-direction packet estimates, this would prove
the residual pointwise codegree target.  It would also fit the inverse-expander
route: energy above `D^(5/2)` would have to return spectral mass to the
canonical low-height packet ray.

No argument in this audit proves `(PFRE)`.  Scalar discrepancy bounds stop
at the already recorded local-beta endpoint.  Additive energy sees only the
completion projection and allows all popular chords to be isolated.  A
proof must use the integer product bands to show that the broad two-point
reciprocal secants cannot carry the critical `D^(5/2)` energy, or must prove
a Carleson packing theorem for those secants directly.

---

## 7. Status

```text
defect-to-each-completion Freiman two-isomorphism:   PROVED;
critical energy lower bound H^4/D:                 PROVED;
popular small-defect chord H^2/D:                  PROVED;
fixed-carrier chord bounds (2.6)--(2.7):           PROVED;
low-rectangle CF-ray collinearity:                 PROVED;
unique completion ray for every true packet:       PROVED;
low-step reciprocal 3AP and forbidden band (4.12): PROVED;
dense fan forces occupation of that ray:           NOT PROVED;
packet-free reciprocal energy bound (PFRE):        OPEN;
residual H<=D^(7/8):                                CONDITIONAL ON PFRE;
sharp four-cycle theorem:                           NOT PROVED.
```

The exact exponent and determinant ledger is replayed in
`src/qp_dense_defect_cf_energy_gate.py` and its focused test module.
