# Global trace versus separate polarization: finite gate

Status: the finite-dimensional, independent-compact-place-torus-equivariant
class with an invariant positive metric and the stated trace architecture is
eliminated, 2026-08-04.  The independent place action is a hypothesis, not a
property proved for the adelic quotient.  The infinite semilocal/global-
polarization program remains open.  No RH claim is made.

## 1. Verdict

The two-prime trace calculation is not the missing theorem.  For every finite
place set, Connes's semilocal trace formula already realizes the sum of the
local Weil distributions on one coupled adele-class space.  At the elementary
level, the connected Euler potential also removes mixed composites exactly.

The missing datum is a positive polarization fixed independently of the
putative zero spectrum and compatible when a new prime is adjoined.  The
smallest finite model has the following dichotomy.

1. If its connected trace is an honest finite equivariant character (or its
   middle cohomology is parity-pure), absence of mixed characters and
   invariance of a positive metric force an orthogonal direct sum of the
   prime, second-prime, and gamma sectors.  There is no cross-place positivity
   mechanism.
2. If its connected trace is only a supercharacter, plethystic logarithm, or
   cumulant, mixed states can cancel virtually.  That cancellation has no
   positive meaning.  Equivariant Hodge contraction removes acyclic glue
   weight by weight, while parity-balanced harmonic sectors remain invisible
   to the signed trace and cannot acquire positivity from it.

The adjoint equation makes the obstruction sharper.  For a finite generator
`A`, a positive Hermitian matrix `G` satisfying

```text
A* G + G A = G
```

exists if and only if `A` is diagonalizable and its spectrum already lies on
`Re(s)=1/2`.  Thus solving for `G` after constructing `A` is exactly the finite
critical-line assertion, not an explanation of it.

Consequently Prompt D's specified finite equivariant unit test is eliminated
as a nontrivial route.  Finite non-equivariant, noncompact, or differently
coupled models are not classified.  The genuinely infinite survivor is much
narrower: construct a canonical
positive cup/star or compression metric on the coupled semilocal object,
without using zeta zeros or the minimum of the Weil form, and prove naturality
as the finite place set grows.

## 2. Exact two-prime normalization

Take the finite places `3` and `5`, and put

```text
x = 3^(-s),  y = 5^(-s).
```

The connected Euler potential is

```text
C(x,y) = -log(1-x) - log(1-y)
       = x + x^2/2 + y + y^2/2 + higher pure powers.
```

It has no `xy` coefficient.  Applying `-d/ds` gives

```text
log(3) (3^(-s) + 3^(-2s) + ...)
  + log(5) (5^(-s) + 5^(-2s) + ...),
```

so the coefficients at `3,9,5,25` are respectively
`log(3),log(3),log(5),log(5)`, while the coefficient at `15` is exactly zero.

A particularly clean translation window has

```text
log(25) < L < log(27).
```

The mixed location `log(15)` lies inside it, while `log(27)` does not.  In the
centered Weil normalization, the individual spikes at `+-log(n)` have weights

```text
log(3)/sqrt(3), log(3)/3, log(5)/sqrt(5), log(5)/5,
```

and there is no spike at `+-log(15)`.  Equivalently, the repository's
quadratic-form convention contributes

```text
2 Lambda(n)/sqrt(n) * autocorrelation(log(n)).
```

This is an exact normalization test, not a new trace construction.

The archimedean multiplier is also fixed rather than fitted:

```text
h_infinity(tau) = -log(pi) + Re psi(1/4 + i tau/2)
```

```text
= -log(pi) - EulerGamma
  + sum_(n>=0) [1/(n+1)
      - (n+1/4)/((n+1/4)^2 + (tau/2)^2)].
```

The script `src/two_prime_global_trace_gate.py` checks the pure/mixed Euler
jet and the `n=0,1` gamma-mode rational part exactly.  The full one-sided
degree-two ladder has the regularized gamma determinant already checked in
`src/archimedean_gamma_determinant.py`; two modes are only a finite fixture.

