# Local `k=2` clusters: the macroscopic screen fails the Frobenius moment

Status: exact moment-level no-go for a positive-length equal-depth block,
plus a sharp audit of what remains locally possible, 2026-08-11.  This note
does not assert anything about the location of an actual zeta zero and does
not prove a zero-free strip.

## 1. Verdict

Let

```text
C_0=3/2-(1/sqrt(2))*cot(1/sqrt(2)),
r_0=(1-C_0)/2.
```

The global simple-line theorem permits, at the count level, concentrating
all allowed off-line points into one block of ordinate length

```text
H=(1-C_0+o(1))*T=(2*r_0+o(1))*T.                    (1.1)
```

Inside that block put one reflected pair at each natural pair-center
spacing

```text
Delta=4*pi/ell,        ell=log(T/(2*pi)).             (1.2)
```

Each center contributes two zero-points, so its point density
`2/Delta=ell/(2*pi)` is the Riemann--von Mangoldt density.  Slowly chirping
the spacing by replacing `ell` with `log(t/(2*pi))` gives the full interval
count with `O(1)` discrepancy.  Put the remaining points simply on the
critical line.  Thus Riemann--von Mangoldt counts, symmetry, distinctness,
and the global simple-line density do **not** exclude this clustered block.

The evaluated Zeta23 Frobenius moment does exclude it when the block has any
fixed common depth `alpha>0`.  In the legal bandwidth-one
Montgomery--Taylor probe, a `k=2` pair lattice has a `q=1` reciprocal alias
of operator scale

```text
X_0^(alpha/2),           X_0=exp(ell),                (1.3)
```

on a positive proportion of the coordinate directions.  For a block of
length `H`, write `d_H=(1+o(1))*H*ell/(2*pi)`.  Its pair matrix `Q_H`
satisfies

```text
tr((Q_H)_-) >= c_alpha*d_H*X_0^(alpha/2),             (1.4)
```

where `c_alpha` may be chosen uniformly positive when
`alpha>=delta>0`.  Any on-line filler of the correct total multiplicity has
trace `O(d_0)`, where `d_0=(1+o(1))*T*ell/(2*pi)`.  Consequently, if

```text
H*X_0^(alpha/2) >> T,                                (1.5)
```

then the completed zero matrix has

```text
||Ghat||_F^2 >> d_0.                                 (1.6)
```

This contradicts the Zeta23 identity
`||Ghat||_F^2=(c_*^(-1)+o(1))*d_0`.  In particular, the proposed
macroscopic block (1.1) is impossible under the complete current moment
ledger.

There is an equally important converse limitation.  If

```text
H*X_0^alpha=o(T),                                    (1.7)
```

then inserting such a block changes both leading moments by `o(d_0)`.
It also has global off-line density `o(1)`.  A block in this range may have
`q asymp H*ell` pair rows.  In particular, one may also require
`H=o(sqrt(T))` and use an exactly arithmetic block: the discrepancy between
its constant local density and Riemann--von Mangoldt density is then
`O(1+H^2/T)=O(1)`.  Its endpoint-lobe synthesis matrix has a smallest
singular value bounded above by `exp(-c*q)`.  Thus all present bulk inputs
remain compatible with **exponentially poor arbitrary-data frame
conditioning**.

That last statement is not yet a screened carrier.  A small frame singular
value produces a nearly dependent row combination; Birman--Schwinger
screening instead asks for the selected negative row to have bounded
target-conditioned leverage against the positive rows.  No implication
between those statements follows from counts or the first two moments.

The exact outcome is therefore:

```text
macroscopic equal-depth k=2 cluster:  ruled out by Frobenius;
sublinear exponentially ill-conditioned cluster: compatible with all bulk inputs;
selected-row exponential screening:  still a target-conditioned local gate.
```

The previously constructed tapered `k=3` island supplies an actual
moment-compatible power screen, `K<=X^(2alpha/3+o(1))`; it does not supply
an exponential screen.

## 2. The legal bandwidth-one probe

Use the endpoint-mollified Montgomery--Taylor window from the evaluated
Zeta23 moment, with

```text
support(phi_T) subset [-ell/2,ell/2],
a_T=ell^(-1)*integral phi_T(t)^2dt -> a_*>0,
h_0=2*pi/ell,
tau_n=tau_0+n*h_0,
d_0=floor(T/h_0).                                    (2.1)
```

Away from its fixed-width endpoint ramps,

```text
phi_T(ell*x)^2 -> v_*(x)=cos(sqrt(2)*x),
                       -1/2<x<1/2.                   (2.2)
```

For a real coefficient vector `c`, put

```text
p_c(t)=sum_(0<=n<d_0)c_n*exp(-i*n*h_0*t).
```

At pair centers

