# Robin criterion: colossally abundant envelope audit

Status: second Nicolas--Robin fail-fast checkpoint; variational concavity proved
but shown insufficient to order the Robin score; 2026-08-01.

## 1. Exact exponent transitions

For `epsilon>0`, a colossally abundant number maximizes

`sigma(n)/n^(1+epsilon)`.

The optimization separates prime by prime.  Increasing the exponent of `p`
from `a-1` to `a` changes

`A(n)=log(sigma(n)/n)` by

`b_(p,a) = log((1-p^(-(a+1)))/(1-p^(-a)))`

and changes `L=log n` by `log p`.  The transition occurs at the exact slope

`epsilon_(p,a)=b_(p,a)/log p`.

Sorting all these slopes in decreasing order generates the colossally abundant
frontier: at an event, multiply the current integer by its event prime.

## 2. What the envelope proves

The points `(L,A)` lie on the upper variational envelope selected by supporting
lines `A-epsilon L`.  Its successive slopes are the decreasing values
`epsilon_(p,a)`.  Hence the polygonal interpolation of the colossally abundant
frontier is concave.  This is a genuine invariant absent from the primorial
sequence.

Robin's logarithmic score, however, is

`R(L)=A(L)-gamma-log log L`.

The barrier `log log L` is also concave.  The difference of two concave
functions has no prescribed monotonicity or sign.

At one exponent event the exact increment is

`Delta R = epsilon_(p,a) log p
           - [log log(L+log p)-log log L]`.

Thus its sign compares the envelope slope with a secant slope of the barrier.
Both slope sequences decrease, but no variational principle orders one against
the other.

## 3. Numerical structural test

`src/robin_ca_envelope_audit.py` generates exact transition parameters and
restricts output to a range complete with respect to its prime cutoff.  With
primes through `20,000`, the trusted range contains thousands of exponent
events.  Above `5040`, both signs of `Delta R` occur many times and the sign
changes repeatedly.

This rejects:

- monotonicity of the Robin score along the CA frontier;
- a single-crossing principle between envelope and barrier slopes;
- simple interlacing by exponent-transition type.

The computation does not test RH: sampled Robin margins remain below zero, as
expected.  It tests whether variational extremality itself supplies the missing
order law, and the answer is no.

## 4. Compression versus leverage

Colossal abundance gives an exact and valuable reduction: a Robin
counterexample can be sought on an extremal multiplicative frontier.  But the
frontier invariant controls the concavity of `A`, whereas RH requires the
vertical comparison `A<gamma+log log L`.  Concavity alone cannot control that
comparison because the target barrier shares the same curvature sign.

At local maxima of `R`, adjacent transition slopes bracket the barrier's
secant slope.  Restricting to these maxima prunes tests, but bounding their
heights remains exactly the Robin problem.  No integer gap helps: the score is
real-valued and its margin tends to zero.

## 5. Verdict

The two hoped-for discrete invariants have now been separated and rejected:

1. primorial append-one-prime monotonicity reduces to fine Chebyshev error and
   is conditionally false under Cramér;
2. colossally abundant envelope concavity is unconditional but does not order
   the difference from Robin's concave barrier.

Nicolas--Robin remains an elegant arithmetic compression, not an easier proof
engine under the structures audited here.  It should be demoted unless a new
invariant couples the envelope slope to the barrier height.  The next portfolio
candidate is the Nyman--Beurling--Báez-Duarte closure criterion, admitted only
for a fail-fast search for a non-Hilbertian dual or exact interpolation law;
ordinary `L2` approximation is already disfavored by our synthesis.

## Literature anchors

- G. Robin, *Grandes valeurs de la fonction somme des diviseurs et hypothèse
  de Riemann*, J. Math. Pures Appl. 63 (1984), 187--213.
- L. Alaoglu and P. Erdős, *On highly composite and similar numbers*, Trans.
  Amer. Math. Soc. 56 (1944), 448--469.
