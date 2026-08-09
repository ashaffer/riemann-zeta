# R174 exact-divisor peak and contour-conditioning gate

## Status

There is an elementary way to make the analytic target left open by the
transition-hull obstruction globally compatible.  Let `Omega` be a fixed
simply connected localization domain, let `Z` have a fixed nonempty divisor,
and let

```text
q(s)=exp[a(1-s)]                                         (0.1)
```

be one-to-one on a neighborhood of the closed localization domain.  On a
fixed right cap, approximate the local branch

```text
-Log Z-L_H                                                (0.2)
```

by a delayed polynomial `P_H(q)`, where `L_H` is any holomorphic head
logarithm which is uniformly bounded on a slightly larger cap.  Then

```text
h_H=L_H+P_H(q(s)),             G_H=Z exp(h_H)             (0.3)
```

has exactly the divisor of `Z` and satisfies

```text
G_H=1+O(H^(-A))                                          (0.4)
```

on the cap.  The optional target relative to the head is the entire
`q`-polynomial `P_H`; consequently its trace on a completed `q`-contour is
automatically compatible with the filled polynomial hull.  It can be chosen
with degrees between `N` and `(1+d)N`, where `N` is comparable to `log H`.

This positive result does **not** have fixed-power contour conditioning.
There is a sharp qualitative reason.  For every exact-divisor family

```text
G_H=Z exp(h_H),             |G_H-1|<=epsilon_H            (0.5)
```

on a fixed cap, quantitative analytic continuation around one retained zero
gives

```text
osc_K h_H >= c epsilon_H^(-alpha)                        (0.6)
```

on a fixed larger bridge.  Equivalently, on any fixed enclosing contour
`Gamma`,

```text
 max_Gamma |exp h_H|
 -------------------  >= exp[c epsilon_H^(-alpha)].      (0.7)
 min_Gamma |exp h_H|
```

Here `c,alpha>0` depend only on the fixed geometry and on `Z`.  Thus cap
accuracy `epsilon_H=H^(-A)` forces logarithmic oscillation at least a fixed
power `H^(A alpha)`.  In particular it is impossible to combine (0.4) with

```text
sup_K |h_H-h_H(s_*)|=O(log H),                           (0.8)
```

or with the two-sided contour bound

```text
H^(-lambda) <= |exp h_H| <= H^lambda.                    (0.9)
```

The explicit delayed-polynomial construction has the correct scale: it
gives `sup |h_H|<=H^beta` and hence only stretched-exponential conditioning
`exp(+-H^beta)`.  Its full-contour lower bound is nonzero and its winding is
exactly the divisor of `Z`, but a polynomial lower bound and a polynomial
upper bound cannot hold simultaneously.

The conclusion is specific and limited.  It closes the hoped-for
`O(log H)` logarithm / polynomially conditioned exact-divisor input for the
`GL_2` and connected-hull route.  It does not close a version which permits
the already budgeted fixed-power **logarithmic** growth `|h_H|<=H^beta`.

```text
exact-divisor cap peak                                    THEOREM
delayed polynomial in the exponential q-coordinate       THEOREM
global filled-hull compatibility                          THEOREM
full-contour nonvanishing and correct winding             EXACT
cap error H^(-A) with h oscillation O(log H)              IMPOSSIBLE
two-sided multiplier conditioning H^(+-lambda)            IMPOSSIBLE
necessary contour condition number                        exp(c H^(A alpha))
fixed-power logarithmic growth |h_H|<=H^beta              AVAILABLE
arithmetic optional-prime realization at that scale       OPEN
fixed uniform zeta zero-free strip                        NOT PROVED
zeros approaching Re(s)=1                                 NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R168-FINITE-UNION-LATE-SUPPORT-AND-TRANSITION-HULL-GATE.md`](R168-FINITE-UNION-LATE-SUPPORT-AND-TRANSITION-HULL-GATE.md),
[`R170-HIGH-GIRTH-TRANSFER-DETERMINANT-AMPLIFIER.md`](R170-HIGH-GIRTH-TRANSFER-DETERMINANT-AMPLIFIER.md),
and
[`R171-CAP-NORMALIZED-UNIT-SUM-AND-MATRIX-ESCAPE-AUDIT.md`](R171-CAP-NORMALIZED-UNIT-SUM-AND-MATRIX-ESCAPE-AUDIT.md).

## 1. Fixed geometry and notation

Let `Omega` be simply connected and let `Z` be a nonzero holomorphic
function on `Omega`.  Assume that `Z` has at least one zero.  Fix nested
right-cap discs

