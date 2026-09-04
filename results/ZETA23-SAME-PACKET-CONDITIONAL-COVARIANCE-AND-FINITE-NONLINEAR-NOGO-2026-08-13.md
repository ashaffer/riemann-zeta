# Same-packet reserve: finite nonlinear closure fails, and the minimum live enrichment is two-dimensional

Status: exact finite-power residue theorem, positive-covariance contact
rigidity, isolated-divisor countermodel, and exact two-channel actual-arithmetic
theorem card, 2026-08-13.  The actual von Mangoldt transverse coefficient is
not estimated.  No arithmetic reserve, zero-free strip, or RH statement is
proved.

## 1. Verdict

On the selected target-positive-null face write the completed arithmetic
operator as

```text
Q_ar=-N_rho+R_Lambda,rho,                            (1.1)
```

where `N_rho>=0` is the selected negative carrier.  For a normalized carrier
state `e` with

```text
N_rho=K_rho*e*e^*,
```

the missing theorem is

```text
<e,R_Lambda,rho e> >=epsilon*K_rho+o(K_rho).         (1.2)
```

Three natural attempts do not manufacture (1.2).

1. For every finite power `d>=2`, a holomorphic test which vanishes to order
   `d-1` at a selected simple zero makes the clean residue of
   `(xi'/xi)^d` exactly the residue of a differentiated **linear**
   logarithmic derivative.  Integration by parts returns the original linear
   detector.  Every unselected zero retains its Laurent-germ debt.
2. A finite positive Hermitian covariance of polynomial logarithmic-
   derivative features either keeps a positive pole contact or projects away
   the entire principal part.  Contact subtraction, an oriented derivative,
   or a finite-part extraction is indefinite.
3. The functional equation, conjugation, finite order, positive resolvents,
   and every such local covariance are also possessed by an isolated matched
   quartet.  Once that whole quartet is selected, its reserve is exactly zero.
   They therefore cannot imply a fixed positive fraction.

There is a sharp surviving enlargement.  Add one target-neutral coherent
channel `v`, and retain a fixed carrier fraction `eta`.  On
`span{e,v}`, the actual reserve has three entries

```text
r=<e,R e>,       c=<v,R v>,       z=<e,R v>.         (1.3)
```

The best phase gives exactly

```text
eta*r+(1-eta)*c+2*sqrt(eta*(1-eta))*abs(z).          (1.4)
```

Thus one extra coherent channel is sufficient if (1.4) is at least
`epsilon*eta*K_rho`; it is also the minimum dimensional escape from a failed
one-dimensional edge within the linear-quadratic packet class.  When
`r=o(K_rho)`, a fixed-fraction theorem requires `c_+` or `abs(z)` to be
carrier-sized.  This is not supplied by completion or covariance.  It is one
new signed actual-`Lambda` transverse correlation.

The research decision is therefore to replace the preselected scalar GA by a
**coupled two-dimensional GA/GP card**: construct one target-neutral `v`,
evaluate the actual arithmetic phase in (1.4), and make the compact geometric
transfer uniform for that same phase.  A positive incoherent ensemble loses
the `z` term and is strictly weaker.

## 2. Exact finite-power collapse

Let

```text
X(s)=xi'(s)/xi(s).
```

Near a zero `rho` of multiplicity `m`, put `w=s-rho` and write

```text
X(s)=m/w+a_0+a_1*w+... .                             (2.1)
```

### Theorem 2.1 (all clean finite powers are locally linear)

Let `d>=1`, and suppose that `H` is holomorphic with

```text
H(s)=h_(d-1)*w^(d-1)+O(w^d).                        (2.2)
```

Then

```text
Res_rho H*X^d=m^d*h_(d-1)                           (2.3)
```

and exactly the same residue is obtained from

```text
m^(d-1)*(-1)^(d-1)/(d-1)! * H*X^(d-1),             (2.4)
```

where the superscript on the last `X` denotes differentiation.  On a closed
contour, repeated integration by parts turns (2.4) into

```text
m^(d-1)/(d-1)! * H^(d-1)*X.                         (2.5)
```

For a simple zero, the nominal nonlinear detector is therefore precisely a
linear completed logarithmic-derivative detector after `d-1` integrations by
parts.

