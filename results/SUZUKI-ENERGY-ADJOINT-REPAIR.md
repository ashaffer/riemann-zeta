# Suzuki's finite-window energy derivative: adjoint repair and phase test

Status: the abstract form-space theorem is proved below at the ordinary
mathematical level.  Its Riesz/partial-adjoint core is formalized in Lean;
the distributional ODE and the application-specific closed-form and form-core
hypotheses remain analytic inputs.  Section 8 gives the falsification protocol
whose completed run is reported in
[`SHIFT-PHASE-COVARIANCE-FAIL-FAST.md`](SHIFT-PHASE-COVARIANCE-FAIL-FAST.md).

This note does **not** prove the Riemann hypothesis.  It repairs a domain gap
in one finite-window construction and isolates the additional covariance that
would be needed before its real spectra could have canonical arithmetic
content.

## 1. Why this audit is necessary

For a fixed support `a>0`, let `A_a` be the self-adjoint operator associated
with the localized completed Weil form `Q_W^a`, and let `lambda_a` be the
bottom of its spectrum.  Suzuki chooses a real shift

```text
sigma < lambda_a,                 T_(a,sigma) = A_a - sigma I,
```

completes `C_c^infty(-a,a)` in the energy norm

```text
||u||_(a,sigma)^2 = Q_W^a(u) - sigma ||u||_2^2,
```

