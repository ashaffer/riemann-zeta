# Farey virial audit and prime-5 control theorem

Status: completed fail-fast pass, 2026-08-04.  Both the naive Farey virial
route and its canonical nonlocal Knapp--Stein continuation are pruned.  The
prime-5 control experiment has a kernel-checked finite-dimensional Lean
theorem.  No RH claim is made.

## 1. Outcome

The two experiments gave complementary answers.

1. The Farey transfer operator is an exact carrier of zeta zeros, but a zeta
   zero is represented by a singular cusp/scattering state, not by an ordinary
   vector in the natural Hilbert space.  The honest adjoint calculation has a
   nonzero forcing term and the wrong parameter involution for RH.  Thus an
   identity of the form

   `(4 Re(q)-1) E_q = 0`, with `E_q>0`,

   cannot be obtained from the natural Hilbert adjoint by discarding a boundary
   term.  The discarded term is where the zeta information lives.

2. The canonical principal-series intertwiner does not rescue the Farey route.
   It implements `q -> 1-q`, while the RH reflection for `zeta(2q)` is
   `q -> 1/2-conj(q)`.  The Casimir eigenvalues rule out an equivariant map
   with the latter parameters.  After automorphization, the scalar relating
   the two cusp channels is exactly the modular scattering quotient
   `Lambda(2q-1)/Lambda(2q)`.  Thus the proposed nonlocal normalization either
   has the wrong symmetry or imports the zeta pole problem it was meant to
   solve.

3. At `L=327/100`, in the 12-dimensional Legendre Ritz space, interval
   arithmetic certifies that the old `{2,3}` form has a negative test vector,
   that the prime-5 event repairs that vector, and that the completed active
   matrix is positive definite.  A generated Lean certificate proves a robust
   version for every real matrix in the stated entrywise intervals.  This is a
   genuine finite prime-event rescue, but the block coupling approaches the
   critical value one as the Ritz space is refined.

The Farey branch is therefore closed unless a genuinely new, non-equivariant
arithmetic order structure is found.  Calling another normalization an
"intertwiner" does not make it independent if its boundary scalar is already
the zeta scattering quotient.

## 2. The exact Farey dictionary

Let `q=xi+i eta`, with `xi>0`, and define

`(P_(0,q) f)(x)=(1+x)^(-2q) f(x/(1+x))`,

`(P_(1,q) f)(x)=(1+x)^(-2q) f(1/(1+x))`,

`P_q^+=P_(0,q)+P_(1,q)`, and `P_q^-=P_(0,q)-P_(1,q)`.

Bonanno's classification writes an analytic fixed function as

`f(z)=c z^(-2q)+B_q[b t^(-1)+phi](z)`,

where

`phi in H_xi=L2((0,infinity),t^(2xi-1)e^(-t)dt)`.

The three boundary classes must not be conflated:

| boundary data | fixed equation | arithmetic meaning |
|---|---|---|
| `c=b=0` | `P_q^+ f=f` | even Maass form |
| `c=b=0` | `P_q^- f=f` | odd Maass form |
| `c=0`, `b!=0` | `P_q^+ f=f` | `zeta(2q)=0`, or `q=1` |

Thus the statement "eigenvalue one iff a zeta zero" is correct only after the
singular boundary class has been specified.  More precisely, an analytically
continued Eisenstein/period-function family already exists for general `q`;
its `z^(-2q)` coefficient is proportional to `zeta(2q)`.  A zeta zero removes
that incoming boundary coefficient.  It does not create an interior `L2`
eigenvector.

Primary sources are Bonanno's complex-temperature formulation
<https://arxiv.org/abs/2211.11664>, Bonanno--Isola's Farey/Selberg construction
<https://arxiv.org/abs/0907.1471>, and the real-temperature spectral analysis
<https://arxiv.org/abs/0708.0686>.

## 3. Exact fixed-metric adjoint

On `H_xi`, write

`M phi(t)=e^(-t) phi(t)`,

`N_q phi(t)=integral J_(2q-1)(2 sqrt(st))/(st)^(q-1/2)
                         phi(s) dm_q(s)`.

The map

`W_q phi(t)=t^(q-1/2)e^(-t/2)phi(t)`

is unitary from `H_xi` to the fixed space `L2(0,infinity;dt)`.  Direct
cancellation of the weights gives

