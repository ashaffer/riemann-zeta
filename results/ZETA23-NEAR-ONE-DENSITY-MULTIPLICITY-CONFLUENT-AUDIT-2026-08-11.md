# Near-one density and multiplicity do not close the asymmetric confluent gate

Status: primary-source exponent audit, exact Chebyshev/Hermite cost, and
compatibility check for the corrected sparse islands, 2026-08-11.  No
zero-free strip is proved.

## 1. Verdict

Let

```text
L=log T=log X+o(log T),
rho=1/2+alpha+i*gamma,       alpha=1/2-delta,
```

and use the reduced asymmetric carrier from
[`ZETA23-ASYMMETRIC-TWO-LOBE-HALF-PERIOD-GATE-2026-08-11.md`](ZETA23-ASYMMETRIC-TWO-LOBE-HALF-PERIOD-GATE-2026-08-11.md).
Its free lobe has relative length `a>1/2`, its retained separation is
`d<2/3`, and its power margin over the same-lobe prime term is

```text
G(alpha,a,d)=alpha*d-a/2.                              (1.1)
```

The largest countermodel-safe limiting margin is

```text
G -> 1/12                    (alpha->1/2, a->1/2, d->2/3). (1.2)
```

The strongest unconditional horizontal density bound at the rows which
still enter the confluent system is Huxley's bound, not the Guth--Maynard
transition estimate.  Those rows may begin at

```text
Re rho = 1/2+alpha*d-o(1) -> 5/6                      (1.3)
```

and Huxley permits `T^(1/3+o(1))` of them globally.  The strongest
horizontally sensitive uniform short-interval theorem audited below is on
intervals of length
`T^(27/82+epsilon)`, and its upper bound is still a positive power of `T`.
Bellotti has a stronger genuinely local disk lemma at the moving
Vinogradov--Korobov scale, but its allowed radius is too small to reach the
fixed `5/6` gate.  On a fixed microscopic interval containing that gate, the
best applicable unconditional input remains an `O(L)` total-zero count.  The
current explicit Riemann--von Mangoldt error permits

```text
q <= 0.20152*L+0.48920*log L+O(1)                    (1.4)
```

zeros, with multiplicity, in an interval of diameter `o(1)`.  No horizontal
dependence is known uniformly at that scale.

Ivic's strongest explicit near-one multiplicity estimate does not repair
this.  It bounds the multiplicity of one zero, while an aperiodic cluster
may consist entirely of distinct simple zeros.  Exact repetitions are also
benign for the asymmetric mirror: they merely add the same positive weight
to an identical row.  Thus a multiplicity bound is not a bound for the
confluent order.

There is an exact quantitative obstruction to treating (1.4) as a tolerable
fixed-power loss.  A `q`-jet exterior datum at the seed center, extrapolated
from the free lobe, has Chebyshev cost

```text
C_q=T_(q-1)(2*d/a)
   =cosh((q-1)*arcosh(2*d/a)).                        (1.5)
```

After packet normalization this costs `C_q^(-2)` in the quadratic carrier.
At the optimal reduced limiting geometry,

```text
arcosh(8/3)=log((8+sqrt(55))/3)=1.63680651775648...,
q/L=kappa must satisfy
kappa < 1/(24*arcosh(8/3))=0.02545607328... .         (1.6)
```

The explicit uniform allowance `kappa=0.20152` instead corresponds to a
carrier-exponent loss

```text
2*0.20152*arcosh(8/3)=0.65969849...,                  (1.7)
```

almost eight times the permitted order coefficient and far larger than the
entire margin `1/12`.  This does not assert that the zeta zeros attain the
worst Chebyshev configuration.  It proves that the cited density,
short-interval, and multiplicity theorems do not imply the required uniform
target-conditioned Hermite estimate.

The corrected two-scale `k=3` island remains compatible for every fixed
`alpha<1/2`, including `alpha` arbitrarily close to `1/2`.  Its power-length
terminal block lies near `Re rho=5/6`, where Huxley allows much more than the
island uses, while its high-depth cap is only polylogarithmic.  The original
broad fixed-profile cap remains excluded above
`alpha=(sqrt(577)-19)/12`.  Bellotti's `O(1)` density theorem prunes caps at
the moving Vinogradov--Korobov edge, but it does not apply to any fixed strip
or to the fixed `5/6` confluent gate.

