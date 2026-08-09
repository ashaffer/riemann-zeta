# R175 unique-zero transform and outer-growth conservation

## Status

The unique-zero truncated-log transform does remove every artificial finite
value divisor.  For an integer `q>=2`, put

```text
T_(q-1)(u)=sum_(j=1)^(q-1)(-1)^(j+1)u^j/j,

Phi_q(F)=F exp[-T_(q-1)(F-1)].                           (0.1)
```

Then

```text
Phi_q'(F)/Phi_q(F)
 =(-1)^(q-1)(F-1)^(q-1)F'/F.                            (0.2)
```

The notation on the left means the logarithmic derivative with respect to
the underlying variable.  The transform has exactly the finite zeros of
`F`, with the same multiplicities, while (0.2) starts at the `q`-fold Euler
support.  For `q=2`,

```text
Phi_2(F)=F exp(1-F),
Phi_2'/Phi_2=(1-F)F'/F.                                  (0.3)
```

There is, however, an exact outer-growth conservation law.  Center the
high-jet disc at

```text
s_*=1+r+i gamma.
```

Let a retained simple zero be at distance `d`, and choose a right Cauchy
radius `a` with

```text
0<a<r<d<R.                                                (0.4)
```

Suppose the response `B_H=Phi_q'/Phi_q` obeys its natural right-circle
bound

```text
max_(|s-s_*|=a)|B_H(s)|<=H^(-q(r-a)+o(1)).               (0.5)
```

In the best case, assume this is the only pole in the localization disc and
write

```text
B_H(s)=1/(s-rho)+G_H(s),             G_H holomorphic.    (0.6)
```

Then necessarily

```text
max_(|s-s_*|=R)|G_H(s)|
 >=H^(lambda_crit-o(1)),

lambda_crit
 =q(r-a)log(R/d)/log(d/a).                               (0.7)
```

This is exactly the exponent which consumes the support gain.  A high-jet
contradiction with an assumed outer bound `H^(lambda+o(1))` requires

```text
q>lambda log(d/a)/[(r-a)log(R/d)].                       (0.8)
```

But (0.7) forces the right side of (0.8) to be at least `q`.  Thus the
criterion reduces identically to the impossible strict inequality

```text
q>q.                                                       (0.9)
```

For the standard choice `a=r/2`, (0.8) is precisely

```text
q>2 lambda log(2d/r)/[r log(R/d)],                       (0.10)
```

the conditional R166 threshold.

The transformed function pays more than a large logarithmic derivative.
If `F=Z exp(g_H)` is in a fixed exact-divisor class, then

```text
Phi_q(F)=Z exp(h_H),
h_H=g_H-T_(q-1)(F-1).                                    (0.11)
```

On any slightly larger enclosing contour, (0.7) implies

```text
condition number(Phi_q/Z)
 >=exp[H^(lambda_crit-o(1))].                             (0.12)
```

Thus `Phi_q` has stretched-exponential two-sided conditioning.  This is the
sharp, geometry-calibrated version of the R174 exact-divisor propagation
barrier.

The conclusion closes this **high-jet mechanism**, not analytic existence.
Explicit truncated-log sequences have one fixed zero, converge geometrically
to one on a cap, and pay exactly this kind of outer growth.  If the zero
divisor is a fixed finite cluster, a bounded-gap power-sum lemma preserves
(0.7).  If the number of additional zeros grows with `H`, there is no
uniform bounded-gap conclusion; this returns to the signed growing-divisor
gate rather than rescuing the unique-zero claim.  If `F` has a pole in the
disc, `Phi_q(F)` has an essential singularity and (0.2) has a pole of order
`m(q-1)+1`, so the simple logarithmic ledger has already been lost.

The `H`-exponent statements below take `q` fixed, as in the conditional
R153/R166 high-jet step.  The same calculation permits a growing `q` only
when all `o(1)` terms are uniform relative to `q` and the resulting derivative
orders remain within the available analytic ledger; no such uniform claim is
needed here.

