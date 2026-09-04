# QP pair energy: adjoint, split `O(2,2)` theta, and the vector-Hecke gate

**Date:** 2026-08-22  
**Verdict:** the adjoint reduction has an exact invariant upgrade.  If

```text
K=(c11,-c12;-c21,c22),       k=det K,
E=a*b^T-a'*b'^T,             det E=-A*B,
```

then `X=K^T E` is traceless and `det X=-kAB`.  Smith normalization gives

```text
u*v+k*t^2=A*B.                                      (0.1)
```

More invariantly, put `K*=adj(K)^T`.  In the fixed split quadratic lattice

```text
W=(M_2(Z),det) = U direct-sum U,
```

the two vectors `(K*,E)` have Gram matrix

```text
diag(k,-A*B).                                      (0.2)
```

Thus the complete off-diagonal pair energy is a sum of nonsingular diagonal
Fourier coefficients of one genus-two theta kernel for the dual pair
`Sp_4 x O(2,2)`.  No varying Smith lattice is present, and the actual
prime-power mask can be retained exactly as a Schwartz test vector.

This does not yet prove the pair-energy bound.  It identifies a sharp new
theorem which would prove it: on the actual-mask subspace, the sum of the
diagonal nonsingular theta coefficients must have `L^2 -> C` norm

```text
D^(1/2) q^o(1).                                    (0.3)
```

The input test vector has norm at most

```text
D^(1/2) q^o(1) ||z||_2^4,                          (0.4)
```

so (0.3) gives the required `D q^o(1)||z||_2^4` off-diagonal energy.
The exponent `1/2` in (0.3) is sharp on the translation tangent family.

Neither regularized Siegel--Weil nor an ordinary scalar GL(2) spectral large
sieve proves (0.3).  After ideal spherical factorization, the standard
large sieve has squared constant `D^2`; (0.3) needs squared constant `D`.
Thus one full factor `D` is missing.  The exact missing input is a
boundary-subtracted, mask-sensitive, vector-valued relative large sieve for
the split `O(2,2)` Bessel transform.  At the large prime `q`, its
nonabelian local factor has the favorable normalized size `O(q^-1)` after
two one-dimensional modes are removed, but the actual mask has not been
factored so that this local convolution theorem applies.

No FC, QP, or new strip theorem is asserted here.

---

## 1. Exact weighted pair energy

Let `tau(a,b,c)` be the retained actual-prime-power triple mask; for the
absolute pair-energy problem it may be replaced by its support indicator.
For an ordered color matrix `C`, write

```text
w_z(C)=|z_c11 z_c12 z_c21 z_c22|,
m(C)=#{(a,b): product_(i,j) tau(a_i,b_j,c_ij)!=0}. (1.1)
```

For two completions let

```text
U=[a a'],       V=[b b'],       H=diag(1,-1),
A=det U,        B=det V,        E=U*H*V^T.         (1.2)
```

Then

```text
E=a*b^T-a'*b'^T,              det E=-A*B.          (1.3)
```

In the all-eight-distinct actual sector, an off-diagonal pair has
`A*B!=0`.  Residual pinning gives

```text
tr(K^T E)=<K,E>=0.                                  (1.4)
```

Let

```text
nu(C,E)=#{ordered distinct completion pairs with difference E}. (1.5)
```

The exact off-diagonal energy is

```text
P_z=sum_(C,E!=0) w_z(C) nu(C,E).                    (1.6)
```

The fixed-secant theorem and the fixed-color theorem already prove

```text
max_(C,E!=0) nu(C,E)<<q^o(1),
sum_(E!=0)nu(C,E)=m(C)(m(C)-1)<<D q^o(1).           (1.7)
```

The desired theorem is

```text
P_z<<D q^o(1)||z||_2^4.                             (1.8)
```

It is enough for FC by the proved quadratic bootstrap.

There is also an exact Schatten formulation.  If `A_c` is the
partial-permutation matrix

```text
(A_c)_(a,b)=tau(a,b,c)
```

and

```text
B_z=sum_c |z_c| (A_c tensor A_c),                  (1.9)
```

then direct expansion gives

```text
||B_z||_(S^4)^4=sum_C m(C)^2 w_z(C).               (1.10)
```

The diagonal pair in (1.10) is `sum_C m(C)w_z(C)` and the remaining part
is exactly (1.6).

---

## 2. The adjoint ternary lattice

Put

```text
X=K^T E.                                           (2.1)
```

Equations (1.3)--(1.4) give

