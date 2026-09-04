# Remote parallel-null fan falsification audit

Date: 2026-08-29

Status: no counterexample found.  The physical remote-null branch is
nonempty, including on actual prime-power support, but every measured line
population product is `O(D)` and the strongest whole-star ratio is 1.26.

Replay:

```bash
python3 results/verify_zeta23_qp_remote_parallel_null_fan_falsifier_affine_falsifier.py
```

The script uses exact literal hard windows for the integer and critical
prime-power scans.  The `U=35,40,44` actual-prime-power scans inherit the
core builder's floating support-selection boundary; all incidence, line,
witness, null, stationary-height, and ratio tests after materialization are
exact.

## 1. Literal critical-window search

For a residual edge `(b,B)--(c,C)`, a left line has primitive direction
`p=(p1,p2)` and a right null-dual line has direction `(p2,p1)`.  The exact
stationary constants audited here are

```text
h_U=p2*d-p1*D,               h_V=p1*e-p2*E.
```

The table gives the maximum null-line population product.  `nonaff` is the
maximum among pairs for which both row-witness graphs are non-affine.

| mask | q | D | null fans | both non-affine | max product/D | max nonaff |
|---|---:|---:|---:|---:|---:|---:|
| all integers | 809 | 25 | 8 | 8 | 12/25 = .480 | 12 |
| all integers | 1400 | 33 | 4 | 0 | 9/33 = .273 | 0 |
| all integers | 3500 | 52 | 44 | 16 | 12/52 = .231 | 12 |
| all integers | 10000 | 86 | 332 | 40 | 36/86 = .419 | 12 |
| all integers | 20000 | 121 | 460 | 68 | 49/121 = .405 | 9 |
| prime powers | 11801 | 94 | 0 | 0 | 0 | 0 |
| prime powers | 25013 | 135 | 0 | 0 | 0 | 0 |
| prime powers | 100003 | 265 | 0 | 0 | 0 | 0 |
| prime powers | 200003 | 371 | 0 | 0 | 0 | 0 |
| fixed seven actual primes | 5868182 | 1912 | 4 | 0 | 9/1912 = .00471 | 0 |

The strict prime-power graphs in the growing ladder have residual degree
one, so no rich line occurs.  The known seven-prime double star does contain
three-point null-dual arms, but their witnesses are affine and their product
is only 9.

### Exact physical remote certificate

At `q=809,D=25`, take the residual edge

```text
(b,B)=(391,440), (c,C)=(449,399), a=377.
```

One left arm lies on `8d-9D=1`, with primitive direction `(9,8)`:

```text
(d,D;x)=(377,335;449), (404,359;419),
        (449,399;377), (485,431;349).
```

Its primitive parameters and witnesses are

```text
(t,x)=(0,449),(3,419),(8,377),(12,349),
```

which are non-affine.  One right arm lies on the null-dual line with
direction `(8,9)`:

```text
(e,E;y)=(335,377;440),(391,440;377),(431,485;342),
(s,y)=(0,440),(7,377),(12,342),
```

and is also non-affine.  Here

```text
h_U=1, h_V=-1,  |U||V|=12,  max|de-DE|=12.
```

All displayed physical triples lie in the literal window: the maximum
absolute cubic residual is 20199, below `qD=20225`.  Both arms are remote by
a huge margin:

```text
min(|p_i|)^2 H_U^3/q = 8^2*12^3/809 > 136,
min(|r_i|)^2 H_V^3/q > 136.
```

Thus the physical remote parallel-null case cannot be declared empty or
reduced automatically to affine witnesses.  It nevertheless satisfies the
target scale with room to spare.  After deleting the central neighbor, the
right arm has only two points; the literal critical scans found no example
where both remaining non-affine arms still had at least three points.

## 2. Materialized actual-prime-power remote fans

| q,U | D | null fans | both nonaff | h=(0,0) | max product/D | max after central deletion |
|---:|---:|---:|---:|---:|---:|---:|
| 11801,35 | 94 | 960 | 896 | 0 | 36/94 = .383 | 25/94 = .266 |
| 11801,44 | 94 | 2636 | 2444 | 0 | 80/94 = .851 | 63/94 = .670 |
| 25013,40 | 135 | 976 | 928 | 0 | 49/135 = .363 | 36/135 = .267 |
| 50021,40 | 189 | 1108 | 1068 | 0 | 36/189 = .190 | 25/189 = .132 |

