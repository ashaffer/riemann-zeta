# R121 composite-CRT sparse-bridge gate

Status: the exact balanced-semiprime CRT factorization has been carried
through both the R105 full-completion formula and the signed R116 primitive
packet.  It does not produce an R118/R119 prime packet with a harmless
Hilbert-valued complementary coordinate.  At the coefficient-uniform level,
retaining the complementary inverse matrix costs its sharp Hilbert
factorization norm `asymp sqrt(r)`; this exactly cancels the `sqrt(p)`
operator saving available from the first prime when `p asymp r`.  More
decisively, the signed primitive packet has the exact local factor

```text
H_p=p e_p(-inverse(r) m n z)+1.                       (0.1)
```

The first term is a one-prime diagonal.  Applying the complementary prime
turns it into

```text
c e_c(-m n z),             c=pr,                     (0.2)
```

which is exactly the smooth ordinary `mu(d)Lambda(b)` Type-II term of R116,
and after Vaughan recompletion the logarithmically weighted Mertens carrier.
Thus the new sparse `(P,x,y)` theorem controls genuine prime-modulus
short-box packets and the CRT off-diagonal, but it cannot by itself cross
the composite primitive diagonal.  A completion-preserving fixed power now
has to use cancellation in the globally recombined Mobius term.  No fixed
zero-free strip, and no theorem that such a strip cannot exist, is proved
here.

Date: 2026-08-07.

Predecessors:

* [`R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md`](R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md),
  especially Sections 5--6;
* [`R111-OUTER-PRIME-PACKET-SEPARATION-AUDIT.md`](R111-OUTER-PRIME-PACKET-SEPARATION-AUDIT.md),
  Sections 9--10;
* [`R116-SIGNED-JOINT-TYPEII-ATTACK.md`](R116-SIGNED-JOINT-TYPEII-ATTACK.md),
  for the signed conductor theorem and primitive dual;
* [`R118-ENDPOINT-SQUARE-FUNCTION-PRIME-AVERAGE-GATE.md`](R118-ENDPOINT-SQUARE-FUNCTION-PRIME-AVERAGE-GATE.md);
  and
* [`R119-SPARSE-VIETA-FACTOR-FRAME-THEOREM.md`](R119-SPARSE-VIETA-FACTOR-FRAME-THEOREM.md).

## 1. Verdict and notation

Let

```text
c=pr,                 p!=r,          p,r asymp N,
N=sqrt(c),                                              (1.1)
```

with `p,r` prime.  On the square-root Vaughan box, `d,b asymp N`, and the
actual coefficients, including an arbitrary bounded Mellin frequency, are

```text
alpha_d=mu(d)d^(-1-it),
beta_b=Lambda(b)b^(-1-it).                            (1.2)
```

Smooth fixed-ratio factors may be separated exactly as in R116 Corollary
3.2; they only add unimodular powers to (1.2) and an absolutely summable
profile index.

The `g=1` inverse-product slice of R105 is

```text
F_c(k)=sum_(d,b;(db,c)=1)
 alpha_d beta_b e_c(k inverse(db)).                   (1.3)
```

Only `a=k mod c` matters.  If `(a,c)>1`, its reduced additive conductor is
`1,p`, or `r`, and R116 Corollary 4.1 already gives total cost
`c^(1/2+epsilon)` for all such classes after the complete signed `Q_h`
profile is recombined.  The only possible top obstruction is therefore

```text
(a,c)=1.                                             (1.4)
```

The magnitude of the integer representative `k=j theta`, including the top
range `abs(k)asymp c^2`, has no effect on the CRT identities below.  What is
essential is that all `j,theta` shells giving the residue `a` remain inside
the signed hyperbola fold.  No absolute value in the shell parameter is
taken.

There are two separate reasons the proposed bridge stops.

1. Before the signed multiplier sum, the complementary CRT phase is a
   genuinely two-variable inverse matrix.  Treating it as a Hilbert-valued
   coefficient has a sharp `sqrt(r)` cost, not a subpower cost.
2. After the signed multiplier sum, its primitive diagonal is the ordinary
   smooth Mobius--von Mangoldt product.  The first-prime average leaves that
   diagonal intact.

The second statement is an exact identification of the surviving term, not
merely a failure of one inequality.

## 2. Exact CRT factorization of the R105 completion

Write

```text
rbar=inverse(r) mod p,       pbar=inverse(p) mod r.   (2.1)
```

For every integer `u`, CRT gives

```text
e_c(u)=e_p(rbar u)e_r(pbar u).                       (2.2)
```

Consequently, on units,