#### Proof

The only term which can pair with the zero of order `d-1` in (2.2) to create
a residue is the leading term

```text
X^d=m^d*w^(-d)+O(w^(-d+1)).                         (2.6)
```

This proves (2.3).  Also

```text
X^(d-1)=m*(-1)^(d-1)*(d-1)!*w^(-d)+O(1),           (2.7)
```

so (2.4) has the same leading coefficient `m^d*w^(-d)` and no other polar
terms.  Its residue against `H` is again (2.3).  Repeated contour integration
by parts gives (2.5).  QED

The qualification "selected" is essential.  At an unselected simple zero
`nu`, `H(nu)` need not vanish.  The difference between `X^d` and (2.4) then
has poles of orders at most `d-1`, whose coefficients are polynomials in the
regular Laurent germ

```text
a_(nu,0),a_(nu,1),... .                              (2.8)
```

For `d=2` this is the already audited `2*a_nu*H(nu)` term in the simple-zero
case.  Higher `d` replace it by higher Bell-polynomial debts; they do not
acquire a sign.  An unselected zero of multiplicity different from the
selected multiplicity may retain even the top-order pole, which is a
strictly larger debt rather than a cancellation.

The replay module verifies (2.3)--(2.4) exactly for arbitrary rational germs,
multiplicity three, and every `1<=d<=8`.  The unit tests extend this to
`d<=10` with a second germ.

## 3. Conditional positive covariance keeps contact or loses the detector

The preceding theorem concerns holomorphic contour residues.  A Hermitian
square has a different, equally rigid obstruction.

### Theorem 3.1 (positive principal-part rigidity)

Let a finite meromorphic feature vector have Laurent expansion

```text
F(w)=sum_(k=1)^D a_(-k)*w^(-k)+a_0+O(w),            (3.1)
```

and let `A>=0`.  Then

```text
E(w)=F(w)^* A F(w)                                  (3.2)
```

is bounded as `w->0` if and only if

```text
A^(1/2)*a_(-k)=0,       1<=k<=D.                    (3.3)
```

In that case

```text
lim_(w->0) E(w)=a_0^* A a_0>=0.                    (3.4)
```

#### Proof

Factor `A=B^*B`, so `E=norm(BF)^2`.  If the highest nonzero principal-part
vector of `BF` is `B*a_(-k)`, its squared norm gives a strictly positive
leading term of order `abs(w)^(-2k)`.  Therefore boundedness forces it to
vanish.  Descend through the remaining principal parts to obtain (3.3).
The converse and (3.4) are immediate.  QED

For the same-point polynomial feature

```text
F=(1,X,X^2,...,X^D),                                (3.5)
```

Theorem 3.1 says something even simpler.  After a Cholesky factorization,
the energy is a positive sum

```text
sum_j w_j*abs(P_j(X))^2,       w_j>0.               (3.6)
```

If any `P_j` is nonconstant, its highest degree contributes a strictly
positive pole contact.  A bounded covariance has only constant rows.  The
checker computes this leading coefficient directly.

General conditional covariance can project onto the joint kernel in (3.3)
and retain the regular-germ square (3.4).  That is a legitimate positive
quantity, but it is not the oriented finite residue (2.3), nor is it the
linear reserve (1.2).  Recovering either by subtracting the contact,
polarizing a derivative, or taking a finite part is a difference of positive
squares and loses the sign.  This is the all-finite-feature form of the
previous `|X|^2` contact obstruction.

## 4. Sharp coefficient-free countermodel

Fix `0<alpha<1/2` and `gamma>0`, and put

```text
Xi_(alpha,gamma)(s)
 =[(s-1/2)^2-(alpha+i*gamma)^2]
  *[(s-1/2)^2-(alpha-i*gamma)^2].                   (4.1)
```

This real entire polynomial obeys

```text
Xi(1-s)=Xi(s),       conjugate(Xi(conjugate(s)))=Xi(s),  (4.2)
```

and its divisor is exactly the matched quartet

```text
1/2 +/- alpha +/- i*gamma.                          (4.3)
```

To the right of the divisor, the real part of its logarithmic derivative is
a sum of positive Poisson kernels.  Thus functional-equation symmetry,
reality, finite order, local Laurent identities, and the usual right-side
positive resolvent structure do not distinguish it from the abstract inputs
used in the proposed covariance arguments.

