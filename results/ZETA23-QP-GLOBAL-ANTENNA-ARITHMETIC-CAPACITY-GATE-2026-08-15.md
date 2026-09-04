# QP global-antenna arithmetic capacity gate

**Date:** 2026-08-15  
**Verdict:** a globally nonnegative actual-prime-power Delsarte antenna can
never have fixed-power gain.  This is true even when its node coefficients
are arbitrary real numbers.

For the half-integer shell centre `Y=(2N+1)/2`, width `w=1/5`, and the
actual prime-power nodes

```text
u_n=log(n/Y),       n=p^k,       |u_n|<w,
```

suppose

```text
Q(t)=1+sum_n lambda_n cos(t u_n)>=0       for every real t.       (0.1)
```

Then

```text
Q(0)<=max(2,1+2 omega(4Y))<=1+2 log_2(4Y).             (0.2)
```

Here `omega(m)` is the number of distinct prime divisors of the integer
`m`.  Consequently (0.1) cannot give `A_H>=Y^c` for any fixed `c>0`.

The point is arithmetic, not smoothness or positivity of the coefficients.
Every shell prime whose base does not divide the numerator or denominator
of `Y` supplies an independent torus phase.  Global nonnegativity lets those
phases be chosen simultaneously against the signs of all corresponding
coefficients.  Only the `omega(4Y)` prime bases already present in the centre
escape that independent-phase minimization.

This theorem closes the following proposed shortcut:

```text
construct an all-real nonnegative/SOS/kernel antenna first,
then restrict it to the QP band.                              (0.3)
```

It does **not** close finite-aperture QP.  A polynomial band may end long
before the high-dimensional Kronecker orbit reaches the adverse torus phase.
Any successful fixed-power antenna must therefore exploit the finite upper
edge `B=Y^(50/33)` essentially.  No QP-KILL, QP-PROMOTE, equivalence, or zeta
strip is asserted here.

---

## 1. Setup

It is useful to prove the rational-centre statement.  Let

```text
Y=a/b,       gcd(a,b)=1,       b>1,
2w<log 2.                                                   (1.1)
```

Let `P_Y` be the set of integer prime powers `n=p^k` in
`[Y exp(-w),Y exp(w)]`.  Since consecutive powers of a fixed prime have
ratio at least `2`, while the shell has ratio `exp(2w)<2`, there is at most
one member of `P_Y` with any prescribed prime base `p`.

Split the shell into

```text
I={p^k in P_Y:p divides ab},
E={p^k in P_Y:p does not divide ab},
m=#I<=omega(ab).                                           (1.2)
```

The condition `b>1` ensures that no node is zero.  It also ensures that two
distinct shell nodes are not negatives of one another: if
`log(n/Y)=-log(n'/Y)`, then `nn'=Y^2=a^2/b^2`, impossible for integers
`n,n'` because `gcd(a,b)=1` and `b>1`.

## 2. Prime-log torus

Take the finite set of prime bases occurring in `ab` and in `P_Y`, and put

```text
z_p=exp(i t log p).                                       (2.1)
```

The real flow `t -> (z_p)_p` is dense in the corresponding torus.  Indeed,
the logarithms of distinct primes are rationally independent by unique
factorization.  Independence together with `2 pi` follows from Kronecker's
criterion: a contrary integer relation would equate a nonzero integral power
of `exp(2 pi)` with a positive rational number; the former is transcendental
by the Gelfond--Schneider theorem.  Thus an inequality holding for every real
`t` holds on the whole prime-phase torus by continuity.

Write

```text
chi_n(z)=z^(v(n/Y)),                                     (2.2)
```

where `v(r)` is the finite vector of prime valuations of a positive rational
`r`.  Then (0.1) is equivalent to nonnegativity on the whole torus of

```text
Q(z)=1+sum_(n in P_Y) lambda_n Re chi_n(z).             (2.3)
```

## 3. Independent external phases

Fix all torus coordinates belonging to primes dividing `ab`.  If `n=p^k`
lies in `E`, its character has the form

