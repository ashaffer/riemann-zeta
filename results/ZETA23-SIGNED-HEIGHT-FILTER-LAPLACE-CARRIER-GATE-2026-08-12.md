# Signed height filters null samples cheaply but do not normalize the Laplace carrier

Status: exact separated-node signed interpolation theorem, exact two-leg
Wiener factorization audit, and carrier-normalization obstruction,
2026-08-12.  No fractional arithmetic edge, zero-free strip, or new bound on
a zeta zero is proved.

## 1. Verdict

There is a genuine escape from the most obvious bandwidth objection.
Suppose the active cross-prime offsets are

```text
u_j=log(n_j/Y)
```

in a fixed bounded interval.  After an `O(1/Y)` harmless perturbation of the
cross center, the set `{0,u_1,...,u_M}` is `c/Y`-separated.  If

```text
H >= C*Y*log(M+1),
```

then there is a complex signed measure `mu`, supported in the high-frequency
interval `[H,3H]`, whose
Fourier transform obeys

```text
phi(0)=1,
phi(u_j)=0                 (1<=j<=M),
||mu||_TV<=sqrt(2).                                  (1.1)
```

At the carrier parameters `Y=X^0.66`, its maximum frequency is `o(X)`.  Thus a
bounded-total-variation signed Beurling filter can annihilate the whole
finite prime-power cluster inside the available ordinate aperture.  Zero
counting, Bernstein's inequality, and the density of the prime nodes do
**not** force an exponential norm bill.

This does not produce the requested arithmetic reserve.  Equation (1.1)
normalizes the point evaluation

```text
q(0)=sum_k h_k.
```

The selected off-line carrier is instead the compact Laplace functional

```text
L_alpha(q)=sum_k b_k*h_k,
b_k=integral W_alpha(u)*exp(i*xi_k*u)du.             (1.2)
```

For a fixed-width smooth lobe, `b_k=O_A(|xi_k|^-A)` for every `A`.  The
frequencies used in (1.1) are of size `Y log Y`, so a filter may have
`q(0)=1` and exact prime nulls while its actual carrier in (1.2) is
superpolynomially small.  Narrowing the lobe to width `1/H` restores the
high-frequency Laplace overlap but loses `O(1/H)` in endpoint capacity.

Independent two-leg factorization does not remove this distinction.  In
relative Fourier coordinates every complex cross spectrum factors with the
sharp cost

```text
inf_(h_k=conj(ell_k)r_k) ||ell||_2*||r||_2
 =sum_k |h_k|.                                      (1.3)
```

Consequently the correctly normalized problem is exactly the existing
Wiener atomic extremal

```text
E_Y=sup{|L_alpha(q)|:q(u_j)=0, ||h||_1<=1}.          (1.4)
```

The KMT/von-Mangoldt quadrature proves only

```text
E_Y << (log Y)^(-3/10),                             (1.5)
```

an upper bound which retains the power exponent.  No lower bound
`E_Y>=Y^(-kappa)` with `kappa<0.0180304...` is known.  The signed Gram
construction proves algebraic nulling but gives no such lower bound.

The same audit closes the proposed componentwise Selberg and Vaughan
shortcuts.  Any method which bounds the central prime cluster after taking
absolute values meets carrier-scale mass.  Any componentwise fixed-power
estimate for the recompleted Type-I head is already a fixed-strip PNT
estimate.  Only a joint signed all-sector correlation remains.

## 2. Carrier-aligned modulation is centered at `log(n/Y)`

Let the two physical lobes have centers separated by `D=log Y`.  A common
global modulation by `eta` contributes `exp(i eta log n)` to a cross-prime
translate.  But exact alignment with the selected pair forces the relative
lobe counterrotation `exp(-i eta D)`.  The actual multiplier is therefore

```text
exp(i*eta*(log n-D))=exp(i*eta*u_n),                 (2.1)
```

not `exp(i eta log n)`.

