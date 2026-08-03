# De Branges/canonical-system and function-field bridge audit

Status: research ledger, not an RH proof and not a novelty claim.  Sources were
checked through 2026-07-31.  The purpose is to state targets sharply enough that
we can tell a new intermediate theorem from Weil positivity in new notation.

## 1. Canonical-system target

Let `Q_a` denote the zeta Weil form on the support window `[-a,a]` in the
normalization used by RHBridge.

### CS-a (separated realization target)

Construct, without assuming RH, for every `a > 0`:

1. a positive semidefinite canonical-system Hamiltonian `H_a(x)`;
2. its de Branges/reproducing-kernel Hilbert space `B_a`;
3. an injective transform `U_a` from the RHBridge test space to `B_a`;
4. an *independently derived* identity

       Q_a(f,g) = <U_a f, U_a g>_{B_a}.

Items 1--4 imply window positivity, and injectivity implies nondegeneracy.  If
they hold compatibly for every `a`, the existing RHBridge Weil criterion gives
RH.

The useful subtarget is therefore not merely "find a de Branges space".  It is
to derive item 4 first on a dense arithmetic core from the prime/archimedean
explicit formula, with all closure and limit operations controlled independently
of positivity.  Positivity then comes from item 1 rather than being inserted
into the identification.

### CS-b (finite-interval spectral approximation)

Suzuki's 2026 conjecture suggests a more concrete version: build compatible
self-adjoint nonlocal realizations of the first derivative on `[-a,a]`, and
prove strong/norm resolvent convergence as `a -> infinity` together with an
unconditional determinant or trace identification with completed zeta.  A
genuine bridge theorem would have to specify:

* the operators and domains without referring to the unknown zeros;
* self-adjointness before any zeta spectral assertion;
* convergence strong enough to exclude spectral pollution;
* a zeta determinant/trace identity including multiplicities and completeness.

Self-adjoint finite-window operators alone say nothing about RH.  The last two
bullets are the decisive content.

## 2. Hidden-RH audit for the canonical-system route

| Proposed assumption | Audit |
|---|---|
| `Q_a >= 0` for every `a` | Exactly global Weil positivity after exhaustion; equivalent to RH. |
| The zeta screw kernel is positive definite on every finite interval | Equivalent to its being a screw function globally, hence equivalent to RH in Suzuki's theorem. |
| The zeta Weyl function is Herglotz/Nevanlinna | Its pole/positivity restrictions force the relevant zeta zeros onto the real spectral axis; this is an RH-strength assumption, not neutral canonical-system input. |
| There is a self-adjoint operator whose complete spectrum is the imaginary parts of all zeta zeros | Already forces those ordinates to be real, hence RH once the spectral identification is literal and complete. |
| A positive Hamiltonian exists | Harmless by itself.  The exact identification of its kernel or Weyl function with zeta is the RH-bearing step. |
| de Branges's older auxiliary positivity condition | Do not use: Conrey--Li showed the proposed conditions fail for the relevant zeta/L-function examples. |

Burnol's Sonine/de Branges spaces unconditionally attach vectors and complete or
minimal systems to zeta zeros.  This supplies legitimate analytic machinery,
but not the missing positivity or self-adjoint realization.

## 3. Function-field/Hodge-index target

Weil's curve-over-finite-fields proof has three structural ingredients:
Frobenius correspondences, a trace/intersection formula, and a Hodge-index
inequality.  The number-field analogue should be stated as a package rather
than invoked as analogy.

### FF-a (restricted arithmetic Hodge package)

Construct a real vector space `Corr_zeta`, a linear map `D` from the compactly
supported RHBridge test core, and a symmetric intersection pairing `I` such
that, without RH,

1. `D(f * f^*)` is defined using prime powers and the archimedean place;
2. the exact explicit-formula identity gives
   `Q(f,g) = -I(D(f), D(g))` (with the sign fixed once);
3. `D` is compatible with convolution/involution and support exhaustion;
4. the degree-zero subspace containing all `D(f)` satisfies the restricted
   Hodge inequality `I(X,X) <= 0`;
