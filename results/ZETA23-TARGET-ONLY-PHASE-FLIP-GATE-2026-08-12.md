# Target-only quotient admits a normalized reciprocal-separation phase flip

Status: exact two-packet compression, a target-only no-extension theorem,
and a strictly-deepest three-pair screening configuration, 2026-08-12.  This
is a normalized Paley--Wiener/Gabor operator statement.  It is not an
existence theorem for zeta zeros and proves no zero-free strip.

## 1. Verdict

The fixed-width mirror sign does **not** extend from the joint positive-row
quotient to the target-only quotient.

The first obstruction is simpler than the abstract transverse reservoir.
If two packets are separated by `D`, a collateral pair whose ordinate is
shifted by

```text
Delta gamma=+/-pi/D                                (1.1)
```

acquires opposite phases on the two packets.  Its cross block is therefore
the negative of the selected cross block, up to the local packet error
`O(w/D)`.  Consequently the selected negative carrier vector is a positive
carrier vector for the collateral pair.  Imposing the collateral positive
row would delete this vector; imposing only the selected positive row does
not.

There are two precise consequences.

1. One equal-depth collateral pair at (1.1) changes the selected value
   `-kappa` to `o(kappa)`.  Thus even one tie destroys every uniform
   `-c*kappa` mirror margin.  The residual sign is not asserted.
2. Let the selected depth be `alpha`, and take two distinct collateral
   pairs at the two gaps in (1.1), both at depth

   ```text
   alpha_1=alpha-epsilon_L,
   epsilon_L>0,             epsilon_L*D -> 0.       (1.2)
   ```

   The selected pair is then strictly deepest, while on its full-carrier
   vector the sum of the selected and two collateral pair forms is

   ```text
   (1-o(1))*kappa>0.                                (1.3)
   ```

For `D=dL`, the earlier test choice `epsilon_L=L^(-2)` satisfies (1.2).
The same vector is feasible for every direct carrier slice
`eta=theta*kappa`, `0<theta<=1`, so (1.3) screens all fixed `theta` at once.

This does not contradict the mirror-alignment theorem with every positive
row imposed.  At the phase flip, the collateral positive row is, to leading
order, the selected negative row itself.  The two theorems concern different
quotients.

The `L^(-2)` Hermite collision by itself is not the escape.  For a fixed
packet its global row displacement is

```text
O(D*abs(Delta gamma)+w*abs(Delta alpha)).            (1.4)
```

At `abs(Delta)=L^(-2)` and `D asymp L`, this is `O(1/L)`, so the pair remains
mirror-aligned up to `o(kappa)`.  Promoting that difference to carrier size
costs at least the reciprocal `Omega(L)` in coefficient norm (and
`Omega(L^2)` after the center phases are gauged away and only the local
Hermite difference remains).  The phase flip instead occurs at the natural
reciprocal-separation scale `1/D` and costs no norm amplification.

## 2. Exact packet compression

Demodulate by the selected ordinate.  The completed reflected-pair kernel
at depth `beta>0` and relative ordinate `delta` is

```text
K_(beta,delta)(t,s)
 =(2/L^2)*exp(-i*delta*(t-s))*cosh(beta*(t-s)).       (2.1)
```

Choose a real, nonnegative, even packet

```text
phi in C_c^infinity((-w/2,w/2)),   ||phi||_2=1,      (2.2)
```

In the repository coefficient-map normalization, use the representatives

```text
q_-(t)=sqrt(L)*phi(t+D/2),
q_+(t)=sqrt(L)*phi(t-D/2),                           (2.2a)
```

and let `u,v` be their normalized coefficient vectors, centered at
`t_-=-D/2` and `t_+=D/2`, with `D>w`.  The `sqrt(L)` in (2.2a) is what
converts the kernel factor `2/L^2` in (2.1) into the common compression
factor `2*A_beta^2/L` below.  This symmetric placement makes the
raw selected positive/negative rows proportional to `u+v` and `u-v`; no
change of positive-row quotient is hidden in a Lorentz refactorization.  Put

```text
A_beta=integral phi(s)*exp(beta*s)ds,
m_beta=2*A_beta^2/L,
C_beta=cosh(beta*D).                                 (2.3)
```

At `delta=0`, direct integration gives the exact full reflected-pair
compression

