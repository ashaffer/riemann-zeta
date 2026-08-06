# Suzuki defect escape and phase-independent resolvent checkpoint

## Verdict

The vector-compatibility branch closes, but it reveals a stronger positive
operator theorem.

1. Under the natural zero-extension embeddings, the normalized finite
   reference defect vectors do **not** converge to a nonzero global de Branges
   defect vector.  Their Riesz norms grow at least exponentially with the
   window, and the normalized vectors converge weakly to zero.  This is an
   exact analytic no-go theorem, not a Galerkin observation.
2. Assuming RH, compactly supported smooth functions form a graph core for
   the global Stone generator of translations.  Consequently every finite
   self-adjoint extension, with an arbitrary extension phase depending on the
   window, converges to that generator in generalized strong resolvent sense.
3. Hence the correctly formulated fixed-core weighted spectral measures do
   converge, independently of phase.  The moving reference-defect Clark
   measures are not among those fixed-vector measures.
4. This conditional strong-resolvent theorem cannot prove RH or convergence
   of raw eigenvalues, characteristic functions, or determinants.  The
   positive ambient Hilbert space used in the proof already comes from Weil
   positivity, and strong resolvent topology deliberately discards the
   escaping boundary vectors that carry the extension phase.

Thus Suzuki's proposed strong-resolvent limit is conditionally automatic and
too weak to be the missing RH mechanism.  The genuinely nontrivial limit is a
stronger boundary/determinant statement.

## 1. General nested-Riesz dichotomy

Let

```text
H_a subset H_b subset H_infinity
```

be isometrically nested Hilbert spaces with dense union.  Suppose one
algebraically consistent functional `ell` is bounded on every `H_a`, and let
`v_a` be its Riesz vector:

```text
<f,v_a>_(H_a) = ell(f),       f in H_a.
```

If `P_a` is the orthogonal projection from `H_b` onto `H_a`, uniqueness of
Riesz representatives gives

```text
P_a v_b = v_a.                                           (1.1)
```

Put `s_a=||v_a||^2=||ell|H_a||^2`.  Then `s_a` is
nondecreasing, and (1.1) gives the exact normalized geometry

```text
|<v_a/sqrt(s_a),v_b/sqrt(s_b)>| = sqrt(s_a/s_b),
projection mass                         = s_a/s_b,
projection tail                         = 1-s_a/s_b.       (1.2)
```

There are only two cases.

- If `sup_a s_a<infinity`, then `ell` extends boundedly to `H_infinity`.
  Its global Riesz vector `v_infinity` satisfies
  `v_a=P_a v_infinity`, so the normalized vectors converge strongly whenever
  `v_infinity` is nonzero.
- If `s_a->infinity`, then for every fixed old vector `f`,

  ```text
  <f,v_a/sqrt(s_a)> = ell(f)/sqrt(s_a) -> 0.
  ```

  Uniform boundedness and density of the old vectors imply
  `v_a/sqrt(s_a) -> 0` weakly.  Since their norms are one, no phases and no
  subsequence can make them converge strongly.

The scalar projection, coherence, tail, and amplified Riesz lower-bound
identities are Lean-checked in
[`RieszKernelEscape.lean`](../lean/rhbridge/RHBridge/RieszKernelEscape.lean)
and audited in
[`RieszKernelEscapeAudit.lean`](../lean/rhbridge/RHBridge/RieszKernelEscapeAudit.lean).
The Hilbert-space projection and density argument above is the analytic input,
not a hidden Lean axiom.

## 2. Application to Suzuki's reference defect vectors

Fix a common shift `sigma=-c<=0` for which the form

```text
||f||_c^2 = Q_W(f)+c||f||_2^2
```

is positive on the relevant nested union.  Under RH one may take `c=0`; one
may also take any fixed `c>0`.  Both terms are translation invariant.

The finite `-i` defect vector is the Riesz representative of ordinary Fourier
evaluation at `i`:

```text
ell_-(f) = integral_R f(x)e^(-x) dx = fhat(i),
(A_a+cI)v_(a,-) = e^(-x).                              (2.1)
```

Choose a fixed nonzero `phi in C_c^infinity(-r,r)` with `ell_-(phi) != 0`, and
write

```text
(tau_t phi)(x)=phi(x-t).
```

Then

```text
||tau_t phi||_c=||phi||_c,
ell_-(tau_t phi)=e^(-t)ell_-(phi).                    (2.2)
```

For `a>r`, choose `t=-a+r`, so the translate is supported inside `[-a,a]`.
The Riesz inequality gives

```text
s_a=||v_(a,-)||_c^2
  >= e^(2(a-r)) |ell_-(phi)|^2/||phi||_c^2.           (2.3)
```

Therefore `s_a->infinity` at least exponentially, and Section 1 yields

```text
v_(a,-)/||v_(a,-)||_c  -> 0 weakly.                  (2.4)
```

Right translation gives the same conclusion for the `+i` defect vector.
This proves three things at once:

- evaluation `f -> fhat(i)` is unbounded on the global translation-invariant
  completion;
