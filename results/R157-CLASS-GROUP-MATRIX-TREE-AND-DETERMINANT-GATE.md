# R157 class-group matrix-tree and determinant gate

## Status

The class-character bank of R151 has a natural group-circulant matrix.  Its
nontrivial Fourier eigenvalues are the Hecke `L`-functions, and the Laplacian
cofactor is a positive spanning-tree polynomial.  This gives a real new
identity:

```text
det'(zeta_F I-Z)
 =product_(eta!=1)[zeta_F-L_F(s,eta)]
 =M tau,                                                    (0.1)
```

where `M=|C_H|` and `tau` is any Laplacian cofactor.  Every edge series in
`tau` is supported beyond `H`, so `tau` is supported beyond `H^(M-1)`.
Moreover

```text
K=zeta_F det'(zeta_F I-Z)=M zeta_F tau                     (0.2)
```

has nonnegative Dirichlet coefficients, the same support, and retains a
zeta zero when the nontrivial class `L`-values do not vanish there.

This is a genuine positive raw detector, but not a zero-localizing one.  It
has no constant term.  Factoring its first monomial leaves all zeros fixed
and replaces the absolute cutoff `H^(M-1)` by relative frequencies
`log(n/N_0)`, for which there is no large gap.  Absolute support of an
unnormalized Dirichlet series can be moved arbitrarily by multiplication by
`N^(-s)` without changing any zero.

Normalizing by the class-field zeta function does recover a constant-one
nonlinear amplifier:

```text
W=K/zeta_(H_C)=product_(eta!=1)[zeta_F/L_eta-1].            (0.3)
```

It is supported beyond `H^(M-1)`.  When `M-1` is even,
`[1-W]'/[1-W]` has nonnegative coefficients and retains the target.  But its
collective mixed numerator has completed degree and conductor ledger
`asymp M log D`, exactly the sum of the eigenfactor ledgers.  The determinant
packages the mixed divisors; it does not divide their normalized cost by
`M`.  In the uniform off-diagonal specialization the construction is
literally the scalar root filter `1-U^(M-1)` from R153.

```text
group-circulant Fourier diagonalization                    EXACT
directed/undirected matrix-tree normalization              EXACT
positive cofactor support beyond H^(M-1)                  THEOREM
positive raw target detector K                             THEOREM
raw support as a zero-localization gain                    FALSE
normalized determinant amplifier                           EXACT
collective completed ledger smaller than M log D           FALSE
pseudoinverse/resolvent target detector                     FALSE
coefficient-specific class-group determinant estimate      OPEN
fixed uniform zeta zero-free strip                         NOT PROVED
zeros approaching one                                      NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R151-CLASS-CHARACTER-HEAD-QUOTIENT-GATE.md`](R151-CLASS-CHARACTER-HEAD-QUOTIENT-GATE.md),
[`R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md`](R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md),
and
[`R156-MOVING-VALUE-AND-SIGNED-MIXED-PACKET-GATE.md`](R156-MOVING-VALUE-AND-SIGNED-MIXED-PACKET-GATE.md).

## 1. Quotient partial zetas and the convolution matrix

Let `F` be the real quadratic field in R151 and let

```text
G=C_H=Cl(F)/Gamma_H,                 M=|G|>=2.              (1.1)
```

For `g in G`, define the quotient partial zeta function

```text
Z_g(s)=sum_([a] mod Gamma_H=g) N(a)^(-s),                  (1.2)
```

where the sum is over nonzero integral ideals.  For a character
`eta in G^`, inflated to `Cl(F)`, Fourier inversion gives

```text
L_eta(s)=sum_(g in G) eta(g)Z_g(s),
Z_g(s)=M^(-1)sum_(eta in G^) conjugate(eta(g))L_eta(s),     (1.3)

L_1=zeta_F.                                                 (1.4)
```

Index rows and columns by `G` and put

```text
Z(s)_(x,y)=Z_(y x^(-1))(s).                                (1.5)
```

For the Fourier vector `v_eta(x)=eta(x)`, equations (1.3)--(1.5) give

```text
Z(s)v_eta=L_eta(s)v_eta.                                   (1.6)
```

Thus `Z` is normal and diagonalized by the finite Fourier transform.  Its
row and column sums are `zeta_F`.

There are two equivalent matrix-tree interpretations.

* For an arbitrary finite abelian quotient, regard
  `Z_(y x^(-1))` as the weight of the directed edge `x -> y`.
  Translation makes the directed graph balanced and makes all rooted
  arborescence cofactors equal.
* In the present quadratic setting, conjugation of ideals sends a class to
  its inverse without changing its norm.  Hence

  ```text
  Z_g=Z_(g^(-1)),                                           (1.7)
  ```

  so `Z` is symmetric and the same cofactor is the ordinary weighted
  undirected spanning-tree polynomial.

