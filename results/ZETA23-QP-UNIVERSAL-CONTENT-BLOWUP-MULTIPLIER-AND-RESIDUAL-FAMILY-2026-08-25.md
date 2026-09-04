# QP universal content blow-up: all square-content multipliers and the surviving residual ray

**Date:** 2026-08-25  
**Verdict:** after recentering at the content-dependent cusp, the union of
all integral multiplier charts

```text
g=2Jd^2,                 J>=1,
```

has fixed-`Q` cardinality

```text
O((B/Q^(1/3))*Q^epsilon)
 =O(D^(23/48+epsilon))
 =O(D^(-1/48)*sqrt(A)*Q^epsilon)                     (0.1)
```

in the already-reduced compact remote energy collar.  The estimate is
uniform in `J`; summing the multiplier one chart at a time would lose it.
The same proof includes the odd half-integral cusp scales: the complete
locus `d^2|g`, with `g=K*d^2`, also satisfies (0.1).

For arbitrary `g`, denominator clearing gives an exact integral normal
crossing.  Its balanced and two one-band axes are now closed at
`sqrt(A)*Q^epsilon` by the companion report.  The remaining two-factor
locus is real: an explicit infinite compact-remote family has `d^2` not
dividing `g`, both normal factors nonzero, and errors of order `Q^(1/2)`.
It does not violate the desired estimate, but it rules out closing the
residual by forcing square content.

The genuinely nonzero arbitrary-content two-factor count remains open.
No sharp four-cycle theorem is proved here.

## 1. Exact multiplier normal form

Let `p>d>=1`, `(p,d)=1`, and put `ell=p^2-d^2`.  For `J>=1` define

```text
g=2Jd^2,
Q=J*p*ell+c,             y=J*d*ell+u,
h=d*c-2p*u.                                             (1.1)
```

With `r=g(p-d)/2`, `s=g(p+d)/2`, and

```text
e=r(Q+y)-y^2,            f=s(Q-y)-y^2,
n=p*y-Q*d,
```

direct expansion gives

```text
e+u^2=J*d*(p-d)*(h-d*u),
f+u^2=J*d*(p+d)*(h+d*u),
n=p*u-c*d,               e-f=2Jd^2*n.                (1.2)
```

There is also an exact transverse identity:

```text
u*y=-J*d*p*n-(e+f)/2.                                 (1.3)
```

Thus the multiplier changes only the scale of the central normal crossing;
it creates no new algebraic shape.

## 2. Count all multipliers before summing them

Assume the fixed compact collar `d<=eta*p`, `eta<1`, the remote cut
`|y|>>Q^(2/3)`, and

```text
|e|<=A<=B,             |f|<=B,
Q=D^(33/16),            B<D^(7/6),
A>=D,                   B=o(Q).                       (2.1)
```

Equations (1.2)--(1.3), together with the slope equation, first imply

```text
|u| << Q*B/y^2 << B/Q^(1/3)=:X=o(sqrt(A)).           (2.2)
```

Consequently `u^2=o(A)`, and (1.2) retains the asymmetric band strengths:

```text
|u| << B/(J*d^2*p),
|h| << B/(J*d*p),
|c| << B/(J*d^3).                                     (2.3)
```

In particular `|c|=o(Q)`, so

```text
J*p^3 asymp Q,              p<<Q^(1/3).               (2.4)
```

Substituting (2.4) in the height bound gives the uniform estimate

```text
|h| << X/d.                                           (2.5)
```

Suppose first that `h!=0`.  There are only

```text
sum_(d<<X) O(X/d) <<X*log Q                           (2.6)
```

possible signed pairs `(d,h)`.  For each such pair,

```text
h=d*Q-J*d*p*ell-2p*u
```

shows that

```text
p | d*Q-h.                                            (2.7)
```

The integer on the right is nonzero and polynomially bounded in `Q`, so
there are `Q^epsilon` possible `p`.  Once `(d,h,p)` is fixed there is at
most one `J`: increasing `J` changes

```text
u=(d*Q-h-J*d*p*ell)/(2p)
```

by `d*ell/2 asymp d*p^2`, whereas (2.3)--(2.4) confines each candidate to
`O(B*p^2/(Q*d^2))`; their ratio is `O(B/(Q*d^3))=o(1)`.

If `h=0`, then `p|Q`.  A nonexact point has `|u|>=d/2`; hence (2.3) gives

```text
J*p*d^3<<B,             d^3<<B*p^2/Q<<X.             (2.8)
```

This costs only `X^(1/3)Q^epsilon`, and the same gap makes `J` unique.
The remaining `h=u=0` points satisfy

```text
Q=J*p*(p-d)*(p+d),                                   (2.9)
```

so they are divisor-many exact cusps.  Combining (2.6)--(2.9) proves
(0.1).

The power ledger is

