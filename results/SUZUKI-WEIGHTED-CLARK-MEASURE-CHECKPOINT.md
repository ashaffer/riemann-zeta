# Suzuki weighted Clark-measure checkpoint

## Verdict

The weighted checkpoint does **not** presently establish convergence to the
zeta-zero operator.  It does, however, resolve the normalization and expose
two independent obstructions that the raw root count could not see.

1. The atom `2*pi/Phi'(lambda)` is a raw Clark-measure atom, not the
   spectral probability of an arbitrary fixed vector.  For the canonical
   normalized reference defect vector, the probability atom is instead

   ```text
   2/[(1+lambda^2)Phi'(lambda)] = rho(lambda)^2.       (0.1)
   ```

2. In the exact Hermite--Biehler countermodel from the preceding checkpoint,
   these normalized weights converge correctly for every nonexceptional
   Clark parameter.  At `alpha=-1`, which is the zeta parameter in the
   canonical Frostman gauge used below, however, the entire probability mass
   escapes to infinity.  Thus exponential type, symmetry, and Clark
   normalization do not imply the tightness needed here.
3. The completed-Weil Galerkin phasors give positive, nearly normalized
   candidate weights, but their projected root vectors are highly
   nonorthogonal and violate the Bessel bound.  They are therefore not a
   certified finite spectral measure.  A separate root-free comparison with
   the zeta Cauchy transform also fails at the first discriminating nonreal
   probes in the tested models.
4. More decisively, a fixed negative auxiliary shift has a different global
   target even assuming RH: it adds a nonzero Lebesgue absolutely continuous
   component to the translation spectrum.  Suzuki's pure zeta-zero target is
   the unshifted model.  Making admissible shifts tend to zero along cofinal
   windows is already equivalent, for the antitone window floors, to global
   Weil positivity.

There is also a topology gap before this can be called a necessary
strong-resolvent test: the finite normalized defect vectors move with the
window.  Strong resolvent convergence controls their scalar measures only
after the comparison maps are specified and those vectors are proved to
converge to a fixed ambient vector.  Suzuki's proposed embeddings do not yet
prove that compatibility.

**Follow-up.**  The gap is now closed negatively in
[`SUZUKI-DEFECT-ESCAPE-AND-RESOLVENT-CHECKPOINT.md`](SUZUKI-DEFECT-ESCAPE-AND-RESOLVENT-CHECKPOINT.md).
Translation invariance forces the finite reference Riesz norms to grow at
least exponentially, so the normalized vectors converge weakly to zero under
the natural embeddings.  The same follow-up proves that, once RH supplies the
positive ambient space, generalized strong-resolvent convergence and the
correct fixed-core weighted measures are phase-independent and automatic.

This checkpoint neither proves nor disproves RH.  It closes the generic
weighted-Clark shortcut and shows that the current fixed-shift approximants
cannot canonically have the unshifted pure-point zeta operator as their direct
global target.

## 1. Three measures that must not be conflated

Let `Theta_a` be the meromorphic-inner characteristic normalized by
`Theta_a(i)=0`, let `alpha` be an extension parameter, and write

```text
H_a(z) = (alpha+Theta_a(z))/(alpha-Theta_a(z)),
Theta_a(x) = exp(i Phi_a(x)).
```

With the upper-half-plane Herglotz convention

```text
Re H_a(z)
  = c_a Im z
      + (1/pi) integral_R Im z/|t-z|^2 d sigma_a(t),  (1.1)
```

a simple crossing `Theta_a(lambda)=alpha` has raw Clark mass

```text
sigma_a({lambda}) = 2*pi/Phi_a'(lambda).             (1.2)
```

For the normalized reference defect vector

```text
g_(a,-) = v_(a,-i)/sqrt(K_a(-i,-i)),
```

the intended regular, densely defined canonical-extension model has scalar
spectral measure

```text
nu_a(dx) = sigma_a(dx)/[pi(1+x^2)],

nu_a({lambda})
  = |K_a(lambda,-i)|^2
      /[K_a(-i,-i)K_a(lambda,lambda)]
  = rho_a(lambda)^2
  = 2/[(1+lambda^2)Phi_a'(lambda)].                  (1.3)
```

When `c_a=0`, this is a probability measure.  The same Clark normalization is
a subprobability measure on the real line when `c_a>0`, and `c_a` is the
Herglotz mass at infinity; in that case it should not be called the complete
spectral probability of an ordinary self-adjoint operator without first
specifying the corresponding relation/model.

