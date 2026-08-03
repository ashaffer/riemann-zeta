# Post-trilemma RH paths

Status: newly synthesized portfolio after the coherence-without-mass audit;
2026-08-01.  These are research programs, not RH claims.

Every path below is completion-native, phase-sensitive, and equipped with a
kill test.  None is admitted merely because its final condition is equivalent
to RH.

## Path A: parabolic Maslov degree for theta-zero collisions

Let

`H_t(x)=integral_0^infinity exp(tu^2)Phi(u)cos(xu)du`,

so `partial_t H=-partial_x^2 H`.  Define the two-component field

`F(t,x)=(H_t(x), partial_x H_t(x))`.

Its zeros are exactly real double zeros of the heat-deformed xi function—the
collision events governing the de Bruijn--Newman constant.

### Exact orientation theorem

At a generic collision, `H=H_x=0` and `H_xx!=0`.  The Jacobian is

`det D_(t,x)F = H_t H_xx - H_x H_xt = -H_xx^2 < 0`.

Thus every collision has the same local Brouwer degree.  Unlike ordinary
spectral flow on a zeta quartet, this signed index cannot cancel: its absolute
value counts collisions.

### Proposed amplifier

On a rectangle `[0,T] x [-X,X]`, the boundary winding of `F/|F|` equals the
negative number of enclosed collisions.  For large `T`, real-rootedness is
known.  The target is to use the exact modular theta relation to evaluate or
homotope the other three boundary pieces and show that the degree is zero as
`X,T->infinity`.

### Why this passes the new admission rule

- Carrier: a double zero of the completed theta heat flow.
- Topology: integer Brouwer degree, insensitive to collision amplitude.
- Completion: the full modular kernel enters before the degree is defined.
- Amplifier: all local crossing forms have one sign.
- Closed limit: still open and explicitly load-bearing.
- Countermodel: generic even heat kernels with positive Newman constant have
  nonzero degree, so heat evolution alone does not imply the conclusion.

### Kill test

Derive the finite-rectangle boundary formula.  If modularity controls only the
vertical tails while the `t=0` winding is exactly the unknown number of real
xi zeros, the construction is merely the argument principle in parabolic
coordinates and should be downgraded.  It survives only if modularity removes
or independently fixes that bottom-edge winding.

Prior for a genuinely new boundary identity: `8--15%`; end-to-end RH prior:
`1--3%`.

**Gate result:** the horizontal boundary winding is exactly
`-(H_x^2-H H_xx)/(H^2+H_x^2)`, and the vertical winding is the spatial
derivative of the Laguerre density divided by the same denominator.  The
global degree therefore repackages the prior Laguerre target and lacks a
nonvanishing compactification at `|x|=infinity`.  See
`PARABOLIC-MASLOV-DEGREE-AUDIT.md`.  Prune Path A as an independent amplifier.

## Path B: shifted-xi Schur index and a Loewner chain

For `a>0`, define on the upper half-plane

`Theta_a(z)=xi(1/2+a+iz)/xi(1/2-a+iz)`.

For real `x`, the functional equation and conjugation give

`|Theta_a(x)|=1`.

A denominator zero in the upper half-plane corresponds to a zeta zero with
`Re(rho)<1/2-a`, hence by symmetry to one with `Re(rho)>1/2+a`.  Generalized
Schur theory therefore supplies an unsigned carrier: the negative-square or
pole index of

`K_a(z,w)=(1-Theta_a(z)conj(Theta_a(w)))/(-i(z-conj(w)))`.

In bounded windows this index counts off-line zeros beyond displacement `a`
without quartet cancellation.

### Exact parameter cocycle

The shifted ratios obey

`Theta_(a+b)(z)=Theta_a(z-ib) Theta_b(z+ia)`.

This is a nonautonomous multiplicative evolution in `a`.  Its infinitesimal
logarithmic generator is built from the symmetric sum of two values of
`xi'/xi`.  The proposed order law is that this evolution is a Schur/Loewner
chain as `a` decreases from the unconditional zero-free range to zero.

### Proposed amplifier

If `K_a` is positive for every `a>0`, then `Theta_a` has no upper-half-plane
poles, so zeta has no zero with displacement greater than `a`.  Sending
`a->0` proves RH.  Positivity would follow from a Herglotz generator or a
positive conservative realization of the cocycle.

### Kill test

Compute the generator and determine whether its Herglotz property is simply a
Hadamard expansion with every off-line term already assumed nonnegative.  If
so, the Loewner language adds no mechanism.  A surviving proof must derive
the generator sign from modular or adelic structure before using zero
locations.

The script `src/shifted_xi_pick_scan.py` tests finite Pick matrices.  Initial
matrices for `a=0.05,...,0.6` and sample points through height 30 are positive,
as expected from verified low zeros; this is a falsifier, not RH evidence.