Consequently this route proves no unconditional fixed strip.  Even a new
zero-side theorem would leave the independent Wiener-atomic cross-prime gate
from the asymmetric report.

## 2. Exact global density envelope

Write `N(sigma,T)` for the number of zeros with `Re rho>=sigma` and
`|Im rho|<=T`, counted with multiplicity.  The primary results give the
piecewise envelope

```text
d_I(sigma)  =3*(1-sigma)/(2-sigma),          1/2<=sigma<=7/10,
d_GM(sigma) =15*(1-sigma)/(3+5*sigma),       7/10<=sigma<=4/5,
d_H(sigma)  =3*(1-sigma)/(3*sigma-1),        4/5<=sigma<1,

N(sigma,T)<=T^(d(sigma)+o(1)).                        (2.1)
```

The transition endpoints agree.  Guth--Maynard also record the convenient
uniform corollary `d(sigma)<=(30/13)(1-sigma)`, but that corollary is weaker
than Huxley near one.

For a target line `sigma=1-delta`, Huxley gives

```text
d_H(1-delta)=3*delta/(2-3*delta).                     (2.2)
```

This is positive for every fixed `delta>0`, so its upper bound is eventually
much larger than `L`.  More importantly, the shallow-row reduction in the
asymmetric carrier does not leave only rows near the target.  In the reduced
limiting geometry it leaves every row to the right of `5/6-o(1)`, and

```text
d_H(5/6)=1/3.                                         (2.3)
```

For comparison, the bulk-refuted formal center geometry has gate `7/8` and
`d_H(7/8)=3/13`.  Both are polynomial ceilings and therefore permit an
`O(L)` collision group at one height.

Bellotti proves a genuinely stronger moving-line statement:

```text
N(sigma,T)=O_A(1)
for sigma>=1-A*L^(-2/3)*(log L)^(-1/3), A>A_0.        (2.4)
```

This is useful at the Vinogradov--Korobov scale but cannot yield a fixed
`sigma<1`.  It also does not control the active rows at (1.3).

