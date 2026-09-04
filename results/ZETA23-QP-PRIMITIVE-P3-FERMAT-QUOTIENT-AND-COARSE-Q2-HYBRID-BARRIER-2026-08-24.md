# QP broad gate: primitive `p^3` Fermat quotients and the coarse-`p^2` hybrid barrier

**Date:** 2026-08-24  
**Verdict:** no currently proved Postnikov, Heilbronn, additive-energy, or
classical Burgess estimate supplies the required `p^(-2/33)` saving for the
actual prime-power shell.  In fact the often-quoted formal `p^(-1/48)`
Burgess saving is not licensed for the cubefull modulus `p^3`: arbitrary
Burgess moment `r` is available for cubefree moduli, whereas a general
primitive character modulo `p^3` is covered classically only for `r<=3`.
At length `p`, `r=3` is exactly trivial.

The proposed coarse-archimedean cutoff does give an exact character
expansion modulo `p^2`.  It does not automatically give the apparent
`p^(-1/8)` gain.  The cutoff has Mellin bandwidth `|t|~p`; after squaring,
the common-carrier kernel is

```text
K_u(eta)=sum_(b in shell) eta(b)b^(iu),       u=t-s.       (0.1)
```

An order-one proportion of the Mellin mass has `|u|~p`, whose analytic
conductor is `p^2(1+|u|)~p^3`.  Moreover the principal character reconstructs
the nonseparable coarse reciprocal mask, not a rank-one constant.  Thus the
coarse decomposition relocates the same hybrid/tangent restriction gate.

The precise new input which would close this scalar route is a
prime-supported, coefficient-sensitive hybrid square-function estimate at
least as strong as a `p^(-2/33)` saving after the coarse principal/tangent
projection.  No cited theorem proves it.

---

## 1. Exact primitive-character coordinate and conductor strata

Let `p` be an odd prime.  Every unit modulo `p^3` has a unique decomposition

```text
n=omega(n)<n>,
omega(n)^(p-1)=1,                 <n> in 1+p Z/p^3 Z.       (1.1)
```

Put

```text
ell(<n>)=log(<n>)/p mod p^2.                              (1.2)
```

Characters are parametrized by

```text
chi_(alpha,beta)(n)
 =theta(omega(n))^alpha e_(p^2)(beta ell(<n>)),
alpha mod p-1,                       beta mod p^2.          (1.3)
```

Here `theta` is a fixed generator of the character group of the Teichmueller
factor.  The conductor is exactly `p^3` iff `p` does not divide `beta`.

For `1<=n<p`, define

```text
Q_2(n)=(n^(p-1)-1)/p mod p^2.                             (1.4)
```

Taking the truncated logarithm of `n^(p-1)` gives the exact identity

```text
ell(<n>)
 =(p-1)^(-1)(Q_2(n)-p Q_2(n)^2/2) mod p^2.                (1.5)
```

Thus a primitive shell character is a corrected **second Fermat quotient**
phase modulo `p^2`, with a tame twist.

Now fix a primitive `chi=(alpha,beta)` and let `psi=(alpha',beta')` range
over primitive characters.  The ratio `bar(chi)psi` has conductor

```text
p^3  if beta'-beta is a unit mod p,
p^2  if beta'-beta is a nonzero multiple of p mod p^2,
p    if beta'=beta and alpha'!=alpha,
1    if psi=chi.                                          (1.6)
```

The exact numbers of partners are

```text
conductor p^3:   p(p-2)(p-1),
conductor p^2:   (p-1)^2,
conductor p:     p-2,
principal:       1.                                      (1.7)
```

They sum to `p(p-1)^2`, the number of primitive characters modulo `p^3`.
In particular a proportion `(p-2)/(p-1)=1-O(1/p)` of all ratio pairs remain
at conductor `p^3`.

On the conductor-`p^2` stratum, write `beta'-beta=p gamma`.  Reducing (1.5)
modulo `p` gives

```text
e_(p^2)(p gamma ell(<n>))
 =e_p(gamma (p-1)^(-1) q_p(n)),                           (1.8)
```

where `q_p` is the ordinary first Fermat quotient.  Classical first-quotient
technology therefore reaches only the `O(1/p)` conductor-lowered ratio
stratum, and still carries an arbitrary tame twist.  The generic stratum is
the second-quotient problem (1.5).