```text
unique finite zero divisor of Phi_q                       EXACT
H -> H^q logarithmic-response support                     EXACT
right-circle H^(-q(r-a)) bound                           EXACT
outer response exponent lambda_crit                       THEOREM
stretched-exponential unit conditioning                   THEOREM
general-radius high-jet comparison                        q>q NO-GO
standard a=r/2 R166 comparison                            q>q NO-GO
fixed finite zero cluster                                 SAME EXPONENT
growing auxiliary zero cloud                              SIGNED GATE OPEN
analytic exact-divisor families                           EXIST
unique-transform high-jet strip proof                     CLOSED
fixed uniform zeta zero-free strip                        NOT PROVED
zeros approaching Re(s)=1                                 NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md`](R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md),
[`R154-COPRIME-FILTER-PACKET-AND-RESULTANT-GATE.md`](R154-COPRIME-FILTER-PACKET-AND-RESULTANT-GATE.md),
[`R166-MIXED-PRODUCT-SUPPORT-AMPLIFIER-AND-COLLECTIVE-COFACTOR-GATE.md`](R166-MIXED-PRODUCT-SUPPORT-AMPLIFIER-AND-COLLECTIVE-COFACTOR-GATE.md),
and
[`R174-EXACT-DIVISOR-PEAK-AND-CONTOUR-CONDITIONING-GATE.md`](R174-EXACT-DIVISOR-PEAK-AND-CONTOUR-CONDITIONING-GATE.md).

## 1. Exact algebra and cap gain

Write

```text
u=F-1.                                                     (1.1)
```

Where `|u|<1`, the Taylor series for the logarithm gives

```text
Log Phi_q(F)
 =Log(1+u)-T_(q-1)(u)
 =sum_(j=q)^infinity (-1)^(j+1)u^j/j.                    (1.2)
```

Differentiating (1.2), or differentiating (0.1) directly, gives

```text
[Log Phi_q(F)]'
 =[1/F-T_(q-1)'(u)]F'
 =(-1)^(q-1)u^(q-1)F'/F.                                (1.3)
```

At a zero of `F`, the exponential factor in (0.1) is finite and nonzero.
Consequently `Phi_q(F)` has exactly the finite zeros of `F`, including
multiplicity.  At such a zero, the factor multiplying `F'/F` in (1.3)
tends to

```text
(-1)^(q-1)(-1)^(q-1)=1,                                 (1.4)
```

so the logarithmic residue is unchanged.

For `|u|<=1/2`, (1.2) gives the uniform estimate

```text
|Log Phi_q(F)|
 <=|u|^q/[q(1-|u|)]<=2|u|^q/q.                          (1.5)
```

In particular, when the right-cap error tends to zero,

```text
Phi_q(F)-1=O_q(|F-1|^q).                                 (1.6)
```

Thus a cap estimate `F-1=O(H^(-mu+o(1)))` improves to

```text
Phi_q(F)-1=O(H^(-qmu+o(1)))                              (1.7)
```

for fixed `q`.

Assume in the half-plane of absolute convergence that

```text
F=1+U,
U(s)=sum_(n>H)u(n)n^(-s).                                (1.8)
```

Then (1.3) becomes

```text
B_H=(-1)^(q-1)U^(q-1)U'/(1+U).                          (1.9)
```

Every nonconstant Dirichlet monomial in (1.9) contains at least `q`
factors from the tail, counting the differentiated factor.  Hence

```text
supp B_H subset {n>H^q}.                                 (1.10)
```

Coefficient positivity is not asserted and is not needed below.

Let `s_*=1+r+i gamma` and choose `0<a<r`.  On the right circle
`|s-s_*|=a`, its left edge is `Re(s)=1+r-a`.  Positivity or an absolute
Euler majorant therefore gives

