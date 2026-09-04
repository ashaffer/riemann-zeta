# Positive categorical routes and finite fail-fast gates

Status: exact finite-dimensional theorem cards and a research-priority audit,
2026-08-12.  This note develops the constructive side of the categorical
consolidation.  It does not prove a uniform zero-free strip, RH, failure of a
strip, or a statement about ZFC.

## 1. Verdict

The expanded categorical search produces three materially sharper directions
and several useful pruning rules.

1. **Restrict descent to the actual arithmetic operator system.**  The earlier
   probe-cone theorem asked whether local probes detect every Hermitian matrix.
   That is unnecessarily strong.  There is an exact quotient-cone criterion
   for detection only on a zero-independent zeta operator system.  Better, a
   completely positive recovery map is a finite semidefinite certificate for
   such detection.  This is the best near-term categorical gate.
2. **Use the Stinespring covariance, not an arbitrary nonlinear transform.**
   A completely positive observation has a canonical positive multiplicative
   defect.  Its covariance kernel is automatically positive and measures
   exactly the information outside the multiplicative domain.  This is the
   polarization of a quadratic Kadison--Schwarz defect, not the additive
   cross-effect of the linear CP map (which is zero).  If an arithmetically
   defined semilocal conditional expectation has a carrier-grade transverse
   covariance, it is a genuine candidate reservoir.  It still must occur in
   the completed explicit-formula identity with the correct sign; complete
   positivity alone does not supply that identity.
3. **Replace exact polarization by a quantitative polarization defect.**  A
   positive dagger satisfying

   ```text
   -epsilon G <= A*G+GA-G <= epsilon G,       epsilon<1,
   ```

   confines every eigenvalue of `A` to

   ```text
   abs(Re(lambda)-1/2)<=epsilon/2.
   ```

   Thus a spectrum-independent arithmetic metric with a uniform defect below
   one would already imply a fixed strip; exact purity is not required.  This
   is a genuinely weaker target than the exact adjoint equation, although
   fitting the metric after seeing `A` remains circular.

Two further formulations substantially reduce wasted work without themselves
adding positivity.

- The relevant complex-row obstruction is the image of the actual remainder
  in one explicit coequalizer

  ```text
  H/(im(X*)+C a).
  ```

  Every place contribution which vanishes there can be discarded before any
  delicate norm estimate.
- A filtered/bornological `Newton diagram` should record both the growth grade
  and this quotient direction.  Size without transverse direction is useless;
  transverse direction below the carrier grade is also useless.

Pro/ind, Mosco, corona, and ultraproduct language becomes important only after
one finite-stage mechanism survives.  It specifies the topology which cannot
lose a moving carrier.  It does not sign the carrier.  Bare Tannakian duality,
generic correspondences, ordinary `Ext`, and `K`-theory without a uniform
spectral gap should be parked.

## 2. Priority table

| Route | What is genuinely new? | First finite gate | Feasibility | Recommendation |
|---|---|---|---|---|
| zeta-restricted probe cone | weaker and more relevant than universal cone generation | quotient-cone separation optimization; an SDP after fixing a candidate negative direction | high | run now |
| CP recovery on the zeta operator system | constructive order-reflection certificate | Choi-matrix feasibility SDP | high at finite stage, medium-low uniformly | run now with the preceding gate |
| CP/Stinespring covariance | canonical positive multiplicative defect | `{infinity,p,q}` covariance and carrier-grade test | medium | run if a natural semilocal expectation is available |
| quotient obstruction projection | removes aligned and constraint-generated remainder exactly | project every place row modulo `im(X*)+C a` | very high | make standard preprocessing |
| carrier-slice positive support | tests the only sign of the remainder that can cancel the aligned carrier | one finite state-cone SDP | very high | make the primary operator remainder test |
| filtered/bornological grades | organizes bounded and unbounded remainders honestly | grade-plus-angle ledger | high as bookkeeping, low as engine | use, but do not count as a proof route |
| conservative pro/ind or Mosco limit | prevents a finite mechanism from losing a moving carrier | moving-vector Mosco test and compatibility defect | medium | defer until a finite mechanism survives |
| approximate positive polarization | exact quantitative route to a fixed strip | zero-independent two-prime/gamma metric with defect `<1` | low, high upside | small parallel program |
| bare Tannaka, generic bimodules, ordinary `Ext/K` | no new order in their generic form | counterexamples below | low | park |

The scores concern the ability to execute the *next theorem card*, not the
probability of proving a strip.

## 3. Theorem card A: order descent on a zeta operator subspace

### 3.1 Exact restricted probe-cone criterion

Let `H` be finite-dimensional and let

```text
P=Pos(H) subset Herm(H)
```

be the positive semidefinite cone.  Let `j_i:E_i->H` be isometric probes and
put