```text
X=B/Q^(1/3)<=D^(7/6-11/16)=D^(23/48),
sqrt(A)>=D^(1/2),
sqrt(A)/X>=D^(1/48).                                 (2.10)
```

## 3. Odd multipliers cost nothing extra

The parity-complete formulation writes

```text
g=K*d^2,                  K>=1,
c_0=2Q-K*p*ell,           u_0=2y-K*d*ell,
h_0=d*c_0-2p*u_0.                                    (3.1)
```

Then

```text
4e+u_0^2=K*d*(p-d)*(h_0-d*u_0),
4f+u_0^2=K*d*(p+d)*(h_0+d*u_0),
2n=-(h_0+p*u_0).                                    (3.2)
```

The proof of Section 2 applies verbatim with `K*p^3 asymp Q`.  The height
congruence is now

```text
p | 2d*Q-h_0,                                        (3.3)
```

and the balanced axis has `p|2Q`.  Therefore (0.1) holds for every
`d^2|g`, not only for even `K=2J`.  This also reconciles the exact cusp
factorization `g=K*d^2`, whose scale `K/2` can be half-integral.

## 4. Universal blow-up and the axes already closed

For arbitrary content define

```text
C=2d^2Q-g*p*ell,          U=2d*y-g*ell,
H=C-2p*U,                 j_-=H-dU,  j_+=H+dU.       (4.1)
```

Then, exactly,

```text
2d*n=-(H+pU),
4d^2e+U^2=g*(p-d)*j_-,
4d^2f+U^2=g*(p+d)*j_+,                               (4.2)

4d^2*((p-d)f-(p+d)e)=4d^2*U*y.                      (4.3)
```

The companion central-content report uses the equivalent signs
`T=-C`, `v=U`, `z=-H`.  It proves, with the asymmetric mask preserved,

```text
H=0,             j_-=0,             j_+=0
```

each has `O(sqrt(A)*Q^epsilon)` points.  On `j_-=0`, integrality forces
`U=2d*xi`, `e=-xi^2`, and

```text
p | Q-xi,                    p+d | Q+xi.             (4.4)
```

On the broad-square axis `j_+=0`, the only asymmetric danger is
`xi=-t` near the second root `t=g(p-d)`.  Putting
`eta=t-g(p-d)` replaces the long `t`-range by `|eta|<<sqrt(A)` and gives

```text
p-d | 2(Q+eta),              p-2d | 2(Q+3eta).       (4.5)
```

These are divisor peels, not cancellation estimates.  Details and the
balanced-axis proof are in Section 4.3 of
`ZETA23-QP-REFLECTED-C-MAJOR-ARC-COUNT-AND-BALANCED-OFFSET-COUNTEREXAMPLE-2026-08-25.md`.

## 5. A genuinely non-square-content residual family

Fix `m>=2` and let `d>2`.  Put

```text
p=m*d+1,                  ell=p^2-d^2,
g=2d,
Q=(p*ell-1)/d,            y=ell.                     (5.1)
```

The numerator defining `Q` is divisible by `d`.  Since `(p,d)=1`, the
corresponding integral point has

```text
r=d*(p-d),                s=d*(p+d),
C=H=-2d,                  U=0,
j_-=j_+=-2d,                                         (5.2)

e=-(p-d),                 f=-(p+d).                  (5.3)
```

For fixed `m`, one has

```text
Q asymp d^2,              y asymp Q,                 (5.4)
```

so this is compact-remote, not an endpoint artifact.  Moreover

```text
g=2d,                     d^2 does not divide g.     (5.5)
```

The errors are `Q^(1/2+o(1))`; hence the family enters the admissible
energy masks, for example whenever `A,B>=D^(33/32+epsilon)`, still well
inside `m^2M^3<D^(1/2)` for small fixed epsilon.

This family proves that the arbitrary-content residual cannot be discarded
by asserting `d^2|g`, nor by deleting the three axes of Section 4.  It gives
one coherent ray for each of its centres, so it is not a counterexample to
the desired packet count.  Its role is diagnostic: the final theorem must
count or cancel genuine two-factor content rounding.

## 6. Status

```text
exact g=2Jd^2 multiplier identities:                PROVED;
all-J fixed-Q count O(B/Q^(1/3) Q^epsilon):         PROVED;
extension to every d^2|g, including odd K:          PROVED;
universal integral blow-up (4.1)--(4.3):            PROVED;
balanced and one-band arbitrary-content axes:       PROVED (companion);
forcing d^2|g outside those axes:                   FALSE;
infinite genuine two-factor family (5.1):           PROVED;
arbitrary-content nonzero two-factor count:         OPEN;
sharp four-cycle bound:                              NOT PROVED.
```

The replay implementation and tests are

```text
src/qp_universal_content_blowup.py
src/test_qp_universal_content_blowup.py
```

