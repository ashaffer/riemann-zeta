# R130 null-tail Hadamard dilation frame gate

Status: an exact null-on-tail Fourier/Hadamard detector frame is proved.
It improves the *unnormalized* adjacent-cutoff zero multiplier from
`M^(-Re rho)` to `M^(1/2-Re rho)`, has shift span only `log(2M)`, and can
be made either complex with all squarefree integers in `(M,2M]` or real
with a constant-density subset.  The same tight-frame identity also gives
the decisive reality check: the bank's arithmetic energy is exactly the
sum of the energies of its individual dilation coordinates.  The apparent
factor `M` in zero energy is paid by `M` added coordinates.  On the complete
field those coordinates are shifted copies of the original prime field,
or equivalently arbitrary phased convolutions with `Lambda`; neither R116
nor R118 gives them a primitive fixed-power saving.

A stronger one-member coherent null block is also evaluated.  Its zero
multiplier is asymptotic to a nonzero constant times `M^(1-rho)` for every
fixed zero `rho` with `Re rho<1`.  Euler summation, however, identifies its
completed Type-I main term with `sqrt(M)` times the same center-annihilated
prime-discrepancy field at scale `X/M`.  Only the discretization error is
power-small.  Thus both constructions transport the missing zero-free
estimate to a smaller scale; they do not supply it.  No fixed zero-free
strip is proved or disproved.

Date: 2026-08-08.

**2026-09-02 successor scope correction.**  References below to R116 saving
“all proper conductors” apply only to its balanced squarefree-semiprime
packet.  R128 restores all conductor classes exactly, but the restored object
is the original full positive R71 energy.  The null-tail frame does not
transfer the packet-level saving to that global object.

Predecessors:

* [`R123-TRUNCATED-MOBIUS-DILATION-BANK-GATE.md`](R123-TRUNCATED-MOBIUS-DILATION-BANK-GATE.md),
  for exact truncated-Mobius collapse and the adjacent-cutoff detector;
* [`R116-SIGNED-JOINT-TYPEII-ATTACK.md`](R116-SIGNED-JOINT-TYPEII-ATTACK.md),
  for the primitive reciprocal-to-smooth-Mobius dual;
* [`R118-ENDPOINT-SQUARE-FUNCTION-PRIME-AVERAGE-GATE.md`](R118-ENDPOINT-SQUARE-FUNCTION-PRIME-AVERAGE-GATE.md),
  for the sparse prime-modulus endpoint gain; and
* [`R102-CENTER-ANNIHILATED-OFF-AXIS-GATE.md`](R102-CENTER-ANNIHILATED-OFF-AXIS-GATE.md),
  for the complete `Q_h` prime field used in the coherent-block audit.

## 1. Dilation notation and the null tail

Put

```text
(U_q F)(R)=q^(-1/2)F(R-log q),
C_M=sum_(q<=M) mu(q)U_q.                              (1.1)
```

For

```text
f_R(t)=t^(-1/2)V_Q(R-log t),
F_(d,b)(R)=sum_(m>=1)f_R(mdb),                        (1.2)
```

the scaling identity in R123 gives, for any finitely supported sequence
`a(q)`,

```text
sum_q a(q)U_q F_(d,b)(R)
 =sum_(n>=1)[sum_(q|n)a(q)]f_R(ndb).                  (1.3)
```

Suppose the support on the right of (1.3) restricts `n<=M`.  Then every
operator supported on `q>M` is identically zero on this frozen tail.  In
particular,

```text
(C_M+sum_(M<q<=2M)b(q)U_q)F_(d,b)=f_R(db)             (1.4)
```

for completely arbitrary tail coefficients `b(q)`.  This is the null
space which the frame below uses.  Notice that (1.4) is a statement about
the frozen Vaughan tail, not the complete prime field.

Let

```text
S_M={q integer:M<q<=2M, mu(q)^2=1},      N=#S_M.      (1.5)
```

