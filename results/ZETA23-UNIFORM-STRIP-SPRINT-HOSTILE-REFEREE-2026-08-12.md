# Uniform-strip sprint: hostile referee audit

Status: independent audit of the four current theorem cards and their
possible combinations, 2026-08-12.  Constants, signs, endpoint terms, and
quantifiers were recomputed.  This report proves no zero-free strip.

## 1. Binary verdict

```text
Depth-sensitive microscopic count                    PASS
Poisson/Fourier continuation ledger                  PASS
Candidate-relative positive-reserve reduction        PASS AS A REDUCTION
Candidate-relative fixed fractional lower edge       OPEN
Mertens anchored step-Poincare theorem                PASS
Mertens exact rank-one/ANOVA refinement               PASS
Mertens principal-band decomposition                  PASS
Interlaced-binomial growing Pick screen                PASS
Fixed-width reflected-pair Poisson cap                 PASS AFTER CORRECTION
Green--Poisson one-representative dual ledger           PASS CONDITIONALLY
Known fixed-power short-increment estimate            ABSENT
Global compact Pick transfer                          OPEN
Any combination in the audited files proves a strip  NO
```

The only supersession is harmless: the exact ANOVA argument improves the
anchored endpoint constant from `2H` to `H`.  The older `2H` theorem remains
true.

## 2. Depth-sensitive count and Poisson ledger

At

```text
sigma=1+u,       u=(log |t|)^(-1/2),       L=log |t|,
```

the completed logarithmic derivative has the correctly signed form

```text
sum_rho (sigma-beta)/[(sigma-beta)^2+(t-gamma)^2]
 =L/2+Re zeta'(sigma+it)/zeta(sigma+it)+O(1).
```

The absolutely convergent von Mangoldt series gives
`|zeta'/zeta|<=u^(-1)+O(1)`, so the sum is
`L/2+O(sqrt L)`.  For `beta>=sigma_0` and
`|gamma-t|<=C/L`, each summand is at least

```text
A/(A^2+C^2/L^2),       A=1+u-sigma_0.
```

This gives

```text
N_cell(sigma_0,t;C)
 <=[(1-sigma_0)/2]L+O_(sigma_0,C)(sqrt L).
```

There is no missing factor two for right-half reflected-pair centers.  At
the current parameters the constants are therefore exactly

```text
beta>=0.99:       (0.005+o(1))L,
beta>=0.8234:     (0.0883+o(1))L.
```

The pair Poisson kernel has Fourier transform

```text
2*pi exp(-(1/2+u)|xi|) cosh(b|xi|),
```

while the Pick potential has, off zero frequency,

```text
2*pi exp(-alpha|xi|) sinh(b|xi|)/|xi|.
```

Thus their exact multiplier is

```text
exp((1/2+u-alpha)|xi|) tanh(b|xi|)/|xi|.
```

At `alpha=0.49` and cell-resolving frequencies `|xi|asymp D=dL`, its
exponential part is `exp(0.01D+o(L))=Y^(0.01+o(1))`.  The sign and direction
of analytic continuation in the report are correct.

Binary consequence: the count is a strictly better **upper** ledger.  It
does not force spacing, bounded jet order, a positive collateral response,
or a compact Pick interpolant.

## 3. Candidate-relative arithmetic edge

On the selected-positive quotient, the decomposition

```text
K_ar=-N_rho+R_other,rho
```

implies exactly

```text
Q_ar(q_rho)+K_rho
 =<q_rho,R_other,rho q_rho>.
```

Hence

```text
Q_ar(q_rho)>=-(1-epsilon)K_rho+o(K_rho)
```

is equivalent to a fixed positive reserve

```text
<q_rho,R_other,rho q_rho>
 >=epsilon K_rho+o(K_rho).
```

This is an identity, not an estimate.  In particular `R_other,rho` is not
known to be a positive operator.  The isolated completed selected block has
`R_other,rho=0`, so coefficient-free geometry cannot prove the requested
fractional inequality.  The sub-`log 2` support lemma correctly kills every
same-leg prime-power translate; it does not kill the completed cross scalar
or create the reserve.

The exponent comparison is also correct:

```text
E_0/d=0.0119000134.../0.66=0.0180303234...,
1/2-E_0/d=0.4819696766....
```

Binary consequence: this report identifies the weakest scalar still needed,
but supplies no positive fraction of it.

## 4. Mertens energy and zero mode

For

```text
S_n=M(n+H)-M(n),       1<=n<=N=X-H,
T=sum_(n<=N) S_n,
```

the exact window weight is trapezoidal and satisfies

```text
|T-HM(X)|<=H^2.
```

The ANOVA identity

```text
sum |S_n|^2=|T|^2/N+sum |S_n-T/N|^2
```

therefore gives the sharper bound

