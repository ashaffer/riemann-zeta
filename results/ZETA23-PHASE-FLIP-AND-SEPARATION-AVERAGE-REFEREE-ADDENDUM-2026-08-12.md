# Referee addendum: target-only phase flips and separation averaging

Status: **PASS AFTER TWO NORMALIZATION/SCOPE PATCHES**, 2026-08-12.

This addendum audits

- `ZETA23-TARGET-ONLY-PHASE-FLIP-GATE-2026-08-12.md`; and
- `ZETA23-SEPARATION-AVERAGE-POSITIVE-COSINE-NOGO-2026-08-12.md`.

Both principal results are correct in their stated fixed-width packet scope.
The first draft of the phase-flip report omitted the `sqrt(L)` coefficient
representative needed for its displayed common normalization.  The first
draft of the averaging report described a conditional point-packet
divergence as though it followed from the more general cross-weighted
hypothesis.  Both defects are patched.  Neither affected the main sign,
carrier-scale, or averaging no-go arguments.

## 1. Target-only phase flip

### 1.1 Exact compression and normalization

After demodulation by the selected ordinate, the reflected-pair kernel is

```text
(2/L^2) exp(-i*delta*(t-s)) cosh(beta*(t-s)).
```

For a standard-`L^2` unit packet `phi`, the repository coefficient
representatives are `sqrt(L)` times its translates.  Their two factors of
`sqrt(L)` turn `2/L^2` into the displayed compression scale

```text
m_beta=2*A_beta^2/L,
A_beta=integral phi(s)exp(beta*s)ds.
```

With symmetric centers `-D/2,D/2`, direct integration at `delta=0` gives

```text
M_(beta,0)=m_beta [[1,cosh(beta D)],
                         [cosh(beta D),1]].
```

For arbitrary `delta`, center-freezing the modulation gives the ideal matrix

```text
m_beta [[1,C_beta exp(i delta D)],
        [C_beta exp(-i delta D),1]],
```

and a complete-pair remainder bounded by

```text
||E|| <= |delta| w m_beta(1+C_beta).
```

The bound follows entrywise from
`|exp(-i delta(t-s))-exp(-i delta(t_j-t_k))|<=|delta|w`;
positivity of `phi` and `cosh` makes the undisturbed absolute entry exactly
the corresponding `delta=0` entry.  Thus same-lobe and reverse-cross pieces
have not been silently deleted.

### 1.2 Sign and carrier fraction

For the selected pair, the exact positive and negative directions are

```text
e_+=(u+v)/sqrt(2),
e_-=(u-v)/sqrt(2),
```

and the selected carrier is

```text
kappa=m_alpha(cosh(alpha D)-1).
```

On `e_-`, a collateral pair has ideal expectation

```text
m_beta(1-cosh(beta D)cos(delta D)).
```

At `delta=+/-pi/D` this becomes `m_beta(1+cosh(beta D))`, with relative
remainder `O(w/D)`.  The sign is therefore the opposite of the selected
pair at carrier scale.

One equal-depth collateral gives

```text
-kappa+m_alpha(1+C_alpha)+O(kappa w/D)=o(kappa).
```

This kills a uniform `-c*kappa` isolation margin but makes no residual sign
claim.  The report states that distinction correctly.

For the strict-deepest version, take two distinct collateral ordinates at
`+pi/D` and `-pi/D`, both at depth

```text
beta=alpha-epsilon_L,
epsilon_L>0,
epsilon_L D -> 0.
```

Then each collateral expectation is `(1-o(1))*kappa`, while the selected
expectation is `-kappa`.  The sum is therefore

```text
(1-o(1))*kappa>0.
```

The two pairs are distinct, the target is strictly deeper than both, and all
full-pair and local-width errors are `o(kappa)`.  Since `e_-` attains the
top eigenvalue of the rank-one selected carrier, it is feasible even at
`theta=1`, and hence for every `0<theta<=1`.

### 1.3 Divisor compatibility

The ordinate offsets are `O(1/L)` and the cluster contains only three
reflected pairs.  Current Riemann--von Mangoldt error terms, local-count
upper bounds, horizontal density estimates, simplicity proportions, and
leading normalized moment data permit such an `O(1)` sparse cluster.  They
do not imply its existence.  Choosing the two collateral depths smaller by
`epsilon_L` is compatible with selecting the target as the unique deepest
pair.