`Ahat_q := W_q(M+N_q)W_q^(-1)`,

`(Ahat_q psi)(t)=e^(-t)psi(t)
  + integral_0^infinity e^(-(t+s)/2)
      J_(2q-1)(2 sqrt(st)) psi(s) ds`.

The kernel is symmetric in `s,t`, so complex conjugation gives the exact
adjoint

`Ahat_q^* = Ahat_(conj(q))`.

This is the clean adjoint calculation sought in the roadmap.  It also exposes
the first mismatch: Hilbert adjunction implements `q -> conj(q)`, whereas the
reflection whose fixed line is RH for `zeta(2q)` is

`q -> 1/2-conj(q)`.

The Bessel integral is Hilbert--Schmidt for `Re(q)>0`.  Multiplication by
`e^(-t)` has spectrum `[0,1]`; consequently the relevant eigenvalue one is an
essential-spectrum threshold.  The operator `I-Ahat_q` is not Fredholm there.

## 4. The honest real-part identity

The homogeneous Hilbert equation

`(M+-N_q-I)phi=0`

is the Maass branch.  The zeta branch instead satisfies the affine equation

`(M+N_q-I)phi=(I-M-N_q)t^(-1)`.

The formal vector `phi+t^(-1)` solves the homogeneous equation, but

`t^(-1) notin H_xi` for `xi<=1`.

In particular it is never an admissible Hilbert vector in the zeta critical
strip.  Set

`psi=W_q phi`,

`rho_q=W_q(I-M-N_q)t^(-1)`,

`S_q=(Ahat_q+Ahat_q^*)/2`.

Taking the real part of the affine equation gives the exact identity

`< (S_q-I)psi, psi > = Re < rho_q, psi >`.

The forcing is explicit:

`rho_q(t)=t^(q-1/2)e^(-t/2) [ (1-e^(-t))/t`

`          - sum_(m>=0) (-1)^m t^m/(m!(m+2q-1)) ]`.

The bracket's constant term is

`1-1/(2q-1)=2(q-1)/(2q-1)`.

It therefore does not vanish at a nontrivial zeta zero.  If instead one tries
to use the formal singular vector, its positive norm has the cutoff divergence

`integral_0^epsilon t^(2xi-3)dt`.

Any finite-part subtraction destroys automatic positivity.  This is the
precise failure of the proposed virial identity: the cusp term is not an error
term waiting to be estimated away.  It is the scattering channel that carries
the arithmetic boundary condition.

## 5. The canonical-intertwiner calculation closes the Farey gate

Let

`q#=1/2-conj(q)`.

Suppose a bounded, boundedly invertible multiplication operator `G=M_w` were
to implement the missing arithmetic reflection:

`G Ahat_q^* G^(-1)=Ahat_(q#)`.

The multiplication term commutes with `G`.  Equality of the continuous Bessel
kernels would require

`w(t)/w(s) J_(2 conj(q)-1)(2 sqrt(st))
   =J_(-2 conj(q))(2 sqrt(st))`.

Putting `s=t` cancels the weight.  Equality for every small positive `t`, and
the leading powers in the Bessel series, force

`2 conj(q)-1=-2 conj(q)`, hence `q=1/4`.

Thus no local positive change of density implements the arithmetic involution
at any nonreal zeta parameter, including points on the proposed RH line.
A dilation cannot repair this because it changes the fixed multiplication
term `e^(-t)` unless the dilation is trivial.

The natural nonlocal candidate is now explicit.  For the line-model principal
series

`(pi_q(g)f)(x)=|cx+d|^(-2q) f((ax+b)/(cx+d))`,

the normalized Knapp--Stein operator is initially

`(I_q f)(t)=Gamma(q)/(sqrt(pi) Gamma(q-1/2))`

`             * integral_R |t-x|^(2q-2) f(x) dx`.

It satisfies

`I_q pi_q(g)=pi_(1-q)(g) I_q`,  `I_(1-q) I_q=1`,

and its `n`th circle-type multiplier is

`(1-q)_(|n|)/(q)_(|n|)`.

It is unitary on `Re(q)=1/2`; away from that line these multipliers grow or
decay like `|n|^(1-2q)`, so it is not a bounded positive similarity on one
fixed standard `L2` space.  Its unnormalized spherical scalar is the purely
archimedean, zero-free factor

