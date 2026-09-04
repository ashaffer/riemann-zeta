# HT-HAT(0.019): frozen finite diagnostic

Date frozen: 2026-08-31  

The pre-run hostile audit amended the logical passport and replay requirements
without changing any numerical parameter, center, seed, or stopping rule.
Machine card: `results/context/zeta23_ht_hat_prereg_v1.json`

## The exact candidate

Fix

\[
 w=\frac15,\qquad \alpha=\frac{49}{100},\qquad
 \phi(u)=\left(1-\frac{|u|}{w}\right)e^{\alpha u}.
\]

For a frozen half-integer $Y$, list the ordinary primes

\[
 Ye^{-w}\leq p\leq Ye^w,
 \qquad v_p=\log(p/Y),
\]

in increasing order.  Let \(\ell_p\) be the ordinary piecewise-linear nodal
hat on these log nodes, truncated at the first and last node, and set

\[
 a_{p,Y}=\int_{v_1}^{v_J}\phi(u)\ell_p(u)\,du,
 \qquad
 \lambda_{p,Y}=\frac{a_{p,Y}}{\sum_q a_{q,Y}},
 \qquad
 P_Y(t)=\sum_p\lambda_{p,Y}\cos(tv_p).
\]

The finite statement tested at each frozen center is

\[
 P_Y(t)\geq-Y^{-19/1000}
 \quad
 \left(Y^{931/2000}\leq t\leq Y^{50/33}\right).
\]

The centers, fixed before looking, are

\[
 Y\in\{512.5,1024.5,2048.5,4096.5\}.
\]

## Theorem passport and route position

This is a QP/Turan diagnostic using ordinary primes, the complete stated shell,
a fixed nonnegative coefficient vector, probability normalization by its
truncated mass, and the full continuum band.  It does not optimize the weights
after seeing the frequencies.

The target tested here is a **one-sided normalized floor**.  It is weaker than
the earlier report's two-sided raw \(|b-P|\) high-tail approximation target.
Accordingly, this run is a bounded falsifier for one explicit DPA candidate,
not an execution or proof of that stronger theorem.

The existing low/mid theorem is an \(O(Y^{-.019})\) estimate with an
unsharpened constant.  Consequently, even an asymptotic proof of the target
here combines directly to give DPA_P(c) for every \(c<.019\), rather than
literal coefficient-one DPA_P(.019).  Choosing \(.0189<c<.019\) preserves the
intended exponent ordering.  The parallel LTRAD_P(.0189,.001) sibling remains
independently open; this experiment cannot establish the QP contradiction or
the strip by itself.

## Controls and falsifiers

Every control receives freshly computed hat weights.

1. **Odd half-grid.**  Keep the two endpoint nodes and snap every interior
   node to the nearest same-sign odd multiple of \(\pi/B\),
   \(B=Y^{50/33}\).  Order and uniqueness are mandatory.  At $t=B$, all
   snapped interior cosines must equal $-1$ to numerical precision.  This is
   the positive control showing that the scan detects a deliberately aligned
   antipode.
2. **Order-preserving jitter.**  Keep endpoints fixed and perturb internal
   nodes by the frozen PCG64 seeds and amplitudes in the machine card.  These
   controls preserve rank, sign, aperture, and local gap scale, but not
   arithmetic structure.

No post-outcome scale additions or parameter changes are licensed.

## Decision rule and trust labels

The floating phase grid and local optimization are `FLOAT-SCOUT` only.  For
the actual prime vector, a `PASS` requires a complete Arb interval cover.  On
each cell \([a,b]\), positivity of the weights gives the rigorous interpolation
bound

\[
 \inf_{[a,b]}P_Y
 \geq
 \min\{\underline{P_Y(a)},\underline{P_Y(b)}\}
 -\frac{(b-a)^2}{8}\sum_p\lambda_{p,Y}v_p^2.
\]

All such leaf bounds must exceed the exact Arb enclosure of
\(-Y^{-19/1000}\).  A `FAIL` requires a rigorous in-band Arb point witness
strictly below that floor.  Otherwise the result is `INCONCLUSIVE`.  Any
decisive outcome is recomputed by the same implementation at 256 bits.  This
is a precision-stability check, not independent software verification.  The
accepted dyadic leaves must additionally be prefix-free, have Kraft sum one,
and survive an executable from-disk leaf-hash replay.  The artifact records a
source-code hash.

## Logical ceiling

Even four certified passes prove only four finite fixed-vector inequalities.
They do **not** prove eventuality in (Y), `HT-HAT(0.019)`, `DPA_P(0.019)`, a
uniform zero-free strip, or RH.  The useful outcome is narrower: determine
whether this explicit candidate is already falsified, whether the finite
margin is large or collapsing, and whether actual prime geometry visibly
separates from matched non-arithmetic controls.
