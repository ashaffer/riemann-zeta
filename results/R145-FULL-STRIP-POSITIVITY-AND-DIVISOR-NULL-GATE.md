# R145 full-strip positivity and divisor-null gate

## Status

R144 found a nonnegative degree-zero virtual character which deletes every
bounded-support Frobenius in the prime head.  This report tests whether its
remaining signed divisor can be removed by unconditional explicit-formula
positivity, Artin holomorphy, a bank of virtual masks, or reciprocal
nonlinearization.

All four automatic closures fail for exact reasons.

1.  A test function whose zero-quartet response is nonnegative throughout
    the full critical strip must decay by `sech(x/2)` on the prime side.
    Its local weight is at most `2/(n+1)`, so it recovers exactly the
    Poitou `log X` scale and can never supply the GRH `sqrt(X)` scale.
2.  Every pointwise-nonnegative degree-zero virtual character has
    anti-effective Artin conductor.  Gamma cancellation therefore leaves a
    finite-conductor term of the sign needed to pay for the missing head.
3.  Even assuming Artin holomorphy, the abstract order constraints permit a
    regular-character zero pattern which cancels *every* degree-zero detector
    at a Riemann zero simultaneously.
4.  Reciprocal derivative jets *do* inherit the exact deleted Euler head:
    their signed coefficients are coefficientwise dominated by the positive
    direct jets.  The obstruction is no longer the signed Euler estimate.
    It is the divisor side: a reciprocal only exchanges a zero for a pole,
    and a finite jet can be flattened by the uncontrolled regular Laurent
    germ while leaving that divisor in place.

The squarefree-discriminant parity mask is the most favorable special case:
its virtual conductor is exactly `1`.  It still carries a quadratic
numerator zero ledger and a Dedekind denominator pole ledger of normalized
size `O(log rd(K))`.  Unconditional Poitou forces that same ledger to be at
least logarithmic in the head length, leaving no surplus.

```text
full-strip-positive test-function decay        sech(x/2), SHARP
unconditional local prime weight               O(1/n), SHARP
unconditional discriminant gain                O(log X), MAXIMAL HERE
degree-zero nonnegative Artin conductor         ANTI-EFFECTIVE
squarefree parity virtual conductor             EXACTLY 1
regular-order simultaneous mask cancellation   ALGEBRAICALLY ADMISSIBLE
Artin/Dedekind holomorphy closure               INSUFFICIENT
direct reciprocal closure                      LAURENT-CONDITIONED
reciprocal signed Euler tail                    CONTROLLED
target-specific signed divisor theorem          OPEN
fixed uniform zeta zero-free strip              NOT PROVED
zeros approaching one                           NOT PROVED
```

Date: 2026-08-08.

Predecessor:
[`R144-BOUNDED-SUPPORT-VIRTUAL-CHARACTER-ANNIHILATOR.md`](R144-BOUNDED-SUPPORT-VIRTUAL-CHARACTER-ANNIHILATOR.md).

## 1. Explicit-formula convention

Let `F:R->R` be even and have enough exponential integrability for the
following bilateral Laplace transform:

```text
Phi_F(s)=integral_R F(x) exp[(s-1/2)x] dx.                   (1.1)
```

A zero `rho=beta+i gamma`, together with its functional-equation and
conjugate partners, contributes through

```text
Re Phi_F(beta+i gamma)
 =integral_R F(x) cosh[(beta-1/2)x] cos(gamma x) dx.         (1.2)
```

The corresponding prime-power term has the shape

```text
Lambda(n)n^(-1/2)F(log n).                                  (1.3)
```

Under GRH only `beta=1/2` is sampled.  Unconditionally, discarding the zero
side by positivity requires (1.2) to be nonnegative for the entire strip.

## 2. Full-strip positivity forces Poitou decay

**Theorem 2.1.**  Suppose

```text
Re Phi_F(beta+i t)>=0           for 0<beta<1 and all t in R. (2.1)
```

Then

```text
|F(x)|<=F(0)/cosh(x/2).                                      (2.2)
```

Consequently

```text
n^(-1/2)|F(log n)|<=2F(0)/(n+1).                            (2.3)
```

**Proof.**  Fix `0<a<1/2` and put

```text
G_a(x)=F(x)cosh(a x).                                       (2.4)
```

By (1.2), the Fourier transform of `G_a` is nonnegative.
Bochner's theorem makes `G_a` positive definite.  Positivity of its
`2 by 2` Gram matrix gives