Primary sources for (2.1)--(2.4) are Ingham,
[*On the estimation of N(sigma,T)*](https://doi.org/10.1093/qmath/os-11.1.201),
Huxley,
[*On the difference between consecutive primes*](https://doi.org/10.1007/BF01418933),
Guth--Maynard,
[*New large value estimates for Dirichlet polynomials*](https://arxiv.org/abs/2405.20552),
and Bellotti,
[*A new zero-density estimate for zeta(s) and the error term in the Prime Number Theorem*](https://arxiv.org/abs/2508.02041).

## 3. The local density input still leaves one exceptional cluster

Karatsuba--Korolev prove, for fixed `0<epsilon<0.001`,

```text
H=T^(27/82+epsilon),          x=T^(0.1*epsilon),
N(sigma,T+H)-N(sigma,T-H)
 <=13*H*L*x^(1-2*sigma),      1/2<=sigma<=1.          (3.1)
```

At `sigma=5/6`, the right side is

```text
13*L*T^(27/82+(14/15)*epsilon),                       (3.2)
```

and at `sigma=7/8` it is
`13*L*T^(27/82+(37/40)*epsilon)`.  These bounds are enormously larger
than `L`.  Their theorem for `H>=(log T)^600` is an almost-all-height result
with an exceptional set; a uniform strip cannot discard the interval
containing the hypothetical target zero.

Bellotti's local disk lemma is stronger, but only at the moving near-one
scale.  For `K << log log t`, it states

```text
#{rho: |1+i*t-rho|
       <=K/((log t)^(2/3)*(log log t)^(1/3))} << K.   (3.3)
```

Thus it gives `O(1)` local order at a fixed multiple of the
Vinogradov--Korobov radius.  To make this disk reach `Re rho=5/6`, however,
one would need

```text
K >=(1/6+o(1))*L^(2/3)*(log L)^(1/3),
```

which is far outside `K<<log L`.  The lemma therefore does not constrain the
fixed-gate confluent cluster.

At microscopic scale one can make the remaining `O(L)` statement explicit.
Bellotti--Wong prove, for `T>=e`,

```text
|N(T)-T/(2*pi)*log(T/(2*pi*e))|
 <=0.10076*log T+0.24460*log log T+8.08344.           (3.4)
```

Subtract (3.4) at the endpoints of `[t-h,t+h]`, with `t` comparable to `T`
and `h=o(1)`.  The main-term difference is `o(L)`, so the number of all zeros
in that interval satisfies (1.4).  Restricting to `Re rho>=sigma` cannot
increase the count, but none of the global estimates in Section 2 lowers
the coefficient uniformly in the center `t`.

Equations (3.1)--(3.4) are from the primary papers
Karatsuba--Korolev,
[*Behaviour of the argument of the Riemann zeta function on the critical line*](https://www.mathnet.ru/eng/rm1741),
Theorem 1 of Chapter I, Bellotti, Lemma 2.4 of
[*A new zero-density estimate for zeta(s) and the error term in the Prime Number Theorem*](https://arxiv.org/abs/2508.02041),
and Bellotti--Wong,
[*Improved estimates for the argument and zero-counting function of the Riemann zeta-function*](https://arxiv.org/abs/2412.15470).

### The half-isolated detector does not count the cluster

Maynard--Pratt's Theorem 4 says that a half-isolated zero `rho_0` has, for
some

```text
exp((log log T)^3)<=Y<=T^(5/log log T),
```

a short prime detector of absolute value at least `(log T)^(-C)`.  Their
Corollary 5 counts such anchors globally:

```text
#{half-isolated rho: Re rho>=sigma, Im rho in [T,2T]}
 <=T^(2*(1-sigma)+o(1)).                              (3.5)
```

Neither statement bounds the number of zeros attached to one anchor.  The
definition is deliberately asymmetric: a `Y`-half-isolated `rho_0` may have
arbitrarily many zeros within `(log |Im rho_0|)^2` satisfying

```text
|Re rho-Re rho_0|<=1/(10*log Y),     Im rho>=Im rho_0. (3.6)
```

Consequently the lowest-ordinate member of an `O(L)` simple cluster on one
vertical line can be half-isolated while all other members lie above it and
are explicitly allowed by (3.6).  Its detector lower bound says nothing
about their number.  At `sigma=5/6`, (3.5) is only the global ceiling
`T^(1/3+o(1))` on anchors.  If the cluster has varying real parts, the
deepest/lowest member need not be half-isolated at all: a nearby zero may
occupy the forbidden intermediate real-part band between (3.6) and the
alternative drop `(log log T)^2/log Y`.

This is the first fatal quantifier in applying the half-isolated method here:
it gives an existential detector for one asymmetric anchor, not a uniform
packing bound for every cluster.  Maynard--Pratt explicitly state that they
cannot unconditionally improve `N(sigma,T)` by this method; their density
improvement assumes Hypothesis F, which restricts zeros to finitely many
fixed vertical lines.  The unconditional Theorem 4 and Corollary 5 therefore
cannot imply the needed `q/L<0.02545607328...`.  The primary source is
[*Half-isolated zeros and zero-density estimates*](https://arxiv.org/abs/2206.11729).

## 4. What the near-one multiplicity theorem actually says

For one zero `beta+i*gamma`, put `delta=1-beta` and `L=log gamma`.  Ivic's
explicit theorem gives, uniformly for `beta>=5/6`,

```text
m(beta+i*gamma)
 <=C
  +[13.35*beta/(3*delta*log 6+beta*log 2)]*delta^(3/2)*L
  +[7*(3-2*beta)+epsilon]
    /[9*delta*log 6+3*beta*log 2]*log L.              (4.1)
```

In particular,

```text
m(beta+i*gamma)<=4*log L+20*delta^(3/2)*L.            (4.2)
```

The exact leading coefficients from (4.1) at the two carrier gates are

```text
beta=5/6:  0.51371506...*L
             +(2.11137162...+O(epsilon))*log L+O(1),
beta=7/8:  0.40381548...*L
             +(2.28147346...+O(epsilon))*log L+O(1).       (4.3)
```

Thus even if multiplicity were incorrectly substituted for cluster order,
(4.3) would be weaker than the total microscopic count (1.4) at the active
lines.  Near the target itself, the leading coefficient is
`(13.35/log 2+o(1))*delta^(3/2)=19.25997...*delta^(3/2)`, but this has no
bearing on a cluster of simple zeros whose real parts range down to (1.3).
For scale only, compare the exact first coefficient with the
`delta`-dependent reduced-edge allowance
`(1/12-(2/3)*delta)/(2*arcosh(8/3))`.  Equality occurs at
`delta=0.01195686648...`; below that, even the one-zero multiplicity
coefficient would fit the carrier bill.  The fatal point is that it neither
counts distinct neighbors nor applies that small coefficient to the active
rows near `5/6`.

The structural point is stronger than the numerical comparison.

1. A zero of multiplicity `m` contributes `m` copies of the same explicit-
   formula row.  In the asymmetric periodic mirror this common weight occurs
   on both sides and exact repetition is favorable.
2. A confluent obstruction is a group of distinct nearby full row parameters
   `(gamma_j,alpha_j)`.  Every member can be simple, so (4.1) applies with
   `m=1` and says nothing about the group order.
3. Statistical bounds for the number of high-multiplicity zeros likewise do
   not exclude one exceptional simple cluster.

The theorem numbering matters here.  The 1999 paper's Theorem 3 is the
Vinogradov-symbol antecedent

```text
m(beta+i*gamma) << (1-beta)^(3/2)*log gamma+log log gamma.
```

Its Theorem 4 assumes that near-one zeros are isolated and is not the source
of the numerical constants in (4.1).  Those constants are exactly Theorem 4
of the 2017 paper; (4.2) is its Corollary 1.  The 2017 proof itself calls its
result a sharpening of “Theorem 4” of the 1999 paper, but direct comparison
of the two primary texts shows that this backward theorem number is an
apparent cross-reference error: the unconditional antecedent is 1999
Theorem 3, whereas 1999 Theorem 4 is the different isolation result.

The primary references are Ivic,
[*On the multiplicity of zeros of the zeta-function*](https://arxiv.org/abs/math/0501434),
and, for the explicit constants in (4.1),
[*On the multiplicities of zeros of zeta(s) and its values over short intervals*](https://arxiv.org/abs/1706.08268),
Theorem 4 and Corollary 1.

## 5. Exact Chebyshev/Hermite extrapolation bill

Normalize the free interval to `[-1,1]`.  Its physical center is `c_-`, its
half-length is `aL/2`, and the seed center is at distance `dL`.  The normalized
seed point is therefore

```text
z=(x_+-c_-)/(aL/2)=2*d/a>1.                           (5.1)
```

In a `q`-fold confluent limit, matching the seed-generated analytic datum asks
the free-lobe packet to reproduce the moments of exterior evaluation through
degree `q-1`.  The norm of exterior evaluation on polynomials of degree at
most `q-1`, with the supremum norm on `[-1,1]`, is exactly

```text
sup_(deg p<q) |p(z)|/sup_[-1,1]|p|
 =T_(q-1)(z)=cosh((q-1)*arcosh z).                    (5.2)
```

Consequently every signed representing measure on the free lobe has total
variation at least (5.2), and equality is attained in the dual extremal
problem.  With an `L2` norm the Christoffel function has the same exponential
base, up to powers of `q`.  Thus, if `q=kappa*L+o(L)`, the coefficient cost is

```text
C_q=X^(kappa*arcosh(2*d/a)+o(1)).                     (5.3)
```

The selected negative coordinate is linear in the normalized packet, so the
quadratic carrier loses twice this exponent.  A necessary ledger inequality
for a uniform theorem based only on the order bound is

```text
2*kappa*arcosh(2*d/a)<alpha*d-a/2.                   (5.4)
```

At the reduced edge, (5.4) gives (1.6).  For comparison, the already-refuted
formal center carrier has

```text
z=3,
arcosh 3=log(3+2*sqrt(2))=1.76274717403909...,
G->1/8,
kappa<1/(16*arcosh 3)=0.03545602053... .             (5.5)
```

Even there, (1.4) would allow a quadratic exponent loss
`2*0.20152*arcosh 3=0.71045762...`, versus a margin of only `1/8`.

The conclusion of (5.2)--(5.4) is deliberately limited.  Raw divided
differences can contain additional inverse powers of the spacing; natural
confluent weights remove those false spacing powers.  They do not make the
exterior-evaluation norm (5.2) disappear.  Subpower retention follows from
this ledger only after a uniform `q=o(L)` theorem (plus collision-stable
weight control).  A tolerable fixed-power theorem would require at least the
sharp coefficient in (1.6).  None of Sections 2--4 supplies either statement.

## 6. Compatibility of the corrected sparse islands near one

The density correction to the tapered `k=3` island is essential and remains
valid near one.  Put

```text
alpha=1/2-delta,          b=2*alpha/3,
sigma_b=1/2+b=5/6-(2/3)*delta.                       (6.1)
```

The repaired two-scale island has a terminal block of population

```text
T^(alpha/3+o(1))=T^(1/6-delta/3+o(1))                (6.2)
```

at depth `b`.  Huxley's ceiling there is

```text
d_H(sigma_b)
 =(3/2-2*alpha)/(1/2+2*alpha)
 =(1+4*delta)/(3-4*delta).                            (6.3)
```

At `delta=0`, (6.2) has exponent `1/6` and (6.3) has exponent `1/3`; the
strict inequality persists for `0<alpha<1/2`.  Every population at a fixed
depth above `b` lies in the polylogarithmic Gevrey cap and is `T^o(1)`, below
Huxley's positive-power ceiling for every fixed line below one.

The local checks also pass.  The right-hand zeros of the `k=3` lattice have
unit-interval density

```text
L/(6*pi)+O(1)=0.0530516...*L+O(1),                   (6.4)
```

and the reflected pair-points have twice this density,
`L/(3*pi)=0.1061033...*L`.  With the on-line filler, the construction has the
full Riemann--von Mangoldt density `L/(2*pi)+o(L)=0.1591549...*L`, and every
constructed zero is simple.  Thus a microscopic subinterval contains
`o(L)` constructed points, while the corresponding unit-window bound also
includes its `L/(2*pi)` main term.  Both are compatible with (3.4); the
Karatsuba--Korolev bound is much larger still.  The rank and Frobenius
ledgers remain those proved in
[`ZETA23-SPARSE-ISLAND-ZETA-SPECIFIC-DENSITY-AUDIT-2026-08-11.md`](ZETA23-SPARSE-ISLAND-ZETA-SPECIFIC-DENSITY-AUDIT-2026-08-11.md).

The original broad cap put `T^(alpha/3+o(1))` zeros at every fixed depth just
below `alpha`.  Comparing that exponent with Huxley gives the already-audited
cutoff

```text
alpha_*=(sqrt(577)-19)/12=0.4184020249... .           (6.5)
```

It is therefore illegal near one, but (6.1)--(6.4) show why the two-scale
repair is legal for fixed `alpha<1/2`.

There is one moving-line qualification.  If `delta` is allowed to shrink on
the Vinogradov--Korobov scale, Bellotti's (2.4) permits only `O(1)` zeros above
the corresponding moving line and can prune a multi-point high cap there.
That does not affect the fixed-`alpha` counterconfiguration relevant to a
fixed-strip theorem, and it does not constrain the terminal `5/6` block.

The polylogarithmic tapered `k=2` island remains handled by the exact
asymmetric mirror lemma.  None of the density or multiplicity inputs found
here reopens it.  The power-length varying-depth `k=3` screen, with the
two-scale correction above, remains the relevant bulk-compatible cap.

## 7. Exact obstruction and next sufficient input

The cited unconditional results prove all of the following and no more:

```text
global deep-row count at the reduced gate:       <=T^(1/3+o(1));
uniform long local count:                         a positive power of T;
moving-edge disk count:                           O(K), K<<log log T;
uniform microscopic total count:                 <=(0.20152+o(1))*L;
half-isolated anchor count:                       global, not per cluster;
one-zero multiplicity near 1:                     O(delta^(3/2)*L+log L);
distinct-simple confluent order at one height:    no o(L) bound.          (7.1)
```

The last line is the obstruction.  It is exactly the quantity that enters
the Chebyshev/Hermite bill, while the multiplicity estimate controls a
different and favorable degeneration.

A zero-side theorem sufficient for the present ledger would have to give,
uniformly at the target height, either

```text
q=o(L),
```

for the naturally grouped rows to the right of the carrier gate, or at least

```text
q/L < (alpha*d-a/2)/(2*arcosh(2*d/a))                (7.2)
```

together with a signed target-conditioned Hermite construction attaining
that cost.  At the optimal reduced edge, the right side tends to
`0.02545607328...`, not the available `0.20152`.  A global density theorem, an
almost-all local theorem, or a bound on exact multiplicity cannot imply
(7.2).

Therefore the asymmetric carrier plus the strongest audited unconditional
density and multiplicity inputs does not close a genuine fixed zero-free
strip.  This is an exact limitation of this input package, not a claim that
the actual zeta divisor realizes the hostile confluent configuration.
