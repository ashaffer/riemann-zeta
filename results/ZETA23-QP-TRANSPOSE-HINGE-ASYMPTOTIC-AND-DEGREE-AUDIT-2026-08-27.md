# Transpose-hinge asymptotic and resonance-degree audit (2026-08-27)

## Binary conclusions

1. The persistent hinge correlations have an explicit asymptotic.  They
   come from common multiples of two rational linear periods; the
   quadratic reciprocal phase then supplies a nonzero limiting integral.
2. There is no independent carrier congruence.  It is automatically
   satisfied whenever the two linear frequencies are integral.
3. Literal divisor-bounded partner degree is false: one fixed packet pair
   has `Theta(F)` principal-resonant hinge partners in the critical tower.
4. Bounded-period (hence constant-size limiting-correlation) partners are
   divisor-bounded.  For a central lane `b=F`, the full resonance-density
   weighted degree is also `F^o(1)`.

These statements concern the exact all-integer balanced-tower model.  They
do not prove the global masked packet theorem.

## 1. Phase expansion at the actual top scale

Write `e(x)=exp(2 pi i x)`, `Q=q^3/8=F^3 R^3`, and

```text
G_(a,b)(h)=sum_(0<=n,n'<F)
 e(h Q/((aR-n)(b(R+1)-n'))).
```

Fix positive rational lane ratios `alpha,beta` and pass through integers
`F` for which `a=alpha F`, `b=beta F` are integral.  Put `x=n/F`, `y=n'/F`.
Uniformly for `n,n'<F`,

```text
Q/((aR-n)(b(R+1)-n'))
 = C_(alpha,beta) + lambda_(alpha,beta)n
   + mu_(alpha,beta)n'
   + F/(alpha beta R) V_(alpha,beta)(x,y)
   + O(F/R^2),                                      (1.1)

C_(alpha,beta)=F(R-1)/(alpha beta),
lambda_(alpha,beta)=1/(alpha^2 beta)=F^3/(a^2b),
mu_(alpha,beta)=1/(alpha beta^2)=F^3/(ab^2),

V_(alpha,beta)(x,y)
 =(x/alpha)^2-(x/alpha)(1-y/beta)+(1-y/beta)^2.
```

Indeed, with `U=n/a` and `V=1-n'/b`, the two reciprocal factors give

```text
(1-U/R)^(-1)(1+V/R)^(-1)
 =1+(U-V)/R+(U^2-UV+V^2)/R^2+O(R^(-3)).
```

For `K=floor(R/F)` and `K<h<=2K`, set `s_h=hF/R`.  Multiplying (1.1) by
`h` leaves the quadratic term at order one and makes the displayed
remainder `O(1/R)`.

Define the exact linear period

```text
d_(alpha,beta)
 =lcm(den(lambda_(alpha,beta)),den(mu_(alpha,beta))). (1.2)
```

Equivalently, for arbitrary integral lanes,

```text
d_(a,b)=lcm(a^2b/gcd(a^2b,F^3),
            ab^2/gcd(ab^2,F^3)).                    (1.3)
```

Then both linear terms in (1.1) are integral exactly when `d_(a,b)|h`.
The carrier is not an extra condition, because

```text
C_(alpha,beta)=a(R-1)lambda_(alpha,beta)
               =b(R-1)mu_(alpha,beta).              (1.4)
```

Thus `d_(a,b)|h` automatically implies `h C_(alpha,beta)` is integral.

## 2. Limiting packet and Gram formula

Let

```text
I_(alpha,beta)(s)
 =int_0^1 int_0^1
   e(s V_(alpha,beta)(x,y)/(alpha beta)) dx dy,

J_(alpha,beta)(s)=I_(alpha,beta)(s)+I_(beta,alpha)(s).
```

For fixed rational `alpha,beta` and fixed period `d=d_(alpha,beta)`, (1.1)
and a Riemann sum give, uniformly for `K<h<=2K`,

```text
F^(-2) G_(a,b)(h)=I_(alpha,beta)(s_h)+o(1),  d|h;
G_(a,b)(h)=O_d(F),                              d does not divide h. (2.1)
```

The second line follows by Abel summation in a variable whose fixed root
of unity is nontrivial; the quadratic amplitude has bounded total
variation.  Therefore the transpose-merged column

```text
H_(a,b)=G_(a,b)+G_(b,a)
```

obeys

```text
sum_(h~K)|H_(a,b)(h)|^2
 ~ K F^4/d * int_1^2 |J_(alpha,beta)(s)|^2 ds.       (2.2)
```

For a hinge `(alpha,beta,gamma)`, put

```text
d1=d_(alpha,beta), d2=d_(beta,gamma), L=lcm(d1,d2).
```

Only multiples of `L` contribute at order `F^4` to the cross Gram.  By
(1.4), both carriers equal one there.  Consequently the exact-alias-
removed normalized correlation has the limit

```text
sqrt(d1 d2)/L
 * |int_1^2 conjugate(J_(alpha,beta)(s))
                  J_(beta,gamma)(s) ds|
   / sqrt(int|J_(alpha,beta)|^2 int|J_(beta,gamma)|^2).  (2.3)
```

Exact phase aliases contribute only `F^o(1)` cell-pair multiplicity and
are negligible relative to `KF^4` here; in all three concrete families
below their computed cross-alias mass was exactly zero.  Formula (2.3) is
for fixed rational ratios/periods; it is not uniform when the denominators
grow with `F`.

## 3. The three observed rational families

The exact slopes and periods are:

| family | `(alpha,beta,gamma)` | `(lambda1,mu1; d1)` | `(lambda2,mu2; d2)` | `L` |
|:---|:---|:---|:---|---:|
| A | `(7/8,1,7/6)` | `(64/49,8/7;49)` | `(6/7,36/49;49)` | 49 |
| B | `(1,9/8,6/5)` | `(8/9,64/81;81)` | `(160/243,50/81;243)` | 243 |
| C | `(5/6,1,10/9)` | `(36/25,6/5;25)` | `(9/10,81/100;100)` | 100 |

If one nevertheless writes a carrier-difference congruence, it is
identically satisfied:

```text
A: L(C1-C2)=14 F(R-1),
B: L(C1-C2)=36 F(R-1),
C: L(C1-C2)=30 F(R-1).                              (3.1)
```

The common-frequency density factors `sqrt(d1d2)/L` are respectively
`1`, `1/sqrt(3)`, and `1/2`.  A 96-point tensor Gauss calculation of the
smooth integrals in (2.3) gives:

| family | integral overlap before density | predicted limit | last finite value |
|:---|---:|---:|---:|
| A | .535605955 | .535605955 | .537353449 at `F=144` |
| B | .732039785 | .422643367 | .429685855 at `F=160` |
| C | .469499403 | .234749701 | .242284558 at `F=144` |

The match identifies the resonance mechanism and explains the persistent
nonzero correlations.  The finite discrepancies have the sign and size
expected from convergence to the Riemann-sum limit; this numerical match
is a check of (2.3), not part of its proof.

## 4. Partner degree: false literally, true after weighting

### 4.1 Linear-degree counterexample

Take `F=N^8`, `R=N^25`, with sufficiently large `N` divisible by `6`, and
fix

```text
{a,b}={7F/8,F},  so d_(a,b)=49.
```

For every integral guaranteed lane `c` in, say, `[0.9F,1.1F]`,

```text
d_(F,c)=(c/gcd(c,F))^2 <= 1.21F^2.                 (4.1)
```

This follows directly from the two reduced linear frequencies `F/c` and
`F^2/c^2`.  Hence

```text
lcm(49,d_(F,c)) <= 49*1.21F^2 < K=F^(17/8)
```

for all sufficiently large `F`.  There is therefore a common principal
frequency in `(K,2K]` for every one of these `Theta(F)` lanes, and its
carrier is automatically aligned by (1.4).  Thus the unweighted principal-
resonance partner degree is linear, not divisor-bounded.

### 4.2 Bounded-period partners

There is a sharp useful replacement.  If `d_(b,c)=d`, (1.3) implies

```text
b^2 c divides d F^3,  and  b c^2 divides d F^3.     (4.2)
```

For a fixed `d`, every possible `c` is therefore a divisor of `dF^3`, so
there are at most `tau(dF^3)=F^o(1)` choices.  Summing over
`d<=F^o(1)` still gives only `F^o(1)` partners.

Moreover, the density prefactor in (2.3) satisfies

```text
sqrt(d1d2)/lcm(d1,d2)
 <=sqrt(min(d1,d2)/max(d1,d2)).                    (4.3)
```

Since the integral overlap is at most one, a fixed positive limiting
correlation forces `d2` to lie between `eta^2 d1` and `d1/eta^2`.  For
`d1=F^o(1)`, constant-size principal-correlation partners are consequently
divisor-bounded.

### 4.3 A weighted-degree lemma for the central lane

For `b=F`, write `r_c=c/gcd(c,F)`.  Equations (4.1) and (4.3) bound the
common-frequency density for a fixed first period `d1` by

```text
min(1,sqrt(d1)/r_c).
```

On a fixed shell interval `[AF,BF]`, group `c` by
`g=gcd(c,F)`.  Then `c=gr`, `g|F`, and

```text
sum_(AF<=c<=BF) 1/r_c
 <= sum_(g|F) sum_(AF/g<=r<=BF/g) 1/r
 <<_(A,B) tau(F)=F^o(1).                           (4.4)
```

Thus the resonance-density weighted partner degree is `F^o(1)` whenever
`d1=F^o(1)`, despite the `Theta(F)` raw degree.  Extending (4.4) uniformly
from the central lane `b=F` to every shell lane, and controlling the
nonprincipal `O(F)` terms in (2.1) in aggregate, are the remaining analytic
tasks suggested by this calculation.

## 5. Scope ledger

The three degree statements must not be conflated.

1. **Common-multiple partners.**  For the exact tower sequence
   `F=N^8,R=N^25`, sufficiently large `N` divisible by `6`, and the fixed
   packet `{7F/8,F}`, there are `Theta(F)` lanes `c` for which
   `lcm(d_(7F/8,F),d_(F,c))<K`.  This asserts only that at least one common
   principal frequency occurs below the band length.  It does not assert a
   fixed lower bound for every corresponding normalized Gram entry.
2. **Fixed-correlation partners.**  Formula (2.3) applies to fixed rational
   lane ratios, hence fixed periods, along integral scaling subsequences.
   Within this principal-resonance regime, if `d1=F^o(1)` and the limiting
   normalized correlation is at least a fixed `eta>0`, then (4.3) forces
   `eta^2 d1<=d2<=d1/eta^2`; (4.2) then leaves only `F^o(1)` partners.
   This is not asserted uniformly for ratios or periods that vary rapidly
   with `F`.
3. **Weighted partners.**  The bound (4.4) sums the common-frequency density
   weights and is proved only when the shared lane is exactly `b=F`, with a
   fixed shell-ratio interval and `d1=F^o(1)`.  No uniform analogue for an
   arbitrary lane `b` is proved here.

Accordingly, the calculation explains and controls the observed rational
hinges but does **not** close the full transpose-quotiented Gram estimate.
One still needs a uniform weighted-degree theorem for noncentral lanes and
an aggregate estimate for the nonprincipal frequency classes.