```text
B_0 compactly contained in B_1 compactly contained in
Omega\div(Z),                                             (1.1)
```

and a smooth Jordan domain

```text
D compactly contained in Omega                           (1.2)
```

which contains `B_1` and at least one zero of `Z`, while `Z` has no zero on
`partial D`.  All constants below may depend on this fixed geometry.

For a compact set `K` and a holomorphic function `h`, write

```text
osc_K h=inf_(c in C) sup_(s in K)|h(s)-c|.               (1.3)
```

This is the correct branch-invariant size for a logarithm: replacing `h` by
`h+2 pi i k` does not change either `exp h` or (1.3).

We use one standard quantitative continuation fact.  If a fixed finite
chain of overlapping discs joins a disc `E` to a compact set `K`, then
there are `C>=1` and `theta in (0,1)` such that every function `f`
holomorphic on a neighborhood of the chain satisfies

```text
sup_K |f|
 <=C [sup_E |f|]^theta
       [max(1,sup_(chain)|f|)]^(1-theta).                (1.4)
```

This follows by iterating Hadamard three-circles, exactly as in R169,
Section 4.  Covering a fixed compact curve by finitely many final discs
gives the same statement with `K` equal to that curve.

## 2. Monodromy forces a power-sized logarithm

### Theorem 2.1 -- exact-divisor logarithm propagation barrier

There are a compact bridge `K compactly contained in D` and constants
`c>0`, `alpha>0` with the following property.  Let `0<epsilon<1/4`, let
`h` be holomorphic on `Omega`, and put

```text
G=Z exp h.                                                (2.1)
```

If

```text
sup_(B_1)|G-1|<=epsilon,                                 (2.2)
```

then

```text
osc_K h >= c epsilon^(-alpha).                           (2.3)
```

#### Proof

Choose a zero `rho` of `Z`, of multiplicity `m>=1`, and a small positively
oriented circle `gamma` around `rho` containing no other zero.  Join `B_0`
to `gamma` by a fixed tubular chain which avoids all zeros of `Z`.  Enlarge
the chain slightly while remaining in `D\div(Z)`, and include its closure
in `K`.

On `B_1`, equation (2.2) permits the branch

```text
ell=Log G,                 |ell|<=2 epsilon.             (2.4)
```

Define on the zero-free chain

```text
f=ell'=h'+Z'/Z.                                          (2.5)
```

Although the notation `ell'` initially comes from `B_1`, the right side of
(2.5) is a single-valued holomorphic function everywhere on the chain.
Cauchy's estimate on the nested cap discs gives

```text
sup_(B_0)|f|<=C_0 epsilon.                               (2.6)
```

Subtract from `h` a constant attaining (1.3) up to a factor two.  Cauchy's
estimate on the slightly enlarged chain, together with boundedness of
`Z'/Z` there, gives

```text
sup_(chain)|f|<=C_1[1+osc_K h].                          (2.7)
```

Apply (1.4) from `B_0` to `gamma`.  For fixed `C_2` and
`theta in (0,1)`,

```text
sup_gamma |f|
 <=C_2 epsilon^theta[1+osc_K h]^(1-theta).               (2.8)
```

But the logarithmic residue cannot be propagated away:

```text
integral_gamma f(s) ds
 =integral_gamma h'(s) ds+integral_gamma Z'(s)/Z(s) ds
 =2 pi i m.                                              (2.9)
```

Therefore `sup_gamma|f|` is bounded below by the fixed positive number
`2 pi m/length(gamma)`.  Rearranging (2.8) proves (2.3) with

```text
alpha=theta/(1-theta).                                   (2.10)
```

QED.

The proof is a quantitative version of the elementary obstruction to a
single-valued logarithm of `Z`.  The cap says that `h` almost equals the
local branch `-Log Z`.  Continuing its derivative around a retained zero
must accumulate the missing residue.  A globally holomorphic `h` can do
this only by becoming nonnormal between the cap and the zero.

### Corollary 2.2 -- contour condition-number lower bound

After enlarging the fixed Jordan domain slightly if necessary, there is
`c_1>0` such that

```text
log {max_(partial D)|exp h|/min_(partial D)|exp h|}
 >=c_1 epsilon^(-alpha).                                 (2.11)
```

Indeed, the logarithm of the quotient on the left is exactly

```text
osc_(partial D) Re h
 :=max_(partial D)Re h-min_(partial D)Re h.               (2.12)
```

On a fixed compact subset of `D`, Borel--Caratheodory, or equivalently a
disc-chain estimate for a harmonic conjugate normalized at one point,
gives