Select the whole quartet, with multiplicity.  There is no unselected divisor,
so

```text
R_other=0                                           (4.4)
```

exactly.  Every inequality `R_other>=epsilon*K` with `epsilon>0` fails.

This is not an Euler-product model and does not share zeta's actual gamma and
prime terms.  Its scope is precise: it rules out a derivation from completion,
functional-equation pairing, positive covariance, or finite-order local
identities alone.  A successful theorem must use a property which (4.1) does
not possess--in the present normalization, an actual von Mangoldt
correlation.

The whole selected multiplicity must also be marked.  If only one copy of a
multiple selected zero is removed, every unmarked copy contributes another
negative selected row.  No uniform positive reserve can be stated before
this confluent bookkeeping is fixed.

## 5. The minimum coherent enrichment

The next theorem identifies the smallest remaining quadratic packet rather
than merely saying that "more covariance" is needed.

### Theorem 5.1 (exact two-channel reserve)

Let `e,v` be orthonormal vectors in the selected-positive-null space, with

```text
N=K*e*e^*,       N*v=0,       K>0.                 (5.1)
```

Let `R=Q_ar+N`, and define

```text
r=<e,R e>,       c=<v,R v>,       z=<e,R v>.        (5.2)
```

For `0<eta<1`, set

```text
q_phi=sqrt(eta)*e+exp(i*phi)*sqrt(1-eta)*v.          (5.3)
```

Then

```text
<q_phi,N q_phi>=eta*K,                              (5.4)
```

and

```text
max_phi <q_phi,R q_phi>
 =eta*r+(1-eta)*c
  +2*sqrt(eta*(1-eta))*abs(z).                      (5.5)
```

A maximizing phase is `phi=-arg z`.  Consequently this two-dimensional
family contains a state satisfying the fractional reserve precisely when

```text
eta*r+(1-eta)*c
 +2*sqrt(eta*(1-eta))*abs(z)
 >=epsilon*eta*K.                                   (5.6)
```

#### Proof

Expand the Hermitian quadratic form in (5.3).  Its cross term is

```text
2*sqrt(eta*(1-eta))*Re(exp(i*phi)*z).               (5.7)
```

Maximizing (5.7) proves (5.5); (5.4) follows from (5.1).  QED

There is a useful necessary scale statement.  Put `c_+=max(c,0)`.  If (5.6)
holds, then

```text
max(c_+,abs(z))
 >=[(epsilon*eta*K-eta*r)_+]
   /[(1-eta)+2*sqrt(eta*(1-eta))].                  (5.8)
```

Thus, if the original scalar has `r=o(K)` and `eta` is fixed away from zero
and one, the transverse diagonal or mixed entry must be `Omega(K)`.  There is
no gain in the carrier exponent from merely adding one formal dimension.

An incoherent positive ensemble with covariance

```text
eta*e*e^*+(1-eta)*v*v^*                             (5.9)
```

has no mixed term.  Its reserve is only `eta*r+(1-eta)*c`.  Therefore the
complex coherence in (5.3), and specifically the actual phase of `z`, is the
smallest genuinely new datum.

There is a coordinate-free form useful for constructing `v`.  Let

```text
W=(selected-positive-null space) intersect ker(N) intersect e^perp,
w=P_W*R*e.                                           (5.10)
```

Then

```text
sup_(v in W, norm(v)=1) abs(<e,R v>)=norm(w).        (5.11)
```

If `w!=0`, the maximizing direction is `v=w/norm(w)` up to phase.  Thus the
new mixed arithmetic datum is exactly one **conditional Schur residual**,
not an unspecified matrix:

```text
Z_rho=norm(P_W*R_Lambda,rho*e).                     (5.12)
```

The transverse diagonal on that direction must still be retained.  If the
compression `C=P_W R P_W` has lower edge `-M`, the explicit sufficient
condition

```text
eta*r-(1-eta)*M
 +2*sqrt(eta*(1-eta))*Z_rho >=epsilon*eta*K         (5.13)
```

follows by choosing the direction in (5.11).  Alternatively a positive
eigenvector of `C` can close (5.6) through its diagonal even when the mixed
residual is small.  The two genuinely distinct surviving mechanisms are
therefore

