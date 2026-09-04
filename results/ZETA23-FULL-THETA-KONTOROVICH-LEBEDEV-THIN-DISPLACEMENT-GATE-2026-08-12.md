# Full-theta Kontorovich--Lebedev orbit formula and thin-displacement gate

Status: no fixed zero-free strip is proved.  The target-only displacement
range is much smaller than the full Hermite--Biehler range: for
`a=0.499999`, only `0<y<10^(-6)` must be signed.  The fully recompleted
two-dimensional theta kernel has an exact, absolutely convergent modular
orbit/Kontorovich--Lebedev expansion.  Its elementary orbit densities are
signed, however, and the modular compensation is irreducibly infinite.
Taylor expansion in the tiny displacement fails uniformly at the conductor
scale `y*log|t|asymp 1`.

Date: 2026-08-12.

## 1. A target-only thin-displacement theorem

Write

```text
X(s)=xi(1/2+s),
D_(a,y)(t)=|X(a+y-i*t)|^2-|X(a-y-i*t)|^2.            (1.1)
```

The preceding theta-autocorrelation theorem identifies `D_(a,y)` with the
Fourier transform of the positive full-theta autocorrelation `K_(a,y)`.
For exclusion of zeros, the full range `y>0` is unnecessary.

### Theorem 1.1 (thin target-only detector)

Fix `0<a<1/2`.  If

```text
D_(a,y)(t)>0 for every real t and every 0<y<1/2-a,    (1.2)
```

then every nontrivial zeta zero satisfies

```text
abs(Re(rho)-1/2)<=a.                                 (1.3)
```

#### Proof

Suppose `X(b+i*gamma)=0` with `a<b<1/2`.  Set

```text
y=b-a,       t=-gamma.
```

Then the first term in (1.1) is zero, and hence

```text
D_(a,b-a)(-gamma)=-|X(2a-b+i*gamma)|^2<=0,           (1.4)
```

contradicting (1.2).  If the second value in (1.4) is also a zero, the right
side is zero and strict positivity still gives the contradiction.  Thus
common horizontally shifted zeros, arbitrary multiplicity, and a full
functional-equation quartet require no separate argument.  Reflection gives
the left side of (1.3).  The classical strict critical strip excludes
`b=1/2`.  QED.

In particular, the explicit target

```text
a=0.499999                                             (1.5)
```

requires (1.2) only for

```text
0<y<10^(-6).                                         (1.6)
```

This is strictly weaker than proving that `E_a` is Hermite--Biehler.  It is
nevertheless sufficient for the desired uniform strip.

## 2. The fully recompleted two-dimensional theta object

It is convenient in this section to use the Rodgers--Tao scale

```text
Phi(u)=sum_(n>=1)
 [2*pi^2*n^4*exp(9u)-3*pi*n^2*exp(5u)]
 exp[-pi*n^2*exp(4u)].                               (2.1)
```

Let

```text
theta(x)=sum_(n in Z) exp(-pi*n^2*x),
h(u)=exp(u)*theta(exp(4u)).                           (2.2)
```

The one-dimensional modular relation gives the two exact identities

```text
h(-u)=h(u),
Phi(u)=(1/16)*(d_u^2-1)h(u).                         (2.3)
```

For

```text
u=(p+q)/2,       v=(p-q)/2,
T(p,q)=h(u)h(v)
 =exp(p)theta(exp(2p+2q))theta(exp(2p-2q)),           (2.4)
```

two-dimensional Poisson inversion is simply

```text
T(-p,q)=T(p,q),       T(p,-q)=T(p,q).                (2.5)
```

Put

```text
L=[(d_p+d_q)^2-1][(d_p-d_q)^2-1]
  =d_p^4-2(d_q^2+1)d_p^2+(d_q^2-1)^2.               (2.6)
```

Then the fully recompleted product is

```text
Phi((p+q)/2)Phi((p-q)/2)=(1/256)*L T(p,q).           (2.7)
```

Formula (2.7) retains the zero orbit, both axis orbits, all interior lattice
orbits, and their Poisson duals before differentiation.  The zero and axis
orbits are annihilated exactly by one of the two factors in `L`; the surviving
object is rapidly decreasing in both original variables.  This avoids the
four separately divergent lattice sums obtained by integrating the raw
`+,-,-,+` derivative pieces.

