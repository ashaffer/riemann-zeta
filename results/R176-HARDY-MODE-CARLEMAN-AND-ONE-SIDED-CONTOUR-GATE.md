# R176 Hardy-mode, Carleman, and one-sided-contour gate

## Status

The pole of

```text
B_q=(1-F)^(q-1)F'/F                                      (0.1)
```

at a retained `F`-zero really does occupy a negative Hardy mode which no
regular germ can cancel.  On a complete circle this gives an exact
orthogonal lower bound.  The proposed escape was to keep that lower bound
while estimating `B_q` only on a right boundary, where its Dirichlet support
beyond `H^q` makes it very small, and to suppress the uncontrolled part of
the contour by a Carleman weight.

There is a sharp answer.  Let `E` be the controlled right arc and let

```text
omega=omega(rho,E;D)                                     (0.2)
```

be its harmonic measure at the enclosed zero.  If `delta` bounds `B_q` on
`E` and `M` bounds it on the rest of the contour, then

```text
|res_rho B_q| <= C_D delta^omega M^(1-omega).             (0.3)
```

Consequently

```text
M >=c_D delta^[-omega/(1-omega)].                         (0.4)
```

This is optimal.  Analytic Carleman weights obey the same harmonic-measure
tradeoff, and outer functions attain the exponent in (0.4).  Moreover, every
such local extremal can be represented exactly in the nonlinear form (0.1).
Thus the special pole-plus-regular-germ algebra does not improve the
one-sided continuation constant.

For the actual head-deleted zeta function

```text
F_H(s)=zeta(s) product_(p<=H)(1-p^(-s)),                  (0.5)
```

one has on every fixed right arc `Re(s)>=1+a`

```text
|B_(q,H)(s)| <=C_a^q H^(-qa) log H.                       (0.6)
```

Hence a hypothetical enclosed zeta zero forces

```text
max_(partial D\E)|B_(q,H)|
 >=H^[qa omega/(1-omega)-o(q)].                           (0.7)
```

The large complementary norm is not optional noise: it is forced by the
zero and is precisely where the negative Hardy coefficient is paid back.
Known absolute bounds there are only of stretched-exponential size,
`exp(O_D(qH^(1-sigma_-)))`, so (0.3) gives no contradiction.

Functional-equation pairing does not remove this bill.  Reflection of
`B_q` splits exactly into a target-bearing **linear** logarithmic derivative
and a nonlinear term which is analytic at the target.  Keeping the target
therefore loses the `H^q` support; deleting the linear term deletes the
target.  The finite Euler head also inserts a reflection multiplier of
exponential size.

An explicit dilation of zeta supplies a countermodel with all of the local
features used by a one-sided argument: a fixed near-one zero, positive
ordinary Dirichlet coefficients after head deletion, exact support beyond
`H^q`, and arbitrarily small right-boundary norm.  Its complementary norm
pays (0.4).  It is not degree-one zeta, so it does not rule out a genuinely
zeta-specific theorem; it proves that Hardy orthogonality, late support,
positivity, and one-sided continuation alone cannot give one.

```text
complete-circle negative Hardy mode                         EXACT
regular-germ cancellation of that complete mode             IMPOSSIBLE
right-arc-only pole lower bound                              FALSE
optimal right/complement interpolation                      (0.3)
Carleman improvement over harmonic measure                  IMPOSSIBLE
nonlinear form (0.1) improves local continuation            FALSE
actual H^q right-tail decay                                  EXACT
forced complementary growth                                 EXACT
functional-equation target-preserving H^q channel           IMPOSSIBLE
coefficient-specific logarithmic-mean bound                  OPEN
fixed uniform zeta zero-free strip                           NOT PROVED
zeros approaching Re(s)=1                                   NOT PROVED
```

Date: 2026-08-08.

Predecessors:

* [`R126-PUNCTURED-CONTOUR-ALL-MOMENT-AND-KEYHOLE-GATE.md`](R126-PUNCTURED-CONTOUR-ALL-MOMENT-AND-KEYHOLE-GATE.md),
  for the connector form of the winding debt;
