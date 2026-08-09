# Multigap superoscillatory filters and the zero-discrepancy wall

Status: R92 exact finite-gap filter calculus, exact prime-support
positivity, explicit pole-plus-notch filters, exact conditioning, exact
cancellation of the leading Riemann--von Mangoldt background to arbitrary
finite order, a broad-band minimax comparison, and a fail-fast theorem for
the complete signed remainder.  The proposed extra cancellation is real:
several prime-log gaps can annihilate the pole, a vertical notch, and the
smooth ordinate density while retaining a normalized target response.
What remains is not the smooth zero density.  It is a horizontally weighted
zero-discrepancy measure.  Riemann--von Mangoldt and the functional equation
do not control that measure, and the exact explicit formula restores the
whole target contribution.

The no-go proved here applies to every real smooth weight supported in a
finite union of prime-power-log gaps, with an arbitrary finite collection
of linear moment, Christoffel, or smooth-density constraints.  It also
applies, with an inequality in place of equality, to every discretely
positive version of such a filter.  It does not rule out a new theorem for
the target-conditioned horizontally weighted zero sum; that theorem is
exactly the missing input.

```text
several actual prime-log gaps                         AVAILABLE
prime-power coefficients                             EXACTLY ZERO
pole cancellation                                    EXACT
target normalization                                 EXACT
finite vertical vanishing moments                    EXACT
leading smooth Riemann--von Mangoldt term             CANCELABLE
closed-form arithmetic-center notch                  EXPLICIT
notch coefficient condition number                   EXPONENTIAL IN ORDER
broad-band minimax filter                             JUST SUPPORT TRANSLATION
ordinary S(t) remainder                              TOO LARGE
functional-equation horizontal pairing               DOES NOT CANCEL
abstract RvM-compatible companion zeros              DEFEAT ANY LOCAL NOTCH
complete signed remainder under target hypothesis    EXACTLY ONE
fixed zero-free strip                                 NOT PROVED.             (1.1)
```

## 2. The exact multigap class

Retain the notation

```text
S={log(p^m): p prime, m>=1}                              (2.1)
```

from R91.  Choose pairwise disjoint actual gaps

```text
I_j=(x_j-h_j,x_j+h_j),       I_j intersect S=empty,
0<x_0<...<x_K.                                           (2.2)
```

For the fixed nonnegative even bump `phi` of R91 put

```text
phi_j(x)=h_j^(-1)phi((x-x_j)/h_j),

Phi_j(z)=integral phi_j(x)e^(-zx)dx
        =e^(-z x_j)J(h_jz).                              (2.3)
```

Fix a putative zero and the three horizontal rates

```text
rho_0=1-e+iT,
sigma=1+delta,
r=delta+e,
a=delta+1/2,
c=a-r=1/2-e.                                             (2.4)
```

Only `0<e<1/2` is relevant to a strip beyond the critical line.  Normalize
the gap bases at the target rate:

```text
B_j(x)=phi_j(x)/Phi_j(r),
F_j(z)=integral B_j(x)e^(-zx)dx=Phi_j(z)/Phi_j(r),
F_j(r)=1.                                                (2.5)
```

For arbitrary real coefficients `w_j`, define

```text
W=sum_(j=0)^K w_j B_j,
H(z)=H_W(z)=sum_j w_jF_j(z).                             (2.6)
```

Because every `B_j` is supported in a gap,

```text
W(log p^m)=0                                             (2.7)
```

for every prime power.  Thus the prime sum is identically zero:

```text
Q_W(s)=sum_n Lambda(n)W(log n)n^(-s)=0                  (2.8)
```

for every complex `s`.  In particular the prime-side positivity condition
is exact, with equality, regardless of the signs or sizes of the `w_j`.
This is stronger than merely preserving nonnegative coefficients.

All proposed finite filtering conditions are linear in `w`.  For example,

```text
sum_j w_j=1,                         H(r)=1,
sum_j w_jF_j(delta)=0,               H(delta)=0,
sum_j w_jF_j^(ell)(a)=0,             H^(ell)(a)=0          (2.9)
```

