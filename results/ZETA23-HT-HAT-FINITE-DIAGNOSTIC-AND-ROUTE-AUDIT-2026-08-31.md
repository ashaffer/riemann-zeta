# HT-HAT finite diagnostic and route audit

Date: 2026-08-31

Preregistration:
[machine card](context/zeta23_ht_hat_prereg_v1.json) and
[theorem card](ZETA23-HT-HAT-PREREGISTRATION-2026-08-31.md).

Primary data:
[finite diagnostic](ZETA23-HT-HAT-FINITE-DIAGNOSTIC-2026-08-31.json) and
[Arb certificates](ht_hat_certificates_2026_08_31/).

## Verdict

All four preregistered **finite fixed-vector** inequalities pass:

\[
 P_Y(t)\geq -Y^{-19/1000}
 \qquad
 (Y^{931/2000}\leq t\leq Y^{50/33})
\]

for the exact explicit BHP hat vector at
\(Y=512.5,1024.5,2048.5,4096.5\).  Each pass has a complete Arb
continuum cover at 192 and 256 bits, an exact prefix-free dyadic partition
with Kraft sum one, and a successful source-hashed from-disk replay.

This does **not** prove the asymptotic HT-HAT statement.  It does not prove the
earlier two-sided raw high-tail approximation theorem, DPA_P, LTRAD_P, a
uniform zero-free strip, or RH.

## Certified results

| \(Y\) | primes | floating minimum | floor | depth/floor | 256-bit leaves | actual rank among actual + 9 jitters |
|---:|---:|---:|---:|---:|---:|---:|
| 512.5 | 33 | -0.5181819103 | -0.8882103233 | 0.583400 | 522 | 7/10 |
| 1024.5 | 59 | -0.3949336487 | -0.8765975908 | 0.450530 | 2,045 | 7/10 |
| 2048.5 | 104 | -0.3047493943 | -0.8651326780 | 0.352257 | 4,096 | 3/10 |
| 4096.5 | 198 | -0.2655989333 | -0.8538157342 | 0.311073 | 16,384 | 5/10 |

The displayed minima are FLOAT-SCOUT locations.  The PASS claims do not rely
on them: every continuum cell was bounded by

\[
 \inf_{[a,b]}P_Y
 \geq
 \min\{\underline{P_Y(a)},\underline{P_Y(b)}\}
 -\frac{(b-a)^2}{8}
   \frac{\sum_p a_{p,Y}v_p^2}{\sum_p a_{p,Y}}.
\]

The Arb evaluator used the shared raw numerator and mass
\[
 P_Y(t)=
 \frac{\sum_p a_{p,Y}\cos(tv_p)}{\sum_p a_{p,Y}},
\]
so the certificate is not a rounded-node or rounded-weight proxy.

The primary JSON has SHA-256

\[
\texttt{a1a3264a4694273772cb53e549fe32b71abc881e6e9d2ea47ce2a51739aa293e}.
\]

The certified source hash is

\[
\texttt{766274b3239be32ad38c827a4478f1c2e1f3f4346c3a4470b221c10307daefea}.
\]

This is same-code replay and precision stability, not independent formal
verification or a kernel-checked theorem.

## Controls

The odd half-grid positive control worked at every scale.  Its minima were
between \(-0.9947\) and \(-0.99999\), with target ratios
\(1.120,1.138,1.155,1.171\); hence it violated the target four times.  The
scanner therefore detects an intentionally planted antipodal obstruction.

The nine order-preserving jitter controls gave target-ratio ranges

\[
\begin{array}{c|c}
Y & \text{jitter range}\\ \hline
512.5 &[0.5054,0.6151]\\
1024.5 &[0.3824,0.4760]\\
2048.5 &[0.3366,0.4185]\\
4096.5 &[0.2647,0.3274].
\end{array}
\]

The actual vector sits inside these ranges and has ranks \(7,7,3,5\) out of
ten when smaller depth is ranked better.  There is no visible finite
actual-prime advantage over the matched local perturbations.

## What information was gained

Three hypotheses were separated.

1. The explicit hat candidate is already destroyed by a moderate-scale
   high-tail antipode: **not observed at the four licensed scales**.
2. The numerical/certification apparatus is too weak to see an obstruction:
   **rejected by the half-grid controls**.
3. The favorable finite trend is visibly caused by prime-specific arithmetic:
   **not supported**, because the jitter controls share it.

The depth ratios decrease from \(0.583\) to \(0.311\), and the pointwise
empirical depth exponents rise from \(0.105\) to \(0.159\).  This is
encouraging for survival of the candidate, but it is not an asymptotic
estimate.  At these centers the target floors are still between \(-0.888\)
and \(-0.854\), close to the universal convexity floor \(-1\).  The run mainly
rules out near-total phase alignment; it does not yet test the eventual
near-zero floor in the true asymptotic regime.

## The exact mathematics exposed by the run

Let \(I_V\) be linear interpolation on consecutive prime-log nodes.  The
definition of the weights gives the exact identity

\[
 \left(\sum_p a_{p,Y}\right)P_Y(t)
 =
 \int_{v_1}^{v_J}\phi(u)\,I_V[\cos(t\,\cdot)](u)\,du.
\]

On a cell with midpoint \(m_j\), width \(d_j\), and \(u=m_j+x\),

\[
\begin{aligned}
I_V[\cos(t\,\cdot)](m_j+x)-\cos(t(m_j+x))
={}&\cos(tm_j)\{\cos(td_j/2)-\cos(tx)\}\\
&+\sin(tm_j)\{\sin(tx)-(2x/d_j)\sin(td_j/2)\}.
\end{aligned}
\]

Thus the open high-tail problem is an aggregate, signed interpolation-error
problem over prime gaps, not a local mesh-size estimate.  A double-precision
analytic evaluation at the four observed floating minima gave normalized
continuous-integral values only

\[
2.13\cdot10^{-5},\quad 1.98\cdot10^{-6},\quad
2.33\cdot10^{-6},\quad -2.06\cdot10^{-7},
\]

while the discrete minima had magnitude \(0.27\) to \(0.52\).  The finite
minima are therefore almost entirely the aggregate interpolation error.  The
median cell phase \(t d_j\) at those minima was between \(120\) and \(251\);
the low-frequency Taylor/mesh argument is far outside its valid regime.

## Decision-tree update

The correct next move is **not** to append larger centers to this ladder.
That would violate the stopping rule and, because the matched jitters show the
same trend, has low arithmetic information gain.

The surviving analytic target is a one-sided aggregate interpolation-error
theorem.  A useful proof attempt must exploit cancellation among the exact
cell terms above, equivalently a gap-weighted exponential sum over
\[
e^{it m_j}=\left(\frac{\sqrt{p_jp_{j+1}}}{Y}\right)^{it},
\]
uniformly over the transition and high bands.  A bound based only on the
largest prime gap cannot work because \(t d_j\gg1\) here.  Before another
finite experiment, the highest-information task is to determine whether
summation by parts, prime Dirichlet-polynomial estimates, or a blockwise
large-sieve argument supplies a fixed saving for this exact signed statistic.

Finally, the route adapter must retain its exponent slack.  The existing
low/mid result is \(O(Y^{-.019})\) with an unsharpened constant, so an
asymptotic HT-HAT(.019) result combines directly to DPA_P(c) for every
\(c<.019\), for example \(c=.01895\), not literal coefficient-one
DPA_P(.019).  LTRAD_P(.0189,.001) remains a separate open sibling.