- no global Riesz vector can project to all the finite reference vectors;
- the canonical normalized finite Clark vectors cannot converge strongly to
  a nonzero fixed ambient vector under zero extension.

The global de Branges kernel at `i` is instead a defect vector of
`mathsf D=U^(-1)MU`.  It represents evaluation after the nontrivial de Branges
transform `U`, not ordinary Fourier evaluation `fhat(i)` on the compact core.
This resolves the domain ambiguity in Suzuki's Section 7: these are different
global operators and different functionals.

## 3. The global compact core is essentially self-adjoint

Now assume RH and let `H_infinity` be the completion of
`C_c^infinity(R)` in the Weil norm.  Translations form a strongly continuous
unitary group `U_t`; let `Dbar` be its Stone generator.  Suzuki proves that

```text
Dbar[f]=[i f']                 for f in C_c^infinity(R). (3.1)
```

The missing strengthening is a standard group-mollification lemma.

### Core lemma

`C_c^infinity(R)` is a graph core for `Dbar`.

To prove it, choose `eta in C_c^infinity(R)` and define the Bochner integral

```text
x_eta = integral_R eta(t) U_t x dt.                  (3.2)
```

These are smooth vectors for the generator, with `Dbar x_eta` obtained by
differentiating `eta`.  If compact-core vectors `f_n` converge to `x` in the
Hilbert norm, then

```text
f_(n,eta) = integral_R eta(t)U_t f_n dt
```

is the ordinary convolution of two compactly supported smooth functions, so
it remains in `C_c^infinity(R)`.  Moreover,

```text
||f_(n,eta)-x_eta|| <= ||eta||_1 ||f_n-x||,
||Dbar f_(n,eta)-Dbar x_eta||
  <= ||eta'||_1 ||f_n-x||.                            (3.3)
```

Finally, an approximate identity `eta_epsilon` sends every
`x in Dom(Dbar)` to `x` in the graph norm.  Combining the two approximations
proves the lemma.

It follows that the closure of the compact-core differential operator is
already self-adjoint:

```text
closure(D_infinity)=Dbar=mathsf D_(pi/2).             (3.4)
```

This also answers Suzuki's explicit Section 7.4 question negatively.  The
closed de Branges minimal operator `mathsf D=U^(-1)MU` has deficiency indices
`(1,1)` and is a proper restriction of `Dbar`.  If every compact test lay in
`Dom(mathsf D)` with action `i f'`, closedness and the core lemma would force
`Dbar subset mathsf D`, contradicting those deficiency indices.  Thus some
compact-core vectors necessarily lie outside `Dom(mathsf D)`.

## 4. Phase-independent generalized strong resolvent convergence

The operator consequence is abstract.  Let `H_a` be increasing closed
subspaces with dense union in `H`, let `P_a` be their projections, and let
`B_a` be any self-adjoint operator on `H_a`.  Suppose a graph core `D` of a
self-adjoint `B` has the eventual exact-agreement property

```text
f in Dom(B_a),       B_a f=Bf                       (4.1)
```

for every fixed `f in D` and all sufficiently large `a`.

For `z` off the real line, define the generalized resolvent

```text
R_a(z)=J_a(B_a-z)^(-1)J_a*,                          (4.2)
```

where `J_a:H_a->H` is the inclusion and `J_a*=P_a`.  The set `(B-z)D` is
dense in `H`.  If `y=(B-z)f` belongs to it, (4.1) gives, eventually,

```text
R_a(z)y=f=(B-z)^(-1)y.                               (4.3)
```

Both sides of (4.2) are uniformly bounded by `1/|Im z|`; hence convergence on
the dense set extends to every `y in H`:

```text
R_a(z) -> (B-z)^(-1) strongly.                       (4.4)
```

For Suzuki under RH, `H_a` is the closure of
`C_c^infinity(-a,a)` in `H_infinity`, and every finite self-adjoint extension
contains that minimal domain.  Equations (3.1)--(3.4) supply the graph core.
Therefore

```text
J_a(D_(a,theta(a))-z)^(-1)J_a*
  -> (Dbar-z)^(-1) strongly                           (4.5)
```

for **every** phase function `theta(a)`.

The embedded finite operators are not densely defined on `H_infinity`, so
(4.5), not an unqualified ordinary-resolvent statement, is the canonical
formulation.  If desired, extend each finite operator by any self-adjoint
operator on `H_a^perp`; its complementary resolvent vanishes strongly because
`P_a->I`, giving ordinary strong resolvent convergence to the same `Dbar`.

A fixed common shift is load-bearing.  If the shifts vary with `a`, the
energy spaces are not isometrically nested, and this theorem does not apply
without new comparison maps.

## 5. The repaired weighted spectral-measure theorem

Let `h` be one fixed nonzero compact-core vector.  For all sufficiently large
windows it is literally the same vector in `H_a` and `H_infinity`.  Functional
calculus applied to (4.5) gives, for every `varphi in C_0(R)`,