The elementary squarefree counting formula gives

```text
N=(6/pi^2)M+O(sqrt(M)),                              (1.6)
```

so `N asymp M`.

## 2. Exact Fourier frame

Enumerate `S_M={q_1,...,q_N}`, put `Q=N+1`, and let

```text
omega=exp(2 pi i/Q).
T_j=C_M+sum_(ell=1)^N mu(q_ell)omega^(j ell)U_(q_ell),
                    0<=j<Q.                          (2.1)
```

These are `Q` different completed operators, but by (1.4) they act
identically on every active free cofactor `m<=M`.

For a complex parameter `s`, define

```text
A_M(s)=sum_(q<=M)mu(q)q^(-s),
lambda_j(s)=A_M(s)
 +sum_(ell=1)^N mu(q_ell)omega^(j ell)q_ell^(-s).     (2.2)
```

### Theorem 2.1 (null-tail tight detector frame)

The bank (2.1) has the following exact properties.

1. Its shift span is `log(2M)` and every member satisfies (1.4).
2. For every complex `s` with `sigma=Re s`,

```text
(1/Q)sum_(j=0)^(Q-1)abs(lambda_j(s))^2
 =abs(A_M(s))^2+sum_(q in S_M)q^(-2 sigma).           (2.3)
```

Consequently

```text
max_j abs(lambda_j(s))
 >=[sum_(q in S_M)q^(-2 sigma)]^(1/2)
 asymp M^(1/2-sigma)                                 (2.4)
```

uniformly for `sigma` in a fixed compact interval.
3. More generally, for every complex Hilbert space `H` and every
`H`-valued field `F`,

```text
sum_(j=0)^(Q-1)norm(T_j F)_H^2
 =Q[norm(C_MF)_H^2+sum_(q in S_M)norm(U_qF)_H^2].    (2.5)
```

### Proof

The first assertion is (1.4).  Apply Parseval for the `Q` by `Q` discrete
Fourier matrix to the vector

```text
(A_M(s), mu(q_1)q_1^(-s),...,mu(q_N)q_N^(-s)).       (2.6)
```

This proves (2.3), and the largest summand is at least the average.  Since
all `q` lie in `(M,2M]` and `N asymp M`, (2.4) follows.  The same Parseval
identity for an `H`-valued vector

```text
(C_MF, mu(q_1)U_(q_1)F,...,mu(q_N)U_(q_N)F)          (2.7)
```

proves (2.5).  QED.

The row `j=0` is exactly `C_(2M)`, because nonsquarefree tail coefficients
of the latter vanish.  The remaining rows are phased Mobius extensions.
Thus at least one bank member retains some familiar arithmetic structure,
but (2.4) does not say that the good member is `j=0`.

### Real version

Complex coefficients are harmless in a quadratic energy estimate, but
they are not necessary.  Choose a power of two `Q_0` with

```text
(N+1)/2<Q_0<=N+1,       L=Q_0-1,                     (2.8)
```

select `L` elements of `S_M`, and take a Sylvester Hadamard matrix of
order `Q_0` whose first column is all ones.  Use that first column for
`C_M` and the remaining `L` columns, multiplied by the selected `mu(q)`,
for the null tail.  Orthogonality of the columns proves the real analogues
of (2.3)--(2.5), with `L asymp M` and coefficients `plusminus 1`.  A
paired bank `C_M plusminus B_j` also works, but doubles the number of rows;
the first-column Hadamard construction cancels the baseline cross terms
without that doubling.

## 3. Baseline cancellation and the norm that spends the gain

For one Hadamard/Fourier row, the tail coefficient norms are

```text
norm(b_j)_infinity=1,
norm(b_j)_2=asymp sqrt(M),
norm(b_j)_1=asymp M.                                 (3.1)
```

Including the operator weight in `U_q`, its raw projective translation
norm is

```text
sum_(q in S_M)abs(b_j(q))q^(-1/2) asymp sqrt(M).      (3.2)
```

