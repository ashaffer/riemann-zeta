# Functional-equation pairing does not remove the sigma-kernel sign debt

Status: the zero orbit under the functional equation and conjugation is
inserted exactly into the R129 sigma-difference kernel.  The prime-side
coefficients, paired and quartet zero kernels, vertical masses, and
target-to-pole ratios are computed.  The result is a sharp dichotomy.

```text
exact leading-Gamma cancellation + nonzero paired positive-real kernel    IMPOSSIBLE
functional pair or full quartet removes the negative lobes                NO
Stechkin pairing gives a positive-real zero kernel                         YES
Stechkin pairing has a nonzero 1/z tail and a log(T) Gamma term            NECESSARILY
fixed-gap target can still beat the pole at principal-part level          YES
fixed zero-free strip from this mechanism                                 NOT PROVED
```

The obstruction is not a numerical failure of the usual Stechkin
parameters.  It is a vertical-mass theorem: a nonzero paired positive-real
resolvent kernel has positive vertical mass, while exact cancellation of
the leading Gamma term sets exactly that mass to zero.

Date: 2026-08-08.

Predecessor:

* [`R129-SIGMA-DIFFERENCE-LOGDERIVATIVE-GATE.md`](R129-SIGMA-DIFFERENCE-LOGDERIVATIVE-GATE.md).

## 1. The largest natural family and its prime coefficients

Put

```text
D(s)=-zeta'(s)/zeta(s),

K_(m,h)(z)=sum_(j=0)^m (-1)^j binom(m,j)/(z+jh)
           =integral_0^infinity e^(-zu)(1-e^(-hu))^m du,        (1.1)
```

where `m>=0`, `h>0`, and `K_(0,h)(z)=1/z`.  Add a Stechkin-style
horizontal comparison, with

```text
d=sigma_1-sigma>=0,
H_(m,h;kappa,d)(z)=K_(m,h)(z)-kappa K_(m,h)(z+d).               (1.2)
```

For `Re(s)>1`, absolute convergence gives the exact identity

```text
Delta_(m,h)D(s)-kappa Delta_(m,h)D(s+d)
 =sum_(n>=2) Lambda(n)n^(-s)
    (1-n^(-h))^m(1-kappa n^(-d)).                              (1.3)
```

Thus all prime coefficients are nonnegative for

```text
0<=kappa<=2^d.                                                  (1.4)
```

The continuous-positive range `0<=kappa<=1`, which includes Stechkin's
choice and every positive-real candidate below, has the more useful
Laplace representation

```text
H(z)=integral_0^infinity e^(-zu)W(u)du,
W(u)=(1-e^(-hu))^m(1-kappa e^(-du))>=0.                        (1.5)
```

Moreover, `W` is increasing.  Consequently `H(x)>0` for every `x>0`
unless the operator is identically zero.

There is no lost no-debt candidate outside this range.  If `m=0` and
`kappa>1`, the vertical mass computed below is negative, so paired
positivity is impossible.  If `kappa<0`, the second resolvent is added
rather than subtracted and the `1/z` coefficient is at least one, making
the Gamma debt larger.  For `m>=1` the mass is zero for every real
`kappa`, and Theorem 3.1 applies directly.

Let `C` be the sum of the resolvent coefficients in (1.2).  Equivalently,
`C=W(0)`.  Then

```text
C=(1-kappa)                         if m=0,
C=0                                 if m>=1,                    (1.6)

H(z)=C/z+O(z^(-2))                  if m=0,
H(z)=O(z^(-m-1))                    if m>=1.                    (1.7)
```

For horizontal shifts which are fixed, or more generally `o(T)`, the
archimedean part of the corresponding logarithmic derivative is

```text
(C/2)log T+O(1).                                                (1.8)
```

Hence the R129 finite differences (`m>=1`) cancel the leading Gamma term
exactly.  In order zero, the affine comparison cancels it exactly only at
`kappa=1`.

## 2. The functional pair and the full quartet

Let `rho=beta+i gamma`, and write

```text
sigma=1+r,
a=sigma-beta,
b=sigma-(1-beta),
a+b=2sigma-1=1+2r=:S.                                         (2.1)
```