```text
gamma_j=beta+j*Delta,
Delta=4*pi/ell,             P=2*pi/Delta=ell/2,      (2.3)
```

the lower-member evaluations are

```text
F_j(c)=integral phi_T(t)*p_c(t)*exp(alpha*t)
                         *exp(i*gamma_j*t)dt.         (2.4)
```

The normalized signed form is

```text
Q(c)=(2/(a_T*ell^2))*Re sum_j F_j(c)^2.              (2.5)
```

The factor two is the reflected mate; no pair row or multiplicity is
duplicated.

## 3. Infinite `k=2` alias calculation

Bilinear Poisson summation gives

```text
sum_(j in Z)F_j(c)^2
 =P*sum_(q=-1)^1 exp((alpha+i*beta)*q*P)
     *integral phi_T(t)*phi_T(q*P-t)
               *p_c(t)*p_c(q*P-t)dt.                 (3.1)
```

The `q=+-2` intersections are support endpoints and vanish for the
mollified window.  Define

```text
B_r=integral phi_T(P/2+x)*phi_T(P/2-x)
                  *cos(r*h_0*x)dx.                   (3.2)
```

The `q=1` alias matrix has entries

```text
(Q_1)_(nm)
 =(1/(a_T*ell))*X_0^(alpha/2)*B_(n-m)
    *cos(theta-pi*(n+m)/2),                          (3.3)
```

where `theta` is the harmless lattice offset.  Choose
`theta=pi/4` and every squared cosine in (3.3) is `1/2`.  The lower bound
below does not require that choice.  Indeed, put

```text
E_even(T)=ell^(-2)*sum_(r even)B_r^2,
E_odd(T) =ell^(-2)*sum_(r odd) B_r^2.                (3.4)
```

Both quantities have strictly positive limits.  Positivity of the even
limit already follows from `B_0`.  If the odd limit vanished, every odd
Fourier coefficient of the positive limiting overlap on one half of the
period would vanish.  Its periodic extension would then have half the
original period, which is impossible because that overlap is positive in
the interior of one half-period and zero in the other.  Hence

```text
min(E_even(T),E_odd(T))>=e_*>0                       (3.5)
```

for all sufficiently large `T`.  Since `n+m` and `n-m` have the same
parity, the two contributions to the squared Frobenius norm are weighted
by `cos(theta)^2` and `sin(theta)^2`, respectively.  Thus the estimate is
uniform in the lattice phase; count rounding or slow chirping cannot tune
the alias away.

Parseval for the coordinate Fourier series gives

```text
sum_(r in Z)B_r^2
 =ell*integral [phi_T(t)*phi_T(P-t)]^2dt
 =ell^2*(I_2+o(1)),                                  (3.6)

I_2=integral_0^(1/2)
       v_*(x)*v_*(1/2-x)dx>0.                        (3.7)
```

Consequently, on any consecutive coordinate section of length `d'->infty`,

```text
c*d'*X_0^alpha <= ||Q_1||_F^2
                 <=C*d'*X_0^alpha.                  (3.8)
```

For `theta=pi/4`, the normalized leading constant in (3.8) is
`I_2/(2*a_*^2)`.  For arbitrary phase it is the corresponding positive
combination of the two parity energies in (3.4).

The other two aliases are smaller in Frobenius norm by the fixed factor
`X_0^(-alpha/2)`.  The same periodization argument as for the sparse-island
base block gives

```text
||Q_infinity||op=O(X_0^(alpha/2)),                   (3.9)

tr Q_infinity=O(d'+X_0^(alpha/2)).                   (3.10)
```

It follows that

```text
||Q_infinity||_F^2 >=c*d'*X_0^alpha,

||Q_infinity||_1
 >=||Q_infinity||_F^2/||Q_infinity||op
 >=c*d'*X_0^(alpha/2).                               (3.11)
```

Since `d'->infinity` and `X_0^(alpha/2)->infinity`, the bound in (3.10) is
`o(d'*X_0^(alpha/2))`.  Since
`tr(H_-)= (||H||_1-tr H)/2` for Hermitian `H`, (3.10)--(3.11) yield

```text
tr((Q_infinity)_-)
 >=c*d'*X_0^(alpha/2).                               (3.12)
```

This is the extensive negative trace which arbitrary-data frame
conditioning does not see.

## 4. Finite blocks and exact Riemann--von Mangoldt spacing

First take an arithmetic block of pair centers of length `H`.  Restrict the
coordinate indices to the inner block at distance `D=sqrt(T)` from its two
ends.  Twice integrating the `C^2` taper gives

```text
abs(phi_T_hat(r-i*alpha))
 <=C*X_0^(alpha/2)/(1+r^2).                           (4.1)
```

The trace norm of the omitted pair rows on that inner coordinate section is

```text
O(X_0^alpha/D^2)=o(1).                               (4.2)
```