```text
e_c(k inverse(db))
 =e_p(rbar k inverse(d)inverse(b))
  e_r(pbar k inverse(d)inverse(b)).                  (2.3)
```

This is a product of two inverse-product matrices.  The second factor is
not a product of one function of `d` and one function of `b`.

The same issue is visible in R105's exact full-completion formula.  With

```text
alphahat_c(h)=sum_d alpha_d e_c(-hd),

betatilde_c(n)=beta_(inverse(n))
  1_(inverse(n) in I_b),                             (2.4)
```

one has

```text
F_c(k)=c^(-1)sum_(h,n mod c)
 alphahat_c(h)betatilde_c(n)S_c(kh,n;c).             (2.5)
```

If `h=(h_p,h_r)` and `n=(n_p,n_r)` under CRT, then exactly

```text
S_c(kh,n;c)
 =S_p(rbar k h_p,rbar n_p;p)
  S_r(pbar k h_r,pbar n_r;r),                        (2.6)

alphahat_c(h_p,h_r)
 =sum_d alpha_d
   e_p(-rbar h_p d)e_r(-pbar h_r d).                 (2.7)
```

Moreover, `betatilde_c` is supported on the CRT inverse curve

```text
(n_p,n_r)=(inverse(b) mod p,inverse(b) mod r),
b in I_b.                                            (2.8)
```

Thus, if the `r` coordinates are retained and the `p` coordinates are
exposed, the coefficient seen by the `p`-Kloosterman matrix is

```text
G_p(h_p,n_p)
 =sum_(h_r,n_r)
   alphahat_c(h_p,h_r)betatilde_c(n_p,n_r)
   S_r(pbar k h_r,pbar n_r;r).                       (2.9)
```

It is a matrix coefficient in `(h_p,n_p)`, not a separated pair of input
sequences.  Equations (2.7)--(2.8) also show that it is not a common
coefficient array as `p` varies: the complementary CRT phase and the
companion prime `r` vary with the row.

This is not the coefficient in R118.  The latter is built from four common
short-box autocorrelations and has the sparse identity

```text
P=h_1h_2h_3h_4,       x=h_1+h_3,
y=h_2+h_4,            Q=xy.                          (2.10)
```

No such four-profile factorization is present in (2.9).  One can create it
only after splitting both full `p`-residue coordinates into genuine
Blomer--Pascadi short boxes.  For local modulus `p`, their critical length
is

```text
H_0=sqrt(p).                                         (2.11)
```

But the projections of (2.7)--(2.8) have length `asymp p`, so each input
requires `asymp sqrt(p)` short intervals and there are `asymp p` box pairs.
The square-root recombination cost for arbitrary box coefficients is
`p^(1/2)`, already larger than R118's `p^(-1/4)` transition gain.  In
addition, the primitive residues `a mod p` fill `F_p^*`; partitioning them
into R118 blocks of length `H_0` produces `sqrt(p)` multiplier blocks, whose
best plain square-function cost `p^(1/4)` exactly spends that gain.

These block ledgers do not prove that a coefficient-specific global
recombination is impossible.  They do prove that (2.5) is not directly an
R118 packet with subpower projective cost.

## 3. Sharp Hilbert cost of retaining the complementary prime

The obstruction in (2.3) can be quantified without a block partition.  For
an odd prime `q` and `kappa!=0 mod q`, let

```text
U_q(u,v)=e_q(kappa inverse(u)inverse(v)),
u,v in F_q^*.                                        (3.1)
```

Inverting the row and column labels turns `U_q` into the matrix
`e_q(kappa uv)`.  Its Gram matrix is

```text
U_q U_q^*=q I-J.                                     (3.2)
```

Hence its singular values are

```text
sqrt(q), with multiplicity q-2,       and 1 once,    (3.3)
```

and in particular

```text
norm(U_q)_op=sqrt(q).                                (3.4)
```

There is also a sharp statement for the proposed Hilbert retention.  Define

```text
gamma_2(U_q)=inf
 [max_u norm(xi_u) max_v norm(eta_v)],               (3.5)
```

where the infimum is over all Hilbert factorizations
`U_q(u,v)=<xi_u,eta_v>`.  Since

```text
norm(U_q)_*=1+(q-2)sqrt(q),                          (3.6)
```

and any such factorization satisfies

```text
norm(U_q)_*
 <=(sum_u norm(xi_u)^2)^(1/2)
   (sum_v norm(eta_v)^2)^(1/2)
 <=(q-1) max_u norm(xi_u) max_v norm(eta_v),         (3.7)
```

