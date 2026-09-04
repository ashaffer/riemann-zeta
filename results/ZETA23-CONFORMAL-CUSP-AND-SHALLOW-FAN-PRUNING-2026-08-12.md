# The conformal Pick cusp and a shallow-fan pruning theorem

Status: exact conformal identity, exact continuum rigidity, exact half-delay
construction, and a growing compact-transfer theorem, 2026-08-12.  The
remaining deep-fan quadrature is open.  No global Pick transfer, zero-free
strip, or RH result is proved.

## 1. Verdict

The all-jet contour has a simple conformal meaning.  Put

```text
h(x)=-lambda_0+(2/d)log cos(x/2)-i*x/d,
w(h)=2 exp[d(h+lambda_0)/2]-1.                     (1.1)
```

Then, exactly,

```text
w(h(x))=exp(-i*x).                                 (1.2)
```

Thus the continuum half-disk problem is a positive-real boundary problem
on the unit circle.  In the bounded (more generally, subcritical-cusp)
class, if the whole contour were physically available, then `V=wU` would
have nonnegative real part on its boundary and the interior zero `w=0`;
the minimum principle forces `V`, and hence `U`, to vanish.  Bare
holomorphy is not enough at this unbounded boundary: exponential type
`d/2` is the sharp escape threshold.

This does **not** give a finite actual-count counterexample.  The contour
runs to `Re h=-infinity`, whereas the physical half-plane stops at
`Re h=-alpha*L`.  In the `w` plane this removes a cusp of size

```text
exp[-alpha*d*L/2+O(1)]                             (1.3)
```

at `w=-1`.  The elementary half-delay uses precisely that cusp and signs an
entire phase cell at target cost

```text
alpha*d*L/2=.1617*L                                (1.4)
```

for `(alpha,d)=(.49,.66)`.  This is a rigorous universal construction, but
it is far above the available `0.025391255 L` surcharge.

The useful positive result is a pruning theorem.  Let the largest inward
scaled depth of every row in one microscopic cell be `Lambda_L`.  If

```text
Lambda_L=o(L/log L),                               (1.5)
```

then the coherent compact endpoint construction signs every row in that
cell, with arbitrary cardinality and spacing, while losing only `o(L)` in
the carrier exponent.  Therefore a fixed-exponent growing-jet obstruction
must have depth reach at least order `L/log L`; concentration and row count
alone are not enough.

In particular, the natural odd root-of-unity sampling of (1.1) has maximum
depth `O(log L)` for `O(L)` rows and is rigorously harmless at fixed-power
scale.  It cannot falsify the desired surcharge theorem.

What remains is exact and narrow: a counterexample would require a positive
quadrature of growing jet order whose nodes reach the cusp at scaled depth
at least `L/log L`, with quantitative positive-spanning condition number;
a proof would need a uniform compressor for precisely those deep fans.

## 2. Exact conformal form and sharp continuum rigidity

For `-pi<x<pi`, exponentiating (1.1) gives

```text
exp[d(h(x)+lambda_0)/2]
 =cos(x/2)exp(-i*x/2)
 =(1+exp(-i*x))/2,                                 (2.1)
```

which proves (1.2).  More precisely, put

```text
Omega={h=u+i*v: |v|<pi/d,
       u<-lambda_0+(2/d)log cos(d*v/2)}.           (2.2)
```

Then `w` maps `Omega` conformally onto the unit disk, with inverse

```text
h(w)=-lambda_0+(2/d)Log[(1+w)/2].                 (2.3)
```

The parametrization `x:-pi -> pi` gives `w=exp(-i*x)`, so it traverses the
boundary **clockwise**, i.e. with negative orientation; `Omega` is the
left/cusp side of the curve.  It contains

```text
h_*=-lambda_0-(2/d)log 2,      w(h_*)=0.           (2.4)
```

Suppose `U` is bounded and holomorphic in `Omega`, has the needed
nontangential boundary values, and obeys

```text
Re[exp(-i*x)U(h(x))]>=0.                           (2.5)
```

Then `F(w)=wU(h(w))` belongs to `H^infinity` of the disk, has nonnegative
boundary real part, and satisfies `F(0)=0`.  The Poisson/minimum principle
gives `Re F>=0`; its interior minimum forces `Re F=0`, and the open mapping
theorem gives `F=0`, then `U=0`.  This is the maximum-principle version of
the all-moment identity

