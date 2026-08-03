# Möbius multiplicative-nesting audit

Status: an exact coherent tree exists, but its density loss prevents the
proposed entropy amplification, 2026-08-01.

Fix a logarithmic frequency `gamma` and write

`f_gamma(n) = mu(n) n^(-i gamma)`.

For every squarefree `q`, multiplicativity gives the exact dilation law

`f_gamma(qn) = mu(q) q^(-i gamma) f_gamma(n)` when `(n,q)=1`,

and `f_gamma(qn)=0` otherwise.  Consequently, for every finite interval `I`,

`sum_((n,q)=1, n in I) f_gamma(qn)`

` = mu(q) q^(-i gamma) sum_((n,q)=1, n in I) f_gamma(n)`.

This is genuine phase-coherent nesting.  Products of distinct primes produce
a Boolean family of dilated descendant channels, with their phases fixed by
the prime factors rather than chosen after observing the sums.

## The density obstruction

The descendants occupy only multiples of `q`, and the exact identity further
removes base points sharing a prime with `q`.  Their ambient relative density
is asymptotically

`(1/q) product_(p|q) (1-1/p) = phi(q)/q^2`.

If `q` is a product of selected primes, this loss is multiplicative at every
level.  Even before demanding disjoint descendants, the total density of all
channels indexed by subsets of primes `p_1,...,p_k` is bounded by

`product_(j=1)^k (1 + (p_j-1)/p_j^2)`.

This grows only like a power of `log p_k`; it is not the exponential mass
needed for a positive-entropy tree.  Counting `2^k` formal branches therefore
confuses combinatorial branch count with occupied density.  For large primes,
each new binary choice contributes roughly `1/p`, not one bit of information
at positive measure.

There is, however, a genuine finite-depth propagation theorem.  For fixed
squarefree `q`, the coprime Dirichlet series is exactly

`sum_((n,q)=1) mu(n)n^(-s)`

` = zeta(s)^(-1) product_(p|q) (1-p^(-s))^(-1)`.

Therefore every zero `rho` of `zeta` remains a pole of the restricted series;
none of the finite Euler multipliers vanishes.  If the zero is simple, its
residue is multiplied by

`product_(p|q) (1-p^(-rho))^(-1)`.

So a resonance survives every *fixed finite* sequence of prime exclusions.
This is stronger than a pigeonhole statement and establishes coherent
finite-depth branching.

What is missing is uniformity when `q=q(X)` gains more prime factors as the
scale grows.  The Euler multiplier has no scale-independent lower bound from
the pole alone, while the occupied density `phi(q)/q^2` collapses
multiplicatively.  Fixed-depth persistence therefore does not imply a
positive-entropy infinite tree.

## Verdict

Multiplicativity supplies phase coherence and the pole supplies finite-depth
persistence, but neither supplies abundance uniformly in depth.  Combining
them yields a sparse coherent tree, not yet a positive-entropy tree.  Thus the
proposed implication

`one off-line zero => positive-density nested biased blocks`

does not follow from the present estimates.

The branch should be pruned unless one can prove a genuinely new
coprimality-stability estimate for the resonant Möbius sum.  Such an estimate
must retain a scale-independent fraction of the bias under many successive
prime exclusions; merely averaging over divisors or invoking qualitative
Chowla does not suffice.
