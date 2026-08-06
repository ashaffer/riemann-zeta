# Suzuki projective-kernel checkpoint

Status: the exact direct-system intertwiner is obstructed in the tested
completed-Weil Galerkin models, but this does **not** obstruct Suzuki's weaker
strong-resolvent program.  More decisively, a naturally embedded cofinal
construction whose admissible shifts tend to zero already entails global
nonnegativity of the finite-window Weil floors.  That limiting step cannot be
used as an unconditional shortcut to positivity.

## 1. Exact projective invariant

Let `D_a*` and `D_b*` be two adjoints with one-dimensional labelled
eigenspaces and normalized generators `d_a(z)` and `d_b(z)`.  If a complex
linear isometry `U` preserves the spectral parameter and intertwines the
adjoints, then

```text
U d_a(z) = q(z) d_b(z),                 |q(z)|=1.
```

Therefore their normalized Gram kernels obey

```text
K_a(z,w) = conjugate(q(z)) q(w) K_b(z,w).
```

Two classes of quantities are consequently invariant:

```text
|K(z,w)|,
K(z,w) K(w,u) K(u,z).                   (Bargmann triple)
```

This statement is independent of the phases chosen for individual
deficiency vectors.  A self-adjoint extension phase also cannot repair a
mismatch because it selects a boundary relation only after the maximal
adjoint and its defect lines have been fixed.

Lean proves the diagonal-gauge identity, unit modulus of the comparison
scalars, pairwise squared-magnitude invariance, and Bargmann-triple invariance
in [`ProjectiveGramInvariant.lean`](../lean/rhbridge/RHBridge/ProjectiveGramInvariant.lean).
Its audit contains no project axiom.

## 2. Finite necessary-condition diagnostic

For a positive Galerkin metric `T_s=A-sI`, the projected Riesz representative
of the exponential functional is

```text
d_s(z)=T_s^-1 P exp(-i z x).
```

Its energy Gram kernel can be assembled without forming a dense spectral
grid:

```text
K_s(z,w)=<P exp(-i z x), T_s^-1 P exp(-i w x)>_L2.
```

The diagnostic normalizes the diagonal, fits the available target shift on
alternating training probes, and reports phase-gauge, magnitude, and Bargmann
residuals on held-out probes.  The scalar metric is an exact positive control;
the Dirichlet energy is a continuum-derived negative control.

| model | dimension | comparison | full gauge RMS | max magnitude defect |
|---|---:|---|---:|---:|
| scalar control | 10 | shifts `0,-1` | `2.87e-16` | `3.33e-16` |
| Dirichlet control | 10 | shifts `0,-1` | `.0330` | `.0521` |
| completed Weil | 6 | `L:1.75→2.485`, common `s=-.05` | `.5195` | `.5995` |
| completed Weil | 8 | same | `.6193` | `.4235` |
| completed Weil | 10 | same | `.6271` | `.4399` |
| completed Weil | 6 | same, common `s=-.25` | `.6061` | `.4435` |
| completed Weil | 8 | same | `.5928` | `.3593` |
| completed Weil | 10 | same | `.5983` | `.3599` |

Thus the natural exact, same-`z`, common-shift unitary intertwiner is strongly
incompatible with these finite models.  Separately tuned target shifts do not
give a stable conclusion: their optima are truncation-sensitive and often hit
the search interval boundary.

Allowing the justified affine coordinate gauge is important.  Fitting
`z_target=alpha*z+beta` reduces much of the geometric window mismatch, but it
does not remove the held-out defect:

| dimension | shift | fitted `alpha` | training RMS | held-out RMS | full RMS |
|---:|---:|---:|---:|---:|---:|
| 6 | `-.25` | `.688` | `.0048` | `.142` | `.072` |
| 8 | `-.25` | `.684` | `.0053` | `.178` | `.092` |
| 10 | `-.25` | `.669` | `.0095` | `.154` | `.080` |

The fits are interior, have `beta=0`, and sit near the pure geometric dilation
factor `.704`.  An exact scalar-dilation control has full residual below
`4e-16`.  Thus dilation explains most of the raw `.6` residual; the remaining
failure is smaller but genuinely out of sample.  It still concerns exact
finite equivalence, not asymptotic convergence.

