# Tiny-delta Bergman mollifier and spectral-principal-mode audit

Status: focused uniform-strip attempt, 2026-08-12.  This note optimizes the
Bergman/Mobius-mollifier construction at `beta_0=1-delta`, makes one completely
explicit tiny choice of `delta`, and audits the exact reciprocal-hyperbola form
against unconditional Kloosterman, Kuznetsov, large-sieve, and exponent-pair
inputs.  All estimates below are required uniformly on every dyadic height
interval; no zero-density inference is used.

The exponent optimization succeeds.  A fixed spectral saving would easily
dominate the `O(delta)` super-conductor excess.  It nevertheless does not prove
the strip, because every applicable spectral estimate omits a degenerate
frequency.  In the present form that frequency is an unsmoothed principal
Mobius mode.  It must supply a negative main term which cancels a growing
diagonal.  Bounding it with a fixed power is already a fixed-strip Mertens (or
reciprocal-zeta) theorem.

```text
explicit candidate strip                         Re(s) < 1-10^(-6)
infimum deleted-diagonal power threshold         theta =1+2 delta+O(delta^2)
explicit power-saved implementation              theta > 1+2 delta+O(delta^2)
explicit mollifier length                        X=T^(1+3*10^(-6))
polynomial-product diagonal                      T^(-0.999992*10^(-6)+o(1))
Euler--Maclaurin completion                      o(1)
hypothetical fixed spectral saving               beats the O(delta) excess
actual conductor-block diagonal                  >>T^(2.000002*10^(-6))/log T
missing term                                     principal short-interval Mobius mode
known spectral estimates                         do not estimate that mode
uniform zero-free strip                          NOT PROVED
```

## 1. Symbolic optimization of the Bergman detector

Fix `delta>0`, choose a disc radius

```text
r=eta*delta,             lambda=delta+r=(1+eta)delta,                 (1.1)
```

and put

```text
sigma_-=1-lambda,        sigma_+=1+r,
Omega_T=[sigma_-,sigma_+] x [T-r,2T+r].                              (1.2)
```

Every nontrivial zero has real part less than one.  Therefore, if

```text
rho=beta+i gamma,        beta>=1-delta,        T<=gamma<=2T,          (1.3)
```

then the disc `D(rho,r)` is contained in `Omega_T`.  For every Dirichlet
polynomial `M`,

```text
E_M(s)=1-zeta(s)M(s),             E_M(rho)=1.                         (1.4)
```

The subharmonic area mean-value inequality gives the uniform, pointwise-zero
obstruction

```text
integral_(Omega_T)|E_M(s)|^2 dA(s) >= pi*r^2.                         (1.5)
```

The number on the right can be extremely small; for fixed `delta,r` it is a
positive constant independent of `T`.  Thus an `o(1)` area bound, uniformly for
each dyadic `T`, proves a strip.  An almost-all-height or density estimate does
not suffice.

More precisely: if the area norm is `o(1)` as `T` tends to infinity through
all powers of two, then (1.5) excludes every zero satisfying (1.3) above some
height, because those dyadic intervals cover the ordinates.  The finite
remaining height range is compact and can be checked separately if one wants
the same explicit `delta`; without that finite check, it still combines with
the classical nonvanishing on `Re(s)=1` to give some uniform positive strip.

Take

```text
theta=1+c*delta,         X=floor(T^theta),
M_X(s)=sum_(d<=X)mu(d)d^(-s),
D_X(s)=sum_(m<=X)m^(-s).                                               (1.6)
```

Writing

```text
1-D_X(s)M_X(s)=-sum_(X<n<=X^2)c_X(n)n^(-s),
c_X(n)=sum_(d|n; d<=X; n/d<=X)mu(d),                                  (1.7)
```

one has `c_X(n)=0` for `2<=n<=X` and `|c_X(n)|<=tau(n)`.  Its exact area
diagonal is

```text
<<T X^(1-2*sigma_-)(log X)^3
 =T^[1-theta+2*lambda*theta+o(1)].                                    (1.8)
```

Consequently the sufficient power-exponent inequality for this diagonal to
be `o(1)` is

```text
theta>1/(1-2*lambda),                                                  (1.9)
```

