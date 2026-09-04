# Primitive shifted cubes: congruence and pair-Fourier audit

**Date:** 2026-08-28  
**Binary verdict:** the estimate `N_prim(P)<<P^(9/16+epsilon)` is not
proved.  Gcd normalization converts every stratum to a unit cubic
congruence, but the standard multiplicative large sieve gives `P^(1+o(1))`
in the hardest stratum, losing `P^(7/16)`.  Pairing the transition points
produces a plausible sharp correlation theorem with main term `T^2`, but
elementary factorization loses a factor `P`; additive Fourier analysis
isolates two wild prime-power frequency strata for which no licensed
estimate is available.

## 1. Frozen primitive transition

Fix positive constants

```text
alpha<=beta,        lambda<=Lambda,        eta>0,
```

and put

```text
T=P^(9/16),         H=P^(7/16),            T*H=P.
```

Let `N_prim(P)` count integer quadruples satisfying

```text
alpha*T<=A,B<=beta*T,
lambda*P<=u<=Lambda*P,
gcd(A,B)=1,
A*u^3-B*P^3=Delta,          0<|Delta|<=eta*H.       (1.1)
```

The target is

```text
N_prim(P)<<_epsilon T*P^epsilon.                    (1.2)
```

All constants below may depend on the frozen shell constants.

## 2. Two exact gcd normalizations

Put

```text
g=gcd(u,P),       u=g*x,       P=g*y,       gcd(x,y)=1.
```

Then

```text
g^3|Delta,
e=Delta/g^3,
A*x^3-B*y^3=e,                 0<|e|<=E=eta*H/g^3. (2.1)
```

In particular

```text
g<=E_0=(eta*H)^(1/3),          y=P/g.                (2.2)
```

There are only `P^o(1)` possible `g`, since `g|P`.

Now define the cross-content

```text
d=gcd(A,y^3).                                             (2.3)
```

For every prime `l|y`, the fact that `x` is a unit modulo `l` gives

```text
v_l(e)=v_l(A)       if v_l(A)<3*v_l(y),
v_l(e)>=3*v_l(y)    if v_l(A)>=3*v_l(y).
```

Consequently the following equality, not merely a divisibility, holds:

```text
gcd(e,y^3)=gcd(A,y^3)=d.                                (2.4)
```

Write

```text
A=d*a,       e=d*f,       n=y^3/d.                       (2.5)
```

Then

```text
gcd(a,n)=gcd(f,n)=1,
a*x^3==f (mod n),
a~T/d,       0<|f|<=E/d.                                (2.6)
```

Since `d|e`, one has `d<=E`.  Hence

```text
n/y=y^2/d >= y^2/E=P^2*g/(eta*H)>>P^(25/16).             (2.7)
```

Thus every residue class modulo `n` meets the fixed `x~y` shell only
`O(1)` times.

## 3. The pointwise cube-root bound

For units modulo `n`, a soluble congruence `z^3==c (mod n)` is a coset of
the kernel of the cube map.  The kernel has size at most

```text
kappa_3(n)<=3^omega(n)<<_epsilon n^epsilon.              (3.1)
```

Indeed, the cube map is an automorphism on the unit group modulo a power
of `2`, while its kernel has at most three elements modulo every odd prime
power; the Chinese remainder theorem proves (3.1).

For fixed `(a,f)`, (2.6), (2.7), and (3.1) therefore leave at most
`P^epsilon` admissible `x`.  The number `B` is then uniquely determined by
(2.1).  If `N(g,d)` denotes the part of (1.1) with the specified contents,
then

```text
N(g,d)<<_epsilon (T/d)*(E/d)*P^epsilon
       <<P^(1+epsilon)/(g^3*d^2).                       (3.2)
```

This closes only strata satisfying `g^3*d^2>=H`.  In the unit stratum
`g=d=1`, it gives `P^(1+epsilon)`, losing the factor

```text
P/T=H=P^(7/16).                                          (3.3)
```

## 4. Exact multiplicative Fourier formula and its large-sieve limit

Let `mathcal A`, `mathcal F`, and `mathcal X` be the sets in (2.6), after
discarding elements that are not units modulo `n`.  Orthogonality of all
Dirichlet characters modulo `n` gives the exact relaxed congruence count

