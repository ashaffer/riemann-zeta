# Actual-node adversarial design: asymptotic audit

**Date:** 2026-08-13

**Verdict:** **no subpower Schur design, no improved zeta bound, and no
zero-free strip.**  The continuous real-cosine data are most naturally
explained by a random-polytope/atomic-norm law of square-root type (with a
logarithmic gain), not by a subpower law.  A new explicit high-band frame
design gives a theorem-grade `M^{-1/2}` model lower bound, but this is far
below the required scale.

This note attacks, rather than merely restates, the adversarial-design route
from
`ZETA23-OFF-WALL-CONTROL-QSP-CODING-NONCOMMUTATIVE-DESIGN-SPRINT-2026-08-13.md`.
It also records new diagnostics added to
`prime_wiener_continuous_exchange_probe.py`.

---

## 1. The correct new variable is an atomic cancellation cost

For the real-cosine relaxation write

```text
a(xi)=(cos(u_1 xi),...,cos(u_M xi)) in R^M,
b(xi)=2 Re[(cosh((alpha+i xi)w)-1)/(w(alpha+i xi)^2)].       (1.1)
```

The primal continuous extremal is

```text
E_B=sup{|integral b dh| : integral a dh=0, ||h||_TV<=1,
                         supp(h) subset [0,B]}.               (1.2)
```

Split the band into a low carrier band `L=[0,T]` and a high cancellation
band `H=[T,B]`.  For a vector `x in R^M`, define its high-band atomic norm

```text
||x||_(A_H)=inf{||mu||_TV : supp(mu) subset H,
                            integral_H a dmu=x}.               (1.3)
```

The carrier-aware cancellation cost is

```text
C_(T,B)=inf { ||nu||_TV+||mu||_TV :
              supp(nu) subset L, supp(mu) subset H,
              integral a d(nu+mu)=0,
              integral_L b dnu=1 }.                           (1.4)
```

Let `epsilon_T=sup_(xi in H)|b(xi)|`.  Direct scaling gives the exact
perturbative comparison

```text
1/C_(T,B)-epsilon_T <= E_B <= 1/C_(T,B)+epsilon_T.             (1.5)
```

For the upper bound, split any feasible `h=nu+mu`; its high carrier is at
most `epsilon_T`, while scaling by the low carrier shows that the latter is
at most `1/C_(T,B)`.  For the lower bound, normalize a near-minimizer in
(1.4); the high carrier can change its value by at most `epsilon_T`.

Because the target has the analytic tail bound

```text
|b(xi)| <= 2(cosh(alpha*w)+1)/(w(xi^2+alpha^2)),               (1.6)
```

one can make `epsilon_T` an arbitrary fixed power by taking a polynomial
`T`.  Consequently, modulo this harmless tail,

```text
the desired subpower E_B lower bound
    is equivalent to C_(T,B)<=Y^(o(1));

any theorem C_(T,B)>=Y^delta with delta>0.0180303234
    kills this carrier route at the required threshold.       (1.7)
```

This is sharper than asking vaguely for a good Gramian.  It identifies the
only quantity whose asymptotic can matter: the total variation needed to
represent a carrier-rich low phase vector by the high-frequency prime-log
phase curve.

### One-atom specialization

For `q=a(xi_0)`, put

```text
R_H(q)=inf{||mu||_TV : integral_H a dmu=q}.                    (1.8)
```

Then

```text
E_B >= [b(xi_0)-epsilon_T R_H(q)]/[1+R_H(q)].                  (1.9)
```

The numerical optimizer turns out to use almost exactly this architecture:
one low atom supplies the carrier and the other `M` atoms cancel its vector.

Linear-programming duality also gives

```text
R_H(q)=sup_z { <z,q> : sup_(xi in H)|<z,a(xi)>|<=1 }.          (1.10)
```

This is the relevant *directional finite-window Sidon constant*.  A global
Sidon estimate that ignores the carrier direction can be sharp and still be
useless; (1.10) asks whether the particular low carrier vector has an
anomalously cheap representation in the high phase dictionary.