## 3. Exact Kontorovich--Lebedev modular-orbit expansion

Define the Rodgers-scale autocorrelation

```text
calK_(alpha,eta)(q)
 :=integral_R Phi((p+q)/2)Phi((p-q)/2)
      sinh(alpha*p)sinh(eta*p) dp.                   (3.1)
```

Use the Fourier convention

```text
calKhat_(alpha,eta)(t)=integral_R calK(q)exp(-i*t*q)dq.
```

For `k>=1`, put

```text
lambda_t(k)=sum_(d|k)(d^2/k)^(i*t/2),                (3.2)
z_k(p)=2*pi*k*exp(2p),
B_t(z)=(z^2+9)K_(i*t/2)(z)+6z K'_(i*t/2)(z),         (3.3)
```

where `K_nu` is the modified Bessel function.  Pairing divisors `d` and
`k/d` shows that `lambda_t(k)` is real.

### Theorem 3.1 (fully recompleted KL formula)

For fixed real `t` and positive `alpha,eta`,

```text
calKhat_(alpha,eta)(t)
 =1/2 sum_(k>=1) lambda_t(k)
   integral_0^infinity exp(p)sinh(alpha*p)sinh(eta*p)
     *z_k(p)^2*B_t(z_k(p)) dp.                       (3.4)
```

For every fixed set of parameters, the sum of the half-line orbit integrals
in (3.4) is absolutely convergent.

#### Derivation

The interior `(m,n)` lattice term in (2.4) has `q`-transform

```text
(n/m)^(-i*t/2) K_(i*t/2)(2*pi*m*n*exp(2p)).          (3.5)
```

There are four sign choices for nonzero `m,n`.  Grouping by `k=mn` gives
`4*lambda_t(k)`.  On Fourier transforming (2.6), its `p`-operator is

```text
L_t=d_p^4+2(t^2-1)d_p^2+(t^2+1)^2.                  (3.6)
```

The Bessel equation gives the exact raising-operator collapse

```text
L_t[exp(p)K_(i*t/2)(z_k(p))]
 =16 exp(p)z_k(p)^2 B_t(z_k(p)).                     (3.7)
```

Combining the factors `1/256`, `4`, and `16` yields `1/4` on the full
`p`-line.  Equation (2.5) makes the differentiated transform even in `p`,
giving the factor `1/2` and the half-line formula (3.4).  On `p>=0`, one has
`z_k>=2*pi*k`; standard exponential decay of `K_nu(z)` and its derivative
proves absolute convergence.  QED.

The relation to the centered normalization in (1.1) is

```text
D_(a,y)(t)=16*calKhat_(2a,2y)(2t).                   (3.8)
```

Thus (3.4) is a direct spectral formula for the exact target-only detector,
not a model kernel.

## 4. Why (3.4) is not a positive spectral factorization

Both new factors in (3.4) are intrinsically signed.  Already

```text
lambda_t(2)=2*cos((t/2)*log 2),                      (4.1)
```

and the imaginary-order Bessel combination `B_t(z)` changes sign.  This is
not caused by the completion polynomial being omitted: (3.7) is the exact
action of both completion operators.  Standard large-imaginary-order
asymptotics of `K_(i*t/2)(z)` show oscillation in `t` for fixed `z`, and the
same is true after the nonzero differential combination (3.3).

Consequently:

- the smallest interior orbit `k=1` is already a signed KL density;
- the first compensating orbit `k=2` has an additional signed divisor phase;
- pairing `d` with `k/d` makes the coefficient real, not positive;
- two-dimensional Poisson summation makes the orbit series convergent and
  even, but does not make its individual terms nonnegative.

As a normalization check, at centered parameters

```text
a=0.499999, y=0.01, t=1.95,
```

high-precision quadrature of the first modular orbits in (3.4), multiplied
by the factor `16` in (3.8), gives

```text
k=1:  +1.97073981142984821e-4
k=2:  +2.38464235295676853e-7
k=3:  -1.40165092803453330e-9
k=4:  -2.30973513206909456e-12
k=5:  -1.20437127312674817e-14,

sum through k=6: 1.97311041405567821e-4,
direct xi value: 1.97311041405567780e-4.              (4.2)
```