```text
C(g,d)=1/phi(n) * sum_(chi mod n)
       S_A(chi)*S_X(chi^3)*conj(S_F(chi)),               (4.1)
```

where

```text
S_A(chi)=sum_(a in mathcal A) chi(a),
S_F(chi)=sum_(f in mathcal F) chi(f),
S_X(chi^3)=sum_(x in mathcal X) chi(x)^3.                (4.2)
```

The principal contribution is tiny:

```text
|mathcal A|*|mathcal F|*|mathcal X|/phi(n)
 <<_epsilon 1/(P*g*d)*P^epsilon.                         (4.3)
```

The nonprincipal spectrum is the obstruction.  Here is the strongest
bound furnished by the standard fourth-moment large sieve at these
lengths.  Since

```text
(T/d)^2<n,             (E/d)^2<n,                       (4.4)
```

character orthogonality turns both fourth moments into literal product
equalities, rather than merely congruences.  The divisor bound gives

```text
sum_chi |S_A(chi)|^4 <<_epsilon phi(n)*(T/d)^2*n^epsilon,
sum_chi |S_F(chi)|^4 <<_epsilon phi(n)*(E/d)^2*n^epsilon. (4.5)
```

Moreover

```text
sum_chi |S_X(chi^3)|^2
 =phi(n)*#{x_1,x_2 in mathcal X:(x_1/x_2)^3==1 (mod n)}
 <<_epsilon phi(n)*y*n^epsilon.                          (4.6)
```

For (4.6), choose a cube root of unity modulo `n`; because the `x`-shell
has length `O(y)<n`, it gives at most `O(y)` pairs, and (3.1) bounds the
number of roots.

Holder with exponents `(4,2,4)` in (4.1) now proves

```text
C(g,d)<<_epsilon sqrt((T/d)*(E/d)*y)*P^epsilon
       <<P^(1+epsilon)/(g^2*d).                          (4.7)
```

But (4.7) divided by (3.2) is `g*d`.  Thus this standard separate-moment
character large sieve never improves the pointwise root bound on any
normalized stratum; at `g=d=1` the two bounds coincide at `P^(1+o(1))`.
The displayed moments therefore cannot close the problem through this
Holder step.  A successful Fourier theorem must use additional correlation
between the three transforms in (4.1).

## 5. Prime-square shadow and the carry

The obstruction is already present for `P=p` prime.  Then `g=d=1`, and
primitivity is equivalent to `gcd(A,Delta)=1`, because

```text
gcd(A,Delta)=gcd(A,B*p^3)=1.                             (5.1)
```

Write `u=s+j*p`, with `1<=s<=p-1` and `j` in a fixed finite set.  For the
Fermat quotient

```text
q_p(v)=(v^(p-1)-1)/p (mod p),                            (5.2)
```

one has, by direct binomial expansion,

```text
q_p(s+j*p)=q_p(s)-j/s (mod p).                           (5.3)
```

The necessary congruence `A*u^3==Delta (mod p^2)` is exactly equivalent to

```text
A*s^3==Delta (mod p),
q_p(A)+3*q_p(s)-3*j/s==q_p(Delta) (mod p).                (5.4)
```

Thus the first `p`-adic lift digit is a constrained Fermat-quotient
incidence.  The function `q_p(s)` on canonical representatives
`1<=s<p` is not a bounded-degree rational function over `F_p`; ordinary
Weil estimates do not apply.  Existing individual Heilbronn/Fermat-
quotient bounds do not estimate the constrained trilinear sum in (5.4).

## 6. Exact pair closure

For a fixed `u`, elimination gives

```text
P^3*(A_1*B_2-A_2*B_1)=A_2*Delta_1-A_1*Delta_2=O(P).
```

Hence the coefficient determinant vanishes for large `P`; primitivity
leaves at most one transition point over each `u`.

For two distinct transition points put

```text
c=A_1*A_2,
z=u_2^3-u_1^3,
D=A_1*B_2-A_2*B_1,
r=A_2*Delta_1-A_1*Delta_2.                              (6.1)
```

Then exactly

```text
c*z-D*P^3=-r,                  |r|<=C_0*P.               (6.2)
```

More precisely, let `Q(P)` count quadruples `(A_1,A_2,u_1,u_2)` in their
respective shells, with `u_1!=u_2`, for which there is an integer `D`
satisfying

