# QP approximate tangent stability: the Fejer plateau, curvature, and wrap label

**Date:** 2026-08-25  
**Scope:** symmetric chart `lambda=1/4`, compact collar  
**Verdict:** the exact `P^(-4)` rational-tangent saving is not stable once
`P^2>H`.  A same-sign regular singleton gives a sharp counterexample in a
small power window.  For opposite signs there is, however, an exact joint
stationarity--fold identity: outside an integer wrap sector a near character
has curvature `>>dK/P`.  This removes the genuinely Airy-degenerate layer but
leaves `D^(7/96)` in the flattened worst-cell ledger.  Retaining the two
unequal masks would close that numerical gap if it supplied the natural
`sqrt(A/B)` gain; that vector-valued step is not proved here.

No aggregate cancellation or sharp four-cycle bound is claimed.

## 1. Exact transfer and character width

The primal identities give

```text
p*y-Q*d=n,                 |g*n|<=2B.                 (1.1)
```

The physical and primitive tangent parameters are

```text
t=(Q+y)/(2Q),              t_0=(p+d)/(2p),
t-t_0=n/(2Qp).                                       (1.2)
```

For

```text
Phi(t)=h/(4t)+k/(4(1-t))-m*t                         (1.3)
```

put

```text
M_(h,k)(t)=k/(4(1-t)^2)-h/(4t^2).                   (1.4)
```

In a fixed collar and for `|h|,|k|<H`,

```text
|M_(h,k)(t)-M_(h,k)(t_0)|
 <<H*B/(Q*G*P)=:mu.                                  (1.5)
```

At `t_0`, writing `r=p+d`, `s=p-d`,

```text
M_(h,k)(t_0)=p^2*(k/s^2-h/r^2).                     (1.6)
```

In the generic reduced parity the cyclic modulus is

```text
R=r^2*s^2=(p^2-d^2)^2 asymp P^4.                    (1.7)
```

Thus (1.5) is exactly an interval of

```text
W_+=1+O(R*mu)
   =1+O(H*B*P^3/(Q*G))                              (1.8)
```

adjacent residue characters.  This confirms the proposed character-width
normalization.  It does not supply square-root cancellation between those
characters.

## 2. Why the exact `P^(-4)` mass does not persist

When `P^2<=H`, each exact/shifted CRT layer has normalized Fejer mass

```text
M_layer <<P^(-4).                                    (2.1)
```

When `P^2>H`, a nonempty layer can consist of one frequency pair.  Its mass
is then `asymp H^(-2)`, not `P^(-4)`.  In fact, when
`min(r^2,s^2)>2H`, the residue map on the Fejer box is injective: equality of
two residues implies

```text
r^2 | h_1-h_2,             s^2 | k_1-k_2,            (2.2)
```

and hence equality of the pairs.  The unconditional vector bound in this
range is only

```text
||layers in E||_2
 <<min(sqrt(#E)*H^(-2), H^(-1)).                     (2.3)
```

The second term is the exact `l^2` norm of all triangular coefficient
products, up to an absolute constant.

There is also a closed-form regular counterexample.  Suppose

```text
4|p,       3|d,       gcd(p,d)=1,
h=p/4+d/3,       k=p/4-d/3,       m=d/3.             (2.4)
```

Then direct expansion gives

```text
p^2*(k/s^2-h/r^2)-m
 =-d^5/(3*(p^2-d^2)^2).                              (2.5)
```

Both `h,k` are positive in the compact collar, so `Phi''>0`: this is a
regular quadratic mode, not an opposite-sign fold.  It therefore cannot be
dismissed by changing only the Airy/fold treatment.

At the worst energy endpoint

```text
Q=D^(33/16), H=D^(17/16), B=D^(7/6),
G=1,        P_f=Q/B=D^(43/48),
d^2 asymp P_f^3/Q=D^(5/8).                           (2.6)
```

Equation (2.5) lies comfortably inside (1.8), while its Fejer product has
size `H^(-2)`.  At `P=P_f`,

```text
W asymp H*P^2,
sqrt(W)*P^(-4) asymp sqrt(H)*P^(-3).                 (2.7)
```

Therefore the proposed high-`P` bound fails when

```text
P>H^(5/6).                                           (2.8)
```

The energy exponents give

```text
H^(5/6)=D^(85/96),       P_f=D^(86/96).              (2.9)
```

So there is a genuine `D^(1/96)` counter-window, and at its top the singleton
exceeds `sqrt(W)P^(-4)` by `D^(1/32)`.

## 3. Exact stationarity--fold identity

The preceding counter uses same-sign frequencies and therefore does not
decide whether a near character can inhabit the opposite-sign Airy layer.
For `h>0`, `k=-v<0`, put

```text
u=(h+v)/2,
F=h*s^3-v*r^3,
A=p^2*(h/r^2+v/s^2).                                (3.1)
```

