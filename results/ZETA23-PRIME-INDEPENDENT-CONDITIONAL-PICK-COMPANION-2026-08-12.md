# A prime-independent conditional-Pick companion and its exact missing measure law

Status: exact sharp-Loewner square representation, an explicit
prime-independent companion theorem, an archimedean-complete one-square
arithmetic target, and a negative-square obstruction, 2026-08-12.  The
conditional-Pick hypothesis below is not proved for the actual von Mangoldt
data.  No zero-free strip or improved zero bound is proved.

## 1. Verdict

There is a distinguished prime-independent way to turn conditional Pick
positivity into the joint two-dimensional Ritz orientation inequality.

Let `S` be the endpoint-jet and selected-positive-row quotient, let `a` be
its unit carrier direction, and, assuming the projection is nonzero, let
`g` be the projection to `S` of the unique endpoint/Jacobi boundary vector

```text
r=P_m*Delta*q_(m-1).                                (1.1)
```

Here `P_m` is the endpoint-moment projection, `Delta=diag(tau_k)`, and
`q_(m-1)` is the last discarded discrete orthogonal polynomial.  Thus `g`
is fixed by the grid, endpoint order, and selected candidate geometry, not
by any prime coefficient.

Put

```text
theta_* =1-|<a,g/||g||>|^2.                         (1.2)
```

If `dim S>=3`, then for every `0<theta<=theta_*` there is an explicit unit
companion

```text
w_(g,theta) perpendicular a                         (1.3)
```

depending only on `(a,g,theta)` and one geometry-fixed tie-breaker, and a
phase `omega`, such that

```text
z_theta=sqrt(theta)*a
        +omega*sqrt(1-theta)*w_(g,theta)

is perpendicular to g.                             (1.4)
```

Consequently the genuinely weaker arithmetic law

```text
<x,(K+delta*I)x> >=0      for every x in S with x perpendicular g
                                                               (1.5)
```

implies the exact joint Ritz inequality

```text
theta*r+(1-theta)*d
 +2*sqrt(theta*(1-theta))*c >=-delta,               (1.6)

r=<a,Ka>,  d=<w,Kw>,  c=|<w,Ka>|.                  (1.7)
```

Law (1.5) is much weaker than a whole lower edge.  It permits an arbitrarily
large negative square in the known direction `g` and arbitrarily large
positive spectrum.  Its companion remains linear in every completed prime,
pole, and gamma coefficient.

The exact Loewner representation identifies the minimum arithmetic content
still missing.  If

```text
Phi_x(t)=2*S(t)*sum_k x_k/(t-tau_k),                (1.8)
```

then, after the standard `L^(-2)` normalization,

```text
<x,Kx>=L^(-2)*integral nu_X(t)*|Phi_x(t)|^2 dt.     (1.9)
```

The joint inequality needs only one signed-measure comparison:

```text
integral |Phi_(z_theta)|^2 d(nu_shift,+)
 >= integral |Phi_(z_theta)|^2 d(nu_shift,-).       (1.10)
```

This “one-square Jordan domination” is necessary and sufficient for the
chosen boundary state.  It is strictly weaker than pointwise positivity of
`nu_shift`, positivity of the whole Pick matrix, a KMT maximum bound, or a
whole-matrix lower edge.

Neither confluent Loewner structure nor an unanchored statement that the
Pick kernel has at most one negative square implies (1.10).  A single
negative Cauchy atom already has one negative square, but its negative
functional can be rotated onto `z_theta`.  The missing property is therefore
not merely generalized-Nevanlinna index `<=1`; it is a **geometry-anchored**
negative square, equivalently (1.5), or the still weaker one-square law
(1.10).

## 2. Exact sharp square and confluent Pick representations

On the critical grid, write

```text
tau_k=tau_0+2*pi*k/L,
S(t)=sin(L*(t-tau_0)/2).                            (2.1)
```