for `0<=ell<L`.  The last line makes a vertical notch of order `L` at the
critical horizontal rate, since

```text
d^ell/dv^ell H(a+iv)|_(v=0)=i^ell H^(ell)(a).             (2.10)
```

If `A` is the matrix of any such finite list of constraints and `b` their
desired values, the exact least-Euclidean-norm solution is

```text
w_min=A^t(AA^t)^(-1)b,
||w_min||_2^2=b^t(AA^t)^(-1)b,                            (2.11)
```

provided the rows have full rank.  Formula (2.11) is the finite Christoffel
form of the construction.  Its natural target-line `l1` condition number is

```text
Cond_1(W)=sum_j|w_j|.                                    (2.12)
```

It controls `H(r+iv)` up to the harmless bump-transform ratios.

There is no rank obstruction.  In the point-gap limit the rows in (2.9)
are evaluations of the extended exponential-polynomial system

```text
1, e^(e x), e^(-cx), x e^(-cx),...,x^(L-1)e^(-cx).       (2.13)
```

This is an extended Chebyshev system, so its ordered collocation matrices
are nonsingular.  Consecutive prime-power-log gaps have mesh tending to
zero; their centers can approximate any fixed ordered pattern.  Since
`h_j->0`, the exact bump matrix is a small perturbation of the nonsingular
point matrix.  Hence every fixed finite list (2.9) can be imposed exactly
in sufficiently high actual gaps.

This proves an important positive fact:

```text
finite multigap pole and zero-density filtering is algebraically feasible.
                                                               (2.14)
```

## 3. Closed-form pole-plus-notch filter

The conditioning can be seen without hiding it in a matrix inverse.  First
take the point-gap limit with arithmetic centers

```text
x_j=X+jd,                  0<=j<=K, d>0.                   (3.1)
```

Write

```text
P(q)=sum_(j=0)^K w_jq^j,
q(z)=e^(-(z-r)d).                                         (3.2)
```

Then

```text
H(z)=e^(-(z-r)X)P(q(z)).                                 (3.3)
```

Introduce

```text
q_delta=e^(ed)>1,
q_a=e^(-cd) in (0,1).                                    (3.4)
```

The target and pole conditions are `P(1)=1` and
`P(q_delta)=0`.  A notch of order `L` at `a` says that `q_a` is a root of
order `L`.  The minimal-degree filter is therefore

```text
P_L(q)
 =[(q_delta-q)/(q_delta-1)]
  [(q-q_a)/(1-q_a)]^L.                                   (3.5)
```

It has, exactly,

```text
H(r)=1,
H(delta)=0,
H^(ell)(a)=0,                0<=ell<L.                    (3.6)
```

All roots in (3.5) are positive, so the monomial coefficients alternate in
sign.  There is no hidden cancellation in their `l1` norm:

```text
Cond_1(P_L)
 =(q_delta+1)/(q_delta-1)
  [(1+q_a)/(1-q_a)]^L

 =coth(ed/2)coth(cd/2)^L.                                 (3.7)
```

Thus a high-order local notch is exponentially ill-conditioned.  It also
has large pass bands.  On the critical vertical line,

```text
q(a+iv)=q_a e^(-ivd),                                    (3.8)
```

and the notch factor has modulus

```text
|q(a+iv)-q_a|/(1-q_a)
 =2q_a|sin(vd/2)|/(1-q_a).                               (3.9)
```

It vanishes at `v=2pi m/d`, but at the midpoints it is
`2q_a/(1-q_a)`.  If `cd` is small, (3.9) is much larger than one, and its
`L`-th power creates exponentially high intervening lobes.  The vanishing
moments cancel a local Taylor jet; they do not make a broad vertical stop
band.

The exact actual-gap filter is obtained by solving (2.9).  Since the bump
matrix tends to the point matrix, (3.5)--(3.7) give its asymptotics for each
fixed `L`.  If `L` grows, the inverse matrix and the true gap widths must be
retained; the closed form already displays the dangerous exponential.

## 4. What the smooth Riemann--von Mangoldt density sees

