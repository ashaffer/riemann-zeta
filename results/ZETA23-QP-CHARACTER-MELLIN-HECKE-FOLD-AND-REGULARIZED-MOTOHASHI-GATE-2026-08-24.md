# QP character--Mellin removal, Hecke-fold obstruction, and regularized Motohashi gate

**Date:** 2026-08-24  
**Scope:** the coprime double-Poisson sector of `(2E.F7o20y)`, its lower
DFI blocks, and the proposed noncuspidal `GL(3)` repair.

## Binary verdict

There are four separate conclusions.

```text
moving fan congruence in the coprime c-sector:
    REMOVABLE EXACTLY by unitary character Fourier transform;

remaining c-dependence of the Fourier weights:
    REMOVABLE by sign/dyadic Mellin inversion;

opposite-cusp oldforms and GL(2) continuous spectrum:
    COMPATIBLE with the resulting nebentypus Kuznetsov formula;

fold of the resulting difference-of-products coefficient into two
short Hecke polynomials:
    FALSE by an exact two-spike counterexample;

coefficient-blind punctured autocorrelation bound at the tensor norm:
    FALSE by an exact D^3 lower bound;

Yang Type-I reciprocity for pi=1 boxplus 1 boxplus 1:
    RELEVANT, but does not state the arbitrary-mask vector square function;

Suvitie's shifted-divisor mean square:
    DOES NOT IMPLY that vector square function;

Hou--Pan's prime-level cuspidal GL3 large sieve and its stated
two-Kloosterman bilinear estimate:
    GENUINELY SHARP for one boundary sequence, but DOES NOT MATCH the
    one-modulus DFI kernel or the common-carrier two-index tensor;

full mask-dependent subtraction of every singular, degenerate, and polar
channel, followed by a D^2 regularized square-function bound:
    OPEN, and exactly the remaining plausible Motohashi route.
```

The common carrier can be stored *geometrically* in the second `GL(3)`
Whittaker coordinate: `(m,n)=(b,ac)` corresponds to
`diag(abc,b,1)`.  It cannot be stored with the required arbitrary shell and
`z` weights in one fixed low-conductor Hecke eigenvector.  Treating those
weights as an external two-index tensor is possible formally, but the
needed one-unipotent Plancherel estimate is then the original
Hilbert-valued BDH gate, not a consequence of existing scalar reciprocity.

This report sharpens, rather than replaces,
[`ZETA23-QP-MASK-PRESERVING-LOCAL-LIFT-AND-GL3-RECIPROCITY-AUDIT-2026-08-24.md`](ZETA23-QP-MASK-PRESERVING-LOCAL-LIFT-AND-GL3-RECIPROCITY-AUDIT-2026-08-24.md).

---

## 1. Exact double-Poisson normal form

Fix coprime step parameters `R,S`, put `N=R*S`, and restrict first to
`(c,N)=1`.  In the conventions of `(2E.F7o20y)`, one completed cell is

```text
T_(c,a)(r,s)
 =J*K/c
  *sum_(nu == U0*r*c mod R)
   sum_(mu == V0*s*c mod S)
    W1hat(J*nu/(c*R))*W2hat(K*mu/(c*S))
    *e_c(-a_bar*N_bar*nu*mu).                         (1.1)
```

Writing

```text
nu=U0*r*c+R*x,             mu=V0*s*c+S*y              (1.2)
```

gives the exact quotient form

```text
T_(c,a)(r,s)
 =J*K/c sum_(x,y)
   W1hat(J*(U0*r/R+x/c))*W2hat(K*(V0*s/S+y/c))
   *e_c(-a_bar*x*y).                                  (1.3)
```

Indeed `N_bar*(R*x)*(S*y)=x*y (mod c)` and every term containing `c`
vanishes modulo `c`.

For two copies, with `Delta=nu*mu-nu'*mu'`, the primitive numerator sum is

```text
1/c sum_(a mod c)^* e_c(-a*h-a_bar*N_bar*Delta)
  =S(-h,-N_bar*Delta;c)/c.                            (1.4)
```

Equivalently, in the quotient variables,

```text
N_bar*Delta == x*y-x'*y' (mod c).                     (1.5)
```

The quotient in (1.3) therefore exposes the issue correctly, but it is not
the best coordinate system for the `c`-sum.  The congruences in (1.1) can
be diagonalized before taking the quotient.

---

## 2. Character removal of the moving fan congruence

### Theorem 2.1 (unitary fan diagonalization)

Let `(U*c,R)=1`.  For each divisor `g|R`, put `R_g=R/g` and restrict the
fan coefficient `alpha_r` to `(r,R)=g`.  Define

```text
alpha_tilde_g(chi)
 =phi(R_g)^(-1/2)
  sum_(r0 mod R_g)^* alpha_(g*r0)*conj(chi(r0)).       (2.1)
```

Then