```text
J(X,H)>=(H^2/N)(|M(X)|-H)_+^2,
|M(X)|<=H+sqrt(NJ(X,H))/H.
```

All endpoint coefficients and the constant `H` check exactly.  The earlier
residue-chain proof with `2H` also checks.

Consequently

```text
J(X,X^theta)<<X H^(2-eta)
```

would give the strip width

```text
delta=min(1-theta,theta*eta/2).
```

The `0.99` boundary-safe calibration

```text
theta=0.98,       eta=1/49
```

is exact: both the target energy and the crude full-convolution boundary
have exponent `X^2.94`.  Taking `theta=0.97` gives a strict boundary margin.

The full Fourier energy has exactly `X+H-1` nonzero windows and

```text
J^*>=H^2|M(X)|^2/(X+H-1).
```

Outside

```text
||alpha||<X^0.01/H
```

the coefficient-blind Dirichlet-kernel estimate is already at the target
scale.  Thus the unresolved principal band contains the rank-one mean
projection.  Centered dispersion controls only the orthogonal variance.

The recompletion

```text
T=-sum_(dm>=2) mu(d)(Lambda(m)-1)w(dm)/log(dm)
```

is exact.  A bound `T<<H X^0.99` already gives
`M(X)<<X^0.99`; estimating its `d=1` part separately with that power gives
the corresponding PNT error and is likewise already strip-strength.

The 2026 almost-all short-interval theorem gives arbitrary fixed logarithmic
savings, not `H^(-eta)` with fixed `eta`.  Its constants are not uniform for
taking the logarithmic exponent to grow with `X`.  Hence it does not fill
this gate.

Binary consequence: the Mertens route is an exact equivalent-strength
reformulation, not an unconditional shortcut.

## 5. Combination audit

### 5.1 Poisson equilibrium plus arithmetic reserve: NO

The equality `L/2+O(sqrt L)` does not force a deep collateral reservoir.
Critical-line zeros of density `L/(2*pi)` alone contribute the whole main
Poisson mass because one critical-line kernel has integral `pi`.  Such
shallow rows are power-negligible compared with the selected carrier in the
current reduction.  Therefore the Poisson equilibrium cannot be converted
into the lower bound

```text
<q,R_other q>>=epsilon K
```

without a new sign-and-depth theorem.

### 5.2 Cell count plus Pick compression: NO

The cumulative cap still permits a linear depth fan.  At `alpha=0.49`, one
effective row at each gap

```text
alpha-b=k/L,       1<=k<=0.01L,
```

obeys the cap at every depth.  Thus neither bounded cluster cardinality nor
bounded Hermite order follows.  A uniform growing-jet/compact-support
theorem remains necessary.

### 5.3 Centered dispersion plus principal-band control: NO

The exact decomposition is orthogonal:

```text
energy = mean rank-one term + centered variance.
```

No strength in the centered variance bounds the mean term.  Every theorem
which removes the constant start-variable mode also removes the component
that recovers `M(X)`.  Reintroducing it is precisely the fixed-strip gate.

### 5.4 Logarithmic savings at many scales: NO

The positive slowly varying model

```text
a(n)=exp(-sqrt(log(n+2)))
```

has arbitrary fixed logarithmic short-increment savings at every fixed
polynomial scale while its partial sums remain `X^(1-o(1))`.  Any proposed
multiscale upgrade must therefore use a new specifically multiplicative,
signed input; the displayed scale iteration alone cannot create a fixed
power.

## 6. Global Pick and Green--Poisson cards

### 6.1 Interlaced-binomial screen: PASS

For the two chains

```text
h_n=-1-i*n*pi/d,
h'_n=-1-i*(n+1/2)*pi/d,       0<=n<=K,
```

the `K`-th binomial differences of every polynomial of degree below `K`
vanish.  Taylor expansion in a disk of radius `r<alpha`, the half-disk sign
conditions, and Lagrange interpolation give

```text
|U(alpha)|
 <=K^C[2*pi*c/(alpha*d)+o(1)]^K,
K/L->c<alpha*d/(2*pi).
```

Thus the forced attenuation exponent

```text
F_(alpha,d)(c)=c*log[alpha*d/(2*pi*c)]
```

and its unconstrained maximizer `c=alpha*d/(2*pi*e)` are correct.  This is
a real growing-list obstruction to any argument that silently treats every
fixed-cell constant as `X^o(1)` uniformly in the number of cells.

An initial count audit of this screen made a material scale error: it
applied the `(0.005+o(1))L` cap for one `C/L` ordinate window to all `2cL`
nodes, although the nodes span a fixed-width interval and `Theta(L)` phase
cells.  That would have given the unsupported restriction `c<=.0025`.

