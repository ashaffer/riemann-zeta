# Two-prime-plus-infinity fail-fast audit

Status: fixed-place positivity at every support is disproved; exact semilocal
locality survives, but it does not supply positivity.  The next surviving test
must enlarge the active place set when the support crosses a new prime event.
No RH claim is made.

Roadmap note, 2026-08-05: the prime-5 finite control proposed in Section 6 was
subsequently completed.  See
[`FAREY-VIRIAL-AND-PRIME5-CONTROL-2026-08.md`](FAREY-VIRIAL-AND-PRIME5-CONTROL-2026-08.md).
The historical “next target” text is retained as provenance.

## 1. The question and the answer

The proposed unit test was to retain only the places

`S = {infinity, 2, 3}`

and ask whether product-formula or categorical gluing could make their Weil
form positive without merely putting the three local pieces in a direct sum.
There are two materially different quantifiers:

1. **Fixed places, arbitrary compact support.**  This is false.  Section 2
   gives an explicit family of pole-zero test functions on which the form is
   negative as their support grows.
2. **A fixed support window in which no omitted prime is active.**  This
   survives.  In the repository convention, the places 2 and 3 contain every
   active finite-prime contribution while `L < 2 log 5`.  Existing Arb work
   already certifies a representative point in this window, subject to the
   analytic/software trust base recorded in `CODEX-REVIEW.md`.

The useful conclusion is therefore not “semilocality fails.”  It is that the
place set and support cannot be separated.  A global construction must explain
why each newly active prime repairs modes that the preceding fixed-place form
eventually loses.

## 2. Exact analytic obstruction for a fixed finite place set

Use the Fourier convention

`vhat(t) = integral_R v(x) exp(-i t x) dx`.

For a finite set `P` of primes, let `Q_P` be the standard-sign Weil form with
the archimedean place and precisely the prime places in `P`.  On the subspace

`vhat(i/2) = vhat(-i/2) = 0`,

the pole term vanishes and Plancherel gives

`Q_P(v) = (1/(2 pi)) integral_R M_P(t) |vhat(t)|^2 dt`,

where

`M_P(t) = -log pi + Re psi(1/4 + i t/2)`

`         - 2 sum_(p in P) log p sum_(m>=1) p^(-m/2)
                                      cos(m t log p)`.

For the theorem in this section, take the real test domain

`D={(-partial_x^2+1/4)phi : phi in C_c^infinity(R), phi real}`.

Every member of `D` satisfies the two pole-moment conditions.  The restricted
form is normalized by the displayed multiplier identity

`Q_P(v)=(1/(2 pi)) integral_R M_P(t)|vhat(t)|^2 dt`.

This identity, including the Fourier sign and the factors `1/(2 pi)` and `2`
in the prime term, is the load-bearing normalization of the theorem; a paper
version must derive it from the time-domain semilocal form rather than refer
to a “standard sign.”

For `P={2,3}`, its value at zero is

`M_{2,3}(0)`

` = psi(1/4) - log pi`

`   - 2 log(2)/(sqrt(2)-1) - 2 log(3)/(sqrt(3)-1)`

` = -11.72045865774345... < 0`.

This negative multiplier value can be reached while satisfying the pole
conditions exactly.  Choose a nonzero real `phi` in `C_c^infinity(R)` and set

`phi_R(x) = R^(-1/2) phi(x/R)`,

`v_R = (-partial_x^2 + 1/4) phi_R`.

Then

`vhat_R(z) = (z^2+1/4) R^(1/2) phihat(Rz)`,

so `vhat_R(+-i/2)=0`.  After the substitution `u=Rt`, dominated convergence
and the Schwartz decay of `phihat` give

`Q_{2,3}(v_R) / ||v_R||_2^2  ->  M_{2,3}(0) < 0`.

The same argument works for every fixed finite prime set: its multiplier at
zero is already negative before finite-prime terms are added, and every added
term makes it more negative.  Conversely,

