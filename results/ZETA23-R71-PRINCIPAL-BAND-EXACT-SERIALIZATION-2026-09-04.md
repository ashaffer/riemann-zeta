# ZETA23 R71 principal-band exact serialization and top-box closeout

Date: 2026-09-04  
Registry target: R188  
Status: exact finite serialization and low-denominator suppression proved;
global fixed-power estimate fails the imported-Wright scale test and remains
open

Preflight:
[`zeta23_r188_principal_band_serialization_preflight_v1.json`](context/zeta23_r188_principal_band_serialization_preflight_v1.json)  
Literature log:
[`zeta23_r188_principal_band_literature_search_2026-09-04.json`](context/zeta23_r188_principal_band_literature_search_2026-09-04.json)

This report is a theorem-passport continuation of R187.  Its exact
tail-to-R81 bridge is the local-predecessor theorem in
[`R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md`](R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md),
not a new bridge.  The R188 delta is to insert R187's smooth additive
principal multiplier and affine center without losing the physical cutoff,
and then to audit global applicability.  The classification is
**LOCAL_PREDECESSOR + PROJECT_SYNTHESIS**.  No literature-novelty claim is
made.

## 0. Verdict

Freeze

```text
eta=nu=1/100,       k=4,       U=V=floor(X^(9/20)),
delta=X^(-1+nu)=X^(-99/100).                            (0.1)
```

There is an exact completion-preserving finite serialization of R187's
principal field.  In the direct cofactor coordinate its outer coefficient
has polylogarithmic `l1` and weighted `l2` cost; the affine center remains as
an explicit constant/logarithmic density, and the complete quadratic form
retains tail--tail, both tail--center terms, and center--center.  Smooth
principal localization suppresses every nonzero alias with denominator
`q << delta^(-1)=X^(99/100)` by an arbitrary fixed power.  Thus the
effective principal geometry has

```text
q >= X^(99/100+o(1)),       |a| <= X^(1/100+o(1)),
physical free quotient <=X^(1/100+o(1)).               (0.2)
```

Using the window's full fifth-order Fourier decay at the target scale gives
the sharper equivalent collar

```text
q > X^(499/500),       |a| <= X^(1/400),
physical free quotient <=X^(1/500+o(1)).              (0.2a)
```

The discarded field has size `X^(49/100+o(1))`, exactly the square-root
target scale, so (0.2a) is an exponent-equivalent reduction rather than a
power saving.  The exact completed residual remains inside the collar.

Accordingly, the live obstruction is a high-denominator rational principal
(major-arc/projector) sector, not the analytic additive-frequency tail that
R187 already bounded.

It does **not** follow that determinants are small.  The same core contains
determinant one, determinant of order `X`, and reducible pairs.  In
particular the `g=1`, `M=N=X`, `J=Theta=X`, `|j theta|=X^2=MN` box remains.
Wright's recorded scalar bound on it is

```text
X^(15/8+o(1)),
```

whereas the elementary physical energy scale is `X^(1+o(1))`.  Principal
localization does not remove this box, and the finite
`gamma=mu_>U*Lambda_>V` coordinate preserves a natural-size top-semiprime
subfamily.  Therefore the previously tempting balanced budget
`1/40-1/200=1/50` is **not a global endpoint** and must not be counted.

The exact adapter succeeds algebraically and fails analytically.  A crude
pre-integration-by-parts R84 Mellin ledger can pay
`(1+Z)^(1/2)<=X^(1/200+o(1))`, but this is not an unavoidable projective
loss: R104's full ledger has `(1+Z)^(1/2-B)` and removes large `Z` by
integration by parts.  The decisive top box has `Z` constant and fails even
with subpower projective cost.  No `X^(49/50)` completed bound, zero-free
strip, four-cycle bound, or RH theorem is proved.

## 1. Exact test and cutoff passport

Use the Fourier convention

```text
e(x)=exp(2*pi*i*x),       fhat(xi)=integral f(t)e(-xi*t)dt.  (1.1)
```

Let `r=R+s`, with `s` in the frozen compact output block, and put

```text
f_r(t)=t^(-1/2)V(r-log t).                              (1.2)
```

There are fixed `0<c_0<c_1` such that every `f_r`, and every one of the
finitely many `2h`-shifted windows entering the prelocalized `f_r^Q` below,
is supported in `[c_0 X,c_1 X]`.  Choose once and for all