```text
C_J=closure cone{j_i Gamma_i j_i* : Gamma_i>=0}.
```

Let `V subset Herm(H)` be a real linear subspace containing `I` and specified
independently of the sign of the completed form.  With orthogonality taken in the
Hilbert--Schmidt pairing, the following are equivalent.

```text
(A1)  A in V and j_i* A j_i>=0 for every i  imply A>=0;

(A2)  V intersect C_J* = V intersect P;

(A3)  closure(C_J+V_perp)=closure(P+V_perp).          (3.1)
```

#### Proof

The probe-cone duality gives

```text
{A : j_i*Aj_i>=0 for every i}=C_J*.
```

This proves `A1 iff A2`.  For any cone `C` and linear space `W`,

```text
closure(C+W)*=C* intersect W_perp.
```

Apply this with `W=V_perp`.  Since `P` is self-dual, the duals of the two
closed cones in `A3` are respectively `C_J* intersect V` and `P intersect V`.
The bipolar theorem proves `A2 iff A3`.  QED

This is strictly sharper than requiring `C_J=P`.  The probes need generate
positive states only **modulo directions orthogonal to the actual arithmetic
operator subspace**.

### 3.2 Operator-system version

If necessary replace `V` by `V+R I`, and let `E=V+iV` be the resulting
complex operator system.  Define

```text
Phi_J:E -> direct_sum_i B(E_i),
Phi_J(A)=direct_sum_i j_i* A j_i.                     (3.2)
```

With this unital convention, condition (3.1), applied to the enlarged `V`, is
exactly level-one order reflection of `Phi_J`.  For an arbitrary original
subspace not containing `I`, (3.1) asserts order reflection only on that
subspace, not automatically on the larger operator system it generates.  If
a proof uses tensor ancillas or matrix-valued relations, replace it by
complete order reflection of

```text
id_(M_n) tensor Phi_J
```

at every matrix level.  The present scalar completed Weil-form positivity
problem needs level one.  Matrix amplification by itself merely repeats the
negative mirror eigenvalue and adds no information.

### 3.3 What the zeta operator system must mean

The useful finite-stage space `V_T` cannot be `span{K_T}` chosen after the
completed matrix has been diagonalized; then the criterion is tautological.
It should be generated before the sign test by, for example,

- the allowed prime-translation matrices on the fixed packet space;
- the pole/main and archimedean matrices;
- the exact symmetry and endpoint-jet relations;
- the permitted packet, phase, or support parameters; and
- every hypothetical carrier deformation which the advertised theorem must
  exclude.

The smaller `V_T` is, the more arithmetic relations have been used.  Those
relations must be proved from coefficients and support geometry, not from the
zero divisor or the negative eigenspace.

### 3.4 Finite fail-fast test

At the smallest exact mirror stage:

1. build a rational/interval basis of `V_T`;
2. build the chosen probe maps `j_i`;
3. search for

   ```text
   A in V_T intersect C_J* with A not >=0;             (3.3)
   ```

4. if found, save `A` as the structured countermodel; and
5. if none is found, seek a dual certificate for (3.1), then test the next
   support.

The non-PSD condition in (3.3) is not itself a convex constraint.  Once a
candidate negative vector `z` is fixed, the normalization `z*Az=-1` turns the
remaining search into an SDP; a global separation test therefore requires a
direction search, an equivalent cone-containment method, or a certified
finite covering.  It should not be advertised as one unconditional SDP.

Failure of (3.3) for a broad structural `V_T` does not prove positivity of the
actual zeta matrix.  It proves that the selected probes are order-reflecting
on the specified arithmetic class.  Conversely, a counterexample prunes that
class of local arguments unless an additional zeta relation removes it.

For quantitative work define

```text
nu(A)=max(0,-lambda_min(A)),
nu_J(A)=sup_i max(0,-lambda_min(j_i*Aj_i)),

kappa_T=inf_{A in V_T, nu(A)>0} nu_J(A)/nu(A).         (3.4)
```

A bound `inf_T kappa_T>0` is a uniform observability theorem.  Plain order
reflection need not supply such a bound on an unbounded cone, so (3.4) is a
separate quantitative gate rather than an automatic corollary of (3.1).

### 3.5 Exact mirror sanity check

For the normalized mirror operator system

```text
E_mir=span_C{I,J},             J=[[0,1],[1,0]],
A=a I+b J,                    a,b real,               (3.5)
```

the two coordinate probes see only `(a,a)`.  Their observation kills `J`, so
it is not injective and cannot have a positive recovery; `a>=0` does not
exclude `abs(b)>a`.

The two symmetry probes

```text
e_+=(1,1)/sqrt(2),          e_-=(1,-1)/sqrt(2)
```

instead give

