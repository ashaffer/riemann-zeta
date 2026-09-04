# Endpoint-flat packets: exact autocorrelation and the surviving prime polynomial

Status: exact packet/autocorrelation/completion ledger and a localized
two-lobe refinement, 2026-08-11.  The refinement retains a single core pair
at the full `X^alpha/L` scale up to a subpower loss.  Its only power-sized
arithmetic term is one smooth transition-scale von Mangoldt polynomial.
No fixed-power estimate for that polynomial, general signed carrier theorem,
or zero-free strip is proved here.

## 1. Verdict

The flat binomial-tail packet in
[`ZETA23-SINGLE-CORE-PAIR-ONLINE-SCREENING-BOUND-2026-08-11.md`](ZETA23-SINGLE-CORE-PAIR-ONLINE-SCREENING-BOUND-2026-08-11.md)
can be evaluated exactly.  Its Fourier coefficients are rational finite
binomial sums, and its zero-extended autocorrelation is an explicit finite
sum of elementary sine kernels.  If the grid is centered at the selected
ordinate `gamma`, the common grid translation survives on the prime side as

```text
Re R_f(y)=C(y)*cos(gamma*y).                           (1.1)
```

It cannot be removed or replaced by `1`.

The exact completed quadratic form is

```text
Q(f)=Pole(f)+Arch(f)
     -2*sum_(n<X) Lambda(n)/sqrt(n)
          *C(log n)*cos(gamma*log n),                 (1.2)
```

or, without deleting the zeta-pole continuum,

```text
Q(f)=Arch(f)+R_0(f)
     -2*integral_[1,X] v^(-1/2) C(log v)cos(gamma log v)
                         d(psi(v)-v),                 (1.3)

R_0(f)=2*integral_0^L e^(-y/2)C(y)cos(gamma*y)dy.     (1.4)
```

Thus (1.3) retains the gamma term, both zeta-pole pieces, the continuum
center, every prime power, and the absolute grid phase.  Formula (1.4) is
exactly the rational `1/[2*pi*(1/4+t^2)]` remainder in the Zeta23 density.

There is no coefficient-positivity shortcut.  For every nonzero odd packet,

```text
integral_(-L)^L C(y)dy=abs(integral q)^2=0,
C(0)>0,                                               (1.5)
```

so `C` is negative somewhere.  The extra factor `cos(gamma*y)` and the
signed measure `d(psi-v)` each independently destroy a fixed sign.

A stronger packet is obtained by replacing one binomial tail by a binomial
**band**.  It has two opposite endpoint-flat lobes of any fixed width `w>0`,
at distance

```text
s_0=(L/pi)*arcsin sqrt(r_1/R)
    =sqrt(m*L/T)*Theta(1),                            (1.6)
```

from the two endpoints.  After exact coefficient normalization its selected
pair edge is

```text
kappa_band
 =(c_(alpha,w)+o(1))*Y^alpha/L,

Y=exp(L-2*s_0-w)=X^(1-o(1)),
c_(alpha,w)=4*sinh(alpha*w/2)^2/(alpha^2*w)>0.        (1.7)
```

Its autocorrelation splits exactly into two same-lobe correlations and one
opposite-lobe convolution.  The former activate only bounded prime powers
up to a binomially negligible tail.  The latter is concentrated at
`log v=log Y+O(w)` and reduces (1.3), at its power scale, to

```text
S_(Y,w)(gamma)
 =integral v^(-1/2) omega_(T,w)(log(v/Y))
                  cos(gamma*log v)d(psi(v)-v),        (1.8)
```

where `omega_(T,w)` converges to the triangular weight
`(1-abs(u)/w)_+`.  More precisely,

```text
Q_cross(f)/L^2=(1+o(1))*S_(Y,w)(gamma)/L.             (1.9)
```

Consequently the matched missing estimate is

```text
S_(Y,w)(gamma)=o(Y^alpha).                            (1.10)
```

The published KMT pointwise estimate and fixed-order Vaughan/Type-II
recompletions give only

```text
S_(Y,w)(gamma)<<sqrt(Y)/(log Y)^(3/10)
```

(or another `Y^(1/2-o(1))` bound).  Relative to (1.7), the unresolved ratio
is

```text
Y^(1/2-alpha)/(log Y)^(3/10),                         (1.11)
```