one gets the lower bound `gamma_2(U_q)>>sqrt(q)`.  Conversely, taking a
scaled row factorization gives `gamma_2(U_q)<<sqrt(q)`.  Therefore

```text
gamma_2(U_q)asymp sqrt(q).                           (3.8)
```

Now retain the `r` factor of (2.3) as an inner product and apply the
Hilbert-valued extension of the `p` inverse-matrix operator bound.  Even in
the most favorable complete-residue model, its coefficient-uniform constant
is

```text
norm(U_p)_op gamma_2(U_r)
 asymp sqrt(p)sqrt(r)=sqrt(c).                       (3.9)
```

For two coefficient intervals of lengths `asymp N`, direct Cauchy gives

```text
sum_(d,b)abs(alpha_d beta_b)
 <=N norm(alpha)_2 norm(beta)_2
 =sqrt(c)norm(alpha)_2 norm(beta)_2.                 (3.10)
```

Thus (3.9) is exactly the direct scale.  The complementary factor is not an
extra sparse coordinate of subpower norm.  Its sharp Hilbert norm consumes
the entire first-prime operator saving at `p asymp r`.

This is a no-go theorem for the proposed **coefficient-uniform Hilbert
factorization**.  It is not a no-go theorem for every joint arithmetic
estimate using the special signs of `mu` and `Lambda`.  The next section
shows exactly what those signs would have to cancel.

## 4. Exact one-prime primitive diagonal

The signed packet makes the surviving obstruction completely explicit.
Let `W` be the exact recombined R116 profile.  Its two-dimensional Fourier
transform satisfies

```text
What(0,n)=0,                                         (4.1)
```

and `n` lies in a fixed finite subset of the nonzero integers.  The first
frequency `m` decays faster than any prescribed fixed power.  Put

```text
gamma_c(z)=sum_(db=z mod c)alpha_d beta_b,            (4.2)

F_c(a)=sum_z^* gamma_c(z)e_c(a inverse(z)),

V_c(a)=sum_(m,n)What(m,n)S_c(m,na;c).                (4.3)
```

For a prime `q` and units `lambda,n,z mod q`, define

```text
H_q^(lambda)(m,n;z)
 =sum_x^* e_q(lambda m x)
   sum_a^* e_q(lambda a[inverse(z)+n inverse(x)]).   (4.4)
```

### Lemma 4.1 (exact local primitive factor)

For every prime `q` and units `lambda,n,z`, one has

```text
H_q^(lambda)(m,n;z)
 =q e_q(-lambda m n z)-c_q(m),                       (4.5)
```

where `c_q(m)` is the Ramanujan sum.  In particular, if `q` does not divide
`m`,

```text
H_q^(lambda)(m,n;z)
 =q e_q(-lambda m n z)+1.                            (4.6)
```

#### Proof

The inner sum in (4.4) is

```text
q 1_(inverse(z)+n inverse(x)=0)-1.                   (4.7)
```

There is one solution, `x=-nz`.  Substitution into the first term of
(4.7), followed by summation of the second term over `x`, gives (4.5).
QED.

Take `lambda=rbar` at `p` and `lambda=pbar` at `r`.  CRT factors the inner
sum in R116 Theorem 5.1, denoted there by `H_c`, as

```text
H_c(m,n;z)
 =H_p^(rbar)(m,n;z)H_r^(pbar)(m,n;z).                (4.8)
```

On the main frequency range `(m,pr)=1`, Lemma 4.1 gives the exact
identity

```text
H_c(m,n;z)
 =[p e_p(-rbar m n z)+1]
  [r e_r(-pbar m n z)+1]

 =c e_c(-m n z)
  +p e_p(-rbar m n z)
  +r e_r(-pbar m n z)+1.                             (4.9)
```

The tails where `p|m` or `r|m` are power-small after (4.1) and the rapid
decay in `m`, exactly as in R116.  Equation (4.9) otherwise has no error.

The requested one-prime averaging is visible by stopping after the first
factor:

```text
H_c
 =p e_p(-rbar m n z)H_r^(pbar)(m,n;z)
   +H_r^(pbar)(m,n;z).                               (4.10)
```

The first summand is the `p`-diagonal.  The `p` Kloosterman variable has
already been forced to `x=-nz`; it is not a noncentral Vieta row to which
R118 or R119 applies.  Keeping the second prime as a Hilbert coordinate
does not shrink it.  Its own diagonal multiplies the phase to

```text
e_p(-rbar m n z)e_r(-pbar m n z)=e_c(-m n z),        (4.11)
```

which is slowly varying when `z=db asymp c` and `m,n` are fixed physical
frequencies.

