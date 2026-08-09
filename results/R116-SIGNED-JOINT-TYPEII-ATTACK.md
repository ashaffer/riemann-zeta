# R116 signed joint Type-II conductor collapse and primitive dual gate

Status: a new conductor-sensitive theorem is proved for the exact smooth
`Q_h` hyperbola fold.  On a balanced squarefree semiprime modulus, all
nonprimitive multiplier classes together are smaller than the physical top
scale by a square root.  The remaining primitive class has an exact
metaplectic/Poisson dual: it is the ordinary, slowly varying
`mu(d)Lambda(b)` Type-II sum, up to the same square-root error.  After exact
Vaughan recompletion this is a smooth logarithmically weighted Mertens sum.
Thus the low-conductor obstruction in R113 is removed, but the primitive
block still requires genuinely new Mobius cancellation.  No fixed zero-free
strip is proved or disproved.

Date: 2026-08-07.

Predecessors:

* [`SIGNED-JOINT-RECIPROCAL-COMPRESSION-GATE.md`](SIGNED-JOINT-RECIPROCAL-COMPRESSION-GATE.md)
  for the exact `Type-II - gamma` field and the zero-orbit obstruction;
* [`R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md`](R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md)
  for the actual `mu(d)Lambda(b)` top block;
* [`R113-R105-MULTIPLIER-AVERAGE-FAIL-FAST-AUDIT.md`](R113-R105-MULTIPLIER-AVERAGE-FAIL-FAST-AUDIT.md)
  for product-fiber Parseval and the previously unresolved modular aliases;
* [`R114-NUMERATOR-COMPLETION-AND-TRANSITION-GATE.md`](R114-NUMERATOR-COMPLETION-AND-TRANSITION-GATE.md)
  for the coefficient-uniform numerator-completion boundary; and
* [`FULL-R71-RECIPROCAL-RESPONSE-GATE.md`](FULL-R71-RECIPROCAL-RESPONSE-GATE.md)
  for the identification of `-gamma` with the punctured slow axis.

## 1. Verdict

The useful off-wall operation is to refrain from estimating the folded
multiplier profile one residue at a time.  Keep the complete signed `Q_h`
profile and use two-dimensional Poisson summation on the congruence

```text
j theta = a (mod c).                                  (1.1)
```

The exact vanishing of the first kernel marginal removes the zero Fourier
row after Poisson.  Compact physical support removes the zero Fourier
column.  If the additive phase in `F_c(a)` has conductor

```text
q=c/(a,c),                                            (1.2)
```

the resulting hyperbola fold is of square-root size in **q**, not in `c`.
Combining this with R113's product-fiber Parseval gives

```text
sum_(a: conductor(a)=q) F_c(a)V_c(a)
  <<c^epsilon q.                                      (1.3)
```

For the actual balanced semiprime moduli

```text
c=p r,             p,r asymp sqrt(c),                 (1.4)
```

all proper conductors are `1,p,r`.  Hence their complete contribution is

```text
<<c^(1/2+epsilon).                                    (1.5)
```

This proves that the modular-zero aliases and every other nonprimitive
alias are not the top-box obstruction once the signed profile is recombined
before Cauchy.  In particular, no separate power estimate for `F_c(0)` is
needed.

There is also an exact answer for the remaining conductor `q=c`.  If
`gamma_c(z)` is the inverse-product Vaughan convolution modulo `c`, then

```text
sum_(a mod c)F_c(a)V_c(a)
 =c sum_z gamma_c(z) Phi_c(z/c)+O(c^(1/2+epsilon)),    (1.6)

Phi_c(x)=sum_(m,n) What(m,n)e(-mnx).                  (1.7)
```

Equivalently, for the actual coefficients,

```text
main(c)
 =c sum_(d,b)
    mu(d)Lambda(b)/(db)^(1+it) Phi_c(db/c).           (1.8)
```