which diverges for every fixed `alpha<1/2`.  If a separate sparse multipair
carrier supplied only the scale `X^(2*alpha/3)/L`, its matched scalar target
would instead be `o(X^(2*alpha/3))`; the exponent gap would be still larger.

Under the one-pair/all-other-atoms-on-line carrier theorem, (1.10), uniformly
at every possible selected ordinate, would exclude a pair of depth `alpha`.
Under a general signed carrier theorem it would do the same whenever that
carrier has margin comparable to (1.7).  This is the strongest honest
zero-free implication.  A single real estimate for one weight is not called
an unconditional Turan equivalence here: additional off-line pairs can
screen, and a standalone converse requires a separating family or the
signed carrier theorem.

## 2. Exact Fourier coefficients of the flat tail

Put

```text
x=pi*t/L,
W_(R,r)(u)=sum_(j=r)^R binom(R,j)u^j(1-u)^(R-j),
q_(R,r)(t)=sin(x)*W_(R,r)(cos(x)^2),
p_(R,r)(t)=i*q_(R,r)(t).                              (2.1)
```

The binomial tail has the exact monomial expansion

```text
W_(R,r)(u)
 =sum_(k=r)^R (-1)^(k-r) binom(R,k)binom(k-1,r-1)u^k. (2.2)
```

Indeed the coefficient of `u^k` on the left is

```text
binom(R,k)*sum_(j=r)^k (-1)^(k-j)binom(k,j)
 =(-1)^(k-r)binom(R,k)binom(k-1,r-1).
```

For `0<=ell<=R`, define the rational number

```text
b_ell
 =sum_(k=max(r,ell))^R
    (-1)^(k-r) binom(R,k)binom(k-1,r-1)
    *2^(-2*k)*binom(2*k+1,k-ell)*(2*ell+1)/(2*k+1),

lambda_ell=(2*ell+1)*pi/L.                            (2.3)
```

Differentiating the cosine expansion of `cos(x)^(2*k+1)` gives

```text
sin(x)cos(x)^(2*k)
 =sum_(ell=0)^k 2^(-2*k)binom(2*k+1,k-ell)
    *(2*ell+1)/(2*k+1)*sin((2*ell+1)x).
```

Therefore

```text
q_(R,r)(t)=sum_(ell=0)^R b_ell*sin(lambda_ell*t).     (2.4)
```

In the half-integer critical modes `omega=+/-(ell+1/2)*2*pi/L`, the real
coefficient vector of `p=i*q` is

```text
c_(ell+1/2)=-b_ell/2,
c_(-ell-1/2)=b_ell/2.                                (2.5)
```

Hence

```text
sum c_q^2=(1/2)*sum b_ell^2
         =(1/L)*integral_(-L/2)^(L/2) q(t)^2dt.       (2.6)
```

Equations (2.2)--(2.6) are an exact coefficient certificate; no asymptotic
interpolation determinant is involved.

## 3. Exact zero-extended autocorrelation

For `0<=y<=L`, put

```text
C(y)=integral_(-L/2)^(L/2-y)q(t)q(t+y)dt,
C(-y)=C(y).                                          (3.1)
```

For positive `a,b`, define

```text
I_(a,b)(y)
 =cos((a+b)*y/2)*sin((a-b)*(L-y)/2)/(a-b)
  -cos((a-b)*y/2)*sin((a+b)*(L-y)/2)/(a+b),          (3.2)
```

where the first quotient has its continuous value when `a=b`.  In
particular,

```text
I_(a,a)(y)=(L-y)*cos(a*y)/2-sin(a*(L-y))/(2*a).       (3.3)
```

Centering the overlap interval at `-y/2` and using the product-to-sum
identity proves the exact finite formula

```text
C(y)=sum_(j,k=0)^R b_j*b_k*I_(lambda_j,lambda_k)(y). (3.4)
```

At zero, orthogonality gives

```text
C(0)=L/2*sum b_j^2=L*sum c_q^2.                      (3.5)
```

Now center the absolute critical grid at `gamma` and set

```text
f_gamma(t)=1_[ -L/2,L/2 ](t)*p(t)*exp(-i*gamma*t).
```

Then

```text
R_f(y)=integral f(u)conj(f(u+y))du
      =exp(i*gamma*y)*C(y),                           (3.6)
```

