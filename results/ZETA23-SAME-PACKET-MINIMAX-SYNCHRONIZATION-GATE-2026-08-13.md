# Same-packet QP/GP/GA synchronization: exact minimax criterion and finite no-go

**Date:** 2026-08-13  
**Verdict:** separate QP, GP, and GA witnesses do **not** synchronize by
convexity, Caratheodory, or phase optimization alone.  In a
factorization-stable compact autocorrelation class, synchronization is
equivalent to one explicit simplex of scalarized inequalities.  The
separate gate theorems check only the vertices of that simplex.  Exact
three-coordinate scalar packets give an interior Schur obstruction even
when every separate witness is compact, normalized, and QP-null.  No
zero-free strip is proved.

## 1. Put all three gates on one state

Fix a hypothetical actual candidate `rho`, and let `R=q*tilde(q)` be the
Hermitian autocorrelation of the **final** compact packet.  It is important
that this is the final packet, after every QP modulation, GP correction,
two-leg placement, and coherent GA phase has been made.  Normalize the
selected carrier by

```text
K_rho(R)=1.                                           (1.1)
```

Let `P_rho` be the normalized family satisfying the common requirements:

```text
compact physical support and endpoint regularity;
positive definiteness;
every active QP prime-power null;
the stated QP carrier/loss lower bound;
the fixed candidate geometry and marked multiplicity. (1.2)
```

All explicit-formula divisor and arithmetic evaluations are affine in `R`.
Put, in the compressed two-gate notation,

```text
s_GP(R)=u-R_other,rho(R),
s_GA(R)=R_Lambda,rho(R)-g,       g>u.                (1.3)
```

Every individual linear GP half-disk/divisor sign and scalar remote bound can
instead be retained as its own affine slack `s_j`; an operator-norm bound is
the corresponding family of scalar slacks.  Nonlinear spectral-factor,
disconnected-support, and exponent-bill conditions must be placed in
`P_rho` and their convexity proved separately.  That is the safer
formulation; (1.3) is only its final scalar compression.

At an actual candidate the completed explicit formula identifies

```text
R_Lambda,rho(R)=R_other,rho(R)                       (1.4)
```

on this *same* `R`.  Thus `s_GP>=0` and `s_GA>=0` contradict (1.4) when
`g>u`.  If the two inequalities are proved on different states, (1.4)
produces no contradiction.

More sharply, (1.4) itself supplies the interior minimax certificate

```text
(s_GP(R)+s_GA(R))/2=(u-g)/2<0       for every R.     (1.5)
```

Before normalization the right side is `(u-g)K_rho(R)/2`.  Therefore no
convex interpolation theorem can turn the two separate witnesses into one
under the candidate hypothesis.  Proving that the relevant joint
scalarization is nevertheless nonnegative would already be the desired
candidate contradiction, not a free consequence of convexity.

There is one normalization caveat.  Equation (1.1) is legitimate only when
QP, GP, and GA use the same positive carrier functional.  Renormalizing the
three outputs by three different quantities destroys affinity and does not
create a common state.

## 2. Exact minimax/separation theorem

Assume first that `P_rho` is compact and convex in an autocorrelation
topology and that every member has a legal scalar compact factor in the
required packet class.  For continuous affine slacks `s_1,...,s_m`, define

```text
Gamma_rho=max_(R in P_rho) min_(1<=j<=m) s_j(R).     (2.1)
```

### Theorem 2.1 (same-packet scalarization)

Let `Delta_(m-1)` be the probability simplex.  Then

```text
Gamma_rho
 =min_(lambda in Delta_(m-1))
    max_(R in P_rho) sum_j lambda_j*s_j(R).          (2.2)
```

Consequently one legal state satisfies every gate if and only if

```text
max_(R in P_rho) sum_j lambda_j*s_j(R)>=0            (2.3)
```

for **every** `lambda` in the simplex.  Fixed robust margins replace zero
by the desired positive margin on both sides.

#### Proof

For each fixed `R`,

```text
min_j s_j(R)=min_(lambda in Delta) sum_j lambda_j*s_j(R).
```

The displayed payoff is affine in each variable.  Compact convex minimax,
or equivalently separation of the convex slack image from the nonnegative
orthant, interchanges max and min and gives (2.2).  Attainment gives the
last assertion.  QED