```text
integral_(-pi)^pi exp(-i*x)h(x)^k dx=0,
k=0,1,... .                                       (2.6)
```

The cusp hypothesis is sharp.  If, as `Re h -> -infinity` in `Omega`,

```text
|U(h)|<=C exp[-tau*Re h],       tau<d/2,           (2.7)
```

then `F(w)=O(|1+w|^(-2*tau/d))` belongs to `H^1`, so the same argument
still forces `U=0`.  At the endpoint `tau=d/2`, however,

```text
U_crit(h)=exp[-d*(h+lambda_0)/2]=2/(1+w)           (2.8)
```

is entire in `h` and satisfies

```text
Re[w*U_crit(h)]=1                                  (2.9)
```

on the contour.  Thus the often-stated claim with only "analytic on the
full contour interior" is false; one must control the prime end at
`w=-1`.  This endpoint countermodel is exactly the half-delay below.

For the physical rescaling `z=alpha+h/L`, however, analyticity is available
only for `Re h>-alpha L`.  On that cut,

```text
|1+w|=2 exp[d(Re h+lambda_0)/2]
      >=2 exp[-alpha*d*L/2+O(1)].                 (2.10)
```

Thus the ideal argument illegally fills the exponentially small cusp around
`w=-1`.  This is the exact escape from continuum rigidity.

## 3. The exact half-delay and what it costs

Write a node in one normalized phase cell as

```text
z=alpha-lambda/L-i*x/(dL),       |x|<=pi.          (3.1)
```

The Schur function

```text
U_half(z)=exp(-d*L*z/2)                              (3.2)
```

has target modulus `exp(-alpha*d*L/2)`.  Its normalized row margin is

```text
Re[exp(-i*x)U_half(z)]
 =exp[-alpha*d*L/2+d*lambda/2]cos(x/2)>=0.          (3.3)
```

In conformal coordinates its target-normalized response is

```text
exp(-d*h/2)=2 exp(d*lambda_0/2)/(1+w).             (3.4)
```

The pole at `w=-1` explains both why it evades Section 2 and why its price is
half of the full delay.  At `.49,.66`, (3.2) spends `.1617 L`, so it is a
fallback construction rather than closure of the present ledger.

## 4. A growing shallow-fan compact-transfer theorem

### Theorem 4.1

Fix `0<d<1`, `alpha>0`, and `C<infinity`.  Let

```text
D=dL,
beta_j=alpha-lambda_j/L,
delta_j=c_j/L,
0<=lambda_j<=Lambda_L,       |c_j|<=C,             (4.1)
```

where the list may have arbitrary finite cardinality and spacing.  If

```text
(Lambda_L+1)log L=o(L),                            (4.2)
```

then the real compact two-endpoint construction of the coherent
microcluster theorem can be chosen with degree

```text
n_L=O_(d,C)(Lambda_L+1)                            (4.3)
```

and signs every row in (4.1), while its selected carrier is

```text
exp[alpha*d*L-O_(d,C)((Lambda_L+1)log L)]
 =exp[alpha*d*L-o(L)].                             (4.4)
```

The conclusion is uniform in the number of rows.

#### Proof

Put `s=-lambda-i*c`.  The required virtual translation is `exp(-d*s)`.
On the rectangle in (4.1), `|d*s|=O_(d,C)(Lambda_L+1)`.  Its Taylor
polynomial `p_n`, with real coefficients and `p_n(0)=1`, obeys the elementary
complex remainder bound

```text
|exp(-d*s)-p_n(s)|
 <=exp(R)*R^(n+1)/(n+1)!,
R=d*sqrt(Lambda_L^2+C^2).                           (4.5)
```

Stirling's bound shows that a sufficiently large fixed multiple of
`Lambda_L+1` makes (4.5) less than `1/8`, proving (4.3).  Consequently

```text
Re[exp(-i*d*c)p_n(-lambda-i*c)]
 >=exp(d*lambda)-1/8>=7/8.                         (4.6)
```

Choose the fixed endpoint bump in a compact Gevrey-2 class, so its derivative
norms obey `||phi^(k)||<=C^(k+1)(k!)^2`.  (The standard flat exponential
bump has this property.)  Apply the compact differential filter

```text
p_n(L*(-partial_t-alpha))                          (4.7)
```

to the right endpoint bump and use the unfiltered left endpoint bump, with
the scalar correction imposing the selected positive-row equation.  This
does not enlarge support.  Integration by parts gives (4.6) as the exact
leading collateral factor, exactly as in the fixed-rectangle coherent
microcluster theorem.