which proves (1.1).  If the permitted common grid center is changed from
`gamma` to `gamma+delta`, the exact phase is
`cos((gamma+delta)y)`.  Since `delta=O(1/L)` and `y` reaches `L`, this phase
change is bounded but not asymptotically zero; a prime estimate must be
uniform in the actual translated phase.

Finally, `q` is odd.  Fubini on the compact support gives (1.5).  Continuity
and (3.5) show that every nonzero such autocorrelation changes sign.  This
rules out the proposed use of coefficient positivity before any estimate of
the primes is attempted.

## 4. Every completed term

The following is stated on the complexification of the repository's real
Weil form.  Equivalently, it is the sum of the real forms of `Re f_gamma`
and `Im f_gamma`, so no extra complex-form assumption is needed.

Let `F_gamma` be the ordinary-frequency Fourier transform used in the Lean
form and put

```text
A_+=integral f_gamma(t)exp(t/2)dt,
A_-=integral f_gamma(t)exp(-t/2)dt.                  (4.1)
```

The exact three pieces are

```text
Pole(f_gamma)=2*Re(A_+*conj(A_-)),                   (4.2)

Arch(f_gamma)
 =integral_R [quarterDigammaReal(2*pi*xi)-log pi]
      *abs(F_gamma(xi))^2 dxi,                       (4.3)

Prime(f_gamma)
 =2*sum_(n<X) Lambda(n)/sqrt(n)
       *C(log n)*cos(gamma*log n).                   (4.4)
```

The harmless convention at `n=X` is immaterial because `C(L)=0`; it may be
included.  Formula (4.2) also has the exact correlation spelling

```text
Pole(f_gamma)
 =4*integral_0^L C(y)cos(gamma*y)cosh(y/2)dy.         (4.5)
```

Splitting `4*cosh(y/2)=2*e^(y/2)+2*e^(-y/2)` and using

```text
d psi(e^y)=sum_n Lambda(n)delta_(log n)(dy),
v^(-1/2)dv=e^(y/2)dy
```

turns `Pole-Prime` into (1.3)--(1.4).  Thus the continuum in `d(psi-v)` is
the `e^(y/2)` half of the pole term, while `R_0` is the other half.  There is
no dropped residue.

### 4.1 Background-size audit

Assume the absolute grid has `d=O(T*L)` modes, all in `[c*T,C*T]`, and
`sum c_q^2=1`.  Directly from (4.1),

```text
abs(A_+)+abs(A_-)
 <=C*X^(1/4)*sqrt(d)/T
 <=C*X^(1/4)*sqrt(L/T),

abs(Pole)<=C*X^(1/2)*L/T.                            (4.6)
```

This keeps the pole term separate rather than relying on cancellation with
the primes.  In the transition regime `X=T^(1+o(1))`, (4.6), divided by
`L^2`, is `o(1)`.

For every autocorrelation with `C(0)=L`, Cauchy--Schwarz gives
`abs(C(y))<=L`.  Hence

```text
abs(R_0)<=4*L.                                       (4.7)
```

The digamma multiplier is bounded below by an absolute constant and grows
only logarithmically.  Plancherel, the endpoint condition, and the fact that
all grid frequencies are `O(T)` give

```text
-C*L <=Arch(f_gamma)<=C*L^2.                         (4.8)
```

Thus `Arch/L^2=O(1)`, `R_0/L^2=O(1/L)`, and the separate pole term is even
smaller.  For fixed `alpha>0`, all three are

```text
o(Y^alpha/L),                                        (4.9)
```

the normalized carrier scale in (1.7).  The upper bound in (4.8) is not
called a small absolute gamma term; it is only power-negligible at the
matched carrier scale.  Its one-sided lower bound is `O(L)`, as needed in a
lower-edge argument.

## 5. A normalized two-lobe binomial band

Let `R asymp T*L`, choose

```text
r_1=ceil(m/2),
s_0=(L/pi)*arcsin sqrt(r_1/R),                        (5.1)
```

and fix `w>0`.  Choose `r_2` to be the nearest integer to

```text
R*sin(pi*(s_0+w)/L)^2.                               (5.2)
```

Assume `r_2<=R`, `r_1/R=o(1)`, and `s_0+w=o(L)`.  Define

```text
B_R(u)=W_(R,r_1)(u)-W_(R,r_2)(u)
      =P(r_1<=Binomial(R,u)<r_2),

q_B(t)=sin(pi*t/L)*B_R(cos(pi*t/L)^2).               (5.3)
```

