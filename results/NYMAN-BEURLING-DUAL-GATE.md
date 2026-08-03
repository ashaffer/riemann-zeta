# Nyman--Beurling fail-fast gate: duality and exact interpolation

Status: non-Hilbertian-dual and exact-interpolation search completed; branch
demoted; 2026-08-01.

## 1. Mellin-space statement

Let `H=L2((0,1),dt)` and let `NB` be Nyman's closed dilation space.  The Mellin
transform is an isometry from `H` to the Hardy space of the half-plane
`Re(s)>1/2`.  The target `1_(0,1)` transforms to `1/s`.

For Nyman's generator `rho_alpha`, Burnol records the exact identity

`M rho_alpha(s) = (alpha-alpha^s) zeta(s)/s`.

Consequently every zero `rho` with `Re(rho)>1/2` annihilates the generator
space while the target takes the nonzero value `1/rho`.  The Hardy reproducing
kernel at `rho` is an explicit dual witness.

Evaluation gives the lower bound

`distance(1,NB)^2 >= (2 Re(rho)-1)/|rho|^2`.

The carrier is exact, but its metric size tends to zero if the zero approaches
the critical line or moves to large height.  Thus the old collapsing-margin
problem is present in its sharpest possible form.

## 2. Burnol's exact inner-factor theorem

Let `B(s)` be the Blaschke product in `Re(s)>1/2` formed from all zeros of
`zeta` in that half-plane.  Burnol proves

`M(NB)=B H2`.

He also proves that the norm of the orthogonal projection of the target onto
`NB` is

`|B(1)| = product_(Re(rho)>1/2) |(1-rho)/rho|`.

Therefore

`distance(1,NB)^2 = 1-|B(1)|^2`.

For one simple forbidden zero `rho=beta+i gamma`, its individual factor gives

`1-|1-rho|^2/|rho|^2 = (2 beta-1)/|rho|^2`,

exactly matching the reproducing-kernel obstruction.  There is no missing
stronger Hilbert-space invariant: the distance is already the complete
Blaschke obstruction.

## 3. The quantized quotient is tautological

The model space

`K_B = H2 minus B H2`

is an exact quotient obstruction.  If the forbidden zero set is finite, its
dimension, counting multiplicity, is the number of those zeros.  This is
integer-valued and cannot be cancelled by small amplitudes.

But this does not supply a proof mechanism.  `K_B={0}` exactly when `B=1`,
which exactly says there are no zeros in `Re(s)>1/2`.  Computing the index from
the analytic symbol invokes the argument principle and returns the forbidden
zero count.  Computing it from the arithmetic side requires proving cyclicity
or outerness of the zeta multiplier, which is the Nyman criterion itself.

Thus the quantization solves detection, not exclusion.

## 4. Why changing `L2` does not help

Beurling's `Lp` theorem identifies density with the zero-free half-plane

`Re(s)>1/p`.

- `p=2` gives the RH boundary.
- `p<2` puts the boundary to the right of `1/2` and gives only a weaker
  zero-free assertion.
- `p>2` puts it left of `1/2` and demands exclusion of the known critical-line
  zeros, so the density assertion is false.

Hence there is no fixed non-Hilbertian exponent that preserves equivalence
while creating additional norm slack.  Letting `p` tend to two merely restores
the same collapsing boundary.

Hahn--Banach duality also adds no order: its annihilators are precisely Hardy
evaluation kernels and their derivative kernels at the forbidden zeros.

## 5. The discrete Báez--Duarte system

Báez--Duarte's strengthening restricts the dilation parameters to `1/n`.
Finite sections yield explicit Gram matrices and Schur-complement distances,
but Gram positivity is automatic.  The substantive statement is that their
distances tend to zero.  Any off-line zero imposes the same nonzero evaluation
obstruction; under RH, constructing approximants uses Möbius/zeta cancellation.

Thus:

- determinant positivity contains no RH information;
- determinant or Schur-complement convergence to zero is the closure
  criterion itself;
- exact interpolation at an off-line zero proves failure, while proving that
  there are no interpolation nodes is RH;
- coefficient formulas return the Möbius cancellation route already audited
  in this repository.

## 6. Verdict

The tightly scoped search found the strongest available structures, but they
close the branch rather than promote it:

1. the full dual obstruction is explicitly the off-line-zero Blaschke product;
2. its integer-valued model-space dimension is the forbidden-zero count;
3. its metric distance has the exact collapsing scale
   `(2 beta-1)/|rho|^2`;
4. changing `Lp` shifts the zero-free boundary and loses equivalence;
5. the discrete system's remaining convergence is Möbius cancellation in
   Hilbert-space form.

Nyman--Beurling is therefore an exceptionally transparent model of *why* the
previous approaches fail, but not an easier target.  It should be demoted.
The top three literature equivalence families have now all failed their
specified promotion gates; the correct next action is a portfolio regroup,
not automatic pursuit of the next cosmetic reformulation.

## Literature anchors

- J.-F. Burnol, *A note on Nyman's equivalent formulation of the Riemann
  Hypothesis* (1999/2001).
- L. Báez-Duarte, *A strengthening of the Nyman--Beurling criterion for the
  Riemann hypothesis* (2002).
- J.-F. Burnol, *A lower bound in an approximation problem involving the zeros
  of the Riemann zeta function*, Adv. Math. 170 (2002), 56--70.
