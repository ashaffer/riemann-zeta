# QP carrier: primitive `q^2` ray polar and ordered-matching stability gate

**Date:** 2026-08-24  
**Verdict:** the full two-copy `q^2` packet expansion has an exact
mask-preserving relative-trace factorization.  Its diagonal fibre is a
positive, coefficient-dependent multiplicative-ray/Hankel polar, output
centering removes exactly one degree rank-one term, and the remaining fibre
is an explicit transverse operator.  This does **not** prove the sharp
`D`-scale vector square theorem.

There are two exact hostile conclusions.

1. The primitive ray coefficient is the centered quotient count

   ```text
   Gamma_*(t)=N_(q^2)(t)/q^2-4D^2(q-1)/q^3.             (0.1)
   ```

   Every actual pair of edges sharing a carrier already has a quotient-ray
   witness.  Thus ray **support** does not separate tangent from transverse;
   only the excess in (0.1) can do so.
2. Short residual blocks are triangle matchings, and distinct ordered blocks
   cannot cover exactly the same vertex multiset.  But this qualitative
   obstruction has no uniform spectral gap: two triangle matchings can have
   normalized projection overlap `1-O(1/N)` while differing at only one
   boundary incidence.

The one surviving theorem is therefore an arithmetic zero-frequency
restriction for the ordered family of residual matchings, equivalently a
centered estimate for the off-diagonal fibre below.

## 1. Exact coarse lift and the full two-copy expansion

Put

```text
Q=q^2,
R={r mod Q:0<|r|<=qD, q does not divide r},
f=1_R,
beta_h=Q^(-1) sum_(r in R)e_Q(-h r).                    (1.1)
```

Let `W` be the exact coarse plateau from the conductor-lowering report and
write

```text
X_(a,b,c)=8abc-q^3,
C_h(b,c)=sum_a W(X_(a,b,c)/Q)e_Q(h X_(a,b,c)).          (1.2)
```

Since the support of `W` contains at most one lift of `R`, Fourier inversion
gives the literal physical matrix

```text
T=sum_(h mod Q) beta_h C_h.                             (1.3)
```

Expanding both copies of (1.3) and summing the frequencies before making an
inequality gives

```text
(T^*T)_(c,c')
 =sum_(b,a,a') W(X_(a,b,c)/Q)W(X_(a',b,c')/Q)
    1_R(X_(a,b,c))1_R(X_(a',b,c')).                    (1.4)
```

Thus the full cross-Gram is exactly the common-carrier Gram of the hard
physical mask.  The favorable scalar packet budget is not lost; rather, it
is insufficient to control the synthesis at the selected carriers.

The additive conditional expectation onto residue classes modulo `q` is

```text
E_1 f(x)=(2D/q)1_((x,q)=1).                            (1.5)
```

Consequently, on the physical unit support,

```text
T=T_0+T_*,
T_0=(2D/q)C_0,
T_*=sum_(q does not divide h) alpha_h C_h,
alpha_h=beta_h.                                        (1.6)
```

This is the exact principal/primitive split.  It is not orthogonal after
restriction to the physical carrier set, so cross terms must not be bounded
packetwise.

### 1.1 The missing Archimedean polar is visible in log coordinates

For a shell node put

```text
x_p=log(2p/q).                                         (1.7)
```

If `tau={a,b,c}` is an accepted all-distinct triple with residual `rho_tau`,
then

```text
s_tau:=x_a+x_b+x_c
      =log(8abc/q^3)
      =log(1+rho_tau/q^3),
|s_tau|<=2D/q^2.                                      (1.8)
```

Let `A_tau` be the adjacency of its triangle.  There are two exact
identities:

```text
A_tau x=s_tau 1_tau-x_tau,                            (1.9)
x^*A_tau x=s_tau^2-(x_a^2+x_b^2+x_c^2).              (1.10)
```

Equivalently, if `E_tau` projects onto constants on the triangle and
`F_tau=I_tau-E_tau`, then

```text
A_tau=2E_tau-F_tau,                                   (1.11)
E_tau x=(s_tau/3)1_tau.                               (1.12)
```

Thus `x` is almost entirely in the local eigenvalue `-1` channel on every
physical triangle.  Globally, if `r_p` is the triangle degree and

