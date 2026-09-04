# QP four-cycle: exact Markov lift and adaptive packet equilibrium

**Date:** 2026-08-29

## Verdict

There are two necessary audit requirements for any replacement of the
present `A2/A4` interface.

1. Its globally reconstructed source must equal `m(C)w(C)`, rather than the
   stronger factorial source.  The complete `J/m(C)` pair lift, with its
   diagonal charged to the occupied-color baseline, is one canonical way to
   accomplish this; it is not the unique legal normalization.
2. Any claim of necessity must retain the same rank-one color weight on both
   sides.  Replacing that weight by two independent maximum pair loads is a
   strictly stronger sufficient relaxation.

Neither correction proves a new arithmetic estimate.  With unrestricted
singleton packets, the best adaptive packet certificate is identically the
original positive fourth trace.  Conversely, restricting the packet library
to affine/Hankel or other physical carriers creates genuine mathematical
content, but also creates a sufficient structural conjecture which is
strictly stronger than the scalar endpoint.  This distinction is the stable
fixed point of the audit.

## 1. Exact positive source

Put

```text
kappa(a,b,c)=1_(|8abc-q^3|<=qD),
A_z(a,b)=sum_c z_c kappa(a,b,c).
```

The raw fourth Schatten trace is

```text
sum_(a1,a2,b1,b2) sum_(c11,c12,c21,c22)
 kappa(a1,b1,c11) kappa(a1,b2,c12)
 kappa(a2,b1,c21) kappa(a2,b2,c22)
 conjugate(z_c11) z_c12 z_c21 conjugate(z_c22).
                                                               (1.1)
```

For an oriented color rectangle

```text
C=(c11,c12;c21,c22)
```

let `Gamma(C)` be its physical completion occurrences
`X=(a1,a2,b1,b2)` satisfying the four displayed hard windows, and put

```text
m_C=|Gamma(C)|,
w_z(C)=|z_c11 z_c12 z_c21 z_c22|.
```

Termwise absolute values give the exact positive majorant

```text
F_+(z)=sum_C m_C w_z(C).                             (1.2)
```

It is an equality with (1.1) for nonnegative `z`.  Thus a uniform bound
`F_+(z)<<Dq^o(1)||z||_2^4` is the positive four-cycle endpoint; no pair
factorial is present in its source.

All occurrence-level exceptional reductions must be made before defining
`m_C`.  More precisely, if a proved positive baseline removes a set
`Gamma_base(C)`, define

```text
Gamma_res(C)=Gamma(C)\Gamma_base(C),
r_C=|Gamma_res(C)|.                                  (1.3)
```

Then the source splits linearly as the baseline occurrence mass plus
`sum_C r_C w_z(C)`.  A pair-level deletion made after (1.3) does not change
`r_C`; it must partition, rather than silently delete, the pair source below.

## 2. Exact reciprocal-multiplicity lift

For every `C` with `r_C>0`, give every ordered pair
`(X,X') in Gamma_res(C)^2` coefficient `1/r_C`.  Then

```text
sum_(X,X') 1/r_C =r_C,

sum_C sum_(X,X') w_z(C)/r_C
 =sum_C r_C w_z(C).                                 (2.1)
```

This is the complete Markov kernel `J/r_C` on the completion fiber.  It is
positive semidefinite and has every row sum equal to one.  A partition by
the **source row** can therefore be made without changing its scalar mass.
This does not mean that arbitrary completion peels or pair-cell restrictions
commute atomwise with the lift: renormalizing a smaller fiber changes all of
its coefficients, while restricting `J/r_C` to a signed cell generally
destroys both row stochasticity and positive semidefiniteness.

Split (2.1) into diagonal and off-diagonal pairs:

```text
W_res(z)=sum_(C:r_C>0) w_z(C),

N_res(z)=sum_C sum_(X!=X') w_z(C)/r_C
        =sum_C (r_C-1)w_z(C),

sum_C r_Cw_z(C)=W_res(z)+N_res(z).                  (2.2)
```

The existing determinant-layer theorem gives

```text
W_res(z)<=W_full(z)<<Dq^o(1)||z||_2^4.             (2.3)
```

Thus, for this particular lift, only `N_res` needs a new estimate.  The alternative weight
`1/(r_C-1)` on ordered distinct pairs is also exact for `r_C>=2`, but is
singular at one and its completion-label matrix is not positive
semidefinite.  Equation (2.2) is the cleaner interface because (2.3) is
already available.  More generally, any row-stochastic comparison kernel,
or a proof which never introduces completion pairs, is legal.  Reciprocal
multiplicity is therefore a useful canonical choice, not a logically
mandatory representation.

