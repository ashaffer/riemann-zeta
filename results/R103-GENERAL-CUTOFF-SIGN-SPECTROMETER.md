# R103 generalized-cutoff sign spectrometer

Status: exact arithmetic sign characterization of the rightmost-zero
abscissa.  The square-root sign proposed in R99 is false by R101, but the
same factorial ratios with a variable cutoff have a sharp phase transition:
the least cutoff at which their logarithm becomes nonpositive has power
exponent exactly

```text
Theta=sup_rho Re(rho).                                      (0.1)
```

Consequently, proving an eventual nonpositive sign at any one fixed cutoff
`M=N^alpha`, `alpha<1`, is equivalent in strength to proving a fixed
zero-free strip (up to choosing an exponent strictly beyond `Theta`).  The
integrality construction supplies the spectrometer, but not its missing
fixed-power bound.  No fixed strip and no failure of every fixed strip is
proved here.

Date: 2026-08-07.

## 1. The monotone cutoff family

For integers `N>=4` and `1<=M<N/2`, put

```text
H_N(M)=sum_(M<q<=N)(N-2q)Lambda(q)
      =log P_(N,M),                                      (1.1)

E_N(M)=sum_(q<=M)(N-2q)Lambda(q).                       (1.2)
```

Here `q` ranges over all integers; only prime powers contribute.  R99 and
R96 give the exact identity

```text
N R(N)=-H_N(M)-E_N(M)-N+1,                              (1.3)
```

where

```text
R(x)=sum_(n<=x)Lambda(n)(2n/x-1)-1+x^(-1).              (1.4)
```

As `M` increases below `N/2`, the high tail is nonincreasing:

```text
H_N(M+1)-H_N(M)=-(N-2M-2)Lambda(M+1)<=0.                (1.5)
```

At `M=floor(N/2)`, every remaining coefficient is nonpositive.  Hence the
integer threshold

```text
m_*(N)=min{1<=M<=floor(N/2): H_N(M)<=0}                 (1.6)
```

always exists.

## 2. Exact exponent theorem

Let

```text
Theta=sup{Re(rho): zeta(rho)=0, 0<Re(rho)<1}.           (2.1)
```

**Theorem 2.1 (cutoff-sign spectrometer).**

```text
limsup_(N->infinity) log m_*(N)/log N =Theta.           (2.2)
```

Equivalently, for every fixed `0<alpha<1`:

1. if `alpha>Theta`, then

   ```text
   H_N(floor(N^alpha))<0                                (2.3)
   ```

   for all sufficiently large `N`;

2. if `alpha<Theta`, then (2.3) fails for infinitely many `N`.

### Proof of the upper bound

Fix

```text
Theta<b<alpha<1.                                       (2.4)
```

The standard explicit-formula converse, recorded in R95--R96, gives

```text
R(N)=O_b(N^b).                                         (2.5)
```

Put `M=floor(N^alpha)`.  The ordinary prime number theorem and partial
summation give

```text
psi(M)=M+o(M),
A(M):=sum_(q<=M)q Lambda(q)=M^2/2+o(M^2).              (2.6)
```

Therefore

```text
E_N(M)=N psi(M)-2A(M)
      =NM-M^2+o(NM)+o(M^2)
      =(1+o(1))NM,                                     (2.7)
```

because `M=o(N)`.  From (2.5),

```text
N R(N)=O(N^(1+b))=o(NM).                               (2.8)
```

Substitution in (1.3) yields

```text
H_N(M)=-(1+o(1))NM<0.                                  (2.9)
```

Thus `m_*(N)<=N^(alpha+o(1))` eventually.  Letting
`alpha` decrease to `Theta` proves the upper bound in (2.2).

### Proof of the lower bound

Fix `alpha<Theta`.  There is a zeta zero with real part `beta>alpha`.
Choose

```text
alpha<a<beta.                                          (2.10)
```

The lower one-sided implication in R96 says that an eventual estimate

