# Selected character-twist method audit

**Date:** 2026-08-13

## Verdict

For a fixed selected modulus and character, the symmetrized statistic has two
useful exact rewritings: an Abel identity and a predecessor/successor-prime
integral.  Both show that the obstacle is not an ordinary character sum over
primes.  It is a character evaluated at a prime and weighted by the two
neighboring consecutive-prime gaps.

In the surviving shell

```text
Y^beta < q <= Y^theta,
beta=1537/10000=.1537,  theta=797/5000=.1594,
kappa=.0180303234,
```

Burgess, Vaughan/Heath--Brown identities, pretentious bounds, and Dirichlet
zero density do not give a black-box transfer to this coefficient.  The 2026
Chen--Gupta--Li theorem for arbitrary character polynomials does apply after
rescaling, but its unavoidable first term is already larger than the total
number of characters.  Thus it is quantitatively vacuous at the required
threshold.

This is a scoped methods obstruction.  It is **not** a no-go theorem for the
actual primes, and it does not show that the selected-frequency estimate is
false.  It says that a proof needs new information about the gap-conditioned
prime-running coefficient (or cancellation in its Gauss-weighted
recombination), not merely a stronger theorem for ordinary sums
`sum Lambda(n) chi(n)`.

---

## 1. Exact collection and Abel identities

Let `p_m,...,p_(n+1)` be consecutive primes in a physical block and put

```text
v_j=log(p_j/Y),  d_j=log(p_(j+1)/p_j),  phi_j=phi(v_j).
```

The frozen character mode is

```text
C(chi)=1/2 sum_(j=m)^n d_j
       [phi_j chi(p_j)+phi_(j+1) chi(p_(j+1))].       (1.1)
```

Collecting the two incident half-edges at each vertex gives exactly

```text
C(chi)=sum_(j=m)^(n+1) H_j chi(p_j),                 (1.2)

H_m       =phi_m d_m/2,
H_j       =phi_j(d_(j-1)+d_j)/2       (m<j<n+1),
H_(n+1)   =phi_(n+1)d_n/2.                           (1.3)
```

For the ordinary prime-character prefixes

```text
P_j(chi)=sum_(k=m)^j chi(p_k),
```

summation by parts is therefore

```text
C(chi)=H_(n+1)P_(n+1)(chi)
       +sum_(j=m)^n (H_j-H_(j+1))P_j(chi).           (1.4)
```

This is the strongest direct telescoping identity.  It does not remove the
gap weights.  If `phi` has bounded first derivative and the block has bounded
logarithmic length, then

```text
|H_(n+1)|+sum_j |H_(j+1)-H_j| << sum_j d_j << 1.     (1.5)
```

There is no power-small variation factor in (1.5).  The gap-square and
truncated higher-moment estimates improve quadratic norms of the `H_j`; they
do not turn the total variation in (1.5) into `Y^(-c)`.  Consequently a
black-box bound for `max_j |P_j(chi)|` cannot yield the desired dimensionless
power saving through (1.4).

### 1.1 Exact edge conditioning

Writing `g_j=p_(j+1)-p_j`, every block prime is a unit modulo `q`.  Hence

```text
chi(p_(j+1))
 =chi(p_j) chi(1+g_j p_j^(-1) mod q),                (1.6)
```

and an edge in (1.1) is exactly

```text
d_j chi(p_j)/2 *
[phi_j+phi_(j+1)chi(1+g_j p_j^(-1) mod q)].          (1.7)
```

Formula (1.7) displays the missing correlation: the character value at the
starting prime is coupled to its *successor gap*.  Neither multiplicativity
nor an identity for `Lambda(p_j)` separates these two variables.

---

## 2. Exact prime-running integral

For a real `x` between two consecutive primes, let

```text
p^-(x)=largest prime <=x,   p^+(x)=smallest prime >=x.
```

Since `d_j=int_(p_j)^(p_(j+1)) dx/x`, (1.1) is exactly

```text
C(chi)=1/2 int_(p_m)^(p_(n+1))
 [phi(log(p^-(x)/Y))chi(p^-(x))
 +phi(log(p^+(x)/Y))chi(p^+(x))] dx/x.               (2.1)
```

Thus the symmetrization averages the forward and reverse prime-running
operators; it does not convert them to a Dirichlet polynomial with a smooth
deterministic coefficient.  The map

```text
x -> chi(p^-(x))  (or chi(p^+(x)))                   (2.2)
```