This is a numerical validation of the exact constants in (3.4), not a sign
proof.  It also shows the actual compensation: modular dual orbits alternate
and repair one another.  Absolute values discard precisely this repair.

## 5. The same obstruction in positive-half theta blocks

There is a second fully convergent recompletion which exposes the high-height
mechanism.  Let `Phi_n` be the `n`th summand of (2.1), `A_n=pi*n^2`, and

```text
I_n^+(s)=integral_0^infinity Phi_n(u)exp(su)du.
```

Direct integration and one incomplete-gamma recurrence give

```text
I_n^+(s)
 =(s-1)/8*A_n^(-(1+s)/4)*Gamma((5+s)/4,A_n)
   +(1/2)A_n exp(-A_n).                              (5.1)
```

The boundary term in (5.1) is the explicit modular compensation missing
from the divergent full-line termwise Mellin expansion.  In centered
variables define

```text
C_n(w)=4[I_n^+(2w)+I_n^+(-2w)].                     (5.2)
```

Then

```text
X(w)=sum_(n>=1) C_n(w)                              (5.3)
```

locally uniformly on the plane.  Nevertheless no finite partial sum can
prove the strip.  If `Phi_N=sum_(n<=N)Phi_n` and the first nonzero odd
boundary derivative is `Phi_N^(2r+1)(0)`, repeated integration by parts gives

```text
sum_(n<=N)C_n(w)
 =8*Phi_N^(2r+1)(0)/(2w)^(2r+2)
   +O(|w|^(-2r-4)).                                  (5.4)
```

Such a finite `r` exists for every `N`: otherwise real analyticity would
make `Phi_N` even, whereas as `u->-infinity` it has a nonzero `e^(5u)`
leading term and as `u->+infinity` it has double-exponential decay.

Hence, for every `a,y>0`, its modulus difference is eventually negative:
to justify the sign one retains the structure of the endpoint expansion,
not merely the absolute `O`-term in (5.4).  Repeated integration by parts
in fact gives a full expansion in even inverse powers of `w`, with real
coefficients.  If

```text
m=2r+2,
c_r=8*Phi_N^(2r+1)(0)/2^m,
```

then, uniformly for `x` in a fixed compact interval,

```text
sum_(n<=N)C_n(x-i*t)
 =c_r*(x-i*t)^(-m)[1+d_r*(x-i*t)^(-2)+O(t^(-4))]
```

for a real `d_r` (with the evident interpretation if the next coefficient
vanishes).  Consequently the `d_r` term cancels at the first
`x`-dependent order in the difference, and

```text
|sum_(n<=N)C_n(a+y-i*t)|^2
 -|sum_(n<=N)C_n(a-y-i*t)|^2
 =-4*m*a*y*c_r^2*t^(-2m-2)+O(t^(-2m-4))<0            (5.5)
```

for all sufficiently large `t`.  This supplies the sign conclusion that a
coarse separate use of the remainder in (5.4) would not by itself prove.

For the first derivative specifically,

```text
Phi_n'(0)
 =-A_n(8A_n^2-30A_n+15)exp(-A_n),                   (5.6)

Phi_1'(0)=+0.03949876526774993468...,
Phi_2'(0)=-0.03949868261495415741...,
Phi_3'(0)=-0.00000008265279563810... .               (5.7)
```

The full modular identity is exactly

```text
sum_n Phi_n^(2j+1)(0)=0 for every j>=0.              (5.8)
```

Thus `n=1` is the smallest signed boundary obstruction, `n=2` is its first
near-exact compensator, and successive theta terms cancel successively
higher algebraic remnants.  At centered height `t=46`, `a=0.499999`, and
`y=0.01`, a high-precision scout gives

```text
diagonal n=1:       -1.20346501050605e-14
diagonal n=2:       -1.20347582855054e-14
twice cross (1,2):  +2.40694083907267e-14
combined n<=2:      +1.60893284166920e-25.           (5.9)
```

