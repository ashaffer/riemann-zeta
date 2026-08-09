# R144 bounded-support virtual-character annihilator

## Status

R143 reduced the primitive low-support branch to natural alternating and
symmetric actions.  This report supplies a new cancellation mechanism for
exactly that survivor.

If `pi(g)=Fix(g)` is a permutation character of degree `m`, then

```text
f_q(g)=(m-Fix(g))_(falling q)                                (0.1)
```

is an integral virtual character, is nonnegative on every group element,
and vanishes whenever `g` moves fewer than `q` points.  Every power of such
an element is also annihilated.  The associated Artin logarithmic derivative
has nonnegative coefficients even at ramified primes, has zero archimedean
degree in a totally real realization, and has normalized conductor and zero
ledger `O_q(log rd(K)+log T)`.

This is a genuine improvement over R141.  For bounded absolute support it
deletes the entire prime head exactly; the former requirement that `L/m` be
exponentially small is unnecessary.

It is not yet a strip proof.  A nonzero genuine representation cannot kill
the transpositions of `S_m` or the `3`-cycles of `A_m`, because those classes
generate the group.  Exact annihilation therefore requires a mixed virtual
character.  Its Artin object is a quotient of Dedekind zeta functions, and
the removed Euler head is paid for by a signed auxiliary divisor.  No known
theorem prevents that divisor from cancelling the selected Riemann-zeta
zero in the required target disc.

```text
falling-support virtual character                 EXACT
all-prime coefficient nonnegativity               PROVED
bounded-support head annihilation                  EXACT
normalized conductor/zero ledger                  O_q(1)
natural S_m transposition parity mask              EXACT / LINEAR
natural A_m three-cycle mask                       EXACT / QUADRATIC
identity/transposition/three-cycle two-set mask    EXACT
genuine monomial exterior mask                     ENTIRE / APPROXIMATE
genuine exact generating-class mask                IMPOSSIBLE
cheap prescribed-Frobenius field                   OPEN
target auxiliary-divisor noncancellation           OPEN
fixed uniform zeta zero-free strip                 NOT PROVED
zeros approaching one                              NOT PROVED
```

Date: 2026-08-08.

Predecessor:
[`R143-SOLVABLE-SUPPORT-QUOTIENT-AND-PRIMITIVE-CLASSIFICATION.md`](R143-SOLVABLE-SUPPORT-QUOTIENT-AND-PRIMITIVE-CLASSIFICATION.md).

## 1. The falling-support character

Let `E/Q` be finite Galois with group `G`, and let `G` act on a set `Omega`
of size `m`.  Write

```text
P=C[Omega],              pi(g)=tr P(g)=Fix(g),                (1.1)
U=m*1-P,                 u(g)=m-Fix(g)=supp(g).               (1.2)
```

Here `U` is a degree-zero integral virtual representation.  For an integer
`q>=1`, define in the representation ring

```text
Theta_q= tensor_(h=0)^(q-1) [U-h*1].                         (1.3)
```

Its character is

```text
f_q(g)=u(g)[u(g)-1]...[u(g)-q+1]=(supp(g))_q.                (1.4)
```

This immediately gives:

**Theorem 1.1.**  `Theta_q` is an integral degree-zero virtual
representation and

```text
f_q(g)>=0                                                       for all g,
f_q(g)=0                 iff supp(g)<q.                       (1.5)
```

Moreover `supp(g^v)<=supp(g)`, so

```text
supp(g)<q  =>  f_q(g^v)=0 for every v>=1.                    (1.6)
```

This is an algebraic support-threshold filter.  It uses no averaging and no
approximation.

## 2. The Artin logarithmic derivative

Let `L(s,Theta_q)` be the virtual Artin `L`-function and put

```text
D_q(s)=-L'/L(s,Theta_q).                                    (2.1)
```

At an unramified prime,

```text
D_q(s)
 =sum_(p,v>=1) f_q(Frob_p^v) log(p) p^(-vs)+ramified terms.  (2.2)
```

All displayed coefficients are nonnegative.  Positivity also survives
ramification.  If `I_p` is inertia and `sigma_p` is a Frobenius lift, then

```text
tr[sigma_p^v | Theta_q^(I_p)]
 =1/|I_p| sum_(h in I_p) f_q(sigma_p^v h)>=0.                (2.3)
```

The equality follows by inserting the inertia projector.  It is valid by
linearity for virtual representations, and every summand is nonnegative by
(1.5).

For an unramified prime `p`, the condition

```text
supp(Frob_p)<q                                               (2.4)
```

