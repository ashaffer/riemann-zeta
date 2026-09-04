# SUSY/DPP partition-function collapse card

**Date:** 2026-08-13

**Verdict:** **the exterior-power partition function gives a clean explicit
legal design, but its relative determinant collapses exactly to directional
Christoffel leverage.  Near-unique factorization of the common fermionic
volume alone cannot improve the ratio.  No subpower design or strip is
obtained.**

Let `mu` be a legal probability measure on the allowed frequency band and
write

```text
a(xi) in C^M,             v(xi)=(a(xi),b(xi)) in C^(M+1),
G=integral a a^* dmu,     H=integral v v^* dmu,
Delta(mu)=det(H)/det(G)                                      (1.1)
```

when `G` is nonsingular.  The pseudoinverse Schur complement is the correct
form in the singular case.

## 1. Andréief is exactly volume-sampled interpolation loss

Andréief gives

```text
Z_M:=integral |det[a(xi_1),...,a(xi_M)]|^2 dmu^M=M!*det(G),

Z_(M+1):=integral |det[v(xi_0),...,v(xi_M)]|^2 dmu^(M+1)
          =(M+1)!*det(H).                                  (1.2)
```

Draw `X=(xi_1,...,xi_M)` from the volume-sampling/DPP density
`|det A_X|^2/Z_M`, and let `I_X b` be the unique feature interpolant through
the sampled target values.  Expanding the augmented determinant along the
extra sample gives

```text
det[v(xi_0),v(X)]
 =det[a(X)]*(b(xi_0)-I_X b(xi_0))                           (1.3)
```

up to a harmless sign/conjugation convention.  Hence

```text
E_(X~volume) ||b-I_X b||_(L2(mu))^2=(M+1)*Delta(mu).        (1.4)
```

Thus the fermionic volume ratio is not a new invariant.  It is precisely
the weighted least-squares residual, viewed as the expected interpolation
loss of a volume-sampled basis.  Product singular values bias which bases
are sampled, but after normalization they leave only the carrier-relative
error in (1.4).

## 2. Exact low-atom/high-DPP computation

This computation exposes the proposed supersymmetric cancellation.  Let
`nu` be any legal high-band probability design, put

```text
G_0=integral a a^* dnu,       q=a(xi_0),
L=q^*G_0^(-1)q,               b_0=b(xi_0),                 (2.1)
```

and first idealize the high-band carrier to zero.  Mix one low carrier atom
with the high design:

```text
mu_epsilon=epsilon*delta_(xi_0)+(1-epsilon)*nu.             (2.2)
```

The denominator and augmented numerator factor exactly as

```text
det G_epsilon
 =(1-epsilon)^(M-1)*det(G_0)*(1-epsilon+epsilon*L),

det H_epsilon
 =epsilon*(1-epsilon)^M*|b_0|^2*det(G_0).                  (2.3)
```

Therefore the entire high fermionic partition function cancels:

```text
Delta(mu_epsilon)
 =|b_0|^2 * epsilon*(1-epsilon)
              /(1-epsilon+epsilon*L).                      (2.4)
```

The maximizing mixture and value are

```text
epsilon_*=1/(1+sqrt(L)),
max_epsilon Delta(mu_epsilon)=|b_0|^2/(1+sqrt(L))^2.       (2.5)
```

Here `L` is the inverse directional Christoffel function, equivalently the
bosonic resolvent left after the fermionic determinant cancels.  Equations
(2.3)--(2.5) are the finite-dimensional SUSY reduction: any exact
Grassmann/boson representation evaluates to this same scalar Schur
complement.

For the actual target, let

```text
epsilon_H=sup_(xi in supp(nu)) |b(xi)|.                    (2.6)
```

Distance to a fixed feature subspace is 1-Lipschitz in `L2(mu_epsilon)`, so

```text
sqrt(Delta_actual(mu_(epsilon_*)))
 >= |b_0|/(1+sqrt(L))-epsilon_H.                            (2.7)
```

This is a concrete relative lower lemma for an explicit legal design.  One
may take `nu` to be normalized Lebesgue measure on `[B/2,B]`; its Gramian is
the exact cosine Gramian already evaluated by
`prime_wiener_continuous_exchange_probe.py`.

## 3. Why cluster expansion cannot remove the square root

Suppose `||q||^2>=cM` and the high phase curve is directionally incoherent:

```text
sup_(xi in supp(nu)) |<q,a(xi)>| <= C*sqrt(M)*R.            (3.1)
```

Then

```text
q^*G_0 q <= C^2*M*R^2,
L=q^*G_0^(-1)q >= ||q||^4/(q^*G_0 q)
                 >= c_1*M/R^2.                             (3.2)
```

Consequently (2.5) is at most

```text
sqrt(Delta)<=C_1*|b_0|*R/sqrt(M).                          (3.3)
```

For random-like polynomially many phase cells, `R` is of square-root
logarithmic size.  This is exactly the previously observed
`sqrt(log K/M)` random-polytope law.  A subpower carrier requires a high-band
design with `L=Y^(o(1))`, which in turn requires a genuinely coherent phase
direction violating (3.1).  That is the original directional
Christoffel/atomic-cancellation problem, not a determinant expansion gain.

Conversely, a frame bound `G_0>=cI` gives `L<=C M`; inserting it into (2.7)
recovers the explicit `M^(-1/2)` lower design.  Thus the same Christoffel
number sandwiches both sides in the generic regime.

## 4. Unique factorization and conductor audit

Near-unique factorization may help estimate `det(G_0)` or the individual
Andréief partition functions.  Estimating that common volume alone cannot
help their ratio in (2.3): `det(G_0)` cancels before any inequality is
applied.  A carrier-sensitive factorization theorem could still help, but
then it must bound `L`, the overlap with the *specific carrier direction*;
that is exactly the original open gate.

Expanding the determinant into products of `M` independently sampled legal
frequencies is harmless as an analytic DPP average.  Treating those products
as one physical test, however, tensorizes frequencies and incurs the old
`Y^2` conductor/product-frequency bill.  Keeping the samples separate avoids
that bill but returns (1.4) and (2.5); combining them supplies no third
option.

The exact truth boundary is therefore

```text
Andréief/DPP interpolation identity                 PROVED;
low-atom/high-design determinant formula            PROVED;
fermionic common-volume cancellation                EXACT;
remaining bosonic/directional Christoffel leverage  ORIGINAL OPEN GATE;
subpower explicit design                            NOT FOUND;
uniform zero-free strip                             NOT PROVED.          (4.1)
```