* [`R129-SIGMA-DIFFERENCE-LOGDERIVATIVE-GATE.md`](R129-SIGMA-DIFFERENCE-LOGDERIVATIVE-GATE.md),
  for zero-mass kernels and the signed vertical debt;
* [`R133-HIGH-JET-EULER-RECURRENCE-GATE.md`](R133-HIGH-JET-EULER-RECURRENCE-GATE.md),
  for the local-jet localization ledger;
* [`R150-TRANSLATED-CARRIER-AND-FUNCTIONAL-EQUATION-GATE.md`](R150-TRANSLATED-CARRIER-AND-FUNCTIONAL-EQUATION-GATE.md),
  for the circular carrier and reflection gates; and
* [`R154-COPRIME-FILTER-PACKET-AND-RESULTANT-GATE.md`](R154-COPRIME-FILTER-PACKET-AND-RESULTANT-GATE.md),
  for the complete-circle Hardy calculation and the regular polynomial germ.

## 1. The negative Hardy coefficient is genuine

Let `B` be meromorphic on a neighborhood of

```text
closed D(rho,R)={s:|s-rho|<=R}                           (1.1)
```

and suppose its only pole there is a simple pole at `rho`, with residue
`m`.  Write

```text
B(s)=m/(s-rho)+G(s),                                     (1.2)
```

where `G` is holomorphic on the disc.  If

```text
G(rho+z)=sum_(n>=0)g_n z^n,                              (1.3)
```

then on the boundary circle

```text
B(rho+Re^(it))
 =(m/R)e^(-it)+sum_(n>=0)g_n R^n e^(int).                (1.4)
```

The target pole is the Fourier mode `-1`; every regular Taylor coefficient
has a nonnegative mode.  Parseval therefore gives the exact identity

```text
1/(2pi) integral_0^(2pi)|B(rho+Re^(it))|^2 dt
 =|m|^2/R^2+sum_(n>=0)|g_n|^2R^(2n).                     (1.5)
```

In particular,

```text
||B||_(L^2(partial D))>=|m|/R.                           (1.6)
```

Equivalently, the negative projection recovers the residue exactly:

```text
m=R/(2pi) integral_0^(2pi)
       B(rho+Re^(it))e^(it)dt.                           (1.7)
```

Thus the regular germ cannot cancel the target on the **complete** circle.
This is stronger than selecting a large Taylor derivative at an exterior
point: it isolates the pole with condition number one in the natural Hardy
norm.

The qualification "complete" is decisive.  On every proper compact arc of
the circle, polynomials can approximate `-m/(s-rho)` arbitrarily well.  The
regular germ can therefore cancel the pole on that arc while growing on the
omitted part.  The next section computes the exact cost of doing so.

## 2. Sharp harmonic-measure interpolation

Let `D` be a bounded simply connected Jordan domain, let `rho` lie in `D`,
and split its boundary, up to endpoints of harmonic measure zero, into

```text
partial D=E union C.                                      (2.1)
```

Think of `E` as the part lying in the absolutely convergent half-plane and
`C` as the left boundary plus the connectors.  Put

```text
omega=omega(rho,E;D),          0<omega<1.                (2.2)
```

### Theorem 2.1 -- one-sided pole interpolation

Suppose `B` is meromorphic on a neighborhood of `closed D`, its only pole
in `D` is a simple pole at `rho`, and

```text
res_rho B=m!=0.                                           (2.3)
```

For `1<=p<infinity`, define the conditional harmonic-measure norms

```text
X_(E,p)=
 {1/omega integral_E |(s-rho)B(s)|^p domega_rho(s)}^(1/p),

X_(C,p)=
 {1/(1-omega) integral_C |(s-rho)B(s)|^p domega_rho(s)}^(1/p).
                                                               (2.4)
```

Then

```text
|m|<=X_(E,p)^omega X_(C,p)^(1-omega).                    (2.5)
```