deletes its complete local logarithmic derivative, including every prime
power.  At a ramified prime the corresponding exact condition is that every
element in every relevant inertia--Frobenius coset have support `<q`.
Merely bounding one Frobenius representative is insufficient.

## 3. Unconditional continuation

No Artin-holomorphy conjecture is needed to define the global divisor.  On
expanding (1.3), `Theta_q` is an integral combination of tensor powers
`P^(tensor j)`.  The latter is the permutation representation on
`Omega^j`.  If

```text
Omega^j=disjoint-union_a G/H_(j,a),                          (3.1)
```

then Artin formalism gives

```text
L(s,P^(tensor j))=product_a zeta_(E^H_(j,a))(s).             (3.2)
```

Thus `L(s,Theta_q)` is explicitly a product and quotient of Dedekind zeta
functions.  Its meromorphic continuation, functional equation, and divisor
ledger are unconditional.

If `E` is totally real, complex conjugation acts trivially on `P`.  Since
`Theta_q` has degree zero, its real Gamma factors cancel exactly.

## 4. Size of the normalized ledger

Let

```text
b_q=<f_q,1>_G=1/|G| sum_(g in G)f_q(g)                      (4.1)
```

be the trivial-character multiplicity.  For natural `S_m` or `A_m`, fixed
`q`, and `m` tending to infinity,

```text
b_q=m^q+O_q(m^(q-1)).                                       (4.2)
```

An elementary uniform lower bound comes from derangements:

```text
b_q >= Prob(g is a derangement)*(m)_q
     >=c (m)_q                                               (4.3)
```

for an absolute `c>0` once `m` is large.  On the other hand, put

```text
||sum_chi n_chi chi||_deg=sum_chi |n_chi|chi(1).             (4.4)
```

This norm is submultiplicative, and

```text
||(m-h)1-P||_deg<=2m-h.                                     (4.5)
```

Consequently

```text
||Theta_q||_deg<=product_(h<q)(2m-h)<=(2m)^q,               (4.6)
||Theta_q||_deg/b_q<=O(2^q exp[O(q^2/m)]).                  (4.7)
```

The absolute zero count of every numerator and denominator factor, divided
by the source multiplicity `b_q`, therefore costs only the factor in (4.7).

The tensor-conductor inequality

```text
a_p(V tensor W)
 <=dim(W)a_p(V)+dim(V)a_p(W)                                (4.8)
```

gives

```text
a_p(P^(tensor j))<=j m^(j-1)a_p(P).                         (4.9)
```

Since the conductor-discriminant formula identifies

```text
sum_p a_p(P)log p=log D_K,                                  (4.10)
```

where `K=E^H` is the original degree-`m` permutation field, expansion of
(1.3) yields

```text
1/b_q sum_p |a_p(Theta_q)|log p
 <=O(q 2^q exp[O(q^2/m)]) log rd(K).                         (4.11)
```

For fixed `q`, both the conductor and divisor ledgers are `O_q(1)` after
normalization.  A slowly growing `q` remains admissible whenever its
exponential variation fits below the high-jet localization budget.

## 5. Exact natural symmetric-group masks

For natural `S_m`, the sign character gives a much cheaper transposition
filter.  Put

```text
f_S(g)=supp(g)-[1-sgn(g)].                                  (5.1)
```

If `g` is even, this is `supp(g)`.  If `g` is odd, it is
`supp(g)-2`, which is nonnegative.  Therefore

```text
f_S(g)>=0,
f_S(g)=0 iff g=1 or g is a transposition.                    (5.2)
```

As a virtual character,

```text
Theta_S=(m-1)1+sgn-P
       =(m-2)1-Std+sgn.                                     (5.3)
```

Its trivial multiplicity is `m-2`, and

```text
L(s,Theta_S)=zeta(s)^(m-1)L(s,sgn)/zeta_K(s).                (5.4)
```

Thus the normalized positive detector is

```text
A_S=[(m-1)D_zeta-D_(zeta_K)+D_sgn]/(m-2).                   (5.5)
```

The finite-conductor variation is at most

```text
[log D_K+log d_sgn]/(m-2)=O(log rd(K)),                      (5.6)
```

and every power of a transposition is killed.

The simpler quadratic mask

```text
supp(g)[supp(g)-2]                                          (5.7)
```

is also nonnegative on `S_m` and kills the identity and transpositions.  Its
trivial multiplicity is `(m-2)^2`; (5.1) is preferable because it is linear
and has a smaller absolute divisor ledger.

## 6. Alternating and two-set masks

Every nonidentity element of natural `A_m` moves at least `3` points, so

```text
f_A(g)=supp(g)[supp(g)-3]                                   (6.1)
```