```text
chi in C_c^infinity((0,infinity)),
chi=1 on an open neighbourhood of [c_0,c_1],
chi_X(t)=chi(t/X),       supp(chi_X) subset [cX,CX],    (1.3)
```

where `0<c<c_0<c_1<C`.  Let `m` be the fixed even multiplier from R187,
equal to one on `[-1,1]` and supported in `[-2,2]`, and define

```text
phi_r=F^(-1)[m(xi/delta) fhat_r(xi)],
Phi_r(t)=chi_X(t)phi_r(t).                              (1.4)
```

The multiplication by `chi_X` in (1.4) is essential: the inverse low-pass
`phi_r` is Schwartz but is not compactly supported.  If `P_R` is R187's
Fourier transform of the signed measure after restriction by `chi_X`, then
Fubini and Fourier inversion give exactly

```text
G_R^pri(r)=integral Phi_r(t)dmu_R(t),                   (1.5)

dmu_R=sum_n a(n)delta_n-(A_R+B_R log t)dt,
a=(mu_>U*Lambda_>V)*1.                                 (1.6)
```

Thus no boundary atom, center term, or low-pass tail has been silently
deleted.

## 2. Finite gamma plus affine serialization

Put

```text
gamma(q)=(mu_>U*Lambda_>V)(q),       a=gamma*1,
T=ceil(CX)+1,
C_T=sum_(q<=T)gamma(q)/q,
ell_T(t)=C_T-A_R-B_R log t,                           (2.1)

D_q[Phi]=sum_(j>=1)Phi(qj)-q^(-1)integral Phi(t)dt.   (2.2)
```

### Theorem 2.1 (exact finite completion)

For every test `Phi in C_c^infinity((0,T))`, and hence for every `Phi_r` in
(1.4),

```text
sum_n a(n)Phi(n)-integral(A_R+B_R log t)Phi(t)dt
 =sum_(q<=T)gamma(q)D_q[Phi]
   +integral ell_T(t)Phi(t)dt                           (2.3)

 =sum_(q<=T)gamma(q)/q sum_(b!=0)Phihat(b/q)
   +integral ell_T(t)Phi(t)dt.                          (2.4)
```

Every sum in (2.3)--(2.4) is finite in `q`, and the alias sum is absolutely
convergent.  The identity preserves the rectangular Vaughan order.

#### Proof

Since `a=gamma*1` and `Phi` is supported below `T`,

```text
sum_n a(n)Phi(n)=sum_(q<=T)gamma(q)sum_(j>=1)Phi(qj).  (2.5)
```

Adding and subtracting
`sum_(q<=T)gamma(q)q^(-1) integral Phi` gives (2.3).  Extend `Phi` by zero.
Poisson summation gives

```text
D_q[Phi]=q^(-1)sum_(b!=0)Phihat(b/q),                  (2.6)
```

because negative and zero physical samples vanish and the Fourier zero mode
is exactly the subtracted integral.  Smooth compact support gives absolute
alias convergence.  All divisors `d,b,q` and physical quotients meeting the
test support are finite, so no conditionally convergent cofactor identity or
changed limiting order is used.  QED.

The point of `ell_T` is completion, not an error estimate.  Its two channels
are

```text
(C_T-A_R)dt,             -B_R log(t)dt.                (2.7)
```

One scalar cofactor zero mode cannot replace a genuinely affine center on a
whole output interval.

### Theorem 2.2 (the complete square)

Let

```text
L_R(t,u)=integral psi_R(r)Phi_r(t)conjugate(Phi_r(u))dr,
Lhat_R(xi,eta)=double_integral L_R(t,u)e(-xi*t-eta*u)dtdu,
L_ell(t)=integral L_R(t,u)ell_T(u)du,
Lhat_ell(xi)=integral L_ell(t)e(-xi*t)dt.              (2.8)
```

Then exactly

```text
E_R^pri
 =sum_(q1,q2<=T) gamma(q1)gamma(q2)/(q1*q2)
    sum_(a,b!=0)Lhat_R(-a/q1,b/q2)
  +2 Re sum_(q<=T)gamma(q)/q sum_(a!=0)Lhat_ell(-a/q)
  +double_integral L_R(t,u)ell_T(t)ell_T(u)dtdu.       (2.9)
```

Changing all alias signs gives the same formula.  Equation (2.9) contains
tail--tail, both conjugate tail--center terms, and center--center before any
absolute value.  It is simply (2.4) squared and Fubini applied to finite
outer sums; no cancellation has been asserted.

## 3. Coefficient ledgers and reduced rationals

The elementary divisor identity gives

