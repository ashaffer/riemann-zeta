# QP centered band-pass: coprime top-block audit

**Date:** 2026-08-22  
**Verdict:** the support estimate which was previously only granted in the
top-modulus DFI ledger is elementary in the coprime block.  Together with
ordinary numerator Parseval it gives the frozen, separable coprime
top-Farey form with loss

```text
q^(3/11)=D^(9/16).
```

If this estimate held for the complete centered HSM reduction, it would
give `D^(41/32+o(1))`, improving `D^(21/16)` by `D^(1/32)`.  It does **not**
currently do so.  The exact DFI weight depends on the mismatch, lower
modulus blocks are present, noncoprime blocks have a different complete-sum
formula, and the Ramanujan/major axes must be grouped with the signed
band-pass cancellation before taking absolute values.  Thus no new slope
block or four-cycle exponent is claimed.

## 1. A support-energy lemma

Let `(U,R)=1`, let `I` be an interval of at most `R` consecutive integers,
and put

```text
n_c=#{1<=r<=P: there is |nu|<=V with nu==U*c*r (mod R)}.
```

Assume

```text
2*V<R,                 2*P*V<R,                  (1.1)
```

and restrict to `(c,R)=1`.  Then

```text
sum_(c in I, (c,R)=1) n_c^2
  <<P*V*tau(R)*(1+log(2*min(P,V))).               (1.2)
```

Here and below harmless absolute constants allow signed fan intervals and
fixed enlargements.

To prove (1.2), expand the square.  If `(r,nu)` and `(r',nu')` occur for
the same `c`, then

```text
R | r'*nu-r*nu',
|r'*nu-r*nu'|<=2*P*V<R.
```

Consequently

```text
r'*nu=r*nu'.                                       (1.3)
```

The zero direction is absent: `(c,R)=1`, `0<r<R`, and `nu=0` would imply
`R|r`.  Write the two vectors on their common primitive ray as

```text
(r,nu)=g*(a,b),       (r',nu')=g'*(a,b),
(a,b)=1,              a>0.                        (1.4)
```

The two congruences are equivalent to

```text
R|g*(U*c*a-b),        R|g'*(U*c*a-b).             (1.5)
```

With `d=(R,g,g')`, (1.5) leaves at most `d+1` possible `c` in an interval
of length `R`: modulo `R/d`, the coefficient `a` is invertible whenever a
solution exists, because `(a,b)=1`.

Put `m=max(g,g')`.  There are at most `O(P*V/m^2)` possible nonzero
primitive rays.  On the shell `max(g,g')=m`,

```text
sum_(max(g,g')=m) ((R,g,g')+1)<<m*tau(R).          (1.6)
```

Indeed, for one boundary, sum
`(R,g,m)` over `g<=m` by its divisors; the other boundary is identical.
Summing `(P*V/m^2)*(1.6)` proves (1.2).

For a second coprime fan basis `(V_0,S)` with fan count `Q` and the same
dual window length `V`, Cauchy--Schwarz gives

```text
sum_(c in I,(c,R*S)=1) n_c*m_c
 <<V*sqrt(P*Q)*(R*S)^o(1).                         (1.7)
```

At the balanced top block,

```text
P=Q=sqrt(D),       R,S,C~q/sqrt(D),
K=q/D,             V=C/K=sqrt(D),                 (1.8)
```

so (1.7) is exactly

```text
sum_c n_c*m_c<<P*Q*q^o(1).                        (1.9)
```

This proves the support part of the previously granted display
`(2E.F7o20z2)` for the coprime top block.

## 2. Numerator Parseval is also exact there

For fixed coprime `c`, let the transformed row and color frequencies obey

```text
0<|nu|,|mu|<=V,             2*V^2<c.              (2.1)
```

The maps from the physical fan indices to `nu` and `mu` are injective in
this range.  For arbitrary coefficient vectors `x_nu,y_mu`, put