The inverse phase has disappeared.  The surviving integers `m,n` are
bounded physical aliases and `Phi_c(db/c)` is a fixed-scale smooth function
of `db/c`.  Summing `Lambda(b)` by the PNT turns (1.8), at low Mellin
frequency, into a smooth dyadic Mobius sum.  Exact Vaughan recompletion uses

```text
(mu*Lambda)(n)=-mu(n)log n                            (1.9)
```

and turns the same block into the usual logarithmically weighted Mertens
carrier.  Vinogradov--Korobov supplies a subpower gain here.  A fixed power
is fixed-strip strength.

Thus the new mechanism makes a real reduction:

```text
modular zero and proper conductors       POWER-SAVED;
primitive reciprocal conductor          EXACTLY DUALIZED;
primitive dual ordinary Type-II sum      MERTENS-SENSITIVE;
fixed zero-free strip                     STILL OPEN.  (1.10)
```

## 2. The complete signed profile

The argument is most transparent after fixed-ratio scaling.  Let
`L(t,u)` be a compactly supported smooth kernel in the positive quadrant,
and assume the exact signed marginal identity

```text
integral_R L(t,u)dt=0                   for every u.   (2.1)
```

For the R102/R104 kernel this is not an assumption: it follows from applying
`Q_h` to the field before localization.  The other marginal also vanishes,
although only (2.1) is needed below.

After absorbing fixed ratio constants into the coordinates, the R81 line
profile is

```text
W(sigma,tau)
 =integral_R L(y+sigma,y)e(tau y)dy.                  (2.2)
```

All statements remain uniform when the arguments of `L`, `sigma`, `tau`
are multiplied by constants in a fixed compact subset of `(0,infinity)`.
This covers `c/X`, both denominator ratios, every fixed output block, and
the finite `Q_h` translate family.

Use the Fourier convention

```text
What(xi,eta)=double_integral W(sigma,tau)
                         e(-xi sigma-eta tau)d sigma d tau. (2.3)
```

Integrating first in `tau` gives the exact identity

```text
What(xi,eta)
 =e(xi eta)integral_R L(t,eta)e(-xi t)dt.             (2.4)
```

Consequently:

```text
What(0,eta)=0;                                        (2.5)

What(xi,eta)=0 unless eta lies in a fixed compact
positive interval;                                   (2.6)

abs What(xi,eta)<<_A (1+abs(xi))^(-A)                 (2.7)
```

for every fixed derivative order admitted by the window.  R104's scale
seminorm supplies (2.7) for every fixed `A` once the fixed-order B-spline is
chosen above `A`.  Piecewise-polynomial knots cause only the already
recorded bounded-variation constants.  The proof may alternatively be made
first after an arbitrarily small smoothing and then passed to the R104
limit.

Equation (2.5) is where the signed `-gamma` contact is used.  Without first
recombining the three `Q_h` translates, the individual profiles need not
satisfy it and the theorem below has a full zero-row term.

## 3. Conductor-sensitive hyperbola folding

Let `c` be squarefree and comparable to the physical scale.  For a divisor
`q|c`, put `s=c/q`.  If `q>1` and `u` is a unit modulo `q`, define

```text
V_(c,q)(u)
 =sum_(j,theta in Z;
       j theta =s u mod c)W(j/c,theta/c).             (3.1)
```

For `q=1`, define

```text
V_(c,1)(0)=sum_(c|j theta)W(j/c,theta/c).             (3.2)
```

These are exactly the residue folds whose additive phase has conductor
`q`.  No dyadic triangle in `j` or `theta` has been taken.

### Theorem 3.1 (signed conductor square root)

Uniformly for squarefree `c`, divisors `q|c`, and `(u,q)=1`,

```text
abs V_(c,q)(u)<<_epsilon c^epsilon sqrt(q).           (3.3)
```

For `q=1`, the right side is read as `c^epsilon`.

### Proof

The elementary divisor identity