---

## 2. An explicit actual-node frame design

There is a closed-form continuous design for every actual node set.  Let
`rho` be normalized Lebesgue measure on a high interval `H`, and set

```text
G_H=integral_H a(xi)a(xi)^T d rho(xi),
q=a(xi_0),
z=G_H^(-1)q,
dmu(xi)=a(xi)^T z d rho(xi).                                  (2.1)
```

Then

```text
integral_H a dmu=q,
||mu||_TV <= R_2(q):=sqrt(q^T G_H^(-1)q).                     (2.2)
```

The first identity is exact.  The second is Cauchy--Schwarz.  Therefore

```text
h=(delta_(xi_0)-mu)/(1+R_2(q))                                (2.3)
```

is feasible in (1.2), and

```text
E_B >= [b(xi_0)-epsilon_T R_2(q)]/[1+R_2(q)].                 (2.4)
```

Moreover, taking `w` to dominate `|h|` and placing any unused probability
mass at an arbitrary legal frequency gives an explicit adversarial design
with

```text
Delta(w) >= ([b(xi_0)-epsilon_T R_2(q)]/[1+R_2(q)])^2.        (2.5)
```

Thus this is a direct `w_Y`, not just a dual approximation argument.

If the normalized high-band Gramian obeys `G_H>=c I` and `||q||^2<=M`,
then `R_2(q)<=sqrt(M/c)`.  For fixed `xi_0` with `b(xi_0)>0` and negligible
tail,

```text
E_B >= c_1/sqrt(M),       Delta(w)>=c_2/M.                     (2.6)
```

For separated frequencies this frame hypothesis follows from the usual
Ingham/Hilbert inequality once the high interval length times the minimum
separation is large.  In the cosine problem one must apply it to the signed
frequency set `{+u_j,-u_j}`: near-reflected nodes can cause a small Gram
eigenvalue even when the original `u_j` are separated.

This is a rigorous model lower bound and an explicit arithmetic recipe.  It
is not remotely the desired `Y^(-o(1))` design: since
`M asymp Y/log Y`, it is of square-root size.

The number

```text
q^T G_H^(-1)q                                                   (2.6a)
```

is the directional inverse Christoffel function (or leverage score) of the
carrier.  In a generic high-band frame it is `asymp M`.  The exterior-power
or DPP determinant ratio is another expression for the same leverage after
augmentation, so a generic DPP volume calculation cannot change the
square-root conclusion.  A useful DPP effect would have to make this
*specific directional* Christoffel number subpolynomial, not merely make
`det(G_H)` small or the point process repulsive.

### Floating actual-node values

The updated probe evaluates the exact analytic Gram entries on
`H=[B/2,B]`.  The following are floating diagnostics; their eigenvalue
bounds have not been interval-certified.

| `Y` | `M` | `lambda_min(G_H)` | `R_2(a(0))` | bound (2.4), `xi_0=0` | bound at dominant atom |
|---:|---:|---:|---:|---:|---:|
| 100 | 9 | .1188 | 5.363 | .03140 | .04073 |
| 300 | 23 | .1879 | 7.081 | .02477 | .02626 |
| 1000 | 61 | .2533 | 11.242 | .01635 | .01761 |
| 3000 | 151 | `6.32e-5` | 17.296 | .01094 | .01232 |

At `Y=3000`, the small eigenvalue comes from the almost reflected pair

```text
u=log(3001/3000)= .000333277790...,
u=log(2999/3000)=-.000333388901...,
||u_1|-|u_2||=1.11111117e-7.                                  (2.7)
```

The aperture resolves their cosine difference only weakly.  Nevertheless
`R_2(a(0))^2=299.1`, essentially `2M=302`: the carrier direction is almost
orthogonal to the bad eigenvector.  This is an important DPP warning.
A tiny determinant or Gram eigenvalue helps only if the augmented carrier
has leverage in that same direction; the Schur complement correctly ignores
an irrelevant twin-prime collision.

---

## 3. Generic asymptotic: square root, with a logarithmic gain