```text
B_a=sum_(nu,mu)x_nu*y_mu*e_c(-a_bar*lambda*nu*mu),
(lambda,c)=1.                                      (2.2)
```

Completing primitive numerators to all residues and using Parseval gives

```text
1/c*sum_(a mod c)^* |B_a|^2
 <=sum_(t mod c)|sum_(nu*mu==t mod c)x_nu*y_mu|^2.
```

Since `2*V^2<c`, modular product equality is ordinary integer product
equality.  Cauchy--Schwarz on each multiplication fibre and the divisor
bound therefore prove

```text
1/c*sum_(a mod c)^* |B_a|^2
 <<c^o(1)*||x||_2^2*||y||_2^2.                    (2.3)
```

At (1.8), `2*V^2=2D<C` for all sufficiently large `q`, so (2.3) applies
uniformly.

## 3. The exact exponent obtained by the frozen top block

Use the standard balanced notation

```text
X=J*K_dual=q^(84/33),       C=q^(25/33),
P*Q=q^(16/33).                                    (3.1)
```

For a top dyadic family `c~C`, the two-dimensional Poisson prefactor is
`X/c`, and the DFI top-block normalization is `1/C`.  Equations (1.9) and
(2.3) give the unconditional algebraic estimate for the **frozen,
separable, coprime top-Farey form**

```text
1/C*sum_(c~C,(c,R*S)=1)(X/c)^2
       *(1/c)*sum_a^*|B_(c,a)|^2
 <<P*Q*X^2/C^3*q^o(1)
 =q^(109/33+o(1)).                                 (3.2)
```

The diagonal correlation scale is

```text
P*Q*X=q^(100/33),                                  (3.3)
```

so (3.2) loses

```text
X/C^3=q^(9/33)=q^(3/11)=D^(9/16).                 (3.4)
```

Were (3.2) a bound for the full primal dyadic moment, the standard dyadic
Cauchy step would give

```text
Q_nd(z)<<D^(1+(9/16)/2+o(1))*||z||_2^4
       =D^(41/32+o(1))*||z||_2^4,                 (3.5)
```

which is smaller than `D^(21/16)` by `D^(1/32)`.

## 4. Why (3.5) is not a theorem

There are four nonoptional complements.

1. The exact DFI factor `h(c/C,n/C^2)` depends on the mismatch
   `n=j*k-j'*k'-h`.  Freezing or separating it before Poisson is not an
   identity; its uniform transform cost has not been bounded.
2. The delta symbol contains lower `c` blocks.  Replacing it by only
   `c~C`, or by a coprime Jutila family, requires an approximation error
   against the fourth moment of the product polynomial.  No such estimate
   is currently available.
3. When `(c,R*S)>1`, the coprime inverse formula (2.2) is invalid.  The raw
   complete bilinear sum has conductor-lowered compatibility conditions;
   a separate local calculation, including all gcd weights, is required.
4. The `Delta==0` numerator axis is Ramanujan rather than Weil.  Its
   `h==0` part is tied to the product diagonal, and the remaining terms can
   only be treated after retaining the zero-integral band-pass sum in `h`.
   Bounding individual moduli or shifts positively destroys precisely that
   cancellation.

The smooth positive completion removes physical fan endpoints, but it does
not remove any of these four arithmetic terms.  The existing
`D^(21/16)` four-cycle theorem does not identify their complement as a
separate sector with a better exponent.  Consequently (3.2) is a genuine
top-block lemma and a useful exponent target, but it cannot be interpolated
with the existing theorem to produce a uniform improvement.

```text
coprime top-block support energy:                  PROVED;
coprime fixed-c numerator Parseval:                PROVED;
frozen separable top-Farey loss D^(9/16):          PROVED;
exact DFI mismatch-weight separation:             OPEN;
lower/noncoprime/Ramanujan completion:             OPEN;
uniform dyadic moment with beta=9/16:              NOT PROVED;
new uniform slope-block or four-cycle exponent:    NONE.
```
