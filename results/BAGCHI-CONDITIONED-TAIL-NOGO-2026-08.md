# Conditioned Bagchi tail: zero-free-support no-go

Status: fixed-cutoff conditional-tail route pruned, 2026-08-04.  Finite-prime
Haar independence is correct, but the conditioned limiting tail is zero-free.
If the deterministic continued tail contains an off-line zeta zero, the
Rouche-sized approximation event has conditional probability exactly zero.
No RH claim is made.

## 1. The proposed gate

Let

```text
D={s:1/2<Re(s)<1}
```

and fix `y`.  Write the finite Euler product and analytically continued
remainder as

```text
P_y(s)=product_(p<=y) (1-p^(-s))^(-1),
R_y(s)=zeta(s)/P_y(s)
      =zeta(s) product_(p<=y)(1-p^(-s)).             (1)
```

For a vertical shift `tau`, set

```text
R_(y,tau)(s)
 =zeta(s+i tau) product_(p<=y)(1-p^(-s-i tau)).     (2)
```

The phase cylinder is

```text
A_y(eta)={tau:|p^(-i tau)-1|<eta for every p<=y}.   (3)
```

For fixed `y`, Kronecker equidistribution gives it limiting density

```text
a_eta^pi(y),
a_eta=(2/pi) asin(eta/2),                           (4)
```

for `0<eta<2`.  Thus the small-prime event is rare but has positive density
when `y` is fixed.

The hoped-for argument was to condition on (3), control (2) relative to (1)
in sup norm on a zero-containing compact, and apply Rouche.  An unconditional
bad-set subtraction cannot do this because (4) is exponentially small in
`y/log y`; finite-block independence appeared to offer a way around that
loss.

More precisely, let `K` be a disk and put

```text
m_K=min_(s in boundary K)|zeta(s)|.
G_tau=max_(s in boundary K)|zeta(s+i tau)-zeta(s)|.
```

Rouche replication needs `G_tau<m_K`.  If a head/tail argument proves
`G_tau<=e_head+E_tail` with `e_head<=theta*m_K`, then it needs, for some fixed
`kappa>0`,

```text
Pr(E_tail<(1-theta)m_K | A_y(eta)) >= kappa.        (5)
```

Any positive relative conditional probability would suffice; the issue is
whether the continued tail in (2), rather than a zero-free random surrogate,
satisfies it.

## 2. The corrected conditioned model

Bagchi's ordinary functional limit theorem sends zeta translates to a random
Euler product.  In the corrected joint convention, one records
`p^(-i tau)` alongside `zeta(s+i tau)`; these coordinates become independent
Haar variables `omega_p`.  Removing the factors at `p<=y` and conditioning
those finitely many phases to lie in the arcs (3) leaves the large-prime
coordinates independent and Haar.  The resulting conditional model is

```text
Z_y(s,omega)=product_(p>y)(1-omega_p p^(-s))^(-1). (6)
```

On every compact subset of `D`, the logarithm

```text
sum_(p>y) sum_(k>=1) omega_p^k/(k p^(ks))           (7)
```

converges almost surely locally uniformly.  The `k=1` part converges from
independence and `sum_p p^(-2 sigma)<infinity` for `sigma>1/2`; the `k>=2`
part converges absolutely.  Hence (6) is the exponential of a holomorphic
function and is almost surely nowhere zero on `D`.

This is the critical point: analytic continuation of `R_y` can carry zeros,
but its conditional random Euler-product model cannot.  The no-go below does
not depend on accepting a particular joint-limit reference: Rouche plus a
classical zero-density estimate proves the actual relative frequency is zero.

## 3. Zero-free-support theorem

**Theorem.**  Suppose `rho in D` is a zero of `zeta`.  Choose a closed disk
`K` around `rho`, contained in `D`, whose boundary contains no zeta zero.  For
every fixed `y`, let

```text
m_y=min_(s in boundary K) |R_y(s)|>0.               (8)
```

Then, for every `0<epsilon<m_y`,

```text
Pr(||Z_y-R_y||_(boundary K)<epsilon)=0.             (9)
```

Consequently the limiting relative frequency of shifts satisfying both the
phase cylinder and this continued-tail approximation is zero.

### Proof

The finite product in (1) is holomorphic and nonzero on `D`, so `R_y` has the
same zeros as `zeta` in `K`.  Every sample `Z_y` is holomorphic and zero-free
there.  If the inequality in (9) held, Rouche's theorem would give `Z_y` and
`R_y` the same number of zeros in `K`, a contradiction.  Thus the event is
empty, independently of how its probability is estimated.

For the actual shifts there is an independent quantitative proof.  Let
`sigma_*=min_(s in K)Re(s)>1/2`.  Every shift satisfying the analogous
boundary inequality for `R_(y,tau)` supplies a zeta zero in the translated
disk `K+i tau`.  A fixed zero ordinate accounts for at most `2 radius(K)`
values of `tau`.  Carlson's classical density estimate

```text
N(sigma_*,T) << T^(4 sigma_*(1-sigma_*)+epsilon)
```