If instead

```text
delta=sup_E|B|,             M=sup_C|B|,                  (2.6)
```

and `R_D=max_(partial D)|s-rho|`, then

```text
|m|<=R_D delta^omega M^(1-omega),                        (2.7)

M>= (|m|/R_D)^[1/(1-omega)]
       delta^[-omega/(1-omega)].                         (2.8)
```

#### Proof

The function

```text
A(s)=(s-rho)B(s)                                         (2.9)
```

is holomorphic on `D` and satisfies `A(rho)=m`.  Subharmonicity of
`log|A|` and the harmonic-measure solution of the Dirichlet problem give

```text
log|m|<=integral_(partial D)log|A(s)|domega_rho(s).       (2.10)
```

Apply Jensen's inequality separately on `E` and `C` to obtain (2.5).
Taking the two supremum bounds for `A`, each at most `R_D` times the
corresponding bound for `B`, proves (2.7), and rearrangement gives (2.8).
QED.

The logarithmic form (2.10) is the strongest and most useful version.  It
shows that a logarithmic mean, rather than a supremum or an `L^2` norm, is
the natural currency for a one-sided contour.

### 2.1 Moving contours do not delete the bill

Theorem 2.1 applies separately to every `H`-dependent domain `D_H`.  A thin
keyhole can make the uncontrolled boundary short in arclength, but the
relevant quantity is its harmonic measure from `rho`, not its length.  A
long thin finger leading from the zero to the right body generally makes
the right exit harmonic measure small.  All geometric optimization is
therefore recorded by the single number `omega_H`; there is no limit in
which the complement disappears while a fixed right-boundary influence is
retained.

## 3. Carleman weights have exactly the same condition number

Let `W` be holomorphic on `D`, continuous on its closure, and normalized by

```text
W(rho)=1.                                                 (3.1)
```

Put

```text
a_W=sup_E|W|,                 c_W=sup_C|W|.              (3.2)
```

The two-constants theorem applied to `W` gives

```text
1<=a_W^omega c_W^(1-omega),                              (3.3)
```

or, with `kappa=(1-omega)/omega`,

```text
a_W>=c_W^(-kappa).                                       (3.4)
```

On the other hand, the weighted residue identity is

```text
m=1/(2pi i) integral_(partial D)W(s)B(s)ds.              (3.5)
```

An absolute estimate for (3.5) has, up to fixed boundary-length constants,
the cost

```text
delta a_W+M c_W
 >=delta c_W^(-kappa)+M c_W.                             (3.6)
```

Optimizing the right side over `c_W>0` gives

```text
inf_(c>0){delta c^(-kappa)+Mc}
 =C_omega delta^omega M^(1-omega).                       (3.7)
```

Thus an analytic weight can redistribute the contour bill, but it cannot
improve its harmonic-measure exponent.  Formula (3.7) is the Carleman dual
of (2.7).

This exponent is sharp.  Let `u(s)=omega(s,E;D)`.  Since `D` is simply
connected, `u` has a harmonic conjugate, so there is a holomorphic function
`g` with `Re(g)=u`.  For `T>0`, define

```text
A_T(s)=exp{-T[g(s)-g(rho)]},
B_T(s)=A_T(s)/(s-rho).                                    (3.8)
```

Then `res_rho B_T=1`, while, in the nontangential boundary sense,

```text
|A_T|=exp[-T(1-omega)]       on E,
|A_T|=exp[T omega]           on C.                        (3.9)
```

Consequently the relation between the two norms is exactly

```text
M_T asymp delta_T^[-omega/(1-omega)].                    (3.10)
```

Smoothing the boundary data near the two endpoints gives extremals
holomorphic on a neighborhood of every closed subarc, with the same
exponent.  Hence (2.8) is not a defect of a three-lines proof.

### 3.1 The nonlinear form imposes no extra local restriction

The extremals above can be put exactly into the form (0.1).  More generally,
suppose `B` has residue one at `rho` and no other pole in `D`.  There is a
holomorphic function `Y`, with its only zero a simple zero at `rho`, such
that

