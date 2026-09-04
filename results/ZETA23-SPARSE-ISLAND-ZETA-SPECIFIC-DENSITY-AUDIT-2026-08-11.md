# Horizontal zero density cuts off the broad sparse-island cap

Status: rigorous zeta-specific correction and repaired counterconfiguration,
2026-08-11.  Huxley's horizontal zero-density theorem excludes the original
fixed-profile, power-length high-depth cap in part of the parameter range.
It does not exclude either a wholly polylogarithmic island or a power-length
terminal block with a polylogarithmic high-depth cap.  No zero-free strip is
proved.

## 1. Verdict

Use the notation of
[`ZETA23-SPARSE-TAPERED-K3-ISLAND-2026-08-11.md`](ZETA23-SPARSE-TAPERED-K3-ISLAND-2026-08-11.md):

```text
L=log X=log T+o(log T),       s=6*pi/L,
b=2*alpha/3,                 0<alpha<1/2.
```

The illustrative choice in that report was

```text
H_0=X^(alpha/3),
alpha_j=b+(alpha-b)*psi(j/J_0),       J_0*s asymp H_0.       (1.1)
```

For this fixed-shape profile, classical horizontal zero density imposes a
new restriction.  Put

```text
alpha_*=(sqrt(577)-19)/12=0.4184020249....             (1.2)
```

Then Huxley's theorem excludes (1.1) as a model for the actual zeta zeros
whenever

```text
alpha>alpha_*.                                         (1.3)
```

This does not invalidate the sparse-screening theorem.  There are two exact
repairs under canonical padding `eta asymp log L`.

1. Take the whole island to have polylogarithmic length, for example

   ```text
   H_poly=L^9/eta.                                     (1.4)
   ```

   It still satisfies
   `H_poly*eta/L^8 -> infinity` and
   `H_poly*X^(4*alpha/3)=o(T)`, so the complete Gevrey, endpoint-jet,
   count, and moment proof is unchanged.  Every fixed-depth population is
   then only `T^o(1)`.

2. Keep the terminal depth-`b` block at length `H_0`, but put the excess
   depth `alpha-b` on a second Gevrey scale

   ```text
   W=L^9/eta,
   alpha_j=b+(alpha-b)*psi(j*s/W).                    (1.5)
   ```

   The terminal population has size `X^(alpha/3+o(1))`, which all quoted
   density bounds permit at depth `b`; every population at a fixed depth
   strictly above `b` has size only `T^o(1)`.  The carrier remains

   ```text
   0<K<=X^(2*alpha/3+o(1)).                            (1.6)
   ```

Thus horizontal zero density genuinely prunes the broad cap, but it does
not rule out the sparse `k=3` screening mechanism.

## 2. Huxley's exact cutoff

Let `u<alpha` be fixed.  Since `psi(0)=1` and `psi` is continuous, there is
a fixed `c_u>0` such that

```text
#{j:alpha_j>=u}>=c_u*H_0*L=T^(alpha/3+o(1)).          (2.1)
```

Each such center supplies one right-hand zero with real part at least
`1/2+u`.  Huxley's classical estimate is

```text
N(sigma,T)
 <<T^[3*(1-sigma)/(3*sigma-1)+o(1)].                  (2.2)
```

At `sigma=1/2+u`, its exponent is

```text
d_H(u)=3*(1/2-u)/(1/2+3*u).                           (2.3)
```

Equations (2.1)--(2.3), followed by `u` increasing to `alpha`, require

```text
alpha/3<=d_H(alpha),
6*alpha^2+19*alpha-9<=0.                              (2.4)
```

The positive root in (2.4) is exactly (1.2).  Hence every
`alpha>alpha_*` gives a strict contradiction.  Equality is not decided by
this exponent comparison.

The other density exponents quoted in the repository give weaker top-cap
cutoffs:

```text
Huxley                         0.4184020...
Guth--Maynard direct           0.4274538...
(30/13)*(1-sigma) corollary    45/103=0.4368932...
Ingham                         0.4476568....           (2.5)
```