```text
g_p=sum_(tau contains p)s_tau,
```

then

```text
T x=g-diag(r_p)x,                                     (1.13)
x^*T x=sum_tau s_tau^2-sum_p r_p x_p^2.              (1.14)
```

This is an explicit Archimedean/Hankel--Eisenstein polar missed by constant
centering.  If the unweighted degrees have their expected nearly regular
size `D/(log q)^2`, (1.14) predicts a negative mode much larger than
`sqrt(D)`.  That asymptotic degree statement is not proved here, so (1.14)
is not an actual-prime counterexample.  It does show that the stronger
unweighted carrier norm should not be the final FC target with only the
constant removed.

### 1.2 The full coarse principal operator absorbs this polar in weighted FC

For the actual weighted four-cycle matrix define

```text
A_(z,0)(a,b)
 =(2D/q)sum_c z_c W((8abc-q^3)/q^2).                  (1.15)
```

Assume `||W||_infinity<=C_W` and `W` is supported in `|X|<q^2/2`, as in
the exact coarse lift.  If

```text
p_0=min S>q e^(-.2)/2,
```

then fixing any two variables leaves an interval for the third of length

```text
q^2/(8p_0^2)<e^.4/2<1.                               (1.16)
```

Hence every fixed-`c` coarse layer has at most one entry in each row and
column and at most `|S|` entries, while every matrix cell belongs to at most
one `c` layer.  If `M=|supp z|`, exact Hilbert--Schmidt and Schur estimates
give

```text
||A_(z,0)||_HS^2
 <=4C_W^2 D^2 |S|/q^2 ||z||_2^2,                     (1.17)

||A_(z,0)||_op^2
 <=4C_W^2 D^2 M/q^2 ||z||_2^2.                       (1.18)
```

Therefore

```text
||A_(z,0)||_S4^4
 <=16C_W^4 D^4 |S|M/q^4 ||z||_2^4
 <=16C_W^4 D^4/q^2 ||z||_2^4.                        (1.19)
```

At `D=q^(16/33)`, the last factor is `q^(-2/33)`.  Thus the entire coarse
principal operator--including the log mode and its higher smooth
companions--is harmless for weighted FC, even though it need not be small
as an **unweighted** carrier operator.  Schatten triangle inequality permits
it to be removed before attacking the primitive cross-Gram.  This is the
correct nonvacuous interpretation of the coefficient-dependent polar.

## 2. Exact primitive relative trace

Let `U=(Z/QZ)^*`.  Define a ray lift from colour space to
`ell^2(S_b x U)` by

```text
(H z)(b,u)
 =sum_(a,c,h in U: h a c=u mod Q)
    alpha_h W(X_(a,b,c)/Q) z_c,                        (2.1)
```

and define fibrewise Fourier evaluation by

```text
(E F)(b)=sum_(u in U)e_Q(8bu)F(b,u).                   (2.2)
```

### Theorem 1 (exact mask-preserving factorization)

```text
T_*=E H.                                               (2.3)
```

On each carrier fibre,

```text
(E^*E)_b(u,v)=e_Q(8b(v-u))
             =1_(u=v)+K_b^off(u,v).                   (2.4)
```

Let `P_b` and `P_c` remove constants in the two physical copies, and put

```text
delta_*=P_c T_*^* 1_b.                                (2.5)
```

Then

```text
(P_b T_* P_c)^*(P_b T_* P_c)
 =P_c H^*H P_c
  +P_c H^*K^off H P_c
  -delta_* delta_*^*/|S_b|.                           (2.6)
```

**Proof.**  Equation (2.3) follows by inserting `u=hac` in (2.2).  If
`e_b=|S_b|^(-1/2)1_b`, then

```text
E^*P_bE=I+K^off-(E^*e_b)(E^*e_b)^*.                   (2.7)
```

Conjugating (2.7) by `H`, and observing that
`P_cH^*E^*e_b=delta_*/sqrt(|S_b|)`, proves (2.6). `square`

Thus (2.6) is precisely the requested degree + coefficient-dependent polar
+ transverse decomposition.  The first term is positive.  The last term is
the exact empirical degree correction, not a modeled main term.

## 3. The ray polar is an exact centered quotient correlation

For `t in U`, define

