# Mertens increment Poincare theorem and the zero-mode gate

Status: exact deterministic strengthening and scoped Type-I/II obstruction,
2026-08-12.  The short-increment criterion is shown to imply a larger
zero-free strip than the earlier quadratic-energy route, and the existence
of any fixed-power instance of that criterion is shown to be qualitatively
equivalent to the existence of some fixed zero-free strip.  No such
fixed-power estimate, and hence no strip, is proved here.  The Poincare
argument is elementary and may be folklore; novelty outside this project is
not claimed.

## 1. Verdict

Put

```text
M(x)=sum_(n<=x) mu(n),
J(X,H)=sum_(1<=n<=X-H)|M(n+H)-M(n)|^2.              (1.1)
```

The direct anchored inequality is

```text
|M(X)| <= 2H+sqrt(X*J(X,H))/H.                      (1.2)
```

Consequently, if for fixed `0<theta<1` and `eta>0`, with
`H=floor(X^theta)`,

```text
J(X,H) << X*H^(2-eta),                              (1.3)
```

then

```text
M(X) << X^theta+X^(1-theta*eta/2),                  (1.4)

zeta(s)!=0 for
Re(s)>max(theta,1-theta*eta/2)
     =1-min(1-theta,theta*eta/2).                   (1.5)
```

This improves the previous route through
`S(X)=sum_(n<=X)|M(n)|^2`, whose strip width was only

```text
(1/3)*min(2-2theta,theta*eta).                       (1.6)
```

For a given `eta`, the two terms in (1.5) balance at

```text
theta=2/(2+eta),       strip width=eta/(2+eta).      (1.7)
```

The improvement is deterministic; it does not supply (1.3).  In fact, the
existential statement

```text
there are fixed theta in (0,1), eta>0 satisfying (1.3)   (1.8)
```

is qualitatively equivalent to the existence of some fixed zero-free strip.
Thus (1.3) is an independent formulation and may expose useful arithmetic
structure, but it is not a lower-logical-strength target.

## 2. Anchored step-Poincare theorem

### Theorem 2.1

Let `1<=H<=X/2`.  For any real sequence `a(n)` with `a(0)=0`, put

```text
A(N)=sum_(n<=N)a(n),
J_a(X,H)=sum_(1<=n<=X-H)|A(n+H)-A(n)|^2.            (2.1)
```

If `|a(n)|<=1`, then

```text
J_a(X,H)>=(H^2/X)*(|A(X)|-2H)_+^2,                 (2.2)

|A(X)|<=2H+sqrt(X*J_a(X,H))/H.                     (2.3)
```

### Proof

For each `1<=r<=H`, let

```text
k_r=floor((X-r)/H),       N_r=r+k_r*H.              (2.4)
```

Then `X-H<N_r<=X`, while `|A(r)|<=H`.  Therefore

```text
|A(N_r)-A(r)|
 >=|A(X)|-|A(X)-A(N_r)|-|A(r)|
 >=|A(X)|-2H.                                      (2.5)
```

Telescope down the residue chain and apply Cauchy--Schwarz:

```text
sum_(j=0)^(k_r-1)
 |A(r+(j+1)H)-A(r+jH)|^2
 >=(|A(X)|-2H)_+^2/k_r
 >=(H/X)*(|A(X)|-2H)_+^2.                          (2.6)
```

The `H` residue chains are disjoint, and all their increment starting
points lie in `[1,X-H]`.  Summing (2.6) over `r` proves (2.2), and (2.3)
follows immediately.  QED

Apply Theorem 2.1 to `a(n)=mu(n)`.  Substitution of (1.3) into (2.3)
gives (1.4).  The Mellin identity

```text
1/zeta(s)=s*integral_1^infinity M(x)x^(-s-1)dx      (2.7)
```

then proves (1.5), by the identity-theorem argument in the quadratic-energy
report.

The scale in (2.2) is sharp for bounded-increment information alone.  For
the real sequence `a(n)=c`, `0<c<=1`, one has

```text
A(X)=cX,
J_a(X,H)=(X-H)c^2H^2
         asymp H^2*A(X)^2/X.                        (2.8)
```

Thus improving the powers in (2.2) requires arithmetic information special
to Mobius; no stronger coefficient-free Poincare inequality is available.

### Corollary 2.2 -- the imprint of one hypothetical zero

Suppose `zeta` has a zero with real part `beta`.  For every `epsilon>0`,
there are arbitrarily large `X` for which

```text
|M(X)|>=X^(beta-epsilon).                            (2.9)
```

Otherwise (2.7) would analytically continue `1/zeta` across that zero.
Fix `theta<beta` and put `H=floor(X^theta)` along this sequence.  Theorem
2.1 gives

```text
J(X,H)>=X^(2beta-1-2epsilon)*H^2                    (2.10)
```

for all sufficiently large selected `X`, up to an absolute constant.  If

```text
beta>max(theta,1-theta*eta/2),                      (2.11)
```