```text
|A_1*A_2*(u_2^3-u_1^3)-D*P^3|<=C_0*P,                  (6.3)
```

without requiring that either endpoint is a transition.  The implication

```text
Q(P)<<_epsilon T^2*P^epsilon                            (PC)
```

would give

```text
N_prim(P)*(N_prim(P)-1)<=Q(P)
```

and hence (1.2), after replacing `epsilon` by `2*epsilon`.

Collapsing `A_1*A_2=c` costs only

```text
#{(A_1,A_2):A_1*A_2=c}<=tau(c)<<_epsilon P^epsilon.      (6.4)
```

Thus, for prime `P=p`, the core of `(PC)` is the unweighted statement

```text
#{c~X, u_1!=u_2~p, p does not divide c*u_1*u_2:
  ||c*(u_2^3-u_1^3)/p^3||<=C_0/p^2}
 <<_epsilon X*p^epsilon,             X=T^2=p^(9/8).      (6.5)
```

Its scale is sharp: its random main term is

```text
X*p^2*(p/p^3)=X.                                         (6.6)
```

Exact rational resonances can themselves contribute `asymp X`.  For
example, if `4|P`, then `(u_1,u_2)=(P,5P/4)` gives

```text
(u_2^3-u_1^3)/P^3=61/64,
```

and every `c==0 (mod 64)` is counted.  Therefore no valid proof may demand
power cancellation from every fixed input pair.

There is nevertheless exact self-reproduction along each fixed input
pair.  Fix `z!=0`, and suppose two triples `(c_i,D_i,r_i)` satisfy (6.2),
with `c_i~X` and `|r_i|<=C_0*P`.  Eliminating `z` gives

```text
P^3*(c_1*D_2-c_2*D_1)=c_1*r_2-c_2*r_1.                 (6.7)
```

The right side has magnitude `O(X*P)=O(P^(17/8))<P^3`.
It follows that both sides vanish.  Hence

```text
c_1*D_2=c_2*D_1,        c_1*r_2=c_2*r_1.                (6.8)
```

Thus every admissible `(c,D,r)` over one fixed `z` is an integral multiple
of a single primitive triple.  This is useful structure, but it does not
by itself sum the primitive rays over `z`: an exact resonance can have a
small primitive first coordinate (the denominator `64` example above),
and then contributes `asymp X` multiples.

In the prime unit branch, write that primitive triple as `(a,d,b)`, so

```text
c=t*a,       D=t*d,       r=t*b,       a*z-d*p^3=-b.     (6.9)
```

Here `b!=0`, since `p` does not divide `a*z`.  Moreover `gcd(a,b)=1`:
any common prime divisor would also divide `d*p^3`; it cannot be `p`, and
otherwise would contradict primitivity of the triple.  Since `c~X` and
`|r|<<p`, (6.9) gives the sharp ray constraints

```text
a>>X/p=p^(1/8),             |b|<<a*p/X=a*p^(-1/8).       (6.10)
```

The remaining pair theorem is equivalently a weighted count of these
nonzero primitive rays.  Constraints (6.10) alone still allow the crude
factor-`p` excess in (8.3).

## 7. Prime valuation audit for the pair congruence

Assume `P=p>3` is prime and restrict to actual transition inputs.  They
are units modulo `p`.  Let `v=v_p(z)` in (6.1); also `p` does not divide
`c`.

* If `v=2`, (6.2) first forces `p^2|r`, but `|r|<p^2` for large `p`, so
  `r=0`; it would then force `p^3|z`, a contradiction.  This stratum is
  empty.
* If `v=1`, then `r=p*r_0` with `|r_0|<=C_0`, and

  ```text
  c*(z/p)==-r_0 (mod p^2).                               (7.1)
  ```

  There are `O(p)` input pairs with `u_2^3==u_1^3 (mod p)`.  For each
  pair and each of `O(1)` values of `r_0`, (7.1) determines at most one
  `c<X<p^2`; after (6.4), this branch is `O(p^(1+epsilon))`, which is
  smaller than `X=p^(9/8)`.
