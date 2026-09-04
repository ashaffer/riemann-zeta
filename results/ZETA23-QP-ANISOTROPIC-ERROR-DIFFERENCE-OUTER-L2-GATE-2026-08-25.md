# QP anisotropic error-difference outer-L2 gate

**Date:** 2026-08-25  
**Verdict:** the proposed `sqrt(A/B)` gain is a sharp finite theorem if the
outer variable is genuinely Fourier-dual to the reduced error difference
`(e-f)/g`, with no aliasing and no uncontrolled multiplicity inside one
error pair.  It survives arbitrary selected subsets and even Hilbert-valued
contractions.  Merely having some outer `L2` norm, or merely being on the
stationary no-wrap branch, does not supply this Fourier transference.

Thus the numerical gain is real, but its identification with the physical
completion-sum norm remains an open intertwining step.  No four-cycle bound
is claimed.

## 1. Exact finite operator inequality

Let `I,J` be integer intervals of cardinalities `a<=b`, let `g,L` be
positive integers, and assume the reduced differences do not wrap:

```text
g*L>diam(I-J).                                       (1.1)
```

Let `Omega` be an arbitrary subset of

```text
{(e,f) in I*J: g|(e-f)}.                            (1.2)
```

For every `(e,f)` let `H_(e,f)` be a Hilbert space, let
`T_(e,f):H_(e,f)->K` be a contraction into another Hilbert space, and define

```text
(Qx)(s)=sum_((e,f) in Omega)
 e_L(s*(e-f)/g)*T_(e,f)x_(e,f),       s in Z/LZ.    (1.3)
```

The outer norm is normalized counting measure.  Put

```text
mu(Omega)=max_(r mod L)
 # {(e,f) in Omega:(e-f)/g==r mod L}.               (1.4)
```

Then

```text
||Qx||_(L2_s(K))^2
 <=mu(Omega)*sum_((e,f) in Omega)||x_(e,f)||^2.      (1.5)
```

Moreover, under (1.1),

```text
mu(Omega)<=a.                                        (1.6)
```

Indeed, Parseval gives the exact identity

```text
||Qx||_2^2
 =sum_(r mod L)||sum_((e,f) in Omega_r)T_(e,f)x_(e,f)||^2.  (1.7)
```

Cauchy on each fiber proves (1.5).  For (1.6), choose `e`; equality of the
reduced difference then forces `f`, and there are only `a` choices for `e`.
No positivity or regularity of the selected coefficients is used.

This is the strongest unconditional statement at this level: the exact
constant is the actual maximum fiber `mu(Omega)`.  It is sharp.  If a
translate of `I` lies in `J`, take the `a` pairs on one difference diagonal,
set all contractions equal to the identity, and take equal scalar inputs.
Then equality holds in (1.5).

For the full isotropic `b` by `b` window the corresponding sharp norm is
`sqrt(b)`.  The anisotropic `a` by `b` norm is `sqrt(a)`, so the exact ratio
of the worst-case bounds is

```text
sqrt(a/b) asymp sqrt(A/B).                           (1.8)
```

Here `a=2A+O(1)` and `b=2B+O(1)` for centered product-error windows.  The
same proof works for dyadic annuli and arbitrary deletions.

## 2. Consequence for a genuinely transferred no-wrap quadratic branch

Suppose a fixed-content, fixed-wrap quadratic piece of the physical
operator has an exact representation

```text
T_phys x(s)=sum_(|e|<=A,|f|<=B,g|(e-f))
 e_L(s*(e-f)/g)*K_(e,f)x_(e,f),                     (2.1)
```

where, after removing the common quadratic stationary amplitude `Lambda`,
every `K_(e,f)` is a contraction and there is at most one orthogonal input
atom per error pair.  Then (1.5)--(1.6) prove

```text
||T_phys||<=Lambda*sqrt(2A+1).                       (2.2)
```

Flattening the two errors to the wide window gives only
`Lambda*sqrt(2B+1)`.  Thus (2.2) supplies precisely the proposed
`sqrt(A/B)` improvement, uniformly under arbitrary selected pair weights.

At the worst energy endpoint,

```text
A=D,             B=D^(7/6),
sqrt(A/B)=D^(-1/12)=D^(-8/96).                      (2.3)
```

Applied to the no-wrap quadratic ledger `D^(55/96)`, this would give

```text
D^(55/96-8/96)=D^(47/96),                           (2.4)
```

which is below the square-root target by `D^(-1/96)`.

Equations (1.5)--(2.4) are proved.  The hypothesis that the physical
completion operator actually has the form (2.1) is not.

## 3. Two exact obstructions to an automatic gain

### 3.1 An unspecified outer L2 norm is insufficient

Replace the Fourier characters in (1.3) by identical unit vectors
`psi_(e,f)=psi`.  Take `g=1`; on the full `a` by `b` rectangle, take normalized equal
scalar coefficients.  Their input norm is one, while the output squared norm
is

```text
a*b,                                                   (3.1)
```

not at most `a`.  Equivalently, evaluate every difference character at the
single outer frequency zero.  This loses a factor `b` in energy, exactly the
factor whose square root was supposed to be gained.

