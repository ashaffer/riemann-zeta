# Compression synthesis audit

> Superseded as the primary roadmap by `CORE-INSIGHTS-SYNTHESIS.md`, which
> incorporates the Stage 1--3, support-saturation, and determinant-limit
> audits.  This file remains as the detailed history of the earlier
> compression pass.

## The common statement

Most of the recent research branches are coordinate descriptions of one
operator-theoretic question.  Let `J_a` localize the input to a support window,
let `P_a` observe the corresponding interior output, and let `T` be the global
Weil operator.  A first-crossing zero mode produces

`u != 0`,  `J_a u = u`,  `P_a T J_a u = 0`.

Equivalently,

`T u` lies in `ker P_a`.

The desired theorem is the transversality statement

`range(J_a) intersect T^{-1}(ker P_a) = {0}`.

For a spatial restriction, `ker P_a` consists of exterior-supported
residuals.  For Suzuki's mean-removal projection, it consists of constants on
the interval.  After differentiation that constant defect disappears, giving
the distributional interior equation.

Lean formalizes this common algebraic skeleton in
`CompressedKernelSynthesis.lean`.

## What this condenses

| Previous language | Compression language |
|---|---|
| zero Weil energy at a nonnegative first crossing | radical vector of the compressed form |
| pole + archimedean = prime cross balance | `T u` is invisible to every interior variation |
| Suzuki constant-convolution equation | raw convolution belongs to the one-dimensional constant defect |
| collar boundary residual | the unobserved component of `T u` in `ker P_a` |
| failed global Fourier multiplier equation | compression does not imply `T u=0`; it only locates `T u` in the defect |
| Schur complement/cross contraction | quantitative transversality between the localized range and defect preimage |
| canonical endpoint determinant | a proposed coordinate test for the same transversality |
| Birman--Schwinger eigenvalue exclusion | preconditioned coordinate test for the same transversality |
| zero-side quartet cancellation | spectral-coordinate test for the same transversality |

This explains why many apparently different final inequalities became
equivalent to positivity: they were universal quantitative formulations of
the same transversality statement.

## The genuinely established chain

1. Consensus literature: RH is equivalent to global Weil positivity.
2. Consensus literature plus continuity and a positive base window: failure
   of RH leads to a first support where the lowest localized spectral value is
   zero.
3. Elementary quadratic-form theory: at a nonnegative window, a zero-energy
   vector lies in the radical.
4. Repository normalization work: on the smooth core, the radical equation is
   exactly the pole--archimedean--prime balance and, through the imported
   Suzuki identity, the screw-kernel weak equation.
5. Elementary compression algebra: the weak equation says that the global
   operator output lies in the projection defect.

Items 3 and 5 are abstractly kernel-checked.  Item 4 is kernel-checked after
the named Guinand--Weil and Suzuki literature axioms are admitted.

## Domain caveat discovered by this audit

The repository does **not** yet contain a full formal instantiation of the
closed unbounded operator `A_a`, its form domain, Suzuki's completed spaces,
and the extended derivative isomorphism.  The files
`SuzukiKernelZeroReduction.lean` and `CompressedKernelSynthesis.lean` prove
generic algebraic equivalences; they do not themselves prove that an
arbitrary first-crossing eigenvector belongs to the smooth/H1 core or maps to
an ordinary `L_0^2` kernel vector of `G_a`.

Suzuki's literature supplies the intended operator dictionary, including the
exceptional statement that generalized eigenvalue zero is the kernel problem
for `G_a`.  But a complete repository-level theorem composing that dictionary
with the first-crossing eigenvector remains absent.  Reports should therefore
label the `A_a`--`G_a` zero-mode passage **literature-backed and abstractly
modeled**, not fully formalized.

This caveat does not invalidate the research reduction, but it lowers the
formal completion status and identifies a concrete bridge worth backfilling
if the compression formulation yields new mathematics.

## What the negative experiments really show

The experiments did not produce many unrelated failures.  They tested common
ways of proving transversality:

* finite propagation: defect determined by finitely many interfaces--false
  because the archimedean operator has continuous delays;
* global multiplier uniqueness: defect forced to zero--false because
  compression permits nonzero exterior output;
* total positivity: sign-regularity forces transversality--false for the
  natural discrete Green kernel;
* canonical zero parameter: defect encoded by independent endpoint lines--the
  available shifted construction uses a different spectral parameter;
* relative cross contraction: angle between the two spaces is uniformly
  acute--equivalent to positivity when asserted universally;
* generic elliptic preconditioning: transversality follows from the principal
  symbol--numerically a rescaling of the original ground margin;
* zero-by-zero phase isolation: spectral coordinates diagonalize the defect--
  false unconditionally because off-line quartets are indefinite and the
  sampling family is overcomplete.

They collectively say that the missing theorem must use a special invariant
of the **pair** `(localized subspace, zeta operator defect)`, not a generic
property of either object separately.

## Simpler roadmap

The program can now be stated in three stages rather than many routes:

1. **Closed-domain bridge.** Precisely instantiate the first-crossing radical
   as a compressed-kernel witness for the continuous Suzuki operator.
2. **Defect characterization.** Describe all possible interior-invisible
   outputs `T u` using both arithmetic coordinates (prime/digamma balance) and
   spectral coordinates (zero quartets), without demanding termwise signs.
3. **Transversality theorem.** Prove that no nonzero compactly supported input
   can produce such a defect.  A useful new invariant must couple support,
   arithmetic translations, and the one-dimensional/exterior defect at once.

Stage 1 is now composed in `SuzukiClosedDomainLiterature.lean`.  A
first-crossing form-domain vector maps, for every negative shift, to a nonzero
kernel vector of the extended continuous-kernel operator on Suzuki's completed
space.  The two closed-domain analytic inputs remain explicitly audited
literature axioms.  See `STAGE1-CLOSED-DOMAIN-BRIDGE.md`.

The audit also sharpens Stage 2: recovering an ordinary pointwise
constant-convolution equation from this completed kernel vector is a separate
regularity/representative theorem, not part of the abstract Stage-1 bridge.

Stage 2 is now completed in the weaker and domain-correct form.  The single
defect functional is synchronized across the completed Suzuki kernel,
arithmetic pole--archimedean--prime balance, and polarized symmetric-disk zero
sum.  See `STAGE2-DEFECT-CHARACTERIZATION.md`.  Ordinary-L2 or pointwise
representatives are optional regularity upgrades, not prerequisites for the
Stage-3 transversality problem.

Stage 3 has its first genuinely new invariant.  Adding the first-crossing
parameter history proves that the defect cannot be inherited from any smaller
window; equivalently, its orthogonal component in every proper boundary collar
is nonzero.  This qualitative support saturation is proved in
`Stage3SupportSaturation.lean`.  It does not yet supply quantitative collar
mass or exclude a boundary-saturating radical vector, so transversality remains
the decisive open theorem.