The two zeros at ordinate `gamma` are `beta+i gamma` and
`1-beta+i gamma=1-conjugate(rho)`.  Their paired real kernel at vertical
offset `y=t-gamma` is

```text
G_(beta)(y)=Re H(a+iy)+Re H(b+iy).                              (2.2)
```

The complete orbit is

```text
{beta+i gamma, 1-beta+i gamma,
  beta-i gamma, 1-beta-i gamma}.                               (2.3)
```

At an evaluation height `t=T`, its exact quartet contribution is

```text
Q_(beta,gamma;T)
 =G_(beta)(T-gamma)+G_(beta)(T+gamma).                          (2.4)
```

For a target orbit with `gamma=T` and `beta=1-epsilon`, this becomes

```text
Q_target
 =H(r+epsilon)+H(r+1-epsilon)
  +Re H(r+epsilon+2iT)+Re H(r+1-epsilon+2iT).                   (2.5)
```

The first two terms are positive in the range (1.5).  In the
Gamma-cancelled branch the last two tend to zero whenever the horizontal
kernel scale is `o(T)`.  Thus functional reflection supplies a real extra
target term.  The issue is the sign of the same kernel away from the
target ordinate.

## 3. Vertical-mass theorem

### Theorem 3.1 -- pairing and Gamma cancellation are incompatible

For every real `x>0`,

```text
integral_(-infinity)^infinity Re H(x+iy)dy=pi C.                (3.1)
```

Consequently,

```text
integral G_(beta)(y)dy=2pi C,                                  (3.2)
integral [G_(beta)(y)+G_(beta)(2T-y)]dy=4pi C.                  (3.3)
```

If either the functional-pair kernel or the quartet kernel is nonnegative
for every vertical offset and is not identically zero, then `C>0`.
Equivalently, it has a nonzero positive `1/z` tail and pays a leading
archimedean cost `(C/2)log T`.

In particular, if the leading Gamma term is cancelled exactly (`C=0`),
then neither the pair nor the quartet can be nonnegative everywhere.  This
holds for every `m,h,r,kappa,d`; conjugation and functional reflection do
not neutralize the R129 negative lobes.

#### Proof

Expand `H` as its finite real linear combination of resolvents.  Since

```text
integral_(-infinity)^infinity
  (x+c)/[(x+c)^2+y^2]dy=pi,                                    (3.4)
```

(3.1) is `pi` times the sum of the coefficients.  Translation and the
change of variable `y -> 2T-y` give (3.2)--(3.3).  A continuous
nonnegative, nonzero function has positive integral.  Formula (1.7) then
identifies this positive mass with a positive `1/z` coefficient, and the
standard digamma asymptotic gives (1.8).  QED.

This is also the elementary rational version of the Herglotz obstruction:
a positive-real boundary kernel represents a positive measure.  Deleting
its total measure while retaining a nonzero value is impossible.

For the exact-cancellation candidates the contradiction can be read off
immediately:

```text
m>=1:       C=0 for every kappa;
m=0:        C=0 exactly when kappa=1.                           (3.5)
```

At `y=0`, (1.5) makes `G_beta(0)>0`, so a negative lobe must occur.

## 4. The affine kernel and the sharp tail condition

The order-zero affine kernel is

```text
H(z)=1/z-kappa/(z+d).                                          (4.1)
```

Writing `p_x(y)=x/(x^2+y^2)`, its functional pair is

```text
G_beta(y)
 =p_a(y)+p_b(y)-kappa[p_(a+d)(y)+p_(b+d)(y)].                  (4.2)
```

Since `a+b=S`, expansion at vertical infinity gives

```text
G_beta(y)
 ={S-kappa(S+2d)}/y^2+O(y^(-4)).                              (4.3)
```

Therefore a necessary condition for paired positivity is

```text
kappa<=S/(S+2d),
1-kappa>=2d/(S+2d).                                            (4.4)
```

This is sharp at the level of the vertical tail.  In particular, the
Gamma-cancelling choice `kappa=1` has a negative tail `-2d/y^2` for every
`d>0`; at `d=0` the whole kernel is zero.

