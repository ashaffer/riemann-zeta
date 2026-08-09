# R149 degree-zero L-data and distinct-divisor gate

## Status

R146 left the exterior Euler quotient

```text
F_m(s)=L(s,Psi_m),
Psi_m=lambda_(-1)(Std)=sum_(j=0)^(m-1)(-1)^j exterior^j Std,
```

as a live signed-divisor mechanism.  This report imports the strongest
classification and distinct-zero theorems that apply to it, and audits the
last formal escape in R145: the regular Artin order pattern.

The conclusions are sharp.

1.  Booker's degree-zero classification applies to `Psi_m`.  Since `F_m` is
    nontrivial, it has infinitely many genuine zeros and infinitely many
    genuine poles.  Its total uncancelled divisor mass is not `o(T)`.
2.  For `m=3`, Bombieri--Perelli strengthens this to `>>T log T` zeros and
    `>>T log T` poles, counted with residual multiplicity.
3.  Also for `m=3`, Booker gives a genuinely zeta-specific statement:
    infinitely many zeros of `zeta` survive the standard Artin denominator.
    This is stronger than undifferentiated divisor abundance, but it has no
    horizontal localization.
4.  Selberg-class degree-zero rigidity, ratios-of-Artin-L-functions converse
    theorems, and analytic torsion do not add the missing localization.
5.  The regular order pattern

    ```text
    ord_rho L(s,chi)=e chi(1)
    ```

    forces `ord_rho zeta_E=e[E:Q]`, but violates none of the unconditional
    Heilbronn--Stark--Foote--Murty inequalities.  No known unconditional
    nonreal-zero multiplicity bound is strictly below `[E:Q]` in the required
    uniformity.
6.  Existing explicit multiplicity estimates are of size
    `log d_E+[E:Q] log(|Im rho|+2)`, not `<[E:Q]`.  Existing near-one regions
    have width only the reciprocal of the same quantity.
7.  Lemke Oliver--Thorner--Zaman do provide a horizontal escape for *almost
    all* `S_3` fields: the standard factor is nonvanishing in a near-one box.
    The remaining problem is to prove that the heavily locally conditioned
    exterior-mask family contains a field outside their `O(Q^epsilon)`
    exceptional set while retaining the R146 discriminant budget.

```text
nontrivial degree-zero quotient => infinitely many poles       THEOREM
nontrivial degree-zero quotient => infinitely many zeros       THEOREM
total residual divisor not o(T)                                THEOREM
cubic residual zeros and poles >> T log T                      THEOREM
infinitely many zeta-specific cubic survivors                  THEOREM
right-half-strip zeta-specific survivor                        OPEN
regular-order pattern excluded algebraically                   FALSE
uniform Dedekind multiplicity < degree                         NOT KNOWN
almost-all-field standard-factor nonvanishing                  THEOREM
masked-field escape from the exceptional family                OPEN
fixed uniform zeta zero-free strip                             NOT PROVED
zeros approaching one                                          NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R140-DEGREE-ZERO-LOCALIZATION-AND-FROBENIUS-DICHOTOMY.md`](R140-DEGREE-ZERO-LOCALIZATION-AND-FROBENIUS-DICHOTOMY.md),
[`R145-FULL-STRIP-POSITIVITY-AND-DIVISOR-NULL-GATE.md`](R145-FULL-STRIP-POSITIVITY-AND-DIVISOR-NULL-GATE.md),
[`R146-FROBENIUS-ENTROPY-AND-INERTIA-ADJOINT-GATE.md`](R146-FROBENIUS-ENTROPY-AND-INERTIA-ADJOINT-GATE.md),
and
[`R148-CUBIC-LOCAL-SELECTION-AND-ZERO-AVOIDANCE-GATE.md`](R148-CUBIC-LOCAL-SELECTION-AND-ZERO-AVOIDANCE-GATE.md).

## 1. Conventions and the exterior quotient

Let `M/Q` be Galois with group `G=S_m`, and let `Std` denote the
`(m-1)`-dimensional standard representation.  For a meromorphic function
`A`, use the convention

```text
ord_rho A > 0   for a zero,
ord_rho A < 0   for a pole.                                  (1.1)
```

The exterior character is