```text
1_(s|j theta)
 =sum_(d|s)sum_(e|s/d)mu(e)
      1_(de|j)1_(s/d|theta)                           (3.4)
```

is exact.  Indeed, for fixed `j` the inner Mobius sum selects
`d=(s,j)`, after which `s/d|theta` is precisely `s|j theta`.

Put

```text
A=de,              B=s/d.                            (3.5)
```

Because `(s,q)=1`, both `A` and `B` are units modulo `q`.  Writing
`j=A v`, `theta=B w`, the remaining congruence is

```text
v w=u' (mod q),                 (u',q)=1.             (3.6)
```

Poisson summation in the two residue progressions gives

```text
sum_(v w=u' mod q)W(Av/c,Bw/c)

 =c^2/(ABq^2) sum_(m,n in Z)
    What(mc/(Aq),nc/(Bq)) S_q(m,n*u';q),              (3.7)
```

up to harmless sign choices in the Kloosterman arguments.  Here

```text
S_q(m,n;q)=sum_(x mod q)^* e_q(mx+n inverse(x)).      (3.8)
```

The support statement (2.6) forces

```text
Bq asymp c                                             (3.9)
```

and leaves only `O(1)` possible nonzero integers `n`.  Equation (2.5)
kills `m=0`.  For the remaining terms, the composite Weil bound and (2.7)
give

```text
abs S_q(m,n*u';q)
 <<q^(1/2+epsilon)(m,n,q)^(1/2),                      (3.10)

sum_(m!=0)abs What(mc/(Aq),nc/(Bq))
 <<_A (Aq/c)^A.                                      (3.11)
```

The bounded nonzero `n` give `(m,n,q)^(1/2)<<_W 1`, even when `q` has
small prime factors.  Substitution in (3.7), using (3.9), yields

```text
abs(grid_(A,B))
 <<q^(1/2+epsilon)(Aq/c)^(A-1)
 <<q^(1/2+epsilon).                                  (3.12)
```

There are at most `tau_3(s)=c^o(1)` grids in (3.4), proving (3.3).

When `q=1`, (3.7) is ordinary rectangular Poisson summation.  Statements
(2.5)--(2.7) give the same proof with the Kloosterman factor replaced by
one.  QED.

The theorem is stronger than applying Weil after treating each integer
alias independently.  It says that the square root is the square root of
the **reduced conductor**.  In particular, the apparent no-oscillation
class `a=0 mod c` has size `c^o(1)`, not `c^(1/2)` or `c`.

### Corollary 3.2 (native fixed-ratio parameter bridge)

In the unrecombined R105 display, Mellin separation places the factors
`d^(-it)b^(-it)` in the Vaughan coefficients and the complementary Mellin
factor in `nu_t`.  Theorem 3.1 must not be applied after taking an absolute
value in `t`.  Recombine that integral first.  On a fixed-ratio product box
the resulting profile is a family

```text
W_x(sigma,tau),             x=db/c in [x_0,x_1],      (3.13)
```

with (2.5)--(2.7) uniform in `x`.  The dependence on `log x` is smooth in
the Banach seminorm consisting of the support bound, the zero-row identity,
and the fixed number of `xi` derivatives used in Theorem 3.1.

Choose a smooth cutoff equal to one on `[log x_0,log x_1]`, periodicize it,
and take its vector-valued Fourier series.  Two integrations by parts in
`log x` give an absolutely summable decomposition

```text
W_x=sum_(ell in Z) omega_ell(x) W_ell,

sum_ell N_A(W_ell)<<N_(A,2)(W),
omega_ell(x)=x^(i lambda_ell).                        (3.14)
```

Every `W_ell` still satisfies `What_ell(0,eta)=0`, because Fourier
coefficient extraction is linear and the zero row vanishes for every `x`.
Moreover

```text
omega_ell(db/c)
 =c^(-i lambda_ell)d^(i lambda_ell)b^(i lambda_ell), (3.15)
```

