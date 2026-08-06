# Suzuki spectral-counting checkpoint

## Verdict

The proposed immediate Weyl obstruction does **not** close the Suzuki route.
What can be proved at present is sharper in logic but weaker in consequence:

1. after the fixed-window adjoint construction is repaired by closure and
   form duality, its extension eigenvalues are counted exactly by the winding
   of one monotone boundary phase;
2. every fixed-window characteristic has only linear high-energy zero density;
3. neither statement controls the opposite limit in which the support grows
   while the spectral compact is fixed;
4. finite completed-Weil Galerkin models strongly exhibit geometric winding
   proportional to the support, but this remains a diagnostic rather than a
   continuum, support-uniform theorem.

Thus the genuine fork is now explicit.  For fixed `T`, determine whether the
phase mass

```text
turns_L([0,T]) = (Phi_L(T)-Phi_L(0))/(2*pi)
```

stays bounded as `L -> infinity` or grows like `L*T/(4*pi)`.  The first
behavior is compatible with a zeta-like compact limit.  The second would
exclude compact-local divisor convergence to any target with finitely many
zeros in `[0,T]`.

Nothing in this note proves or disproves RH.

**Follow-up.**  The generic side of the phase-mass fork is now resolved in
[`SUZUKI-COMPACT-PHASE-MASS-FAIL-FAST.md`](SUZUKI-COMPACT-PHASE-MASS-FAIL-FAST.md):
an exact type-`a` Hermite--Biehler family can have the full fixed-window Weyl
density while its fixed-compact phase remains bounded.  The surviving theorem
is a zeta-specific decay estimate for normalized defect-line coherence, not a
consequence of type or symmetry.

## 1. Conventions and repaired fixed-window object

The repository's support parameter is `L`, while Suzuki's interval is
`[-a,a]` with

```text
a = L/4.
```

For an auxiliary shift `sigma < inf spec(A_a)`, write

```text
T_(a,sigma) = A_a - sigma I,
v_+ = T_(a,sigma)^(-1) exp(x),
v_- = T_(a,sigma)^(-1) exp(-x).
```

The repaired construction in `SUZUKI-ENERGY-ADJOINT-REPAIR.md` closes the
minimal energy-space derivative before applying von Neumann theory.  Its
characteristic is, up to harmless convention changes,

```text
W_(a,sigma,theta)(z)
  = (z-i) I_+(z) + exp(i theta) (z+i) I_-(z),
I_+/- (z) = integral_[-a,a] v_+/-(x) exp(i z x) dx.
```

Suzuki's v1 preprint states this characteristic and its real-eigenvalue
interpretation, but it does not prove a finite-`a` phase theorem, interlacing,
compact resolvent, or a Weyl law.  Its displayed adjoint argument also uses
the energy-to-`L2` continuity implication in the wrong direction.  The
form-dual/Riesz repair is therefore a real prerequisite, not a cosmetic
rewrite.

The exact phase theorem uses four repaired inputs: the minimal derivative is
closed, densely defined, and symmetric; every defect space is the line
spanned by the entire vector map `v_z=T^(-1)exp(-iz x)`; the Green identity
and von Neumann domains hold for the closure; and the displayed
characteristic is the resulting boundary determinant.  Fourier uniqueness
then makes the minimal operator simple.  To identify these point eigenvalues
with the *entire* spectrum of every extension, one additionally needs the
standard regularity/meromorphic-resolvent hypothesis from the
Krein--de Branges model.  The phase count below is exact for the characteristic
zeros and hence for the extension point spectrum even before that final
exhaustion statement.

## 2. Exact boundary phase

Every object in this section depends on both `a` and `sigma`; the shorter
notation suppresses them only for readability.  Define on the real line

```text
E_(a,sigma)(x)
  = - (x-i) I_+(x) / ((x+i) I_-(x)).                 (2.1)
```

Reflection and reality give

```text
(x+i) I_-(x) = conjugate((x-i) I_+(x)).             (2.2)
```

The numerator and denominator cannot vanish together at a real point: that
would put the same nonzero defect vector in every self-adjoint extension.
Simplicity of the minimal derivative excludes such a common summand.  Hence
`E_(a,sigma)(x)` is a continuous unit phasor on all of `R`.  Since `R` is
simply connected, it has a continuous lift

```text
E_(a,sigma)(x) = exp(i Phi_(a,sigma)(x)).            (2.3)
```

