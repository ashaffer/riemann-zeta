# R128 all-arity proper-conductor cancellation and complete chirp duality

Status: an exact cancellation missed by the conductor-by-conductor estimates
in R116 is proved.  Once **all** residue/conductor classes for one modulus
are recombined before taking an absolute value, their two-dimensional finite
Fourier transform is a complete bilinear-chirp transform.  Consequently the
proper-conductor classes cancel the Ramanujan proper-divisor correction of
the primitive class exactly, modulus by modulus.  The complete class sum is
the ordinary-product dual with no `X^(1/2)` (or other) conductor remainder.

This must not be misread as an estimate for the ordinary dual.  R120's
primitive-only scalar is signed, and one frozen ordinary-dual block remains
signed.  Positivity is recovered only after every gcd sector, fixed-ratio
profile, orientation, and Vaughan component is included; that complete
ordinary-dual family is simply another exact representation of the original
positive R71 energy.  Its coefficients are still

```text
C(n)=(mu*Lambda)(n)=-mu(n)log n,
```

and a fixed-power upper bound for the complete separating family is still
fixed-zero-free-strip strength.  Thus the global proper-conductor comparison
is now exact, but no fixed strip and no failure of all fixed strips is proved.

Date: 2026-08-08.

Predecessors:

* [`R116-SIGNED-JOINT-TYPEII-ATTACK.md`](R116-SIGNED-JOINT-TYPEII-ATTACK.md)
  for the conductor square-root theorem and the primitive Ramanujan
  expansion;
* [`R120-PRIMITIVE-MOBIUS-MELLIN-KERNEL-GATE.md`](R120-PRIMITIVE-MOBIUS-MELLIN-KERNEL-GATE.md)
  for the ordinary-product/Mobius-log dual and its signed Mellin spectrum;
* [`R124-ACTUAL-QH-PRIMITIVE-MELLIN-SIGN-GATE.md`](R124-ACTUAL-QH-PRIMITIVE-MELLIN-SIGN-GATE.md)
  for the previously missing global proper-conductor comparison; and
* [`R123-TRUNCATED-MOBIUS-DILATION-BANK-GATE.md`](R123-TRUNCATED-MOBIUS-DILATION-BANK-GATE.md)
  and
  [`R125-ADJACENT-FILTER-PRIME-PACKET-BRIDGE-GATE.md`](R125-ADJACENT-FILTER-PRIME-PACKET-BRIDGE-GATE.md)
  for the exact cofactor collapse and its scale-replication obstruction.

## 1. Verdict and terminology

For one modulus `c`, let

```text
F_c(a)=sum_(z mod c)^* gamma_c(z)e_c(a inverse(z)),

V_c(a)=sum_(j,theta in Z; j theta=a mod c)
                         W(j/c,theta/c).              (1.1)
```

Here `W` is the fully recombined signed `Q_h` profile.  Smooth fixed-ratio
parameters and the R113 Mellin parameter may be retained; they are suppressed
in (1.1).  Define

```text
J_c^(all)=sum_(a mod c)F_c(a)V_c(a).                  (1.2)
```

The new identity is

```text
J_c^(all)
 =c sum_z^* gamma_c(z)
       sum_(m,nu in Z) What(m,nu)e_c(-m nu z).        (1.3)
```

It is exact for every positive integer `c`, not merely squarefree or
balanced semiprime `c`.  No Weil bound, Cauchy inequality, or arithmetic
cancellation is used.

Here “all” includes the `a=0` fold and hence the `j theta=0` axes.  If one
starts instead with R104's already punctured off-axis bulk, subtract the
same axis terms from both sides of (1.3).  R104 proves those separately
isolated terms polylogarithmic.  Restoring them gives (1.3) exactly; they are
not a proper-conductor remainder.

Call the right side `O_c`, for the **complete ordinary dual**.  This notation
is deliberate.  It is not the same object as an isolated positive energy,
and it is not legitimate to infer that an individual `O_c`, gcd sector, or
fixed-ratio profile is nonnegative.  R120's `P_X` is the leading ordinary
piece extracted from a primitive-only, usually `g=1`, frozen block and has a
signed Mellin multiplier.  In contrast, if (1.3) is applied to every block
of the exact R71 decomposition and those blocks are then restored, their sum

```text
O_full=sum_(all g, profiles, orientations, heads) O_block
```

satisfies

```text
O_full=E_R71>=0.                                     (1.4)
```

The positivity in (1.4) belongs to the **sum**, because it is equal to the
original Gram energy.  It does not contradict R120/R124's sign computations
for a selected primitive profile.