choose `epsilon` smaller than both strict gaps.  Then (2.10) is larger than
`X*H^(2-eta)` by a fixed power.  Thus a single zero in the forbidden region,
not a dense family of zeros, defeats (1.3).  Zero-density information which
still permits one such zero cannot by itself close this mean-square target.

## 3. Exact internal correlation ledger

Expanding (1.1) without discarding the endpoints gives

```text
J(X,H)=sum_(k,l<=X) mu(k)mu(l) W_(X,H)(k,l),        (3.1)
```

where

```text
W_(X,H)(k,l)
 =[
    min(X-H,k-1,l-1)
   -max(1,k-H,l-H)+1
  ]_+.                                              (3.2)
```

In the interior this is the usual triangular weight `H-|k-l|`; (3.2) is
the exact boundary-corrected kernel.

There is a simpler full-convolution diagnostic.  Set

```text
a_k=mu(k)*1_(1<=k<=X),
J^*(X,H)=sum_(n in Z)|sum_(n<k<=n+H)a_k|^2.         (3.3)
```

Then, exactly,

```text
J^*(X,H)
 =sum_(|h|<H)(H-|h|)
    sum_(1<=k,k+h<=X)mu(k)mu(k+h)                  (3.4)

 =integral_0^1 |A_X(alpha)|^2|D_H(alpha)|^2dalpha, (3.5)

A_X(alpha)=sum_(k<=X)mu(k)e(k alpha),
D_H(alpha)=sum_(j=1)^H e(j alpha).                  (3.6)
```

The internal and full energies obey only

```text
0<=J^*(X,H)-J(X,H)<2H^3.                            (3.7)
```

Indeed, the difference consists of fewer than `2H` boundary windows, each
of absolute size at most `H`.  This is a genuine bookkeeping warning.  The
full Fourier target implies the internal target with no loss, but the
reverse transfer absorbs (3.7) only when

```text
H^(1+eta)<<X.                                       (3.8)
```

Outside that range, replacing (3.2) by the translation-invariant Fejer
kernel silently introduces a boundary term larger than the desired power
saving.  A spectral proof must retain the finite-section projection or use
a taper whose boundary cost is explicitly budgeted.

There is also an exact absolute-value obstruction.  Define

```text
A_abs(X,H)=sum_(k,l<=X)|mu(k)mu(l)|W_(X,H)(k,l).     (3.9)
```

For every `H->infinity` with `H=o(X)`,

```text
A_abs(X,H)>>X*H^2.                                  (3.10)
```

To prove this, discard the two endpoint ranges and partition the remaining
integers into blocks of length `floor(H/2)`.  If `m_b` is the number of
squarefree integers in block `b`, every ordered pair in that block has
`W_(X,H)(k,l)>=H/2`.  The squarefree density gives
`sum_b m_b=(6/pi^2+o(1))X`, while there are `O(X/H)` blocks.  Cauchy--Schwarz
therefore gives

```text
A_abs(X,H)>=(H/2)sum_b m_b^2>>H*(XH)=XH^2.
```

Thus applying the triangle inequality to the exact Mobius correlations
loses the entire desired factor `H^eta`.  A successful correlation or
Type-II argument must preserve the signs jointly; squarefree support and
absolute sieve majorants cannot suffice.

## 4. Why standard Fourier norms do not close the power

Two exact power comparisons prune coefficient-blind spectral attacks.

First, for any coefficients `|a_k|<=1` and any fixed `q>=1`, Parseval,
the trivial `L^infinity` bound, interpolation, and the Dirichlet-kernel norm
give

```text
||A||_(2q)^2 <=X^(2-1/q),
|||D_H|^2||_(q/(q-1)) <<_q H^(1+1/q),               (4.1)

J^*(X,H)<<_q X^(2-1/q)H^(1+1/q).                   (4.2)
```

At `H=X^theta`, the exponent in (4.2) exceeds the target exponent in
(1.3) by

```text
(1-theta)*(1-1/q)+theta*eta>0.                      (4.3)
```

Thus no fixed-moment Holder/Parseval interpolation using only coefficient
size reaches (1.3).  The case `q=1` is already the trivial bound
`J^*<=XH^2`.

Nor do logarithmic estimates at many polynomial scales self-improve by a
coefficient-free argument.  The single bounded positive sequence

```text
a(n)=exp(-sqrt(log(n+2)))
```

has, for every fixed `0<theta<1` and `H=X^theta`,

```text
A(X)=X*exp(-(1+o(1))*sqrt(log X))=X^(1-o(1)),

J_a(X,H)
 =X*H^2*exp(-(2+o(1))*sqrt(log X))
 <<_B X*H^2/(log X)^B                              (4.4)
```

for every fixed `B`.  These estimates follow from slow variation, with the
initial `O(H)` starting points contributing a smaller term.  Thus even all
fixed logarithmic savings, simultaneously across fixed polynomial scales,
are compatible with a near-linear endpoint sum.  Arithmetic sign
information is indispensable.

