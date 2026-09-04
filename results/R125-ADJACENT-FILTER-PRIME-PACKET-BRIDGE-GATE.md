# R125 adjacent-filter prime-packet bridge gate

Status: the R123 truncated-Mobius operation, its exact free-cofactor
collapse, and its adjacent-cutoff zero-faithfulness all survive an
equation-level audit.  The unique linear combination which cancels the
collapsed balanced tail is, after normalization convenient for the
reciprocal divisor coefficient,

```text
Delta_P=P(C_(P-1)-C_P)=P^(1/2)tau_(-log P).          (0.1)
```

On the completed prime field this has direct arithmetic coefficient
`P(delta_P*Lambda)`, which is supported on `P` times prime powers.  That
looks like a prime-modulus bridge, but it is not.  The reciprocal R104/R105
interface does not use the direct coefficient `a`; it uses its divisor
kernel `c_a=mu*a`.  For the adjacent difference,

```text
c_(Delta_P)=P delta_P*(mu*Lambda)
           =-P delta_P mu log.                       (0.2)
```

After removing the common factor `P`, the reduced denominators are therefore
general squarefree integers, not primes.  The adjacent operation reproduces
the original canonical cofactor sequence at the smaller scale `X/P`.

Even an optimistic projection onto the prime-only part of that sequence
does not yield a fixed-power black-box R118 estimate.  Completing its prime
denominator gives one full Fourier coordinate; the `sqrt(B)`-block
square-function cost exactly spends R118's maximal `B^(-1/4)` gain.  The
composite part is not power-smaller and cannot be discarded.  Consequently
the proposed adjacent-filter/native-prime bridge is killed twice: first by
exact Mobius inversion, and again at the R118 norm endpoint on its prime
slice.  No fixed zero-free strip is proved or disproved.

Date: 2026-08-08.

Predecessors:

* [`R123-TRUNCATED-MOBIUS-DILATION-BANK-GATE.md`](R123-TRUNCATED-MOBIUS-DILATION-BANK-GATE.md);
* [`R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md`](R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md);
* [`R111-OUTER-PRIME-PACKET-SEPARATION-AUDIT.md`](R111-OUTER-PRIME-PACKET-SEPARATION-AUDIT.md);
* [`R118-ENDPOINT-SQUARE-FUNCTION-PRIME-AVERAGE-GATE.md`](R118-ENDPOINT-SQUARE-FUNCTION-PRIME-AVERAGE-GATE.md);
* [`R119-SPARSE-VIETA-FACTOR-FRAME-THEOREM.md`](R119-SPARSE-VIETA-FACTOR-FRAME-THEOREM.md);
  and
* [`R121-COMPOSITE-CRT-SPARSE-BRIDGE-GATE.md`](R121-COMPOSITE-CRT-SPARSE-BRIDGE-GATE.md).

## 1. Audit of the R123 collapse

Use R123's notation

```text
(tau_aF)(R)=F(R+a),

C_Y=sum_(q<=Y)mu(q)q^(-1/2)tau_(-log q),             (1.1)

f_R(t)=t^(-1/2)V_Q(R-log t),

F_(d,b)(R)=sum_(m>=1)f_R(mdb).                       (1.2)
```

The scaling identity is exactly

```text
q^(-1/2)f_(R-log q)(t)=f_R(qt).                     (1.3)
```

Therefore

```text
C_YF_(d,b)(R)
 =sum_(n>=1)[sum_(q|n;q<=Y)mu(q)]f_R(ndb).           (1.4)
```

If the original support restricts `n<=M` and `Y>=M`, every divisor of an
active `n` occurs in the bracket, giving

```text
C_YF_(d,b)=f_R(db).                                  (1.5)
```

There is no missing boundary term in this identity: a translated term with
index `q` becomes the original profile at total cofactor `qn`, so the same
support cutoff is used after reindexing.

For an arbitrary finite arithmetic field

```text
D_(a,V)(R)=sum_n a(n)n^(-1/2)V(R-log n),             (1.6)
```

the corresponding full-field identity is

```text
C_YD_(a,V)=D_(mu_<=Y*a,V).                           (1.7)
```

This confirms the important scope distinction in R123: (1.5) may be used
on a frozen Vaughan tail, but a zero detector is obtained only by applying
(1.7) to every head and boundary piece as well.

The shift span and critical triangle norm are also correct.  The largest
translation in (1.1) is `log Y`, and on a critical envelope
`abs(F(S))<=exp(S/2+o(R))`,