After summing (4.9) against `gamma_c(z)What(m,n)`, the three proper local
terms have total size

```text
<<(p+r)c^epsilon norm(gamma_c)_1
 <<c^(1/2+epsilon)norm(gamma_c)_1,                   (4.12)
```

while the joint diagonal is exactly

```text
c sum_z^* gamma_c(z)Phi_c(z/c),

Phi_c(x)=sum_(m,n)What(m,n)e(-mnx).                  (4.13)
```

This recovers R116's primitive duality with a stronger interpretation: its
main term is the repeated one-prime diagonal that any CRT prime average has
to retain.

## 5. Actual Vaughan coefficients, profiles, and nonunits

Substitution of (1.2) into (4.13) gives

```text
M_c(t)=c sum_(d,b;(db,c)=1)
 mu(d)Lambda(b)/(db)^(1+it) Phi_c(db/c).             (5.1)
```

All actual phases have been retained:

* the top `k=j theta` range was recombined before (4.3);
* the signed `Q_h` translates are what give (4.1);
* a fixed-ratio dependence of `W` gives an absolutely summable family of
  formulas (5.1), with only unimodular changes to (1.2); and
* the Mellin factor `(db)^(-it)` remains inside the ordinary Type-II sum.

The unit restriction creates no hidden top term on the balanced box.  Each
length-`O(N)` interval contains only `O(1)` multiples of `p` or `r`.  Hence
there are `O(N)` pairs with `(db,c)>1`, compared with `asymp N^2` unit
pairs.  For the normalized coefficients (1.2), their total absolute mass is

```text
<<N^(-1+epsilon)=c^(-1/2+epsilon).                   (5.2)
```

In the original R105 gcd decomposition these pairs belong to `g>1`
sectors, rather than to the primitive inverse in (1.3).  Equation (5.2)
becomes at most `c^(1/2+epsilon)` after the leading factor `c` in (5.1),
so restoring or removing them cannot cancel the natural-size unit
diagonal.  This statement is restricted to balanced squarefree semiprimes;
nonsquarefree tail moduli still require the Type-I/Vaughan recompletion
specified in R116.

At bounded `t`, PNT summation in `b` changes (5.1) into

```text
M_c(t)
 =c sum_(d asymp N)mu(d)d^(-1-it)G_(c,t)(d/N)
  +c exp[-(log c)^(3/5-o(1))].                       (5.3)
```

When the Vaughan heads are restored before estimation, the exact identity

```text
(mu*Lambda)(n)=-mu(n)log n                           (5.4)
```

turns the same diagonal into

```text
-c sum_n mu(n)log(n)n^(-1-it)Phi_c(n/c).             (5.5)
```

Thus there are only two possible outcomes of the CRT treatment.

* If the `r` factor is treated coefficient-uniformly as a Hilbert vector,
  the sharp factorization cost (3.8) returns the direct bound.
* If the two CRT factors are recombined coefficient-specifically, their
  primitive diagonals give (5.1)--(5.5).  A fixed power then requires new
  Mobius cancellation of fixed-strip strength.

No finite-field sparse-frame estimate distinguishes these alternatives,
because the Vieta character row has disappeared on the diagonal before the
coefficient signs are used.

## 6. Simultaneous two-prime averaging is a low-frequency cluster

One might try to avoid the one-factor obstruction by summing both `p` and
`r` before Cauchy.  The diagonal in (4.13) shows sharply why this is not a
large-sieve problem at fixed power.

Put `X=N^2`.  For one Fourier mode `a=mn!=0`, the frequency acting on the
long product variable `z` is

```text
xi_(p,r)=a/(pr),             p,r asymp N.             (6.1)
```

The physical `z` interval has length `asymp X`, so its Fourier resolution
is `X^(-1)`.  But

```text
diam{xi_(p,r):p,r asymp N}<<abs(a)/X.                (6.2)
```

Thus, for fixed `a`, all semiprime rows occupy only `O(abs(a)+1)` Fourier
resolution cells.  More quantitatively, if `mathcal C_X` is the set of
balanced semiprimes in one fixed-ratio box, pigeonholing intervals of
length `X^(-1)` gives

```text
max_J #{c in mathcal C_X:a/c in J}
 >>#mathcal C_X/(abs(a)+1).                          (6.3)
```

Rows whose frequencies lie in one such cell have pairwise inner products
of order `X` after restricting `z` to a suitable fixed-proportion
subinterval.  Hence a coefficient-uniform additive large sieve for these
rows must retain the local multiplicity in (6.3).  For a fixed nonzero
mode it is `#mathcal C_X=X^(1-o(1))`, not a subpower quantity.