```text
Psi_m=sum_(j=0)^(m-1)(-1)^j exterior^j Std,
Psi_m(g)=det(1-g|Std)
        =m 1_(g is an m-cycle).                              (1.2)
```

In particular,

```text
Psi_m(1)=0,                    <Psi_m,1>=1.                  (1.3)
```

The first identity is the signed Artin degree; it must not be confused with
the absolute auxiliary degree `2^(m-1)` from R146.  At an unramified
`m`-cycle prime, with `T=p^(-s)`, the local factor is

```text
F_(m,p)(s)
 =product_(d|m)(1-T^d)^(-m mu(d)/d).                         (1.4)
```

At every other unramified prime it is one.  Chebotarev and the coefficient
of `T` in (1.4) show that `F_m` is not the constant function one.

For `m>=3`, complex conjugation is never an `m`-cycle.  Since both the
virtual dimension and the character value at complex conjugation vanish,
the signed archimedean factor cancels.  The squarefree-discriminant,
totally-real setting of R146 also cancels every tame-transposition local
factor and has signed conductor one.  None of the classification arguments
below uses the *absolute* hook expansion.

## 2. Booker closes the global degree-zero question

Booker's definition of an L-datum is a triple `(f,K,m_F)` satisfying his
axioms A1--A4.  Its divisor coordinate is normalized by

```text
m_F(z)=ord_(s=1/2+iz) Lambda_F(s).                            (2.1)
```

Thus `Re z` is vertical height and `Im z=1/2-Re s` is horizontal location.
Most importantly, Booker calls an L-datum **positive** when only finitely
many `z` have `m_F(z)<0`: positivity means finitely many poles.  It does
not mean nonnegative Euler or logarithmic coefficients.

Every genuine Artin representation gives an L-datum, without assuming the
Artin holomorphy conjecture.  The L-data form a group, so the integral
virtual representation `Psi_m` also gives an L-datum.  Its prime-power
traces are bounded, so A1 is automatic.  Its analytic degree is the signed
dimension

```text
d_(Psi_m)=Psi_m(1)=0.                                       (2.2)
```

Booker's converse theorem says that if a positive L-datum has degree
`d<5/3`, then either

```text
d=0 and L_F(s)=1,
or d=1 and L_F(s)=L(s+it,chi)                               (2.3)
```

for a primitive Dirichlet character `chi`.

### Theorem 2.1 -- unavoidable exterior divisor

For every nontrivial exterior quotient `F_m=L(s,Psi_m)` with `m>=3`:

```text
F_m has infinitely many poles;
F_m has infinitely many zeros.                              (2.4)
```

Indeed, finitely many poles would make the degree-zero datum positive, so
(2.3) would give `F_m=1`, contrary to (1.4).  Applying the same argument to
the datum `-Psi_m`, whose L-function is `1/F_m`, proves the assertion about
zeros.

Booker's multiplicity-one theorem gives a quantitative but weaker global
statement.  A nonzero L-datum satisfies

```text
sum_(|Re z|<=T) |m_F(z)| != o(T).                            (2.5)
```

Equivalently, along an unbounded sequence of heights the total residual
divisor mass is `>=cT` for some `c>0`.  Equation (2.5) says nothing about
`Im z`, hence nothing about `Re s`.