Every term in `B_R` contains `u^(r_1)`, so `q_B` vanishes to order at least
`2*r_1>=m` at both endpoints.  It is a half-integer trigonometric polynomial
of maximum mode `R+1/2`, hence belongs to the same endpoint-jet coordinate
space as the flat tail.

For `0<=s<=L/2`, put

```text
b(s)=cos(pi*s/L)
     *[W_(R,r_1)(sin(pi*s/L)^2)
       -W_(R,r_2)(sin(pi*s/L)^2)],

J_B=integral_0^(L/2)b(s)^2ds,
a_B=sqrt(L/(2*J_B)),
p_B(t)=i*a_B*q_B(t).                                 (5.4)
```

Since `q_B(L/2-s)=b(s)` and `q_B` is odd, exact orthogonality gives

```text
sum_q c_q^2
 =(a_B^2/L)*integral q_B(t)^2dt
 =(2*a_B^2*J_B)/L=1.                                (5.5)
```

This is the coefficient normalization relevant to the matrix Rayleigh
quotient.

Standard binomial concentration, after the change
`u=sin(pi*s/L)^2`, has physical transition width

```text
Delta s=O(sqrt(L/T)).                                (5.6)
```

For a guard of size `L*sqrt(A/T)`, the two binomial tails outside the guarded
band are `O(X^(-A))`.  Therefore, for fixed `w`,

```text
b(s) -> 1_[s_0,s_0+w](s) in every fixed L^p,
J_B=w+o(1).                                          (5.7)
```

The exact lower-pair evaluation is

```text
F_B(gamma-i*alpha)
 =2*i*a_B*integral_0^(L/2)
      b(s)*sinh(alpha*(L/2-s))ds.                    (5.8)
```

Equations (5.4)--(5.8) give

```text
(2/L^2)*abs(F_B(gamma-i*alpha))^2
 =(1+o(1))*X^alpha*e^(-2*alpha*s_0)/(w*L)
      *[(1-e^(-alpha*w))/alpha]^2
 =(c_(alpha,w)+o(1))*Y^alpha/L,                      (5.9)
```

which proves (1.7).  In the endpoint budget `m/T=O(eta)`, `eta=o(L)`, one
has `s_0=o(L)`, so `Y=X^(1-o(1))`.  Unlike the broad `abs(p)<=1` packet,
the normalization in (5.4) puts amplitude `asymp sqrt(L/w)` on a fixed-width
lobe and recovers the full `1/L` pair scale.

## 6. Exact same-lobe/cross-lobe decomposition

For `y>=0`, define

```text
U_B(y)=integral_R b(s)b(s+y)ds,

D_B(y)=integral_R b(s)b(L-y-s)ds,                    (6.1)
```

where `b` is extended by zero outside `[0,L/2]`.  Splitting the overlap into
left-left, right-right, and left-right pieces gives the exact identity

```text
C_B(y)=a_B^2*[2*U_B(y)-D_B(y)].                      (6.2)
```

There is only one cross term for `y>0`; inserting a factor two in front of
`D_B` would be an error.  In the ideal-band limit (5.7),

```text
U_B(y) ->(w-y)_+,

D_B(log Y+u) ->(w-abs(u))_+,
log Y=L-2*s_0-w.                                     (6.3)
```

Thus the same-lobe part is at bounded logarithmic shifts, while the cross
lobe is the triangular log window at `v asymp Y`.  The exact binomial
functions in (6.1), not the ideal limits, remain in every identity below.

Insert (6.2) into the centered term in (1.3).  With

```text
omega_(T,w)(u)=D_B(log Y+u)/w,                       (6.4)
```

the cross term is exactly

```text
H_cross
 =2*a_B^2*w*S_(Y,w)(gamma)
 =(L*w/J_B)*S_(Y,w)(gamma).                          (6.5)
```

The same-lobe term has only `log v<=w+o(1)` apart from an `O(X^(-A))`
binomial tail.  Positivity of `Lambda`, Chebyshev's bound, and (5.6) give

```text
H_same=O_w(L)+o(1).                                  (6.6)
```

The transition layers of width `O(sqrt(L/T))` contribute at most a
polylogarithm by absolute values when `Y=T^(1-o(1))`; they are also
`o(Y^alpha)` for every fixed `alpha>0`.  Combining (4.7), (5.7), and
(6.5)--(6.6) proves (1.9), with the gamma and pole terms separately bounded
as in Section 4.1.

