# R164 explicit z-plane collective cofactor template

## Status

The finite-channel algebraic problem has an explicit affirmative answer for
`q=2`.

On the simply connected strip

```text
D={z:|Im(z)|<pi},                                        (0.1)
```

there is a holomorphic function

```text
g(z)=z m(z),                                             (0.2)
```

such that `m` is zero-free, `g(1)=1`, and

```text
1-[g(z)-1]^2=z exp(1-z).                                 (0.3)
```

The right side has no zero except the simple zero at `z=0`.  Therefore, for
any fixed positive weights `w_1,...,w_J` with sum one, taking every
`g_j=g` gives the literal multichannel identity

```text
1-sum_j w_j[g_j(z)-1]^2=z exp(1-z).                     (0.4)
```

There is also a genuinely distinct two-channel version on the explicit disc

```text
Omega={z:|z-1/2|<1}.                                     (0.5)
```

For every real `0<|epsilon|<=1/100`, put

```text
phi(z)=z(1-z),
g_+(z)=g(z)exp(epsilon phi(z)),
g_-(z)=g(z)exp(-epsilon phi(z)).                         (0.6)
```

Then `g_+` and `g_-` are distinct, each is `z` times a zero-free
holomorphic function, both equal one at `z=1`, the weights are
`w_+=w_-=1/2`, and

```text
P_epsilon(z)
 =1-1/2{[g_+(z)-1]^2+[g_-(z)-1]^2}
 =z exp(1-z) U_epsilon(z),                               (0.7)
```

where `U_epsilon` is holomorphic and zero-free on `Omega`.  Quantitatively,

```text
sup_(Omega)|U_epsilon-1|<0.064.                          (0.8)
```

Thus the desired collective cofactor can be made zero-free with a fixed
positive weight vector and genuinely different channels.  No polynomial
identity can do this on the whole plane under the same zero-free-multiplier
requirements: polynomial `g_j=z m_j` force every `m_j=1`, returning the
extra root `z=2`.

This settles the finite-dimensional algebraic question, not the zeta
problem.  The template `g` omits the value `2` throughout `D`.  R155 says a
head-deleted zeta quotient retaining a zero cannot omit that value on the
full connected bridge to its right cap.  Hence an actual optional-prime
realization must leave this `z`-domain, lose uniform approximation on the
bridge, or acquire the forced mixed point elsewhere.  R163 can shape the
template locally on filled discs; neither report gives global control of the
composition with zeta or of the boundary winding needed for a fixed strip.

Date: 2026-08-08.

Predecessors:
[`R160-FINITE-COLLECTIVE-CUTOFF-STOKES-HURWITZ-GATE.md`](R160-FINITE-COLLECTIVE-CUTOFF-STOKES-HURWITZ-GATE.md)
and
[`R163-PRIME-BLOCK-LIFT-AND-RANDOM-SIGN-ROUNDING-GATE.md`](R163-PRIME-BLOCK-LIFT-AND-RANDOM-SIGN-ROUNDING-GATE.md).

## 1. The zero set of `1-z exp(1-z)`

Put

```text
P_0(z)=z exp(1-z),       F(z)=1-P_0(z).                  (1.1)
```

### Lemma 1.1

In the strip `D`, the only zero of `F` is `z=1`, and it has order two.

### Proof

Suppose first that

```text
z=x+iy,       0<|y|<pi,       z exp(1-z)=1.              (1.2)
```

Write `z=R exp(i theta)` with the principal argument.  The signs of
`theta` and `y` agree, and both lie strictly between `-pi` and `pi`.
The phase equation in (1.2) is

```text
theta-y=2 pi k.                                          (1.3)
```

The left side lies in `(-pi,pi)`, so `k=0` and `theta=y`.  If `y>0`, then

```text
R=y/sin y,       x=y cot y.                              (1.4)
```

The modulus equation becomes

```text
log(y/sin y)+1-y cot y=0.                                (1.5)
```

Both terms on the left are strictly positive.  Indeed `sin y<y`, while
`y cot y<1` for `0<y<pi/2` by `tan y>y`, and `y cot y<=0` for
`pi/2<=y<pi`.  The case `y<0` is identical by evenness.  Thus no nonreal
solution of (1.2) lies in `D`.

If `y=0`, a solution must have `x>0`, and

```text
log x+1-x=0.                                             (1.6)
```

The strict concavity inequality `log x<=x-1` gives `x=1`.  Finally, with
`z=1+w`,

```text
log P_0(1+w)=log(1+w)-w=-w^2/2+O(w^3),                  (1.7)
```

so `1-P_0(1+w)=w^2/2+O(w^3)`.  The zero has order two.
QED.

## 2. Construction of the zero-free multiplier

The quotient

```text
H(z)=[1-z exp(1-z)]/(1-z)^2                             (2.1)
```

extends holomorphically across `z=1`, with `H(1)=1/2`.  By Lemma 1.1 it is
zero-free on the simply connected strip `D`.  Choose the holomorphic
logarithm of `H` normalized by

```text
Log H(0)=0                                               (2.2)
```

and define

```text
r(z)=(1-z)exp([Log H(z)]/2).                             (2.3)
```

Then

```text
r(0)=1,       r(z)^2=1-P_0(z).                          (2.4)
```

Set

```text
g(z)=1-r(z).                                             (2.5)
```

Equations (2.4)--(2.5) prove (0.3), and `r(1)=0` gives `g(1)=1`.

It remains to verify the precise divisor requirement in (0.2).  The
identity

```text
g(z)=[1-r(z)^2]/[1+r(z)]
    =z exp(1-z)/[1+r(z)]                                (2.6)
```