```text
Phi_sym(A)=(a+b,a-b).                                 (3.6)
```

This is an order isomorphism from `E_mir` to `C direct_sum C`, with positive
recovery

```text
Psi(x,y)=((x+y)/2)I+((x-y)/2)J.                       (3.7)
```

Thus the restricted criterion is nonvacuous: a tiny coherent probe family can
reflect order on a tiny arithmetic operator system even though it cannot
reflect order on all matrices.  It also exposes the limitation.  For
`m(I+CJ)`, the second output is `m(1-C)`, exactly the unresolved negative
carrier.  Symmetry probes detect the obstruction but do not sign it.  A useful
zeta probe system must retain this coherence while making its output
arithmetically controllable.

### 3.6 Novelty assessment

The cone duality is standard finite-dimensional convex analysis.  The new
value is the zeta-specific weakening from universal PSD generation to
generation modulo `V_T_perp`, together with a finite structured countermodel
search.  This is an actionable refinement, not a new abstract theorem.

## 4. Theorem card B: completely positive recovery

### 4.1 Exact recovery implies order reflection

Let `E subset A` be an operator system in a finite-dimensional C-star algebra,
let

```text
Phi:A->B
```

be unital completely positive, and suppose there is a unital positive map

```text
Psi:B->A
```

such that

```text
Psi Phi(a)=a                     for every a in E.     (4.1)
```

Then `Phi` is order-reflecting on `E`:

```text
a in E, Phi(a)>=0  implies  a=Psi(Phi(a))>=0.          (4.2)
```

If `Psi` is completely positive, the same proof at every matrix level makes
`Phi|E` a complete order embedding.

This is the constructive form of Theorem card A.  The local observation has
a positive **recovery channel** on the arithmetic operator system.

### 4.2 Approximate recovery gives a quantitative lower bound

Suppose `Psi` is unital positive and, for one Hermitian `a in E`,

```text
||a-Psi Phi(a)||<=epsilon K.                           (4.3)
```

If `Phi(a)>=0`, then

```text
a>=-epsilon K I.                                      (4.4)
```

Indeed `Psi Phi(a)>=0`, and an Hermitian operator within `epsilon K` in
operator norm of a positive operator has lower edge at least `-epsilon K`.
Thus an approximate recovery error smaller than a hypothesized carrier margin
rules out that carrier.  A carrier-uniform `o(K_T)` recovery is enough even
when no fixed unnormalized spectral margin exists.

### 4.3 Finite fail-fast test

For fixed matrix algebras the Choi matrix of `Psi` is the variable in a
semidefinite feasibility problem:

```text
Choi(Psi)>=0,
Psi(I)=I,
Psi Phi(e_k)=e_k                for a basis e_k of E.  (4.5)
```

Run (4.5) at the smallest `{pole,gamma,p,q}` or normalized mirror stage.

- If it is feasible, the Choi matrix is a checkable finite certificate of
  complete order reflection on `E`.
- If it is infeasible, exact CP recovery is pruned.  One may minimize the
  recovery error in an order-unit or completely bounded norm.
- Before either computation, check `E intersect ker(Phi)=0`.  A nonzero
  Hermitian kernel element immediately rules out any left inverse.  Injectivity
  is necessary but is not sufficient for a positive inverse.

The asymptotic theorem would then be: construct `Phi_T,Psi_T` naturally under
adjoining primes and prove a carrier-normalized recovery error below the
required margin.  This is an arithmetic estimate, not a consequence of the
finite SDP.

### 4.4 Novelty assessment

Recovery is standard operator-system theory.  As a research formulation it is
materially new here: it converts vague local-to-global optimism into a Choi
matrix certificate and exposes a quantitative approximate version.  It should
replace further generic partition-gluing experiments.

## 5. Theorem card C: CP covariance as a positive transverse candidate

### 5.1 Exact covariance positivity

Let `Phi:A->B` be unital completely positive and define

```text
Cov_Phi(a,b)=Phi(a* b)-Phi(a*) Phi(b).                (5.1)
```

For every finite tuple `a_1,...,a_r`, the matrix

```text
[Cov_Phi(a_i,a_j)]_(i,j)                              (5.2)
```

is positive in `M_r(B)`.

#### Proof

Use a Stinespring representation

```text
Phi(a)=V* pi(a) V,                 V*V=I.
```

Then

```text
Cov_Phi(a_i,a_j)
 =V*pi(a_i)*(I-VV*)pi(a_j)V.                          (5.3)
```

For vectors `xi_j` in the output Hilbert space, the quadratic sum from (5.2)
is

```text
|| (I-VV*) sum_j pi(a_j)V xi_j ||^2>=0.               (5.4)
```

QED

