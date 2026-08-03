# Sonine complete-minimal systems: biorthogonal reflection gate

Status: finite-quartet signature derived; completeness/minimality and
co-Poisson reflection do not supply positivity beyond Weil's pairing; branch
demoted; 2026-08-01.

## 1. Burnol's unconditional structure

Let `L_a` be Burnol's extended Sonine space: functions constant on `(0,a)`
whose cosine transforms are also constant there.  Completed Mellin evaluation
at every `w != 0,1` is continuous, represented by a vector `Y_(w,k)^a` for
each derivative order.

Burnol proves for the nontrivial zeta zeros, with multiplicity:

- the evaluator system is minimal exactly for `a<=1`;
- it is complete exactly for `a>=1`;
- hence at `a=1` it is complete and minimal and has a unique biorthogonal
  system;
- for simple zeros, the dual functions are normalized versions of
  `zeta(s)/(s-rho)`.

This is substantial unconditional rigidity.  It does not assume RH.

## 2. Exact Fourier action

The completed Mellin transform obeys

`M(F_+ f)(s)=M(f)(1-s)`,

where `F_+` is the unitary cosine transform.  Using Burnol's bilinear
evaluation convention gives

`F_+ Y_w = Y_(1-w)`

and, with derivative evaluators, the corresponding triangular jet action.
Complex conjugation gives `C Y_w=Y_(conjugate(w))`.  Therefore the Hermitian
critical-line reflection is

`J=C F_+ : w -> 1-conjugate(w)`.

This is exactly the involution in Weil's zero-side pairing.

## 3. Finite simple-zero signature

Take a finite zero set invariant under

`tau(rho)=1-conjugate(rho)`

and use the evaluator/dual coordinates supplied by minimality.  Up to harmless
nonzero normalization factors, reflection has matrix

`R_(rho,sigma)=1 if rho=tau(sigma), else 0`.

The associated Hermitian form is `c^* R c`.

- If `Re(rho)=1/2`, then `tau(rho)=rho`; the block is `[1]` and is positive.
- If `rho` is off the line, `{rho,tau(rho)}` is a two-cycle; the block is

  `[[0,1],[1,0]]`,

  with eigenvalues `+1,-1`.
- A full ordinary zeta quartet contains two such cycles and contributes two
  negative directions.

Arbitrary evaluator normalizations replace a cycle block by

`[[0,a],[conjugate(a),0]]`,

whose eigenvalues are `+|a|,-|a|`.  The signature is invariant.

The diagnostic `src/sonine_reflection_signature.py` reproduces signatures
`(2,0,0)` for a critical conjugate pair and `(4,2,0)` after adding one off-line
quartet.

## 4. Multiplicities do not help

For a zero of multiplicity `m`, Burnol uses derivative evaluators
`Y_(rho,k)`, `0<=k<m`, and triangular combinations of
`zeta(s)/(s-rho)^l` in the dual system.  Fourier reflection maps the jet at
`rho` to the jet at `1-rho` by an invertible triangular matrix.

On an off-line reflected pair this gives a Hermitian block congruent to

`[[0,I_m],[I_m,0]]`.

Sylvester inertia is therefore `(m,m)`.  Multiplicity merely repeats the
negative directions.

## 5. Why completeness and minimality do not imply positivity

Completeness says the evaluator vectors span densely.  Minimality says each
has a unique dual coordinate.  Neither constrains the signature of a unitary
involution permuting those coordinates.

Indeed, at `a=1` the evaluator system is complete-minimal unconditionally,
whether or not an off-line quartet exists.  The cosine transform itself has
both `+1` and `-1` eigenspaces.  Co-Poisson intertwining proves the reflection
law but supplies no theorem placing the zeta evaluator span in a positive
reflection subspace.

Demanding positivity of the reflection form is exactly demanding that every
zero be a fixed point of `tau`, hence exactly RH.

## 6. Alignment with the prior two gates

The same two-per-quartet signature has now appeared in three precise forms:

1. the finite-zero Weil pairing;
2. the generalized-Nevanlinna negative-square kernel;
3. the Sonine evaluator/biorthogonal reflection form.

These are not three independent constraints.  They are the same Hermitian
involution transported through explicit formula, logarithmic derivative, and
Mellin/Fourier coordinates.

This is valuable compression: any future attempt using one of these systems
must identify an additional arithmetic theorem rather than count the same
negative blocks again.

## 7. Gate verdict

The Sonine route supplies unusually strong unconditional spectral synthesis,
but its proposed positivity engine fails:

- evaluator completeness and minimality hold without RH;
- co-Poisson/Fourier reflection gives exactly the functional-equation
  involution;
- the finite-quartet reflection block is the Weil block;
- a quartet gives two negative directions independently of normalization;
- positivity of the full reflection metric is RH itself.

Path 3 is therefore demoted.  All three post-regroup index/rigidity paths have
now converged to the same negative-signature invariant without producing an
arithmetic computation that forces its index to zero.

The correct next action is another synthesis, now sharper than the previous
one: determine whether the repeated two-per-quartet invariant yields a useful
universal no-go theorem, and search outside Hilbert/reflection/explicit-formula
coordinates for an arithmetic mechanism that computes an index rather than
detects it.

## Literature anchor

- J.-F. Burnol, *Two complete and minimal systems associated with the zeros of
  the Riemann zeta function*, J. Théor. Nombres Bordeaux 16 (2004), 65--94.