This is precisely the finite/infinite convex conclusion supplied by Sion's
minimax theorem.  It does not say that (2.3) is true.  Separate existential
gate statements prove only

```text
max_R s_j(R)>=0                  for each j,          (2.4)
```

which checks (2.3) at the simplex vertices `lambda=e_j`.  An interior
`lambda` can still be a strictly negative certificate.

Caratheodory gives no extra sign.  In the `m`-dimensional slack image it can
reduce a *known* convex representation to at most `m+1` states, but it
cannot infer that the image meets the nonnegative orthant.  In particular,
mixing a GP witness and a GA witness requires their unreported cross-slacks.

### Theorem 2.2 (exact two-witness adapter)

Suppose the GP witness and GA witness have slack vectors

```text
R_GP: (a,-b),        R_GA: (-c,d),
a,b,c,d>=0.                                          (2.5)
```

The convex mixture `(1-lambda)R_GP+lambda R_GA` satisfies both gates for
some `0<=lambda<=1` if and only if

```text
b*c<=a*d.                                            (2.6)
```

Indeed the exact allowed interval is

```text
b/(b+d)<=lambda<=a/(a+c),                           (2.7)
```

with the evident zero-denominator conventions.  Thus the product of the
two own-slacks must pay the product of the two cross-deficits.  Separate
gate reports provide `a,d>=0`; they provide no bound resembling (2.6).

For the actual common-observable polarity the criterion always fails.  Put
`Delta=g-u>0`.  If the GP witness has own-slack `a` and the GA witness has
own-slack `d`, then necessarily

```text
b=a+Delta,       c=d+Delta,
a*d-b*c=-Delta*(a+d+Delta)<0.                       (2.8)
```

So not even arbitrarily large endpoint own-slacks can bridge a positive
upper/lower gap by convex interpolation.

### Factorization qualification

The convex lift is not a randomized-packet cheat when the class is closed
under scalar spectral factorization.  If `R_i=q_i*tilde(q_i)` have a common
interval support/type, then the Fourier transform of
`sum theta_i R_i` is `sum theta_i |Q_i|^2>=0`; continuous
Fejer--Riesz/Krein factorization returns one compact scalar `q` of half type.
The same is true when every packet has one fixed outer two-leg factor and
only its inner lobe is mixed.

This qualification is not known for arbitrary GP outputs with varying
two-leg gaps, causal factors, and endpoint sublayers.  A spectral factor of
a convex mixture may fill the convex hull of the supports.  Therefore the
actual route needs either

```text
a common-factor packet class closed under the lift, or
a direct deterministic same-packet selection theorem.               (2.9)
```

Failure of (2.9) makes convex synchronization unavailable even before the
minimax obstruction.  Granting (2.9) still does not remove that obstruction.

## 3. Exact common-observable counterexample

Let the normalized QP face have a completed observable `0<=f<=1`, and put

```text
s_GP=1/4-f,                 s_GA=f-3/4.              (3.1)
```

The state `f=0` is a GP witness and `f=1` is a GA witness.  Nevertheless
there is no common state.  Exactly,

```text
max_(0<=f<=1) min(1/4-f,f-3/4)=-1/4,                (3.2)
```

attained at `f=1/2`.  The dual scalarization `lambda=1/2` also has value
`-1/4`, although both vertex scalarizations have value `+1/4`.

For the two endpoint witnesses, (2.5) is

```text
(a,b,c,d)=(1/4,3/4,3/4,1/4),
a*d-b*c=-1/2.                                       (3.3)
```

This is the exact logical shape of (1.4): GP asks the common completed
observable to be below `u`, GA asks it to be above `g`, and separate states
can realize both extremes without yielding a contradiction.

## 4. Coherent GA enrichment can destroy the QP null

The QP constraint is imposed on an autocorrelation and is quadratic in a
spectral factor.  Let `e,v` be two channels and put

```text
q=sqrt(eta)*e+exp(i*phi)*sqrt(1-eta)*v.              (4.1)
```

At an active offset `u`, its autocorrelation contains

```text
R_q(u)=eta*R_e(u)+(1-eta)*R_v(u)
       +sqrt(eta*(1-eta))*[phase-twisted cross rows]. (4.2)
```