Therefore the stationary no-wrap label `j=0` and the curvature lower bound
do not by themselves prove (2.1).  One must identify an actual physical
outer variable whose difference-character Gram matrix has bounded Bessel
norm.  This is the same kind of completion-sum intertwining missing from the
thickened-CRT square-root argument.

The `Q=1009` fixture gives a genuine warning: distinct reduced differences
already occur inside the same fixed completion level `S=2Q`.  Section 4
turns this warning into an exact no-go for the direct Fourier identification.

### 3.2 Repeated atoms inside one error pair cost their multiplicity

If `R` selected physical atoms carry the same pair `(e,f)` and their
synthesis vectors are coherent, take normalized equal coefficients.  The
outer energy is `R`, while a mask-only application of (1.6) would predict at
most `a`.  For `R>a` this is false.  The exact theorem (1.5) remains correct,
because its fiber multiplicity is `mu=R`.

Thus a physical use of (2.2) needs either:

1. one atom per error pair after the fixed direction/content decomposition;
2. an orthogonal internal vectorization of the repeated atoms; or
3. a separate `q^o(1)` bound for their coherent multiplicity.

Arbitrary selected coefficients do not create a problem once one of these
structural facts and the true difference Fourier variable are present.  In
their absence, the `sqrt(A/B)` gain is false as a mask-only operator claim.

## 4. Attachment to the universal off-content blow-up

For a reduced remote point put `ell=p^2-d^2` and define

```text
mathcal C=2*d^2*Q-g*p*ell,
U=2*d*y-g*ell,
H=mathcal C-2*p*U,
J_-=H-d*U,                 J_+=H+d*U.               (4.1)
```

Direct expansion gives the universal identities

```text
4*d^2*e=g*(p-d)*J_--U^2,
4*d^2*f=g*(p+d)*J_+-U^2,                            (4.2)
2*d*n=-(H+p*U),              n=(e-f)/g.             (4.3)
```

These formulas yield one exact no-go and one rigorous low-`P` theorem.

### 4.1 The difference label is not the completion Fourier label

The physical completion transform is dual to `S=a+b`.  In the symmetric
chart `S=2Q`, so every point at fixed `Q` carries the same outer character

```text
e(alpha*S)=e(2*alpha*Q),                             (4.4)
```

independently of `n`.  But `n` varies within a fixed completion level.  For
example, at `Q=1009` the two remote points

```text
(y,r,s)=(-144,24,18),        n=1,
(y,r,s)=(-100,11,9),         n=9                     (4.5)
```

both have `S=2018`.  Thus the physical completion columns for these two
reduced differences are aliases, not orthogonal Fourier characters.

Consequently the completion Fourier transform does **not** turn (4.3) into
the Parseval identity (1.7).  A nonlinear stationary action or a new outer
variable could still produce a Bessel estimate, but the direct assertion
that `(e-f)/g` is the existing completion Fourier variable is false.

### 4.2 Low primitive height forces a closed one-band branch

There is an exact integral gate.  If `|e|<=A` and

```text
g*(p-d)>4*d^2*A+U^2,                                (4.6)
```

then (4.2) gives `|J_-|<1`, hence

```text
J_-=0.                                               (4.7)
```

This is not a heuristic smallness claim: `J_-` is an integer.  The remote
off-content bounds give, in a compact collar,

```text
|U|/|d| <<B/Q^(1/3)=o(sqrt(A)),
d^2/(g*P) asymp P^2/Q.                              (4.8)
```

Therefore

```text
|J_-|<<A*P^2/Q.                                     (4.9)
```

For every fixed `eta>0`, the power-separated range

```text
A*P^2/Q<=D^(-eta),                                  (4.10)
```

satisfies (4.6) for all sufficiently large `D`.  Writing
`A=D^(1+u)` and `P=D^pi`, this is

```text
pi<17/32-u/2                                        (4.11)
```

with a fixed power margin.  A bare numerical condition `A*P^2/Q<1`
without room is not enough to absorb the collar constants; (4.6) is the
exact endpoint criterion.

The forced branch is divisor-major.  From (4.2) and (4.7),

```text
U=2*d*z,          e=-z^2,          n=-(p+d)*z       (4.12)
```

for an integer `z`; a rational number whose square is integral is integral.
Using `n=p*y-Q*d` gives

```text
p|(Q-z),             (Q-z)/p=(y+z)/d=:L.            (4.13)
```

Then `Q=pL+z`, `y=dL-z`, and `a=Q+y=(p+d)L`.  Since
`a*v=Q^2+e=Q^2-z^2`, cancellation of `L` gives

```text
p+d | Q+z.                                           (4.14)
```

The pair of divisors in (4.13)--(4.14) determines `p,d`; then `y,v,r,s,g`
are determined if a valid point exists.  Hence, uniformly at fixed `Q`,

```text
# {J_-=0 points with |e|<=A}
 <=sum_(|z|<=sqrt(A)) tau(Q-z)*tau(Q+z)
 <<sqrt(A)*Q^o(1).                                  (4.15)
```