For any real multiplier `nu` for which the sharp form is defined, its
sign-conjugated matrix is exactly

```text
H_nu(k,l)
 =integral_R 4*S(t)^2*nu(t)
        /[(t-tau_k)*(t-tau_l)]dt.                  (2.2)
```

Therefore every complex coefficient vector satisfies

```text
x^*H_nu*x=integral_R nu(t)*|Phi_x(t)|^2dt,          (2.3)
```

with `Phi_x` from (1.8).  The constant multiplier has

```text
H_1=2*pi*L*I.                                      (2.4)
```

Equations (2.2)--(2.4) survive every orthogonal endpoint and target-row
compression.  Thus for `K=P_S H_nu P_S/L^2`, adding a constant `c` to the
multiplier adds exactly

```text
(2*pi*c/L)*I                                       (2.5)
```

to `K`.  In particular, the shift `delta*I` corresponds to

```text
nu_delta=nu+delta*L/(2*pi).                         (2.6)
```

The regularized Cauchy transform

```text
J_nu(z)=integral_R 4*S(t)^2*nu(t)
       *[1/(t-z)-t/(1+t^2)]dt                      (2.7)
```

has the exact confluent Loewner data

```text
H_nu(k,l)=[J_nu(tau_k)-J_nu(tau_l)]/(tau_k-tau_l),
H_nu(k,k)=J_nu'(tau_k).                             (2.8)
```

If `nu>=0`, then `J_nu` is Herglotz and every Pick matrix in (2.8) is
positive.  Conversely, the finite compressed statement needed here is much
smaller: (1.5) asks positivity only after one known hyperplane compression,
and (1.10) asks it on only one square.

This also explains why divided differences are the correct collision
coordinates.  If a target row is varied in depth or ordinate, its normalized
difference quotient converges to the derivative of its Cauchy feature in
(1.8).  The associated `2 x 2` form is the corresponding confluent Pick jet;
no raw near-collision singularity occurs.  Orthogonalizing that derivative
gives the previously defined confluent target-row companion.  The theorem
below applies equally to that companion whenever its boundary state lies in
the anchored hyperplane.

## 3. Anchored conditional-Pick companion theorem

### Theorem 3.1

Let `H` be a complex Hilbert space of dimension at least three, `a` a unit
vector, and `0!=g in H`.  Set

```text
rho=<a,g>,
g_perp=g-rho*a,
beta=||g_perp||,
theta_*=beta^2/||g||^2.                             (3.1)
```

For every `0<theta<1` with `theta<=theta_*`, there is a unit `w perpendicular
a` satisfying

```text
|<g,w>|=sqrt(theta/(1-theta))*|<g,a>|.              (3.2)
```

Hence a unit phase `omega` can be chosen so that (1.4) holds.  If `a` is
already perpendicular to `g`, the conclusion also holds at `theta=1`, with
`z_1=a`.

If a Hermitian operator `K` obeys (1.5), then the boundary Ritz value on
`span{a,w}` satisfies (1.6).

Conversely, if `theta>theta_*`, no unit `w perpendicular a` and no phase can
make a boundary state of carrier mass `theta` orthogonal to `g`.

#### Proof

When `beta>0`, put `u=g_perp/beta`.  Choose a unit
`v perpendicular span{a,u}` and set

```text
t=sqrt(theta/(1-theta))*|rho|/beta,
w=t*exp(i chi)*u+sqrt(1-t^2)*v,                     (3.3)
```

where `chi` is arbitrary.  Condition `theta<=theta_*` is exactly `t<=1`.
Varying `chi` gives (3.2), and a second phase `omega` cancels the two terms
in `<g,z_theta>`.  If `rho=0`, take `t=0` and choose `v` in
`a^perp intersect g^perp`.

By (1.5),

```text
<z_theta,K z_theta>>=-delta.                        (3.4)
```