so it only changes the unimodular phases of `alpha_d` and `beta_b`.
Their `l2` norms and the integer-product fiber bound are unchanged.

The compact R81 line integral has the required two log-ratio derivatives;
R104's fixed scale seminorm includes the spline knots, and the finite `Q_h`
translate sum changes the norm by only a fixed factor.  Consequently
Theorem 3.1 and Section 4 below apply to the actual fixed-ratio R105 family
with the projective cost in (3.14), not merely to a profile artificially
frozen at one value of `db/c`.

## 4. Product-fiber Parseval plus the conductor theorem

On the R105 square-root box let

```text
F_(c,q)(u)
 =sum_(d in I_D,b in I_B;(db,c)=1)
    alpha_d beta_b e_q(u inverse(db)),                (4.1)

D,B asymp sqrt(c),
norm(alpha)_2 norm(beta)_2<<c^(-1/2+epsilon).         (4.2)
```

For the actual coefficients,

```text
alpha_d=mu(d)d^(-1-it),
beta_b=Lambda(b)b^(-1-it),                            (4.3)
```

and (4.2) is R113 (2.5).

Every residue class modulo `q` contains only

```text
<<(1+c/q)c^epsilon                                   (4.4)
```

admissible pairs `(d,b)`: the integer product `db` lies in a fixed-multiple
interval of length `O(c)`, giving `O(1+c/q)` integer lifts, and each lift
has divisor-many factorizations.  Additive Parseval therefore proves

```text
sum_(u mod q)abs F_(c,q)(u)^2
 <=q(1+c/q)c^epsilon
        norm(alpha)_2^2 norm(beta)_2^2
 <<c^epsilon.                                        (4.5)
```

This is the conductor-uniform version of R113 Lemma 3.1.

For any `Q<=c`, (4.5), Theorem 3.1, and Cauchy give the general low-conductor
ledger

```text
sum_(q|c;q<=Q)
 abs sum_(u mod q)^*F_(c,q)(u)V_(c,q)(u)
 <<c^epsilon Q.                                      (4.6)
```

Thus every conductor `q<=c^(1-delta)` is power-saved, for every squarefree
`c`.  More specifically, all proper conductors together cost at most

```text
<<c^(1+epsilon)/P^-(c),                              (4.7)
```

where `P^-(c)` is the least prime factor.  The balanced-semiprime case is
the clean endpoint `P^-(c)asymp sqrt(c)`.

### Corollary 4.1 (all proper conductors on a semiprime)

Let

```text
c=p r,              p!=r,       p,r asymp sqrt(c).    (4.8)
```

For a conductor `q|c`, put

```text
C_q=sum_(u mod q)^*F_(c,q)(u)V_(c,q)(u).              (4.9)
```

Then

```text
abs C_q<<c^epsilon q.                                (4.10)
```

Indeed, (4.5), Theorem 3.1, and Cauchy give

```text
norm(F_(c,q))_2<<c^epsilon,
norm(V_(c,q))_2<<c^epsilon q.                        (4.11)
```

The proper divisors of `c` are `1,p,r`, so

```text
sum_(q|c;q<c)abs C_q<<c^(1/2+epsilon).               (4.12)
```

This closes the modular-zero class for every squarefree modulus, every
fixed-power-low conductor by (4.6), and all proper conductors for the
balanced squarefree semiprime family.  It is essential
that all `theta` shells be recombined before (3.1).  A separate dyadic
absolute value destroys (2.6) and restores the old folding loss.

The finite tail coefficient `a_(U,V)(c)` can be nonzero on nonsquarefree
`c`, even though the completed coefficient `-mu(c)log c` is squarefree.
Accordingly, Theorem 3.1 applies directly either to the squarefree tail
subfamily or after the exact Type-I/Vaughan recompletion.  It is not
permission to delete the nonsquarefree tail before that recombination.

## 5. Exact primitive duality

It remains to understand `q=c`.  Put

