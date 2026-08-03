# Orthogonal portfolio: sprint-1 gate audit

Status: first-pass pruning, 2026-08-01.  Numerical observations are explicitly
separated from proofs and structural obstructions.

## A. Theta heat-flow gate: survives, but only weakly

For the de Bruijn--Newman flow

`H_t(x) = integral_0^infty exp(t u^2) Phi(u) cos(xu) du`,

the first candidate is the Laguerre expression

`L_t(x) = H_t'(x)^2 - H_t(x) H_t''(x)`.

Strict positivity at real `x` excludes real double zeros.  Since all zeros are
real for sufficiently large `t`, exclusion of double zeros for every `t>0`
would prevent the first collision before zero and prove `Lambda<=0`.

There is an exact identity, obtained by symmetrizing the two products:

`L_t(x) = (1/4) double_integral a_t(u)a_t(v) *`

`  ((u+v)^2 cos(x(u-v)) + (u-v)^2 cos(x(u+v))) du dv`,

where `a_t(u)=exp(tu^2)Phi(u)`.  This is not manifestly positive.  Thus any
proof must use special modular/theta structure; positivity of `Phi` alone does
not settle the sign.

The script `src/xi_heat_laguerre_scan.py` evaluated `H_t` and its first two
derivatives by oscillatory quadrature.  On

`0 <= t <= 0.5`, `0 <= x <= 80`,

the expression remained positive.  The smallest scale-normalized value was
about `0.173`.  This passes a falsification test but mostly lies in the region
controlled by already verified low zeta zeros.  It is not evidence that the
sign holds at all heights.

**Decision:** retain.  Next gate: derive a modular decomposition of the double
integral into positive pieces, or find a high-height sign failure with
certified oscillatory quadrature.

**Subsequent result (2026-08-01):** the first Laguerre density is the Fourier
transform of an explicit nonnegative convolution density.  The tempting
Polya-convexity proof is structurally impossible for a nonconstant smooth even
density, and the density's exact heat PDE has sign-indefinite forcing, so an
elementary maximum principle also fails.  See
`THETA-LAGUERRE-CONVOLUTION-AUDIT.md` and
`THETA-HEAT-EVOLUTION-AUDIT.md`.  Retain only the genuinely modular/nonlocal
subpath.

**Further result:** modularity's concrete role is all-order cancellation of
odd boundary jets.  Any half-line kernel with a first nonzero odd boundary
jet has an algebraic Fourier tail whose Laguerre density is eventually
negative.  This proves that individual theta summands and generic finite
truncations cannot work.  See `THETA-BOUNDARY-JET-CANCELLATION.md`.

## B. Relative-index gate: ordinary index is pruned

Let an off-line zero be

`rho = 1/2 + delta + i gamma`, `delta != 0`.

Functional equation and conjugation generate the quartet

`1/2 +/- delta +/- i gamma`.

In the centered spectral coordinate its points are `+/- gamma +/- i delta`.
Any natural signed crossing number or spectral-flow contribution which is odd
under complex conjugation sums to zero on this quartet: there are two points
above and two below the real axis.  Thus an ordinary Fredholm/KK index can
vanish even when RH fails.

An unsigned upper-half-plane count would detect two points, but it is not the
ordinary homotopy-stable signed index.  A Pontryagin negative-square index can
detect them, but establishing that index is precisely a global kernel
positivity problem closely related to the Weil/Suzuki criterion.

**Decision:** prune ordinary relative spectral flow as an independent route.
Retain only if the cyclic-homology relative cycle canonically produces a
negative-square count rather than net flow; no such mechanism is currently in
hand.

## C. Entropy gate: one-scale abundance, no nesting

Suppose a hypothetical zero forces, along some sequence of `X`,

`|M(X)| >= c X^beta`, with `beta>1/2`.

Partition `[1,X]` into `N=X/H` blocks with sums `B_j`, so `|B_j|<=H`.  Put

`theta=(c/2)X^(beta-1)`.

If `k` blocks satisfy `|B_j|>=theta H`, the triangle inequality gives the sharp
elementary lower bound

`k >= (c/2) X^beta/H`, hence `k/N >= (c/2)X^(beta-1)`.

Thus a global resonance forces polynomially many weakly biased blocks at each
chosen scale, but their fraction and normalized bias both tend to zero.  The
argument supplies neither a common phase nor nesting of the exceptional
blocks.  Almost-all short-interval cancellation is compatible with this
conclusion.

There can still be a positive *fractal dimension* of exceptional blocks when
`H=X^alpha`, but converting separate one-scale sets into one coherent tree is
exactly the missing theorem; it does not follow from the pole alone.

**Decision:** downgrade but do not fully kill.  The next and only worthwhile
target is a multiplicative nesting lemma.  Do not import general entropy or
Chowla machinery unless such a lemma is found.

**Subsequent result (2026-08-01):** multiplicativity gives an exact
phase-coherent tree under squarefree dilations, and the restricted Euler
product proves that an off-line pole survives every fixed finite sequence of
prime exclusions.  But each generation is confined to channels of density
`phi(q)/q^2`, with no uniform control as the depth grows.  Formal branch count
does not become positive-measure entropy.  See
`MOBIUS-MULTIPLICATIVE-NESTING-AUDIT.md`.  Prune unless a new
coprimality-stability theorem retains a uniform fraction of the bias.

