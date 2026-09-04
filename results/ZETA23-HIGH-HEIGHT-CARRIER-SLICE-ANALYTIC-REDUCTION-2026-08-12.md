# The high-height carrier slice has a canonical prime-side realization

Status: exact finite-dimensional reduction from the completed Gabor form,
exact rank-one carrier formula, and a rigorous shallow/deep collateral
dichotomy, 2026-08-12.  A subsequent actual-coefficient fixture now exists,
but no uniform estimate of the remaining deep/actual-prime operator is
proved.  No zero-free strip or RH statement is proved.

**Subsequent correction.**  The target-subtracted quantity in this report is
an exact diagnostic, but it is not an independent remainder theorem.  On the
selected quotient,

```text
R_full,T=N_T+K_ar,T|S_T.
```

Consequently its support is the direct arithmetic dual with the multiplier
range `[0,1)` deleted and an aligned `eta` baseline added.  Any language below
that prioritizes `h_eta(R_full,T)` is superseded by the direct constrained
edge `q_eta(K_ar,T)`.  See
[`ZETA23-CARRIER-SLICE-ALIGNED-BASELINE-NOGO-2026-08-12.md`](ZETA23-CARRIER-SLICE-ALIGNED-BASELINE-NOGO-2026-08-12.md),
the executable
[`ZETA23-ACTUAL-HIGH-HEIGHT-CARRIER-SLICE-FIXTURE-2026-08-12.md`](ZETA23-ACTUAL-HIGH-HEIGHT-CARRIER-SLICE-FIXTURE-2026-08-12.md),
and the corrected
[`ZETA23-DIRECT-CARRIER-SLICE-FRONTIER-SYNTHESIS-2026-08-12.md`](ZETA23-DIRECT-CARRIER-SLICE-FRONTIER-SYNTHESIS-2026-08-12.md).

## 1. Verdict

There is a canonical version of the proposed high-height carrier slice which
does not use the unselected zeta zeros.

Fix a *hypothetical* reflected target pair and work in the complexified finite
endpoint-flat Gabor space.  Let `x_0` and `y_0` be its positive and negative
evaluation rows **after division by the program support parameter `L`**.  In
terms of the raw evaluation rows `x_raw,y_raw`, the convention is
`x_0=x_raw/L`, `y_0=y_raw/L`; this absorbs the repository's common `L^(-2)`
factor.  Then the correct quotient and carrier are

```text
S_T=ker(x_0^*),
N_T=2*(P_(S_T)y_0)*(P_(S_T)y_0)^*.                 (1.1)
```

Conditioning on the putative target is legitimate in a contradiction
argument.  By contrast, replacing (1.1) by the common kernel of the positive
rows of **all** actual off-line zeros uses the unknown collateral divisor and
is not an independent arithmetic construction.

Let

```text
K_ar,T=K_pole,T+K_arch,T-K_prime,T                 (1.2)
```

be the actual completed arithmetic matrix, assembled by polarizing the
repository's finite Gabor formula.  If

```text
K_0,T=2*(x_0*x_0^*-y_0*y_0^*)                     (1.3)
```

Equivalently, in raw-row notation,
`K_0,T=(2/L^2)*(x_raw*x_raw^*-y_raw*y_raw^*)` and
`N_T=(2/L^2)*(P_S y_raw)*(P_S y_raw)^*`.

is the selected pair matrix, the actual full-form remainder on the quotient
is

```text
R_full,T=P_S*(K_ar,T-K_0,T)*P_S.                   (1.4)
```

Every entry of (1.4) is determined by the pole and gamma integrals, the finite
von Mangoldt sum allowed by compact support, and the target parameters.  No
collateral zero is needed to define or compute it.  **Under the contradiction
hypothesis that this target pair actually occurs in the divisor** (with one
occurrence marked if its multiplicity is larger), the explicit formula then
gives the second, useful interpretation

```text
R_full,T=P_S*(K_divisor,T-K_0,T)*P_S,              (1.5)
```

so it is exactly the on-line plus collateral screening operator, including
any unmarked copies of a multiple target.  For an arbitrary scan point which
is not assumed to be a zero, (1.4) remains a well-defined arithmetic
diagnostic but (1.5) does not have that screening interpretation.

The associated carrier-slice SDP is not merely reducible to a scalar dual.
Because `N_T` has rank one, it is an exact constrained Rayleigh problem with
an explicit carrier/complement/transverse decomposition.  This identifies
precisely what can make the slice carrier-positive.

The present analytic estimates settle only one branch.  On the normalized
two-lobe packet geometry, the on-line rows and every collateral pair of depth
at most `alpha*d-epsilon` contribute `o(kappa_T)`, where