The left side is one allowed phase in the phase-optimized boundary Ritz
value.  Maximizing the cross phase replaces its cross term by
`2*sqrt(theta*(1-theta))*|<w,Ka>|`, proving (1.6).  QED

For the converse, every unit `w perpendicular a` satisfies
`|<g,w>|<=beta`.  Cancellation would require the right side of (3.2), so
`sqrt(theta/(1-theta))*|rho|<=beta`, which is exactly
`theta<=theta_*`.

In dimension two, the same proof works only at the single balanced value
`theta=theta_*`, because there is no vector `v` with which to decrease
`|<g,w>|`.  Thus (1.2) is also an exact geometric admission gate: a
one-anchor/two-dimensional proof cannot reach carrier fractions above
`theta_*` without additional structure.

### Corollary 3.2 (minimal one-square version)

The full conditional law (1.5) can be replaced by the single inequality

```text
<z_theta,(K+delta*I)z_theta> >=0.                   (3.5)
```

Under (2.3)--(2.6), this is exactly (1.10).  No assertion about any other
vector or any pointwise value of the multiplier is required.

## 4. The inherited Jacobi boundary anchor

Before the selected-row quotient, let

```text
W_m={x: sum_k x_k*tau_k^j=0, 0<=j<m},              (4.1)
P_m=projection onto W_m,
A_m=P_m*Delta*P_m|W_m.                              (4.2)
```

For every exact sharp multiplier, endpoint compression gives

```text
[A_m,B_m]=s*r^*-r*s^*,
r=P_m*Delta*q_(m-1),
s=P_m*H_nu*q_(m-1).                                 (4.3)
```

The vector `r` is nonzero, independent of `nu`, and cyclic for the trailing
Jacobi matrix `A_m`.  It is the unique geometric boundary through which
multiplication by the coordinate leaks out of `W_m`.  This distinguishes it
from `s`, which contains the arithmetic coefficients.

Let `P_S` impose the selected positive row and put

```text
g=P_S*r.                                            (4.4)
```

Using `g` in Theorem 3.1 produces a companion which is independent of the
prime sequence.  Every entry in (1.7) is therefore one linear completed
von-Mangoldt--continuum--gamma scalar.  No `K^2` or `K^3` correlation is
introduced.

The word ``boundary'' here is inherited from the endpoint compression.
After the additional selected-row compression, `g=P_S*r` is no longer
characterized as the unique displacement boundary of the twice-compressed
pair.  Compressing `A_m,B_m` by `P_S` adds the usual terms

```text
-P_S*A_m*(I-P_S)*B_m*P_S
+P_S*B_m*(I-P_S)*A_m*P_S,                          (4.4a)
```

which supply an additional selected-row boundary.  Thus `g` is a
distinguished, geometry-defined, prime-independent **inherited anchor**, not
a uniquely canonical anchor after the selected quotient.

There is a natural coordinate-free choice for the otherwise free vector
`v` in (3.3).  Let

```text
h_alpha=P_S*partial_alpha(y_alpha)                  (4.5)
```

be the confluent target-depth row and project it orthogonally away from
`span{a,g_perp}`.  When this projection is nonzero, prescribing its
normalization fixes `v` without using the primes.  This gives a
geometry-defined **boundary--confluent
companion**.  It is stable under collision because (4.5) is the Hermite
limit of normalized divided differences.  If it vanishes, the construction
does not silently become arithmetic-adaptive: one may use the first nonzero
vector in the geometry-fixed Jacobi Krylov list
`g,A_m g,A_m^2 g,...`, after the same projections, or record failure of the
two-dimensional companion.

Projection through the selected row can make `g` small or zero, and
`theta_*` need not be uniformly close to one.  If `g=0`, Theorem 3.1 and
formula (1.2) are not invoked: `x perpendicular g` is the whole space, and
a companion must be fixed by a separate geometry-only tie-breaker.  The
nonzero inherited-anchor mechanism has disappeared rather than selected a
canonical direction.  These are genuine geometric failure modes, not
arithmetic estimates.  In the existing floating fixtures
at `alpha=.4` and aperture fraction `.2`, the values of `theta_*` were

