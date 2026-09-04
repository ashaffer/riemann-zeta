# High-denominator consecutive-gap exceptional-tail gate

**Date:** 2026-08-13

**Verdict:** a 2026 exceptional-short-interval theorem improves the
large-gap excision in the actual-prime Voronoi antenna.  Gafni--Tao's
general exceptional-set bound, combined with their displayed unconditional
zero-density envelope, gives the exact exponent

```text
mu(797/5000) <= 63827/65000.
```

Consequently, in any fixed multiplicative shell,

```text
sum_(p_j asymp Y, g_j > C_w Y^(797/5000)) g_j
  <<_(w,epsilon) Y^(63827/65000+epsilon),             (0.1)
```

where `g_j=p_(j+1)-p_j`.  The complete logarithmic Voronoi mass attached
to these gaps is therefore

```text
O(Y^(-1173/65000+epsilon)),
1173/65000=.018046153846...>.0180303234.              (0.2)
```

This strictly improves the `Y^(1/4)` truncation obtainable from
Stadlmann's mean-square-gap theorem.  Splitting the boundary cells in the
rational-alias localization into short-gap and exceptional long-gap cells
also raises the rigorously deletable rational denominator from `Y^(1/10)`
to `Y^(1537/10000)`.  Every surviving **one-gap** near recurrence has reduced
denominator in

```text
Y^(1537/10000) < q <<_w Y^(797/5000).                (0.3)
```

The corridor width is `57/10000=.0057`, versus `.06` in the original
`.1<q<=.16` gate.  These rational exponents sit just inside the optimized
continuous boundary for this Gafni--Tao/half-cell argument; Section 2 gives
the exact optimization and both safety margins.

Equation (0.3) must not be promoted to a statement about all rational
blocks.  A recurrence spanning several consecutive gaps can have a
denominator larger than `Y^(797/5000)`.  On a curvature block its natural
Dirichlet denominator can still be as large as `Y/sqrt(t)`.

No bound for the final retained signed sum is proved here, and no
zero-free strip is claimed.

---

## 1. Exact half-cell form of the antenna error

Keep the notation

```text
v_j=log(p_j/Y),
C_j=the logarithmic Voronoi cell of v_j,
lambda_j=integral_(C_j) phi(u)du,
P_Y(t)=sum_j lambda_j exp(i t v_j).
```

Let `v(u)=v_j` on `C_j`.  There is an exact identity

```text
P_Y(t)-integral_(-w)^w phi(u)exp(i t u)du
 =integral_(-w)^w
   phi(u)[exp(i t v(u))-exp(i t u)]du.                (1.1)
```

For an interior consecutive gap put

```text
Delta_j=v_(j+1)-v_j=log(p_(j+1)/p_j),
m_j=(v_j+v_(j+1))/2.
```

The two half-gap contributions to (1.1) are exactly

```text
integral_(v_j)^(m_j)
 phi(u)[exp(i t v_j)-exp(i t u)]du

+integral_(m_j)^(v_(j+1))
 phi(u)[exp(i t v_(j+1))-exp(i t u)]du.               (1.2)
```

Their absolute sum is at most

```text
2 ||phi||_infinity Delta_j.                           (1.3)
```

On a fixed multiplicative shell,

```text
Delta_j<=g_j/p_j<<_w g_j/Y.                           (1.4)
```

Thus (0.1) deletes every half-cell belonging to a gap larger than
`C_w Y^(797/5000)` at the cost (0.2).  This uses the exact Voronoi integral;
there is no approximation of the oscillatory factor in this step.

---

## 2. Gafni--Tao gives the needed large-gap mass

For fixed `theta`, Gafni and Tao define `mu(theta)` so that the set of
`x in [X,2X]` on which the prime number theorem fails in an interval of
length `x^theta` has measure

```text
O(X^(mu(theta)+epsilon)).                              (2.1)
```

Their Theorem 1.2 gives

```text
mu(theta)
 <= inf_(epsilon>0)
    sup_(A(sigma)>=1/(1-theta)-epsilon)
    [(1-theta)(1-sigma)A(sigma)+2sigma-1].            (2.2)
```

On the local part of the Table-1 envelope relevant here, the exact
optimization (valid throughout `2/15<=theta<=353/1445`) is

```text
s_GT(theta)=(45 theta-6)/65,
mu(theta)<=1-s_GT(theta).                              (2.3)
```