Suppose temporarily that all the non-target zeros being modeled lie on the
critical line.  Their paired ordinate kernel is

```text
K_a(t)=2 Re H(a-it).                                      (4.1)
```

The leading smooth density is

```text
dM(t)=(1/(2pi))log(t/(2pi))dt.                            (4.2)
```

For a real `W` supported away from zero, the distributional Fourier
identity

```text
integral_R e^(itx)log|t|dt=-pi/|x|,       x!=0             (4.3)
```

gives the exact leading smooth functional

```text
integral_0^infinity K_a(t)dM(t)
 =-1/2 integral_0^infinity W(x)e^(-ax) dx/x.              (4.4)
```

The constant `-log(2pi)` in (4.2) is supported at `x=0` under Fourier
transform and therefore contributes nothing.  Low ordinates and the
`O(t^(-2))` correction to the differentiated main term are additional
bounded linear functionals; any fixed number of them can be appended to
the matrix `A` in (2.11).

For the arithmetic point model, (4.4) is

```text
B_a(W)
 =-e^(-cX)/2 sum_(j=0)^K w_j q_a^j/(X+jd).               (4.5)
```

The root of order `L` in (3.5) implies

```text
sum_j w_jq_a^j j^m
 =(q d/dq)^mP_L(q)|_(q=q_a)=0,
0<=m<L.                                                   (4.6)
```

If `Kd<X`, expand

```text
1/(X+jd)=X^(-1)sum_(m>=0)(-jd/X)^m.                       (4.7)
```

Equations (4.5)--(4.7) show that the same vertical notch cancels the first
`L` terms of the smooth-density functional.  Quantitatively,

```text
|B_a(W)|
 <= e^(-cX)/(2X)
    sum_j |w_j|q_a^j
    (Kd/X)^L/(1-Kd/X).                                   (4.8)
```

One can instead make (4.4) exactly zero.  Add the row

```text
sum_j w_j integral B_j(x)e^(-ax)dx/x=0                    (4.9)
```

and one additional gap to (2.11).  The point-limit functional
`e^(-cx)/x` is not a linear combination of the rows in (2.13); generic
ordered collocation has full rank, and the density of high gap centers plus
continuity gives exact actual-gap solutions.  Thus neither the inverse
moment `1/x` nor a finite gamma-factor correction is an algebraic obstacle.

This is the main success of the multigap experiment:

```text
the pole and the smooth critical-line background can be canceled together.
                                                               (4.10)
```

## 5. A broad notch is only translation to a later gap

The large lobes in (3.9) suggest replacing vanishing moments by a minimax
or Christoffel stop-band filter.  The arithmetic model gives a sharp
reality check.  If `P` has degree at most `K`, `P(1)=1`, and

```text
M_a(P)=max_(|q|=q_a)|P(q)|,                               (5.1)
```

the Bernstein--Walsh inequality for the disk gives

```text
M_a(P)>=q_a^K.                                           (5.2)
```

Up to a fixed pole-cancellation factor, this rate is attained by

```text
P_broad(q)
 =q^(K-1)(q_delta-q)/(q_delta-1).                        (5.3)
```

Indeed,

```text
P_broad(1)=1,
P_broad(q_delta)=0,

max_(|q|=q_a)|P_broad(q)|
 <=q_a^(K-1)(q_delta+q_a)/(q_delta-1).                   (5.4)
```

Its coefficient condition number is only

```text
Cond_1(P_broad)=coth(ed/2),                               (5.5)
```

but (5.3) uses only the final two centers `X+(K-1)d` and `X+Kd`.  The
factor `q_a^K=e^(-cKd)` is exactly the horizontal attenuation obtained by
moving the two-gap construction `Kd` farther to the right.  Distributing a
fixed span among many Christoffel centers does not beat the capacity of the
disk; the optimum simply spends the whole span.

At the farthest center `x_max`, however, the containing prime-log gap has

```text
h_max << e^(-(19/40)x_max),                              (5.6)
```