```text
tr X=0,                 det X=det K det E=-kAB.    (2.2)
```

The all-distinct prime-power shell has width ratio strictly below two.
Distinct prime powers in that shell cannot have the same prime base.
Consequently the four entries of `K` have content one.  There are
`P,Q in SL_2(Z)` with

```text
P*K*Q=diag(1,k).                                   (2.3)
```

Set

```text
E_0=P^(-T) E Q^(-T).                               (2.4)
```

The pairing and determinant are unchanged.  Writing

```text
E_0=(x u;v y),
```

the orthogonality relation is `x+k*y=0`.  Hence, for an integer `t`,

```text
E_0=(-k*t u;v t),
u*v+k*t^2=A*B.                                     (2.5)
```

Equivalently, define

```text
L_K={K^T E:E in M_2(Z), tr(K^T E)=0}.              (2.6)
```

Conjugation by `Q^T` is an integral isometry from `L_K` to

```text
L_k={(-k*t u;k*v k*t):u,v,t in Z},                 (2.7)
```

and

```text
(-det X)/k=u*v+k*t^2.                              (2.8)
```

Thus all primitive `K` of determinant `k` give the same integral ternary
lattice.  What varies with `K` is the transported prime-power test vector,
not the quadratic space.

### The coordinate `t` is not invariant

It is tempting to sum `k` first in (2.5), since for `t!=0`

```text
k=(A*B-u*v)/t^2.                                   (2.9)
```

This is valid in one chosen Smith chart but not invariant under the
stabilizer of that chart.  For

```text
h_n=(1 n;0 1),
X=(-k*t u;k*v k*t),
```

one computes exactly

```text
Ad(h_n)X=(-k*t' u';k*v' k*t'),
t'=t-n*v,        v'=v,
u'=u+2*k*n*t-k*n^2*v.                              (2.10)
```

In particular `t=0` can become `t'!=0` inside the same integral lattice.
The split between `t=0` and `t!=0` depends on a rational isotropic flag; it
is not an adjoint-orbit invariant.  An adelic unfolding may still use
(2.9), but it must sum the moving flag and extract all of its constant-term
or tangent channels.  Merely summing form levels before a fixed-`k` large
sieve is therefore not canonical.

---

## 3. Finite `PGL_2` involutions: exact gain and exact coherence

Let `q` be the odd prime parameter.  In the active range,

```text
0<|k|,|A|,|B|<q,
```

so `K,E,X` are invertible modulo `q`.  Cayley--Hamilton and (2.2) give

```text
X^2=-det(X) I.                                     (3.1)
```

Hence `[X]` is a nonidentity involution in `G=PGL_2(F_q)`.  Conversely,
every projective involution has a traceless representative.

There are two conjugacy classes, split and nonsplit.  Their centralizers
have orders `2(q-1)` and `2(q+1)`, so their sizes are

```text
|I_split|   =q(q+1)/2,
|I_nonsplit|=q(q-1)/2.                             (3.2)
```

Let `T_epsilon` be convolution by `1_(I_epsilon)`.  Since the kernel is
central, on an irreducible representation `pi` it acts by

```text
lambda_(pi,epsilon)
 =|I_epsilon| chi_pi(h_epsilon)/dim(pi).            (3.3)
```

The determinant square class gives a nontrivial one-dimensional character
`eta` of `PGL_2(F_q)`.  On one fixed involution class,

```text
|lambda_(1,epsilon)|=|lambda_(eta,epsilon)|
                    =|I_epsilon|.                 (3.4)
```

Thus there are two block-main modes, not one.  The elementary character
table of `PGL_2(F_q)` gives, for every other irreducible representation,

```text
|chi_pi(h_epsilon)|<=2,       dim(pi)>=(q-1)/2,
```

and therefore

```text
max_(pi notin {1,eta}) |lambda_(pi,epsilon)|<<q.   (3.5)
```

If `Pi_ab` denotes projection onto the functions constant on each
determinant-square-class block, then, also for Hilbert-valued functions,

```text
||(1-Pi_ab) T_epsilon F||_2<<q ||F||_2.            (3.6)
```

After normalization by the degree `|I_epsilon|asymp q^2`, (3.6) is an
`O(q^-1)` local factor.  For the union of both classes, the `eta` eigenvalue
is only the difference of the two class sizes, of order `q`.