The matching power obstruction is not inferred from the divisor-bound upper
estimate.  If
`p` is prime in `(X/2,X]`, then `c_X(2p)=-2`; these `>>X/log X` terms give the
matching lower bound

```text
Diagonal >>T X^(1-2*sigma_-)/(log X)^2.                              (1.9a)
```

Thus `theta<1/(1-2*lambda)` is impossible and strict inequality is
sufficient.  The displayed bounds do not decide the equality case, which is
irrelevant to the strictly power-saved implementation below.  In this precise
power-exponent sense, (1.9) is the threshold for this mollifier.

Under `theta=1+c*delta`, the sufficient strict inequality becomes

```text
c>2(1+eta)/(1-2(1+eta)delta).                                        (1.10)
```

The radius only affects a fixed constant in (1.5), so the exponent-optimal
choice is `eta` arbitrarily small.  The infimum threshold is

```text
theta=1+2 delta+O(delta^2).                                           (1.11)
```

In particular, making the desired strip thinner does not move the mollifier
below the conductor: it makes it only barely super-conductor.

## 2. A completely explicit tiny calibration

Set

```text
delta=10^(-6),       r=delta^2=10^(-12),
lambda=delta+r,      theta=1+3 delta.                                 (2.1)
```

Then

```text
1-theta+2*lambda*theta
 =-0.999991999994... *10^(-6),                                       (2.2)
```

so (1.8) is `o(1)`.  The coefficient-blind absolute offdiagonal scale is

```text
X^[4(1-sigma_-)]=T^[4*theta*lambda]
                =T^[4.000016000012...*10^(-6)].                       (2.3)
```

This is the precise `O(delta)` excess which a signed theorem would have to
remove.

Euler--Maclaurin causes no further restriction.  Multiplication by the trivial
bound

```text
|M_X(s)|<<X^(1-sigma_-)*log X                                       (2.4)
```

gives the following squared-area exponents for `zeta-D_X`:

```text
integral correction             -1+4*theta*lambda,
k-th Bernoulli correction       4k-1+4*theta*(lambda-k),
K-th remainder                  1+4K*(1-theta)+4*theta*lambda.        (2.5)
```

The first is `-0.999995999984...`.  Taking the fixed integer `K=100000`
makes the last exponent less than `-0.19`; every Bernoulli correction is also
power-saved.  Constants are enormous but depend only on the fixed candidate
`delta`, which is legitimate in an asymptotic strip proof.  Hence

```text
||(zeta-D_X)M_X||^2_(L2(Omega_T))=o(1).                               (2.6)
```

Thus the explicit strip would follow from the single uniform signed estimate

```text
||1-D_X M_X||^2_(L2(Omega_T))=o(1).                                  (2.7)
```

No density statement has been substituted for (2.7).

## 3. Smoothing and the conductor cutoff do not change the exponent

There is no sharp-cutoff loophole in the calculation.  For the ordinate
integral one may choose a nonnegative `W in C_c^infinity((1/2,5/2))` which is
at least one on a neighbourhood of `[1,2]`, and prove the stronger smoothed
bound

```text
integral integral W(t/T)|E_M(sigma+it)|^2 dt d sigma=o(1).             (3.1)
```

Positivity of the zero detector forces `hat(W)(0)=integral W>0`.  A
signed ordinate weight with zero Fourier mass could suppress the degenerate
frequency, but it would no longer majorize a positive area norm and (1.5)
would be lost.

Every arithmetic interval can be decomposed by a smooth dyadic partition of
unity; the finitely many endpoint terms satisfy the same power bounds as in
Section 2.  Alternatively one may give the Mobius cutoff a smooth upper skirt
while retaining a plateau equal to one through `X`.  The exact coefficient
deletion through `X`, and all coefficients below the skirt, are unchanged.

The unweighted zeta truncation can also be recompleted from `X` to a conductor
cutoff `Y=kappa*T`.  Poisson/Euler--Maclaurin has no nonzero stationary mode in
the discarded `m`-tail as soon as

```text
Y>max(t)/(2*pi),                                                       (3.2)
```

up to a fixed safety factor determined by the support of `W`.  Changing
`kappa` changes constants only.  It cannot replace the conductor exponent one
by an exponent below one.  We take `Y=floor(T)` below for clarity.