The rapid `m` decay permits truncation at `abs(m)<=X^epsilon` with a
power-small error; `n` has fixed support.  Consequently all effective
frequencies together occupy only `X^epsilon` resolution cells.  This is a
low-rank family, but low rank here means coherence, not cancellation.  The
separate labels `(p,r)` do not create two independent frequencies because
the phase depends on them only through the product `pr`.

The same fact can be stated without Fourier cells.  On normalized compact
variables

```text
u=p/N,       v=r/N,       w=z/X,                     (6.4)
```

the phase is `e(-a w/(uv))`, with no large parameter.  Standard smooth
tensor approximation, together with the fixed-ratio profile separation of
R116, writes the full diagonal kernel to error `X^(-A)` as an
`X^epsilon`-projective sum of products of one-variable smooth functions of
`p,r,d,b`.  It supplies separation, not an oscillatory saving.

There is an especially direct reality check on the substantial semiprime
subfamily from R105.  If `c=pr` with both primes beyond the Vaughan cutoffs,
then

```text
a_(U,V)(pr)=-log(pr),       h(pr)pr=-log(pr).         (6.5)
```

The outer `(p,r)` weight therefore has one sign and rank two in `log p,
log r`; it does not cancel the clustered diagonal.  Smooth PNT summation in
`b` and smooth separation of the remaining ratios leave precisely a family
of sums

```text
sum_(d asymp N)mu(d)d^(-1-it)G(d/N).                 (6.6)
```

After squaring, these are scale-stable Mertens autocorrelations.  Therefore
the simultaneous two-factor transform does not convert (4.13) into a
sparse `(p,r,z)` large sieve with a fixed reserve.  It converts it into a
subpower-rank average of the same smooth Mertens detectors.

This conclusion is sharp for the proposed transform: arbitrary
coefficients can align on the coherent cell in (6.3), while the actual
coefficients leave `mu(d)` as the only unexploited fixed-power source.  A
new theorem about those signs could still win; frequency separation of the
semiprime rows cannot.

## 7. Consequence for the outer semiprime average

Let `h(c)` be the exact outer R105/Vaughan coefficient.  Proper conductors
and the CRT cross terms may be discarded at their proved
`c^(1/2+epsilon)` scale.  The remaining outer target is therefore, jointly
with the Vaughan heads,

```text
sum_(c asymp X)h(c)c
 sum_(d,b)mu(d)Lambda(b)/(db)^(1+it)Phi_c(db/c).      (7.1)
```

This is R116 (10.2).  Averaging `p` while retaining `r` does not turn its
main term into a long-coordinate nonzero-frequency large-sieve row: on the
CRT diagonal the two apparently rapid local phases combine by (4.11) into
the fixed-scale phase `e(-mn db/c)`.  Squaring before the outer `c` sum
removes the Mobius signs and preserves the physical diagonal.

A fixed power for (7.1) remains a legitimate possible new theorem.  It
would have to exploit the signed outer coefficient, the primitive ordinary
product term, the Type-I heads, and the fixed-ratio profile family before
any Cauchy step.  Failure of the present CRT/Hilbert bridge does not show
that such cancellation is false.

## 8. Final ledger

```text
R105 full-completion CRT factorization                 EXACT;
complementary prime as scalar outer weight             FALSE;
complementary prime Hilbert factorization cost          sqrt(r), SHARP;
first-prime full inverse operator norm                   sqrt(p);
balanced combined coefficient-uniform scale             sqrt(pr), DIRECT;
R118/R119 packet after full-support partition            FIXED-POWER COST;
proper multiplier conductors                             POWER-SAVED;
nonunit d,b strata on balanced squarefree box            LOWER-DIMENSIONAL;
one-prime primitive diagonal                             EXACT, (4.6);
two-prime primitive diagonal                             ORDINARY mu-Lambda;
simultaneous (p,r,z) frequency family                    X^o(1) CELLS / COHERENT;
completion-preserving CRT sparse bridge                  KILLED;
global signed Mobius diagonal cancellation               OPEN;
fixed zero-free strip                                    NOT PROVED;
nonexistence of a fixed zero-free strip                  NOT PROVED.       (8.1)
```

The useful conclusion is narrow but definitive: the local sparse Vieta
theorems are no longer the missing estimate on the balanced semiprime
primitive block.  The obstruction is the exact CRT diagonal (4.9), and the
next attack should begin from the globally recombined ordinary Mobius form
(7.1), not from another short-box partition of (2.5).