```text
|G_a(x)|<=G_a(0)=F(0).                                      (2.5)
```

Let `a` increase to `1/2` to obtain (2.2).  Substituting `x=log n`
gives (2.3).  QED.

The partial-strip form is also exact.  Positivity only for

```text
|beta-1/2|<A                                                (2.6)
```

forces

```text
|F(x)|<=F(0)sech(Ax),                                       (2.7)
n^(-1/2)|F(log n)|
 <=2F(0)/[n^(1/2+A)+n^(1/2-A)].                             (2.8)
```

The square-root prime weight occurs only at `A=0`, when the zeros have
already been confined to the critical line.  Whole-strip positivity has
`A=1/2` and necessarily pays `1/n`.

Poitou's kernel realizes equality at the exponent level.  Writing

```text
F(x)=f(x)/cosh(x/2)                                         (2.9)
```

turns a local term into

```text
2 log(NP)/(NP)^(j/2) F(j log NP)
 =4 log(NP)/[1+(NP)^j] f(j log NP).                         (2.10)
```

This is precisely the local correction in Brueggeman--Doud,
[*Local corrections of discriminant bounds and small degree extensions of
quadratic base fields*](https://doi.org/10.1142/S1793042108001389),
Propositions 2.2--2.3.  Summing (2.10) through `X` gives only `O(log X)`.

**Corollary 2.2.**  No explicit-formula proof which makes each possible
off-critical zero quartet nonnegative can derive a `sqrt(X)` discriminant
penalty from splitting through `X`.  Such an improvement must exploit the
actual signed zero configuration.  Replacing it by universal positivity is
an RH-strength assumption in another form.

The functional-equation-odd part of a test does not evade the theorem: it
cancels on the zero quartets and, for a self-dual object, on the two-sided
prime sum as well.

## 3. Nonnegative degree zero means anti-effective conductor

Let `Theta` be a virtual character with

```text
Theta(1)=0,               Theta(g)>=0 for every g.           (3.1)
```

At a ramified prime, with lower ramification groups `I_i`, the Artin
conductor exponent is

```text
a_p(Theta)
 =sum_(i>=0)|I_i|/|I_0|
   [Theta(1)-1/|I_i| sum_(g in I_i)Theta(g)]<=0.             (3.2)
```

Thus

```text
q(Theta)<=1.                                                 (3.3)
```

Every exact R144 falling-support mask has property (3.1).  Total reality and
degree zero cancel its Gamma factor, but (3.2) normally leaves a negative
finite-conductor constant in the logarithmic derivative.  The same
pointwise positivity which deletes the head fixes the sign of this debt.

For the natural `S_m` parity mask,

```text
L(s,Theta_S)=zeta(s)^(m-1)L(s,chi_sign)/zeta_K(s),           (3.4)
q(Theta_S)=d_(chi_sign)/D_K<=1.                              (3.5)
```

The conductor contribution is

```text
1/2 log q(Theta_S)
 =-1/2 log[D_K/d_(chi_sign)].                               (3.6)
```

At the real evaluation point used in a missing-head argument, (3.6) can
cancel the pole at one as soon as

```text
log rd(K)>>log X.                                            (3.7)
```

This is exactly the unconditional Poitou scale, not the sub-square-root
scale needed by R141.

## 4. The squarefree parity exception

Suppose the natural `S_m` field `K` has squarefree discriminant and every
inertia group is tame transposition inertia.  The parity class function
vanishes on every inertia element, and

```text
d_(chi_sign)=D_K,
q(Theta_S)=1.                                                (4.1)
```

Thus the finite-conductor escape disappears exactly.  This is the most
favorable possible parity detector.

It still does not isolate zeta.  In

```text
D_S=(m-1)D_zeta+D_(chi_sign)-D_(zeta_K),                     (4.2)
```

a numerator zero of `zeta` or `L(s,chi_sign)` has negative residue, while a
denominator zero of `zeta_K` has positive residue.  Along the real axis a
real denominator zero has the wrong sign to cancel the pole at one, but
ordinary complex zeros acquire arbitrary phase in higher derivatives and
in nonsymmetric smoothed formulae.

Moreover the varying quadratic numerator has `O(log D_K)` zeros in every
fixed-height ledger.  After division by the source multiplicity `m-2`, its
absolute cost is

```text
O(log rd(K)+log T).                                         (4.3)
```

The same is true of the Dedekind denominator.  The conductor cancellation
in (4.1) is a *signed* cancellation; it does not cancel the absolute zero
ledger.  A crude numerator-zero forcing argument would require

```text
log rd(K)=o(log X),                                         (4.4)
```

whereas R144's unconditional Poitou theorem already forces

```text
log rd(K)>=(4-o(1))log X.                                   (4.5)
```

The two estimates meet at the same exponent.  Squarefree discriminant
removes a constant term but leaves no quantitative surplus.

## 5. The regular-order null direction

The local divisor problem cannot be solved by Artin formalism or by adding
more degree-zero masks.

Fix a nontrivial zero `rho` of `zeta` of order `e>0`.  Write a hypothetical
Artin order character as

```text
H_rho=sum_(chi in Irr(G)) n_chi chi,
n_1=e.                                                       (5.1)
```

For a subgroup `H`, Dedekind holomorphy requires

```text
<H_rho,Ind_H^G 1>=ord_rho zeta_(E^H)>=0.                    (5.2)
```

Let `reg` be the regular character.  Both patterns

```text
H_0=e reg,                                                   (5.3)
H_N=e*1+N(reg-1),                 N>=0,                      (5.4)
```

have trivial coefficient `e`, nonnegative irreducible coefficients, and
satisfy every inequality (5.2), since a degree-`d` permutation character
has order

```text
e d                                  for H_0,
e+N(d-1)                             for H_N.                (5.5)
```

These patterns are not asserted to occur for an actual extension.  Their
role is decisive: they are fully compatible with Artin holomorphy and every
formal Dedekind order constraint.

Now let `phi` be any exact mask with

```text
phi(1)=0,
a_1=<phi,1>>0.                                               (5.6)
```

Since

```text
<phi,reg>=phi(1)=0,
<phi,reg-1>=-a_1,                                           (5.7)
```

we obtain

```text
<phi,H_0>=0,
<phi,H_N>=a_1(e-N).                                         (5.8)
```

Thus the proportional order pattern (5.3) cancels every degree-zero mask
simultaneously.  With `N>e`, even the sign reverses.  This remains true for
an arbitrarily large bank of falling-factorial, parity, two-set, exterior,
or tensor masks.

For the R144 falling-support bank the first explicit adverse direction is
already the standard representation.  If

```text
a_0(m,q)=E_(g in S_m) (m-Fix(g))_q,                         (5.9)
```

then Frobenius reciprocity for the point stabilizer gives

```text
<f_q,Std>=a_0(m-1,q)-a_0(m,q)
          =-q m^(q-1)+O_q(m^(q-2))<0                       (5.10)
```

for fixed `q` and large `m`.  A sufficiently large standard-representation
zero multiplicity therefore defeats every fixed bounded-`q` bank.  Adding
exterior powers changes this particular direction but cannot change the
regular-character identity (5.7).

**Corollary 5.1.**  Neither Artin holomorphy, Dedekind holomorphy, nor
Heilbronn-character inequalities can prove the target residue lower bound
required by R144.  One needs an analytic independence or joint-zero theorem
which excludes the regular-order null direction for the actual fields.

## 6. Why adding a small degree does not repair it

The null direction in Section 5 exists because every exact identity mask
has degree zero.  Add a virtual character of nonzero degree `d`.  Under the
proportional order pattern (5.3), it acquires target order `ed`, but its
coefficient at the identity is also exactly `d`.

Consequently the normalized target residue and the leakage from every
completely split head prime carry the same calibration factor.  At the
high-jet point, the identity-prime contribution is evaluated at the Euler
radius `r`, while the target zero is farther away.  Suppressing the former
therefore suppresses the latter at least as strongly.  This is the linear
representation version of R141's one-sign calibration theorem.

Exact identity deletion, zero archimedean degree, and immunity to the
proportional order pattern cannot be obtained simultaneously by adding a
small genuine representation.

## 7. Reciprocal jets: Euler closure succeeds, divisor closure fails

Let `F` be any Euler quotient for which

```text
A=-F'/F                                                     (7.1)
```

has nonnegative Dirichlet coefficients and the required exact deleted head.
Put `g=1/F` and, for `j>=0`,

```text
P_j=(-1)^j F^(j)/F,              Q_j=g^(j)/g.               (7.2)
```

**Theorem 7.1 (reciprocal coefficient domination).**  Every `P_j` has
nonnegative Dirichlet coefficients and

```text
|coeff_n Q_j|<=coeff_n P_j                 for every n.     (7.3)
```

Both sides retain the exact deleted head.

**Proof.**  Direct differentiation gives

```text
P_(j+1)=A P_j-P_j',             Q_(j+1)=A Q_j+Q_j'.         (7.4)
```

Starting with `P_0=Q_0=1`, multiplication by the nonnegative series `A`
preserves coefficientwise domination.  On a Dirichlet coefficient,
differentiation multiplies by `-log n`; hence `-P_j'` is nonnegative and
`|coeff_n Q_j'|=(log n)|coeff_n Q_j|<=coeff_n(-P_j')`.
Induction proves (7.3).  All nonconstant coefficients in either recurrence
are generated from the support of `A`, so exact rough support is inherited.
QED.

Thus the same incomplete-Gamma Euler-tail estimate which controls the
positive direct jet controls the signed reciprocal jet.  The Type-II sign
problem on the coefficient side is genuinely gone in this exact-head
setting.

The divisor problem is not.  If locally

```text
F(s)=(s-rho)^mu h(s),                  h(rho) != 0,          (7.5)
```

then

```text
F^(j)/F
 =sum_(ell=0)^j binom(j,ell)(mu)_ell
      (s-rho)^(-ell) h^(j-ell)/h.                           (7.6)
```

The pair `(F,1/F)` detects either sign of a nonzero integer `mu`: one
orientation has a pole of every sufficiently high derivative order.  But
the regular-character pattern (5.3) permits `mu=0` for every mask at once.
Even when `mu!=0`, the regular germ can flatten any prescribed finite jet.

Indeed, fix an observation point `z_* != rho` and an integer `N`.  Let `T_N`
be the degree-`N` Taylor polynomial at `z_*` of
`-mu log(s-rho)`, and set

```text
F_N(s)=(s-rho)^mu exp[T_N(s)].                              (7.7)
```

This function retains the divisor `mu` at `rho`, but

```text
F_N(s)/F_N(z_*)=1+O((s-z_*)^(N+1)).                         (7.8)
```

All derivatives of both normalized orientations through order `N` vanish
at `z_*`.  This local countermodel does not claim that `F_N` is an Artin
Euler product; it proves that divisor location and multiplicity alone give
no finite-jet lower bound.  Such a bound must control the global regular
germ, which is precisely the old remote-divisor/Cauchy ledger.

Passing directly to `1/F` therefore makes denominator zeros into harmless
zeros but makes desired numerator zeros into poles whose leading coefficient
contains the complete analytic Laurent unit.  Head support and Euler
positivity give no lower bound for that unit.  The finite-head example

```text
1/zeta(s) product_(p<=X)(1-p^(-s))^(-1)                     (7.9)
```

has a pole at every zeta zero and an Euler series supported on `X`-rough
integers, while its pole coefficient can be exponentially ill-conditioned.
This is R142's Laurent-conditioning obstruction in its simplest form.

The scale-invariant nonlinear quantities

```text
(1/L)^(j)/(1/L)                                             (7.10)
```

remove the Laurent-unit scale.  They retain generic simple poles at the
zeros which their leading falling factorial was meant to cancel.  A closer
auxiliary zero then beats any gain in pole order exponentially.  Exact head
deletion makes the signed Euler coefficients easier to upper-bound, but it
does not remove those closer singularities or the regular-order cancellation
in Section 5.

Scalar common-divisor constructions return R142's spurious hypersurface;
vector constructions return its corona lower bound.  None supplies the
missing target-specific divisor theorem.

## 8. Verdict

R145 closes the universal explicit-formula route at the exact exponent:

```text
positivity for all possible zero quartets
        => sech(x/2) prime kernel
        => 1/n local weight
        => log X discriminant information.                  (8.1)
```

It also proves that the virtual Artin divisor cannot be controlled by
representation theory alone.  The regular-character order pattern is a
common null direction for every degree-zero detector and is compatible with
all standard holomorphy inequalities.

The surviving possibilities are therefore genuinely arithmetic:

1. construct many cheap prescribed-Frobenius `A_m/S_m` fields and prove that
   their actual Artin order vectors cannot all lie near the null direction;
2. prove a target-conditioned signed zero correlation which uses the actual
   phases rather than full-strip positivity; or
3. prove an unconditional field-discriminant lower bound stronger than
   Poitou for the coefficient-specific bounded-support pattern.

Each would be new.  Neither a fixed zeta zero-free strip nor its negation has
been proved.

Successor:
[`R146-FROBENIUS-ENTROPY-AND-INERTIA-ADJOINT-GATE.md`](R146-FROBENIUS-ENTROPY-AND-INERTIA-ADJOINT-GATE.md).
