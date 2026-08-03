# Arithmetic angle and dual-frame checkpoint

Status: low-rank angle and scalar ground-state mechanisms are rejected; the
exact surviving object is a support-dependent contractive dual frame, with its
nested old-state column determined explicitly, 2026-08-01.

## 1. Exact angle certificate

On the two-moment relative space let

`A = continuum incidence energy`, `P = prime incidence energy`,

and let `D` be the exact scalar degree.  Write

`alpha = inf spec(A)`, `beta = inf spec(P)`,
`Delta = D-alpha-beta`.

For spectral cutoffs `s,t>0`, let

`U = 1_[0,s)(A-alpha I)`, `V = 1_[0,t)(P-beta I)`,

and put `c=||UV||`.  Spectral calculus and the sharp weighted two-projection
bound give

`A+P-D I >= [kappa(s,t,c)-Delta] I`,

where

`kappa(s,t,c)`

` = (s+t-sqrt((s-t)^2+4 s t c^2))/2`.

Thus the independently checkable sufficient condition is

`c^2 <= ((s-Delta)(t-Delta))/(s t)`.

This is genuinely noncircular: the projections and angle belong to the two
separate positive component operators.  It is only sufficient, so failure does
not say that the joint form is negative.

## 2. The low-rank angle fails fast

`src/incidence_angle_scan.py` optimizes every pair of two-band cutoffs in the
relative Legendre Galerkin space.  At dimension 12:

| support | missing reserve `Delta` | best two-band `kappa` | result | first multilevel certificate |
|---:|---:|---:|:---:|---:|
| 1.750 | `0.120750` | `0.160640` | passes | `2/10` modes |
| 2.485 | `0.683291` | `0.331696` | fails | `8/10` modes |
| 2.996 | `1.024936` | `0.455244` | fails | `9/10` modes |
| 3.555 | `0.961621` | `0.484131` | fails | `9/10` modes |
| 4.040 | `1.246355` | `0.585738` | fails | `9/10` modes |

The multilevel certificate retains the exact first `k` eigenvalues of each
component and replaces every higher eigenvalue by the next spectral floor.  It
is a rigorous matrix lower bound and becomes the full Galerkin matrix when all
modes are retained.  Refinement makes the compression worse:

- at dimension 28, support `2.485` first certifies at `24/26` modes;
- at dimension 28, support `2.996` first certifies at `25/26` modes;
- in the dangerous even block at support `4.040`, it needs `12/13` modes.

The strong separation of the lowest component eigenvectors is therefore
misleading.  Some raw right angles merely compare opposite parities.  Even
within the dangerous parity block the component ground-state overlap is tiny,
but the scalar deficit is much larger than the first excitation gaps.  Almost
the complete spectral profiles are required to recover the observed joint
margin.

This prunes a fixed-dimensional or fixed-number-of-bands angle theorem.

## 3. Exact Feshbach reduction, and why comparison still loses

Let `A0=A-alpha I`, `P0=P-beta I`, choose a low archimedean projection `U`, and
write the target operator in low/high blocks as

`H = A0+P0-Delta I = [[L,C*],[C,K]]`.

When `K>0`, completed-square algebra gives the exact equivalence

`H>=0  iff  L-C* K^-1 C >= 0`.

This is a useful finite low-sector reduction but not a proof: using the exact
`K^-1` merely repackages the target.  Replacing `K` by an independently
controlled comparator produces a legitimate sufficient theorem.  An
exploratory calibration using `theta P0` as the retained prime comparator
required

| support | required `theta` |
|---:|---:|
| 1.750 | `0` |
| 2.485 | `0.96348` |
| 2.996 | `0.97410` |
| 3.555 | `0.98759` |
| 4.040 | `0.998974` |

Thus even the high-sector resolvent must be reproduced almost exactly.  A
generic comparison theorem with fixed loss cannot close.

Low-rank boundary data do not repair this.  At support `4.04`, dimension 28,
the first three endpoint jets capture only `0.47%` of the centered component
force.  Six prime-kink values capture `63.5%`; values and derivatives at all
kinks capture `98.3%`, but then use `12` traces in a `13`-dimensional parity
block.  The normalized outer endpoint amplitude also falls to `2.58e-8`.
There is no observed scalar Wronskian or fixed boundary jet controlling the
dangerous mode.

## 4. Why the normalized Markov generator cannot directly factor the form

For a finite prime set `S`, put

`F_(S,sigma)(t)=Gamma_R(sigma+i t)`
`                 product_(p in S)(1-p^(-sigma-i t))^-1`.

At `sigma=1/2`, direct logarithmic differentiation gives

`partial_sigma log |F_(S,sigma)(t)|^2 = E_S(t)-D_S`.

Normalizing by the zero-phase value subtracts the value at `t=0` and gives the
unconditional Levy/Markov generator `E_S(t)`.  Hence the scalar counterterm is
exactly the difference between the genuine local contraction and the Weil
symbol.