is a nonnegative integral virtual character which vanishes precisely at the
identity and the `3`-cycles.

There is also one mask which handles the minimal classes of both `A_m` and
`S_m`.  Let `P_1=P`, and let `P_2` be the permutation representation on
unordered `2`-subsets.  Write

```text
d_1(g)=m-Fix_1(g),
d_2(g)=binom(m,2)-Fix_2(g).                                 (6.2)
```

If `s=supp(g)` and `t_2` is the number of `2`-cycles of `g`, then

```text
d_2=s m-s(s+1)/2-t_2.                                      (6.3)
```

It follows that

```text
f_23=(m-2)d_1-d_2=s(s-3)/2+t_2>=0.                          (6.4)
```

The right side is zero exactly for the identity, a transposition, or a
`3`-cycle.  The virtual character is

```text
Theta_23=[m(m-3)/2]1-(m-2)P_1+P_2,                          (6.5)
```

with trivial multiplicity

```text
b_23=(m-2)(m-3)/2.                                          (6.6)
```

If `K_2` is the `2`-set resolvent field, then

```text
L(s,Theta_23)
 =zeta(s)^[m(m-3)/2] zeta_(K_2)(s)/zeta_K(s)^(m-2).         (6.7)
```

The pointwise inequality in (6.4), averaged over ramification groups, gives

```text
log D_(K_2)<=(m-2)log D_K.                                  (6.8)
```

Hence (6.7) again has `O(log rd(K))` normalized conductor variation.

## 7. A genuine entire approximate mask

Virtual signs are not needed merely to make the support *small*.  Let

```text
W=wedge^2 P,                    d=binom(m,2).                 (7.1)
```

Then

```text
chi_W(g)=[Fix(g)^2-Fix(g^2)]/2.                             (7.2)
```

The defect

```text
h_W(g)=d-chi_W(g)                                            (7.3)
```

is nonnegative.  If `s=supp(g)`, the elementary inequality

```text
d-chi_W(g)<=(m-1)s                                          (7.4)
```

gives

```text
0<=h_W(g)/d<=2s/m.                                          (7.5)
```

The same inequality survives inertia averaging and gives
`log q(W)/d=O(log rd(K))`.

This representation is monomial.  On the lines

```text
C(e_i wedge e_j),                                           (7.6)
```

the group acts through signed permutation matrices.  If `H` stabilizes the
unordered pair `{1,2}` and `theta` records its action on
`e_1 wedge e_2`, then

```text
W=Ind_H^G theta.                                             (7.7)
```

For natural `S_m`, `theta` is detected by `(12)`; for `A_m`, by
`(12)(34)`.  It is a nontrivial one-dimensional character, and

```text
L_Q(s,W)=L_(E^H)(s,theta)                                   (7.8)
```

is a nontrivial finite-order Hecke `L`-function, hence entire.

Thus

```text
d D_zeta-D_W                                                 (7.9)
```

is an unconditional positive low-support detector with an entire auxiliary
factor.  Its defect is still of order `s/m`, however; it does not give the
exact bounded-support deletion of Sections 1, 5, and 6.

## 8. Why exact deletion must be virtual

The contrast between Sections 1 and 7 is forced.

**Theorem 8.1.**  Let `C` generate a finite group `G`, and let `V` be a
unitary representation of dimension `d`.  If

```text
d-Re chi_V(c)=0                    for every c in C,          (8.1)
```

then `V` is trivial.

**Proof.**  Every eigenvalue of `V(c)` has modulus one.  Equality of the real
trace with `d` forces every eigenvalue to be `1`, hence `V(c)=I`.  Since `C`
generates `G`, the full representation is trivial.  QED.

Transpositions generate `S_m` and `3`-cycles generate `A_m`.  Therefore no
nontrivial genuine-representation defect can annihilate those classes
exactly.  Any exact Artin mask must use mixed virtual signs, and hence a
quotient `L`-object with a signed divisor.  This is not an artifact of the
falling-factorial choice.

## 9. The remaining divisor gate

Let

```text
Theta_q=b_q*1+sum_(chi!=1)n_chi chi.                         (9.1)
```

At a Riemann-zeta zero `rho`, the residue of the normalized logarithmic
derivative is

```text
r_q(rho)
 =[b_q ord_rho(zeta)+sum_(chi!=1)n_chi ord_rho L(s,chi)]/b_q. (9.2)
```

Exact head deletion controls neither the sign nor the size of (9.2).  In the
permutation-tensor realization, the same issue is a signed linear
combination of orders of Dedekind zeta functions at exactly `rho`.

The high-jet argument would proceed if one could prove

