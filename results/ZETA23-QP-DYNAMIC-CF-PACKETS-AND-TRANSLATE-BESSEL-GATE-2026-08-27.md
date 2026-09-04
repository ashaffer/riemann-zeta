# QP self-orbit dynamic CF packets and the translate-Bessel gate

**Date:** 2026-08-27  
**Verdict:** at every active dyadic reciprocal scale, a local cluster of one
short self-orbit is automatically an exact affine packet.  More strongly,
every connected cluster in the natural radius graph is one affine line and
its direction is a principal continued-fraction convergent of the anchor
slope.  Hence only `O(log q)` local coherent directions occur.

This proves the local half of an excess-implies-packet theorem while
retaining the actual prime-power mask.  For the stronger sufficient
total-edge problem one may legally enlarge to the complete integer orbit;
then each affine line piece is a contiguous all-one interval and the known
one-fan estimate applies separately.  It does not prove the needed global
dyadic moment: one legal full-integer self-orbit has 49 parallel translates
of the same convergent direction.  Numerical square-mean tests show almost
perfect orthogonality between such translates, but a canonical-orbit Bessel
theorem for their aggregation remains open.  The sharp four-cycle bound is
not proved.

## 1. The scale-correct target

For

```text
S_gamma(h)=sum_(t,j) alpha_t alpha_j
 e(h q^3/(8 b_t B_j))
```

the scale-correct dyadic estimate is

```text
sum_(K<h<=2K)|S_gamma(h)|^2
 <<(q^2/K)q^o(1),             q/D^2<=K<=q/D.       (1.1)
```

Writing

```text
R_K=sqrt(q/K),
```

the active range is

```text
sqrt(D)<=R_K<=D.                                    (1.2)
```

A coherent packet of physical diameter `R_K` has `R_K^2=q/K` cells and
saturates (1.1).  The previously proved one-fan `B`-process gives (1.1) for
one complete affine fan.  The question is whether many translated fans can
add coherently.

## 2. Exact self-orbit affine-area identity

Fix the primitive anchor `gamma=(c,C)` and label a physical orbit vertex
`v_i=(b_i,B_i)` by

```text
t_i=c*b_i-C*B_i,               |t_i|<=D.            (2.1)
```

Direct elimination of the second coordinates gives

```text
C det(v_2-v_1,v_3-v_1)
 =(t_2-t_1)(b_3-b_1)-(b_2-b_1)(t_3-t_1).           (2.2)
```

This identity allows the labels to span their full interval of diameter
`2D`; no local label assumption is hidden.  If the three first coordinates
have diameter at most `R`, then

```text
|C det(v_2-v_1,v_3-v_1)|<=4DR.                     (2.3)
```

Therefore `4DR<C` forces exact affine collinearity by integrality.

Now join two selected orbit vertices when their sup-norm distance is at
most `R`.  Three consecutive vertices on a graph path have first-coordinate
diameter at most `2R`, so `8DR<C` makes every such triple collinear.
Collinearity propagates along the path.  This proves:

> **Dynamic self-orbit packet theorem.** If
> `8DR<min(c,C)`, every connected component of the physical radius-`R`
> graph is contained in one exact affine line.

The statement is hereditary under arbitrary deletion, so it applies
without relaxing the actual prime-power mask.  At the project scale
`D=q^(16/33+o(1))`, one has `D^2/q=q^(-1/33+o(1))`; hence the hypothesis is
uniformly valid for every `R=R_K<=D` once `q` is sufficiently large.

This is a geometric statement only.  The established one-fan `B`-process
uses a contiguous all-one affine interval; its cancellation is not
hereditary under arbitrary deletion.  Consequently even a single affine
component does **not** yet give a mask-uniform restricted form of (1.1).
That conclusion is available only when the induced lane weights retain the
contiguous all-one (or an independently controlled bounded-variation)
hypothesis of the one-fan estimate.

## 3. Every dynamic direction is a continued-fraction convergent

Let a close difference be

```text
v'-v=g(p,P),               gcd(p,P)=1,              (3.1)
```

and orient it with `P>0`.  Its primitive anchor determinant is

```text
r=c*p-C*P=(t'-t)/g.                                  (3.2)
```

If the sup-norm difference is at most `R`, then

```text
|r|<=2D/g,             |P|<=R/g.                    (3.3)
```

Under `4DR<c`,

```text
|C/c-p/P|=|r|/(c|P|)<1/(2P^2).                     (3.4)
```

Legendre's criterion says that `p/P` is a principal continued-fraction
convergent of `C/c`.  Principal convergent denominators grow at least as
fast as every other Fibonacci number, so there are `O(log q)` possibilities.
Thus:

> **Dynamic direction theorem.** All nontrivial radius-`R_K` packet
> components use `O(log q)` exact affine directions, uniformly after the
> actual mask is imposed.