Therefore `R_e(u)=R_v(u)=0` does not imply `R_q(u)=0`.  An exact three-tap
fixture is

```text
e=(1,0,0),       v=(0,1,0),       q=(e+v)/sqrt(2).  (4.3)
```

Both channels have lag-one autocorrelation zero, while

```text
R_q(1)=1/2.                                           (4.4)
```

The incoherent convex mixture `(R_e+R_v)/2` remains QP-null, but it deletes
the coherent cross term which GA2 needs.  Thus the GA2-selected direction
and phase must be inserted **before** checking every QP null.  Individual
nullness of the carrier and transverse channel is insufficient.

There is an exact algebraic formulation.  Write the active QP rows as

```text
F_n(q)=<q,T_(u_n)q>=0.                               (4.5)
```

For `q=Ae+Bv`, with `F_n(e)=0`,

```text
F_n(q)=|B|^2 F_n(v)
       +conj(A)B<e,T_(u_n)v>
       +conj(B)A<v,T_(u_n)e>.                       (4.6)
```

Hence a phase-free sufficient condition is that `span{e,v}` be a common
totally isotropic two-plane for every active shift form:

```text
<x,T_(u_n)y>=0
for x,y in {e,v} and every n.                        (4.7)
```

For one selected phase, (4.6) is the exact weaker simultaneous quadratic
system that must be solved.  QP-PROMOTE supplies one null ray; it supplies
neither (4.7) nor a solution of that growing system.

At first order the correct GA direction is therefore not the old full
`W=e^perp`.  It lies in the common tangent kernel

```text
T_QP(e)=intersection_n ker[D F_n(e)],                (4.8)
```

and also in the GP tangent/compact-realization cone.  A local joint reserve
would have to control

```text
Z_joint=||P_(T_QP intersection T_GP) R_Lambda e||,  (4.9)
```

then integrate that tangent direction to an exact finite state satisfying
(4.6).  The existing GA2 quantity with projection only onto `W` can be large
entirely normal to the QP face.

### 4.1 Exact compact scalar phase counterexample

The preceding example could be dismissed as one-dimensional.  The next
fixture retains an actual coherent phase and an exact scalar factor.

Take a normalized three-tap compact packet

```text
q=(a,b,c),       |a|^2+|b|^2+|c|^2=1,              (4.10)
```

and impose the QP-null row

```text
R(1)=b*conj(a)+c*conj(b)=0.                         (4.11)
```

Its untouched coherent lag is

```text
z=R(2)=c*conj(a),       |z|<=1/2.                   (4.12)
```

The last inequality is the exact Schur/AM--GM bound
`|a*c|<=(|a|^2+|c|^2)/2<=1/2`.  Now let GP require

```text
Re z>=2/5                                             (4.13)
```

and let GA require

```text
Im z>=2/5.                                            (4.14)
```

Both have normalized compact QP-null witnesses:

```text
q_GP=(1,0,1)/sqrt(2),       z=1/2,
q_GA=(1,0,i)/sqrt(2),       z=i/2.                  (4.15)
```

No common phase exists, because (4.13)--(4.14) would force

```text
|z|^2>=2*(2/5)^2=8/25>1/4.                          (4.16)
```

This remains false after allowing the entire convex disk `|z|<=1/2`.
Every point of that disk is itself realized by a scalar packet of the form
`(a,0,c)`, so neither mixing, Caratheodory reduction, nor scalar
factorization repairs the phase mismatch.

The fixture is not a zeta model and makes no claim about actual Lambda
coefficients.  Its rigorous scope is narrower and useful: no theorem using
only separate existential gate witnesses, positivity, compactness,
normalization, and free coherent phase can establish same-packet
compatibility.

## 5. The joint exponent bill

At `alpha=.49`, `d=.66`, the conservative GP ledger is

```text
raw carrier exponent              =.3234,
Green base bill                   =.298008745,
S=available correction surcharge =.025391255
  =5078251/200000000.                              (5.1)
```

If QP-PROMOTE costs `Y^(-kappa_QP)` and the remaining GP compact correction
costs `X^(-c_GP)`, the final carrier exponent is

```text
sigma_final=S-c_GP-d*kappa_QP.                      (5.2)
```

The exact joint condition is

```text
c_GP+d*kappa_QP<S-sigma                             (5.3)
```