* If `v>=3`, this branch is empty for distinct positive inputs in fixed
  `O(p)` shells, once `p` is large.  Indeed,

  ```text
  z=(u_2-u_1)*(u_2^2+u_1*u_2+u_1^2).
  ```

  If `p|(u_2-u_1)`, the second factor is a unit modulo `p` and the first
  factor, a nonzero integer of size `O(p)`, has `p`-adic valuation at most
  one.  If `p` does not divide the first factor, `p^3|z` would force the
  positive second factor, of size `O(p^2)`, to be divisible by `p^3`,
  which is impossible.  (The diagonal `u_1=u_2` was excluded.)

Thus the only unresolved prime branch is

```text
v_p(u_2^3-u_1^3)=0.                                     (7.2)
```

The unit restrictions in (6.5) are forced by actual prime-base
transitions.  Even if they are removed in the relaxed count, all new
branches are harmless.  If `p|c`, write `c=p*c_1`, where
`c_1~X/p=p^(1/8)<p`; the residual is `p*r`, `|r|=O(1)`, and

```text
c_1*(u_2^3-u_1^3)==r (mod p^2).                          (7.3)
```

For fixed `(c_1,u_1,r)`, the resulting cubic congruence for `u_2` has at
most three nonsingular roots modulo `p^2`; a right side of valuation one
has no cubic root, while a zero right side leaves only the `O(1)` multiples
of `p` in the input shell.  Hence this branch is
`O((X/p)*p)=O(X)`.  If `p` does not divide `c` but divides `z`, the
valuation-one branch has `O(p)` input pairs and determines `c` modulo
`p^2`, hence contributes `O(p)`; valuation two is impossible; and
valuation at least three has only `O(1)` nonunit input pairs and contributes
`O(X)`.  Thus the relaxed prime count also reduces to `p` not dividing
`c*z`.

Cross-content factors must still be retained for composite `P`; simply
treating all coefficients as units is not a valid uniform reduction.

## 8. Dyadic gap factorization and its exact loss

Write

```text
k=u_2-u_1,
u_2^3-u_1^3=k*(3*u_1^2+3*k*u_1+k^2).                    (8.1)
```

On a dyadic block `k~K`, the integer `D` in (6.2) has size

```text
D~X*K/P.                                                 (8.2)
```

For a fixed unit `c` and fixed `r=O(p)`, reduce (6.2) modulo `c`.  Since
`gcd(c,p)=1`, `D` occupies one residue class modulo `c`, and (8.2) leaves
`O(1)` possibilities after the input shells are fixed.  For each resulting
integer

```text
n=(D*p^3-r)/c,
```

the number of representations `n=u_2^3-u_1^3` is `O(tau(|n|))`: choose
the divisor `k=u_2-u_1` of `n`, and then the quadratic factor in (8.1)
determines `u_1` in at most two ways.  Therefore

```text
Q_p(c)<<_epsilon p^(1+epsilon),
Q_p<<_epsilon X*p^(1+epsilon).                           (8.3)
```

The factor `p` in (8.3) is precisely the summation over the possible
residuals `r`; factorization supplies no cancellation among the nearby
integers `D*p^3-r`.  The desired estimate is `X*p^epsilon`.

For actual transition pairs, one-point-per-input makes gaps
`K<=T^2/P=P^(1/8)` harmless by the elementary bound `O(P*K)<=T^2`.
The long gaps remain.

## 9. Exact prime-cube Fourier problem

Split the fixed input shell into `O(1)` intervals

```text
mathcal U_j={j*p+s: 1<=s<=p-1}
```

and harmless end pieces.  Put `q=p^3`, let `mathcal C` be the units in a
fixed `c~X` interval (the omitted nonunits were handled in Section 7), and
let `mathcal R=[-C_0*p,C_0*p] cap Z`.  Define

```text
S_j(a)=sum_(u in mathcal U_j) e_q(a*u^3),
Rhat(h)=sum_(r in mathcal R) e_q(-h*r).                  (9.1)
```

Additive orthogonality gives, for two digit intervals, the exact pair
count

```text
Q_(j_1,j_2)=1/q * sum_(h mod q) Rhat(h)
 sum_(c in mathcal C) S_(j_2)(h*c)*conj(S_(j_1)(h*c)),   (9.2)
```

with the `u_1=u_2` terms subtracted when `j_1=j_2`.  The `h=0` term is

```text
asymp (p*X*p^2)/p^3=X,                                  (9.3)
```