is not multiplicative.  Halasz/pretentious estimates therefore have no
direct input.  Vaughan and Heath--Brown identities decompose `Lambda(n)`;
they do not decompose (2.2).  An expansion of `p^+(x)` or `p^-(x)` in prime
indicators must enforce the absence of every intermediate prime, recovering
the growing-order consecutiveness problem rather than eliminating it.

Kim's actual-prime forward prime-running main term is conjectural already for
each fixed `q>=3`; his proved theorems concern modified Cramer models.  The
forward/reverse average in (2.1) is a different and potentially better object,
but no actual-prime, growing-modulus power estimate for it was located.

---

## 3. Quantitative audit of character large values

The retained-gap cutoff implies

```text
max_j |H_j| << Y^(theta-1+o(1)),
sum_j |H_j|^2 << Y^(theta-1+o(1)).                   (3.1)
```

Scale `H_j` by `Y^(theta-1)` and regard (1.2) as a length-`N=Y`
Dirichlet polynomial with coefficients bounded by one.  A value

```text
|C(chi)| >= Y^(-kappa)                               (3.2)
```

corresponds to the unnormalized threshold

```text
V=Y^(1-theta-kappa+o(1))=Y^(.8225696766...+o(1)).    (3.3)
```

The first term in Chen--Gupta--Li, Theorem 1.1, is `N^2/V^2`.  Here it is

```text
Y^[2(theta+kappa)+o(1)]
 =Y^(.3548606468...+o(1)).                           (3.4)
```

For prime `q`, all nonprincipal characters are primitive, but there are only

```text
q=Y^(b+o(1)),  beta<b<=theta<=.1594                 (3.5)
```

characters.  Therefore (3.4) is larger than the entire family; no choice of
the auxiliary divisor in that theorem removes its first term.

The standard hybrid second moment uses the sharper second estimate in (3.1)
and permits

```text
# {chi: |C(chi)|>Y^(-kappa)}
 <<Y^(theta+2kappa+o(1))
 =Y^(.1954606468...+o(1)),                           (3.6)
```

which is still larger than `q` throughout the shell.  Recent large-value
technology therefore does not even rule out one bad character per selected
modulus, much less the prescribed Gauss-weighted superposition.

For comparison, at a prime modulus the triangle inequality in the exact
Gauss expansion would require

```text
sum_(chi nonprincipal)|C(chi)| <<sqrt(q)Y^(-kappa),  (3.7)
```

so the required average individual size at the bottom of the shell is

```text
Y^[-(beta/2+kappa)+o(1)]
 =Y^(-.0948803234...+o(1)).                          (3.8)
```

Zero-density theorems classify characters through zeros of `L(s,chi)` and
control ordinary twisted von Mangoldt sums.  There is no identity connecting
that classification to largeness of (2.1).  Even a better zero-density
exponent alone cannot supply (3.8).

---

## 4. What remains mathematically live

The audit leaves three legitimate ways forward:

1. prove a pointwise theorem directly for the symmetrized prime-running
   integral (2.1);
2. prove cancellation in the one prescribed Gauss-weighted sum without
   bounding all `C(chi)` separately;
3. exploit additional structure of the phase-selected `(q,r)` that is absent
   from a theorem uniform over arbitrary selected rational frequencies.

The exact target remains

```text
|1/phi(q) sum_(chi nonprincipal)
 tau_q(chibar;r) C_q^sym(chi)| <<Y^(-c),  c>kappa.    (4.1)
```

Nothing in this audit eliminates (4.1) for actual primes.

---

## Primary literature checked

- D. A. Burgess, [*On character sums and primitive roots*](https://www.mathnet.ru/eng/mat267).
- D. R. Heath-Brown, [*Prime numbers in short intervals and a generalized
  Vaughan identity*](https://doi.org/10.4153/CJM-1982-095-9).
- B. Chen, V. Gupta, and Y. C. Li, [*Large Value Estimates for Dirichlet
  Polynomials with Characters and Zero Density of Dirichlet
  L-Functions*](https://arxiv.org/abs/2507.08296v2), especially Theorem 1.1.
- J. Kim, [*Prime Running Functions*](https://arxiv.org/abs/2006.13355),
  especially Conjecture 2.2 and the model theorems in Section 4.
- R. J. Lemke Oliver and K. Soundararajan, [*Unexpected biases in the
  distribution of consecutive primes*](https://arxiv.org/abs/1603.03720),
  whose consecutive-pattern formulas are conjectural for actual primes.
- C. F. Lau, [*Residue Class Patterns of Consecutive
  Primes*](https://arxiv.org/abs/2409.12819v2), an occurrence theorem rather
  than a quantitative growing-modulus mixing estimate.