With canonical reflection normalization, `E(-x)=E(x)^(-1)` and the lift can
be chosen odd with `Phi(0)=0`.

### 2.1 Strict monotonicity

Normalize unit deficiency vectors `d_+`, `d_-` so that the von Neumann
boundary form is

```text
B(u,v) = 2 i (c_+(u) conjugate(c_+(v))
                  - c_-(u) conjugate(c_-(v))).       (2.4)
```

For the real defect vector `v_x`, isotropy gives

```text
c_-(v_x) = exp(i Phi(x)) c_+(v_x).                   (2.5)
```

On the other hand,

```text
B(v_x,v_y) = (x-y) <v_x,v_y>_T.                     (2.6)
```

Insert (2.5) into (2.4), divide (2.6) by `x-y`, and let `y -> x`.
With the displayed orientation,

```text
Phi'(x) = ||v_x||_T^2 / (2 |c_+(v_x)|^2) > 0.       (2.7)
```

The coefficient `c_+(v_x)` is nonzero: otherwise isotropy also makes
`c_-(v_x)=0`, putting `v_x` in the minimal domain, where the distributional
first-order eigen-equation has only the zero solution.  Reversing the phase
convention reverses the sign of `Phi`, not the strict monotonicity statement.

This derivation is standard simple-symmetric-operator theory.  It is not a
theorem printed in Suzuki v1.

There is also a normalization-free inner-function proof.  The repaired ratio
is a nonconstant meromorphic inner/Livšic function on the upper half-plane.
Its numerator contains `z-i`, while

```text
I_-(i) = <T^(-1) exp(-x), exp(-x)>_2 > 0,
```

so `E(i)=0`.  The canonical factorization therefore gives

```text
Phi'(x)
  = tau + sum_(zeta in Z(E) cap C_+)
      2 Im(zeta)/|x-zeta|^2
  >= 2/(1+x^2),                    tau >= 0.          (2.8)
```

This independently proves strict monotonicity.  The lower bound is uniform
in `a` but integrates to only a bounded amount on a fixed compact; it does
not provide the support-growing phase mass needed below.

### 2.2 Exact count

For the extension labelled by `theta`,

```text
x is an eigenvalue  iff  Phi(x) = theta + 2*pi*k
                           for some k in Z.           (2.9)
```

Consequently, for `u < v`,

```text
N_(a,sigma,theta)((u,v])
  = #{k in Z : Phi(u) < theta+2*pi*k <= Phi(v)}
  = floor((Phi(v)-theta)/(2*pi))
      - floor((Phi(u)-theta)/(2*pi)).                 (2.10)
```

In particular,

```text
|N((u,v]) - (Phi(v)-Phi(u))/(2*pi)| < 1.             (2.11)
```

Different extension phases therefore change an interval count only through
the endpoint floors.  The load-bearing analytic quantity is the phase
increment, not the optimized phase label.

Equations (2.10)--(2.11), including the exact integer-interval membership
statement, are formalized without project axioms in
`RHBridge/BoundaryPhaseCounting.lean`.

## 3. What fixed-window entire-function theory gives

Because `v_+/-` lie in `L2[-a,a]`, they lie in `L1[-a,a]`, and

```text
|W_(a,sigma,theta)(z)|
  <= C_(a,sigma,theta) (1+|z|) exp(a |Im z|).        (3.1)
```

Thus `W` is a Cartwright-class entire function of exponential type at most
`a`.  Cartwright--Levinson zero counting gives, for fixed `a`,

```text
n_(a,sigma,theta)(R) = (d_(a,sigma)/pi) R + o_(a,sigma,theta)(R),
0 <= d_(a,sigma) <= 2*a,                             (3.2)
```

where `d` is the width of the indicator diagram.  Interlacing makes the width
independent of `theta`.  More concretely, after zero extension,

```text
W = Fourier(omega_theta),
omega_theta = i[(partial_x-1)v_+
             + exp(i theta)(partial_x+1)v_-].        (3.3)
```

Paley--Wiener--Schwartz identifies `d` with the convex-support width of this
distribution.  The full coefficient `d=2a` therefore needs a theorem that
`omega_theta` reaches both endpoints.  Neither Suzuki v1 nor the present repair
proves that endpoint-support/unique-continuation statement; exponential type
at most `a` alone is insufficient.

In repository normalization, the corresponding full-type prediction is

```text
N_L([0,R]) = (L/(4*pi)) R + o_L(R).                  (3.4)
```