```text
N_m(t)=#{(r,s) in R^2:r=t s mod m}.                    (3.1)
```

The kernel in the positive term of (2.6) is

```text
Gamma_*(t)
 =sum_(h in U) conjugate(alpha_h)alpha_(th).           (3.2)
```

### Theorem 2 (primitive-ray autocorrelation)

Uniformly for every `t in U`,

```text
Gamma_*(t)=N_Q(t)/q^2-N_q(t)/q^3
          =N_Q(t)/q^2-4D^2(q-1)/q^3.                  (3.3)
```

For the full additive frequency set,

```text
Gamma_all(t)=N_Q(t)/q^2.                               (3.4)
```

Hence the conductor-at-most-`q` part is the
ratio-independent baseline

```text
Gamma_<=q(t)=4D^2(q-1)/q^3.                            (3.5)
```

**Proof.**  Expanding (3.2) gives

```text
Gamma_*(t)
 =q^(-4) sum_(r,s in R)c_(q^2)(r-ts).                 (3.6)
```

For prime `q`,

```text
c_(q^2)(n)=q(q-1) if q^2|n,
            -q       if q|n but q^2 does not divide n,
             0       otherwise.                       (3.7)
```

This yields the first equality in (3.3).  Every nonzero residue class
modulo `q` has exactly `2D` representatives in `R`, so

```text
N_q(t)=(q-1)(2D)^2.                                   (3.8)
```

Full additive orthogonality gives (3.4), and subtraction gives (3.5).
`square`

In particular,

```text
Gamma_*(1)
 =2D(q-1)/q^2-4D^2(q-1)/q^3
 =sum_(h in U)|alpha_h|^2 asymp D/q.                  (3.9)
```

The physical pullback of (3.2) is

```text
(H^*H)_(c,c')
 =sum_(b,a,a') W_(a,b,c)W_(a',b,c')
   Gamma_*(a c (a'c')^(-1)).                          (3.10)
```

This is a positive multiplicative Hankel/Farey-ray Gram.  Formula (3.3)
shows exactly what its principal subtraction removes: the uniform quotient
density, not merely the single constant frequency.

The log identities (1.8)--(1.14) explain why this subtraction must be the
full coarse operator rather than the physical constant vector alone.  On
the coarse window one still has `x_a+x_b+x_c=O(1/q)`, so the same local
negative eigenspaces occur in `T_0` with precisely the density needed to
remove their mean contribution.

## 4. Hostile support audit: every physical pair is already on a ray

Take two fine edges sharing `b`, and write

```text
rho=8b a c-q^3,             sigma=8b a'c'-q^3.         (4.1)
```

Then the exact integer identity is

```text
rho a'c'-sigma a c=q^3(a c-a'c').                     (4.2)
```

Therefore

```text
rho a'c'=sigma a c mod q^2,                           (4.3)
```

and `(rho,sigma)` is a witness counted by
`N_Q(ac(a'c')^(-1))`.  This holds for every actual common-carrier pair,
including broad non-tangent pairs.

Consequently the proposed dichotomy

```text
quotient-ray support = tangent polar,
no quotient-ray witness = transverse
```

is false.  The only potentially selective object is the **centered excess**
`N_Q(t)-4D^2(q-1)/q`.  Proving that the pullback of this excess is exhausted
by the already controlled affine/Hankel charts is itself a new incidence
theorem.

## 5. The physical ordered-matching relative trace

There is a second, completely physical factorization.  On the all-distinct
sector partition the actual residual interval into half-open blocks of
length `q`.  Since the smallest shell node `p_0` satisfies `q<8p_0`, every
block is a vertex-disjoint triple matching.  Let `A_v` be its triangle
adjacency, let `P` remove constants, and put

```text
B_v=P A_v P,                  B=sum_v B_v=PTP.         (5.1)
```

Every `A_v` is a direct sum of `K_3` adjacencies, so `||B_v||<=2`.  With
`V=O(D)` occupied-or-empty positions, one has the exact relative trace

```text
B^2=Q_diag+R_cross,
Q_diag=sum_v B_v^2,
R_cross=sum_(v!=w)B_vB_w,                              (5.2)

||Q_diag||<=4V<<D.                                    (5.3)
```

