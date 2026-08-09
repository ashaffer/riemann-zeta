# R146 Frobenius entropy and inertia-adjoint gate

## Status

R144--R145 left two apparent arithmetic escapes for an exact Artin head
mask:

1. replace the factorially rare bounded-support Frobenius condition by a
   high-density zero set; or
2. ramify the head primes and annihilate their inertia-invariant local
   factors.

Both ideas produce useful exact masks.  Neither supplies the missing divisor
sign.

The sharp findings are as follows.

1.  The fixed-point/derangement mask has constant-density local zero set,
    but its normalized irreducible Artin degree is
    `2^(m+o(m))`.  The same exponential is forced for every fixed
    fixed-point or cycle-count threshold.
2.  The exterior Euler character

    ```text
    Psi_m=lambda_(-1)(Std)=det(1-Std)
    ```

    is exactly `m` on `m`-cycles and zero elsewhere.  It is a nonnegative
    degree-zero integral virtual character with trivial multiplicity one.
    It therefore deletes every non-inert unramified prime and, for `m>=3`,
    every transposition-ramified local factor.  Its signed Gamma and
    conductor degrees vanish in a totally real squarefree-discriminant
    `S_m` field of degree `m>=3`.
3.  The same character has absolute Artin degree `2^(m-1)` and absolute
    tame conductor `2^(m-2)` at each transposition prime.  More generally,
    every exact transposition-inertia annihilator pays at least one absolute
    conductor unit per source unit at each head prime.
4.  There is a universal entropy--Fourier inequality.  If a normalized
    positive class mask is supported on a set of density `alpha`, then its
    normalized absolute Artin degree `C` and the local entropy
    `I=-log(1-alpha)` obey

    ```text
    C I >= 1.                                               (0.1)
    ```

    Thus making the bad Frobenius set rare moves the same cost into the
    auxiliary divisor.
5.  Exact ramified deletion is the kernel of the inertia-invariants map.
    Frobenius reciprocity gives an induced genuine permutation character in
    the adjoint image which contains the trivial character once and
    annihilates that whole kernel.  It is an algebraically admissible common
    Artin order pattern.  A finite bank of bounded-support inertia masks has
    a single polynomial-degree induced null direction.
6.  For the original identity/transposition head, unconditional Poitou
    positivity already gives `log rd(K)>=(4-o(1))log X`.  Hence the
    sublogarithmic root-discriminant scale required by an *absolute* R145
    zero ledger is impossible.  Current field constructions are much more
    expensive still and are not uniform in growing degree or growing local
    specification.

```text
bounded-support sublogarithmic field              IMPOSSIBLE
bounded-support local density                     FACTORIAL
derangement irreducible complexity                2^(m+o(m))
single nonidentity class complexity               >=2^((m-1)/2)
positive-mask entropy product C I                 >=1
exterior total-cycle mask                         EXACT
signed total-cycle conductor                      1
absolute transposition-conductor ledger           >=theta(X)
inertia-invariants adjoint null                    EXACT
finite bounded-support inertia bank               COMMON NULL
exceptional correlated field/divisor theorem      OPEN
fixed uniform zeta zero-free strip                 NOT PROVED
zeros approaching one                             NOT PROVED
```

Date: 2026-08-08.

Predecessor:
[`R145-FULL-STRIP-POSITIVITY-AND-DIVISOR-NULL-GATE.md`](R145-FULL-STRIP-POSITIVITY-AND-DIVISOR-NULL-GATE.md).

## 1. The original squarefree bounded-support field cannot close absolutely

Let `K/Q` be totally real of degree `m=m(X)->infinity`.  Suppose every
`p<=X` is unramified and its natural `S_m` Frobenius is the identity or a
transposition.  Then `K` has at least `m-2` degree-one primes above each
such `p`.

Use the Brueggeman--Doud local correction with

```text
f(u)=[3(sin u-u cos u)/u^3]^2.                              (1.1)
```

After division by `m`, their formula gives

```text
log rd(K)
 >=4(1-2/m) min_(|u|<=delta) f(u)
      sum_(p<=X) log p/(p+1)
   -[12pi/(5m delta)]log X-O(1).                            (1.2)
```

Since

```text
f(u)=1-u^2/5+O(u^4),
sum_(p<=X)log p/(p+1)=log X+O(1),                           (1.3)
```

taking `delta=m^(-1/3)` proves