Here stationarity asks that `A` be an integer (with the original Poisson
integer equal to its negative), while `F=0` is the fold equation at `t_0`.
One has the exact identity

```text
A=(h+v)-X-cF,                                        (3.2)
X=6d^2*u/(p^2+3d^2),
c=2p^2*d/((p^2-d^2)^2*(p^2+3d^2)),                  (3.3)
Phi''(t_0)=4p^3*F/(p^2-d^2)^3.                       (3.4)
```

Proof: use

```text
A=2p^2*((p^2+d^2)u-2pdw)/(p^2-d^2)^2,
F=2*(p*(p^2+3d^2)w-d*(3p^2+d^2)u),                  (3.5)
```

where `w=(h-v)/2`, and eliminate `w`.

There is an immediate no-wrap transversality lemma.  Assume

```text
dist(A,Z)<=mu,       mu<=X/2,
X+c|F|<1/2.                                           (3.6)
```

Then the nearest integer in (3.2) is `h+v`, and

```text
|F| >=(X-mu)/c,
|Phi''(t_0)| >=6p*d*u/(p^2-d^2) asymp d*K/P.         (3.7)
```

Thus the dangerous near character is forced away from the fold.  Using the
physical relation `d^2 asymp GP^3/Q`, the hypothesis `X>>mu` is precisely,
up to collar constants,

```text
G^2*P^2 >>B.                                         (3.8)
```

At (2.6),

```text
X=D^(-5/48),       mu=D^(-35/48),
|Phi''|>>H*d/P=D^(23/48).                            (3.9)
```

The true Airy/second-derivative crossover is only

```text
H^(2/3)*Q^(-1/3)=D^(1/48).                           (3.10)
```

Hence the genuinely Airy-degenerate portion of the no-wrap branch is empty.
The available quadratic amplitude is

```text
sqrt(Q/(H*d/P))=D^(19/24).                           (3.11)
```

Replacing `D^(49/48)` by (3.11) in the flattened transition ledger improves
it by `D^(-11/48)`, from `D^(77/96)` to

```text
D^(55/96).                                           (3.12)
```

This is substantial but remains `D^(7/96)` above the square-root target.

## 4. The integer wrap label

Let `m_+` be the positive stationarity integer and define

```text
j=h+v-m_+.                                           (4.1)
```

Equation (3.2) becomes the exact near-resonance condition

```text
|j-X-cF|<=mu,             j=round(X+cF).             (4.2)
```

Clearing denominators gives a simpler linear equation.  Define

```text
a=d*(2p+d)*(p-d)^2,
b=d*(2p-d)*(p+d)^2.                                  (4.3)
```

Then

```text
R*(A-m_+)=jR+bv-ah.                                  (4.4)
```

Thus fixed `j` gives a rank-one Diophantine strip, not a divisor conic.  Its
exact solutions form one progression with primitive step

```text
(b/g_0,a/g_0),       g_0=gcd(a,b) in {d,2d,4d}.      (4.5)
```

The factors `2,4` are parity only, and the step is `asymp P^3`; consequently
there is at most one exact solution in a box of side `H<P^2`.

For approximate solutions the wrap range is

```text
|j|<<1+H*d/P.                                        (4.6)
```

For fixed `u`, increasing `h` by one and decreasing `v` by one changes
`X+cF` by exactly

```text
theta=c*(r^3+s^3)=4p^3*d/(p^2-d^2)^2 asymp d/P.     (4.7)
```

The elementary rotation count therefore gives only

```text
#h for fixed u
 <<(1+H*d/P)*(1+mu*P/d)
 <<1+H*d/P+H*mu+mu*P/d.                             (4.8)
```

At the worst endpoint `mu*P/d=o(1)`, but `Hd/P=D^(23/48)` is larger than
`Hmu=D^(1/3)`.  Hence the hoped-for deterministic `O(1+Hmu)` wrap count does
**not** follow from rational spacing alone.  An average in `u` or in the wrap
character is still needed.

For `j!=0`, (4.2)--(4.4) instead force, away from a half-integer boundary,

```text
|Phi''| asymp |j|*P/d.                               (4.9)
```

Accordingly the quadratic amplitudes decay like `|j|^(-1/2)`.  A genuine
outer `l^2_j` sum would cost only a logarithm; an absolute sum costs
`sqrt(#j)` and is not sufficient.  This is the exact wrap square-function
target.

The no-wrap hypothesis cannot simply be omitted.  The finite fixture

```text
p=100, d=3, H=235,
(h,k,m)=(200,-167,-366)                              (4.10)
```

has

```text
dist(M,m)=880354/99820081 <47/2000=H/p^2,
Phi''=196764000000/997302429271=0.197296...,
|Phi'''|=8792.05... .                                (4.11)
```