## 3. Connected-character splitting

Let `R` be a characteristic-zero coefficient ring and let

```text
C(x,y,u) in R[[x,y,u]]
```

be a connected character.  If every coefficient whose monomial involves at
least two of `x,y,u` vanishes, then coefficientwise

```text
C(x,y,u) = c + C_p(x) + C_q(y) + C_infinity(u).
```

This elementary identity is important: at the decategorified connected-trace
level, exact exclusion of every mixed primitive leaves no cross-place datum.
Any useful cross-place information must therefore be extension, differential,
or polarization data invisible to this character.

Now let a finite Hilbert complex carry an equivariant unitary action of the
compact place torus `T^3`, and assume that the differential and the proposed
polarization respect that action.  This independent compact-torus action is a
model hypothesis; it has not been derived for the multiplicatively coupled
adelic/product-formula quotient, and the archimedean modes are not
automatically its characters.  Under the hypothesis, the standard weight
decomposition gives

```text
C = direct-sum_(chi) C_chi,
```

and distinct weight spaces are orthogonal: if `v` and `w` have characters
`chi` and `eta`, invariance gives

```text
<v,w> = chi(t) conjugate(eta(t)) <v,w>
```

for every `t`; choosing `t` with `chi(t) != eta(t)` forces `<v,w>=0`.
The differential, Hodge Laplacian, harmonic projection, and every equivariant
generator preserve this decomposition.

For the six weights

```text
p, p^2, q, q^2, gamma_0, gamma_1,
```

the invariant Gram pattern is therefore diagonal.  Finite-dimensional
unitarity also makes the representation semisimple, so a nontrivial extension
cannot evade the splitting while retaining the invariant positive metric.

There is one necessary caveat.  A supercharacter can have zero coefficient at
a mixed weight because its even and odd multiplicities agree, without that
weight space being zero.  This does not rescue the argument: positivity does
not descend from a supertrace, and equivariance still prevents that mixed
weight from pairing with any of the pure coordinate-axis weights.  Additional
geometry could assign it a role, but that role is not determined by the trace
unit test.

There is an exact finite countermodel to the idea that noncommutative
chain-level gluing is enough.  Let

```text
B_p = [[1,0],[0,0]],
B_q = (1/2)[[1,1],[1,1]].
```

These are noncommuting orthogonal projections.  Put identical copies of this
two-dimensional bridge in even and odd degrees and join them by the identity
differential.  Add one pure even `p` state and one pure even `q` state.  Then,
for every `k>=1`,

```text
Str(P^k)=Str(Q^k)=1,
```

while the supertrace of every word containing both `P` and `Q` is zero.  The
model has noncommuting cross-place structure and a canonical positive chain
metric, but the bridge is contractible.  Its cohomology is exactly the
orthogonal `p direct-sum q` pair.  Every word acts by identical matrices on
the even and odd bridge copies, so their supertraces cancel for all words;
this is the proof, while the regression script checks only finite fixtures.
The example is a concrete "fake globality" control: signed cancellation can
make a trace look globally glued while adding no cohomological polarization.

## 4. Positive adjoint metric equivalence

Let `A` be a finite complex matrix.  Then the following are equivalent.

1. There is a positive-definite Hermitian `G` such that
   `A* G + G A = G`.
2. `A - (1/2)I` is similar to a skew-Hermitian matrix.
3. `A` is diagonalizable and every eigenvalue has real part `1/2`.

For `1 => 2`, let `S=G^(1/2)`.  The adjoint equation says

```text
(A-(1/2)I)* G + G (A-(1/2)I) = 0,
```

so `S(A-(1/2)I)S^(-1)` is skew-Hermitian.  Conversely, if
`T(A-(1/2)I)T^(-1)` is skew-Hermitian, then `G=T* T` is positive and satisfies
the equation.  The equivalence with item 3 is the finite-dimensional spectral
theorem.

