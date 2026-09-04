# QP four-cycle: parabolic gap-token aggregation

**Date:** 2026-08-17  
**Verdict:** the assigned primitive rank-one relation mass at direction
height `H` satisfies the stronger estimate

```text
sum_(C assigned, h(e_C)~H) w_z(C)
 <<sqrt(D*H) q^o(1) ||z||_2^4.                    (0.1)
```

This replaces the previous `H*sqrt(D)` bound.  Consequently the complete
curvature contribution is at four-cycle strength whenever the third-slice
factor `K_C` is bounded:

```text
sqrt(D/H) * sqrt(D*H)=D.                          (0.2)
```

In particular, (0.1) closes the low-product parabolic sector
`lambda1*lambda2<=q/D`, where `K_C=O(1)`.

An occupied-line refinement below now replaces the pointwise parabolic
factor `K_C*(1+sqrt(D/H))` by

```text
K_C+sqrt(D*K_C/H).                                (0.3)
```

Combined with (0.1), this changes the high-slice curvature loss from `K`
to `sqrt(K)`.  At the balanced high-product block it proves
`D^(35/32+o(1))`, not `D`; the first occupied point on each line and the
remaining `n`-weighted orthogonality gate are stated precisely below.

A determinant-and-content refinement of (0.1) also improves the complete
parabolic-chart sector, over all feasible minima blocks, to

```text
D^(5/4+o(1)).                                      (0.4)
```

Its curvature part is `D^(37/32+o(1))`; the `D^(5/4)` maximum comes from
the first occupied point on each line.  This is a scoped parabolic result:
the nondegenerate and identically-zero high-slice sectors are not changed.

---

## 1. Primitive gap coordinates

Normalize `||z||_2=1`.  Write the assigned primitive rank-one relation as

```text
e=r*s^T,
r=(r1,r2), s=(s1,s2),
gcd(r1,r2)=gcd(s1,s2)=1.                           (1.1)
```

All four components are nonzero in a nonconstant active parabolic chart by
the previously proved zero-component lemma.  Work in one dyadic block

```text
||r||_infinity~R,  ||s||_infinity~S,  R*S~H.       (1.2)
```

For a color matrix `C=(x,y;zeta,w)` killed by `e`, primitivity gives unique
nonzero integers `eta,theta` such that

```text
s1*x-s2*y       = r2*eta,
s1*zeta-s2*w    = r1*eta,
r1*x-r2*zeta    =-s2*theta,
r1*y-r2*w       =-s1*theta,                        (1.3)
eta*theta       =-det(C).                          (1.4)
```

Hence `0<|eta*theta|<<D`.

Attach the four gap tokens

```text
A=(s,r2*eta), B=(s,r1*eta),
C=(r,-s2*theta), T=(r,-s1*theta).                 (1.5)
```

---

## 2. A fixed color pair sees only divisor-many tokens

Consider a fixed ordered color pair `(x,y)`.  If it occurs in an `A` token,
then

```text
|s_i|<<S,
|s1*x-s2*y|=|r2*eta|<<R*D.                        (2.1)
```

All colors are comparable with `q`.  The candidate vectors `s` lie in the
symmetric convex body

```text
|s_i|<<S,       |x*s1-y*s2|<<R*D,                 (2.2)
```

whose area is

```text
<<S*R*D/q=H*D/q.                                  (2.3)
```

At the QP scale `q=D^(33/16+o(1))`, and every primitive quadratic direction
of an actual chart has `H<<D`.  Therefore (2.3) is
`D^2/q=q^(-1/33+o(1))<1`.  A symmetric convex body of area below two cannot
contain two linearly independent integral vectors.  All its integral points
are collinear, and it contains at most the two primitive vectors `+s0,-s0`.

After `s` is fixed, the token offset is fixed by `(x,y)`.  Thus every color
pair belongs to only `q^o(1)` `A` tokens, after the logarithmically many
dyadic/sign blocks.  The same statement holds for `B,C,T`.

Define the matching energies

