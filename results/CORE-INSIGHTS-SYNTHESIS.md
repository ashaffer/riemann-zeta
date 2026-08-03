# Core insights synthesis

Status: compression audit of the program through 2026-07-31.  This document
separates reusable mathematics from coordinate changes, countermodels, and
RH-equivalent restatements.

Update (2026-08-01): the subsequent orthogonal-path audits are compressed in
`FAILURE-MECHANISM-SYNTHESIS.md`.  Their common obstruction is a
fidelity--amplification--closure trilemma: an exceptional zero is globally
phase-coherent but locally square-summable, so localization and averaging
retain at most a vanishing or finite-energy signal, while uniform global
amplification tends to reinsert RH.

## 1. The one object behind most branches

At support `a`, the central object is the lowest spectral mode of the localized
zeta Weil form, equivalently the possible kernel of its Friedrichs operator or
of the completed compressed Suzuki operator.  The following languages describe
that same obstruction:

- vanishing localized Weil energy;
- a weak radical annihilating every form-domain variation;
- prime versus pole--archimedean cross balance;
- a symmetric-disk zero-sum radical identity;
- a compressed continuous Suzuki-kernel null vector;
- a constant-convolution or Wiener--Hopf defect;
- eigenvalue one of a Birman--Schwinger transform;
- a boundary/collar residual;
- a finite-window determinant ground state.

Moving among these coordinates is useful for choosing tools, but it does not
create independent equations.  Stage 2 proved this explicitly for the
completed, arithmetic, and zero-side descriptions.

## 2. What is genuinely established

1. The normalization-matched arithmetic Weil form and its smooth and
   logarithmic-domain explicit formulas are connected to the actual zeta
   zero sum using named literature inputs.
2. Many finite Galerkin windows are rigorously positive, with independent
   prime-side and zero-side numerical checks and kernel-checked certificates.
3. Exact support-extension, activation, collar, cross-kernel, and continuous
   Suzuki identities are formalized.
4. Failure of RH produces, via consensus first-crossing theory, a nonzero weak
   radical at a finite positive support.
5. Such a first-crossing mode is support-saturating: it is inherited from no
   smaller window and has nonzero component in every proper collar.
6. Real-zero entire finite-window characteristic functions converging
   compact-locally to completed xi would imply RH by Hurwitz.  The exact
   abstract and CCM-shaped implications are formalized.

None of items 1--6 excludes the radical.

## 3. The decisive empirical fact

The lowest localized eigenvalue becomes extraordinarily small as support
grows.  Refinement repeatedly reveals a smaller margin.  The same near-null
state reappears after preconditioning, in collar cross ratios, and in the CCM
finite-window ground state.  This explains why absolute perturbation bounds,
uniform coercivity, and fixed positive gaps repeatedly fail.

The program should therefore treat the near-kernel as structure to identify,
not an error to dominate.

## 4. General no-go principles learned

### Coordinate multiplication adds no rank

Prime, zero, kernel, and Euler--Lagrange descriptions of one radical are not
independent constraints.  A contradiction must use parameter history,
asymptotics, or new arithmetic structure.

### Support saturation is qualitative only

Nonzero mass in every collar does not give a useful lower rate.  Shrinking
`L2` collar mass tends to zero, and an axiom-free model shows that even a fixed
uniform collar lower bound is compatible with a nonzero radical.

### Generic operator theory cannot prove zeta transversality

Finite-dimensional countermodels defeat conclusions based only on symmetry,
closedness, compactness, determinant one, reflection invariance, or simple
ground states.  The natural total-positivity and generic preconditioning
routes also failed direct numerical tests.

### Universal relative bounds can hide the conclusion

The sharp Schur/cross contraction and several proposed leakage inequalities
become equivalent to positivity when asserted for all vectors and supports.
They are certificates, not independent mechanisms, unless derived from a
strictly weaker arithmetic statement.

### Asymptotic zero statistics do not control exceptional zeros

