# Orthogonal research paths after the Weil near-kernel audit

Status: research prospectus, 2026-07-31.  These are proposed programs and
falsifiable intermediate targets, not claimed theorems.

## Executive conclusion

Our work did not reveal a route from fixed-window positivity to RH.  It did
reveal why many apparently different routes failed: they were coordinate
descriptions of the same localized Weil near-kernel.  Prime/zero formulas,
Suzuki kernels, collar propagation, Birman--Schwinger transforms, CCM
determinants, and canonical-system radicals did not supply independent
constraints.  The ground margin collapses so quickly that excellent `L2`
alignment is compatible with almost complete failure in the relative energy
topology.

The next program should therefore import structure which is not already
encoded by the explicit formula.  The three best candidates are:

1. a combinatorial Hodge index for finite-prime Frobenius correspondences;
2. a passive-scattering realization whose negative index counts off-line
   zeros;
3. a multiscale arithmetic inverse theorem turning an off-line zero into
   forbidden persistent structure of a multiplicative function.

A fourth, cheaper-to-falsify path seeks a stable multivariate lift of the xi
Jensen polynomials.

## Lessons that constrain every future path

### Coordinate changes do not add information

The explicit formula is one identity.  Rewriting its possible radical as a
prime balance, zero sum, convolution equation, kernel null vector, or
determinant mode cannot by itself contradict that radical.  A successful path
must add geometry, dynamics, or arithmetic rigidity not derivable from the
same identity.

### Absolute errors are the wrong currency

The localized ground eigenvalue collapses by many orders of magnitude.  The
CCM vector can have `L2` alignment above `0.99999` while its scale-free
Feshbach ratio is above `0.999999`.  Any comparison must live in a graph norm,
an index, or an exact structural class stable under limits.

### Finite-window positivity is evidence, not propagation

Arbitrarily many positive truncations do not identify the infinite limit.
Uniform support propagation is essentially where RH hides.  A new route must
make the limit automatic through a closed category: cohomological
correspondences, passive systems, inverse-theorem rigidity, or stable
polynomials.

### Exceptional zeros evade average statistics

GUE, density-one hyperbolicity, almost-all short-interval cancellation, and
generic simplicity can coexist with a sparse off-line set.  The target must be
pointwise enough to detect one exceptional zero.

## Path I: finite-prime tropical Hodge theory via Lorentzian polynomials

### Connection

Weil's function-field proof obtains RH from an intersection pairing and the
Hodge index theorem on a surface.  In characteristic zero, the arithmetic and
scaling sites provide Frobenius correspondences and partial Riemann--Roch
geometry, but the decisive square/intersection inequality is missing.

Modern Lorentzian-polynomial theory supplies an abstract Hodge--Riemann
package for objects far more combinatorial than algebraic varieties.  Its
Hessian has exactly one positive direction; its support is governed by
M-convexity; and the class is closed under many positive differential and
specialization operations.  This machinery postdates the original
function-field analogy and is naturally compatible with tropical semirings.

The proposed bridge is not “build all of absolute algebraic geometry.”  For a
finite set of primes `S` and a finite set of scaling parameters, construct a
finite correspondence semiring and its intersection/volume polynomial

`V_S(x_0,...,x_m) = degree((x_0 H + sum_j x_j Gamma_j)^d)`.

Prove directly that `V_S` is Lorentzian.  The Lorentzian Hodge--Riemann
inequality would then give the conditional negative definiteness of the
degree-zero correspondence pairing.  The explicit formula should identify
that finite pairing with the `S`-truncated Weil form.  A monotone or Mosco
limit in `S` would produce the full Weil inequality.

### Why this adds rank

The inequality would come from the incidence/exchange structure of prime
correspondences, not from diagonalizing the Weil form.  It is therefore not a
restatement of positivity.  It attacks the exact geometric ingredient that
makes the function-field theorem work.

### First three targets

1. Define the finite-prime divisor/correspondence algebra and verify that its
   degree recovers the prime-power coefficients `log p` with the correct
   archimedean completion.
2. Compute the support of `V_S` and test the M-convex exchange axiom.  Failure
   here cheaply kills the naive Lorentzian model.
3. Prove Lorentzianity inductively under adjoining one prime, then identify
   the resulting quadratic Hodge inequality with the truncated Weil form.

### Principal danger

Inventing the intersection product may simply insert the desired positivity.
The admissibility test is functoriality: product, degree, and Frobenius
composition must be defined before the Weil inequality is examined.  The
archimedean place may also fail to arise from a Lorentzian-preserving limit.

### Assessment