For reference, the ideal normalized weight has Mellin transform

```text
integral_(-w)^w (1-abs(u)/w)e^(z*u)du
 =4*sinh(z*w/2)^2/(w*z^2),                           (6.7)
```

with its continuous value `w` at `z=0`.  It is nonzero at every real
`z=alpha>0`; localization has not accidentally annihilated the selected
off-line residue.

## 7. The exact arithmetic gate

Partial summation transfers the published KMT sharp-prefix estimate to every
fixed bounded-variation log weight in (6.4).  Since
`log T/log Y ->1`, its range condition still applies when
`Y=X*exp(-o(L))`.  Uniformly for the actual translated phase,

```text
abs(S_(Y,w)(gamma))
 <<_w sqrt(Y)/(log Y)^(3/10).                         (7.1)
```

The variation here is uniform in `T`.  Indeed

```text
d/du W_(R,r)(u)
 =R*binom(R-1,r-1)u^(r-1)(1-u)^(R-r).               (7.1a)
```

The ratio of the two beta densities for `r_1<r_2` is strictly monotone, so
`B_R=W_(R,r_1)-W_(R,r_2)` is a single nonnegative bump and has variation at
most two.  Composition with the monotone map
`u=sin(pi*s/L)^2` preserves variation; multiplying by `cos(pi*s/L)` adds at
most one.  Finally convolution gives

```text
Var(D_B)<=norm(b)_1*Var(b)=O_w(1),
Var(omega_(T,w))=O_w(1).                             (7.1b)
```

Thus (7.1) does not hide a growing derivative loss from the narrowing
binomial transitions.

The continuum part is retained in `S`; direct integration by parts makes it
smaller than the right side.  No prime power is removed.  Equations
(5.9), (6.5), and (7.1) give the exact normalized comparison

```text
[abs(H_cross)/L^2]/kappa_band
 <<_(alpha,w) Y^(1/2-alpha)/(log Y)^(3/10).           (7.2)
```

This proves (1.11).  A Vinogradov--Korobov or fixed-order Type-II estimate of
shape `Y^(1/2-o(1))` has the same exponent defect.

The faithful missing theorem is therefore:

> For some fixed `alpha<1/2` and fixed `w>0`, uniformly at every selected
> core ordinate and permitted common grid translation, prove
> `S_(Y,w)(gamma)=o(Y^alpha)` at the carrier-selected
> `Y=X*exp(-o(log X))`.

Together with the one-pair/on-line carrier theorem this excludes a pair of
that depth.  To handle the actual zeta zero set, one must additionally prove
the general signed carrier margin or an estimate strong enough to absorb all
other off-line pairs.  Conversely, a pre-existing zero-free boundary
`Re rho<=1/2+alpha-delta` gives a fixed-power bound for the smooth version of
(1.8) by the standard Mellin-contour shift.  These two implications explain
why (1.10) is strip-strength, but they do not turn one real packet estimate
without a carrier into a standalone if-and-only-if theorem.

## 8. The ordinary-product component is not annihilated

The identity

```text
Lambda=A*1,
A(q)=(mu*Lambda)(q)=-mu(q)log q                       (8.1)
```

gives the exact completion-preserving ordinary-product spelling of (1.8):

```text
S_(Y,w)(gamma)
 =Re sum_(q,m>=1) A(q)*(q*m)^(-1/2+i*gamma)
       *omega_(T,w)(log(q*m/Y))
   - continuum.                                      (8.2)
```

All Vaughan heads, common-factor sectors, and product fibers are represented
in (8.2).  The coefficient of the ordered product `(q,m)` is exactly

```text
A(q)*(q*m)^(-1/2+i*gamma)
     *omega_(T,w)(log(q*m/Y)).                        (8.3)
```

After summing `q|n`, its arithmetic coefficient is exactly

```text
Lambda(n)*n^(-1/2+i*gamma)
     *omega_(T,w)(log(n/Y)).                          (8.4)
```

It is not zero.  In fact `b(s)>0` for `0<s<L/2`, so `D_B(y)>0` for every
interior cross shift; every prime power in the effective cross window has a
nonzero coefficient in (8.4).