If `J_c^(unit)` denotes the contribution of unit residues `a`, R116 proves
by a Ramanujan expansion that

```text
J_c^(unit)=O_c+R_c^(Ram)                             (1.5)
```

on its balanced-semiprime support, where
`R_c^(Ram)=O(c^(1/2+epsilon))` was estimated by absolute values.  Equations
(1.2)--(1.3) instead imply the exact identity

```text
J_c^(nonunit)=-R_c^(Ram).                            (1.6)
```

For arbitrary `c`, (1.6) remains true if `R_c^(Ram)` is defined as
`J_c^(unit)-O_c`; it then also contains the finitely many Fourier modes whose
second frequency is nonunit modulo `c`.  Thus the correct full ledger is

```text
primitive/unit Ramanujan correction       PRESENT and signed;
all nonprimitive conductor classes         ITS EXACT NEGATIVE;
complete all-class remainder               ZERO;
complete ordinary dual                     ORIGINAL R71 ENERGY;
fixed-power bound for that dual             STILL OPEN.              (1.7)
```

The large balanced-semiprime background is therefore not removed by a new
estimate.  It cancels only after the outer coefficients of every cofactor
arity and the exact Vaughan heads are restored inside `O_full`.  Proving
that cancellation with a fixed power remains the Mobius-log problem.

## 2. Complete bilinear-chirp transform

Use

```text
e_c(x)=exp(2 pi i x/c),

What(m,nu)=double_integral W(sigma,tau)
                 e(-m sigma-nu tau)d sigma d tau.    (2.1)
```

Initially take `W` in `C_c^infinity(R^2)`.  The actual finite-smoothness
spline profile follows by the same smoothing limit used in R104--R120.

### Theorem 2.1 (complete chirp duality)

For every `c>=1` and every unit `z mod c`,

```text
sum_(j,theta in Z) W(j/c,theta/c)
                         e_c(j theta inverse(z))
 =c sum_(m,nu in Z)What(m,nu)e_c(-m nu z).           (2.2)
```

Consequently (1.3) holds for every finitely supported coefficient family
`gamma_c` on the unit group.

### Proof

Write

```text
j=x+cJ,       theta=y+cT,
0<=x,y<c,     J,T in Z.                              (2.3)
```

The chirp is unchanged by `J,T`:

```text
e_c(j theta inverse(z))=e_c(x y inverse(z)).         (2.4)
```

Poisson summation on the translated unit lattice gives

```text
sum_(J,T)W(J+x/c,T+y/c)
 =sum_(m,nu)What(m,nu)e_c(mx+nu y).                  (2.5)
```

The remaining finite Fourier transform is elementary.  Summing first in
`y`,

```text
sum_(x,y mod c)e_c(x y inverse(z)+mx+nu y)
 =c e_c(-m nu z),                                    (2.6)
```

because the `y`-sum imposes `x=-nu z mod c`.  Inserting (2.6) into
(2.3)--(2.5) proves (2.2).  Multiplication by `gamma_c(z)` and summation in
`z` proves (1.3).  QED.

There is no hidden coprimality assumption on `m` or `nu` in this proof.
That is exactly why it is stronger than first restricting to unit `a` and
then expanding a Ramanujan sum.  Nor is squarefreeness of `c` used.
The vanishing `Q_h` marginal is also not used in Theorem 2.1; it remains
essential elsewhere for center annihilation, axis control, and the
zero-faithful detector, but not for this finite Fourier cancellation.

The sign in (2.2) agrees with R116 (5.8): the finite transform in (2.6)
sets `x=-nu z`, leaving `e_c(mx)=e_c(-m nu z)`.  There is one factor `c`,
not `c^2`; the `y`-sum contributes `c` and the `x` residue is then unique.

### Corollary 2.2 (exact all-conductor comparison)

For every finite R105 packet to which (1.1) applies, let `O_c` be its
ordinary dual (1.3).  Then

```text
J_c^(all)-O_c=0.                                     (2.7)
```

After summing the exact gcd sectors, fixed-ratio partition, conjugate
orientations, and Vaughan components, the conductor remainder is still
zero and the sum of the `O_c` is the original packet energy.  If the axes
were removed before forming (1.1), the same statement holds after their
R104 terms are restored.

This corollary is an algebraic comparison, not the upper bound
`O_full<<X^(1-delta)`.

## 3. Why the proper conductors cancel the primitive correction

The identity can be seen directly in the conductor language.  For
squarefree `c`, R116's primitive/unit calculation contains