A fixed core vector has yet another measure.  Under the de Branges energy
transform `f -> fhat`, the normalized eigenvector at `lambda` is
`K_a(.,lambda)/sqrt(K_a(lambda,lambda))`, so

```text
mu_(a,f)({lambda})
  = |fhat(lambda)|^2/K_a(lambda,lambda).              (1.4)
```

Equation (1.2) alone says nothing about (1.4).  Equation (1.3) applies only to
the named reference defect vector.

The scalar identities behind (1.2)--(1.3), including

```text
(phase-level density)*(reference atom)
  = 1/[pi(1+x^2)],                                   (1.5)
```

are checked in
[`ClarkSpectralWeight.lean`](../lean/rhbridge/RHBridge/ClarkSpectralWeight.lean)
and audited by
[`ClarkSpectralWeightAudit.lean`](../lean/rhbridge/RHBridge/ClarkSpectralWeightAudit.lean).
Equation (1.5) is an integrand identity; turning it into convergence still
requires a mesh and tightness theorem.

## 2. A root-free convergence criterion

The Stieltjes transform of (1.3) can be read directly from the inner
function, without locating roots or differentiating their phase:

```text
m_a(z)
  = integral_R d nu_a(t)/(t-z)
  = [i H_a(z)-z]/(1+z^2),       Im z>0.              (2.1)
```

The singularities at `z=+/-i` are removable.  Formula (2.1) remains valid
when (1.1) has a linear term; in that case `nu_a(R)=1-c_a`.

Consequently, local uniform convergence of `m_a` on the upper half-plane,
together with preservation of total mass, is the clean root-free formulation
of weak probability-measure convergence.  It is only a conditional operator
test here.  If comparison isometries `J_a` satisfy

```text
J_a g_(a,-) -> g_(infinity,-)
```

and the embedded resolvents converge strongly, then the associated scalar
measures converge.  Neither strong resolvent convergence by itself nor a
moving sequence of unrelated Clark vectors implies this conclusion.

### The exact zeta target

Put

```text
A(z) = xi(1/2-i z),
Theta_xi(z) = [A(z)-i A'(z)]/[A(z)+i A'(z)],
S = (xi'/xi)(3/2) = 0.046135928060462575...,
q = (1-S)/(1+S),
theta_infinity = (Theta_xi-q)/(1-q Theta_xi).
```

Then `theta_infinity(i)=0`.  At every zeta zero on the critical line,
`theta_infinity(gamma)=-1`, so the selected Clark parameter in this gauge is
`alpha=-1`.  A further unimodular Livsic gauge would relabel the parameter.
Assuming RH, with ordinates repeated by multiplicity,

```text
sigma_infinity
  = (pi/S) sum_gamma m_gamma delta_gamma,

nu_infinity
  = (1/S) sum_gamma
      [m_gamma/(1+gamma^2)] delta_gamma,              (2.2)

H_infinity(z)
  = (1/S) (xi'/xi)(1/2-i z),

m_infinity(z)
  = { (i/S)(xi'/xi)(1/2-i z)-z }/(1+z^2).            (2.3)
```

The meromorphic identity (2.3) is unconditional away from poles; its
interpretation as the transform of the positive real measure (2.2) is
conditional on RH.  Under RH,

```text
S = sum_gamma m_gamma/(1+gamma^2),
```

so `nu_infinity` has total mass one.  The first symmetric zero pair alone has
mass

```text
2/[S(1+gamma_1^2)] = 0.215897528605125... .          (2.4)
```

This is why compact mass must be compared with the target compact mass, not
with one.

## 3. The generic countermodel: convergence except at the relevant phase

For the exact-type Hermite--Biehler family constructed in
[`SUZUKI-COMPACT-PHASE-MASS-FAIL-FAST.md`](SUZUKI-COMPACT-PHASE-MASS-FAIL-FAST.md),
let `alpha=exp(i theta)`.

For every fixed `-pi<theta<pi`, with `t=tan(theta/2)`, there is one compact
atom and

```text
nu_(a,theta) => delta_t,

nu_(a,theta)({lambda_(a,0)})
  = 1 - 2 sec(theta/2)^2/(pi*a) + o(1/a).            (3.1)
```

Thus all surplus roots have total normalized mass
`2 sec(theta/2)^2/(pi*a)+o(1/a)`.  Weighted convergence survives even though
the eventual raw root density grows like `a`.

The asymptotics come from an explicit positive phase remainder.  If
`Phi_a(x)=2 arctan(x)+D_a(x)`, then