This is the conceptually strongest route.  Estimated chance of a meaningful
new finite-prime Hodge theorem: `10--20%`; chance that the complete limiting
package reaches RH: `1--3%`.

## Path II: prime Euler factors as a passive scattering network

### Connection

Connes interprets critical zeros as an absorption spectrum and noncritical
zeros as resonances.  Suzuki's screw function packages RH as positivity of a
translation kernel.  In systems and scattering theory, the analogous
distinction is exact: a passive system has a contractive analytic transfer
function; generalized passive systems live in Pontryagin spaces, where the
number of negative squares of the de Branges--Rovnyak kernel counts unstable
poles.

This suggests replacing the unsuccessful search for a positive zeta
Hamiltonian by an **index computation**.  Construct a completed zeta transfer
function `S(z)` whose kernel

`K_S(z,w) = (1 - S(z) conjugate(S(w))) / (-i(z-conjugate(w)))`

is the transform of the Suzuki/Weil kernel.  In generalized Nevanlinna theory,
the negative index of such a kernel should count off-critical zero pairs.  RH
becomes the statement that the index is zero.

The new proposal is to realize each Euler factor, the gamma factor, and the
Poisson summation correction as elementary colligations, and combine them by
feedback/cascade rules which preserve passivity or add known indices.  The
global conclusion would follow from exact index bookkeeping rather than a
support-uniform spectral gap.

### Why this adds rank

Passivity is a causal composition law.  It is stronger than positivity of one
fixed quadratic form and is preserved by interconnection.  The arithmetic
content would enter locally through Euler factors, while analytic
continuation would enter through a lossless feedback identity.  This is
different from simply declaring a self-adjoint operator with the zeros as its
spectrum.

### First three targets

1. Freeze a precise completed transfer function and prove that its kernel is
   congruent to the already normalized Suzuki screw kernel.
2. Produce explicit finite-prime state-space realizations and compute their
   negative-square index exactly.
3. Determine whether Poisson summation is a lossless interconnection which
   continues the Euler cascade from `Re(s)>1` into the critical strip without
   creating negative index.

### Principal danger

Euler factors are naturally passive only in the half-plane of absolute
convergence.  If the global feedback law needed for continuation is equivalent
to RH, the construction is circular.  The first kill test is therefore to
compute Pick matrices for finite-prime/gamma models and see whether their index
is controlled independently of a zero-free assumption.

### Assessment

This is the best analytic continuation of our current operator work, but it
changes the invariant from a collapsing eigenvalue to an integer index.
Estimated chance of a non-circular index theorem: `8--15%`; chance it closes
RH: `0.5--2%`.

## Path III: an entropy/inverse theorem for an off-line-zero resonance

### Connection

An off-line zero with real part `beta > 1/2` produces a coherent term of scale
`x^beta` in explicit-formula or Perron transforms.  Existing multiplicative
function theory proves cancellation for Möbius/Liouville in almost all short
intervals and increasingly strong Fourier/Gowers uniformity on average.  But
those theorems do not exclude a sparse coherent resonance, which is why merely
citing Chowla or GUE is insufficient.

The proposed target is a converse or inverse theorem:

> If one zero has real part `beta > 1/2`, then on a positive-entropy tree of
> logarithmic scales there are Dirichlet-polynomial blocks whose normalized
> phases correlate coherently with the same character `n^(it)` and whose
> amplitudes obey a multiplicative consistency law.

One would then combine entropy decrement, short-interval Fourier uniformity,
and pretentious distance across scales to show that such persistent coherence
forces Möbius to pretend to one fixed Archimedean character.  Euler-factor
signs make that impossible with bounded pretentious distance.

The potentially overlooked point is **scale history**.  Current average
results examine most intervals at one scale or finitely many correlations.
An individual zero is global and should force the same phase through a nested
family of scales.  A tree/entropy inverse theorem can be pointwise in the
exceptional zero while still using average estimates at each level.

### Why this adds rank

This route uses multiplicativity and information flow between scales, neither
of which is present in the localized Weil operator.  It would rule out a zero
by showing that its required arithmetic witness cannot exist, rather than by
proving a universal quadratic form positive.

### First three targets

1. Derive, unconditionally and with explicit smoothing, the nested-scale
   resonance forced by one zero `rho`; quantify the density of good branches.
2. Prove a multiscale inverse theorem converting that resonance into bounded
   pretentious distance to `n^(i Im(rho))`.
3. Use prime-by-prime divergence to contradict the required pretence.

### Principal danger

A single zero may force only very sparse exceptional scales, too sparse for
entropy decrement.  Existing almost-all theorems are fully compatible with
such exceptions.  Step 1 is therefore the decisive checkpoint; it must produce
positive entropy without smuggling in a density hypothesis equivalent to RH.

