# QP combinatorial inverse gate: popular differences, BSG, and label dispersion

**Date:** 2026-08-24  
**Verdict:** broad energy above `D^(5/2+epsilon)` does force polynomially
many popular differences, each with polynomial multiplicity.  At the
critical fan size `H=D^(7/8)`, both guaranteed exponents are only
`3/4+epsilon`; a fixed-difference graph can still be a matching until
`epsilon=1/8`.  Standard Balog--Szemeredi--Gowers therefore retains a
polynomial core but does not force a packet.

This is a genuine limitation of a purely additive inverse step.  A Behrend
set reaches energy `D^(21/8-o(1))` with no three-term progression.  More
strongly, the exact endpoint-lattice fixture in Section 4 assigns globally
consistent integer mixed labels to its broad rectangles, has no three-point
full affine packet, and makes the label injective in the base for all but
`D^(61/32+o(1))` rectangles.  Its total energy is
`D^(84/32-o(1))`.  Thus BSG, dependent random choice, or additive-cube
production alone cannot supply the repeated error label needed by the
product-error rigidity lemma.

The fixture deliberately violates the individual physical product bands.
It is a proof-mechanism obstruction, not a QP counterexample.  A successful
inverse theorem must use those bands before, or during, label recurrence.
Section 6 does insert the bands into the cube extraction.  It proves that
supercritical energy supplies `D^(3+2epsilon)` all-broad additive
three-cubes, but reciprocal third-difference rigidity then puts every one
of them in the *high*-volume sector `|rsu|>>q^2`; it does not create a
contradiction.  Raw direction capacity is ample for that outcome.
No packet-free `D^(5/2+o(1))` theorem or sharp four-cycle bound is claimed.

## 1. The exact popular-difference consequence

Let `A` have size `H`, write

```text
r(d)=#{a in A:a+d in A},       E(A)=sum_d r(d)^2,     (1.1)
```

and suppose the nondegenerate broad part has mass `E`.  The narrow and
degenerate parts are `O(D^2 log q+H^2)`, so when
`E>>D^(5/2+epsilon)` they may be discarded first.  Since

```text
sum_d r(d)=H^2,                                      (1.2)
```

the levels with `r(d)<E/(2H^2)` contribute at most `E/2` to the full
energy supporting the broad mass.  Dyadically decomposing the remaining
levels gives a number `L` and a set `P` of differences such that

```text
L <= r(d)<2L                 for d in P,
L >= E/(2H^2),
|P| L^2 >> E/log(2H),
|P| >> E/(H^2 log(2H)).                              (1.3)
```

This is the strongest conclusion available from the two elementary moment
identities alone.  At

```text
H=D^(7/8),             E=D^(5/2+epsilon),             (1.4)
```

it reads

```text
L, |P| >= D^(3/4+epsilon-o(1)).                       (1.5)
```

The graph with edges `{a,a+d}` for a fixed `d` has `r(d)` edges.  If `A`
has no three-term progression, this graph is a matching: two consecutive
edges would give `a-d,a,a+d`.  The matching capacity is `H/2`, whereas

```text
L/H >= D^(-1/8+epsilon-o(1)).                         (1.6)
```

Consequently `(1.5)` does not force even one concatenated same-direction
pair for any fixed `epsilon<1/8`.  The exponent `1/8` is exact: the maximum
possible energy is `H^3=D^(21/8)`, so the hypothesis itself becomes
impossible beyond that endpoint.

Direction-pair recurrence is nevertheless cheap.  A rectangle is
determined by its base and two defect shifts, and there are only `O(D^2)`
ordered shift pairs.  Hence `E>D^(5/2+epsilon)` already gives one fixed
pair carrying

```text
>>E/D^2=D^(1/2+epsilon)                              (1.7)
```

rectangles.  Two distinct bases produce an additive three-cube with the
same two face directions.  Thus the obstruction is not a shortage of
overlapping rectangles; it is the absence of a repeated mixed error label.

## 2. What standard BSG retains