If unordered pairs are used, their coefficient is `2/r_C`.  Mixing that
convention with the ordered `1/r_C` convention introduces a factor-two
error.

### 2.1 Baseline admission rule

Only a theorem for a literal positive subcollection of (1.2) may be
subtracted from this positive source.  The following uses are safe.

* The proved repeated-node, permutation, square-edge, and corresponding
  equality sectors may be removed by their occurrence IDs.
* The occupied-fiber term (2.3) is safe after every further positive
  deletion.  In particular the complete `r_C<=2` part costs at most
  `2W_res` and may be removed if desired.
* A direct affine completion patch may be removed on a finite instance only
  when every occurrence is assigned once and its global direct-trace charge
  is certified.  The still-open global `H_aff` packing assertion is not a
  proved baseline.

A cancellation theorem for a transformed signed expression is not, merely
by itself, a positive baseline for (1.2).  Thus the random-sign square
function, a tangent theorem in a different tensor coordinate, or a local
affine host theorem must first be supplied with an exact positive source
map before it is entered in this ledger.

## 3. Completeness and sector order

Let

```text
E_res={(C,X,X'): X,X' in Gamma_res(C), X!=X'}.
```

Each atom `e` has source coefficient

```text
rho_e=1/r_C.                                        (3.1)
```

Completion predicates, such as the eight-distinct predicate, must already
have been applied in (1.3).  Pair predicates may now partition `E_res` by

```text
signed determinant cell,
zero/nonzero carrier secants,
the four positional masks,
or a physical packet carrier.                       (3.2)
```

Every atom must occur exactly once across the pair-sector source manifests.
An `external_sectors` string is not a charge.  In particular, zero-secant
atoms cannot be omitted unless their normalized mass has an explicit proved
baseline certificate.  Reversal `X<->X'` changes `(A,B)` to `(-A,-B)`;
both oriented atoms remain in the ordered source.  A single signed cell is
neither row-stochastic nor generally positive semidefinite.  Consequently
the global `J/r_C` Gram interpretation cannot be imported into an individual
cell, parity class, or post-Rademacher block without a separate argument.
For example, in a three-point fiber the reversal-closed subcell containing
only `(X_1,X_2)` and `(X_2,X_1)` has completion matrix
`(E_12+E_21)/3`, with eigenvalues `1/3,-1/3,0`.

A cell-local digest cannot verify (2.1).  The family-level manifest must
record each residual fiber, its full occurrence list, `r_C`, all diagonal
baseline atoms, and all ordered off-diagonal atoms across sibling cells.

## 4. Exact packet reconstruction

Write the two oriented color-pair vertices of `C` as

```text
gamma(C)=(c11,c12),       eta(C)=(c21,c22),
p_(c,d)=|z_c z_d|.
```

Then

```text
N_res(z)=sum_(e in E_res) rho_e p_gamma(e)p_eta(e). (4.1)
```

Fix a physical packet library independently of `z`.  A legal allocation is
a finite collection of packets and numbers `theta_(t,e)>=0` such that

```text
theta_(t,e)>0 only when e is licensed by packet t,
sum_t theta_(t,e)=rho_e for every e.                (4.2)
```

Define the nonnegative packet matrix

```text
K_t(gamma,eta)=sum_(e with endpoints gamma,eta) theta_(t,e).
                                                               (4.3)
```

Equations (4.1)--(4.3) give exact source conservation:

```text
N_res(z)=sum_t <p,K_t p>.                           (4.4)
```

There is no legal uncharged remainder.  A remainder is allowed only if its
term IDs, rational coefficients, and an independent `O(D)` theorem are
serialized.

The packet library may contain only carriers with an independently verified
physical predicate and a local theorem for the exact kernel (4.3).  The
exact-secant partial matching is the current serialized example.  Existing
four-edge affine/Hankel host and fixed-direction results may motivate further
candidates, but they are admissible here only after an atom-level lift and a
local bound for their allocated normalized kernel have been checked; a
direct trace estimate for a completion patch is not automatically such a
certificate.  A projected token line which has not been lifted to the four
physical windows is not a packet.  The known non-affine-witness examples
rule out that shortcut.

## 5. The rank-one weighted equilibrium certificate

Normalize