Put

```text
G_(T,X)(s)=D_Y(s)M_X(s)-1.                                            (3.3)
```

The same Euler--Maclaurin estimate gives

```text
||(D_X-D_Y)M_X||^2_(L2(Omega_T))
 <<T^[-1+4*theta*lambda+o(1)]=o(1),                                  (3.4)
```

and therefore (2.7) is equivalent to

```text
||G_(T,X)||^2_(L2(Omega_T))=o(1).                                    (3.5)
```

All subsequent spectral decompositions may consequently be carried out with
smooth weights and a genuine conductor-length unweighted variable.  Smoothing
does not remove the obstruction below.

## 4. The exact reciprocal hyperbola and its forced main cancellation

The coefficients of (3.3) are

```text
G_(T,X)(s)=sum_(n>Y)b_(T,X)(n)n^(-s),
b_(T,X)(n)=sum_(d|n; d<=X; n/d<=Y)mu(d),                              (4.1)
```

or, with every Mobius sign retained,

```text
G_(T,X)(s)
 =sum_(m<=Y)m^(-s) sum_(Y/m<d<=X)mu(d)d^(-s).                         (4.2)
```

For all sufficiently large `T`, `X>2Y`.  Complete divisor cancellation gives
the solid block

```text
b_(T,X)(n)=-1                    (Y<n<=2Y).                            (4.3)
```

This identity is unaffected by a smooth upper skirt at `X`: all relevant
divisors lie in its plateau.  The diagonal in the smoothed or unsmoothed area
norm therefore satisfies

```text
Delta_G >>T^(2-2*sigma_-)/log T
        =T^(2*lambda)/log T
        =T^[2.000002...*10^(-6)]/log T.                              (4.4)
```

It tends to infinity.  Hence (3.5) is not a theorem of the form "offdiagonal
is smaller than diagonal".  It requires the signed asymptotic

```text
OffDiag_G=-Delta_G+o(1).                                              (4.5)
```

In particular, a spectral large-sieve upper bound which discards signs cannot
prove (3.5), even if its error is power-saving.

## 5. What a genuine fixed spectral saving would accomplish

With the smooth ordinate weight, expansion of (4.2) produces

```text
T*hat(W)(T log(d_1*m_1/(d_2*m_2))).                                  (5.1)
```

Rapid decay localizes a dyadic block `d_i asymp D`, `m_i asymp M` to

```text
|d_1*m_1-d_2*m_2| <<D*M/T * T^epsilon.                               (5.2)
```

The coefficient-blind size of all near frequencies in the original deleted
polynomial is (2.3).  Therefore a *complete signed asymptotic*, including every
main term, of the schematic form

```text
OffDiag_F=O(T^[4*theta*lambda-kappa+epsilon])                          (5.3)
```

for one fixed `kappa>0` would prove (2.7) whenever

```text
4*theta*lambda<kappa.                                                 (5.4)
```

The quantifiers can be made explicit.  Given any fixed `kappa>0`, choose

```text
0<delta<min(10^(-2),kappa/8),    r=delta^2,    theta=1+3delta.        (5.5)
```

After decreasing the harmless upper bound `10^(-2)` if necessary, (1.9) and
`4*theta*(delta+delta^2)<kappa` both hold.  If (5.3) then holds for every
`epsilon>0`, uniformly for all sufficiently large dyadic `T`, choosing
`epsilon<(kappa-4*theta*lambda)/2` proves the area norm `o(1)` and hence the
high-height strip.  This conditional implication is a uniform zero theorem,
not a density theorem.

More generally, if conductor recompletion returned the forced main term in
(4.5) with an error `O(T^[C*delta-kappa])`, choosing
`delta<kappa/(2C)` would prove a strip.  Thus the proposed tiny-delta escape is
numerically sound: any honest fixed spectral saving dominates the conductor
excess after `delta` is made small enough.  The failure is that known estimates
do not give (5.3) or (4.5) for the complete form.

## 6. The omitted mode in physical space

The critical block has

```text
D asymp X,             M asymp Y asymp T.                             (6.1)
```

