# The four-row growing-jet envelope has an exponential capacity defect

Status: exact depth barrier, exact one-cell Taylor-conditioning barrier,
scoped fail-fast verdict, and primary-literature audit, 2026-08-13.  The
global compact Pick gate remains **open**.  No zero-free strip or RH statement
is proved.

## 1. Binary verdict

The conditional four-rows-per-jet danger

```text
E_4(b)={1/(8*K_b)} log[(alpha+b)/(alpha-b)]
```

reaches

```text
max E_4=.0288268337...>.0253912552... .            (1.1)
```

That envelope assumes that an order `r~cL` positive Tchakaloff fixture can be
made simultaneously

1. supported in one microscopic phase cell;
2. uniformly positive-spanning for the order-`r` analytic Taylor jet;
3. subexponentially conditioned; and
4. compatible with an exponentially small analytic remainder.

The third premise is **false** in the natural Taylor/Schur coordinates.  If
`E_r` is the evaluation matrix of any such one-cell fixture, then

```text
kappa_2(E_r)>=4^(r-o(r)).                           (1.2)
```

The bound is independent of the number, placement, and positive weights of
the Tchakaloff nodes.  It applies before any Pick or arithmetic input.  A
change to a Chebyshev basis merely transfers the same exponential factor to
the conversion back to the local Taylor/Schur jet.

There is a second, independent obstruction.  Every exact positive quadrature
for the all-jet contour through order `r` has a node of scaled depth

```text
lambda_max >= {2/(e*d)-o(1)} r.                    (1.3)
```

At `d=.66`, the coefficient in (1.3) is

```text
2/(e*d)=1.1147861853... .                           (1.4)
```

Thus the fixture is neither shallow nor uniformly conditioned when its order
grows linearly with `L=log X`.

This is a rigorous no-go for the **advertised growing-jet/Tchakaloff
realization of (1.1)**.  It is not a no-go theorem for every mixed-depth
global Pick construction.  In particular, it does not prove the desired GP
upper transfer and it does not construct an actual-zero obstruction.

## 2. The all-jet contour and its exact inverse phase

Fix `d>0` and `lambda_0>0`.  The continuum dependence used in the proposed
fixture is

```text
h(x)=-lambda_0+(2/d)log cos(x/2)-i*x/d,
integral_(-pi)^pi exp(-i*x) h(x)^k dx=0,            (2.1)
```

for every nonnegative integer `k`.  Write

```text
h+lambda_0=-lambda-i*x/d,
lambda=-(2/d)log cos(x/2)>=0,
a=d/2.                                              (2.2)
```

The useful observation is that (2.1) has an exact inverse-phase exponential.
For any fixed `1<s<3`,

```text
Re{exp(-i*x) exp[-s*a*(h+lambda_0)]}
 =exp(s*a*lambda) cos[(1-s/2)x] >0.                 (2.3)
```

The positivity is uniform relative to the exponential:

```text
cos[(1-s/2)x]>=m_s,
m_s=cos(|1-s/2|*pi)>0.                              (2.4)
```

This identity is what abstract Tchakaloff existence does not quantify.

## 3. A forced linear-depth theorem

### Theorem 3.1 (positive all-jet quadrature must be deep)

Let `x_j in (-pi,pi)`, let `w_j>0`, and define `h_j=h(x_j)`.  Suppose

```text
sum_j w_j exp(-i*x_j) h_j^k=0,       0<=k<=r.       (3.1)
```

Then, for every `1<s<3`,

```text
lambda_max >=(2/d)*sqrt{
  [ ((r+1)!*m_s)^(1/(r+1))/s ]^2-(pi/2)^2
},                                                   (3.2)
```

whenever the radicand is positive.  Taking

```text
s=1+1/sqrt(r+1)                                    (3.3)
```

gives (1.3).

#### Proof

Put

```text
z_j=s*(a*lambda_j+i*x_j/2)
```

and let `P_r(z)=sum_(k=0)^r z^k/k!`.  Since
`P_r[-s*a*(h+lambda_0)]` is a polynomial of degree at most `r` in `h`, (3.1)
gives

```text
sum_j w_j exp(-i*x_j)P_r(z_j)=0.                    (3.4)
```

The integral form of the exponential remainder gives, because
`Re z_j>=0`,

```text
|exp(z_j)-P_r(z_j)|/|exp(z_j)|
 <=|z_j|^(r+1)/(r+1)!.                              (3.5)
```

If the reverse of (3.2) held, the right side of (3.5) would be strictly less
than `m_s` at every node.  Equations (2.3)--(2.4) would then imply

```text
Re{exp(-i*x_j)P_r(z_j)}>0
```

at every node, contradicting (3.4) and positive weights.  Stirling's formula
and (3.3) give

```text
((r+1)!)^(1/(r+1))/s=(r/e)*(1+o(1)),
```

which proves (1.3).  QED

This theorem does not say that a depth of `1.1148r` is sufficient.  It only
rules out every shallower exact positive realization.

## 4. The capacity-`1/4` conditioning theorem