```text
<h,varphi(D_(a,theta(a)))h>
  -> <h,varphi(Dbar)h>.                               (5.1)
```

Because the total mass is the same fixed `||h||^2`, the normalized scalar
spectral measures converge weakly.  Under the regular finite de Branges model,
their atoms are

```text
mu_a^h({lambda})
  = |hhat(lambda)|^2/K_a(lambda,lambda),              (5.2)
```

not the moving reference weights `rho_a(lambda)^2`.

For the unshifted RH target,

```text
mu_infinity^h
  = sum_gamma m_gamma |hhat(gamma)|^2 delta_gamma.    (5.3)
```

Thus (5.1) proves the topology-correct fixed-core weighted convergence,
conditionally on RH and independently of the finite extension phases.  It
does not force any individual finite eigenvalue to approach a zeta zero:
surplus eigenvectors can escape weakly while their total overlap with each
fixed core vector converges.

For a fixed shift `c>0`, the same argument targets the honest mixed measure

```text
mu_(infinity,c)^h
  = sum_gamma m_gamma |hhat(gamma)|^2 delta_gamma
      + (c/(2*pi)) |hhat(t)|^2 dt.                   (5.4)
```

This again confirms that the fixed-shift target is not the pure zeta-zero
operator.

## 6. A natural mixed Cauchy probe is not the finite defect limit

Under RH put

```text
S=(xi'/xi)(3/2),       C_c=S+c/2,
tau_c=sum_gamma m_gamma delta_gamma+c dt/(2*pi).
```

The fixed global vector

```text
g_c(t)=1/[sqrt(C_c)(t+i)]
```

is normalized in `L^2(tau_c)`.  Its probability measure and Stieltjes
transform are

```text
d nu_c(t)=d tau_c(t)/[C_c(1+t^2)],

m_c(z)
  = { i[(xi'/xi)(1/2-i z)+c/2]/C_c-z }/(1+z^2).     (6.1)
```

Here `Im z>0`; the lower-half-plane formula is obtained by reflection.

This is a legitimate fixed target probe.  Section 2 proves that it is not the
strong limit of the finite ordinary-Fourier evaluation kernels under natural
zero extension.  Choosing maps that send those escaping kernels to `g_c`
would require a new noncanonical comparison transform; maps that remain
asymptotically the identity on the dense compact core cannot do both.

## 7. Numerical corroboration and scope

[`suzuki_defect_escape_diagnostic.py`](../src/suzuki_defect_escape_diagnostic.py)
computes the finite-Galerkin shadow of `s_a` without locating any roots.  At
the certified fixed shift `sigma=-1/4`, dimensions 10 and 12 give

```text
L      s_L (m=10 / m=12)       base tail from L=1
1.000  1.6589 / 1.6591         0
1.750  3.4026 / 3.4031         about 0.512
2.485  5.6692 / 5.6986         about 0.708
2.996  7.6563 / 7.7362         0.7833 / 0.7855
```

Here `L=4a`.  At the D-rated continuation `L=8`, `s_L` is about `98`, and more
than `98.3%` of the normalized defect mass lies outside the projection of the
`L=1` space.  This agrees with the analytic escape theorem but is not used to
prove it.  The default run stayed below 44 MB resident memory.

The companion
[`test_suzuki_defect_escape_diagnostic.py`](../src/test_suzuki_defect_escape_diagnostic.py)
checks the exact projection formulas, an explicit nested-metric projection,
the exponential Riesz lower bound, and reflection symmetry.

## 8. What remains genuinely nontrivial

Generalized strong resolvent convergence and fixed-core weighted convergence
are now accounted for under RH.  They do not select the zeta divisor.  A
finite-to-infinite theorem with genuine RH content must retain the escaping
boundary information in a stronger topology, for example:

1. locally uniform convergence of a correctly normalized characteristic or
   Weyl function;
2. norm-resolvent convergence or convergence of compact spectral projections
   with multiplicity control;
3. a renormalized boundary-scattering limit for the exponentially growing
   unnormalized Riesz kernels;
4. the explicit entire-function limit in Suzuki's Corollary 1.6.

The third option is the closest surviving descendant of the Clark route: the
unit reference vectors escape, but their projective boundary ratio may retain
information after the exponential growth is factored out.  Any such claim
must be proved directly; it is not a consequence of strong resolvent
convergence.

## 9. Status and source boundary

- **F:** the scalar projection/coherence/tail identities and amplified Riesz
  bound in Lean.
- **A:** the nested-Riesz dichotomy, translation escape, group-mollifier core
  lemma, generalized-resolvent theorem, and fixed-vector functional-calculus
  corollary.
- **D:** the finite Legendre--Weil rows only.

Suzuki constructs the finite extensions, the RH-conditional global Weil
space, its translation group, the de Branges operator, and the natural
embeddings in Sections 6--7 of
[*Weil's quadratic form via the screw function*](https://arxiv.org/html/2606.09096v1).
The core, defect-escape, and phase-independence conclusions above are not
claimed there; they are the new deductions isolated by this checkpoint.