```text
P_A=sum_(s1*x-s2*y=d_A) |z_x*z_y|^2,              (2.4)
Q_B=sum_(s1*zeta-s2*w=d_B) |z_zeta*z_w|^2,        (2.5)
R_C=sum_(r1*x-r2*zeta=d_C) |z_x*z_zeta|^2,        (2.6)
S_T=sum_(r1*y-r2*w=d_T) |z_y*z_w|^2.              (2.7)
```

The bounded token overlap proves

```text
sum_A P_A, sum_B Q_B, sum_C R_C, sum_T S_T
 <<q^o(1).                                         (2.8)
```

No primality input is needed here beyond integral shell localization; the
strict power in `q>D^2` supplies the thinness.

---

## 3. Four Cauchy--Schwarz and the hyperbola operator

For fixed `(r,s,eta,theta)`, let `W_gamma` be the total assigned four-color
weight.  The linear equations (1.3) make every relevant pair projection a
matching.  Two Cauchy--Schwarz estimates give

```text
W_gamma<=sqrt(P_A*Q_B),
W_gamma<=sqrt(R_C*S_T),                            (3.1)
```

and hence

```text
W_gamma<=(P_A*Q_B*R_C*S_T)^(1/4).                 (3.2)
```

Sum (3.2) and pair the `A,C` and `B,T` factors.  It is enough to bound

```text
Sigma_AC=sum_(r,s) sum_(0<|eta*theta|<<D)
              sqrt(P_(s,r2*eta)*R_(r,-s2*theta)). (3.3)
```

For fixed `r,s`, the standard integer hyperbola operator has `ell^2` norm
`sqrt(D)q^o(1)`.  Therefore

```text
Sigma_AC
 <<sqrt(D)
   (sum_(r,s,eta) P_(s,r2*eta))^(1/2)
   (sum_(r,s,theta) R_(r,-s2*theta))^(1/2).        (3.4)
```

Fix an `A` token `(s,d)`.  A lift to `(r,eta)` must satisfy

```text
r2 divides d,        eta=d/r2.                    (3.5)
```

There are `q^o(1)` choices for `r2` and `O(R)` choices for `r1`; hence the
first sum in (3.4) is `O(R q^o(1))` by (2.8).  Symmetrically the second is
`O(S q^o(1))`.  Thus

```text
Sigma_AC<<sqrt(D*R*S)q^o(1)=sqrt(D*H)q^o(1).      (3.6)
```

The identical estimate holds for the `B,T` pairing.  Cauchy--Schwarz between
the two pairings proves (0.1).  Summing the logarithmically many factor-size
and sign blocks costs only `q^o(1)`.

---

## 4. Actual occupied-line aggregation

The ambient ternary-lattice slice count is

```text
K_C=1+D/lambda3(C)
    <<1+D*lambda1(C)*lambda2(C)/q.                 (4.1)
```

It is wasteful to multiply the curvature count on every occupied
parabolic line by this potential count.  There is an exact primitive
multiplier attached to each actual line.

Let `K=(x,-y;-zeta,w)` be the signed color matrix, `k=det K!=0`, and let
`L=<K,M>` be its pinned integral common level.  The active-scale level
estimate proved in the fixed-secant reduction gives

```text
|L|~|k|q,                     L!=0.                (4.2)
```

Choose unimodular complements to `r,s`.  In the resulting integral carrier
coordinates,

```text
U^T K V=(0,theta;eta,gamma),        eta*theta=-k,
a=U(u,alpha),                       b=V(v,beta).    (4.3)
```

Here `alpha=det(r,a)` and `beta=det(s,b)`, after fixing the orientations of
the complements.  These transverse coordinates count actual rather than
potential slices.
Indeed, if

```text
rho_ij=8*a_i*b_j*c_ij-q^3,
```

then the color relation gives the exact second-gap identity

```text
q^3*alpha*beta
=-(r1*s1*rho_11*a2*b2-r1*s2*rho_12*a2*b1
   -r2*s1*rho_21*a1*b2+r2*s2*rho_22*a1*b1).
```

