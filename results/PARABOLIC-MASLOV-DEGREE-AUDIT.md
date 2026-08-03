# Parabolic Maslov-degree audit

Status: the collision orientation is useful, but the boundary amplifier
collapses to the existing Laguerre target; Path A is pruned as independent,
2026-08-01.

Let

`F(t,x)=(H_t(x), H_x(t,x))`

for the backward heat flow `H_t=-H_xx`, and identify this vector with

`Z(t,x)=H(t,x)+i H_x(t,x)`.

## Local degree

At a generic collision `H=H_x=0`, `H_xx!=0`,

`det D_(t,x)F = H_t H_xx-H_x H_xt = -H_xx^2<0`.

Thus every generic collision has local Brouwer degree `-1`.  This genuinely
avoids the quartet cancellation that killed ordinary signed spectral flow.

## Exact boundary one-form

Away from collisions,

`d arg Z = Im(dZ/Z)`.

Along a horizontal edge one obtains

`partial_x arg Z`

` = (H H_xx-H_x^2)/(H^2+H_x^2)`

` = -(H_x^2-H H_xx)/(H^2+H_x^2)`.

Thus the horizontal winding density is exactly the negative normalized first
Laguerre density.

Along a vertical edge, the heat equation gives

`partial_t arg Z`

` = (H H_xt-H_x H_t)/(H^2+H_x^2)`

` = (H_x H_xx-H H_xxx)/(H^2+H_x^2)`

` = partial_x(H_x^2-H H_xx)/(H^2+H_x^2)`.

Hence the finite-rectangle degree formula contains no independent positive
quantity: its horizontal term is the Laguerre expression already studied,
and its vertical term is its spatial derivative divided by the same phase
amplitude.

## Global closure obstruction

As `|x|->infinity`, both `H` and `H_x` tend to zero.  The map `F/|F|` therefore
has no automatic nonvanishing compactification at the vertical ends.  A
renormalization must determine the asymptotic direction of `(H,H_x)`, which is
equivalent to controlling the high-frequency xi phase and its zeros.

On the `t=0` edge, evaluating the winding is likewise the variation of
`arg(xi+i xi')`; monotonicity is precisely Laguerre positivity.  The modular
theta relation removes all algebraic boundary jets but does not determine this
beyond-all-orders phase.

## Verdict

The same-sign local degree is an exact and reusable observation.  But the
proposed global amplifier is not new: proving zero boundary degree requires
the same completed-theta Laguerre sign or equivalent zero-phase control that
Path A was intended to derive.

Path A is therefore pruned as an independent route.  It may serve as a
topological interpretation of any future modular Laguerre proof, but it does
not currently supply that proof.