```text
abs(C_YF(R))
 <=exp(R/2+o(R))sum_(q<=Y)abs(mu(q))/q
 <<exp(R/2+o(R))log(2Y).                             (1.8)
```

On a zero carrier the multiplier is

```text
A_Y(s)=sum_(q<=Y)mu(q)q^(-s).                        (1.9)
```

If `P` is prime and `M<P<2M`, then

```text
A_P(s)-A_(P-1)(s)=-P^(-s),                          (1.10)

max(abs(A_(P-1)(s)),abs(A_P(s)))
 >=(1/2)P^(-Re(s))>=1/(4M),                         (1.11)
```

for `0<Re(s)<1`.  Both cutoffs are at least the integer cofactor bound
`M`, so both satisfy (1.5).  This proves R123's two-bank claim, including
its `exp[-o(R)]` lower bound when `M=exp[o(R)]`.

The audit therefore finds no defect in R123's main theorems.  It does find
one structural fact which must be exposed before trying to use both bank
members arithmetically: on the collapsed tail the two members are identical,
whereas on the completed field their difference is a shifted copy of the
whole field.  The next section makes this exact.

## 2. The adjacent pair has one tail direction and one shift direction

Let

```text
T(R)=sum_(d,b)mu(d)Lambda(b)F_(d,b)(R)               (2.1)
```

be a frozen tail for which all free cofactors satisfy `m<=M`.  With
`P>M`, (1.5) gives

```text
C_(P-1)T=C_PT
 =B(R):=sum_(d,b)mu(d)Lambda(b)f_R(db).              (2.2)
```

Hence for arbitrary scalars `u,v`,

```text
(uC_(P-1)+vC_P)T=(u+v)B.                            (2.3)
```

The two filters have rank one on the collapsed balanced tail.  If
`u+v!=0`, the original `mu(d)Lambda(b)` obstruction remains.  The unique
top-canceling direction is `v=-u`.

Composition does not create a second collapsed direction.  If both cutoffs
are at least `M`, then on every active free cofactor

```text
C_(Y_0)C_(Y_1)F_(d,b)
 =sum_(n<=M)(mu*mu*1)(n)f_R(ndb)
 =sum_(n<=M)mu(n)f_R(ndb).                           (2.4)
```

Thus a product of the adjacent filters reintroduces a Mobius-weighted free
cofactor instead of isolating either balanced factor.  Higher compositions
give further Dirichlet convolutions, not independent projections.

Since `mu(P)=-1`, the exact operator difference is

```text
C_(P-1)-C_P=P^(-1/2)tau_(-log P).                   (2.5)
```

Equation (2.5) vanishes on the frozen tail in (2.1): after (1.3), every
term has free cofactor `Pm>M`.  It does not vanish on the completed field.
By (1.7),

```text
(C_(P-1)-C_P)D_(a,V)=D_(delta_P*a,V),               (2.6)
```

where `delta_P` is the point mass at `P`.  Thus the information in the
top-canceling direction is carried by the recombined heads and by the field
at the lower physical scale, not by a second copy of (2.2).

For the reciprocal-coefficient normalization used below, put

```text
Delta_P=P(C_(P-1)-C_P)
       =P^(1/2)tau_(-log P).                         (2.7)
```

Its zero multiplier is

```text
Delta_P(s)=P^(1-s),                                  (2.8)
```

which is nonzero at every nontrivial zeta zero.  There are two distinct
normalizations here and they must not be conflated.  At physical scale `X`,
the raw excess amplitude contributed by a zero `rho=beta+i gamma` is

```text
X^(beta-1/2)abs(Delta_P(rho))
 =X^(beta-1/2)P^(1-beta),                            (2.9)
```

whereas the response of `Delta_P` on the corresponding critical-line
carrier has magnitude `P^(1/2)`.  Dividing by that critical response gives
the relative scale ratio

```text
X^(beta-1/2)P^(1-beta)/P^(1/2)
 =(X/P)^(beta-1/2).                                  (2.10)
```

Thus `Delta_P` is not a destructive zero filter.  Literally it is
`P^(1/2)` times the shifted original field; after division by the same
critical-line factor it has the original detector's off-line ratio at
effective scale

```text
B=X/P.                                               (2.11)
```

This also prevents a false conclusion from (2.2): canceling the frozen hard
tail has not made the completed arithmetic field easy; it has moved the
full difficulty to scale `B`.

## 3. Direct support is not reciprocal-denominator support

The tempting bridge fails at a precise Mobius-inversion step.  For any
finite arithmetic coefficient `a`, put

