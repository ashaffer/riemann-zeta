# QP sharp four-cycle: pure-state channel, sharp tangent theorem, and the scattered inverse gate

**Date:** 2026-08-25
**Binary verdict:** the sharp four-cycle estimate is **not proved**.  The best
unconditional project estimate remains

```text
tr((A_z^* A_z)^2) << D^(9/8+o(1)) ||z||_2^4.
```

This attack nevertheless produces four exact advances.

1. The rank-one fourth-trace problem is, with no constant loss, the completely
   positive channel norm `S_1 -> S_2`, equivalently its dual `S_2 -> S_infinity`.
2. The complete multiplicative-tangent sector satisfies the desired
   `D q^o(1)` bound for arbitrary complex coefficients, even on the full
   integer shell.
3. For every residual edge, its two entire physical neighborhoods form a
   Cartesian determinant strip: every missing cross corner has determinant
   `O(D)`, whether or not that corner is itself an edge.
4. In Cramer-token coordinates, two linearly independent anchors give an
   explicit opposite-arm lattice count.  A later content/scale audit shows
   that this count is always at least order `D` in the physical range, so it
   does **not** close a broad token sector at the target scale.

The exact remaining sufficient theorem is an edgewise product bound for two
**scattered physical reciprocal arms**.  Affine/ruling arms are already closed
and literal hard-window examples show that they sharply saturate the target.

## 1. The lossless target

Put

```text
kappa(a,b,c)=1_(|8abc-q^3|<=qD),
A_z(a,b)=sum_c kappa(a,b,c)z_c.
```

For `P_b[a,c]=kappa(a,b,c)`, define

```text
Phi(X)=sum_b P_b X P_b^*.
```

Then, exactly,

```text
A_z A_z^*=Phi(zz^*),
tr((A_z^*A_z)^2)=||Phi(zz^*)||_HS^2.               (1.1)
```

For `u_b=P_bx` and `v_b=P_by`, Gram-matrix Cauchy--Schwarz gives

```text
||Phi(xy^*)||_HS^2
 <=||Phi(xx^*)||_HS ||Phi(yy^*)||_HS.              (1.2)
```

Applying (1.2) termwise to a singular-value decomposition proves, with the
same best constant `K`,

```text
sup_z ||Phi(zz^*)||_HS/||z||_2^2
 =||Phi||_(S1->S2)
 =||Phi^*||_(S2->Sinf).                            (1.3)
```

Thus the sharp target is exactly

```text
||Phi^*(Y)||_op <<sqrt(D)q^o(1)||Y||_HS.           (1.4)
```

This is the correct mask-sensitive vector-valued two-inverse large sieve.  It
is not a center convolution estimate.

## 2. The exact cyclic incidence and the tangent theorem

Cyclically write

```text
T_((b,B),(c,C))
 =sum_a kappa(a,b,c)kappa(a,B,C).                  (2.1)
```

The missing-coordinate interval has width below one, so `T` is a `0/1`
incidence.  For `xi_(c,C)=conj(z_c)z_C`, direct expansion gives

```text
||T xi||_2^2=||A_z||_(S4)^4,
||xi||_2^2=||z||_2^4.                              (2.2)
```

Split an edge by

```text
delta=bc-BC.
```

On the tangent sector `delta=0`, write

```text
b=gu, B=gv, c=vd, C=ud,       gcd(u,v)=1.          (2.3)
```

For fixed reduced ratio and fixed `d`, the remaining condition is

```text
|8guvda-q^3|<=qD.
```

With `M=max(u,v)` and `n=ga`, the allowed interval for `n` has length
`O(D/M)`.  The divisor bound therefore gives column degree

```text
O((1+D/M)q^o(1)).                                  (2.4)
```

An `ell^1` block estimate followed by

```text
sum_(u~M) sum_(d:ud in shell)|z_(ud)|^2
 <=q^o(1)||z||_2^2                                 (2.5)
```

and dyadic summation proves

```text
||T_tan(conj(z) tensor z)||_2^2
 <<Dq^o(1)||z||_2^4.                               (2.6)
```

This includes the full diagonal `b=B,c=C`.  No positivity replacement or
center grouping is used.

## 3. A sharp sufficient theorem for the residual sector

Let `T_res` be the restriction to `delta!=0`, and let `l(p),r(gamma)` be
the two endpoint degrees.  For every finite bipartite graph with biadjacency
matrix `B`,

```text
||B||_(2->2)^2
 <=max_(x~y) deg(x)deg(y).                          (3.1)
```

Consequently the residual degree-product theorem