If the field has critical growth

```text
abs(F(S))<=exp(S/2+o(S)),                             (3.3)
```

then the same triangle calculation instead contains the extra scale loss
from `F(R-log q)` and costs

```text
sum_(q in S_M)1/q asymp 1.                           (3.4)
```

The corresponding critical Hilbert norm is

```text
[sum_(q in S_M)1/q^2]^(1/2) asymp M^(-1/2).          (3.5)
```

At `Re s=1`, (2.4) is also `asymp M^(-1/2)`.  Hence the
`sqrt(M)` improvement over one adjacent coordinate is exactly the
`sqrt(M)` increase in the critical Hilbert norm of the tail block.  With
unweighted coefficient conventions the same statement is the factor
`norm(b_j)_2=sqrt(M)` in (3.1).

This is not an artifact of Cauchy--Schwarz.  Identity (2.5) proves it with
equality.  Averaging the bank cancels all cross terms and leaves one copy
of the energy of every added dilation.  Taking differences of two rows
cancels `C_M` and annihilates the frozen tail altogether, but on the
complete field it leaves precisely a signed sum of those same dilation
coordinates.  It therefore moves the zero carrier into the cutoff heads;
it does not delete it.

## 4. What the completed fields actually are

For a finitely supported arithmetic sequence `a`, write

```text
D_(a,V)(R)=sum_n a(n)n^(-1/2)V(R-log n).              (4.1)
```

The exact convolution identity is

```text
T_jD_(a,V)=D_(c_j*a,V),                               (4.2)

c_j(q)=mu(q)1_(q<=M)
 +1_(q=q_ell for some ell)mu(q_ell)omega^(j ell).     (4.3)
```

For the complete prime field this is

```text
(c_j*Lambda)(n)
 =sum_(q|n)c_j(q)Lambda(n/q).                         (4.4)
```

Except in the unphased row, (4.4) is an arbitrary Fourier modulation of
a length-`M` divisor coefficient.  The identity

```text
mu*Lambda=-mu log                                    (4.5)
```

which creates R116's primitive smooth-Mertens dual does not simplify the
phased tail.  R116 still saves the proper reciprocal conductors in its
balanced squarefree-semiprime packet, but its
primitive term becomes the ordinary sum with coefficient (4.4), and no
fixed power is available there.

R118 is coefficient-uniform only after a common prime-modulus sparse
`(P,x,y)` packet has been constructed.  It does not construct that packet
from the full-support composite primitive term, and (4.4) adds an
independent dilation/divisor coordinate.  Projectively separating that
coordinate pays (3.2); treating it in a Hilbert square function gives the
exact cost (2.5).  Thus the currently proved R116/R118 theorems do not give
a coefficient-uniform fixed-power bound for all augmented fields.

There is an even sharper way to state the obstruction.  Applying (2.5) to
the *complete* `Q_h` prime field eliminates the arbitrary-looking rows and
gives a sum of unfiltered shifted prime-field energies.  Those shifted
fields themselves contain every zeta zero.  Power-saving their sum is not
a cutoff-head estimate already in the repository; it is the desired
zero-free estimate at the smaller scales.

## 5. Fixed-power optimization

Let the original physical scale be `X=exp R`, choose

```text
M=X^a,              Y=X/M=X^(1-a),       0<a<1.      (5.1)
```

For a zero `rho=beta+i gamma`, the average frame multiplier in (2.3) has
tail size

```text
sum_(q in S_M)q^(-2 beta) asymp M^(1-2 beta).         (5.2)
```

Thus its zero-carrier energy at scale `X` is, up to the fixed residue and
window factors,

```text
X^(2 beta-1)M^(1-2 beta)=Y^(2 beta-1).                (5.3)
```

At `beta=1`, the apparent multiplier loss is `M^(-1)=X^(-a)` in energy.
But the critical energy of the `M` shifted coordinates is