The classical Stechkin choice demonstrates the other side of the
dichotomy.  Put

```text
sigma_1=(1+sqrt(1+4sigma^2))/2,
kappa=1/sqrt(5).                                                (4.5)
```

Stechkin's lemma says that (4.2) is nonnegative for every zero in
`0<beta<1` and every `y`.  This is precisely the standard functional-pair
device; see Stechkin's original paper and, for the displayed modern
normalization, Lemma 6.2 of
[Ahn--Kwon](https://www.numdam.org/item/10.5802/aif.3274.pdf).
It succeeds because

```text
C=1-1/sqrt(5)=0.552786...>0.                                  (4.6)
```

The corresponding Gamma coefficient is

```text
(1/2)(1-1/sqrt(5))log T.                                       (4.7)
```

Thus Stechkin pairing is not a counterexample to Theorem 3.1; it is the
canonical example showing that positive pairing becomes possible exactly
after restoring a positive mass and a logarithmic archimedean term.

Allowing `d=d(T)` does not evade this conclusion.  Paired positivity still
forces (4.4).  If `d -> d_0>0` while `d=o(T)`, cancellation of the two
digamma logarithms would require `kappa ->1`, contradicting (4.4).  If
`d->0`, the required Gamma-cancelling ratio differs from `1` by
`o(d)`, whereas (4.4) requires `1-kappa>=2d/S+O(d^2)`.  If `d->infinity`,
(4.4) gives `kappa=O(1/d)`, too small to cancel either `log T` or
`log d` (indeed `log d/d=o(log T+log d)`).  Horizontal movement of
`sigma_1` therefore cannot hide the mass in a remote Gamma factor.

## 5. Exact target-to-pole ratios

There are two useful ledgers.

First, if one only groups the zero terms in the R129 zeta explicit formula,
the pole at `1` has main response `H(r)`.  The same-height target pair has
response

```text
T_pair=H(r+epsilon)+H(r+1-epsilon),
R_zeta=T_pair/H(r).                                            (5.1)
```

Second, the fully functional-equation-symmetric explicit formula pairs the
poles at `0` and `1`, just as it pairs the zeros.  Its pole response is

```text
P_pair=H(r)+H(r+1),
R_completed=T_pair/P_pair.                                     (5.2)
```

The second is the appropriate ledger when termwise Stechkin positivity is
used.  The first is the optimistic ledger used in R129.  The obstruction
works in either one.

For the entire continuous-positive family (1.5), both ratios admit sharp
parameter-free upper bounds.  For `0<epsilon<=1/2`,

```text
R_zeta
 <=r/(r+epsilon)+r/(r+1-epsilon),                              (5.3)

R_completed
 <=r(r+1)/[r(r+1)+epsilon(1-epsilon)].                         (5.4)
```

#### Proof

With respect to the exponential probability measure of rate `r`, `W(u)`
is increasing while `e^(-cu)` is decreasing.  Negative covariance gives

```text
H(r+c)/H(r)<=r/(r+c),                                          (5.5)
```

which proves (5.3).  For (5.4), divide the numerator and denominator
inside the Laplace integral by `1+e^(-u)`.  The remaining multiplier is

```text
g_epsilon(u)
 =[e^(-epsilon u)+e^(-(1-epsilon)u)]/[1+e^(-u)]
 =cosh((1/2-epsilon)u)/cosh(u/2).                              (5.6)
```

It is decreasing.  A second negative-covariance inequality removes the
increasing weight `W`.  Direct integration with `W=1` gives (5.4).  QED.

The bounds are optimal over `m,h,kappa,d`: take `kappa=0`, keep `m` fixed,
and let `h->infinity`.  Then

```text
K_(m,h)(x)->1/x,                                                (5.7)
```

so equality is approached in (5.3)--(5.4).  One may take, for example,
`h=T^alpha`, `0<alpha<1`, preserving the R129 high-ordinate Gamma
cancellation.  Adding a positive Stechkin subtraction (`kappa>0`) only
tilts the Laplace weight toward larger `u` and lowers target retention.

A nonnegative trigonometric polynomial can have first Fourier ratio
arbitrarily close to `a_1/a_0=2`.  Thus the optimistic target-over-pole
condition is `R>1/2`.  Equations (5.3)--(5.4) show respectively that it
requires

```text
3r^2+r>epsilon(1-epsilon)                    (zeta-pole ledger), (5.8)
r(r+1)>epsilon(1-epsilon)                    (completed ledger). (5.9)
```

Both windows are nonempty for every fixed `epsilon>0`.  Hence this route
does not fail because reflection destroys the principal target reserve.
For example, with `epsilon=r=0.1`, the classical parameters (4.5) give

```text
R_zeta=0.55170...,
R_completed=0.51604....                                        (5.10)
```

The target beats one half in both ledgers, but the Gamma coefficient
(4.7) remains.

## 6. A fixed-gap lower bound for the unavoidable Gamma debt

The mass obstruction can be quantified without assuming the special
Stechkin values.  Suppose the order-zero affine pair (4.2) is nonnegative.
Put

```text
C=1-kappa,
q=r(r+1),
S=1+2r=sqrt(1+4q).                                             (6.1)
```

The algebraic identity

```text
H(x)=C/x+kappa d/[x(x+d)]                                     (6.2)
```

and the tail condition `kappa d<=CS/2` imply

```text
P_pair=H(r)+H(r+1)
 <=C S^3/(2q^2).                                                (6.3)
```

Indeed,

```text
1/r+1/(r+1)=S/q,
1/r^2+1/(r+1)^2=(2q+1)/q^2,                                   (6.4)
```

and replacing `x(x+d)` by `x^2` in (6.2) gives (6.3).  Therefore

```text
[(C/2)log T]/P_pair
 >=[q^2/S^3]log T.                                             (6.5)
```

If the target has enough completed-pole reserve to beat one half, (5.9)
forces `q>epsilon(1-epsilon)`.  Since
`q^2/(1+4q)^(3/2)` is increasing,

```text
[(C/2)log T]/P_pair
 > {epsilon^2(1-epsilon)^2
    /[1+4epsilon(1-epsilon)]^(3/2)} log T.                      (6.6)
```

For every fixed gap `epsilon>0`, this normalized archimedean cost tends to
infinity.  The lower bound is only a necessary-tail bound, not a claim of
the optimal moving zero-free region; classical Stechkin positivity pays
an even larger cost, of order `epsilon log T` when `r` is of order
`epsilon`.  Formula (6.6) is enough for the fixed-strip question: shrinking
the `1/z` coefficient cannot make the log debt negligible while retaining
both global paired positivity and a fixed-gap target reserve.

For completeness, in the optimistic one-pole ledger the same argument
gives

```text
C/H(r)>=2r^2/(1+4r),                                           (6.7)
```

and (5.8) again makes the normalized Gamma debt diverge for fixed
`epsilon`.

## 7. Verdict

Functional-equation symmetry helps the target but not the sign problem.
It adds the reflected zero at the target ordinate, and the best possible
principal target ratios (5.3)--(5.4) genuinely exceed one half in a
fixed-gap parameter window.  However:

1. every R129 finite-difference kernel has zero vertical mass;
2. pairing `rho` with `1-conjugate(rho)` doubles that zero mass rather than
   changing it;
3. adding conjugates doubles it again;
4. a nonzero nonnegative pair or quartet must instead have positive mass;
5. that mass is exactly a positive `1/z` coefficient and produces a
   `log T` Gamma term;
6. the affine tail condition and target reserve make that term
   non-negligible by the fixed-gap bound (6.6).

Thus there is no choice of `m,h,r,kappa,sigma_1` in this family which has
all three desired properties:

```text
nonnegative prime coefficients,
nonnegative functional-pair (or quartet) zero kernel,
zero leading archimedean log(T) coefficient.                    (7.1)
```

This closes the proposed automatic functional-pair/Stechkin repair of
R129.  It proves neither that a fixed zero-free strip exists nor that one
does not exist.  A continuation would again have to estimate a signed,
target-conditioned zero correlation; symmetry alone cannot turn it into a
positive measure.
