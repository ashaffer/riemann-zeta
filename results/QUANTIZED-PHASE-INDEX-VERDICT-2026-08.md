# Quantized completed phase/index: finite-prime verdict

Status: the two finite-prime Euler-phase architectures defined below do not
supply a continuous-symbol winding in the all-prime limit, 2026-08-04.  The
zero-side polynomial winding increment is valid.  No RH claim and no universal
Fredholm or arithmetic-index no-go is made.

## 1. Verdict

Prompt E asked for an integer-valued invariant of the completed prime--gamma
object that

1. changes when one off-critical functional-equation quartet is inserted;
2. is computable from arithmetic data without factoring `xi` or counting its
   zeros; and
3. survives the all-prime limit in a topology that preserves its index.

The first item is easy and exact.  A vertically shifted completed phase has a
winding jump of four on the whole centered real axis when a simple quartet
enters its strip.  The second and third items fail for the two canonical Euler
realizations:

- the literal two-sided shifted Euler quotient is null-homotopic at every
  finite set of primes and is not even bounded in Besicovitch `B^2` as the
  prime cutoff grows;
- the functional-equation-normalized right-shift phase is also null-homotopic
  at every finite cutoff.  It does converge in `B^2`, but not uniformly in the
  RH-relevant range.  `B^2` convergence alone supplies no canonical
  invertible continuous symbol or inherited winding class.

Thus the natural quantized phase route hits a precise topology trilemma:

```text
weak mean-square closure     exists, but supplies no continuous symbol;
uniform-symbol closure       preserves winding, but fails below Re(s)=1;
divisor/contour closure      detects the quartet, but is zero counting.
```

The strongest honest arithmetic integer already available is the negative
Morse index of a localized completed Weil operator.  It is finite and
unconditional for each window, but it is exactly Weil-form inertia.  No known
theorem computes its jumps as an unsigned quartet count without proving the
missing completed positivity statement.

## 2. The quartet is invisible to real critical-line phase

Put

```text
X(z) = xi(1/2 + i z)
```

and insert a simple off-line quartet through

```text
Q_(gamma,delta)(z)
  = ((z-gamma)^2 + delta^2) ((z+gamma)^2 + delta^2),
gamma,delta > 0.
```

Its roots are `+-gamma +- i delta`.  The polynomial is real and even, and for
real `x`,

```text
Q_(gamma,delta)(x) > 0.
```

Consequently multiplication by `Q` preserves functional-equation symmetry
and changes neither the sign nor the phase of `X(x)` on the centered real
line.  It therefore defeats every detector using only that boundary phase.

There is also an exact compact-open version.  With

```text
A = gamma^2 + delta^2,
```

one has

```text
Q(z)/A^2
  = 1 + 2(delta^2-gamma^2)z^2/A^2 + z^4/A^2,
```

and hence on `|z| <= R`,

```text
|Q(z)/A^2 - 1| <= 2R^2/A + R^4/A^2.
```

For fixed `delta`, this tends to zero as `gamma` tends to infinity.  Therefore
no integer invariant continuous in ordinary compact-open topology can detect
every remote quartet.  This statement has an important scope restriction:
`Q/A^2` does not preserve the Euler product or the global asymptotic growth of
`xi`.  It is a no-go for compact-local and boundary-phase data, not for a
genuinely global weighted topology.

Lean proves the exact expansion, evenness, strict positivity, and sign
preservation in `RHBridge.QuantizedPhaseIndexNoGo`.

## 3. A shifted phase does detect the quartet

Let `P` be a real polynomial with no root on `Im(z)=+-a`, and orient the real
axis from `-infinity` to `+infinity`.  Then

```text
S_(P,a)(x) = P(x-ia)/P(x+ia)
```

has unit modulus, tends to one at both ends, and the argument principle gives

```text
wind S_(P,a)
  = #{lambda : P(lambda)=0 and |Im(lambda)|<a},
```

with multiplicity.  Therefore the whole-line contribution of `Q` is

