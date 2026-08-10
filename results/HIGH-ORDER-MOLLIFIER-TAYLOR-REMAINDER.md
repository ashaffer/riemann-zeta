# Exact Taylor-remainder completion of the high-order Mellin carrier

Status: **exact principal-pole residue identity proved and regression-tested;
its proportional-order large-deviation ledger is derived.  This does not prove
a zero-free strip or RH.**

Date: 2026-08-09.

This note completes the first item in Section 8 of
[`HIGH-ORDER-MOLLIFIER-SHIFT-AUDIT.md`](HIGH-ORDER-MOLLIFIER-SHIFT-AUDIT.md).
The central residue polynomial is not merely an unspecified possible
cancellation.  In the principal simple-pole model it combines with the target
residue into one exact exponential Taylor remainder.

## 1. Principal local model

Write

```text
z=w-1,
L=log Y,
z_0=w_rho-1.
```

After multiplying the high-order Mellin transform by the unchanged
first-order auxiliary kernel, the singular part has the form

```text
exp(L z)/[z^(k-1)(z-z_0)].                               (1.1)
```

Analytic prefactors from the full Bettin--Gonek kernel have been frozen at
this stage.  Formula (1.1) isolates the interaction of the target pole
`z=z_0` with the new central pole `z=0`.

The target residue is

```text
T_k(L,z_0)=exp(L z_0)/z_0^(k-1).                         (1.2)
```

For `k>1`, expansion

```text
1/(z-z_0)=-sum_(m>=0) z^m/z_0^(m+1)                    (1.3)
```

shows that the complete residue at `z=0` is

```text
C_k(L,z_0)
 =-sum_(n=0)^(k-2) L^n/[n! z_0^(k-1-n)].                (1.4)
```

For `k=1`, the sum is empty and there is no central pole.

## 2. Exact completion identity

Adding (1.2) and (1.4) gives

```text
T_k(L,z_0)+C_k(L,z_0)
 =[exp(L z_0)-E_(k-2)(L z_0)]/z_0^(k-1),                (2.1)
```

where

```text
E_m(u)=sum_(n=0)^m u^n/n!,
E_(-1)=0.                                                (2.2)
```

Thus the completed carrier is the remainder after truncating the exponential
series at exactly the order forced by the central Mellin pole.

This is a finite algebraic identity.  It uses no asymptotic estimate, no
zero-free region, and no hypothesis about zeta zeros beyond the local
simple-pole coordinate in (1.1).

Equivalently, the residue polynomials have generating function

```text
sum_(q>=0) [-C_(q+2)(L,z_0)] u^q
 =exp(Lu)/(z_0-u),                                      (2.3)
```

as a formal power series at `u=0`, after matching coefficients with the
normalization in (1.4).

## 3. Positive-real specialization and Poisson transition

Let

```text
z_0=delta>0.
```

Dividing the completed residue by the uncompleted target residue gives

```text
S_(k,L)(delta)
 =1-exp(-delta L)E_(k-2)(delta L).                       (3.1)
```

This is exactly

```text
P{Poisson(delta L)>=k-1}.                               (3.2)
```

Consequently, for

```text
k=alpha L+O(1),
```

there are three regimes.

### 3.1 `delta<alpha`

The truncation point lies above the Poisson mean.  The survival fraction is
exponentially small:

```text
S_(k,L)(delta)
 =exp[-L Phi(delta,alpha)+o(L)],                         (3.3)
```

where

```text
Phi(delta,alpha)
 =delta+alpha[log(alpha/delta)-1]
 >=0.                                                    (3.4)
```

The uncompleted target residue carries the opposite exponential factor
`exp[L Phi+o(L)]`.  Their product therefore has no positive extra exponent.
The central polynomial repays the whole apparent gain.

### 3.2 `delta=alpha`

The cutoff is at the mean.  The survival fraction is of constant order
(asymptotically one half under the usual integer normalization), while
`Phi(alpha,alpha)=0`.  Again there is no positive extra exponent.

### 3.3 `delta>alpha`

The truncation point lies below the mean, so

```text
S_(k,L)(delta)->1.                                      (3.5)
```

The central polynomial no longer cancels the target at exponential scale,
and the naive rate `Phi(delta,alpha)` survives in the principal model.