This favorable local fact does not by itself estimate (1.6).  On a fixed
square-class sector, every actual pair already satisfies `[K^T E] in
I_epsilon`.  Hence `chi_pi([K^T E])` is constant on that sector.  Inserting
the character expansion of `1_(I_epsilon)` into (1.6) returns a scalar
identity: all nonprincipal characters combine coherently to reconstruct
the same positive mass.  Expander mixing applies to a separated kernel
`f(K)g(E)`, whereas the actual four prime-power masks form a joint function
of `(K,E)`.

Thus (3.6) becomes useful only after a mask-preserving factorization or
relative-trace unfolding whose Hilbert norm is controlled.  Producing that
factorization is part of the missing theorem.

---

## 4. A Smith-free orthogonal-pair identity

On `W=M_2(Z)` put

```text
Q(Y)=det Y,
B_Q(Y,Z)=Q(Y+Z)-Q(Y)-Q(Z)=tr(adj(Y) Z).             (4.1)
```

This is the even unimodular split lattice `U direct-sum U` of signature
`(2,2)`.  Define the involution

```text
K*=adj(K)^T.                                       (4.2)
```

For two-by-two matrices,

```text
adj(K*)=K^T,               det(K*)=det K.           (4.3)
```

Consequently (1.3)--(1.4) become

```text
Q(K*)=k,
Q(E)=-A*B,
B_Q(K*,E)=tr(K^T E)=0.                             (4.4)
```

For an ordered pair `Y=(Y_1,Y_2)` define its half-integral Gram matrix

```text
calQ(Y)=
 ( Q(Y_1)          B_Q(Y_1,Y_2)/2
   B_Q(Y_1,Y_2)/2  Q(Y_2) ).                       (4.5)
```

Every actual off-diagonal completion pair therefore gives

```text
calQ(K*,E)=diag(k,-A*B),                            (4.6)
```

a nonsingular diagonal Gram matrix in one fixed quadratic lattice.  This
is the invariant replacement for the varying ternary forms (2.8).

The connected orthogonal group of `W` is isogenous to
`SL_2 x SL_2`; its action is the left-right action on `M_2`.  The
factorization

```text
E=U*H*V^T,             H=diag(1,-1),               (4.7)
```

places the determinant packets `A=det U` and `B=det V` in the two GL(2)
factors.  This is the precise source of the hoped-for two Hecke
polynomials.

---

## 5. Exact genus-two theta coefficient with the actual mask

Define the scalar mask on integral orthogonal pairs by

```text
rho_z(K*,E)=w_z(C) nu(C,E),                         (5.1)
```

where `K` is the signed matrix attached to `C`.  The map `K -> K*` is an
involution, so no information is lost.

The mask can be made into an adelic Schwartz vector without completing it
to a rectangle.  Choose a fixed `eta in C_c^infinity(W(R)^2)` supported in
a sup-norm ball of radius less than `1/3`, with `eta(0)=1`, and put

```text
phi_(z,infinity)(Y)
 =sum_(K,E) rho_z(K*,E) eta(Y-(K*,E)),
phi_(z,f)=1_(W(Z_hat)^2).                           (5.2)
```

The translates in (5.2) are disjoint.  At integral points, `phi_z` equals
the exact prime-power pushforward mask (5.1), and for every fixed Sobolev
order `s`,

```text
||phi_(z,infinity)||_(H^s)^2
 =C_(eta,s) sum_(K,E)|rho_z(K*,E)|^2.              (5.3)
```

Thus retaining the actual mask is rigorous; the issue is estimating this
nonfactorizable, `q`-dependent test vector, not defining it.

Let `omega` be the Weil representation for the dual pair

```text
Mp_4 x O(W)
```

on `S(W(A)^2)`, and define

```text
Theta(g,h;phi)=sum_(Y in W(Q)^2)(omega(g,h)phi)(Y). (5.4)
```

For `T in Sym_2(Q)`, additive-character orthogonality gives the exact
Siegel Fourier coefficient

```text
Theta_T(phi)
 =int_(Sym_2(Q) backslash Sym_2(A))
    Theta(n(S),1;phi) psi(-tr(TS)) dS
 =sum_(Y:calQ(Y)=T) phi(Y).                         (5.5)
```

Equations (4.6), (5.1), and (5.5) give

```text
P_z=
 sum_(0<|k|<<D, 0<|n|<<D^2)
 Theta_(diag(k,-n))(phi_z),                         (5.6)
```

where the mask itself restricts `n` to actual products `A*B` and counts
all their realized factorizations.

The identical-completion term has `E=0`.  It lies in the degenerate
coefficients

```text
T=diag(k,0)                                        (5.7)
```

