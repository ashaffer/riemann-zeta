# Finite operator-system admission gate for the two-packet zeta fixture

Status: exact finite-dimensional order/Choi results, a zero-independent
arithmetic/support provenance check, and floating-point place diagnostics,
2026-08-12.  No zero-free strip, RH statement, or positivity theorem for the
full Weil form is proved here.

## 1. Verdict

The first categorical order-descent experiment gives a sharp three-level
answer.

1. On the reflection-symmetric mirror system

   ```text
   E_mir=span_C{I,J},                 J=[[0,1],[1,0]],
   ```

   coordinate probes fail, while the two parity probes have an exact UCP
   recovery.  The successful recovery is only spectral readout: on the
   normalized reflected-pair matrix `m(I+CJ)`, `C>1`, it returns
   `m(1+C)` and `m(1-C)`.  It detects the negative carrier but supplies no
   arithmetic reason for the second number to be nonnegative.
2. The first zero-independent left/right support contrast enlarges the
   self-adjoint system to

   ```text
   V_asym=span_R{I,J,Z}=Sym_2(R),      Z=diag(1,-1).
   ```

   No finite family of scalar vector-state probes can be order-reflecting on
   this system.  This is exact: finitely many scalar inequalities define a
   polyhedral cone, whereas the `2 x 2` PSD cone is not polyhedral.  Even the
   four natural coordinate/parity probes are injective but miss an explicit
   indefinite matrix with a strict positive margin.
3. A full matrix-valued pair probe does have a UCP inverse, but it retains the
   complete `2 x 2` block.  Thus cross-aware matrix descent survives only in
   a conservative form at this minimal stage; it has not compressed or signed
   the problem.

The most natural Stinespring-covariance candidate also closes at this stage.
Block dephasing of

```text
H=[[A,B],[B*,D]]
```

has exact Kadison covariance `diag(BB*,B*B)`.  After diagonal normalization,
its norm is the square of the existing Schur coupling

```text
||A^(-1/2) B D^(-1/2)||.
```

It therefore packages the old cross term rather than adding a new positive
direction.  The repository's prime-5 diagnostics put this coupling between
`0.8779366` and `0.9998517` in the tested fixtures: below one at those finite
stages, but almost saturated and with no uniform margin.

The actionable conclusion is narrow.  **Stop treating fixed finite
scalar-probe/sheaf refinements as exact order-reflection mechanisms on the
full asymmetric system.**  Continue an operator-system route only with
matrix-valued cross probes which are smaller
than the full ambient block, have a positive recovery on the actual
arithmetic system, and produce outputs whose sign is independently
arithmetically controllable.

## 2. The exact zero-independent arithmetic fixture

Two matrices must not be conflated.  The normalized Paley--Wiener mirror
`m(I+CJ)` is the compression of a *hypothetical reflected zero pair*; it is
used in Section 3 only to calibrate what the probes see.  It is not inserted
as a zero-independent arithmetic generator.  The operator system below is
built separately from the repository's support metric, prime translation,
pole, and archimedean pieces.  The two constructions share the same
reflection algebra `span{I,J}`, which is precisely what makes the calibration
applicable.

### 2.1 Why `L=7/4`, two hats, is the first honest stage

The repository's fixed physical support is

```text
[-7/16,7/16].
```

In `src/weil_core.py` this is `L=7/4`.  With two interior hats,

```text
d=7/24,                    centers=-7/48,+7/48,
```

and the exact `L2` Gram matrix is

```text
G=(7/144)(4I+J)
 =[[7/36,7/144],[7/144,7/36]].                      (2.1)
```

This is the smallest stage at which the support reaches the first prime
translation: `2 log 2<7/4`, while `2 log 3>7/4`.

Let `P_2` denote the unsigned `p=2` translation form.  Only one directed hat
overlap survives.  The exact symmetric form is

```text
P_2=p_2 J,

p_2=96 log(2)(7/8-log(2))^3/(49 sqrt(2))>0.         (2.2)
```

The completed Weil form uses `-P_2`; the sign does not change the generated
operator system.  Since `G` and `P_2` commute, whitening gives exactly

```text
G^(-1/2) P_2 G^(-1/2)
 =G^(-1)P_2
 =(48p_2/35)(4J-I).                                 (2.3)
```

