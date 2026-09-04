# Endpoint-jet compact carrier margin

Status: exact qualitative correction and quantitative gate, 2026-08-11.  This
note proves a separation-free negative edge at each fixed set of parameters.
It does not give an effective lower bound strong enough to compare with the
remote tail, and therefore does not prove a zero-free strip.

Later quantitative correction: the qualitative compactness theorem remains
valid, but its proposed uniform asymptotic target is false on the whole
collared carrier and the near-full-pair power target is false even in the
core from zero-count and density inputs alone.  See
[`ZETA23-ENDPOINT-JET-COLLAR-CARRIER-RATE-OBSTRUCTION-2026-08-11.md`](ZETA23-ENDPOINT-JET-COLLAR-CARRIER-RATE-OBSTRUCTION-2026-08-11.md)
and
[`ZETA23-CORE-SUBLATTICE-CARRIER-POWER-LOSS-2026-08-11.md`](ZETA23-CORE-SUBLATTICE-CARRIER-POWER-LOSS-2026-08-11.md).
After imposing the proved simple-critical-line density, the explicit core
configuration has `K<=X^(6*alpha/7+o(1))/L`; compatibility with separately
evaluated trace, Frobenius, and pair-correlation data is not claimed.  This
does not affect the strict fixed-parameter conclusion.

## 1. Verdict

The vanishing of an ordinary Cauchy--Vandermonde minor when two rows collide
is not, by itself, an obstruction to the signed zero-side carrier.  Rows
which collide have the same hyperbolic orientation and their positive
multiplicity weights add.  After collision strata are compactified in this
way, the following is true.

For fixed `T,L,m`, a compact ordinate carrier, a fixed upper bound on total
multiplicity, and a distinguished pair of depth at least `delta>0`, the
endpoint-jet zero form has a negative eigenvalue bounded away from zero
uniformly over all allowed configurations, with no zero-separation
hypothesis.  The bound follows by compactness and is not effective in the
parameters.

Thus clustering/confluent interpolation repairs the *qualitative* carrier
gate.  For a distinguished pair constrained to a fixed modulation core, a
surviving tail-comparison question is

```text
log(1/kappa_comp(T,L,m,delta))
       = o(eta^2*T/log T) ?
```

The displayed estimate is false if the distinguished pair may lie in the
collar.  Even in the core, zero-count and simple-line-density inputs permit
the `k=7` power loss `K<=X^(6*alpha/7+o(1))/L`; any core lower theorem at a
power scale must therefore allow at least the loss `alpha/7` on that ledger.
No suitable lower estimate follows below.  In particular, the earlier
estimate for the least singular value of the full value-interpolation matrix
is too pessimistic for this signed question, but replacing it by a divided-
difference norm does not by itself supply the required rate.

## 2. Setup

Let `V_m` be the real endpoint-jet space from Theorem 2.1 of the endpoint-jet
report, equipped with the coefficient `ell^2` norm (equivalently, fix once
and for all an orthonormal basis for that norm), and put

```text
Ev_z(c)=F_c(z).
```

For a finite reflection-invariant configuration write its local quadratic
form, before an inessential common positive normalization, as

```text
Q_Z(c)
 = sum_(r on line) M_r F_c(r)^2
   + 2 sum_(z below line) M_z Re(F_c(z)^2).             (2.1)
```

Here all multiplicities are positive integers and `F_c(conj z)=conj F_c(z)`.
An off-line pair is parameterized by `(gamma,alpha)`, with
`z=gamma-i*alpha`; at `alpha=0` its term in (2.1) becomes the positive term
`2M_z F_c(gamma)^2` continuously.

All matrices below use this fixed orthonormal basis and the common
isolated-zero normalization `1/(a*L^2)`.  Without a fixed domain norm and a
common positive normalization, an eigenvalue magnitude would not be
invariant under a change of coordinates; its sign and inertia would be.