```text
log rd(K)>=(4-o(1))log X.                                  (1.4)
```

This is unconditional and does not use squarefreeness.  See
Brueggeman--Doud,
[*Local corrections of discriminant bounds and small degree extensions of
quadratic base fields*](https://doi.org/10.1142/S1793042108001389),
Theorem 2.4.

R145 showed that resolving the parity numerator and Dedekind denominator
separately would require

```text
log rd(K)=o(log X).                                         (1.5)
```

Equations (1.4)--(1.5) are incompatible.  This kills the absolute-divisor
closure of the original squarefree parity construction.  It does *not*
exclude fields on the `C log X` scale, nor does it exclude a signed divisor
cancellation which uses the virtual conductor identity before taking
absolute values.

## 2. Arithmetic entropy of bounded support

The fraction of `S_m` occupied by permutations of support at most `L` is

```text
delta_(m,L)
 =sum_(j<=L) binom(m,j)D_j/m!
 =sum_(j<=L) D_j/[j!(m-j)!],                                (2.1)
```

where `D_j` is the derangement number.  Thus

```text
-log delta_(m,L)=(1-o(1))m log m             if L=o(m),     (2.2)
```

and, for fixed `0<alpha<1`, support at most `alpha m` still
costs

```text
(1-alpha+o(1))m log m.                                     (2.3)
```

In particular, identity/transposition density is

```text
[1+binom(m,2)]/m!=exp[-(1+o(1))m log m].                    (2.4)
```

Under the standard local-Malle independence model, prescribing `s~X/log X`
such primes in an `S_m` family predicts

```text
log rd(K) >=~ s log(1/delta_(m,L))/m.                       (2.5)
```

For `m=X^a` and `L=o(m)`, the right side is `(a+o(1))X`.
This is a heuristic rate, not an unconditional field lower bound.  Its role
is to show that the sought construction would be exponentially exceptional,
not a typical point missed by a constant in a counting theorem.

Bhargava--Shankar--Wang prove qualitative existence of totally real
squarefree-discriminant `S_m` fields with any fixed finite collection of
compatible local conditions.  Their degree and local specification are
fixed; the error is not uniform in the simultaneous limits required here.
The published error exponents are already far above the one-expected-point
scale after multiplication by (2.4).  Kedlaya's squarefree-discriminant
construction is likewise fixed-degree and explicitly does not provide these
splitting restrictions.  See

- Bhargava--Shankar--Wang,
  [*Squarefree values of polynomial discriminants I*](https://doi.org/10.1007/s00222-022-01098-w)
  and
  [*II*](https://doi.org/10.1017/fmp.2025.9);
- Kedlaya,
  [*A construction of polynomials with squarefree discriminants*](https://doi.org/10.1090/S0002-9939-2012-11231-6);
- Lagarias--Weiss,
  [*Splitting behavior of `S_n`-polynomials*](https://doi.org/10.1007/s40993-015-0006-6).

For `p<m`, asking for `m-O(1)` linear residue factors also makes `p` a
common power-basis index divisor.  This is a monogenic obstruction, not a
field-discriminant obstruction, so it does not promote (2.5) to a theorem.

## 3. The derangement mask

Let `F(g)=Fix(g)` and define

```text
Theta_m(g)=m! 1_(F(g)=0).                                   (3.1)
```

It is a nonnegative integral virtual character, vanishes at the identity,
and has trivial multiplicity

```text
b_m=<Theta_m,1>=D_m.                                        (3.2)
```

The ordered-tuple permutation character

```text
P_j=Ind_(S_(m-j))^(S_m) 1
```

has value `(F(g))_j`.  Inclusion--exclusion therefore gives

```text
Theta_m=sum_(j=0)^m (-1)^j [m!/j!] P_j.                     (3.3)
```

The canonical Dedekind expansion has absolute degree

```text
B_m=sum_j [m!/j!](m)_j=m! 2^m,
B_m/b_m=(e+o(1))2^m.                                       (3.4)
```

This exponential is not an artifact of the permutation basis.  If
`chi^lambda` has degree `f^lambda` and `eta_lambda` is the corresponding
derangement-graph eigenvalue, then

```text
a_lambda=<Theta_m,chi^lambda>=f^lambda eta_lambda,          (3.5)
C_m=(1/D_m)sum_(lambda|-m)(f^lambda)^2|eta_lambda|.          (3.6)
```

The irreducible absolute Artin degree satisfies

```text
2^m exp[-O(sqrt m)] <= C_m <=(e+o(1))2^m.                   (3.7)
```

For the lower bound, take

```text
k=floor(m/2-m^(2/3)),       r=m-k,
lambda=(r,mu),                                               (3.8)
```

where `mu|-k` has `(f^mu)^2>=k!/p(k)`.  The hook formula gives

```text
f^lambda=binom(m,k)f^mu/Q,        Q<=exp[O(m^(1/3))].       (3.9)
```

Ku--Wales prove `|eta_lambda|>=D_r` for `r>=floor(m/2)`.
Substitution into (3.6), together with `p(k)=exp[O(sqrt k)]`, gives
(3.7).  The primary inputs are Ku--Wales,
[*Eigenvalues of the derangement graph*](https://doi.org/10.1016/j.jcta.2009.10.002),
and Renteln,
[*On the spectrum of the derangement graph*](https://doi.org/10.37236/1000).

For every fixed `t`, the threshold

```text
Theta_(m,t)=m! 1_(F<t)                                      (3.10)
```

has

```text
b_(m,t)=sum_(i<t)binom(m,i)D_(m-i)                          (3.11)
```

and exact Newton expansion

```text
Theta_(m,t)
 =m!P_0+sum_(j=t)^m (-1)^(j-t+1)[m!/j!]
      binom(j-1,t-1)P_j.                                   (3.12)
```

Its canonical normalized degree is

```text
~ [e/sum_(i<t)1/i!] m^(t-1)2^(m-t+1)/(t-1)!,              (3.13)
```

and a coset-pinching argument reduces its irreducible trace norm to the
derangement graph on `S_(m-t+1)`.  Hence its irreducible normalized degree
is also

```text
2^(m+o(m)).                                                 (3.14)
```

The head condition `Fix(g)>=t` has positive limiting density.  The local
condition is now cheap, but (3.14) moves the exponential cost into the
auxiliary zero and conductor ledger.

## 4. Class indicators and the entropy--Fourier law

The phenomenon is not special to fixed points.  Let `A` be a nonempty
conjugacy-invariant subset of a finite group `G`, not containing the
identity, and let

```text
alpha=|A|/|G|,
Theta=alpha^(-1)1_A=sum_chi a_chi chi.                      (4.1)
```

Then `<Theta,1>=1`, `Theta(1)=0`, and

```text
C=sum_chi |a_chi|chi(1)>=||Theta||_infinity=1/alpha.         (4.2)
```

Forcing a prime into the zero set `G\A` costs local entropy

```text
I=-log(1-alpha)>=alpha.                                     (4.3)
```

Combining (4.2)--(4.3) proves the exact uncertainty inequality

```text
C I>=1.                                                     (4.4)
```

For a single `S_m` conjugacy class of type

```text
mu=1^f product_(ell>=2)ell^(a_ell),
s=m-f,                  q=sum_(ell>=2)a_ell,                (4.5)
```

put

```text
z_mu=f! product_(ell>=2)ell^(a_ell)a_ell!,
Theta_mu=z_mu 1_(C_mu).                                    (4.6)
```

Its irreducible expansion is

```text
Theta_mu=sum_(lambda|-m)chi^lambda(mu)chi^lambda.           (4.7)
```

Column orthogonality and `|chi^lambda(mu)|<=f^lambda` give

```text
C(mu)=sum_lambda f^lambda|chi^lambda(mu)|>=z_mu.            (4.8)
```

Pinching to the Young subgroup of the individual cycle blocks sharpens this
to

```text
C(mu)>=f! product_(ell>=2)a_ell! 2^(s-q)
       >=f!2^(s/2)>=2^((m-1)/2).                            (4.9)
```

Thus no nonidentity single-class indicator has subexponential normalized
Artin degree.

In the high-jet notation `X=exp(lambda k/r)`, suppose the allowable absolute
divisor complexity is `C<=X^(kappa+o(1))`, with `kappa<1/2`.
Equation (4.4) forces

```text
I>=X^(-kappa-o(1)),
I pi(X)>=X^(1-kappa-o(1))/log X.                            (4.10)
```

Under local-Malle independence the right side is the logarithmic field
cost.  It is strictly larger than `X^kappa`.  For the symmetric-group masks
above, (3.7), (3.14), or (4.9) also force `m=O(log X)`, so division by the
field degree changes only logarithms.  Equation (4.10) is a conditional
local-independence no-go, not an unconditional discriminant theorem; an
exceptionally correlated field family remains logically possible.

There is one cheap structural exception.  If `N normal G`, `Q=G/N`, then

```text
Theta_N=|Q|1-Reg_Q                                          (4.11)
```

vanishes on `N` and has normalized absolute degree `2`.  It factors entirely
through the quotient field.  For `S_m`, `m>=5`, the only nontrivial
fixed-index example is parity,

```text
1-sign,             L(s,Theta)=zeta(s)/L(s,sign),           (4.12)
```

which is exactly R145's undiluted quadratic auxiliary obstruction.

## 5. Dimension cancellation is not local-factor cancellation

Let `P` be the natural permutation representation and try

```text
phi_0=(m-1)1-P,
L(s,phi_0)=zeta(s)^(m-1)/zeta_K(s).                         (5.1)
```

At an odd squarefree-discriminant prime, inertia is
`I=<tau>`, with `tau` a transposition.  Tame Frobenius is represented by an
element `h in S_(m-2)`.  As an `S_(m-2)` representation,

```text
P^I=1+P_(m-2),
phi_0^I=(m-2)1-P_(m-2).                                    (5.2)
```

This has dimension zero but is not the zero virtual representation.  If
the cycles of `h` have lengths `c_1,...,c_v`, then, for `T=p^(-s)`,

```text
L_p(s,phi_0)
 =(1-T)^(-(m-2)) product_i(1-T^(c_i)).                      (5.3)
```

It equals one only when every `c_i=1`.  Its logarithmic coefficient at
`p^j` is

```text
(m-2)-Fix(h^j)>=0.                                         (5.4)
```

Thus the apparent `X/m` ramification construction secretly retained the
same complete relative-splitting condition.

## 6. The exterior total-cycle mask

There is nevertheless an exact full-centralizer annihilator:

```text
Psi_m=lambda_(-1)(Std)
     =sum_(j=0)^(m-1)(-1)^j exterior^j Std.                 (6.1)
```

For a permutation `g`,

```text
Psi_m(g)=det(1-g|Std)
 =m,       if g is an m-cycle,
 =0,       otherwise.                                      (6.2)
```

Indeed, more than one permutation cycle leaves a nonzero fixed vector in
`Std`; for an `m`-cycle the determinant is
`product_(zeta^m=1,zeta!=1)(1-zeta)=m`.

Murnaghan--Nakayama gives the irreducible identity

```text
Psi_m=p_m=sum_(j=0)^(m-1)(-1)^j chi^(m-j,1^j).              (6.3)
```

Consequently

```text
<Psi_m,1>=1,
Psi_m(1)=0,
||Psi_m||_(abs degree)=2^(m-1),
||Psi_m||_infinity=m.                                      (6.4)
```

A power of a non-`m`-cycle cannot become an `m`-cycle.  Thus an unramified
prime has identically trivial local factor whenever its Frobenius is not an
`m`-cycle.  The excluded class has density only `1/m`.

For an `m`-cycle Frobenius,

```text
L_p(s,Psi_m)
 =exp[m sum_((v,m)=1)T^v/v]
 =product_(d|m)(1-T^d)^(-m mu(d)/d).                        (6.5)
```

Assume `m>=3`.  For transposition inertia and `h in S_(m-2)`, neither `h`
nor `tau h` can be an `m`-cycle.  Therefore

```text
(Psi_m)^I=0                                                 (6.6)
```

as a full `S_(m-2)` virtual representation, and the ramified local factor is
one regardless of residue type.

The character is pointwise nonnegative, so all unramified and ramified
logarithmic-derivative coefficients are nonnegative.  In a totally real
`S_m` field of degree `m>=3` with squarefree discriminant, every finite
inertia group is a tame transposition and

```text
archimedean degree=0,
signed Artin conductor=0,
q(Psi_m)=1.                                                 (6.7)
```

The restriction `m>=3` is essential.  For `m=2`, the transposition is
itself the full cycle, so `(Psi_2)^I` is not zero and the signed conductor is
not cancelled.  This is the familiar quadratic parity case, not the new
ramified-deletion mechanism.

This is a real new cancellation mechanism.  Its remaining failure is not
on the Euler side.

## 7. Absolute conductor cost of exact ramified deletion

For the hook representation in (6.3),

```text
a_tau(chi^(m-j,1^j))=binom(m-2,j-1).                        (7.1)
```

Hence

```text
sum_j a_tau(chi^(m-j,1^j))=2^(m-2).                        (7.2)
```

Equation (6.7) is signed cancellation; (7.2) is the absolute auxiliary
zero/conductor ledger.

There is also a basis-free lower bound.  Write

```text
phi=sum_(lambda|-m)x_lambda chi^lambda,
b=x_(m)>0,                                                   (7.3)
```

and let

```text
T_m phi(h)=[phi(h)+phi(tau h)]/2,       h in S_(m-2).       (7.4)
```

Pieri branching gives

```text
<T_m phi,1>
 =b+x_(m-1,1)+x_(m-2,2).                                  (7.5)
```

Exact deletion forces (7.5) to be zero.  Since the last two representations
have transposition conductor exponents `1` and `m-3`, respectively,

```text
A_tau^abs(phi)=sum_lambda |x_lambda|a_tau(chi^lambda)>=b.   (7.6)
```

For `m>=5`, the same identity gives

```text
||phi||_(abs degree)/b>=m.                                 (7.7)
```

If every odd `p<=X` has transposition inertia, (7.6) yields

```text
(1/b)sum_lambda |x_lambda|log q(chi^lambda)
 >=sum_(3<=p<=X)log p
 =theta(X)+O(1)~X.                                         (7.8)
```

At `X=exp(lambda k/r)`, this absolute rate is `lambda/r`.  It exceeds the
Cauchy localization rate available in the R141--R145 high-jet geometry.
Thus an arithmetic construction alone cannot rescue the ramified route;
one must use the signed cancellation in (6.7) without resolving its factors
absolutely.

## 8. The inertia-invariants adjoint theorem

The common divisor obstruction has a general representation-theoretic form.
Let

```text
I normal C <=G,
T_(I,C):R(G)->R(C/I),        T_(I,C)(V)=V^I.                (8.1)
```

For every virtual character `phi` and `psi in R(C/I)`, restriction,
inflation, and Frobenius reciprocity give

```text
<T_(I,C)phi,psi>_(C/I)
 =<phi,Ind_C^G Inf_(C/I)^C psi>_G.                          (8.2)
```

Therefore

```text
T_(I,C)^*(psi)=Ind_C^G Inf psi,
ker T_(I,C)=(image T_(I,C)^*)^perp.                         (8.3)
```

In particular,

```text
P_C=T_(I,C)^*(1)=Ind_C^G 1                                (8.4)
```

is a genuine transitive permutation character with

```text
<P_C,1_G>=1.                                                (8.5)
```

If `T_(I,C)phi=0`, the Artin order pattern

```text
H=e P_C                                                     (8.6)
```

has zeta order `e`, nonnegative integral irreducible coefficients, and

```text
<phi,H>=0.                                                  (8.7)
```

It satisfies every permutation/Dedekind holomorphy inequality because it is
itself a genuine permutation character.  As in R145, (8.6) is an
algebraically admissible order pattern, not a claim about the zeros of an
actual field.

For an actual prime take `C=D`, its decomposition group.  The quotient
`D/I` is cyclic and generated by Frobenius.  Its local Euler factor is
identically one exactly when

```text
T_(I,D)phi=0.                                               (8.8)
```

Thus exact ramified deletion automatically creates the induced common null
`e Ind_D^G1`.

For transposition inertia in `S_m`,

```text
C=N_(S_m)(I)=S_2 times S_(m-2),
C/I=S_(m-2).                                                (8.9)
```

Under Frobenius characteristics,

```text
T_I=h_2^perp,                 T_I^*=h_2 multiplication,     (8.10)
P_C=[m]+[m-1,1]+[m-2,2].                                   (8.11)
```

Equation (8.11) is precisely the three-term null dual to (7.5).

An explicit non-degree-zero kernel element is

```text
f_m(g)=(-1)^(number of 2-cycles of g).                      (8.12)
```

It obeys `T_I f_m=0`, `f_m(1)=1`, and

```text
<f_m,1>
 =[z^m]e^(-z^2)/(1-z)
 =sum_(j<=m/2)(-1)^j/j! ->e^(-1).                          (8.13)
```

After multiplication by `m!` it is an integral virtual character.  It
evades the degree-zero regular null of R145, but (8.7) still kills it.

## 9. Approximate leakage and finite banks

Put

```text
W=T_(I,C)phi,
b_I(phi)=<phi,P_C>=<W,1_(C/I)>,                             (9.1)
Lambda_I(phi)=||W||_(L2(C/I)).                              (9.2)
```

Then

```text
|b_I(phi)|<=Lambda_I(phi).                                 (9.3)
```

If `phi=V_+-V_-`, let

```text
Delta=dim V_++dim V_-,
A_I^abs=(dim V_+-dim V_+^I)+(dim V_--dim V_-^I).            (9.4)
```

The quotient invariant budget gives

```text
|<phi,P_C>|<=Lambda_I(phi)<=Delta-A_I^abs.                  (9.5)
```

Thus preserving an `eta` fraction of the source against the induced order
direction forces at least the same scale of local Euler leakage.  For a
cyclic residue quotient generated by `F`, the identity

```text
|C/I| b_I(phi)
 =phi(1)-a_I(phi)+sum_(j=1)^(|C/I|-1)tr(F^j|phi^I)          (9.6)
```

makes the conductor/leakage calibration explicit.

A finite detector bank does not remove the null.  If masks `phi_j` satisfy
normalizer-wide `T_(I_j)phi_j=0`, choose conjugates of the bounded-support
inertia groups on disjoint subsets and put

```text
U=product_j I_j times S_(m-s),                              (9.7)
```

where `s` is total support.  Then every `I_j` is normal in `U`, so

```text
<phi_j,Ind_U^(S_m)1>
 =dim(phi_j^U)
 =dim((phi_j^(I_j))^(U/I_j))=0.                             (9.8)
```

The single genuine order pattern `e Ind_U1` contains the trivial character
once and has degree

```text
[S_m:U]=m!/[(m-s)! product_j|I_j|]=O(m^s).                  (9.9)
```

So every fixed bounded-support exact-deletion bank has a common
polynomial-degree induced null.

## 10. Construction reality check

For fixed `m` and fixed `X`, current squarefree-discriminant theorems can
qualitatively impose the required local conditions.  They do not give the
uniform one-expected-point result needed as `m,X` grow.

For example, imposing simple transposition ramification at every odd
`p<=X` has local density

```text
product_(3<=p<=X)[1/p+O_m(1/p^2)]
 =exp[-theta(X)+O_m(log log X)].                            (10.1)
```

The ideal high-dimensional lattice threshold predicts

```text
log rd(K)~2X/m.                                             (10.2)
```

The published fixed-degree power-saving error only certifies a much larger
`O_m(X)` scale, and its implied constant depends on the growing local
specification.  The analogous unramified no-`m`-cycle condition is locally
far denser, but the exterior mask pays (6.4) and retains the induced divisor
null.

Golod--Shafarevich and cutting-tower constructions do not provide an
alternative: their finite quotients in the relevant pro-`p` towers are
solvable and cannot supply growing alternating composition factors.

## 11. Verdict

R146 isolates a universal local/global duality:

```text
rare bad Frobenius support
        <--> large absolute character complexity,           (11.1)

exact ramified local deletion
        <--> induced permutation-character divisor null.    (11.2)
```

For `m>=3`, the exterior total-cycle character proves that remarkably strong
local cancellation is algebraically possible: degree, Gamma factor, signed
conductor, all transposition-ramified factors, and all non-inert unramified
factors can vanish simultaneously.  The failure is the same one exposed by
R145, now in its exact local adjoint form.  Standard holomorphy constraints
permit an auxiliary order vector which cancels the target zeta order.

The live successor is consequently narrower:

1. exploit the special exterior-Euler hook divisor with a genuine joint-zero
   theorem, rather than its absolute `2^m` expansion;
2. prove a correlated field-family zero-density theorem strong enough to
   select a no-`m`-cycle field whose negative hook factors avoid the target
   localization disc; or
3. find a signed global invariant outside the Artin order pairing and the
   whole-strip-positive explicit formula.

None is presently proved.  R146 proves neither a fixed zero-free strip nor
zeros approaching one.

Successor:
[`R147-EXTERIOR-CYCLE-FAMILY-SELECTION-GATE.md`](R147-EXTERIOR-CYCLE-FAMILY-SELECTION-GATE.md).