There (5.2) has product width `X`.  If `m_1,m_2,d_2` are fixed, the allowed
`d_1` lie in an interval of length

```text
H asymp X/T=T^(theta-1)=T^(3 delta)
  =X^[(theta-1)/theta]
  =X^[2.999991...*10^(-6)].                                          (6.2)
```

After a delta method, character decomposition, or Poisson completion, all
nonprincipal additive/character frequencies have oscillation.  The zero
frequency does not.  Its coefficient is a signed Mobius average on the
intervals (6.2).  Treating it separately requires uniform information of the
shape

```text
sum_(x<d<=x+H)mu(d)                                                    (6.3)
```

at a microscopic fixed-power relative length.  No unconditional fixed-power
cancellation is known there.  Almost-all short-interval theorems cannot be used
in a norm which must rule out a zero at every height.

The same mode is visible before discretizing shifts.  Replacing the `m`-sum in
(4.2) by its zero-frequency integral and setting `u=dm` gives

```text
P_0(s)=integral_Y^(XY) u^(-s)
       [sum_(u/Y<d<=min(u,X)) mu(d)/d] du,                             (6.4)
```

up to harmless smooth endpoint weights.  Formula (6.4) is the continuous
principal reciprocal-hyperbola mode.  Kuznetsov controls the complementary
nonzero Kloosterman indices; it does not turn (6.4) into a cuspidal error.

Even a global classical PNT bound is too weak.  A Vinogradov--Korobov type
estimate supplies only

```text
M(x)<<x*exp(-c(log x)^(3/5)(log log x)^(-1/5)),                        (6.5)
```

up to the customary harmless variations.  Multiplying this saving by a fixed
power `T^(C delta)` yields

```text
exp(C delta log T-c'(log T)^(3/5)(log log T)^(-1/5)),                  (6.6)
```

which tends to infinity for every fixed `delta>0`.  Logarithmic savings have
the same defect.  They can support a shrinking zero-free region, not a fixed
strip.

## 7. The exact Mellin/Perron identity: smoothing preserves the poles

The principal obstruction is not an artefact of the delta method.  Put
`X_*=X+1/2`, so the Perron threshold does not pass through an integer.
Initially in `Re(s)>1`, sharp Perron inversion gives

```text
M_X(s)=1/(2*pi*i) integral_((a)) X_*^w/[w*zeta(s+w)] dw,              (7.1)
```

and hence

```text
zeta(s)M_X(s)-1
 =1/(2*pi*i) integral_((a)) X_*^w/w * zeta(s)/zeta(s+w) dw -1.        (7.2)
```

When `zeta(s)!=0`, the residue at `w=0` cancels the final one.  At a zeta
zero, that point collides with a denominator-zero singularity, so the
cancellation cannot be used uniformly through the putative zero.  For
`zeta(s)!=0`, a fixed leftward contour shift meets poles

```text
w=rho-s                                                               (7.3)
```

from zeta zeros.  Avoiding (7.3) with a fixed-power error is precisely a
fixed zero-free theorem.

For a smooth cutoff `U(d/X)` equal to one near the origin, `1/w` in (7.1) is
replaced by its Mellin transform `hat(U)(w)`.  That transform has residue one
at zero, and (7.3) is unchanged.  A fixed smoothing function cannot vanish at
all unknown offsets `rho-s`.  Thus neither smoothing the mollifier nor
smoothing the spectral test deletes the reciprocal-zeta principal mode.
The residue-one normalization is forced: choosing a smooth transform with
zero residue would leave the constant coefficient in `zeta(s)M(s)-1`
uncancelled, whose area norm is of order `T`, not `o(1)`.  Smoothing therefore
cannot algebraically project away the principal mode while retaining a
mollifier for `1/zeta`.

Conversely, a fixed-power bound `M(x)<<x^(1-epsilon)` would make

```text
1/zeta(s)=s integral_1^infinity M(x)x^(-s-1)dx                        (7.4)
```

analytic for `Re(s)>1-epsilon`.  This is already a fixed zero-free strip.
The missing power in (6.3)--(6.4) is therefore not a routine input waiting to
be read off from the PNT.

## 8. Audit of the strongest relevant unconditional tools

The following comparison uses the estimates in their stated roles, rather than
transferring a saving from a different family by analogy.

