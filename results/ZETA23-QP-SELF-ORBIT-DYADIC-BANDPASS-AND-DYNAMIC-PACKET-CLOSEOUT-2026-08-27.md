# QP self-orbit dyadic bandpass and dynamic-packet closeout

**Date:** 2026-08-27  
**Verdict:** the scale-correct dyadic reciprocal large sieve is compatible
with the coherent adjacent orbit and would prove the total-edge theorem,
hence the sharp four-cycle bound.  A new exact local theorem proves that at
every active dyadic scale, each connected cluster of the actual self-orbit
mask is one affine packet whose direction is a principal continued-fraction
convergent of the anchor slope.

This completes the geometric half of the proposed packet inverse theorem.
There is also an important legal simplification: positivity permits enlarging
the actual prime-power vertices and carrier rows to the complete integer
self-orbit *before* Fourier expansion.  The old global large-sieve target
failed on that enlargement, but the scale-correct dyadic target below does
not.  Thus the remaining theorem need not survive arbitrary prime-mask
holes; it may use the canonical all-one Beatty/continued-fraction orbit.

This still does **not** complete the analytic half.  The two reciprocal
charts are rank one at Selberg resolution, distinct translated affine
packets can have identical phases, and positive near-collision counting
loses a power.  Exact reciprocal aliases are divisor-rigid and harmless;
what remains is a signed, mean-zero discrepancy theorem in moving
neighborhoods of Möbius translates.  That theorem is presently open.  The
sharp four-cycle bound is not proved.

## 1. The corrected theorem that would close the argument

Let `beta_t` be the indicator of the **complete integer** physical
self-orbit with `|t|<=D`.  This is a legal enlargement of the actual
prime-power vertex mask, and it still has `sum beta_t<<D`.  Put

```text
T=q^3/8,
S_gamma(h)=sum_(t,j) beta_t beta_j
             e(h*T/(b_t*B_j)),
L_0=q/D^2,                 H=q/D.                  (1.1)
```

More explicitly, enlarge both endpoint vertex sets from the actual nodes to
all integer shell nodes and enlarge the carrier row set in the same way.
Every old hard-window edge remains, so positivity gives

```text
E_actual<=E_full-integer.                          (1.1a)
```

Dropping one of the two hard windows can only enlarge this full-integer
count again.  The Selberg majorant is applied only after these two monotone
steps.  This is why `(DRPLS)` below is needed only for the canonical
full-integer orbit rather than uniformly for arbitrary deleted masks.

The right scale-sensitive target is

```text
sum_(K<h<=2K)|S_gamma(h)|^2
 <<(q^2/K)q^o(1),          L_0<=K<=H.              (DRPLS)
```

This differs decisively from the false global target
`sum_(h<=H)|S(h)|^2<<qD`.  On one dyadic block, Cauchy gives

```text
sum_(K<h<=2K)|S_gamma(h)|
 <=sqrt(K)*sqrt(q^2/K)*q^o(1)
 =q*q^o(1).                                       (1.2)
```

For `1<=h<=L_0`, the trivial bound `|S(h)|<=D^2` gives the same
`ell^1` output:

```text
sum_(h<=L_0)|S(h)|<=L_0*D^2=q.                     (1.3)
```

The one-window Selberg reduction is

```text
E_gamma
 <<D^3/q+(D/q)sum_(1<=|h|<=H)|S_gamma(h)|.         (1.4)
```

There are `O(log q)=q^o(1)` dyadic blocks, so `(DRPLS)` and
`(1.2)--(1.4)` give

```text
E_gamma<<D*q^o(1).                                 (1.5)
```

Since the rooted self-orbit degree sum is at most `E_gamma`, this proves
NDS and the sharp four-cycle bound.  The constant Fourier mode is

```text
D^3/q=D^(15/16+o(1)),                              (1.6)
```

strictly below budget.

The normalization is sharp.  At frequency `K`, write

```text
R_K=sqrt(q/K).                                      (1.7)
```

A coherent `R_K` by `R_K` packet has `|S(h)|` of order `R_K^2`, and hence

```text
K*R_K^4=q^2/K.                                     (1.8)
```

Thus coherent packets saturate `(DRPLS)` instead of refuting it.  In the
active range,

```text
sqrt(D)<=R_K<=D.                                   (1.9)
```

## 2. New theorem: every dynamic cluster is an exact affine CF packet

Let the primitive anchor be `gamma=(c,C)` and label a physical self-orbit
vertex `v_i=(b_i,B_i)` by