```text
gamma_c(z)=sum_(db=z mod c)alpha_d beta_b,             (5.1)

F_c(a)=sum_(z mod c)^*gamma_c(z)e_c(a inverse(z)).    (5.2)
```

For a unit `a`, both `j` and `theta` in (1.1) are units modulo `c`.
Poisson summation in their residue classes gives the exact expansion

```text
V_c(a)
 =sum_(m,n in Z)What(m,n)S_c(m,na;c).                  (5.3)
```

The support of `n` is finite by (2.6), and `m=0` is absent by (2.5).

### Theorem 5.1 (primitive reciprocal-to-ordinary transform)

Let `c=pr` satisfy (4.8), with `p,r` larger than the fixed second-frequency
support in (2.6).  Then

```text
sum_(a mod c)^*F_c(a)V_c(a)

 =c sum_(z mod c)^*gamma_c(z)
      sum_(m,n)What(m,n)e_c(-mnz)
  +O_epsilon(c^(1/2+epsilon)norm(gamma_c)_1).         (5.4)
```

For the actual coefficients, `norm(gamma_c)_1<=c^epsilon`.

### Proof

Insert (5.2)--(5.3).  The inner sum over `a` and the Kloosterman variable
`x` is

```text
H_c(m,n;z)
 =sum_(x mod c)^*e_c(mx)
    sum_(a mod c)^*e_c[a(inverse(z)+n inverse(x))].   (5.5)
```

The `a`-sum is the Ramanujan sum

```text
c_c(inverse(z)+n inverse(x))
 =sum_(d|(c,inverse(z)+n inverse(x)))d mu(c/d).       (5.6)
```

The term `d=c` has the unique solution

```text
x=-nz (mod c)                                        (5.7)
```

and contributes

```text
c e_c(-mnz).                                         (5.8)
```

For `c=pr`, CRT factorization makes the proper-divisor contribution at a
fixed `m` at most

```text
<<p(r,m)+r(p,m)+(p,m)(r,m).                           (5.9)
```

For example, the `d=p` condition fixes `x mod p`; summing the remaining
unit coordinate modulo `r` gives the Ramanujan sum `c_r(m)`, of magnitude
`(r,m)` up to an absolute factor.  The other two terms are identical or
easier.  Thus (5.9) is `O(p+r)` when `(m,c)=1`.  If `p|m` or `r|m`, it can
be larger, but (2.7) supplies an arbitrary fixed inverse power of that
prime.  Summing `m` and the finitely many `n` therefore gives

```text
sum_(m,n)abs What(m,n)
  abs[H_c(m,n;z)-c e_c(-mnz)]
 <<c^(1/2+epsilon).                                  (5.10)
```

Sum (5.10) with `abs(gamma_c(z))`.  QED.

Combining Theorem 5.1 with (4.12) yields the complete-residue statement

```text
sum_(a mod c)F_c(a)V_c(a)

 =c sum_(d,b)alpha_d beta_b Phi_c(db/c)
   +O(c^(1/2+epsilon)),                               (5.11)

Phi_c(x)=sum_(m,n)What(m,n)e(-mnx).                  (5.12)
```

Fixed ratio changes replace `Phi_c` by a uniformly bounded family of smooth
profiles.  Formula (5.11) is the main structural result of this report.
It is the joint estimate which separate `l2` bounds could not see.

The square-root error is a genuine win.  The main term is also a precise
reality check: complete reciprocal cancellation has rotated the critical
block into a slowly varying ordinary product phase; it has not made it
small.

## 6. What the actual coefficients become

Substituting (4.3) in (5.11) gives

```text
M_c(t)
 =c sum_(d asymp sqrt(c),b asymp sqrt(c))
    mu(d)Lambda(b)/(db)^(1+it) Phi_c(db/c).           (6.1)
```

At bounded `t`, smooth PNT summation in `b` gives uniformly for
`d asymp sqrt(c)`

