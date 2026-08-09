# Nonlocal Ward covariance no-go

Status: exact completion theorem, exact abstract sign countermodels, and a
complete finite arithmetic diagnostic; 2026-08-06.  This note kills the
proposed R72 nonlocal Ward--innovation bridge as a separate algebraic
mechanism.  It does **not** prove or disprove the Riemann Hypothesis.

## 1. Verdict

The last survivor in R72 was the global covariance remainder

```text
G=K(Z,Z)-2 Re sum_n a_n K(phi_n,Z)
  +sum_(n!=r) a_n conjugate(a_r)K(phi_n,phi_r).            (1.1)
```

It was hoped that `G` would supply, with a forced sign, the second connected
`Lambda*Lambda` copy missing from a local semiprime-fiber calculation.
There is no such independent identity.

The decisive facts are:

1. Exact Vaughan completion gives

   ```text
   G=K(C_full+E_Y,C_full+E_Y)-D_tail                       (1.2)
   ```

   identically.  Thus the proposed nonlocal cancellation is the unknown
   completed energy with its tail diagonal moved to the other side.
2. Selberg's Ward identity rewrites selected one-product diagonal weights.
   It gives no sign for the center or for unequal-product Gram entries.
3. A complete finite numerical model with the actual grouped Vaughan
   coefficient, B-spline coboundary, continuous terminal Markov law, smooth
   Type-I center, and every unequal product violates all four natural
   orientations of the proposed lift in the same configuration.
4. The strongest functional-equation rescue becomes a product of singular
   boundary values of `xi'/xi`.  An honest regulator leaves a divergent
   contact term carrying the zeros themselves.

Consequently R72 supplies useful identities and a cubic semiprime
calibration, but no positive cancellation gain.  A direct arithmetic bound
for the right side of (1.2) could still prove the P4/R71 target; it would be
the original problem, not a Ward shortcut.

## 2. Exact completion collapse

Let `K` be any Hermitian terminal covariance and set

```text
T=sum_n a_n phi_n,
D_tail=sum_n abs(a_n)^2 K(phi_n,phi_n).                   (2.1)
```

Expanding the square gives the unconditional identity

```text
D_tail+G=K(T-Z,T-Z).                                     (2.2)
```

Now let `L` be the full von Mangoldt field, let `H=L-T` be the exact Type-I
head, and let `P` denote the pole field.  With

```text
C_full=L-P,
Z_exact=P-H,                                             (2.3)
```

one has `T-Z_exact=C_full`.  If the explicit Type-I evaluation is

```text
H_app=H+E_Y,
Z_app=P-H_app=Z_exact-E_Y,                               (2.4)
```

then

```text
T-Z_app=C_full+E_Y.                                      (2.5)
```

Substitution in (2.2) proves (1.2), or more explicitly,

```text
G=K(C_full,C_full)
  +2 Re K(C_full,E_Y)+K(E_Y,E_Y)-D_tail.                 (2.6)
```

With the exact head, `E_Y=0`.  With an approximate head, Cauchy--Schwarz
only gives

```text
abs(K(C_full,E_Y))
 <=sqrt(K(C_full,C_full)K(E_Y,E_Y)),                     (2.7)
```

so a small Euler-defect energy cannot control the mixed term before the
unknown completed energy is controlled.

For any proposed Ward counterterm `C_W`, (2.6) is equivalently

```text
G+C_W=K(C_full+E_Y,C_full+E_Y)-(D_tail-C_W).             (2.8)
```

If `D_tail-C_W` is the cubic anisotropy plus controlled companions, a bound
on the left of (2.8) is exactly the desired bound on the complete carrier.
No new source of sign has appeared.  Positivity of covariance gives only
the sharp generic statement `G>=-D_tail`.

This proves a scoped no-go: Vaughan completion, polarization, and total
variance cannot derive the missing lift.  It does not forbid an additional
zeta-specific correlation theorem.