```text
kappa_T=lambda_max(N_T)
       =X^(alpha*d+o(1))/L.                         (1.6)
```

Therefore a carrier-scale positive slice must come from a deeper collateral
cluster or from another completion/localization term not already proved
subcarrier.  A near-tie pair can do this in the abstract hyperbolic fixture,
but its required orientation has not been realized in the normalized
two-pair Gabor class or proved for the actual zeta data.

Thus the slice is a legitimate zero-independent **diagnostic**, after
conditioning on the target, but no carrier-scale lower bound for the actual
high-height slice is currently proved.  It is also the upper envelope of
every quotient obtained by nulling more positive rows: a subcarrier upper
bound here would be decisive without ever constructing the unknown
all-zero quotient, whereas a positive lower value would only admit a
reservoir which additional rows could still delete.

## 2. The actual finite completed operator

Let

```text
H_T=E_-,T direct_sum E_+,T                         (2.1)
```

be any finite endpoint-flat two-lobe Gabor coefficient space for which the
completed explicit formula has been invoked.  On its complexification write

```text
Q_T(f)=Pole_T(f)+Arch_T(f)-Prime_T(f)
      =<f,K_ar,T f>.                                (2.2)
```

The arithmetic matrix is zero-independent.  In the repository's correlation
convention, for `f=ell+r`, its cross block is specified exactly by

```text
Lambda_pr,r(ell)
 =sum_(n: log n in I_+-I_-)
    Lambda(n)/sqrt(n)
      *integral ell(u)*conj(r(u+log n))du,

Lambda_pole,r(ell)
 =A_+(ell)*conj(A_-(r))+A_-(ell)*conj(A_+(r)),

Lambda_arch,r(ell)
 =integral m(xi)*F_ell(xi)*conj(F_r(xi))dxi,

Lambda_comp,r
 =Lambda_pole,r+Lambda_arch,r-Lambda_pr,r.          (2.3)
```

Thus

```text
Q_cross,T(ell,r)=2*Re Lambda_comp,r(ell).           (2.4)
```

Compact support makes the prime sum in (2.3) finite.  Equations (2.2)--(2.4)
retain every prime power, both pole evaluations, the archimedean multiplier,
and the absolute target phase.

For a putative zero

```text
rho_0=1/2+alpha+i*gamma,
```

the reflected-pair contribution has the exact hyperbolic factorization
(1.3).  Let `i_T:S_T->H_T` be the isometric inclusion in (1.1), put

```text
a_T=i_T^* y_0,
N_T=2*a_T*a_T^*,
kappa_T=2*||a_T||^2.                                (2.5)
```

The selected pair becomes a pure negative square on the quotient:

```text
i_T^* K_0,T i_T=-N_T.                              (2.6)
```

Consequently (1.4) is equivalently characterized by the exact identity

```text
i_T^* K_ar,T i_T=-N_T+R_full,T.                    (2.7)
```

This is the canonical full-form carrier decomposition.  It is valid without
choosing or nulling any collateral positive row.

## 3. Exact carrier-slice theorem

For `0<=eta<=kappa_T`, define

```text
F_eta={Gamma>=0 on S_T:
         Tr Gamma=1,
         Tr(N_T Gamma)>=eta},

h_eta(R)=max_(Gamma in F_eta) Tr(R Gamma).          (3.1)
```

### Theorem 3.1 (pure-state, scalar-dual, and rank-one-carrier reduction)

Let `R=R^*` on `S_T` and `0<=eta<kappa_T`.  Then

```text
h_eta(R)
 =max_(||z||=1, <z,N_T z>>=eta) <z,Rz>
 =inf_(mu>=0)
    [lambda_max(R+mu*N_T)-mu*eta].                 (3.2)
```

At `eta=kappa_T`, if `a_hat=a_T/||a_T||`, then

```text
h_kappa_T(R)=<a_hat,R*a_hat>.                       (3.3)
```

Write

```text
S_T=C*a_hat direct_sum H_perp,
R=[[r_0,b^*],[b,D]],
r_0=<a_hat,R*a_hat>,        b=P_perp*R*a_hat.       (3.4)
```

For `eta=theta*kappa_T`, `0<=theta<=1`, one has the exact formula

```text
h_(theta*kappa_T)(R)
 =max_(theta<=x<=1, ||w||=1 in H_perp)
    [x*r_0+(1-x)*<w,Dw>
      +2*sqrt(x*(1-x))*abs(<b,w>)].                (3.5)
```

The terms with `w` are omitted at `x=1`, and the evident one-dimensional
interpretation applies when `H_perp={0}`.  In particular,