and can be as small as the elementary guaranteed scale
`h_max >> x_max e^(-x_max)` for the selected largest gap in a unit interval.
Moving right therefore broadens the Fourier uncertainty interval from
`1/h` at precisely the same time that it attenuates the critical line.
There is no known lower bound for an available gap large enough to turn the
attenuation into a uniform estimate for the discrepancy term below.

## 6. The `S(t)` remainder pays the full condition number

Write the ordinary Riemann--von Mangoldt decomposition, for `t>=2`, as

```text
N(t)=M(t)+S(t)+O(1/t),
S(t)=O(log t).                                            (6.1)
```

After (4.4) or (4.9) removes the smooth part, Stieltjes integration by parts
gives, on a truncated band `[2,Omega]`,

```text
|integral K_a(t)dS(t)|
 <<log(2+Omega)
   [|K_a(2)|+|K_a(Omega)|
    +integral_2^Omega |K_a'(t)|dt].                       (6.2)
```

For the normalized bump basis, rapid decay of `phi` and a change of
variable `u=h_jt` give

```text
integral_R |d/dt F_j(a-it)|dt
 <<_phi (1+x_j)e^(-cx_j)/h_j.                            (6.3)
```

Consequently every triangle-variation use of (6.1) costs

```text
log(2+Omega)
sum_j |w_j|(1+x_j)e^(-cx_j)/h_j.                         (6.4)
```

This bound retains both the superoscillatory coefficient condition number
and the inverse physical gap width.  The elementary guaranteed lower bound
for the selected largest gap only gives

```text
1/h_j << e^(x_j)/x_j,                                    (6.5)
```

so even one normalized component in (6.4) can cost

```text
exp[(1-c)x_j]=exp[(1/2+e)x_j]                             (6.6)
```

up to polynomial factors.  The order-`L` filter additionally pays (3.7).
Thus canceling the smooth density before applying the known pointwise
bound for `S(t)` is not enough.  It replaces a power-many term count by a
total-variation estimate at least as badly conditioned.

The obstruction is not merely that the best published bound for `S(t)` has
an inconvenient logarithm.  Ordinate counting has discarded the horizontal
locations `beta`, while the actual kernel depends exponentially on them.

## 7. Functional-equation symmetry exposes the missing measure

Pair a zero `beta+i gamma` with its functional-equation mate
`1-beta+i gamma`.  Put

```text
u=beta-1/2.                                               (7.1)
```

At the zero-frequency point `sigma=1+delta`, their combined transform is

```text
H(a-u-i gamma)+H(a+u-i gamma).                            (7.2)
```

For a point component at `x`, the horizontal multiplier in (7.2) is

```text
2e^(-ax)cosh(ux).                                        (7.3)
```

The ordinary counting function sees only `gamma`; it does not see the
factor `cosh(ux)`.  A critical-line notch cancels (7.2) at `u=0`.  Its even
Taylor expansion leaves

```text
2 sum_(m>=1) u^(2m)H^(2m)(a-i gamma)/(2m)!               (7.4)
```

off the line.  Finitely many moments can remove finitely many terms in
(7.4), but not the continuum `0<=u<=1/2-e` while also retaining the
endpoint target

```text
a-(1/2-e)=r,
H(r)=1.                                                   (7.5)
```

Indeed, if (7.2) vanished for an interval of `u` at one fixed `gamma`,
analytic continuation would force the relevant even part of `H` to vanish
identically; imposing this for the shifted kernel would also remove the
target reserve.

For a zero just to the left of the putative rightmost zero, write

```text
beta=1-e-g,                  g>=0,
gamma=T+v.                                               (7.6)
```

Its near-edge member contributes to the shifted explicit formula through

```text
H(r+g-iv).                                               (7.7)
```

There is no critical-line attenuation in (7.7) when `g` is small.  The
actual object left after smooth-density cancellation is therefore the
horizontally weighted discrepancy measure

```text
dD_W(g,v)
 =sum_(rho near rho_0) H(r+g-iv)
  - any chosen smooth ordinate model.                    (7.8)
```