`c_inf(q)=sqrt(pi) Gamma(q-1/2)/Gamma(q)`.

There is also a representation-theoretic obstruction before any positivity
argument.  The principal-series Casimir is `lambda(q)=q(1-q)`.  A genuine
intertwiner from `pi_(conj(q))` to `pi_(q#)` would require equal Casimirs, but

`lambda(conj(q))-lambda(q#)=conj(q)-1/4`.

It therefore vanishes for every nonreal parameter, including parameters on
`Re(q)=1/4`.  The RH reflection is not a Weyl symmetry.

The local source calculation confirms that no hidden zeta factor occurs at
infinity.  With the boundary trace

`beta_q(f)=lim_(t->0) t^(1/2-q) f(t)`,

one has `beta_q(rho_q)=2(q-1)/(2q-1)`, and on the one-dimensional singular
boundary quotient

`[I_q rho_q]=((q-1)/q) [rho_(1-q)]`.

Only rational and gamma factors appear locally.  Arithmetic enters exactly
when the construction is automorphized.  The modular Eisenstein constant term
is

`E(z,q)=y^q+varphi(q)y^(1-q)+...`,

where

`varphi(q)=c_inf(q) zeta(2q-1)/zeta(2q)`

`          =Lambda(2q-1)/Lambda(2q)`.

The Farey boundary coefficients make the same quotient visible:

`C_q=zeta(2q)/2`,  `D_q=zeta(2q-1)/(2q-1)`,

so

`D_q/C_q=2/(2q-1) * zeta(2q-1)/zeta(2q)`.

At a zero of `zeta(2q)`, the incoming coefficient vanishes while the outgoing
coefficient does not: this is a pure-outgoing resonance, not a positive
Hilbert eigenstate.  Completing or renormalizing the vector can move these
zeta factors between the operator and the section, but cannot remove them.

The cusp flux gives the same verdict.  For

`u(y)=A y^q+B y^(1-q)`,  `q=xi+i eta`,

the exact boundary form at height `Y` is

`F_Y=eta(|A|^2 Y^(2xi-1)-|B|^2 Y^(1-2xi))`

`    +(2xi-1) Im(A conj(B) Y^(2i eta))`.

On the unitary line `xi=1/2`, conservation is equivalent to unit-modulus
scattering.  At a zeta resonance the completed incoming coefficient is zero,
so `F_Y=-eta |B|^2 Y^(1-2xi)`, which is nonzero and diverges when `xi<1/2`.

**Verdict.**  The canonical nonlocal path is pruned.  A sign or positivity
theorem for the global scattering scalar in `1/4<Re(q)<1/2` would already
exclude its poles and hence contain the RH obstruction.  Any future Farey
proposal must exhibit an independently constructed arithmetic order structure
that is neither a principal-series intertwiner nor a repackaging of this
scattering coefficient.

Primary sources for the normalization are Bruggeman--Lewis--Zagier,
*Function theory related to PSL(2,R)*, equations (1.28)--(1.31),
<https://people.mpim-bonn.mpg.de/zagier/files/tex/BLZ/PSL2R-Oct13-2011.pdf>;
Lewis--Zagier, *Period functions for Maass wave forms I*, Chapter IV,
<https://arxiv.org/abs/math/0101270>; and Bonanno--Isola, equation (2.36),
<https://arxiv.org/abs/0907.1471>.  Zagier's earlier invariant-space proposal
already makes explicit that a positive unitarization of the relevant global
representation would imply RH (and more), rather than provide a known
zero-independent construction:
<https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinRiemannZeta/eisenstein-zeta-978-3-662-00734-1_10.pdf>.

## 6. Prime-5 block rescue

For

`2 log 5 < L < 2 log 7`,

let `Q_0` be the arithmetic Ritz form with finite prime places `{2,3}`, let
`R_5` be the new prime-5 term, and let `Q_1=Q_0+R_5`.  Split the Ritz space into
the negative spectral subspace of `Q_0` and its orthogonal complement.  In this
basis write

`Q_1 = [ A  B  ]`.

`      [ B* D  ]`

The exact finite-dimensional criterion is

`Q_1>0 iff A>0, D>0, and ||A^(-1/2) B D^(-1/2)||<1`.