5. equality rigidity (`I(X,X)=0` only for the geometrically trivial class)
   supplies window nondegeneracy.

This restricted package is enough; a full theory of an arithmetic surface is
not logically required.  It is nevertheless stronger than a cosmetic
reformulation because `D`, `I`, and the Hodge inequality must be defined and
proved independently of the Weil form.

### FF-b (semilocal descent target)

For a finite set `S` of places containing infinity, seek an unconditional
positive trace form `T_S` and an exact decomposition

    Q_a = T_S + R_{S,a}

on the fixed support window, where `R_{S,a}` is explicitly controlled and tends
to zero monotonically (or is itself positive) as `S` exhausts the primes.
Connes--Consani identify the archimedean/Sonin positivity mechanism and state
that the framework extends semilocally, but the general semilocal positivity is
the RH-relevant gap.  A sign-controlled remainder theorem would be a real
intermediate result; merely proving `R_{S,a} -> 0` without a lower bound is not,
because the RHBridge margins collapse.

## 4. Hidden-RH audit for the function-field route

| Proposed assumption | Audit |
|---|---|
| "There is a number-field Frobenius with the zeta zeros as eigenvalues" | If Frobenius purity/self-adjointness is included, RH is already encoded. |
| Exact intersection identity plus Hodge negativity on all zeta test classes | This proves Weil positivity directly; useful as a geometric reduction, but not a weaker consequence. |
| Standard conjecture of Hodge type for a genuinely constructed zeta motive | Potentially a meaningful conjectural implication, but existence of that motive and the trace identity are presently additional major assumptions. |
| Function-field RH or Deligne purity alone | Does not transfer to the number field; an explicit comparison/functor is required. |
| Positivity at each finite set of places | Must include a uniform/exhaustion theorem.  Otherwise it does not imply global positivity. |

## 5. Recommended work order

1. Align the existing RHBridge kernel with Suzuki's continuous screw kernel on
   a fixed window, including the precise derivative/integration map between
   test spaces.  This is an unconditional identification lemma and gives access
   to canonical-system tools without assuming positivity.
2. Formalize an abstract `CanonicalRealizationPackage` whose fields correspond
   exactly to CS-a, and prove that it implies `PositiveAt a` and nondegeneracy.
   Keep the realization and zeta-identification hypotheses separate.
3. Attempt CS-b first at finite `a`: identify Suzuki's finite-interval operator
   with the window kernel and determine whether its self-adjointness is
   unconditional or depends on positivity of that kernel.
4. Treat FF-a as a longer-horizon conjectural interface.  Near-term work should
   target FF-b's remainder sign, because the repository already has the local
   prime/archimedean decomposition needed to state it exactly.

## Primary sources

* M. Suzuki, [Weil's quadratic form via the screw function](https://arxiv.org/abs/2606.09096), 2026 (preprint): continuous-kernel framework and finite-interval self-adjoint-operator conjecture.
* M. Suzuki, [Aspects of the screw function corresponding to the Riemann zeta-function](https://arxiv.org/abs/2206.03682), JLMS 2023: positivity/screw-function equivalents to RH and unconditional small-window results.
* J. B. Conrey and X.-J. Li, [A note on some positivity conditions related to zeta- and L-functions](https://arxiv.org/abs/math/9812166), IMRN 2000: obstruction to de Branges's proposed auxiliary positivity conditions.
* J.-F. Burnol, [Sur certains espaces de Hilbert de fonctions entieres...](https://arxiv.org/abs/math/0105120), 2001, and [Two complete and minimal systems associated with the zeros of the Riemann zeta function](https://arxiv.org/abs/math/0203120), J. Théorie des Nombres Bordeaux 2004: unconditional Sonine/de Branges structures attached to zeta zeros.
* A. Weil, [On the Riemann Hypothesis in Function-Fields](https://doi.org/10.1073/pnas.27.7.345), PNAS 1941: original function-field theorem.
* A. Connes and C. Consani, [Weil positivity and Trace formula, the archimedean place](https://arxiv.org/abs/2006.13771), Selecta Math. 2021: Sonin/trace positivity at the archimedean place and the semilocal program.
