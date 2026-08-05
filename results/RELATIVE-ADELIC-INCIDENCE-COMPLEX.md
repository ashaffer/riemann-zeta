# Relative adelic incidence complex

Status: a formal one-step incidence ansatz and an exact rank-two pole
reduction are identified; a closed continuum Hilbert-complex realization and
the exactly normalized incidence/Weil-form identity remain open, 2026-08-05.

## 1. Completed incidence differential

Gauss's digamma formula writes the nonconstant archimedean multiplier as

`integral_(t>0) w_infinity(t) (1-cos(xi t/2)) dt`,

with

`w_infinity(t)=exp(-t/4)/(1-exp(-t)) > 0`.

Formally, Plancherel identifies this, after fixing every normalization, with
the norm square of the continuum incidence expression

`d_infinity f(t,x)=sqrt(w_infinity(t)) (f(x)-f(x-t/2))`.

For a prime power `n`, completing the negative autocorrelation gives the
discrete edge

`d_n f(x)=sqrt(Lambda(n)/sqrt(n)) (f(x)-f(x-log n))`.

On a smooth compactly supported core, put all continuum and active discrete
edges in a direct-integral/direct-sum edge space and write

`d_a f = d_infinity f direct-sum (d_n f)_active`.

Taking the next differential to be zero makes an algebraic one-step complex on
that core, so the square-zero identity is automatic.  It does not yet make a
closed Hilbert complex.  Because `w_infinity(t)` is singular like `1/t` at
zero, a complete construction must prove that the continuum map is densely
defined and closed or closable, identify its domain with the intended
logarithmic form domain, and establish the exact incidence/Weil-form identity
with every factor of two.  These are open obligations.

At the coefficient level, Gauss supplies the continuum measure and the
previously proved Möbius identity `mu*log=Lambda` supplies the connected
discrete weights.  This verifies the formal ansatz, not its operator closure.

Thus the coefficient and square-zero gates pass on the smooth core.  The
operator-domain and exact-normalization gates remain.

## 2. Rank-two pole sector

After completing every translation to a difference square, the terms not in
`||d_a f||^2` are zero-mode/boundary terms:

1. a scalar degree deficit times `||f||^2`;
2. the pole pairing
   `2 <f,e^(x/2)> <f,e^(-x/2)>`.

Writing the two pole moments as `p,m`,

`2 p m = ((p+m)^2-(p-m)^2)/2`.

The pole sector therefore has exact signature `(1,1)`.  Lean now proves this
identity and proves that the two classical Weil moment conditions

`<f,e^(x/2)>=<f,e^(-x/2)>=0`

annihilate the entire pole form.  On this relative codimension-two subspace,

`Q_a(f)=archimedeanTerm_a(f)-primeTerm_a(f)`.

This motivates an analogy with passing from absolute to relative adelic
cohomology.  What is proved here is the rank-two form calculation and its
annihilation by the moment conditions, not a cohomology computation for a
closed adelic complex.

## 3. Remaining inequality

Conditional on the closed realization and exact normalized form identity, on
the relative subspace positivity becomes a Poincaré inequality for the
completed incidence differential:

`||d_a f||^2 >= degreeDeficit(a) ||f||^2`

subject to the two moment constraints.

This is still an RH-strength global target when required for every support,
but it is structurally cleaner than the original form:

- every nonzero-delay term is a manifestly positive edge square;
- all prime--prime composites have already cancelled through Möbius incidence;
- the indefinite pole block is absent;
- the only issue is the spectral gap of one relative differential.

## 4. Numerical checkpoint

`src/relative_incidence_gap.py` independently assembles the pole-free
archimedean-minus-prime matrix and projects onto the common kernel of the two
moment vectors.  Representative 20-mode Ritz minima are

| support | relative minimum |
|---:|---:|
| 1.750 | `9.27e-2` |
| 2.485 | `1.84e-5` |
| 2.996 | `5.22e-8` |
| 3.555 | `1.64e-9` |
| 4.040 | `1.85e-11` |

These are non-certified upper bounds and decrease under refinement.  They do
show that removing the boundary classes greatly enlarges the early-window
margin: at support `2.485` the unrestricted margin is around `3.5e-10`, five
orders of magnitude smaller than the 20-mode relative value.

The margin still collapses rapidly with support, so the moment reduction does
not by itself prove a support-uniform gap.

## 5. New analytic target

The correct next target is the **relative incidence Poincaré theorem**:

> For every finite support `a`, every logarithmic-form-domain function
> orthogonal to `e^(x/2)` and `e^(-x/2)` has completed continuum-plus-prime
> incidence energy at least the exact degree deficit.

A useful proof cannot estimate the continuum and prime edges independently;
the margins show that the inequality becomes asymptotically sharp.  It must
use a global sampling/frame identity or a support-dependent extremal theorem.

The most promising immediate calculation is to find the Euler--Lagrange
equation of the constrained relative minimizer.  The two Lagrange multipliers
are now exactly the removed pole coordinates.  If Poisson summation forces a
nonzero boundary Wronskian or a strict interlacing law for that constrained
equation, it supplies the missing Poincaré strictness without separately
bounding large cancelling pieces.

## 6. Fail-fast verdict on a higher differential

A tempting repair was to keep the completed incidence map `d_0`, add a
nonzero map `d_1` out of its edge space with `d_1 d_0 = 0`, and hope that the
resulting two-step Hodge complex cancels the scalar degree deficit.  This does
not work in degree zero.  For every such extension,

`<Delta_0 x,x> = ||d_0 x||^2`,

so the degree-zero energy is independent of `d_1`.  Consequently

`||d_0 x||^2 - degreeDeficit(a) ||x||^2 >= 0`

is still equivalent to exactly the same relative Poincare inequality as
before.  `RHBridge.CompletedIncidenceComplexNoGo` proves this abstractly for
bounded continuous maps between real Hilbert spaces.  Applying the same
observation to the proposed continuum map requires the unbounded-domain work
stated in Section 1.

This prunes the naive "pair the odd edge sector with one more differential"
route.  A viable cohomological reformulation must instead change the primary
completed differential, place the Weil object in a different degree, or
derive the sharp gap from additional arithmetic structure.  Merely changing
higher cohomology cannot affect the missing degree-zero estimate.