The Vinogradov--Korobov and Bellotti--Trudgian--Yang zero-free regions
approach `1`; they do not exclude any fixed `1/2+alpha<1`.  Bellotti's
`O(1)` density theorem likewise applies near the moving VK boundary, not at
the fixed lines used here.

## 3. Why the terminal block survives density

At terminal depth `b=2*alpha/3`, use Ingham when `b<1/4` and Huxley
when `b>=1/4`.  In the Huxley range the exponent is

```text
d_H(b)=(3/2-2*alpha)/(1/2+2*alpha).                   (3.1)
```

For `3/8<=alpha<1/2`,

```text
alpha/3<d_H(b).                                      (3.2)
```

Indeed, (3.2) is equivalent to
`2*alpha^2+(13/2)*alpha-9/2<0`, whose positive root is
larger than `1/2`.  When `0<alpha<3/8`, Ingham instead gives

```text
d_I(b)=(3/2-2*alpha)/(3/2-2*alpha/3)>alpha/3.        (3.3)
```

The last inequality follows from
`4*alpha^2-45*alpha+27>0`, in particular throughout
`0<alpha<3/8`.  The Guth--Maynard exponents are also larger than
`alpha/3` wherever their improved range applies.  Thus a terminal
population of size

```text
H_0*L=X^(alpha/3+o(1))                               (3.4)
```

is below every horizontal density ceiling used here.

For the two-scale profile (1.5), fix `u>b`.  The set
`{j:alpha_j>=u}` lies in the `W`-cap, so it contains only

```text
O(W*L)=T^o(1)                                        (3.5)
```

right-hand zeros.  Every fixed-line zero-density estimate has a positive
power ceiling and therefore permits (3.5).  For `u<=b`, the preceding
Ingham--Huxley comparison applies.

The local horizontal second-moment input is also too coarse.  In the
pair-counting convention of
[`QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md`](QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md),
the terminal block contributes `O(H_0*L)`.  The Karatsuba--Korolev bound on
windows of length `H_K=T^(27/82+epsilon)` is `O(H_K/L)`, and

```text
(H_0*L)/(H_K/L)
 =T^(alpha/3-27/82-epsilon+o(1))*L^2 ->0.             (3.6)
```

The unit-window ceiling is only `O(L)`, exactly the scale used by the
construction.  No deterministic zeta-zero spacing or repulsion theorem in
the audited inputs forbids the simple separated atoms.

## 4. The two-scale Gevrey and endpoint audit

Write the repaired form as

```text
Q=Q_(b,J_0)+R_(J_1),
J_0*s asymp H_0,             J_1*s asymp W.           (4.1)
```

The finite sampling lemma for `Q_(b,J_0)` is independent of `J_0`, hence

```text
||Q_(b,J_0)||<=2*X^b.                                 (4.2)
```

Apply the Gevrey Poisson lemma only to `R_(J_1)`.  Its alias-localization
scale is now `W`, and the endpoint neighborhood can be taken as

```text
rho=L^6/W.                                           (4.3)
```

The aliases `q=-2,...,2` have operator size at most
`X^(2*alpha/3+o(1))`.  At `q=3`, the endpoint-jet factor is

```text
(e*T*rho/m)^(2*m)
 =O(L^6/(W*eta))^(2*m)=o(X^(-A))                     (4.4)
```

for every fixed `A`, because `W*eta/L^8=L -> infinity`.  The legal
bandwidth-one moment window stops short of the `q=3` alias by `eta`; its
Gevrey error is

```text
W*X^alpha*exp(-c*sqrt(W*eta/L))=X^(-A).              (4.5)
```

Equations (4.2)--(4.5) prove the same operator bound as the one-scale
construction.  The base and cap ranks are respectively `O(H_0*L)` and
`O(W*L)`.  Their Frobenius costs satisfy

```text
H_0*X^(2*b)=X^(5*alpha/3)=o(T),
W*X^(4*alpha/3)=o(T).                                (4.6)
```

Thus the first and Frobenius moments, and the equivalent leading
pair-correlation statistic, retain their required values up to `o(N)`.
The count, endpoint-cardinality, and qualitative negative-direction proofs
are unchanged.