```text
|U|+|U'|<=H^(-(r-a)+o(1)),                              (1.11)
```

equation (1.9) gives (0.5).  More generally, all arguments below work with

```text
max_(|s-s_*|=a)|B_H|<=H^(-tau+o(1))                      (1.12)
```

and `tau` in place of `q(r-a)`.

### 1.1 Generic cap consequence

Even without the concentric high-jet geometry, R174 gives a useful direct
statement about the response.  Suppose `Phi_q(F_H)=Z exp(h_H)` has a fixed
nonempty divisor and

```text
sup_(fixed cap)|Phi_q(F_H)-1|<=epsilon_H.                (1.12a)
```

On a smaller cap, Cauchy's estimate gives `B_H=O(epsilon_H)`.  Propagate
`B_H` along a fixed zero-free chain to a small circle around one retained
zero.  Since

```text
integral B_H(s)ds=2 pi i m                               (1.12b)
```

on that circle, the quantitative continuation inequality implies, for
fixed `c,alpha>0`,

```text
sup_(fixed bridge)|B_H|>=c epsilon_H^(-alpha).           (1.12c)
```

A buffered Borel--Caratheodory argument then gives

```text
condition number(Phi_q/Z)
 >=exp[c epsilon_H^(-alpha)].                            (1.12d)
```

By (1.6), cap error `|F_H-1|<=H^(-mu+o(1))` permits
`epsilon_H=H^(-qmu+o(1))`, so (1.12c)--(1.12d) become

```text
sup |B_H|>=H^(qmu alpha-o(1)),
condition number(Phi_q/Z)>=exp[H^(qmu alpha-o(1))].       (1.12e)
```

The exponent `alpha` in this chain formulation is geometry-dependent and
not automatically sharp enough for a high-jet comparison.  Theorem 2.1
computes the exact exponent in the concentric Cauchy geometry.

### Pole warning

If `F` has a pole of order `m`, then the exponential in (0.1) has an
essential singularity.  Equation (1.3) has a pole of order

```text
m(q-1)+1.                                                 (1.13)
```

Therefore the theorem below treats the best possible localization case:
`F` is holomorphic in the disc and its relevant zero divisor is fixed.  A
pole does not improve the ledger; it destroys the proposed simple-divisor
outer bound before the high-jet comparison begins.

## 2. Sharp single-pole outer-growth theorem

Put

```text
z=s-s_*,              zeta=rho-s_*,              |zeta|=d. (2.1)
```

### Theorem 2.1 -- inner flatness forces the critical outer exponent

Fix `0<a<d<R`.  Suppose `B_H` is meromorphic on a neighborhood of
`{|z|<=R}`, has one simple pole at `z=zeta` with residue one, and no other
pole there.  Write

```text
B_H(z)=1/(z-zeta)+G_H(z),                                (2.2)
```

where `G_H` is holomorphic.  If for some fixed `tau>0`,

```text
max_(|z|=a)|B_H(z)|<=H^(-tau+o(1)),                      (2.3)
```

then

```text
max_(|z|=R)|G_H(z)|
 >=H^(tau log(R/d)/log(d/a)-o(1)).                       (2.4)
```

#### Proof

Write the error in (2.3) as `H^(-tau+eta_H)`, where
`eta_H ->0`.  Choose numbers `omega_H ->0` such that

```text
omega_H>=2|eta_H|,
omega_H log H ->infinity,                                (2.5)
```

and put

```text
k_H=floor[(tau-2omega_H)log H/log(d/a)].                 (2.6)
```

For large `H`, this is a nonnegative integer.  Cauchy's estimate on the
inner circle gives

```text
|B_H^(k_H)(0)|/k_H!
 <=a^(-k_H)H^(-tau+eta_H).                              (2.7)
```

The pole term has Taylor coefficient

```text
(1/k_H!)[d^(k_H)/dz^(k_H) 1/(z-zeta)]_(z=0)
 =-zeta^(-k_H-1).                                       (2.8)
```