In particular `Cov_Phi(a,a)>=0`.  Its vanishing says that the relevant
Stinespring defect is zero.  Vanishing for both `a` and `a*` is the usual
multiplicative-domain condition; in that case the CP observation creates no
new cross term from `a`.

### 5.2 Why this is different from arbitrary nonlinear calculus

The adapter trilemma says a nonlinear transform creates uncontrolled
prime--prime and prime--archimedean additive cross-effects.  Formula (5.3)
instead identifies the polarization of the quadratic Kadison--Schwarz defect
`a |-> Cov_Phi(a,a)`; its entire covariance matrix has a canonical positive
sign.  It is a multiplicative defect of `Phi`, not `cr_2 Phi` (the latter
vanishes because `Phi` is linear).  A Hilbert-C-star-module correspondence
with a normalized cyclic vector
produces the same construction through

```text
Phi_xi(a)=<xi,pi(a)xi>.
```

Thus a correspondence is potentially substantive only if it supplies one of
two things:

1. a positive recovery as in Section 4; or
2. a nonzero Stinespring covariance which enters the arithmetic identity.

An imprimitivity/equivalence merely transports the old order problem.  A
generic nonfaithful correspondence can forget it.

### 5.3 Candidate zeta use

The natural experiment is a zero-independent conditional expectation from a
coupled semilocal/all-place algebra to the packet operator system.  Its
covariance measures the part of multiplication lost under observation.  For
the target and aggregate generators, test whether the covariance has a
carrier-grade component transverse to the aligned mirror class.

Complete positivity supplies only (5.2).  A successful theorem must also
prove an exact completed identity of the schematic form

```text
actual remainder = signed arithmetic image of Cov_Phi + subcarrier error, (5.5)
```

with the useful sign.  Without (5.5), covariance is an unrelated positive
matrix and cannot repair the Weil form.

### 5.4 Dephasing sanity check

Let `Phi_diag:M_2->D_2` be diagonal conditional expectation.  For the mirror
swap `J`,

```text
Phi_diag(J)=0,
Cov_(Phi_diag)(J,J)=Phi_diag(J*J)=I.                  (5.6)
```

The covariance is positive and as large as possible even though dephasing
has simply erased the off-diagonal carrier.  Nothing in the original linear
explicit formula assigns the new `I` in (5.6) the coefficient needed to fix
the mirror.  This is the minimal counterexample to the claim that positive CP
covariance alone is an engine; identity (5.5) is indispensable.

### 5.5 Finite fail-fast test

For a proposed `Phi`:

1. verify that it is defined from primes, gamma, pole, and support data before
   zeros or bad eigenvectors are used;
2. compute (5.2) on the exact normalized mirror and on the
   `{infinity,p,q}` fixture;
3. test whether it vanishes by the multiplicative-domain criterion;
4. project it through the obstruction quotient in Section 6;
5. compare its positive norm with the carrier scale; and
6. derive (not fit) the coefficient and sign with which it appears in the
   completed explicit formula.

Zero covariance, aligned covariance, `o(K_T)` covariance, or absence of (5.5)
parks the route immediately.

### 5.6 Novelty assessment

Stinespring covariance is standard.  Its identification as an obvious
categorically canonical positive multiplicative defect is a genuinely new
lead for this program.  No present construction proves (5.5), so this is a
research direction rather than evidence for a strip.

## 6. Theorem card D: the universal quotient obstruction

### 6.1 Exact row obstruction

Let `X:H->Y`, let `S=ker X`, and let `P_S` be the orthogonal projection.  Let
`a,g,e in H` be the Riesz vectors of the target, aggregate, and remainder rows,
with

```text
g=lambda a+e.
```

Put

```text
a_bar=P_S a,       g_bar=P_S g,       e_bar=P_S e.
```

Assume `a_bar!=0` and `g_bar!=0`, and define

```text
Obs_(X,a)(e)=P_(a_bar_perp) e_bar.                    (6.1)
```

Then

```text
a_bar wedge g_bar=a_bar wedge e_bar,                 (6.2)

||a_bar wedge g_bar||
 =||a_bar|| ||Obs_(X,a)(e)||,                         (6.3)

sup_{h in S, ||h||<=1, <g_bar,h>=0} |<a_bar,h>|^2
 =||a_bar wedge g_bar||^2/||g_bar||^2.                (6.4)
```

Consequently complex aggregate-null target leverage exists exactly when
`Obs_(X,a)(e)!=0`.  Every component in

```text
im(X*)+C a                                             (6.5)
```

is annihilated.  Equations (6.1)--(6.5) are the concrete coequalizer form of
the exterior obstruction `Omega`.

If `g_bar=0`, the aggregate row is vacuous on the feasible object and must be
handled separately; the wedge quotient is intentionally not used in that
degenerate case.

### 6.2 Additivity and the new pruning rule

If

```text
e=sum_v e_v,
```