```text
D_a'(x)
  = sum_(n>N_a) {
      2/[(x-u_(a,n))^2+1]
        + 2/[(x+u_(a,n))^2+1] },

a D_a'(x) -> 4/pi,
a D_a(x)  -> 4x/pi                              (3.2)
```

locally uniformly for fixed `x`.  This follows from
`sum_(n>N_a)u_(a,n)^(-2)~1/(pi*a)`.  The implicit phase equation then gives

```text
lambda_(a,0)
  = t - 2t(1+t^2)/(pi*a) + o(1/a),
```

and substitution into (1.3) gives (3.1).  The fixed-`a` Blaschke/Herglotz model
has no linear mass at infinity, so the remaining probability mass is the
stated leakage.

The parameter `theta=pi`, equivalently `alpha=-1`, is exceptional.  The two
nearest roots obey

```text
lambda_a^+/- = +/-sqrt(pi*a/2)(1+o(1)),
nu_(a,pi)({lambda_a^+/-}) -> 1/2.                    (3.3)
```

Hence `nu_(a,pi)` is not tight on the real line.  It converges vaguely to zero
there and to a unit atom at infinity on the one-point compactification.  The
limiting Herglotz function is the pure linear term `-i z`.

Indeed, on the scale `x=O(sqrt(a))`, the phase equation is

```text
pi - 2/x + 4x/(pi*a) + o(a^(-1/2)) = pi.
```

It yields `x^2~pi*a/2`; inserting this into (1.3) yields mass `1/2` for each
sign.  This also explains why vague convergence on the real line loses all
mass even though every finite measure is normalized.

This is not a counterexample to Suzuki's zeta-specific claim.  It proves the
precise generic limitation: all the type, symmetry, normalization, and
fixed-window Weyl data used so far still allow complete mass escape at the
actual zeta Clark parameter.

## 4. A fixed negative shift has the wrong pure-point target

There is a stronger target mismatch independent of Section 3.  Under RH, the
global zero-frame representation gives, with the repository Fourier
normalization,

```text
Q_W(f) = sum_gamma m_gamma |fhat(gamma)|^2,
||f||_2^2 = (1/(2*pi)) integral_R |fhat(t)|^2 dt.
```

For a fixed `sigma=-c<0`, the shifted norm is therefore

```text
Q_W(f)-sigma||f||_2^2
  = sum_gamma m_gamma |fhat(gamma)|^2
      + (c/(2*pi)) integral_R |fhat(t)|^2 dt.         (4.1)
```

The canonical global multiplication measure is

```text
tau_c = sum_gamma m_gamma delta_gamma + c dt/(2*pi). (4.2)
```

Every nonzero core vector has a nonzero absolutely continuous contribution.
Thus fixed-shift finite-window operators may legitimately converge to a
mixed-spectrum global operator, but not canonically to Suzuki's unshifted
pure zeta-zero operator.  This conclusion holds even after granting RH; it is
a target-identification obstruction, not evidence against RH.

The scalar fact that the shift adds exactly `c||f||_2^2`, and that this mass
vanishes for a nonzero vector only at `c=0`, is Lean-checked in the module
linked in Section 1.  Identifying its density as (4.2) uses Plancherel and the
global zero-frame representation.

Could one choose `sigma_a -> 0`?  For an antitone cofinal family of
finite-window spectral floors, the repository already proves

```text
there are strictly admissible sigma_a -> 0
  iff every finite-window floor is nonnegative.       (4.3)
```

See
[`CofinalShiftPositivity.lean`](../lean/rhbridge/RHBridge/CofinalShiftPositivity.lean).
For the zeta Weil form, the right side is the all-window positivity criterion
equivalent to RH.  Consequently a vanishing admissible shift is not an
independent shortcut to the unshifted global space.

An explicit noncanonical quotient or comparison map might remove the
Lebesgue component, but it must be constructed and shown to intertwine the
operators.  The canonical zero-extension/direct-limit construction does not
do so.

## 5. Finite diagnostics and their boundary

Two deliberately separate diagnostics were run.

### Phase-derived candidate weights

[`suzuki_weighted_clark_measure_diagnostic.py`](../src/suzuki_weighted_clark_measure_diagnostic.py)
computes

```text
p_phase(lambda)=2/[(1+lambda^2)Phi'(lambda)]
```

at sampled phase roots on `[-96,96]`.  Across the tested certified supports,
both symmetry phases, and dimensions 10 and 12, the derivatives were positive
and the captured candidate mass was approximately `0.960--0.999`.  The
dimension-10 and dimension-12 Cauchy transforms were close.  This is evidence
for the algebraic density/weight cancellation, but only after an exact
meromorphic-inner identification would these be spectral probabilities.