The ratio of the right side of (2.7) to the magnitude in (2.8) is at most

```text
d H^(-tau+eta_H)(d/a)^k_H
 <=C H^(eta_H-2omega_H)=o(1).                            (2.9)
```

It follows from (2.2) that

```text
|G_H^(k_H)(0)|/k_H!
 >=(1-o(1))d^(-k_H-1).                                  (2.10)
```

If `M_H=max_(|z|=R)|G_H(z)|`, the outer Cauchy estimate gives

```text
M_H R^(-k_H)>=(1-o(1))d^(-k_H-1),                       (2.11)
```

and hence

```text
M_H>=(1-o(1))d^(-1)(R/d)^k_H.                            (2.12)
```

Using (2.6) and then letting `omega_H ->0` proves (2.4).  QED.

For the unique-zero response, `tau=q(r-a)` by (1.11), which gives (0.7).
The theorem is independent of the particular formula for `B_H`: every
meromorphic response with the same right flatness and retained pole pays
the same outer exponent.

On `|z|=R`, the pole term in (2.2) is bounded by `(R-d)^(-1)`.  Hence
(2.4) also implies

```text
max_(|z|=R)|B_H(z)|
 >=H^(tau log(R/d)/log(d/a)-o(1)).                       (2.13)
```

Thus the conclusion is a large-response theorem as well as a theorem about
the pole-subtracted remainder.  The remainder is singled out because it is
the quantity appearing in the high-jet outer ledger.

## 3. Exact comparison with the high-jet window

Suppose one tries to combine

```text
max_(|z|=a)|B_H|<=H^(-tau+o(1)),
max_(|z|=R)|G_H|<=H^(lambda+o(1)).                       (3.1)
```

Take derivative order `k=c log H+O(1)`.  The inner Cauchy bound is
negligible compared with the target pole precisely when

```text
-tau+c log(d/a)<0,
c<tau/log(d/a).                                          (3.2)
```

The outer remainder is negligible compared with the target pole precisely
when

```text
lambda-c log(R/d)<0,
c>lambda/log(R/d).                                       (3.3)
```

Such a `c` exists if and only if

```text
lambda<tau log(R/d)/log(d/a).                            (3.4)
```

Theorem 2.1 says that (3.4) is impossible for the exact-divisor response:
the lower bound on the right is the actual necessary outer exponent.

For `tau=q(r-a)`, condition (3.4) can be written

```text
q>lambda log(d/a)/[(r-a)log(R/d)].                       (3.5)
```

Substitution of the forced value

```text
lambda>=lambda_crit
 =q(r-a)log(R/d)/log(d/a)                                (3.6)
```

makes the right side of (3.5) at least `q`.  The strict high-jet window is
empty.  No choice of the general right-circle radius `a` changes this:
the same two logarithmic ratios occur reciprocally in (3.5) and (3.6).

For the notation of R166, take `a=r/2`.  Then

```text
log(d/a)=log(2d/r),
q(r-a)=qr/2,                                              (3.7)
```

and (3.5) becomes exactly (0.10).  This verifies rather than assumes that
the comparison reduces to `q>q`.

One can also optimize the right circle before making the comparison.  Put

```text
C(a)=(r-a)/log(d/a),                  0<a<r.              (3.7a)
```

The support exponent available per channel is proportional to `C(a)`.
It tends to zero at both endpoints and has a unique maximum at the solution
of

```text
(r-a)/a=log(d/a).                                        (3.7b)
```

At that maximizing radius,

```text
lambda_crit=q C(a)log(R/d),                              (3.7c)
```

while the optimized closure condition is

```text
q>lambda/[C(a)log(R/d)].                                 (3.7d)
```

Substitution again gives `q>q`.  Therefore the equality is not an artifact
of the conventional halfway circle `a=r/2`.

For the especially tempting transform `Phi_2(F)=F exp(1-F)`, this reads