Neither (6.1) nor functional-equation symmetry bounds (7.8).  A theorem
that did so uniformly with reserve would already be a target-conditioned
zero-density or zero-repulsion theorem of fixed-strip strength.

## 8. An abstract zero configuration defeating generic counting

The preceding information loss can be made exact.  Let a filter satisfy

```text
H(r)=1.                                                   (8.1)
```

Because `H` is entire, for every such filter there is an `epsilon_W>0` for
which

```text
|H(r+g-iv)-1|<=1/4
        whenever 0<=g<=epsilon_W, |v|<=epsilon_W.         (8.2)
```

One explicit permissible choice follows from

```text
|H'(z)|
 <=sum_j |w_j|(x_j+h_j)
   sup_(x in I_j)e^(-(Re z-r)x)
   sup_(|z-r|<=1)|J(h_jz)/J(h_jr)|:                       (8.3)
```

take `epsilon_W` smaller than the reciprocal of four times the right side.
Large conditioning merely makes the companion window smaller; generic zero
counting supplies no lower zero-spacing bound with which to exclude it.

Now start with any abstract zero multiset obeying conjugation, the
functional-equation symmetry, and

```text
N(t)=M(t)+O(log(2+t)).                                    (8.4)
```

Adjoin a distinct simple quartet generated by

```text
rho_1=1-e-g+i(T+v),
0<g<epsilon_W,
0<|v|<epsilon_W.                                         (8.5)
```

The new multiset still satisfies (8.4), with its counting error changed by
at most two at positive ordinate, and it has all the required symmetries.
Yet the near-edge member of the new quartet has real response at least
`3/4` after choosing the sign of sufficiently small `v`.  If the
functional-equation mate cancels this response, the original target
quartet has already lost the same reserve; otherwise the companion survives
in the remainder.

The example can be made stronger.  In an interval of length
`o(1/Cond_1(W)x_max)` around `T`, adjoin up to `c log T` such simple
quartets and remove the same number of baseline ordinates from a neighboring
unit interval.  The resulting counting function still satisfies (8.4),
while its local filter response changes by `asymp log T`.  Equivalently,
ordinary Riemann--von Mangoldt error permits a discrepancy measure with the
worst sign on the whole continuity window of the filter.

Thus even after the smooth main term is canceled exactly,

```text
Riemann--von Mangoldt counting + functional symmetry
does not imply a signed remainder smaller than the target.              (8.6)
```

This counterconfiguration is not asserted to be the zeta zero set.  Its
purpose is precise: any proof using only the generic information (8.4),
symmetry, and the multigap interpolation identities cannot close the
remainder.  It must import a genuinely zeta-specific horizontal or local
correlation theorem.

## 9. Exact spectral restitution survives every finite filter

There is an even shorter audit for the actual zeta zeros.  Use exactly the
notation of Theorem 10.1 in
`R90-DISCRETE-PRIME-SUPPORT-INTERPOLATION-GATE.md`.  Suppose

```text
rho_0=1-e+iT                                               (9.1)
```

is a zeta zero, and take any multigap weight in the class of Section 2 with

```text
H(delta)=0,
H(r)=1.                                                    (9.2)
```

It may also satisfy any finite number of notch, inverse-moment,
Riemann--von Mangoldt, gamma-factor, or Christoffel orthogonality
conditions.  Equations (2.8) and the exact two-point explicit formula give

```text
0
 =Q_W(sigma)+Re Q_W(sigma+iT)
 =-1+E_0(W)+E_1(W;T,rho_0).                               (9.3)
```

Therefore

```text
E_0(W)+E_1(W;T,rho_0)=1.                                 (9.4)
```

No finite collection of background constraints changes (9.4).  It only
changes which portion of the remaining actual zero system supplies the
one.  In particular an estimate

```text
|E_0+E_1|<=1-epsilon                                     (9.5)
```

cannot follow from multigap support, moment algebra, or generic zero
counting under the target hypothesis.  Proving (9.5) by an additional
zeta-specific theorem would contradict that hypothesis and would be the
desired zero-exclusion argument.

For a non-invisible weight satisfying only

```text
W(log p^m)>=0                                             (9.6)
```