Fill the residual-index interval with zero blocks and take its unitary
discrete Fourier transform

```text
Bhat_l=V^(-1/2)sum_v e_V(-lv)B_v.                      (5.4)
```

Operator Parseval is exact:

```text
sum_l Bhat_l^*Bhat_l=sum_v B_v^2=Q_diag,               (5.5)
B=sqrt(V) Bhat_0.                                      (5.6)
```

The desired `D`-scale theorem is therefore equivalent, up to the already
controlled term (5.3), to either of the following:

```text
||R_cross||<<D q^o(1),                                (5.7)

||Bhat_0||^2<<q^o(1).                                 (5.8)
```

Equation (5.5) alone only gives `||Bhat_0||^2<<D`.  Thus the exact missing
gain is a factor `V asymp D` at the single physical zero frequency.  This is
the ordered residual-matching form of the two-inverse BDH theorem.

Projecting only the two global vectors `1,x` is not an automatic repair.
The literal prime-power fixture at `q=4751` has two residual blocks with

```text
||P_1 A_v P_1 A_w P_1||=2.29184...,
||P_(1,x) A_v P_(1,x) A_w P_(1,x)||=2.29066...,        (5.9)
```

where the unprojected branching norm is `sqrt(6)`.  Thus the log direction
is a real family-level polar, but removing its two-dimensional first jet
does not suppress the primitive branching cross-Gram.  The weighted bound
(1.19) removes the whole coarse synthesis; the residual still needs
(5.7)/(5.8).

## 6. Exact common-support obstruction and its stability failure

Suppose matchings in two strictly ordered residual blocks cover exactly the
same vertex multiset `U`.  Multiplying the triple products in either
matching gives

```text
product_(p in U)p.                                     (6.1)
```

But every triple product in the later block is larger than every triple
product in the earlier block.  Their geometric means cannot be equal.
Hence identical covered multisets, even on a closed subfamily of triangles,
are impossible across distinct blocks.

This removes the exact parallel-class equality mode, but not its stable
approximations.  Let `E_v,E_w` be the orthogonal projections onto functions
constant on each triangle of two matchings.  If `M_(v,w)` is the bipartite
intersection matrix of their triangles, then linearity gives

```text
M_(v,w)(e,f)=1 if e and f share a vertex, else 0,
||E_vE_w||=||M_(v,w)||/3.                              (6.2)
```

An exact norm-one component is a closed 3-regular common-cover component
and is forbidden by (6.1).  There is nevertheless no uniform gap.  Take

```text
M_N=I+S+S^2-E_(0,0),                                  (6.3)
```

where `S` is the cyclic shift.  It is connected, has one missing incidence,
has no 3-regular component, and is realizable as the intersection graph of
two triangle matchings after private boundary vertices are added.  Yet

```text
||M_N||/3 >=(3N-1)/(3N)=1-1/(3N).                     (6.4)
```

The product identity does yield a sharp one-boundary necessary condition.
If two ordered `k`-triangle blocks differ by only one shell vertex on each
side, with shell maximum `U`, then

```text
(U+1)/U <=((q^2+D)/(q^2-D))^k,                        (6.5)
```

so `k` must be at least of order `q/D`.  This does not supply the required
aggregate spectral gap, and two or more boundary ratios return to the
short-product/determinant-spacing problem.  Thus exact product conservation
rules out perfect saturation but does not prove a power-saving stability
theorem.

## 7. Audit of the withdrawn Dong--Robles--Zeindler estimate

