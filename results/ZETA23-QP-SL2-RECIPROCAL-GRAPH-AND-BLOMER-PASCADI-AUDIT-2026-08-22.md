# QP high-completion tail: the `SL_2` reciprocal graph and Blomer--Pascadi audit

**Date:** 2026-08-22  
**Verdict:** the reciprocal carrier does not leave a genuinely curved
incidence problem after a common row is fixed.  In exact unimodular
coordinates the second reciprocal carrier is an affine dilation of the
first, up to the original `O(D)` determinant defect.  Thus a Huxley or
determinant-method argument based only on reciprocal curvature cannot sum
the scattered high partners.

For a fixed residual-numerator layer, additive completion really does give
the Blomer--Pascadi kernel `S(a m,n;c)`.  Its arguments, however, are the
additive Fourier variables of the physical carrier masks.  Those masks may
be point masses and consequently have full Fourier support.  Moreover, at
`N=D=q^(16/33)` the dominant Blomer--Pascadi saving is only

```text
q^(-19/1056).
```

Even the unrealistically favorable product of four independent such gains
is `q^(-19/264)`, smaller than the missing four-cycle gain
`q^(-4/33)=q^(-32/264)`.  The numerical deficit is `q^(13/264)`, before
paying any Fourier-block or varying-layer loss.  No uniform high-completion
tail is proved by this route.

---

## 1. Exact residual graph

Fix an anchor color pair

```text
gamma=(c,d),                 gcd(c,d)=1,
```

and choose `(u,v)` with

```text
d*v-c*u=1.
```

Put `g=(d,c)` and `s=(u,v)`.  Every anchor row and every partner color pair
have unique expansions

```text
x(e)=(a,A)=m(e)*g-e*s,
g'(k)=(d',c')=n(k)*g-k*s,                          (1.1)
```

where

```text
e=a*c-A*d,                 k=c*d'-c'*d.
```

The second row defect is exactly

```text
f=a*c'-A*d'=e*n(k)-m(e)*k.                         (1.2)
```

This preserves the actual shell and prime-power masks pointwise; no box
completion has been made.

There is a useful centered form.  Define

```text
tau=u/d,
alpha_e=a/d=m(e)-tau*e,
beta_k=d'/d=n(k)-tau*k,
gamma_k=c'/c=n(k)-(v/c)*k.
```

Then, exactly,

```text
f=e*beta_k-k*alpha_e,
gamma_k=beta_k-k/(c*d).                            (1.3)
```

Thus the large common linear part `tau` cancels.  The surviving problem is
a determinant graph between the two shell-rounding intercepts `alpha_e`
and `beta_k`.

## 2. Reciprocal curvature cancels exactly

Let `b=b(e)` be the anchor carrier and `B=B(e,k)` the carrier for the
partner.  Write

```text
r =8*a*c*b-q^3,             r'=8*a*c'*B-q^3,
|r|+|r'|<<q*D.
```

With `Lambda=q^3/(8*c*d)`, (1.3) gives

```text
b=Lambda/alpha_e+O(D/q),
B=Lambda/(alpha_e*gamma_k)+O(D/q).                 (2.1)
```

Consequently

```text
B=(c/c')*b+O(D/q).                                 (2.2)
```

This is not just a Taylor approximation.  Direct subtraction of the two
product residuals gives the exact integral defect

```text
ell_1=c'*B-c*b=(r'-r)/(8*a),       |ell_1|<<D,     (2.3)
```

and the second row similarly gives

```text
ell_2=d'*B-d*b,                    |ell_2|<<D.
```

They obey

```text
c*ell_2-d*ell_1=B*k.                               (2.4)
```

Hence, after conditioning on a common row, the two hyperbolas
`b~q^3/(8ac)` and `B~q^3/(8ac')` are homothetic and compose to the affine
strip

```text
c'*B-c*b=O(D).                                     (2.5)
```

The apparent reciprocal second derivative has disappeared.  A determinant
method applied before this elimination merely rediscovers the affine or
Hankel packets already merged in the coherent theorem.  After those rich
lines are removed, one or two selected points may remain on polynomially
many translates of (2.5); ordinary Huxley curvature supplies no aggregation
across those translates.

The exact missing anchored estimate can be stated directly.  If

```text
E_gamma(k)={e: all actual masks and both reciprocal carriers hold},
```

then partner uniqueness at fixed `k` reduces the second-factorial gate to

```text
#{k: K<=#E_gamma(k)<2K} << (D/K)*q^o(1).           (RG_K)
```