```text
gamma(q)=0 for q<=UV,
|gamma(q)|<=sum_(b|q)Lambda(b)=log q.                  (3.1)
```

Consequently, with `h(q)=gamma(q)/q`,

```text
sum_(q<=T)|h(q)|                  <<log^2(2T),
sum_(q<=T)q|h(q)|^2              <<log^3(2T),
sum_(q>UV)|h(q)|^2               <<log^2(2UV)/(UV),
|C_T|                            <<log^2(2T).          (3.2)
```

Thus the direct nonprimitive outer coefficient has `X^o(1)` `l1` cost and
`X^o(1)` weighted Hilbert cost.  This does not estimate the coherent alias
sum inside each cofactor.  R187's `A_R,B_R=R^O(1)`, together with (3.2),
also makes the affine residual a two-channel `X^o(1)` coefficient family.
Its field and cross-term sizes need not be subpower; the statement concerns
only serialization cost.

There is also an exact finite reduced-rational basis.  For `n<=N`, define

```text
what_N(d)=sum_(k<=N/d)gamma(dk)/(dk).                  (3.3)
```

The identity `q 1_(q|n)=sum_(d|q)c_d(n)` gives

```text
a(n)=sum_(d<=N)what_N(d)c_d(n),
|what_N(d)|<<log^2(2N)/d.                              (3.4)
```

On positive tests supported below `N`, this yields exactly

```text
sum_n a(n)delta_n-(A_R+B_R log t)dt
 =[what_N(1)-A_R-B_R log t]dt
  +what_N(1)sum_(j!=0)e(jt)dt
  +sum_(2<=d<=N)what_N(d)
     sum_((r,d)=1,1<=r<d)sum_(j in Z)e((j+r/d)t)dt.    (3.5)
```

The coefficient bounds are

```text
sum_(d<=N)|what_N(d)|                  <<log^3(2N),
sum_(d<=N)phi(d)|what_N(d)|^2          <<log^5(2N).    (3.6)
```

Hence the Ramanujan/Hilbert coefficient cost is `X^o(1)`.  By contrast,
expanding every reduced residue as an independent scalar and taking a
triangle inequality has only the crude ledger

```text
sum_(d<=N)phi(d)|what_N(d)| << N log^2(2N),            (3.7)
```

which is not subpower.  A vector or complete-residue theorem is therefore
required; (3.6) does not license scalar `l1` summation over all residues.

### Proposition 3.1 (the finite Vaughan tail is pole-faithful)

For `Re(s)>1`, let

```text
M_U(s)=sum_(d<=U)mu(d)d^(-s),
L_V(s)=sum_(b<=V)Lambda(b)b^(-s),
mathcal A_(U,V)(s)=sum_n a(n)n^(-s).                   (3.8)
```

Then, first by absolutely convergent Dirichlet convolution and afterwards
by meromorphic continuation,

```text
mathcal A_(U,V)(s)
 =zeta(s)[1/zeta(s)-M_U(s)]
          [-zeta'(s)/zeta(s)-L_V(s)]
 =[1-zeta(s)M_U(s)]
          [-zeta'(s)/zeta(s)-L_V(s)].                 (3.9)
```

At every nontrivial zero `rho` of `zeta`, the first factor in the last line
equals one, while the second retains the logarithmic derivative's simple
pole, whose residue records the zero multiplicity.  Thus finite gamma
factorization has not removed
or weakened the nontrivial-zero carrier.  The prelocalized `Q_h` multiplier
on that zero mode is

```text
[exp(h(rho-1/2))-exp(h/2)]^2,                         (3.10)
```

which is nonzero for every nontrivial zeta zero, as audited in R102.  This
is a pole-level reason, independent of the top-box norm calculation, that
neither the finite Vaughan coordinate nor faithful center annihilation makes
the endpoint a coefficient-free estimate.

## 4. Low denominators are suppressed, not deleted

The exact cutoff in (1.4) broadens the strict multiplier support.  The
correct statement is an arbitrary-power leakage estimate, not compact
support of `Phi_r` in Fourier space.

### Theorem 4.1 (low-cofactor suppression)

Uniformly in the frozen output block and for every fixed `A>=1`,

```text
|Phihat_r(xi)|
 <<_A X^(1/2)
   [1+X dist(xi,[-2delta,2delta])]^(-A).               (4.1)
```

It follows that, for `q<=(4delta)^(-1)`,

```text
sum_(a!=0)|Phihat_r(a/q)|
 <<_A X^(1/2)(q/X)^A,                                 (4.2)
```