The Taylor coefficients, the Gevrey derivative bound, and Stirling give a
filter norm at most `exp[O(n_L log L)]`; this explicit choice is important,
since an arbitrary fixed smooth bump has no useful uniform growing-derivative
bound.  The wrong-end endpoint contribution has the same upper cost.  Thus
the total normalization cost is at most

```text
exp[O(n_L log L)].                                 (4.8)
```

Condition (4.2) makes (4.8) subexponential relative to the endpoint carrier;
it also makes the wrong-end term negligible.  This proves (4.4) and every
strict row sign.  No inverse matrix depends on the list cardinality.  QED

The theorem is a direct compact two-leg statement for a target-local cell.
It does not by itself combine independently recentered remote cells, nor
does it prove the global scalar Schur surcharge theorem after an arbitrary
representative product.

## 5. Root-of-unity sampling is below the danger scale

Take odd `N` and the phases

```text
x_j=2*pi*j/N,       -(N-1)/2<=j<=(N-1)/2.          (5.1)
```

The associated contour depths are

```text
lambda_j=lambda_0-(2/d)log cos(x_j/2).             (5.2)
```

The largest one is exactly

```text
Lambda_N=lambda_0+(2/d)log csc[pi/(2N)]
        =(2/d)log N+O_(d,lambda_0)(1).             (5.3)
```

Thus even `N=Theta(L)` gives `Lambda_N=O(log L)`, and Theorem 4.1 signs the
whole root fan with loss `O((log L)^2)=o(L)`.  The logarithmic singularity at
the missing root `-1` is not deep enough to produce a fixed exponent.

This corrects the tempting inference that increasingly dense sampling of
the visible contour must approach the continuum obstruction.  Density on
the circle is not the relevant resource; penetration into its exponentially
small physical cusp is.

### 5.1 Cross-check with the cosh lattices

There is no conflict with either exact lattice theorem in the earlier Pick
audit.  The uniform cosh quotient

```text
B_(a,D)(s)=cosh[(D/2)(s-a)]/cosh[(D/2)(s+a)]
```

signs the depth/ordinate continuum through **every** phase cell.  It is
asymptotic to the full delay `exp(-D*s)` and costs `alpha*D+O(1)` at the
target.  By contrast, (3.2) is a half-delay and its factor
`cos(D*delta/2)` is nonnegative only in one recentered cell; it changes
sign in the neighboring cells.  Independent recentering would destroy the
single global analytic function.

The alternating half-density sinh/cosh lattice attains a half-product for
one specially interlaced node per cell.  It does not sign the full
depth/phase continuum in every cell.  Thus the three exact models line up:

```text
one arbitrary cell continuum       half-delay cost alpha*D/2,
special alternating global list    half-product cost,
all cells, all phases and depths    full-delay cost alpha*D.
```

None is an upper or lower theorem for an arbitrary finite deep fan.

## 6. Exact remaining gate

Theorem 4.1 removes every fan satisfying

```text
max lambda_j=o(L/log L).                           (6.1)
```

The continuum identity shows that arbitrarily high fixed jets do exist if
unbounded depth is allowed.  To decide the global surcharge, one now needs
one of the following mutually exclusive quantitative results.

1. **Positive result:** compress every actual fan reaching
   `lambda >= cL/log L`, under the completed Poisson cumulative budget, at
   surcharge `<0.025391255 L`, and make the construction stable under the
   representative-product phase twist and compact recentering.
2. **Negative result:** construct positive atomic quadratures for (2.4) of
   order `r asymp L/log L` (or stronger), with all depths `<alpha L`, with a
   quantified positive-spanning constant strong enough that Taylor and
   Schur remainders force loss `>=0.025391255 L`; then verify the cumulative
   depth-sensitive Poisson count, not merely the total row count.

No theorem presently supplies either statement.  The conformal reduction
does show that generic Carleson embedding, root-of-unity sampling, fixed
Hermite order, and bounded-depth coherent interpolation are no longer the
right search space.

## 7. Reproducibility

The companion module checks (1.2), (3.3), (5.3), and the Taylor bound (4.5):

```text
src/conformal_pick_cusp.py
src/test_conformal_pick_cusp.py
```

These computations reproduce elementary identities only.  They do not
certify a growing quadrature or a zero-free strip.