and equals `sum_C m(C)w_z(C)`.  It need not be bounded in the theta step:
the proved quadratic bootstrap absorbs it once (5.6) is `O(D)`.

---

## 6. The exact test-vector norm

The determinant band is a three-coordinate matching.  Applying its
multilinear `ell^(4/3)` bound to the four functions `|z|^2` gives

```text
sum_C w_z(C)^2
 <=||||z|^2||_(4/3)^4
 =||z||_(8/3)^8
 <=||z||_2^8.                                      (6.1)
```

Using (1.7),

```text
sum_(K,E)|rho_z(K*,E)|^2
 =sum_C w_z(C)^2 sum_E nu(C,E)^2
 <=(max_(C,E)nu(C,E))
   *sum_C w_z(C)^2 sum_E nu(C,E)
 <<D q^o(1)||z||_2^8.                              (6.2)
```

Combining (5.3) and (6.2),

```text
||phi_(z,infinity)||_(H^s)
 <<D^(1/2)q^o(1)||z||_2^4.                         (6.3)
```

This is the useful norm calculation: the varying Smith bases and all
prime-power masks cost no more than `sqrt(D)` in the natural `L^2` test
norm.

---

## 7. The sharp theta large-sieve target

Let `M_D` denote the subspace of Schwartz vectors obtained by the exact
pushforward (5.1)--(5.2) from actual prime-power completion pairs.  A
sufficient theorem is:

### Vector theta restriction theorem `(VTR)`

For some fixed Sobolev order `s`, uniformly for `phi in M_D`,

```text
|sum_(0<|k|<<D,0<|n|<<D^2)
      Theta_(diag(k,-n))(phi)|
 <<D^(1/2)q^o(1)||phi_infinity||_(H^s).             (VTR)
```

The finite component is normalized as in (5.2), and degenerate Gram
matrices are omitted.

Equations (5.6), (6.3), and `(VTR)` prove

```text
P_z<<D q^o(1)||z||_2^4,                             (7.1)
```

which closes the pair bootstrap and FC.

The exponent in `(VTR)` is sharp.  In the translation tangent family one
fixed `C` has `m(C)asymp sqrt(D)`, its `asymp D` ordered off-diagonal pairs
have distinct `E`, and `nu(C,E)=1`.  For the flat vector on its four colors,
`rho_z` is constant on `asymp D` points.  Hence

```text
||rho_z||_1/||rho_z||_2 asymp sqrt(D).              (7.2)
```

No uniform exponent smaller than `1/2` is possible.

The restriction to `M_D` is essential.  For arbitrary bump trains on
orthogonal integral pairs, one may select `N` allowed frames with equal
positive coefficients, giving ratio `sqrt(N)` with no relation to `D`.
Thus `(VTR)` is a prime-mask/factorization theorem, not a general bound for
all Schwartz vectors.

---

## 8. Why standard theta and Hecke theorems stop one factor short