```text
t_i=c*b_i-C*B_i,                 |t_i|<=D.          (2.1)
```

Direct elimination gives the exact identity

```text
C*det(v_2-v_1,v_3-v_1)
 =(t_2-t_1)(b_3-b_1)-(b_2-b_1)(t_3-t_1).          (2.2)
```

If the first-coordinate diameter of the three points is at most `R`, then

```text
|C*det(v_2-v_1,v_3-v_1)|<=4D*R.                   (2.3)
```

The determinant is integral.  Therefore `4DR<C` forces the three points
to be exactly collinear.

Join two selected vertices when their sup-norm distance is at most `R`.
Every length-two path has first-coordinate diameter at most `2R`.  Applying
`(2.3)` along paths proves:

> **Dynamic affine-packet theorem.**  If `8DR<C`, every connected component
> of the radius-`R` self-orbit graph lies on one exact affine lattice line.

This is hereditary under arbitrary deletion, so its geometric conclusion
retains the actual prime-power mask.  At `R=R_K<=D`, its asymptotic margin
is

```text
q/(D*R_K)>=q/D^2=q^(1/33+o(1)).                   (2.4)
```

There is also an exact direction theorem.  Write a close difference as

```text
v'-v=g*(p,P),       gcd(p,P)=1,       P>0,
r=c*p-C*P=(t'-t)/g.                                 (2.5)
```

Then

```text
|r|<=2D/g,                   |P|<=R/g.              (2.6)
```

If `4DR<c`,

```text
|C/c-p/P|=|r|/(c*P)<1/(2P^2).                      (2.7)
```

Legendre's criterion makes `p/P` a principal continued-fraction convergent
of `C/c`.  Hence only `O(log q)` dynamic directions occur.  On one such
line the labels advance by the nonzero integer `r`, so

```text
#(one line)<=1+floor(2D/|r|).                      (2.8)
```

A global translate refinement is also available.  Suppose all physical
vertices lie in a box of sup-diameter `W`, put `M=max(c,C)`, and assume

```text
W+2DR<M.                                           (2.9)
```

For a fixed realized primitive direction `(p,P)`, all vertices with the
same label modulo `|r|` lie on one translate of that line.  Indeed, if
`t-s=kr`, then

```text
(v_t-v_s)-k*(p,P)=n*(C,c)                          (2.10)
```

for an integer `n`; `(2.9)` forces `n=0`.  Thus this direction supports at
most `|r|` parallel lines, each satisfying `(2.8)`.  This sharp
line-number/line-length tradeoff still does not prove Fourier orthogonality
between the translates.

The analytic one-fan `B`-process previously proved in the project assumes
a contiguous all-one affine interval.  It is not hereditary under prime
deletion, but the positive full-integer enlargement in Section 1 removes
that problem.  On the complete integer orbit, the intersection of one
affine lattice line with the shell and label interval is a contiguous
all-one interval, so the one-fan estimate applies to each individual line
pair.  What remains is lossless aggregation across the many translated
line pairs; absolute summation still pays a power.

## 3. The two inverse charts collapse to one resolution cell

For one ordered pair put

```text
n_(t,j)=b_t*B_j,       m_(t,j)=B_t*b_j,
kappa_(t,j)=n_(t,j)-m_(t,j).                       (3.1)
```

The orbit labels give exactly

```text
C*kappa_(t,j)=t*b_j-j*b_t.                         (3.2)
```

On the project shell this implies

```text
|kappa_(t,j)|<=2e^0.4 D,
|T/n_(t,j)-T/m_(t,j)|<=4e^1.2 D/q.                 (3.3)
```

Consequently two simultaneous reciprocal collisions have the same nearest
integer shift once their total error plus `8e^1.2D/q` is below one.  A
`1/K` collision in the first chart automatically produces a constant
multiple `1/K` collision in the second throughout the whole active range.

This gives no extra dimension.  The product-space uncertainty is

```text
q/K in [D,D^2],                                    (3.4)
```

while `|n-m|=O(D)`.  Thus the second condition is contained in the first
condition's uncertainty.  Transverse leverage would require `q/K=o(D)`,
or `K>>q/D`, outside the Selberg band.  Moreover

```text
theta_2(t,j)=theta_1(j,t),                          (3.5)
```

so the two Fourier sums are identical for the symmetric coefficient mask
`beta_t beta_j`.  The common-shift lemma is true, but it does not improve
`(DRPLS)`.