```text
Z=||z||_2^2,       x_c=|z_c|^2/Z,
mu_(c,d)=x_c x_d,  sum_(c,d)mu_(c,d)=1.             (5.1)
```

### 5.1 Exact marginal version

For (4.3), let

```text
r_t(gamma)=sum_eta K_t(gamma,eta),
c_t(eta)=sum_gamma K_t(gamma,eta),

U_t(x)=sum_gamma r_t(gamma)mu_gamma,
V_t(x)=sum_eta c_t(eta)mu_eta.                      (5.2)
```

Cauchy over the weighted packet edges gives

```text
<p,K_t p>^2<=Z^4 U_t(x)V_t(x).                     (5.3)
```

For arbitrary positive balances `lambda_t`, a second Cauchy inequality gives

```text
N_res(z)^2/Z^4
 <=(sum_t lambda_t U_t(x))
   (sum_t lambda_t^(-1)V_t(x)).                    (5.4)
```

For fixed packets and `x`, the infimum over balances is exact:

```text
inf_lambda RHS of (5.4)
 =(sum_t sqrt(U_t(x)V_t(x)))^2.                    (5.5)
```

Packets with `U_tV_t=0` contribute zero and may be omitted from (5.5).

### 5.2 Relation to the present A4 certificate

If only a support and Schur maxima are retained, put

```text
R_t=max_gamma r_t(gamma),
C_t=max_eta c_t(eta),
a_t^2=R_t C_t,

U_t^supp=sum_(gamma in L_t)mu_gamma,
V_t^supp=sum_(eta in R_t)mu_eta.
```

Then

```text
U_t<=R_t U_t^supp,       V_t<=C_t V_t^supp,

sqrt(U_tV_t)<=a_t sqrt(U_t^supp V_t^supp).         (5.6)
```

The current A4 maximum-load theorem further bounds the two sums uniformly
over two independent pair vertices.  Therefore the implication hierarchy is

```text
legacy maximum pair-load A4
 => support/a_t common-x equilibrium
 => exact-marginal common-x equilibrium
 => the direct positive source.                    (5.7)
```

The first two arrows can be strict on harmless star configurations.

The cover, its allocations, and the balances may depend on `x`: the desired
bound has quantifiers `for every z, there exists a certificate`.  The packet
library and every local packet theorem must remain fixed and uniform in
`z`.  This adaptivity does not disturb (4.2) or (4.4), but it is only one
possible sufficient proof architecture, not a canonical dual formulation of
the endpoint.

## 6. Sufficiency theorem

Fix the exact residual occurrence manifest and a fixed physical packet
library.  Suppose that for every probability vector `x` on the shell there
is an allocation satisfying (4.2) and positive balances satisfying

```text
(sum_t lambda_t U_t(x))
(sum_t lambda_t^(-1)V_t(x))
 <<D^2q^o(1).                                       (6.1)
```

Then (5.4), (2.2), and the proved baseline (2.3) imply

```text
F_+(z)<<Dq^o(1)||z||_2^4.                          (6.2)
```

Together with the proved positive exceptional-sector bounds, (6.2) implies
the sharp fourth-cycle estimate.

The same conclusion follows from the support/a_t version with `a_t^2` in
the second sum.  Numerically, the equilibrium target is `D` after taking a
square root, while the serialized product target remains `D^2`.

## 7. The tautology boundary

The sufficiency theorem is an interface, not yet a new theorem.  If the
packet library contains every singleton source atom, take one packet per
atom.  Both inequalities in (5.3)--(5.5) are then equalities, so

```text
inf_(all unrestricted covers) sum_t sqrt(U_tV_t)
 =N_res(z)/Z^2.                                     (7.1)
```

Consequently the assertion that an unrestricted adaptive cover has
equilibrium cost `O(D)` is exactly the positive four-cycle assertion under
a new name.

If singleton fallback is forbidden and the library is restricted to
affine/Hankel or another fixed geometric class, (6.1) is no longer
tautological.  It is also no longer necessary: the scalar endpoint could
hold through cancellation, diffuse rank-one geometry, or another packet
class.  Such a statement must be presented as a route-specific sufficient
conjecture, not as the minimal equivalent endpoint.

The same warning applies to each of the following:

```text
maximum pair-load A4,
GACCT/NDS/RDP or a dominant-line cover,
polynomial affine capture of every excess,
arbitrary-Hilbert--Schmidt-dual residual reduction,
all-plus/random-sign unconditionality,
or a packet-versus-remainder comparison.            (7.2)
```