then

```text
Obs_(X,a)(e)=sum_v Obs_(X,a)(e_v).                    (6.6)
```

Thus the correct first computation is not the full norm of every place term.
It is its image under (6.1).  Aligned prime modes, positive-row coboundaries,
and common residue multipliers vanish exactly before asymptotics.  Only the
surviving projected rows need carrier-scale estimates.  Actual phases still
matter because the surviving terms in (6.6) can cancel.

### 6.3 Scope warning

This theorem is exact for the complex homogeneous row-null problem.  The
minimal aggregate condition in the current mirror audit is one real signed
quadratic equation.  That problem is governed by the state/effect carrier
lemma, not by replacing it with (6.4).  The quotient projection remains a
useful diagnostic for stronger complex-row variants, but it must not be used
to overstate the minimal one-real conclusion.

### 6.4 `Ext` is the wrong word in finite Hilbert space

Finite-dimensional Hilbert spaces form a semisimple category, so ordinary
`Ext^1` vanishes.  The class in (6.1) is a coequalizer/quotient or Plucker
obstruction, not a hidden extension class.  A derived route becomes new only
after specifying a genuinely nonsemisimple arithmetic category and a map from
its extension data to (6.1) or to the ordered carrier obstruction.

### 6.5 Novelty assessment

This is a repackaging of the dagger-kernel/exterior lemma, but a productive
one.  It turns the open remainder into a linear per-place projection and
should materially reduce future prime/collateral calculations.

## 7. Theorem card E: filtered and bornological grades

### 7.1 Exact graded dagger construction

Let `X_T->infinity` be a base scale and let objects be families of finite
Hilbert spaces.  For real `alpha`, set

```text
F^alpha Hom(H,G)
 ={S=(S_T): ||S_T||=O(X_T^alpha)},

F^<alpha Hom(H,G)
 ={S=(S_T): ||S_T||=o(X_T^alpha)}.                    (7.1)
```

Then

```text
F^alpha o F^beta subset F^(alpha+beta),
(F^alpha)*=F^alpha,                                   (7.2)
```

and replacing either factor by a little-`o` family makes the composition
little-`o` at degree `alpha+beta`.  Therefore

```text
gr^alpha Hom=F^alpha/F^<alpha                         (7.3)
```

forms a graded dagger category.  More general gauges are legitimate only
after their multiplication and order laws are specified.  The bounded
carrier-normalized degree is the corona C-star category from the four-lemma
consolidation.  Arbitrary nonzero degrees form a graded star category; a
C-star order at every grade must not be assumed automatically.

### 7.2 Grade-and-angle necessity

Let `S_T` be the positive-null object, let `N_T>=0` and `R_T=R_T*` on `S_T`,
and let `Gamma_T` be normalized positive states supported on `S_T`.  Suppose

```text
B_T<=-c K_T N_T,                  c>0,
Tr(N_T Gamma_T)>=eta>0,
Tr((B_T+R_T)Gamma_T)=o(K_T).                          (7.4)
```

Then (7.4) implies

```text
||(P_S R_T P_S)_+||>=c eta K_T-o(K_T).                (7.5)
```

Thus a successful remainder must have both:

1. carrier or larger grade; and
2. positive pairing in the feasible carrier direction.

A large operator norm in an orthogonal or negative direction is not useful.
Equation (7.5), not the existence of a graded category, supplies the order
content.

There is a sharper finite formulation.  For fixed carrier mass `eta`, define
the compact convex carrier slice (assumed nonempty)

```text
F_eta={Gamma>=0 : Tr(Gamma)=1,
                     range(Gamma) subset S,
                     Tr(N Gamma)>=eta},

h_eta(R)=sup_(Gamma in F_eta) Tr(R Gamma).             (7.5a)
```

If

```text
B<=-c K N
```

and some `Gamma in F_eta` obeys aggregate cancellation with error

```text
abs(Tr((B+R)Gamma))<=epsilon K,
```

then exactly

```text
h_eta(R)>=(c eta-epsilon)K.                            (7.5b)
```

This follows by subtracting the upper bound on `Tr(B Gamma)`.  Moreover

```text
h_eta(R)<=||(P_S R P_S)_+||.                          (7.5c)
```

The support function in (7.5a) is a semidefinite program.  It is materially
sharper than bounding `||R||`: an arbitrarily large negative eigenvalue makes
the full norm large but cannot pay the positive cancellation bill.  It is
also sharper than the unrestricted positive-part norm when the positive
eigenvectors lie outside the carrier slice.  For the actual one-real aggregate
constraint, (7.5a) is the correct first operator test; the row wedge in
Section 6 addresses a different, stronger complex-null problem.

### 7.3 The categorical Newton diagram

For each arithmetic contribution record the pair