the same exact identity and prime positivity imply

```text
E_0(W)+E_1(W;T,rho_0)>=1                                 (9.7)
```

after the normalization (9.2).  Thus polynomial or other
discretely-positive approximations do not escape restitution.

## 10. Precise no-go theorem and surviving input

Define `G_fin` to be the class of real `C_c^infinity((0,infinity))` weights
whose support is contained in a finite union of components of
`(0,infinity)\S`.  Permit:

1. an arbitrary number of gap components, possibly depending on `T`;
2. arbitrary real coefficients and arbitrary conditioning;
3. any finite collection, also depending on `T`, of homogeneous linear
   constraints on `H`, its derivatives, inverse moments of `W`, or fixed
   smooth zero-density functionals;
4. the two normalizations `H(delta)=0` and `H(delta+e)=1`.

### Theorem 10.1 (finite multigap zero-filter no-go)

If `rho_0=1-e+iT` is a zeta zero, every `W in G_fin` satisfying item 4 has

```text
E_0(W)+E_1(W;T,rho_0)=1.                                 (10.1)
```

Consequently no uniform fixed-reserve bound smaller than one can be derived
from the defining properties in items 1--4, Riemann--von Mangoldt counting,
and functional-equation symmetry alone.

#### Proof

The support condition gives `Q_W=0` exactly.  Substitute the two
normalizations into the exact identity (10.4) of R90.  This proves (10.1).
Sections 6--8 show independently why replacing the actual zero sum by its
smooth counting model does not strengthen the hypotheses enough to bound
the remainder.  The added linear constraints never enter the prime-side
identity.  QED.

The theorem is intentionally precise about its class.  It does **not** say
that every imaginable signed zero estimate is impossible.  It says that
finite multigap interpolation, even with perfect cancellation of every
chosen smooth background, supplies no such estimate.  The only surviving
input would be a uniform theorem of the form

```text
| sum_(rho!=rho_0) H_W(sigma+iT-rho)
  + sum_rho H_W(sigma-rho)
  + trivial/pole corrections |
 <=1-epsilon,                                             (10.2)
```

for a target-normalized, discretely positive `W`, with the full
horizontal `beta` dependence and the full condition number retained.
By (9.3), (10.2) is already strong enough to exclude `rho_0`.  It is not a
consequence of a new filter design.

## 11. Decision

The multigap idea has been executed through its strongest finite linear
form.

1. Several actual prime-log gaps allow exact pole cancellation, exact
   target normalization, and arbitrary finite vertical vanishing moments
   while the prime side remains identically zero.
2. The arithmetic-center filter is explicit.  An order-`L` notch has
   condition number
   `coth(ed/2)coth((1/2-e)d/2)^L` and exponentially high side lobes.
3. The leading Riemann--von Mangoldt background is the inverse moment
   `-(1/2) integral W(x)e^(-ax)dx/x`.  The notch cancels its first `L`
   expansion terms, and one more gap cancels it exactly.
4. A true broad stop band is capacity-limited.  Its optimal exponential
   rate is achieved simply by moving a two-gap filter to the farthest
   available gap, where the inverse gap width and uncertainty band grow.
5. The known `S(t)` bound pays the total vertical variation, hence the full
   coefficient condition number and `1/h`.
6. More fundamentally, ordinate counting omits the horizontal factor
   `cosh((beta-1/2)x)`.  Functional-equation symmetry doubles this even
   dependence; it does not cancel it.
7. Riemann--von Mangoldt-compatible simple companion zeros can lie inside
   any target-retention window, so generic counting cannot bound the local
   signed remainder.
8. For the actual zeta zero system, exact spectral restitution gives
   remainder one for every prime-invisible filter and at least one for every
   discretely positive filter.

Thus multigap filtering successfully removes the smooth background but does
not remove the target-conditioned zero discrepancy.  This route proves
neither a fixed zero-free strip nor the nonexistence of one.  Its only
continuation is a genuinely zeta-specific signed theorem for the complete
horizontally weighted remainder, not another finite collection of filter
moments.