```text
H_c(m,nu;z)
 =sum_(x mod c)^*e_c(mx)
    c_c(inverse(z)+nu inverse(x)).                    (3.1)
```

Let `c_p` be the prime Ramanujan sum and let

```text
kappa_p(c)=inverse(c/p) mod p.
```

A local calculation, valid also when `p|nu`, gives

```text
H_c(m,nu;z)
 =product_(p|c)
   [p 1_(p does not divide nu)
      e_p(-kappa_p(c)m nu z)-c_p(m)].                 (3.2)
```

Expanding (3.2), and putting `r=c/d`, yields the exact divisor formula

```text
H_c(m,nu;z)
 =sum_(d|c;(d,nu)=1)
    d R_r(m)e_d(-m nu z inverse(r)),                  (3.3)

R_r(m)=product_(p|r)[-c_p(m)].                       (3.4)
```

The `d=c` term, when present, is R116's ordinary dual.  Every `d<c` term
is the proper-divisor correction estimated in R116 (5.9)--(5.10).  Formula
(3.3) is useful for an isolated primitive class, but it is not the end of
the calculation.  The nonunit values of `a` omitted in (3.1) are precisely
the other conductor classes in (1.2).  The complete finite transform
(2.6) proves, without matching the divisor grids one by one, that their
aggregate is the negative of all the `d<c` terms, together with the missing
`(c,nu)>1` part of the `d=c` term.  What remains is exactly (2.2).

This explains why R116's two separately valid estimates did not reveal the
cancellation:

```text
abs(primitive correction)+abs(proper classes)
```

was taken before the two pieces were put back into the same finite Fourier
transform.  On balanced semiprimes both are individually
`O(c^(1/2+epsilon))`; jointly their sum is zero.

The cancellation is more local than an all-arity Mobius cancellation.  It
occurs for each `c`, each coefficient packet, and each smooth profile.  The
outer sign `mu(c)` is not used.

## 4. Passage to the actual R105/R71 object

Three scope points are needed to use Theorem 2.1 in the repository object.

1. **The profile must be complete.**  All signed `Q_h` translates and all
   `theta` shells belonging to a fixed smooth partition member must be
   recombined before (2.2).  Taking an absolute value shell by shell destroys
   the finite chirp transform just as it destroys R116's zero-row identity.
   The `j theta=0` sectors may either be retained in this complete fold or
   removed and restored with R104's exact axis identities; the latter choice
   changes intermediate displays by only the already proved polylogarithmic
   terms.
2. **Product-dependent profiles cause no error.**  Before the product fiber
   is grouped, apply (2.2) separately to every `(d,b)` with its actual smooth
   ratio parameter `x=db/c`.  Equivalently, use R116 Corollary 3.2's
   absolutely summable vector-valued Fourier separation and apply (2.2)
   term by term.  No truncation is needed; truncating at projective error
   `X^-A` is optional.
3. **Common divisors and heads are restored linearly.**  The R105 display
   first fixes `g=(q_1,q_2)` and applies the residue calculation to the
   reduced denominator.  Theorem 2.1 applies for each `g`.  It also applies
   to tail-tail, tail-head, head-tail, and head-head packets separately.
   Adding them coefficientwise invokes

   ```text
   A_(U,V)+three Vaughan heads
     =mu*Lambda=-mu log=C.                            (4.1)
   ```

For the completed `g=1` block, the resulting ordinary dual has the exact
shape recorded in R120,

```text
sum_((c,n)=1) C(c)C(n)c^(-it)n^(-1-it)
                    Phi_lambda(n/c),                 (4.2)
```

with smooth cutoffs and the finite/projective profile family understood.
Other `g` sectors have `C(gc),C(gn)` and their rescaled kernels.  Summing
every such sector gives

```text
O_full
 =sum_(q_1,q_2)C(q_1)C(q_2)
    sum_(m_1,m_2>=1)L(q_1m_1,q_2m_2)

 =integral psi(R)
    abs[sum_q C(q)sum_m f_R(qm)]^2dR
 =E_R71.                                              (4.3)
```

Equation (4.3) is R120 (6.10)--(6.11), now reached through the complete
ordinary dual without an unproved global proper-conductor remainder.

The identity is exact after a smooth approximation.  The compact B-spline
kernel follows by bounded-variation convergence.  If one insists on a
finite projective truncation and the previously evaluated Type-I form, the
only errors are the arbitrarily small projective truncation and the already
recorded Euler defect; there is no conductor error.

## 5. What has and has not become positive