This is a high-energy statement with `L` fixed.  Its remainder and the onset
of its asymptotic regime may depend arbitrarily badly on `L`.

## 4. Why the ordinary Weyl law is not the decisive obstruction

The positive zeta-zero count obeys the Riemann--von Mangoldt asymptotic

```text
N_zeta(R)
  = R/(2*pi) * log(R/(2*pi)) - R/(2*pi) + O(log R).  (4.1)
```

Therefore no one fixed finite window can reproduce the zeta divisor all the
way to infinite height: (3.4) is linear while (4.1) is `R log R`.  Suzuki's
proposal, however, sends the support to infinity.  Matching the two displayed
leading *counts* predicts

```text
L approximately 2 * (log(R/(2*pi)) - 1),             (4.2)
R approximately 2*pi * exp(L/2 + 1).                 (4.3)
```

So a fixed-`L` linear tail may begin only after an exponentially large
crossover, while every fixed compact lies in a different, potentially
zeta-like regime as `L` grows.  There is no contradiction between the two
orders of limits.

The elementary escaping spectrum

```text
lambda_(a,n) = a^2 + n/a,       n = 0,1,2,...        (4.4)
```

makes the quantifier failure explicit.  Its gap is exactly `1/a`, so its
high-energy density becomes arbitrarily large; nevertheless every fixed
compact is eventually empty because its spectral onset is `a^2`.  The gap,
block-spacing, and compact-escape statements are formalized in
`RHBridge/BoundaryPhaseCounting.lean`.

Accordingly, a theorem of the form

```text
N_L(R) = (L/(4*pi)) R + O_L(1),       R -> infinity  (4.5)
```

does not answer the required question.  One needs an error/onset estimate
uniform in `L` in a specified joint range.

## 5. Bounded-memory Galerkin checkpoint

The completed-Weil Legendre model was evaluated sequentially at the certified
fixed shift `sigma=-1/4`.  The spectral endpoint was

```text
T = gamma_12 + 40 = 96.446247697063...
```

and each boundary phasor used 12,001 real samples.  Here `L<=749/250` is the
range on which the repository's independent full-space certificates make the
shift continuum-safe; all root and phase values remain finite-Galerkin
diagnostics.

| `L` | dimension | `N_(theta=0)` | `N_(theta=pi)` | phase turns | `L*T/(4*pi)` |
|---:|---:|---:|---:|---:|---:|
| 1.750 | 8  | 14 | 13 | 13.4555 | 13.4312 |
| 1.750 | 10 | 14 | 13 | 13.4411 | 13.4312 |
| 1.750 | 12 | 14 | 13 | 13.4433 | 13.4312 |
| 2.485 | 8  | 20 | 19 | 19.1472 | 19.0722 |
| 2.485 | 10 | 19 | 19 | 18.8028 | 19.0722 |
| 2.485 | 12 | 19 | 19 | 18.9496 | 19.0722 |
| 2.996 | 8  | 23 | 23 | 22.8781 | 22.9941 |
| 2.996 | 10 | 23 | 23 | 22.9134 | 22.9941 |
| 2.996 | 12 | 23 | 23 | 22.7835 | 22.9941 |

The winding differs from the geometric prediction by at most `0.270` turns.
Changing the extension phase changes the count by at most one, exactly as the
floor formula predicts.  This says the previous selected-divisor mismatch is
substantially an index-density issue, not merely a bad phase optimization.
The exact printed rows are archived in `suzuki-phase-winding.csv` and are
reproduced by `src/suzuki_phase_winding_diagnostic.py`.

It is evidence for

```text
Phi_L(T)-Phi_L(0) approximately (L/2) T             (5.1)
```

over the tested range.  It is not evidence that the error in (5.1) stays
bounded for arbitrary support, and fixed dimensions are not a convergent
discretization theorem for the unbounded extensions.

## 6. Convergence topology matters

If suitably normalized characteristics converge locally uniformly to a
nonzero holomorphic target on a neighborhood of a compact whose boundary is
zero-free, Rouche's theorem makes the enclosed zero count eventually
constant.  A support-uniform lower bound forcing

```text
N_L([0,T]) -> infinity
```

would therefore refute that compact-local characteristic/divisor limit.

It would not, by itself, refute strong-resolvent convergence.  Under strong
resolvent convergence, additional eigenvectors can escape weakly and spectral
counts need not stabilize.  Norm-resolvent convergence or convergence of the
relevant finite-rank spectral projections would be strong enough.  Suzuki's
varying-space strong-resolvent expectation also needs explicit comparison
maps and densely defined embedded operators before it becomes a standard
operator-convergence statement.