The moment identity `integral C_B=0` does not contradict (8.2).  It is the
zero **Mellin-frequency** coefficient of the complete autocorrelation.  The
ordinary/zero-conductor sector in the R128 chirp decomposition means zero
**modular reciprocal phase** and still carries the Dirichlet phase
`(q*m)^(i*gamma)` and the pointwise product weight.  These are different
notions of zero mode.  The relevant ideal cross Mellin coefficient is (6.7),
which is strictly positive at every real depth `alpha>0`.

Consequently the binomial band does not unlock a theorem that applies only
to nonzero reciprocal phases.  Wright-type fixed savings for such phases
still omit the exact ordinary component (8.2); approximate moment
cancellation cannot replace coefficientwise annihilation.

## 9. The sparse `k=3` alias and the shorter prime scale

The sparse tapered `k=3` screen has a potentially useful second geometry.
Its surviving negative alias is `q=2`, on

```text
t+u=2*L/3.                                           (9.1)
```

A normalized real packet with opposite fixed-width lobes near `+L/3` and
`-L/3` has a negative cross-autocorrelation near

```text
y=2*L/3,
Y=exp(2*L/3)=X^(2/3),
gamma asymp T asymp X=Y^(3/2).                       (9.2)
```

The same coefficient normalization as Section 5 gives a zero-side alias
margin

```text
kappa_(k=3) asymp Y^alpha/L=X^(2*alpha/3)/L.         (9.3)
```

The completed prime side is again (1.8), now with length `Y` and height
`gamma=Y^(3/2+o(1))`.  KMT remains applicable in this range and yields only

```text
S_(Y,w)(gamma)<<sqrt(Y)/(log Y)^(3/10).              (9.4)
```

The larger ratio `gamma/Y=Y^(1/2)` does create curvature in an unweighted
one-variable sum.  It does not survive the completion-preserving balanced
Vaughan block.  Equation (8.2) factors its phase exactly as

```text
(q*m)^(i*gamma)=q^(i*gamma)*m^(i*gamma).             (9.5)
```

On a Type-II box the two factors in (9.5) are absorbed into the two
coefficient sequences.  Cauchy or the large sieve then gives no curvature
gain.  Recovering a gain from the actual first sequence requires cancellation
in

```text
-mu(q)log(q)*q^(i*gamma),                            (9.6)
```

which is the same `A'=(1/zeta)'` ordinary component exposed by the exact
all-head recompletion.  Dropping it and estimating only a nonzero
reciprocal-phase sector is not completion preserving.

Thus the `k=3` geometry gives a real screen-versus-shorter-prime-scale
dichotomy, but no currently applicable fixed saving.  Its matched gate is

```text
S_(Y,w)(gamma)=o(Y^alpha),                            (9.7)
```

and (9.4)/(9.3) again leaves

```text
Y^(1/2-alpha)/(log Y)^(3/10).                        (9.8)
```

For fixed `alpha<1/2` this is still strip-strength when coupled to the sparse
carrier.  This audit does not assert that no future coefficient-specific
prime theorem can exploit `gamma=Y^(3/2)`; it proves that ordinary phase
curvature, generic Type-II bounds, and the currently audited reciprocal
theorems do not do so after exact recompletion.

## 10. Prime-translate nulling: an exact live projection criterion

There is a sharper finite-dimensional candidate which dimension counts alone
do not settle.  Fix one lobe `r` and let `E` be the allowed coefficient
space for an opposite bandlimited lobe.  For every active prime power in the
cross window put

```text
v_n=P_E T_(log n-log Y)r.                             (10.1)
```

Let `p_+`, `p_-` denote the two projected pole vectors, let `x_alpha` be the
projected positive-mate vector if it is not already removed by parity, and
let `a_alpha` be the projected Laplace evaluation vector for the desired
negative mate.  Define

```text
S_(r,Y)=span({v_n: n is an active prime power}
             union {p_+,p_-,x_alpha}).               (10.2)
```

For a genuinely free opposite lobe `ell in E`, the simultaneous conditions

```text
<ell,v_n>=0 for every n,
<ell,p_+>=0,  <ell,p_->=0,  <ell,x_alpha>=0          (10.3)
```

are linear.  The exact optimum is

```text
sup_(ell in S_(r,Y)^perp, norm ell=1)
       abs(<ell,a_alpha>)
 =norm(P_(S_(r,Y)^perp)a_alpha).                     (10.4)
```

