# Referee audit of the completion-preserving coboundary/Type-II route

Status: hostile internal audit, 2026-08-11.  This report verifies the exact
reduction and identifies its first open estimate.  It proves no zero-free
strip and makes no novelty claim.

## 1. Binary verdict

**Does the reduction currently yield any fixed `eta>0`?  No.**

The fixed-order reduction is a valid conditional implication:

```text
|B_(U,V)^(k)(x)-Z_(U,V)^(k)(x)|
  <=x^(1/2-eta+o(1))
for one fixed eta>0

              implies

Delta<=1/2-eta.
```

The repository does not prove the displayed premise for any fixed positive
`eta`.  Its strongest proved full-field/frozen-center calibration is

```text
exp[R-c_h R^(4/5)(log R)^(-3/5)],
```

so its effective `eta(R)` tends to zero.  The first genuinely unproved
estimate is the cutoff-complete, one-sided two-shift bound

```text
X_I<=exp((1-2eta+o(1))R),       0<eta<=1/2 fixed,
```

where `X_I` contains every unequal-total-product and center term after only
the grouped atomic diagonal is removed.  This is not supplied by positivity,
the large sieve, Ward identities, cutoff transport, or the local Mobius
recursions presently in the repository.

The reduction itself is not circular: it is an exact change of coordinates
from the fixed-window prime discrepancy.  Treating the missing two-shift
bound as though it followed from the coordinate change would be circular,
because the completed energy has exact exponential width `2 Delta` and the
proposed bound is already the desired fixed strip in energy coordinates.

## 2. Exact identity ledger

The following parts survive direct algebraic checking.

1. **Vaughan completion.**  With

   ```text
   a_(U,V)=mu_(>U)*Lambda_(>V)*1,
   h_(U,V)=mu_(<=U)*log+Lambda_(<=V)
            -mu_(<=U)*Lambda_(<=V)*1,
   ```

   one has `a_(U,V)+h_(U,V)=Lambda` coefficientwise.  Thus grouping the
   balanced tail by total product does not delete any cofactor.  For distinct
   primes exceeding both cutoffs, the two factor assignments give the one
   coefficient `a_(U,V)(pq)=-log(pq)`.

2. **Center.**  From the definitions of `I_pol`, `I_0`, and `Z`, setting

   ```text
   P=J_0 M_U(1),
   Q=J_1 M_U(1)+J_0[M_U'(1)-M_U(1)L_V(1)]
   ```

   gives exactly

   ```text
   Z(exp R)=exp(R/2)[J_0-PR-Q]-I_0.
   ```

   Therefore `I_0` cancels after the scale coboundary and the displayed
   formula for `Delta_ell Z` is correct.

3. **Coboundary.**  The B-spline distribution symmetry gives

   ```text
   W_(ell,k)(t)=Phi_(ell/k,k)(t+ell)-Phi_(ell/k,k)(t),
   ```

   nonnegative, even, and supported in `[-ell,ell]`.  With one cutoff pair
   used at both endpoints, the discrete part of `Delta_ell(B-Z)` is exactly

   ```text
   T(R)=sum_n a_(U,V)(n)n^(-1/2)W_(ell,k)(R-log n).
   ```

   If `z(R)=Delta_ell Z(R)`, its block energy is exactly

   ```text
   integral psi |T-z|^2
    =sum_(m,n) a(m)conjugate(a(n))/sqrt(mn)
       integral psi W(R-log m)W(R-log n)dR
     -2 Re sum_n a(n)/sqrt(n)
       integral psi W(R-log n)conjugate(z(R))dR
     +integral psi |z|^2.
   ```

   Hence all unequal products, all cross-cofactor/parity terms, the tail--
   center cross term, and the center square are retained.  This is the
   decisive ordering check requested in the audit.

