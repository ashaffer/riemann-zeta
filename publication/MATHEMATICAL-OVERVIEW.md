# Mathematical overview

## 1. The strongest present conclusion

Let

```text
H_a = L²([-a,a], ℝ)
```

with each vector extended by zero to the real line.  In mathlib's
ordinary-frequency Fourier convention, write `fHat` for that zero extension's
Fourier transform and set

```text
D_a = {f in H_a : integral log(1 + (2*pi*xi)^2) |fHat(xi)|² dxi < infinity}.
```

The repository defines on `D_a` the arithmetic compact-support Weil form

```text
Q_a(f) = pole_a(f) + arch_a(f) - prime_a(f),
```

where

```text
pole_a(f)  = 2 <f, exp(x/2)> <f, exp(-x/2)>,

arch_a(f)  = integral
               (Re digamma(1/4 + i*pi*xi) - log(pi)) |fHat(xi)|² dxi,

prime_a(f) = sum over log(n) < 2a
               2 Lambda(n)/sqrt(n) * integral f(x) f(x + log(n)) dx.
```

The sum is finite because `f` and its translate have disjoint support once
`|log n| >= 2a`.

At

```text
a = 7/16                         (L = 4a = 7/4 in the program convention),
```

the only active prime power is `n=2`.  Lean proves that the general arithmetic
form is exactly the previously certified prime-2 time-domain form and proves,
for every nonzero `f in D_(7/16)`,

```text
(22699 / 10^9) ||f||² < Q_(7/16)(f).
```

The principal declarations are

- `RHP2Bridge.GeneralZetaWeilForm.weilForm_seven_sixteenths`;
- `RHP2Bridge.GeneralZetaWeilForm.weilForm_seven_sixteenths_strict_lower_bound`.

They are in
[`GeneralZetaWeilForm.lean`](../lean/rhbridge/RHBridge/GeneralZetaWeilForm.lean),
and the focused
[`GeneralZetaWeilFormAudit.lean`](../lean/rhbridge/RHBridge/GeneralZetaWeilFormAudit.lean)
reports only Lean/mathlib's standard logical axioms.

This is a local theorem about a precisely defined arithmetic form.  It is not
a theorem about all support sizes and is not RH.

| Theorem-card field | Record |
|---|---|
| Evidence class | Lean theorem |
| Scope | Real `L²` vectors supported in `[-7/16,7/16]` and lying in the logarithmic form domain |
| Bound | Strict lower bound `22699/10^9` times the squared norm |
| Formal trust base | The standard axioms printed by `GeneralZetaWeilFormAudit.lean`; no project literature axiom |
| Semantic boundary | Arithmetic pole–archimedean–prime form, not yet the formally proved zero-side sum |
| Nearest nonclaim | No positivity conclusion for arbitrary support and no RH conclusion |
| Focused check | `cd lean/rhbridge && env LEAN_NUM_THREADS=1 lake env lean RHBridge/GeneralZetaWeilFormAudit.lean` |

## 2. Why the logarithmic domain matters

The archimedean multiplier grows like `log(1+xi²)`.  Consequently the Weil
form is not an everywhere-defined bounded quadratic form on plain `L²`.
Putting the logarithmic Fourier weight into the domain is therefore not a
technical embellishment: it is the natural form domain.

[`GeneralZetaWeilForm.lean`](../lean/rhbridge/RHBridge/GeneralZetaWeilForm.lean)
proves that this domain is closed under zero, addition, and real scalar
multiplication and packages it as a real submodule.  The theorem at `a=7/16`
is stated on this full intrinsic domain, not merely on smooth vectors or a
finite Galerkin space.

## 3. The proof architecture behind the endpoint

The final inequality is short only because several independent mathematical
reductions have already been proved.

### 3.1 Fourier and interval geometry

The interval vector is extended by zero, transformed in `L²`, and related to
its time-domain autocorrelation by Plancherel.  This fixes every factor of
`2*pi` and converts the prime term into a translation correlation rather than
an unexplained matrix entry.

Relevant reusable modules include

- [`IntervalZeroExtension.lean`](../lean/weilcert/IntervalZeroExtension.lean);
- [`AutocorrelationPlancherelCore.lean`](../lean/rhbridge/RHBridge/AutocorrelationPlancherelCore.lean);
- [`AutocorrelationPlancherel.lean`](../lean/rhbridge/RHBridge/AutocorrelationPlancherel.lean).

### 3.2 Archimedean analysis

The real part of the digamma function is represented by a positive Gauss
integral and bounded by explicit logarithmic weights.  This turns the
archimedean contribution into a controlled Fourier multiplier and supplies
the comparison needed by the full-space transfer.

The general special-function content is isolated in the `Glide` digamma and
Gamma modules; the prime-2 normalization is kept in downstream compatibility
modules.  The general package is useful independently of zeta.

### 3.3 Legendre decomposition and full-space transfer

Normalized Legendre polynomials provide a complete orthonormal basis on the
interval.  The proof separates a finite low-mode block from its orthogonal
complement.  Exact projection formulas, Fourier leakage estimates, pole
residuals, and a two-block coercivity inequality control the complement and
the cross term.  Thus positivity is transferred from a finite block to the
entire logarithmic form domain.

The key point is conceptual: finite-matrix positivity alone would only be a
Galerkin statement.  The complement and cross estimates are what make the
endpoint a full-domain theorem.

### 3.4 Exact finite arithmetic