Consequently

```text
0<|alpha*beta|<<h(e)*D.
```

Nonvanishing uses the actual-shell coprimality and `||r||,||s||<q`: for
example, `alpha=det(r,a)=0` would force the primitive vector `r` to contain
the coprime shell pair `(a1,a2)`.

A maximal integral parabolic carrier line with primitive parameter has

```text
a(t)=a+t*A*r,             b(t)=b+t*B*s,
gcd(A,B)=1.                                          (4.4)
```

Constancy of `<K,a(t)b(t)^T>` gives

```text
A*theta*beta+B*eta*alpha=0.                         (4.5)
```

Thus, with `g=gcd(eta*alpha,theta*beta)`, after a simultaneous sign choice,

```text
eta*alpha=g*A,             theta*beta=-g*B.         (4.6)
```

The quadratic coefficient of the product-matrix line is therefore not an
unspecified nonzero multiple of `e`; it is exactly

```text
M_2=A*B*e.                                          (4.7)
```

There are only divisor-many lines with a fixed primitive pair `(A,B)`.
Indeed

```text
L=theta*u*beta+eta*alpha*v+gamma*alpha*beta,
```

and multiplication by `k=-eta*theta` shows

```text
g divides k*L.                                      (4.8)
```

Once `(A,B,g)` is fixed, (4.6) fixes `(alpha,beta)`, and the level equation
is one primitive affine line in `(u,v)`.  Hence, for
`n=|A*B|`, the number of maximal lines with multiplier `n` is

```text
<<tau(n)*tau(|k*L|)=q^o(1).                         (4.9)
```

Every product entry lies in an interval of length `O(D)`.  An entry on
which `|e_ij|=h(e)` therefore gives at most

```text
1+sqrt(D/(n*h(e)))                                  (4.10)
```

actual points on that line.  If `J_C` is the number of maximal lines which
are actually occupied, ordering their multipliers and using (4.9) gives

```text
m_par(C)
 <<J_C+sqrt(D/h(e))*sum_(occupied lines) n^(-1/2)
 <<J_C+sqrt(D*J_C/h(e)) q^o(1).                    (4.11)
```

The degenerate-slice congruence cover has only `q^o(1)` lines per third
slice, so

```text
J_C<<K_C q^o(1).                                   (4.12)
```

This proves the actual occupied-line improvement

```text
m_par(C)
 <<K_C+sqrt(D*K_C/h(e)) q^o(1),                    (4.13)
```

in place of `K_C*(1+sqrt(D/h(e)))`.

## 5. Weighted consequence and exact remaining gate

On a dyadic block `h(e)~H<=D`, `K_C<=K`, equations (0.1) and (4.13) give

```text
sum_C m_par(C) w_z(C)
 <<(K*sqrt(D*H)+D*sqrt(K))q^o(1)||z||_2^4.         (5.1)
```

At the balanced high-product scale

```text
||r||~||s||~D^(5/16),       H=D^(5/8),
|eta|~D^(5/8),              |theta|~D^(3/8),
gcd(eta,theta)=D^o(1),
P~D^(5/4),                  K~D^(3/16),             (5.2)
```

the first term in (5.1) is exactly `D`, while the curvature term is

```text
D*sqrt(K)=D^(35/32).                                (5.3)
```

Thus actual occupancy saves `sqrt(K)=D^(3/32)` over the former `K*D`
curvature estimate at this block, but it does not prove FC.

Over the whole feasible minima range `P<=q^(2/3)=D^(11/8+o(1))`, the
curvature term in (5.1) is at most

```text
D*sqrt(K)<=D^(37/32+o(1)).                          (5.4)
```

The occupied-line term in the unrefined estimate (5.1) can still reach
`D^(21/16+o(1))` when the relation height is `D` and `K=D^(5/16)`.
Section 6 removes part of this artificial worst case by retaining the
determinant size and the content of `(eta,theta)`.