```text
(growth grade, obstruction image).                    (7.6)
```

The pruning rules are exact.

- A term below the carrier grade cannot satisfy (7.5).
- A carrier-grade term killed by (6.1) cannot create complex transversality.
- A term above the carrier grade is not a corona morphism; its own leading
  sign and target angle become the primary analytic problem.
- Terms at the same top grade must be summed before their leading symbol is
  judged, because coefficient-specific cancellation can occur.

### 7.4 Fail-fast tests

1. Prove upper and lower growth bounds before naming a leading class.
2. If `||R_T||/K_T` is unbounded, stop using the bounded corona and identify a
   higher grade.
3. If growth oscillates between grades, work subsequentially or prove a
   regular-variation statement; do not assert one canonical symbol.
4. Always retain the target/feasible-state pairing in addition to the norm.

### 7.5 Novelty assessment

The filtration is useful and honest bookkeeping.  It does not generate an
estimate.  Its material contribution is to prevent bounded-corona language
from swallowing an unbounded actual remainder and to combine exponent and
angle screening in one ledger.

## 8. Theorem card F: conservative pro/ind and Mosco limits

### 8.1 Exact inductive positivity

Let

```text
H_1 -> H_2 -> ...
```

be isometric embeddings and let Hermitian forms `q_n` satisfy exact
compatibility

```text
q_(n+1)(i_n x)=q_n(x).                                (8.1)
```

On the algebraic inductive limit `D`, define `q` by (8.1).  Then

```text
q>=0 on D  iff  q_n>=0 for every n.                   (8.2)
```

If `D` is a form core and `q` is closable, its closed extension remains
nonnegative.  This theorem is exact but tautological: it converts a coherent
all-stage proof into a global proof; it does not prove any stage.

### 8.2 Mosco lower-bound transfer

Let lower-semicontinuous quadratic forms `q_n` on a common Hilbert space
Mosco-converge to `q`, and assume

```text
q_n(x)>=-epsilon_n ||x||^2,             epsilon_n->0. (8.3)
```

Then `q>=0`.  For a Mosco recovery sequence `x_n->x`, the sequence is norm
bounded and hence the lower bounds give `liminf q_n(x_n)>=0`; therefore

```text
q(x)>=limsup q_n(x_n)>=liminf q_n(x_n)>=0.             (8.4)
```

The same statement can be made on varying Hilbert spaces only after explicit
comparison maps are part of the data.

### 8.3 Moving-carrier fail-fast test

Suppose unit vectors `u_n` obey

```text
u_n weakly ->0,             q_n(u_n)<=-eta<0.          (8.5)
```

Then the `q_n` cannot Mosco-converge to a form with `q(0)=0`: the Mosco liminf
condition would require

```text
0=q(0)<=liminf q_n(u_n)<=-eta.                         (8.6)
```

This is the exact test for a topology which loses a carrier moving to remote
height.  The familiar operators

```text
A_n=I-2 e_n e_n*
```

converge strongly to `I` while retaining a negative eigenvalue at every
stage; strong convergence alone is therefore not carrier-conservative.

### 8.4 Finite/cofinal admission tests

Before investing in a pro/ind construction, compute:

1. the exact adjacent-stage compatibility defect in (8.1);
2. whether the carrier states escape weakly as in (8.5);
3. whether comparison maps preserve the logarithmic form domain;
4. whether the lower bounds in (8.3) are carrier-normalized and uniform; and
5. whether a form core or tightness theorem survives completion.

A pro-object which retains every stage also retains every unresolved sign.  A
colimit which forgets the moving states is unusable.  The useful limit is one
whose enrichment preserves the carrier state/form pairing; corona and Hilbert
ultraproduct formulations do this only after uniform boundedness has been
proved.

### 8.5 Novelty assessment

These are standard form-convergence facts.  Their role is downstream quality
control.  They should not consume the main research effort until a
finite-stage order or covariance mechanism passes Sections 3--5.

## 9. Theorem card G: quantitative positive polarization

### 9.1 Additive approximate Rosati theorem

Let `A` be a finite complex matrix and let `G>0` be a positive metric fixed
independently of the spectrum under investigation.  Suppose

```text
-epsilon G <= A*G+GA-G <= epsilon G.                  (9.1)
```

Then every eigenvalue `lambda` of `A` satisfies

```text
abs(Re(lambda)-1/2)<=epsilon/2.                        (9.2)
```

#### Proof

For an eigenvector `Av=lambda v`,

```text
v*(A*G+GA-G)v
 =(2 Re(lambda)-1) v*Gv.                              (9.3)
```

Divide the two Loewner inequalities in (9.1) by the positive scalar `v*Gv`.
QED

If a global arithmetic generator has the nontrivial zeta zeros as its
spectrum, a zero-independent family of metrics satisfying (9.1) with one
uniform `epsilon<1` confines those zeros to