```text
carrier-scale conditional Schur residual Z_rho,
or carrier-scale positive transverse edge of C.     (5.14)
```

The word "minimum" is scoped to finite linear-quadratic packet enrichments:
dimension one is the failed scalar (1.2); dimension two is sufficient exactly
under (5.6).  This does not rule out an unrelated nonlinear or infinite-
dimensional method.

## 6. Actual-`Lambda` spelling and the coupled theorem card

The three entries in (5.2) require no collateral-zero list.  Since `Nv=0`,

```text
r=Q_ar(e)+K,
c=Q_ar(v),
z=<e,Q_ar v>.                                       (6.1)
```

The complex cross entry is recovered from four real completed quadratic
evaluations:

```text
z=1/4*[Q_ar(e+v)-Q_ar(e-v)]
  -i/4*[Q_ar(e+i*v)-Q_ar(e-i*v)].                   (6.2)
```

Each evaluation in (6.2) is the same finite actual von Mangoldt sum plus its
pole and archimedean completion already used by the program.  With endpoint
lobes of diameter below `log 2`, same-lobe prime-power translates vanish;
the new datum is one completed cross-leg actual-`Lambda` correlation.

The weakest surviving theorem is now:

> For every hypothetical candidate in the fixed first-strip band, construct
> a compact target-neutral channel `v` in the same positive-null packet space
> and one fixed `eta,epsilon>0` such that (5.6) holds for the actual completed
> von Mangoldt form.  The compact Pick transfer must simultaneously control
> the collateral geometry of the maximizing state (5.3), including its
> actual arithmetic phase.

This is a coupled GA/GP target.  It is weaker than proving (1.2) for a
preselected `e`, because a large mixed coefficient may close (5.6) even when
`r` has the isolated value zero.  It is stronger than an aggregate
prime-null equation: the same phase must preserve the geometric negative
carrier and every completion term.

This deliberately changes one quantifier from the earlier standalone GA
card.  The old `A_geom` had to choose `e` before inspecting the von Mangoldt
value.  Here `e` remains geometric, but the transverse direction

```text
v=P_W*R_Lambda*e/norm(P_W*R_Lambda*e)               (6.3)
```

may depend on the actual coefficients.  That dependence is noncircular on
the arithmetic side because `R_Lambda=Q_ar+N` is assembled without a
collateral-zero list.  Its exact price is on the geometric side: GP must be
uniform for this arithmetic-selected direction, or prove its collateral
bound after the selection.  A geometric theorem only for a state fixed
before `Lambda` cannot be silently applied to (6.3).

There are two immediate fail-fast tests.

```text
actual arithmetic test:  compute/prove c_+ or abs(z) >= constant*K;
geometric test:           transfer the phase-optimized q_phi with o(K) debt.
```

Failure of both `c_+=Omega(K)` and `abs(z)=Omega(K)` reduces the enlarged
packet to the isolated obstruction and definitively closes this finite
covariance escape.

### 6.1 Actual-coefficient transverse probe

The new script

```text
src/same_packet_transverse_reserve_probe.py
```

assembles the existing sharp-Gabor arithmetic matrix from the actual
von Mangoldt coefficients, pole rows, and archimedean matrix.  It imposes
the endpoint jets and the selected-positive null, then computes (5.12), the
transverse spectral edges, and the two explicit channels in (5.14).

At `alpha=0.49`, `eta=1/2`, and the default aperture, the finite floating
scan gives the following ratios.  The probe ordinate is `gamma=1.5*T`.

| `T` | `K` | `r/K` | `Z/K` | `lambda_max(C)/K` |
|---:|---:|---:|---:|---:|
| 64 | 0.45198 | 2.494 | 1.020 | 2.418 |
| 128 | 0.95085 | 1.663 | 0.554 | 1.653 |
| 256 | 1.49224 | 1.726 | 0.200 | 1.206 |
| 512 | 2.27884 | 1.444 | 0.219 | 0.838 |
| 1024 | 3.26421 | 1.337 | 0.122 | 0.630 |

Every algebraic residual in the replay is below `10^(-8)`; the observed
residuals are in fact around machine precision.  At these small scales the
transverse diagonal and mixed entries are not numerically absent.