Now put the contour nodes into the physical half-plane at anchor `b`:

```text
z_j=b+h(x_j)/L,
u_j=(z_j-b)/b.                                      (4.1)
```

Admissibility `Re z_j>=0` and `|x_j|<pi` imply

```text
-1<=Re u_j<=0,
|Im u_j|<=pi/(b*d*L).                               (4.2)
```

Let the order-`r` real half-space Taylor matrix be the map

```text
A_r P(j)=Re{exp(-i*x_j)P(u_j)},   deg P<=r,          (4.3)
```

written on the real and imaginary Taylor coefficients of `P`.

### Theorem 4.1 (one-cell jet condition number)

For every set of nodes satisfying (4.2), with enough rows for full real
column rank,

```text
log kappa_2(A_r)
 >=(2r-3/2)log 2-r*tau_L,                           (4.4)
```

where

```text
eta_L=2*pi/(b*d*L),
cosh(tau_L)={eta_L+sqrt(eta_L^2+4)}/2.              (4.5)
```

In particular, if `r=Theta(L)`, then

```text
tau_L=O(L^(-1/2)),
log kappa_2(A_r)>=r*log 4-o(r).                     (4.6)
```

Moreover, if `K_r` is the convex hull of the real half-space row normals and
`0 in K_r`, its centered Euclidean inradius satisfies

```text
inrad_0(K_r)<=4^(-r+o(r)).                          (4.6a)
```

#### Proof

Use the monic Chebyshev polynomial for `[-1,0]`,

```text
p_r(u)=2^(1-2r) T_r(2u+1).                          (4.7)
```

Under `zeta=2u+1`, (4.2) lies in the rectangle

```text
-1<=Re zeta<=1,       |Im zeta|<=eta_L.             (4.8)
```

The Bernstein ellipse with parameter `rho=exp(tau_L)` contains (4.8).  The
identity

```text
1/cosh(tau_L)^2+eta_L^2/sinh(tau_L)^2=1             (4.9)
```

checks the corner.  The extremal formula for `T_r` on a Bernstein ellipse
therefore gives

```text
max_j |p_r(u_j)|
 <=2^(1-2r) exp(r*tau_L).                           (4.10)
```

The coefficient vector of `p_r` has Euclidean norm at least one because the
polynomial is monic.  After normalizing that vector, (4.10) gives

```text
sigma_min(A_r)
 <=sqrt(N)*2^(1-2r)exp(r*tau_L).                    (4.11)
```

The two constant-coordinate columns of `A_r` are `cos x_j` and `sin x_j`.
Their squared norms sum to `N`, so
`sigma_max(A_r)>=sqrt(N/2)`.  Dividing proves (4.4).  QED

For (4.6a), use the normalized real coefficient vector of `p_r` as a linear
functional.  Every row has absolute pairing bounded by (4.10), so the whole
convex hull lies in a slab of that half-width.  No larger centered ball fits
inside it.  This is the positive-spanning version of the same obstruction and
does not depend on a choice of quadrature weights.

The theorem is stated for the actual point-evaluation rows.  For a fixed
number of normalized derivative rows, differentiating (4.7) changes the
near-null estimate by only a power of `r`; a growing confluent multiplicity
requires its own normalization theorem and is not claimed here.

### Why a basis change does not repair the Schur argument

Chebyshev coordinates can make evaluation on a real interval numerically
benign.  The desired conclusion, however, is an order-`r` zero or controlled
Taylor jet at the anchor, followed by the Schur propagation factor

```text
[(alpha-b)/(alpha+b)]^r.                            (4.12)
```

The conversion from a Chebyshev basis on `[-1,0]` back to that local Taylor
jet contains exactly the capacity factor exposed by (4.7).  A reparameterized
proof can move the `4^r` loss; it cannot make it `exp(o(r))`.

The conclusion is not an artifact of the affine coordinate `u`.  In the
natural half-plane Schur coordinate

```text
omega_b(z)=(z-b)/(z+b),                             (4.12a)
```

the real segment `0<=z<=b` is again `[-1,0]`.  The one-cell imaginary
thickness maps to an `O(1/L)` complex thickening of that interval, with only
`O(1/L^2)` horizontal overshoot.  The same Bernstein-ellipse proof therefore
gives the rate `log 4-o(1)`, while the target is exactly

```text
omega_b(alpha)=(alpha-b)/(alpha+b).                 (4.12b)
```

The capacity defect is aligned with the Schur coordinate used in the
conditional attenuation calculation.

Likewise, pushing nodes all the way to the half-plane boundary cannot give
both desired properties.  If their normalized radius is `q<1`, the bounded
analytic Taylor tail is at best

```text
q^(r+1)/(1-q).                                      (4.13)
```

Keeping `q<=1-epsilon` gives an exponential remainder but leaves (4.6).
Taking `q=1-o(1)` to seek another normalization makes (4.13) lose its fixed
exponential saving.

## 5. What happens to the numerical danger envelope