Nothing below depends on choosing the directed or undirected language.

## 2. Laplacian cofactor and exact support amplification

Define

```text
Delta=zeta_F I-Z.                                          (2.1)
```

Its diagonal entry is

```text
zeta_F-Z_e=sum_(g!=e)Z_g,                                  (2.2)
```

and its off-diagonal entries are `-Z_(y x^(-1))`.  Its Fourier eigenvalues
are

```text
lambda_1=0,
lambda_eta=zeta_F-L_eta,                eta!=1.             (2.3)
```

Let `tau` be any principal cofactor of `Delta`.  Kirchhoff's matrix-tree
theorem, or its balanced directed version, gives

```text
tau=sum_T product_({x,y} in T) Z_(y x^(-1)),               (2.4)
```

with the evident directed-edge version in the arborescence convention.
Every coefficient in (2.4) is nonnegative.  Translation makes the `M`
cofactors equal.  Comparing the coefficient of `t` in

```text
det(tI+Delta)=t product_(eta!=1)(t+lambda_eta)              (2.5)
```

with the sum of the cofactors proves the exact normalization

```text
det'(Delta):=product_(eta!=1)lambda_eta=M tau.              (2.6)
```

This also proves (0.1) without any appeal to signs in the Fourier product.

### Theorem 2.1 -- tree-support amplification

Every Dirichlet coefficient of `Z_g`, `g!=e`, at an integer `n<=H` is zero.
Consequently

```text
supp tau subset {n>H^(M-1)}.                               (2.7)
```

#### Proof

If an integral ideal `a` has norm at most `H`, every prime ideal dividing
`a` also has norm at most `H`.  By the definition of `Gamma_H` all of their
classes die in `G`, so the class of `a` is `e`.  This proves the first
claim.  A spanning tree has exactly `M-1` edges.  Each monomial in (2.4) is
therefore a Dirichlet convolution of `M-1` series supported at norms greater
than `H`, and its product norm is greater than `H^(M-1)`.  Positivity rules
out cancellation.  QED.

The same argument shows that a rooted forest with `k` components, and hence
`M-k` edges, is supported beyond `H^(M-k)`.

## 3. The full characteristic polynomial and rooted forests

For a scalar `c`, put

```text
D_c=det(zeta_F I-cZ),
Q_c=product_(eta!=1)(zeta_F-cL_eta).                        (3.1)
```

Spectrally,

```text
D_c=(1-c)zeta_F Q_c.                                       (3.2)
```

On the other hand,

```text
zeta_F I-cZ=c Delta+(1-c)zeta_F I.                         (3.3)
```

Write the matrix-forest expansion as

```text
det(tI+Delta)=sum_(k=1)^M t^k Phi_k,                       (3.4)
```

where `Phi_k` is the positive rooted-forest polynomial with `k` components.
The endpoint normalizations are

```text
Phi_1=M tau,
Phi_M=1.                                                    (3.5)
```

Substituting `t=(1-c)zeta_F/c` in (3.4), and then using (3.2), gives the
exact identity

```text
Q_c=sum_(k=1)^M
     c^(M-k)(1-c)^(k-1) zeta_F^(k-1) Phi_k.                (3.6)
```

For `0<=c<=1`, every term in (3.6) has nonnegative Dirichlet coefficients.
The forest expansion also exposes the target/head tradeoff.

* At `c=1`, only the spanning-tree term survives:

  ```text
  Q_1=Phi_1=M tau,                                         (3.7)
  ```

  with support beyond `H^(M-1)`, but `Q_1` does not retain a
  `zeta_F` zero.
* At every fixed `0<=c<1`, the empty-forest term

  ```text
  (1-c)^(M-1)zeta_F^(M-1)                                 (3.8)
  ```

  remains, so the exact head shift disappears.
* The first derivative transverse to the singular point `c=1` is

  ```text
  K:=-partial_c D_c|_(c=1)
    =zeta_F Q_1=M zeta_F tau.                              (3.9)
  ```

  It retains both positivity and the full tree support.

Thus (3.9) is the unique first forest layer carrying both the target factor
and all `M-1` nonidentity edges.

## 4. A positive raw target detector, and why raw support is not enough

Assume that `rho` is a zero of `zeta_F` and that

```text
L_eta(rho)!=0                         for every eta!=1.     (4.1)
```

Equations (2.6) and (2.3) give

```text
tau(rho)=(-1)^(M-1)M^(-1)
         product_(eta!=1)L_eta(rho)!=0.                    (4.2)
```

Hence `K` in (3.9) has exactly the `zeta_F` multiplicity at `rho`.  By
Theorem 2.1 it is a nonzero Dirichlet series with nonnegative coefficients
supported beyond `H^(M-1)`.  This is the strongest positive statement
supplied directly by the determinant.