and for every fixed `D>0`,

```text
sum_(q<=(4delta)^(-1)) |gamma(q)|/q
    sum_(a!=0)|Phihat_r(a/q)|
 <<_D X^(-D).                                         (4.3)
```

Let `G_low` denote only the gamma nonzero-alias sum on the left of (4.3),
and put `G_high=G_R^pri-G_low`; in particular, the whole `ell_T` term remains
in `G_high`.  Then, after increasing `D`,

```text
integral psi_R|G_R^pri|^2
 =integral psi_R|G_high|^2+O_D(X^(-D)).                (4.3a)
```

Thus the low-`q` gamma line, its self energy, and its cross term with the
completed high part are smaller than every prescribed fixed power.  No part
of the affine residual is being called a low-denominator error.

#### Proof

Product-convolution and scaling give

```text
Phihat_r(xi)
 =integral X chihat(X(xi-zeta))
     m(zeta/delta)fhat_r(zeta)dzeta.                  (4.4)
```

The second factor is supported on `|zeta|<=2delta`; the order-four window
has uniformly integrable scaled Fourier transform, so
`integral |m fhat_r| <<X^(-1/2)`.  The Schwartz decay of `chihat` proves
(4.1).  If `q<=(4delta)^(-1)`, then for every `a!=0`

```text
dist(a/q,[-2delta,2delta])>=|a|/(2q).                 (4.5)
```

Apply (4.1) with exponent `A+2`, sum the resulting convergent series in
`a`, and relabel the exponent to obtain (4.2), including at `A=1`.
Finally use `|gamma(q)|<=log q`:

```text
X^(1/2-A)sum_(q<=(4delta)^(-1))(log q)q^(A-1)
 <<X^(1/2)(X^(-nu))^A log X.                          (4.6)
```

Since `nu=1/100` is fixed, choosing `A` proves (4.3) for arbitrary `D`.
QED.

Similarly, aliases with `|a|/q` outside any fixed enlargement of
`[-2delta,2delta]` are power-small.  Thus the surviving core has, at exponent
scale,

```text
q>=X^(99/100),       |a|<=2*delta*q<<X^(1/100),
n=q*v<=CX  ==>  v<=X^(1/100+o(1)).                    (4.7)
```

This is a high-cofactor/small-physical-quotient statement.  It is not a
low-determinant statement.

### Theorem 4.2 (target-matched cofactor/alias collar)

Let

```text
Q_X=floor(X^(499/500)),       A_X=floor(X^(1/400)),

G_collar(r)=integral ell_T(t)Phi_r(t)dt
 +sum_(Q_X<q<=T)gamma(q)/q
      sum_(0<|a|<=A_X)Phihat_r(a/q).                  (4.8)
```

Uniformly in the fixed output block,

```text
||G_R^pri-G_collar||_infinity
 <<X^(49/100)log^2X=X^(49/100+o(1)).                 (4.9)
```

Consequently, by weighted `L2` Minkowski in both directions,

```text
integral psi_R|G_R^pri|^2 <=X^(49/50+o(1))
 iff
integral psi_R|G_collar|^2 <=X^(49/50+o(1)).         (4.10)
```

Every center and energy cross term is retained through the field-level
definition (4.8); (4.10) does not estimate sectors independently.  On the
retained physical support `q*v<=CX`, one has

```text
q>X^(499/500),       v<=C X^(1/500)=X^(1/500+o(1)),
0<|a|<=X^(1/400).                                  (4.11)
```

#### Proof

In scaled variables, `f_r(Xu)=X^(-1/2)F_s(u)` and the order-four window
gives

```text
|Fhat_s(w)|<<[1+|w|]^(-5).                           (4.12)
```

Writing the compactified low pass as a scaled convolution gives exactly

```text
Phihat_r(xi)
 =X^(1/2){chihat * [m(w/(X*delta))Fhat_s(w)]}(X*xi).
                                                               (4.13)
```

Schwartz decay of `chihat` and (4.12) therefore imply the uniform global
bound

```text
|Phihat_r(xi)|<<X^(1/2)[1+X|xi|]^(-5).               (4.14)
```

For `q<=Q_X`, summing (4.14) over every nonzero integer alias gives

```text
sum_(a!=0)|Phihat_r(a/q)|
 <<X^(1/2)(q/X)^5.                                   (4.15)
```

Using `|gamma(q)|<=log q` and summing `q^4 log q` yields