There is also a sharp capacity for one line.  Along primitive direction
`(p,P)`, labels advance by the nonzero integer `r`.  Hence

```text
#(one affine component)<=1+floor(2D/|r|).           (3.5)
```

This is an exact continued-fraction version of the coherent packet length
bound.

## 4. Exact reciprocal curvature on one packet pair

If the first affine lane has first-coordinate step `p` and the second has
second-coordinate step `P`, its reciprocal phase is

```text
Phi(u,v)=Q/[(b+p*u)(B+P*v)],       Q=q^3/8.          (4.1)
```

At the origin,

```text
Phi_uu=2Qp^2/(b^3 B),
Phi_vv=2QP^2/(b B^3),
Phi_uv=QpP/(b^2 B^2),
det Hess(Phi)=3Q^2p^2P^2/(b^4B^4).                 (4.2)
```

Thus every noncoordinate packet pair has a uniformly definite Hessian at
the expected scale `p^2P^2/q^2`.  This is the exact local curvature behind
the one-fan estimate.  It is not lost in the self-orbit reduction.

## 5. Parallel translates are the genuine survivor

The direction theorem does not bound translations.  At

```text
q=200000,       D=371,       R=20,                  (5.1)
```

three complete full-integer self-orbits give:

| anchor | direction | nontrivial translates | component sizes |
|---|---:|---:|---:|
| `(106319,106348)` | `(1,1)` | 11 | six `26`, five `25` |
| `(104467,111006)` | `(17,16)` | 49 | thirty-six `5`, thirteen `4` |
| `(118951,95146)` | `(4,5)` | 12 | eleven `10`, one `11` |

Every displayed direction is a principal convergent of `C/c`, and every
component obeys (3.5).  The second row is an exact counterexample to the
claim that `O(log q)` directions imply boundedly many packet pieces.  It is
not an actual-prime counterexample and it does not violate (1.1).

For a dynamic decomposition `{P_lambda}`, define

```text
S_(lambda,mu)(h)
 =sum_(i in P_lambda,j in P_mu)
   alpha_i alpha_j e(hQ/(b_i B_j)).                 (5.2)
```

The missing mask-sensitive translate theorem has two parts:

```text
sum_(h~K)|sum_(lambda,mu) S_(lambda,mu)(h)|^2
 <<q^o(1) sum_(lambda,mu)sum_(h~K)|S_(lambda,mu)(h)|^2,   (TB)

sum_(lambda,mu)sum_(h~K)|S_(lambda,mu)(h)|^2
 <<(q^2/K)q^o(1).                                      (PS)
```

Together `(TB)` and `(PS)` prove (1.1).  Neither follows merely from the
number of convergent directions.

The three fixtures above were evaluated at `K=256`, where
`R_K=27.95...` and their affine component decompositions are unchanged.
The ratios of the left side of `(TB)` to its right side without `q^o(1)`
were respectively

```text
1.0115867,       1.0734656,       1.0542993.         (5.3)
```

Their total dyadic masses divided by `q^2/K` were

```text
0.1277274,       0.0950567,       0.0254534.         (5.4)
```

This is strong finite evidence for translate Bessel orthogonality, not a
proof.  Exact nonprincipal aliases in completed fan coordinates warn that a
coefficient-blind Cotlar argument is insufficient; the self-orbit and
actual masks must be retained.

## 6. Multilevel obstruction audit

The multilevel tangent construction does not refute `(TB)` in one
self-orbit.  Fixing its step `h` fixes the anchor, and all source and centre
vertices then satisfy

```text
B-b=h.
```

They form one affine component.  Varying `h` creates the many old patches
but also changes the anchor slope, so those patches cannot be aggregated in
one `S_gamma`.  The regression fixture takes `m=10^11,L=10,h=11`; all 22
vertices form one radius-500 component while `D^2<q`.

## 7. Status

```text
exact self-orbit affine-area identity (2.2):            PROVED;
radius component is one exact affine packet:            PROVED;
every dynamic packet direction is a CF convergent:      PROVED;
number of dynamic directions is O(log q):               PROVED;
one-line label capacity (3.5):                           PROVED;
exact reciprocal Hessian determinant (4.2):             PROVED;
bounded number of parallel translates:                  FALSE;
fixed-anchor multilevel obstruction to translate Bessel: NO;
translate Bessel theorem (TB):                           OPEN;
packet square-sum theorem (PS):                          OPEN;
dyadic reciprocal moment (1.1):                         OPEN;
sharp four-cycle bound:                                 NOT PROVED.
```

Reproduction:

```text
PYTHONPATH=src pytest -q src/test_qp_self_orbit_dynamic_packets.py
```

Implementation:

```text
src/qp_self_orbit_dynamic_packets.py
src/test_qp_self_orbit_dynamic_packets.py
```