```text
c_a=mu*a.                                            (3.1)
```

Since `1*c_a=a`, the exact R104 divisor expansion is

```text
D_(a,V)(R)
 =sum_q c_a(q)sum_(m>=1)f_R(qm).                    (3.2)
```

It is `c_a(q)/q`, not `a(q)/q`, which becomes the reciprocal Poisson
coefficient.  For the original prime field,

```text
c_Lambda=mu*Lambda=-mu log.                          (3.3)
```

Apply the normalized adjacent difference (2.7).  Its direct arithmetic
coefficient is indeed

```text
a_P(n)=P(delta_P*Lambda)(n)
      =P Lambda(b)                    if n=Pb.        (3.4)
```

Thus the direct samples are `P` times prime powers.  But their divisor
kernel is

```text
c_(a_P)
 =mu*a_P
 =P delta_P*(mu*Lambda)
 =-P delta_P mu log.                                 (3.5)
```

Consequently the exact reciprocal expansion is

```text
Delta_PD_(Lambda,V)
 =P sum_d[-mu(d)log d]sum_(m>=1)f_R(Pdm).            (3.6)
```

At physical scale `Pdm asymp X`, put `B=X/P`.  After Poisson summation the
cofactor attached to `q=Pd` is

```text
h_P(Pd)=P[-mu(d)log d]/(Pd)
       =-mu(d)log d/d.                               (3.7)
```

This is exactly the canonical cofactor sequence at scale `B`; `P` has
become only a common dilation.  Squaring one fixed `Delta_P` field gives

```text
q_1=Pr,       q_2=Ps,
gcd(q_1,q_2)=P gcd(r,s),                             (3.8)
```

and for the generic coprime pair the R105 form is

```text
integral_t sum_((r,s)=1,k)
 [-mu(r)log(r)r^(-1-it)]
 [-mu(s)log(s)s^(-1+it)]
 nu_(P,t)(k)e_r(k inverse(s))dt.                    (3.9)
```

The reduced denominators `r,s asymp B` are arbitrary squarefree integers.
In particular, the substantial balanced-semiprime family from R105 remains.
The adjacent difference has reduced the physical scale from `X` to `B`, in
exact agreement with the critical-normalized zero-carrier ratio (2.10), but it has not changed
the reciprocal arithmetic type.

This correction is essential.  Reading (3.4) directly as a prime
denominator coefficient would interchange an arithmetic sample with its
Mobius-inverted divisor kernel.  R104 (3.6) shows that those are different
objects.

There is also no help from averaging several adjacent primes `P`.  If
different `P` fields are summed before squaring, generic cross terms have
common gcd one and return the composite R121 interface.  If they are kept
in a square-function, each diagonal is simply another copy of (3.9) at its
corresponding scale.

Iteration is equally rigid.  For `D=product_(i=1)^t P_i`, composition of
the normalized adjacent differences gives

```text
Delta_(P_1)...Delta_(P_t)D_(Lambda,V)
 =D D_(delta_D*Lambda,V),                            (3.10)

c_iterated=D delta_D*(mu*Lambda).                    (3.11)
```

After the common dilation `D` is removed, the reciprocal coefficient is
again `-mu(d)log(d)/d`.  Thus no finite adjacent-filter bank peels a prime
factor from the canonical reduced denominator; it only moves the same
problem to scale `X/D`.

## 4. Optimistic prime-only projection

Although (3.9) is not prime-supported, retain only its slice `r,s` prime to
give R118 the most favorable possible test.  This slice is not a
power-complete replacement for (3.9), but it does produce a literal prime
modulus.

After a fixed finite subdivision, take the `s` interval to have length less
than `B<=r`; its residues are then injective.  Fix the outer prime
`r asymp B` in that slice and put, suppressing harmless smooth weights,

```text
beta_s=Lambda(s)s^(-1+it)1_(s asymp B).              (4.1)
```

Extend `beta` by zero modulo `r` and define

```text
betahat_r(h)=sum_s beta_s e_r(-hs).                  (4.2)
```

Fourier inversion gives the exact formula

```text
sum_s beta_s e_r(k inverse(s))
 =r^(-1)sum_(h mod r)betahat_r(h)S(h,k;r),           (4.3)
```

up to the one nonunit term `s=r`, which is a diagonal/ramified term and is
elementary.  Thus the prime-only slice really reaches a prime-modulus bilinear
Kloosterman-sum form.

It does not reach the **short-support** form assumed by the BP/R118 trace.
The Fourier coordinate `h` in (4.3) occupies the whole residue system.
Parseval is exact:

```text
sum_(h mod r)abs(betahat_r(h))^2
 =r sum_s abs(beta_s)^2
 asymp log B.                                        (4.4)
```

More precisely, the PNT gives

```text
sum_(s asymp B)abs(Lambda(s)/s)^2
 asymp log B/B.                                      (4.5)
```

There is no power-sized norm gain hidden in prime support:

```text
sum_(s prime asymp B)Lambda(s)/s asymp 1,

sqrt(pi(2B)-pi(B))
 [sum_(s prime asymp B)abs(Lambda(s)/s)^2]^(1/2)
 =B^o(1).                                            (4.6)
```

Consequently passing the prime coefficient through an outer `l^2` norm
recovers its direct `l^1` scale, up to logarithms.

The projection cannot dispose of the complement.  Standard squarefree
mean values give

```text
sum_(d asymp B)abs(mu(d)log(d)/d)^2
 asymp log^2(B)/B,                                   (4.7)

sum_(p prime asymp B)abs(log(p)/p)^2
 asymp log(B)/B.                                     (4.8)
```

Thus the prime slice is only a logarithmic fraction of the canonical
cofactor energy.  The composite squarefree slice is not smaller by a fixed
power; unfolding it as `mu*Lambda` returns the balanced R105/R121 packet.

The other full coordinate is also genuine.  In the R111 line amplitude

```text
A_(g,r,s,theta)(j)
 =g integral L_Q(u+gj,u)e(theta u/(grs))du,          (4.9)
```

put `g=P`, `r,s asymp B`, and `u asymp X=PB`.  The
physical support and fixed-ratio phase give

```text
abs(j)<<B,          abs(theta)<<B,                   (4.10)
```

with natural-size subboxes at `j,theta asymp B`.  Hence `k=j theta`, after
reduction modulo `r`, is not confined to one square-root interval.  The
zero marginal requires recombining these shells before an absolute value;
it does not shorten the full residue support in (4.3).

## 5. Sharp R118 exponent obstruction

For a prime modulus `r asymp B`, write

```text
H=sqrt(B).                                           (5.1)
```

R118's native BP packets have two additive input intervals of length `H`.
At a multiplier transition of length `L=H`, its strongest relative saving
is

```text
L^(-1/2)=H^(-1/2)=B^(-1/4).                         (5.2)
```

The full coordinate `h mod r` in (4.3) needs

```text
B/H=H                                                (5.3)
```

critical short intervals.  Even granting that the entire `k` coordinate,
all endpoints, all central terms, and every common-profile separation cost
nothing, coefficient-uniform square-function recombination over (5.3)
costs

```text
sqrt(H)=H^(1/2)=B^(1/4).                             (5.4)
```

Equations (5.2) and (5.4) cancel exactly.  There is no fixed reserve.

This is the favorable one-full-coordinate ledger.  In the actual form,
the `k` coordinate also ranges over `B` residues.  Splitting both coordinates
creates `H^2=B` short-box pairs; their ordinary square-function cost is

```text
sqrt(H^2)=H=B^(1/2).                                 (5.5)
```

After the R118 gain (5.2), the method is worse than direct by
`B^(1/4)`.  R119's fixed-prime gain `B^(-1/24+epsilon)` is smaller and
therefore cannot repair either ledger.

The equality in the favorable ledger is not an artifact of using triangle
inequality.  R118 Sections 2--3 give coherent-array examples showing that
an independent block/endpoint coordinate has exactly its diagonal physical
volume.  Treating the `H` full-support blocks as an arbitrary Hilbert
coordinate recreates that counterexample.  Parseval (4.4) controls the
sum of block energies, but R118 supplies no bound for their projective
`l^1(l^2)` recombination better than (5.4).

The exact missing estimate can therefore be stated cleanly.  One would need
a coefficient-specific theorem such as

```text
sum_(h-blocks J)norm(betahat_r 1_J)_2
 <<B^(1/4-delta)
   [sum_h abs(betahat_r(h))^2]^(1/2),                (5.6)
```

uniformly through the outer prime and profile family, or a global R118
square-function theorem which bypasses this projective norm.  Cauchy gives
(5.6) only with `delta=0`.  Neither adjacent filtering nor prime support of
`Lambda` proves a positive `delta`.

## 6. No alternative prime-factor scale fixes the ledger

Return first to the actual collapsed balanced block

```text
sum_(d asymp N,b asymp N)mu(d)Lambda(b)f_R(db),
N=sqrt(X).                                           (6.1)
```