`M_P(t) = log(|t|/(2 pi)) + o(1)`

up to a bounded finite-prime oscillation, so it tends to positive infinity.
To realize a positive direction in the same real domain, choose `T` with
`M_P(T)>0`, replace `phi_R` by `phi_R(x) cos(Tx)`, and again apply
`-partial_x^2+1/4`.  As `R` tends to infinity, its Fourier mass concentrates
at `+-T` and the Rayleigh quotient tends to `M_P(T)>0`; the two separated
bumps have vanishing overlap.  Thus the fixed-place form is genuinely
indefinite; reversing its overall sign does not help.

This is a theorem about fixed `P` and expanding support.  It does not contradict
positivity on an individual finite support window.

## 3. The first omitted-prime event is visible numerically

In the repository convention, `v` is supported in `[-L/4,L/4]`, its
autocorrelation is supported in `[-L/2,L/2]`, and the prime power `n` becomes
active when

`2 log n < L`.

The first prime omitted from `{2,3}` is therefore 5, at

`L_5 = 2 log 5 = 3.2188758248682006...`.

The lightweight script `src/semilocal_fixed_places_falsifier.py` compares the
fixed `{2,3}` form with the form containing every active prime power.  It
compresses both matrices to the two exact exponential-moment constraints.  At
Legendre dimension 12 it reports:

| `L` | fixed `{2,3}` Ritz minimum | all active primes Ritz minimum |
|---:|---:|---:|
| 3.270 | `-1.4807945716e-5` | `+2.5055646872e-5` |
| 3.400 | `-6.3552277486e-2` | `+2.3434101423e-5` |
| 4.000 | `-1.4984796559e-1` | `+1.3313134790e-7` |

These are ordinary floating-point Rayleigh--Ritz calculations, not interval
certificates.  A stable negative value is a finite-dimensional falsifier for
the assembled fixed-place matrix; the analytic argument in Section 2 removes
all dependence on this numerical evidence.  The positive full-form columns
are observations only and do not prove positivity at those supports.

The striking point is structural: once 5 is allowed, the tested negative
direction is repaired.  This is evidence that omitting the newly active prime
is not a harmless approximation.

Reproduce the light scan with

```text
python3 src/semilocal_fixed_places_falsifier.py
python3 src/semilocal_fixed_places_falsifier.py \
  --supports 3.27 3.4 4.0 --dimension 12 --dps 24
```

## 4. Algebraic gluing gates

Several finite “shared object” realizations can now be classified without
guesswork.

### 4.1 Positive trace plus a log-determinant of a sum

Let `tau` be a faithful finite trace and let `0 <= P,Q <= 1`.  If

`tau(P)=tau(P^2)`, `tau(Q)=tau(Q^2)`, and `tau(PQ)=0`,

then `P` and `Q` are orthogonal projections.  Indeed, positivity and
faithfulness applied to `P-P^2` and `Q-Q^2` make them projections, while
`tau(PQ)=tau(PQP)=0` gives `PQ=0`.

Consequently, an ordinary positive-trace model which uses

`-tau log(1-z_2 P-z_3 Q)`

to match the first two pure Euler coefficients and cancel the first mixed
coefficient is forced into orthogonal local sectors.  It can reproduce the
Euler product, but supplies no cross-place positivity mechanism.  The claim is
specific to positive contractions, a faithful positive trace, and this
log-determinant architecture; signed, noncommuting, or non-type-I models are
not covered.

### 4.2 Finite all-order commuting model

Let `U_2,U_3` be commuting invertible finite matrices and `L` a trace or
supertrace.  If

`L(U_2^m U_3^n)=0` for every `m,n>=1`,

then finite-dimensional invertibility expresses 1 as a polynomial in strictly
positive powers of either matrix.  It follows that all pure moments and
`L(1)` vanish as well.  Hence a finite commuting shared-Frobenius model cannot
retain nonzero local Euler moments while deleting every mixed moment in this
architecture.