Primary source: Andrew R. Booker,
[*L-functions as distributions*](https://doi.org/10.1007/s00208-015-1178-z),
Math. Ann. 363 (2015), Definition 1.3, Example 1.4(3), and Theorems
1.6--1.7; see also [arXiv:1308.3067](https://arxiv.org/abs/1308.3067).

### 2.1 The R140 model is not literally an L-datum

The one-prime model in R140 has

```text
log K(s)=sum_(k>=1) d_k q^(-ks)/k,
d_k asymp q^k                                                   (2.6)
```

along a subsequence.  In Booker's normalization this gives

```text
f(q^k)=d_k log(q) q^(-k/2),                                  (2.7)
```

so `|f(q^k)|^2` is of order `q^k`; A1's subpolynomial square-mean
condition fails.  Therefore R140 is not a counterexample inside Booker's
class.  What survives the audit is narrower: all conclusions (2.4)--(2.5)
remain compatible with every compensating pole lying on the critical line
and with one selected off-line zeta zero being cancelled.

## 3. The cubic quotient and its exact field factorization

Now let `M/Q` be an `S_3` Galois extension.  Write

```text
epsilon = sign,
V       = Std,
k       = M^(A_3)                         (quadratic resolvent),
C       = M^(<tau>)                       (a non-Galois cubic field), (3.1)
```

where `tau` is any transposition.  The three permutation-character
identities are

```text
Ind_(A_3)^(S_3) 1       =1+epsilon,
Ind_(<tau>)^(S_3) 1     =1+V,
Reg_(S_3)               =1+epsilon+2V.                       (3.2)
```

Artin formalism therefore gives

```text
zeta_k =zeta L(s,epsilon),
zeta_C =zeta L(s,V),
zeta_M =zeta L(s,epsilon)L(s,V)^2
        =zeta_k L(s,V)^2.                                   (3.3)
```

Since `exterior^2 V=epsilon`,

```text
Psi_3=1-V+epsilon.                                          (3.4)
```

Consequently the exterior quotient has the three equivalent exact forms

```text
F_3(s)=L(s,Psi_3)
      =zeta(s)L(s,epsilon)/L(s,V)
      =zeta_k(s)/L(s,V)
      =zeta(s)zeta_k(s)/zeta_C(s).                           (3.5)
```

Squaring (3.5) and using the last identity in (3.3) yields

```text
F_3(s)^2=zeta_k(s)^3/zeta_M(s).                             (3.6)
```

There is no omitted zeta factor in (3.6).  At an unramified `3`-cycle
prime,

```text
F_(3,p)(s)=(1-T^3)/(1-T)^3,                                 (3.7)
```

while every other unramified local factor is one.

For later order calculations, put

```text
e       =ord_rho zeta,
n_eps   =ord_rho L(s,epsilon),
n_V     =ord_rho L(s,V).                                   (3.8)
```

Then

```text
ord_rho F_3=e+n_eps-n_V,
ord_rho zeta_k=e+n_eps,
ord_rho zeta_M=e+n_eps+2n_V.                               (3.9)
```

## 4. Cubic noncancellation is abundant but not localized

### 4.1 Infinitely many zeta-specific survivors

Consider

```text
D(s)=L(s,V)/zeta(s).                                        (4.1)
```

The representation `V` is the dihedral automorphic induction of a
nontrivial character of `A_3`; its L-function is a cuspidal `GL_2`
L-function.  Booker's Corollary 1.9 applies to the quotient of this
`GL_2` L-function by the trivial `GL_1` L-function and proves that `D`
has infinitely many poles.

Equivalently,

```text
ord_rho zeta > ord_rho L(s,V)                               (4.2)
```

at infinitely many nontrivial zeta zeros, with residual multiplicity.
These are genuinely zeta-specific survivors.  Since a nontrivial quadratic
L-function is entire, `n_eps>=0` at such a point, and (3.9) shows that each
point in (4.2) is a zero of `F_3`.

One can see the converse-theorem contradiction directly.  If (4.1) had
only finitely many poles, its positive degree-one L-datum would have to be
a shifted primitive Dirichlet L-function.  At an unramified prime its first
logarithmic coefficient is

```text
V(g)-1 = 1 on the identity class,
        -1 on transpositions,
        -2 on 3-cycles.                                    (4.3)
```

The value `-2` occurs on a positive-density prime set, whereas a shifted
Dirichlet prime coefficient has modulus at most one.  This is impossible.

The result is global: it does not show that (4.2) holds at a prescribed
zeta zero or at any point with `Re rho>1/2`.

### 4.2 `T log T` residual divisor in both orientations

Set

```text
U(s)=zeta(s)L(s,epsilon)=zeta_k(s),
W(s)=L(s,V).                                                 (4.4)
```

Bombieri--Perelli's distinct-zero theorem applies to `(U,W)`.  Their
hypotheses B(I)--B(III) hold because these are fixed degree-two Euler
products of finite order with the usual functional equations.  For
B(IV), the first prime coefficients on `S_3` are

| class | density | `a_U=1+epsilon` | `a_W=V` |
|---|---:|---:|---:|
| identity | `1/6` | `2` | `2` |
| transposition | `1/2` | `0` | `0` |
| `3`-cycle | `1/3` | `2` | `-1` |

Hence Chebotarev gives

```text
E|a_U|^2=2,              E|a_W|^2=1,
E(a_U conjugate(a_W))=0.                                  (4.5)
```

Their density hypothesis is classical for the fixed zeta and Dirichlet
factors.  For `W`, it follows from Beckwith--Liu--Thorner--Zaharescu:
for a fixed cuspidal `GL_2` representation,

```text
N_pi(sigma,T) <<_pi T^(1-c(sigma-1/2)) log T,
c<1/4-2theta,                 theta<=7/64.                  (4.6)
```

The total gamma-degree sums of `U` and `W` are equal.  Thus, in both
orientations,

```text
sum_(0<Im rho<T) max(ord_rho U-ord_rho W,0) >>_M T log T,
sum_(0<Im rho<T) max(ord_rho W-ord_rho U,0) >>_M T log T.   (4.7)
```

The first line counts zeros of `F_3`; the second counts poles.  The
`U`-surplus in the first line may come from `zeta`, from `L(s,epsilon)`, or
from both.  Equation (4.2), not (4.7), is the available zeta-specific
statement, and it currently has no positive-proportion form.

Primary sources: E. Bombieri and A. Perelli,
[*Distinct zeros of L-functions*](https://doi.org/10.4064/aa-83-3-271-281),
Acta Arith. 83 (1998), Theorem 1; and O. Beckwith, D. Liu, J. Thorner, and
A. Zaharescu,
[*A zero density estimate and fractional imaginary parts of zeros for
GL2 L-functions*](https://doi.org/10.1017/S0305004122000445),
Math. Proc. Cambridge Philos. Soc. 174 (2023), Theorem 1.1; see also
[arXiv:2103.01956](https://arxiv.org/abs/2103.01956).

## 5. Why the other degree-zero classifications do not localize

### 5.1 The Selberg and extended Selberg classes

The Selberg class and Kaczorowski--Perelli's extended class require that
`(s-1)^rF(s)` be entire of finite order for some integer `r>=0`.  By
Theorem 2.1, the exterior quotient has infinitely many poles, so it is not
in either class.  If it had only the allowed finite pole set, degree-zero
rigidity would force it to be one, reproducing the Booker contradiction.

Primary source: J. Kaczorowski and A. Perelli,
[*On the structure of the Selberg class, VII: 1<d<2*](https://doi.org/10.4007/annals.2011.173.3.4),
Ann. of Math. 173 (2011), especially the analytic-continuation axiom and
the discussion of degrees below one.

### 5.2 Ratios of Artin L-functions

Hochfilzer--Oliver prove, for example, that the quotient of a primitive
three-dimensional Artin L-function by `xi(s)` has infinitely many poles
under their stated `+1`-eigenspace hypothesis.  Their method assumes
finitely many poles, invokes a converse theorem, and contradicts the Euler
product.  It extends the same global phenomenon; it gives no rightmost or
selected-zero conclusion for the equal-degree quotient `(1+epsilon)/V`.

Primary source: L. Hochfilzer and T. Oliver,
[*Ratios of Artin L-functions*](https://doi.org/10.1016/j.jnt.2021.07.007),
J. Number Theory 236 (2022), Theorem 1.1; see also
[arXiv:1910.02821](https://arxiv.org/abs/1910.02821).

### 5.3 The one existing horizontal family theorem

There is a serious but conditional-on-selection escape.  Let `M/Q` vary
over `S_3` Galois extensions of discriminant at most `Q`, and take the
unique minimal normal subgroup `N=A_3`.  Then

```text
zeta_M(s)/zeta_k(s)=L(s,V)^2.                               (5.1)
```

Lemke Oliver--Thorner--Zaman, Theorems 3.1, 3.3, and 3.7,
show that, apart from `O_epsilon(Q^epsilon)` fields, `L(s,V)` is holomorphic
and nonvanishing in the region

```text
1-Re(s)
 <=[epsilon/(10|S_3|)]
    [log d_M/(log d_M+log(3+|Im s|))].                      (5.2)
```

through their first (very large) height range.  In particular their region
contains a fixed near-one box, with width depending on `epsilon`, for
heights bounded by a large power of `d_M`.

Thus, if an admissible R146 field outside the exceptional set can be chosen
with a selected zeta zero `rho` in (5.2), then `n_V=0` there and

```text
ord_rho F_3=e+n_eps>=e>0.                                  (5.3)
```

This would exclude the regular null and protect the target zero.  It is not
yet a theorem for the R146 family: prescribing no `3`-cycle Frobenius at a
long initial prime segment is a very sparse, zero-correlated condition, and
the presently proved count of such fields need not exceed the
`O(Q^epsilon)` exceptional set within the required discriminant budget.

Primary source: R. J. Lemke Oliver, J. Thorner, and A. Zaman,
[*An approximate form of Artin's holomorphy conjecture and non-vanishing of
Artin L-functions*](https://doi.org/10.1007/s00222-023-01232-2),
Invent. Math. 235 (2024), Theorems 3.1, 3.3, and 3.7; see also
[arXiv:2012.14422](https://arxiv.org/abs/2012.14422).

## 6. Analytic torsion does not trivialize the quotient

Identity (1.2) is the supertrace identity

```text
sum_j (-1)^j tr(g|exterior^j Std)=det(1-g|Std).             (6.1)
```

It is tempting to read (6.1) as an acyclic torsion cancellation.  That
interpretation supplies no divisor theorem.

Ray--Singer analytic torsion is a special value

```text
log T_RS=(1/2)sum_q (-1)^q q zeta_(Delta_q)'(0).             (6.2)
```

It requires a geometric cochain complex and contains the weight `q` absent
from (6.1).  The exterior algebra here has no differential.  A Koszul
differential obtained by contraction or exterior multiplication by a
vector is `S_m`-equivariant only when that vector is invariant, while

```text
Std^(S_m)=0.                                                (6.3)
```

Fried/Ruelle-type identities likewise evaluate torsion at a special
spectral value for an acyclic flat bundle; they do not make an Artin Euler
quotient divisor-free as a function of `s`.  In the cubic case, (3.6)
exhibits the obstruction concretely: the relative determinant contains
`zeta_M` in the denominator, so a torsion-like interpretation permits the
poles rather than removing them.

Primary source for (6.2): D. B. Ray and I. M. Singer,
[*R-torsion and the Laplacian on Riemannian manifolds*](https://doi.org/10.1016/0001-8708(71)90045-4),
Adv. Math. 7 (1971).

## 7. Audit of the regular-order multiplicity escape

Let `E/Q` be Galois with group `G`, `n=|G|=[E:Q]`, and let `rho!=1` be a
nontrivial zeta zero of order

```text
e=ord_rho zeta(s)>0.                                       (7.1)
```

For `chi in Irr(G)`, put

```text
n_chi=ord_rho L(s,chi),
Theta_rho=sum_chi n_chi chi.                                (7.2)
```

This is the Heilbronn virtual character.  Artin formalism and our sign
convention give

```text
ord_rho zeta_(E^H)=<Theta_rho,Ind_H^G 1>,
ord_rho zeta_E=Theta_rho(1)=sum_chi n_chi chi(1).            (7.3)
```

The R145 null direction is

```text
n_chi=e chi(1),                Theta_rho=e Reg_G.            (7.4)
```

It has `n_1=e` as required and annihilates every degree-zero virtual
character.  Equations (7.3)--(7.4) give

```text
ord_rho zeta_E=e sum_chi chi(1)^2=e|G|=en,
ord_rho zeta_(E^H)=e[G:H].                                  (7.5)
```

For `S_3`, (7.4) reads

```text
(n_1,n_epsilon,n_V)=(e,e,2e).                               (7.6)
```

Then `ord_rho zeta_k=2e`, `ord_rho zeta_C=3e`, and
`ord_rho zeta_M=6e`; both (3.5) and (3.6) have order zero.

### 7.1 Stark and Foote--Murty allow the pattern

Foote--Murty prove

```text
sum_(chi in Irr(G)) n_chi^2
 <=(ord_rho zeta_E)^2.                                     (7.7)
```

They in fact obtain the stronger pointwise Heilbronn-character bound
`|Theta_rho(g)|<=Theta_rho(1)`.  Under (7.4), the two sides of (7.7) are

```text
e^2|G|        and        e^2|G|^2,                          (7.8)
```

so there is a factor `|G|` of slack.  The pointwise bound is also satisfied:
`e Reg_G` vanishes away from the identity and equals `e|G|` at the
identity.  Heilbronn restriction is satisfied exactly because

```text
Res_H^G Reg_G=[G:H]Reg_H.                                  (7.9)
```

Stark's theorem says that if `ord_rho zeta_E<=1`, every Artin L-function is
holomorphic at `rho`; Foote--Wales has an order-at-most-two version for
solvable extensions.  These are local holomorphy criteria, not upper bounds
on `ord_rho zeta_E`, and (7.5) is outside their hypotheses.

Primary sources: H. M. Stark,
[*Some effective cases of the Brauer--Siegel theorem*](https://doi.org/10.1007/BF01405166),
Invent. Math. 23 (1974), Theorem 3; and R. Foote and V. K. Murty,
[*Zeros and poles of Artin L-series*](https://doi.org/10.1017/S0305004100001316),
Math. Proc. Cambridge Philos. Soc. 105 (1989), especially the proposition
giving (7.7).

### 7.2 Higher-multiplicity existence results point the other way

Hu--Kaneko--Martin--Schildkraut prove unconditionally that a nonabelian
Galois extension produces infinitely many nontrivial Dedekind-zeta zeros of
multiplicity at least two.  If the group has an irreducible representation
of degree at least three, they obtain infinitely many of multiplicity at
least three.  They explicitly note that their methods do not prescribe the
larger multiplicities predicted by Artin factorization.  These are lower
bounds, not caps, and do not conflict with (7.5).

Primary source: D. Hu, I. Kaneko, S. Martin, and C. Schildkraut,
[*Order of zeros of Dedekind zeta functions*](https://doi.org/10.1090/proc/16041),
Proc. Amer. Math. Soc. 150 (2022), Theorems 1.1--1.2; see also
[arXiv:2107.03269](https://arxiv.org/abs/2107.03269).

The 2026 result of Gun--Sahu proves, among other parity statements, that a
Galois number field of odd degree has no nontrivial real zero of odd order.
The RH target here is nonreal, and an `S_m` normal closure has even degree
for `m>=2`; this theorem does not constrain (7.4).

Primary source: S. Gun and D. Sahu,
[*On higher order real zeros of Dedekind zeta functions*](https://doi.org/10.1017/S0305004126101923),
Math. Proc. Cambridge Philos. Soc. 181 (2026).

### 7.3 The best elementary explicit upper bound is much larger than `n`

Let `d_E` be the absolute discriminant and let `N_E(T)` count nontrivial
zeros with `|Im rho|<=T`, including multiplicity.  Hasanalizade--Shen--Wong
prove, for `T>=1`,

```text
|N_E(T)-T/pi log[d_E(T/(2pi e))^n]|
 <=0.228(log d_E+n log T)+23.108n+4.520.                    (7.10)
```

If `rho=beta+it`, `t>=2`, has multiplicity `mu`, then
`mu<=N_E(t+1)-N_E(t-1)`.  Applying (7.10) at both endpoints and using

```text
d/dT {T/pi log[d_E(T/(2pi e))^n]}
 =(1/pi)[log d_E+n log(T/(2pi))]                            (7.11)
```

gives the explicit safe consequence

```text
mu
 <=1.093[log d_E+n log(t+1)]+46.216n+9.040.                (7.12)
```

Writing `rd(E)=d_E^(1/n)`, this is

```text
mu/n
 <=1.093[log rd(E)+log(t+1)]+46.216+9.040/n.                (7.13)
```

For the dangerous simple-target case `e=1`, the regular pattern needs only
`mu=n`, far below (7.12).  For a fixed `E`, the right side grows with
height while the required `en` is fixed.  If `E` is allowed to depend on
the target, (7.13) retains the extra `log rd(E)+log t` factor.  Thus the
standard explicit zero count cannot exclude (7.5) in either regime.

Primary source: E. Hasanalizade, Q. Shen, and P.-J. Wong,
[*Counting zeros of Dedekind zeta functions*](https://doi.org/10.1090/mcom/3665),
Math. Comp. 91 (2022), Corollary 1.2; see also
[arXiv:2102.04663](https://arxiv.org/abs/2102.04663).

### 7.4 Near one, the available gain is field-dependent and ultra-thin

For sufficiently large `d_E`, Kadiri proves that for `|t|>1`,
`zeta_E(beta+it)` has no zero when

```text
beta>
1-1/[12.55 log d_E+9.69n log|t|+3.03n+58.63].              (7.14)
```

For `|t|<1`, there is at most one zero in

```text
beta>1-1/(12.74 log d_E),                                  (7.15)
```

and it is simple and real.  Hence a regular multiple zero is impossible in
(7.15), but so is the nonreal target under discussion.  In root-discriminant
form, the denominator in (7.14) is

```text
n[12.55 log rd(E)+9.69 log|t|+3.03]+58.63.                 (7.16)
```

This width shrinks with the degree and height.  It does not yield a fixed
`delta>0`, and allowing the auxiliary field to grow makes it narrower.

Primary source: H. Kadiri,
[*Explicit zero-free regions for Dedekind zeta functions*](https://doi.org/10.1142/S1793042112500078),
Int. J. Number Theory 8 (2012); see also
[arXiv:1106.1868](https://arxiv.org/abs/1106.1868).

Even granting a log-free density estimate of the idealized shape

```text
N_E(sigma,T) << (d_E T^n)^(C(1-sigma)),                     (7.17)
```

a single zero of multiplicity `en` is excluded only when roughly

```text
(1-beta)n[log rd(E)+log T] << log(en).                      (7.18)
```

That is an ultra-near-one scale of order
`log n/[n(log rd(E)+log T)]`, not a fixed strip.  Equation (7.18) is also
why ordinary density estimates cannot replace target-specific joint-zero
information.

Under GRH, Grenie--Molteni obtain much sharper explicit multiplicity
bounds, but GRH already excludes the off-line target and therefore cannot
serve as an unconditional escape.  See
[*Zeros of Dedekind zeta functions under GRH*](https://doi.org/10.1090/mcom/3008),
Math. Comp. 85 (2016), Theorem 1.1 and Corollary 1.2.

## 8. Verdict and exact live target

The global divisor question is settled as far as present classification
theorems can settle it:

```text
F_m is not a disguised pole-free degree-zero L-function;
its zeros and poles are necessarily infinite;
for m=3 both residual orientations have T log T mass;
infinitely many of its zeros genuinely retain a zeta zero.  (8.1)
```

None of (8.1) is horizontal.  All the cited theorems are compatible with
the `T log T` pole/zero surplus lying on `Re(s)=1/2` and with cancellation
at every selected off-line zeta zero.

The exact pointwise target for a cubic exterior field `M` is

```text
ord_rho L(s,V_M)
 < ord_rho zeta(s)+ord_rho L(s,epsilon_M),                  (8.2)
```

at a selected right-edge zeta zero `rho`; the stronger sufficient condition
is

```text
L(rho,V_M)!=0.                                              (8.3)
```

A strip-counting version would prove, for some `sigma>1/2`,

```text
sum_(Re rho>=sigma, 0<Im rho<=T)
 max(ord_rho zeta-ord_rho L(s,V_M),0) > 0                  (8.4)
```

whenever zeta has a zero in that right strip.  Booker proves only the
unrestricted infinite-height analogue of (8.4), with no `sigma`.

There are now exactly two credible ways to obtain (8.2):

1. a zeta-specific horizontal joint-zero theorem for `zeta` and the
   dihedral standard factors; or
2. a quantitative count of locally masked `S_3` fields large enough to
   escape the Lemke Oliver--Thorner--Zaman exceptional set within the R146
   conductor/root-discriminant budget.

A generic Dedekind-zeta multiplicity bound, a degree-zero classification,
or analytic torsion does not reach (8.2).  This report proves neither a fixed
zero-free strip nor the existence of zeta zeros approaching one.

Successor:
[`R150-TRANSLATED-CARRIER-AND-FUNCTIONAL-EQUATION-GATE.md`](R150-TRANSLATED-CARRIER-AND-FUNCTIONAL-EQUATION-GATE.md).