If one keeps the *same-b* Poisson ledger of the conditional calculation and
charges the unavoidable Taylor inversion rate `log 4` per jet, its optimistic
diagnostic becomes

```text
E_4,cap(b)
 ={1/(8*K_b)}
   max{0,log[(alpha+b)/(alpha-b)]-log 4}.            (5.1)
```

At `(alpha,d)=(.49,.66)`, numerical optimization gives

```text
max E_4,cap=.01093464159...
at b=.4300097900...,
.02539125521...-max E_4,cap=.01445661362... .       (5.2)
```

Equation (5.2) is a diagnostic for the old ledger, not a universal theorem
about redesigned mixed-depth fans.  Once nodes have different physical
depths, their Poisson costs and the correct nonlinear Pick geometry must be
recomputed jointly.  The rigorous conclusion is (4.6): the uniform
conditioning premise used to obtain (1.1) is unavailable.

## 6. Primary-literature audit

The literature supports the scope distinction rather than filling the gap.

* Bayer and Teichmann, [*The proof of Tchakaloff's
  Theorem*](https://arxiv.org/abs/math/0502473), Proc. AMS 134 (2006),
  3035--3040, prove finite positive cubature with at most the dimension of the
  moment space, including noncompact support under only the moments actually
  used.  Their theorem has no lower bound on weights, no node-depth bound, and
  no growing-degree condition number.  It therefore gives the `O(r)` count
  but none of the missing uniform estimates.
* Bojanov, Braess and Dyn, [*Generalized Gaussian quadrature
  formulas*](https://doi.org/10.1016/0021-9045(86)90008-0), J. Approx. Theory
  48 (1986), 335--353, prove canonical positive quadratures for extended
  Chebyshev systems.  Ma, Rokhlin and Wandzura,
  [*Generalized Gaussian Quadrature Rules for Systems of Arbitrary
  Functions*](https://doi.org/10.1137/0733048), SIAM J. Numer. Anal. 33
  (1996), 971--996, give a numerical construction.  Neither result says that
  the real and imaginary contour jets in (2.1) form a uniformly conditioned
  extended Chebyshev system as `r` grows, especially at the logarithmic
  endpoint singularity.  Positivity of quadrature weights is not a lower
  bound on the convex-hull inradius.
* Gautschi, [*On inverses of Vandermonde and confluent Vandermonde matrices
  III*](https://doi.org/10.1007/BF01432880), Numer. Math. 29 (1978), 445--450,
  and Li, [*Lower bounds for the condition number of a real confluent
  Vandermonde matrix*](https://doi.org/10.1090/S0025-5718-06-01856-4), Math.
  Comp. 75 (2006), 1987--1995, prove exponential lower bounds for broad real
  Vandermonde and fixed-multiplicity confluent classes.  Theorem 4.1 above is
  the sharper problem-specific version: the interval capacity gives the
  exact rate `log 4`, and the microscopic imaginary thickening changes it by
  only `o(r)`.
* Sarason, [*Generalized interpolation in
  H-infinity*](https://doi.org/10.1090/S0002-9947-1967-0208383-8), Trans. AMS
  127 (1967), 179--203, includes finite Caratheodory--Fejer/confluent data in
  compressed-shift interpolation.  It characterizes exact finite
  `H-infinity` feasibility; it does not turn the reflected-pair Poisson cap
  into a uniform growing-order compressed-shift norm, nor does it supply the
  compact two-leg Paley--Wiener realization required by GP.

Thus no primary theorem located in the survey defeats (4.6), supplies the
missing growing-order inradius, or promotes the `0.0288268L` envelope to an
admissible obstruction.

## 7. Exact scope and next target

| assertion | verdict |
|---|---|
| fixed-order positive Tchakaloff quadrature exists | **yes** |
| exact order-`r` quadrature can remain at scaled depth `o(r)` | **no**, Theorem 3.1 |
| a one-cell order-`r` Taylor evaluation family can have `exp(o(r))` condition number | **no**, Theorem 4.1 |
| the conditional `0.0288268337L` four-row envelope is admissible as stated | **no** |
| (5.2) is a universal ceiling for arbitrary mixed-depth Pick fans | **no** |
| a different global compact Pick upper construction is ruled out | **no** |
| GP is proved or falsified | **no** |

The four-row branch should therefore be retired in its present form.  A live
GP attack must avoid reconstructing a growing local Taylor jet from one-cell
point evaluations.  The two remaining logical possibilities are:

1. a direct global Schur/Pick construction whose norm is controlled by the
   reflected-pair Poisson measure without local jet inversion; or
2. a genuinely mixed-depth obstruction analyzed in its native Pick metric,
   with its varying Poisson costs and compact-tail error included from the
   start.

## 8. Reproduction

```bash
python3 src/test_growing_jet_tchakaloff_barrier.py
python3 results/verify_zeta23_growing_jet_tchakaloff_barrier.py
```

The verifier intentionally reports `gp_closed=false`.  `PASS` means the
depth, capacity, and scoped ledger calculations replay; it does not mean a
strip has been proved.