exactly the desired scale.

The depth-one frequencies `h=p^2*a`, `a!=0 (mod p)`, are harmless.  Here

```text
S_j(p^2*a*c)=sum_(s mod p) e_p(a*c*s^3),                 (9.4)
```

up to an end-piece completion.  Weil and completion give
`|S_j|<<sqrt(p)*log p`, while

```text
sum_(a mod p, a!=0)|Rhat(p^2*a)|<<p*log p.               (9.5)
```

Their total contribution to (9.2) is `O(X*p^(-1)*log^3 p)`.

The remaining frequencies `v_p(h)=0` and `v_p(h)=1` are wild.  The sums
in (9.1) run over one canonical base-`p` digit slice, not over a complete
`p`-adic residue ring.  In particular `S_j(1)` can have size comparable
to `p`; a uniform square-root stationary-phase estimate is false.

Even the essentially optimal global fourth moment does not give the
needed masked correlation.  Factoring sums of two cubes gives

```text
sum_(h mod p^3)|S_j(h)|^4<<_epsilon p^5*p^epsilon.       (9.6)
```

Indeed, orthogonality counts
`u_1^3+u_2^3==u_3^3+u_4^3 (mod p^3)`.  The shell permits only `O(1)`
multiples of `p^3`; for each fixed sum, factorization of
`u_1^3+u_2^3` bounds its representations by `O(tau(n))`, proving (9.6).
Applying Cauchy to (9.2) after summing over `c` loses the dependence between
`h` and the dilate `h*c` and remains far above `X`.

Thus the precise missing prime theorem is the centered, mask-sensitive
estimate

```text
sum_(h!=0 mod p^3) Rhat(h)
 sum_(c~p^(9/8))
 [S_(j_2)(h*c)*conj(S_(j_1)(h*c))-diagonal]
 <<_epsilon p^3*p^(9/8+epsilon).                        (9.7)
```

It must allow the exact resonances in Section 6 while controlling their
aggregate.  Separate Weyl, Burgess, Weil, VMVT, or character-moment bounds
do not imply (9.7).

## 10. Divisibility enumeration and the cubic-sieve gate

There is a second exact reorganization in the prime-base case.  For fixed
`A` and `Delta`, the divisibility

```text
A | B*p^3+Delta                                             (10.1)
```

puts `B` in one residue class modulo `A`.  Since both the `A`- and
`B`-shells have length and location `asymp T`, there are `O(1)` admissible
lifts.  Thus the multiset

```text
mathcal N={n=(B*p^3+Delta)/A:
           A,B~T, 0<|Delta|<=H, A|(B*p^3+Delta)}            (10.2)
```

has total multiplicity

```text
M=#mathcal N<<T*H<<p.                                       (10.3)
```

The transition condition is exactly that `n=u^3` with `u` in the input
shell.

This admits a rigorous power-sieve formulation.  Let `mathcal L` contain
`L` primes `ell==1 (mod 3)`, `ell` not dividing `p`, all of size
`p^(7/16+o(1))`, and choose a nontrivial cubic character `chi_ell` for
each.  If `n=u^3`, then `chi_ell(n)=1` unless `ell|u`; only `O(1)` primes
of this size can divide one `u~p`.  Expanding a square therefore gives

```text
R_cube
 << M/L + 1/L^2 * sum_(ell_1!=ell_2)
    |S(ell_1,ell_2)|,                                      (10.4)
```

where

```text
S(ell_1,ell_2)=sum_(n in mathcal N)
 chi_(ell_1)(n)*conj(chi_(ell_2)(n))                       (10.5)
```

with the multiplicities from (10.2).  There are at least `H` such primes
of size `H*p^o(1)`: for example, the prime number theorem in the fixed
progression `1 (mod 3)` supplies this many in `[Q,2Q]` for
`Q=H*(log H)^2` and all sufficiently large `p`.  Taking `L=floor(H)`,
the diagonal term in (10.4) is

```text
M/L<<p/H=T.                                                (10.6)
```

Consequently a uniform square-root estimate

```text
S(ell_1,ell_2)<<p^(1/2+epsilon)                            (10.7)
```

would more than close the transition.  Even the weaker right side
`T*p^epsilon` would suffice.