```text
X sum_(q in S_M)q^(-2) asymp X/M=Y.                  (5.4)
```

It has exactly the same `X^(-a)` factor.  If one somehow proved a complete
arithmetic bound

```text
frame energy <<Y^(1-kappa),       0<kappa<=1,         (5.5)
```

then comparison with (5.3) would exclude

```text
beta>1-kappa/2.                                      (5.6)
```

The parameter `a` cancels.  Formula (5.6) is simply the zero-free strip
which a `Y^(-kappa)` energy saving for the complete prime field already
implies.  A single adjacent coordinate has an additional `M^(-1)` in both
its zero energy and its arithmetic energy and leads to the same condition.

In a less scale-aware ledger, the frame seems to improve the adjacent
zero-energy loss from `X^(-2a)` to `X^(-a)`.  The row coefficient energy
`norm(b_j)_2^2=X^a` spends exactly that improvement, restoring the same
threshold.  This is the large-bank/operator-norm failure requested in the
gate.

For comparison:

* R118 saves `H^(-1/2)` in amplitude at `X=H^2`, hence `X^(-1/2)` in
  energy.  If that estimate applied to the *complete* augmented field it
  would correspond to `kappa=1/2` in (5.5).  It applies only to the sparse
  prime-modulus endpoint, not the composite primitive field, so this
  conditional calculation cannot be invoked.
* R116's balanced-semiprime proper-conductor estimate
  `O(c^(1/2+epsilon))` is already a contribution to the bilinear/energy
  expression inside R105, against a top contribution of order `c`; it must
  not be squared a second time.  It therefore records a one-half exponent
  saving on that scoped contribution, not a full energy power.  The
  primitive conductor, which contains the smooth-Mertens/zero carrier, has
  `kappa=0`.  The frame does not transfer the proper-conductor saving to
  that primitive term.

There is also a geometric cost: `log(2M)=a log X+O(1)` is a macroscopic
shift, whereas R123's regular schedule uses `log M=o(log X)`.  Every
R116/R118 packet would have to be rebuilt uniformly down to scale `Y`.
With no new estimate on the null-tail coordinates, the optimal choice is
therefore the smallest allowed `M` (the original `X^o(1)` cofactor bound),
not a positive fixed `a`.

## 6. The stronger coherent null block

The tight frame is not the strongest scalar zero detector in its null
space.  Consider the all-integer coherent block

```text
B_M=sum_(M<q<=2M)U_q.                                (6.1)
```

It also vanishes identically in (1.3) whenever the resulting cofactor is
restricted to `n<=M`.  Its zero multiplier is

```text
L_M(s)=sum_(M<q<=2M)q^(-s).                          (6.2)
```

### Proposition 6.1 (coherent Mellin multiplier)

For every fixed `s` with `0<sigma=Re s<1`,

```text
L_M(s)=I(s)M^(1-s)+O_s(M^(-sigma)),                  (6.3)

I(s)=integral_1^2 v^(-s)dv
    =(2^(1-s)-1)/(1-s).                              (6.4)
```

Moreover `I(s)!=0` throughout `sigma<1`.  Hence

```text
abs L_M(s) asymp_s M^(1-sigma)                       (6.5)
```

for all sufficiently large `M` depending on `s`.

### Proof

Euler summation gives (6.3).  If `I(s)=0`, then `2^(1-s)=1`.  The left
side has modulus `2^(1-sigma)>1` when `sigma<1`, a contradiction.  QED.

The fixed-`s` qualification matters: no height-uniform lower bound is
asserted.  For excluding a particular hypothetical zero this is enough,
because `X`, hence `M=X^a`, may tend to infinity after the zero is fixed.
A positive squarefree block has the same leading term divided by
`zeta(2)`, with a weaker elementary discrepancy error.

The multiplier (6.5) is much larger than (2.4), and there is no bank.  The
completed field nevertheless reveals why this does not prove a strip.

### Proposition 6.2 (exact reduced-scale Type-I main)