```text
M_(beta,0)
 =m_beta*[[1,C_beta],[C_beta,1]].                    (2.4)
```

For arbitrary `delta`, freeze the modulation in (2.1) at the two packet
centers.  This is an exact decomposition

```text
M_(beta,delta)
 =m_beta*[[1, C_beta*exp(+i*delta*D)],
           [C_beta*exp(-i*delta*D),1]]
   +E_(beta,delta),                                  (2.5)

||E_(beta,delta)||op
 <=abs(delta)*w*m_beta*(1+C_beta).                   (2.6)
```

Indeed, on the support of the `(j,k)` packet entry,

```text
abs((t-s)-(t_j-t_k))<=w,
abs(exp(-i*delta*(t-s))
    -exp(-i*delta*(t_j-t_k)))<=abs(delta)*w.         (2.7)
```

Because `phi>=0` and `cosh(beta*(t-s))>0`, the absolute integral in (2.7)
is exactly the corresponding entry of (2.4).  The maximum row-sum bound
then proves (2.6).  Thus (2.5) is not a cross-block toy: it is the complete
pair compression, with a rigorous local-width remainder.

The full normalization is also visible in (2.5).  The diagonal same-lobe
piece has size `m_beta`; the cross coefficient is `m_beta*C_beta`; and

```text
m_beta/(m_beta*C_beta)=O(exp(-beta*D)).               (2.8)
```

Writing `C_beta=(exp(beta*D)+exp(-beta*D))/2` shows that the reverse cross
branch is smaller than the dominant cross branch by `exp(-2*beta*D)`.
Hence all same-lobe and reverse terms are already present in (2.4)--(2.6);
none has been discarded.

## 3. Selected carrier and the phase-flip identity

For the selected pair `(alpha,0)`, let

```text
e_+=(u+v)/sqrt(2),       e_-=(u-v)/sqrt(2).          (3.1)
```

Equation (2.4) gives the exact eigenvalues

```text
lambda_+=m_alpha*(1+C_alpha),
lambda_-=m_alpha*(1-C_alpha).                        (3.2)
```

The selected positive-row quotient is `e_+^perp`.  Its carrier top vector
is exactly `e_-`, and

```text
kappa=-lambda_-=m_alpha*(C_alpha-1).                 (3.3)
```

For a collateral pair at depth `beta` and
`delta=+/-pi/D`, (2.5)--(2.6) give

```text
<e_-,M_(beta,delta)e_->
 =m_beta*(1+C_beta)+R_beta,

abs(R_beta)<= (pi*w/D)*m_beta*(1+C_beta).            (3.4)
```

Compare (3.4) with the selected value `-kappa`.  More generally, before
specializing the phase, the ideal part is

```text
<e_-,M_(beta,delta)e_->
 =m_beta*(1-C_beta*cos(delta*D))
   +O(abs(delta)*w*m_beta*(1+C_beta)).               (3.5)
```

This is the target-only phase invariant.  On the joint quotient, the
collateral positive row forces the corresponding positive coordinate to
zero and restores the negative mirror sign.  On the target-only quotient,
the cosine in (3.5) is unconstrained.

## 4. One tie removes the margin; two shallower pairs screen

First take `beta=alpha`.  Combining (3.3)--(3.4) gives

```text
<e_-,(M_(alpha,0)+M_(alpha,+/-pi/D))e_->
 =2*m_alpha+O((w/D)*m_alpha*C_alpha)
 =o(kappa).                                         (4.1)
```

Equation (4.1) deliberately makes no sign claim.  It proves the needed
fact: one equal-depth phase-flipped pair eliminates every fixed negative
fraction of the carrier.

Now take `beta=alpha-epsilon_L`, with (1.2).  Since the packet width is fixed,

```text
m_beta/m_alpha=1+O(epsilon_L*w),

(1+C_beta)/(C_alpha-1)
 =exp(-epsilon_L*D)
   *(1+O(exp(-beta*D))+O(exp(-alpha*D))).            (4.2)
```

Consequently

```text
m_beta*(1+C_beta)/kappa=1-o(1).                      (4.3)
```

Put two distinct collateral pairs at relative ordinates `+pi/D` and
`-pi/D`, both with depth `beta`.  Equations (3.3), (3.4), and (4.3) yield