```text
sum_b Lambda(b)/b^(1+it) Phi_c(db/c)
 =G_(c,t)(d/sqrt(c))
  +O(exp{-C(log c)^(3/5)(loglog c)^(-1/5)}),          (6.2)
```

where `G_(c,t)` is a fixed-scale smooth profile.  Therefore

```text
M_c(t)
 =c sum_(d asymp sqrt(c))
      mu(d)d^(-1-it)G_(c,t)(d/sqrt(c))
  +c exp{-C(log c)^(3/5)(loglog c)^(-1/5)}.           (6.3)
```

The displayed Vinogradov--Korobov shape may absorb fixed powers of
logarithms.  It is `c^(1-o(1))`, not `c^(1-delta)`.

There is an even more invariant form.  When the complementary Vaughan heads
are restored before estimating, the exact identity

```text
sum_(db=n)mu(d)Lambda(b)=-mu(n)log n                  (6.4)
```

turns every product-dependent smooth weight into

```text
-c sum_n mu(n)log(n)n^(-1-it)Phi_c(n/c).              (6.5)
```

The omitted heads are precisely the Type-I and evaluated-center pieces
already tracked in R102--R105.  The `Q_h` operation kills the rank-two
center but does not kill the zero carriers in (6.5).

A bound

```text
sum_(d asymp D)mu(d)d^(-1)G(d/D)<<D^(-delta)          (6.6)
```

for a scale-stable detector family whose Mellin transforms have no common
zero continues `1/zeta(s)` through `Re(s)>1-delta`.  Conversely a zeta zero
`rho` contributes at scale `D^(rho-1)` whenever the Mellin response of `G`
at `rho` is nonzero.  R102's detector multiplier

```text
[exp(h(rho-1/2))-exp(h/2)]^2                          (6.7)
```

is nonzero for every nontrivial zeta zero, and the R80 bank supplies the
needed scale/frequency coverage for the complete field.  Thus a uniform
fixed power in (6.3)--(6.5) is not an elementary corollary of PNT; it is the
fixed-strip theorem in its remaining smooth-Mobius form.

This conclusion does **not** prove that the primitive main term cannot
cancel after summing `c`, all fixed-ratio blocks, and all Type-I cross terms.
It proves exactly where such a new cancellation must act.

## 7. Multiplicative characters and exceptional zeros

The character expansion confirms the same boundary.  On the unit group
modulo `q`, define

```text
tau_q(u,chi)=sum_(x mod q)^*chi(x)e_q(ux).             (7.1)
```

Fourier inversion gives

```text
F_(c,q)(u)
 =1/phi(q) sum_(chi mod q)tau_q(u,chi)
     A_c(chi)B_c(chi),                                (7.2)

A_c(chi)=sum_d alpha_d chi(d),
B_c(chi)=sum_b beta_b chi(b).                         (7.3)
```

For the principal character and `u=0`, (7.2) is exactly the unoscillated
product `A_c(chi_0)B_c(chi_0)`.  Theorem 3.1 shows why this coefficient need
not be estimated separately: its **signed kernel multiplier** is small.

For the completed, product-dependent convolution one has

```text
sum_n [(mu chi)*(Lambda chi)](n)n^(-s)
 =-L'(s,chi)/L(s,chi)^2
 =(1/L(s,chi))'.                                      (7.4)
```

A zero of `L(s,chi)` of multiplicity `r` gives a pole of order `r+1` in
(7.4).  Thus a real exceptional character is not a favorable missing case;
its near-one zero makes the derivative reciprocal larger.  Burgess bounds
for a bare character sum do not bound the two factors in (7.3) with a fixed
power uniformly through this pole.  A character-by-character proof would
ask for uniform zero-free regions for Dirichlet `L`-functions, stronger than
the zeta-only target and obstructed by the possible exceptional real
character.

The additive conductor theorem avoids this detour entirely.  It uses Weil
only after the signed zero row has vanished, and it leaves the zeta-specific
primitive Mobius block visible rather than replacing it by a family of
Dirichlet-L problems.