Its `J` coefficient is nonzero.  Consequently the metric and the first prime
already generate `span{I,J}`.  The centered pole form and the archimedean
form also lie there exactly: reflection exchanges the two hats, and the
archimedean multiplier is even.  Thus

```text
E_arith,sym=span_C{I,K_gamma,K_pole,K_2}=span_C{I,J}. (2.4)
```

This conclusion uses no zero, negative eigenvector, or fitted factorization.

### 2.2 The first asymmetric support generator

The strict system (2.4) is adequate only for a theorem which freezes exact
reflection symmetry.  The advertised packet/support class permits the two
lobes to be distinguished before any bad zero is selected.  Let `P_L,P_R` be
the projections onto the normalized original left and right hat rays after
Gram whitening.  Direct calculation from (2.1) gives

```text
P_L-P_R=(sqrt(15)/4) Z,             Z=diag(1,-1).   (2.5)
```

Hence `Z` is a zero-independent support observable.  It is not manufactured
from a negative eigenvector.  Adding it gives

```text
E_asym=span_C{I,J,Z},
(E_asym)_sa=Sym_2(R).                                (2.6)
```

If a proposed theorem explicitly excludes every lobe-asymmetric support
observable, it may remain on (2.4).  It then inherits the parity-output
limitation in Section 3.  A theorem intended to cover the asymmetric packet
class must pass (2.6).

## 3. Exact scalar-probe and Choi tests

### 3.1 Coordinate probes fail before the asymmetric enlargement

Write

```text
A=aI+bJ in (E_mir)_sa.
```

The coordinate vector states give

```text
Phi_coord(A)=(a,a).                                  (3.1)
```

Thus `J` is a nonzero Hermitian kernel element.  Both observed scalars are
zero, hence positive, while `J` has eigenvalues `-1,1`.  The map is neither
order-reflecting nor injective and cannot have any linear, positive, or CP
left inverse.

### 3.2 Parity probes have an exact CP recovery

Put

```text
e_+=(1,1)/sqrt(2),        e_-=(1,-1)/sqrt(2),
P_+=e_+e_+*,              P_-=e_-e_-*.
```

Then

```text
Phi_par(A)=(a+b,a-b),
Psi(x,y)=xP_+ + yP_-,
Psi Phi_par(A)=A.                                   (3.2)
```

The map `Psi:C direct_sum C -> M_2` is UCP.  Its direct-sum Choi datum is

```text
Choi(Psi)=P_+ direct_sum P_->=0,
spec Choi(Psi)={0,0,1,1},
P_++P_-=I.                                          (3.3)
```

This is an exact feasible point for the finite Choi SDP; no numerical solver
is required.  It proves complete order reflection on `E_mir`.

It does not prove positivity of the zeta form.  For the exact normalized
mirror block

```text
M=m(I+CJ),                         C>1,
```

the two outputs in (3.2) are exactly its eigenvalues

```text
m(1+C)>0,                 m(1-C)<0.                 (3.4)
```

Recovery has exposed, not repaired, the obstruction.

### 3.3 Four scalar probes are injective on `Sym_2` but still fail

Take `e_1,e_2,e_+,e_-`.  Their observation matrix on the ordered basis
`I,J,Z` has rank three, so failure cannot be blamed on loss of linear
information.  Define

```text
A_*=7/16 I-(9 sqrt(2)/32)(J+Z)

   =[[7/16-9sqrt(2)/32, -9sqrt(2)/32],
     [-9sqrt(2)/32, 7/16+9sqrt(2)/32]].             (3.5)
```

Its eigenvalues are

```text
{-1/8,1}.                                           (3.6)
```

Nevertheless its four probe values are

```text
(14-9sqrt(2))/32,
(14+9sqrt(2))/32,
(14-9sqrt(2))/32,
(14+9sqrt(2))/32.                                  (3.7)
```

All are strictly positive because `14^2>2*9^2`.  Thus `A_*` is a structured
strict counterexample to order reflection.  A positive recovery is
impossible: it would send the positive tuple (3.7) to the indefinite matrix
(3.5).  This is an exact infeasibility certificate for the corresponding
Choi SDP.

### 3.4 No finite scalar family can repair this