Indeed `(RG_K)` gives
`sum_k binom(#E_gamma(k),2)<<D*K*q^o(1)`, which is the certified sufficient
bound `(AF_2)`.  Equations (1.2), (2.3), and the actual prime/carrier masks
are the structure a proof of `(RG_K)` must retain.

## 3. The exact Kloosterman transform

On one fixed residual layer, the product congruence has the form

```text
x == lambda*inverse(y) (mod c_0),                  (3.1)
```

with `c_0~q` and `lambda` a unit on every populated layer.  For physical
weights `F,G`, put

```text
T_lambda(F,G)=sum_(x mod c_0)^* F(x)G(lambda*inverse(x)).
```

Double additive Fourier inversion gives exactly

```text
T_lambda(F,G)
 =c_0^(-2) sum_(h,n mod c_0) Fhat(h)Ghat(n)
                  S(h,n*lambda;c_0).              (3.2)
```

Kloosterman symmetry gives

```text
S(h,n*lambda;c_0)=S(lambda*n,h;c_0),               (3.3)
```

so (3.2) is genuinely the Blomer--Pascadi kernel `S(a m,n;c)` with
`a=lambda`, not merely an analogy.

There are three applicability losses.

1. The intervals in Theorem 1.1 are intervals in `h,n`, not in the short
   physical residuals or carriers.  An allowed physical point mass has
   `|Fhat(h)|=1` for all `h`, so no short Fourier support follows from the
   project masks.
2. Splitting one unrestricted Fourier side into length-`D` blocks costs at
   least

   ```text
   sqrt(q/D)=q^(17/66+o(1))                        (3.4)
   ```

   under absolute block summation; both sides cost `q^(17/33+o(1))`.
3. The modulus and the numerator layer vary.  For prime-power moduli the
   theorem's `(h,n,c_0)=1` restriction also requires a separate gcd-layer
   decomposition outside the initial-interval exception.

Thus a scalar fixed-layer theorem does not provide the required vector
square function over Fourier blocks and residual numerators.

## 4. Blomer--Pascadi exponent audit

Theorem 1.1 of Blomer--Pascadi bounds the bilinear form, relative to
`||alpha||_2||beta||_2*N*c^(1/2)`, by the sum

```text
c^(13/32)/N^(7/8)
 +c^(5/16)/N^(11/16)
 +c^(1/9)/N^(1/3).                                 (4.1)
```

At `c~q` and `N=D=q^(16/33)`, the three relative powers are

```text
q^(-19/1056),       q^(-11/528),       q^(-5/99). (4.2)
```

The first term dominates.  It beats the earlier *scalar local* shortfall
`q^(1/66)=q^(16/1056)` by only

```text
19/1056-1/66=1/352.                                (4.3)
```

This is the entire permissible loss in a hypothetical frequency-localized
local bridge.

For the present uniform four-cycle problem, the missing gain from the
proved `D^(5/4)` trace to `D` is

```text
D^(1/4)=q^(4/33)=q^(32/264).                       (4.4)
```

Even granting four independent, lossless applications of the dominant
Blomer--Pascadi saving gives only

```text
q^(-4*19/1056)=q^(-19/264),                        (4.5)
```

leaving the positive-power deficit

```text
32/264-19/264=13/264.                              (4.6)
```

This fourfold multiplication is already optimistic: the proof of Theorem
1.1 itself uses a fourth moment, and the QP layers are neither independent
nor frequency localized.  Therefore the new theorem does not close the
uniform high tail even before (3.4).

## 5. Surviving target

A successful analytic replacement would have to prove a **centered,
vector-valued** version of (3.2), square-summing simultaneously over

```text
Fourier blocks I,J,
residual numerators lambda_rho,
varying shell moduli c_0,
```

while preserving the actual prime-power and arbitrary `z` masks.  In the
residual coordinates, this is precisely `(RG_K)` after coherent affine
packets are merged.  A positive scalar sum or absolute frequency-block
decomposition cannot provide it.

```text
SL2 residual identity f=e*n-m*k:                    PROVED;
centered intercept identity f=e*beta-k*alpha:       PROVED;
reciprocal composition is affine:                  PROVED;
fixed layer Fourier kernel is S(a*m,n;c):           PROVED;
BP scalar saving at N=D is 19/1056:                 VERIFIED;
four lossless BP gains close q^(4/33):              NO;
native masks have short additive Fourier support:   FALSE;
centered vector/layer square function:              OPEN;
uniform high-completion tail:                       OPEN.
```

Source for (4.1): Blomer--Pascadi, *Bilinear forms with Kloosterman sums
via quadratic characters*, Theorem 1.1,
<https://arxiv.org/abs/2607.24311>.