The implementation is
[`suzuki_boundary_intertwiner_diagnostic.py`](../src/suzuki_boundary_intertwiner_diagnostic.py).
It uses roughly 43 MB in the displayed scan.  The calculation is not an
interval certificate and the Galerkin vectors are not certified graph-limit
approximations of the unbounded adjoints.

## 3. What this does and does not prune

The exact theorem applies if one claims

```text
U D_a* = D_b* U
```

with the same spectral coordinate.  It does not apply unchanged to:

- an affine reparameterization `z -> alpha z + beta`, reflection, or an
  antiunitary comparison;
- a nonunitary embedding or compression;
- equality or convergence of only one selected self-adjoint extension;
- strong-resolvent convergence of genuinely different truncations.

In particular, natural truncations of one global operator need not be
unitarily equivalent at finite support.  The stable cross-window failure above
therefore prunes an overstrong direct-system claim, not the intended
asymptotic route.  For the latter, the relevant observable is convergence,
after specified embeddings and coordinate normalization, of the transported
defect kernel on compact `z,w` sets.

## 4. Exact shift compatibility and the real circularity checkpoint

For an old vector embedded by zero extension, the completed Weil energy and
the `L2` norm are unchanged.  Hence

```text
t_(b,sigma_b)(Jf)-t_(a,sigma_a)(f)
  = (sigma_a-sigma_b) ||f||_2^2.
```

The scalar identity and its rigidity corollary are formalized, without heavy
zeta imports, in
[`NestedShiftRigidity.lean`](../lean/rhbridge/RHBridge/NestedShiftRigidity.lean).
The zeta specialization follows from the existing
`ActivationCancellation.weilForm_nestedSupport_eq` and
`NestedSupport.norm_nestedSupport` theorems.  Exact isometry on even one
nonzero old vector forces `sigma_a=sigma_b`.

There is an even sharper cofinal statement.  Let `lambda(a)` be an antitone
family of window floors and let `a_n` tend to infinity.  Lean proves

```text
(exists sigma_n -> 0 with sigma_n < lambda(a_n) for every n)
  iff
(lambda(a) >= 0 for every a).
```

The reverse implication uses the explicit shifts `sigma_n=-1/(n+1)`.  See
[`CofinalShiftPositivity.lean`](../lean/rhbridge/RHBridge/CofinalShiftPositivity.lean).
For the completed zeta Weil family, the further identification of the
right-hand side with RH is the consensus Weil criterion, not a theorem of this
abstract module.

Consequently a natural-core limit cannot obtain an admissible vanishing shift
for free: proving that such shifts exist is already the global positivity
problem in another form.  A genuinely unconditional survivor must instead
use a fixed negative shift and identify the resulting shifted global model,
or use explicit varying-space comparison maps that do not silently assume an
unshifted Hilbert completion.

## 5. Follow-up calibration and next honest target

The next fail-fast target was an overdetermined comparison of a canonically
normalized finite characteristic with a separately derived zeta model:

1. fix every sign, parity, spectral-coordinate, and zero-free normalization;
2. use one scalar datum to choose the only auxiliary shift;
3. test independent characteristic values and compact-set kernel invariants;
4. under refinement, require held-out residuals to tend to zero;
5. only after that seek a certified graph- or strong-resolvent theorem.

That normalization and test are now complete.  A derivative calibration and
two weak imaginary-axis values pass extremely closely, but stronger real and
off-axis probes fail nonmonotonically; the easy agreement is a near-Cayley
effect.  See
[`SUZUKI-LIVSIC-CALIBRATION-FAIL-FAST.md`](SUZUKI-LIVSIC-CALIBRATION-FAIL-FAST.md).

That divisor-level gate is now complete on the certified range.  The fixed
shift `sigma=-1/4` is continuum-admissible through `L=749/250`; one phase is
fit on alternating zeta ordinates and tested using ordered injective root
matching.  The held-out error remains large, including at both exact symmetry
phases `theta=0,pi`, although it improves with support.  See
[`SUZUKI-FIXED-SHIFT-DIVISOR-CHECKPOINT.md`](SUZUKI-FIXED-SHIFT-DIVISOR-CHECKPOINT.md).
No conclusion about RH follows from the finite scan.
