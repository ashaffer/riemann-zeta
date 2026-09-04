# QP two-index Poincare spectral side and the polar-projection no-go

**Date:** 2026-08-24  
**Scope:** arbitrary finitely supported physical data `f(b,n)`, with both
indices retained as generic `GL(3)` Whittaker indices.

## Binary verdict

The exact two-index spectral side exists and is standard:

```text
f(b,n)
 -> sum_(b,n) f(b,n)*P_(b,n)/(b*n)
 -> sum_(pi) |sum_(b,n)f(b,n)A_pi(b,n)|^2
    + minimal Eisenstein + maximal Eisenstein.          (0.1)
```

At a fixed congruence level, the geometric side is exactly

```text
identity + short Weyl w4 + short Weyl w5 + long Weyl w6. (0.2)
```

For two positive indices, all other Weyl cells are incompatible.  The
residual constant-induced Eisenstein series has no generic Fourier
coefficient and therefore contributes zero.

Subtracting the **complete minimal and maximal Eisenstein projection** is
a genuine Pythagorean contraction in automorphic `L2`.  It is **not** a
contraction at the physical coefficient norm.  The Poincare synthesis map
is not an isometry from `ell^2_(b,n)`: its Gram operator is (0.2), not the
identity.  More decisively, after every noncuspidal component is removed,
one retained cusp form gives the exact finite-support lower bound

```text
||Pi_cusp S_Psi||^2_(ell2(E)->L2)
 >= |<W_pi,Psi>|^2/N(pi) * sum_((b,n) in E)|A_pi(b,n)|^2. (0.3)
```

The coefficient energy on the right is unbounded as `E` grows.  Thus no
uniform arbitrary-data Plancherel contraction at the diagonal coefficient
norm exists, even after the strongest canonical polar subtraction.

This does **not** disprove the desired `D^(2+o(1))` estimate on the special
finite QP hyperbolic mask.  It identifies it exactly as a new
mask-sensitive **two-index cuspidal large sieve**, not a consequence of
Poincare Plancherel.