and studies `D=i d/dx` in that energy Hilbert space.  Section 6.2 of
[Suzuki's 2026 v1 preprint](https://arxiv.org/html/2606.09096v1) argues that
continuity of a functional in the energy norm implies continuity in the
`L2` norm.  The implication goes in the other direction: since

```text
T_(a,sigma) >= (lambda_a-sigma) I,
||u||_2 <= (lambda_a-sigma)^(-1/2) ||u||_(a,sigma),
```

`L2`-continuity implies energy-norm continuity, but energy-norm continuity
need not imply `L2`-continuity.  The same passage writes `T_(a,sigma)v` for a
generic form-domain vector, although an unbounded operator is defined only on
its operator domain.

This is a gap in the displayed proof, not a counterexample to its conclusion.
The conclusion can be recovered by treating `T_(a,sigma)v` as a form-dual
object.  The repair is useful beyond this paper because it applies to any
coercive translation-invariant energy form on a finite interval.

## 2. Abstract setting

All inner products below are linear in the first variable.  Let

```text
I = (-a,a),              H = L2(I),              C = C_c^infty(I).
```

Let `t` be a densely defined closed Hermitian form on `H`.  Assume:

1. **Strict coercivity.**  There is `c>0` such that

   ```text
   t[u] >= c ||u||_H^2.
   ```

2. **Core.**  `C` is a form core for `t`.

3. **Distribution compatibility.**  The inclusion of `C`, with its usual
   test-function topology, into the form domain is continuous.  Thus every
   continuous form-dual functional restricts to a distribution on `I`.

4. **Energy symmetry of differentiation.**  `D=i d/dx` maps `C` to `C` and

   ```text
   t(Du,v) = t(u,Dv)                    (u,v in C).
   ```

Write

```text
V = Dom(t),       (u,v)_V = t(u,v),       ||u||_V^2=t[u].
```

Coercivity gives a continuous dense rigging

```text
V  ->  H  ->  V^x,
```

where `V^x` is the continuous anti-dual of `V`.  The pivot embedding and the
Riesz map are

```text
(iota h)(u) = (h,u)_H,              (Jv)(u) = (v,u)_V.
```

Both maps are linear; `J:V -> V^x` is an isometric isomorphism.  For a
functional `F` on `C`, define the distributional transpose of `D` by

```text
(D^x F)(u) = F(Du),                 u in C.
```

With these conventions, `D^x` acts as `i d/dx` on ordinary distributions.
Indeed, for a locally integrable `f`, integration by parts gives

```text
D^x(iota f) = iota(i f').
```

This sign is tied to the anti-dual convention used here; the transpose on
linear distributions is often written with the opposite sign.  Lean/mathlib
also makes the inner product conjugate-linear in its first slot.  Its formal
counterpart of a functional equation at `z` therefore produces an adjoint
eigenvector at `conj(z)`.  The Lean module records that conjugation explicitly
rather than silently changing (3.2).

The abstract Riesz and partial-adjoint statements in Sections 2--3 are
formalized in
[`GelfandTripleAdjoint.lean`](../lean/rhbridge/RHBridge/GelfandTripleAdjoint.lean),
with focused axiom output in
[`GelfandTripleAdjointAudit.lean`](../lean/rhbridge/RHBridge/GelfandTripleAdjointAudit.lean).
The interval-specific distributional ODE classification is deliberately kept
as a separate analytic input.

## 3. The repaired adjoint theorem

### Theorem 3.1 (energy-space adjoint)

Regard `D=i d/dx` as a densely defined operator

```text
D : C subset V -> V.
```

Under assumptions 1--4, `D` is symmetric and closable.  Its Hilbert-space
adjoint in `V` is characterized by

```text
Dom(D*) = {v in V : D^x(Jv) belongs to J(V)},
J(D*v)  = D^x(Jv).                                      (3.1)
```

Here equality is equality of distributions on `I`; the range condition says
that the resulting distribution extends to a continuous form-dual functional
lying in the Riesz image.

#### Proof

Symmetry is assumption 4, and every densely defined symmetric operator is
closable.  By definition, `v` belongs to `Dom(D*)` precisely when there is a
`g in V` such that

```text
(Du,v)_V = (u,g)_V                  for every u in C.
```

Taking complex conjugates and using the definitions of `J` and `D^x`, this is
equivalent to

```text
(Jv)(Du) = (Jg)(u)                  for every u in C,
D^x(Jv)  = Jg.
```

Since `J` is bijective, such a `g` exists exactly under the range condition in
(3.1), and then `g=J^(-1)D^x(Jv)`.  This proves the theorem.  Notice that the
argument never applies the unbounded operator associated with `t` to a generic
element of `V`.  QED

### Theorem 3.2 (deficiency spaces)

For every `z in C`, set

```text
e_z(x) = exp(-i z x).
```

Then

```text
Ker(D* - z) = C * J^(-1)(iota e_z).                     (3.2)
```

In particular, `D` has deficiency indices `(1,1)`.

#### Proof

By Theorem 3.1,

```text
D*v=zv    iff    D^x(Jv)=z Jv.
```

The right side is the distributional ordinary differential equation

```text
i (Jv)' = z Jv.
```

On the connected interval `I`, all its distributional solutions are scalar
multiples of `e_z`.  Conversely, `e_z` belongs to `H=L2(I)` for every complex
`z`, and coercivity makes the pivot embedding `H -> V^x` continuous.  Hence
`iota e_z` lies in `V^x`, and surjectivity of the Riesz map supplies the unique
vector `J^(-1)(iota e_z) in V`.  It satisfies the range condition in (3.1) and
is nonzero.  Formula (3.2) follows.  Taking `z=i` and `z=-i` gives one
deficiency vector in each half-plane.  QED

### Corollary 3.3 (operator representation)

Let `T>=cI` be the positive self-adjoint operator representing `t`.  Then, for
every `h in H`,

```text
J^(-1)(iota h) = T^(-1) h.                             (3.3)
```

Consequently one may take

```text
v_+ = T^(-1) exp(x),              v_- = T^(-1) exp(-x)  (3.4)
```

as the deficiency vectors at `+i` and `-i`.

#### Proof

Strict positivity makes `T^(-1)` a bounded operator on `H`, with range in
`Dom(T)`.  If `v=T^(-1)h`, then for every `u in V`,

```text
(Jv)(u) = t(v,u) = (Tv,u)_H = (h,u)_H = (iota h)(u).
```

Injectivity of `J` proves (3.3).  In particular, no separate assertion that
`exp(+/-x)` belongs to the range of `T` is needed.  It belongs to `H`, and the
bounded inverse supplies its unique preimage.

If reflection `Ru(x)=u(-x)` preserves `t`, then `R` commutes with `T` and
interchanges the two vectors in (3.4).  Their energy norms are therefore
equal.  Without reflection symmetry they can simply be normalized separately
before applying von Neumann's extension theorem.

## 4. Boundary determinant

Let `d_+` and `d_-` be unit deficiency vectors at `+i` and `-i`.  Von
Neumann's theorem gives the self-adjoint extensions

```text
Dom(D_theta)
  = Dom(closure(D)) direct_sum C * (d_+ + exp(i theta) d_-),
theta in R/(2 pi Z).                                    (4.1)
```

Let `v_z=J^(-1)(iota e_z)`.  Define

```text
F_+(z) = integral_I exp(-i z x) conjugate(d_+(x)) dx,
F_-(z) = integral_I exp(-i z x) conjugate(d_-(x)) dx.
```

The continuous embedding `V -> L2(I)` and boundedness of `I` imply
`d_+,d_- in L1(I)`.  Hence `F_+` and `F_-` are entire functions of exponential
type at most `a`.  Direct evaluation of the boundary form

```text
B(v,w)=(D*v,w)_V-(v,D*w)_V
```

shows that `v_z` belongs to (4.1) exactly when

```text
W_(t,theta)(z)
  := (z+i) F_+(z) + exp(-i theta) (z-i) F_-(z) = 0.     (4.2)
```

Thus the zeros of `W_(t,theta)` are precisely the eigenvalues of the
self-adjoint extension `D_theta` and are real.  They are simple as well.  The
map `z -> v_z` is entire as a `V`-valued map.  If both `W(lambda)=0` and
`W'(lambda)=0`, then `v_lambda` and `v'_lambda` obey the same extension
boundary condition, while differentiation of the weak eigen-equation gives

```text
(D_theta-lambda)v'_lambda=v_lambda.
```

Self-adjointness makes the inner product of the left side with `v_lambda`
zero, whereas the right side gives `||v_lambda||_V^2`, a contradiction.

Changing the inner-product convention, replacing `z` by `-z`, and changing
the phases of the normalized deficiency vectors transforms (4.2) into
Suzuki's displayed formula when the form is invariant under complex
conjugation, so the deficiency vectors carry the required real structure:

```text
(z-i) integral v_+(x) exp(i z x) dx
  + exp(i theta) (z+i) integral v_-(x) exp(i z x) dx.
```

These changes multiply or reflect the characteristic function and relabel
`theta`; they do not alter its real-zero conclusion.

The argument through (4.2) is unconditional for a fixed coercive shifted form.
It does not identify the zeros with zeta zeros and does not give a canonical
choice of `theta`.

## 5. Audit of the completed Weil instantiation

Let `q_a(u,v)=Q_W^a(u,v)` be the completed localized zeta Weil form in the
normalization used by RHBridge.  The following inputs are supplied by the
operator theory in the cited literature and are not reproved in this note:

1. **Closed semibounded form.**  `q_a` is lower semibounded and closed (or
   lower semicontinuous with its canonical closed realization), and has an
   associated self-adjoint operator `A_a` with discrete spectrum.  See
   [Suzuki 2026 v1, Sections 1--3](https://arxiv.org/html/2606.09096v1) and the
   Connes--Consani--Moscovici construction cited there.

2. **Form core.**  The form-norm closure of `C_c^infty(-a,a)` gives the
   relevant energy space.  The proof of Suzuki's Theorem 1.1, especially the
   inclusion around equation (3.2), shows that a known form core lies in that
   smooth closure and hence that the closure is the whole form domain.
   Corollary 1.2 then states the corresponding minimization result.  A fully
   formal implementation should import the exact form-core statement, rather
   than infer it only from equality of Rayleigh infima.

3. **Strict shift.**  For `sigma<lambda_a`, the shifted form

   ```text
   t_(a,sigma)(u,v) = q_a(u,v) - sigma (u,v)_2
   ```

   is coercive with constant `lambda_a-sigma`.

4. **Distribution continuity.**  On a fixed compact interval, the Weil
   distribution and the convolution map are continuous on the smooth test
   topology.  This makes the inclusion of the test core into the logarithmic
   form domain continuous and permits the use of distributions in Theorem 3.2.

The energy symmetry needed in assumption 4 of Section 2 is elementary once
the Weil form has been identified correctly; it is not an RH input.  Write

```text
q_a(u,v) = W(u * tilde(v)),
(tau_s u)(x)=u(x-s).
```

For `u,v in C_c^infty(-a,a)` and sufficiently small `s`, simultaneous
translation stays inside the interval and

```text
(tau_s u) * tilde(tau_s v) = u * tilde(v).
```

Differentiating at zero and remembering that the second argument of a
Hermitian form is conjugate-linear gives

```text
q_a(iu',v)=q_a(u,iv').                                (5.1)
```

The `L2` term has the same property, so (5.1) holds for `t_(a,sigma)`.  The
completed pole terms cause no exception: simultaneous translation already
cancels inside the autocorrelation before `W` is applied.

Reflection invariance likewise follows from the even/Hermitian completed Weil
kernel.  Therefore, conditional only on literature inputs 1, 2, and 4, the
abstract theorem proves at every fixed `a` and every `sigma<lambda_a` that

```text
Ker(D_(a,sigma)^* - z)
  = C * (A_a-sigma I)^(-1) exp(-i z x),
n_+=n_-=1.                                             (5.2)
```

This repairs the finite-window self-adjoint-extension construction without
assuming `sigma=0`, Weil positivity, or RH.

### What remains conditional or open

The following statements do not follow from (5.2):

- that `sigma=0` is admissible at every support;
- that one choice of extension phase is canonical;
- that the finite-window extensions form a compatible family as `a` grows;
- strong or norm resolvent convergence to a global operator;
- compact-local convergence of a characteristic determinant to completed
  xi;
- any conclusion about RH.

Suzuki's global energy space and the heuristic strong-resolvent discussion in
Section 7 of the 2026 paper explicitly proceed under RH, where `sigma=0` is
available.  That conditional global picture cannot be used to justify the
unconditional finite-to-infinite passage.

## 6. Exact metric compatibility across windows

There is an elementary obstruction that should be handled before any
strong-resolvent claim.  Let `0<a<b`, use zero extension, and let
`sigma_a<lambda_a`, `sigma_b<lambda_b`.  For old-core vectors supported in
`(-a,a)`, restriction of the global Weil form gives

```text
q_b(u,v)=q_a(u,v).
```

Therefore

```text
t_(b,sigma_b)(u,v)-t_(a,sigma_a)(u,v)
  = (sigma_a-sigma_b) (u,v)_2.                         (6.1)
```

Consequently the natural zero-extension map is isometric on the old core if
and only if

```text
sigma_a = sigma_b.                                     (6.2)
```

For a finite range of windows one can choose a common shift below the lowest
of their spectral bottoms.  For an exhaustion `a->infinity`, the same natural
Hilbert-space nesting requires a fixed number satisfying

```text
sigma < lambda_a for every a.                          (6.3)
```

The stronger inequality `sigma < inf_a lambda_a` is sufficient but not
necessary; equality with the infimum is allowed when it is not attained at a
finite window.  RH makes `sigma=0` available because every finite-window
bottom is then strictly positive, even if their infimum is zero.
Unconditionally, (6.3) is an additional global analytic assertion and is not
supplied by the fixed-window construction.
Allowing `sigma` to vary is legitimate, but then one must formulate resolvent
convergence for varying Hilbert spaces and provide explicit comparison maps;
the phase `theta(a)` cannot by itself repair the metric mismatch in (6.1).

## 7. Shift and phase covariance at one window

Even at fixed `a`, the energy metric and deficiency vectors depend on the
auxiliary shift.  This produces a sharp, finite-window falsification test.

Fix `sigma,mu<lambda_a` and set

```text
R_sigma=(A_a-sigma I)^(-1),       R_mu=(A_a-mu I)^(-1).
```

The resolvent identity gives the exact relation

```text
R_mu - R_sigma = (mu-sigma) R_mu R_sigma.              (7.1)
```

In particular,

```text
v_z^(sigma)=R_sigma e_z,          v_z^(mu)=R_mu e_z,   (7.2)
```

so changing the shift can change the full deficiency family, rather than
merely its normalization.  Scalar operators are an explicit exception; the
resolvent identity alone does not assert nontrivial dependence.

For each shift, choose normalized deficiency vectors and define `F_+`, `F_-`
as in Section 4.  Away from the isolated zeros of the denominator, define the
meromorphic boundary phase function

```text
M_sigma(z)
  = - (z+i) F_+^(sigma)(z) / ((z-i) F_-^(sigma)(z)).   (7.3)
```

Equation (4.2) says

```text
z is an eigenvalue of D_(sigma,theta)
                              iff    exp(-i theta)=M_sigma(z).  (7.4)
```

Changing the phases of the two normalized deficiency vectors multiplies
`M_sigma` by a constant of modulus one.  Its dependence on `z`, modulo such a
constant, is therefore intrinsic.

### Theorem 7.1 (phase-labelled spectral covariance criterion)

The phase-labelled spectral divisors at shifts `sigma` and `mu` agree after a
constant relabeling `theta -> theta+delta` if and only if

```text
M_mu(z) = exp(-i delta) M_sigma(z)                     (7.5)
```

as meromorphic functions of `z`.  Equivalently,

```text
F_+^(mu)(z) F_-^(sigma)(z)
---------------------------------  = constant in z,    (7.6)
F_-^(mu)(z) F_+^(sigma)(z)
```

and the constant has modulus one after compatible normalization.

For the interval derivative there are no eigenvalues common to every
self-adjoint extension, so the phase selected by a regular real `z` is
unique.  Indeed, if a vector lies in a self-adjoint reducing summand of the
minimal symmetric operator, it is orthogonal to every defect vector `v_z`
with `Im z>0`: the self-adjoint restriction has no nonreal eigenvalue.
Riesz duality then makes its Fourier--Laplace transform vanish throughout an
open half-plane.  Analytic uniqueness forces the vector to be zero.  Thus the
minimal operator is simple and has no common self-adjoint summand.  Together
with the simple-zero argument in Section 4, the spectral divisors below are
unambiguous.

#### Proof

If (7.5) holds, then (7.4) immediately identifies the spectral divisor at
`theta` for `sigma` with that at `theta+delta` for `mu`.  Conversely, at every
regular real `z`, the one-dimensional boundary quotient of `v_z` is isotropic
and therefore selects a unique self-adjoint-extension phase; equivalently,
`M_sigma(z)` and `M_mu(z)` have modulus one.  Equality of the phase-labelled
spectral divisors for every `theta` therefore gives (7.5) on all regular real
points.  The identity theorem extends it meromorphically.  Cancelling the
common rational factors in (7.3) gives (7.6).  QED

This is a statement about spectral divisors, not unitary equivalence of the
operators in their two different energy metrics.  Operator equivalence would
require an additional intertwining map.

A normalization-free two-point form is particularly useful.  At regular
points `z,z_0`, set

```text
C_(sigma,mu)(z;z_0)
 = M_mu(z) M_sigma(z_0) / (M_sigma(z) M_mu(z_0)).       (7.7)
```

Then full phase covariance holds exactly when

```text
C_(sigma,mu)(z;z_0) = 1                                (7.8)
```

identically.  Thus two certified values that exclude equality already
falsify constant-phase covariance.

For a single selected phase rather than the full extension family, the exact
criterion is slightly weaker.  Characteristic functions
`W_(sigma,theta_sigma)` and `W_(mu,theta_mu)` have the same zero divisor if
and only if their quotient extends to a zero-free entire function whose
reciprocal is also entire.  Finite-window self-adjointness alone gives no
reason for this condition.

Failure of (7.5) would not disprove RH and would not exclude a specially tuned
pair `sigma(a),theta(a)` having a limit.  It would prove that the finite real
spectra are not independent of the auxiliary energy shift up to the natural
one-parameter phase ambiguity.  Any surviving limit proposal would then have
to specify and justify both choices.

## 8. Decisive pass/fail protocol

### Analytic checkpoint

The finite-window repair **passes** if the following can be established for
the exact completed form without assuming `sigma=0` or positivity of `q_a`:

1. the smooth space is a form core and embeds continuously in the logarithmic
   energy domain;
2. (5.1) holds on that core;
3. the dual adjoint formula (3.1) applies;
4. (5.2) and the boundary determinant (4.2) follow.

It **fails** as a foundation for the Suzuki route if any of these requires
global Weil positivity, or if the claimed energy space is not the form
completion on which the Riesz argument applies.  The existence of
`J^(-1)e^(+/-x)` is not an additional obstacle: it follows automatically from
strict coercivity, as shown in Corollary 3.3.

### Shift/phase checkpoint

After the analytic checkpoint passes, test (7.8) before studying large
support.  A lightweight Galerkin diagnostic can use the existing completed
Weil matrices:

1. choose two shifts safely below the computed smallest eigenvalue;
2. solve `(Q_a-sigma I)v=e_z` and `(Q_a-mu I)v=e_z` for the projected
   exponential vectors at several real `z`;
3. construct normalized deficiency vectors from `z=+i,-i`;
4. evaluate the cross-ratio (7.7) at high precision;
5. repeat under dimension and precision refinement.

This floating calculation is a diagnostic only.  Stable deviation from one
identifies the likely failure mechanism; a continuum falsification requires
an analytic argument or certified discretization error bounds.  Conversely,
values close to one do not prove covariance, especially near the collapsing
Weil margin where resolvent inversion is ill-conditioned.

The cleanest analytic version differentiates the resolvent:

```text
d R_sigma / d sigma = R_sigma^2.                       (8.1)
```

After cancelling the shift-dependent but `z`-independent deficiency-vector
normalizations, constant-phase covariance forces

```text
d/dsigma [log M_sigma(z)-log M_sigma(z_0)] = 0          (8.2)
```

for all regular `z,z_0`.  Finding one pair for which the derivative is nonzero
proves failure of full phase covariance without computing any eigenvalue.

## 9. Relation to the virial no-go and to RH

The regular virial argument failed because eigenstate commutators vanish and
compression moves every apparent sign into an omitted boundary channel.  The
energy-space derivative studied here retains that channel: its self-adjoint
extensions are defined by a nonlocal boundary form involving
`(A_a-sigma I)^(-1)exp(-izx)`.  It is therefore genuinely outside the local
transport and finite-commutator classes already pruned.

The repair also shows why self-adjointness is not enough.  It produces a circle
of real-zero characteristic functions for every support and every admissible
shift.  Arithmetic information can enter only through a canonical and
compatible choice of metric, phase, and limit.  Suzuki's stated target is a
quotient of the form `z^2 xi/xi'`, which is meromorphic.  Under the natural
requirement that any normalizing factors are entire and zero-free, ordinary
compact-local convergence of the resulting entire characteristic functions
on all of `C` cannot have that target across poles of `xi'`.  Without that
regularity requirement the normalization claim is underspecified; a rigorous
proposal must state its regularity and use pole-free compacta, spherical
convergence, or a reformulated entire determinant.  Direct convergence to
completed `xi` would be a distinct, stronger entire-target alternative.
Either identification would still require an RH-strength final argument;
none of Sections 2--8 proves it.

The first two checkpoints are now resolved:

1. the fixed-window adjoint theorem is repaired under the named analytic
   inputs in Sections 2--5;
2. equivalence of shifted norms does not supply full phase covariance, by the
   exact Dirichlet control in Section 8.

The live obligations are therefore:

3. construct either a zeta-specific intertwiner or an independently canonical
   tuned sequence `(sigma(a),theta(a))`;
4. prove the corresponding varying-window graph/resolvent limit while
   respecting the exact metric identity (6.1);
5. specify the meromorphic-target topology and prove the arithmetic
   determinant identification in that topology.

## 10. Primary sources and status boundaries

- M. Suzuki,
  [*Weil's quadratic form via the screw function*](https://arxiv.org/html/2606.09096v1),
  2026: localized Friedrichs operator, energy-space derivative, deficiency
  construction, and conditional limiting proposal.
- M. Suzuki,
  [*Aspects of the screw function corresponding to the Riemann zeta-function*](https://arxiv.org/abs/2206.03682),
  JLMS 2023: global screw-kernel positivity equivalents to RH.
- M. Suzuki,
  [*On the Hilbert space derived from the Weil distribution*](https://arxiv.org/html/2301.00421),
  2025/2026: de Branges identification under RH and unconditional auxiliary
  spaces.
- A. Connes, C. Consani, and H. Moscovici,
  [*Zeta Spectral Triples*](https://arxiv.org/html/2511.22755),
  2025: finite self-adjoint approximants and the still-open determinant limit
  to completed xi.
- J.-F. Burnol,
  [*The Explicit Formula and the conductor operator*](https://arxiv.org/abs/math/9902080),
  1999: local conductor and bounded commutator calculus.  It supplies important
  local spectral machinery but not the cross-place finite-window covariance
  isolated here.

The standard representation theorem for closed forms, the Riesz theorem,
distributional uniqueness for a first-order constant-coefficient ODE, and von
Neumann's deficiency-index theorem are used as consensus functional analysis.
They are not new claims of this project.