```text
Y'/Y=B.                                                    (3.11)
```

Indeed, integrate the holomorphic function
`B(s)-1/(s-rho)` and exponentiate after multiplying by `s-rho`.

For an integer `q>=1`, let

```text
R_q'(z)=[(1-z)^(q-1)-1]/z,        R_q(0)=0,
Psi_q(z)=z exp(R_q(z)).                                   (3.12)
```

The apparent singularity in `R_q'` is removable, `R_q` is a polynomial,
and

```text
d/dz log Psi_q(z)=(1-z)^(q-1)/z.                         (3.13)
```

Also `Psi_q'(0)=1`, so `Psi_q` has a local holomorphic inverse at zero.
After replacing `Y` by `cY` for a sufficiently small nonzero constant, its
image lies in that inverse chart.  Define

```text
F=Psi_q^(-1)(cY).                                        (3.14)
```

Then `F` is holomorphic on `D`, has exactly the zero of `Y`, and

```text
(1-F)^(q-1)F'/F=Y'/Y=B.                                 (3.15)
```

Therefore neither the unique-zero transform nor the regular polynomial germ
improves one-sided analytic continuation.  An arithmetic normalization
`F=1+U` on the right is additional information; it is addressed next.

## 4. Application to the head-deleted zeta tail

Assume hypothetically that `rho` is a zeta zero of multiplicity `m` with
`1/2<Re(rho)<1`.  Choose a fixed target-isolating Jordan domain `D` which

* contains `rho` and no other zeta zero;
* avoids the zeta pole at `1`;
* has closure in `Re(s)>0`; and
* has a nonempty boundary arc `E` contained in `Re(s)>=1+a` for some
  fixed `a>0`.

Such a domain can be made by joining a small zero-isolating disc to a right
cap by a thin tube avoiding the discrete zeta divisor.  Let `C=partial D\E`
and let `omega` be as in (2.2).

For `H>=2`, put

```text
P_H(s)=product_(p<=H)(1-p^(-s)),
F_H(s)=zeta(s)P_H(s).                                     (4.1)
```

The zeros of every factor in `P_H` lie on `Re(s)=0`, so on `D` the zero
divisor of `F_H` is the chosen zeta divisor.  In `Re(s)>1`,

```text
F_H(s)=product_(p>H)(1-p^(-s))^(-1)=1+U_H(s),             (4.2)
```

where `U_H` has nonnegative Dirichlet coefficients and every nonconstant
index is strictly larger than `H`.  Also

```text
F_H'/F_H=-sum_(p>H)sum_(k>=1)(log p)p^(-ks).              (4.3)
```

Define

```text
B_(q,H)=(1-F_H)^(q-1)F_H'/F_H.                           (4.4)
```

Equations (4.2)--(4.3) show that, up to the common sign `(-1)^q`, its
Dirichlet coefficients are nonnegative and

```text
supp B_(q,H) subset {n:n>H^q}.                            (4.5)
```

At `rho`, the factor `(1-F_H)^(q-1)` equals one, so

```text
res_rho B_(q,H)=m.                                       (4.6)
```

### Theorem 4.1 -- forced complementary contour growth

There is a constant `C_a` such that, uniformly on `E`,

```text
|F_H-1|<=C_a H^(-a),
|F_H'/F_H|<=C_a H^(-a)log H.                             (4.7)
```

Consequently

```text
delta_(q,H):=sup_E|B_(q,H)|
 <=C_a^q H^(-qa)log H,                                   (4.8)
```

and Theorem 2.1 forces

```text
sup_C|B_(q,H)|
 >=c_D
   [C_a^q H^(-qa)log H]^[-omega/(1-omega)].              (4.9)
```

In logarithmic form,

```text
log sup_C|B_(q,H)|
 >=omega/(1-omega)
   [qa log H-q log C_a-log log H]+O_D(1).                (4.10)
```

#### Proof

For `sigma>=1+a`, absolute convergence gives