```text
epsilon_gap <= Re(rho) <= 1-epsilon_gap,

epsilon_gap=(1-epsilon)/2>0,                          (9.4)
```

more simply `abs(Re(rho)-1/2)<=epsilon/2`; in particular it gives a fixed
zero-free strip adjacent to `Re(s)=1`.  The exact equation `epsilon=0` is the
critical-line/RH-strength case.

### 9.2 Multiplicative version

If an arithmetic Frobenius-like endomorphism `F` obeys

```text
e^(-2 delta) q G <= F*G F <= e^(2 delta) q G,          (9.5)
```

then every eigenvalue satisfies

```text
sqrt(q)e^(-delta)<=abs(lambda)<=sqrt(q)e^(delta).      (9.6)
```

This follows by evaluating (9.5) on an eigenvector.  Exact Rosati unitarity is
the special case `delta=0`.

### 9.3 Correct categorical formulation

Bare rigid or neutral Tannakian structure supplies duality and reciprocal
spectrum, not (9.1) or (9.5).  The required object is closer to:

- a rigid C-star tensor/dagger category;
- a faithful unitary fiber functor to Hilbert spaces;
- a Frobenius/generator endomorphism whose trace or determinant gives the
  completed explicit formula; and
- a positive dagger, defined before its zero spectrum, for which the Rosati
  defect is uniformly bounded.

The new search target is therefore not immediately an exact Hodge structure.
It is a **uniformly quasi-polarized arithmetic object with defect below one**.
This is weaker and potentially more approachable.

### 9.4 Finite fail-fast test

For a concrete candidate `A_S,G_S` on `{infinity,p,q}` compute

```text
Delta_S=G_S^(-1/2)(A_S*G_S+G_S A_S-G_S)G_S^(-1/2).   (9.7)
```

The route advances only if all of the following hold.

1. `G_S` is constructed from arithmetic/categorical data without zero
   eigenvectors, Cholesky factorization of the desired Weil form, or
   optimization against the desired spectral band.
2. The exact prime, gamma, and pole trace fixture is reproduced.
3. `||Delta_S||<1` with a mechanism plausibly uniform under adjoining primes.
4. The construction is genuinely coupled.  An independent compact place
   torus with invariant metric and no mixed character returns the already
   eliminated orthogonal sector model.
5. There is a conservative spectral/determinant limit identifying the
   generator with completed zeta.

Solving a Lyapunov LMI for `G_S` after `A_S` is known is a detector and can
encode the desired spectral strip (and, for nonnormal matrices, may impose
additional control).  Only a functorial metric with independent
provenance counts.  Approximate tensor-coherence errors must be summable or
uniform; an error growing with the number of primes gives no fixed strip.

### 9.5 Sharp off-line sanity check

For

```text
A_a=diag(1/2+a,1/2-a),              a real,           (9.8)
```

equation (9.3) shows that every positive metric satisfying (9.1) must have

```text
epsilon>=2 abs(a).                                    (9.9)
```

Taking `G=I` attains equality.  Therefore optimizing the metric after seeing
this block recovers exactly its distance from the critical line; it cannot
manufacture a better strip.  The only possible gain is independent arithmetic
provenance for `G` together with an a priori defect estimate.

### 9.6 Novelty assessment

The matrix inequality is elementary.  Its use as an **approximate rather than
exact** polarization target is a materially new direction from the
consolidation.  It has the highest conceptual upside and the lowest current
construction readiness.

## 10. Theorem card H: obstruction and index classes which should be parked

### 10.1 Corona `K`-classes require the missing gap

Let `A=(A_T)` be a uniformly bounded self-adjoint family in

```text
product_T B(H_T) / direct_sum_(norm->0) B(H_T).       (10.1)
```

The class `[A]` is invertible only if the smallest singular values of `A_T`
are bounded away from zero eventually; conversely such a bound supplies a
bounded inverse class.  Therefore continuous sign functional calculus and a
stable negative-spectral `K_0` class require a uniform asymptotic gap.

Defining `P_-(A_T)` separately at every finite stage is exact but is the
original negative spectral projection.  Passing to `K`-theory does not make
its arithmetic value computable.  A new index route needs an independent
arithmetic Fredholm cycle and a proved pairing equal to the carrier index.

### 10.2 Ordinary extension and motive routes

- `Ext^1` in finite Hilbert space vanishes.
- Morita equivalence is conservative and transports the sign problem.
- A nonfaithful motive or localizing invariant can forget the negative line.
- Trace, supertrace, and `K_0/K_1` of the ambient algebra do not determine the
  order of the selected element.

These formalisms should be revisited only when a concrete arithmetic cycle,
nonsemisimple extension, or positive realization maps nontrivially to the
quotient obstruction of Section 6 or the carrier state of (7.5).