Thus (3.8)--(3.12) transfer to the finite block with

```text
d'=(1+o(1))*H*ell/(2*pi).                            (4.3)
```

The actual density varies slowly across a positive-length dyadic block.
This is repaired without losing the lower bound.  Put pair centers at the
quantiles

```text
integral_(gamma_0)^(gamma_j)
       log(t/(2*pi))/(4*pi)dt=j+vartheta.             (4.4)
```

Their two reflected points satisfy Riemann--von Mangoldt counting with
bounded discrepancy inside the block.  Divide the block into intervals of
length

```text
R=T^(1/3).                                            (4.5)
```

On each interval, (4.4) differs from an arithmetic progression of spacing
`4*pi/log(t_c/(2*pi))` by

```text
O(R^2/(T*ell))=o(1/ell).                              (4.6)
```

For that local arithmetic progression, repeat Section 3 with
`ell_c=log(t_c/(2*pi))` and `P_c=ell_c/2`.  The overlap and its two parity
energies have the same positive limits uniformly for `ell_c=ell+O(1)`.
The matrix phase step is `pi*ell_c/ell`: if
`abs(ell_c-ell)>>1/R`, Dirichlet averaging gives mean squared cosine
`1/2+o(1)` on a section of length `asymp R*ell`; in the complementary case,
the even/odd argument (3.4)--(3.5) gives the same uniform lower bound.
Thus (3.8)--(3.12) hold uniformly for every local lattice phase.

Equation (4.6) then shows that the actual Gabor rows and these local alias
matrices differ by `o(1)` in the relative Hilbert--Schmidt estimate.  Use
an inner coordinate section of each interval, deleting a guard `D=T^(1/8)`
at both ends.  Pair rows
outside that interval have trace norm
`O(X_0^alpha/D^2)=o(R*ell*X_0^(alpha/2))` on its inner section by (4.1).
Indeed, the ratio here is
`T^(alpha/2-7/12+o(1))/ell=o(1)` for every `alpha<1/2`; at this second use
of the guard the tail need not be `o(1)` absolutely.

Pinch the full matrix to the direct sum of these inner coordinate sections.
The Frobenius norm cannot increase under pinching.  Nor can the negative
trace increase: `H -> tr(H_-)` is convex and pinching is an average of
unitary conjugations.  Hence the negative trace of the unpinched block is at
least the sum of the local negative traces.  Since the guards remove only
`o(H)` ordinate length, (3.12) proves

```text
tr((Q_H)_-)
 >=c*d_H*X_0^(alpha/2),
d_H=(1+o(1))*H*ell/(2*pi).                            (4.7)
```

This proves (1.4) for the exact count-compatible chirped block, including a
block adjacent to either end of the modulation interval.  A distinguished
pair may be placed in its interior or at its count-rounded boundary without
affecting (4.7).

## 5. Positive fillers cannot repair a macroscopic block

Let `P_on>=0` be the normalized matrix of every on-line point.  The
full-grid Poisson identity bounds the trace of one simple on-line row by an
absolute constant.  The total zero count therefore gives

```text
tr P_on=O(d_0).                                      (5.1)
```

For Hermitian `A` and positive `P`, the variational formula gives

```text
tr((A+P)_-)>=tr(A_-)-tr P.                           (5.2)
```

If (1.5) holds, (4.7), (5.1), and (5.2) imply

```text
tr((Q_H+P_on)_-)
 >=(c/2)*d_H*X_0^(alpha/2).                          (5.3)
```

Cauchy--Schwarz on at most `d_0` negative eigenvalues now yields

```text
||Q_H+P_on||_F^2
 >=tr((Q_H+P_on)_-)^2/d_0
 >=c'*(d_H^2/d_0)*X_0^alpha.                         (5.4)
```

For `H=theta*T`, fixed `theta>0`, this is

```text
||Q_H+P_on||_F^2>=c_theta*d_0*X_0^alpha.             (5.5)
```

The evaluated Zeta23 moment is only

```text
||Ghat||_F^2=(c_*^(-1)+o(1))*d_0.                    (5.6)
```

Equations (5.5)--(5.6) are incompatible.  This excludes the block of length
`(1-C_0)T` permitted by counts and global density.

## 6. A compatible sublinear cluster and its exact conditioning warning

The preceding theorem is deliberately not overstated.  Choose instead

```text
H*X_0^alpha=o(T),       H*ell ->infinity,
H=o(sqrt(T)).                                          (6.1)
```

There is no loss in the last restriction: for every fixed `alpha<1/2`, one
may take `H=T^theta` with
`0<theta<min(1/2,1-alpha)`.  Center the block at `t_c`, put
`ell_c=log(t_c/(2*pi))`, and use the exact spacing `4*pi/ell_c`.  On every
subinterval of this block, its two-point-per-center count differs from the
Riemann--von Mangoldt main term by `O(1+H^2/T)=O(1)`.  Endpoint rounding and
on-line fillers repair this bounded discrepancy.