```text
R(x)>=-C x^a                                           (2.11)
```

would exclude every zero with real part greater than `a`.  Taking the
contrapositive, for every `C` there are arbitrarily large real `x` with

```text
R(x)<-C x^a.                                           (2.12)
```

R101 proves the uniform sampling relation

```text
R(x)-R(floor(x))=O(1).                                 (2.13)
```

Thus (2.12) also holds, after changing the constant, along arbitrarily
large integers `N`.  For `M=floor(N^alpha)`, Chebyshev's bound gives

```text
0<=E_N(M)<=N psi(M)<<N^(1+alpha).                      (2.14)
```

Choosing a fixed sufficiently large constant in (2.12), equations
(1.3), (2.10), and (2.14) imply along that integer sequence

```text
H_N(M)=-NR(N)-E_N(M)-N+1>0.                            (2.15)
```

Hence `m_*(N)>N^(alpha+o(1))` infinitely often.  Letting `alpha`
increase to `Theta` proves the lower bound in (2.2).  QED.

## 3. Exact logical consequences

**Corollary 3.1 (fixed-strip sign criterion).**  The following are
equivalent:

1. `Theta<1`;
2. there is a fixed `alpha<1` for which

   ```text
   P_(N,floor(N^alpha))<=1                              (3.1)
   ```

   eventually;
3. there is a fixed `alpha<1` such that

   ```text
   m_*(N)<=N^alpha                                      (3.2)
   ```

   eventually.

Indeed, (3.1) and (1.3), with `E_N(M)<<NM`, give

```text
R(N)>=-O(N^alpha),                                     (3.3)
```

and the R96 Landau theorem excludes zeros in `Re(s)>alpha`.  Conversely,
if `Theta<1`, choose `Theta<alpha<1` and apply Theorem 2.1.

The reverse eventual sign cannot be a substitute.  If `H_N(M)>=0`
eventually for any choice `M<N/2`, then (1.3) gives `R(N)<0` eventually;
between consecutive integers the ramp decreases.  This contradicts either
R96 applied to the upper side or the known critical-line zeros.  Thus
`P_(N,M)<1` occurs infinitely often for every such cutoff rule.

**Corollary 3.2 (RH endpoint).**

```text
RH  <=>  limsup log m_*(N)/log N=1/2.                  (3.4)
```

R101 shows why no eventual sign should be expected at the endpoint itself:

```text
H_N(floor(sqrt(N)))
 =Omega_+/- (N^(3/2)log log log N).                    (3.5)
```

The threshold consequently crosses the square-root cutoff in both
directions infinitely often, even if RH is true.

## 4. The crossing identity and the remaining arithmetic theorem

If `m_*(N)>1`, minimality in (1.6) implies that `m_*(N)` is a prime power
and that the overshoot obeys

```text
-(N-2m_*)Lambda(m_*) < H_N(m_*) <=0,
abs(H_N(m_*))<=N log N.                                  (4.1)
```

At the crossing, (1.3) becomes

```text
-R(N)
 =psi(m_*)-2A(m_*)/N+1+O(log N).                       (4.2)
```

When `m_*->infinity` and `m_*=o(N)`, the PNT turns (4.2) into

```text
-R(N)=m_*(N)(1+o(1))+O(log N).                         (4.3)
```

Thus the cutoff is not merely analogous to the negative ramp excursion;
it is its arithmetic scale, up to the smaller-scale PNT error.  This also
explains why ordinary factorial inequalities have not oriented it: an
eventual power bound for `m_*` is already exactly the desired one-sided
prime-barycenter theorem.

The useful reformulation left by this report is

```text
prove m_*(N)<=N^(1-eta) eventually for one eta>0.       (4.4)
```

It is monotone in the cutoff and expressed entirely through rational
factorial products, but Theorem 2.1 is a reality check: (4.4) is a fixed
zero-free strip, not an integrality consequence presently in hand.