```text
max_(p~gamma) l(p)r(gamma)<<Dq^o(1)                (RDP)
```

would prove the full residual operator bound, which is stronger than what is
needed on the rank-one tensor `conj(z) tensor z`.

`(RDP)` is not assumed below.  It is the remaining sufficient arithmetic
gate.

## 4. The missing-corner-stable determinant breakthrough

Fix one residual edge, witnessed by

```text
(a,b,c), (a,B,C).
```

Let one left neighbor and one right neighbor be witnessed by

```text
(x,b,d), (x,B,D),
(y,e,c), (y,E,C).
```

Writing the six product errors as, for example,

```text
8xbd=Q+r_bd,       Q=q^3,
```

direct expansion gives the exact identity

```text
(Q+r_bd)(Q+r_ec)(Q+r_BC)
 -(Q+r_BD)(Q+r_EC)(Q+r_bc)
 =512axybBcC(de-DE).                               (4.1)
```

Each error is at most `qD`, while all physical coordinates are comparable
with `q`.  Three-factor telescoping in (4.1) therefore proves

```text
|de-DE|<<D                                          (4.2)
```

for **every Cartesian pair** of opposite neighbors.  The cross edge need not
exist.  If

```text
U={(d,D): left neighbors},
V={(e,E): right neighbors},
F(u,v)=u_1v_1-u_2v_2,
```

then the local residual problem is now

```text
|F(u,v)|<<D for all U x V,
prove |U||V|<<Dq^o(1).                              (4.3)
```

Unlike a bare determinant-strip statement, every point in `U` and `V`
retains its actual reciprocal hard-window row witness `x` or `y`.

## 5. What is already closed inside (4.3)

If one arm is a full affine progression

```text
U={u_0+tp:0<=t<L},
```

then endpoint subtraction gives, for every `v in V`,

```text
(L-1)|F(p,v)|<=2 max_(u,v)|F(u,v)|<<D.             (5.1)
```

For each fixed integer `F(p,v)`, the corresponding `v` lie in one parallel
rank-one ruling.  If every retained ruling fiber has occupancy at most `R`,
then

```text
|U||V|<<R(D+L)<<RD,                                (5.2)
```

because the physical quadratic drift already gives `L<<sqrt(D)`.  Thus the
one-affine/one-ruling-sparse sector proves `(RDP)` when `R=q^o(1)`.

This is sharp.  There are literal all-integer hard-window bicliques
`K_(L,L)` with

```text
D=512L^2,              |U||V|=L^2=D/512,           (5.3)
```

all edges residual.  Their determinant layers are affine diagonals/rulings.
They saturate `(RDP)` but do not violate it.

## 6. Cramer normal form, and why it is not yet the proof

Orient

```text
p=(b,B), q_0=(C,c), u=(D,d), v=(e,E),
delta=det(p,q_0).
```

With

```text
k=det(p,u), r=det(u,q_0), ell=det(v,q_0), t=det(p,v),
```

Cramer's rule and Pluecker give

```text
delta*u=r*p+k*q_0,
delta*v=ell*p+t*q_0,
delta*det(u,v)=rt-k*ell.                            (6.1)
```

All displayed minors are `O(D)`.  This contracts the visible coordinates
from scale `q` to scale `D`, but it is an invertible repackaging: the cross
tolerance becomes `O(|delta|D)`.  Without the reciprocal witnesses, two
families of `D` nearly parallel integer vectors can have all `D^2` cross
determinants of size `O(D)`.

There is an exact two-anchor lattice consequence.  Suppose two left
tokens `(k_1,r_1),(k_2,r_2)` are independent and put

```text
g_1=gcd(k_1,r_1),
Delta_12=|k_1r_2-r_1k_2|,
E=max_(left x right)|rt-kell|.
```

Fixing the cross determinant against the first anchor leaves an integral
line whose primitive step changes the determinant against the second anchor
by exactly `Delta_12/g_1`.  Hence

```text
|V| <=(2 floor(E/g_1)+1)
      (floor(2E g_1/Delta_12)+1).                   (6.2)
```

The symmetric inequality bounds `|U|` from two independent right tokens.
However, primitivity gives `g_1|delta` and
`Delta_12=|delta|*|det(u_1,u_2)|<=|delta|D`.  With
`E<<|delta|D`, the right side of (6.2) is consequently always at least a
constant times `D`.  It supplies no factor `1/|U|` and therefore does not
close any nontrivial arm product at the target scale.  This corrects the
earlier broad-sector interpretation; the inequality itself remains valid.

Two further tempting shortcuts also fail.