```text
osc_K h<=C_D osc_(partial D) Re h.                       (2.13)
```

Combine (2.3) and (2.13).

In particular, if `epsilon=H^(-A)`, then

```text
condition number_(partial D)(exp h)
 >=exp[c_1 H^(A alpha)].                                 (2.14)
```

No constants `lambda,A>0` can therefore make both

```text
|G-1|<=H^(-A)                       on B_1,
H^(-lambda)<=|exp h|<=H^lambda      on partial D          (2.15)
```

hold for all large `H`.  The second line would make the logarithm in
(2.11) at most `2 lambda log H`, contradicting (2.14).

The same argument rules out `osc_Kh=O(log H)` directly.  Notice that this
is stronger than an argument-principle slogan: it supplies the unavoidable
conditioning scale.

### Corollary 2.3 -- what a one-sided contour bound costs

Winding does not prohibit a lower bound by itself.  What (2.14) says is
that the opposite side must then be very large.  For example, if

```text
min_(partial D)|exp h|>=H^(-lambda),                     (2.16)
```

then

```text
max_(partial D)|exp h|
 >=H^(-lambda)exp[c_1H^(A alpha)].                       (2.17)
```

Conversely, a polynomial upper bound forces a stretched-exponentially
small lower bound.  This is the precise full-contour reality check needed
by a Rouche argument.

## 3. A hull-compatible delayed polynomial construction

The preceding theorem does not say that a cap-normalized exact-divisor
family is impossible.  It says that such a family must pay a power in its
**logarithm**.  We now give an explicit construction at that scale.

Assume that (0.1) is one-to-one on a neighborhood of `closed D`, and write
`Phi` for its holomorphic inverse on a neighborhood of `q(closed D)`.  Let
`L_H` be a family holomorphic on a neighborhood of `closed D`.  Suppose
there is a fixed `q`-disc

```text
Delta_1={|q-q_*|<=r_1}                                   (3.1)
```

whose inverse image lies in the zero-free right cap and on which

```text
Psi_H(q)=-Log Z(Phi(q))-L_H(Phi(q))                      (3.2)
```

is holomorphic and uniformly bounded.  Fix a smaller concentric disc
`Delta_0` of radius `r_0<r_1`.  Since the exponential never vanishes, take
`Delta_1` small enough that

```text
mu=min_(Delta_1)|q|>0.                                   (3.3)
```

### Theorem 3.1 -- delayed entire-q cap peak

There are a fixed integer `d>=1` and constants `C,c,beta_0>0` such that,
for every integer `N>=1`, there is a polynomial

```text
P_(H,N)(q)=sum_(n=N)^(N+dN)c_(n,H,N)q^n                 (3.4)
```

satisfying

```text
sup_(Delta_0)|P_(H,N)-Psi_H|<=C exp(-cN),                (3.5)
sup_(q(closed D))|P_(H,N)|<=C exp(beta_0N).              (3.6)
```

The constants are independent of `H` whenever the bound in (3.2) is.

#### Proof

On `Delta_1`, put

```text
F_(H,N)(q)=q^(-N)Psi_H(q).                               (3.7)
```

Its supremum is at most `C mu^(-N)`.  Let `Q_(H,N)` be the Taylor
polynomial of degree `dN` about `q_*`.  Cauchy's estimate gives

```text
sup_(Delta_0)|F_(H,N)-Q_(H,N)|
 <=C mu^(-N)(r_0/r_1)^(dN).                             (3.8)
```

Define

```text
P_(H,N)(q)=q^NQ_(H,N)(q).                               (3.9)
```

It has the delayed support (3.4).  If
`R_0=max_(Delta_0)|q|`, then its error is bounded by

```text
C[(R_0/mu)(r_0/r_1)^d]^N.                               (3.10)
```

Choose `d` once so that the bracket is less than one.  This proves (3.5).
The same Cauchy coefficient bounds, now evaluated on the fixed compact
`q(closed D)`, give (3.6).  QED.

Take

```text
N=ceil[(A+1)c^(-1)log H]                                (3.11)
```

and define

```text
h_H(s)=L_H(s)+P_(H,N)(q(s)),
G_H(s)=Z(s)exp(h_H(s)).                                  (3.12)
```

Equations (3.2) and (3.5) imply

```text
sup_(Phi(Delta_0))|G_H-1|<<H^(-A).                       (3.13)
```

Every exponential in (3.12) is a unit, so

```text
div G_H=div Z                                             (3.14)
```

with multiplicity.  Most importantly for R168, the target relative to the
head is not a discontinuous left/right prescription:

```text
h_H-L_H=P_(H,N)(q).                                      (3.15)
```

It is an entire function of `q`.  Hence it extends across every filled
polynomial hull in the `q`-plane.  This is the strongest possible form of
hull compatibility.

If conjugation symmetry is required, apply the construction simultaneously
on the conjugate cap pair and symmetrize the polynomial as in R168.  The
same exponential estimates and delayed support remain valid.

### 3.1 Size ledger

Equation (3.6) and `N comparable to log H` give

```text
sup_D |P_(H,N)(q(s))|<=H^(beta+o(1))                     (3.16)
```

for a fixed `beta>0`.  If

```text
sup_D |L_H|<=H^(eta+o(1)),                               (3.17)
```

then

```text
sup_D |h_H|<=H^(max(beta,eta)+o(1)).                     (3.18)
```

This is fixed-power logarithmic growth, not `O(log H)` growth.

For the finite Euler head

```text
L_H(s)=sum_(p<=H)Log(1-p^(-s)),                          (3.19)
```

the family is uniformly bounded on every fixed cap in `Re(s)>1`.  If the
left edge of `D` is `Re(s)=1-a>1/2`, the elementary prime-sum estimate gives

```text
sup_D |L_H|<=H^(a+o(1)).                                 (3.20)
```

Thus (3.17) holds in the actual optional-prime geometry.  The construction
lands exactly in the fixed-power logarithmic ledger already recorded in
R166--R171.

The coefficient `ell^1` norm of (3.4) is at most `exp(CN)=H^C`, not
exponentially small.  The theorem is therefore an analytic target theorem,
not yet an actual-prime realization theorem.  Any arithmetic lift must
compare this coefficient demand with the available block capacity and with
the high-girth support gain.

## 4. Full-contour divisor and conditioning ledger

Let `Gamma=partial D`.  Since `Z` has no zero there, (3.12) gives the exact
nonvanishing bound

```text
min_Gamma|G_H|
 >=min_Gamma|Z| exp[-sup_Gamma|Re h_H|]>0.               (4.1)
```

Using (3.18), the explicit guaranteed scale is only

```text
exp[-H^(beta_*+o(1))]
 <= |G_H|/|Z|
 <= exp[H^(beta_*+o(1))]                                 (4.2)
```

for a fixed `beta_*>0`.  On the other hand,

```text
(1/(2 pi i))integral_Gamma G_H'/G_H ds
 =(1/(2 pi i))integral_Gamma Z'/Z ds,                    (4.3)
```

because the integral of `h_H'` vanishes.  Thus the winding is exactly the
number of retained zeros of `Z` in `D`, with multiplicity.  No artificial
zero or pole was introduced.

Equations (4.1)--(4.3) answer the topological part cleanly:

```text
global hull compatibility     yes,
correct nonzero winding       yes,
nonvanishing on the contour   yes,
power conditioning            no.                        (4.4)
```

The failure is not an artifact of the Taylor construction.  Corollary 2.2
shows that every exact-divisor construction with cap error `H^(-A)` has
condition number at least `exp(cH^(A alpha))` on a fixed enclosing contour.

## 5. Consequences for the matrix and connected-hull routes

The transition-hull obstruction in R168 can be avoided only by replacing
the incompatible cutoff with one globally holomorphic target.  Theorem 3.1
does exactly that, and even makes the relative target an entire delayed
polynomial in `q`.  Therefore polynomial-hull topology is no longer the
remaining objection at the abstract analytic level.

The price is unavoidable.  A retained divisor and power-small cap error
force fixed-power logarithmic escape.  Consequently:

1. A `GL_2` split may use this target only in the `exp(H^beta)` matrix-size
   regime, not with polynomially bounded matrix entries and inverses.
2. A connected-hull prime approximation must carry a target whose
   logarithmic size is a fixed power of `H`; a theorem for uniformly bounded
   targets or `O(log H)` logarithms is insufficient.
3. A Rouche step which assumes both a polynomial upper bound and a
   polynomial boundary gap for the exact-divisor multiplier is impossible.
   One-sided conditioning remains logically possible only by paying the
   stretched-exponential cost on the other side.
4. The remaining viable question is arithmetic and exponent-specific:
   can the optional-prime block capacity and high-girth support gain absorb
   the necessary `H^(A alpha)` logarithmic excursion while preserving the
   determinant cofactor?  This report neither proves nor disproves that
   stronger statement.

Thus the desired strongly conditioned analytic input has failed fast, but
the larger fixed-power-logarithm program remains open.