A signed graded model can match any prescribed finite jet, including the
first two pure moments and one mixed cancellation.  That only proves algebraic
feasibility: a supertrace has no positivity leverage, and an unrelated positive
Gram matrix would be vacuous.  Exact gamma realization is also necessarily
infinite-dimensional or regularized, since `Gamma_R` has infinitely many
poles/zeros while a finite determinant has only finitely many.

## 5. What survives from the adelic/S-unit direction

The naive regulator torus of the `S`-units

`Z[1/6]^x = {+-2^a 3^b}`

with its induced flat metric has a two-dimensional Epstein spectrum.  The
translations by 2 and 3 become lattice periods, and mixed lattice vectors are
unavoidable.  This rules out that particular flat-torus Laplacian, not every
operator built from `S`-units.

Likewise, the regular representation of the multiplicative idele-class
quotient has continuous log-modulus spectrum and no compact-resolvent
Hamiltonian.  A positive Fock model on `{2^a3^b}` has the right Euler partition
function, but its raw spectrum contains all mixed composites; locality appears
only after taking `log Z`, as a cumulant identity rather than a positive state.

The genuine survivor is Connes's additive semilocal adele-class construction

`X_S = (R x Q_2 x Q_3) / Z[1/6]^x`.

Its renormalized distributional trace is exactly a sum of the local
archimedean, 2-adic, and 3-adic Weil distributions; no mixed composite term
remains in the final local sum.  This is real cross-place/product-formula
locality, not a direct-sum ansatz.  But the renormalized trace is not presented
as a faithful positive state, and the theorem does not prove Weil positivity.
It passes the locality gate and fails to cross the sign gate.

## 6. Pruned and surviving targets

The fail-fast verdict is:

| Candidate | Verdict | Exact scope |
|---|---|---|
| `{infinity,2,3}` positive at every support | **Killed** | explicit broad-bump theorem |
| finite positive shared log-determinant | **Killed** | faithful trace, positive contractions, saturated local coefficients |
| finite exact all-order commuting supertrace | **Killed** | invertible commuting matrices in the stated determinant architecture |
| flat `S`-unit regulator torus | **Killed** | induced Euclidean Laplacian only |
| signed finite second jet | **Passes algebraically** | no positivity implication |
| additive semilocal trace | **Passes locality** | positivity remains open |
| `{infinity,2,3}` before 5 activates | **Survives** | finite-window necessary test |

The next nonvacuous, finite and falsifiable target is the **5-event rescue**.
On the first window above `L=2 log 5`, isolate the negative spectral sector of
the old `{2,3}` form and determine whether the complete 5-place correction is
positive on that sector with a quantitative cross bound.  It is important not
to demand that the 5-update be positive on the whole ambient space: the
repository has already disproved that stronger one-prime Loewner statement.

A successful event theorem would have the form

`Q_{2,3,5} >= 0 on E_old^- direct-sum E_transition`,

with `E_old^-` defined spectrally before fitting the correction and with all
archimedean, moment, and cross terms fixed by the explicit formula.  Failure on
this first event would prune support-coupled induction.  Success would be a
genuine finite-stage bridge, still far weaker than RH; repeating it uniformly
over every prime event is where RH-strength difficulty would re-enter.

## 7. Primary literature anchors

- Alain Connes, *Trace formula in noncommutative geometry and the zeros of the
  Riemann zeta function*, Section VII: <https://arxiv.org/abs/math/9811068>.
- Alain Connes and Caterina Consani, *Weil positivity and Trace formula, the
  archimedean place*: <https://arxiv.org/abs/2006.13771>.
- Alain Connes, Caterina Consani, and Henri Moscovici, *Zeta zeros and prolate
  wave operators*: <https://arxiv.org/abs/2310.18423>.
