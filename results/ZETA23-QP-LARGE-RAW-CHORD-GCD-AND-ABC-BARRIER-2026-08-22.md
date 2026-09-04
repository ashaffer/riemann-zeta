# QP common carriers: large raw chords, a gcd reduction, and the `abc` barrier

**Date:** 2026-08-22  
**Verdict:** a repeated residual shift has a useful exact divisor invariant.
If its color translation is `(v,w)` and `g=gcd(v,w)`, then the parallel
color lines are indexed by only `O(D/g)` nonzero invariants.  This closes
the large-`g` part of the parallel-line count, but leaves the primitive
range `g<sqrt(D)`.

Standard `abc`, even if assumed, does not close that range.  It excludes
some high-exponent prime-power patterns, but is vacuous on the generic
all-prime stratum.  An exact odd-prime finite fixture below has two disjoint
primitive-range long chords with the same color translation and different
carrier drops, using globally distinct primes throughout.  This is not an
asymptotic counterexample, but it rules out a coprimality-only merger.

---

## 1. The gcd/line-invariant lemma

Fix coprime rows `a,a'` in the project shell and write a common neighbor as

```text
(b,c,d),       bc in I_a,       bd in I_a',
h=a'd-ac,      |h|<<D.
```

Suppose a repeated nonzero residual difference `k` sends two or more color
pairs by the same oriented translation

```text
(c,d) -> (c+v,d+w),             v,w>0,
k=a'w-av.
```

Put

```text
g=gcd(v,w),                     lambda=vd-wc.
```

Then

```text
g | k,                          g | lambda,
k!=0,                           lambda!=0,
a'lambda=vh-ck,                 |lambda|<<D.       (1.1)
```

The divisibilities are immediate.  If `k=0`, coprimality of `a,a'` makes
`a|w` and `a'|v`, impossible because both color chords are shorter than the
smallest shell node.  If `lambda=0`, the positive vectors `(c,d)` and
`(c+v,d+w)` are proportional.  Both are primitive because their coordinates
are distinct shell prime powers, so they would be equal, again impossible.
The last identity in (1.1) follows by expanding `vh-ck`.

Consequently the possible parallel color lines number at most

```text
O(D/g).                                             (1.2)
```

More explicitly, with `v=gv0`, `w=gw0`, and `lambda=g ell`, every source
on one such line has

```text
v0 d-w0 c=ell,
(c,d)=(c0,d0)+t(v0,w0),                            (1.3)
```

and the repeated chord is exactly `t -> t+g`.  Thus all components having
the same `lambda` lie on one affine color line.  The line count (1.2) is at
most `sqrt(D)` when `g>=sqrt(D)`.  The unresolved case is precisely the
primitive-ish range `g<sqrt(D)`.

There is a useful exact ledger for what remains.  Put

```text
e=k/g,                         ell=lambda/g.
```

Then the primitive direction and the affine color line obey

```text
a'w0-a v0=e,                  v0 d-w0 c=ell.        (1.3a)
```

For fixed `e`, the first equation has at most one primitive chord direction
in the shell: the difference of two solutions would be a multiple of
`(a',a)`, larger than the available chord box.  The elementary parameter
count is nevertheless

```text
sum_(1<=g<<D) O((D/g)^2)=O(D^2).                   (1.3b)
```

Even the part `g>=sqrt(D)` sums only to `O(D^(3/2))`, not `O(D)`, if one
forgets the reciprocal carrier tests.  Thus (1.2) is a per-translation
gain.  The missing global gain must couple the two small primitive defects
`(e,ell)` to the carrier rounding; divisibility alone does not supply it.

For an edge whose carrier drops from `b` to `B=b-u`, put

```text
s=B(c+v)-bc,                  t=B(d+w)-bd.
```

The two product windows give `|s|+|t|<<D`, and exact elimination gives

```text
u lambda=ws-vt.                                    (1.4)
```

This pins the tangent defect but does not aggregate the distinct nonzero
`lambda` lines.

---

## 2. The strongest direct consequence of standard `abc`

Write the four colors of one chord as distinct prime powers

```text
c=p1^e1, d=p2^e2, c+v=p3^e3, d+w=p4^e4.
```

Their determinant equation is a coprime `abc` equation

```text
(c+v)d-c(d+w)=-lambda.                             (2.1)
```

If `D=q^(delta+o(1))`, standard `abc` applied to (2.1) yields the necessary
condition

```text
sum_(j=1)^4 1/e_j >=2-delta-o(1).                 (2.2)
```

At the project value `delta=16/33`, the right side is `50/33`.  Thus `abc`
does exclude, for example, a chord whose four colors all have exponent at
least three.  It does not touch the generic all-prime layer: there the two
large terms in (2.1) have height `asymp q^2`, while their radical already
contains four distinct primes of size `asymp q`, so the `abc` quality is at
most `1/2`.  The product equation `q^3+r=8abc` with prime `a,b,c` similarly
has quality at most `3/4` before the radical of `r` is even counted.

Vertex-disjoint isolated chords introduce new prime bases rather than
reusing old ones.  Multiplying or combining their equations only increases
this radical surplus.  Standard `abc` controls powerful/small-radical
configurations; the isolated all-prime sector is the opposite extreme.

---

## 3. Exact all-prime finite long-chord fixture

Take