Equivalently, the remaining balanced theorem is the `n`-weighted
orthogonality estimate

```text
sum_C (sum_(n occupied by C) n^(-1/2)) w_z(C)
 <<sqrt(D*H)q^o(1)||z||_2^4.                       (5.5)
```

Neither the determinant-layer mass nor unweighted gap-token overlap proves
(5.5): they allow the same color to occur at `K` different primitive slope
products and lose `sqrt(K)`.  A weighted `Aff x Add` estimate or a direct
affine/Hankel merger must supply precisely this orthogonality.

The exact plane-covolume identity still gives

```text
K_C-1
 <<D/q * sqrt(eta^2*||r||^4+theta^2*||s||^4)
          /gcd(eta,theta).                         (5.6)
```

Simply inserting (5.6) into the color hyperbola operator is insufficient:
it weights that operator by `|eta|/gcd(eta,theta)` or its transpose, whose
norm can be polynomially larger than `sqrt(D)`.

## 6. Determinant-content refinement

Split further into dyadic blocks

```text
|eta|~E,       |theta|~T,       gcd(|eta|,|theta|)~G,
||r||~R,       ||s||~S.                              (6.1)
```

The `eta`--`theta` matrix in (3.3), restricted to this block, has maximum
row degree `O((T/G)q^o(1))` and maximum column degree
`O((E/G)q^o(1))`.  Indeed, for fixed `eta`, the possible common divisors in
`[G,2G)` are divisors of `eta`, and there are only `q^o(1)` of them; each
leaves `O(T/G)` multiples for `theta`.  Schur's test therefore gives

```text
||1_(|eta|~E,|theta|~T,gcd~G)||_(2->2)
 <<sqrt(E*T)/G q^o(1).                              (6.2)
```

The divisor lift after (3.4) is unchanged: its two token sums are still
`O(Rq^o(1))` and `O(Sq^o(1))`.  Thus (3.6) sharpens on (6.1) to

```text
sum_(C in block) w_z(C)
 <<sqrt(E*T*R*S)/G q^o(1)||z||_2^4.                 (6.3)
```

The factor `G^(-1)` is necessary.  The exact saturated-plane covolume is

```text
P_C~sqrt(E^2*R^4+T^2*S^4)/G.                       (6.4)
```

The saturated plane has, up to absolute reduction constants, the same
first two successive minima as the ambient completion lattice.  Hence
`P_C~lambda1*lambda2`, by two-dimensional Minkowski, and

```text
K_C<<1+D*P_C/q.                                    (6.5)
```

Write

```text
R=D^r, S=D^s, E=D^e, T=D^t, G=D^g,
p=max(e+2r,t+2s)-g,
kappa=max(0,p-17/16).                              (6.6)
```

The feasible conditions are

```text
e+t<=1,       r+s<=1,       0<=g<=min(e,t),
p<=11/8.                                             (6.7)
```

Equations (4.13), (6.3), and (6.5) give the two exponents

```text
singleton: kappa+(e+t+r+s)/2-g,
curvature: (1+kappa+e+t)/2-g.                       (6.8)
```

The curvature exponent is at most `37/32` immediately from
`kappa<=5/16` and `e+t<=1`.  For the singleton exponent, the two
inequalities defining `p` imply

```text
r+s<=p+g-(e+t)/2.                                  (6.9)
```

If `p<=17/16`, (6.8) is at most `1`.  Otherwise (6.9) bounds it by

```text
3*p/2-13/16-g/2 <=5/4.                             (6.10)
```

The endpoint is attained in the exponent polytope, up to swapping the two
factors, at

```text
(r,s,e,t,g)=(11/16,3/16,0,1,0),
p=11/8, kappa=5/16.                                (6.11)
```

Thus the whole parabolic-chart contribution is

```text
Q_par(z)<<D^(5/4)q^o(1)||z||_2^4,                 (6.12)
```