GUE-type spacing and density-one statements cannot exclude a zero-density
off-line set.  Pointwise ordinate rigidity strong enough to do so is already
RH-equivalent.

### Real-zero approximants need identification, not only self-adjointness

Every finite CCM/Suzuki characteristic function may have real zeros while its
limit remains unidentified.  Compact-local convergence to xi carries the
global content.  Suzuki's proposed `z^2 xi/xi'` target also has an entire-limit
problem because the ratio is a priori meromorphic.

## 5. The compressed bottleneck

All live approaches now require a **near-kernel identification theorem**:

> After the correct normalization, the lowest localized Weil mode converges
> in a topology strong enough to determine its transform or arithmetic
> residual, and the limiting object is the specific CCM comparison vector
> `k_lambda = E(h_lambda)`.

Here `h_lambda` is not the ordinary prolate ground state.  It is the uniquely
normalized zero-integral linear combination of prolate modes 0 and 4 used by
CCM, followed by their arithmetic map `E`.  CCM already prove that the Fourier
transform of `k_lambda` converges to completed xi uniformly on closed
substrips.  The missing identification is the normalized Weil ground state
versus `k_lambda`.

This statement is stronger than observed numerical alignment but more
informative than positivity.  It is the common missing input behind:

- prolate--Weil ground-state comparison;
- finite-window simplicity and parity;
- CCM determinant convergence to xi;
- a non-circular boundary-flux law;
- any quantitative description of the collapsing margin.

## 6. Strength audit of the current determinant subtargets

Reflection symmetry plus simplicity only gives a pure even or odd state; an
odd simple ground state is possible in an axiom-free model.  Numerically the
zeta even block lies below the odd block through the tested range, but the gap
collapses rapidly.

Moreover, a cofinal theorem that the relevant parity block stays positive or
always contains the first mode is close to the classical parity-restricted
Weil criteria.  It must not be treated as a routine finite-dimensional lemma.
The useful target is therefore not bare even/odd ordering, but a structural
comparison that simultaneously explains the eigenvector's prolate shape.

## 7. New minimal roadmap

### A. Build a relative `k_lambda`--Weil comparison

Construct the precise CCM vector `k_lambda = E(h_lambda)` in the same finite
window and decompose the localized space into `span(k_lambda)` and its
orthogonal complement.  Seek estimates of the form

`||offDiagonal||^2 < complementGap * scalarDefect`

in scale-adapted units.  Absolute operator norm is the wrong quantity because
both the Weil margin and parity gap collapse.  The first falsification test is
whether this dimensionless ratio remains separated from one under refinement.

### B. Convert relative comparison into eigenvector convergence

Prove simplicity and control the normalized ground vector in weighted `L1`
or another topology that gives compact-local Fourier convergence.  Plain `L2`
convergence is insufficient on growing intervals without a uniform weight.

### C. Identify the determinant limit

Use the exact finite-window determinant identity and zero-free normalization
to prove compact-local convergence directly to `z -> xi(1/2-i z)`.  Hurwitz
then supplies RH; this implication is already formalized.

## 8. Kill rules for the next attempt

Stop or reformulate immediately if:

1. the proposed estimate is universal Schur positivity in disguise;
2. its constant is divided by the collapsing absolute ground margin;
3. it uses the fixed-window radical identity as if its coordinate forms were
   independent;
4. it assumes a positive zeta Hamiltonian, Herglotz function, or globally
   positive screw kernel;
5. it asks finite-window self-adjointness alone to identify the limit;
6. the relative prolate comparison ratio approaches one under refinement.

## 9. Fresh next checkpoint

The exact residual audit reveals an earlier checkpoint than Feshbach theory.
For each fixed zero disk, compact-local convergence
`Fourier(k_lambda) -> Xi` makes the zero-side residual tend to zero because Xi
vanishes at every zeta zero unconditionally.  The missing step is interchange
of the support and zero-radius limits.  Prove or falsify a zero-tail estimate
uniform in `lambda` for the normalized comparators.  Only after that should we
measure the two-by-two Feshbach quantities around `k_lambda`.
