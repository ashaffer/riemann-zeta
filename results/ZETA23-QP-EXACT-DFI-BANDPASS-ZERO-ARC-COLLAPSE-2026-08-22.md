# QP exact DFI band-pass: collapse to the zero Farey arc

**Date:** 2026-08-22  
**Verdict:** in the balanced worst block of the smooth completed **interior
stationary HSM kernel**, the exact signed shift sum makes every DFI term with
a nonzero primitive Farey numerator rapidly decaying.  This holds before the
row and colour Poisson transforms, uniformly in the delta modulus and
without a coprimality assumption involving `R*S`.  Consequently the frozen
coprime top-block form of size `q^(109/33+o(1))` is a valid positive auxiliary
form, but it is not a mass-bearing sector of the exact signed HSM expression.

Only the modulus-one, zero-numerator term survives.  By the exact delta
identity, that term is an archimedean approximate identity which reproduces
the original centered HSM form up to a rapidly decaying error.  Bounding it
at diagonal strength is therefore equivalent to the missing HSM theorem;
this audit gives no new four-cycle exponent.

The argument covers the exact completed interior term only.  It does not
bound the stationary boundary, nonstationary B-process terms, or restore the
original prime-power masks.

## 1. Scales and the exact delta weight

Use the balanced notation

```text
D=q^(16/33),       C=q/sqrt(D)=q^(25/33),
L=q/D=q^(17/33),   X=q^(84/33),
B0=X/(R*S)=q^(34/33),
B0/C=C/D=q^(9/33).                                  (1.1)
```

Let `w` be the fixed smooth function supported in `(1/2,1)` in the
Heath--Brown/DFI delta symbol.  With a harmless normalization convention,
its two-variable weight is

```text
h_DFI(x,y)=sum_(m>=1) 1/(x*m)
              *[w(x*m)-w(|y|/(x*m))].              (1.2)
```

Thus, for a delta modulus `c` and mismatch `n`, one has the exact expansion

```text
C^(-2)*h_DFI(c/C,n/C^2)
 =sum_(m>=1) 1/(c*C*m)
   *[w(c*m/C)-w(|n|/(c*C*m))].                     (1.3)
```