```text
h_(theta*kappa_T)(R)
 <=max_(theta<=x<=1)
    [x*r_0+(1-x)*lambda_max(D)
      +2*sqrt(x*(1-x))*||b||].                     (3.6)
```

For every unit `w in H_perp`, the expression in (3.5) at `x=theta` is a
rigorous lower bound.  Hence (3.5) separates the three possible sources of a
carrier-scale positive slice:

```text
carrier diagonal r_0,
positive complement edge lambda_max(D),
transverse coupling ||b||.                         (3.7)
```

#### Proof

The feasible state set is compact.  At an extreme point of rank `r>=2`,
Hermitian perturbations on the range have real dimension `r^2` and obey at
most the two active affine equations `Tr Delta=Tr(N_T Delta)=0`.  A nonzero
two-sided feasible perturbation exists, contradicting extremality.  Thus a
linear objective has a rank-one optimizer.

For every feasible `Gamma` and `mu>=0`,

```text
Tr(R Gamma)
 <=lambda_max(R+mu*N_T)-mu*eta.                    (3.8)
```

When `eta<kappa_T`, mixing the top carrier state with a sufficiently small
full-rank state gives a primal Slater point, so finite-dimensional SDP
duality gives equality.  At `eta=kappa_T`, equality in
`Tr(N_T Gamma)<=kappa_T Tr Gamma` forces support on `C*a_hat`, proving
(3.3).  Finally every unit vector has the form

```text
z=sqrt(x)*a_hat+e^(i*phi)*sqrt(1-x)*w,
```

and optimizing `phi` gives (3.5).  Replacing the two `w`-dependent terms by
their separate maxima gives (3.6).  QED

### Corollary 3.2 (exact full-form screening functional)

Define

```text
q_eta=max_(Gamma in F_eta) Tr(K_ar,T Gamma).        (3.9)
```

Then, by (2.7),

```text
q_eta
 =max_(Gamma in F_eta) Tr((R_full,T-N_T)Gamma)
 =inf_(mu>=0)
    [lambda_max(R_full,T+(mu-1)*N_T)-mu*eta]        (3.10)
```

for `eta<kappa_T`, with the corresponding top-carrier restriction at the
boundary.  Moreover,

```text
q_eta<=h_eta(R_full,T)-eta.                         (3.11)
```

Thus

```text
h_eta(R_full,T)<eta                                (3.12)
```

is a rigorous sufficient certificate that every state in the carrier slice
has negative completed form.  Conversely, the existence of a nonnegative
completed state in the slice forces `h_eta(R_full,T)>=eta`.  The latter is
only a necessary test; the exact sign test is (3.10).

At full carrier, (3.3) and (2.7) give the especially simple arithmetic
identity

```text
h_kappa_T(R_full,T)
 =<a_hat,K_ar,T*a_hat>+kappa_T
 =Q_T(a_hat)+kappa_T.                               (3.13)
```

This is an exact finite von-Mangoldt/pole/gamma scalar, not a collateral-zero
ansatz.

### Corollary 3.3 (the target-only slice is the noncircular upper envelope)

Let `S_prime` be any further positive-row quotient with

```text
S_prime subset S_T,                                (3.14)
```

and compress `N_T,R` to `S_prime`.  For every threshold for which the smaller
slice is nonempty,

```text
h_eta^(S_prime)(R|S_prime)<=h_eta^(S_T)(R).         (3.15)
```

Indeed every state supported on `S_prime` is also a state supported on
`S_T`, with the same two trace pairings.  Thus a prime-side subcarrier upper
bound on the target-only slice automatically survives the imposition of all
additional, even unknown, positive rows.  The converse is false: a positive
direction found in the larger target-only quotient may be deleted by a
collateral positive row.  Consequently a carrier-scale **lower** value of the
noncircular slice is an admission result, not yet a construction on the
all-positive-row quotient.

## 4. The aggregate-cross slice on the exact mirror packet

The aggregate proposal uses only the lobe-cross block, so it needs one extra
geometric input.  On the exact normalized two-packet mirror compression in
the repository,

```text
M_0=m_T*[[1,C_T],[C_T,1]],
C_T=cosh(alpha*D_T)>1,
e_+=(u+v)/sqrt(2),       e_-=(u-v)/sqrt(2).         (4.1)
```

After adjoining only directions in the common kernel of the **four
lobe-restricted** selected rows `x_0^-`, `x_0^+`, `y_0^-`, and `y_0^+`, the
positive-null object is

```text
S_mir,T=C*e_- direct_sum W_T.                       (4.2)
```