The binding point is the common Ingham/Guth--Maynard endpoint

```text
sigma=7/10,                 A(sigma)=30/13,            (2.4)
```

because

```text
1-[(1-theta)(3/10)(30/13)+2(7/10)-1]
 =(45 theta-6)/65.                                    (2.5)
```

Take the simple interior rational

```text
theta=797/5000,             1/(1-theta)=5000/4203.
```

Substitution of every rational piece of the unconditional `A(sigma)`
envelope in Table 1 gives

```text
(1-theta)(1-sigma)A(sigma)+2sigma-1 <=63827/65000,
s_GT(theta)=1173/65000.                               (2.6)
```

The exact checker verifies all later Table-1 pieces as well; in
particular, it does not rely on the paper's informal phrase "sufficiently
small Delta" in its sample calculation near `theta=2/15`.

Now let `[p,p+g]` be a prime gap in a fixed shell and put

```text
H=C_0 Y^(797/5000)
```

with `C_0` large enough that `x^(797/5000)<=H` throughout a harmless
enlargement of the shell.  If `g>=2H`, then every

```text
x in [p,p+g-H]
```

starts an interval `[x,x+x^(797/5000)]` containing no prime.  Prime powers
contribute only `O((log Y)^2)` to its Mangoldt sum: for each `k>=2`, an
interval of length `H` contains at most

```text
O(H Y^(1/k-1)+1)
```

`k`-th powers, and there are `O(log Y)` possible `k`.  Hence, for large
`Y`, all these starts lie in the fixed `delta=1/2` exceptional set in
(2.1).

The start intervals from distinct prime gaps are disjoint.  Therefore

```text
sum_(g_j>=2H)(g_j-H)
 <= measure(exceptional set)
 <<Y^(63827/65000+epsilon).                            (2.7)
```

Since `g_j<=2(g_j-H)` on this range, (2.7) proves (0.1) after renaming
`2C_0` as `C_w`.  The dyadic or fixed-multiplicative shell changes only
the implied constant.