```text
0,  if 0 < a < delta;
4,  if a > delta.
```

The reciprocal convention changes `+4` to `-4`.  A positive-height closure
sees two and a quarter-plane count sees one, so the domain must always be
stated when quoting a quartet index.

At `a=delta`, numerator and denominator share boundary factors.  Canceling
them on that single slice gives the midpoint winding two, but there is no
jointly continuous extension in `(a,x)`.  Locally near `(x,a)=(gamma,delta)`,
the singular pair is, up to a nonzero unit,

```text
(y-i epsilon)/(y+i epsilon) = conjugate(w)/w,
y=x-gamma, epsilon=a-delta.
```

It has charge `-2` in counterclockwise `(y,epsilon)` coordinates while the
horizontal winding jumps by `+2` as `a` increases.  This explains both the
integer jump and why a global square-root or Pfaffian half-phase cannot simply
be chosen through the defect.

For completed `xi`, the formal analogue is

```text
xi(1/2+a+ix) / xi(1/2-a+ix).
```

The functional equation makes it a unit phase where defined.  Its raw
whole-line winding needs the gamma and large-height regularization.  The
polynomial result above proves the *increment contributed by one inserted
quartet*; it does not by itself define the global `xi` winding.

There is a second limitation.  The shifted winding counts every zero in a
strip, including all critical-line zeros.  Turning it into an off-line defect
requires comparison with the total zero count or following its jumps in `a`.
That comparison is the argument principle/Turing zero count in new notation.

## 4. Symmetry census

The functional-equation quartet is a regular orbit of its two reflections.
For the untwisted finite models considered here, the ordinary signed sums
cancel over that orbit.  In particular:

- if a closed Fredholm operator `T` has an antiunitary `J` with
  `J T J^(-1)=T*`, then `J` identifies `ker(T)` with `ker(T*)`, so its
  ordinary Fredholm index is zero;
- the ordinary signature and full-quartet parity of the displayed minimal
  blocks do not see one quartet;
- the minimal indefinite block has inertia `(1,1)` per off-line conjugate
  pair and `(2,2)` for the full quartet, so its signature is zero while its
  negative inertia is two;
- the whole-line shifted winding survives as the unsigned value four.

This reproduces, rather than replaces, two earlier survivors.  For one
*distinct simple* quartet the scalar generalized-Nevanlinna kernel has two
negative squares.  Repeated roots require care: the scalar logarithmic
derivative can multiply a rank-one feature without increasing its rank, so an
algebraic multiplicity factor must not be asserted automatically.  The other
survivor is ordinary holomorphic degree, which is precisely zero counting.

These examples do not classify all twisted, equivariant, eta, or Krein
refinements.  A genuinely new index would need extra arithmetic grading data
that canonically distinguishes the members of a quartet without reading their
zero locations.

## 5. Literal shifted Euler quotient: topology and `B^2` both fail

Fix `0<a<1/2`, and for one prime put

```text
r_- = p^(-1/2+a),   r_+ = p^(-1/2-a),
V_(p,a)(z) = (1-r_- z)/(1-r_+ z),   |z|=1.
```

Both radii are below one.  Scaling them by `t in [0,1]` contracts `V` through
nonvanishing loops to the constant one.  Hence every finite-prime torus
product has zero `H^1/K_1` class.  This is a torus statement; the quasiperiodic
real translation orbit is not itself a closed loop.

The all-prime limit fails more strongly.  Haar orthogonality gives exactly

```text
||V_(p,a)||_2^2
  = 1 + (r_- - r_+)^2/(1-r_+^2).
```

Prime-coordinate independence multiplies these local norms.  Since

```text
(r_- - r_+)^2
  = p^(-1+2a) (1-p^(-2a))^2
```

and the sum over primes diverges, the finite products are not even bounded in
Bohr/Besicovitch `B^2`.  The reciprocal convention changes the harmless
denominator to `1-r_-^2` and has the same divergence.  The separated gamma
factor is not a Bohr-almost-periodic factor that can cancel this norm growth.