* Although both endpoint gcds divide `delta`, a bound
  `degree(g)<<min(g,D/g)q^o(1)` is false.  The physical biclique (5.3) has
  endpoint gcd one and degree `asymp sqrt(D)`.
* The exact Fejer Stinespring lift has no harmonic normalization loss, but
  its carrier integer disappears from the phase modulo one.  A fixed-lattice
  Airy estimate therefore has no automatic Bessel synthesis across all
  carriers/charts.  A completely positive repetition model realizes the
  missing square-root multiplicity.

There is also an exact second-order error ledger.  If

```text
alpha=xd-ac, beta=xD-aC, gamma=ye-ab, eta=yE-aB,
```

then

```text
xy(de-DE)
 =a^2 delta+ab alpha-aB beta+ac gamma-aC eta
  +alpha gamma-beta eta.                            (6.3)
```

Rectangular mixed differences of the weighted left side reduce to a
bilinear error remainder of size `O(D^2)=o(q)`.  This does not force
vanishing: the four terms carry different denominators `x_i y_j`, hence no
common `q`-scale divisor.  A literal prime-scale six-window fixture at
`q=809,D=26` has mixed remainder `56`.  It is not an `(RDP)` counterexample;
it decisively rules out the automatic-divisibility shortcut.

## 7. The exact theorem still missing

The surviving statement is a bilinear Freiman/ruling inverse theorem with
physical curvature:

> Let `U` and `V` be the two reciprocal hard-window arms around one residual
> edge.  If `|F(u,v)|<<D` for all `U x V` and `|U||V|` is larger than
> `Dq^o(1)`, then a power-sized fraction of one arm lies in a parallel
> rank-one/affine ruling.  After that ruling is merged, the same assertion
> iterates on the remainder.

The lattice estimate (6.2) does not supply the transverse half of this
dichotomy after the physical content factors are inserted.  Both the
scattered/generic aggregation and the approximately-collinear packet
packing therefore require separate input.

Equivalently, prove `(RDP)` directly.  An alternative analytic closure is

```text
||Phi_res^*(Y)||_op
 <<sqrt(D)q^o(1)||Y||_HS.                           (7.1)
```

The recent line-concentration philosophy for additive energy on algebraic
surfaces is closely aligned with this inverse object, but those theorems do
not directly retain the two reciprocal row witnesses or the hard product
mask.  Rational-point theorems for nonzero-torsion space curves likewise do
not directly apply to the planar reciprocal curve here.  Importing either
result without a new physical intertwining lemma would leave the main gap
unchanged.

## 8. Verification and calibrated status

Exact identities, finite hostile models, and numerical hard-window scans are
implemented in

```text
src/qp_pure_state_channel.py
src/qp_rank_one_h_tangent_residual.py
src/qp_tangent_plucker_inverse.py
src/qp_simultaneous_divisor_rdp.py
```

with focused tests in the matching `test_*.py` files.  Lean independently
checks the polynomial identities in

```text
lean/weilcert/QPPureStateChannel.lean
lean/weilcert/QPRankOneHTangentResidual.lean
lean/weilcert/QPTangentPluckerInverse.lean
lean/weilcert/QPSimultaneousDivisorRDP.lean
```

The prover certificates deliberately do not assert the open asymptotic
inverse theorem.

The final focused replay ran `85` Python tests and all seven relevant Lean
files successfully; the touched artifacts pass whitespace/diff checks.

```text
pure-state/channel norm equivalence:                   PROVED;
complete tangent-sector sharp bound:                   PROVED;
residual edge-degree criterion implies sharp bound:    PROVED;
six-window Cartesian determinant strip:                PROVED;
two-anchor token lattice inequality:                    PROVED;
two-anchor inequality closes a broad physical sector:   FALSE AFTER SCALE AUDIT;
mixed-error O(D^2) remainder automatically vanishes:    FALSE;
one-affine/one-ruling-sparse residual sector:           PROVED;
affine hard-window saturation at constant*D:            CONSTRUCTED;
determinant strip without physical witnesses:           INSUFFICIENT;
fixed-lattice Airy automatically aggregates globally:  FALSE ABSTRACTLY;
two-scattered physical inverse theorem:                 OPEN;
complete sharp four-cycle estimate:                     NOT PROVED;
best unconditional exponent:                            9/8.
```

Subjective probabilities after this attack are roughly: `90%` that the
sharp bound is true, `60%` that the strong integer-shell `(RDP)` itself is
true, and `45%` that a quantitative ruling-extraction theorem closes the
actual prime-power problem without a second major idea.  These are research
priors, not mathematical conclusions.
