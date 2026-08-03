# A compressed, orthogonal RH research portfolio

Status: roadmap after the fixed-window, CCM, stable-lift, passive-Euler, and
graphic-matroid audits; 2026-08-01.  This is a research program, not an RH
claim.

## 1. What the entire program has actually taught us

### One analytic obstruction wore many costumes

The localized Weil radical, Suzuki-kernel null vector, prime/archimedean
balance, Birman--Schwinger eigenvector, collar mode, CCM ground state, and
finite-window determinant defect are largely the same object in different
coordinates.  Translating among them was useful for normalization and for
finding counterexamples, but did not add independent equations.

### The small margin is structural

The localized ground energy collapses extremely rapidly.  Excellent `L2`
alignment does not imply graph-norm alignment: the CCM comparator reached
over `0.9998` overlap while its scale-free Feshbach ratio exceeded
`0.9999998`.  Any proof based on a uniform numerical gap, absolute
perturbation, or generic transversality is aimed at the wrong invariant.

### The completion cannot be assembled naively from primes

Local Euler factors have the wrong Nevanlinna orientation for a passive
factor-by-factor realization.  Likewise, the prime-shift graph has a positive
Laplacian, but the archimedean/pole residual is strongly indefinite and of
order one.  The completed global object is not a harmless local product plus a
small correction; the completion performs the decisive cancellation.

### Closed classes are valuable; equivalent certificates are not

Stable polarization of a Jensen polynomial, positivity of the universal
Schur complement, and Lorentzianity of a quadratic polynomial whose Hessian is
the Weil form are all equivalent ways of assuming the desired conclusion.
A useful structural class must be assigned by independent arithmetic or
geometric data and must be closed under the required infinite limit.

### One exceptional zero is the adversary

Density-one results, random-matrix statistics, almost-all short-interval
cancellation, and eventual Jensen hyperbolicity do not control a zero-density
exceptional set.  Every admitted path must explain how it detects one off-line
zero.

### The proper Bayesian unit is a load-bearing lemma

Long chains of correct setup barely update the chance of RH if their last
lemma is equivalent to RH.  We should attach priors to the first genuinely new
mechanism and test it before building surrounding infrastructure.

## 2. Admission rule for a new path

A path enters the portfolio only if it answers all five questions.

1. **New invariant:** what does it use besides the explicit formula?
2. **Exceptional sensitivity:** why does one off-line zero violate it?
3. **Completion:** where do the gamma factor and pole live natively?
4. **Closed limit:** what theorem carries finite/local objects to the global
   object without a collapsing constant?
5. **Kill test:** what calculation or lemma can reject the mechanism early?

## 3. Path A -- theta heat flow and a no-collision principle

### Independent invariant

The de Bruijn--Newman deformation

`H_t(z) = integral_0^infty exp(t u^2) Phi(u) cos(zu) du`

obeys a backward heat equation.  For `t` above the Newman threshold its real
zeros evolve by the repulsive Calogero--Moser/Dyson system

`x_k'(t) = 2 sum_(j != k) 1/(x_k-x_j)`.

Rodgers--Tao proved the threshold `Lambda >= 0`; RH is `Lambda <= 0`, hence
`Lambda=0`.  The new invariant is collision time under a parabolic flow, not a
Weil eigenvalue.

### Proposed cross-field mechanism

Use displacement-convex entropy and inverse-gap energies from Dyson gas and
optimal-transport theory, but with the exact modular theta kernel as boundary
data.  Since all zeros are real for sufficiently large `t`, failure before
zero must occur at a real double zero.  The minimal analytic target is:

> For every `t>0`, the two theta integrals `H_t(x)` and `partial_x H_t(x)`
> have no common real zero.

Rather than attack this as generic simplicity, seek a sum-of-squares or strict
Wronskian identity obtained from the modular relation for `Phi`.  A successful
identity would prevent the first collision and propagate real-rootedness all
the way to `t=0`.

### Why it might have been underexploited

The zero ODE has mostly been used in the direction proving `Lambda>=0`.
Optimal-transport convexity, renormalized Coulomb energy, and modern
many-particle gradient-flow estimates suggest different monotone quantities.
The arithmetic theta kernel is much more rigid than a general heat datum.

### Kill test

Compute the proposed Wronskian/inverse-gap candidates directly from the theta
integral over a grid of `t>0`.  A sign change kills that candidate immediately.
More fundamentally, determine whether modularity yields an identity stronger
than positivity of a kernel already known to be RH-equivalent.

### Prior

Chance of a new monotonicity or no-collision lemma: `8--15%`.  Conditional
chance that it reaches `Lambda<=0`: `10--20%`.  End-to-end: roughly `1--3%`.

