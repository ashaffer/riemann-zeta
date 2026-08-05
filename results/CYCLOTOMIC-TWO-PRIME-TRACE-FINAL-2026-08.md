# Cyclotomic two-prime trace gate: final audit

Status: narrow finite one-trace gate closed, 2026-08-04.  The general
cyclotomic/global-cohomology path remains open but unconstructed.  No RH claim
is made.

## Verdict

Cyclotomic homology gives a genuine cohomological determinant for each
finite-field local zeta function.  It does **not** currently give a connected
global object for `Spec Z` whose trace simultaneously has

- the pure prime-power von Mangoldt coefficients;
- no mixed `p^a q^b` primitive coefficients;
- the archimedean gamma ladder; and
- an independent positive polarization.

The exact two-prime calculation closes only a narrow architecture.  Direct
sums recover the Euler product but contain no cross-place geometry.  Ordinary
tensor/Fock constructions contain mixed raw states, but their connected
logarithm can remove those products exactly.  That is not an obstruction if a
positive Hilbert pairing is constructed separately from the signed connected
trace, as it is in the function-field paradigm.

What fails is the demand that one finite commuting linear trace both retain
all pure moments and kill every raw mixed moment.  No tested construction yet
supplies the global real realization and compatible polarization, but the
two-prime calculation does not prove that an infinite, derived, graded, or
noncommutative construction is impossible.  The path is parked for resource
allocation, not mathematically pruned.

## 1. What works locally

For a prime `p`,

```text
Z_p(s) = (1-p^(-s))^(-1),
-Z_p'(s)/Z_p(s) = sum_(k>=1) log(p) p^(-ks).
```

Hesselholt constructs the finite-field Hasse--Weil zeta function as a
regularized determinant on periodic topological cyclic data.  This is real
cohomological content, not decorative categorification.  See
[Hesselholt, *Topological Hochschild homology and the Hasse--Weil zeta
function*](https://arxiv.org/abs/1602.01980).

For two primes, the direct-sum object

```text
T_p direct-sum T_q
```

has additive logarithmic trace and hence recovers exactly

```text
sum_(k>=1) log(p) p^(-ks) + sum_(k>=1) log(q) q^(-ks).
```

It has no mixed term for the tautological reason that the two sectors are
orthogonal summands.  This is precisely the ordinary Euler-product assembly
already available analytically.

## 2. The mixed-trace obstruction

For a genuine tensor gluing, multiplicativity gives

```text
Str(F_p^a tensor F_q^b)
  = Str(F_p^a) Str(F_q^b).
```

Thus nonzero pure traces produce mixed `p^a q^b` raw states.  Those states are
not present as connected terms in the logarithmic derivative of the zeta
Euler product.  This observation by itself is harmless: for example,

```text
Z(z_p,z_q)=1/((1-z_p)(1-z_q))
```

has mixed states in `Z`, while `log Z` is exactly the sum of the two pure
connected series.

There is also a finite-dimensional all-orders no-go.  Let `U_p,U_q` be
commuting invertible matrices and `L` a trace or supertrace.  If

```text
L(U_p^a U_q^b)=0  for every a,b>=1,
```

then Cayley--Hamilton expresses the identity as a polynomial in strictly
positive powers of either invertible matrix.  It follows that every pure
moment and `L(1)` also vanish.  A finite shared-Frobenius object therefore
cannot retain all pure Euler moments while deleting every mixed moment.

The plethystic logarithm or Witt ghost primitives do delete disconnected
products.  Their output is a connected, generally signed cumulant.  It cannot
serve as a positive metric by itself, but a successful theory need not ask it
to: the polarization may be a separate structure.

This exposes a reusable design principle, not a universal no-go:

> Do not infer positivity of the connected Lefschetz trace from the Hilbert
> pairing.  A successful cohomology must specify the signed trace and the
> positive polarization as two compatible roles, even if both arise from one
> underlying object.

## 3. Cross-prime and real-place failures

In the Nikolaus--Scholze formalism a cyclotomic spectrum carries structure
maps `phi_p:X -> X^(tC_p)` for all primes.  These cyclotomic maps are not, by
the axioms alone, the geometric Frobenii on finite-field fibers of `Spec Z`,
nor do they assemble the corresponding Euler factors and real place.  The
formalism therefore clarifies the available structure but does not by itself
manufacture the required global arithmetic Frobenius or real realization
([primary source](https://arxiv.org/abs/1707.01799)).

Morin's construction relates topological cyclic homology and determinant
lines to special zeta values at integers.  The real place is supplied through
a separate Weil--etale/archimedean complex, not by a global positive
Frobenius object whose spectrum is the nontrivial zeta zeros
([Morin](https://arxiv.org/abs/2011.11549)).  From the disappearance of the
relevant positive-degree torsion after rational/complex realization in the
computed real topological Hochschild homology of the integers, we infer that
this object does not itself expose the infinite gamma ladder; the paper does
not state that gamma conclusion
([Dotto et al., especially Theorem 5.27](https://arxiv.org/abs/1711.10226)).

## 4. Final classification

| Construction | Pure local coefficients | No mixed primitives | Gamma place | Positive exclusion engine |
|---|---:|---:|---:|---:|
| direct sum over primes | yes | yes | separate insertion | no new engine |
| tensor/Fock plus connected logarithm | yes | yes after connected extraction | absent | separate pairing possible, not constructed globally |
| plethystic logarithm alone | yes | yes | absent | signed cumulant, not itself a metric |
| current THH/TC special-value theories | at fixed places/integers | not a global trace | separate complex | no zero-locating polarization |

The direct-sum construction rephrases the known Euler product and gives no new
geometry.  The finite commuting one-trace architecture is impossible.  The
more appropriate connected-trace-plus-separate-polarization architecture
survives conceptually, but no current construction provides its all-prime
comparison, canonically integrated archimedean realization, adjoint law, and
zero-locating spectrum.
It remains a long-horizon open program rather than a rapid RH strategy.
