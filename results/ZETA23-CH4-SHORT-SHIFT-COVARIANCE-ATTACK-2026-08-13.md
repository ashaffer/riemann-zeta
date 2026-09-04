# CH4 short-shift covariance attack and thin-product no-go

**Date:** 2026-08-13  
**Verdict:** the common-height fourth moment has a strictly weaker physical
`L2` successor with substantial exponent room.  That successor remains open.
A theorem uniform over arbitrary block-dependent separated coefficients is
rigorously false, even when the product support consists of actual pairs of
primes.  The exact first-return coefficient is therefore indispensable.

No post-`q` tail estimate or zero-free strip is proved here.

## 1. Sharp bands-first successor

Fix one legal common height `t`, and restrict to a dyadic curvature regime

```text
H_I asyp Y^h,             8/33<=h<=5797/10000.
```

Let `q_I(t),a_I(t)` be the reduced fraction selected from this one height.
After inserting the taper, smooth amplitude, exact residual logarithmic
chirp, the unique band crossing `q_I`, and block-boundary transport, write

```text
B_I(t)=sum_P hat(Delta^t_(I,P))(a_I(t))
      =sum_n d_(I,t)(n) exp(i t log n).                 (1.1)
```

The sum over `P` in (1.1) is taken **before** every moment.  The exact SPF
telescope makes its interior atomic measure the difference of two positive
Voronoi measures, the prime endpoint and the `q_I`-rough endpoint.  Both have
mass `O(H_I)` on the bounded taper support.  The discarded/crossing boundary
mass is `O(Y^.1594)=o(H_I)` and the residual chirp has modulus one.  Hence

```text
|B_I(t)|<<H_I.                                           (1.2)
```

It follows pointwise that

```text
sum_I |B_I|^4/H_I^3
 <<Y^(-h) sum_I |B_I|^2.                                (1.3)
```

Consequently the following regime-adaptive covariance theorem is sufficient:
for some fixed `epsilon>0`, uniformly in the one legal common height,

```text
sum_(I:H_I asyp Y^h) |B_I(t)|^2
 <<Y^(1+h-4*kappa-epsilon+o(1)),                        (SC_h)

kappa=.01974048259....
```

Indeed `(SC_h)` and (1.3) give CH4 with `delta=epsilon/4`.  A uniform
near-linear estimate `sum_I|B_I|^2<<Y^(1+o(1))` is more than needed.  Over the
full aperture its exact margin is

```text
h_min-4*kappa=8/33-4*kappa=.1634623111....              (1.4)
```

and it would permit every

```text
0<delta<2/33-kappa=.040865577....                       (1.5)
```

This is physical selected energy.  It is not the falsified arbitrary-selector
residue `L2`, which sums all residue frequencies and separates the dyadic
bands.

## 2. Exact short-shift form

Expanding only after the complete telescope gives

```text
sum_I |B_I(t)|^2
 =sum_I sum_(n,m in supp I)
   d_(I,t)(n) conjugate(d_(I,t)(m))
   exp(i t log(n/m)).                                  (2.1)
```

Thus `(SC_h)` is exactly a signed short-shift covariance theorem for the
actual `q_I(t)`-rough-to-prime first-return transport.  Its quantifiers are:

1. one shared `t` selects every `(a_I,q_I)`;
2. `d_(I,t)` contains the taper and residual chirp;
3. the crossing band occurs once;
4. early, late, and cross-band terms remain inside (2.1);
5. the right side is `Y^(1+h-4*kappa-epsilon)`, not merely `o(Y^(1+h))`.

Taking absolute values over shifts is not an innocuous relaxation.  There is,
however, a useful exact diagonal gain which is stronger than the raw
Stadlmann exponent.  Every retained terminal-prime edge has length at most

```text
G=Y^theta,                 theta=797/5000=.1594.
```

For either positive endpoint Voronoi measure, every atom on an edge has mass
at most its edge length, while the total mass is `O(Y)`.  Bounded tapers and
the bounded overlap of the block cover therefore give

```text
D(t):=sum_I sum_n |d_(I,t)(n)|^2
 <<Y*G*Y^o(1)=Y^(1.1594+o(1)).                        (2.2)
```

This diagonal fits below the shallow `(SC_h)` allowance by the small but
strict exponent

```text
8/33-4*kappa-theta=.004062312064....                  (2.3)
```