The current arXiv record for Dong--Robles--Zeindler,
*Bilinear forms with Kloosterman fractions and applications*, is
[withdrawn](https://arxiv.org/abs/2601.00292).  The authors state that a
missing factor `L^2` in their equation (2.53) changes `L^5` to `L^7`, so
the argument no longer gives the claimed improvement.  Therefore its
Theorems 1.4/1.6 cannot be used as input.

It is still useful to perform the exact counterfactual parameter audit.
The v1 form was

```text
B_(a,b)(M,N)
 =sum_(m~M,n~N,(m,n)=1) alpha_m beta_n e(a mbar/(bn)),

|B_(a,b)|
 <<||alpha||_2||beta||_2 (a+bMN)^(1/4)(M+N)^(1/6)
      min(M,N)^(1/3) max(M,N)^(-1/12)(MN)^epsilon.     (7.1)
```

### 7.1 Fixed residual inversion is necessarily unbalanced

After Fourier expansion in the target of the physical inverse
permutation, a fixed-modulus layer has the form

```text
sum_(|x|<=D) F(x)e_q(t lambda xbar).                   (7.2)
```

In (7.1), the inverse is taken modulo `bn`.  Keeping the QP modulus equal
to the prime `q` forces `bn=q`; hence the `n` variable is a singleton
(`n=q,b=1`, or the transposed endpoint).  There is no balanced
`M=N=D` substitution.  The most optimistic formal choice is

```text
M=D, N=q, a<=q,
factor in (7.1) = q^(1/3)D^(7/12).                    (7.3)
```

For `D=q^(16/33)`, (7.3) is `q^(61/99)`.  Relative to the *dense*
Cauchy factor `(qD)^(1/2)=q^(49/66)`, this looks like the saving

```text
q^(-25/198).                                          (7.4)
```

But (7.2) is already a restriction of a permutation, so its true
`l2 -> l2` factor is one.  The positive factor in (7.3) gives no operator
gain.  Fourier recombination cannot turn the dense comparison (7.4) into
the required vector square estimate.

### 7.2 The balanced top-DFI substitution is algebraically false

The top DFI block is

```text
K_c(h,Delta)
 =c^(-1)S(-h,-(RS)^(-1)Delta;c)
 =c^(-1)sum_(x mod c)^*
    e_c(-hx-xbar (RS)^(-1)Delta),                    (7.5)
```

with `c~C=q^(25/33)` and `|Delta|<=D`.  If (contrary to fact) (7.5)
were a separated balanced instance of (7.1) with both lengths `C`, the
claimed `1/12` saving would be

```text
C^(-1/12)=q^(-25/396).                                (7.6)
```

The missing QP saving is `q^(-2/33)=q^(-24/396)`, so even this fantasy
has only the margin

```text
q^(-1/396).                                           (7.7)
```

There is no exact substitution:

1. the inverse coefficient `(RS)^(-1)Delta (mod c)` moves with `c`;
2. the direct phase `e_c(-hx)` depends jointly on the residue `x` and
   modulus `c`, and cannot be placed in a coefficient sequence independent
   of `c`;
3. fixing `c` makes those weights legal but collapses the modulus variable
   to a singleton, losing (7.6);
4. the `Delta` coefficient is the four-fan additive-autocorrelation
   pushforward carrying the `D^3` norm barrier, not a separated scalar
   sequence controlled by (7.1); and
5. the theorem supplies no mask-sensitive vector square over `c,Delta`
   and the arbitrary colour coefficient `z`.

The numerator size is not the decisive obstruction:
`|(RS)^(-1)Delta|` represented before reduction is at most `CD<C^2` at
the working scales.  Nor is compositeness alone decisive.  The fatal
points are the moving two-sided phase, the loss of balance when it is
frozen, and, first of all, withdrawal of the claimed theorem.

```text
Dong--Robles--Zeindler 1/12 estimate available:       NO (WITHDRAWN);
fixed-q residual layer is a balanced application:     NO;
formal fixed-layer dense saving:                       q^(-25/198);
actual inverse-permutation operator gain:              NONE;
formal top-DFI saving if a match existed:               q^(-25/396);
required QP saving:                                    q^(-24/396);
formal spare margin:                                   q^(-1/396);
exact separated top-DFI match:                         NO.
```

## 8. Wright's fixed-factor trilinear theorem: exact reciprocity audit

Wright's current v2 preprint,
[*Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced
convolutions*](https://arxiv.org/abs/2604.25177), proves a bound for

```text
B(M,N,A;R)
 =sum_(a~A,m~M,n~N) alpha_m beta_n nu_a
    e(theta*a*mbar/(nR)),                             (8.1)
```

with `(m,nR)=1` and `M<<N^2`.  The fixed factor really can be exposed in
one leg of our opened Kloosterman sum.  Put `k=R_step*S_step`.  Additive
reciprocity gives the exact identity

```text
S(-h,-k^(-1)Delta;c)
 =sum_(x mod c)^* e(-hx/c)
    e(Delta*cbar/(kx)) e(-Delta/(ckx)).               (8.2)
```

Thus the inverse part of (8.2) has the literal Wright assignment

```text
m_W=c, n_W=x, R_W=k, a_W=Delta, theta=1.             (8.3)
```

This is the only assignment that keeps `m_W,n_W` at the balanced scale.
At the top DFI point,

```text
M_W=N_W=C=q^(25/33), A_W=D=q^(16/33),
R_W=k=R_step*S_step~C^2=q^(50/33).                   (8.4)
```

Wright's Theorem 2.1 has base factor

```text
(AMN)^(1/2)R^(1/4)                                  (8.5)
```

and five bracket exponents.  In powers of `q`, (8.4) gives

```text
true l2 trivial exponent:                         1,
base exponent in (8.5):                         91/66,
bracket exponents:
  -25/264, +25/264, -191/660, -73/660, -25/264.     (8.6)
```

The positive second term dominates.  The resulting exponent is

```text
91/66+25/264=389/264
               =1+125/264.                          (8.7)
```

So even after pretending that every other weight in (8.2) is separated,
the theorem loses `q^(125/264)` relative to the true `l2` trivial bound.

This also explains the tempting numerical resonance.  If one falsely sets
`R_W=1`, the largest bracket term is

```text
q^(-41/660),                                         (8.8)
```

while the missing QP saving is

```text
q^(-2/33)=q^(-40/660).                               (8.9)
```

The apparent margin is only `q^(-1/660)`.  But `R_W=1` is not an exact
map.  Absorbing `k` into the inverse variable instead makes

```text
m_W=kx~C^3, n_W=c~C,
M_W=C^3>N_W^2=C^2,                                  (8.10)
```

outside the theorem's range.

There are independent structural mismatches as well.  The direct factor
`e(-hx/c)` in (8.2) depends jointly on `m_W,n_W`; the triangular unit range
`x<c`, the DFI/Fourier weights, and the actual product mask depend on `c`;
and the `Delta` sequence is the arbitrary-`z` four-fan autocorrelation,
not a free separated coefficient with a harmless norm.  Freezing `c`
makes these coefficients legal but again collapses a balanced variable.
The case `h=0` deletes the direct factor only on the degenerate
Ramanujan/polar axis, not on the primitive transverse block.

```text
literal inverse-leg reciprocity map:                    EXACT;
fixed factor in that map:                               R_W~C^2;
Wright bound at the literal parameters:                 WORSE THAN TRIVIAL;
no-fixed-factor 1/660 resonance:                        FORMAL ONLY;
R_W=1 via m_W=kx within M<<N^2:                         NO;
full two-sided Kloosterman/mask match:                   NO;
power gain for the QP primitive square function:        NONE.
```

## 9. Binary conclusion

```text
full q^2 two-copy recombination before Cauchy:             EXACT;
primitive fibre factorization T_*=E H:                     EXACT;
degree correction in the centered Gram:                    EXACT RANK ONE;
primitive ray coefficient as centered quotient count:      PROVED;
generic quotient baseline is conductor <=q:                PROVED;
exact log/Hankel negative polar on every triangle:           PROVED;
constant-only unweighted carrier theorem is natural:        NO;
weighted coarse principal S4 contribution:                  O(D^4/q^2), PROVED;
projection off span{1,x} closes cross-block restriction:     FALSE FINITELY;
ray support isolates tangent pairs:                         FALSE;
length-q residual blocks are triangle matchings:            PROVED;
within-block centered square budget O(D):                   PROVED;
identical-support parallel classes across ordered blocks:   IMPOSSIBLE;
uniform stability gap from product conservation:            FALSE ABSTRACTLY;
ordered zero-frequency restriction (5.7)/(5.8):             OPEN;
D-scale vector square theorem:                              NOT PROVED;
sharp four-cycle theorem:                                   NOT PROVED.
```

Executable exact checks are in

```text
src/qp_q2_primitive_ray_polar.py
src/test_qp_q2_primitive_ray_polar.py
```

The physical residual-atom construction and literal prime-power fixtures are
in

```text
src/qp_q2_packet_cross_gram_discovery.py
src/test_qp_q2_packet_cross_gram_discovery.py
```