## 4. Path B -- cyclotomic cohomology with an archimedean polarization

### Independent invariant

For smooth proper varieties over finite fields, topological Hochschild/cyclic
homology recovers the cohomological regularized-determinant description of the
Hasse--Weil zeta function.  Deninger's rational-Witt construction attaches
flows with prime periodic orbits to arithmetic schemes and meets the
Fargues--Fontaine curve locally.

The missing synthesis is a global cohomology object for `Spec Z` with:

- cyclotomic Frobenius at every finite prime;
- a genuine real/archimedean factor;
- a positive polarization;
- a determinant equal to completed xi.

If an infinitesimal Frobenius `Theta` satisfies

`Theta^* + Theta = 1`

on the middle cohomology under a positive pairing, every eigenvalue has real
part `1/2`.  This is the exact characteristic-zero analogue of the weight
argument, and the conclusion follows spectrally without small margins.

### Proposed cross-field mechanism

Form an adelic homotopy pullback from the local `TP/TC` objects, a rational-Witt
dynamical object, and a real cyclotomic or `C2`-equivariant archimedean object.
The product formula should be encoded by the gluing map rather than imposed as
an analytic correction.  Search for the polarization through cyclotomic
duality or a trace pairing in the resulting stable category.

This archimedean suggestion is not empty terminology: real topological
Hochschild homology `THR` is already defined for rings and schemes with
involution, and `THR(Z)` has been computed away from 2.  What is not known is
an identification of its real fixed-point data with the gamma factor or an
adelic gluing theorem of the required kind.

### Exceptional sensitivity and completion

One off-line zero would be an eigenvalue of `Theta` with the wrong weight and
would directly contradict the adjoint relation.  Gamma and pole terms must be
determinants of the archimedean and degree-zero/two pieces, respectively.

### Kill test

Before constructing a global theory, test the local-to-global determinant in
the simplest object `Spec Z`: can the known finite-prime `TP` determinants and
a candidate real factor reproduce the completed functional equation without
inserting xi by hand?  If not, stop.  If yes, the next gate is whether the
duality pairing is positive rather than merely perfect.

### Prior

Chance of a coherent new global cohomological object: `3--8%`; conditional
chance its polarization proves RH: `15--30%`; end-to-end: `0.5--2%`.  This is
the deepest and slowest path, but the one most analogous to successful proofs
over finite fields.

## 5. Path C -- relative cyclic/KK index on the adele-class inclusion

### Independent invariant

Connes--Consani--Marcolli already realize the explicit formula on the cyclic
homology of the cokernel of the restriction from adele classes to ideles.  The
unresolved sign is a *relative* trace `Tr_X-Tr_Y`.  Modern relative index,
spectral-flow, and Kasparov machinery may encode that subtraction as a
fundamental class rather than as an indefinite analytic residual.

The target is a relative Fredholm/Krein cycle whose negative index equals the
number of off-critical zero pairs in a bounded spectral window.  Homotopy or
an assembly theorem would then force that index to vanish.

### Why this differs from the failed passive cascade

It is global from the start: local Euler factors are not required to be
passive.  The invariant is integer-valued and stable under compact
perturbations, so the collapsing Weil margin is irrelevant.

### Kill test

Quartet symmetry can make an ordinary signed index cancel even when off-line
zeros exist.  The first task is purely algebraic:

> Does the natural relative cycle produce an unsigned negative index, a
> `Z/2` obstruction, or only a net spectral flow that cancels on every zero
> quartet?

If it only gives net flow, kill the path.  If it counts negative squares, test
finite `S` stabilization and functoriality before attempting an index theorem.

### Prior

Chance the natural index survives the quartet-cancellation audit: `10--20%`;
end-to-end chance: `0.3--1%`.

## 6. Path D -- multiscale entropy forced by one off-line zero

### Independent invariant

This path uses multiplicativity and information flow across nested scales.
An off-line zero `rho=beta+i gamma` produces a coherent Mellin resonance.  The
needed new theorem is not average Chowla cancellation, but an inverse result:

> A single resonance with `beta>1/2` forces a positive-entropy tree of nested
> blocks carrying one persistent phase `n^(i gamma)`.

Entropy decrement and higher Fourier/Gowers uniformity could then force
Möbius to pretend to that phase, contradicting its prime-by-prime distance.

### Kill test

Derive the strongest unconditional nested-block consequence of one pole of
`1/zeta`.  If it guarantees only one branch or a polynomially vanishing
fraction of blocks, current almost-all results cannot see it and the route is
killed in its present form.  No general Chowla machinery should be developed
before this lemma passes.

### Prior

Chance that multiplicativity amplifies one resonance to positive entropy:
`3--8%`; end-to-end chance: `0.1--0.5%`.