### Assessment

This route is mathematically orthogonal and exploits recent tools, but the
exceptional-set gap is severe.  Estimated chance of a useful nested-scale
resonance theorem: `5--12%`; chance of reaching RH: `0.2--1%`.

## Path IV: a stable-polynomial lift of the xi Jensen array

### Connection

RH is equivalent to hyperbolicity of every xi Jensen polynomial.  Eventual
hyperbolicity for each fixed degree is known, so the problem is the
two-parameter transition where degree and shift grow together.  Modern
Lee--Yang/Polya--Schur theory classifies stability-preserving operations, while
strongly Rayleigh measures, mixed characteristic polynomials, and Lorentzian
polynomials provide multivariate certificates whose diagonal specializations
are real-rooted.

Seek a multiaffine stable polynomial `P_N(z_1,...,z_N)` built from the positive
theta-kernel moment representation of xi such that a diagonal specialization
or polarization equals the Jensen polynomial.  Stability would then survive
specialization and limits, proving all required hyperbolicity at once.  The
probabilistic version asks whether the normalized xi moment array is the
partition function of a strongly Rayleigh measure.

### Why this adds rank

Univariate coefficient inequalities are usually too weak and become RH
equivalents.  A multivariate stable lift adds negative-dependence identities
between many coefficients.  If those identities follow from a determinantal
or exclusion-process model of the theta kernel, real-rootedness is structural.

### First checkpoint

Before proving anything abstract, solve the finite inverse problem for small
`N`: test the Rayleigh inequalities and search for a determinantal/mixed-
characteristic representation matching the exact xi moments.  A systematic
failure of the necessary inequalities kills this path quickly.

### Assessment

This is the cheapest high-value experiment and could yield new results on xi
coefficients even if it fails to prove RH.  Estimated chance of a nontrivial
stable lift for a growing family: `10--25%`; chance the lift covers the full
two-parameter array and proves RH: `0.5--2%`.

## Recommended allocation

1. Start with Path IV's finite inverse problem because it is inexpensive and
   sharply falsifiable.
2. In parallel conceptually, formulate Path I's finite-prime correspondence
   polynomial.  This is the highest-upside structural program.
3. Reuse the existing Suzuki normalization to run Path II's negative-square
   index test; stop immediately if analytic continuation already presupposes
   the desired index.
4. Attempt Path III only after proving the off-line-zero nested-scale lemma;
   do not spend time importing generic Chowla machinery before that checkpoint.

These paths are orthogonal in their decisive invariants: Hodge signature,
Pontryagin negative index, entropy/pretentious distance, and multivariate
stability.  Success or failure in one should therefore update the others only
weakly.

## Primary literature anchors

- A. Connes, *Trace formula in noncommutative geometry and the zeros of the
  Riemann zeta function*: https://arxiv.org/abs/math/9811068
- A. Connes and C. Consani, *Geometry of the arithmetic site*:
  https://arxiv.org/abs/1502.05580
- A. Connes and C. Consani, *Geometry of the scaling site*:
  https://arxiv.org/abs/1603.03191
- A. Connes and C. Consani, *The Riemann--Roch strategy, complex lift of the
  scaling site*: https://arxiv.org/abs/1805.10501
- A. Connes and C. Consani, *Weil positivity and trace formula, the
  archimedean place*: https://arxiv.org/abs/2006.13771
- P. Branden and J. Huh, *Lorentzian polynomials*:
  https://arxiv.org/abs/1902.03719
- M. Suzuki, *Aspects of the screw function corresponding to the Riemann zeta
  function*: https://arxiv.org/abs/2206.03682
- K. Matomaki and M. Radziwill, *Multiplicative functions in short intervals*:
  https://arxiv.org/abs/1501.04585
- K. Matomaki, M. Radziwill, T. Tao, J. Teravainen, and T. Ziegler, *Higher
  uniformity of bounded multiplicative functions in short intervals on
  average*: https://annals.math.princeton.edu/2023/197-2/p03
- M. Griffin, K. Ono, L. Rolen, and D. Zagier, *Jensen polynomials for the
  Riemann zeta function and other sequences*:
  https://arxiv.org/abs/1902.07321
- M. Griffin et al., *Jensen polynomials for the Riemann Xi function*:
  https://arxiv.org/abs/1910.01227
- J. Borcea and P. Branden, *The Lee--Yang and Polya--Schur programs I*:
  https://arxiv.org/abs/0809.0401
- B. Rodgers and T. Tao, *The de Bruijn--Newman constant is non-negative*:
  https://arxiv.org/abs/1801.05914