therefore gives an unconditional measure `o(T)` for all such shifts.  Since
the fixed cylinder has measure asymptotic to `a_eta^pi(y) T`, intersecting
with it and dividing by its positive fixed density still tends to zero.  This
proves the stated relative-frequency conclusion without a conditional limit
theorem.  For a modern explicit form of the estimate, see
[Chourasiya](https://arxiv.org/abs/2412.02068).

The theorem also holds if the approximation is posed directly for
`zeta(s+i tau)` and `zeta(s)`: the full random Euler product is zero-free, and
Rouche again separates the two functions.

## 4. Why stronger probability estimates do not repair it

The usual large-prime variance estimate is valid but points in the wrong
direction.  If `sigma_0=min_(s in K) Re(s)>1/2`, then schematically

```text
E |log Z_y(s,omega)|^2
  is at most sum_(p>y) p^(-2 sigma_0) -> 0.         (10)
```

After standard compactness estimates, `Z_y->1` in probability locally
uniformly as `y->infinity`.  At the hypothetical zero, however,

```text
R_y(rho)=0                                          (11)
```

for every `y`.  Thus conditional `L2`, high-moment, large-sieve, and
concentration estimates make the random tail approach `1`; they do not make
it approach the analytically continued deterministic remainder.

The scale comparison is unfavorable even before the support obstruction.  If

```text
V_y=sum_(p>y)p^(-2 sigma_0)
    is asymptotic to y^(1-2 sigma_0)/((2 sigma_0-1)log y),
```

then unconditional Chebyshev is only polynomial in `y`.  Optimized
high-moment or Bernstein bounds have scale

```text
exp(-c/V_y)=exp(-c y^(2 sigma_0-1) log y),          (12)
```

still much larger than the fixed-width cylinder
`exp(-c_eta y/log y)` for every `sigma_0<1`.  Conditional independence does
give a valid `o(1)` relative bad probability for the **centered random log
tail**, including a sup-norm version on a slightly smaller compact.  That
success only proves `Z_y` is near `1`.  Identifying it with the zero-carrying
continued tail is the false step.

Head alignment also becomes more expensive when `y` grows.  On
`Re(s)>=sigma_0`, the cylinder implies

```text
|Delta log P_y(s)|
 <= eta A_y,
A_y=sum_(p<=y)1/(p^sigma_0-1)
    is asymptotic to y^(1-sigma_0)/((1-sigma_0)log y). (13)
```

Fixed relative head accuracy therefore requires `eta_y=O(1/A_y)`.  With this
shrinking arc, the cylinder cost is

```text
-log density(A_y(eta_y))=(1-sigma_0+o(1))y,         (14)
```

not merely order `y/log y`.

This also explains the limit-order trap.

1. Fixing `y` and taking `T->infinity` gives the exact zero-free law (6).
2. Taking `y->infinity` afterward cannot turn the zero conditional frequency
   into a positive one.
3. Letting `y=y(T)` grow before equidistribution abandons the fixed-block Haar
   argument.  It is a different shrinking-target problem requiring
   quantitative simultaneous Diophantine approximation coupled to zeta.

There is one precise diagonal window not eliminated by the fixed-limit
argument.  Write `d=(2 sigma_0-1)^2`.  Carlson's estimate shows that a
conditional success probability bounded below by `kappa>0` can contradict
zero density only if the cylinder density obeys

```text
density(A_y) >> T^(-d+epsilon).                    (15)
```

For fixed `eta`, this permits at most `y` on the rough scale
`log T log log T`; after the head-accuracy shrinkage in (13), it permits only

```text
y < (d/(1-sigma_0)+o(1)) log T.                    (16)
```

No standard `L2`, high-moment, large-sieve, hybrid-universality, or
independent-Euler theorem provides the required zero-bearing small-ball bound
uniformly in this diagonal regime.  Equation (16), rather than a vague
conditional-tail hope, is the only surviving quantitative target.

## 5. Equivalence, not a new route

Bagchi's strong-recurrence theorem already says that positive-density
self-approximation of zeta throughout `D` is equivalent to RH.  Hybrid
universality allows finitely many prime phases to be prescribed while
approximating a **nonvanishing** target.  Under RH, zeta itself is such a
target on every compact subset of `D`; if RH is false, Section 3 supplies the
support obstruction.  Conditioning the finite phases therefore does not
weaken the decisive premise.  It exposes the same equivalence more finely.

The primary starting points are [Bagchi's functional-limit
thesis](https://digitalcommons.isical.ac.in/masters-dissertations/41/), his
[joint-universality paper](https://doi.org/10.1007/BF01161980), and his
[strong-recurrence equivalence](https://doi.org/10.1007/BF01903937).
Classical hybrid universality does permit a fixed finite phase box together
with approximation of a nonvanishing target; see
[Pankowski](https://doi.org/10.4064/aa141-1-3).  It supplies positive lower
density, but no quantitative constant or uniform shrinking-box theorem as
`y->infinity`.  The equivalence of continuous, discrete, and hybrid
universality is treated abstractly by
[Andersson](https://arxiv.org/abs/2310.03619).

### 5.1 Phase-convention audit

The sign of the joint phase must be frozen explicitly.  Since

```text
p^(-s-i tau)=p^(-s) p^(-i tau),
```

recording `p^(-i tau)` gives the joint limit `(Z(s,omega),omega_P)`; recording
`p^(i tau)` gives `(Z(s,conjugate(omega)),omega_P)`.

Version 1 of [Endo's proposed hybrid joint limit
theorem](https://arxiv.org/abs/2410.17575) records `p^(i tau)` but states the
first of these two limits.  Its random Dirichlet model uses `omega(n)`, which
exhibits the inversion.  A one-coordinate moment also detects it: with the
recorded coordinate `x_p=p^(i tau)`, the actual limit has

```text
E[x_p Z(s,conjugate(x))]=p^(-s),
E[x_p Z(s,x)]=0.
```

Haar inversion preserves the marginals and, after a separate compact-open
repair to the support-density estimate at `sigma_phi=1/2`, preserves the full
product support and hybrid-universality corollary.  It therefore does not
change the present no-go.  It does matter when an exact conditional law,
rather than only support, is claimed.  The corrected convention is used in
Section 2.  The exact replacement theorem, one-prime witness, proof patch,
and support repair are recorded in
[`ENDO-HYBRID-JOINT-LIMIT-CORRECTION-2026-08.md`](ENDO-HYBRID-JOINT-LIMIT-CORRECTION-2026-08.md).

## 6. Helson countermodel calibration

The finite-phase mechanism is not zeta-specific.  For a completely
multiplicative unimodular `chi`, the Helson Euler product

```text
zeta_chi(s)=product_p (1-chi(p)p^(-s))^(-1)         (17)
```

has relative vertical phases `p^(-i tau)` just as zeta does.  Multiplication
by the fixed phases `chi(p)` preserves Haar measure, so finite-block
equidistribution and the zero-free random-tail law are unchanged.

Nevertheless, Helson zeta functions can have highly flexible prescribed
zeros and poles after meromorphic continuation.  Seip constructs universal
Helson functions with prescribed divisors in substantial portions of the
half-critical strip; the published Bochkov--Romanov theorem obtains
essentially arbitrary divisors in `21/40<Re(s)<1`.  Andersson's 2024 preprint
states a Mittag--Leffler construction permitting prescribed zeros and poles
throughout `Re(s)<1`.  See
[Seip](https://arxiv.org/abs/1812.11729),
[Bochkov--Romanov](https://arxiv.org/abs/2106.15949), and
[Andersson](https://arxiv.org/abs/2408.15713).

The small-prime condition can even be imposed exactly without changing that
divisor.  Given a prescribed-zero Helson character `chi`, a finite prime set
`F`, and arbitrary phases `eta_p`, replace `chi(p)` by `eta_p` on `F`.  In
`Re(s)>1`, the new Helson zeta satisfies

```text
zeta_eta(s)=zeta_chi(s)
  product_(p in F) (1-chi(p)p^(-s))/(1-eta_p p^(-s)). (18)
```

The finite multiplier is holomorphic and nonzero for `Re(s)>0`, so (18)
continues meromorphically and preserves every zero and pole there.  Taking
`eta_p=1` for all `p<=y` produces an exact finite-cylinder prescribed-zero
countermodel.  Thus no finite amount of near-trivial prime-phase data can
determine the divisor of the continuation.

There is also a deterministic tail obstruction.  If

```text
T_y(s)=zeta_eta(s) product_(p<=y)(1-eta_p p^(-s))
```

has a zero in `K`, then every ordinary finite tail

```text
product_(y<p<=z)(1-chi(p)p^(-s))^(-1)
```

is zero-free there.  Its boundary distance from `T_y` is therefore at least
`min_(boundary K)|T_y|`; otherwise Rouche supplies a zero.  Ordinary finite
Euler tails cannot converge locally uniformly to a zero-carrying continued
tail.

This is not a countermodel to the zeta functional equation or its gamma
factor.  It is a decisive countermodel to any argument using only

1. Euler-product form in `Re(s)>1`;
2. finite-prime Haar independence;
3. generic large-prime concentration; and
4. meromorphic continuation.

Such data, even with any fixed initial prime phases prescribed exactly,
coexist with prescribed off-line zeros.  A revival would need a
zeta-specific global relation that changes the support calculation itself;
ordinary conditional tail bounds cannot do so.

## 7. Verdict

The fixed-cutoff conditioned Bagchi route is pruned.  Its missing estimate is
not merely as hard as controlling an exponentially rare intersection.  Under
the negation of RH, the desired Rouche neighborhood is disjoint from the exact
conditional limiting support.

The reusable lesson is:

> Finite Euler phases can be independent while analytic continuation of the
> tail is globally dependent.  Removing finitely many Euler factors does not
> localize a zero; it leaves the zero in a deterministic remainder lying
> outside the zero-free random Euler-product support.

Only a growing-cutoff arithmetic construction that does not pass through the
fixed-block Bagchi limit remains logically distinct.  It currently has no
positive-density mechanism and should not remain an active RH path without a
new quantitative idea.
