# QP mass radialization: atomic defect, exact threshold, and binary gate

**Date:** 2026-08-15  
**Binary verdict:** the probability-normalized radialization statement is
**false on the actual prime shells**.  After replacing it by the exact
Turan mass normalization, neither a counterexample nor a proof is known.
The weakest statement sufficient for a strip is the threshold implication
`LTRAD(d,c)` below; it is already a coefficient-sensitive localized prime
modulus theorem, not a consequence of abstract convex geometry.

No QP theorem, QP-to-strip implication, or zero-free strip is proved here.

---

## 1. The probability-normalized statement is exactly false

Let

```text
K_N=[N^(1/2),N^(A')],                  1<A'<50/33,
R_N^K=sup_(N<=Y<=2e^wN) r_+(K_N;S_Y),
R_N^QP=sup_(N<=Y<=2e^wN) r_+(H_Y;S_Y).               (1.1)
```

Define the discarded probability depth by taking the supremum of

```text
-M^(-1) sum_(p in I) cos[t log(p/Y)].                 (1.2)
```

For every sufficiently large `N`, choose a prime `p in [N,2N]` and put
`Y=p+1/2`.  Then `p` lies in the width-`w` shell, and

```text
t_p=pi/log(Y/p)=2pi p+O(1).                           (1.3)
```

Thus `t_p in K_N` for large `N`, while

```text
cos[t_p log(p/Y)]=-1.                                 (1.4)
```

The singleton interval `I={p}` proves that (1.2) has supremum exactly `1`.

On the other hand, the unconditional Vinogradov--Korobov tent certificate
on the actual prime-power nodes, proved in
`ZETA23-QP-TENT-EXPLICIT-FORMULA-STRIP-AND-AMPLIFICATION-GATE-2026-08-15.md`,
gives

```text
R_N^QP<=exp[-c (log N/log log N)^(1/3)]=o(1).         (1.5)
```

Consequently, for every fixed `lambda>0` and `C<infinity`,

```text
1 not<=C(R_N^QP)^lambda                               (1.6)
```

for all large `N`.  This is an actual-prime counterexample to the original
probability-normalized `RAD_hi`, not a generic toy model.

---

## 2. Correct mass normalization

The natural quantity is

```text
E_N^-(A')=
 sup -N^(-1)sum_(p in I)cos[t log(p/Y)],              (2.1)
```

with the same centers, shells, and common band `K_N`.  A singleton now has
size only `1/N`.

The half-integer phase theorem and a partition into

```text
J_w=ceil(2log2/w)                                    (2.2)
```

logarithmic pieces prove

```text
L_N(A')<=(4/3)J_w E_N^-(A'),                         (2.3)
```

where `L_N` is Turan's `N^(-1)` prime-interval modulus.  Conversely, every
event in (2.1) is bounded by the modulus of that same prime sum.  Hence
`E_N^-` and the localized natural prime modulus are equivalent up to the
fixed phase-partition and comparable-scale constants.  More precisely, the
reverse bound uses `sup_(N' asymp N)L_(N')`, since an allowed shell can lie
across a neighboring dyadic scale; it is not literally `E_N^-<=L_N` with
`L_N` restricted to intervals inside `[N,2N]`.

Pairing a high-band antipode with the uniform probability on all shell
primes and using the prime number theorem gives only

```text
E_N^-(A')>>_w R_N^K/log N.                            (2.4)
```

This has the wrong direction for the reverse bridge.  The corrected open
power comparison is

```text
MRAD_QP(lambda): E_N^-(A')<< (R_N^QP)^lambda.         (2.5)
```

Here `R_N^K<=R_N^QP`; only the common-band radius occurs in the automatic
wrong-way estimate (2.4), while the larger full QP radius is the weakest
one sufficient in (2.5).  The singleton counterexample does not refute
(2.5).

---

## 3. Weakest sufficient inverse statement

For fixed `d,c>0`, define

```text
LTRAD(d,c):
E_N^-(A')>=N^-d  ==>  R_N^QP>=N^-c                  (3.1)
```

for all sufficiently large `N`.  If DPA is known with exponent `c_0>c`,
then `R_N^QP<=N^-c_0=o(N^-c)`, so (3.1) forces
`E_N^-<N^-d`.  Equation (2.3) then gives the natural prime saving
`L_N<<N^-d`, and the audited local Turan theorem gives strip width
`(d/A')^2` when its half-power coverage condition holds.

This threshold form is strictly all that the reverse proof needs.  It also
removes every atomic loophole: an event on the left side of (3.1) must obey

```text
M>=-sum_(p in I)cos[t log(p/Y)]>=N^(1-d).             (3.2)
```

Thus one may restrict (3.1) to prime intervals containing at least
`N^(1-d)` primes.  For `d=.019`, the required event has at least
`N^.981` atoms.

---

## 4. Why the corrected gate remains open

A large negative value in (2.1) is one scalar statement in the uniform
prime-interval direction.  The full QP radius in (1.1) asks for a positive
measure on `H_Y` whose moment is the same negative number at every prime-power node,
or equivalently tests every signed coefficient vector of carrier one.
Neither averaging the one large direction nor restricting to its
`N^(1-d)` atoms supplies those simultaneous equal moments.

The support-only Fejer constructions in the existing bridge report violate
power directional-to-radial comparisons even after rational independence
and finite-aperture perturbation.  They are not actual-prime
counterexamples, but they prove that a valid (3.1) must use quantitative
arithmetic of the complete prime shell.  Since (2.3) and the trivial reverse
modulus inequality make `E_N^-` a localized form of the original natural
prime modulus, proving (3.1) is essentially the coefficient adapter `COMP`,
not a weaker generic inverse theorem.

```text
probability-normalized RAD:          FALSE, actual primes;
mass-normalized phase bridge:        PROVED;
atomic floor at strip threshold:     REMOVED;
MRAD_QP(lambda):                     OPEN;
LTRAD(d,c):                          OPEN;
actual-prime counterexample to MRAD: NOT FOUND;
QP => strip:                         NOT PROVED.
```

Replay is in `src/qp_zeta_reverse_phase_gate.py` and
`src/test_qp_zeta_reverse_phase_gate.py`.
