# Stage 2: completed defect characterization

## Parsimony correction

Stage 2 cannot generally demand an ordinary `L_0^2` representative.  Suzuki's
completed kernel space is not contained in `L2`, and the closed derivative of
the constant interval function is explicitly nonzero even though its interior
derivative vanishes.  Endpoint distribution data are part of the construction,
not a technical nuisance to discard.

Accordingly, the invariant object is the weak defect functional

`g -> B_a(f,g)`

on the logarithmic form domain.  It is meaningful for the actual
first-crossing vector and automatically includes interior and boundary data.

## Synchronized characterizations

For a first-crossing mode `f` and every form-domain variation `g`, Lean now
packages three descriptions of the same vanishing defect:

1. **Completed kernel:** `D_bar f` is a nonzero vector in the kernel of the
   extended Suzuki operator.
2. **Arithmetic:**
   `B_pole(f,g) + B_arch(f,g) = B_prime(f,g)`.
3. **Zero side:** the polarized Guinand--Weil sums over zeros in symmetric
   disks converge to zero.

The zero-side statement uses disk exhaustion and does not assume RH,
termwise positivity, or unconditional scalar convergence.

All three are retained in the single structure `DefectCharacterization`; the
constructor `characterizeFirstCrossing` prevents the coordinate descriptions
from drifting apart.

## Trust boundary

Two standard form-domain inputs are currently axiomatized:

* closure of the logarithmic domain under addition;
* the radical theorem for the closed symmetric nonnegative form.

The explicit-formula disk limit and completed Suzuki bridge retain their
previous named literature axioms.  The public audit prints the full dependency
set.  None of these inputs assumes RH.

## What Stage 2 does not claim

It does not claim pointwise values, an ordinary derivative, or the classical
integral equation for every completed vector.  Those are optional regularity
upgrades.  The weak arithmetic and zero-side equations already constitute the
domain-safe defect characterization needed for Stage 3.

Stage 3 can therefore be stated parsimoniously: prove that no nonzero
form-domain vector can satisfy this one weak functional identity in all three
coordinates.

Lean now makes this exact through
`riemannHypothesis_of_no_defectCharacterization`: excluding the synchronized
package at every positive support and negative shift implies RH.  Conversely,
failure of RH constructs such a package at one finite positive support for
every negative shift.