The following distinction is load-bearing:

```text
one frozen Phi_lambda Mellin form                   SIGNED;
one g=1 coprime form sum_d mu(d)|B_d|^2             SIGNED;
R120 primitive-only leading scalar                  SIGNED;
complete ordinary-dual family O_full                POSITIVE,
                                                     because O_full=E_R71.
                                                               (5.1)
```

Thus Theorem 2.1 removes the proposed escape in which a global
proper-conductor remainder of exponent one might cancel the ordinary dual.
There is no such remainder after complete recombination.  It does **not**
make R124's individual multiplier `lambda_P(tau)` nonnegative.  Its negative
bands are repaired by other gcd/profile/head members of `O_full`, not by a
pointwise sign change in that one member.

In particular, R124 Lemma 6.1 no longer needs a hypothetical estimate

```text
R_rho(X)<<X^theta
```

for the conductor remainder: at the exact all-class level that remainder is
zero.  If a modulation isolates a zero `rho=beta+i gamma`, the complete
ordinary dual has the same positive response as the original detector,

```text
O_(full,rho)(X)
 =A_rho X^(2beta-1)(1+o(1)),       A_rho>0,           (5.2)
```

subject to the same nondegenerate localization hypotheses already recorded
in R102/R120.  What remains missing is an upper bound for the left side.

## 6. Why all cofactor arities do not make the ordinary dual small

The coefficient identity behind exact Vaughan recompletion is

```text
C=mu*Lambda=-mu log,          C*1=Lambda.             (6.1)
```

Put `A(s)=1/zeta(s)`.  Then

```text
sum_n C(n)n^(-s)=A'(s)=-zeta'(s)/zeta(s)^2,

zeta(s)A'(s)=-zeta'(s)/zeta(s)
             =sum_n Lambda(n)n^(-s).                 (6.2)
```

This is the exact all-cofactor-arity cancellation.  It reduces the pole of
`A'` at a zero of multiplicity `j` from order `j+1` to the simple logarithmic
derivative pole, but it does not remove the zero.  The correction

```text
[zeta(s)-1]A'(s)                                     (6.3)
```

has the same order-`j+1` pole as `-A'(s)`.  Hence treating the free-cofactor
or all-arity completion as a power-small perturbation is analytically false
unless the corresponding zero-free information has already been proved.

This also explains R123--R125.  The truncated-Mobius filter collapses the
free cofactor and exposes `C`; the adjacent filter moves the same `C` field
to a smaller scale.  Neither operation changes the singularity in (6.2).

For comparison, if `r>1` is a fixed squarefree omitted factor, then for
`(d,r)=1`

```text
C(rd)=mu(r)C(d)+C(r)mu(d).                           (6.4)
```

With

```text
A_r(s)=sum_((d,r)=1)mu(d)d^(-s)
      =1/zeta(s) product_(p|r)(1-p^(-s))^(-1),       (6.5)
```

the fixed-`r` coefficient series is

```text
sum_((d,r)=1) C(rd)/r d^(-s)
 =mu(r)/r A_r'(s)+C(r)/r A_r(s).                     (6.6)
```

At every zeta zero of multiplicity `j`, (6.6) has a pole of order `j+1`;
the derivative term cannot be canceled by the second term.  Thus a strategy
which separates omitted-factor sectors and asks for a fixed-power smooth
bound in any one of them has simply returned to the fixed-strip problem.
The complete chirp identity avoids estimating these sectors separately; it
does not estimate the surviving ordinary dual.

For a precise smooth-sum gate, let `w` be compactly supported in
`(0,infinity)` and put

```text
S_(r,w)(Y)=sum_((d,r)=1) C(rd)/r w(d/Y),
What_w(s)=integral_0^infinity w(x)x^(s-1)dx.          (6.7)
```

Mellin inversion in the scale gives exactly

```text
integral_0^infinity S_(r,w)(Y)Y^(-s)dY/Y
 =What_w(s)[mu(r)/r A_r'(s)+C(r)/r A_r(s)].          (6.8)
```

If `S_(r,w)(Y)<<Y^theta` for a bank whose Mellin transforms have no common
zero, the right side continues holomorphically through `Re(s)>theta`.
Equation (6.6) then excludes zeta zeros there.  This is an exact
coefficient-level reason that signed all-arity estimates cannot be imported
as a cheap lemma.

## 7. Fail-fast test of an asymmetric ratio tilt

A natural last attempt is to multiply one orientation of the ordinary dual
by the ratio

```text
x=n/c
```