Let `v_1,...,v_r` be any finite family of scalar probes and consider

```text
C_v={A in Sym_2(R): v_i* A v_i>=0 for every i}.      (3.8)
```

This is an intersection of finitely many linear halfspaces and hence a
polyhedral cone.  The cone `Pos_2(R)` is not polyhedral: every ray
`R_+ uu*`, with `u` a real projective direction, is extreme, giving a
continuum of extreme rays.  Since `Pos_2(R) subset C_v`, equality is
impossible.  Therefore every finite scalar family misses an indefinite
matrix.

For a finite family of **real rank-one** vector probes, one can equivalently
place a negative eigenvector halfway across the largest gap between their
projective directions.  If the gap is `delta`, then

```text
A=I-c ww*,       1<c<sec(delta/2)^2,                (3.9)
```

is indefinite and has positive expectation on every probe.  The reproducible
script implements this constructive witness as well as the exact special
case (3.5).

The polyhedral theorem concerns arbitrary fixed finite scalar vector-state
observations (including complex vectors); the explicit angular construction
in (3.9) is for real rank-one probes.  It does not rule out matrix-valued
compressions, a smaller pre-specified arithmetic subspace, or a separate
arithmetic theorem which signs the actual element without reflecting order on
all of `Sym_2(R)`.

## 4. Matrix-valued cross-aware probe: exact but conservative

Let `U=[e_+ e_-]`.  Keep the full parity-pair matrix rather than its two
diagonal scalar entries:

```text
Phi_pair(A)=U* A U in M_2,
Psi_pair(B)=U B U*.
```

Both maps are unitary conjugations, hence UCP, and

```text
Psi_pair Phi_pair=id.                               (4.1)
```

The Choi matrix of `Psi_pair` is the rank-one positive matrix
`vec(U)vec(U)*`, with eigenvalues `{0,0,0,2}`.  On the symmetric system,
`Phi_pair(A)` is diagonal.  On the asymmetric generator, `U*ZU` is
off-diagonal.  The full matrix output retains exactly the cross term which
separate scalar parity probes discard.

Thus matrix-order descent passes at the minimal stage, but only by carrying
the complete two-packet block.  To become useful at larger stages, a proposed
matrix probe must satisfy all three conditions:

1. its output is materially smaller or more local than the ambient operator;
2. it still has positive recovery on the zero-independent arithmetic system;
3. the recovered local matrix inequalities are independently provable from
   prime, pole, gamma, and support coefficients.

Condition 2 without condition 3 is detection, not a positivity engine.

## 5. The natural Stinespring covariance is Schur-equivalent

Let `E` be conditional expectation onto the two diagonal blocks and let

```text
H=[[A,B],[B*,D]]=H*.
```

Then exactly

```text
Cov_E(H,H)
 =E(H^2)-E(H)^2
 =diag(BB*,B*B)>=0.                                 (5.1)
```

This is the canonical positive Kadison--Schwarz defect.  It contains no new
entry: it is precisely the squared old/positive cross coupling.

When `A,D>0`, put

```text
C=A^(-1/2) B D^(-1/2),
H_tilde=[[I,C],[C*,I]].                              (5.2)
```

Equations (5.1)--(5.2) give

```text
Cov_E(H_tilde,H_tilde)=diag(CC*,C*C),
||Cov_E(H_tilde,H_tilde)||=||C||^2.                 (5.3)
```

But the Schur-complement theorem says

```text
H_tilde>0 iff ||C||<1.                              (5.4)
```

Therefore the apparently new covariance threshold

```text
Cov_E(H_tilde,H_tilde)<I                            (5.5)
```

is equivalent to the existing Schur coupling criterion.  Positivity of the
covariance alone is automatic and does not sign `H`.

The zero-independent prime-5 block split in
[`prime5_block_rescue.py`](../src/prime5_block_rescue.py) provides the natural
arithmetic test.  At dimension 12 the reproduced floating diagnostics are:

| support | unrestricted `||C||` | unrestricted `||Cov||` | pole-null `||C||` | pole-null `||Cov||` |
|---:|---:|---:|---:|---:|
| `3.27` | `0.990443104` | `0.980977542` | `0.877936628` | `0.770772723` |
| `3.30` | `0.994081693` | `0.988198412` | `0.982110747` | `0.964541520` |
| `3.40` | `0.999851669` | `0.999703361` | `0.971620388` | `0.944046179` |