Consequently it is enough to prove the one-sided signed off-diagonal bound

```text
Re sum_I sum_(n!=m)
 d_(I,t)(n)conjugate(d_(I,t)(m))exp(i*t*log(n/m))
 <<Y^(1+theta+o(1)).                                  (2.4)
```

Equations (2.2)--(2.4) give CH4 for every fixed

```text
0<delta<(8/33-4*kappa-theta)/4
       =.001015578016....                             (2.5)
```

An absolute shifted-correlation estimate does not follow from (2.2), and the
adversarial construction below shows why: off-diagonal terms can coherently
rebuild the full block factor.  The exact arithmetic signs must be retained.

## 3. A definitive no-go for arbitrary local product factors

The late Buchstab range has a useful but dangerous separation.  Put

```text
p asyp Y^(1/3),       r asyp Y^(2/3),       pr in I,
H=Y^h,                h<=.5797<2/3.          (3.1)
```

For fixed `r`, the interval of possible `p` values has length `H/r<1`.
Therefore each block contains at most one `p` above a given `r`: the product
rectangle is one point per column.

Let `E_I` be the actual prime pairs in (3.1), and let `N_I=#E_I`.  Given any
selected rational carrier and any unit residual chirp `omega_I(pr)`, choose
the bounded block-dependent factor

```text
alpha(p)=1,
beta_I(r)=conjugate(e_(q_I)(a_I*p(r)*r)*omega_I(p(r)*r))
                                                        (3.2)
```

on the unique occupied fibre.  Then `|beta_I(r)|=1` and exactly

```text
sum_((p,r) in E_I)
 alpha(p) beta_I(r)e_(q_I)(a_I*p*r)omega_I(pr)=N_I.     (3.3)
```

This is not a probabilistic model.  The support in (3.3) consists of actual
primes.  The prime number theorem gives, across `[Y,2Y]`,

```text
N=sum_I N_I asyp Y/(log Y)^2                           (3.4)
```

for one fixed dyadic `p` interval.  There are `K asyp Y/H` blocks, so Cauchy
and (3.3) give

```text
sum_I |S_I|^2=sum_I N_I^2
 >=N^2/K >>Y*H/(log Y)^4=Y^(1+h-o(1)).                (3.5)
```

The closing allowance is `Y^(1+h-4*kappa-epsilon)`.  Thus an estimate uniform
over arbitrary bounded or `L2`-controlled **block-dependent** `beta_I` misses
by at least `Y^(4*kappa-o(1))`.  Bazin, Bettin--Chandee, Wright, or a large
sieve cannot be imported after replacing the exact first-return factor by an
arbitrary local sequence: that proposed interface is false.

The scope is exact.  Formula (3.2) is not the actual nearest-survivor weight.
This does not disprove `(SC_h)` for the SPF process; it proves that its escape
must use the arithmetic law relating `beta_I` across occupied fibres and
blocks, or cancellation between Buchstab bands.

## 4. Primary-literature boundary through 2026-08-13

The closest located results do not furnish (2.1).