```text
L      roots   candidate mass   overlap-square sum   max root coherence
1.000  15--16  0.960072--0.998959  1.00163--1.18468  0.945608--0.981626
1.750  26--27  0.974347--0.998299  1.02294--1.44253  0.994006--0.997995
2.485  37--38  0.982483--0.997466  1.06368--1.63629  0.998042--0.999340
2.996  45--46  0.983686--0.997384  1.07301--1.58752  0.999090--0.999708
```

Each range is over dimensions 10 and 12 and phases `0` and `pi`; every sampled
phase derivative was positive.

The same script independently constructs the projected Galerkin defect
vectors.  Distinct root vectors have maximum normalized coherence
`0.9456--0.9999`, and the sums of their reference-overlap squares violate the
Bessel bound, reaching `1.64` on `L<=2.996`.  Therefore those overlaps are
exact finite-dimensional quantities but **not** the atoms of an orthogonal
extension eigenbasis.  The projection is not a structure-preserving finite
functional model.

### Root-free target comparison

[`suzuki_weighted_clark_target_diagnostic.py`](../src/suzuki_weighted_clark_target_diagnostic.py)
applies (2.1) to the one-scalar calibrated Livsic models.  Errors are tiny at
the weak imaginary-axis probes near the normalization point, roughly
`2e-7--8e-5` at `i/4` and `2i`.  At the first discriminating zeta-scale probes
they remain much larger and nonmonotone:

```text
L      error at 14+0.5i   error at 14+2i
1.750  0.188019--0.188467  0.046562--0.047112
2.485  0.183896--0.208892  0.035136--0.058953
2.996  0.201367--0.242542  0.051744--0.066890
```

This fails the current finite calibrated model at its first useful weighted
Cauchy checkpoint.  It does not disprove convergence at larger support: the
models are moving near-floor calibrations, are not certified graph
approximants, and do not come with convergent ambient comparison vectors.

The tests in
[`test_suzuki_weighted_clark_measure_diagnostic.py`](../src/test_suzuki_weighted_clark_measure_diagnostic.py)
check the analytic phase derivative, the two weight normalizations, the
Bessel/orthogonality guardrail, the Cauchy transform, the exact xi
logarithmic-derivative transform, and (2.4).

The certified phase run, root-free target run, and seven-test suite used one
BLAS thread.  Their observed peak resident memory was below 48 MB; the two
main runs took about 22 seconds each on the checkpoint machine.  Reproduction
commands are recorded in
[`lean/README-verify.md`](../lean/README-verify.md).

## 6. What survives

The original proposed implication

```text
strong resolvent convergence
  => convergence of the finite Clark reference measures
```

is not available for the canonical reference vectors.  The follow-up proves
more: under natural zero extension those unit vectors weakly escape, so no
vector-compatibility theorem of the proposed kind can hold.  The correct
strong-resolvent probes are fixed compact-core vectors, whose finite atoms are
`|hhat(lambda)|^2/K_a(lambda,lambda)`.  Assuming RH, their measures converge
automatically for every extension phase by the graph-core generalized-
resolvent theorem.

For the unshifted pure zeta target, Step 3 forces `sigma=0`, whose global
admissibility is already the RH-strength positivity statement.  For a fixed
negative shift, the honest target is the mixed measure (4.2).  Those are the
two mathematically coherent branches; comparing a fixed-negative-shift model
directly with (2.2) mixes them.

What remains nontrivial is therefore stronger than fixed-vector spectral
measure convergence: a locally uniform characteristic/determinant limit,
norm-resolvent control, or a renormalized boundary-scattering limit that
retains the exponentially escaping Riesz kernels.

## 7. Status and primary source

- **F:** the scalar Clark/reference normalization, density cancellation, and
  fixed-shift mass identities in Lean.
- **A:** the Herglotz/Stieltjes conversion, zeta normalization, explicit
  Hermite--Biehler asymptotics, and the Plancherel/zero-frame target
  identification, conditional on RH where stated.
- **D:** all completed-Weil finite Galerkin rows.

Suzuki's finite characteristic, global zero-frame representation under RH,
and proposed varying-window operator limit are in M. Suzuki,
[*Weil's quadratic form via the screw function*](https://arxiv.org/abs/2606.09096v1),
especially Theorem 1.5 and Sections 6--8.  The preprint proposes embeddings
and strong-resolvent convergence but does not prove the comparison-vector
compatibility or the fixed-shift global identification required above.