4. **Euler defect and its sign.**  If
   `E=T_head^app-T_head^exact`, then

   ```text
   B-Z=C_full+E,
   Delta_ell(B-Z)=D_(ell,k)+Delta_ell E.
   ```

   This agrees with the signed-defect convention in the joint-cutoff report.
   The direct two-shift report uses the opposite symbol
   `epsilon=T_head^exact-T_head^app`; its formula
   `D_full=G+Delta epsilon` is the same identity.

5. **Fixed-order exponent implication.**  For fixed `k` and
   `U=V=floor(x^theta)`, `0<theta<=theta_k`, the Euler error is bounded at
   `theta_k` and tends to zero below it.  Since the fixed transform has no
   zero off the imaginary axis, the stated law

   ```text
   limsup log(1+|B-Z|)/log x=Delta
   ```

   follows from the fixed-window width theorem.  Thus a proved
   `O(x^(1/2-eta))` bound really would give a uniform strip.

6. **Energy exponent.**  Conditional on the same fixed-window explicit
   formula, Proposition 3.1 has the correct proof mechanism.  The upper
   bound follows from absolute zero-side summability.  If
   `e^(-sigma R)D_ell` were in `L2` with `sigma<Delta`, Cauchy--Schwarz would
   make its one-sided Laplace transform holomorphic in `Re(s)>sigma`, while
   an off-line zero of displacement greater than `sigma` supplies a genuine
   pole.  Monotonicity of the cumulative energy then gives
   `limsup log(1+E_ell(T))/(2T)=Delta`.

7. **Dirichlet and Fourier forms.**  For fixed finite cutoffs,

   ```text
   sum_n a_(U,V)(n)n^(-s)
    =(1-zeta(s)M_U(s))[-zeta'(s)/zeta(s)-L_V(s)]
   ```

   in `Re(s)>1`.  The finite block polynomial and the complete two-frequency
   formula are the safe critical-line objects; analytically continuing this
   infinite series to `Re(s)=1/2` would simply reinsert the zero poles.

The focused finite-algebra regression tests also pass:

```text
PYTHONPATH=src python3 -m unittest -v \
  src/test_type2_block_mechanism_probe.py \
  src/test_fixed_step_spectral_cooling_probe.py

8 tests, all passed.
```

These tests check finite identities only, not the missing asymptotic bound.

## 3. First open estimate and why the attempted bridges do not prove it

On a regular block the exact completed energy decomposes as

```text
E_I=D_I+X_I,
```

where `D_I=exp(o(R))` is the grouped atomic diagonal.  Positivity gives only
`X_I>=-D_I`; it gives no useful upper bound.  Consequently

```text
X_I<=exp((1-2eta+o(1))R)
```

for one fixed `0<eta<=1/2` is the first missing theorem.

The existing gates correctly prevent the following invalid simplifications.

- Vaughan polarization plus a Ward counterterm gives identically the
  original completed energy minus the tail diagonal.  It is a relabeling,
  not a new signed inequality.
- Cutoff variance removes the cutoff-independent common mode and therefore
  cannot control the cutoff mean carrying `C_full`.
- Separate rectangle, cofactor, parity, or Type-I estimates delete the
  cross terms that restore the zeta factor.  A sufficiently uniform
  rectangle estimate would already force a power-saving Mertens bound.
- The exact cutoff flow leaves every zeta-zero principal part unchanged, so
  no local shell contraction acts on the carrier.
- The proved Vinogradov--Korobov estimate supplies only a sublinear exponent
  saving.  It cannot be promoted to fixed `eta` by notation or by optimizing
  the existing fixed-step schedule.

Thus the surviving statement is a genuinely global, Mobius-specific,
cutoff-complete two-shift theorem.  Nothing presently in the reduction
proves it.

## 4. Repairable defects and quantifier clarifications

These do not invalidate the fixed-order reduction, but they should be fixed
before publication.

1. **No uniqueness theorem.**  The phrase “There is one
   completion-preserving way” should read “There is a
   completion-preserving way.”  The report exhibits a faithful ordering; it
   does not classify every possible completion-preserving construction.