Second, Davenport's Mobius-specific uniform estimate

```text
sup_alpha |A_X(alpha)| <<_B X/(log X)^B             (4.5)
```

and `integral |D_H|^2=H` give

```text
J^*(X,H)<<_B H*X^2/(log X)^(2B).                    (4.6)
```

For `H=X^theta`, (4.6) could imply (1.3) only if

```text
X^(1-theta+theta*eta)<< (log X)^(2B),               (4.7)
```

which is false for every fixed `B`.  Arbitrarily large fixed logarithmic
savings therefore do not become the required power saving.

A uniform Type-I/II estimate of the stronger form

```text
sup_alpha |A_X(alpha)|<<X^(1-delta)                 (4.8)
```

would need

```text
delta>=(1-theta+theta*eta)/2                        (4.9)
```

to close through this route.  But (4.8) includes `alpha=0` and hence already
asserts `M(X)<<X^(1-delta)`, which by itself proves a fixed strip.  A
minor-arc bilinear theorem avoids that conclusion only by excluding the
central frequency; it then leaves precisely the mode to which the present
criterion is sensitive.

These are no-go statements for the displayed norm templates, not for a
Mobius-specific signed correlation or finite-section dispersion theorem.

## 5. The parity term in an absolute Type-I decomposition

The exact multiplicative identity

```text
mu(n)=sum_(d^2|n) mu(d)*lambda(n/d^2)               (5.1)
```

follows either prime by prime or from

```text
1/zeta(s)=[zeta(2s)/zeta(s)]*[1/zeta(2s)].          (5.2)
```

Consequently a short Mobius sum is a signed superposition of short
Liouville sums at square-dilated scales.  The `d=1` summand has the original
interval length.  Any triangle-inequality treatment of (5.1) must therefore
control that long Liouville block separately; square-divisor sparsity does
not remove it.

This is a genuine parity gate.  Since

```text
sum lambda(n)n^(-s)=zeta(2s)/zeta(s),               (5.3)
```

a fixed power bound for Liouville partial sums in a half-plane adjacent to
one is itself a fixed-strip statement for zeta.  The same anchored
Poincare argument applies to Liouville increments.  Thus an absolute
Type-I use of (5.1) merely transfers the target to its `d=1` parity term.
A joint signed bilinear estimate allowing cancellation among the square
scales is not ruled out, but no such fixed-power theorem is presently in
the audited input.

## 6. Existential equivalence with a fixed strip

The forward implication follows from Theorem 2.1: any one pair
`theta in (0,1)`, `eta>0` satisfying (1.3) gives the positive strip width
in (1.5).

Conversely, suppose zeta has no zero in `Re(s)>q` for some fixed `q<1`.
The standard reciprocal-zeta/Perron implication gives, for every
`epsilon>0`,

```text
M(x)<<_epsilon x^(q+epsilon).                       (6.1)
```

Choose `q+epsilon<theta<1`.  Every length-`H` increment with
`H=floor(X^theta)` then has absolute value `O(X^(q+epsilon))`, and hence

```text
J(X,H)<<X^(1+2q+2epsilon).                          (6.2)
```

Choose any fixed

```text
0<eta<2-2*(q+epsilon)/theta.                        (6.3)
```

Equations (6.2)--(6.3) imply (1.3).  Therefore

```text
some fixed strip exists
 iff some fixed-power short-increment estimate (1.3) exists. (6.4)
```

The exponents in the two directions are not inverse-optimal; (6.4) is an
existential logical classification.

## 7. Research decision

The best unconditional imported estimate currently has the form

```text
J(X,H)<<_(B,epsilon) X*H^2/(log X)^B
```

in a polynomial short-interval range.  It is `H^(-o(1))`, not (1.3).

An exact exceptional-set ledger makes the missing power transparent.  If
there are fixed `a,b>0` such that

```text
|M(n+H)-M(n)|<=H^(1-a)
```

outside at most `X*H^(-b)` starting points, then the trivial bound `H` on
the exceptional set gives

```text
J(X,H)<<X*H^(2-min(2a,b)).                          (7.1)
```

The resulting strip width is

```text
min(1-theta,theta*a,theta*b/2).                     (7.2)
```

Thus a dispersion theorem may divide the work between a power-saving
typical bound and a power-sparse exceptional set, but both ledgers must be
fixed powers.  Logarithmic savings in either place remain subpower.

The exact live options are therefore:

1. a finite-section, signed average of the correlations in (3.1)--(3.2)
   with a genuine power saving;
2. a joint Type-I/II theorem that retains cancellation across the parity
   term in (5.1); or
3. direct low-frequency control strong enough to improve (4.6), without
   assuming the corresponding zero-free estimate at `alpha=0`.

Ordinary fixed Fourier moments, Davenport logarithmic uniformity, an
untracked full Fejer replacement, and absolute square-divisor decomposition
are pruned at the displayed ledgers.  None of this proves (1.3), a fixed
strip, or RH.
