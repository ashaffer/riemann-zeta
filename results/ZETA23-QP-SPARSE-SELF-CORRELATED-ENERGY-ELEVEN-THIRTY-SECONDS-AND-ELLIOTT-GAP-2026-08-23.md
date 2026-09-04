# QP sparse self-correlated energy: `11/32` saving and the Elliott gap

**Date:** 2026-08-23  
**Verdict:** at the critical support size

```text
M=D^(11/8)=q^(2/3+o(1)),       D=q^(16/33+o(1)),                  (0.1)
```

the self-correlated congruence energy satisfies the unconditional bound

```text
E_full
 <<M^3 D^2/q + q^(1/2) M^(3/2) D q^o(1)
 <<q M D * D^(-11/32+o(1)).                                    (0.2)
```

The principal character gives the matching structural lower bound

```text
E_full >>M^3 D^2/q=q M D * D^(-3/8+o(1)),                       (0.3)
```

for critical actual-prime-power supports.  Therefore no estimate of the
form `E_full<<qMD D^(-eta)` can have `eta>3/8`.  The proved saving `11/32`
is only `1/32` short of this absolute ceiling.

Closing that last `1/32` by a coefficient-uniform large sieve would require
the conjectural `N+qM` sparse-prime large-sieve constant.  This is the
prime-modulus large-sieve conjecture attributed to Elliott, not a currently
available theorem.  The special self-correlation of the coefficient used
here leaves a narrower problem open.

---

## 1. The two energies

Let `A` be a set of `M` actual prime powers in the project shell.  For a
shell modulus `a`, set

```text
B_a(chi)=sum_(b in A) chi(b),
H_a(chi)=sum_(0<|h|<<D) chi(h).                                  (1.1)
```

The nonprincipal second energy is

```text
E_1=np sum_a 1/phi(a) sum_(chi!=1) |B_a(chi)|^2 |H_a(chi)|^2.    (1.2)
```

Adding the principal character gives, up to the harmless deletion of
nonunits, the positive congruence count

```text
E_full
 =sum_(a,b_1,b_2 in A) sum_(0<|h_1|,|h_2|<<D)
       1_(a divides b_1 h_1-b_2 h_2).                            (1.3)
```

The mixed fourth energy is

```text
E_2=sum_a 1/phi(a) sum_(chi!=1) |B_a(chi)|^2 |H_a(chi)|^4.       (1.4)
```

The proved mixed-`H^2` product-large-sieve theorem gives

```text
F:=sum_a 1/phi(a) sum_(chi!=1)|B_a(chi)|^2 <=M^2,
E_2<<q M D^2 q^o(1).                                            (1.5)
```

## 2. Unconditional `11/32` saving

Cauchy--Schwarz between (1.2), `F`, and `E_2` gives

```text
E_1
 <=F^(1/2) E_2^(1/2)
 <<q^(1/2) M^(3/2) D q^o(1).                                   (2.1)
```

The principal term is at most

```text
E_pr<<M^3 D^2/q.                                                 (2.2)
```

Thus (2.1) and (2.2) prove the first inequality in (0.2).  In powers of
`D`, at `M=D^(11/8)` and `q=D^(33/16)`, the three raw energy exponents are

```text
classical q M D:             71/16 =142/32,
mixed nonprincipal (2.1):   131/32,
principal (2.2):             65/16 =130/32.                      (2.3)
```

The mixed term controls, and the saving is

```text
142/32-131/32=11/32.                                            (2.4)
```

Among fixed product moments `B H^r`, `r=2` is optimal for this
interpolation.  At `r=3`, the support length is already `qD^3>q^2`; the
resulting estimate `E_1<<M^(5/3)D^2` saves only `D^(7/48)` from `qMD` at
the critical support.  Higher fixed `r` are weaker.

## 3. The exact principal obstruction

There are only `O(q^(1/2+o(1)))` proper prime powers in a fixed project
shell.  Hence a critical set of `M=q^(2/3)` actual prime powers contains
`M(1-o(1))` primes.