The strongest fixture is `q=11801,U=44`.  Its maximizing pair has
directions `(1,1),(1,1)`, populations 10 and 8, both non-affine witness
graphs, and parameter spans 1026 and 1090.  Hence its two remote numerators
are

```text
1026^3 = 1080045576 >> q,   1090^3 = 1295029000 >> q.
```

After removing the central neighbor from both arms, 9 and 7 non-affine
points remain, giving the still-physical product 63.  This is stronger than
the `q=809` certificate as evidence that the remote fan is a genuine local
configuration rather than a central-edge artifact.  It still does not
violate `|U||V| << D q^o(1)`.

This logarithmic fixture uses a fixed smooth cutoff rather than the
constant-one literal radius `qD`: its displayed fan has minimum literal
radius 11483, about `122.2D`, and cross-determinant cap 6516, about `69.3D`.
Thus it is evidence for an `O_U(D)` theorem, not for sharp constant one.  The
`q=809` certificate above is the strict `|residual|<=qD` test.

The height stratification is informative.  No tested physical prime-power
rich null fan has `h_U=h_V=0`.  The maximum products occur for small but
nonzero heights (at `q=11801,U=44`, product 80 lies in
`max(|h_U|,|h_V|)<=8`).  Exact zero is not merely empirically rare on the
actual mask: two distinct shell prime powers have distinct prime bases and
are coprime.  A primitive line with `h=0` is a line through the origin, so
every point on it is `(tp1,tp2)` with gcd `t`; coprimality forces `t=1`.
It therefore contains at most one admissible ordered prime-power pair.
The projected `D^2` countermodels at exactly zero stationary height cannot
lift literally to an actual-prime-power rich arm.  Small nonzero height is
the real remaining case.

## 3. Strengthened dominant-fan whole-star test

For every residual edge, let `U,V` be its full endpoint neighborhoods and
let `R_U,R_V` be their largest affine-line occupancies (one- and two-point
arms are treated as lines).  The audited ratio is

```text
|U||V| / (D + R_U R_V).
```

| q,U | worst degrees | R_U,R_V | exact minimum line covers | ratio |
|---:|---:|---:|---:|---:|
| 11801,35 | 10,7 | 3,3 | 4,3 | 70/103 = .680 |
| 11801,44 | 14,9 | 3,2 | 6,5 | 126/100 = 1.260 |
| 25013,40 | 10,8 | 2,3 | 5,4 | 80/141 = .567 |
| 50021,40 | 9,7 | 2,2 | 5,4 | 63/193 = .326 |

The maximum exact affine-line cover of any arm in these fixtures is six.
This is compatible with a `q^o(1)` line-cover theorem, but finite bounded
degrees cannot establish one.  No growth in the dominant-fan ratio is
visible; the sole value above one is the resonant small-q fixture and is
only 1.26.

## 4. Parametric control and route verdict

The existing physical affine transition grid supplies an exact parametric
null-fan control.  For every `L`, both arms have direction `(1,1)`, affine
witnesses and stationary heights `(1,-1)`, while

```text
|U||V|=L^2,             D_window=512L^2.
```

It therefore saturates the correct linear-in-D order at constant `1/512`.
No parametric physical model with non-affine remote witnesses and
superlinear population product was found.  The rational-ray algebra can
make projected `D^2` fans at `h=0`, but the common row-completion masks are
exactly the missing condition; on actual prime powers, the preceding gcd
argument already forbids the required rich zero-height lines.

The local RDP route would genuinely bypass global `H_aff`, but only in its
whole-star form.  If one proves uniformly that

```text
|U_e||V_e| << q^o(1) (D + maximum null-line-pair product)
```

and proves the physical parallel-null fan bound for that maximum, then
`deg(p)deg(gamma)<<Dq^o(1)` follows edgewise.  The standard bipartite
edge-degree spectral inequality then closes the residual operator directly;
there is no packet selection, double assignment, or colorwise affine
Carleson summation, so the global `H_aff` obstruction disappears.

A theorem only for one selected line pair does **not** suffice: the rest of
each star could occupy many lines.  One must additionally prove either the
displayed dominant-fan inverse or a `q^o(1)` physical line-cover theorem.
The finite cover counts and ratios support this strengthened route but do
not prove it.