The high-frequency columns `a(xi)` can be modeled, after decorrelation, by
`K` random sign vectors in `R^M`.  Let `q` have norm `asymp sqrt(M)`, and
let

```text
R_K(q)=inf{||c||_1 : sum_(k<=K)c_k X_k=q}.                     (3.1)
```

The standard random-polytope inradius estimate (the Gluskin/Kashin regime)
for `CM<=K<=exp(cM)` gives, for a fixed generic `q`,

```text
R_K(q) asymp sqrt(M/log(K/M))                                  (3.2)
```

with high probability.  The easy obstruction direction is already
instructive:

```text
R_K(q)>=||q||^2/max_k |<q,X_k>|
       >= c sqrt(M/log K),                                    (3.3)
```

because the maximum of `K` subgaussian correlations is
`O(sqrt(M log K))`.  The reverse inequality is the random-polytope inradius
theorem.

Combining (1.9) with (3.2), a polynomial number of effectively independent
phase cells predicts

```text
E_B asymp sqrt(log(K/M)/M),                                   (3.4)
```

up to target-dependent constants.  Thus among the proposed possibilities,
the generic answer is **`M^{-1/2}` up to a square-root logarithm**.  It is
not `log(M)/M`, and it is not subpower.  With `M asymp Y/log Y` and
polynomial `K`, (3.4) is of order `log(Y)/sqrt(Y)`.

The arithmetic route can beat this only if the prime-log phase curve has a
highly non-generic coherent convex-hull direction.  Pairwise phase
orthogonality, a well-conditioned average Gramian, or a DPP volume estimate
all lead back to (2.6)--(3.4), not to a subpower lower bound.

### A tractable one-atom kill test

For the numerically observed one-atom architecture, define the prime-log
kernel

```text
K(xi_0,xi)=<a(xi_0),a(xi)>.                                   (3.5)
```

Every high-band representation of `q=a(xi_0)` satisfies

```text
R_H(q)>=||q||^2/sup_(xi in H)|K(xi_0,xi)|.                    (3.6)
```

Hence a uniform arithmetic estimate

```text
sup_H |K(xi_0,xi)| <= M Y^(-delta)                            (3.7)
```

forces `R_H(q)>=Y^delta` and caps the one-atom carrier at
`O(Y^(-delta))`.  Any `delta>.0180303234` kills that observed architecture.
To kill arbitrary low signed combinations one needs the carrier-aware
version `C_(T,B)>=Y^delta` from (1.4), rather than only (3.7).  Conversely,
a subpower success must exhibit a carrier-rich low measure whose high-band
atomic representation cost is `Y^(o(1))`.  This is a precise falsifiable
criterion.

---

## 4. What the support atoms and weights actually do

The probe now reports every support atom and weight (`--show-support`), JSON
output (`--json`), arbitrary powers `B=Y^beta` (`--bandwidth-power`), phase
cells, normalized gaps, weight effective support, and the frame certificate
of Section 2.

At the full aperture `B=Y^(50/33)`:

| `Y` | `M` | `E_B` | dominant `xi` | dominant mass `w_0` | `(1-w_0)/w_0` | objective from `xi<=50` |
|---:|---:|---:|---:|---:|---:|---:|
| 100 | 9 | .06842194 | 6.497 | .39458 | 1.534 | 1.00079 |
| 300 | 23 | .05541187 | 7.920 | .34286 | 1.917 | 1.00000 |
| 1000 | 61 | .04046958 | 6.543 | .23370 | 3.279 | 1.00000 |
| 3000 | 151 | .03157993 | 7.384 | .18939 | 4.280 | 1.00000 |

The tiny excess above one is cancellation from the negligible high-frequency
target values.  The invariant observation is strong:

```text
one atom at xi about 6--8 supplies essentially the entire carrier;
the other M atoms spend their total variation cancelling its feature vector.
                                                                    (4.1)
```

The dominant-mass to extremal ratio is

```text
w_0/E_B = 5.77, 6.19, 5.77, 6.00,                              (4.2)
```