## 5. Fixed-order higher moments still do not detect the repair

Consider a fixed `p`-th matrix moment made from a physical support of length
`lambda*L`.  A normalized row of depth at most `d` has squared coefficient
norm at most

```text
X^(d*lambda+o(1)).                                   (5.1)
```

The terminal perturbation has rank `X^(alpha/3+o(1))` and depth `b`; the cap
has subpower rank and depth `alpha`.  Hence their `p`-Schatten ledgers are
bounded by

```text
terminal: X^(alpha/3+b*lambda*p+o(1)),
cap:      X^(alpha*lambda*p+o(1)).                   (5.2)
```

The unconditional diagonal/Rudnick--Sarnak range quoted by Zeta23 is
`lambda*p<2`, together with the separately evaluated boundary
`p=2,lambda=1`.  In that range (5.2) is at most

```text
terminal: X^(5*alpha/3+o(1)),
cap:      X^(2*alpha+o(1)),                          (5.3)
```

and both are `o(T)` for `alpha<1/2`.  If `G_0` is the on-line background,
its operator norm is polylogarithmic.  The noncommutative telescoping
identity

```text
(G_0+E)^p-G_0^p
 =sum_(r=0)^(p-1) (G_0+E)^(p-1-r)*E*G_0^r            (5.4)
```

and `rank(AEB)<=rank(E)` give the same `o(T)` bound for every mixed trace
term.  Thus no currently quoted fixed-order supported moment excludes the
two-scale island.  A growing-order theorem, a moment beyond total support
two, or a maximum-sensitive local statistic would be new input.

## 6. Prime-side and varying-window audit

Varying the cutoff and lattice offset reconstructs complex triangular
von Mangoldt shells, but the strongest audited pointwise estimate on a
carrier-selected shell is still

```text
S_Y(gamma)<<sqrt(Y)/(log Y)^(3/10).                  (6.1)
```

The island carrier on that shell has size at most `Y^alpha`.  Since
`alpha<1/2`, (6.1) is larger by
`Y^(1/2-alpha-o(1))`.  The completed fixed-window Type-II estimate has only
Vinogradov--Korobov, hence subpower, saving and does not change the exponent.
The exact Euler product therefore remains a possible discriminator, but no
evaluated prime-side identity in the repository currently supplies the
needed fixed power.

## 7. First exact new zeta-specific statement

A direct zero-side statement which would exclude both repairs is a uniform
polylogarithmic-window horizontal-density deficit.  For every fixed
`sigma>1/2`, require, at the Gevrey scale

```text
W*eta/L^8 -> infinity,
N(sigma;t-W,t+W)=o(W*L)                              (7.1)
```

uniformly for `t asymp T`.  The fixed profile has a positive fraction of
`W*L` right-hand zeros above some fixed `sigma<1/2+alpha`, so (7.1) rules it
out.  Global zero density proves only an averaged or almost-all-height
version of (7.1); one exceptional interval remains possible, and one is
enough to defeat a uniform strip.

An alternative is a maximum-sensitive consequence of the complete explicit
formula: a target-conditioned lower edge or signed prime estimate which
forbids (1.6) for the actual zeta divisor.  Neither statement is proved by
Riemann--von Mangoldt counting, global line density, the known horizontal
density exponents, the first two moments, supported fixed-order higher
moments, KMT, or the current completed Type-II bounds.  These are next-input
statements, not declarations that the overall route is complete or blocked.

Primary local references:

- [`R98-QUASI-RH-BOOTSTRAP-GATE.md`](R98-QUASI-RH-BOOTSTRAP-GATE.md),
  Section 3, for Ingham, Huxley, and Guth--Maynard;
- [`QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md`](QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md),
  Section 7.2, for local horizontal second moments;
- [`ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md`](ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md),
  Section 7, for the support-depth moment barrier; and
- [`ZETA23-VARYING-CUTOFF-OFFSET-TURAN-BLINDNESS-2026-08-11.md`](ZETA23-VARYING-CUTOFF-OFFSET-TURAN-BLINDNESS-2026-08-11.md)
  for the exact varying-window limitation.