The imported primary source is Ayla Gafni and Terence Tao,
[*On the number of exceptional intervals to the prime number theorem in
short intervals*](https://arxiv.org/abs/2505.24017), Essential Number
Theory 5 (2026), 221--241, Theorem 1.2 and Table 1.

### Exact optimization of the two cutoffs

Let the required strip saving be

```text
kappa=0.0180303234=90151617/5000000000.
```

Within the certified local Gafni--Tao envelope (2.3), the infimum gap
exponent that clears `kappa` is

```text
theta_0=(65 kappa+6)/45
       =796885669/5000000000
       =.1593771338.                                  (2.8)
```

If `Q=Y^beta`, the half-cell collar at the top aperture has saving

```text
c_collar=2-50/33-2 beta-theta
        =16/33-2 beta-theta.                          (2.9)
```

The main inverse-image length has saving `8/33-beta`, which is nonbinding
here.  Consequently the supremal rational-cutoff exponent on the boundary
of this certificate is

```text
beta_0=(16/33-theta_0-kappa)/2
      =25363884781/165000000000
      =.153720513824....                              (2.10)
```

The infimum possible one-gap corridor width in this argument is therefore

```text
theta_0-beta_0
 =116667787/20625000000
 =.0056566199757....                                  (2.11)
```

The strict strip inequality means the boundary values themselves cannot
be used.  The chosen rational pair

```text
theta=797/5000=.1594,
beta =1537/10000=.1537                                (2.12)
```

has corridor width `.0057` and exact positive margins

```text
s_GT(theta)-kappa
 =1028979/65000000000=.000015830446...,

c_collar-kappa
 =2996639/165000000000=.000018161448....              (2.13)
```

Thus (2.12) is a convenient interior rational certificate very close to
the continuous optimum, rather than a claim that the decimal endpoints
are attained.

### Corollary 2.1 (improved rational-alias mass)

Let `M_t(Q)` be the physical rational-alias union from the prior report.
It has

```text
|M_t(Q)|<<Q sqrt(t),
R_t(Q)<< (t/Y)Q^2                                    (2.14)
```

connected components.  Enlarging this union to all Voronoi cells that
meet it adds at most two boundary cells per component.  Decompose those
cells into their physical half-cells, one half for each adjacent prime
gap.  This is important: no whole-cell maximal-gap bound and no
Cauchy--Schwarz boundary estimate is used below.

The cell cover here is taken for `M_t(Q)` itself, before any long half-cells
are removed.  One must not first form `M_t(Q) minus L_Y` and recount its
components, since the long-gap deletion could fragment that set.  The
original cell-cover inclusion has collars only at the endpoints of the
original `M_t(Q)` components; subtracting `L_Y` afterward creates no new
collars.

Put

```text
H=C_w Y^(797/5000).
```

There are `O(R_t(Q))` boundary half-cells.  A half-cell belonging to a gap
at most `H` has physical length `O(H)`, so all such half-collars have total
length `O(R_t(Q)H)`.  The large half-collars have total length

```text
O(sum_(g_j>H) g_j).                                   (2.15)
```

because every prime gap supplies only two half-cells and repetitions only
reduce the union.  Equations (0.1), (2.14), and (2.15) therefore give

```text
sum_(C_j meets M_t(Q)) lambda_j
 << Q sqrt(t)/Y
    +(t/Y)Q^2 H/Y
    +Y^(-1173/65000+epsilon).                         (2.16)
```

Take

```text
Q=Y^(1537/10000),           t<=Y^(50/33).
```

The three savings in (2.16), at the largest legal `t`, are respectively

```text
1-25/33-1537/10000
 =29279/330000=.0887242424...,

2-50/33-2(1537/10000)-797/5000
 =1489/82500=.0180484848...,

1173/65000=.0180461538....                            (2.17)
```

All exceed `.0180303234`.  Thus (2.16) proves

```text
sum_(C_j meets M_t(Y^(1537/10000))) lambda_j
 <<Y^(-1173/65000+epsilon)                            (2.18)
```

uniformly on `Y<=t<=Y^(50/33)`.  This is a strict strengthening of the
earlier `Q=Y^(1/10)` localization theorem.

One cannot set `Q=Y^(797/5000)` by the same argument: the small half-collar
saving would fall to

```text
2-50/33-3(797/5000)
 =1097/165000=.00664848...,                           (2.19)
```

well below the strip threshold.  The proved cutoff is `1537/10000`, not
the gap exponent `797/5000`.

---

## 3. The exact retained successor sum

For `t>=Y`, take

```text
Q=Y^(1537/10000),
eta_t=sqrt(t)/Y,
omega_t(x)=t/(2 pi x).
```

Let `B_t(Q)` be the union of the Voronoi cells meeting a point at which

```text
|omega_t(x)-a/q|<=eta_t/q
```

for some reduced `a/q`, `q<=Q`.  Let `L_Y` be the union of the two
logarithmic half-cells belonging to every physical gap

```text
g_j>C_w Y^(797/5000).
```

The exact retained error is

```text
R_Y(t)=integral_([-w,w] minus (B_t(Q) union L_Y))
 phi(u)[exp(i t v(u))-exp(i t u)]du.                  (3.1)
```

Corollary 2.1, (0.2), and the Fourier decay of the tent give, uniformly for
`Y<=t<=Y^(50/33)`,

```text
P_Y(t)
 =R_Y(t)
  +O(Y^(-29279/330000+epsilon))
  +O(Y^(-1489/82500+epsilon))
  +O(Y^(-1173/65000+epsilon))
  +O(Y^-2).                                           (3.2)
```

The old endpoint pieces are smaller than all displayed errors.  Hence a
proof of

```text
sup_(Y<=t<=Y^(50/33)) |R_Y(t)|<=Y^(-c),               (3.3)
```

for one fixed

```text
.0180303234<c<1173/65000                             (3.4)
```

would close the super-conductor portion of the antenna.  The transition
range `Y^.751<=t<=Y` remains the companion target already isolated in the
rational-alias report.

---

## 4. What the denominator window does and does not mean

For a gap `[p,p+g]`, define its exact mean velocity

```text
alpha_j=(t/(2 pi g)) log((p+g)/p).
```

The mean-value theorem gives `alpha_j=omega_t(x_j)` for some
`x_j in (p,p+g)`; no Taylor remainder is being hidden.  Suppose its phase
increment is nearly integral:

```text
||g alpha_j||<=eta_t.                                 (4.1)
```

After reducing the nearest fraction `a/g`, its denominator `q` divides
`g`, and

```text
|alpha_j-a'/q|<=eta_t/g<=eta_t/q.
```

Thus the minor condition excludes `q<=Y^(1537/10000)`, while Section 2
deletes `g>C_w Y^(797/5000)`.  This proves the exponent window (0.3); the
fixed shell constant in its upper bound is intentionally retained.

For a block of gaps, however, the physical span is

```text
D=p_k-p_j=g_j+...+g_(k-1),                            (4.2)
```

which need not be at most `Y^(797/5000)`.  A near recurrence of the endpoints
can have reduced denominator dividing `D`, not one of its constituent
gaps.  On a curvature block of physical length

```text
L_c=Y/sqrt(t),                                        (4.3)
```

Dirichlet approximation still allows

```text
Y^(1537/10000)<q<=L_c.                               (4.4)
```

At `t=Y`, the upper end in (4.4) is `Y^(1/2)`; at
`t=Y^(50/33)` it is `Y^(8/33)`.  Large-gap truncation therefore does not
reduce the complete block problem to (0.3).

---

## 5. Forward/reverse prime-running decomposition

Away from the one kink of `phi`, Taylor expansion of the nonoscillatory
cell masses gives

```text
lambda_j
 =phi(v_j)(Delta_(j-1)+Delta_j)/2
  +O(Delta_(j-1)^2+Delta_j^2).                        (5.1)
```

The kink cell and endpoints obey the same total exponent after a separate
one-cell estimate.  Stadlmann's mean-square-gap theorem then gives the
uniform leading formula

```text
P_Y(t)
 =1/2 sum_j Delta_j
    [F_t(p_j)+F_t(p_(j+1))]
  +O(Y^(-77/100+epsilon)),                            (5.2)

F_t(x)=phi(log(x/Y))exp(i t log(x/Y)).
```

Thus the leading Voronoi measure is the arithmetic mean of a forward and
a reverse gap-running measure.

On a physical block `[X,X+L]`, put `alpha=t/(2 pi X)`.  Uniformly on the
block,

```text
exp(i t log(p/Y))
 =exp(i t log(X/Y))exp(2 pi i alpha(p-X))
  [1+O(t L^2/Y^2)].                                  (5.3)
```

Thus a block with `L=o(Y/sqrt(t))` has a genuine frozen additive model.
At the exact frozen rational frequency `alpha=a/q`, define the two
transition masses

```text
M^L_(r,s)=sum_(p_j == r mod q, p_(j+1) == s mod q)
           Delta_j phi(v_j),

M^R_(r,s)=sum_(p_j == r mod q, p_(j+1) == s mod q)
           Delta_j phi(v_(j+1)).                     (5.4)
```

The frozen rational Fourier mode in (5.2), apart from the common block
phase in (5.3), is exactly

```text
1/2 sum_(r,s mod q)
 [M^L_(r,s)exp(2 pi i a r/q)
  +M^R_(r,s)exp(2 pi i a s/q)].                       (5.5)
```

Equivalently, (5.5) is the average of the discrete Fourier transforms of
a left row marginal and a right column marginal.

There is no exact cancellation in (5.5).  Even in the constant-amplitude
specialization `M^L=M^R=M`, the gap-by-gap multiplier is

```text
[exp(2 pi i a r/q)+exp(2 pi i a s/q)]/2
 =exp(pi i a(r+s)/q) cos(pi a(s-r)/q),                (5.6)
```

and the cosine factor can have modulus one.  Summation by parts of the
forward-minus-reverse mode produces first differences of consecutive
gaps, for which no useful total-variation estimate is known.

Jaeyoon Kim's
[*Prime Running Functions*](https://arxiv.org/abs/2006.13355),
Experimental Mathematics 31 (2022), 1291--1313, studies precisely the
unweighted row marginals in (5.4).  Even for a fixed modulus `q>=3`, the
equidistributed main term is Conjecture 2.2.  The paper's modified Cramer
model predicts opposite `x/log x` biases for forward and reverse running
functions.  Consequently that model predicts cancellation of the first
bias term in the symmetrization (5.2), but it proves neither the
deterministic cancellation nor a power saving, and it does not cover
growing `q`.

This comparison is a useful warning: ordinary Bombieri--Vinogradov
estimates for `Lambda` do not directly control (5.5).

### 5.1 Why the standard elementary attacks stop

The obstruction can be quantified rather than described vaguely.

First, Stadlmann's second moment alone gives, for `G=Y^gamma`,

```text
(1/Y) sum_(g_j>G) g_j
 <=(1/(YG)) sum_j g_j^2
 <<Y^(.23-gamma+epsilon).                             (5.7)
```

Thus an absolute moment truncation needs
`gamma>.23+kappa=.2480303234`; it cannot produce the `.1594` cutoff.
Gafni--Tao's exceptional-*measure* theorem is the ingredient that genuinely
crosses this gap.

Second, even granting the standard Selberg-sieve upper bound for each fixed
even `g`,

```text
#{p asymp Y: p and p+g prime}
 << S(g)Y/(log Y)^2,                                  (5.8)
```

discarding the word *consecutive* and summing the absolute gap weights up
to `G` only gives a bound of order

```text
(1/Y) sum_(g<=G) g S(g)Y/(log Y)^2
 <<G^2/(log Y)^2,                                     (5.9)
```

not a negative power.  Upper-bound sieve estimates neither preserve the
successor partition nor create cancellation between residue classes.

Third, write `z_j=exp(i t v_j)`.  The exact increment relation

```text
z_(j+1)=z_j exp(i t Delta_j)                          (5.10)
```

allows Abel summation only if one controls the variation of the reciprocal
increments `1/(exp(i t Delta_j)-1)`.  The retained minor condition does not
give that: individual near recurrences can still have denominator in (0.3),
and no power bound for the total variation of consecutive prime gaps is
known.  Forward/reverse symmetrization changes the numerator but not this
denominator obstruction.

Finally, the second gap moment does make the classical additive large sieve
look tantalizing.  For the frozen coefficient sequence in (5.2),

```text
sum_j |lambda_j|^2 <<Y^(-.77+epsilon),                (5.11)
```

so Parseval gives an excellent root-mean-square bound in additive frequency.
But the required statement (3.3) is pointwise for every `t`.  Bernstein or
Cauchy conversion of this `L^2` estimate to `L^infinity` costs at least the
square root of the physical frequency length and gives only
`Y^(.115+epsilon)`.  A dispersion theorem for the successor weights in
(5.5), with pointwise minor-arc output rather than an averaged-modulus
output, would be new input; the classical large sieve does not supply it.

---

## 6. Literature scope and checked no-go statements

| Input | What it genuinely supplies | What it does not supply |
|---|---|---|
| Gafni--Tao, Theorem 1.2 | The power exceptional-set measure used in (2.7); the optimized interior certificate gives `1173/65000` | No oscillatory cancellation on the retained gaps |
| Stadlmann, mean-square gaps | `sum g_j^2<<Y^(123/100+epsilon)` | By absolute tail truncation alone it needs `G>Y^(.23+c)`; it cannot reach `Y^(797/5000)` |
| Järviniemi, large differences between consecutive primes | Strong mass bounds at gap thresholds `Y^.45` and `Y^.5` | No theorem at the `Y^.1594` threshold needed here |
| Li, primes in almost all short intervals | Prime-containing intervals down to exponent `1/21.5+epsilon`, outside `O(Y log^-B Y)` starts | The stated exceptional measure is logarithmic, not the fixed power required here |
| Kim, prime running functions | Identifies the exact gap-weighted residue statistic and its modeled forward/reverse bias | Fixed-modulus main term is conjectural; no growing-modulus Fourier bound |
| Green--Tao, restriction theory of the Selberg sieve | Sharp `L^p`, `p>2`, estimates for prime-tuple exponential sums | An `L^p` estimate is not the pointwise-in-`t` bound (3.3), and the coefficients here are consecutive-gap masses |

The only theorem-grade no-go conclusions used here are scoped:

1. Mean-square gaps plus an absolute Markov tail cannot by itself truncate
   below exponent `.23+c`.
2. The interval `.1537<q<=.1594` (in exponent notation) describes
   individual gap recurrences only; promoting it to all blocks is false by
   (4.2).
3. The forward/reverse opposite-bias statement is a probabilistic-model
   prediction, not a proved cancellation theorem.

No cited result eliminates the actual retained sum (3.1).

---

## 7. Reproduction

The exact rational zero-density optimization and strip-margin comparison
are checked by

```bash
python3 results/verify_zeta23_high_denominator_gap_tail.py
```

Expected output includes

```text
mu_bound=63827/65000
tail_saving=1173/65000
rational_cutoff=1537/10000
margin_over_strip_threshold=0.000015830446...
```

The checker audits the rational exponent ledger.  It does not reprove the
imported zero-density or exceptional-set theorems.