```text
lambda_crit=2(r-a)log(R/d)/log(d/a),                     (3.7e)
```

and the putative closure condition reduces to `2>2`.  Removing all finite
mixed values at the first nonlinear level therefore does not create even a
small exponent margin.

### Meaning of the equality case

At `lambda=lambda_crit`, the only potentially useful derivative order is
asymptotically

```text
k_crit=q(r-a)log H/log(d/a).                             (3.8)
```

At this order the inner response, the retained pole, and the outer regular
germ all have the same exponential scale.  There is no strict domination
from which Rouche, Cauchy, or a one-pole high-jet lower bound can start.
Improving constants or taking a neighboring integer derivative does not
open an exponent interval.

## 4. From the outer remainder to the unit condition number

Now assume the exact-divisor form

```text
F_H=Z exp(g_H),
Phi_q(F_H)=Z exp(h_H),
h_H=g_H-T_(q-1)(F_H-1).                                  (4.1)
```

Suppose first that `rho` is the only zero of `Z` in the disc.  On a fixed
neighborhood,

```text
Z'/Z=1/(s-rho)+J_Z(s),                                  (4.2)
```

where `J_Z` is fixed and holomorphic.  Therefore

```text
B_H=1/(s-rho)+[J_Z+h_H'],
G_H=J_Z+h_H'.                                            (4.3)
```

Theorem 2.1 and boundedness of `J_Z` imply

```text
max_(|s-s_*|=R)|h_H'(s)|
 >=H^(lambda_crit-o(1)).                                 (4.4)
```

Fix a buffer radius `R_1>R` on which `h_H` remains holomorphic.  The
Borel--Caratheodory derivative estimate gives

```text
max_(|s-s_*|<=R)|h_H'(s)|
 <=C_(R,R_1)
   [max_(|s-s_*|=R_1)Re h_H-min_(|s-s_*|=R_1)Re h_H].    (4.5)
```

Indeed, subtract the midpoint of the boundary range of `Re h_H` and one
imaginary constant, apply Borel--Caratheodory on the larger disc, and then
apply Cauchy's derivative estimate on the smaller disc.

Combining (4.4)--(4.5) gives

```text
log {max_(|s-s_*|=R_1)|exp h_H|
     /min_(|s-s_*|=R_1)|exp h_H|}
 >=H^(lambda_crit-o(1)).                                 (4.6)
```

This proves (0.12).  Since `Z` is bounded above and below away from zero on
the outer contour, the condition number of `Phi_q(F_H)` itself differs from
that of `exp h_H` by only a fixed multiplicative factor.  Thus

```text
condition number_(R_1)(Phi_q(F_H))
 >=exp[H^(lambda_crit-o(1))].                            (4.7)
```

Equations (2.4) and (4.7) must not be conflated:

```text
outer logarithmic response G_H       size H^lambda_crit,
exact-divisor unit Phi_q/Z           condition exp(H^lambda_crit). (4.8)
```

The high-jet comparison uses the first quantity.  A two-sided boundary or
Rouche conditioning argument must pay the second.

## 5. Fixed finite clusters and growing clouds

The single-pole assumption displays the exponent without power-sum
notation.  It is not essential when the divisor is fixed and finite.

Suppose

```text
B_H(s)=sum_(j=1)^J m_j/(s-rho_j)+G_H(s),                 (5.1)
```

where `J`, the positive integers `m_j`, and the points `rho_j` are fixed,
and `G_H` is holomorphic on the outer disc.  Let

```text
d=min_j |s_*-rho_j|.                                     (5.2)
```

The standard finite power-sum lemma supplies a fixed `L=L(J)` and a
constant `c_J>0` such that, for every sufficiently large `k`, some
`ell in {k,...,k+L}` satisfies

```text
|sum_j m_j(rho_j-s_*)^(-ell-1)|
 >=c_J d^(-ell-1).                                       (5.3)
```

