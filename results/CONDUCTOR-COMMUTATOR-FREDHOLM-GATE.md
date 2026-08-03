# Burnol conductor--commutator global Fredholm audit

Status: local phase calculus verified; naive adelic/global Fredholm assembly
fails compactness, summability, and Fredholmness before any RH input;
2026-08-01.

## 1. Burnol's exact local operators

On `L2(K_v,dx)` let

`A_v=log|x|_v`, `B_v=F_v A_v F_v^(-1)`.

Burnol's conductor and commutator operators are

`H_v=A_v+B_v`, `K_v=i[B_v,A_v]`.

They commute with local dilations.  `H_v` is essentially self-adjoint and
bounded below; `K_v` is bounded and essentially self-adjoint.  Under the
multiplicative spectral transform their multipliers are respectively the
first and second logarithmic derivatives of the Tate--Gel'fand--Graev local
gamma factor.  Inversion commutes with `H_v` and anticommutes with `K_v`.

This is completion-native local phase information and is mathematically
stronger than a formal prime-kernel decomposition.

## 2. Finite-prime radial spectrum

On the unramified radial subspace of `L2(Q_p)`, Burnol identifies it with
`L2(S1)` and obtains multiplication operators.  Their spectra include

```
spec(H_p) = [-2 log(p)/(sqrt(p)-1),
              2 log(p)/(sqrt(p)+1)],

spec(K_p) = [-M_p,M_p],
```

where `M_p>0` and `M_p ~ 2 log(p)^2/sqrt(p)` as `p->infinity` (Burnol gives
the multiplier explicitly).

In particular, both spectra contain zero in their continuous spectrum.
Furthermore `K_p` vanishes on the ramified subspace.

### Consequences

1. A nonzero multiplication operator on the nonatomic space `L2(S1)` is not
   compact.
2. Therefore neither nontrivial radial `H_p` nor `K_p` belongs to any finite
   Schatten class.
3. The off-diagonal part of `K_p` with respect to the inversion grading is not
   Fredholm, because zero lies in its essential spectrum.
4. The bounded transform of `H_p` is likewise non-Fredholm at zero.

Thus no local Fredholm index is available to sum over places.

## 3. Direct-sum assembly is noncompact

The norm of the unramified `K_p` block is asymptotic to

`2 log(p)^2/sqrt(p)`,

which tends to zero.  This is not enough for compactness of the Hilbert direct
sum: a direct sum is compact only when every component is compact and the
component norms tend to zero.  Every `K_p` component is already noncompact.

Consequently the direct-sum commutator is bounded but noncompact and has zero
in essential spectrum with infinite multiplicity.  It cannot be the compact
perturbation required for the proposed relative index.

## 4. Restricted-tensor-product sum is not defined on the vacuum

Let `eta_0` be the standard unramified radial vector.  Burnol's matrix entries
give the exact local fluctuations

```
||H_p eta_0||^2 = 2 log(p)^2/(p-1),

||K_p eta_0||^2
 = 2 log(p)^4 sum_(j>=1) j^2 p^(-j)
 = 2 log(p)^4 p^(-1)(1+p^(-1))/(1-p^(-1))^3.
```

Hence

`sum_p ||H_p eta_0||^2` and `sum_p ||K_p eta_0||^2`

both diverge.  Their leading growth is governed respectively by sums of
`log(p)^2/p` and `log(p)^4/p`.

Therefore the formal operators `sum_p H_p` and `sum_p K_p` do not act on the
natural restricted-tensor-product vacuum without a new renormalization and
domain construction.  The diagnostic
`src/conductor_commutator_summability.py` displays this divergence by prime
cutoff.

## 5. What Burnol's sum over places actually means

The global explicit formula sums **local distributional expectation values**
after inserting a compactly supported multiplicative test function.  For each
fixed support only finitely many prime powers contribute directly, and the
archimedean/pole terms complete the identity.

This is not the spectral trace of an already-existing operator
`sum_v H_v` on one adelic Hilbert space.  Passing from the distributional sum
to a global operator requires precisely the summability and domain theorem
that fails for the naive tensor/direct-sum constructions above.

## 6. Renormalization does not automatically preserve an index

One can subtract vacuum expectations or insert prime-dependent weights to
make some sums converge.  Neither operation currently helps:

- the vacuum expectations of the commutators already vanish, while their
  variances diverge;
- any nonzero scalar multiple of a local radial multiplier remains
  noncompact;
- weights strong enough to give Schatten summability alter the explicit
  formula and have no demonstrated relation to the zeta screw index;
- negative index is not additive under the prime/archimedean completion.

A cutoff family also does not define a stable index: zero belongs to the
essential spectrum at every local stage, so ordinary Fredholm spectral flow
is undefined without opening a gap.

## 7. Scattering/Toeplitz alternative

The local unitary `F_v I_v` has the Tate gamma factor as multiplier, suggesting
a Toeplitz index after choosing a Hardy polarization.  Locally this measures
winding of a gamma/Euler phase.  Globally, however, the infinite product of
local phases is not defined on the critical boundary without the completed
zeta regularization.  Once regularized, its inner factor records the zeta
zeros and its Toeplitz index is the argument-principle count already found in
the Nyman and Nevanlinna audits.

This remains useful conceptual alignment, but not an independent arithmetic
index computation.

## 8. Gate verdict

The conductor commutator is a genuine local phase operator, but the proposed
global Fredholm bridge fails at the operator-assembly level:

- local blocks are noncompact and non-Schatten;
- zero lies in continuous essential spectrum;
- the inversion-graded block is non-Fredholm;
- direct sums remain noncompact;
- tensor sums have divergent vacuum fluctuations;
- the available global sum is distributional, not operator-theoretic;
- the scattering alternative returns zero counting after regularization.

Path 2 is therefore **demoted in its naive global-index form**.  A future
revival would require a new relative polarization or semifinite index theory
whose trace is proved compatible with the explicit formula; merely
renormalizing the local sums is not enough.

The next independent checkpoint is Path 3: Burnol's complete-minimal Sonine
zero systems and their biorthogonal reflection pairing.  It should be tested
first on a finite off-line quartet to determine whether the desired positivity
is automatic, false, or exactly Weil positivity.

## Literature anchor

- J.-F. Burnol, *The Explicit Formula and the conductor operator* (1999),
  especially Theorems E2, E3, F1--F3 and the local gamma spectral transform.
