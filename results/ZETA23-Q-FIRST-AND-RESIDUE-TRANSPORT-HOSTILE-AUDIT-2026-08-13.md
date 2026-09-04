# Hostile audit: universal base, `q`-first transport, and residue moments

**Date:** 2026-08-13  
**Binary verdict:** **PATCH** overall; both deletion theorems pass after exact
scope patches, and the finite residue identities pass after normalization
fields were added.

## 1. Verdict ledger

```text
universal rough-base q-group saving beta/2=.0799:     PASS
claim that it controls the full antenna:              NOT MADE
universal theorem superseded for the q-group:         YES
global integer-base q-first saving beta=.1598:        PASS
composite selected denominators:                      PASS
changing q across blocks / adjacent deleted nodes:    PASS
long-edge or boundary discard needed for q-group:     NO
all later centers non-q_I in their own block:         PASS
finite twice-mass Parseval identities:                PASS
old all-nonzero ledger sharp for composite q:         PATCHED
principal subtraction for a != 0 identities:          PATCHED
selector-uniform signed non-q tail:                    OPEN
integer/logarithmic taper transfer:                    SEPARATE INPUT
```

The stronger conclusion is therefore

```text
Y^-1 sum_I |D_I^(first)|
   << Y^(-799/5000+o(1)),                            (1.1)
```

uniformly over arbitrary blockwise reduced fractions with
`q_I>=Y^(799/5000)`.  The rough-gap square theorem is no longer needed for
this resonant group.  It remains a correct theorem and may have other uses.

## 2. Why the global `q`-first deletion is exact

On half-open blocks `I`, let

```text
D={interior n in I: q_I divides n}.
```

Since `q_I<Y` and the shell lies at size `Y`, no point of `D` is prime.
Start from the integer lattice, delete `D` simultaneously, and then delete
every other composite.  The final active set and the initial active set are
unchanged from the original telescope.  Every center deleted in the second
group lies in some block `I` and is not divisible by that block's `q_I`.

Every initial interior integer cell has mass one.  Simultaneous deletion,
including deletion of adjacent nodes, therefore gives

```text
||nu_(Z\D)-nu_Z||_TV=2 #D.                          (2.1)
```

Partition each deleted integer's original Voronoi cell according to the
final survivor receiving that mass.  This is a canonical cellwise
decomposition even if the receiver is across a curvature-block boundary.
For every bounded, blockwise selected test function `f`,

```text
sum_I |D_I^(first)(f)|
 <=2 ||f||_infty sum_I #D_I.                        (2.2)
```

The elementary count

```text
sum_I #D_I <=sum_I (|I|/q_I+O(1))
             <<Y^(1-beta)+K
```

proves (1.1), because `K<<Y^(1-8/33)=o(Y^(1-beta))`.
Prime endpoints are permanent survivors and automatically stop transport
across prime gaps.  Long gaps cause no extra cost in (2.1), and a jump in
`f`, `a_I`, or `q_I` at a block boundary is harmless under total variation.

For one fixed denominator with no boundary interaction, the exact residue
vector of the first group is

```text
v_0=-2N,       v_1=v_(-1)=N,
```

so its Fourier coefficient is
`N(cos(2*pi*a/q)-1)`.  This explicit formula is not needed globally; the
total-variation proof remains valid when different block deletion sets have
adjacent nodes.

## 3. Relation to the universal rough-base theorem

The theorem based on `R_(Y^(4/25))` is internally correct:

```text
sum_I E_I <<Y(log Y)^2,
sum_I N_I <<Y^(1-beta),
sum_I |D_I| <<sqrt(sum N_I sum E_I),
```

which gives the normalized saving `beta/2=.0799`.  The refinement argument
is selector-stable after its stated boundary-edge removal.  It is strictly
superseded by (1.1) for the resonant group, because the integer base makes
every deleted cell have mass one.

One scope correction was required.  At the retained-gap cutoff
`theta=797/5000`, the block-boundary cost saves `.0830242...`, but the
separate Gafni--Tao long-gap tail saves only

```text
1173/65000=.0180461538....                           (3.1)
```

Thus the `.0799` q-group bound clears the maximum carrier bill on retained
edges; (3.1) does not itself clear a bill `.01974049`.  The global q-first
proof avoids both removals for the q-group.  Neither statement bounds the
remaining signed arithmetic tail.

## 4. Exact residue-vector normalization

Let `v=(v_r)_(r mod q)` be a **twice-mass** vector for a signed transport and
write

```text
R_v(a;q)=1/2 sum_(r mod q) v_r e_q(ar),
C_s=sum_r v_r v_(r+s).                              (4.1)
```

For the pre-, at-, post-, q-first, and q-first-tail transport vectors,
`sum_r v_r=0`.  Exact Parseval and the exact fourth moment are

```text
sum_(a mod q)|R_v(a;q)|^2 =q/4  sum_r v_r^2,         (4.2)
sum_(a mod q)|R_v(a;q)|^4 =q/16 sum_s C_s^2.         (4.3)
```

For a non-zero-sum vector, such as the initial or final trapezoid rule, the
sums over `a != 0` require subtraction of