## 4. Exact aliases are rigid and harmless

Group the reciprocal sum by its integer product:

```text
c(n)=#{(t,j):b_t*B_j=n},
S(h)=sum_n c(n)e(h*T/n).                            (4.1)
```

Injectivity of each orbit coordinate and the divisor bound give

```text
c(n)<=tau(n)=q^o(1),
sum_n c(n)^2<=D^2*q^o(1).                          (4.2)
```

Hence the exact product diagonal costs

```text
K*sum_n c(n)^2
 <<K*D^2*q^o(1)
 <=(q^2/K)q^o(1),                                  (4.3)
```

because `K<=q/D`.

Even exact *nonzero* reciprocal aliases are divisor-rigid.  If `n!=n'`
and

```text
T*(1/n-1/n')=r in Z,                               (4.4)
```

write `n=g*a`, `n'=g*b`, `(a,b)=1`.  Clearing denominators gives

```text
q^3*(b-a)=8*r*g*a*b.                               (4.5)
```

It follows that `a|q^3`, `b|q^3`, and `ab|q^3`.  With
`c_0=q^3/(ab)`,

```text
c_0*(b-a)=8*r*g,                                   (4.6)
```

so `g|c_0(b-a)`.  Standard divisor bounds leave only `q^o(1)` exact
product pairs and `q^o(1)` orbit realizations.  Exact aliases are not the
missing mass.

They do refute a naive geometric Cotlar assertion.  At

```text
q=100000, D=265, gamma=(50000,50007),               (4.7)
```

one full-integer orbit contains

```text
P_-195=(42891,42885),       P_-232=(57184,57176),
P_-260=(57188,57180),       P_-174=(42888,42882),
```

with the two exact identities

```text
42891*57176=57188*42882=2452335816,
42885*57184=57180*42888=2452335840.                (4.8)
```

The ordered pairs are non-tangent, lie in distinct far-separated cells,
and have identical phases in both reciprocal charts.  This particular
content-swap alias is nonprimitive and is absent from the actual
prime-power mask; `(4.2)--(4.6)` show why exact aliases are harmless even
before making that deletion.  It nevertheless proves that distinct packet
locations alone do not imply pairwise phase decay.

## 5. The exact remaining signed Möbius discrepancy

Let `W` be smooth and supported in `1<=|u|<=2`.  Poisson summation gives

```text
M_W(K)=sum_h W(h/K)|S(h)|^2
 =K sum_(n,n')c(n)c(n') sum_(r in Z)
   W_hat(K*(r-T*(1/n-1/n'))).                      (5.1)
```

Because `W(0)=0`,

```text
integral W_hat=W(0)=0.                             (5.2)
```

That mean-zero sign is indispensable.  A positive close-pair majorant sees
at least `D^4/K` pairs by pigeonhole and is polynomially too large near the
top of the band.

For `r=0`, Schwartz localization reduces to

```text
|n-n'|<<q/K.                                       (5.3)
```

Since `q/K<=D^2=o(q)`, fixing three of the four shell factors determines at
most one fourth factor.  Thus this single slice has at most `D^3q^o(1)`
near pairs and is within budget when `q/K>=D^(3/2)`.  This is not a partial
`(DRPLS)` theorem, because all `r!=0` slices remain.

For a general integer shift define

```text
F_r(n)=q^3*n/(q^3-8*r*n).                          (5.4)
```

There is the exact normal form

```text
T*(1/n-1/n')-r
 =[(q^3-8*r*n)*(n'-F_r(n))]/(8*n*n').              (5.5)
```

Therefore the first genuinely sufficient new theorem is

```text
sum_r sum_(n!=n') c(n)c(n')
 W_hat(-K*(q^3-8*r*n)*(n'-F_r(n))/(8*n*n'))
 <<(q/K)^2*q^o(1).                                 (MSPD)
```

Multiplying `(MSPD)` by `K` gives `q^2/K`.  Exact-alias rigidity controls
only the centers `n'=F_r(n)`.  It gives no discrepancy estimate in their
moving neighborhoods of width `q/K`.  Summation by parts would already
need precisely this canonical-orbit product discrepancy.

Equivalently, after the dynamic packet decomposition, one needs a
canonical-orbit translate Bessel theorem and packet square-sum theorem.  If

```text
S_(lambda,mu)(h)
 =sum_(i in P_lambda,j in P_mu)
   beta_i beta_j e(h*T/(b_i*B_j)),                  (5.6)
```

the two sufficient estimates are