2. **Frozen versus moving cutoffs.**  The scale coboundary identity uses the
   same `U,V` at `R` and `R+ell`.  The fixed-order width law uses
   `U(R)=V(R)=floor(e^(theta R))`.  A block argument must therefore define a
   frozen-at-the-block cutoff field, state the block length, compare it with
   the full field through the Euler defect, and account for cores/endpoints.
   One must not write `Delta_ell` of the globally moving-cutoff field and
   silently treat it as the frozen-cutoff difference.  The later direct
   two-shift report supplies the needed regular-block convention; the
   candidate note should import it explicitly.

3. **High-zero tail in fixed-step cooling.**  The factor `1/|gamma|` alone
   is not summable over zeta zeros.  The claimed exponential decay in `k`
   requires the additional high-frequency estimate

   ```text
   |sinc(h gamma/2)|<=min(1,2/(h|gamma|)),
   ```

   followed by Riemann--von Mangoldt counting.  The later full-field report
   contains the stronger correct multiplier bound, so this is a proof-text
   repair rather than a failed claim.

4. **Semiprime asymptotic.**  Lemma 6.1 should assume `W` is not identically
   zero (equivalently, under nonnegativity, `integral W>0`) before using
   asymptotic notation `~`.  To call it literally part of the tail diagonal,
   also state `U,V<=X^theta` (normally `U=V=floor(X^theta)`) and restrict to a
   block/core on which the energy weight is the displayed `W`.

5. **Proposition/Lemma packaging.**  Proposition 3.1 and the semiprime
   asymptotic currently have proof spines, not fully quantified
   publication-ready proofs.  Their completion would improve exposition but
   would not supply the missing fixed-power estimate.

6. **Growing-order branch has two debts.**  Even if a subexponential or
   fixed-power estimate were proved for the locally constant fixed-step
   schedule, a varying-test zero-isolation theorem is still required before
   reading it as a zero-free conclusion.  The fixed-order branch does not
   have this extra debt.

## 5. Exact source locations

- The candidate explicitly labels itself an attack surface rather than a
  bound at `COBOUNDARY-DISPERSION-CANCELLATION-CANDIDATE.md:21-24`.
- Total-product grouping, the center, the coboundary, and the signed Euler
  defect are at that file's lines `28-122`.
- The energy-width argument is at lines `124-163`; the full Gram expansion
  and its mandatory center terms are at lines `165-212`.
- The semiprime diagonal is at lines `250-279`, and the unproved blockwise
  varying-test converse is acknowledged at lines `369-376`.
- The success threshold and the statement that the off-diagonal remains
  open are at lines `477-490`.
- The fixed-order Vaughan formula and width law are at
  `publication/FIXED-WINDOW-WIDTH-AND-TYPE-II-REDUCTION.md:242-304`; the
  manuscript itself identifies the desired fixed saving at lines `457-460`.
- The exact finite two-frequency field and Euler completion are at
  `DIRECT-CUTOFF-COMPLETE-TWO-SHIFT-GATE.md:64-221`; its surviving theorem is
  stated at lines `441-456`.
- The Ward completion collapse is the identity at
  `NONLOCAL-WARD-COVARIANCE-NOGO.md:46-113`.
- The Mobius-specific audit states that the remaining global theorem is
  essentially the strip itself at
  `MOBIUS-TWO-SHIFT-RENORMALIZATION-GATE.md:51-61` and `495-516`.
- The best proved subpower bound and its frozen-center transfer are at
  `FULL-FIELD-VK-SUBPOWER-BOUND.md:94-176`; that report explicitly preserves
  the varying-test gap at lines `480-484`.

## 6. Referee disposition

Accept the fixed-order construction as a rigorous **reduction**, after the
minor quantifier repairs above and specialist review of the analytic
packaging.  Reject any claim that it currently proves a fixed strip, yields
an `eta>0`, or provides evidence that the missing two-shift estimate is true.
The next valid advance must prove a new upper bound for the complete
all-sector correlation; another decomposition of the same completed square
is not progress toward the strip.
