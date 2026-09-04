# QP Cartesian determinant-strip line-spread theorem

**Date:** 2026-08-29

**Status:** proved abstract inverse theorem and a new strict reduction of the
two-scattered residual gate.  The physical rich-line lift and its global
affine Carleson charge remain open; hence this does not yet prove the sharp
four-cycle bound.

## 0. Theorem

For nonempty finite sets of nonzero integer vectors `U,V subset Z^2`, put

```text
F(u,v)=u_1*v_1-u_2*v_2,
K=max_(u in U,v in V)|F(u,v)|,
R_U=max_affine_line |U intersect line|,
R_V=max_affine_line |V intersect line|.
```

### Theorem CDLS -- Cartesian determinant line spread

```text
|U|*|V| <=162*max(1,K)*R_U*R_V.                    (0.1)
```

In particular, if `K<<D` and both arms are line-sparse with
`R_U,R_V=q^o(1)`, then

```text
|U||V|<<Dq^o(1).                                   (0.2)
```

This is exactly the residual edge degree-product estimate `(RDP)` in the
two-scattered sector.  It uses no hard-window row witnesses after the
Cartesian determinant strip has been established.

## 1. One-arm lattice line-spread lemma

Let `S subset Z^2` be finite and let

```text
Delta=max_(x,y in S)|det(x,y)|>0,
R=max_affine_line |S intersect line|.
```

Choose `x_0,y_0 in S` with `|det(x_0,y_0)|=Delta` and apply the inverse of
the matrix with columns `x_0,y_0`.  Every transformed `z in S` lies in
`[-1,1]^2`, because its coordinates are

```text
det(z,y_0)/Delta,        det(x_0,z)/Delta.          (1.1)
```

The transformed integer lattice has covolume `1/Delta`.  Minkowski applied
to a square supplies a primitive lattice vector `v` with

```text
||v||_infinity<=2/sqrt(Delta).                      (1.2)
```

On lattice lines parallel to `v`, the values of `det(v,z)` are consecutive
multiples of `1/Delta`.  Inside `[-1,1]^2` their absolute values are at most
`2||v||_infinity`; hence at most

```text
2 floor(4 sqrt(Delta))+1 <=1+8sqrt(Delta)           (1.3)
```

parallel lines meet the square.  Each contains at most `R` selected points,
so

```text
|S|<=R(1+8sqrt(Delta))<=9R sqrt(Delta).             (1.4)
```

If `Delta=0`, all nonzero members of `S` lie on one line through the origin,
and `|S|<=R`.

## 2. Couple the two arms by Pluecker

Let `Delta_U,Delta_V` be the maximum same-arm determinants.  Choose pairs
attaining both maxima.  The bilinear Pluecker identity is

```text
F(u_1,v_1)F(u_2,v_2)-F(u_1,v_2)F(u_2,v_1)
 =-det(u_1,u_2)det(v_1,v_2).                        (2.1)
```

Therefore

```text
Delta_U*Delta_V<=2K^2.                              (2.2)
```

When both determinants are nonzero, `(1.4)` and `(2.2)` give

```text
|U||V|
 <=81 R_U R_V sqrt(Delta_U Delta_V)
 <=81sqrt(2) K R_U R_V,
```

which is stronger than `(0.1)`.  If one determinant vanishes, that arm lies
on one line.  Fixing one of its nonzero vectors partitions the other arm
among at most `2K+1` affine level lines of `F`; this also implies `(0.1)`.

## 3. Consequence for the QP decision tree

The six-product identity around a residual transition edge already proves

```text
|F(u,v)|<<D       for every (u,v) in U x V.         (3.1)
```

The previously open “two scattered arms” clause is therefore solved as soon
as scattered is made literal:

```text
R_U,R_V=q^o(1).                                     (3.2)
```

More generally, a polynomial RDP violation now forces a polynomial product
`R_U R_V`; it cannot be supported by two direction-diverse arms.  This is a
genuine excess-implies-rich-lines inverse theorem.