while its curvature subterm is `D^(37/32+o(1))`.  No conclusion for the
nondegenerate or identically-zero high-`K` slices is included in (6.12).
Those broad sectors remain at `D^(21/16+o(1))`, so the global fourth-trace
and operator exponents are unchanged by this scoped refinement.

## 7. Normalized-GCD line tokens and the two-chord residual

There is an exact multiplicative form of the open `n` weight.  Separate
signs and write

```text
(eta,beta)=t*(q0,p0),       gcd(p0,q0)=1,
(theta,alpha)=u*(s0,r0),   gcd(r0,s0)=1.             (7.1)
```

If

```text
g0=gcd(q0*r0,s0*p0),
```

then the transverse common factor and primitive line multipliers are

```text
gcd(eta*alpha,theta*beta)=t*u*g0,
|A|=q0*r0/g0,             |B|=s0*p0/g0.             (7.2)
```

Consequently all scale in `t,u` cancels:

```text
n^(-1/2)=|A*B|^(-1/2)
 =gcd(q0*r0,s0*p0)/sqrt(q0*r0*s0*p0).               (7.3)
```

This is the classical normalized-GCD kernel.  Here is the precise
conditional `ell^2` reduction.  Refine the four energies in (2.4)--(2.7)
by the actual wedge coordinate: for example,
`P_(s,d,beta)` sums the top-pair energy over pairs admitting an actual
carrier `b` with `det(s,b)=beta`; define `Q` with the same `beta`, and
`R,S` with `alpha=det(r,a)`.  The pair projections remain matchings after
this refinement.  Freeze `r,s,q0,s0,t,u`.  In the `A,C` pairing of the
four gap-token Cauchy--Schwarz argument, put

```text
f(p0)=P_(s,r2*q0*t,p0*t)^(1/2),
h(r0)=R_(r,-s2*s0*u,r0*u)^(1/2).                    (7.4)
```

The relevant bilinear form is exactly

```text
sum_(p0,r0) gcd(s0*p0,q0*r0)/sqrt(s0*p0*q0*r0)
             *f(p0)*h(r0).                          (7.5)
```

The integers `s0*p0` are distinct as `p0` varies, and so are `q0*r0`.
The normalized-GCD matrix bound makes (7.5) at most `q^o(1)||f||_2||h||_2`.
For fixed `eta`, the possible `q0` divide `eta`; likewise `s0` divides
`theta`.  Thus only divisor-many GCD blocks occur over a fixed
`(eta,theta)`, and the remaining `eta*theta<<D` matrix has norm
`sqrt(D)q^o(1)` exactly as in Section 3.

It follows rigorously that (5.5) holds for any residual family satisfying
the four bounded-multiplicity token estimates

```text
sum_(residual q0,p0 lifts) P_(s,r2*eta,beta)
 <<q^o(1) sum_(base gap tokens) P_(s,r2*eta),        (7.6)
```

and the analogous estimates for `Q,R,S`.  Indeed (7.5), the divisor lifts,
the hyperbola norm, and the same outer Cauchy--Schwarz as in Section 3 give
`sqrt(DH)q^o(1)||z||_2^4`.

Repeated rich tokens have a proved treatment.  Fixed reduced data in
(7.1) fix `(A,B)`, hence the raw carrier direction

```text
delta=(A*r,B*s).                                    (7.7)
```

After grouping all maximal lines with this fixed `delta`, every line with
at least three occupied integer parameters belongs to the fixed-direction
affine/Hankel merger.  The three points expose the quadratic curvature and
pin the intercept invariant; the entire fixed-`delta` merged patch has
fourth trace `O(Dq^o(1))||z||_2^4`.  Such repetitions may therefore be
quotiented before forming the arrays (7.4).  Distinct `delta` blocks remain
in the normalized-GCD summation; no unweighted summation of `O(D)` patch
bounds is asserted here.