Insert this arithmetic block into any count- and moment-compatible on-line
background, replacing the same number of on-line points.  (Such backgrounds
are obtained by balanced selection from the Montgomery--Taylor sharp grid,
with a balanced positive proportion of arbitrarily close, but distinct,
near-duplicates to tune the evaluated Frobenius constant.)  The pair matrix
has rank `O(H*ell)` and, by the sampling bound,

```text
||Q_H||op=O(X_0^(alpha/2)),
||Q_H||F^2=O(H*ell*X_0^alpha)=o(d_0).                (6.2)
```

The removed on-line block has polynomial operator norm and rank
`O(H*ell)`, hence Frobenius square `o(d_0)` after shrinking `H` by an
irrelevant power of `ell` if necessary.  Cross terms with the background
are `o(d_0)` by Cauchy--Schwarz.  Counts have bounded discrepancy, every
point is simple, symmetry is exact, and the global off-line fraction is
`H/T=o(1)`.  Therefore this sublinear equal-depth block is compatible with
all current bulk inputs.

It is nevertheless exponentially ill-conditioned on every fixed proper
endpoint lobe.  Let

```text
I_a=[-a*ell/2,a*ell/2],             0<a<1/2,

(S_q z)(t)=sum_(j=0)^q z_j*exp(i*j*Delta*t).          (6.3)
```

For

```text
z_j=(-1)^(q-j)*binom(q,j),
```

one has exactly

```text
S_q z=(exp(i*Delta*t)-1)^q,
||z||_2^2=binom(2*q,q).                              (6.4)
```

Consequently

```text
sigma_min(S_q:L2 coefficients ->L2(I_a))
 <=C*sqrt(a*ell)*q^(1/4)
      *sin(pi*a*ell/log(T/(2*pi)))^q.                (6.5)
```

For the exact arithmetic construction above, (6.5) applies to all
`q+1 asymp H*ell` pair centers at once.  A common equal-depth Laplace weight
is an invertible multiplier on `I_a` and changes (6.5) by at most a fixed
power of `X_0`.  Thus `q>>ell` makes the upper bound exponentially smaller
than every power of `X_0`, even in the moment-compatible range (6.1).

This proves that Riemann--von Mangoldt counts, global line density, and the
first two moments cannot yield a uniform arbitrary-data interpolation
constant for local off-line rows.

## 7. Why this is not yet exponential carrier screening

Write the positive and negative row matrices of the actual reflected pairs
as `X_C` and `Y_C`.  For one selected negative row `y`, its exact
Birman--Schwinger leverage against the positive matrix `A=X_C^T X_C` is

```text
b(A,y)=y^T*A^dagger*y.                               (7.1)
```

Screening requires `y in range(A)` and `b(A,y)<=1` after the exact row
weights are included.  Formula (6.5) says instead that the positive-row
synthesis has a small singular value: there is a normalized coefficient
vector producing a small linear combination of rows.  This gives no upper
bound for (7.1).

The distinction is already exact in two dimensions.  For

```text
X=diag(1,epsilon),
```

the smallest synthesis singular value is `epsilon`.  The target `e_1` has
leverage one, whereas `e_2` has leverage `epsilon^(-2)`.  The same bad frame
therefore has a threshold target and a maximally unscreened target.

In fact a small singular value makes the leverage large for a target with a
component in that bad direction.  To turn (6.5) into an exponential carrier
upper bound one must prove the separate target-conditioned statement

```text
dist(selected y,range(X_C)) small
and
min{||z||_2^2:X_C^T*z=selected y}<=1+o(1).           (7.2)
```

Neither the trace/Frobenius identities nor global simple-line density
controls (7.2).  Conversely, (5.5) proves that using a positive-length
equal-depth block to force it is illegal.

## 8. Exact scope

The local clustering barrier is now split cleanly.

1. A block using the entire off-line density allowance over length
   `(1-C_0)T` satisfies the count ledger but violates the Frobenius moment by
   the factor `X_0^alpha`.
2. A sublinear block satisfying (6.1) obeys every current bulk input and has
   an exponentially bad endpoint-lobe frame constant.
3. Bad frame conditioning is not selected-row screening.  The remaining
   local theorem is the target-conditioned leverage estimate (7.2).
4. The tapered sparse `k=3` island separately proves a genuine
   moment-compatible power screen.  No construction here improves that to
   an exponential carrier loss.

Thus the full current inputs do rule out the proposed **macroscopic
equal-depth** cluster, but they do not supply the local conditioning theorem
needed for a uniform carrier bound.  No zero-free-strip conclusion follows.