for some fixed `sigma>0`.  Bare statements that GP retains an unspecified
positive power and QP is individually below its old threshold do not imply
(5.3).

At the rounded QP frontier

```text
kappa_promote=.0180303234,
d*kappa_promote
 =2975003361/250000000000
 =.011900013444,

S-d*kappa_promote
 =3372810389/250000000000
 =.013491241556.                                    (5.4)
```

Thus a near-frontier QP theorem leaves at most `.013491241556` of
`X`-exponent for every residual GP correction, and strict closure leaves
less.  A QP theorem with saving `eta` adds exactly `d*eta` to this room.
These are budget identities, not proofs of either gate.

## 6. The exact live extra hypothesis for `ZF(1/100)`

Do **not** assume QP-PROMOTE in this card.  Conditional on a future
QP-PROMOTE theorem, the missing compatibility statement can be supplied in
either of two equivalent-strength forms.

### Direct form

For every sufficiently high hypothetical actual zero with
`alpha in [.49,.5)`, construct by one fixed rule a final compact state
`R_rho in P_rho` and one carrier `K_rho>0` such that, on that same state,

```text
R_other,rho(R_rho)<=u*K_rho+o(K_rho),
R_Lambda,rho(R_rho)>=g*K_rho+o(K_rho),       g>u,   (6.1)

c_GP+d*kappa_QP<S-sigma                           (6.2)
```

for fixed `g-u>0` and `sigma>0`, with every remote and finite-support error
uniformly absorbed in the displayed `o(K_rho)`.

### Minimax form

Prove factorization-stable compact convexity of `P_rho`, include every
affine GP sign, GA reserve, phase, remote scalarization, and frozen budget
margin as a slack `s_j`, and prove

```text
for every lambda in Delta,
max_(R in P_rho) sum_j lambda_j*s_j(R)>=epsilon      (6.3)
```

for one fixed `epsilon>0`.  Theorem 2.1 then produces the direct state.
An operationally stronger but easier-to-state substitute is:

```text
the actual-Lambda direction has carrier-scale Z_joint after projection into
the exact QP+GP tangent and integrates to a final QP-null state on which GP
is uniform,
or GA is uniform on the complete QP+GP feasible face.                  (6.4)
```

Uniformity only over phases, without the transverse direction, the cross-null
system (4.6), and all normalizations, is insufficient.

At an actual candidate, (1.4) contradicts (6.1).  A separately verified
finite-height base case and conjugation then give

```text
zeta(s)!=0 for Re(s)>.99,
delta_ZF=1/100.                                      (6.5)
```

The minimax theorem therefore identifies the exact missing quantifier; it
does not discharge it.

## 7. Literature disposition

* Maurice Sion's [general minimax theorem](https://doi.org/10.2140/pjm.1958.8.171)
  gives (2.2) under the stated compactness/convexity hypotheses.  It does
  not infer the nonnegativity in (2.3) from its values at simplex vertices.
* M. G. Krein's [factorization theory for entire functions of exponential
  type](https://m.mathnet.ru/eng/im3001), together with the already audited
  compact Fejer--Riesz transfer, justifies replacing a convex
  autocorrelation by one scalar factor in factorization-stable support
  classes.  It does not preserve an arbitrary disconnected two-leg support
  pattern.
* Caratheodory only reduces support after a point is known to lie in a
  convex hull.  It has no intersection or same-witness conclusion.
* Schur-complement/PSD inequalities give (4.12) and, in finite truncations,
  semidefinite separation certificates for a failed joint feasibility
  problem.  They do not force the actual-Lambda scalarizations (6.3) to be
  nonnegative.

No surveyed theorem turns separate QP/GP/GA existence statements into the
joint candidate-relative arithmetic assertion (6.1).

## 8. Reproduction

```bash
PYTHONPATH=src python3 src/test_same_packet_minimax_sync_gate.py
python3 results/verify_zeta23_same_packet_minimax_sync_gate.py
```

The checker uses exact rational arithmetic for (3.2)--(3.3), (4.16), and
(5.1)--(5.4), plus explicit `3 x 3` Hermitian matrices for the two phase
witnesses.  `PASS` certifies the synchronization theorem and scoped
counterfixtures; it does not certify QP-PROMOTE, GP, GA2, or a strip.
