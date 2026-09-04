# QP centered band-pass: aligned tangent local-mean theorem

**Date:** 2026-08-22  
**Verdict:** the rational tangent packets themselves do not force a loss in
the centered dyadic moment.  In the balanced completed model with bounded
step defect `|R-S|=O(1)`, the product frequencies produced by the second
Poisson transform have diagonal-strength close-pair energy.  Consequently
the all-one aligned stationary main satisfies the scale-correct local mean
with `beta=0` throughout the high range `K>>sqrt(D)`.

This is a theorem for the aligned/tangent subfamily, not for a scattered
determinant strip.  For a general slope-adapted basis the Bezout residues
`U*r (mod R)` and `V*s (mod S)` are not short intervals; the proof below
then loses its hierarchy at exactly the outer-fan gate.  No new uniform
four-cycle exponent is claimed.

## 1. The aligned product grids

Let `P>=2`, let

```text
P<=n,m,n',m'<2P,             0<=r,s,r',s'<P,
X={R*n+r},                   Y={S*m+s},             (1.1)
```

and assume

```text
R,S>>P^2,                    |R-S|<<1.              (1.2)
```

The signs of `r,s` and fixed translates of all four intervals are
harmless.  Let `H` satisfy

```text
H+P^2+|R-S|*P^2<c*min(R,S)                         (1.3)
```

for a sufficiently small absolute `c`.  Then

```text
#{x,x' in X, y,y' in Y: |x*y-x'*y'|<=H}
 <<P^(4+o(1)).                                      (1.4)
```

Since `|X|=|Y|=P^2`, (1.4) is diagonal strength.

## 2. Proof of the close-product theorem

Expand

```text
x*y-x'*y'
 =R*S*(n*m-n'*m')
  +R*(n*s-n'*s')+S*(m*r-m'*r')
  +(r*s-r'*s').                                    (2.1)
```

The three lower lines have size `O((R+S)P^2)`.  Assumption (1.2), with
its implicit constant chosen larger than the fixed shell constants,
forces

```text
n*m=n'*m'.                                         (2.2)
```

Put

```text
A=n*s-n'*s',                 B=m*r-m'*r'.           (2.3)
```

Writing `S=R+delta`, equations (1.3) and (2.1)--(2.2) then force

```text
A+B=0.                                               (2.4)
```

For fixed outer indices satisfying (2.2), the inner variables therefore
lie on the integral hyperplane

```text
m*r-m'*r'+n*s-n'*s'=0.                              (2.5)
```

If

```text
g=(n,n',m,m'),                                      (2.6)
```

the primitive normal to (2.5) has sup norm `>>P/g`.  The elementary
lattice-point bound for a primitive hyperplane in a `P`-box gives

```text
#{(r,r',s,s') in [0,P)^4 satisfying (2.5)}
 <<P^2*(1+g).                                       (2.7)
```

One way to prove (2.7) is to choose a coefficient of maximal absolute
value, fix two variables and one residue class of a third, and solve for
the fourth.  The main-volume term is `P^3/(P/g)=g*P^2`; the boundary term
is `O(P^2)`.

It remains to average `g`.  Parameterize (2.2) by

```text
n=d*a,       n'=d*b,       m=b*t,       m'=a*t,
(a,b)=1.                                             (2.8)
```

Then the gcd in (2.6) is `(d,t)`.  For fixed comparable coprime `a,b` with
`M=max(a,b)`, both `d` and `t` range over intervals of length `O(P/M)`.
The classical gcd sum gives

```text
sum_(d,t<<P/M) (1+(d,t)) <<(P/M)^2*P^o(1).         (2.9)
```

There are `O(M)` pairs `(a,b)` with `max(a,b)=M`.  Summing (2.9) over
`M<=2P` proves

```text
sum_(n*m=n'*m') (1+(n,n',m,m'))<<P^(2+o(1)).       (2.10)
```

Equations (2.7) and (2.10) prove (1.4).

## 3. A centered long-parameter mean

Put

```text
xi=x/R,                 eta=y/S,
F(tau)=sum_(x in X,y in Y) c_(x,y)*e(tau*xi*eta),
|c_(x,y)|<=1.                                          (3.1)
```