```text
sum_((r,R)=g) alpha_r * 1_(nu == U*r*c mod R)
 =1_((nu,R)=g)*phi(R_g)^(-1/2)
  *sum_(chi mod R_g) alpha_tilde_g(chi)
     chi(nu/g)*conj(chi(U*c)).                         (2.2)
```

Moreover,

```text
sum_(chi mod R_g)|alpha_tilde_g(chi)|^2
 =sum_((r,R)=g)|alpha_r|^2.                            (2.3)
```

**Proof.**  On the indicated gcd stratum, division by `g` turns the
congruence into

```text
nu/g == U*c*r0 (mod R_g).                              (2.4)
```

Multiplication by `U*c` permutes the unit group modulo `R_g`.  Apply
Fourier inversion on that finite abelian group.  Its normalized Parseval
identity is (2.3). `square`

The same theorem applies to the `S`/colour fan.  Every occurrence of a
character contributes `conj(chi(c))`, and every conjugated occurrence
contributes `chi(c)`.  In the opposite-cusp pairing, the net modulus factor
has the form

```text
conj(Xi_R(c))*Xi_S(c).                                 (2.5)
```

This is a nebentypus factor, not an uncontrolled permutation of the fan.

The normalized character sum itself costs no power.  Cauchy and (2.3)
give

```text
phi(R_g)^(-1/2) sum_chi |alpha_tilde_g(chi)|
 <= ||alpha||_2.                                      (2.6)
```

Thus the number of characters is not the obstruction, provided the
subsequent estimate is uniform in the character and its conductor.

### Exact scope

The theorem assumes `(c,R)=1`.  If `(c,R)>1`, multiplication by `c` is not
a permutation and the strata depend on `(c,R)`; conductor-lowering terms
must be split separately.  Formula `(1.1)` itself uses `N_bar (mod c)`, so
the present theorem exactly covers the coprime sector to which the proposed
opposite-cusp Kuznetsov identification applies.  It is not a claim that all
noncoprime DFI sectors have already been spectrally completed.

---

## 3. Mellin removal and the opposite-cusp Kuznetsov family

After (2.2), retain `nu` rather than `x` as the summation variable.  Split
`nu=0`, `nu>0`, and `nu<0`, and dyadically localize each nonzero sign.  If
`F` denotes one resulting smooth weight, Mellin inversion gives

```text
F(J*|nu|/(c*R))
 =1/(2*pi*i) int_(Re w=sigma) MF(w)
    *(J*|nu|/R)^(-w)*c^w dw.                           (3.1)
```

The `nu` list and its character are now independent of `c`; all remaining
modulus dependence is a scalar Mellin monomial and the character (2.5).
The zero axes are separate Ramanujan/degenerate terms.