This is the standard formula behind the facts that `h_DFI(x,y)` is
independent of `y` for `|y|<=x/2` and is `O(x^(-1))`; see
[Heath-Brown, Lemma 4](https://ora.ox.ac.uk/objects/uuid%3Abbd3c62f-f010-44b5-8be5-87e903fb0084).

Formula (1.3), rather than a Mellin majorant, is the useful exact separation
here.

## 2. Put the signed shift back before Poisson

Write the completed multiplication coefficient as `d(x)`.  Insert a shift
variable `r` into the HSM correlation by

```text
1_(x-y=r)=1_(n=0),              n=x-y-r.            (2.1)
```

One may multiply the delta identity by a smooth cutoff
`eta(n/B0)` which equals one at zero.  On the support of the delta this does
not alter the expression.  Off the delta it supplies the usual harmless
mismatch truncation.

The exact interior stationary kernel is

```text
K_L(x,x-r)=sum_(ell~L) omega(ell/L)
 e(Phi_(ell,x)(r)),                                  (2.2)

Phi_(ell,x)(r)
 =3*(T/(R*S))^(1/3)*ell^(1/3)
     *(x^(1/3)-(x-r)^(1/3)).                         (2.3)
```

On the smooth shell `x,x-r~X`, its shift frequency satisfies

```text
partial_r Phi_(ell,x)(r) asymp 1/B0,
partial_r^j Phi_(ell,x)(r)
 <<1/(B0*X^(j-1)),             j>=2.                (2.4)
```

Smooth stationary amplitudes obey the same or better derivative bounds.
This is the precise sense in which `K_L/L` is a band-pass kernel on the
scale `B0`.

After inserting the delta symbol, a primitive numerator `a mod c` produces

```text
e_c(a*(x-y-r)).                                      (2.5)
```

For fixed `x,y,c,a,m`, sum in `r` **before** performing either physical
Poisson transform.

The `r=0` term must be retained in this summation.  If the product diagonal
has already been extracted, restore `r=0`, apply the argument below, and
then subtract its known contribution
`O(L*q^o(1)*||d||_2^2)`.  Deleting `r=0` before summation would leave a
point mass whose Fourier transform is flat and would falsely resurrect the
Ramanujan major axis.

## 3. Nonzero-numerator lemma

Let `c>1` and `(a,c)=1`.  Replace `a/c` by its signed representative modulo
one.  Then

```text
||a/c||>=1/c.                                       (3.1)
```

The first term in the bracket (1.3) is multiplied by
`eta((x-y-r)/B0)` and hence varies in `r` on scale `B0`.  Since every
nonzero DFI modulus allowed by the first term has `c<<C`, (1.1) gives

```text
B0/c >> B0/C=q^(9/33).                              (3.2)
```

By (2.4), the intrinsic band-pass frequency is too small to cancel the
Farey frequency:

```text
dist(partial_r Phi_(ell,x)-a/c,Z)>=1/(2*c)           (3.3)
```

for all sufficiently large `q`.

The second term in (1.3) is supported where

```text
|x-y-r| asymp c*C*m.                                (3.4)
```

Its smooth `r`-scale is `c*C*m`; against `e_c(-a*r)` the number of
oscillations is at least

```text
(c*C*m)/c=C*m>>q^(25/33).                           (3.5)
```

If the mismatch cutoff is shorter, its scale is `B0`, and (3.2) applies
instead.  Poisson summation in `r`, followed by repeated integration by
parts in every nonstationary integral, therefore gives, for every `A>0`,

```text
sum_(r in Z) K_L(x,x-r)*eta((x-y-r)/B0)
 e_c(-a*r)*w(c*m/C)
       <<_A L*q^(-A),                               (3.6)

sum_(r in Z) K_L(x,x-r)*eta((x-y-r)/B0)
 e_c(-a*r)*w(|x-y-r|/(c*C*m))
       <<_A L*q^(-A).                               (3.7)
```

The bounds are uniform in `x,y,c,a,m` on the completed shells.  Summing the
coefficients `1/(c*C*m)`, all allowed `m`, the `O(C)` possible moduli, the
`O(c)` numerators, and the polynomially many data variables still leaves
`O_A(q^(-A))` after increasing the integration-by-parts order.

This proves the exact sector statement

```text
all DFI terms with c>1 and (a,c)=1: RAPIDLY DECAYING. (3.8)
```

No condition `(c,R*S)=1` occurs in the proof.

## 4. What happens to the four advertised complements

The order of operations resolves them as follows.

1. **Mismatch-dependent DFI weight.**  Formula (1.3) treats it exactly.
   The frozen part is killed on the longer scale `B0`; every nonfrozen bump
   is killed on its natural scale `c*C*m`.
2. **Lower modulus blocks.**  They do not require a scaled two-dimensional
   support lemma.  For every `c>1`, their primitive numerator is already
   nonstationary in the signed shift variable.
3. **Noncoprime `(c,R*S)>1`.**  Conductor lowering never appears, because
   the shift sum is completed before the row/colour Poisson transforms.
4. **Ramanujan and Kloosterman axes.**  These axes arise only after those
   transforms.  In the exact signed expression their total contribution is
   part of the cancellation (3.8); separating them and taking absolute
   values destroys that cancellation.  If the product diagonal is treated
   separately, the restored-and-subtracted `r=0` term costs only its already
   admissible diagonal norm.

In particular, the earlier frozen top-block estimate

```text
q^(109/33+o(1))
```

is not false.  It bounds a form obtained after discarding the signed shift
cancellation.  It cannot be interpolated into an estimate for the exact HSM
moment.

## 5. The surviving zero arc is the original gate

For `c=1`, the unique primitive residue is `a=0`.  There is then no Farey
oscillation and neither (3.2) nor (3.5) gives cancellation.  By the exact
delta identity and (3.8), the modulus-one term satisfies

```text
(c=1,a=0 DFI term)
  =(original completed centered HSM form)+O_A(q^(-A))*||d||_2^2. (5.1)
```

Equivalently, the `c=1` DFI kernel is an archimedean approximate identity
on the low shift-frequency band occupied by `K_L`.  Proving that (5.1) has
operator norm `O(L*q^o(1))` is the centered HSM theorem itself.  The delta
method has not diagonalized it; it has merely placed the whole difficult
operator in its zero Farey arc.

## 6. Consequence and scope

```text
exact DFI-weight decomposition:                    PROVED;
all nonzero Farey numerators in completed HSM:     RAPIDLY DECAYING;
lower and noncoprime modulus sectors:              INCLUDED IN THAT PROOF;
separate Ramanujan-axis estimate needed:           NO (if signs retained);
surviving c=1 zero-arc HSM estimate:                OPEN;
stationary boundary/nonstationary completion:      OPEN;
uniform primal dyadic moment improvement:          NONE;
new slope-block or four-cycle exponent:            NONE.
```

The useful conclusion is methodological: a DFI/Kuznetsov attack must not
expect its saving from top-modulus Kloosterman cancellation.  At the QP
band-pass scales, the exact signed shift sum annihilates that entire sector;
any genuine progress must estimate the zero arc directly or use a
decomposition which does not collapse the centered HSM operator into it.

## Appendix: the larger positive frozen sector

There is also a rigorous extension of the earlier top-block calculation,
although (3.8) shows why it does not measure the exact signed form.  Put

```text
c~M=t*C,                 V=t*sqrt(D).               (A.1)
```

For `t>=D^(-delta)` with `delta<1`, the mismatch range
`|n|<=B0` has `|n|/C^2<=D^(-1)<<t`; hence Lemma 4 makes the DFI weight
exactly mismatch-independent on these blocks (apart from the inserted
smooth mismatch cutoff).

For `(c,R*S)=1`, the support-energy lemma at this scale gives

```text
sum_(c~M) n_c*m_c <<t*D*q^o(1),                    (A.2)
```

and fixed-`c` numerator Parseval remains valid because
`V^2<<M`.  With the exact delta normalization, the corresponding positive
frozen block is therefore

```text
E(M)<<X^2*D/(C^2*M)*q^o(1).                        (A.3)
```

Relative to the correlation scale `D*X`, its loss is

```text
E(M)/(D*X)<<X/(C^2*M)
 =D^(9/16)*t^(-1)*q^o(1).                          (A.4)
```

Hence the union of coprime frozen blocks

```text
C*D^(-delta)<=c<=C,       delta<1/16,              (A.5)
```

has the honest auxiliary loss

```text
beta=9/16+delta<5/8.                                (A.6)
```

This is a larger positive-form theorem, not a four-cycle improvement.  In
the exact HSM expression those blocks are already rapidly decaying by
(3.8), while the surviving zero arc is not controlled by (A.3).