The correlation (10.5) is not an ordinary character sum of a polynomial.
To see the obstruction exactly, let `b_0=b_0(A,Delta)` be the representative
in `[0,A)` satisfying

```text
b_0*p^3+Delta==0 (mod A),
q_A(Delta)=(b_0*p^3+Delta)/A.                              (10.8)
```

All admissible lifts are `B=b_0+t*A`, with `t` in a set of `O(1)`
integers, and

```text
n=t*p^3+q_A(Delta).                                        (10.9)
```

The carry can also be written explicitly.  Let `k_A` be the representative
in `(0,A)` of `(p^3)^(-1) (mod A)` and write

```text
p^3*k_A=1+s_A*A.
```

For `0<Delta<A` (which includes the positive residual shell for large
`p`), direct substitution gives

```text
q_A(Delta)=p^3*ceil(k_A*Delta/A)-s_A*Delta.               (10.10)
```

There is an analogous floor formula for negative `Delta`.  Thus even on
one sign the phase contains a Beatty carry whose slope varies with `A`.

The map `q_A(Delta)` is the quotient/carry arising from inversion of
`p^3` modulo the **variable modulus** `A`.  Hence (10.5) is explicitly

```text
sum_(A~T) sum_(0<|Delta|<=H) sum_(admissible t)
 psi_(ell_1,ell_2)(t*p^3+q_A(Delta)),                     (10.11)
```

where `psi_(ell_1,ell_2)` is the CRT product character modulo
`ell_1*ell_2~H^2=p^(7/8+o(1))`.  Neither Weil's theorem nor the classical
cubic large sieve estimates (10.11): the argument of the character is a
Euclidean quotient with varying modulus, not a bounded-degree polynomial
over a fixed finite field.  Applying a generic cubic large sieve to all
integers `n~p^3` also loses the ambient interval length `p^3` and does not
use the sparse carry-defined support (10.2).

Thus the cubic sieve gives an appealing exact target, but (10.7) is a new
carry-correlation estimate.  Merely noting that a cube is a cubic residue
does not improve (10.3).

## 11. Comparison with available technology

The fixed-modulus product-distribution issue in Section 8 is of the same
type as modular-divisor pair-correlation problems that are substantially
easier after averaging the modulus; see Truelsen,
[*Divisor problems and the pair correlation for the fractional parts of
`n^2 alpha`*](https://arxiv.org/abs/0908.4389).  Polynomial-image energy
bounds such as Kerr--Mohammadi--Shparlinski,
[*Additive energy of polynomial images*](https://arxiv.org/abs/2306.10677),
control unmasked additive energy, not the dilated small-arc correlation
(9.7).  Likewise, the small-box results of Kerr--Mohammadi,
[*Points on polynomial curves in small boxes modulo an integer*](https://arxiv.org/abs/1803.10373),
do not give (6.5) at these anisotropic side lengths.

These references do not prove a lower-bound obstruction; they delimit why
(9.7) is new input rather than a direct citation.

## 12. Final ledger

```text
gcd(u,P) and cross-content normalization:          PROVED;
unit cube-root multiplicity:                        P^o(1), PROVED;
pointwise normalized bound:                         P/(g^3*d^2), PROVED;
multiplicative large-sieve bound:                   P/(g^2*d), PROVED;
large-sieve improvement over pointwise bound:       NONE;
prime v_p(z)=1,2,>=3 pair branches:                 WITHIN T^2;
relaxed prime p|c branch:                            WITHIN T^2;
fixed-z scalar-ray self-reproduction:                PROVED;
prime unit pair branch:                             OPEN;
dyadic factorization pair bound:                    T^2*P^(1+o(1));
desired pair bound:                                 T^2*P^o(1);
depth-one additive frequencies:                     HARMLESS;
wild p-adic masked correlation (9.7):               OPEN;
cubic-sieve carry correlation (10.7):               OPEN;
primitive shifted-cube bound:                       NOT PROVED;
sharp four-cycle bound:                             NOT PROVED.
```

Relative to the provisional Huxley-IV primitive estimate
`P^(5/8+epsilon)`, the global numerical gap remains the factor
`P^(1/16)`.  The purely congruential fourth-moment route is weaker: it
stops at `P^(1+o(1))`, a factor `P^(7/16)` above the target.