Thus the full-scale carrier condition is not merely that the nullspace in
(10.3) be nonzero.  In coefficient normalization it is the quantitative
leverage bound

```text
dist(a_alpha,S_(r,Y))^2 >=c*L*Y^alpha.               (10.5)
```

The naive count

```text
dim(E) asymp T*w,
# prime constraints asymp Y*w/log Y                  (10.6)
```

does imply a large algebraic kernel when `Y asymp T`.  It says nothing about
(10.5).  A vector may lie within `exp(-c*T*w)` of a lower-dimensional span;
dimension does not control the smallest singular value of this prime-translate
frame.  If (10.5) held uniformly, (10.3) would remove the power-sized prime
and pole terms while retaining the off-line evaluation, and the carrier plus
explicit formula would give the desired depth-`alpha` exclusion.  Therefore
a uniform lower bound of the size (10.5) is itself strip-strength, not a
routine consequence of (10.6).

There is a real-admissibility point before applying (10.4) to the present
matrix, but Hermitian complexification resolves it.  A real coefficient
vector on the symmetric relative grid satisfies exactly

```text
p(-t)=conj(p(t)).                                    (10.7)
```

Hence its two time lobes are conjugate reflections, not independent vectors
`r` and `ell`.  Allowing them to vary independently gives a complex
polarized packet.  If `A` is the real symmetric completed matrix and
`z=x+i*y`, however, then

```text
conj(z)^T*A*z=x^T*A*x+y^T*A*y.                       (10.8)
```

Thus a negative **total** completed form for the polarized complex packet
already gives a negative admissible real Rayleigh vector, either `x` or
`y`.  Its prime nulls and negative carrier need not descend term by term;
only the negative total is used.  Independent complex lobes are therefore
legitimate for this route.  What remains unresolved is quantitative: the
cross correlation has a sharp Wiener `l^1` factorization norm, and neither
dimension nor an `l^2` prolate estimate controls the required target angle.
See
[`ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md`](ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md).

This route should remain live rather than be dismissed.  A successful next
step would be either

1. a stable lower frame bound proving (10.5) in an admissible real subspace;
   or
2. an upper frame/completeness theorem showing that the Laplace vector is at
   distance `o(sqrt(L*Y^alpha))` from (10.2).

At present neither statement is proved.  The exact atomic dual and the KMT
quadrature give only a logarithmic upper bound for the optimized leverage;
this rules out a fixed positive asymptotic constant but retains the full
power exponent.  Exact pointwise prime-null tests in
the wider repository show why an unconditioned dimension argument is unsafe:
their interpolation cost reappears as remote spectral aliases or an
exponentially poor condition number.  The localized frame (10.2) is more
economical and deserves a direct singular-value computation, but that
computation cannot be replaced by counting constraints.

## 11. Why the apparent escapes do not change the exponent

1. **Positivity.**  Equations (1.5) and (6.2) show that the negative
   cross-lobe is intrinsic.  Positive von Mangoldt coefficients are paired
   with `C(y)cos(gamma*y)` and then centered by `d(psi-v)`.

2. **Exact pole cancellation.**  Centering performs the exact cancellation
   already displayed in (1.3).  What remains is (1.8), not zero.  The
   rational remainder is only `O(L)`.

3. **Abel summation.**  Differentiating the phase costs
   `gamma/v`; using only a PNT bound for `psi(v)-v` loses the transition-scale
   oscillation.  Retaining it leads back to the twisted von Mangoldt
   polynomial in (1.8).

4. **Vaughan/Type II.**  Recompletion restores all heads and the ordinary
   centered dual.  Available pointwise estimates give (7.1), not a fixed
   exponent below `1/2`.

5. **Phase averaging.**  A lobe of width `w` retains the pair evaluation only
   over a modulation range `Delta gamma=O(1/w)`.  Montgomery--Vaughan on that
   range has root scale `w*sqrt(Y)` for the unnormalized triangular window,
   while (5.9) loses the same factor `w` when `w` is narrowed.  The ratio is
   again `Y^(1/2-alpha)` up to logarithms.  The selected zero ordinate is
   pointwise, so an almost-all phase theorem would in any event leave the
   required exceptional ordinate untreated.

The localized packet is therefore a genuine improvement of the zero-side
carrier scale and a useful scalarization of the arithmetic task.  It does
not supply the fixed-power cancellation which that scalarization exposes.