Apply the proof of Theorem 2.1 at this `ell`.  The bounded displacement
`ell-k=O_J(1)` changes only fixed factors, so

```text
max_(|s-s_*|=R)|G_H|
 >=H^[tau log(R/d)/log(d/a)-o(1)].                       (5.4)
```

Thus every fixed finite exact divisor gives the same exponent.

There are three important limitations.

1. If a nearer fixed pole is not the designated source zero, then `d` in
   (5.4) is its distance.  A source-specific conclusion requires the usual
   nearest-cluster separation or a power-sum selection which includes the
   entire fixed cluster.
2. If `J=J_H` grows, the bounded gap in (5.3) need not remain bounded.
   A growing favorable-residue cloud can cancel long blocks of powers, as
   in R153.  The present theorem then becomes a signed joint-divisor problem,
   not a unique-zero theorem.
3. If poles of `F_H` enter the disc, (1.13) replaces the fixed logarithmic
   cluster by high-order poles or essential singularities.  This is a worse
   outer ledger, not an escape from (5.4).

The phrase "one retained zero" alone is therefore insufficient if arbitrary
additional zeros are allowed.  The sharp no-go applies to the claimed
unique-zero or fixed-exact-divisor transform.

## 6. Explicit model and sharpness

The mechanism is not an analytic nonexistence theorem.  The elementary
model already exhibits the required escape.

Let `x=z/zeta`, so the cap `|z|<=a` corresponds to `|x|<=a/d<1`, and define

```text
F_n(x)=(1-x)exp[sum_(j=1)^n x^j/j].                      (6.1)
```

This is exactly

```text
F_n=Phi_(n+1)(1-x).                                      (6.2)
```

It has the single simple zero `x=1`.  For `|x|<1`,

```text
Log F_n(x)=-sum_(j=n+1)^infinity x^j/j,                  (6.3)
```

so on every fixed `|x|<=r_0<1`,

```text
F_n=1+O(r_0^(n+1)).                                      (6.4)
```

Its logarithmic derivative is

```text
F_n'/F_n=-x^n/(1-x),                                     (6.5)
```

up to the fixed derivative factor relating `x` and `z`.  Hence it is
geometrically small on the cap.  On a circle `|x|=R_0>1`, the regular
polynomial germ in (6.1) has derivative of size `asymp R_0^n` along the
positive radial direction.  Choosing `n` proportional to `log H` gives
precisely a fixed power of `H` whose exponent is the quotient of the two
geometric logarithms in Theorem 2.1.

The integrated unit in (6.1) has condition number at least of order

```text
exp(c R_0^n/n),                                           (6.6)
```

on a slightly larger contour.  Thus the distinction in (4.8) is visible in
the simplest possible example.

For a fixed `q`, applying `Phi_q` once more to `F_n` gives another
exact-single-zero family with

```text
Phi_q(F_n)-1=O(r_0^(q(n+1)))                              (6.7)
```

on the cap.  Its outer growth is at least the amount forced above and may be
larger.  This is enough to show that cap normalization, a retained zero, and
the unique-zero transform are analytically compatible.  What fails is the
small outer remainder required to turn `H^q` support into a high-jet
contradiction.

## 7. Decision

The truncated-log transform gives a clean algebraic answer to the mixed
value problem, but not a zero-free-strip mechanism.  Its exact-divisor
regular germ is forced to cancel the retained pole jet up to the critical
order.  The support gain and the outer-growth debt are two sides of the same
Cauchy interpolation identity.

For a unique zero or fixed finite divisor, this route is closed at the
high-jet level.  A continuation would have to use information absent from
the scalar transform: a signed arithmetic correlation in a growing divisor
cloud, a non-Cauchy localization functional, or a multichannel structure
whose outer regular germ is not freely able to cancel the target.  None of
those is proved here, and no conclusion about a fixed zeta zero-free strip
follows.
