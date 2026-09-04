# Referee audit of the high-height carrier-slice iteration

Status: hostile normalization, quantifier, counterexample, and implementation
audit, 2026-08-12.

## Verdict

**PASS AFTER PATCHES** for the stated finite-dimensional reductions and the
double-precision fixture.  The direct constrained arithmetic edge is a
well-defined zero-independent diagnostic after a candidate pair fixes the
quotient.  The target-subtracted support is correctly pruned by the exact
aligned-baseline identity.

This verdict does **not** certify a uniform estimate, a divisor-isolation
theorem, a zero-free strip, or RH.  The five positive numerical values are not
interval-certified and have no actual-zero interpretation.

Audited artifacts:

- `ZETA23-HIGH-HEIGHT-CARRIER-SLICE-ANALYTIC-REDUCTION-2026-08-12.md`;
- `ZETA23-CARRIER-SLICE-ALIGNED-BASELINE-NOGO-2026-08-12.md`;
- `ZETA23-ACTUAL-HIGH-HEIGHT-CARRIER-SLICE-FIXTURE-2026-08-12.md`;
- `ZETA23-DIRECT-CARRIER-SLICE-FRONTIER-SYNTHESIS-2026-08-12.md`;
- `src/high_height_carrier_slice.py` and its focused tests; and
- the previously audited carrier-support solver and aligned-baseline tests.

## 1. Exact normalization and provenance

For raw sharp evaluation rows `x,y`, endpoint inclusion `U`, and program
support parameter `L`, the fixture consistently uses

```text
S_T=W_m intersect ker(x^*),
N_T=(2/L^2)(U^*y)(U^*y)^*,
K_0=(2/L^2)(x x^*-y y^*),
U^*K_0U=-N_T,
K_ar=U^*(H_arch+H_pole-H_prime)U/L^2.
```

The prime matrix contains every prime power `n<=exp(L)` with weight
`Lambda(n)/sqrt(n)`.  The pole matrix retains both Hermitian orientations.
The archimedean matrix uses the multiplier
`Re psi(1/4+it/2)-log pi` with the same sharp-grid convention.  An independent
centered-Loewner plus rational-density assembly reproduces the direct
arithmetic matrix to about `4e-14` in the tested cases.  The rational term is
constructed from its positive density, not defined as a residual.

The first fatal quantifier in the abandoned formulation was the proposed
kernel of **all** off-line positive rows: that object uses the unknown full
zero divisor.  The implemented `S_T` nulls only the externally parameterized
selected row and is noncircular.  The interpretation

```text
K_ar|S_T=-N_T+R_other
```

is valid only under the additional contradiction hypothesis that the
candidate is an actual divisor pair.  At an arbitrary scan point, `K_ar`,
`S_T`, and `N_T` remain valid arithmetic objects, but `R_other` has no
collateral-zero meaning.

## 2. Exact convex identities

For `N=kappa aa^*` and

```text
F_eta={Gamma>=0: Tr Gamma=1, Tr(N Gamma)>=eta},
q_eta(K)=max_(Gamma in F_eta) Tr(K Gamma),
```

the pure-state reduction and scalar dual are correct:

```text
q_eta(K)
 =max_(||z||=1, <z,Nz>>=eta) <z,Kz>
 =inf_(mu>=0)[lambda_max(K+mu N)-mu eta]
```

for `eta<kappa`; at `eta=kappa` the slice is the top carrier line.  The
rank-one optimizer proof correctly uses the at-most-two active affine
constraints on the range of an extreme state.

Target subtraction has no independent reservoir content.  On the selected
quotient,

```text
R_full=K_ar-K_0=K_ar+N,
q_eta(K_ar)+eta<=h_eta(R_full)<=q_eta(K_ar)+kappa.
```

If
`Phi_eta(nu)=lambda_max(K_ar+nu N)-nu eta`, then exactly

```text
q_eta=inf_(nu>=0) Phi_eta(nu),
h_eta(R_full)=eta+inf_(nu>=1) Phi_eta(nu).
```

Thus the target-subtracted functional deletes dual multipliers in `[0,1)`
and adds the aligned baseline.  At every fixed `theta<1`, it automatically
passes when `K_ar=o(kappa)`.  The direct `q_eta` retains genuine isolation
content; the target-subtracted `h_eta` supplies no new convex or arithmetic
gain.