**Further result:** for primorial depth, channel density is `exp(-y+o(y))`,
whereas the Euler residue multiplier and the number of formal branches are
only `exp(o(y))`.  Hence even their optimistic aggregate tends to zero.
See `MOBIUS-PRIMORIAL-DEPTH-BOUND.md`.  This prunes the natural
positive-density version of the nesting route.

**Alternative-density result:** sparse independent prime exclusions with
probability `p^(-a)`, `1-beta<a<1`, produce positive-density sifted sets with
positive entropy per typical multiplicative scale, and almost every restricted
Möbius Dirichlet series retains the hypothetical pole.  However, the pole's
Euler-multiplier increments are always square-summable because `2 beta>1`.
Thus the selector entropy carries only finite total Walsh pole energy.  See
`RANDOM-SIEVE-RESONANCE-CAPACITY.md` and
`RANDOM-SIEVE-WALSH-BARRIER.md`.  This closes the quadratic entropy route;
only a genuinely non-Hilbert endpoint invariant could reopen it.

**Endpoint result:** in every honest sparse sieve with absolute Euler
convergence on a neighborhood of the pole, the selected prime increments are
already `ell^1`; the proposed `ell^(1/beta)` endpoint is therefore finite.
Centered or conditionally renormalized dense Euler products recover divergent
endpoint variation but can coexist with arbitrary prescribed poles and are no
longer Möbius restrictions.  See `NONHILBERT-ENDPOINT-AUDIT.md`.  The endpoint
exponent by itself is pruned.

**Additive--multiplicative invariant result:** the aligned rectangle
`mu(n)mu(n+h)mu(pn)mu(pn+ph)` collapses to a squarefree-pair indicator.  The
true operator commutator using `pn+h` instead has exact all-shifts aggregate
`S(S-S_p)`, so a pole can force size `N^(2 beta)`; however this is spread over
`O(N)` shifts and is compatible with every known qualitative `o(N)`
correlation estimate.  See `ADDITIVE-MULTIPLICATIVE-COMMUTATOR-AUDIT.md`.
The proposed cocycle is pruned unless a new shift-concentration mechanism is
found.

## D. Prime Lee--Yang gate: the naive model is pruned

A finite local bosonic Euler factor is a truncated geometric polynomial

`1+z+...+z^K`,

whose nontrivial zeros lie on `|z|=1`.  Taking `z=p^(1/2-s)` would put those
zeros on the critical line.  But the arithmetic Euler factor is

`(1-p^(-s))^(-1) = (1-p^(-1/2) p^(1/2-s))^(-1)`.

The required coefficient `p^(-1/2)` moves the local singularity away from the
Lee--Yang unit circle.  Removing it changes the von Mangoldt weights and gives
the wrong Dirichlet series.  Finite independent-prime products either have no
zeros (the reciprocal Euler factors) or have local circle zeros for a shifted,
incorrect arithmetic function.  The gamma completion cannot be represented
as a harmless boundary field that repairs this mismatch.

**Decision:** prune independent or finitely occupied prime gases.  A genuinely
interacting global model remains logically possible, but it must derive both
the factors `p^(-k/2)` and the gamma term from an independently ferromagnetic
Hamiltonian.  Without such a Hamiltonian, “Lee--Yang model for xi” is just a
stable lift in new language.

## E. Cyclotomic gate: superseded by connectivity audit

The proposed archimedean object is not entirely speculative.  Real
topological Hochschild homology `THR` exists for rings and schemes with
involution; `THR(Z)` has been computed away from 2, and equivariant descent is
available.  Combined with Hesselholt's finite-field determinant theorem and
Deninger's rational-Witt arithmetic flows, this gives three real pieces of a
possible construction:

1. finite-prime cyclotomic Frobenius (`TP/TC`);
2. an arithmetic flow with prime periodic orbits (`W_rat`);
3. genuine `C2`-equivariant real Hochschild data (`THR`).

No known theorem glues them adelically, identifies the real fixed-point
determinant with the gamma factor, or supplies a positive polarization.  These
are real missing constructions, not consequences of existing formalism.

**Decision:** retain as the long-horizon path.  First gate: calculate whether a
candidate `THR(Z)` fixed-point determinant can even have the pole/gamma shape
of completed zeta.  Do not attempt general cohomology before that calculation.

**Subsequent result (2026-08-01):** this gate failed.  The positive-degree
summands of `THR(Z)` away from 2 are torsion and vanish after complexification;
they cannot supply the formal one-sided complex ladder whose determinant is
the gamma factor.  See `CYCLOTOMIC-CONNECTIVITY-AUDIT.md`.  A separate
archimedean cohomology can reproduce gamma, but then the proposed unified
native realization and its evidentiary advantage are gone.

## Sprint verdict

- **Survive:** theta no-collision; cyclotomic/real cohomology.
- **Narrow survivor:** multiplicative nesting/entropy.
- **Pruned:** ordinary relative spectral flow; independent-prime Lee--Yang
  gas.

The original allocation below has now been superseded: the naive cyclotomic
ladder and pole-plus-multiplicativity nesting mechanism both failed their next
gates.  Remaining effort should concentrate on a genuinely modular, nonlocal
theta identity; the other paths require a new invariant before re-entry.

## Additional primary sources

- Dotto--Moi--Patchkoria--Reeh, *Real topological Hochschild homology*:
  https://arxiv.org/abs/1711.10226
- Hornbostel--Park, *Real topological Hochschild homology of schemes*:
  https://arxiv.org/abs/2209.12796