For the sharp grid, a real unused sine-grid point can be a common zero of
all the transforms in `V_m`.  Such a row contributes the zero form and is
deleted from the effective node set.  A distinguished off-axis node is
never blind, since

```text
|sin(L*(z-tau_0)/2)| >= sinh(L*delta/2) > 0
```

when `|Im z|>=delta`.  Equivalently one may extend the coordinate grid over
the carrier collar, as in the endpoint-jet report.

## 3. Separation-free fixed-parameter theorem

### Theorem 3.1 (compact signed carrier margin)

Fix the following data.

1. A finite-dimensional endpoint-jet space `V_m` of dimension `n>=2`.
2. A compact real ordinate interval `J` and `0<delta<=1/2`.
3. An integer `Nmax<=n`.

Let `C` range over all finite reflection-invariant configurations in

```text
{z : Re z in J, |Im z|<=1/2}
```

having total point multiplicity at most `Nmax` and containing an off-line
pair of depth at least `delta`.  Delete blind real rows as above.  Assume the
Cauchy--Vandermonde evaluation theorem on `V_m`: evaluation onto every set
of at most `n` distinct effective nodes is surjective.

Then, in the fixed coefficient norm and normalization above, there is a
number

```text
kappa_comp=kappa_comp(V_m,J,Nmax,delta)>0              (3.1)
```

such that every normalized local matrix `H_C` of (2.1) satisfies

```text
lambda_min(H_C) <= -kappa_comp.                        (3.2)
```

No lower bound on the separation of distinct nodes is assumed.

#### Proof

First fix a configuration.  Merge coincident on-line atoms, and merge
coincident off-line pairs, by adding their multiplicities.  If an off-line
pair reaches `alpha=0`, merge its limiting contribution into the on-line
atom with twice its multiplicity.  The resulting direct value space has one
positive real coordinate for each effective on-line location and one real
hyperbolic plane for each distinct off-line pair.  Its dimension is at most
the original total point multiplicity and hence at most `n`.

The Cauchy--Vandermonde theorem makes the evaluation map from `V_m` onto
this direct value space surjective.  Pullback by a surjective map preserves
the inertia of the nondegenerate direct form and only appends zero
directions.  Since a pair of depth at least `delta` remains, the pullback has
a negative eigenvalue.  Thus

```text
lambda_min(H_C)<0                                     (3.3)
```

for every allowed `C`, including every collision stratum.

There are only finitely many choices of the number and type of labelled
atoms and of their integer multiplicities, because total multiplicity is at
most `Nmax`.  For each choice, allow atom parameters to range over the
closed carrier, allow collisions, and allow pair depths to reach zero,
while requiring at least one labelled pair to have depth at least `delta`.
This is compact.  The matrix entries, written using the original entire
integrals rather than the removable Cauchy quotient, vary continuously.
The least eigenvalue is continuous.  Equation (3.3) holds at every point of
every compact stratum, so the maximum of these least eigenvalues is strictly
negative.  Taking the minimum of its magnitude over the finite union gives
(3.1)--(3.2).  QED

### Corollary 3.2 (what row coalescence does and does not show)

The estimate

```text
sigma_min(E_values)=O(|z_1-z_2|)
```

for the ungrouped value matrix remains correct.  It cannot, however, be
used to conclude that the most negative eigenvalue of (2.1) tends to zero:
at `z_1=z_2` the two same-orientation atoms become one atom of larger
multiplicity, and Theorem 3.1 remains applicable.  A quantitative proof must
use cluster values or divided differences, rather than demand a uniformly
bounded right inverse for arbitrary independent values on coalescing rows.

## 4. Exact lattice screening check

The full lattice countermodel has one reflected pair at each spacing
`h=2*pi/L`.  It has point density

```text
2/h=L/pi.                                             (4.1)
```

