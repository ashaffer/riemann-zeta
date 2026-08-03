# Hodge low-sector Dirichlet-to-Neumann audit

Status: the exact Green/Dirichlet-to-Neumann identity exists, but its sign is
the remaining enlarged-window positivity pivot.  Analytic continuation of the
exterior residual does not force contraction.  The obstruction and the exact
two-mode pivot are kernel-checked in `RHBridge/HodgeLowSectorNoGo.lean`.

## 1. The exact scalar identity

After every already-controlled direction is Schur-eliminated, group the last
old mode `v` and its positive complement as

`Q = [[lambda, r*], [r, Dhat]]`, with `Dhat > 0`.

The `Dhat`-harmonic extension of `t v` is

`t v + w`, where `w = -t Dhat^-1 r`,

and completing the square gives

`Q(t v+w) = t^2 (lambda - <r,Dhat^-1 r>)`.

Thus, writing `h=<r,Dhat^-1 r>`, Haynsworth inertia additivity gives

`negative_index(Q) = negative_index(Dhat) + negative_index(lambda-h)`.

When `Dhat>0`, the desired strict contraction `h<lambda` is therefore exactly
positivity of the last unresolved enlarged sector.  Equality is exactly a
zero mode.  This is a useful one-scalar reduction, but a Green identity alone
does not determine its sign.

## 2. The off-diagonal correction in the odd two-mode block

For two surviving odd old modes, let

`Lambda-H = [[lambda1-h11, -h13], [-h13, lambda3-h33]]`.

If `lambda1-h11>0`, the exact last pivot is

`p3 = lambda3-h33 - h13^2/(lambda1-h11)`.

Equivalently,

`det(Lambda-H)>0  <->  p3>0`.

Consequently `h33<lambda3` is only the diagonal necessary condition unless
`h33` has already been redefined after eliminating the first mode.  The
`h13` term cannot be dropped on structural grounds.  In the hard activation-5
Galerkin diagnostic at old degree 121, it consumes about 16% of the raw third
mode margin while leaving the exact pivot positive.  This number is
diagnostic, not a continuum certificate.

## 3. Analytic convolution does not force the sign

Let `I` and `E` be disjoint sets of measures `m` and `n`, and on their union
consider the even translation-invariant rank-one form

`Q(f) = ||f||_2^2 - alpha |integral f|^2`.

The nonlocal kernel is the constant function `-alpha`, hence entire.  On the
normalized constant directions, the old gap, exterior gap, squared cross
residual, and exterior response are

`lambda = 1-alpha m`,

`d = 1-alpha n`,

`r^2 = alpha^2 m n`,

`h = alpha^2 m n/(1-alpha n)`.

The exact difference is

`h-lambda = (alpha(m+n)-1)/(1-alpha n)`.

Choose `alpha m<1`, `alpha n<1`, but `alpha(m+n)>1`.  Both separate
compressions are strictly positive, the weak old eigen-equation holds, and
the exterior residual is analytic, yet `h>lambda` and the union has a
negative direction.  For example `m=n=1`, `alpha=3/4` gives

`lambda=d=1/4`, `h=9/4`,

and the harmonic extension with scalar coefficients `(1,3)` has energy `-2`.

This rules out any theorem based only on self-adjointness, convolution form,
evenness, analyticity away from the diagonal, separate block positivity, or
unique continuation of the old weak equation.  It does not rule out a
zeta-specific estimate using the exact prime--digamma cancellation.

## 4. Why Suzuki's boundary form does not supply the missing inequality

Suzuki's 2026 operator construction does provide a nonlocal boundary form,
but first chooses `mu<lambda_a` and equips the test space with the positive
energy of `T_a=A_a-mu I`.  Its ordinary-kernel version is

`S_a=G_a-mu(-Delta_N)^-1`.

At zero energy, taking `mu=0` requires knowing `lambda_a>0`; in the global
discussion the paper makes this specialization only under RH.  Therefore
using that zero-energy Hilbert space or its boundary Wronskian to prove
`lambda_a>0` would assume the missing sign.  See M. Suzuki,
[*Weil's quadratic form via the screw function*](https://arxiv.org/abs/2606.09096),
Sections 1.2, 6, and 8.

## 5. Surviving target

The high-sector theorem can reduce the problem to finitely many low response
entries.  A genuine close must then estimate the explicit zeta Weyl scalar

`<r,Dhat^-1 r>`

or the exact two-mode pivot above from the combined pole + digamma/Lerch -
prime-translation kernel.  A direct estimate would be substantive progress;
renaming the Schur complement as a Green function, analytic continuation, or
a Dirichlet-to-Neumann map does not provide the sign.