It does not provide the normalized logarithmic jet used in R147--R153.
The obstruction is invariant under a monomial shift.

### Theorem 4.1 -- monomial-renormalization obstruction

Let

```text
A(s)=sum_(n>=N_0)a_n n^(-s),       a_n>=0, a_(N_0)>0.      (4.3)
```

Then

```text
A(s)=a_(N_0)N_0^(-s) A_0(s),
A_0(s)=1+sum_(n>N_0)[a_n/a_(N_0)](n/N_0)^(-s).             (4.4)
```

The functions `A` and `A_0` have exactly the same zeros, and

```text
A'/A=-log N_0+A_0'/A_0.                                   (4.5)
```

All positive-order derivatives of the logarithmic derivative therefore
depend only on the relative frequencies

```text
log(n/N_0),                                                (4.6)
```

not on the absolute support `N_0`.

#### Proof

Equations (4.4) and (4.5) are direct factorization and differentiation.
The prefactor is entire and zero-free.  QED.

Multiplication by an arbitrary `L^(-s)` moves the absolute support of every
positive Dirichlet series past `L` without changing any zero.  A concrete
two-term model is

```text
A_N(s)=N^(-s)[1+m^(beta-s)],                               (4.7)
```

whose coefficients are positive and whose zeros

```text
s=beta+(2j+1)pi i/log m                                   (4.8)
```

are independent of `N`.  Thus no zero-free or target-jet theorem can use
absolute first support of an unnormalized series alone.

Applied to `K`, Theorem 2.1 only says `N_0>H^(M-1)`.  After the necessary
normalization, the integer norm spectrum gives no lower bound of size
`(M-1)log H` for (4.6); consecutive possible norms can have logarithmic
ratio as small as `log(1+1/N_0)`.  The matrix-tree identity supplies no
multiplicative gap theorem.  The nominal `H^(M-1)` gain can therefore be
entirely a zero-free monomial prefactor.

## 5. The normalized determinant is the multicharacter nonlinear filter

Let `H_C/F` be the unramified class-field subextension with Galois group
`G`.  Character factorization gives

```text
zeta_(H_C)=product_(eta in G^)L_eta
          =zeta_F product_(eta!=1)L_eta.                   (5.1)
```

For the R151 quotients put

```text
F_eta=zeta_F/L_eta=1+U_eta.                                (5.2)
```

Every `U_eta` has nonnegative Dirichlet coefficients supported beyond `H`.
Using (2.6), (3.9), and (5.1), one obtains the exact normalized identity

```text
W:=product_(eta!=1)U_eta
  =product_(eta!=1)(zeta_F-L_eta)/product_(eta!=1)L_eta
  =K/zeta_(H_C).                                           (5.3)
```

Thus `W` has nonnegative coefficients and

```text
supp W subset {n>H^(M-1)}.                                (5.4)
```

At a point satisfying (4.1) and `zeta_F(rho)=0`,

```text
W(rho)=(-1)^(M-1).                                        (5.5)
```

When `q=M-1` is even, define

```text
P=1-W,
B=P'/P=(-W')/(1-W).                                       (5.6)
```

In the half-plane of absolute convergence, expansion of `(1-W)^(-1)` shows
that `B` has nonnegative Dirichlet coefficients supported beyond `H^q`.
It has a pole at the retained target unless the first target coefficient
degenerates, in which case its order only increases.  In determinant form,

```text
P=[zeta_(H_C)-K]/zeta_(H_C).                               (5.7)
```

If `q` is odd, `W(rho)=-1`; replacing (5.6) by

```text
P=1-W^2                                                   (5.8)
```

restores coefficient positivity and shifts support beyond `H^(2q)`.

Equations (5.3)--(5.8) are a valid normalized amplifier.  They do not create
a new normalized conductor saving.  They are the multicharacter form of the
R153 nonlinear filter, with one collective determinant numerator replacing
the displayed list of scalar mixed values.

## 6. The completed divisor ledger remains linear in M

The spectral product (2.6) is an exact divisor identity.  Each factor

```text
zeta_F-L_eta                                               (6.1)
```

has the common degree-two Gamma and conductor-`D` envelope.  On a fixed
height disc, ordinary completed growth or Jensen bounds therefore give

```text
N_disc(Q_1)
 <<M[log D+log(|gamma|+T+3)+log(M+2)].                     (6.2)
```

The same scale follows directly by summing the eigenfactor ledgers.  Taking
a determinant does not turn the union of their zeros into one degree-two
divisor.

The class field has

```text
D_(H_C)=D^M,                                               (6.3)
```

so `zeta_(H_C)` itself has logarithmic conductor `M log D`.  Both terms in
the collective numerator