```text
q=1600033,          D=69885,
a=791563,           a'=880007.
```

All three displayed constants are prime.  The literal hard window has
exactly the following four common neighbors, listed as `(h,b,c,d)`:

```text
(-14176, 806801, 801761, 721181)
(-8274,  862297, 750161, 674767)
(578,    689929, 937577, 843347)
(6480,   730111, 885977, 796933).                 (3.1)
```

Every one of the twelve coordinates in (3.1) is prime, all fifteen labels
including `q,a,a'` are distinct, and every shell label lies in

```text
(q exp(-.2)/2, q exp(.2)/2).
```

For all four neighbors,

```text
h=a'd-ac,
|8abc-q^3|<qD,               |8a'bd-q^3|<qD.      (3.2)
```

The residual shift `k=14754` produces two disjoint one-edge components,
the first from line 1 to line 3 of (3.1), the second from line 2 to line 4.
Both have

```text
(v,w)=(135816,122166),       gcd(v,w)=6<sqrt(D),
```

but their carrier drops are respectively

```text
u=116872,                    u=132186.             (3.3)
```

Their line invariants and product changes are

```text
(lambda,s,t)=(-15630,-14528,   382),
(lambda,s,t)=(-13854,-26370,-10236).               (3.4)
```

In particular `v>D`, both edges satisfy (1.4), and neither a fixed-carrier-
shift argument nor prime coprimality merges them.  The example is finite;
it does not disprove an asymptotic estimate which uses `D^2/q=o(1)`.

---

## 4. Hardy--Littlewood heuristic for the tangent obstruction

In an admissible odd-prime recentering of the multilevel tangent model, an
anchored pair of completions asks for eleven additional affine forms to be
prime: three nonanchor colors and four row/carrier labels at each of two
completion parameters.  A Hardy--Littlewood prime-tuple heuristic therefore
thins the full-integer count only by

```text
(log q)^(-11),
```

provided the forms are locally admissible.  Hence an anchored factorial
mass of geometric size `D^(3/2)` is heuristically still

```text
D^(3/2)/(log q)^11=D^(3/2-o(1)),                  (4.1)
```

which exceeds the desired `D q^o(1)` AFP scale by a power.  This is not a
construction: the known exact multilevel model has even `q`, and the known
odd-prime rational recentering has a composite anchor.  It does show why
ordinary prime density and standard `abc` are not plausible sources of the
missing power saving.  A proof needs a genuine anti-aliasing theorem for
the coupled reciprocal/product conditions.

---

## 5. The exact free parameter in anchored factorial energy

The existing multilevel tangent construction also identifies the first free
parameter in the anchored factorial statistic.  In its notation, fix
`h in [L,2L]` and define row-pair and color-pair vertices

```text
rho_t=(m+t,m+h+t),                 20L<=t<=21L,
gamma_0=(m,m-h),
gamma_l=(m-l,m-h-l),              L<=l<=2L, l!=h.
```

The carrier joining `rho_t` to `gamma_0` is `m-t`, while the carrier joining
`rho_t` to `gamma_l` is `m+l-t`.  All these triples satisfy the literal
product window proved in the multilevel report.  Hence, for each fixed `h`,
the localized row-pair/color-pair graph contains an exact

```text
K_(L+1,L+1).                                        (5.1)
```

There are only `O(D)` vertices on each side because `D=2048L^2`.  For an
anchor `rho_t`, its `L` other row vertices have codegree `L+1`, and therefore

```text
F(rho_t)
 =sum_(rho'!=rho_t) m(rho_t,rho')*(m(rho_t,rho')-1)
 >=L^2*(L+1)
 asymp D^(3/2).                                     (5.2)
```

In particular, fixing the ordered color neighbors `(gamma_0,gamma_l)` does
not determine the second row pair.  The opposite row/carrier translation
`t'` remains free over an interval of length `asymp sqrt(D)`.  Its exact row
determinant relative to the anchor is

```text
det(rho_t,rho_t')=h*(t-t').                         (5.3)
```

Thus fixing that determinant pins the second row, but the determinant itself
has `asymp sqrt(D)` legal values.  This is the precise tangent parameter that
an attempted `q^o(1)` determination silently omits.

The block (5.1) is one certified coherent affine chart.  It is supposed to be
merged before estimating the generic/scattered remainder, and its merged
Hankel norm is target-sized.  Therefore (5.2) refutes the **raw** AFP estimate
in the full-integer shell, not the post-merger generic AFP sought by the
packet program.  The finite prime fixture in Section 3 supplies the
complementary warning: after leaving the coherent chart, primitive long
chords need not have a common carrier translation even on globally distinct
actual primes.

```text
gcd/line-invariant reduction:                    PROVED;
large-g line count O(sqrt(D)):                   PROVED;
standard abc exclusion of high-exponent chords: PROVED CONDITIONALLY;
standard abc control of the all-prime layer:     NO;
finite all-prime primitive long-chord fixture:   VERIFIED;
raw full-integer AFP bound `F<<D`:                FALSE (COHERENT CHART);
post-merger generic/scattered AFP:                OPEN;
asymptotic actual-prime counterexample:          NOT CLAIMED;
primitive isolated-line aggregate bound:        OPEN.
```

The finite ledger is replayed by

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_large_raw_chord_barrier.py
```
