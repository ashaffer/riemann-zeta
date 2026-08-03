# Non-Hilbert endpoint audit for prime-branch resonance

Status: the honest sieve endpoint is finite; renormalized endpoints are too
flexible to constrain zeros, 2026-08-01.

The proposed escape from the Walsh `L2` barrier was to measure prime
increments `p^(-beta)` in `ell^r` at or below the critical exponent

`r_c = 1/beta < 2`.

For a dense formal prime tree,

`sum_p |p^(-beta)|^r`

diverges when `beta r <= 1`, so this endpoint is genuinely invisible to
quadratic energy.  The question is whether it coexists with honest propagation
of the pole through arithmetic restrictions.

## Absolute pole preservation forces `ell^1`

Let primes be independently selected with probabilities `theta_p`, and let
the sieve multiplier be

`R_P(s)=product_(p in P)(1-p^(-s))^(-1)`.

To preserve a pole at `rho=beta+i gamma` by a nonzero analytic multiplier on
a neighborhood, the sparse-sieve construction imposes, for some `epsilon>0`,

`sum_p theta_p p^(-(beta-epsilon)) < infinity`.

Almost surely this gives absolute local convergence.  Since

`p^(-beta) <= p^(-(beta-epsilon))`, it also gives

`sum_(p in P) p^(-beta) < infinity`.

Thus the actual prime increments lie in `ell^1`, and hence in every `ell^r`
for `r>=1`.  In particular the critical `ell^(1/beta)` capacity is finite.
The random-sieve family of `RANDOM-SIEVE-RESONANCE-CAPACITY.md` falls exactly
under this theorem.

This strengthens the Walsh barrier: honest absolute propagation leaves no
Banach endpoint between `ell^1` and `ell^2` to exploit.

## Conditional or Wick-renormalized products do not constrain poles

One can force nontrivial subquadratic variation by centering the prime
increments, for example through a random analytic factor of the schematic
form

`M_epsilon(s)=exp(sum_p epsilon_p p^(-s))`,

with independent mean-zero signs.  The series converges almost surely in the
half-plane `Re(s)>1/2` in the usual locally uniform sense, while its
`ell^(1/beta)` variation is critical or divergent.  Multiplying any
meromorphic function by this nonzero analytic factor preserves every pole.

Therefore the following data are mutually compatible:

- a pole at any prescribed `rho` with `Re(rho)>1/2`;
- positive branch entropy;
- divergent non-Hilbert prime variation;
- a nonzero analytic random Euler multiplier.

This is a countermodel to any *generic* endpoint-capacity principle claiming
that those properties exclude an off-line pole.  The construction has lost
the decisive arithmetic feature: its coefficients are no longer a
positive-density restriction of Möbius, but a centered or renormalized
multiplicative perturbation.

The flexibility is consistent with the theory of Helson zeta functions,
where unimodular completely multiplicative Euler products can be built with
very broadly prescribed meromorphic zero and pole sets.  Euler-product form
plus subquadratic variation alone is therefore far too weak.

## Phase-balanced positive selections

A deterministic positive selection might try to make

`sum_(p in P) p^(-rho)`

converge conditionally by balancing the phases `exp(-i gamma log p)`, while
retaining divergent absolute endpoint mass.  Convergence at the single point
`rho` is insufficient: pole preservation requires a nonzero analytic
multiplier on an open neighborhood.  Phase balance tuned to `gamma` is not
uniform for nearby imaginary parts, and supplies no locally uniform Euler
product.  Assuming such a continuation separately simply imports the missing
analytic structure.

## Verdict

The non-Hilbert endpoint program is proven ineffective in its current form:

1. honest sparse arithmetic restrictions preserving the pole absolutely have
   finite `ell^1` variation;
2. dense centered/conditional constructions can have divergent endpoint
   variation but admit arbitrary poles and hence give no contradiction.

A revival would require an invariant tied to the *unrenormalized Möbius
coefficients* that is neither controlled by absolute sieve convergence nor
shared by flexible Helson-type Euler products.  Endpoint exponent alone is
not that invariant.