```text
sum_(q<=Q_X)|gamma(q)|/q sum_(a!=0)|Phihat_r(a/q)|
 <<X^(1/2)(Q_X/X)^5 log^2X
 <<X^(49/100)log^2X.                                 (4.16)
```

For `q>Q_X`, the aliases with `|a|>A_X` instead satisfy

```text
sum_(|a|>A_X)|Phihat_r(a/q)|
 <<X^(1/2)(q/X)^5 A_X^(-4)
 <<X^(1/2)A_X^(-4),                                  (4.17)
```

because `q<=T<<X`.  The first estimate in (3.2) now gives

```text
sum_(q>Q_X)|gamma(q)|/q sum_(|a|>A_X)|Phihat_r(a/q)|
 <<X^(1/2)A_X^(-4)log^2X
 <<X^(49/100)log^2X.                                 (4.18)
```

The exponent identities are exact:

```text
1/2-5/500=49/100,       1/2-4/400=49/100.            (4.19)
```

Equations (4.16)--(4.18) prove (4.9), and Minkowski proves (4.10).
The quotient claim follows from `q*v<=CX`.  Here `v=n/q` is the physical
divisor quotient; it is unrelated to the solution-line Poisson dual variable
`j` in Section 5 and the dyadic parameter `J` in Section 7.  QED.

If desired, fixed retreats
`Q_X=X^(499/500-epsilon)` and
`A_X=X^(1/400+epsilon)`, with `0<epsilon<3/400`, make the two error
exponents `49/100-5epsilon` and `49/100-4epsilon`.  Allowing `epsilon` to
tend sufficiently slowly to zero gives the shorthand
`q>=X^(.998-o(1))`, `v<=X^(.002+o(1))`, and
`|a|<=X^(.0025+o(1))`.  None of these refinements removes a unit alias or a
top cofactor.

## 5. Exact determinant and reciprocal serialization

Apply (2.9) to the tail--tail line.  Write

```text
q1=g*m,       q2=g*n,       (m,n)=1,
theta=a*n-b*m.                                               (5.1)
```

The R81/R87 solution-line change of variables is exact.  If
`a=a_0+m*l`, `b=b_0+n*l`, and `a_0 n=theta (mod m)`, then Poisson summation
in `l` gives

```text
A_(g,m,n,theta)(j)
 =g integral L_R(u+g*j,u)e(theta*u/(g*m*n))du,         (5.2)

sum_l H(l+a_0/m)
 =sum_(j in Z)e(j*theta*inverse(n)/m)
      A_(g,m,n,theta)(j).                              (5.3)
```

Completing the line introduces the exact axis correction

```text
-1_(m|theta)Lhat_R(0,-theta/(gmn))
-1_(n|theta)Lhat_R(-theta/(gmn),0)
+1_(theta=0)Lhat_R(0,0).                               (5.4)
```

The cross and affine lines in (2.9) remain beside (5.2)--(5.4); they are not
absorbed into a scalar `theta=0` term.  Since the direct gamma expansion is
finite, the `q1,q2`, determinant, and solution-line rearrangements are
unconditional and preserve the original rectangular summation order.

If the finite reduced-rational basis is used instead, primitivity produces
the line mask

```text
M_g(l)=1_((a_0+m*l,g)=1)1_((b_0+n*l,g)=1).             (5.5)
```

At each prime `p|g`, this excludes at most two residues.  The normalized
local Fourier `l1` norm is at most `3`; CRT therefore gives

```text
sum_(xi mod g)|Mhat_g(xi)|<=3^omega(g)=g^o(1).         (5.6)
```

Prime powers do not increase the norm because (5.5) depends only on the
residue modulo `p`.  Thus this particular primitive mask has subpower
Fourier-algebra cost.  The direct nonprimitive gamma coordinate avoids the
mask entirely.  The norm bound alone does not prove compatibility with a
scalar imported theorem: fiber Poisson shifts the amplitude by fractions of
`1/g`, and no theorem here converts all such fractional shifts into Wright's
integer numerator/fixed-conductor hypotheses at subpower cost.

On the effective principal support,

```text
|theta|/(gmn)=|a/q1-b/q2|<<delta,
Z=|theta|X/(gmn)<<X^nu=X^(1/100).                      (5.7)
```

If one stops at the crude R84 Mellin separation before nonstationary-phase
summation, it costs `(1+Z)^(1/2)`.  Its worst value on (5.7) is

```text
X^(nu/2+o(1))=X^(1/200+o(1)).                         (5.8)
```