The remaining issue has moved upstream.  A rich affine line in a projected
neighbor arm must be lifted to a completion-consistent four-edge
affine/Hankel packet, and all such lifted packets must satisfy the global
Carleson charge

```text
H_aff=max_c sum_t min(L_t,M_t)l_(t,c)<<Dq^o(1).     (3.3)
```

The fixed-direction merger proves the local packet estimate but not this
cross-direction lift/packing.  Thus CDLS closes the two-scattered
determinant-strip mathematics; it does not by itself construct the full
hybrid partition.

### 3.1 The naive projected-line lift is false, literally

There is an automatic but insufficient projective identity.  If projected
neighbors obey

```text
A*d+B*D+C=0,
```

and `x` is their common row witness, then

```text
A*(x*d)+B*(x*D)+C*x=0.                              (3.4)
```

This is a plane in product coordinates, not an affine plane containing the
original triples `(x,b,d)` and `(x,B,D)`.  The distinction already occurs
inside a literal residual hard window with `D^2<q`.

Take

```text
q=809, D=26, (b,B)=(391,440),
(x,d,D')=(349,485,431), (377,449,399),
          (419,404,359), (449,377,335).
```

All eight triples `(x,b,d),(x,B,D')` satisfy

```text
|8*x*column*color-q^3|<=qD.
```

The four projected neighbors lie on the exact line

```text
8*d-9*D'-1=0,
```

and their residual determinant tokens are respectively

```text
b*d-B*D' = -5,-1,4,7,
```

so none belongs to the tangent sector.  Nevertheless the witnesses are not
affine in the primitive line parameter.  More decisively, the eight
original points `(x,column,color)` have affine rank three, so no nontrivial
physical affine-plane equation contains them.  Their product-coordinate
lifts `(xd,xD',x)` have rank two exactly as `(3.4)` predicts.

Taking `(349,485,431)` as the central row/color pair, each of the other
three rows forms a literal four-edge completion rectangle with it.  Every
such displayed rectangle has eight distinct labels.  Thus the mismatch is
not caused by a tangent edge, a repeated label, or a missing completion
corner.  This first example uses ordinary integer coordinates.

The actual prime-power mask does not restore the automatic lift.  In the
materialized `q=11801,U=44` core, the left anchor `(4831,4993)` has the
three neighbors/witnesses

```text
(d,D;x)=(6121,5923;6947),
        (6481,6271;6561),
        (6781,6561;6271).
```

They lie on `-29d+30D=181`, but their witnesses are nonaffine in the
primitive parameters `0,12,22`; the six source triples have affine rank
three (an exact minor is `-750384`).  The homogeneous product lift still
holds.  This support-selection fixture inherits the core builder's floating
nearest-integer trust boundary, but primality, incidence, collinearity,
witness nonaffinity, and rank are checked exactly after materialization.

Therefore a projected rich line cannot simply be relabelled as one of the
already proved physical affine-plane packets, even on tested actual-prime-
power support.  Any successful lift must be a genuinely broader vector-
valued Hankel/fan theorem and must still prove its global completion-
consistent Carleson charge.

### 3.2 A quantified moderate-direction witness interpolation theorem

There is nevertheless a rigorous lift in a substantial direction range.
Fix a collar constant `alpha>0` and suppose

```text
alpha*q <=b,x_t,d_t,
|8*b*x_t*d_t-q^3|<=qD,
d_t=d_0+p*t,                 p!=0,                 (3.5)
```

for a finite, possibly sparse, integer parameter set `T`.  Put

```text
N=q^3/(8b),
epsilon_t=x_t-N/d_t.
```

There is no divisibility assumption here: `N` is an exact rational number.
The hard window gives

```text
|epsilon_t|<=D/(8*alpha^2*q).                       (3.6)
```

Take `t_0<t_1<t_2`, write

```text
a=t_1-t_0,       c=t_2-t_1,       H=a+c,
J=c*x_(t_0)+a*x_(t_2)-H*x_(t_1).                   (3.7)
```

The quantity `J` is an integer.  Direct common-denominator calculation
gives the exact reciprocal divided difference