Each can be a useful proof route, but each imposes structure not supplied by
the `D`-scale scalar endpoint.

### 7.1 Smallest non-tautological assertion inside the packet route

Once a particular physical library and a finite list of source-preserving
local reassignment/merge moves have been frozen, a genuinely new statement
can be made without restoring the maximum-load quantifier:

> **Adaptive profitable-move assertion.**  There are
> `kappa=q^(-o(1))` and `C_epsilon` such that, for every `x` and every legal
> source-preserving packet state of exact-marginal cost `E_x`, if
> `E_x>C_epsilon Dq^epsilon`, one allowed physical move produces another
> state with
>
> ```text
> E_x'-C_epsilon Dq^epsilon
>  <=(1-kappa)(E_x-C_epsilon Dq^epsilon).            (7.3)
> ```

Starting from the canonical singleton or exact-secant state, iteration of
(7.3) produces (6.1).  The move may depend on `x`, but its destination must
belong to the fixed library and must conserve every coefficient in (4.2).

This is smaller than a dominant-line cover, cardinal Carleson theorem, or
arbitrary-dual extractor: it asks only for a profitable physical move at an
actual rank-one overload.  It is also plainly conjectural and stronger than
the endpoint.  A harmless endpoint family need not possess any move in a
chosen affine library.  Accordingly (7.3) is the cleanest route-specific
inverse target, not a logically necessary reformulation of four-cycle.

## 8. Stable schema and experimental action

A v2 source schema needs

```text
residual fiber ID and oriented colors,
full residual completion occurrence manifest,
r_C and exact source coefficient [1,r_C],
source/comparison completion roles,
diagonal occupied-fiber baseline certificate,
family-level ordered-pair completeness digest,
explicit pair-sector allocations including zero secants,
packet-library version and physical proof type,
exact packet row and column marginal profiles,
x (for a finite adaptive certificate), lambda,
the exact common-x product,
and rational upper slacks for any square roots.      (8.1)
```

For a profitable-move certificate, serialize the before/after allocation
ledgers, their exact common source digest, both weighted costs, and the
declared contraction.  A pass or failure of one chosen allocation does not
settle the existential library theorem.  Its negative certificate must
lower-bound the infimum over every allowed reassignment.  The present A4
dual, which dualizes independent maximum pair loads for a fixed cover, is
not such a certificate.

General operator fields `R,Y` are not required for a complete positive
pure-state certificate.  If a partial stopping-time experiment is retained,
the natural data are the residual atom manifest, the same `x`, captured
positive source, and residual positive source.  An arbitrary dual `Y`
belongs to the stronger vector-valued A2/A3 route and should not be made a
condition of this interface.

If the packet route is retained, a conservative next experiment is:

1. implement the exact v2 `1/r_C` family manifest and diagonal baseline;
2. add the exact-marginal common-`x` evaluator beside legacy A4;
3. freeze particular physical packet/merge rules and test those rules on
   hostile controls and actual-prime fixtures;
4. interpret failure as failure of that route, and a finite pass only as a
   sanity check;
5. do not claim a packet inverse or remainder theorem until a growing
   physical excess fixture or an independent arithmetic proof supplies it.

This is not uniquely forced by the endpoint.  A signed-cancellation,
vector-valued, or direct weighted-incidence route can legitimately bypass
the pair lift and its equilibrium oracle.  Without a frozen packet library,
implementing this evaluator is bookkeeping work rather than the uniquely
best mathematical next step.

The physical rank-one-gap experiment is not a substitute: current actual
fixtures have only bounded generic codegree, and constructing a power-rich
generic fixture already contains much of the missing inverse problem.

## 9. Source locations

The exact raw trace, physical pair factorization, and legitimacy of positive
deletions are recorded in
`ZETA23-QP-PHYSICAL-TENSOR-ABSOLUTE-DOMINATION-AND-CENTER-PARTICIPATION-GATE-2026-08-25.md`,
Sections 1--2.  The occupied-color bound used in (2.3) is imported in
`ZETA23-QP-HYBRID-AFFINE-COMPRESSION-TRANSFER-2026-08-29.md`, Section 2.
The current v1 atom schema and A4 maximum-load certificate are
`src/qp_a2_packet_serialization.py` and
`src/qp_a4_serialized_participation.py`, with their finite audit in
`ZETA23-QP-A2-SERIALIZATION-AND-A4-RERUN-2026-08-29.md`.