This crude intermediate charge is not the final all-box ledger.  R104
(8.10) replaces it by `(1+Z)^(1/2-B)` after repeated integration by parts,
so `Z>>1` is harmless when the available smoothness order `B` is chosen.
Algebraic dyadic, divisor, outer-cofactor, and primitive-mask costs are
subpower, and the final `Z=O(1)` projective cost is subpower.  Thus the
projective ledger itself is not the decisive obstruction.  The obstruction
below occurs at `Z asymp 1`, where no factor in (5.8) is paid.

## 6. Hostile geometry inside the same principal core

High denominator does not imply one determinant regime.  Choose a fixed
`0<c_*<C/2` and an integer `Q asymp c_*X`.  The unit aliases give all three
witnesses inside the physical cutoff:

```text
(q1,q2,a,b)=(Q,Q+1,1,1):       g=1, theta=1;
(q1,q2,a,b)=(Q,2Q-1,1,1):      g=1, theta=Q-1;
(q1,q2,a,b)=(Q,2Q,1,1):        g=Q, (m,n)=(1,2).       (6.1)
```

All satisfy `1/qi<=delta` for large `X`.  Thus principal localization
retains low determinant, high determinant, and a reducible face.

The top arithmetic family is equally explicit.  Let `q=p*r`, where `p,r`
are distinct primes in fixed square-root intervals and hence exceed
`U=V=X^(9/20)`.  Then

```text
gamma(pr)=mu(p)Lambda(r)+mu(r)Lambda(p)
         =-(log p+log r)=-log(pr).                    (6.2)
```

The prime number theorem supplies `asymp X/log^2 X` such products in a
fixed-ratio top interval, and therefore

```text
sum_(q=pr asymp X)|gamma(q)/q|^2=X^(-1+o(1)).         (6.3)
```

For `a=1`, the uncompactified principal multiplier factor is identically one
because

```text
X^(99/100)/q<<X^(-1/100)<1.                           (6.4)
```

After multiplication by `chi_X`, this is no longer a literal Fourier-support
identity; the compactified response is instead asymptotic to the same main
term, uniformly as stated in (6.6).

### Proposition 6.1 (the isolated unit-alias block is natural size)

Assume, as in R187, that `psi_R` is nonzero and nonnegative.  There are fixed
square-root prime intervals and a fixed subinterval of the output block for
which, with `S_X` the corresponding distinct semiprimes,

```text
integral psi_R(r)
  |sum_(q in S_X)gamma(q)/q Phihat_r(1/q)|^2dr
 >>X/log^2 X=X^(1-o(1)).                               (6.5)
```

#### Proof

In scaled variables, for `r=R+s` and `q/X` in a fixed compact subinterval of
`(0,C)`, Fourier convergence of the smooth low pass gives uniformly

```text
X^(-1/2)Phihat_r(1/q)
 =mathcal F_s(X/q)+o(1),
mathcal F_s(y)=integral u^(-1/2)V(s-log u)e(-yu)du.    (6.6)
```

The physical cutoff causes no main term in (6.6): `chi=1` on a
neighbourhood of the support of the limiting scaled function, while the
scaled multiplier radius `X*delta=X^(1/100)` tends to infinity.  For any
`s` at which `psi_R(R+s)>0`, `mathcal F_s` is the Fourier transform of a
nonzero compactly supported function.  It cannot vanish on an interval.
Choose a positive `y`-interval on which, after one fixed rotation, its real
part is bounded below, and choose two disjoint fixed square-root prime
intervals whose product ratios have `X/q` in that interval.  The PNT gives

```text
#S_X asymp X/log^2 X,       |gamma(q)/q|asymp log X/X. (6.7)
```

All coefficients have the same negative sign by (6.2), and the response
phases lie in one fixed half-plane.  The field in (6.5) therefore has size
`\gg sqrt(X)/log X` on a fixed output subinterval.  Squaring and integrating
proves (6.5).  QED.

This is the standard R105 top-semiprime witness, sharpened to the literal
unit-alias Gram block.  It is **not** a lower bound for the completed field
(2.9), because the other aliases, reducible terms, and affine cross terms may
cancel it.  It does prove that this channel cannot be bounded separately by
`X^(49/50+o(1))`.  The same proof works after prelocalized `Q_h`: replace
`V` by the nonzero compact window `V_Q`; its zero continuum moment is only
the value at scaled frequency zero and does not annihilate a whole interval.

## 7. Exact Wright scale test

For the `g=1` top box, the physical kernel permits