| Input | What it proves | Exact mismatch |
|---|---|---|
| [Gorodetsky, rough-number variance](https://arxiv.org/abs/2111.00853), Theorem 1.2 | An unconditional asymptotic for continuously averaged short-interval counts of integers with no prime factor at most `y` | For `H=Y^h,y=Y^b`, its condition (1.9) has left side asymptotic to `h log Y/loglog Y` and bounded right side `(1-delta)/b`; it therefore excludes every fixed `b>=.1537`.  It also has neither Voronoi first-return weights nor the selected chirp. |
| Friedlander--Iwaniec, *Opera de cribro*, Proposition 6.26/Corollary 6.28, as quoted explicitly in Gorodetsky | Almost-all rough counts when `y<=Y^(1/20)` | The live cutoff begins at `Y^.1537`, and count variance is not transport covariance. |
| [Xuan/Wolke, rough integers in APs](https://doi.org/10.1017/S0027763000007212) | A Bombieri--Vinogradov theorem for unweighted rough counts, uniform in the prefix and numerator after averaging moduli | It saves logarithms, counts each modulus once, and has no nearest-survivor weight or repeated block-selected modulus. |
| [Matomaki, almost primes in almost all very short intervals](https://arxiv.org/abs/2012.11565) | Vector-sieve remainders and empty-window estimates, sufficient for the proved rough-gap square theorem | Empty-window/diagonal control does not estimate the signed off-diagonal covariance (2.4). |
| [Matomaki--Shao--Tao--Teravainen I](https://arxiv.org/abs/2204.03754) | Higher uniformity for `Lambda` in every interval from length `Y^(5/8+epsilon)` | All live blocks have `h<=.5797<5/8`; the coefficient is also `Lambda`, not first return. |
| [Matomaki--Radziwill--Shao--Tao--Teravainen II](https://arxiv.org/abs/2411.05770) | Higher uniformity from `Y^(1/3+epsilon)` for almost all intervals, with logarithmic strength | It misses the shallow high-height blocks, permits exceptional blocks, and a logarithmic saving is not the fixed `Y^(-4*kappa)` covariance margin. |
| [Le Duc Hieu, short-interval APs](https://arxiv.org/abs/2509.04883) | Uniform prime/AP structure for interval exponent `>17/30` and an unweighted short-interval BDH appendix | It touches only `h>17/30` at the very top of the companion range and does not contain gap weights, selected growing rational phases, or fixed-power first-return covariance. |
| [Bazin, products of primes](https://arxiv.org/abs/2607.15137), Theorem 8/Lemma 10 | A fixed-power whole-prefix modulus average for separated prime products | Block localization loses the shell-to-block normalization; (3.2)--(3.5) additionally rule out a norm-only block-dependent-factor repair. |
| [Bettin--Chandee](https://arxiv.org/abs/1502.00769) and [Wright](https://arxiv.org/abs/2604.25177) | Trilinear Kloosterman-fraction estimates for separated one-variable factors | Their factors are not the jointly generated first-return law; allowing an arbitrary new factor on every thin block is exactly the false theorem in Section 3. |
| [Friedlander--Iwaniec, restricted-support large sieve](https://doi.org/10.4171/RLM/1079) | A logarithmic improvement for special coefficient support in a complete character/modulus average | Its hypothesis `8Q^2<=N` fails on a block with `q^2>H`, and a logarithmic complete-family gain does not give the selected fixed-power OD2 bound. |
| [Stadlmann, mean-square prime gaps](https://arxiv.org/abs/2212.10867) | `sum g_n^2 <<Y^(1.23+epsilon)` | It supplies no signed short-shift covariance.  The separately imposed retained-edge cutoff improves the atomic diagonal to (2.2), but neither result bounds the off-diagonal expression (2.4). |
| [Gafni--Tao, rough numbers between consecutive primes](https://arxiv.org/abs/2508.06463) | An unsigned power envelope used here for the long-gap sector | It is already used to discard the long-edge sector; the surviving coherent-gap model shows that this unsigned ledger does not imply OD2. |
| [Kim, prime running functions](https://arxiv.org/abs/2006.13355) | Random-model theorems and empirical/conjectural successor-gap biases at fixed modulus | Even the fixed-modulus actual-prime main term is not proved; the live modulus grows as a power and is height-selected. |

The survey found no primary theorem accepting simultaneously the exact
two-state first-return cocycle, a polynomial growing selected denominator,
short physical blocks down to `Y^(8/33)`, and one-height pointwise
quantification.

## 5. Smallest honest research target

The next lemma should be stated directly for the actual coefficient, not for
arbitrary separated factors:

```text
sup_(legal t) sum_(I:H_I asyp Y^h)
 |sum_P sum_n d_(I,t,P)(n) exp(i*t*log n)|^2
 <<Y^(1+h-4*kappa-epsilon),                           (5.1)
```

where `sum_P` includes the crossing band before the square.  A plausible
proof must expose a signed renewal/dispersion identity for the exact
two-state cocycle.  Proving unweighted rough-count variance, estimating each
band absolutely, or inserting arbitrary local `beta_I` cannot establish
(5.1).  The numerically weakest clean version is now (2.4): keep the total
covariance at the already proved retained-diagonal scale.

## 6. Reproduction

```bash
PYTHONPATH=src python3 -m unittest -v \
  src/test_thin_short_product_covariance_nogo.py
python3 results/verify_zeta23_thin_short_product_covariance_nogo.py
```

The tests certify unique large-factor fibres on an actual finite prime-product
set, exact phase conjugation including a logarithmic residual chirp, the
Cauchy aggregate floor, and the exact `4*kappa` exponent miss.  They do not
assert anything about the actual first-return coefficient.