is valid throughout `D`.  Indeed `1+r` cannot vanish: if `r(z)=-1`, then
`P_0(z)=0`, hence `z=0`, but `r(0)=1`.  Therefore

```text
m(z)=exp(1-z)/[1+r(z)]                                  (2.7)
```

is holomorphic and zero-free on `D`, with `m(0)=e/2`.  This proves all
claims in (0.2)--(0.4).

The construction has elementary growth.  For `z=x+iy` in `D`,

```text
|P_0(z)|=|z|exp(1-x),
|g(z)|<=1+[1+|z|exp(1-x)]^(1/2).                         (2.8)
```

Thus the template has at most half-exponential growth toward the left edge
of the horizontal strip and is bounded on every right half-strip.  It also
omits `2`: if `g(z)=2`, then `r(z)=-1`, which was just ruled out.

## 3. Genuinely distinct positive channels

Work on the closure of the disc (0.5).  The elementary bounds

```text
1/2<=|z|<=3/2,       -1/2<=Re(z)<=3/2                   (3.1)
```

hold on its boundary in the directions needed below.  In particular,

```text
min_(partial Omega)|P_0(z)|
 >=(1/2)exp(-1/2)>0.303.                                (3.2)
```

On the whole closed disc,

```text
|P_0(z)|<1.5 exp(1.5)<6.73,
|r(z)|<sqrt(7.73)<2.79,
|g(z)|<3.79<4,
|phi(z)|<=9/4.                                           (3.3)
```

Put `u=epsilon phi`.  Direct expansion of (0.7) gives

```text
P_epsilon
 =2g cosh u-g^2 cosh(2u),                               (3.4)

P_epsilon-P_0
 =2g(cosh u-1)-g^2(cosh(2u)-1).                         (3.5)
```

For `|epsilon|<=1/100`, (3.3) gives `|u|<=0.0225`.  The power series for
`cosh` yields

```text
|cosh u-1|<=0.513|u|^2,
|cosh(2u)-1|<=2.103|u|^2.                               (3.6)
```

Consequently, on `partial Omega`,

```text
|P_epsilon-P_0|
 <[2(4)(0.513)+16(2.103)](0.0225)^2
 <0.020.                                                 (3.7)
```

The quotient

```text
E_epsilon=(P_epsilon-P_0)/P_0                           (3.8)
```

extends holomorphically across `z=0`: since `g=O(z)` and
`u=O(z)`, (3.5) is `O(z^3)`, whereas `P_0` has a simple zero.  Equations
(3.2) and (3.7), followed by the maximum-modulus principle, give

```text
sup_Omega |E_epsilon|<0.020/0.303<0.064.                 (3.9)
```

Taking `U_epsilon=1+E_epsilon` proves (0.7)--(0.8), including zero-freeness.
Finally,

```text
g_(+/-)=z [m(z)exp(+/- epsilon phi(z))]                  (3.10)
```

have zero-free bracketed factors, and `phi(1)=0` gives `g_+-(1)=1`.
They are distinct when `epsilon!=0`.  This completes the two-channel
construction.

## 4. Why polynomial and rational shortcuts fail globally

Suppose every `g_j` is a polynomial on the whole plane and

```text
g_j(z)=z m_j(z),       m_j zero-free on C,       g_j(1)=1. (4.1)
```

Then each polynomial `m_j` is a nonzero constant.  The normalization forces
`m_j=1`, hence every `g_j=z`.  For positive weights summing to one and
`q=2`,

```text
1-sum_j w_j(g_j-1)^2
 =1-(z-1)^2=z(2-z),                                     (4.2)
```

which has the forbidden second zero `z=2`.  The same conclusion holds for
rational `m_j` which are holomorphic and zero-free on the Riemann sphere:
they are constant.  Therefore a global polynomial/Waring identity cannot
solve the stated problem; the strip-holomorphic square root or comparable
transcendental structure is essential.

There is also a necessary jet condition at the normalization point.  For
general `q>=2`, every holomorphic channel with `g_j(1)=1` gives

```text
P(1)=1,       P^(k)(1)=0       (1<=k<q).                 (4.3)
```

For `q=2`, the zero-free entire model `P_0=z exp(1-z)` is the simplest
function satisfying this flatness: `P_0(1)=1` and `P_0'(1)=0`.  Its double
contact makes the square root in Section 2 holomorphic at `z=1`.

## 5. What this means for the optional-prime program

Algebraically, the collective-cofactor target is feasible.  It is possible
to have simultaneously

```text
common simple zero at z=0,
right-cap normalization g_j(1)=1,
zero-free individual multipliers g_j/z,
positive fixed weights,
no collective zero except z=0.                           (5.1)
```

The obstruction is now the global realization, not finite-dimensional
Waring geometry.  The base template omits both `0` away from the common
zero and `2` everywhere on `D`.  If one could realize it uniformly as a
head-deleted zeta quotient on the entire connected bridge used in R155,
that quotient would omit the two forbidden values and contradict normality.
Accordingly at least one of the following must occur in an arithmetic lift:

1. the zeta image exits the strip `D` or the chosen compact `Omega`;
2. the optional-prime approximation loses control between the target disc
   and the right cap;
3. an actual channel acquires the forced `2`-point outside the locally
   controlled region; or
4. the collective lower bound fails on the intervening boundary.

R163 proves local analytic shaping on filled conjugate discs and is
compatible with the distinct construction of Section 3.  It does not give
the bridge-wide composition control needed to rule out items 1--4.  Thus
R164 removes the proposed local algebraic obstruction but leaves the global
mixed-point/monodromy theorem as the next decisive gate.