The threshold three is essential.  A line with exactly two actual
parameters is an isolated chord.  Its intercept need not be tangent-pinned,
and a fixed direction can support polynomially many such chords.  Fixing
the full secant `E` restores the proved `q^o(1)` multiplicity, but summing
the varying actual secants is precisely the missing correlation.  Hence,
after the rich fixed-direction quotient, the sole unproved part of (7.6)
is the family of varying-`E` two-point chords.  The normalized-GCD identity
does not by itself bound their repeated token coefficients.

```text
unweighted dyadic relation mass sqrt(DH):           PROVED;
low-P parabolic curvature contribution D:           PROVED;
occupied-line bound K+sqrt(DK/h):                    PROVED;
balanced parabolic block D^(35/32):                  PROVED;
determinant-content block mass sqrt(ETRS)/G:          PROVED;
all-minima parabolic-chart bound D^(5/4):             PROVED;
normalized-GCD reduction of the n weight:             PROVED;
rich (at least three-point) fixed-delta quotient:      PROVED;
fixed-k master-matching / Cotlar collapse:             PROVED;
bounded-token residual n-weighted estimate:           CONDITIONAL;
varying-E two-point chord correlation:                 OPEN;
nondegenerate/zero broad bound D^(21/16):              UNCHANGED;
n-weighted occupied-line orthogonality:               OPEN;
full parabolic FC across all P:                       OPEN;
full four-cycle bound:                               OPEN.
```

Finite strip, divisor-lift, and occupied-line ledgers are replayed in
`src/qp_four_cycle_gap_token_aggregation.py` and its test module.

## 8. Fixed-`k` Cotlar collapse for the two-chord residual

There is an exact obstruction to gaining the missing varying-`E` sum from
the fixed-`(E,k)` partial-matching theorem alone.  It is an obstruction to
that operator argument, not a counterexample to the desired four-cycle
bound.

Let `P_k` be the set of actual-shell color matrices

```text
C=(x,y;z,w),                 x*w-y*z=k.              (8.1)
```

It is one top--bottom partial matching, before `E` is fixed.  Indeed, with
`(x,y)` fixed, two possible bottom pairs obey

```text
x*(w-w')-y*(z-z')=0.                                (8.2)
```

Distinct actual prime powers in the project shell are coprime.  Hence
`(z-z',w-w')=j*(x,y)`, while the shell diameter is smaller than either
coordinate; therefore `j=0`.  Reversing top and bottom proves the column
statement.  Every fixed-`(E,k)` support is consequently a restriction of
this same matching, not a transverse matching.

Write `Pi_k` for its partial-permutation operator.  Allow a nonnegative
coefficient `a_E(C)` on the residual two-chord support; this can include
fixed-`(C,E)` multiplicity and the `n^(-1/2)` weight.  There is a diagonal
operator `D_(E,k)` on top color pairs such that exactly

```text
T_(E,k)=Pi_k D_(E,k),
T_(E,k)^* T_(F,k)=D_(E,k)^* D_(F,k).                 (8.3)
```

Thus

```text
||T_E^* T_F||
 =max_(C in P_k) |a_E(C)*a_F(C)|,                   (8.4)

||sum_E T_(E,k)||
 =max_(C in P_k) sum_E a_E(C)                       (8.5)
```

for the positive form at issue.  In the binary support model, every
nonempty common color makes the cross norm in (8.4) exactly one.  If `R(C)`
residual energy layers contain a single color matrix, then each of those
layers has Cotlar overlap sum at least `R(C)`, and the summed operator has
norm at least `R(C)` by (8.5).  There is no square-root gain.

The proved two-fixed-relation theorem controls the weighted *mass* of the
common support of `E` and `F`.  It cannot make the norm of a nonempty
diagonal projection in (8.3) smaller than one.  Therefore a Cotlar--Stein,
square-function, or Hilbert--Schmidt summation using only

```text
fixed-(E,k) partial matching + two-relation mass
```

is exactly circular: it reduces the problem to the largest positive
varying-`E` coefficient stacked on one `C`, which is the two-chord residual
in (7.6).