```text
c*N/d_(t_0)+a*N/d_(t_2)-H*N/d_(t_1)
 =N*p^2*a*c*H/(d_(t_0)d_(t_1)d_(t_2)).             (3.8)
```

Consequently

```text
|J|
 <=p^2*H^3/(8*alpha^4*q)+H*D/(4*alpha^2*q).        (3.9)
```

Let `H_T=max(T)-min(T)`.  If

```text
p^2*H_T^3/(8*alpha^4*q)
 +H_T*D/(4*alpha^2*q)<1,                           (3.10)
```

then `(3.9)` forces every three-point interpolation defect to vanish.
Thus all pairs `(t,x_t)` lie on one rational affine line.  This proof uses
the actual sparse parameter gaps and does not complete `T` to an interval.

If the projected neighbors are

```text
(d_t,D_t)=(d_0,D_0)+t(p,P),                        (3.11)
```

then `(3.10)` makes `(x_t,d_t,D_t)` an affine line in three-dimensional
neighbor-witness space.  This is the exact conclusion; it is not yet a
four-edge affine/Hankel completion packet.  The two physical triple lines

```text
(x_t,b,d_t),             (x_t,B,D_t)               (3.12)
```

need not even lie in one three-variable affine plane.  If the witness slope
is `rho`, their direction vectors are `(rho,0,p)` and `(rho,0,P)`, and the
scalar triple product with their separation is

```text
rho*(p-P)*(B-b).                                   (3.13)
```

It is generally nonzero.  Therefore the moderate theorem licenses a
physical two-line star/fan candidate, not the existing scalar affine-plane
patch.

At the project scale `D^2/q=o(1)`, the error part of `(3.10)` is automatic
whenever `H_T<<D`.  The genuinely unclosed interpolation range is

```text
p^2*H_T^3 >= c*q                                  (3.14)
```

for a collar-dependent constant `c>0`.  This is the exact remote-curvature
inequality; merely citing `D^2<q` does not remove it.

### 3.3 Two transverse rich lines close at `O(D)`, without a lift

There is also a stronger direct result when both projected arms are affine.
Write

```text
U={u_0+t*p:t in T},       V={v_0+s*r:s in S},
eta=F(p,r).                                             (3.15)
```

Assume both sets have at least two points and

```text
|F(u,v)|<=K                    on U x V.             (3.16)
```

Let `H_T,H_S` be the spans of their sparse integer parameter sets.  Taking
the alternating sum of the four values at the parameter extrema gives

```text
eta*H_T*H_S
 =F(u_min,v_min)-F(u_min,v_max)
  -F(u_max,v_min)+F(u_max,v_max).                   (3.17)
```

If `eta!=0`, then `|eta|>=1`, so

```text
H_T*H_S<=4K/|eta|.                                  (3.18)
```

Since a sparse integer set of span `H` has at most `H+1` elements, and
`H_T+H_S<=H_T*H_S+1` for positive integral spans,

```text
|U||V|
 <=(H_T+1)(H_S+1)
 <=2H_T H_S+2
 <=8K/|eta|+2
 <=8K+2.                                           (3.19)
```

For the physical Cartesian determinant strip, `K<<D`.  Thus every pair of
rich projected lines with non-null direction pairing already satisfies RDP
at `O(D)`.  No witness interpolation, prime distribution, or packet lift is
needed.  This sharpens the earlier fixed-chart harmonic estimate.

The only two-rich-line local block not covered by `(3.19)` is therefore

```text
F(p,r)=0.                                          (PN)
```

For positive directions this is the parallel/ruling relation: up to
primitive normalization one direction is the coordinate-swapped dual of
the other.  If the affine expression in `(t,s)` also has nontrivial linear
coefficients, elementary strip bounds may still close it.  The hard core is
the parallel-null stationary block with small or zero linear coefficients.
The existing positive-definite Hessian theorem closes that block only when
the physical witness rows obey its exact integral stationary affine law.
The interpolation theorem proves such an affine law only under `(3.10)` and
does not, by itself, identify it with the stationary law required by that
theorem.

### 3.4 What affine witness interpolation really closes in the null block