Let `Omega` be a fixed nonnegative band-limited majorant for one compact
interval: `Omega>=1` there and `hat(Omega)` has fixed compact support.
If

```text
B=R*S/H,                                             (3.2)
```

then Fourier expansion and (1.4) give, uniformly in the center `tau_0`,

```text
integral_R Omega((tau-tau_0)/B)*|F(tau)|^2 d tau
 <<B*P^(4+o(1)).                                    (3.3)
```

Indeed, `hat(Omega)(B*(xi*eta-xi'*eta'))` vanishes unless
`|x*y-x'*y'|<<R*S/B=H`; (1.4) then applies.  The right side of (3.3) is
the diagonal mean `B*|X|*|Y|`, up to `P^o(1)`.

## 4. Return to the aligned bilinear chirp

For fixed smooth dyadic cutoffs and flat quotient-fan coefficients, write

```text
A(alpha)=sum_(j,k) W_P(j)*W_P(k)*w_1(j/J)*w_2(k/J)
          *e(alpha*j*k),                            (4.1)

W_P(j)=sum_(0<=r<P)e(-j*r/R).                       (4.2)
```

Take the balanced scales

```text
J~K*R,       R~S~q/P,       B=K*R*S/q,
P^2=D,       K>>P.                                  (4.3)
```

Two-dimensional Poisson summation in `(j,k)` has a nondegenerate bilinear
stationary point.  Uniform stationary phase gives, with rapidly summable
errors,

```text
A(alpha)=alpha^(-1)
 sum_(n,r,m,s) C_(n,r,m,s)(alpha)
 e(-(n+r/R)*(m+s/S)/alpha),                         (4.4)
```

where `n,m` range over fixed translates of `[P,2P]`, `r,s` over `[0,P)`,
and the smooth amplitudes `C` have bounded Mellin/Fourier complexity.
The latter may be separated at `q^o(1)` cost.  Formula (4.4) is the usual
exact quadratic stationary phase behind the completed HSM; no fan endpoint
is present because the long variables have fixed smooth cutoffs.

On `alpha~1/B`, set `tau=1/alpha`.  The Jacobian cancels the squared
stationary amplitude:

```text
|alpha|^(-2) d alpha =d tau.                        (4.5)
```

Moreover

```text
R*S/B=q/K=H,                                        (4.6)
```

and `K>>P` is exactly (1.3), since `H/R~P/K` and
`P^2/R=o(1)`.  Applying (3.3) to (4.4) proves

```text
integral_(alpha~1/B)|A(alpha)|^2 d alpha
 <<(1/B)*||W_P*w_1||_2^2*||W_P*w_2||_2^2*q^o(1).   (4.7)
```

Thus the aligned all-one stationary main has **no dyadic moment loss**.
Equivalently, after the standard centered-kernel linearization it satisfies
`M(K)<<q^(2+o(1))/K` in this subfamily.

## 5. Exact scope

The proof uses the short residues in (1.1).  In a general slope-adapted
unimodular basis the Poisson frequencies are instead

```text
R*n+U*r,                    S*m+V*s,                (5.1)
```

with `U*r` and `V*s` reduced modulo `R,S`.  They can be scattered across
the full moduli.  Then the hierarchy in (2.1) does not force (2.2)--(2.4),
and (1.4) becomes the original approximate-product/outer-fan problem.
Arbitrary physical fan weights also replace the all-one coefficients in
(4.2), although bounded separated weights remain harmless *after* (1.4)
is available.

The lower range `K<=P` is not covered by (1.3).  It is the coherent
parabolic range and must be merged by the existing Hankel packet theorem
or treated separately; the present result does not provide that global
cover.

```text
aligned close-product energy P^(4+o):             PROVED;
aligned centered long-parameter mean:             PROVED;
aligned all-one high-frequency stationary mean:   PROVED;
general modular Bezout residues:                   OPEN;
lower K<=sqrt(D) packet cover:                     OPEN;
uniform dyadic moment / new four-cycle exponent:   NOT PROVED.
```