## 7. Path E -- a nonexchangeable Lee--Yang model as a scout

### Independent invariant

The failed Jensen stable lift was symmetric and therefore tautological.  A
different possibility is an independently defined prime-indexed ferromagnetic
or strongly-Rayleigh model whose partition function specializes to a finite
xi approximant.  Lee--Yang stability would then be inherited from interaction
signs rather than inferred from the zeros.

The variables should index primes or prime powers, not Taylor degree.  The
gamma factor must arise as a boundary field, and Poisson summation as a duality
of the model.  This is a statistical-mechanical realization of the completion,
not a polarization of the Jensen polynomial.

### Kill test

Match the first few exact coefficients and test the Griffiths/Rayleigh
inequalities forced by ferromagnetism.  Euler/Mobius inclusion--exclusion is
likely to produce frustrated or antiferromagnetic signs.  One violated
inequality kills the natural model cheaply.

### Prior

Chance of a nontrivial exact model: `2--6%`; end-to-end below `0.5%`.  Its
value is the low cost of rejection and the possibility of discovering an
unexpected exact duality.

## 8. Portfolio execution order

### Sprint 1: four fail-fast gates

1. **Heat flow:** derive and numerically stress-test candidate Wronskian or
   collision-energy signs from the exact theta kernel.
2. **Relative index:** calculate the contribution of one abstract off-line
   quartet and determine whether the natural index cancels.
3. **Entropy:** quantify the block density forced by one hypothetical pole of
   `1/zeta`.
4. **Lee--Yang:** test necessary correlation inequalities for the first
   prime-indexed coefficient models.

Each gate should take days, not months.  Failures are recorded as theorems or
countermodels.

### Sprint 2: invest only after a gate passes

- If heat-flow signs survive, prove the identity analytically and connect it
  to first-collision exclusion.
- If the index counts rather than cancels, construct the finite-`S` relative
  cycle.
- If positive entropy is forced, import the precise multiplicative-function
  inverse theorem needed.
- If a Lee--Yang model survives, identify its duality and thermodynamic limit.

### Long-horizon track

Independently maintain a concise specification for Path B: the determinant,
duality, and archimedean gluing axioms.  Do not build general cohomological
machinery until the `Spec Z` local-to-global determinant test works.

## 9. Bayesian view

The five paths are orthogonal at their decisive steps: collision exclusion,
Frobenius weight, relative index, entropy amplification, and ferromagnetic
stability.  Their failure probabilities are therefore less correlated than
our earlier collection of Weil-form reformulations.

The present probability that this portfolio yields a complete RH proof is
still only about `1--3%`.  The probability of at least one genuinely new,
publishable structural result is closer to `30--50%`.  The correct strategy is
not optimism about any one path; it is rapid rejection of false mechanisms
followed by concentrated investment in the first mechanism that survives its
load-bearing gate.

## Primary literature anchors

- Rodgers--Tao, *The de Bruijn--Newman constant is non-negative*:
  https://arxiv.org/abs/1801.05914
- Hesselholt, *Topological Hochschild homology and the Hasse--Weil zeta
  function*: https://arxiv.org/abs/1602.01980
- Hesselholt--Nikolaus, *Topological cyclic homology*:
  https://arxiv.org/abs/1905.08984
- Dotto--Moi--Patchkoria--Reeh, *Real topological Hochschild homology*:
  https://arxiv.org/abs/1711.10226
- Hornbostel--Park, *Real topological Hochschild homology of schemes*:
  https://arxiv.org/abs/2209.12796
- Deninger, *Dynamical systems for arithmetic schemes*:
  https://arxiv.org/abs/1807.06400
- Alvarez Lopez--Kim--Morishita, *Regularized determinant formulas for the
  zeta functions of 3-dimensional Riemannian foliated dynamical systems*:
  https://arxiv.org/abs/2410.20758
- Connes, *Trace formula in noncommutative geometry and the zeros of the
  Riemann zeta function*: https://arxiv.org/abs/math/9811068
- Connes--Consani--Marcolli, *The Weil proof and the geometry of the adeles
  class space*: https://arxiv.org/abs/math/0703392
- Connes--Consani, *Knots, primes and the adele class space*:
  https://arxiv.org/abs/2401.08401
- Matomaki--Radziwill, *Multiplicative functions in short intervals*:
  https://arxiv.org/abs/1501.04585
- Matomaki--Radziwill--Tao--Teravainen--Ziegler, *Higher uniformity of bounded
  multiplicative functions in short intervals on average*:
  https://annals.math.princeton.edu/2023/197-2/p03
- Borcea--Branden, *The Lee--Yang and Polya--Schur programs I*:
  https://arxiv.org/abs/0809.0401