This disposes of a tempting false gain.  Fejer averaging over eta appears
to suppress primes by `sinc^2(H log n)`.  Once the selected-positive row is
kept null, its true factor is `sinc^2(H u_n)`.  Prime powers occur
arbitrarily close to `u=0`, and the apparent factor `log Y` has disappeared.

For a finite signed measure supported in `[-B,B]`, normalized by
`phi(0)=1`, Bernstein's elementary estimate is

```text
|phi(u)-1|<=B*||mu||_TV*|u|.                        (2.2)
```

Hence exact nulling at one offset `u` requires

```text
B*||mu||_TV>=1/|u|.                                 (2.3)
```

The prime-in-short-interval bound used elsewhere in the repository gives a
prime with `|u|<<Y^(-19/40)`, so (2.3) rules out narrow signed filters with
`B||mu||_TV=o(Y^(19/40))`.  It does not rule out the full admissible band:
`B` may be much larger than `Y`, and the next theorem shows this is enough.

## 3. Constant-variation signed interpolation

### Theorem 3.1 (separated-node signed nuller)

Let

```text
u_0=0,u_1,...,u_M
```

be distinct real numbers with mutual separation at least `delta`.  If

```text
H*delta >=4*(1+log(M+1)),                           (3.1)
```

there is an absolutely continuous complex measure `mu` on `[H,3H]` such
that

```text
hat(mu)(u_0)=1,
hat(mu)(u_j)=0                  (1<=j<=M),
||mu||_TV<=sqrt(2).                                   (3.2)
```

#### Proof

Use normalized Lebesgue measure `deta/(2H)` on `[H,3H]` and put

```text
e_j(eta)=exp(-i*eta*u_j).
```

Their Gram matrix is

```text
G_(j,k)
 =(1/(2H))*integral_H^(3H) exp(i*eta*(u_j-u_k))deta,
G_(j,j)=1,
|G_(j,k)|<=1/(H*|u_j-u_k|)             (j!=k).      (3.3)
```

After ordering the nodes, separation gives

```text
sum_(k!=j)|G_(j,k)|
 <=[2/(H*delta)]*sum_(m=1)^(M+1)1/m
 <=1/2.                                             (3.4)
```

Thus every eigenvalue of the Hermitian matrix `G` lies in `[1/2,3/2]`.
Set `c=G^(-1)e_0` and

```text
g(eta)=sum_k c_k*e_k(eta),
dmu(eta)=g(eta)deta/(2H).
```

Then `hat(mu)(u_j)=(Gc)_j=(e_0)_j`.  Moreover

```text
integral_H^(3H) |g|^2 deta/(2H)
 =c^*G*c
 =e_0^*G^(-1)e_0
 <=2.
```

Cauchy--Schwarz proves `||mu||_TV<=sqrt(2)`.  QED

### Corollary 3.2 (prime-power nodes fit below the height aperture)

Assume the active integers lie in `[aY,bY]`, for fixed `0<a<b`.  Distinct
integer logarithms satisfy

```text
|log(m/Y)-log(n/Y)|>=c_(a,b)/Y.                     (3.5)
```

The cross center may be perturbed by `O(1/Y)` so its exponential is a
half-integer; then every active integer logarithm is also `c_(a,b)/Y` away
from zero.  Since `M=O(Y)`, Theorem 3.1 applies with

```text
H=C_(a,b)*Y*log Y.                                  (3.6)
```

For `Y=X^d`, fixed `d<1`, one has `H=o(X)`.  In particular (3.6) is legal
at `d=0.66`.

This corollary is a signed interpolation statement only.  It must not be
relabelled a positive spectral moment or a compact carrier theorem.  A full
application must also absorb the `O(1/Y)` center perturbation into the
deterministic divisor construction; no such compact-transfer assertion is
being made here.

## 4. Why `q(0)` is the wrong normalization

In the ideal relative Fourier model write

```text
q(u)=sum_k h_k*exp(i*xi_k*u).                       (4.1)
```

The prime nulls are `q(u_j)=0`.  The theorem above makes `q(0)=1` cheap while
placing all spectral mass at frequencies between `H` and `3H`.  The selected
carrier, however, is the weighted continuous moment