```text
|log F_H(s)|
 <=sum_(p>H)sum_(k>=1)p^[-k(1+a)]/k
 <=C_a H^(-a),                                          (4.11)
```

and

```text
|F_H'/F_H|
 <=sum_(p>H)sum_(k>=1)(log p)p^[-k(1+a)]
 <=C_a H^(-a)log H.                                     (4.12)
```

The first estimate and `|e^z-1|<=2|z|` for small `z` prove (4.7), hence
(4.8).  Apply (2.8) using (4.6).  QED.

Equation (4.10) is the precise answer to the proposed Hardy-mode escape.
The late right tail does detect the pole, but it simultaneously proves that
the omitted contour norm must grow.  One cannot keep the negative Hardy
coefficient while discarding the boundary on which it is conserved.

### 4.1 Available outer bounds are on the wrong scale

Let

```text
sigma_-=min_(s in partial D)Re(s)>0.                     (4.13)
```

On the fixed zero-free boundary, elementary absolute estimates give, when
`sigma_-<1`,

```text
log|P_H(s)|<=C_D H^(1-sigma_-),
|P_H'/P_H|<=C_D H^(1-sigma_-)log H.                       (4.14)
```

The fixed zeta factors are bounded there.  It follows that

```text
log sup_(partial D)|B_(q,H)|
 <=C_D q H^(1-sigma_-)+O_D(q log H).                     (4.15)
```

This is enormously larger than the `q log H` threshold in (4.10).  Raising
`q` does not reverse the comparison because both the support gain and the
outer nonlinear bill are multiplied by `q`.  This is the contour form of
the unique-zero growth trilemma in R153 and the high-jet room condition in
R172.

## 5. A late-supported arithmetic countermodel

The preceding theorem was conditional on a zeta zero.  The following
unconditional model shows that its compensation mechanism is compatible
with positive ordinary Dirichlet coefficients and a fixed near-one divisor.

Fix an integer `L>=1` and a zeta zero

```text
rho_0=1/2+i gamma_0.                                     (5.1)
```

Put

```text
w_L(s)=1+L(s-1),
rho_L=1+(rho_0-1)/L
     =1-1/(2L)+i gamma_0/L.                              (5.2)
```

For a prime cutoff `X`, define

```text
F_(L,X)(s)
 =zeta(w_L(s)) product_(p<=X)(1-p^[-w_L(s)]).            (5.3)
```

The finite head is nonzero at `rho_L`, so `F_(L,X)` has there the fixed
zero inherited from `rho_0`, independently of `X`.  Its added head-factor
zeros lie on

```text
Re(s)=1-1/L,                                             (5.4)
```

strictly to the left of `rho_L`.  A fixed thin domain joining `rho_L` to a
right cap can therefore avoid those zeros, the pole at `1`, and every other
transformed zeta zero.

In `Re(s)>1`, (5.3) has the ordinary Dirichlet expansion

```text
F_(L,X)(s)
 =sum_(n>=1, p|n => p>X)n^(L-1)(n^L)^(-s).              (5.5)
```

Let

```text
H=X^L.                                                    (5.6)
```

Every nonconstant index `n^L` in (5.5) is larger than `H`, and every
coefficient is positive.  Moreover,

```text
F_(L,X)'/F_(L,X)
 =-L sum_(p>X)sum_(k>=1)(log p)
       p^[k(L-1)](p^(kL))^(-s).                          (5.7)
```

It follows exactly as in Section 4 that

```text
B_(q,L,X)=(1-F_(L,X))^(q-1)F_(L,X)'/F_(L,X)             (5.8)
```

has one-sign Dirichlet coefficients, support beyond `H^q`, residue one at
`rho_L` when `rho_0` is simple, and on every fixed right arc
`Re(s)>=1+a`,

```text
|B_(q,L,X)(s)|<=C_(a,L)^qH^(-qa)log H.                  (5.9)
```