At `L=3.27`, dimension 12, the unrestricted floating diagnostic gives

| quantity | value |
|---|---:|
| old minimum | `-5.9149754e-5` |
| dimension of old negative sector | `1` |
| full minimum | `5.8277370e-9` |
| `lambda_min(A)` | `3.4779888e-4` |
| `lambda_min(D)` | `5.8277370e-9` |
| normalized cross norm | `0.9904431` |
| Schur minimum | `6.6159895e-6` |

The corresponding moment-constrained diagnostic has normalized cross norm
`0.8779366`.  The prime-5 update is not positive on the full ambient space;
the success is event-specific block repair, not Loewner monotonicity.

## 7. Certified finite theorem

The new driver `src/certified_prime5_rescue.py` uses the exact Legendre overlap
polynomials and 220-bit `mpmath.iv` enclosures.  At the rational support
`L=327/100` and dimension 12 it certifies:

`lambda_min(Q_1,G) > 10^(-9)`;

an explicit rational vector `v` satisfies

`Q_0(v)/||v||_G^2 = -5.914975397755e-5` within the printed interval;

and on the same vector

`R_5(v)/||v||_G^2 = +4.069486315247e-4` within the printed interval.

Consequently

`Q_1(v)/||v||_G^2 = +3.477988775472e-4`.

The generated theorem `Prime5Rescue12.finitePrime5Rescue` strengthens the
software-interval result.  Its two hypotheses say only that arbitrary real
matrices `Full` and `Old` lie in the stored entrywise intervals.  Lean then
proves simultaneously that

- `Full` is strictly positive on every nonzero vector;
- the exact stored witness is negative for `Old`; and
- `Full-Old` is positive on that same witness.

The proof uses an exact integer LDL congruence for the full midpoint and a
perturbation budget of `10^(-20)`.  The principal theorem's axiom audit is
`[propext, Classical.choice, Quot.sound]`; there are no project axioms,
`sorry`, `admit`, or `native_decide` dependencies.

The exact Lean witness is chosen for a comfortable perturbation margin rather
than to reproduce the extremal generalized eigenvector printed by the interval
driver.  Its Euclidean-normalized midpoint values are

- old `{2,3}`: `-1.332719745904e-5`;
- prime-5 correction: `+8.834174912977e-5`; and
- full: `+7.501455167073e-5`.

This kernel-checks the finite algebra.  The analytic identification of the
stored intervals with the Legendre Weil matrices, their `mpmath.iv`
enclosures, and the statement that their difference is exactly the active
prime-5 term remain external.  Nothing here proves a spectral-projector,
operator-level, support-uniform, or RH statement.

Reproduce with

```text
python3 src/certified_prime5_rescue.py
python3 src/prime5_block_rescue.py \
  --supports 3.27 3.30 3.40 --dimension 12 --dps 24

cd lean/weilcert
lake env lean Prime5Rescue12.lean
lake env lean Prime5Rescue12Audit.lean
```

The theorem is finite-dimensional.  At `L=3.27`, the measured full minimum
falls from about `4.9e-6` at dimension 8 to `5.5e-11` at dimension 16, while
the cross norm reaches about `0.997`.  A uniform operator theorem would have
to control this near-saturation.  Finite full positivity alone cannot supply
that control.

## 8. Decision and next research branch

All four fail-fast tasks are complete:

1. the local no-go is exact;
2. the canonical Knapp--Stein normalization and source action are explicit;
3. automorphization exposes the same zeta scattering quotient, closing the
   Farey path as an independent exclusion engine; and
4. the prime-5 finite rescue is preserved by a kernel-checked Lean theorem.

The right next move is not to refine either experiment into an RH claim.  The
prime-5 certificate is a useful control theorem for event-specific repair, but
its near-critical refinement behavior leaves the uniform-support problem
untouched.  The Farey operator is now another exact detector whose proposed
exclusion engine is circular.

The subsequent finite Lee--Yang inverse-cone test is now also complete.  The
general Newman--Stieltjes shadow survives through dimension 20, while the
independent weighted-spin subclass fails at dimension 16; univariate Taylor
data cannot test unspecified interacting couplings.  See
`results/LEE-YANG-INVERSE-CONE-FINAL-2026-08.md`.  The next orthogonal
fail-fast discriminator is therefore the Mobius residue-to-density gate.