Later terms continue the cancellation.  Equations (5.4)--(5.8), unlike the
numbers in (5.9), are exact and prove that every finite modular/positive-half
truncation ultimately has the wrong sign.

## 6. Why the tiny `y` interval does not close by Taylor expansion

Put

```text
F(x,t)=|X(x-i*t)|^2.
```

For `0<y<1/2-a`,

```text
D_(a,y)(t)
 =2y F_x(a,t)+(y^3/3)F_xxx(a,t)+O(y^5).             (6.1)
```

Equivalently, on the theta side,

```text
K_(a,y)(q)/y
 =integral p*sinh(a*p)Psi((p+q)/2)Psi((p-q)/2)dp
  +O(y^2)                                            (6.2)
```

with an explicit positive pointwise moment remainder before Fourier
transformation.  An absolute `L1` estimate for that remainder is useless at
large height: the leading Fourier density tends exponentially to zero.

More sharply, Stirling's formula shows that horizontal derivatives of the
completed gamma factor have the scale

```text
F_xxx/F_x =O((log(|t|/(2*pi)))^2)                   (6.3)
```

away from additional small-zeta effects.  Thus the relative cubic error in
(6.1) has the unavoidable parameter

```text
(y*log|t|)^2.                                        (6.4)
```

For every fixed positive `y`, however tiny, (6.4) is order one at heights
`|t|=exp(c/y)` and unbounded beyond them.  Near a zero, logarithmic
derivatives of the zeta factor only worsen the comparison.  A uniform
Taylor proof therefore needs a relative lower bound for `F_x(a,t)`, or an
equivalent zero-free estimate, at exactly the line being proved.

For `a=0.499999`, restricting `y` to `10^(-6)` postpones this loss to an
enormous height but does not remove it.  Finite verification plus an absolute
theta remainder has no closed limiting argument.

## 7. A failed positive-definite interpolation from the safe line

For `0<a<b`, the scalar ratio

```text
sinh(a*p)/sinh(b*p)
```

is positive definite in `p`.  One might try to multiply the safe `b=1/2`
kernel by this ratio and invoke a two-variable Schur product theorem.  That
would require the underlying `(p,q)` kernel to be jointly positive definite.
Its exact two-dimensional Fourier transform is

```text
(1/2)[S_(b+y)(lambda,t)-S_(b-y)(lambda,t)],          (7.1)

S_c(lambda,t)
 =X(c-i(lambda+t))X(c-i(lambda-t))
  +X(-c-i(lambda+t))X(-c-i(lambda-t)).               (7.2)
```

Joint positivity is false even on the safe line.  For example, direct
high-precision evaluation at

```text
b=1/2, y=0.1, lambda=t=5
```

gives (7.1) approximately

```text
-3.78502071665114e-4.                                (7.3)
```

The exact formula (7.1) identifies the obstruction; (7.3) is a numerical
falsifier.  Hence positive definiteness of the hyperbolic-sine ratio cannot
transport the safe-line theorem inward.

## 8. Verdict

The direct spectral-factorization attack produced a genuinely new exact
formula, but not a strip.

1. The proof target for `a=0.499999` is only the thin range
   `0<y<10^(-6)`.
2. The full theta product admits the convergent KL orbit formula (3.4).
3. Its first Bessel density and its first nontrivial divisor coefficient are
   signed; Poisson recompletion gives convergence, not termwise positivity.
4. The exact positive-half formula (5.1) shows how `n=2` begins to compensate
   the wrong-sign `n=1` boundary mode, while (5.4)--(5.8) prove that no finite
   block can finish the cancellation.
5. The thin-`y` Taylor expansion loses uniformity at `y log|t|asymp1` and
   needs the same relative lower bound as the desired strip.

The remaining admissible lemma is now narrower than full
Hermite--Biehler positivity but still genuinely global:

> Prove that the **complete signed sum** in (3.4) is positive for
> `alpha=0.999998`, every real `t`, and `0<eta<2*10^(-6)`.

Any future KL proof must establish domination after summing the oscillatory
`lambda_t(k)B_t(z_k)` blocks.  Positivity of individual modular orbits,
finite theta truncation, safe-line interpolation, and a uniform low-order
Taylor remainder are all ruled out by the identities above.