Discarding prime powers makes the `Lambda` variable `b=p` prime up to a
power-smaller absolute error, but the reciprocal denominator is still the
product `dp`.  Since `d asymp N`, exposing `p` by CRT leaves a complementary
factor of the same size.  On the slice where `d` is also prime, R121's sharp
Hilbert ledger costs `sqrt(d)`, exactly canceling the full prime
inverse-matrix saving `sqrt(p)`.  That slice is smaller only by logarithms,
not by a fixed power; general squarefree `d` retains the analogous
multi-factor CRT coupling.  Thus decomposing the `Lambda` factor into primes
does not turn the **product modulus** into a prime modulus or control the
remaining squarefree coefficients.

The same obstruction can be written without specializing the exposed prime
to the full balanced size.  Suppose a prime `q<=N` is extracted from one
factor of an original balanced block of length `N`.  The local R118 length
is `sqrt(q)`, while at least one other coordinate still has length `N`.
It therefore needs

```text
J=N/sqrt(q)                                          (6.2)
```

short boxes.  Combining the most favorable one-coordinate square-function
cost with the maximal local R118 gain gives

```text
J^(1/2) q^(-1/4)
 =N^(1/2)q^(-1/2)
 =(N/q)^(1/2)>=1.                                   (6.3)
```

Equality occurs only at the largest possible prime `q asymp N`; every
smaller prime factor loses a fixed power relative to that endpoint.  With
two full coordinates the loss is larger.

This calculation concerns only an additional, explicit prime-factor
projection.  The actual adjacent difference has already failed earlier at
(3.5): its reduced cofactor `d` is general squarefree.  It nevertheless
shows that forcing a prime slice by hand does not rescue the R118 import.

This covers both tempting alternatives.

1. The R123 adjacent prime `P asymp M=X^o(1)` is far too small to serve as
   a critical local modulus for an `N=X^(1/2)` balanced coordinate.  Even a
   hypothetical power of `P` is only `X^(-o(1))`.
2. Decomposing `Lambda(b)` into primes `b asymp N` reaches the equality case
   of (6.3), but not a strict saving.  Decomposing `mu(d)` as `d=qu` leaves
   the other balanced `b` coordinate of length `N`, so the same calculation
   applies.

There is also an algebraic warning about using the dilation prime itself.
In (2.6), `P` is a factor of every integer selected by `delta_P*a`.  If it
is simultaneously declared to be the reciprocal modulus, that integer is
nonunit modulo `P`; the term belongs to a ramified/common-gcd stratum, not
to the primitive BP character row.  A valid prime modulus appears only
after the additional prime-only projection of Section 4, and that projection
leads to the full-support completion (4.3) while omitting a
power-substantial composite part.

## 7. Disposition

The audited and new ledgers are

```text
R123 scaling and divisor collapse                    EXACT;
R123 full-field convolution                          EXACT;
adjacent two-member zero lower bound                 EXACT / SUBPOWER;
two adjacent filters on collapsed tail               RANK ONE;
unique top-canceling direction                       SINGLE DILATION;
reciprocal-normalized difference                     ZERO-FAITHFUL;
reciprocal-normalized coefficient                    P(delta_P*Lambda);
reciprocal divisor kernel after that normalization   P delta_P*(mu*Lambda);
common-P reduced denominators                        GENERAL SQUAREFREE;
iterated adjacent differences                        SAME REDUCED KERNEL;
prime-only projected Kloosterman completion          EXACT / INCOMPLETE SLICE;
prime-slice completed coefficient support            FULL MOD r;
one-coordinate short-box recombination               EXACTLY SPENDS R118;
actual two-coordinate recombination                  WORSE THAN DIRECT;
adjacent-filter-to-native-R118 bridge                 FAILS BEFORE PACKET;
new full-support prime square-function theorem        OPEN;
fixed zero-free strip                                NOT PROVED;
nonexistence of a fixed zero-free strip              NOT PROVED.          (7.1)
```

The adjacent pair remains a useful scale-recursion identity, but it does
not change the canonical reciprocal coefficient: after the common factor
`P` is removed, the sequence is again `-mu(d)log(d)/d`.  There are therefore
two genuinely new inputs which could advance this branch.  One is a
coefficient-specific theorem that suppresses the composite part of (3.9)
by a fixed power.  The other is a completion-preserving square-function
estimate for the optimistic prime form (4.3) across all `sqrt(B)` Fourier
blocks with a strict `B^(-delta)` improvement over (5.4).  Neither follows
from the adjacent filter or from packetwise R118.
