# R140 degree-zero localization and Frobenius dichotomy

## Status

This report stress-tests the two survivors of R138--R139:

```text
turn global divisor abundance into a pole near a selected zeta zero;
or construct an exceptionally cheap quadratic Frobenius mask.       (0.1)
```

The audit produces four unconditional results.

1.  Bombieri--Perelli's distinct-zero theorem applies to the R138
    quotient

    ```text
    F_(chi,psi)=zeta L_(chi psi)/(L_chi L_psi).                     (0.2)
    ```

    It gives `>>T log T` genuine zeros and `>>T log T` genuine poles of
    `F_(chi,psi)` up to height `T`.  Thus cancellation of its numerator and
    denominator divisors is globally very far from complete.
2.  This global abundance has no horizontal localization.  An explicit
    ordinary Dirichlet-series model has nonnegative Dirichlet and
    logarithmic-derivative coefficients, the exact symmetry `K(s)=K(1-s)`,
    uniform right-boundary bounds, and zeros arbitrarily close to `Re(s)=1`
    whose nearest poles lie on the critical line.  Hence
    Schwarz--Pick, Jensen, Hardy/inner--outer factorization, and boundary
    almost periodicity cannot supply the missing local pole.
3.  A cheap exceptional quadratic mask forces a near-one zero of one of its
    three auxiliary Dirichlet `L`-functions.  At the R138 Cauchy rate

    ```text
    log(d_1 d_2)=o(X^kappa),                                      (0.3)
    ```

    the forced zero has

    ```text
    beta_aux >= 1-kappa-o(1).                                    (0.4)
    ```

    Jutila density makes such masks sparse, but not nonexistent.
4.  Passing from quadratic characters to the full group of even characters
    modulo one prime makes head interpolation exact and cheap in conductor.
    Parseval nevertheless leaves Fourier `l1` mass of square-root size.
    Its exponential rate is strictly larger than the largest available
    Cauchy localization rate.  A centered variant cancels the common
    conductor exactly, but ordinary `L2`/large-sieve control retains the same
    square-root wall.

The conclusion is a fail-fast one, not a solution of the fixed-strip
problem.  The broad degree-zero analytic structure has now been exhausted:
it cannot force local zero--pole pairing.  The quadratic exception is no
longer an unspecified lucky pattern: it is a sparse pattern supported by a
near-one auxiliary zero.  What remains is a genuinely coefficient-specific
signed theorem for the bounded Boolean local alphabet, or a theorem proving
that the sparse mask set is empty.

```text
global distinct zeros and poles                         THEOREM
right-edge localization from broad analytic axioms     FALSE
cheap mask => near-one auxiliary zero                   THEOREM
quadratic-mask density sparsity                         THEOREM
full-character exact head interpolation                 THEOREM
absolute/ordinary-L2 full-character closure             CLOSED
signed Boolean divisor correlation                      OPEN
fixed uniform zero-free strip                           NOT PROVED
zeros approaching one                                   NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R138-DEGREE-ZERO-QUADRATIC-VIRTUAL-L-GATE.md`](R138-DEGREE-ZERO-QUADRATIC-VIRTUAL-L-GATE.md)
and
[`R139-QUADRATIC-UNIVERSALITY-PAIR-REPLICATION-GATE.md`](R139-QUADRATIC-UNIVERSALITY-PAIR-REPLICATION-GATE.md).

## 1. A positive proportion of the divisor is genuinely uncancelled

Let `chi,psi` be the primitive even real quadratic characters from R138 and
put `theta=chi psi`.  Set

```text
U(s)=zeta(s)L(s,theta),             V(s)=L(s,chi)L(s,psi).       (1.1)
```

At an unramified prime their first Euler coefficients are

```text
a_U(p)=1+theta(p),                  a_V(p)=chi(p)+psi(p).        (1.2)
```

They obey the exact identities

```text
a_U(p)^2=a_V(p)^2=2+2theta(p),
a_U(p)a_V(p)=2chi(p)+2psi(p).                                  (1.3)
```

The prime number theorem in progressions therefore gives

```text
sum_(p<=x) a_U(p)^2/p =2 log log x+O(1),
sum_(p<=x) a_V(p)^2/p =2 log log x+O(1),
sum_(p<=x) a_U(p)a_V(p)/p =O(1).                               (1.4)
```

The finitely many ramified primes do not affect (1.4).  Both products have
degree two, the same two even Gamma factors, and the same conductor because
`d_theta=d_chi d_psi`.  Their Euler roots have modulus at most one.
Bombieri--Perelli's density hypothesis is known for each fixed zeta or
Dirichlet `L`-factor, and hence for each product in (1.1).