As `L` grows, the fixed zero line in (5.2) approaches one.  Theorem 4.1
forces the omitted contour norm to grow, and the model pays that bill.  Thus
there is no abstract theorem saying that a fixed near-one divisor is
incompatible with positive `H^q`-late right data.

This model is deliberately not a substitute for zeta: its affine dilation
changes the degree and the center of the functional equation.  Its role is
logical.  Any successful one-sided theorem must use the degree-one zeta
functional equation and its coefficients jointly, not merely late support,
positivity, meromorphic continuation, and a functional equation in the
abstract.

## 6. Functional-equation reflection restores the linear target channel

The same conservation can be seen algebraically for the actual function
(4.1).  Write the zeta functional equation as

```text
zeta(s)=chi(s)zeta(1-s)                                  (6.1)
```

and define

```text
A_H(s)=chi(s)P_H(s)/P_H(1-s).                            (6.2)
```

Then, away from the displayed divisors,

```text
F_H(s)=A_H(s)F_H(1-s).                                   (6.3)
```

Put

```text
v(s)=F_H(1-s)=A_H(s)^(-1)F_H(s).                        (6.4)
```

Since `v'/v=F_H'/F_H-A_H'/A_H`, direct differentiation gives the exact
identity

```text
B_(q,H)(1-s)
 =-(1-v)^(q-1)[F_H'/F_H-A_H'/A_H].                       (6.5)
```

Let

```text
C_q(v)=[(1-v)^(q-1)-1]/v,                               (6.6)
```

with its removable value at zero.  Expanding (6.5),

```text
B_(q,H)(1-s)
 =-F_H'/F_H+A_H'/A_H
  -v C_q(v)[F_H'/F_H-A_H'/A_H].                         (6.7)
```

At an `F_H`-zero, the last term is analytic because
`vF_H'/F_H` is analytic, and `A_H'/A_H` is regular on a target-isolating
disc.  The entire target pole in the reflected response is therefore the
first, linear term

```text
-F_H'/F_H.                                               (6.8)
```

That term has only the original support beyond `H`, not the nonlinear
support beyond `H^q`.  Subtracting it leaves the delayed terms but removes
the target pole.  This is the one-function analogue of R159's exact
target/reflected-delay split.

There is also a large head multiplier hidden in (6.2).  At a fixed point
`s=1+a+it`,

```text
log|P_H(1-s)|=a theta(H)+o(H),                           (6.9)
```

while `P_H(s)` converges to a finite nonzero Euler product.  Hence one
orientation of `A_H` or its inverse has size `exp(aH+o(H))`.  Reflection
does not turn the right-tail estimate into a second small boundary estimate;
it exports the finite-head growth to the reflected side.

## 7. The exact surviving contour target

The strongest remaining version is not an `L^infinity` theorem.  From
(2.10), (4.6), and (4.8), a hypothetical target zero forces

```text
integral_C log^+|(s-rho)B_(q,H)(s)| domega_rho(s)
 >=qa omega log H-O_D(q+log log H).                      (7.1)
```

Accordingly, the one-sided route would close if one could prove, from the
actual zeta coefficients and uniformly under the target-zero hypothesis, a
strict upper bound of the form

```text
integral_C log^+|(s-rho)B_(q,H)(s)| domega_rho(s)
 <=qa omega log H-cq log H                               (7.2)
```

for some fixed `c>0` and an admissible sequence of `q,H` and contours.
This is a coefficient-specific Nevanlinna/Hardy estimate on the
**uncontrolled** boundary.  It is substantially weaker than bounding the
full supremum, but it is not supplied by the functional equation, standard
zeta growth, or late support on `E`.

Outer-function extremals and the dilated-zeta model prove that (7.2) cannot
follow from local meromorphy, the target residue, positivity, and support
alone.  Some new signed or phase-sensitive fact about the actual prime head
would be required.

Thus the contour idea produces a useful sharpened target, but not a fixed
zero-free strip.  The full Hardy mode is protected; every attempt to read it
from only the right boundary pays the same information back through harmonic
measure on the left boundary and connectors.