This also proves a no-go statement.  The Markov generator has `E_S(0)=0`, so

`E_S(0)-D_S=-D_S<0`.

No translation-invariant pointwise Gram multiplier can factor the shifted
form.  A successful factor must use the compact-support Paley--Wiener space and
the two moment constraints.

Scalar Doob/Picone transforms do not do so.  For the archimedean jump density

`nu_infinity(dz)=exp(-|z|/2)/(1-exp(-2|z|)) dz`,

the exponential seed `h(x)=exp(kappa x)` has

`Lh/h = - integral (cosh(kappa z)-1) nu(dz) <= 0`,

the wrong sign for the positive degree.  At the required boundary exponent
`kappa=1/2`, the integral diverges.  The pole moment vectors are therefore not
admissible ground-state seeds.

## 5. The exact completed intertwiner is already an RH criterion

Suzuki's unconditional arithmetic transform has the form

`(U v)(z)=pi^(-1/2) integral S_x(conj z) v'(x) dx`,

where `S_x` is written using completed-xi, von Mangoldt, pole, digamma, and
Hurwitz--Lerch data.  The desired Gram identity is

`pi^-1 <S_x,S_y>`

` = g(x-y)-g(x)-g(-y)+g(0)`.

It would give `Q_W(v)=||Uv||^2`.  Suzuki proves that this identity is equivalent
to RH; the conditional proof uses innerness of the shifted xi quotient, and a
contour proof acquires precisely the off-line-zero residues.  Thus this is the
correct completed factor, but its Gram identity cannot be imported as an
independent literature fact.

The same boundary is visible probabilistically: Nakamura--Suzuki prove that
`exp(g_zeta(t))` is an infinitely-divisible characteristic function if and
only if RH.  Our local contraction avoids circularity precisely because it
factors `E`, not `E-D`.

Primary sources:

- Masatoshi Suzuki, *Weil's quadratic form via the screw function*,
  <https://arxiv.org/abs/2606.09096>;
- Masatoshi Suzuki, *On the Hilbert space derived from the Weil distribution*,
  <https://arxiv.org/abs/2301.00421>;
- Takashi Nakamura and Masatoshi Suzuki, *On infinitely divisible
  distributions related to the Riemann hypothesis*,
  <https://arxiv.org/abs/2306.08317>.

## 6. Surviving exact target: a contractive dual frame

Let `B_a` be the completed incidence gradient on the relative moment space, so

`Q_a=B_a^* B_a-D(a)I`.

Douglas factorization gives the exact equivalent target:

> Construct a contraction `C_a` from the relative vertex space to the incidence
> edge space such that `B_a^* C_a=sqrt(D(a)) I`.

Then

`Q_a=B_a^*(I-C_a C_a^*)B_a >= 0`.

The canonical formula

`C_a=sqrt(D(a)) B_a(B_a^*B_a)^-1`

is circular because its contractivity is the desired inequality.  Progress
requires an arithmetic formula for `C_a` derived before positivity.

There is nevertheless an exact new propagation fact.  If an old relative
state is embedded from support `a` into support `b`, the new-shell gradient is

`B_shell J = sqrt(D(b)-D(a)) V_ab`

for an isometry `V_ab`; this is the polarized form of the disjoint-shift energy
identity.  Given an old dual frame `C_a`, its forced extension on embedded old
states is

`C_b J f = sqrt(D(a)/D(b)) C_a f`

`          direct-sum sqrt((D(b)-D(a))/D(b)) V_ab f`.

The squared coefficients add to one, so this column remains contractive, and
pairing with `B_b J` gives the compressed identity

`J^* B_b^* C_b J = sqrt(D(b)) I`.

Therefore the old--old block of the intertwiner is solved exactly.  This alone
does not prove the full column equation: its pairing against new collar states
is one of the remaining cross conditions.

The only new content at each support event is extending this prescribed
contractive column to genuinely new collar states while satisfying the dual
identity, including that old--collar compatibility.  This is a concrete contractive
operator-completion problem, not another scalar Poincare estimate.

Lean formalizes the angle-reserve implication, the zero-frequency no-go, and
the contractive-dual sufficient theorem in
`RHP2Bridge.IncidenceAngleCriterion`.  The exact nested-support energy identity
was already formalized in `RHP2Bridge.SharpIncidenceTransport`.

## 7. Subsequent collar-completion verdict

The proposed next step has now been carried out.  Generic contractive block
completion is exactly Douglas factorization and hence equivalent to the full
Weil lower bound.  The shell geometry does produce an explicit noncircular
return cycle, but its necessary right-inverse bound fails strongly and worsens
under refinement; fresh-shell and combined variants supply only `4%`--`9%` of
the required degree.  See `INCIDENCE-SHELL-COMPLETION.md` and registry item
`R39`.  Thus the natural recursive dual-frame branch is pruned; only additional
explicit nonlocal cycles in the old-edge kernel remain within this framework.