```text
L_alpha(q)
 =integral W_alpha(u)q(u)du
 =sum_k b(xi_k)h_k,

b(xi)=integral W_alpha(u)exp(i*xi*u)du.              (4.2)
```

If `W_alpha` is `C_c^infinity` on a fixed interval, integration by parts
gives, for every integer `A>=0`,

```text
|b(xi)|<=C_A*(1+|xi|)^(-A).                         (4.3)
```

Thus a unit-Wiener filter supported on `|xi|asymp Y log Y` has

```text
|L_alpha(q)|<<_A Y^(-A),                            (4.4)
```

despite possibly having `q(0)=1`.

For a sharp or merely bounded-variation lobe, the tail in (4.3) is only
`O(1/|xi|)`.  That still gives the full loss `O(1/H)` at (3.6).  Shrinking
the physical lobe to width `w=1/H` makes `b(H)` order `w`; the endpoint
evaluation capacity of a unit packet is also `O(w)` in the product
normalization.  Hence narrowing does not turn (3.2) into a carrier theorem.

There is a useful low--high interpretation.  A low-frequency component can
retain order-one Laplace carrier.  Correcting its order-one values at
`M` separated prime nodes by the stable Hilbert interpolation above has the
generic `sqrt(M)` coefficient cost.  After normalization this is the
familiar `M^(-1/2)=Y^(-1/2+o(1))` scale.  This is a construction-level
cost, not a universal lower bound: beating it is exactly the `l^1`
optimization in the next section.

## 5. Independent two-leg factorization returns the atomic extremal

Let `ell_k,r_k` be independently polarized lobe coefficients.  Their cross
spectrum is

```text
h_k=conj(ell_k)*r_k.                                 (5.1)
```

Cauchy--Schwarz gives

```text
sum_k|h_k|<=||ell||_2*||r||_2.                       (5.2)
```

Conversely, choosing

```text
r_k=sqrt(|h_k|),
ell_k=conj(h_k)/sqrt(|h_k|)
```

on the nonzero coordinates gives equality.  This proves (1.3).  Rescaling
the two factors at fixed `h` also gives

```text
inf (||ell||_2^2+||r||_2^2)=2*||h||_1.              (5.3)
```

Therefore arbitrary complex signs are physically available in the
unconstrained polarized two-leg model, but their exact price is the Wiener
norm.  With

```text
(Vh)_j=sum_k h_k*exp(i*xi_k*u_j),
```

the actual optimized carrier is

```text
E_Y
 =sup_(Vh=0,||h||_1<=1)|<b,h>|
 =inf_lambda ||b-V^T lambda||_infinity.             (5.4)
```

This is finite-dimensional `l^1/l^infinity` quotient duality.  It is also
the exact answer to the independent-two-leg question.  Factorization does
not convert the point-normalized filter of Theorem 3.1 into a
Laplace-normalized one; it sends the latter problem to (5.4).

The actual von Mangoldt quadrature is a legal dual choice in (5.4).  The
audited KMT transition estimate yields (1.5).  This upper bound rules out a
uniform constant carrier but is only logarithmic.  To close the present
strip ledger by prime nulling one needs a lower bound, for the deterministic
geometry-compatible space, of the shape

```text
E_Y>=Y^(-kappa+o(1)),
kappa<0.0180303234... .                              (5.5)
```

Neither Theorem 3.1 nor a stable `l^2` inverse proves (5.5).  Endpoint jets,
the two growing Blaschke branches, and compact transfer can only shrink the
feasible set, so (5.5) remains a necessary quantitative adapter.

Complex polarization itself is not a reality obstruction.  If the total
completed real matrix is `A` and `z=x+i y`, then

```text
conj(z)^T A z=x^T A x+y^T A y.                      (5.6)
```

A negative polarized total form therefore descends to a real component.
What has not been obtained is the negative polarized total form with the
carrier in (5.5).

## 6. Selberg and bilinear pruning

The dangerous local exponent can be seen without matrices.  Put