```text
M=N=X,       Theta=X,       J=X,
K_0=|j theta|=X^2=MN,       Z=1.                      (7.1)
```

This is inside the repository-audited range of the weaker displayed
Wright-I/Bettin--Chandee form used in R105.  That theorem is applicable; it
is simply too weak in the physical normalization.  R104 Section 8 and R105
Section 4 give

```text
||alpha||_2||beta||_2=X^(-1+o(1)),
integral ||nu_t||_2 dt=X^(1+o(1)),
(K_0MN)^(1/2)=X^2,
largest Wright bracket=X^(-1/8+o(1)),
output=X^(15/8+o(1)).                                 (7.2)
```

The direct absolute energy estimate is `X^(1+o(1))`, so (7.2) is worse by
`X^(7/8-o(1))`.  Window smoothness does not delete (7.1): after fixed-ratio
rescaling its amplitude is a fixed nonzero profile on suitable
`j/X,theta/X` boxes.  Nor does finite gamma recombination delete it, by
(6.2)--(6.4).

The calculation

```text
balanced native saving 1/40
minus a crude pre-IBP Z-projective charge 1/200
=1/50                                                     (7.3)
```

is only a nonsharp favorable-subledger calculation: R104's integration by
parts can remove the large-`Z` charge.  More importantly, it applies only to
balanced packets already in the native normalization.  It does not cover
every `g`, the top cofactor box, or the completed affine/reducible sectors.
It is not a proof, endpoint, or global saving.

Unfolding `q=db` returns the balanced factors `d,b~X^(1/2)`, but R105 proves
that the exact fixed-modulus formula then has a full Fourier support and a
modular-inverse image, not the two native short supports required by the
available Blomer--Pascadi theorem.  Treating `d,b` as Wright denominator
variables without proving that new product-kernel interface skips the first
open edge.

### Primary-literature closeout

The dated search log records the exact comparisons.