---

## 2. Exact off-diagonal restriction and the needed exponent

The fixed-modulus two-star identity in the companion report is

```text
sum_b d_b^2
 =Phi^(-2) sum_(chi,psi) F_chi conjugate(F_psi)
                         K(conjugate(chi)psi),
Phi=phi(p^3),
K(eta)=sum_(b in S_p)eta(b).                              (2.1)
```

The remaining broad face needs the factor

```text
D^(-1/8)=p^(-2/33),                 D=p^(16/33).           (2.2)
```

Consequently the scalar pointwise route would need, uniformly on the
relevant nonprincipal ratios,

```text
|K(eta)| <= p^(31/33+o(1)).                               (2.3)
```

Prime powers of exponent at least two contribute only `p^(1/2+o(1))` in a
shell of scale `p`; they are below (2.3).  The hard part is the sum over
actual primes.

### Formal Burgess arithmetic

If one formally inserts modulus `p^k`, interval length `p`, and moment `r`
into the usual Burgess expression, the saving is

```text
delta_k(r)=1/r-k(r+1)/(4r^2).                             (2.4)
```

For `k=3`,

```text
delta_3(r)=(r-3)/(4r^2),
max_r delta_3(r)=delta_3(6)=1/48.                         (2.5)
```

Even this optimistic formal value misses the target by

```text
2/33-1/48=7/176,                                         (2.6)
```

equivalently `21/256` in `D`-exponents.

### The cubefull correction