The remaining finite block is represented by rational interval data.  An
exact `LDL^T` congruence and perturbation bound prove positivity for every real
matrix in the certified entrywise interval.  Lean checks the integer and
rational identities.  Generated files store witnesses; the reusable theorem
explaining why those witnesses imply positivity lives in the ordinary
certificate framework.

This separation is essential for readability:

```text
analytic reduction
    -> finite interval matrix
    -> generic certificate soundness theorem
    -> generated exact witness.
```

The generated witness is the last line of the argument, not the argument's
mathematical motivation.  See
[`CERTIFICATE-GUIDE.md`](CERTIFICATE-GUIDE.md) for the detailed trust ledger.

### 3.5 Exact specialization

Finally, Lean proves that at `a=7/16` the active-prime set is exactly `{2}`,
that its von Mangoldt coefficient agrees with the prime-2 normalization, and
that the pole and archimedean terms are definitionally the same as those in
the certified fixed-window form.  This prevents a positive certificate for a
surrogate normalization from being silently relabeled as a theorem about the
arithmetic Weil form.

## 4. Smaller supports

[`CertifiedBaseInterval.lean`](../lean/rhbridge/RHBridge/CertifiedBaseInterval.lean)
transports the same lower bound to `0 <= a <= 7/16` by nested zero extension.
The vector norm is preserved, and newly listed prime shifts lie beyond the
smaller support diameter, so their autocorrelations vanish.

This propagation currently depends on the explicitly declared standard lemma
`ActivationCancellation.intervalAutocorrelation_eq_zero_of_two_mul_le`.
That lemma says that compactly supported vectors have zero autocorrelation
after a translation by at least the support diameter.  It is consensus
analysis, but until it is proved in Lean the propagated theorem is properly
described as literature-conditional.  The endpoint theorem in Section 1 does
not have this dependency.

## 5. The zero-side bridge and the exact remaining gap

The classical Guinand--Weil explicit formula identifies the arithmetic form
with a transform sum over nontrivial zeta zeros.  The repository formalizes
substantial infrastructure toward that equality:

- local factorization of zeta at a nontrivial zero;
- the logarithmic-derivative principal part;
- the von Mangoldt Dirichlet series on the right half-plane;
- the completed-zeta gamma and reflected contour identities;
- weighted Fourier--Laplace `L¹`/`L²` facts and Plancherel;
- smooth compact-support transform decay;
- finite simple-pole contour machinery.

The global contour limit and the complete zero-sum equality are nevertheless
still imported through
[`GuinandWeilLiterature.lean`](../lean/rhbridge/RHBridge/GuinandWeilLiterature.lean).
For the logarithmic form domain, the zero sum is correctly formulated by
symmetric exhaustion through closed disks rather than by asserting an
unconditionally convergent scalar series.

Therefore the logical situation is

```text
unconditional Lean theorem:
    strict positivity of Q_(7/16)

literature-conditional identification:
    Q_a = symmetric zero-side limit

missing theorem needed for RH:
    Q_a >= 0 uniformly for every a > 0.
```

Even accepting the classical explicit formula, one local positive interval is
far from the all-support assertion equivalent to RH.

## 6. What the negative results contribute

The failed branches are not presented as evidence that RH is inaccessible.
They identify exact hypotheses under which tempting local-to-global mechanisms
cannot work.  The recurring obstruction is that compact local data can be
made blind to global spectral information, while positive local repair terms
do not automatically assemble into a coherent global polarization.

The useful output is a collection of scoped theorems with explicit escape
hatches: a successful construction must change at least one hypothesis of the
corresponding no-go result.  See
[`NO-GO-THEOREM-GUIDE.md`](NO-GO-THEOREM-GUIDE.md) and
[`../NO-GO-ATLAS.md`](../NO-GO-ATLAS.md).

## 7. Reusable mathematical contributions

Several formal packages stand independently of the RH program:

- digamma difference series, vertical Gauss integral, and logarithmic bounds;
- Fourier `L¹`/`L²` compatibility and Wiener--Khinchin identities;
- complete Legendre `L²` bases, Parseval, and interval transport;
- finite simultaneous simple-pole regularization;
- compact-support Fourier--Laplace entirety and exponential-type bounds;
- exact matrix perturbation certificates and optimal two-block coercivity.

Their mathematical narratives, exact declarations, and extraction seams are
collected in
[`LEAN-ANALYTIC-INFRASTRUCTURE.md`](LEAN-ANALYTIC-INFRASTRUCTURE.md) and
[`../lean/UPSTREAMING.md`](../lean/UPSTREAMING.md).

## 8. Appropriate claims

The following formulations match the current artifacts.

- **Appropriate:** “Lean proves a strict lower bound for the explicitly
  defined arithmetic compact-support Weil form at `a=7/16`.”
- **Appropriate:** “The repository formalizes reusable analytic and exact
  certificate machinery used in that proof.”
- **Appropriate:** “Several obstruction theorems rule out specified classes of
  local-to-global mechanisms.”
- **Not appropriate:** “Lean proves the full Guinand--Weil formula.”
- **Not appropriate:** “A finite matrix certificate proves RH.”
- **Not appropriate:** “The repository proves positivity at arbitrary
  support.”

The goal of this exposition is not to make criticism difficult.  It is to make
the exact point of any criticism easy to locate: the theorem statement, the
analytic reduction, the formal dependency ledger, the generated witness, or
the remaining global conjecture.