The last warning does not mean that affine witness graphs are useless.  In
fact they close their local block by a simpler one-variable curvature
argument, without invoking the stationary Hessian theorem.

Here is the exact lemma.  Let `T` be a finite set of distinct integers and
suppose

```text
x_t=x_0+rho*t,             d_t=d_0+p*t,
alpha*q<=x_t,d_t<=beta*q,
|x_t*d_t-N|<=W                         (t in T),       (3.20)
```

where `p*rho!=0`.  If `L=|T|`, choose the parameter of middle rank between
the two extrema.  If its successive gaps are `a,c`, the exact quadratic
interpolation identity is

```text
c*(x*d)_(t_0)+a*(x*d)_(t_2)-(a+c)*(x*d)_(t_1)
  =rho*p*a*c*(a+c).                                  (3.21)
```

The left side has magnitude at most `2W(a+c)`, while middle rank and
integrality give

```text
a*c>=floor((L-1)^2/4).
```

Consequently

```text
|rho*p| floor((L-1)^2/4)<=2W.                       (3.22)
```

In the hard product window of Section 3.2 one may take
`W=D/(8*alpha)`.  Comparing the products at any two parameters a distance
`h>=1` apart also gives

```text
|rho*d_(t+h)+p*x_t|<=2W/h.                          (3.23)
```

Once `D/q` is sufficiently small in terms of `alpha,beta`, `(3.23)` forces
`rho` and `p` to have opposite signs and

```text
(alpha/(2*beta))*|p|<=|rho|<=(2*beta/alpha)*|p|.    (3.24)
```

Thus an affinely witnessed rich line satisfies the explicit population cap

```text
L<=2+C_(alpha,beta)*sqrt(D)/|p|.                    (3.25)
```

The same argument applies to either product leg and to the opposite arm.
Hence, if both projected arms have affine witness graphs, their Cartesian
population product is

```text
|U||V|<<_(alpha,beta) D.                            (3.26)
```

This proves the desired local estimate in particular in the primitive
parallel-null case.  Indeed, after orienting positive primitive directions,

```text
p_1*r_1-p_2*r_2=0       implies       r=(p_2,p_1).  (3.27)
```

No two-variable stationary-Hessian theorem is used in this deduction.  It
would be illegal to use that theorem directly: the two interpolated graphs
give separate rows `x(t)` and `y(s)`, whereas that theorem assumes one
actual row `x(t,s)` on the entire Cartesian chart, satisfying its exact
two-variable stationary affine formula.  The six product windows do not
create the missing cross-row witnesses or the row-lock divisibilities.

It remains to quantify what happens when interpolation fails.  Let
`H_U=diam(T)` and put

```text
lambda_U=b*p_1-B*p_2.                               (3.28)
```

The determinant-token window gives `|lambda_U|H_U<<D`.  Failure of the
subunit criterion `(3.10)`, with its second term absorbed by `D^2/q=o(1)`,
gives

```text
p_i^2*H_U^3>>_(alpha)q.                             (3.29)
```

In the actual distinct-prime-power sector, `lambda_U=0` makes the primitive
direction proportional to `(B,b)`, hence shell-scale; a fixed-width collar
then contains only `O_(alpha,beta)(1)` parameter values.  That case is
already harmless.  For a genuinely rich line `lambda_U!=0`, and combining
the last two inequalities yields the exact near-rational gate

```text
|lambda_U|^3 <<_(alpha) p_i^2*D^3/q.                (3.30)
```

For the null-dual right direction `r=(p_2,p_1)`, define

```text
lambda_V=c*p_2-C*p_1,          k=b*c-B*C.           (3.31)
```

The two small linear coefficients are not independent; direct expansion
gives the useful exact identities

```text
c*lambda_U+B*lambda_V=k*p_1,
C*lambda_U+b*lambda_V=k*p_2.                        (3.32)
```

The analogous failed-interpolation bound holds for `lambda_V`.  Equations
`(3.29)--(3.32)` are the precise residual arithmetic gate.  They do **not**
by themselves prove `|U||V|<<D`: `(3.29)` is a lower bound on a parameter
span, and `(3.30)` is an upper bound on an integral determinant defect.
Neither is an upper bound on the population of a possibly sparse parameter
set.  Closing this remote branch needs an additional prime-mask,
near-rational-direction, or fan-packing theorem.