Put

```text
K=H^3/E.                                              (2.1)
```

One standard polynomial-loss form of Balog--Szemeredi--Gowers gives a
subset `A'` with

```text
|A'| >> H/K,             |A'-A'| << K^4 |A'|.        (2.2)
```

At `(1.4)`,

```text
K=D^(1/8-epsilon),
|A'| >= D^(3/4+epsilon-o(1)),
|A'-A'|/|A'| <= D^(1/2-4epsilon+o(1)).                (2.3)
```

Thus BSG does preserve a polynomial number of points, but `(2.3)` is not a
packet theorem.  Even replacing its polynomial doubling loss by a
subpower loss would not suffice: progression-free Behrend sets already
have subpower doubling.

Indeed, let `R=D^(7/8)` and take a Behrend set

```text
B subset [R,2R],       |B|=R^(1-o(1)),                (2.4)
```

with no nontrivial three-term progression.  Cauchy--Schwarz on its sums or
differences gives

```text
E(B) >= |B|^4/O(R)=R^(3-o(1))=D^(21/8-o(1)).         (2.5)
```

For every fixed `epsilon<1/8`, `(2.5)` exceeds
`D^(5/2+epsilon)`.  Nevertheless every fixed-difference graph is a
matching.  This rules out a purely additive implication

```text
broad energy above D^(5/2+epsilon) => polynomial packet. (2.6)
```

Dependent random choice may still find corners or higher additive cubes in
such a dense set.  The remaining issue is not cube existence but recurrence
of the *same physical mixed label*.  The next fixture isolates this point.

## 3. Exact endpoint-lattice setup

Let `L` tend to infinity and set

```text
y=L^2+1,                  x=L^2-L+1,
q=2y,                     D=q^(16/33),
R=D^(7/8)=L^(28/33+o(1)).                            (3.1)
```

Then

```text
xL-y(L-1)=1,             R=o(L).                     (3.2)
```

For integers `k in [R,2R]`, define

```text
a_k=y+Lk,
b_k=x+(L-1)k,
v_k=y-Lk+3k^2-floor(k^3/L).                          (3.3)
```

The endpoint identity is exact:

```text
x a_k-y b_k=k.                                       (3.4)
```

All three coordinates are `(1+o(1))q/2`.  Their largest shell variation is

```text
LR=D^(61/32+o(1))=o(q),                              (3.5)
```

while `R^2=D^(7/4)` and `R^3/L=D^(51/32+o(1))` are
smaller.  Also, on `[R,2R]`,

```text
Delta^2 v_k
 =6-Delta^2 floor(k^3/L)>0                           (3.6)
```

for all sufficiently large `L`, because
`Delta^2(k^3/L)=O(R/L)=o(1)` and flooring changes a second difference by
less than `2`.  Hence the graph `(k,v_k)` is strictly convex.  No three of
the full points `(k,a_k,b_k,v_k)` are affinely collinear.

Retain only the indices `k` in the Behrend set `B` from `(2.4)`.  The
affine map `k -> a_k` preserves additive energy, so the retained point set
has size `D^(7/8-o(1))`, energy `(2.5)`, and no full affine packet.

## 4. A globally consistent label that defeats cube recurrence

An occupied additive rectangle has indices

```text
k, k+d, k+e, k+d+e in B.                             (4.1)
```

Its completion directions are

```text
r=Ld,                   s=Le,
|rs|=L^2 |de| asymp q |de|.                          (4.2)
```

Thus every nondegenerate rectangle lies in the broad regime
`|rs|>=c q` for a fixed sufficiently small `c`.

Define its integer carrier label by

```text
t(k;d,e)=v_k+v_(k+d+e)-v_(k+d)-v_(k+e).              (4.3)
```

Writing `{z}` for the fractional part of `z`, direct expansion gives the
exact formula

```text
t(k;d,e)
 =6de-3de(2k+d+e)/L+eta(k;d,e),
eta={k^3/L}+{(k+d+e)^3/L}
    -{(k+d)^3/L}-{(k+e)^3/L},       |eta|<2.         (4.4)
```