Thus the low-`P` range (4.10) lands in a rigorously closed algebraic
one-band branch at the natural square-root packet scale.  Above
`P~sqrt(Q/A)`, integrality no longer forces `J_-=0`; there the finite
anisotropic theorem would be useful, but Section 4.1 shows that the physical
completion transform does not provide its required difference character.

### 4.3 A proved weighted residual polytope from three scalar counts

There is still a nonempty weighted subrange above the zero-factor threshold.
Write

```text
A=D^(1+u),       B=D^(1+v),
G=D^gamma,       P=D^pi,                             (4.16)
0<=u<=v,         2u+3v<1/2.
```

Consider an occupied residual cell, so

```text
u+2*pi>=17/16,             gamma+3*pi>=33/16,
gamma+pi<=33/16.                                  (4.17)
```

The last two inequalities express `1<=d<=P` under
`d^2 asymp G*P^3/Q`.  In this range the three available scalar counts have
the following exponents:

```text
Farey:       F=(gamma+5*pi-33/16)/2,
U/cubic:     K=v+gamma+2*pi-17/16,
fixed J_-:   J=gamma+(gamma+3*pi-33/16)/2
                    +(u+2*pi-17/16).                (4.18)
```

These replay respectively

```text
sqrt(G*P^5/Q),
B*G*P^2/Q,
G*sqrt(G*P^3/Q)*(1+A*P^2/Q).                        (4.19)
```

All factors displayed in (4.18)--(4.19) are at least one under (4.17), so
there is no hidden positive-part case.  A point count at most
`D^((1+u)/2)=sqrt(A)` controls arbitrary selected weights at fixed `S` by
Cauchy.  Direct rearrangement gives the exact three closing half-spaces:

```text
Farey closes iff
 gamma<=T_F:=49/16+u-5*pi,

U/cubic closes iff
 gamma<=T_K:=25/16+u/2-v-2*pi,

fixed J_- closes iff
 gamma<=T_J:=83/48-u/3-7*pi/3.                     (4.20)
```

Consequently the minimum of the three proved counts closes **exactly** the
union

```text
gamma<=max(T_F,T_K,T_J).                            (4.21)
```

within (4.16)--(4.17).  The dominance boundaries, useful for reading this
polytope without case-searching, are

```text
T_J>=T_F  iff  pi>=(1+u)/2,
T_K>=T_F  iff  3*pi>=3/2+u/2+v,
T_K>=T_J  iff  2*pi+5u-6v>=1.                      (4.22)
```

The union is nonempty.  At

```text
(u,v,gamma,pi)=(0,0,15/32,17/32),                  (4.23)
```

which lies exactly on `A*P^2/Q=1` and `d asymp1`, one has

```text
(F,K,J)=(17/32,15/32,15/32)<=(1/2,1/2,1/2).        (4.24)
```

There are also cells where the Farey estimate alone wins; for example

```text
(u,v,gamma,pi)=(1/24,1/24,51/96,49/96),
(F,K,J)=(49/96,51/96,51/96),
target=50/96.                                       (4.25)
```

The other two faces are also genuinely active.  With `u=v=0`,
`pi=17/32`, `gamma=127/256`, only the cubic count is below `1/2`.
With `(u,v,gamma,pi)=(0,1/10,23/48,17/32)`, only the fixed-`J_-`
count is below `1/2`, with exponent `31/64`.

However, this optimization does not reach the no-wrap worst cell.  At the
limiting endpoint

```text
(u,v,gamma,pi)=(0,1/6,0,43/48),                    (4.26)
```

one gets

```text
(F,K,J)=(29/24,43/48,25/24),                       (4.27)
```

so even the best count is `D^(43/48)`, far above `sqrt(A)=D^(1/2)`.
Thus (4.21) is a genuine rigorously attached weighted subrange, not a closure
of the residual high-`P` face.

## 5. Reproducibility and status

The finite fibers, direct DFT Parseval identity, sharp diagonal, arbitrary
subset test, collapsed-character obstruction, repeated-atom obstruction,
endpoint exponent ledger, universal blow-up, completion-alias fixture, exact
zero-factor gate, and shifted-divisor majorant are implemented in

```text
src/qp_anisotropic_outer_l2.py
src/test_qp_anisotropic_outer_l2.py
```

Nine focused tests pass.

```text
finite reduced-difference Parseval identity:          PROVED;
arbitrary pair-subset norm <=sqrt(a):                 PROVED;
sqrt(a/b) anisotropic ratio:                          PROVED AND SHARP;
Hilbert-valued contraction version:                   PROVED;
gain from an unspecified outer L2 norm:               FALSE;
gain with uncontrolled same-label multiplicity:       FALSE;
physical completion/error-difference intertwining:    OPEN;
reduced difference is the completion Fourier label:   FALSE;
exact low-height gate (4.6) forces J_-=0:              PROVED;
power-separated A*P^2/Q=o(1) one-band branch:         CLOSED;
three-count residual union (4.21):                    CLOSED;
three-count method closes the worst high-P cell:      FALSE;
no-wrap quadratic branch closed in the fourth trace:  NOT PROVED;
sharp four-cycle bound:                               NOT PROVED.
```