The lobe-restricted qualification is essential.  Membership merely in the
global kernels of `x_0^*` and `y_0^*` makes the full selected-pair operator
vanish on the added direction, but its same-lobe and cross pieces can still
cancel there separately; it does not make the cross observable reduce the
mirror plane.

Put

```text
N_mir,T=kappa_T*e_-e_-^*,       kappa_T=m_T*(C_T-1),
b_T=m_T*C_T,
c_T=b_T/kappa_T=C_T/(C_T-1).                        (4.3)
```

If `B_0,T` is the selected lobe-cross observable, then exactly

```text
B_0,T|S_mir,T=-c_T*N_mir,T.                         (4.4)
```

Let `B_ar,T` be the Hermitian cross operator specified by (2.3)--(2.4), and
define the actual cross remainder

```text
R_cross,T=P_(S_mir,T)*(B_ar,T-B_0,T)*P_(S_mir,T).  (4.5)
```

Again, (4.5) is assembled from actual primes and completion, not from a list
of collateral zeros.  Under the same target-is-an-actual-zero hypothesis as
in (1.5), the explicit formula identifies it with the on-line and collateral
cross operator.

In this section, `F_eta` denotes the slice on `S_mir,T` defined using
`N_mir,T` (rather than the full-form objects `S_T,N_T` of Section 3).

For every `Gamma in F_eta`, exact aggregate cancellation is

```text
0=Tr(B_ar,T Gamma)
 =Tr((R_cross,T-c_T*N_mir,T)Gamma).                 (4.6)
```

Consequently it necessarily obeys

```text
h_eta(R_cross,T)>=c_T*eta.                          (4.7)
```

The exact one-sided crossing functional is sharper:

```text
q_cross,eta
 =max_(Gamma in F_eta)Tr(B_ar,T Gamma)
 =inf_(mu>=0)
    [lambda_max(R_cross,T+(mu-c_T)*N_mir,T)
      -mu*eta].                                     (4.8)
```

If (4.8) is negative, no carrier-retaining aggregate-null state exists.  If
it is nonnegative, cancellation additionally requires a feasible state with
nonpositive aggregate value.  Thus (4.7), like the original carrier-support
proposal, is a necessary fail-fast gate rather than a sufficient completed
positivity theorem.

At full carrier,

```text
h_kappa_T(R_cross,T)
 =<e_-,B_ar,T e_->+b_T
 =2*Re Lambda_comp,r_-(ell_-)+b_T,                 (4.9)
```

where `e_-=ell_-+r_-` is split between the two lobes.  Formula (4.9) is the
smallest actual zero-independent high-height computation: one finite prime
sum and the two completion integrals.  No such high-height matrix or scalar
fixture is presently stored in the repository.

The exact same-lobe diagonal `m_T I` of (4.1) has support `m_T`; relative to
the aligned bill `b_T` its fraction is `1/C_T=sech(alpha D_T)`.  This proves
that the selected diagonal is subcarrier.  It does **not** bound the actual
remainder (4.5).

## 5. Rigorous depth reduction

The zero-side interpretation supplies one asymptotic theorem, with a precise
scope.

Let the selected pair have depth `alpha`, packet separation `D_T=dL+O(1)`,
and carrier `kappa_T=X^(alpha*d+o(1))/L`.  In the target dyadic band, write

```text
R_band,T=R_deep,T+E_shallow,T,                      (5.1)
```

where `R_deep,T` is the compression of collateral pair operators with

```text
beta>alpha*d-epsilon                               (5.2)
```

and `E_shallow,T` contains the on-line rows and the remaining collateral
pairs in that band.  The normalized strip-sampling lemma and the unit-window
zero count give

```text
||E_shallow,T||
 <=X^(alpha*d-epsilon+o(1))*L^O(1)+L^O(1)
 =o(kappa_T).                                       (5.3)
```

Orthogonal compression and taking a lobe-cross block cannot increase this
bound.  Hence (5.3) applies to both the full-form and cross versions of the
band remainder.

For a fixed feasible set, carrier support is one-Lipschitz in operator norm:

```text
abs(h_eta(R+E)-h_eta(R))<=||E||.                    (5.4)
```

It follows that, uniformly in `0<=eta<=kappa_T`,

```text
h_eta(R_band,T)=h_eta(R_deep,T)+o(kappa_T).         (5.5)
```

In particular, if the deep set (5.2) is empty, then

```text
h_eta(R_band,T)=o(kappa_T).                         (5.6)
```

For any fixed carrier fraction `eta=theta*kappa_T`, `theta>0`, (5.6)
fails the necessary aggregate condition (4.7), and it also gives the
full-form sufficient inequality (3.12) for the band operator.