There is a useful but insufficient fixed-direction refinement.  Fix one
color `c` and an opposite-sign projected difference `(R,-S)`, with
`R,S>0`, and put `g=gcd(R,S)`.  If both endpoints lie in the same product
band, then

```text
d=(a+R)*(b-S)-a*b=R*b-S*a-R*S,
|d|<=2D,                  g divides d.               (8.6)
```

For fixed `d`, any two integer solutions of the linear equation in (8.6)
differ by

```text
(Delta a,Delta b)=j*(R/g,S/g).                       (8.7)
```

Along this positive direction the product `a*b` changes by `>>q` at every
nonzero step.  Since `q>>D^2`, at most one solution can lie in the product
band.  There are only `O(1+D/g)` possible multiples `d`.  Same-sign
projected differences, or a difference with exactly one zero component,
change the product by `>>q` and give no nontrivial chord.

For a full raw direction

```text
delta=(R1,R2,-S1,-S2),
G(delta)=max_(i,j) gcd(Ri,Sj),                       (8.8)
```

pair uniqueness makes projection to any one cell injective once the full
color matrix is fixed.  Applying (8.6) in the best cell gives the rigorous
two-chord degree bound

```text
N_2(C,delta)<<1+D/G(delta).                          (8.9)
```

This does not sum the directions.  If `delta=(A*r,B*s)` and `n=|A*B|`, its
weighted coefficient is only

```text
(1+D/G(delta))/sqrt(n).                              (8.10)
```

In the normalized-GCD variables (7.1)--(7.3),

```text
g_ij=gcd(q0*r0*r_i,s0*p0*s_j)/g0,
D/(G*sqrt(n))
 =D*g0/max_ij gcd(q0*r0*r_i,s0*p0*s_j)
   *g0/sqrt(q0*r0*s0*p0).                           (8.11)
```

The last factor is the normalized-GCD kernel, but the new prefactor can be
as large as `D`: coprime multipliers and cross-coprime direction coordinates
have every relevant `g_ij=1`.  Thus (8.9) improves a fixed-direction chord
degree but supplies no summable cross-direction Cotlar coefficient without
an additional average-GCD theorem.

The cross product is genuinely nonzero after the rich-line quotient in the
full-integer model.  At `q=2151`, cutoff `U=1`, take

```text
C=(981,978;972,969),        det C=-27,       L=-35334. (8.12)
```

There are two endpoint-only constant-level carrier lines:

```text
X1=(971,980,1306,1310),   X1'=(974,983,1302,1306),
delta1=(3,3,-4,-4),       E1=(-22,-34,14,2),

X2=(1294,1306,980,983),   X2'=(1298,1310,977,980),
delta2=(4,4,-3,-3),       E2=(-26,-38,10,-2).       (8.13)
```

Direct integer calculation gives

```text
L_C(Xi)=L_C(Xi'),
<K_C, delta_a delta_b^T>=0,
det(E1)=det(E2)=432.                                (8.14)
```

Hence the whole affine line through each pair has constant level.  Exact
enumeration of this color fiber finds only the two displayed parameters on
each line, so neither is removed by the at-least-three-point quotient.  All
four completions are individually all-eight-distinct from the colors, lie
in the project shell, and satisfy

```text
max |(q/2)^(50/33) log(8*a*b*c/q^3)|
 <0.973<1.                                           (8.15)
```

The two distinct energy layers therefore contain the same color edge, and
their binary cross operator in (8.3) has norm one.  Both primitive line
weights have `n=12`, so the `n^(-1/2)`-weighted cross norm is exactly `1/12`,
not zero.  Putting mass `1/2` on the four distinct colors makes this single
edge have quartic weight `1/16`.  This fixture uses full integers, not actual
prime powers, and has only two layers.  It disproves literal cross-`E`
orthogonality, but it does **not** disprove a `q^o(1)` residual multiplicity
theorem, (7.6), or the full four-cycle estimate.

The aligned-matching ledger and the exact fixture are replayed in
`src/qp_four_cycle_weighted_secant_lab.py` and its test module.