```text
chi_n(z)=z_p^k psi_n(z_I),                              (3.1)
```

where `z_p` occurs in no other shell term: there is at most one shell power
with base `p`.  The map `z_p -> z_p^k` is onto the unit circle.  We may
therefore choose every external `z_p` independently so that

```text
lambda_n Re chi_n(z)=-|lambda_n|.                      (3.2)
```

Put

```text
L=sum_(n in E)|lambda_n|,
g(z_I)=1+sum_(n in I)lambda_n Re chi_n(z_I).           (3.3)
```

Global nonnegativity and (3.2) imply

```text
g(z_I)>=L                   for every internal phase z_I. (3.4)
```

Every internal character is nontrivial, so its torus average is zero.
Averaging (3.4) yields

```text
0<=L<=1.                                                  (3.5)
```

Moreover `h=g-L` is nonnegative and has mean `1-L`.  For a nonnegative
torus function, every Fourier coefficient has modulus at most its mean.
The two Fourier coefficients at `+/-v(n/Y)` are `lambda_n/2`; the
noncollision observation after (1.2) shows that they do not aggregate with
another node.  Hence

```text
|lambda_n|<=2(1-L)                 for every n in I.   (3.6)
```

At the identity point of the torus, corresponding to `t=0`, equations
(3.5)--(3.6) give

```text
Q(0)
 =1+sum_E lambda_n+sum_I lambda_n
 <=1+L+2m(1-L).                                        (3.7)
```

If `m=0`, the right side is at most `2`.  If `m>=1`, it is decreasing in
`L` and is at most `1+2m`.  This proves

```text
Q(0)<=max(2,1+2 omega(ab)).                            (3.8)
```

For `Y=(2N+1)/2`, take `a=2N+1`, `b=2`, so `ab=4Y` and (0.2) follows.
QED

## 4. Consequences for the attempted constructions

The exact Delsarte problem only requires `Q>=0` on

```text
H_Y=[Y^.01,Y^(50/33)],                                (4.1)
```

not on the whole line.  Thus (0.2) is a blocker, not the desired finite-band
upper or lower bound.  It nevertheless has four precise consequences.

1. **All-real positive kernels cannot close QP.**  If discretization on the
   actual nodes retains global nonnegativity, its gain is at most logarithmic.
2. **Allowing signed node coefficients does not evade the gate.**  The proof
   minimized each external term according to its coefficient's own sign.
3. **A support-preserving global sum-of-squares hierarchy cannot close QP.**
   Any output of such a hierarchy satisfies (0.1), irrespective of how its
   Gram variables were chosen.
4. **Finite aperture is indispensable.**  A successful fixed-power
   certificate must become negative somewhere beyond `Y^(50/33)`; extending
   its sign condition to all heights destroys the required power gain.

This complements the analytic vertical-capacity gate.  That gate treats
compact shell kernels through their Laplace transforms.  The present theorem
uses only unique factorization, the narrow shell, and global sign; it covers
arbitrary signed coefficients directly on the prescribed prime-power nodes.

## 5. Exact boundary

```text
global actual-node antenna gain:               O(omega(4Y))  PROVED;
global fixed-power Delsarte gain:               IMPOSSIBLE;
all-real SOS/kernel then restriction:           KILLED;
finite-band signed or positive antenna:         OPEN;
QP-KILL / QP-PROMOTE / uniform strip:            NOT PROVED.
```

The remaining target is narrower than before: prove a sign-resolved antenna
which is good only through the polynomial upper edge and whose inevitable
adverse Kronecker return occurs later.

## 6. Replay

The finite replay checks the narrow-shell one-power lemma, the arithmetic
factor count, the affine maximization in (3.7), and the asymptotic separation
between the logarithmic global bound and every fixed power:

```bash
PYTHONPATH=src python3 src/qp_global_antenna_capacity_gate.py --verify
PYTHONPATH=src python3 -m pytest -q src/test_qp_global_antenna_capacity_gate.py
```