The arbitrary-`r` Burgess theorem applies to cubefree moduli.  For general
moduli the classical theorem supplies the displayed bound only for `r<=3`.
This restriction is stated explicitly in Heath-Brown's
[*Burgess's Bounds for Character Sums*](https://arxiv.org/abs/1203.5219)
and in Kerr's
[*Moments of character sums to composite modulus*](https://arxiv.org/abs/1904.04578).
Since `p^3` is cubefull, (2.5) is not a theorem.  The best licensed classical
choice at length `p` is

```text
delta_3(3)=0.                                             (2.7)
```

Kerr's 2019 improvement has the cubefull-part form

```text
N^(1-1/r) q^((r+1)/(4r^2)+o(1))
c^((r-1)/(4r^2)-1/(32r^3)).                              (2.8)
```

For `q=c=p^3` and `N=p`, its exponent in `p` is

```text
1+1/(2r)-3/(32r^3)>1.                                    (2.9)
```

It is therefore also trivial in this range.

---

## 3. What Postnikov and Heilbronn estimates do—and do not—give

Banks and Shparlinski's Postnikov--Korobov theorem
[*Bounds on short character sums and L-functions for characters with a
smooth modulus*](https://arxiv.org/abs/1605.07553) assumes that the maximum
prime-adic exponent `gamma` of the modulus satisfies `gamma>=gamma_0`, and
that the interval length is at least `p^(gamma_0)`.  Their proof explicitly
takes `gamma_0>=e^200`.  The fixed-depth pair

```text
modulus p^3,                    length p                         (3.1)
```

satisfies neither hypothesis.  Powerful-modulus improvements designed for a
fixed small base prime and a growing exponent do not apply when the exponent
is `3` and the base prime grows.

For the first Fermat quotient, Heath-Brown's individual estimate quoted in
Shparlinski's
[*Fermat quotients: Exponential sums, value set and primitive
roots*](https://arxiv.org/abs/1104.3909) is

```text
sum_(M<n<=M+N)e_p(a q_p(n))
 <<N^(1/2)p^(3/8),                                      (3.2)
```

which gives `p^(7/8)` at `N=p`.  This is a first-quotient, conductor-`p^2`,
unweighted-integer statement.  Shparlinski's paper gives stronger results
only on average over the varying prime `p`; it also notes that no individual
bound for the corresponding prime-indexed exponential sums was known.

Shkredov proves

```text
sum_(n=1)^p e_(p^2)(a n^p)
 <<p^(59/68)log(p)^(5/34)                                (3.3)
```

in [*On Heilbronn's exponential sum*](https://arxiv.org/abs/1208.6124).
The phase in (3.3) is the additive Fourier transform of the Heilbronn
subgroup.  It is not an arbitrary primitive Dirichlet character on a shell,
not prime-supported, and not the corrected second-quotient phase (1.5).
Thus the attractive exponent `59/68` cannot be inserted into (2.1).

No primary theorem located in this audit supplies an individual estimate of
the form (2.3) for prime-supported primitive characters modulo `p^3`.

---

## 4. Why ordinary additive energy is not enough

Full character orthogonality already gives a strong fourth moment.  If
`S_p` is a shell of prime powers below `p`, then products of two shell nodes
are below `p^2`.  Hence

```text
b1 b2 == b3 b4 (mod p^3)
       iff
b1 b2 = b3 b4.                                           (4.1)
```

Unique factorization gives

```text
Phi^(-1)sum_(chi mod p^3)|K(chi)|^4
 <<|S_p|^2 p^o(1).                                       (4.2)
```

This moment is already part of the proved character package; it does not
control the coefficient-sensitive off-diagonal form (2.1).

Even a conjecturally diagonal second-quotient additive energy is not a
pointwise solution.  For fixed tame coordinate define

```text
G_beta=sum_(b in S_p)theta(b)^alpha
       e_(p^2)(beta ell(<b>)).                            (4.3)
```

Wild Parseval gives exactly

```text
sum_(beta mod p^2)|G_beta|^4=p^2 E_alpha,                 (4.4)
```

where `E_alpha` is the corresponding signed additive energy of the values
`ell(<b>)`.  Even the ideal estimate `E_alpha<<|S_p|^2p^o(1)` implies only

```text
max_beta |G_beta|
 <=(p^2 E_alpha)^(1/4)
 <<(p|S_p|)^(1/2)p^o(1)=p^(1+o(1)),                      (4.5)
```

because `|S_p|=p^(1+o(1))`.  A fourth-energy theorem alone therefore gives
no pointwise power saving.  One needs a higher-moment large-spectrum theorem
or, more naturally for (2.1), a coefficient-sensitive restriction estimate.

---

## 5. Exact coarse-`p^2` detector

Let

```text
H=pD=o(p^2),
rho=8abc-p^3.                                             (5.1)
```

Choose `W` smooth, supported in `(-1/3,1/3)`, and identically one on
`[-1/4,1/4]`.  Let `I_H` be the unit residue classes modulo `p^2` represented
by integers `r` with `|r|<=H`.  For all sufficiently large `p`, the following
identity is exact:

```text
1_(|rho|<=H)
 =W(rho/p^2) 1_(8abc mod p^2 in I_H).                     (5.2)
```

Indeed the forward implication is immediate.  Conversely the right side
gives `rho=r+k p^2`, with `|rho|<p^2/3` and `|r|<p^2/4`; hence `k=0`.

Multiplicative character orthogonality modulo `p^2` turns (5.2) into

```text
1_(|rho|<=H)
 =W(rho/p^2)/phi(p^2)
   sum_(chi mod p^2) chi(8abc) conjugate(R_H(chi)),
R_H(chi)=sum_(r in I_H)chi(r).                            (5.3)
```

Thus conductor lowering is algebraically exact.  The loss occurs in
separating the archimedean factor.

---

## 6. Mellin bandwidth conservation

Put

```text
w_p(y)=W(p(y-1)),
M_p(t)=integral_0^infty w_p(y)y^(-it)dy/y.                (6.1)
```

Mellin inversion gives

```text
W((x-p^3)/p^2)
 =(2pi)^(-1) integral_R M_p(t)(x/p^3)^(it)dt.             (6.2)
```

After `u=p(y-1)`, for bounded `tau`,

```text
M_p(p tau)
 =p^(-1) integral W(u)(1+u/p)^(-1-ip tau)du
 =p^(-1) W_hat(tau)+O_W(p^(-2)).                          (6.3)
```

Therefore `M_p` has height `asymp p^(-1)` and bandwidth `asymp p`.  For
some fixed interval `J` disjoint from zero,

```text
integral_(pJ)|M_p(t)|dt >>_W 1.                           (6.4)
```

Inserting (6.2) into (5.3) separates the three shell variables:

```text
chi(8abc)(8abc/p^3)^(it)
 =constant_(chi,t)
  [chi(a)a^(it)][chi(b)b^(it)][chi(c)c^(it)].             (6.5)
```

If the other two shell transforms and the residual transform are absorbed
into `F_chi(t)`, the common-carrier count has the exact form

```text
d_b=1/(2pi phi(p^2))
    sum_chi integral M_p(t)F_chi(t)
             conjugate(chi(b))b^(it)dt.                  (6.6)
```

Squaring and summing over the physical shell gives

```text
sum_b |d_b|^2
 =1/((2pi)^2 phi(p^2)^2)
  sum_(chi,psi) integral integral
   M_p(t)conjugate(M_p(s))F_chi(t)conjugate(F_psi(s))
   K_(t-s)(conjugate(chi)psi) dt ds,                     (6.7)

K_u(eta)=sum_(b in S_p)eta(b)b^(iu).                     (6.8)
```

Equation (6.7) is the exact obstruction to inserting the untwisted
modulo-`p^2` Burgess saving `1/8`.

* The strip `|t-s|=O(1)` occupies only `O(1/p)` of the natural absolute
  Mellin pair mass.
* An order-one portion has `|t-s|asymp p` by (6.4).
* On that portion the Dirichlet polynomial (6.8) has local analytic
  conductor `p^2(1+|t-s|)asymp p^3`.

Using absolute values therefore returns a `p^3`-scale hybrid problem.  A
square-function in `(t,s)` could in principle do better, but that is a new
coefficient-sensitive theorem, not a consequence of ordinary modulo-`p^2`
Burgess.

There is a second, independent obstruction.  The principal character in
(5.3) contributes

```text
(H/p^2) T_coarse(b,c),
T_coarse(b,c)=sum_a W((8abc-p^3)/p^2).                    (6.9)
```

The matrix `T_coarse` is a reciprocal-rounding mask: for fixed `(b,c)` its
`a`-window has length `asymp 1`.  It is not the all-ones rank-one operator.
Only its zero Mellin frequency is constant.  Projecting away the global
constant vector does not delete the nonzero frequencies which reconstruct
the tangent/Farey-fan geometry.

For comparison, even an optimistic implementation which Taylor-expands
`t log n` on short blocks and invokes a mixed Burgess/VMVT estimate does not
reach (2.2) with currently available ledgers.  A degree-`d` expansion at
`|t|asymp p` is valid on blocks of length at most `p^(d/(d+1))`.  The best
small-degree formal savings are

```text
d=2:  p^(-1/105),
d=3:  p^(-1/72),                                          (6.10)
```

both far smaller than `p^(-2/33)`.  These figures are optimistic because a
mixed theorem retaining the prime-power shell and all coefficient masks is
still required.

---

## 7. Binary conclusion and exact missing lemma

```text
primitive p^3 shell = corrected second Fermat phase:      PROVED;
generic ratio remains conductor p^3:                      PROVED;
formal arbitrary-r p^3 Burgess saving 1/48:               ARITHMETIC ONLY;
classical theorem licenses that r=6 at p^3:               FALSE;
licensed classical saving at length p:                    ZERO;
Postnikov high-power theorem applies at exponent 3:       FALSE;
first-level Heilbronn bound applies to generic ratios:    FALSE;
ordinary fourth-energy closes the off-diagonal:           FALSE;
coarse p^2 detector is exact:                              PROVED;
coarse Mellin bandwidth is p:                             PROVED;
coarse p^2 route automatically gives saving 1/8:          FALSE;
uniform p^(-2/33) prime-shell restriction:                OPEN.
```

A sufficient replacement is a tangent-projected, mask-sensitive version of

```text
integral integral M_p(t)conjugate(M_p(s))
  F_chi(t)conjugate(F_psi(s))
  K_(t-s)(conjugate(chi)psi) dt ds

 <<p^(-2/33+o(1)) times the natural diagonal norm,         (7.1)
```

uniformly for the QP coefficient family, after removing the full
data-dependent principal/coarse packet.  A merely pointwise alternative
would be

```text
sup_(eta nonprincipal, |u|<<p)
 |sum_(b in actual prime-power shell)eta(b)b^(iu)|
 <=p^(31/33+o(1)),                                       (7.2)
```

but (7.2) is stronger than necessary and is not supplied by the cited
literature.

Executable rational-ledger and finite detector checks:

```bash
PYTHONPATH=src pytest -q \
  src/test_qp_p3_fermat_quotient_barrier.py \
  src/test_qp_fixed_defect_graph_cycles.py
```