For the optional cross-only mirror formulation, the exact factor is
`c=C/(C-1)`, and applying a theorem to `cN` also scales the carrier threshold
from `eta` to `c eta`.  A reducing extension must lie in the kernels of all
four lobe-restricted rows `x^-`, `x^+`, `y^-`, `y^+`; global kernels of `x`
and `y` alone do not reduce the cross observable.

## 3. Quotients, shallow rows, and hostile configurations

Further positive-row compression is monotone at the same absolute threshold:
either the smaller slice is empty, or its support is no larger.  Hence a
negative upper bound on the target-only slice survives every further
quotient; an empty smaller slice already means the requested carrier fraction
was deleted.  A positive value on the larger slice need not survive.

The shallow-depth transfer is legitimate because the cited sampling theorem
is an **operator-norm** bound.  Since `h_eta` is one-Lipschitz in operator
norm, on-line rows and fixed-gap shallow collateral may be removed at
`o(kappa)` cost.  Scalar estimates on one packet would not suffice.  Deep,
remote, collar, and localization summands without such a norm estimate remain
open.

The standard hostile configurations respect, rather than refute, the patched
scope:

- In the one-pair mirror, `R_other=0`; target isolation holds, while the
  target-subtracted object consists of its artificial `N` baseline.
- A near-tie collateral pair lies in the unresolved deep part and can screen
  at carrier scale in the abstract hyperbolic model.  Its normalized joint
  two-pair Gabor realization remains open.
- In the sparse tapered `k=3` island, terminal depth `2alpha/3` exceeds
  `alpha*d` for the relevant `d<2/3`.  The island is therefore classified as
  deep.  It demonstrates that moving carrier-scale screening can remain
  invisible to count, trace, and Frobenius ledgers; those bulk inputs cannot
  prove the missing isolation theorem.

## 4. Sign logic and numerical scope

The proposed two-lemma closing logic is correct:

```text
arithmetic admission:       q_eta(K_ar)>=0,
hypothetical-zero isolation: q_eta(K_ar)<0.
```

A uniform proof of both statements for the same candidate family would be a
contradiction and exclude that family of zeros.  Neither statement is now
proved uniformly.  In particular, `q_eta>=0` says only that one nonnegative
state exists in the relaxed target-only slice; `q_eta<0` says every state in
that slice is negative.

The fixture scans `T=32,64,128,256,512`, one phase, one depth, one aperture,
and the illustrative jet order `m=max(3,ceil(log T))`.  This is not the
mesoscopic/maximal Zeta23 order, which can be of size `eta*T`.  All fifteen
displayed `q_eta` values are positive in floating arithmetic, including
`q_kappa=1.00043884505` at `T=512`.  This verifies execution of the arithmetic
pipeline only.  It gives no uniform lower bound, no extrapolation in `T`, and
no evidence that a scan point is a zero.

## 5. Patches and checks

Clear defects repaired during audit:

1. made the divisor interpretation conditional on the target actually being
   a zero, including multiplicity bookkeeping;
2. fixed raw-row versus normalized-row `L^(-2)` conventions;
3. required lobe-restricted common kernels for the cross-only reduction and
   disambiguated its carrier slice;
4. scaled the threshold correctly when replacing `N` by `cN`;
5. changed a KMT “size” claim to the accurate “available upper bound”;
6. recorded that the fixture jet order is illustrative, not mesoscopic;
7. corrected the documented sharp basis phase from `exp(+i tau_k t)` to the
   implemented `exp(-i tau_k t)`; and
8. added the nonempty-slice qualification to further-quotient monotonicity.

Reproduction after the patches:

```text
PYTHONPATH=src python3 -m pytest -q \
  src/test_carrier_slice_support.py \
  src/test_carrier_slice_baseline.py \
  src/test_high_height_carrier_slice.py

13 passed
```

An independent `T=512` rerun reproduced `kappa=1.31184871408`,
`q_kappa=1.00043884505`, the reported extremal eigenvalues, and all residuals.

## Final scope

The iteration has produced a sound finite target-conditioned arithmetic
diagnostic and an exact no-gain theorem for the target-subtracted support.
Its next honest targets are a uniform arithmetic admission theorem for the
direct `q_eta` and an independent deep-collateral isolation theorem.  The
current work proves neither.