The genus-two Siegel--Weil formula is not `(VTR)`.  It computes a
regularized **orthogonal-group average** of (5.4), whereas (5.6) is a
pointwise, mask-dependent theta value.  Since `dim W=4` and the symplectic
rank is two, this is the boundary of the second-term range; the relevant
identity is regularized and has explicit boundary Eisenstein terms.  See,
for example, [Gan--Qiu--Takeda](https://arxiv.org/abs/1207.4709).  Those
identities do not bound an arbitrary physical bump train by (6.3).

The accidental isogeny `SO(2,2) ~ SL_2 x SL_2` explains the Hecke scale.
In the ideal spherical and separated model, (4.7) would produce

```text
A_(pi1,pi2)
 =(sum_(|A|<=D) alpha_A lambda_pi1(A))
  *(sum_(|B|<=D) beta_B  lambda_pi2(B)).            (8.1)
```

Two ordinary length-`D` spectral large sieves give

```text
int int |A_(pi1,pi2)|^2 dmu(pi1)dmu(pi2)
 <<D^(2+o(1))||alpha||_2^2||beta||_2^2.            (8.2)
```

The square of the `(VTR)` norm is only `D^(1+o(1))`.  Thus (8.2) is too
large by one full factor `D`.

Restricting to the diagonal spectrum does not repair this.  The Hecke
identity folds (8.1) to

```text
lambda_pi(A)lambda_pi(B)
 =sum_(d|(A,B))lambda_pi(A*B/d^2),
c_l=sum_(A*B/d^2=l) alpha_A tensor beta_B,          (8.3)
```

with

```text
l<=D^2,
sum_l||c_l||_2^2<<D^o(1)||alpha||_2^2||beta||_2^2. (8.4)
```

The ordinary large sieve for a polynomial of length `D^2` again has
squared constant `D^2`, not `D`.  A new relative saving of `D` is required
in either formulation.

The actual situation is harder than (8.1).  The prime-power masks select
individual determinant-`A` matrices `U`, not the full spherical double
coset.  The spectral coefficient is therefore the operator

```text
sum_(det U=A) alpha_U pi(U),                        (8.5)
```

not the scalar `lambda_pi(A)`.  The analogous statement holds for `V`,
and the four cell masks couple the two packets.  Formal Hilbert
tensorization applies only after these operators have been converted to
fixed, `pi`-independent Hilbert coefficients.  That conversion has not
been proved.

The observation (2.9) identifies where the missing factor might come from:
on a nonconstant Smith/Bruhat cell, the orthogonality equation determines
one form level.  Formula (2.10) shows why a fixed-chart argument is
insufficient.  An invariant proof must obtain this saving from the
nondegenerate relative orbit while subtracting every moving parabolic
constant term.  Those subtracted terms are the automorphic counterpart of
the tangent/stationary packets.

---

## 9. Exact spectral and local factor still needed

Write the regularized `O(2,2)` Plancherel decomposition schematically as

```text
L^2([SO(W)]) = integral_(pi1,pi2) pi1 tensor pi2 dmu
               + residual/Eisenstein terms.        (9.1)
```

For a nonsingular diagonal Gram matrix `T`, let

```text
J_(pi1,pi2;T)
```

denote the corresponding normalized local-global Bessel/orthogonal-frame
functional.  The exact missing estimate is an operator-valued large sieve
of the form

```text
int_(pi1,pi2)
 || sum_(T=diag(k,-n) in T_D)
       J_(pi1,pi2;T) Phi_(pi1,pi2;T) ||_H^2 dmu
 + continuous part
 <<D^(1+o(1)) sum_T ||Phi_T||_H^2,                 (9.2)
```

after projecting away the degenerate and moving-parabolic boundary
channels.  Here `H` retains the four prime-power fan/mask indices; it may
not be collapsed by positive completion.  Equation (9.2), together with
the exact unfolding of (5.6), is the spectral version of `(VTR)`.

At the large unramified prime `q`, Section 3 supplies the desired local
nonboundary norm: after removing the trivial and determinant-square-class
modes, normalized involution-class convolution has norm `O(q^-1)`, and
this remains true after tensoring with `H`.  At primes dividing the
determinant indices, the required oldvector/local-density statement is

```text
sum_(local Smith/oldvector basis v)
 |J_(pi_p,T)(v)|^2
 <<p^(o(v_p(det T))) sum_v||v||^2.                 (9.3)
```

Any loss such as `p^(v_p(det T)/2)` in (9.3) can accumulate to a power of
`D` and destroy (9.2).  Standard scalar newvector formulas do not imply
(9.3) for the arbitrary operator packets (8.5), and the continuous
Eisenstein/scattering indices require the same Bessel normalization.

Thus the exact remaining theorem can be stated without analogy:

```text
boundary-subtracted split-O(2,2) vector Bessel large sieve,
squared norm D^(1+o(1)),
for the uncompleted actual prime-power test vectors.              (9.4)
```

The finite involution calculation identifies a favorable local multiplier;
the `O(2,2)` lift removes varying Smith levels; and (6.2) proves the right
input norm.  What is absent is the global mask-preserving unfolding and
the one-factor-`D` relative spectral saving in (9.2).

---

## 10. Status ledger

```text
X=K^T E in sl_2, det X=-kAB:                         PROVED;
primitive Smith form uv+k t^2=AB:                   PROVED;
t=0 is not Smith-stabilizer invariant:               PROVED;
finite PGL2 involution classes and q^-1 gap:          PROVED;
direct involution character expansion gives mixing:  FALSE (coherent);
orthogonal pair (K*,E) in fixed U+U lattice:          PROVED;
exact genus-two theta coefficient with actual mask:   PROVED;
test-vector L2 norm <=sqrt(D)||z||_2^4:              PROVED;
VTR norm sqrt(D) implies pair energy D:               PROVED CONDITIONALLY;
sqrt(D) norm exponent is sharp:                       PROVED;
ordinary scalar Hecke large sieve reaches VTR:        FALSE (misses D);
boundary-subtracted vector O(2,2) Bessel large sieve: OPEN;
off-diagonal pair energy / FC / QP:                   OPEN.
```