The result is consequently a genuine normalized packet counterexample to a
geometry-only target-quotient mirror-sign theorem.  It is not a construction
of zeta zeros, an `L`-function divisor, or an actual prime/pole/gamma
remainder.

## 2. Positive separation averaging

### 2.1 Exact effective-delay measure

For selected depth `alpha_0`, collateral depth `alpha_j`, and ordinate gap
`omega`, the product of the two normalized local overlaps is

```text
M(q+i omega)^2/[M(2 alpha_0)M(2 alpha_j)],
q=alpha_0+alpha_j.
```

After extracting the positive log-convexity factor, this is the square of a
characteristic function under the positive tilted packet law.  Hence the
carrier-leading expectation is exactly the negative cosine transform of a
positive effective-delay measure supported at

```text
D+s_1+s_2,  s_1,s_2 in [-w/2,w/2].
```

Changing inner-product convention conjugates the formula or replaces the
sum by a difference; its positivity and support ledger are unchanged.

### 2.2 Support-gap theorem

Let `mu` be a nonzero finite positive measure and assume its cosine transform
is nonnegative everywhere.  Symmetrize it and convolve with the triangular
function supported in `[-epsilon,epsilon]`.  If the symmetrized support has a
gap around zero, the convolution is a continuous positive-definite function
whose value at zero vanishes.  Its `2 x 2` Gram inequality forces it to
vanish identically, contradicting positivity of the convolution integral.

Thus a universal positive cosine profile must put effective-delay support
arbitrarily close to zero.  This proof covers atomic and continuous positive
ensembles.

### 2.3 Quantitative carrier loss

The central-mass lemma is valid.  A symmetric probability on `[-A,A]` with
nonnegative Fourier transform has

```text
sigma([-epsilon,epsilon]) >= epsilon/(8A).
```

For effective delays `D+[-w,w]`, this forces at least order
`epsilon/(A+w)` of the cross-normalized separation mass into
`D<=w+epsilon`.  On that set the cross coefficient has only local packet
size `b_loc`.  If the covariance trace is one, changing from trace weights
to cross-normalized weights gives exactly

```text
1=B_0 integral b_0(D)^(-1) nu(dD),
```

and therefore

```text
B_0 <= C b_loc(A+w)/epsilon.
```

Since the selected negative eigenvalue is uniformly at most a constant
times the cross coefficient, the ensemble carrier is at most
`b_loc L^O(1)`.  A fixed separation `D=dL` instead carries
`b_loc exp(alpha dL+O(1))`.  Universal positive averaging therefore loses
the fixed power `X^(-alpha d+o(1))`.

The point-packet infinite-norm paragraph is valid only under the additional
assumption that the carrier-weighted phase measure itself has nonnegative
cosine transform.  Nonnegativity of the actual cross-weighted measure does
not imply that condition.  The report now labels this as a conditional
aside; the general fixed-power carrier cap above does not use it.

### 2.4 Remaining loophole

The support theorem has a universal frequency quantifier.  A positive
profile tailored to a finite known collateral list remains a finite convex
feasibility problem and is not excluded.  Nor does the theorem reduce the
full proportional-width packet space or control target-transverse
prime/pole/gamma directions.

## 3. Frontier correction

The earlier three-step synthesis needs a material update.

It remains correct that the all-positive-row quotient has a fixed-width
mirror sign.  It is no longer correct to present extension of that sign to
the target-only quotient as an unresolved promising branch: the extension
is false even for a strictly deepest target.  Two reciprocal-separation,
slightly shallower pairs screen the selected carrier at positive scale.

The most obvious repair--a universal positive average over packet
separations--is also unavailable at fixed-power carrier scale.  The surviving
possibilities are narrower:

1. prove an actual completed-arithmetic orientation theorem that excludes
   the phase-flip configuration;
2. solve the adaptive finite-collateral separation feasibility problem with
   all coherent off-block arithmetic terms retained; or
3. find additional zeta-specific local spacing/depth information not present
   in current count, density, or moment inputs.

No numerical or asymptotic bound on actual zeta zeros changes.