```text
<e_-,[M_(alpha,0)
      +M_(beta,+pi/D)+M_(beta,-pi/D)]e_->
 =-kappa+2*(1-o(1))*kappa
 =(1-o(1))*kappa>0.                                 (4.4)
```

All vectors are unit normalized.  There is no inverse-Gram or divided-
difference amplification.  The target has depth `alpha`, while both
collaterals have the strictly smaller depth `alpha-epsilon_L`; hence the
target is the unique deepest pair.

Since `<e_-,N e_->=kappa`, the same `e_-` belongs to every slice

```text
{z: ||z||=1, <z,Nz>>=theta*kappa},   0<theta<=1.     (4.5)
```

Thus the phase-flip configuration is carrier-rich even at the full-carrier
boundary.  It disproves a target-only mirror-sign theorem based solely on
normalized packet geometry.  It does not determine the sign of the actual
prime/pole/gamma remainder.

## 5. Endpoint jets and finite Gabor transfer

The packets in (2.2) are compactly supported strictly inside the physical
endpoints, so every physical endpoint jet vanishes exactly.  The common
binomial endpoint-flat cutoff and smooth Fourier truncation from
`ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md`,
Section 5, apply simultaneously to this fixed family of three pairs.

Here `delta=O(1/L)` and the depths stay in a fixed compact subset of
`(0,1/2)`, so the approximation is uniform.  After exact target-row
projection and Gram--Schmidt, every matrix entry changes by `O_A(T^-A)` for
arbitrary fixed `A`.  This is `o(kappa)`, while the margin in (4.4) is
`(1-o(1))*kappa`.  Therefore (4.4) transfers to the growing-jet finite Gabor
space.  This transfer realizes an admissible coefficient-space
configuration; it does not realize any prescribed set of zeta zeros.

## 6. Count and moment compatibility

The two collateral ordinates differ from the selected ordinate by
`pi/D=O(1/L)` and are distinct.  Adding these two reflected pairs changes

```text
Riemann--von Mangoldt discrepancy                 O(1),
every unit-window count                           O(1),
horizontal density counts                        O(1),
simple-zero proportion                           O(1/N).              (6.1)
```

Thus current count and density theorems **permit** this local pattern; they
do not guarantee it.  The pairs may be declared simple in the formal
count/moment model.  Their completed-operator perturbation has fixed rank
and Frobenius cost `O(kappa^2)`.  In the Zeta23 range
`alpha<=1/2`, `d<2/3`, this is `o(N)` at the leading moment scale, exactly as
in the earlier collateral moment audit.  Trace, Frobenius, and leading
pair-correlation data therefore do not exclude the phase-flip orientation.

This is only compatibility of an abstract divisor ledger plus a genuine
normalized packet compression.  It is not a construction of an entire
Hadamard product, an `L`-function, or the zeta divisor.

## 7. Scope and next gate

What is proved:

| statement | status |
|---|---|
| `L^(-2)` fixed-width Hermite pair gives a carrier transverse block | **no**, it remains aligned up to `o(kappa)` |
| target-only mirror sign holds for every collateral ordinate | **false** |
| one tie at gap `pi/D` preserves a fixed negative margin | **false** |
| two `o(1/D)`-shallower pairs at gaps `+/-pi/D` screen | proved in normalized packet/Gabor geometry |
| current zero counts or density exclude that local pattern | **no** |
| zeta actually contains that pattern | not asserted |

The next geometric question is whether one can average over separations
`D` with **positive** weights so that every collateral cosine transform is
nonnegative, while retaining a fixed fraction of the exponential carrier.
Formally, (3.5) replaces `cos(delta*D)` by the cosine transform of the
separation measure.  Positive measures with nonnegative cosine transforms
exist abstractly, but the carrier weight grows like `exp(alpha*D)` and the
available separation interval has length `O(L)`.  It is not proved that such
an average can keep the selected carrier at fixed-power scale after packet
normalization and endpoint constraints.  This is the exact next gate; no
positive-averaging theorem is claimed here.

The arithmetic alternative is equally sharp: prove that the actual signed
prime/pole/gamma remainder cannot realize the reciprocal-separation phase
orientation in (3.5).  Either route is a genuinely new input.  The joint-row
mirror theorem alone cannot settle the target-only direct `q_eta` problem.