```text
sum_(h~K)|sum_(lambda,mu)S_(lambda,mu)(h)|^2
 <<q^o(1) sum_(lambda,mu)sum_(h~K)|S_(lambda,mu)(h)|^2,  (TB)

sum_(lambda,mu)sum_(h~K)|S_(lambda,mu)(h)|^2
 <<(q^2/K)q^o(1).                                      (PS)
```

Here `beta` is the fixed complete-integer orbit indicator, not an arbitrary
coefficient mask.  Neither `(TB)` nor `(PS)` follows from the local
affine/continued-fraction classification, and neither is proved.

There is one further rigorous reduction inside `(PS)`.  Choose an integer
vector `V` with `det(U,V)=1` and write

```text
(C,c)=a*U+r*V,              gcd(a,r)=1.             (5.7)
```

For an orbit point `z=nU+sV`, its label and physical coordinates obey

```text
t=r*n-a*s,
r*b=p*t+C*s,               r*B=P*t+c*s.            (5.8)
```

Thus `t mod r` indexes the parallel lines exactly.  Fourier transform in
these residues is only an auxiliary Parseval isometry: the physical sum is
its single untwisted mode, and the reciprocal kernel in `(5.8)` is not a
character or a circulant kernel.  Quotient Parseval therefore does not prove
`(TB)`.

Nevertheless, fix one direction family, subdivide each of its lines into
physical diameter-`R=R_K` blocks, and put `u=||U||_infinity`.  The maximum
block size satisfies

```text
M<=1+min(2D/|r|,R/u).                              (5.9)
```

Since this family has at most `O(D)` points, trivial summation gives for its
self-pair packet square sum, up to fixed endpoint constants,

```text
PS<=K*(M*D)^2.                                     (5.10)
```

As `q=K*R^2`, `(5.10)` is within `q^2/K=K*R^4` whenever

```text
|r| >= constant*D^2/R^2
or
u >= constant*D/R.                                 (5.11)
```

For two different direction families `U,V`, the corresponding bound is
`K*M_U*N_U*M_V*N_V`; in particular their cross packet-square sum closes by
the same argument when **both** block caps are at most `R^2/D`.  Therefore
every interaction between two large-remainder/large-step families is
removed.  Every surviving interaction has at least one direction in the
small-remainder/small-step sector

```text
|r| <<D^2/R^2,                 ||U||_infinity<<D/R. (5.12)
```

At the bottom dyadic scale this collapses to the bounded adjacent-direction
packet; at the top it expands to the full critical CF range.  Interactions
of two such hard directions are the worst residual case.  Formula `(5.12)`
is a genuine pruning of packet parameter space, not a proof of the remaining
twisted-tower Bessel estimate.

## 6. Binary status

```text
DRPLS is the correct scale-sensitive sufficient theorem:  PROVED;
DRPLS implies total edges, NDS, and sharp four-cycle:      PROVED;
coherent adjacent orbit refutes DRPLS:                    NO (SATURATES);
dynamic radius component is one exact affine packet:     PROVED;
dynamic packet directions are CF convergents:             PROVED;
number of dynamic directions:                             O(log q), PROVED;
line count/line capacity tradeoff:                        PROVED;
easy/easy large-remainder or large-step PS interactions:  PROVED;
small-remainder/small-step twisted-tower sector:           OPEN;
full-integer enlargement is legal for total edges:        PROVED;
full-orbit line pieces are contiguous all-one intervals:  PROVED;
common-shift two-inverse lemma:                           PROVED;
common shift supplies an independent sieve dimension:    NO;
exact product and reciprocal aliases:                    CONTROLLED;
coefficient-blind cross-cell Cotlar decay:                FALSE;
signed Möbius-shifted product discrepancy (MSPD):         OPEN;
translate Bessel / packet square sum (TB)/(PS):           OPEN;
DRPLS:                                                    OPEN;
total self-orbit edge theorem:                            OPEN;
best unconditional global four-cycle exponent:           9/8 (UNCHANGED);
sharp four-cycle bound:                                  NOT PROVED.
```

Exact algebra and exponent arithmetic are machine-checked in

```text
lean/weilcert/QPSelfOrbitDyadicPacket.lean
src/qp_self_orbit_dyadic_packet.py
src/test_qp_self_orbit_dyadic_packet.py
```

The dynamic packet decomposition and finite translate fixtures are in

```text
src/qp_self_orbit_dynamic_packets.py
src/test_qp_self_orbit_dynamic_packets.py
```