```text
r=Y^(-(1/2-alpha)).                                 (6.1)
```

At `alpha=0.49`, this is `r=Y^-0.01`, and the multiplicative interval
`|log(n/Y)|<=r` has ordinary length `Y^0.99+o(1)`.  The classical
all-interval prime number theorem above exponent `7/12` gives

```text
sum_(|log(n/Y)|<=r) Lambda(n)/sqrt(n)
 =(2+o(1))*r*sqrt(Y)
 =Y^(alpha+o(1)).                                   (6.2)
```

This is exactly the raw carrier exponent.  Consequently a Selberg
majorant/minorant or a triangle inequality which discards the phases in
this central cluster has no fixed-power reserve.  It must keep the signed
candidate-dependent polynomial

```text
sum_(|log(n/Y)|<=r)
 Lambda(n)/sqrt(n)*W(log(n/Y))*exp(-i*gamma*log n).  (6.3)
```

The standard bilinear decompositions do not create oscillation on their
own.  On a rectangular Type-II block,

```text
(dm)^(-i*gamma)=d^(-i*gamma)*m^(-i*gamma),           (6.4)
```

so the phase is rank one.  Componentwise Cauchy--Schwarz loses it.  Exact
recompletion restores the signed Type-I head and all other sectors.  As
proved in the Mertens principal-band audit, a fixed-power bound for the
`d=1` head by itself already implies a fixed zero-free strip.  Therefore a
noncircular bilinear continuation must retain cancellation among all
recompleted sectors before absolute values; its mean projection is the
weighted Mertens carrier.

Equations (6.2)--(6.4) give the narrow obstruction requested here:

```text
coefficientwise Selberg bounds             carrier-scale only;
componentwise Type I                       already strip-strength;
coefficient-blind Type II                  rank-one phase loss;
signed all-sector recombination            open.              (6.5)
```

## 7. Isolated-block and completion sanity checks

Theorem 3.1 uses the actual prime-power nodes, so it correctly has no
content in the isolated completed one-pair model.  More importantly, a
prime-null cross correlation is not by itself the reserve

```text
Q_ar(q_rho)+K_rho.
```

Pole, archimedean, same-leg, compact-transfer, and collateral terms must be
kept in the same total form.  Sub-`log 2` lobes remove the same-leg prime
terms exactly, but they do not factor an arbitrary point-normalized signed
filter with a retained Laplace carrier.  The full completion identity still
returns

```text
Q_ar(q_rho)+K_rho
 =<q_rho,R_other,rho q_rho>.                         (7.1)
```

In the isolated block the right side is zero.  None of the interpolation
identities above changes that fact.

## 8. Research decision

The signed-height escape has been tried to its exact boundary.

1. Bounded-variation signed sample annihilation is feasible inside the
   allowed polynomial ordinate band; a bandwidth/zero-count no-go is false.
2. Exact independent two-leg factorization is also feasible, but its norm is
   precisely the Wiener `l^1` norm.
3. The selected carrier is a Laplace moment, not the value at the centered
   offset.  Enforcing the correct normalization returns exactly the atomic
   extremal (5.4).
4. A stable Hilbert inverse supplies at best the familiar square-root
   construction; it gives no lower bound at the required exponent.
5. Selberg and separated Vaughan estimates lose carrier-scale central mass.

The smallest live theorem in this branch is therefore (5.5), including the
geometry-compatible endpoint and branch constraints, or an equivalent
favorable one-sided estimate for the single completed scalar.  Proving it
would be new arithmetic information; Theorem 3.1 does not supply it.

Primary dependencies:

- `ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md`;
- `ZETA23-BIPARTITE-BLASCHKE-ARITHMETIC-COUPLING-GATE-2026-08-12.md`;
- `ZETA23-CANDIDATE-RELATIVE-FRACTIONAL-ARITHMETIC-EDGE-AUDIT-2026-08-12.md`;
- `ZETA23-MERTENS-TYPEII-PRINCIPAL-BAND-GATE-2026-08-12.md`.