The character in (2.5) is exactly the one occurring in the
Atkin--Lehner-cusp Kloosterman formula of Kiral--Young,
[Theorem 2.7 in the source](https://arxiv.org/abs/1710.00914).  In their
notation, specialize

```text
p=q=1,             u=R,             v=S.              (3.2)
```

For an even character `Xi=Xi_R*Xi_S (mod R*S)`, their theorem gives

```text
S_(1/R,1/S)(m,n;c*sqrt(R*S);Xi)
 =f(Xi,R,S)*conj(Xi_R(c))*Xi_S(c)
  *S(overline(R*S)*m,n;c),                             (3.3)
```

with `(c,R*S)=1`.  The harmless factor `f` is independent of `c`.  Formula
(3.3) is the exact geometric realization of (2.5) and (1.4).

Odd total character parity is handled only after the usual parity split:
one uses a Kuznetsov weight whose integer weight has the same parity as
`Xi(-1)`.  The displayed Kiral--Young formula is the even, weight-zero
sector.  This bookkeeping is not a power loss, but it should not be hidden
inside (3.3).

Kiral--Young's oldform lemma shows that an Atkin--Lehner operator sends the
oldform list indexed by divisors `ell|L` to the same list with

```text
v_p(ell) -> v_p(L)-v_p(ell),                            (3.4)
```

up to the unit Atkin--Lehner eigenvalue.  On an orthonormal oldclass this
is a unitary permutation, so changing to the two cusps does not create a
power loss.  The full Kuznetsov formula also contains the Eisenstein and
scattering spectrum.  Consequently oldforms and `GL(2)` Eisenstein series
are not an obstruction to the *spectral decomposition* once (2.2)--(3.3)
have been made.

They do not imply a sharp norm for the data coefficient on that spectrum.
That is the next, genuinely false, fold.

---

## 4. The lower DFI blocks are below the first nonzero dual block

At the balanced endpoint put

```text
D=q^(16/33),       Y=sqrt(D)=q^(8/33),
C=q^(25/33),       N=R*S=C^2,
J=K=N/Y=q^(42/33), B0=C^2/D=q^(34/33).                (4.1)
```

The Heath--Brown/DFI weight `h(x,y)` is independent of `y` whenever
`|y|<=x/2`.  With

```text
x=c/C,                  y=n/C^2,        |n|<=B0,       (4.2)
```

this holds as soon as

```text
c>=2*C/D=q^(9/33) up to the fixed factor 2.            (4.3)
```

On the other hand, a nonzero integer dual frequency in (1.1) requires

```text
c*R/J >= 1,
```

and `R asymp C`, so

```text
c >= C/Y=q^(17/33).                                    (4.4)
```

The ratio between (4.4) and (4.3) is `Y/2`.  Therefore every block capable
of carrying a nonzero double-Poisson frequency lies in the exact
mismatch-independent range of the DFI weight.  Below `C/Y`, only zero axes
survive, apart from arbitrarily small Schwartz tails.

This proves the promised lower-block statement:

```text
nonzero lower DFI blocks:  same scalar c-weight as the top block;
blocks below C/Y:          zero-axis/degenerate only.                  (4.5)
```

It does **not** remove the exact mismatch cutoff before Poisson, and it
does not estimate the zero axes.  The exact signed-shift treatment of that
cutoff is recorded in
[`ZETA23-QP-EXACT-DFI-BANDPASS-ZERO-ARC-COLLAPSE-2026-08-22.md`](ZETA23-QP-EXACT-DFI-BANDPASS-ZERO-ARC-COLLAPSE-2026-08-22.md).

---

## 5. Exact counterexample to the short Hecke fold

For short sequences `a,b` define their product convolution

```text
u(t)=sum_(mn=t)a_m*b_n,                                 (5.1)
```

and its additive autocorrelation

```text
B_Delta=sum_t u(t+Delta)*conj(u(t)).                    (5.2)
```

The Kuznetsov coefficient forced by (1.4) is

```text
A_pi=sum_(Delta!=0) B_Delta*rho_pi(Delta).              (5.3)
```

It is an additive autocorrelation in a **difference of products**.  It is
not, in general, the product of the two original short Hecke polynomials.

### Theorem 5.1 (two-spike Hecke-fold obstruction)

For every integer `Y>2`, take

```text
a=delta_1+delta_Y,              b=delta_1-delta_Y.       (5.4)
```

Then

```text
u=delta_1-delta_(Y^2),
B_(Y^2-1)=-1.                                           (5.5)
```

But `lambda_pi(Y^2-1)` cannot occur in the formal product of two Hecke
polynomials supported on indices at most `Y`.

**Proof.**  The unramified relation is

```text
lambda(m)lambda(n)=sum_(d|(m,n))lambda(m*n/d^2).         (5.6)
```

If `d>=2`, then `m*n=d^2*(Y^2-1)>Y^2`, impossible for `m,n<=Y`.  If
`d=1`, then `m*n=Y^2-1`; since `(m,n)!=(Y,Y)`, one has
`m*n<=Y*(Y-1)<Y^2-1`, again impossible.  Equations (5.4)--(5.5) give the
nonzero additive coefficient. `square`

This counterexample survives deletion of `Delta=0`, zero-axis subtraction,
and coherent-ray subtraction.  It rules out the proposed algebraic fold.
It does not rule out a genuine Motohashi transform, whose purpose is
precisely to transform additive correlation rather than pretend it is a
multiplicative Hecke product.

---

## 6. Exact `D^3` punctured autocorrelation barrier

Take flat inputs on `[1,Y]` and put `D=Y^2`:

```text
u(t)=#{(m,n) in [1,Y]^2:m*n=t}.                         (6.1)
```

The coefficients `B_Delta` in (5.2) are nonnegative.  Their total mass is
`Y^4`.  At zero shift,

```text
B_0=sum_t u(t)^2<=Y^3,                                  (6.2)
```

because fixing three of `m,n,m'` determines at most one `n'`.  There are
fewer than `2Y^2` nonzero differences.  Hence Cauchy gives the exact lower
bound

```text
sum_(Delta!=0)|B_Delta|^2
 >=(Y^4-Y^3)^2/(2Y^2)
 =Y^4*(Y-1)^2/2
 =(1/2+o(1))*D^3.                                      (6.3)
```

The squared tensor norm is only

```text
(||a||_2^2*||b||_2^2)^2=Y^4=D^2.                       (6.4)
```

Thus puncturing `Delta=0` leaves an exact factor `D` in squared norm, or
`sqrt(D)` after the final Cauchy step.

The balanced exponent ledger is

```text
desired squared data:       q^(166/33),
raw autocorrelation data:   q^(182/33),
signed-shift factor:        q^(17/33),
desired final exponent:     q^(100/33),
raw final exponent:         q^(108/33),
missing power:              q^(8/33)=sqrt(D).           (6.5)
```

### Fourier form and why a single coherent ray is too small

Let

```text
U_Y(theta)=sum_(m,n<=Y)e(theta*m*n).                    (6.6)
```

Then `B_Delta` is the `Delta`-th Fourier coefficient of `|U_Y|^2`, and

```text
sum_(Delta!=0)|B_Delta|^2
 =int_0^1 (|U_Y(theta)|^2-B_0)^2 dtheta.                (6.7)
```

For fixed real `tau`, a two-dimensional Riemann sum gives

```text
D^(-1) U_Y(tau/D)
 -> F(tau):=int_0^1 int_0^1 e(tau*x*y) dx dy.           (6.8)
```

Therefore, for every fixed compact interval `I`,

```text
D^(-3) int_(theta in I/D)|U_Y(theta)|^4 dtheta
 -> int_I |F(tau)|^4 dtau.                              (6.9)
```

The analytic function `F` is not identically zero.  Hence for every fixed
`A`, an interval beyond `A/D` still contributes `c_A*D^3`.  Removing
`Delta=0`, one residue ray, or a fixed multiple of the natural zero arc
cannot save a power.  A successful tangent projection must remove the
whole coefficient-dependent major-arc/degenerate transform, with a
bandwidth growing with `D`.

---

## 7. What Yang's Type-I formula supplies, and what it does not

[Yang, arXiv:2512.03305](https://arxiv.org/abs/2512.03305), Theorem A,
proves for one generic `GL(3)` representation `pi` and one vector
`varphi in pi` the meromorphic identity

```text
J_cusp^heart+J_Eis^heart
 =J_sing^heart+J_dual^heart
  -J_degen^heart+J_degen^(dag,heart)
  +sum_(sign=+,-) sign*(R_dual^sign-R_I^sign).           (7.1)
```

The theorem explicitly includes noncuspidal `GL(3)`, so the specialization

```text
pi=1 boxplus 1 boxplus 1                                (7.2)
```

is the correct representation-theoretic home of the classical additive
divisor/Motohashi phenomenon.  It also includes the `GL(2)` continuous
spectrum, and Sections 9--10 construct particular analytic newvectors and
bound their dual transforms.

This is not yet the QP estimate, for three exact reasons.

1. **One input vector.**  The left side is linear in a previously
   constructed `W_varphi`.  It does not assert that an arbitrary fan/`z`
   mask is the Whittaker sequence of such a vector with the required norm.
2. **Varying inducing data.**  Character--Mellin components generally live
   in different induced representations/nebentypus sectors.  Applying
   (7.1) componentwise is legitimate in shape, but the required uniform
   square-function bound over those components is not in the theorem.
3. **All degenerate terms matter.**  In the minimal-Eisenstein case,
   `J_sing`, three Weyl-degenerate channels, the opposite degenerates, and
   residues are present.  Deleting `Delta=0` or one coherent ray does not
   equal their sum.

The normalized character transform (2.6) shows that the raw number of
characters need not itself cost a power.  The missing statement is norm
control of the vector synthesis and of every regularizing/dual transform,
uniformly in those characters and in the physical carrier mask.

---

## 8. The common carrier as a second `GL(3)` index

The scalar three-factor coefficient

```text
alpha_N=sum_(a*b*c=N) 1_S(a)1_S(b)z_c                  (8.1)
```

forgets which `b` was used when it is squared.  The physical two-star norm
instead uses

```text
alpha_N(b)=1_S(b)*sum_(a*c=N/b)1_S(a)z_c.              (8.2)
```

There is a genuine positive observation.  In the standard `GL(3)`
Whittaker expansion, the integer indices `(m,n)` occur at the torus point

```text
(m,n) -> diag(m*n,m,1).                                (8.3)
```

Thus

```text
(m,n)=(b,a*c) -> diag(a*b*c,b,1).                      (8.4)
```

The two indices encode the total product and the common carrier exactly.
A two-variable archimedean Whittaker weight can localize `b` and `abc` to
short smooth windows.  Integrating one simple-root unipotent coordinate
would force equality of the `m=b` Fourier index between two copies.

### The local Hecke obstruction

For a normalized spherical `GL(3)` Hecke eigenvector, the two-index
coefficients are not arbitrary.  They obey

```text
A(m,1)A(1,n)=sum_(d|(m,n))A(m/d,n/d),                  (8.5)
```

and therefore

```text
A(m,n)=sum_(d|(m,n))mu(d)A(m/d,1)A(1,n/d).             (8.6)
```

In particular,

```text
A(p,p)=A(p,1)A(1,p)-1.                                (8.7)
```

An arbitrary flat local mask with value one at `(p,1)`, `(1,p)`, and
`(p,p)` violates (8.7), which forces the last value to be zero.  On
coprime indices, (8.6) is completely separable.

For a maximal-parabolic Eisenstein representation

```text
pi=chi boxplus sigma,                                  (8.8)
```

the boundary Dirichlet series is fixed:

```text
A_pi(1,n)=sum_(u*v=n)chi(u)lambda_sigma(v)              (8.9)
```

at unramified places, up to the chosen orientation of the two indices.
Formula (8.9) is structurally close to a factorization sum, but it cannot
equal

```text
sum_(a*c=n)1_S(a)z_c                                   (8.10)
```

for arbitrary `z` and an actual-prime/prime-power shell.  A Hecke character
is not the shell selector and the fixed eigenvalue sequence
`lambda_sigma(c)` is not an arbitrary colour vector.

An archimedean window can restrict `n` and `m*n`; it cannot impose the
finite-place condition on each individual factor in (8.10).  A vector can
be ramified or translated at finitely many selected primes, but doing so at
the whole moving shell abandons the fixed low-conductor spherical vector.
No norm-preserving interpolation theorem of that kind is supplied by
(7.1).

### Exact representation verdict

```text
two GL3 indices retain (b,ac) geometrically:                 YES;
one fixed spherical Hecke eigenvector has arbitrary mask:    NO, by (8.5);
maximal Eisenstein boundary gives a factor convolution:      YES, (8.9);
that convolution accepts arbitrary shell z-data:             NO;
external two-index Poincare/Kuznetsov data can encode it:     FORMALLY YES;
existing GL3/GL2 reciprocity gives its sharp one-fibre norm:  NO.          (8.11)
```

If one inserts the arbitrary tensor

```text
F(b,n)=1_S(b)*1_(8*b*n in q+[-D,D])
       *sum_(a*c=n)1_S(a)z_c,                              (8.12)
```

as external `GL(3)` Whittaker/Poincare data, then
one-unipotent Parseval has exactly the desired common-`b` diagonal.
However, bounding the regularized spectral expansion of (8.12) at its
input norm is precisely a Hilbert-valued `GL(3)` Kuznetsov/BDH theorem.
Standard Type-I reciprocity fixes `pi,varphi` and does not state this
arbitrary two-index large sieve.  Replacing a Hilbert-valued scalar
coefficient by (8.12) is a useful reformulation, not a proof.

The best-possible `GL(3)` spectral large sieve does not silently fill this
gap.  [Blomer--Buttcane, Theorem 2](https://arxiv.org/abs/1512.01152)
proves for one boundary sequence

```text
int_(pi in T*Omega) |sum_(n~N)a_n*lambda_pi(n)|^2/N(pi) dpi
 <<(T^5+T^2*N)^(1+epsilon)*||a||_2^2.                 (8.13)
```

Their Proposition 3 shows that the `T^2*N` term is genuinely unavoidable
for some unregularized data.  Its proof is especially informative: the
lower bound comes entirely from maximal-parabolic Eisenstein series
`E(z,1/2+it;u_j)` and from the pole of the zeta factor in the Mellin
transform of their Hecke coefficients.  It is therefore not a
counterexample to a theorem which first subtracts every maximal-Eisenstein
polar channel.  It is exact evidence that this subtraction is mandatory;
the paper does not prove the corresponding perfect large sieve for the
regular remainder.

Moreover, the `GL(3)` Kuznetsov geometric side contains two-modulus
long-Weyl Kloosterman sums, whereas (1.4) is a one-modulus `GL(2)`
Kloosterman kernel.  Equation (8.13) is therefore neither the two-index
one-unipotent Parseval formula required by (8.12), nor a perfect carrier
projector.

---

## 9. Why Suvitie's mean square does not close the regularized gate

[Suvitie, Theorem 1](https://arxiv.org/abs/1110.3950) proves, for
`1<=L<=N` and `1<=F<<N^(1-epsilon)`, that

```text
sum_(f~F) sum_(n~N)
 |sum_(l~L)d(n+l)d(n+l+f)-Motohashi_main(n,l,f)|^2
 <<N^(2+epsilon)+N^(1+epsilon)*L*F.                    (9.1)
```

This is strong evidence that subtracting the complete Motohashi main term
can remove the `D^3` flat-divisor coherence.  It does not imply the QP
estimate.

1. Equation (9.1) uses the fixed arithmetic coefficient `d`, not the
   arbitrary factor mask (8.10).
2. It averages over both the shift `f` and the additive translation `n`.
   The QP product window is fixed by `q` and moves multiplicatively with
   `b`; it is not the average over `n~N` in (9.1).
3. A bound for the sum of `N` translated windows gives no uniform bound for
   the one adversarial masked window.  At `L=N`, the right side is
   `N^(2+epsilon)(1+F)`, so discarding the `n` average loses exactly the
   available factor.
4. The theorem assumes `F<<N^(1-epsilon)` and does not include the full
   endpoint range of all differences in the product box.
5. Most importantly, it has no external carrier fibre `b` and no
   `ell^2_b`-valued coefficient.

The related cuspidal shifted-convolution theorem
[arXiv:1202.3906](https://arxiv.org/abs/1202.3906) likewise treats fixed
Hecke eigenvalues, not arbitrary factorization masks.

Consequently (9.1) neither proves nor refutes the desired statement

```text
sum_(Delta!=0)
 ||B_Delta(F)-T_Delta(F)||_(ell^2_b)^2
   << D^(2+o(1)) * (normalized input norm),             (9.2)
```

where `T(F)` is the pullback of **all** singular, Weyl-degenerate,
opposite-degenerate, and polar channels for the actual vector (8.12).

### A coefficient-blind main term is definitely insufficient

Let `r_Y(t)` be the flat truncated divisor coefficient from (6.1), and put

```text
u_minus(t)=(-1)^t*r_Y(t).                               (9.3)
```

This remains a sum of two separable product convolutions because

```text
(-1)^(m*n)=1_(m even)+1_(m odd)*(-1)^n.                (9.4)
```

Its autocorrelation is

```text
B_minus(Delta)=(-1)^Delta*B_flat(Delta).                (9.5)
```

This last claim has an exact energy proof.  There are

```text
O=ceil(Y/2)^2
```

odd products and `E=Y^2-O` even products in the factor box.  Hence the
`l1` mass of `B_flat` on odd shifts is `2*E*O asymp Y^4`.  There are at
most `Y^2` odd shifts, so

```text
sum_(Delta odd)B_flat(Delta)^2
 >=4*E^2*O^2/Y^2 >>Y^6=D^3.                            (9.6)
```

For every fixed candidate main sequence `T`, the parallelogram inequality
applied to `B_flat-T` and `B_minus-T` shows that one of their squared norms
is at least the left side of (9.6).  Thus one fixed untwisted Motohashi
main sequence cannot cancel both data sets; one retains `D^3` energy.  The
regularizing term in (9.2) must depend on the full finite local vector and
its mask.  A ramified, vector-specific Yang transform could in principle
do that, so (9.3)--(9.5) are not a counterexample to (9.2).  They are an
exact counterexample to any coefficient-blind subtraction.

### Finite-rank polar subtraction is also insufficient

The companion local-lift report proves a stronger Ky Fan obstruction.  It
constructs `L` modulated autocorrelation vectors whose frame operator on
`1<=h<L` is exactly

```text
diag((L-1)^2,(L-2)^2,...,1).                            (9.7)
```

If a fixed polar space has dimension `d`, tensor-scale control for every
modulation forces

```text
sum_(n=1)^(L-d-1)n^2 <= L^2*(K+1)^2.                   (9.8)
```

For `K=L^(1/4)`, this requires

```text
d>=L-O(L^(5/6)).                                       (9.9)
```

See Theorem 3 of
[`ZETA23-QP-MASK-PRESERVING-LOCAL-LIFT-AND-GL3-RECIPROCITY-AUDIT-2026-08-24.md`](ZETA23-QP-MASK-PRESERVING-LOCAL-LIFT-AND-GL3-RECIPROCITY-AUDIT-2026-08-24.md).
Thus finitely many classical residues or a subpower-rank list of major-arc
profiles cannot be the repair.  A full Eisenstein continuum with effective
rank comparable to `L` is not refuted, but constructing and bounding its
mask-dependent inducing data is already the synthesis theorem in (9.2).

Nor may this continuum simply be charged to the existing physical tangent
projection.  The separated-box fixture in
[`ZETA23-QP-BULK-PRODUCT-AUTOCORRELATION-AND-KLOOSTERMAN-ISOMETRY-BARRIER-2026-08-24.md`](ZETA23-QP-BULK-PRODUCT-AUTOCORRELATION-AND-KLOOSTERMAN-ISOMETRY-BARRIER-2026-08-24.md)
has normalized energy `>=D/32768` after an exact one-modulus pullback, while
its physical fan determinant satisfies

```text
|r*s-r'*s'| asymp D.                                  (9.10)
```

It is broad, not tangent.  What remains unproved in that fixture is the
simultaneous actual prime-power/product-window realization and one common
coefficient vector across moving DFI moduli.  Therefore a full regularized
Motohashi identity could still exploit the global signed mask, but its
subtracted term is not automatically one of the already controlled
positive tangent packets.

---

## 10. Hou--Pan's prime-level large sieve does not supply the missing fold

The December 2025 author upload by
[Hou--Pan, *On a spectral large sieve for GL(3)*](https://www.researchgate.net/publication/399139221_On_the_spectral_large_sieve_for_mathrmGL3)
states, for a prime level `mathfrak q` and fixed compact spectral set
`Omega`,

```text
sum_(pi cuspidal of level mathfrak q, mu_pi in Omega)
 |sum_(n~X) alpha_n*A_pi(1,n)/sqrt(n)|^2
 <<(X+mathfrak q^(2+epsilon))*||alpha||^2.             (10.1)
```

It also states the following smooth bilinear estimate, in the intended
cross-modulus notation:

```text
sum_((c1,c2)=1) F(c1/C1,c2/C2)
 sum_(m~M,n~N) alpha_m*beta_n/sqrt(m*n)
   *S(m,c2;c1)*S(n,c1;c2)/sqrt(c1*c2)

 <<sqrt(Cmax/Cmin)
   *sqrt(C1^2+M)*sqrt(C2^2+N)*||alpha||*||beta||.      (10.2)
```

Here `C1,C2,M,N>=2` and `F` has bounded scaled derivatives.  The
searchable 12-page upload renders two entries in the displayed statement
inconsistently, while the cross form in (10.2) is unambiguous from its
long-Weyl formula (2.7) and the expression used in (3.4).  More
importantly, that upload ends after the proof of Theorem 1.1 and contains
no proof of its separately stated Theorem 1.3.  The audit below therefore
**grants (10.2) in its intended form**.  The non-application is algebraic
and remains true even if (10.2) is accepted as a theorem.

### Exact long-Weyl comparison

On the coprime residual-modulus block used by Hou--Pan, the Kıral--Nakasuji
factorization is

```text
S^(mathfrak q)(m1,m2,n1,n2;
               mathfrak q*D1,mathfrak q*D2)
 =mathfrak q
  *S(n1,mathfrak q*m2*D2;D1)
  *S(m1,mathfrak q*n2*D1;D2).                         (10.3)
```

Their large-sieve application inserts the boundary indices `m2=n2=1`,
so its long-Weyl kernel is

```text
S(m,mathfrak q*D2;D1)*S(n,mathfrak q*D1;D2).          (10.4)
```

Our exact top DFI kernel is instead

```text
K_c(h,Delta)=S(-h,-inverse(R*S)*Delta;c)/c,            (10.5)
```

with **one** modulus `c` and both variables in the same classical
Kloosterman sum.

There is an exact dichotomy.

1. Set `D1=c,D2=1` in (10.3).  For boundary data, the second
   Kloosterman sum is modulo one and disappears.  Formula (10.4) becomes
   `S(m,mathfrak q;c)` and loses `n`, hence loses either `h` or `Delta`.
   It cannot equal (10.5) for varying `Delta` and fixed `mathfrak q`.
2. Allow the interior Whittaker index `m2` to vary.  One can then impose
   `mathfrak q*m2 == -inverse(R*S)*Delta (mod c)`, but `m2` depends on
   both `c` and `Delta`.  This is a general two-index coefficient
   `A_pi(m1,m2)`, not the boundary coefficient `A_pi(1,n)` in (10.1).
3. Keep `D1,D2>1`.  Both scalar variables survive, but the result is the
   two-independent-modulus product (10.4), not the one-modulus kernel
   (10.5).  Taking `D1=D2=c` both violates the coprime residual block and
   lands in the common-content terms of the full decomposition.

The same failure can be seen without representation theory.  Suppose
`c=c1*c2`, `(c1,c2)=1`, and both Kloosterman arguments `a,b` are units.
CRT gives

```text
S(a,b;c)=S(a*c2bar,b*c2bar;c1)
          *S(a*c1bar,b*c1bar;c2).                     (10.6)
```

Rewriting these two factors pointwise in the cross shape from (10.2)
forces

```text
m == a*b*c2bar^3 (mod c1),
n == a*b*c1bar^3 (mod c2).                            (10.7)
```

Thus both nominal sequence indices depend jointly on `a,b` and on the
opposite modulus.  Equation (10.6) is a valid pointwise factorization,
but it does not produce the modulus-independent separated coefficients
`alpha_m*beta_n` required by (10.2).  For (10.5), `a*b` contains
`h*Delta`; this is exactly the difference-of-products/autocorrelation
coefficient which failed the short Hecke fold in Section 5.

### The common carrier and polar subtraction

The two scalar sequences in (10.2) arise after opening the square of the
one-boundary polynomial in (10.1).  They are not an arbitrary tensor
`F(b,n)` with `b` retained as a Hilbert fibre.  A singular-value
decomposition of that tensor would replace its Hilbert norm by a nuclear
norm; no rank-free estimate is stated, and the possible square-root rank
loss is the missing `sqrt(D)` itself.

Nor does first subtracting maximal-Eisenstein or polar terms change the
input class.  Theorem (10.1) is stated for the cuspidal family, but its
proof bounds that family by a positive complete Kuznetsov spectral
integral with boundary coefficients `A_pi(1,n)`.  It is not a Plancherel
bound for the signed regular remainder of an arbitrary two-index vector.

There is also a level mismatch.  `mathfrak q` in (10.1) is one fixed
prime automorphic level.  In the QP character--Mellin reduction, the fan
conductors and opposite-cusp levels divide the varying, generally
composite parameters `R,S`, while the DFI modulus `c~C` ranges over all
integers.  Taking `mathfrak q=c` changes the automorphic family with every
DFI modulus and covers only prime `c`; taking `mathfrak q` to be the
ambient QP prime does not produce the second argument in (10.5).

For the latter attempted identification, Hou--Pan's archimedean support
in their proof also gives `D_i << X/mathfrak q^(1-epsilon)`.  With
`mathfrak q=Q`, `D_i~C=Q^(25/33)` would require
`X>=Q^(58/33)`, larger even than the flattened `h*Delta` range
`Q^(50/33)`.  The desired long-Weyl block is outside that compact-spectral
support.

Smoothness is not the decisive failure.  On the nonzero dual blocks,
Section 4 makes the DFI weight mismatch-independent, and dyadic/Mellin
localization gives acceptable scalar modulus weights.  What remains
non-smooth in the relevant sense is the **joint common-carrier mask**:
it is not a separated pair of scalar coefficient sequences.

### Balanced exponent ledger

Write the ambient QP prime as `Q`, to distinguish it from Hou--Pan's
level.  The balanced scales are

```text
D=Q^(16/33),       C=Q^(25/33),
M_h=C^2/D=Q^(34/33),       N_Delta=D=Q^(16/33).        (10.8)
```

Give a hypothetical factorization `c=c1*c2` the exponents
`C1=Q^x,C2=Q^y`, `x+y=25/33`.  The power in the right side of (10.2),
apart from coefficient norms, is

```text
f(x,y)=|x-y|/2
       +max(2*x,34/33)/2
       +max(2*y,16/33)/2.                             (10.9)
```

The Weil/triangle exponent for the same normalization is

```text
25/33 +(34/33+16/33)/2 =100/66.                       (10.10)
```

The extra factor `C^(-1/2)` which converts the normalization in (10.2)
to `S(...;c)/c` occurs on both sides and does not change any saving below.

If every `c` had two power-sized factors, (10.9) has minimum

```text
f=59/66,
```

attained, for example, at `(x,y)=(17/33,8/33)` and in fact on the whole
interval from the equal split to that point.  The formal saving `41/66`
would be ample.

Uniformity fails on the prime/rough-modulus sector.  There one factor is
one, so the optimistic endpoint `(x,y)=(25/33,0)` gives

```text
f_endpoint=91/66,
saving=100/66-91/66=9/66,
required sqrt(D) saving=8/33=16/66,
deficit=7/66=D^(7/32).                                (10.11)
```

This endpoint is not even covered by the stated hypothesis `C2>=2`;
(10.11) grants its formal continuation.  Primes `c~C` contribute only a
logarithmically small, not power-small, fraction (`asymp 1/log C` with
the `1/c` DFI weight), so they cannot be discarded in a uniform power
bound.

### Hou--Pan verdict

```text
perfect prime-level cusp large sieve for one boundary sequence:  YES;
useful evidence after a genuine mask-preserving GL3 lift:         YES;
exact match to the one-modulus DFI Kloosterman kernel:            NO;
arbitrary two-index/common-b coefficient theorem:                 NO;
uniform sqrt(D) saving even under a formal one-modulus endpoint:  NO;
automatic closure after polar/maximal-Eisenstein subtraction:     NO.    (10.12)
```

The result is therefore informative but gives **no current exponent
improvement**.  A new input must either prove the two-index regularized
square function in Section 11 or exploit cancellation in the prime/rough
one-modulus sector that (10.2) does not see.

---

## 11. Precise remaining theorem

The only surviving Motohashi repair is now sharply formulated.

### Mask-sensitive regularized two-index Motohashi square function

For every character--Mellin component and every common-carrier tensor
`F(b,n)` of the form (8.12):

1. construct a `GL(3)` Whittaker/Poincare vector with torus indices
   `(b,n)` and norm comparable to the physical `ell^2_b` input norm;
2. identify, at all finite places and at infinity, the pullback
   `T_Delta(F)` of every term on the right side of (7.1) other than the
   regular dual spectrum;
3. prove (9.2), uniformly in the fan characters, Mellin parameters,
   oldforms, Eisenstein scattering data, and DFI dyadic block; and
4. show that `T(F)` is exactly the tangent/coherent sector already removed
   by the physical broad--tangent decomposition, rather than an additional
   term of the same size.

At the balanced scale, (9.2) saves exactly the factor `D` in squared norm
and hence the missing `sqrt(D)=q^(8/33)` in (6.5).  Nothing weaker closes
the exponent ledger.

The flat model and Suvitie make this theorem plausible after the *full*
coefficient-dependent regularization.  The arbitrary shell mask,
common-carrier fibre, and vector-norm interpolation are genuinely new.
No theorem checked here supplies them automatically, and no faithful
full-mask counterexample to (9.2) is currently known.

---

## 12. Executable certificate

The exact finite identities and exponent ledgers are implemented in

```text
src/qp_character_mellin_hecke_gate.py
src/test_qp_character_mellin_hecke_gate.py
```

The tests verify:

```text
unitary character reconstruction of the moving fan congruence;
character Parseval and multiplicativity of the cusp modulus factor;
the two-spike forbidden Hecke index for every tested Y;
the exact punctured D^3 energy lower bound;
the DFI cutoff exponents 9/33 and 17/33;
the final sqrt(D)=q^(8/33) loss;
the two-index GL3 torus encoding and spherical prime-corner relation;
the fixed maximal-Eisenstein boundary convolution;
the exact scope flags for Yang, Suvitie, and Hou--Pan;
the CRT-forced joint Hou--Pan indices; and
the `59/66` fantasy versus `91/66` one-modulus endpoint ledger.
```

Replay with

```text
python3 -m pytest -q src/test_qp_character_mellin_hecke_gate.py
```