- Wright II, [arXiv:2608.27732](https://arxiv.org/abs/2608.27732), is not
  directly applicable to the unpartitioned top box: its Theorem 2.1 assumes
  both denominator supports have relative length `X^(-sigma)`, `sigma>0`.
  Partitioning both full supports uses `X^(2sigma)` scalar boxes.  On (7.1)
  the unchanged `A^(1/2)` branch gains only `X^(-sigma)` per pair, so scalar
  triangle recombination is no improvement (it loses `X^sigma`).  The
  paper's nominal `X^(-7sigma/5)` comparison concerns the other dominant
  branch and does not apply to this top-box branch.  It also does not couple
  the missing completed sectors.
- Maynard--Pandey--Radziwill,
  [arXiv:2608.14777](https://arxiv.org/abs/2608.14777), give a prime
  exponential-sum term `N/sqrt(B)`.  At principal frequency `alpha=z/X`,
  `B=max(1,|z|)`: this is natural size for `z=O(1)`, and even at the edge
  `|z|=X^(1/100)` its critical normalized square is `X^(99/100+o(1))`, above
  the `X^(49/50)` target.  Their theorem also has no affine-center cross
  term.
- Blomer--Pascadi,
  [arXiv:2607.24311](https://arxiv.org/abs/2607.24311), provide a critical
  fixed-modulus saving only after two native short additive supports are
  present.  R105's exact factor-unfolded formula has one full Fourier support
  and one modular-inverse image, so the required support-preserving lift is
  absent.

No located primary theorem estimates the completed high-cofactor,
short-quotient, projector-coupled field at exponent `49/50`.  This is a
negative applicability result, not evidence that no future theorem can do
so.

## 8. Post-`Q_h` version and its cutoff caveat

Let

```text
c_h=e^(h/2),       Q_h=(tau_h-c_h)^2,
V_Q(x)=V(x+2h)-2c_h V(x+h)+c_h^2V(x),
f^Q_r(t)=t^(-1/2)V_Q(r-log t).                         (8.1)
```

Apply `Q_h` to the field **before** block localization, using a `2h` safety
margin.  Then

```text
integral f^Q_r(t)dt=0,
Q_h[e^(r/2)(alpha+beta*r)]=0.                          (8.2)
```

Hence the frozen tail-center field has the exact finite form

```text
Q_h G_R(r)
 =sum_(q<=CX)gamma(q)sum_(j>=1)f^Q_r(qj)
 =sum_(q<=CX)gamma(q)/q
      sum_(a!=0)fhat^Q_r(a/q).                         (8.3)
```

The full completed von-Mangoldt field has the corresponding R104 formula
with `gamma(q)` replaced by `c(q)=-mu(q)log q`.  R104 then bounds its
`theta=0`, `j=0`, axes, and reducible faces polylogarithmically.  This is a
faithful coordinate change, not a contraction.

There is one order-of-operations caveat.  Low-pass multiplication preserves
the zero integral because `m(0)=1`, but subsequently multiplying its
noncompact inverse by `chi_X` need not preserve it exactly.  Thus one may
use (8.3) before physical cutoff, or use the general finite formula (2.3)
after cutoff with its explicit scalar residual.  One may not claim that all
axes still vanish exactly merely from (8.2).  Applying `Q_h` after a block
cutoff also creates the uncontrolled boundary commutator recorded in R102.

There is nevertheless an arbitrary-power approximate version.  If
`phi_r^Q=F^(-1)[m(xi/delta)fhat_r^Q(xi)]`, then
`integral phi_r^Q=0`.  Because `chi=1` on a fixed collar of the support of
`f_r^Q` and `check(m)` is Schwartz,

```text
|integral chi_X(t)phi_r^Q(t)dt|
 <=||f_r^Q||_1
   integral_(|v|>=cX)delta|check(m)(delta v)|dv
 <<_A X^(1/2)(delta X)^(1-A).                         (8.4)
```

Here `delta X=X^(1/100)`, so (8.4) is `O_D(X^(-D))` for every fixed `D`
after choosing `A`.  Since `C_T<<log^2X`, the scalar zero-mode and its energy
cross terms created solely by post-low-pass physical compactification are
arbitrary-power small.  They are not literally zero; the exact statement is
still (2.3).

Most importantly, R104's fail-fast calculation is already post-`Q_h`.
Therefore center annihilation does not alter the top-box conclusion in
Section 7.

## 9. Disposition and first open edge

The exact outcome is

```text
physical-cutoff principal test                    EXACT
finite gamma plus affine completion               EXACT
tail/tail-center/center-center square              EXACT
low q <<X^(99/100)                                 POWER-SMALL
q<=X^(499/500) or |a|>X^(1/400)                    AT TARGET FIELD SCALE
target-matched retained quotient                    X^(1/500+o(1))
outer cofactor l1 and weighted l2                  X^o(1)
finite Ramanujan Hilbert ledger                    X^o(1)
primitive common-g mask Fourier l1                 X^o(1)
crude pre-IBP Mellin ledger                         up to X^(1/200+o(1))
R104 post-IBP projective ledger at Z=O(1)           X^o(1)
top q~X semiprime sector                           SURVIVES / NATURAL SIZE
scalar Wright all-box estimate                     FAILS PHYSICAL SCALE
completed X^(49/50) estimate                       OPEN.              (9.1)
```

The strongest credible next *adapter* is a lossless product-sensitive
completion theorem which keeps `d,b>X^(9/20)` separate through the
two-frequency energy and lands either in a theorem with native complete
residue supports or in a vector-valued reciprocal estimate whose projective
cost is subpower.  As a serialization theorem alone, that is strictly weaker
than the strip endpoint and is a legitimate fail-fast target.

If the proposed theorem also supplies `X^(-1/50)` on all `g`, all
determinants, the reducible/low-character projector, and the affine (or
prelocalized `Q_h`) completion before absolute values, it is no longer a
preliminary lemma: by R187 it is endpoint-equivalent to the frozen uniform
strip bound.

## 10. Executable and formal guards

The hostile finite guards are

- [`r188_principal_band_serialization_falsifier.py`](../src/r188_principal_band_serialization_falsifier.py),
- [`test_r188_principal_band_serialization_falsifier.py`](../src/test_r188_principal_band_serialization_falsifier.py),
- [`R188PrincipalBandSerialization.lean`](../lean/rhbridge/RHBridge/R188PrincipalBandSerialization.lean), and
- [`R188PrincipalBandSerializationAudit.lean`](../lean/rhbridge/RHBridge/R188PrincipalBandSerializationAudit.lean).

They certify or replay the rational exponent ledger, high-denominator and
small-quotient implications, the target-matched `.998/.002/.0025` Fourier
collar ledger, low/high/reducible determinant witnesses,
primitive-mask Fourier-algebra bound, affine two-channel obstruction,
complete-square cross-term bookkeeping, and the R105 top-box exponent
comparison.  They do not formalize Poisson/Fourier analysis, Wright's
theorem, the PNT semiprime count, or any fixed-power R71 estimate.