Thus it is simultaneously a near character and a genuine cubic/fold-scale
mode.  Here `X=9909/10027=0.988...` wraps near the next integer, exactly as
(4.2) predicts.

## 5. The wrap label is a Poisson alias, not an outer Fourier variable

It is important not to manufacture an orthogonality variable.  In the
opposite-sign notation the original Poisson integer is `m=-m_+`, so

```text
j=h+v-m_+=h-k+m.                                     (5.1)
```

At the central point, for `lambda=1/4`,

```text
Phi'(1/2)=k-h-m=-j.                                  (5.2)
```

Restoring the physical scaling `t=a/S`, the affine character discarded in
the stationary normal form is

```text
e(-j*a).                                             (5.3)
```

But `a` is an integer carrier, so (5.3) is identically one.  This is exactly
why different Poisson integers are aliases in Poisson summation.  The
`S`-dependent constant is also integral when `S` is even; for odd `S` it
retains at most a parity character.  The tangent intercept characters depend
on `(h,k)` and do not turn the independent Poisson alias into a new averaged
coordinate.  Hence neither the physical `a` sum nor the completion-sum
Fourier transform supplies Parseval in `j`.

There is an exact hostile finite model.  Take `L` wrap labels in one dyadic
`j` block, so their curvature amplitudes `|j|^(-1/2)` are comparable, and
sample at any nonempty set of integer carriers.  All affine columns (5.3)
are identical.  After factoring out their common dyadic size,

```text
coherent square=L^2,       diagonal square=L.        (5.4)
```

Thus a pointwise or physically sampled `j` square function loses
`sqrt(L)`; it does not cost only a logarithm.  Full Haar averaging in a new
continuous intercept would diagonalize the labels, but that auxiliary
variable is absent from the fixed-`S` problem.  Any successful wrap estimate
must exploit variation of the **nonlinear stationary action**, the actual
prime-power support, or another genuine outer average.  It cannot use the
alias character alone.

## 6. The anisotropic `D^(7/96)` target

Write the original unequal error widths as

```text
A=D^(1+alpha),       B=D^(1+beta),
0<=alpha<=beta,      2alpha+3beta<1/2.               (6.1)
```

Flattening `|e|<=A`, `|f|<=B` to `|e-f|<=2B` produces (1.5) and the residual
`D^(7/96)` in (3.12).  In the worst cell `beta=1/6`, the energy constraint
forces `alpha=0`, so

```text
sqrt(A/B)=D^(-1/12)=D^(-8/96).                       (6.2)
```

If the two Fejer directions and a Cauchy/square-function step retain this
factor, (3.12) becomes `D^(47/96)`, closing with `D^(-1/96)` slack.

This gain is **not** a pointwise consequence of (1.1): taking `e=0` and
`f` of size `B` makes `|n|` of size `B/g`.  Therefore one may not replace
`B` by `A` in (1.5).  The precise remaining theorem is vector-valued:
retain the two original mask characters through completion, obtain an outer
`L^2` estimate, and recover `sqrt(A/B)` on the no-wrap quadratic branch.

The companion audit
`ZETA23-QP-ANISOTROPIC-ERROR-DIFFERENCE-OUTER-L2-GATE-2026-08-25.md`
proves the exact finite version: if the outer variable is Fourier-dual to
`(e-f)/g`, a no-wrap error rectangle of cardinalities `a<=b` has sharp
operator norm `sqrt(a)`, versus `sqrt(b)` isotropically, even after arbitrary
pair selection.  It also proves that an unspecified outer `L^2` norm or
uncontrolled repetition inside one error pair does not imply this gain.
The physical completion/error-difference intertwining remains open.

## 7. Reproducibility and status

The exact identities, counterfamily, exponent ledger, linear wrap equation,
no-wrap lower bound, and finite fold fixture are implemented in

```text
src/qp_approximate_tangent_character_stability.py
src/test_qp_approximate_tangent_character_stability.py
```

Six focused tests check them with exact rational arithmetic.

```text
character width W=R*mu:                              VERIFIED;
high-P shifted-layer mass P^(-4):                    FALSE;
regular nonfold singleton counterfamily:             PROVED;
exact residue--fold identity:                        PROVED;
no-wrap curvature >=dK/P:                            PROVED;
uniform near-character implies uniform curvature K: FALSE;
fixed-wrap resonance is a linear progression:        PROVED;
deterministic O(1+H*mu) wrap count:                   NOT DERIVED;
wrap label is an existing physical Fourier variable: FALSE;
pointwise logarithmic wrap square sum:                FALSE IN GENERAL;
finite difference-character sqrt(A/B) gain:           PROVED AND SHARP;
physical completion-sum sqrt(A/B) gain:               OPEN;
sharp four-cycle bound:                              NOT PROVED.
```