| Input | What it controls | Why it does not prove (4.5) |
|---|---|---|
| Deshouillers--Iwaniec/Kuznetsov spectral large sieve | Averages of nonzero Kloosterman modes | The degenerate index is an Eisenstein/Ramanujan main term and here contains (6.4); Cauchy--Schwarz also loses the negative main term required in (4.5). |
| Duke--Friedlander--Iwaniec and Bettin--Chandee Kloosterman-fraction bounds | Bilinear/trilinear reciprocal phases with arbitrary coefficient sequences | They save on oscillatory reciprocal phases.  At zero phase they return the coefficient sum, namely the Mobius principal mode. |
| Bettin--Chandee--Radziwill twisted second moment | General twists through `T^(17/33-epsilon)` and special factorable twists through `T^(3/4-epsilon)` | The mollifier here has length `T^(1+3 delta)>T`, outside both ranges; more importantly the theorem does not furnish (4.5) for the reciprocal tail. |
| Dong--Robles--Zeindler 2026 preprint (withdrawn) | Claimed an improvement to `T^(1/2+1/46-epsilon)`, but the authors report that a missing factor invalidates the improved bound | It supplies no usable theorem for this audit; even the withdrawn claimed range was strictly sub-conductor and did not supply the principal Mobius frequency. |
| Wright 2026 unbalanced-convolution preprint | Improved nonprincipal distribution after an expected principal term is subtracted, with logarithmic savings in its application | The subtracted principal term is exactly the term that must create (4.5); logarithmic saving cannot beat `T^(C delta)`. |
| Exponent-pair/nonstationary-phase estimates | Fixed savings when the transformed phase has a nonzero derivative | The principal mode has identically zero derivative.  Applying an exponent pair to it gives the trivial coefficient sum. |

Primary references used for the range audit:

- S. Bettin, V. Chandee, M. Radziwill,
  [The mean square of the product of zeta with Dirichlet polynomials](https://arxiv.org/abs/1411.7764).
- S. Bettin, V. Chandee,
  [Trilinear forms with Kloosterman fractions](https://arxiv.org/abs/1502.00769).
- A. Dong, N. Robles, D. Zeindler,
  [Bilinear forms with Kloosterman fractions and applications](https://arxiv.org/abs/2601.00292)
  (withdrawn; the arXiv record says the claimed improvement fails after a
  missing factor is restored).
- T. Wright,
  [Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions](https://arxiv.org/abs/2604.25177).
- S. Bettin, S. M. Gonek,
  [The theta=infinity conjecture implies the Riemann hypothesis](https://arxiv.org/abs/1604.02740).

The last paper is useful context: sufficiently long uniform mollified moments
are themselves known to imply zero-free half-planes.  It is therefore essential
not to import a sub-conductor or density-level moment estimate as if it were the
super-conductor uniform bound (2.7).

## 9. Verdict and the exact surviving theorem

The tiny-delta optimization does materially sharpen where the barrier lies.
The analytic completion and the deleted-polynomial diagonal are already
power-saved at

```text
delta=10^(-6),       r=10^(-12),       X=T^(1.000003).                (9.1)
```

Moreover, a genuine fixed saving on the *complete signed form* would dominate
the `4.000016...*10^(-6)` excess.  Thus there is no adverse exponent
optimization preventing an extremely thin strip.

But the fixed spectral saving is available only after the principal frequency
has been removed or placed into a main term.  In this problem that main term is
not known: it is simultaneously

```text
the short-interval Mobius average (6.3),
the continuous reciprocal-hyperbola mode (6.4), and
the reciprocal-zeta pole family (7.3).                                (9.2)
```

It must generate `-Delta_G` with an `o(1)` remainder.  Proving that is the
strip-strength arithmetic step, not a consequence of known Kuznetsov or
Kloosterman savings.  Therefore this audit does not prove a uniform zero-free
strip.  The next admissible theorem is narrowly stated: evaluate the complete
principal Mobius mode jointly with the nonprincipal spectrum so that the
forced cancellation (4.5) emerges with a fixed-power error.  Estimating only
the nonprincipal spectrum, or only bounding the offdiagonal in absolute value,
cannot close the argument.