Because `k,d,e=O(R)=o(L)`, this has precisely the broad reciprocal scale

```text
|t(k;d,e)| asymp |de| asymp |rs|/q.                 (4.5)
```

For two bases separated by a nonzero integer `u`, `(4.4)` yields

```text
t(k+u;d,e)-t(k;d,e)
 =-6deu/L+eta(k+u;d,e)-eta(k;d,e),
|eta(k+u;d,e)-eta(k;d,e)|<4.                         (4.6)
```

In particular, if `|de|>=L` then the labels are injective in the base.
There cannot be two occupied rectangles with the same directions `(r,s)`
and the same label `t`, even if dependent random choice has produced the
corresponding eight-vertex additive cube.

The exceptional direction pairs satisfy `0<|de|<L`.  The divisor bound

```text
#{(d,e):0<|d|,|e|<=2R, |de|<L} << L log(2R)          (4.7)
```

shows that all rectangles with such a pair, summed over their possible
bases, number at most

```text
|B| L log(2R)
 =D^(7/8+33/32+o(1))
 =D^(61/32+o(1)).                                    (4.8)
```

Degenerate rectangles contribute only `O(|B|^2)=D^(7/4+o(1))`.  Against
the total energy

```text
D^(21/8-o(1))=D^(84/32-o(1)),                        (4.9)
```

the noninjective sector in `(4.8)` is smaller by `D^(23/32-o(1))`.
Therefore almost all of the supercritical additive energy can sit on
globally consistent, broad, packet-free rectangles whose error labels do
not recur at fixed directions.

This is stronger than an arbitrary edge-colouring obstruction: the label
is the mixed second difference of one integer carrier function, and its
base variation is the corresponding exact third difference.

## 5. Scope and surviving inverse theorem

The fixture is not physical.  For example, after the cancellation of the
linear terms in `a_k v_k`, its variation contains

```text
asymp L^2 k^2,
```

which is `asymp L^2R^2>>D` over the retained interval.  Hence no common
band `|a_kv_k-C|<<D` holds; the second physical product band fails as well.
The construction therefore does not refute the desired QP theorem.

It does prove the following method-level no-go:

```text
popular differences + standard BSG/DRC + additive cubes
do not force a polynomial repeated-label packet at D^(5/2).             (5.1)
```

The missing input must couple the individual product errors across bases.
A viable inverse theorem would have to show that the *simultaneous physical
bands* prevent the label dispersion in `(4.6)` on a polynomial fraction of
the BSG core.  That product-band-aware recurrence statement remains open.

The exact identities, exponent ledger, and finite checks are in
`src/qp_combinatorial_inverse_bsg_drc_gate.py` and
`src/test_qp_combinatorial_inverse_bsg_drc_gate.py`.

## 6. Product-band-aware cube extraction

There is a clean positive cube theorem, but it points into the wrong
metric sector.  Let `B(d,e)` be the number of bases of occupied rectangles
with ordered defect directions `(d,e)`.  Pairing two such bases produces
an ordered additive three-cube, so

```text
C_2(A)=sum_(d,e) B(d,e),
C_3(A)=sum_(d,e) B(d,e)^2.
```

There are only `O(D^2)` ordered direction pairs.  Cauchy--Schwarz gives

```text
C_3(A) >> C_2(A)^2/D^2.                              (6.1)
```

This is also the unnormalized `U^2<=U^3` inequality on an ambient group
of size `asymp D`.

Therefore broad energy

```text
C_2(A)>D^(5/2+epsilon)                               (6.2)
```

forces

```text
C_3(A)>>D^(3+2epsilon).                              (6.3)
```

The previously proved reciprocal rectangle gap bounds the narrow and
degenerate two-cubes by `O(D^2 log q)`.  Fixing such a face leaves at most
`O(D)` choices for the third defect direction.  After summing the three
face-direction pairs, the number of three-cubes with at least one narrow
or degenerate pair is