Prior for an independent Loewner law: `5--10%`; end-to-end: `0.5--2%`.

**Gate result:** the infinitesimal generator at `a=0` is
`2 xi'/xi(1/2+iz)`, and its Herglotz sign is already equivalent to excluding
off-line zeros.  The shifted cocycle samples outside the upper half-plane and
does not propagate Schur positivity from large to small `a`.  See
`SHIFTED-XI-SCHUR-LOEWNER-AUDIT.md`.  Retain `Theta_a` as an unsigned carrier,
but prune the standalone Loewner amplifier.

## Path C: an adelic Hilbert colligation for the shifted ratio

Path B identifies a precise transfer function.  Path C asks for a geometric
reason for its Schur index to vanish.

The Mellin transform turns dilation on the adele-class space into spectral
multiplication, while Poisson summation supplies a unitary additive Fourier
involution.  Construct a mapping-cone or scattering colligation whose transfer
function is exactly `Theta_a`, including gamma and pole factors.

Generalized Schur realization theory says that a Pontryagin state space
produces a transfer function whose negative index counts its negative squares.
The desired new theorem is stronger and geometric:

> the natural adelic state space for `Theta_a` is Hilbert, not merely
> Pontryagin, and its trace pairing is positive for every `a>0`.

Then `Theta_a` is Schur and Path B completes RH.

### Why this is not the discarded cyclotomic path

No nonexistent `THR(Z)` gamma ladder is asserted.  The completed ratio already
contains the independently known archimedean factor, and the first task is a
single explicit transfer-function calculation, not construction of a general
cohomology theory.

### Kill test

Build the finite-prime (`S`-adelic) colligation and calculate its metric
signature.  If the relative trace subtraction necessarily creates a negative
state direction, or if the transfer function equals `Theta_a` only after
inserting xi by hand, prune the path.  Do not attempt an infinite adelic limit
until this finite-`S` signature test passes.

Prior for an exact positive finite-`S` realization: `3--8%`; end-to-end:
`0.3--1.5%`.

**Gate result:** every shifted local Euler factor has real boundary arcs with
gain greater than one, and finite prime phases can align.  A factorwise
passive Hilbert colligation is impossible; completion is irreducibly global.
See `SHIFTED-XI-ADELIC-REALIZATION-AUDIT.md`.  Retain only a one-step global
Poisson realization, for which no construction is currently known.

**Literature identification and final verdict:** the one-step global object is
the shifted-xi de Branges/canonical system studied by Masatoshi Suzuki.  It is
constructed unconditionally in a safe shift range; positivity/innerness for
all positive shifts is explicitly an RH criterion.  Any exact Hilbert
realization factors the same de Branges kernel, so its positive metric is the
whole missing theorem, not an independent bridge.  See
`GLOBAL-POISSON-REALIZATION-VERDICT.md`.  Close Path C as a separate source of
leverage.

## Path D: modular-orbit Gram factorization

The theta audit gave

`H_t'^2-H_t H_t'' = Fourier[b_t]`,

with an explicit positive convolution density `b_t`.  Individual theta
summands fail, and finite truncations necessarily acquire a negative algebraic
tail because they do not cancel all odd boundary jets.

The only admissible factorization is therefore by complete modular orbits,
not by individual `n`-terms.  Expand `b_t` as a two-dimensional theta-lattice
sum, apply two-dimensional Poisson summation before truncation, and seek a
Gram representation of its Fourier transform indexed by dual modular orbits.

### Kill test

Derive the first complete orbit block and test whether its Gram matrix is
positive.  If an orbit block is indefinite, or if the proposed square roots
use the zeros of xi, prune.  The known negative `n=1` diagonal guarantees that
any valid block must contain genuine infinite cross-summand cancellation.

Prior for a nontrivial modular Gram identity: `5--12%`; end-to-end: `1--3%`.

**Gate result:** the first swap-complete cross orbits are sign-indefinite:
`B_(1,2)` and `B_(1,3)` both change sign.  The rectangular-lattice expansion
also has differential coefficients of signs `+,-,-,+`.  Only a fully global
two-dimensional Poisson sum-of-squares identity could survive, and without an
independent square root that is simply the full Laguerre target.  See
`MODULAR-ORBIT-GRAM-AUDIT.md`.  Downgrade Path D.

## Allocation and order

1. **Path A first:** the collision orientation is already an exact new fact;
   the boundary-degree calculation can fail quickly.
2. **Path B second:** the carrier and cocycle are explicit, and finite Pick
   tests are cheap.
3. **Path D third:** higher algebraic cost, but it directly attacks the full
   modular cross terms identified by the prior audit.
4. **Path C long horizon:** proceed only if the finite-`S` signature and exact
   transfer-function gates pass.

Paths A and B are the current Bayesian leaders because their invariants are
quantized or order-valued, completion-native, and sensitive to one exceptional
zero without measuring its vanishing amplitude.