Equation (5.5) is not silently promoted to the entire completed remainder.
Any remote-zero tail, collar contribution, coherent inter-scale term, or
completion term for which an `o(kappa_T)` **operator-norm** estimate has not
been proved remains in an open summand `R_open,T`.  The honest full statement
is

```text
h_eta(R_actual,T)
 =h_eta(R_deep,T+R_open,T)+o(kappa_T).              (5.7)
```

whenever the already-audited subcarrier pieces are placed in the error.
Scalar bounds on one packet do not imply the operator-norm bound needed to
remove a term from (5.7).

The near-tie abstract two-pair fixture shows that `R_deep,T` can have a
carrier-scale positive slice while changing count, trace, and Frobenius
ledgers only by lower-order amounts.  What remains open is whether that
three-coordinate orientation occurs in a normalized two-pair Gabor
restriction or in the actual zeta divisor.  Existence of a pair satisfying
(5.2) is necessary for the band reservoir, not sufficient for its sign.

## 6. What is and is not circular

There are three logically distinct constructions.

1. **Target-conditioned prime-side slice.**  Equations (1.1)--(1.4) use the
   putative target and the actual arithmetic coefficients.  This is a valid
   conditional object and can be evaluated without knowing any other zero.
2. **All-positive-row divisor quotient.**  Taking the kernel of every actual
   off-line positive row can be useful after assuming a complete divisor
   configuration, but it is not a zero-independent arithmetic metric or
   quotient.  Using its favorable geometry as an input would be circular.
3. **Collateral spelling of the remainder.**  Equation (1.5) is an exact
   consequence of the completed explicit formula.  It explains the depth
   obstruction, but an estimate inferred from an invented collateral
   configuration is not thereby an estimate for the actual prime-side
   matrix (1.4).

Accordingly, a carrier-scale value of (3.2) or (4.7) can in principle be
certified with no collateral-zero input by assembling (1.4) or (4.5).  The
repository has not yet done that at high height, and its current coefficient
bounds provide neither a uniform carrier-scale lower bound nor a uniform
subcarrier upper bound for the open operator in (5.7).

## 7. Focused theorem card

The next admissible computation or theorem is now exact.

```text
INPUT
  A hypothetical target (alpha,gamma), a fixed endpoint-flat two-lobe Gabor
  synthesis, and the actual pole/gamma/von-Mangoldt coefficients.

BUILD
  S_T=ker x_0^*,
  N_T=2(P_S y_0)(P_S y_0)^*,
  R_full,T=P_S(K_pole+K_arch-K_prime-K_0)P_S,
  and, on the exact mirror object,
  R_cross,T=P_S(B_pole+B_arch-B_prime-B_0)P_S.

EVALUATE
  h_(theta*kappa_T) from either the scalar dual (3.2) or the exact
  rank-one-carrier formula (3.5).  For the completed sign use (3.10); for
  aggregate crossing use (4.8), not only the necessary norm test.

CERTIFY
  Interval bounds on the finite prime sum and completion integrals, plus an
  operator-norm tail estimate if the synthesis is not exactly finite on the
  divisor side.

DECIDE
  subcarrier: the proposed positive reservoir is ruled out at that carrier
              fraction;
  carrier-or-larger: identify whether the contribution is carrier-diagonal,
              complement-positive, or transverse via (3.5), and then pay
              the full completed-form cost.
```

This theorem card reduces the high-height carrier proposal to a concrete
arithmetic matrix and a one-dimensional eigenvalue minimization.  It does
not supply the missing arithmetic sign.

Principal inputs:

- [`ZETA23-AGGREGATE-CROSS-PRIME-ROW-AUDIT-2026-08-11.md`](ZETA23-AGGREGATE-CROSS-PRIME-ROW-AUDIT-2026-08-11.md),
- [`ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md`](ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md),
- [`ZETA23-COLLATERAL-RESERVOIR-DICHOTOMY-2026-08-12.md`](ZETA23-COLLATERAL-RESERVOIR-DICHOTOMY-2026-08-12.md),
- [`ZETA23-MULTIWITNESS-MULTISCALE-AGGREGATE-CANCELLATION-AUDIT-2026-08-12.md`](ZETA23-MULTIWITNESS-MULTISCALE-AGGREGATE-CANCELLATION-AUDIT-2026-08-12.md), and
- [`ZETA23-CARRIER-SLICE-SUPPORT-FINITE-FIXTURE-2026-08-12.md`](ZETA23-CARRIER-SLICE-SUPPORT-FINITE-FIXTURE-2026-08-12.md).