## 11. Reduced execution program

The positive-route audit suggests the following order of work.

### Phase A: cheap exact pruning

1. Freeze one finite, zero-independent arithmetic operator system `E_T`.
2. Freeze the positive-row map `X_T`, target row `a_T`, and actual aggregate
   decomposition.
3. Project every prime, gamma, pole, rational, and collateral row through
   `Obs_(X,a)` from (6.1).
4. For the quadratic remainder compute or bound the carrier-slice support
   `h_eta` from (7.5a), not merely its two-sided norm.
5. Attach the proved growth grades.  Discard aligned and subcarrier terms.

This produces a much smaller list of actual coefficient combinations.

### Phase B: one finite order experiment

6. Choose a cross-aware observation `Phi_T` rather than an ordinary diagonal
   packet cover.
7. Test restricted cone equality (3.1).
8. Search for a CP recovery (4.5).
9. If recovery fails but `Phi_T` has a natural semilocal origin, compute its
   covariance (5.2) and test (5.5).

There is no reason to run additional generic local windows, matrix
amplifications, dephasings, or free spectrahedral relaxations before this
gate.

### Phase C: only after finite survival

10. Prove carrier-uniform recovery or covariance estimates.
11. Select a carrier-conservative corona, ultraproduct, or Mosco topology and
    pass the moving-vector test (8.5).
12. Prove the cofinal spectral/explicit-formula identification.

### Parallel high-risk program

Independently, test one arithmetically defined metric on the smallest coupled
semilocal generator and evaluate (9.7).  A defect below one, with independent
metric provenance, would be more significant than another exact trace model.

## 12. What has been expanded and what has been pruned

### Expanded

- zeta-restricted rather than universal operator-system order descent;
- CP recovery as a constructive local-to-global certificate;
- CP covariance as a positive, controlled multiplicative defect;
- approximate polarization as a fixed-strip target weaker than exact purity;
- carrier-sensitive Mosco/ultraproduct limits once a finite mechanism exists.

### Pruned as free sources of a strip

- matrix amplification of the mirror;
- generic CP averaging, conditional expectation, or correspondence without a
  recovery or an arithmetic covariance identity;
- bornological terminology without a grade-and-angle estimate;
- ordinary strong, weak, trace, or compact-open limits;
- bare rigid/Tannakian duality;
- ordinary derived `Ext` in semisimple finite Hilbert space;
- a corona `K`-class before a uniform gap is proved; and
- fitted Lyapunov/Rosati metrics.

## 13. Honest novelty and scope

None of the abstract lemmas above is new category theory.  The potentially
novel program-level insights are:

1. the exact quotient-cone target `closure(C_J+V_T_perp)` for the actual zeta
   operator system;
2. the CP-recovery SDP as the finite admission test for local positivity;
3. the Stinespring covariance as a distinguished positive candidate for the
   missing cross-place reservoir;
4. the additive obstruction projection modulo `im(X*)+C a`; and
5. the carrier-slice one-sided support functional as the sharp finite
   cancellation test; and
6. the quantitative `epsilon<1` polarization target which would already give
   a fixed strip.

They become publishable mathematics only if one is paired with a substantive
zeta-specific theorem: a nontrivial recovery bound, an exact covariance
identity with carrier-scale sign, or an independently constructed
quasi-polarization.  At present they are a rigorous and materially narrower
research program, not a zero-free theorem.

## 14. Repository and literature anchors

Repository context:

- `ZETA23-CATEGORICAL-CONSOLIDATION-FOUR-LEMMA-2026-08-12.md`;
- `ZETA23-DAGGER-CATEGORICAL-OPERATOR-COLLAPSE-2026-08-12.md`;
- `ZETA23-CATEGORICAL-SEARCH-GRAMMAR-AND-PRUNING-THEOREM-2026-08-12.md`;
- `CATEGORY-THEORETIC-SEARCH-PRUNING-REFEREE-AUDIT-2026-08-12.md`;
- `CATEGORY-THEORETIC-CONSOLIDATION-REFEREE-AUDIT-2026-08-12.md`;
- `ZETA23-EXOTIC-CATEGORICAL-ESCAPE-STRESS-TEST-2026-08-12.md`;
- `GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md`;
- `ZETA23-OPERATOR-PRECONDITIONING-FUNCTIONAL-CALCULUS-AUDIT-2026-08-12.md`.

Standard background for the terminology includes Stinespring dilation and
multiplicative domains for completely positive maps, operator-system complete
order embeddings, rigid C-star tensor categories and unitary fiber functors,
and Mosco convergence of quadratic forms.  These sources support the abstract
framework only; none supplies the zeta-specific recovery, covariance identity,
or polarization required above.