The primary formulae used below are
[Blomer, Proposition 4 and Sections 7--8](https://arxiv.org/abs/1205.1781)
at level one and
[Blomer--Buttcane--Maga, Theorem 6](https://arxiv.org/abs/1410.5106)
at level `N`.

---

## 1. Exact Poincare synthesis retaining the carrier

Let

```text
X_N=Gamma_0(N)\H_3
```

and let `U` be the upper unipotent subgroup.  Fix
`Psi in C_c^infinity((0,infinity)^2)`.  For `r=(r1,r2)` with both entries
positive, put

```text
Psi_r(z)=e(r1*x1+r2*x2)*Psi(r1*y1,r2*y2),
P_r(z)=sum_(gamma in U(Z)\Gamma_0(N)) Psi_r(gamma*z),
Q_r=P_r/(r1*r2).                                      (1.1)
```

For arbitrary finitely supported data `f(r1,r2)`, define

```text
S_Psi f = sum_r f(r)*Q_r.                              (1.2)
```

Unfolding against a generic automorphic form `varpi` gives

```text
<varpi,Q_r>
 = Atilde_varpi(r)*<Wtilde_(mu_varpi),Psi>,             (1.3)
```

up to the harmless conjugation convention in the inner product.  In the
arithmetically normalized convention of the Kuznetsov formula this is

```text
<varpi,S_Psi f>
 = sqrt(1/N(varpi))*<Wtilde_mu,Psi>
   *sum_r f(r)*A_varpi(r).                             (1.4)
```

Equation (1.4) is the sought carrier-preserving lift.  Taking
`r=(b,n)` retains `b` as the first Whittaker index; no scalarization over
`b` occurs.

The two-index torus point is

```text
(b,n) -> diag(b*n,b,1),                                (1.5)
```

as in the previous report.  The advance here is that (1.2), rather than a
single Hecke eigenvector, accepts an arbitrary external coefficient array.

---

## 2. Complete spectral decomposition

Let

```text
w_Psi(mu)=<Wtilde_mu,Psi>.                              (2.1)
```

Blomer--Buttcane--Maga's level-`N` Kuznetsov formula, summed against
`f(n1,n2)*conj(f(m1,m2))`, gives the exact identity

```text
||S_Psi f||_L2(X_N)^2
 = integral^(N)
    |sum_(b,n) f(b,n)A_varpi(b,n)|^2/N(varpi)
    *|w_Psi(mu_varpi)|^2 dvarpi.                       (2.2)
```

The combined measure in (2.2) contains:

```text
* every cuspidal newform and oldform at level N;
* minimal-parabolic Eisenstein data;
* maximal-parabolic Eisenstein data induced from GL(2);
* the corresponding normalized scattering measures.   (2.3)
```

At level one the split is completely explicit.  Write `nu0=-nu1-nu2`.
Then (2.2) is

```text
C_Psi(f)+E_min,Psi(f)+E_max,Psi(f),                    (2.4)
```

where

```text
C_Psi(f)
 =sum_j |sum_(b,n)f(b,n)A_j(b,n)|^2/||phi_j||^2
       *|w_Psi(nu_j)|^2,                               (2.5)

E_min,Psi(f)
 =1/(4*pi*i)^2 * integral_((0),(0))
   |sum_(b,n)f(b,n)A_(nu1,nu2)(b,n)|^2
   /|zeta(1+3nu0)zeta(1+3nu1)zeta(1+3nu2)|^2
   *|w_Psi(nu1,nu2)|^2 dnu1 dnu2,                     (2.6)

E_max,Psi(f)
 =c/(2*pi*i) * sum_(u_j) integral_(0)
   |sum_(b,n)f(b,n)B_(mu,u_j)(b,n)|^2
   /(|L(u_j,1+3mu)|^2 L(Ad u_j,1))
   *|w_Psi(mu-nu_j/3,2nu_j/3)|^2 dmu.                 (2.7)
```

Here `phi_j` runs through arithmetically normalized `GL(3)` cusp forms,
and `u_j` through arithmetically normalized `GL(2)` cusp forms.  The
coefficient `A_(nu1,nu2)` is the minimal-Eisenstein Hecke coefficient.
The maximal coefficient satisfies

```text
B_(mu,u)(1,m)=sum_(d1*d2=|m|)lambda_u(d1)d1^(-mu)d2^(2mu), (2.8)
```

and is extended to `(b,n)` by the `GL(3)` Hecke relations.

The remaining constant-induced maximal series `E(z,1/2+mu;1)` is a
residue of a minimal Eisenstein series and has only degenerate Fourier
terms.  Its inner product with every `Q_(b,n)`, `b*n!=0`, is zero.  Thus
(2.5)--(2.7) are the complete spectral side in the generic subspace.

---

## 3. Complete geometric side and the four Weyl channels

For `r=(n1,n2)` and `s=(m1,m2)`, define the three kernels below using the
normalizations of
[Blomer--Buttcane--Maga, equations (2.10)--(2.11)](https://arxiv.org/abs/1410.5106):

```text
K4(r,s)
 =sum_(epsilon=+-1)
   sum_(N*D2|D1, n2*D1=m1*D2^2)
    Stilde(epsilon*m2,n2,n1;D2,D1)/(D1*D2)
    *Jtilde_(epsilon;Psi*)(sqrt(n1*n2*m2)/(D1*D2)),    (3.1)

K5(r,s)
 =sum_(epsilon=+-1)
   sum_(N|D1|D2, n1*D2=m2*D1^2)
    Stilde(epsilon*m1,n1,n2;D1,D2)/(D1*D2)
    *Jtilde_(epsilon;Psi)(sqrt(n1*n2*m1)/(D1*D2)),     (3.2)

K6(r,s)
 =sum_(epsilon1,epsilon2=+-1) sum_(N|D1,N|D2)
    S^(N)(epsilon2*m2,epsilon1*m1,n1,n2;D1,D2)/(D1*D2)
    *J_(epsilon;Psi)(sqrt(n2*m1)*D1/D2,
                     sqrt(n1*m2)*D2/D1).              (3.3)
```

Put

```text
Wk_Psi(f)=sum_(r,s)f(r)*conj(f(s))*Kk(r,s).            (3.4)
```

Then the arithmetic evaluation of the same Poincare norm is exactly

```text
||S_Psi f||^2
 =||Psi||^2*sum_r|f(r)|^2
   +W4_Psi(f)+W5_Psi(f)+W6_Psi(f).                    (3.5)
```

The four terms correspond respectively to

```text
identity, short Weyl w4, short Weyl w5, long Weyl w6.  (3.6)
```

For four nonzero generic indices, the compatibility relation in the
Bruhat decomposition kills every other Weyl element.  Equations
(2.4) and (3.5) are the complete two-index trace identity.

This classification also prevents a common category error:
`W4` and `W5` are geometric orbital integrals, not norms of orthogonal
spectral subspaces.  Their quadratic forms need not be positive
separately.  There is no canonical projection `Pi_w4` or `Pi_w5` whose
Pythagorean norm is (3.1) or (3.2).

---

## 4. What full polar subtraction really proves

Inside the generic automorphic Hilbert space, write

```text
H_gen=H_cusp direct_sum H_min direct_sum H_max,        (4.1)
```

with orthogonal Langlands spectral measure.  Let

```text
Pi_Eis=Pi_min+Pi_max.                                   (4.2)
```

For every data vector `f`, the full data-dependent noncuspidal term is
the canonical vector

```text
T_pol(f)=Pi_Eis S_Psi f.                               (4.3)
```

Its coefficients depend on `f`, but its target subspace is fixed.  Exact
Pythagoras gives

```text
||S_Psi f-T_pol(f)||^2
 =||Pi_cusp S_Psi f||^2
 =C_Psi(f),                                            (4.4)

C_Psi(f)+E_min,Psi(f)+E_max,Psi(f)=||S_Psi f||^2.     (4.5)
```

Consequently

```text
C_Psi(f)<=||S_Psi f||^2.                               (4.6)
```

This is a genuine Plancherel contraction in **automorphic `L2`**.

The required physical contraction would instead be

```text
C_Psi(f)<=||Psi||^2*||f||_ell2^2                      (4.7)
```

or its QP-weighted `D^(2+o(1))` analogue.  By (3.5), (4.7) is equivalent
to the new operator inequality

```text
W4_Psi(f)+W5_Psi(f)+W6_Psi(f)
 <=E_min,Psi(f)+E_max,Psi(f)                           (4.8)
```

for every allowed `f`.  Pythagoras does not imply (4.8).  It compares the
left side of (4.4) with the full Poincare norm, whose Gram operator already
contains every Weyl term.

---

## 5. Exact cuspidal obstruction for arbitrary physical data

The failure of an arbitrary-data coefficient contraction is not merely a
logical gap.

### Theorem 5.1 (rank-one cusp alignment)

Fix a generic cuspidal form `pi0` for which

```text
c_(pi0,Psi)=|w_Psi(mu_pi0)|^2/N(pi0)>0.                (5.1)
```

For every finite index set `E subset N^2`, put

```text
S_E=sum_(r in E)|A_pi0(r)|^2,
f_E(r)=1_E(r)*conj(A_pi0(r))/sqrt(S_E).                 (5.2)
```

Then

```text
||f_E||_2=1,
||Pi_cusp S_Psi f_E||^2>=c_(pi0,Psi)*S_E.              (5.3)
```

**Proof.**  Retain only the nonnegative `pi0` summand in (2.5).  The
inner linear form is

```text
sum_(r in E)f_E(r)A_pi0(r)=sqrt(S_E).                  (5.4)
```

This gives (5.3).  The Eisenstein projection is orthogonal to `pi0`, so
subtracting all of (2.6)--(2.7) leaves (5.3) unchanged. `square`

The right side is unbounded over finite `E`.  Here is an elementary local
proof that needs no Ramanujan conjecture.  Choose any unramified prime
`p` for `pi0`, with Satake parameters `alpha_1,alpha_2,alpha_3`.  For
trivial central character,

```text
alpha_1*alpha_2*alpha_3=1,                              (5.5)
```

and the local Hecke generating series is

```text
sum_(k>=0)A_pi0(1,p^k)X^k
 =product_(j=1)^3(1-alpha_j X)^(-1).                   (5.6)
```

The coefficient sequence in (5.6) is never in `ell^2`.

* If some `|alpha_j|>1`, the rational function has a pole inside the unit
  disk, whereas an `ell^2` Taylor series is analytic there.
* Otherwise (5.5) forces all `|alpha_j|=1`.  The rational function has a
  pole on the unit circle, so its radial `L2` norm is unbounded and it is
  not a Hardy `H2` function.

There is no numerator in (5.6), hence no pole cancellation.  Therefore

```text
sum_(k=0)^K|A_pi0(1,p^k)|^2 -> infinity.               (5.7)
```

Taking `E_K={(1,p^k):0<=k<=K}` in (5.3) proves

```text
||Pi_cusp S_Psi||_(ell2(N^2)->L2)=infinity.            (5.8)
```

Thus even the complete data-dependent Eisenstein subtraction does not
turn arbitrary finite coefficient data into a Plancherel contraction at
the diagonal norm.

The finite-support form of the obstruction is useful for the actual QP
domain `Omega_Q`:

```text
||Pi_cusp S_Psi||^2_(ell2(Omega_Q)->L2)
 >=sup_pi |w_Psi(mu_pi)|^2/N(pi)
          *sum_((b,n) in Omega_Q)|A_pi(b,n)|^2.        (5.9)
```

Any claimed finite-scale contraction must in particular beat (5.9).

---

## 6. Consequence for the QP square-function gate

For the physical tensor from the previous report,

```text
f(b,n)=1_S(b)*1_(8*b*n in Q+[-D,D])
       *sum_(a*c=n)1_S(a)z_c,                          (6.1)
```

the two-index Poincare construction is exact: insert (6.1) in (1.2).
No carrier information is lost.  The strongest canonical regularization
is to subtract (4.3), which includes the complete minimal and maximal
Eisenstein continua and all their scattering data.

After that subtraction, the precise remaining assertion is

```text
C_Psi(f)
 <<D^(2+o(1))*(physical normalized input norm).        (6.2)
```

This is a mask-sensitive, vector-valued, two-index **cuspidal spectral
large sieve**.  It is stronger than scalar boundary large sieves because
the coefficients are `A_pi(b,n)`, not `A_pi(1,n)`, and because the
hyperbolic product window correlates the two indices.

Theorem 5.1 rules out deriving (6.2) from an arbitrary-data coefficient
Plancherel contraction.  It does not show that the special support and
factorization in (6.1) violate (6.2).  A proof may still exploit:

```text
* the width-D product window 8*b*n=Q+O(D);
* actual prime-power shell restrictions;
* character--Mellin orthogonality across fan conductors;
* cancellation among the long-Weyl moduli after the exact mask is kept. (6.3)
```

Nor can one additionally call `W4` and `W5` a polar projection.  They are
the geometric short-Weyl pieces in (3.5).  They may be isolated and
estimated, but subtracting them is a signed trace-form manipulation, not
Hilbert-space Pythagoras.

### Final status

```text
arbitrary F(b,n) retained by GL3 Poincare series:       YES;
complete cusp/minimal/maximal spectral side:            YES;
identity/w4/w5/w6 geometric side:                       YES;
generic residual constant term:                        ZERO;
full Eisenstein subtraction is automorphic contraction:YES;
w4,w5 are orthogonal polar projections:                NO;
physical ell2 contraction for arbitrary data:          FALSE, Theorem 5.1;
special QP D^(2+o(1)) cuspidal two-index sieve:         OPEN.             (6.4)
```

---

## 7. Executable certificate

Finite versions of the channel inventory, exact Pythagoras, rank-one
cuspidal alignment, and Satake prime-power energy are implemented in

```text
src/qp_two_index_poincare_polar_gate.py
src/test_qp_two_index_poincare_polar_gate.py
```

Replay with

```text
python3 -m pytest -q src/test_qp_two_index_poincare_polar_gate.py
```