```text
|R_v(0;q)|^2=(sum v_r/2)^2,
|R_v(0;q)|^4=(sum v_r/2)^4.                          (4.4)
```

The code now reports these principal-subtracted identity errors explicitly.

When `q` is composite, the selected numerator is primitive.  Summing over
all `a != 0` is valid but can be very wasteful because it includes
imprimitive characters.  If `c_q` is the Ramanujan sum, the sharp primitive
moment totals are

```text
M_2^*(v;q)
 =sum_((a,q)=1)|R_v(a;q)|^2
 =1/4 sum_(r,t) v_r v_t c_q(r-t),                   (4.5)

M_4^*(v;q)
 =sum_((a,q)=1)|R_v(a;q)|^4
 =1/16 sum_(s,t) C_s C_t c_q(s-t).                  (4.6)
```

Consequently

```text
max_((a,q)=1)|R_v(a;q)|
 <=min((M_2^*)^(1/2),(M_4^*)^(1/4)).                (4.7)
```

The patched ledger reports reduced-frequency RMS, fourth mean, deterministic
envelopes, and the actual reduced maximum separately from the all-nonzero
quantities.

## 5. Sharp sufficient inequalities for the live tail

For one fixed denominator, a coefficient-blind sufficient condition for

```text
Y^-1 max_((a,q)=1)|R_v(a;q)| <=Y^(-kappa-epsilon)
```

is either

```text
M_2^*(v;q) <=Y^(2-2kappa-2epsilon),                 (5.1)
M_4^*(v;q) <=Y^(4-4kappa-4epsilon).                 (5.2)
```

Using the full-frequency identities gives the simpler, stronger sufficient
conditions

```text
q sum_r v_r^2 <=4Y^(2-2kappa-2epsilon),             (5.3)
q sum_s C_s^2 <=16Y^(4-4kappa-4epsilon).            (5.4)
```

If `q=Y^(b+o(1))`, these demand respectively

```text
sum_r v_r^2 <=Y^(2-b-2kappa-2epsilon+o(1)),
sum_s C_s^2 <=Y^(4-b-4kappa-4epsilon+o(1)).          (5.5)
```

For a common-height selector with blocks `I`, moduli `q_I`, and independently
selected primitive numerators `a_I`, the exact deterministic sufficient
inequality is instead

```text
sum_I min((M_(2,I)^*)^(1/2),(M_(4,I)^*)^(1/4))
   <=Y^(1-kappa-epsilon).                            (5.6)
```

This is the correct selector normalization.  If only summed moment totals
are available, Cauchy and Holder give the relaxations

```text
K sum_I M_(2,I)^* <=Y^(2-2kappa-2epsilon),          (5.7)
K^3 sum_I M_(4,I)^* <=Y^(4-4kappa-4epsilon).        (5.8)
```

Thus separate blockwise `L2` control pays a `sqrt(K)` amplitude loss, and
separate `L4` control pays `K^(3/4)`.  An average over numerators cannot be
inserted without these maximum/envelope steps: the common-height selector is
adversarial, not random.

If every block has the same modulus and numerator, one may first add its
residue vectors and apply (4.2)--(4.3) to the sum.  That avoids a formal
`K` loss only by requiring the cross-block cancellation that the desired
theorem must prove.  With varying `q_I`, there is no selector-independent
common finite Fourier group of comparable size.

## 6. Exact surviving target

For fixed `q`, the q-first laboratory computes

```text
R_q^(nonq)=T(primes)-T(Z minus qZ),                 (6.1)
```

as `nonresonant_twice_mass` in
`src/universal_q_reorder_transport.py`.  This is not the same object as
`post_q_vector()` in `src/spf_residue_transport.py`, which uses the
traditional least-prime-factor order and means only the sum of stages
`p>q`.  For composite `q`, there is no least-prime-factor stage `p=q` at all.

The exact remaining arithmetic target is a selector-uniform proof of (5.6),
or a stronger direct coefficient estimate, for the blockwise q-first tails.
The fact that every deletion center is nonzero modulo its local `q_I` does
not imply this cancellation.  Equation (6.1) is, up to its explicit
punctured-lattice term, essentially the selected prime statistic itself.

Finally, the finite vectors use a frozen additive phase on integer nodes.
Changing the sign convention conjugates the transform and does not affect
the moment bounds.  Passing to the logarithmic phase, taper, continuum
baseline, and shell collars remains a separate transfer; integer-valued
coefficients are then replaced by weighted coefficients, although the
Fourier identities themselves persist with the appropriate conjugates.

## 7. Patched and verified artifacts

```text
results/ZETA23-UNIVERSAL-ROUGH-BASE-SELECTOR-Q-GROUP-2026-08-13.md
results/ZETA23-Q-FIRST-INTEGER-BASE-RESONANT-GROUP-2026-08-13.md
results/verify_zeta23_q_first_integer_base.py
src/spf_residue_transport.py
src/test_spf_residue_transport.py
src/universal_q_reorder_transport.py
src/test_universal_q_reorder_transport.py
```

Verification:

```text
9 residue/universal transport tests:                 PASS
universal rough-base exponent/refinement checker:    PASS
q-first fixed-q and varying-q adjacent-node checker: PASS
```