The proposed target `z^2 xi/xi'` introduces a separate topology issue because
it is meromorphic in general.  Any determinant convergence claim must specify
pole-free compacta, spherical convergence, removability, or a reformulated
entire target before Rouche counting can be invoked.

The raw Clark measure must be distinguished from a fixed-vector spectral
measure.  With the Herglotz convention

```text
Re [(alpha+E(z))/(alpha-E(z))]
  = c_alpha Im z
      + (1/pi) integral_R Im z/|x-z|^2 d sigma_alpha(x),
```

a crossing `E(lambda)=alpha` has raw Clark mass

```text
sigma_alpha({lambda}) = 2*pi/Phi'(lambda).           (6.1)
```

This is not, by itself, the spectral probability of a fixed normalized
vector.  For the canonical normalized reference defect vector at `i`,

```text
nu_alpha(dx) = sigma_alpha(dx)/[pi(1+x^2)],
nu_alpha({lambda})
  = 2/[(1+lambda^2)Phi'(lambda)]
  = rho(lambda)^2.                                   (6.2)
```

When the Herglotz linear term vanishes, `nu_alpha` is a probability measure;
otherwise the missing Clark mass lies at infinity.  A different comparison
vector contributes its own squared boundary-transform factor.  Thus a
strong-resolvent obstruction must control the total fixed-vector measure on
compact sets, not merely root counts or individual raw Clark atoms.  The
full normalization and its operator-theoretic boundary are developed in
[`SUZUKI-WEIGHTED-CLARK-MEASURE-CHECKPOINT.md`](SUZUKI-WEIGHTED-CLARK-MEASURE-CHECKPOINT.md).

## 7. The next theorem

For each certified fixed shift and each fixed `T`, estimate

```text
Delta_L(T) = Phi_L(T)-Phi_L(0)
           = integral_0^T
               2 dx / [(1+x^2) rho_L(x)^2],                 (7.1)

rho_L(x)^2
  = |K_L(x,-i)|^2/[K_L(-i,-i)K_L(x,x)].
```

There are now two clean outcomes.

### Crowding outcome

Prove, for some fixed `T>0`,

```text
Delta_L(T) >= c*T*L - C_T,       c>0,               (7.2)
```

uniformly along an admissible cofinal support sequence.  Then the exact floor
count diverges, excluding compact-local divisor convergence to the zeta
target on that compact.

### Escaping-onset outcome

Prove instead that `Delta_L(T)=O_T(1)` for every fixed `T`, and locate a
transition to the fixed-window linear tail near the exponential scale (4.3).
That would pass the counting gate and produce the first rigorous mechanism by
which the finite spectra can have both a zeta-like compact regime and a
geometric far tail.

The correct object for either proof is the normalized defect-kernel ratio in
(7.1).  Exponential type alone cannot decide it.  If raw phase mass grows,
the next target is the normalized spectral measure of a specified comparison
vector.  Individual raw Clark atoms do not determine this measure, and their
vanishing does not by itself establish convergence of its total compact mass.

Finally, a cofinal unconditional family must control the suppressed shift.
Suzuki states shift-independence only as an expectation.  Either one fixed
`sigma` must remain below every window floor, or a quantitatively controlled
`sigma(a)` must be carried through the phase estimates.  The repository's
fixed `-1/4` certificate currently stops at `L=749/250`; using `sigma=0`
globally would already assume the positivity target.

## 8. Primary sources and status boundary

- M. Suzuki, [*Weil's quadratic form via the screw function*](https://arxiv.org/abs/2606.09096v1),
  especially Theorem 1.5 and Sections 6--8: the finite characteristic and the
  conjectural varying-window limit.
- R. T. W. Martin,
  [*Representation of simple symmetric operators with deficiency indices
  (1,1) in de Branges space*](https://arxiv.org/abs/0909.2220), especially the
  regular simple-symmetric/de Branges representation and spectral function.
- L. O. Silva and J. H. Toloza,
  [*De Branges spaces and Krein's theory of entire operators*](https://arxiv.org/abs/1309.1991),
  especially the regular simple-symmetric functional model and interlacing
  extension spectra.

The phase derivation, Cartwright consequence, and quantifier audit in this
note are deductions from the repaired operator setup plus standard consensus
operator and entire-function theory.  They are not attributed to Suzuki v1.