Their Theorem 1 consequently applies in both orientations:

```text
D(T;U,V)>>_(chi,psi) T log T,
D(T;V,U)>>_(chi,psi) T log T.                                  (1.5)
```

Here `D(T;U,V)` is the sum of the positive multiplicity differences
`max(m_U(rho)-m_V(rho),0)` over nontrivial zeros through height `T`.
Since `F=U/V`, (1.5) says exactly

```text
N_zero(F;T)>>T log T,             N_pole(F;T)>>T log T,          (1.6)
```

with multiplicity.  This is stronger than merely proving that the quotient
has infinitely many zeros and poles.

The limitation is equally precise.  The proof of (1.5) is a critical-strip
global count.  It is compatible with every distinct zero and pole counted in
(1.6) lying on `Re(s)=1/2`.  It gives no pole in a disc around a selected
right-edge zero of `zeta`.

Primary source: E. Bombieri and A. Perelli,
[*Distinct zeros of L-functions*](https://doi.org/10.4064/aa-83-3-271-281),
Acta Arith. 83 (1998), Theorem 1.

## 2. Exact analytic countermodel to local pole forcing

The failure of localization is not merely an absence in the proof of
Bombieri--Perelli.  It already fails for an explicit positive
Dirichlet-series model.

Fix `q=2` and `1/2<a<1`.  Define

```text
H_q(s)=[1-q^(1/2-s)]^2/[(1-q^(-s))(1-q^(1-s))],

R_(q,a)(s)
 =[1+q^(a-s)]^2[1+q^(1-a-s)]^2/[1+q^(1/2-s)]^4,

K_(q,a)(s)=H_q(s)^2 R_(q,a)(s).                                (2.1)
```

### Theorem 2.1 -- positive symmetric model with unpaired right zeros

The function in (2.1) has the following properties.

```text
K(s)=K(1-s),                         K(conj(s))=conj(K(s));
K(s)->1 as Re(s)->+infinity;
K and -K'/K have nonnegative ordinary Dirichlet coefficients;
exp(-C_r)<=abs(K(1+r+it))<=exp(C_r) for every fixed r>0.         (2.2)
```

It has zeros of order two at

```text
a+(2m+1)pi i/log q,
1-a+(2m+1)pi i/log q,                                      m in Z, (2.3)
```

and same-height poles of order four on `Re(s)=1/2`.  For `q=2`,
every disc

```text
abs(s-[a+(2m+1)pi i/log 2])<a-1/2                              (2.4)
```

is pole-free.  Thus the zero line in (2.3) can approach `Re(s)=1`
while its compensating pole line remains critical.

#### Proof

Put

```text
C_k=q^k+1-2q^(k/2),
B_k=q^(ak)+q^((1-a)k)-2q^(k/2).                                (2.5)
```

Direct logarithmic expansion in `Re(s)>1` gives

```text
log K(s)=sum_(k>=1) d_k q^(-ks)/k,
d_k=2C_k+2(-1)^(k+1)B_k.                                     (2.6)
```

AM--GM gives `B_k>=0`, and

```text
C_k-B_k=(q^(ak)-1)(q^((1-a)k)-1)>=0.                           (2.7)
```

Thus `d_k=2(C_k+B_k)>0` for odd `k`, while
`d_k=2(C_k-B_k)>=0` for even `k`.  Exponentiating (2.6) proves
coefficient positivity for `K`; differentiating proves it for `-K'/K`.
The bound `d_k<=8q^k` gives (2.2).

For

```text
P_(c,epsilon)(z)=(1+epsilon q^c z)(1+epsilon q^(1-c)z),         (2.8)
```

one has

```text
P_(c,epsilon)(1/(qz))=q^(-1)z^(-2)P_(c,epsilon)(z).             (2.9)
```

Writing the factors in (2.1) as ratios of (2.8) proves the exact
reflection symmetry.  Their elementary zero sets give (2.3)--(2.4).
QED.

### What the countermodel does and does not rule out

The model rules out every proposed localization lemma using only

```text
positivity + degree-zero reflection + exterior H-infinity bounds.         (2.10)
```

In particular, strip Blaschke factors can carry the zero/pole geometry in
(2.3) without changing the boundary modulus.  Whole-strip Jensen formulae
count the critical pole row, while a right substrip has an uncontrolled left
boundary.

Right-boundary almost periodicity does not automatically propagate to
meromorphic almost periodicity in the strip.  Meromorphic almost-periodic
functions have uniformly separated zero and pole sets on every compact
substrip.  Combining two incommensurable lattice models, for example the
`q=2` and `q=3` versions, produces arbitrarily close critical zeros and poles
by Kronecker approximation, and hence violates that necessary separation.

Primary source for the separation criterion: N. D. Parfyonova and
S. Yu. Favorov,
[*Meromorphic almost periodic functions*](https://doi.org/10.30970/ms.13.2.190-198),
Matematychni Studii 13 (2000), Theorem 1 and Corollary 1.

There is one essential caveat.  The coefficient `d_k` in (2.6) can be of
size `q^k`.  The genuine R138 logarithmic coefficient is bounded by

```text
0<=(1-chi(p)^v)(1-psi(p)^v)<=4.                                (2.11)
```

Thus (2.1) kills the broad complex-analytic route, not a theorem exploiting
the exact bounded quadratic local alphabet.

## 3. A cheap quadratic mask forces an auxiliary zero

Let `d_1,d_2` be coprime positive fundamental discriminants, put

```text
chi=chi_(d_1),          psi=chi_(d_2),
theta=chi psi,          q=d_1d_2.                               (3.1)
```

Assume first that every prime through `X` is unramified in the biquadratic
field, and impose the R138 head mask

```text
(q,product_(p<=X)p)=1,
no prime p<=X has chi(p)=psi(p)=-1.                             (3.2)
```

Equivalently, the biquadratic field
`Q(sqrt(d_1),sqrt(d_2))`, of discriminant `q^2`, has no unramified prime
through `X` in the Frobenius class `(-1,-1)`.

Choose a fixed nonnegative smooth `w` supported in `(1/2,1)`, with Mellin
transform `W` and `W(1)>0`.  Put

```text
S_xi(X)=sum_n Lambda(n)xi(n)w(n/X).                             (3.3)
```

Odd prime powers vanish in

```text
S_1-S_chi-S_psi+S_theta,                                      (3.4)
```

by (3.2), and even powers vanish algebraically because both character
values square to one.  Hence (3.4) is exactly
zero.  On the other hand,

```text
S_1(X)=XW(1)+o(X).                                             (3.5)
```

Apply the smoothed explicit formula to the three nonprincipal sums.  If all
their zeros with `abs(Im rho)<=T` satisfy `Re(rho)<=beta_*`, then, for an
arbitrarily large fixed smoothing order `A`,

```text
X <<_w X^beta_* log(qT)+X log(qX)T^(1-A)+o(X).                 (3.6)
```

Taking `T` to be a sufficiently large power of `log(qX)` gives the following
dichotomy.

### Theorem 3.1 -- mask-to-zero theorem

Every mask (3.2) forces a zero of at least one of

```text
L(s,chi),       L(s,psi),       L(s,theta)                     (3.7)
```

at polylogarithmic height and with

```text
beta_aux
 >=1-[log log(qX)+O_w(1)]/log X.                               (3.8)
```

In particular, if

```text
log q=o(X^kappa),                                             (3.9)
```

then

```text
beta_aux>=1-kappa-o(1).                                      (3.10)
```

At the R138 high-jet scale,

```text
X=exp(lambda k/r),
kappa=(r/lambda)log(R/d),                                    (3.11)
```

condition (3.9) is exactly the desired sub-Cauchy conductor budget.
Thus every arithmetically cheap mask automatically brings in a near-one
auxiliary zero capable of paying the source divisor.  The exceptional case
is not independent of the analytic obstruction.

## 4. The exceptional set is sparse, not empty

Let `d_1,d_2<=Q`, and suppose `log Q<=X^(kappa+o(1))`.  Choose
`delta>kappa` in Jutila's range `delta<=1/5`.  Theorem 3.1 assigns to every
mask a zero with real part greater than `1-delta`.

Jutila's zero-density estimate gives at most

```text
Q^(4delta+o(1))                                               (4.1)
```

bad primitive real characters of conductor at most `Q`.  A bad `chi` or
`psi` therefore contributes at most

```text
Q^(1+4delta+o(1))                                             (4.2)
```

ordered pairs.  A bad product `theta`, whose conductor is at most `Q^2`,
contributes at most

```text
Q^(8delta+o(1))                                               (4.3)
```

characters.  Each `theta` has only `Q^o(1)` coprime
fundamental-discriminant factorizations.  Letting `delta` decrease to
`kappa` yields

```text
# {masks d_1,d_2<=Q}
 <<Q^(1+4kappa+o(1))+Q^(8kappa+o(1)).                          (4.4)
```

For `kappa<1/5`, the first term dominates and (4.4) is `o(Q^2)`.  This is a
strong sparsity theorem.  It does not prove that the set is empty, and R138
needs one constructible mask, not a positive density of them.

The sign of a possible exceptional real zero sharpens the picture.  In a
one-exceptional-zero Chebotarev formula,

```text
4 Theta_(--)(X)
 =X+1_(exc=chi)X^beta/beta+1_(exc=psi)X^beta/beta
    -1_(exc=theta)X^beta/beta+error.                            (4.5)
```

A Siegel zero of `chi` or `psi` increases the missing-class mass.  Only a
Siegel zero of the product `theta` can suppress it.  Landau--Page makes such
product characters extremely rare, but neither it nor Deuring--Heilbronn
rules out the one exceptional factorization needed here.

Unconditional least-prime results also miss the required scale.  A Linnik
bound of the shape `p_(--)<<q^L` only gives `log q>>log X`.  R138 needs a
contradiction to `log q=o(X^kappa)`.  A theorem

```text
p_(--)<<(log q)^A                                             (4.6)
```

would close the mask route after choosing `kappa<1/A`; GRH supplies this
shape, but no unconditional theorem does.

Primary density source: M. Jutila,
*Zero-density estimates for L-functions*, Acta Arith. 32 (1977).

## 5. Full even-character interpolation modulo one prime

The quadratic mask prescribes a rare Frobenius pattern before choosing the
characters.  There is a dual construction in which one first chooses a
prime modulus and then interpolates the actual head by all even characters.
It makes the conductor cheap but exposes an exact square-root Fourier wall.

Let `q>X` be prime and

```text
G=F_q^*/{+-1},                 N=abs(G)=(q-1)/2.                (5.1)
```

Let `H` be an inverse-symmetric set containing the identity and every class
`[p^v]` to be killed, and put `h=abs(H)<N`.  Define

```text
phi(g)=N/(N-h) 1_(g notin H).                                 (5.2)
```

Fourier-expand over the even characters modulo `q`:

```text
phi(g)=sum_(chi even mod q) a_chi chi(g).                       (5.3)
```

The principal coefficient is one, and for every nonprincipal even
character

```text
a_chi=-(N-h)^(-1)sum_(g in H) conjugate(chi(g)).                (5.4)
```

Parseval gives the exact identities

```text
sum_(chi nonprincipal) abs(a_chi)^2=h/(N-h),
sum_(chi nonprincipal) abs(a_chi)
 <=sqrt[(N-1)h/(N-h)].                                        (5.5)
```

Now set

```text
A_phi(s)=sum_(chi even mod q) a_chi D_chi(s),
D_chi=-L'/L.                                                  (5.6)
```

For `Re(s)>1`, apart from the omitted Euler factor at `q`,

```text
A_phi(s)=sum_n Lambda(n)phi([n])n^(-s).                         (5.7)
```

It has nonnegative coefficients and kills the prescribed head exactly.
Since `phi(e)=0`, the common even Gamma factor cancels.  Also

```text
sum_(chi nonprincipal)a_chi=-1,                                (5.8)
```

so the signed conductor is only `-(1/2)log q`; derivatives of positive
order remove this constant.

If the head contains all relevant prime powers through

```text
X=exp(lambda k/r),                                             (5.9)
```

then `h=exp[(lambda/r+o(1))k]`.  The absolute auxiliary divisor ledger in
(5.5) therefore has exponential rate

```text
lambda/(2r).                                                   (5.10)
```

Even granting auxiliary zero-freeness throughout `Re(s)>1/2`, the largest
remote-zero radius is `r+1/2`.  For a source at distance `d=r+delta`,

```text
log[(r+1/2)/d]<1/(2r)<lambda/(2r),       lambda>1.              (5.11)
```

Thus the square-root Fourier cost in (5.10) is already larger than the
maximum Cauchy localization gain.  Enlarging `q` reduces the Fourier `l2`
norm but increases the number of characters; ordinary Cauchy--Schwarz or a
large sieve recovers the same `sqrt(h)` quantity.

There is a useful centered variant.  When `q>2X`, take `e` outside the
killed head and set

```text
phi(e)=1,
phi=0 on H,
phi=(N-1)/(N-h-1) elsewhere.                                  (5.12)
```

Then the principal Fourier coefficient is still one but

```text
sum_(chi nonprincipal)a_chi=0.                                (5.13)
```

The conductor cancels exactly.  The Gamma degree is now the single known
zeta Gamma term rather than zero, and

```text
sum_(chi nonprincipal)abs(a_chi)^2
 =h(N-1)/[N(N-h-1)]~h/N.                                     (5.14)
```

This is the correct normalization for a prospective signed fluctuation
theorem.  It does not improve the absolute or ordinary `L2` rate (5.10).

Unlike the quadratic prescribed-pattern construction, the adaptive mask can
also solve the *local* zero-selection problem.  In a fixed near-one rectangle
with left edge `alpha>=4/5`, Jutila gives

```text
sum_(cond chi<=Q) N(alpha,T,chi)
 <<_(epsilon,T) Q^[4(1-alpha)+epsilon].                         (5.15)
```

For `alpha>3/4` this is `o(Q/log Q)`.  Hence all but a vanishing proportion
of prime moduli `q~Q` have no character at all with a zero in that rectangle;
one may choose such a modulus first and build (5.2) afterward.  The remote
critical zero cloud, not target-disc avoidance, is what causes (5.10).

There is one exact low-Fourier exception.  Suppose all head classes lie in a
proper subgroup `K<G` of index `m`.  Character orthogonality gives

```text
phi_K
 =m/(m-1) 1_(G\K)
 =1-[1/(m-1)]sum_(chi in K^perp, chi!=1)chi.                    (5.16)
```

This mask has nonprincipal Fourier `l1` mass exactly one, independent of the
head size.  Its existence is equivalent to a nonprincipal even character
`theta` modulo `q` with

```text
theta(p)=1,                         p<=X.                        (5.17)
```

Thus low Fourier complexity has not vanished; it has become an exceptional
long principal-character run.  The analytic budget would allow (5.15) only
if

```text
log q<=X^vartheta,
vartheta<(r/lambda)log(R/d)<1/(2lambda),                        (5.18)
```

together with zero avoidance for the few characters in `K^perp`.  CRT plus
Linnik constructs (5.16) only with `log q<<X`.  Burgess gives no lower bound
at the scale in (5.17).  Under GRH, a least-nonresidue bound
`p<<log(q)^2` would force `log q>>sqrt(X)`, which lies just beyond the strict
half-power ceiling in (5.18).  This calibrates the exceptional subgroup
loophole but does not close it unconditionally.

## 6. What remains after the dichotomy

The current endpoint is narrower than R138's original list.

* A broad analytic local-pairing theorem is false by Theorem 2.1.
* Global divisor abundance is maximal in order of magnitude by (1.6), but
  does not localize horizontally.
* A cheap quadratic head mask forces the very auxiliary zero that can
  cancel the source.  Density says this phenomenon is rare, not impossible.
* Using all even characters makes interpolation deterministic, but absolute
  values and ordinary second moments hit the exact half-unit wall.
* The only exact low-Fourier escape is a character that is principal on every
  prime in the head, with conductor below the strict half-power threshold.

Accordingly, a successor must prove at least one of the following genuinely
new statements.

1.  **Boolean right-edge incidence.**  For the exact local coefficients

    ```text
    (1-chi(p)^v)(1-psi(p)^v) in {0,4},                          (6.1)
    ```

    a right-edge numerator zero forces a denominator zero in a quantitatively
    prescribed region and for sufficiently many pairs.
2.  **Exceptional-set emptiness.**  Upgrade the sparse count (4.4) to zero
    at a sub-Cauchy conductor scale, necessarily improving polynomial
    least-Frobenius bounds toward (4.6).
3.  **Signed full-character divisor bound.**  In the centered construction
    (5.12), beat the `sqrt(h)` absolute ledger by cancellation in the actual
    character-zero vector, not merely in its common Gamma/conductor term.

Each target is stronger than the imported literature used here.  None is a
renaming of a known zero-free region, but none has been proved in this report.

## 7. Verdict

R138's degree-zero quotient has many genuine zeros and poles, so its divisor
is not secretly trivial.  The missing assertion is specifically local and
right-edge.  General complex analysis cannot provide it: an exact positive
self-reciprocal Dirichlet model places the compensating poles on the critical
line.  Quadratic arithmetic improves the situation only to a sharp
dichotomy: a low-cost missing Frobenius class entails a near-one auxiliary
zero, and such patterns form a zero-density exceptional set.

Therefore this stage proves neither a fixed zero-free strip nor the
nonexistence of one.  It does prove that any continuation must use the exact
bounded Boolean prime-power coefficients in a signed divisor estimate, or
an individual least-Frobenius theorem far beyond current unconditional
bounds.