There is a sharp projected countermodel to any attempt to deduce the missing
upper bound from these inequalities alone.  Let `Q` be large,
`q=2Q`, `n=floor(D/10)`, and take

```text
(b,B)=(Q+1,Q),                 (c,C)=(Q-1,Q),
u_t=(Q+t,Q+t+1),               1<=t<=n,
v_s=(Q+s,Q+s-1),               3n<=s<=4n.           (3.33)
```

Both primitive directions are `(1,1)`, hence null-dual.  Direct calculation
gives

```text
b*d_t-B*D_t=t,                 c*e_s-C*E_s=-s,
b*c-B*C=-1,                    F(u_t,v_s)=t-s+1.     (3.34)
```

Thus every individual token and the full Cartesian cross strip have size
`O(D)`, `lambda_U=1`, `lambda_V=-1`, and `(3.32)` holds.  If
`D^3>>q` (in particular at the project scale), both remote span inequalities
also hold, while

```text
|U||V| asymp D^2.                                      (3.35)
```

This is only a projected-shell countermodel: it does not supply the common
row witnesses required by all six hard product windows.  Its role is exact:
the remote inequalities, determinant strips, null classification, and shell
geometry do not close the branch; whatever closes it must use the omitted
physical witness/prime-mask information.

### 3.5 Exact remaining local and global gates

The local theorem now needed is strictly narrower than the former
two-scattered conjecture:

> **Parallel-null projected-fan theorem.**  For two physical neighbor lines
> satisfying `(PN)` and all six hard product windows, prove
> `|U||V|<<Dq^o(1)`, or host their transitions in a direct physical fan
> packet with the same bound, including the remote range `(3.14)`.

Even this local theorem would not by itself prove `(3.3)`.  Projected lines
are selected relative to a residual anchor edge.  The global theorem must
choose the local fan packets completion-consistently, assign every peeled
completion only once, and prove

```text
max_c sum_t min(L_t,M_t)l_(t,c)<<Dq^o(1).           (3.36)
```

The multilevel tangent fixture shows why the word “canonical” is material:
one packet per maximal completion line gives a polynomially excessive
Carleson ledger, whereas merging the same lines by their common plane or
fixed four-carrier direction gives one `O(D)` packet.  A stopping rule is
part of the theorem, not harmless bookkeeping.

## 4. Falsification scope

The factors `R_U R_V` are necessary.  Parallel affine arms can have
`|U|,|V|` of order `sqrt(D)` and hence `|U||V|` of order `D`; the line
occupancies are equally large.  Without a line cap, the primitive vectors
`(m+t,m+t+1)` can give populations of order `D` in a determinant strip and
product `D^2`.

The theorem therefore does not relabel a rich affine obstruction as
dispersive.  It proves precisely that rich lines are the only obstruction
to the Cartesian strip bound.

The literal example in Section 3.1 also falsifies the most tempting way of
disposing of that obstruction: homogenizing by the row witness does not
intertwine the original color-weighted operator with the product-coordinate
plane.

## 5. Verification

Exact finite ledgers and hostile/random tests are in

```text
src/qp_cartesian_determinant_line_spread.py
src/test_qp_cartesian_determinant_line_spread.py.
```

The focused module has eleven passing tests.  The growing actual-prime-
power peel, projected-line, nonaffine-witness, and dual-assignment replays
are documented in

```text
results/ZETA23-QP-GROWING-AFFINE-PEEL-AND-PROJECTED-LIFT-FALSIFIER-AFFINE-FALSIFIER-2026-08-29.md
results/verify_zeta23_qp_growing_affine_peel_adversarial_affine_falsifier.py
results/verify_zeta23_qp_projected_neighbor_lift_conflict_affine_falsifier.py.
```

The Pluecker identity is independently certified in

```text
lean/weilcert/QPTangentPluckerInverse.lean.
```