At the padded edge `L=ell_1+eta`, the zeta point density is
`ell_1/(2*pi)`.  Hence the full screening lattice has asymptotically twice
the allowed point density and, on a carrier of the modulation-band length,
has about twice as many direct coordinates as `dim V_m`.  It violates the
cardinal hypothesis `Nmax<=dim V_m` in Theorem 3.1.  Restriction to `V_m`
does not change the exact positive-semidefinite lattice identity, but it
does not repair this count failure.

At `L=ell_1/2` the full lattice has the correct leading zeta density, exactly
as recorded in the single-block gate, but then the Gabor space has only
about half as many coordinates as zero points.  This is the other side of
the same count failure.

If instead one keeps every second pair at the padded edge, the point density
has the correct leading scale `L/(2*pi)` but its direct-node count is still
the raw coordinate count `d`; after imposing `m` jets one must thin at least
`m` further nodes (and match the small `L-ell_1` density surplus) before the
count can fit `dim V_m=d-m`.  The exact full-lattice screening identity is
already lost at the every-second step.  For any finite sharp Cauchy pullback
which does satisfy the count hypothesis, surjectivity forces one negative
direction per retained pair, in agreement with Theorem 3.1.  Thus the exact
lattice model is a decisive test against claims based only on local
counting, but it is not a counterexample to the padded
Cauchy--Vandermonde theorem.

## 5. Why the quantitative comparison remains open

For `L=ell_1+eta`, Riemann--von Mangoldt gives, uniformly for intervals in
the height range under discussion,

```text
# zeros in [x,x+R]
  = integral_x^(x+R) log(t/(2*pi))/(2*pi) dt
      + O(log T),                                     (5.1)
```

up to the bounded variation of the main density on a dyadic height range.
For the global `[T,2T]` carrier its average is `ell_1/(2*pi)`; a mesoscopic
padding `eta -> infinity` also absorbs the bounded local variation.  The
interpolation type then has surplus of order `eta/(2*pi)`, while the number
of points which may form one unit-scale cluster is `O(log T)`.  This is
precisely the regime in which a
grouped Paley--Wiener/divided-difference theorem could plausibly give a
margin of the form

```text
kappa_comp >= exp(-poly(log T,1/eta)),                 (5.2)
```

which would dominate the endpoint tail

```text
exp(-c*eta^2*T/log T).                                 (5.3)
```

But (5.2) is not a consequence of the references inspected here.  In
particular, Gaunard's divided-difference restriction theorem for
`N`-Carleson sequences characterizes a Paley--Wiener isomorphism using an
additional generating-function/discrete Muckenhoupt condition.  The zeta
inputs (5.1) and `N(t+1)-N(t)<<log t` give a density gap and an
`N=O(log T)` decomposition, but they do not provide that Muckenhoupt
condition or a quantitative interpolation constant.  Ordinary determinant
bounds reintroduce arbitrary intra-cluster spacings and therefore do not
prove (5.2).

The precise reference is F. Gaunard, *Divided Differences & Restriction
Operator on Paley--Wiener Spaces `PW_tau^p` for `N`-Carleson Sequences*,
Theorem 17 (arXiv:1104.2141).  Its extra condition is substantive, not a
notation for the density hypothesis.

The compactness proof also supplies no rate: its constant may deteriorate
with `n`, `m`, the carrier length, and the shrinking relative density gap.
Consequently it cannot yet be compared honestly with (5.3).

## 6. Revised gate

The carrier conclusions are now:

```text
proved:
  qualitative Cauchy--Vandermonde interpolation;
  separation-free fixed-parameter negative edge after collision merging;
  exponentially small endpoint-jet remote tail;

not proved:
  an effective grouped-interpolation/negative-edge bound with
  log(1/kappa)=o(eta^2*T/log T).
```

Accordingly, zero separation is not logically necessary for the carrier,
and the raw least-singular-value collapse is not an exact no-go theorem.
The uniform-strip route still cannot advance without a quantitative grouped
interpolation theorem (or a different carrier argument), in addition to the
independent prime-side lower-edge estimate.