The corrected fixed-width argument integrates the completed Poisson budget
over the whole screen interval, padded by `s` on each side.  Charging both
horizontal members of each pair gives

```text
N_pair/L
 <=(H+2*s)
   /{2*sum_(a in {a_R,a_L})
       [atan((H+s)/a)+atan(s/a)]}
   +o(1).
```

At `H=c*pi/.66`, `a_R=.01`, `a_L=.99`, and `s=.003`, the unique crossing is

```text
c=0.00465416454...,
F(c)=0.01118512309....
```

The latter is below `E_0=0.0119000134...`.  The corrected report now uses
this bound.  It is a necessary Poisson compatibility ceiling, not evidence
that zeta realizes the screen.

The same proof, with `s=sqrt(H)`, gives the long-interval Carleson bound

```text
N_pair(I)<=[H/(4*pi)+O(sqrt H)]L+o(L).
```

Hence the pair measure has upper long-interval density `L/(4*pi)+o(L)`
without an independently superposed Bellotti--Wong discrepancy.  The
`O(sqrt H)L` boundary allowance prevents this from becoming a strict local
finite-section density theorem on every fixed short interval.

### 6.2 Distinct-cell multiplicity correction: PASS AFTER CORRECTION

An early proposed charge of `eta*L` for `K=L/log L` distinct nearby phase
cells incorrectly assigned `log L` to every cell.  The exact rearrangement
is

```text
sum_(j<=K) log(L/j)
 =K*log(L/K)+O(K)
 =O[L*log log L/log L]=o(L).
```

The current reports retract the fixed-power claim.  A fixed exponent still
requires `Theta(L)` distinct cells or a quantitatively controlled growing
jet inside one or a few cells.  The available all-jet continuum identity
does not provide the latter because its scaled-depth tail and growing-order
quadrature conditioning are uncontrolled.

### 6.3 Green--Poisson dual ledger: PASS CONDITIONALLY

At centered line `x=.9` (actual line `Re s=1.4`), the pair kernel budget

```text
sum K_(x,b_j)(v_j)<=L/2+O(1)
```

has the correct sign and normalization.  For `A=.5`, the minimum of
`K_(x,b)` over `0<=b<=A` occurs at `b=0` or `b=A`; the two endpoint branches
cross at

```text
v^2=(x^2-A^2)/3.
```

The rowwise positive majorant

```text
G<=lambda*K+[g_A-lambda*k_(x,A)]_+
```

is therefore valid.  Under the explicitly stated one-effective-
representative-per-cell condition and an `exp(o(L))` treatment of the
singular target cell, its density term is a Darboux upper sum and converges
to `d/(2*pi)` times the integral.

For `lambda=.304`, direct antiderivatives give

```text
integral_R[g-.304*k]_+=1.38894153847...<1.39,
bill/L<=.152+.66*1.39/(2*pi)=.29800874479...,
reserve/L>=.3234-.29800874479=.02539125521....
```

The switch, positive root, integral, and threshold
`d>0.5655295684...` reproduce numerically.  Calling this a proved
**conditional** bill is accurate: the representative reduction, target-cell
control, compact realization, and arithmetic reserve remain assumptions or
open gates.

The reproducibility module
`src/green_poisson_pick_ledger.py` implements exactly these elementary
formulas and the reflected-pair crossing.  Its three focused tests pass:

```text
python3 -m pytest -q src/test_green_poisson_pick_ledger.py
3 passed
```

## 7. Referee conclusion

The sprint produced four material sharpenings:

1. a depth-sensitive local cap with the correct `0.005` and `0.0883`
   coefficients;
2. an exact rank-one Mertens factorization improving the deterministic
   endpoint constant and isolating the sole principal mode;
3. a fixed-width reflected-pair Poisson/Carleson cap which absorbs the
   first rigorous growing binomial screen inside the old exponent budget;
4. a conditional Green--Poisson dual ledger which more than doubles the
   carrier reserve after one-representative reduction.

Neither is a tightened bound on an actual zeta zero.  The live theorem
cards required for `Re(s)>0.99` remain, independently,

```text
(A) a compact global Pick/sign transfer surviving the allowed growing fan;
(B) a fixed positive candidate-relative arithmetic reserve;
```

or, on the alternative route,

```text
(C) J(X,X^theta)<<X H^(2-eta) for one fixed eta>0.
```

No audited input proves `(A)`, `(B)`, or `(C)`, and no two subpower or
one-sided upper estimates combine to imply one of them.

The strongest new unconditional divisor statement in this sprint is the
fixed-width reflected-pair Poisson cap (and its `L/(4*pi)` long-interval
Carleson-density corollary).  The numerically stronger `0.025391255...`
carrier reserve is a theorem only after the expressly unproved
one-representative and target-cell hypotheses.  Therefore no implication in
the audited chain yields a zero-free strip.