## 3. What the Ward identity does and does not control

Write

```text
b=Lambda log+Lambda*Lambda=mu*log^2,
b*1=log^2.                                                (3.1)
```

For `n=pq`, `x=log p`, `y=log q`, and
`kappa=K(phi_(pq),phi_(pq))`, (3.1) gives

```text
D_(pq)=(x+y)^2 kappa,
C_W=4xy kappa,
D_(pq)-C_W=(x-y)^2 kappa.                                (3.2)
```

This is an exact and useful diagonal relabeling.  But (3.1) has one product
index.  It contains no information about

```text
K(phi_n,phi_r), n!=r,       or       K(phi_n,Z).          (3.3)
```

An exact Type-I head cancels the whole local `pq` composite coefficient.  In
that fiber `G=-D_(pq)`, not `-C_W`: the completion removes the anisotropy as
well.  Recovering precisely the anisotropy after all other products and the
smooth center are restored is the complete-energy estimate in (2.8).

The absence of a generic sign is exact.  Normalize
`K(phi,phi)=K(psi,psi)=1`, put

```text
T=(x+y)phi,   Z=(x+y)psi,   K(phi,psi)=rho, abs(rho)<=1.
```

Then the Gram matrix is positive semidefinite and

```text
D=(x+y)^2,
G=D(1-2rho).                                              (3.4)
```

Taking `rho=1` or `rho=0` changes the sign of `G+C_W` while all scalar Ward
identities remain unchanged.  Two tail atoms with `Z=0` likewise make the
unequal-product contribution `2a_1 a_2 rho`, of either sign.  Therefore no
sign follows from Ward plus positive covariance alone.

## 4. The mandatory Toeplitz twist

The actual scale geometry sharpens the obstruction.  After block
integration, a translation profile `V` and an order-`m` terminal average
give, up to the Fourier normalization,

```text
integral K_R(T,T)dR
 =1/(2pi) integral_R abs(Vhat(t))^2
    [1-abs(a_h(it))^(2m)]
    abs(sum_n a_n n^(-1/2-it))^2 dt,                     (4.1)
```

where `a_h(s)=(1-exp(-hs))/(hs)`.  The arithmetic object is consequently a
two-shift, ratio-twisted divisor correlation.  At `N=pq` its connected
factor is

```text
sum_(dr=pq) Lambda(d)Lambda(r)(d/r)^(-it)
 =2log(p)log(q) cos(t log(p/q)).                          (4.2)
```

It has both signs.  The ordinary Selberg Ward coefficient is only the
untwisted value at `t=0`, precisely where the innovation multiplier in
(4.1) vanishes.

Equivalently, if

```text
kappa_m(d)=1/(2pi) integral abs(Vhat(t))^2
  [1-abs(a_h(it))^(2m)] exp(itd)dt,                       (4.3)
```

then `kappa_m(0)>0`, while its integral in `d` is zero under the usual
integrability hypotheses.  Hence the Toeplitz covariance kernel is negative
somewhere.  Stein integration by parts or another Markov representation can
change the spectral weight in (4.1), but it cannot remove the twist (4.2).

A survivor would need a new cutoff-complete **two-shift** arithmetic
estimate.  The one-shift identity (3.1) cannot provide it.

## 5. The strongest functional-equation rescue also closes

There is a tempting off-wall conversion.  Put `l=xi'/xi`.  Away from zeros,
the functional equation and conjugation give formally on the critical line

```text
l(1/2-it)=-l(1/2+it),
abs(l(1/2+it))^2=-l(1/2+it)^2
                =l'(1/2+it)-xi''/xi(1/2+it).             (5.1)
```

This looks like the desired Toeplitz-to-Hankel Ward linearization.  It is not
a legitimate finite-energy identity: `l` has poles at the known critical
zeros, `abs(l)^2` is not locally integrable there, and the square of the
corresponding boundary distribution is undefined.

Use an honest regulator.  For