so that its logarithmic measure `dx/x` becomes `dx`.  Since R120 proved

```text
Phi(x+1)=Phi(x),             integral_0^1 Phi(x)dx=0, (7.1)
```

one might choose a ratio shell consisting of complete additive periods and
hope to delete the low mode while retaining the zero carrier.

There are three exact obstructions.

### 7.1 The tilt creates only a Mellin notch

On a union `I` of complete unit periods, the tilted response is

```text
kappa_arrow(tau)=integral_I Phi(x)x^(-i tau)dx,

kappa_arrow(0)=0.                                    (7.2)
```

But, generically,

```text
kappa_arrow(tau)
 =-i tau integral_I Phi(x)log(x)dx+O(tau^2).          (7.3)
```

Thus (7.1) creates one zero, not a spectral gap or a fixed-power factor.
In the equal-modulation Mellin diagonalization used in R120, after a zeta
zero is moved to the center frequency its positive diagonal energy is
precisely the `tau=0` carrier.  If (7.2) is imposed on both sides of a
Hermitian detector, that carrier is killed along with the background.
If the reverse orientation is left nonzero so that the carrier survives,
the complete-period cancellation is no longer present in the Hermitian
sum.

An off-diagonal cross detector can move the carrier to `tau!=0`, but its
quadratic form is signed.  Bounding a cross term gives no upper bound for
either positive diagonal; polarization supplies
`2|<A,B>|<=||A||^2+||B||^2` only in the wrong direction.  Restoring the
diagonals restores the unnotched complete ordinary dual.

### 7.2 Additive mean zero removes only the uniform residue component

Write the Fourier series

```text
Phi(x)=sum_(k!=0)A_k e(kx).                           (7.4)
```

Even before a tilt,

```text
1/c sum_(n mod c)Phi(n/c)=sum_(ell!=0)A_(ell c),     (7.5)
```

which is rapidly small but not identically zero unless `Phi` is
band-limited.  More importantly, the actual ordinary dual contains `C(n)`,
not a uniform residue measure:

```text
sum_n C(n)/n Phi(n/c)
 =sum_(k!=0)A_k sum_n C(n)/n e(kn/c).                 (7.6)
```

Equation (7.1) deletes only `k=0`.  Every arithmetic twisted Mobius-log sum
in (7.6) remains.  Partial summation or writing `Phi=Psi'` merely transfers
the derivative to a weighted Mertens sum.

### 7.3 Complete chirp duality is stable under the tilt

Replacing `W` by an asymmetric or cross profile changes `What` and hence
`Phi`, but Theorem 2.1 still applies verbatim.  Proper conductors neither
destroy nor rescue the tilted notch: they again recombine exactly into the
new ordinary dual.  Therefore the tilt is a change of detector gauge, not a
new conductor cancellation.  It offers the forced choice

```text
exact additive-period notch     => centered positive zero carrier killed;
zero-faithful Hermitian family  => nonzero Mellin mode and Mobius endpoint.
                                                               (7.7)
```

The asymmetric-period idea therefore fails fast.

## 8. The remaining theorem

The conductor problem is no longer the missing step.  For a complete
separating modulation/dilation bank, Theorem 2.1 and R102's nonvanishing
zero multiplier reduce the desired statement to

```text
O_full(X)<<X^(1-delta).                              (8.1)
```

If (8.1) holds, a zero `rho=beta+i gamma` contributes the positive response
(5.2), so

```text
2beta-1<=1-delta,
beta<=1-delta/2.                                     (8.2)
```

This is a fixed zero-free strip.  Conversely, the smooth Mobius-log
polynomials in (4.2), (6.2), and R120 show why known Vinogradov--Korobov
information gives only a subpower improvement rather than (8.1).

The exact final ledger is

```text
complete finite chirp transform                    PROVED;
primitive Ramanujan correction                     EXACTLY CANCELED;
all proper conductor classes                       EXACTLY RECOMBINED;
global conductor remainder                         ZERO ALGEBRAICALLY;
complete ordinary dual                             ORIGINAL POSITIVE ENERGY;
asymmetric complete-period tilt                    NOT ZERO-FAITHFUL / SIGNED;
fixed-power ordinary-dual bound                    OPEN;
fixed strip or no-strip conclusion                 NOT PROVED.        (8.3)
```

The next valid attack should work directly on the complete ordinary-dual
family (4.2)--(4.3), preserving its cross-profile/gcd positivity before any
Cauchy step.  Further conductor-by-conductor estimates can no longer improve
the comparison: the exact comparison is already equality.