This also explains why factorwise Euler manipulation below `Re(s)=1` is
illegitimate: analytic continuation of the completed quotient is not the
`B^2` limit of this literal two-sided Euler product.

## 6. Right-shift unit phase: `B^2` exists, but its index does not

Use the functional equation first and set `sigma=1/2+a`, `r_p=p^(-sigma)`.
The natural unit local phase is

```text
U_(p,a)(z) = (1-r_p z^(-1))/(1-r_p z),   |z|=1.
```

It is explicitly contracted to one by `r_p -> t r_p`.  Lean proves that this
radial homotopy is continuous, nonvanishing, and unit norm for every
`t in [0,1]`.  Thus all finite products again have trivial `K_1` class.

Nevertheless their mean-square limit is well behaved.  If `U_P` is the
product through prime `P`, then

```text
||U_Q-U_P||_2^2
  = 2 - 2 product_(P<p<=Q) (1-p^(-1-2a)).
```

It is `B^2`-Cauchy for every `a>0`.  Equivalently, a canonical logarithm has
squared Fourier norm

```text
2 sum_(p,m>=1) p^(-(1+2a)m)/m^2 < infinity.
```

But for `0<a<=1/2` the convergence is not uniform.  Unique factorization
makes the finite set of `log p` rationally independent, so Kronecker density
allows all prime coordinates in a finite tail to approach `i`.  The aligned
phase excursion contains

```text
2 sum_p arctan(p^(-1/2-a)),
```

which diverges when `1/2+a<=1`.  The finite products are therefore not
uniformly Cauchy: on each sufficiently large finite tail, continuity in the
independent torus coordinates lets the accumulated angle hit `pi`, and
Kronecker density then makes the real translation orbit approach that value.
Uniform Euler convergence resumes only for `a>1/2`, the
ordinary half-plane `Re(s)>1`, where the index is trivially zero and contains
no RH information.

In this Fourier model the `B^2` limit is a Besicovitch/Haar-`L^2` class, not a
continuous nonvanishing symbol.  It cannot inherit winding or `K_1` merely
from its finite approximants, and it must not be identified with the
analytically continued completed zeta phase without an additional theorem.
That additional continuation theorem would have to specify an operator
topology and retain
exactly the zero vortices erased by `B^2`.

## 7. The topology trilemma as a theorem-selection rule

The audit leaves three possible topologies, none currently closing the route.

1. **Compact-open or fixed-resolution topology.** A remote normalized quartet
   tends to one, so continuity makes an integer detector blind to it.
2. **Bohr/Besicovitch mean topology.** The normalized finite-prime phase has a
   limit, but that convergence alone supplies no invertible continuous symbol
   or canonical ordinary winding class.
3. **Uniform symbol topology.** Ordinary winding would be stable, but the
   finite-prime products fail to converge in the relevant strip.  Restoring a
   zero-bearing limit requires a counterterm or continuation carrying the
   divisor.  Hurwitz already forbids locally uniform convergence of zero-free
   holomorphic products to a function with a zero on the same domain.

A translation-invariant trace per unit height does not evade the trilemma: it
measures density, so a finite family of uniformly localized defects
contributes zero.  No assertion is made here for arbitrary zero-density
families with broad or nonsummable profiles.  A half-phase does not evade the
trilemma either: the local charge is even only after pairing, while a global
square root requires the very divisor/branch information being sought.

## 8. Relation to existing operator programs

The conclusion is compatible with, and narrower than, the literature.