These numbers are ordinary floating-point Ritz diagnostics.  The separate
finite prime-5 positivity and witness statements at `L=3.27` have stronger
interval/Lean certificates, but those certificates do not certify a uniform
coupling gap.  The approach to `0.9998517` is a fail-fast warning: the
dephasing covariance does not reveal a hidden margin beyond the already
measured Schur margin.

This closes only the obvious old-negative/old-positive conditional
expectation.  A different CP map remains logically possible, but it must
produce a covariance not algebraically equal to an existing Schur cross term
and must enter the completed arithmetic identity with a derived useful sign.

## 6. Numerical arithmetic sanity check

The script also assembles the support, gamma, pole, and unsigned `p=2` pieces
independently at `L=7/4,m=2`, using the same hat and digamma conventions as
`src/weil_core.py`.  At cutoff `240` with `24000` Simpson intervals, after
Gram whitening it reports

```text
gamma  = -0.6658443982 I -0.7113284786 J,
pole   =  0.6999907365 I +0.7124628216 J,
p=2    = -0.0079198859 I +0.0316795436 J.           (6.1)
```

The numerical generator rank is two; the reflection residuals are zero to
machine precision.  The displayed `p=2` matrix is the unsigned translation
form `P_2`; the completed Weil form contains `-P_2`.  Its coefficient agrees
with the exact expression (2.3).  The displayed gamma coefficients depend
mildly on cutoff and are not
interval-certified.  They are not used in Sections 2--5.  Exact reflection
membership follows from symmetry, not from (6.1).

## 7. Reproduction and trust boundary

Run the unit suite (SymPy exact checks plus explicitly floating regression
checks):

```text
python3 src/test_categorical_operator_system_gate.py
```

Run the exact symbolic gate summary plus the low-memory numerical place
assembly:

```text
python3 src/categorical_operator_system_gate.py \
  --cutoff 240 --intervals 24000
```

Reproduce the prime-5 coupling data:

```text
PYTHONPATH=src python3 src/prime5_block_rescue.py \
  --supports 3.27 3.30 3.40 --dimension 12 --dps 24

PYTHONPATH=src python3 src/prime5_block_rescue.py \
  --supports 3.27 3.30 3.40 --dimension 12 --dps 24 --relative
```

The exact trust base is elementary `2 x 2` algebra plus SymPy checking:

- formulas (2.1)--(2.5);
- the kernel and recovery equations (3.1)--(3.3);
- the counterexample (3.5)--(3.7);
- the nonpolyhedral proof in Section 3.4;
- the unitary Choi certificate (4.1); and
- the block identity (5.1)--(5.4).

Floating-point quadrature is used only for (6.1), and floating-point spectral
linear algebra is used for the table in Section 5.  No CVX package is
installed or required: the feasible Choi points and the infeasibility
witnesses at this minimal stage are explicit exact certificates.

## 8. Scope and next admission target

This report does **not** show that the actual zeta Weil matrix is indefinite,
that a uniform strip fails, or that an operator-system proof cannot exist.
It shows:

- local scalar packet positivity cannot glue to global positivity on the
  first support-asymmetric two-packet operator system;
- the parity CP recovery on the symmetric subsystem is tautologically
  spectral;
- a full cross-aware matrix probe can recover order but has not reduced the
  problem; and
- the most natural block Stinespring covariance is exactly the old Schur
  coupling squared.

The next operator-system experiment is admissible only if it avoids these
collapses.  At a larger zero-independent finite stage, define the arithmetic
system from individual prime, pole, gamma, and support generators; select a
proper matrix-valued cross cover; and test whether it has CP recovery while
omitting some ambient directions.  If recovery requires the full block, or
if the local matrices are no easier to sign than the completed matrix, the
route has again only renamed the original positivity problem.

Abstract operator-system recovery and nonpolyhedrality are standard.  The
material contribution here is their exact application to the repository's
`L=7/4` arithmetic/support fixture, the explicit Choi and separation
certificates, and the identification of the proposed CP covariance with the
already-audited prime-5 Schur threshold.