## 8. Reciprocity and varying-modulus dispersion

Additive reciprocity says

```text
e_c(k inverse(z))
 =e(k/(cz))e_z(-k inverse(c)).                        (8.1)
```

On `c,z asymp X` this is self-dual: it exchanges two variables of the same
size.  The slowly varying factor in (8.1) is exactly what becomes
`e_c(-mnz)` in Theorem 5.1 after the complete hyperbola packet is summed.
Thus reciprocity does not lower the primitive conductor; (5.11) is its
completion-preserving form.

A varying-`c` large sieve applied after Cauchy also stops at the same point.
The outer Vaughan coefficient has

```text
sum_(c asymp X)abs h(c)^2=X^(-1+o(1)),                (8.2)
```

while the primitive diagonal in (5.11) is of physical size `X` before a
Mobius saving.  Squaring removes the outer Mobius signs and retains that
diagonal.  Standard dispersion can control the off-diagonal moduli, but it
does not supply a fixed power for (6.3).

There remains one legitimate global possibility:

```text
sum the signed outer h(c), the primitive ordinary-product main term,
the Type-I heads, and all fixed-ratio blocks before any Cauchy step.      (8.3)
```

A fixed power in (8.3) would be a new two-scale Mobius correlation theorem.
Neither the ordinary additive large sieve, separate character estimates,
nor conductor lowering proves it.  Failure of those tools is not a theorem
that (8.3) is false.

## 9. Updated exponent ledger

On the balanced semiprime top box, the exact ledgers are now

```text
product-fiber norm of F at every conductor q       c^o(1);
signed Q_h hyperbola fold, pointwise               q^(1/2)c^o(1);
joint conductor-q block                            q c^o(1);
all q<c                                             c^(1/2+o(1));
primitive q=c                                      c times smooth
                                                   mu-Lambda Type II;
primitive completion error                         c^(1/2+o(1));
known VK gain on primitive Mobius dual             c^(-o(1));
required complete top bound                        c^(1-delta).       (9.1)
```

This improves R113 in two ways.

1. The modular-zero class does not require a standalone Mertens estimate;
   the exact signed profile suppresses it.
2. The remaining endpoint is not an amorphous correlation of two unrelated
   `l2` vectors.  It is explicitly the ordinary smooth Mobius Type-II form
   (6.1), or the weighted Mertens form (6.5) after recompletion.

It also explains why R114's numerator completion stops at the transition.
Numerator completion sees only Parseval.  The additional square-root gain
for proper conductors comes from the missing zero Fourier row (2.5), while
the primitive Fourier matrix rotates that gain into the ordinary product
main term rather than shrinking it.

## 10. Disposition and next theorem

The signed joint attack has therefore made measurable progress but has not
proved the requested strip:

```text
signed -gamma / zero-row recombination                  USED EXACTLY;
modular-zero alias                                      POWER-SAVED;
all proper conductors on balanced semiprimes            POWER-SAVED;
primitive reciprocal block                              EXACTLY DUALIZED;
character/exceptional route                             WORSE TARGET;
separate varying-modulus dispersion                     ENDPOINT;
global primitive Mobius correlation                     OPEN;
fixed strip or no-strip conclusion                      NOT PROVED.    (10.1)
```

The next valid target is narrower than R113 (6.2).  Prove, with the actual
finite family of `Phi_c` from (5.12), a fixed power for

```text
sum_(c asymp X) h(c)c
  sum_(d,b)mu(d)Lambda(b)/(db)^(1+it)Phi_c(db/c),      (10.2)
```

jointly with the exact Vaughan heads and before Cauchy in `c`.  Proper
conductors may now be discarded at the proved cost `X^(1/2+o(1))`.  A
successful proof of (10.2) would be genuinely new arithmetic information
at the primitive conductor; another residue-folding or separate-`l2`
argument cannot supply it.