This table has a severe and explicit limitation: the point
`0.99+i*gamma` is **not asserted to be a zeta zero**.  Consequently adding
the artificial selected operator does not have the zero-side meaning (1.1),
and the positive `r/K` values cannot be read as evidence for GA.  The scan is
also the target-only sharp-Gabor fixture, not the final `d=0.66` compact
two-lobe/Pick state.  It is only a tool validation and a finite search oracle
for proposed transverse channels.  It supplies neither an asymptotic lower
bound nor the same-phase compact geometric estimate.

## 7. Literature audit

The classical results clarify the logical strength of the surviving card.

* Bombieri--Lagarias express the Li coefficients through the Guinand--Weil
  formula and prove their global positivity criterion for a symmetric
  multiset.  This uses an unbounded family of tests; it does not give a fixed
  positive reserve for a candidate-local compact packet:
  <https://doi.org/10.1006/jnth.1999.2392>.
* Freitas gives a Li-type criterion necessary and sufficient for zero-free
  half-planes/strips inside the critical strip.  It is a genuine alternative
  enriched family, but proving its required signs is already the desired
  fixed-strip theorem, not a reserve lemma:
  <https://arxiv.org/abs/math/0507368>.
* Burnol's invariant explicit-formula treatment checks Weil positivity under
  a support condition.  It supplies no candidate-relative strict fraction at
  the growing support used here:
  <https://arxiv.org/abs/math/0101068>.
* Chirre--Goncalves--de Laat use positive semidefinite optimization for pair
  correlation, but their zeta-zero conclusions in this setting assume RH and
  are global averages.  They cannot be inserted while an off-line candidate
  is being assumed, and they do not imply the pointwise entries in (5.2):
  <https://arxiv.org/abs/1810.08843>.
* Available second-moment work for shifted logarithmic derivatives is likewise
  averaged and commonly conditional on RH; it does not control a single
  candidate-adaptive height.  For a representative recent result see
  <https://arxiv.org/abs/2310.15918>.

No primary source located in this survey proves a target-conditioned,
compact, actual-von-Mangoldt inequality of the form (5.6).  The literature
therefore neither closes the gate nor supplies a no-go for the coherent mixed
entry `z`.

Internally, Theorem 2.1 extends the `d=2` Laurent-germ calculation in
`ZETA23-NONLINEAR-LOGDERIVATIVE-SQUARE-HERMITIAN-SIGN-GATE-2026-08-13.md`
to every finite power.  Theorem 5.1 refines the diagonal transverse-reservoir
alternative in
`ZETA23-MULTIWITNESS-MULTISCALE-AGGREGATE-CANCELLATION-AUDIT-2026-08-12.md`
by retaining the coherent off-block entry and identifying its conditional
Schur residual (5.12).  The Freitas alternative has already been audited
directly in
`ZETA23-TAU-LI-ENDPOINT-TRANSPORT-PRIME-LAGUERRE-GATE-2026-08-13.md`;
endpoint positivity does not propagate through its infinite alternating
transform.

## 8. Disposition

```text
strict reserve from FE/completion alone:                    FALSE;
finite log-derivative powers create a new clean detector:   FALSE;
finite PSD covariance removes contact and keeps orientation: FALSE;
isolated full selected quartet has positive reserve:        FALSE;
one-dimensional preselected actual-Lambda reserve:          OPEN;
two-dimensional coherent actual-Lambda criterion (5.6):     EXACT;
carrier-scale transverse entry c_+ or abs(z):                OPEN;
same-phase compact geometric transfer:                       OPEN;
uniform zero-free strip:                                     NOT PROVED.
```

Reproducibility:

```text
python3 src/test_same_packet_conditional_covariance_gate.py
python3 results/verify_zeta23_same_packet_conditional_covariance_gate.py
python3 src/test_same_packet_transverse_reserve_probe.py
python3 results/verify_zeta23_same_packet_transverse_reserve_probe.py
```

The checker verifies the Laurent-residue identities, positive contact
coefficient, Hermitian polarization, phase optimization, isolated-block
failure, and the necessary transverse scale.  It deliberately contains no
numerical evidence for an actual zeta reserve.