| `T` | 64 | 128 | 256 | 512 | 1024 |
|---:|---:|---:|---:|---:|---:|
| `theta_*` | .7275 | .8873 | 1.0000 | .9773 | .9894 |

The parity-sensitive value at `T=256` is consistent with the previously
observed coordinate-companion behavior.  These are floating geometry checks,
not a uniform lower bound for `theta_*`.

## 5. Archimedean completion isolates the missing arithmetic law

For the actual completed sharp form,

```text
nu_X(t)=mu(t)+r_0(t)-(1/pi)*Re E_X(t),
r_0(t)=1/[2*pi*(1/4+t^2)],                           (5.1)

E_X(t)=sum_(n<=X) Lambda(n)n^(-1/2+it)
       -integral_1^X x^(-1/2+it)dx.                 (5.2)
```

The proved gamma bound `mu(t)>-1` and `r_0>=0` imply the pointwise statement

```text
mu+r_0+1>=0.                                        (5.3)
```

Thus `J_(mu+r_0+1)` is genuinely Herglotz and

```text
H_bg+H_1>=0,
K_bg+(2*pi/L)*I>=0.                                 (5.4)
```

The gamma and rational-pole completion therefore create no hidden negative
square after the explicit normalized shift `2*pi/L`.  At a fixed-depth
carrier `kappa asymp X^alpha/L`, this is `o(kappa)`.

For the state `z_theta` of Theorem 3.1, the exact remaining arithmetic target
is only

```text
integral_R |Phi_(z_theta)(t)|^2
 [mu(t)+r_0(t)+1-(1/pi)*Re E_X(t)]dt >=0.           (5.5)
```

If (5.5) holds, then

```text
Q_theta(a,w)>=-2*pi/L=o(kappa).                     (5.6)
```

This is a single complete smoothed correlation, not a pointwise estimate for
`A_X,D_X` and not a maximum over the grid.  In the completion-preserving time
domain it is exactly

```text
<z_theta,(H_bg+H_1)z_theta>
-2*integral_[1,X] v^(-1/2)
   Re R_(f_ztheta)(log v) d(psi(v)-v) >=0.          (5.7)
```

All prime powers and the continuum center remain in (5.7).  Proving (5.5)
or (5.7) for this predetermined geometry-defined state would be a genuinely
weaker arithmetic theorem than the KMT route: it permits large values of
`A_X,D_X` away from this one square and arbitrarily large positive completed
spectrum.

The anchored conditional version is the same statement for every
`x perpendicular g`:

```text
integral |Phi_x|^2*(nu_X+1)>=0,    x perpendicular g.   (5.8)
```

It implies all Theorem 3.1 companions with error `2*pi/L`.  The minimal
version needed for one `theta` is only (5.5).

## 6. Herglotz, conditional positivity, and negative squares

There is a strict hierarchy.

1. `nu_X+1>=0` pointwise makes `J_(nu_X+1)` Herglotz and proves positivity
   of the full sharp Pick matrix.  This is far stronger than needed and is
   not known.
2. Equation (5.8) says the finite confluent Pick form is conditionally
   positive on one **known** hyperplane.  It allows one negative square, but
   that square must be anchored by `g`.
3. Equation (5.5) asks positivity of only one square in that hyperplane.

In Jordan notation, with `nu_X+1=nu_+-nu_-`, (5.5) is exactly

```text
integral |Phi_(z_theta)|^2 dnu_+
 >=integral |Phi_(z_theta)|^2 dnu_-.                (6.1)
```

This is the minimal missing signed-measure property.

An unanchored generalized-Nevanlinna statement is insufficient.  Take one
negative Cauchy atom at a real point `t_0` away from the grid:

```text
dSigma=-M*delta_(t_0).                              (6.2)
```

Its Pick form is

```text
q_M(x)=-M*|Phi_x(t_0)|^2,                           (6.3)
```

which has exactly one negative square, with arithmetic-dependent negative
functional `x -> Phi_x(t_0)`.  For every nonzero predetermined
`z_theta`, choose `t_0` away from the discrete zero set of
`Phi_(z_theta)`; then (6.3) is strictly negative on the proposed state.
Adding the positive shifted archimedean background from (5.3) preserves the
index bound `<=1`, and increasing `M` preserves the failure on `z_theta`.
Any other fixed completed background is still overwhelmed on this state.
Narrow smooth negative bumps give the same strict finite counterexample
inside the smooth signed-multiplier class (with the negative index statement
understood for the shifted positive background).

Thus “Pick index at most one” does not prove the Ritz inequality.  One must
either know its negative functional in advance and place `z_theta` in its
kernel, or prove the direct one-square domination (6.1).

## 7. Exact structural obstruction and scope

The arbitrary-confluent-data theorem for the sharp Loewner map shows that
smooth signed multipliers can prescribe every finite set of Loewner values
and derivatives.  In particular the constant multiplier `-M` gives

```text
H_(-M)=-2*pi*L*M*I,                                 (7.1)
```

which has the same zero/rank-two displacement identity but violates (5.8)
for every anchor and every companion.  Restoring the fixed archimedean
completion does not change this for large `M`.

Therefore none of the following implies the new arithmetic law:

```text
confluent Loewner representation;
rank-two Jacobi displacement;
divided-difference collision stability;
existence of a signed Cauchy representation;
an unanchored bound of one negative square;
the positive gamma/rational completion.             (7.2)
```

This is an information-level obstruction, not a von Mangoldt
counterexample.  The actual multiplier is the specific function (5.1), and
the actual atoms in (5.2) may obey a correlation law absent from arbitrary
signed measures.

The exact research target is now smaller than the earlier three-entry KMT
card:

> Prove the one-square completed inequality (5.5) for the explicit inherited
> boundary-Pick companion `w_(g,theta)`, uniformly in the candidate geometry;
> or prove the anchored conditional-Pick law (5.8).  Separately establish a
> uniform geometric lower bound `theta_*>=theta_0` for the desired carrier
> fraction.

The first alternative is one predetermined smoothed von Mangoldt discrepancy
correlation.  The second permits one carrier-sized negative square but fixes
its direction geometrically.  Either is strictly more targeted than bounding
the complete operator or every `A_X,D_X` value separately.

What is not proved:

1. No uniform lower bound for `theta_*` is known.
2. Neither (5.5) nor (5.8) is proved for actual von Mangoldt coefficients.
3. Current coefficient positivity does not imply them, because (5.7) pairs
   `d(psi-v)` with a sign-changing modulated autocorrelation.
4. The negative-square atom (6.2) is not an actual zeta configuration.
5. No numerical or analytic zero bound is changed.

## 8. Reproducible linear-algebra checks

The finite companion construction is implemented in
[`conditional_pick_companion.py`](../src/conditional_pick_companion.py),
with tests in
[`test_conditional_pick_companion.py`](../src/test_conditional_pick_companion.py).
They verify:

1. exact carrier mass and anchor cancellation for a complex anchor;
2. implication from an anchored conditionally positive form to the
   phase-optimized joint Ritz value;
3. sharp failure above `theta_*`; and
4. the full-carrier endpoint when `a perpendicular g`; and
5. coordinate-free selection by a supplied confluent tie-breaker.

Run:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_conditional_pick_companion.py \
  src/test_carrier_ritz_loewner_gate.py
```

The combined focused suite has ten passing tests.  These checks certify the
finite linear algebra, not the missing actual-von-Mangoldt inequality (5.5).