Let `V_Q` be a fixed compactly supported `C^1` center-annihilated window,
and suppose `R=log X+O(1)`, `M<X`, and `Y=X/M` tends to infinity.  Define

```text
W_Q(z)=integral_1^2 v^(-1/2)V_Q(z-log v)dv.           (6.6)
```

Then, pointwise on a fixed `R`-block,

```text
B_M D_(Lambda,V_Q)(R)
 =sqrt(M)D_(Lambda,W_Q)(R-log M)
   +O_V(sqrt(X)/M).                                  (6.7)
```

The same formula holds for the completed prime-minus-continuum field.
The window `W_Q` has the two vanishing center moments and is again a
`Q_h` window.

### Proof

Expand the left side and sum first in `q`:

```text
sum_k Lambda(k)k^(-1/2)
 sum_(M<q<=2M)q^(-1/2)V_Q(R-log k-log q).             (6.8)
```

For fixed `k`, Euler summation replaces the inner sum by its integral with
error `O_V(M^(-1/2))`.  After `q=Mv`, that integral is

```text
sqrt(M)W_Q(R-log M-log k).                           (6.9)
```

The support restricts `k asymp Y`.  Chebyshev's bound gives

```text
sum_(k asymp Y)Lambda(k)k^(-1/2)<<sqrt(Y),            (6.10)
```

so the total discretization error is

```text
M^(-1/2)sqrt(Y)=sqrt(X)/M.                           (6.11)
```

Convolution in the logarithmic variable commutes with `Q_h`; equivalently,
direct substitution in the two center moments shows that both vanish for
`W_Q`.  This also proves the completed version.  QED.

For `M=X^a`, the error in (6.7) saves `X^(-a)` in amplitude against the
critical `sqrt(X)` scale.  The main term does not.  It is exactly
`sqrt(M)` times the original center-annihilated prime-discrepancy problem
at scale `Y=X^(1-a)`.  Its zero contribution is

```text
sqrt(M)Y^(rho-1/2)
 =X^(rho-1/2)M^(1-rho),                              (6.12)
```

which is the multiplier in (6.3).  Thus divisor switching has not turned
the coherent head into a known Type-I error: it has exposed a self-similar
copy of the full zero carrier.  `Q_h` kills the pole center, but every
nontrivial zero residue remains.

If a bound `D_(Lambda,W_Q)(log Y)<<Y^(1/2-delta)` were already known, then
(6.7) would save

```text
min(a,delta(1-a))                                    (6.13)
```

in amplitude, optimized at `a=delta/(1+delta)`.  Here `delta>0` is itself
a fixed zero-free-strip strength estimate for the complete reduced-scale
field.  With only the currently available subpower prime-error estimate,
`delta=0`, (6.13) supplies no fixed power.

## 7. Verdict

The exact ledger is

```text
null tail q in (M,2M] on every m<=M                 PROVED;
Fourier/Hadamard zero lower M^(1/2-Re rho)           PROVED;
real bank with O(M) rows and plusminus-one tails     PROVED;
tight aggregate arithmetic identity                 PROVED;
coherent zero multiplier c(rho)M^(1-rho)             PROVED;
coherent completed head = reduced Q_h prime field    PROVED;
R118 gain for the augmented composite fields         NOT AVAILABLE;
R116 primitive fixed power after modulation          NOT AVAILABLE;
fixed zero-free strip                                 NOT PROVED.        (7.1)
```

The frame idea fails fast for a precise reason, not merely because the
bank is large: its detector Parseval identity and its arithmetic Parseval
identity are the same identity.  The coherent variant avoids the arbitrary
coefficient tensor but renormalizes the missing estimate to scale `X/M`.
Any successful successor must prove cancellation **between complete
dilation coordinates beyond their tight square function**, or find a
coherent weight whose completed integral main is not an injective
smoothed copy of the prime field.  Neither property follows from the
current R116/R118 literature imports.