while the cancellation cost tracks the random-polytope scale:

| `Y` | `(1-w_0)/w_0` | `sqrt(M/log B)` | ratio |
|---:|---:|---:|---:|
| 100 | 1.534 | 1.136 | 1.351 |
| 300 | 1.917 | 1.631 | 1.175 |
| 1000 | 3.279 | 2.414 | 1.358 |
| 3000 | 4.280 | 3.528 | 1.213 |

Other diagnostics also argue against a coherent arithmetic phase cell:

| `Y` | weight effective support | `|mean exp(i xi/Y)|` | weight/cell-size correlation |
|---:|---:|---:|---:|
| 100 | 4.33 | .406 | .311 |
| 300 | 6.34 | .200 | -.117 |
| 1000 | 13.63 | .121 | -.067 |
| 3000 | 21.54 | .060 | .002 |

Here the middle column is exactly the reported resultant of
`xi/(2 pi Y) mod 1`.  It trends toward zero; the weights do not converge to
Voronoi cell sizes; support signs are irregular; and normalized gaps have a
broad, non-stabilizing distribution.  No multiplicative lattice or stable
phase-cell code was detected.

---

## 5. Scaling audit: the four-point power fit is not a theorem

For the four full-aperture values,

```text
least-squares apparent exponent versus Y:  .2311,
least-squares apparent exponent versus M:  .2792,
local Y exponents: .1920, .2610, .2258.                         (5.1)
```

There is a numerically striking identity

```text
E_B Y^(8/33)=.209, .221, .216, .220,                            (5.2)
```

where `8/33=1-(50/33)/2`.  This initially suggests an aperture-edge chirp
law `sqrt(B)/Y`.  It does **not** survive the more discriminating fixed-`Y`
test.  At `Y=1000`:

| `B` | `E_B` | increase from previous | `sqrt(B)` prediction |
|---:|---:|---:|---:|
| 3981 (`Y^1.2`) | .029396 | -- | -- |
| 11220 (`Y^1.35`) | .034949 | 1.189 | 1.679 |
| 35112 (`Y^(50/33)`) | .040470 | 1.158 | 1.769 |

The aperture dependence is much closer to a logarithmic increase than to
`sqrt(B)`.  Equation (5.2) is therefore a finite-range coincidence or a
transition effect, not evidence for an asymptotic exponent.  The atomic
cancellation cost and phase-cell diagnostics favor (3.4), but even that is
only a model prior, not an actual-node theorem.

The continuous exchange discrepancies are between `5.6e-7` and `4.5e-6`
relatively, and prime-null residuals are between `1e-15` and `2e-14` on the
sampled/refined extrema.  The derivative search is not interval-certified;
the `Y=3000` row is exploratory floating evidence.

---

## 6. Decision

What was achieved:

1. an exact carrier-aware atomic cancellation criterion, (1.4)--(1.7);
2. an explicit actual-node high-band design and Schur lower bound,
   (2.1)--(2.6);
3. a precise generic asymptotic prior: `M^{-1/2}` with a square-root log;
4. a support audit showing that the optimizer is a one-low-atom cancellation
   problem and currently behaves like a random phase polytope;
5. a concrete arithmetic kill target, (3.7), and its full carrier-aware
   upgrade `C_(T,B)>=Y^delta`.

What was not achieved:

```text
an explicit design with Delta>=Y^(-o(1)):       NOT FOUND;
a proof of the random-polytope law for primes:  NOT PROVED;
an actual-node power upper bound killing route: NOT PROVED;
the required E_Y lower bound:                   NOT PROVED;
a uniform zeta zero-free strip:                 NOT PROVED.   (6.1)
```

The route should remain alive only for a targeted attempt to disprove the
random-polytope prior: find a carrier-rich low measure with a visibly
subpower high-band atomic cost.  Merely extending the current floating
power fit is low value.  If no such coherent measure appears, the natural
next theorem is instead an arithmetic lower bound on `C_(T,B)` (or a
large-sieve bound of type (3.7)), which would close this route rather than
prove the strip.