```text
|r_q(rho)|>=exp[-o(k)]                                      (9.3)
```

and exclude a closer cancelling signed divisor in the target disc, while
constructing the prescribed-Frobenius field below the conductor budget.
Neither follows from Artin continuation, ordinary zero density, or the
pointwise positivity of `f_q`.

Taking a reciprocal removes denominator zeros as singularities, but
reintroduces the uncontrolled analytic-unit value at `rho`.  Removing a
finite Euler head from `1/zeta`, for example, multiplies the pole residue by

```text
product_(p<=X)(1-p^(-rho))^(-1),                             (9.4)
```

whose modulus can be exponentially ill-conditioned.  Logarithmic
derivatives avoid (9.4), but necessarily retain the signed divisor in
(9.2).  This is the same value-versus-divisor trade exposed by R141--R142.

## 10. Arithmetic feasibility and lower bounds

For fixed `m` and a finite set `S`, weak approximation, Krasner's lemma, and
Hilbert irreducibility qualitatively produce totally real `S_m` fields with
prescribed unramified local algebras such as

```text
K tensor Q_p = Q_p^(m-2) times Q_(p^2)^unr,                 (10.1)
```

which realizes a transposition at `p`.  There is therefore no qualitative
inverse-Galois contradiction.

When `m-L>p`, such a field cannot be represented at `p` by a power basis
whose defining polynomial has the corresponding distinct linear factors:
there are more degree-one primes than elements of `F_p`.  The
Dedekind--Engstrom common-index criterion then makes `p` divide every
power-basis index.  This is a monogenic obstruction, not field
ramification, and it supplies no discriminant lower bound.

The unconditional Poitou--Odlyzko explicit formula does see the many
degree-one primes.  A convenient finite form is Brueggeman--Doud's local
correction theorem.  Put

```text
f(u)=[3(sin u-u cos u)/u^3]^2.                              (10.2)
```

For a totally real degree-`m` field unramified at `p<=X`, with every such
Frobenius fixing at least `m-L` points, their formula gives

```text
log rd(K)
 >=4(1-L/m) min_(|u|<=delta)f(u)
       sum_(p<=X) log p/(p+1)
   -[12pi/(5m delta)]log X-O(1).                            (10.3)
```

Take `delta=m^(-1/2)`.  If `m->infinity` and `L/m=o(1)`, this yields

```text
log rd(K)>=(4-o(1))log X-O(1).                              (10.4)
```

The prime weight is essentially `log p/(p+1)`, whose sum is
`log X+O(1)`.  This is compatible with `log rd(K)=o(X^kappa)` for every
fixed `kappa>0`; it does not close R141.  The source is Brueggeman--Doud,
[*Local corrections of discriminant bounds and small degree extensions of
quadratic base fields*](https://doi.org/10.1142/S1793042108001389),
Theorem 2.4, building on Poitou's 1976/77 discriminant formula.

Under GRH, the prime weight becomes square-root scale and one recovers

```text
log rd(K)>>sqrt(X)-O(log X),                                (10.5)
```

which contradicts every admissible `kappa<1/2`.  The difference between
(10.4) and (10.5) is genuine: unconditional positivity on the whole
critical strip pays a `p^(-1)` rather than `p^(-1/2)` local weight.

The local-Malle heuristic is stronger still and predicts
`log rd(K)>>X/log X` for fixed degree and about `X` in the growing natural
symmetric family.  Neither uniform field counting nor an unconditional
square-root discriminant inequality of the required kind is known.

## 11. Verdict

R144 changes the live problem in a concrete way:

```text
OLD: support/m must be exponentially tiny in the jet order;
NEW: bounded support can be annihilated exactly at constant normalized cost.
                                                                    (11.1)
```

The natural `A_m/S_m` primitive survivor from R143 is therefore not killed
by the old square-root Fourier ledger.  But exact deletion is necessarily
virtual, and its negative representation mass produces the signed divisor
(9.2).  The two simultaneous missing inputs are now precise:

1. a totally real prescribed-Frobenius field with
   `log rd(K)=o(X^kappa)`, `kappa<1/2`; and
2. a target-conditioned noncancellation theorem for the virtual Artin divisor
   at the selected zeta zero and in its localization disc.

GRH and local-Malle heuristics say the first input should be false.  Current
unconditional explicit-formula technology proves only (10.4), and no known
joint-zero theorem supplies the second.

Neither side of the fixed-strip dichotomy follows from this report.

Successor:
[`R145-FULL-STRIP-POSITIVITY-AND-DIVISOR-NULL-GATE.md`](R145-FULL-STRIP-POSITIVITY-AND-DIVISOR-NULL-GATE.md).