```text
A=l(1/2+sigma+it),
B=l(1/2-sigma+it),       sigma>0,                         (5.2)
```

the functional equation gives

```text
abs(A)^2=-A B
        =A'-xi''/xi(1/2+sigma+it)+A(A-B).                (5.3)
```

The last term is the opposite-boundary contact defect.  Near a simple
critical zero `1/2+i gamma`, the leading part of `-AB` is

```text
1/[sigma^2+(t-gamma)^2],                                 (5.4)
```

whose mass is `pi/sigma`.  It is not a removable error; it records the zero
carrier.  Off-line poles also obstruct the contour motion needed to discard
it.  Thus (5.1) is a singular boundary mirage, while (5.3) restores exactly
the information the formal square appeared to eliminate.

## 6. Complete finite arithmetic gate

The diagnostic
[`src/ward_nonlocal_covariance_probe.py`](../src/ward_nonlocal_covariance_probe.py)
uses all of the following simultaneously:

- the grouped coefficient `a_Y=mu_(>Y)*Lambda_(>Y)*1`;
- the order-`j` fixed-step B-spline coboundary;
- the continuous order-`m` Irwin--Hall terminal law;
- the explicit pole-polynomial Type-I center;
- every unequal total product and the exact-head coordinate in parallel.

At

```text
X=76, Y=5=floor(X^(3/8)), h=0.05, j=m=1,                 (6.1)
```

the support condition holds and the active grouped products are exactly
`70,77,78`; the central semiprime is `77=7*11`.  The audit gives

```text
D_tail                         0.0172669075839
missing Ward copy M            0.00726004686735
full connected covariance 2M  0.0145200937347
unequal-product covariance    -0.00719837885972
center contribution           +0.0000830312729785
G                              -0.00711534758675
full innovation                0.0101515599972            (6.2)
```

All four natural margins are negative in the same complete model:

```text
G-M                            -0.0143753944541
(-M)-G                         -0.000144699280609
full innovation-2M             -0.00436853373755
(-retained connected)-G_ret    -0.0119993157882.          (6.3)
```

Thus neither sign convention for “supply the missing copy,” domination by
the full innovation, nor cancellation in the retained energy is a finite
identity.  With the exact head the same model has

```text
G_exact=+0.0263706742747,
K(C_full,C_full)=0.0436375818586.                         (6.4)
```

The Euler polarization correction is `-0.0334860218615` and reverses the
sign.  This is a direct numerical illustration of (2.6), not a small term
with a preferred orientation.

Gaussian orders `8` through `24`, split at every arithmetic and spline knot,
agree on the decisive quantities to about `1e-15`.  A larger replication at
`X=1200,Y=14` contains `44` active products and `9` central semiprimes and
again makes all four margins negative.

These are reproducible floating diagnostics, not interval certificates.
The exact theorem is the completion collapse (2.6), and the exact abstract
Gram models prove the generic sign no-go.  The arithmetic run shows that the
fixed profiles and explicit center do not rescue any of the proposed finite
orientations.

Focused tests are in
[`src/test_ward_nonlocal_covariance_probe.py`](../src/test_ward_nonlocal_covariance_probe.py).

## 7. Research consequence

Close the R72 nonlocal lift as an independent mechanism.  Retain:

1. the Markov innovation telescope as an exact scale-energy ledger;
2. the Ward/Wick diagonal subtraction as a faithful but indefinite
   renormalization;
3. the cubic near-square anisotropy calibration;
4. R71's complete P4 energy as the actual open target.

Do not spend further effort trying to derive a sign for (1.1) from Vaughan
completion, Selberg's one-shift Ward identity, conditional expectation,
Stein identities, or the unregularized functional equation.  A legitimate
revival must state and prove an independently signed, cutoff-complete
two-shift correlation theorem for (4.1).  After (1.2), such a theorem should
be recognized as a direct attack on the P4/R71 completed energy rather than
as a cheaper cancellation identity.