For a prime modulus `a in A`, the principal character has

```text
B_a(chi_0)=M-1,
H_a(chi_0)=2D q^o(1),
phi(a) asymp q.                                                   (3.1)
```

Summing its nonnegative contribution over the prime elements of `A` gives

```text
E_full>=E_pr>>M^3D^2/q.                                         (3.2)
```

At the critical support this has exponent `65/16` in powers of `D`, so
relative to the classical `71/16` it saves exactly

```text
71/16-65/16=3/8.                                                 (3.3)
```

This proves the ceiling in (0.3); it is not a heuristic random-model
barrier.

## 4. What would close the last `1/32`

The coefficient in `B H^2` is

```text
alpha_n=#{(b,h_1,h_2): b in A, 0<|h_i|<<D, n=b h_1 h_2}.         (4.1)
```

It has

```text
support length N<<qD^2,
sum_n |alpha_n|^2<<M D^(2+o(1)).                                (4.2)
```

Suppose one had, for the prime moduli in `A`, the sparse large sieve

```text
sum_(a in A prime) sum_(chi mod a)^* |sum_n alpha_n chi(n)|^2
 <<(N+qM) sum_n|alpha_n|^2 q^o(1).                              (4.3)
```

At (0.1), `N=qD^2` dominates `qM`.  After restoring the `1/q` conductor
weight, (4.3) would give

```text
E_2<<M D^4 q^o(1),
E_1<<M^(3/2)D^2 q^o(1).                                         (4.4)
```

At `M=q^(2/3)`, the last expression equals the principal scale
`M^3D^2/q`.  Thus (4.3) would close the gap and attain `eta=3/8`.

Via Gauss sums and Parseval over the full character group, the
coefficient-uniform form (4.3) is the sparse-prime additive large sieve
with constant `N+qM`.  Elliott conjectured precisely this constant.  Baier's
account records the conjecture and the earlier bound
`N^2/log N+qM`; for all prime moduli, Wolke's estimate is of size
`q^2 log log q/log q` in the present range:

* Stephan Baier, [*The large sieve with sparse sets of moduli*](https://arxiv.org/abs/math/0508417), equations (3)--(5) in the introduction.

Here `N=q^(65/33)`, so `q^2/log q` is still larger than `N` by a power
`q^(1/33-o(1))`.  The known prime-modulus theorem therefore does not close
even the final `D^(1/32)`.

## 5. Proper prime powers are not the obstruction

Let `P<<q^(1/2+o(1))` be the number of proper prime-power moduli in `A`.
Restricting (1.5) to them improves the elementary factor to

```text
F_pp<<P M.                                                       (5.1)
```

The ordinary product large sieve still gives `E_(2,pp)<<qMD^2`.  Therefore

```text
E_(1,pp)<<M D sqrt(Pq)
          <<M D q^(3/4+o(1)).                                   (5.2)
```

At the critical support, (5.2) has exponent `251/64` in powers of `D`,
strictly below the principal exponent `260/64`.  The unresolved `1/32` is
therefore a prime-modulus sparse/self-correlated problem.

## 6. Numerical diagnostic

For positive `H=[1,D]`, exact FFTs on the multiplicative groups of
contiguous prime shells gave:

```text
q       D    M       E_1,np / mixed bound    E_2,np / (M D^4)
5003    62   257             0.254                    0.331
10007   87   464             0.246                    0.351
20011  121   737             0.231                    0.354             (6.1)
```

These are finite diagnostics, not an asymptotic proof.  They show no
counterexample to the optimal self-correlated estimate (4.4).

## 7. Status

```text
critical energy saving eta=11/32:                 PROVED;
principal ceiling eta<=3/8:                       PROVED;
gap to the ceiling:                               1/32;
coefficient-uniform closure via Elliott LS:       OPEN;
self-correlated closure for alpha in (4.1):       OPEN.                 (7.1)
```