This proves a useful audit rule:

> A metric computed from the eigenvectors of `A`, or from the already known
> positivity margin of the target form, has assumed precisely the spectral
> conclusion that it was meant to prove.

## 5. Functional-equation duality is weaker

For any nonzero rational `a`, set

```text
A_a = [[1/2+a, 0], [0, 1/2-a]],
Omega = [[0, 1], [-1, 0]].
```

Then

```text
A_a^T Omega + Omega A_a = Omega.
```

Thus the functional-equation pairing `rho <-> 1-rho` is perfectly compatible
with an off-line pair.  But if a matrix `G` satisfies

```text
A_a^T G + G A_a = G,
```

its two diagonal entries are forced to vanish.  It cannot be strictly
positive.  By contrast, the real critical-line block

```text
A_gamma = [[1/2, -gamma], [gamma, 1/2]]
```

satisfies `A_gamma^T I + I A_gamma = I`, and `I` is strictly positive.

All four statements are kernel-checked over the rationals in
`RHBridge.FinitePolarizationNoGo`; the audit reports only `propext`,
`Classical.choice`, and `Quot.sound`.

## 6. Comparison with the function-field control

The distinction between trace and polarization is genuine in the successful
function-field case.  The repository's `CurveCertE5.lean` derives Frobenius
data from the point count of an elliptic curve over `F_5`, constructs the
Rosati Gram matrices independently, and kernel-checks their positivity and
Cayley--Hamilton kernel.  The positive form is geometric input; it is not
obtained by factoring the desired Weil matrix after the fact.

The number-field finite toy has no analogue of that independently generated
Rosati structure.  Adding an arbitrary positive form makes a model but does
not explain the explicit formula, while enforcing the adjoint law makes it a
restatement of the critical-line conclusion.

## 7. Surviving infinite target and kill conditions

The surviving target must provide all of the following before it earns an RH
update:

1. one genuinely coupled semilocal/global space, not an orthogonal sum of
   place Hilbert spaces;
2. the exact signed trace, including the fixed archimedean multiplier;
3. a canonical positive polarization defined without zeros, a Cholesky factor
   of the Weil form, or its lowest eigenvalue;
4. a proof of the adjoint law for the global generator;
5. naturality and quantitative control under `S subset S union {p}`;
6. a global limit theorem strong enough to recover completed zeta.

Connes's semilocal trace construction supplies item 1 at the equality level.
The archimedean compression work supplies a positive mechanism at the real
place.  Current semilocal prolate constructions supply substantial operator
machinery, but not items 3--6.  Recent finite Euler-product self-adjoint
approximants likewise leave convergence to `Xi` as the decisive step; their
existence is not an independent positivity proof.

The specified finite equivariant trace/metric class is therefore complete and
negative.  The quantized completed-phase/index audit proposed here was
subsequently completed; see
[`QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md`](QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md).
Returning to global polarization is justified only by a concrete candidate
for item 3.

## 8. Primary literature anchors

- Alain Connes, *Trace formula in noncommutative geometry and the zeros of the
  Riemann zeta function*: <https://arxiv.org/abs/math/9811068>.
- Ralf Meyer, *On a representation of the idele class group related to primes
  and zeros of L-functions*: <https://arxiv.org/abs/math/0311468>.
- Christopher Deninger, *Analogies between analysis on foliated spaces and
  arithmetic geometry*: <https://arxiv.org/abs/0709.2801>.
- Alain Connes and Caterina Consani, *Weil positivity and Trace formula, the
  archimedean place*: <https://arxiv.org/abs/2006.13771>.
- Alain Connes, Caterina Consani, and Henri Moscovici, *Zeta zeros and prolate
  wave operators*: <https://arxiv.org/abs/2310.18423>.
- Alain Connes, Caterina Consani, and Henri Moscovici, *Zeta Spectral
  Triples*: <https://arxiv.org/abs/2511.22755>.