```text
zeta_(H_C)-K                                               (6.4)
```

have completed degree `2M` and the same conductor envelope.  Consequently
the absolute numerator-plus-denominator ledger in (5.7) is still

```text
O(M[log D+log(|gamma|+T+3)]).                              (6.5)
```

The signed degree and conductor cancel in the ratio, just as they do for
each `F_eta`, but the absolute local divisor count does not.  Dividing a
logarithmic determinant by `M` would divide its pole residues by `M` as
well; restoring unit target residue restores the ledger (6.5).

At the known arithmetic scale `log D asymp H`, worst-case power-sum
resolution therefore costs `asymp M H`, while (5.4) supplies only the
`M log H` support scale.  The matrix packaging has not changed the ratio.

## 7. Resolvents and pseudoinverses

The Laplacian has the constant vector in its kernel for every `s`, not only
at a zeta zero.  Its Moore--Penrose/Fourier pseudoinverse has eigenvalues

```text
0,                    eta=1,
[zeta_F-L_eta]^(-1),  eta!=1.                              (7.1)
```

Hence

```text
tr(Delta^+ Delta')
 =sum_(eta!=1)(zeta_F'-L_eta')/(zeta_F-L_eta)
 =Q_1'/Q_1.                                                (7.2)
```

It sees exactly the cofactor divisor and is blind to the target eigenvalue.

Conversely, let `P_0=M^(-1)11^*` be the constant Fourier projector.  Where
`Z` is invertible,

```text
tr(P_0 Z^(-1))=1/zeta_F.                                   (7.3)
```

This retains the target pole but also the full undeleted `zeta_F` Euler
head.  Averaging the nontrivial resolvent in (7.2) lowers each residue and
the ledger by the same factor; it supplies neither the missing target pole
nor a head-amplified unit residue.  Cofactor ratios and effective-resistance
entries have denominators `Q_1` and inherit the same mixed divisor.

Thus the resolvent alternatives are exact:

```text
project away constants       -> lose the zeta target,
retain the constant mode      -> retain the undeleted zeta head,
eliminate modes by determinant-> pay Q_1 and its M-fold ledger.             (7.4)
```

## 8. Uniform-weight specialization: exact reduction to R153

There is a sharp algebraic countermodel to any argument using only
group-circulant symmetry, tree positivity, or determinant stability.  Set

```text
Z_e=a(s),
Z_g=b(s)                  for every g!=e,                  (8.1)
```

with `a,b` positive Dirichlet series and `b` supported beyond `H`.  Character
orthogonality gives

```text
zeta_F=a+(M-1)b,
L_eta=a-b                         (eta!=1),                (8.2)

zeta_F-L_eta=M b,
Q_1=(M b)^(M-1),
tau=M^(M-2)b^(M-1).                                      (8.3)
```

Every nontrivial normalized quotient is the same:

```text
U_eta=zeta_F/L_eta-1=M b/(a-b)=:U.                         (8.4)
```

Therefore

```text
W=U^(M-1),                                                 (8.5)
```

and, when `M-1` is even, (5.6) is exactly

```text
[1-U^(M-1)]'/[1-U^(M-1)].                                 (8.6)
```

This is the scalar root-of-unity amplifier of R153.  The specialization is
the complete graph with equal edge weight `b`; its matrix-tree polynomial
is maximally positive and symmetric.  Hence neither matrix-tree positivity
nor determinant packaging alone can rule out the already proved mixed-point
and signed-cancellation countermodels.

Actual class partial zetas are not uniformly equal.  Equation (8.6) does
not rule out a theorem exploiting their coefficient-specific correlations.
It proves precisely that such a theorem must use more than the group
determinant, positivity, stable-polynomial structure, or the completed
conductor envelope.

## 9. Verdict

The class-group matrix produces two useful exact objects:

```text
K=M zeta_F tau       positive raw target detector,
W=K/zeta_(H_C)       normalized multicharacter amplifier.  (9.1)
```

The first has spectacular absolute support but no constant normalization;
monomial renormalization removes that support without moving its zeros.  The
second has the correct normalization and support, but it is exactly a
nonlinear product of the R151 quotients and pays the full `M log D` mixed
divisor ledger.  Pseudodeterminants omit the target mode, while resolvents
which retain it restore the original zeta head.

The only surviving determinant direction is therefore arithmetic rather
than algebraic:

```text
prove a target-conditioned signed zero estimate for
zeta_(H_C)-M zeta_F tau
using correlations among the actual quotient partial-zeta coefficients.   (9.2)
```

No generic matrix-tree, forest, resolvent, conductor, or positivity theorem
supplies (9.2).  The determinant construction does not prove either side of
the fixed-strip dichotomy.