Almost-periodic Wiener--Hopf and mean-winding theories can define indices
after additional algebraic or operator structure is specified; see
[Coburn--Douglas--Schaeffer--Singer](https://www.numdam.org/item/PMIHES_1971__40__69_0/),
[Murphy](https://doi.org/10.1016/j.jfa.2005.08.012), and
[Yakubovich](https://arxiv.org/abs/math/0606153).  Accordingly, the result here
is not that mean topology can never support an index.  It is that `B^2`
convergence of the displayed Euler phases alone supplies neither the required
invertible continuous symbol nor a specified Fredholm representative.

- Burnol's conductor and commutator supply genuine local phase operators and
  treat finite and archimedean places uniformly.  On the unramified radial
  block the commutator has continuous spectrum through zero, so the naive
  inversion-graded block is not Fredholm.  Burnol also constructs a global
  Lax--Phillips scattering system; its bad-zero Blaschke factor is explicitly
  built from the off-line divisor, so its degree is a zero count rather than
  a zero-independent arithmetic index.  See
  [the conductor operator](https://arxiv.org/abs/math/9902080) and
  [global scattering](https://arxiv.org/abs/math/0001013).
- Connes's adele-class trace program interprets critical zeros as absorption
  spectrum and possible off-line zeros as resonances, with the global trace
  formula as the missing bridge.  It does not furnish the unsigned
  finite-prime index sought here.  See
  [Connes's trace formula](https://arxiv.org/abs/math/9811068).
- Meyer's virtual idele-class representation carries zeros and poles with
  multiplicity, but extracting an unsigned quartet count from its spectrum
  uses a spectral contour.  Its standard odd Fredholm module measures the
  modular direction rather than off-line-zero number.  See
  [Meyer's virtual representation](https://arxiv.org/abs/math/0311468).
- Under their stated simple/even ground-state hypotheses,
  Connes--Consani--Moscovici construct finite arithmetic self-adjoint
  operators and real-zero determinants.  Their convergence to completed
  `Xi` remains the decisive open theorem and would establish RH; finite
  self-adjoint approximants cannot themselves display an off-line quartet.
  See [Zeta Spectral Triples](https://arxiv.org/abs/2511.22755).
- Suzuki's 2026 screw-function framework constructs the localized completed
  Weil operator and proves ground-state continuity unconditionally; an
  off-line failure would force a finite-window crossing.  The global
  self-adjoint limit remains conjectural.  Its finite negative Morse index is
  a legitimate quantized arithmetic object, but presently it is completed
  Weil inertia, not an independently computed quartet index.  See
  [Weil's quadratic form via the screw function](https://arxiv.org/abs/2606.09096).

The generalized-Nevanlinna comparison uses the standard negative-square
factorization framework; see
[Dijksma--Langer--Luger--Shondin](https://doi.org/10.1007/BF01236290).

## 9. Exact scope of the no-go

The following exactly defined class is eliminated:

> Build a completed phase as the direct limit of the natural finite-prime
> shifted Euler loops defined in Sections 5--6, require a uniform invertible
> continuous-symbol limit, and infer an off-line quartet count from its
> ordinary winding.

It is closed because every finite class is zero and the only available
nontrivial limit topology either does not exist or does not carry an index.

The following much narrower possibility is not disproved:

> Construct a new completion-native equivariant or semifinite relative index
> whose topology assigns nonzero size to one remote quartet, whose arithmetic
> representative is defined without zeros or Weil-form eigenvectors, and
> whose all-place summability is proved independently of completed Weil
> positivity.

That is not currently a construction; it is an admission criterion.  Burnol
local commutators, ordinary spectral flow, generalized-Nevanlinna inertia,
localized Weil Morse index, and shifted winding each fail one of its clauses.
Absent a concrete new representative, Prompt E should be parked rather than
iterated through more phase conventions.

## 10. Reproducible artifacts

- `src/quantized_phase_index_gate.py` checks the exact quartet algebra,
  `0/4` winding increment, finite-prime degree, radial unit phase, and the two
  coefficient topologies.
- `src/test_quantized_phase_index_gate.py` contains seven lightweight
  regression tests.
- `RHBridge.QuantizedPhaseIndexNoGo` kernel-checks the quartet sign
  invisibility and the continuous nonvanishing local Euler contraction.
- `RHBridge.QuantizedPhaseIndexNoGoAudit` reports only Lean's standard
  foundational axioms.

The computations are finite fixtures for exact formulas.  The convergence,
divergence, and topology conclusions above are analytic arguments, not
extrapolations from the numerical cutoffs.