The resulting completed principal-pole exponent is therefore

```text
Phi_completed(delta,alpha)
 =0                         if delta<=alpha,
 =Phi(delta,alpha)          if delta>alpha.              (3.6)
```

Equation (3.6) is an exponent ledger for the principal local model, not yet a
complete high-order zeta criterion.  The full rational prefactor and its
high derivatives still require uniform control when `k` grows with `L`.

## 4. Resolution of the absolute-convergence paradox

When `alpha>1/2`, the high-order mollifier coefficients are dominated by
`d^(-alpha)`, so the mollifier is uniformly absolutely bounded on the
critical line.  A naive target-only calculation then appears to combine with
the classical zeta second moment to prove RH.

But every nontrivial zero has

```text
0<delta<1/2<alpha.
```

Hence (3.6) places every such zero in the fully cancelled regime.  The easy
mean-square bound and the completed Mellin detector are consistent: the
central Taylor polynomial removes the apparent exponential target gain.

This supplies a precise rather than merely qualitative explanation of why a
large proportional taper cannot yield a trivial RH proof.

## 5. Interaction with the effective-length no-go

For `0<alpha<1/2`, the mollifier-alone effective-support exponent is

```text
chi(alpha)
 =1-2alpha+2alpha log(2alpha).                           (5.1)
```

At the outer displacement `delta=1/2`, the principal carrier is in the
surviving regime and satisfies

```text
2 Phi(1/2,alpha)=chi(alpha).                             (5.2)
```

Therefore the natural-scale mollifier condition

```text
theta chi(alpha)<=1                                     (5.3)
```

implies

```text
2 theta Phi_completed(delta,alpha)<=1
```

throughout `alpha<=delta<=1/2`.  For `delta<alpha`, the completed exponent is
already zero by (3.6).

Thus the exact Taylor completion strengthens, rather than weakens, the
high-order no-go:

> the elementary mollifier-only mean-value range has no strict detector
> surplus anywhere in the nontrivial displacement interval.

This conclusion concerns the generic proportional-order damping mechanism.
It does not rule out a new arithmetic estimate for the fully completed
`zeta times mollifier` object.

## 6. Full analytic prefactor

In the actual contour product, (1.1) is multiplied by a rational function
`A_t(z)` analytic near `z=0` and nonzero at the target in the generic case.
The central residue becomes

```text
k! Y sum_(m+n=k-2)
  A_t^(m)(0)/m! * L^n/n!.                               (6.1)
```

The exact completed expression is a Hermite/Taylor remainder involving both
`A_t` and the exponential.  For fixed order, this causes no difficulty.  For
`k proportional to L`, a complete theorem must control derivatives of
`A_t` uniformly up to order `k` and retain every nearby singularity.

The principal formula (2.1) captures the closest target-pole interaction but
does not by itself justify replacing the full prefactor by a constant at
growing order.  That replacement is the next analytic seam to audit.

## 7. Consequences for the research program

The high-order route is now classified as follows.

- **Coefficient damping:** genuine and exact.
- **Naively isolated entropy carrier:** algebraically correct but incomplete.
- **Central pole:** unavoidable for the unchanged first-order kernel.
- **Principal target-plus-center completion:** exact Taylor remainder.
- **Generic zero-free-strip shortcut:** refuted.
- **Arithmetic completed-moment mechanism:** still open.

A viable continuation would have to exploit an arithmetic identity in the
full prefactor or in the Möbius-weighted moment.  Merely increasing the taper
order, subtracting the central polynomial, or applying a generic finite
difference does not create exponent surplus.

## 8. Reproducibility

The exact finite identities and transition diagnostics are implemented in

```text
src/high_order_mellin_residue.py
src/test_high_order_mellin_residue.py.
```

The tests verify:

1. target plus central residue equals the Taylor-remainder formula for real
   and complex pole offsets;
2. the central polynomial coefficients have the claimed degree and
   normalization;
3. the real survival factor lies in `[0,1]`;
4. the finite transition occurs near `delta=alpha`;
5. `alpha>1/2` suppresses every displacement below `1/2` in the principal
   model.

No finite test is interpreted as an asymptotic theorem or a zero-free
region.