```text
O(D^3 log q).                                        (6.4)
```

For every fixed `epsilon>0`, subtraction of `(6.4)` from `(6.3)` leaves
`D^(3+2epsilon-o(1))` cubes for which

```text
|rs|, |ru|, |su| >= c q.                             (6.5)
```

Here `r,s,u` are the three completion directions.  This is the strongest
unconditional additive-cube output needed for the proposed inverse route.

Now use the individual product band, not merely additive structure.  At
all eight vertices write

```text
v(z)=C/z+epsilon(z),          C asymp q^2,
|epsilon(z)|<<D/q.                                  (6.6)
```

The integer third mixed difference satisfies the exact integral formula

```text
Box_(r,s,u)(C/z)
 =-6 C r s u integral_[0,1]^3
   (a+theta_1 r+theta_2 s+theta_3 u)^(-4) dtheta,
                                                           (6.7)
```

and `|Box epsilon|<<D/q`.  Since every vertex is in the fixed positive
shell,

```text
|Box_(r,s,u)(C/z)| asymp |rsu|/q^2.                  (6.8)
```

If `|rsu|<c_0q^2` for a sufficiently small fixed `c_0`, integrality makes
the third difference zero.  Equations `(6.6)--(6.8)` then imply

```text
|rsu|<<Dq.                                           (6.9)
```

Thus the product bands give the exact forbidden volume annulus

```text
C_0Dq<|rsu|<c_0q^2.                                 (6.10)
```

But `(6.5)` implies

```text
|rsu|^2=|rs| |ru| |su| >>q^3,
|rsu|>>q^(3/2).                                      (6.11)
```

At the critical relation `q=D^(33/16)`,

```text
q^(3/2)/(Dq)=q^(1/2)/D=D^(1/32).                    (6.12)
```

Consequently an all-broad physical cube cannot fall on the small side
`(6.9)` for large `D`.  Combining `(6.10)` and `(6.12)`, every cube
surviving `(6.4)` must instead satisfy

```text
|rsu|>=c_0q^2.                                       (6.13)
```

This answers the proposed low-volume-cube route negatively: high energy
does force many all-broad cubes, but the product bands themselves push all
of them past the upper rigidity threshold.

There is no counting contradiction in `(6.13)`.  The defect interval has
`O(D^3)` ordered direction triples and at most `H<=D` bases per triple, so
the high-volume sector has raw capacity `O(HD^3)`.  Even at
`H=D^(7/8)` and the largest possible `epsilon<1/8`, this is
`D^(31/8)`, whereas `(6.3)` is at most `D^(13/4-o(1))`.  Pigeonholing only
shows that one high-volume direction triple has `D^(2epsilon-o(1))` bases;
the nonzero third-difference label has enough room to vary there.

The Section 3 fixture makes the volume obstruction explicit at the exact
lattice level.  There `r=Ld`, `s=Le`, `u=Lf`, and `q asymp L^2`, so

```text
|rsu|<q^2   =>   |def|<<L.                           (6.14)
```

The number of nonzero signed triples in `(6.14)` is `O(L log^2 L)`.
Hence the number of nondegenerate low-volume cubes is at most

```text
|B| L log^2 L=D^(61/32+o(1)).                        (6.15)
```

On the other hand, applying the same Cauchy--Schwarz argument with only
`O(R^2)` direction pairs and using `E(B)=R^(3-o(1))` gives

```text
C_3(B)>=R^(4-o(1))=D^(7/2-o(1)).                     (6.16)
```

Thus essentially every additive cube in the integer, packet-free,
endpoint-lattice fixture has high completion volume.  As emphasized above,
that fixture violates the physical product bands; it certifies the sharp
direction-volume and additive-method obstruction, not physical existence.

Closing the inverse branch now requires a theorem that counts the
high-volume cubes in `(6.13)` using simultaneous product errors.  Neither
standard BSG/DRC nor reciprocal third-difference integrality supplies such
a bound.
