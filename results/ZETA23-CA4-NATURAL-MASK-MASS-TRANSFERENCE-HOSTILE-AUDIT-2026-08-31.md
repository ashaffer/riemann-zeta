# Hostile audit of natural-mask transference into `CA4`

Date: 2026-08-31

Routing state: [`ZETA23-UNIFORM-STRIP-CONSOLIDATED-STATE-AND-INTUITION-PUMPS-2026-08-30.md`](ZETA23-UNIFORM-STRIP-CONSOLIDATED-STATE-AND-INTUITION-PUMPS-2026-08-30.md)
Immediate input: [`ZETA23-HAT-TRANSITION-AND-CENTERED-SEMIPRIME-CA4-GATE-2026-08-31.md`](ZETA23-HAT-TRANSITION-AND-CENTERED-SEMIPRIME-CA4-GATE-2026-08-31.md)
Yang--Yang truncation audit: [`ZETA23-YANG-YANG-7962-ZENODO-HOSTILE-AUDIT-2026-08-31.md`](ZETA23-YANG-YANG-7962-ZENODO-HOSTILE-AUDIT-2026-08-31.md)

## Verdict

The contemplated **mass-preserving, coefficient-blind transference is
refuted**.  A scalar theorem for the natural
`(Lambda*Lambda)(m)(Lambda*Lambda)(m+h)` correlation, even at the right
shift scale, does not imply `CA4` from the gap-tail, density, normalization,
or coefficient-norm information currently available.

There is one faithful conditional adapter, but it is selector-sensitive.
It must control the same band-pass norm after twisting the four prime slots
by the exact predecessor/successor-gap ratios.  Equivalently, it must control
the fourth moment of the difference between the hat vector and the closest
natural vector.  This is new input, not a consequence of scalar natural
`HL*(4)`.

An exact bounded-gap motif proves the obstruction at proof-class level.  It
has natural phases `++--` and hat-to-natural ratios

```text
(5/4, 5/4, 3/4, 3/4).
```

Its natural transform vanishes at the selected height while the hat
transform equals `1/4`.  At semiprime level it has positive and negative
signed discrepancy masses both equal to `9/64`, total `l1` discrepancy
`9/32`, and squared `l2` discrepancy

\[
 \frac{33}{128N^2}-\frac{65}{256N^3}.
\]

Every gap is only a constant multiple of the mean gap.  Thus long-gap
deletion, small mesh, prime-scale density, normalization, and diagonal-size
control do not distinguish it.  This is an integral/real-node pseudo-prime
model, not an actual-prime counterexample.  Actual-prime `CA4` remains
**OPEN**.

---

## 1. Passport and the closest possible natural comparator

This audit stays on the QP/Turan positive-antenna branch.  It does not import
a density-of-zeros conclusion into the uniform-strip branch.

For consecutive shell primes, put

\[
 u_j=\log(p_j/Y),\qquad
 \Delta_j=u_{j+1}-u_j,
 \qquad \rho_j={\bf1}_{p_{j+1}-p_j\leq Y^{163/1000}}.
\]

With the frozen tilted tent `phi`, the exact unnormalized retained hat weight
at `p_j` is

\[
\begin{aligned}
 w_j={}&\rho_{j-1}
 \int_{u_{j-1}}^{u_j}\phi(u)
       \frac{u-u_{j-1}}{\Delta_{j-1}}\,du\\
 &+\rho_j
 \int_{u_j}^{u_{j+1}}\phi(u)
       \frac{u_{j+1}-u}{\Delta_j}\,du,
 \qquad
 \lambda_j=\frac{w_j}{\sum_r w_r}.                 \tag{1.1}
\end{aligned}
\]

Thus `lambda` is a probability fixed before `t` is seen.  It satisfies

\[
 S_\lambda:=\sum_j\lambda_j^2
 \ll_\varepsilon Y^{-q+\varepsilon},
 \qquad q=\frac{2787}{3250}.                        \tag{1.2}
\]

Give a natural theorem every favorable passport repair: discard prime powers,
use the same shell and tent, and define

\[
 \eta_j=
 \frac{\phi(u_j)\log p_j}{\sum_r\phi(u_r)\log p_r}.
                                                               \tag{1.3}
\]

The convolution `b=eta*eta` is the smoothly tapered, prime-only shell
restriction of `Lambda*Lambda`.  It is closer to `lambda` than the untapered,
prime-power-inclusive sequence in the natural higher-trace problem.  A
failure to transfer from (1.3) therefore cannot be repaired merely by
restoring those passport mismatches.

Set

\[
 a_n=\sum_{p_ip_j=n}\lambda_i\lambda_j,
 \qquad
 b_n=\sum_{p_ip_j=n}\eta_i\eta_j.                  \tag{1.4}
\]

Both are positive probabilities on shell semiprimes.  If
`r_j=lambda_j/eta_j`, unique factorization gives the exact mask identity

\[
 a_{p_ip_j}=r_i r_j b_{p_ip_j}.                    \tag{1.5}
\]

Consequently natural `HL*(4)` controls the case `r=1`, whereas `CA4` needs
the correlation twisted by four actual adjacent-gap ratios.

---

## 2. Exact norm ledger

Let

\[
 S_\eta=\sum\eta_j^2,
 \quad C=\sum\lambda_j\eta_j,
 \quad D_1=\sum|\lambda_j-\eta_j|,
 \quad D_2=\sum|\lambda_j-\eta_j|^2.
\]

Unique factorization gives, without an asymptotic or probabilistic step,

\[
 \|a\|_1=\|b\|_1=1,\qquad
 \|a\|_2^2=2S_\lambda^2-\sum_j\lambda_j^4,          \tag{2.1}
\]

and

\[
\begin{aligned}
 \|a-b\|_2^2={}&2S_\lambda^2+2S_\eta^2-4C^2
 -\sum_j\lambda_j^4-\sum_j\eta_j^4
 +2\sum_j\lambda_j^2\eta_j^2.                    \tag{2.2}
\end{aligned}
\]

Also

\[
 \|a-b\|_1\leq 2D_1.                              \tag{2.3}
\]

The fact that both sides of (1.4) have total mass one gives only
`sum(a-b)=0`; it gives no small vector norm.

The PNT on a fixed shell gives

\[
 S_\eta=Y^{-1+o(1)}.
\]

The currently proved information implies only

\[
 D_2\leq2S_\lambda+2S_\eta
 \ll Y^{-q+o(1)}.                                  \tag{2.4}
\]

There is no proved estimate `D_1=o(1)`.  In the exponential-gap heuristic,
the leading ratio is

\[
 r_j\simeq\frac{g_{j-1}+g_j}{2\log Y}.
\]

Thus `r` has the Gamma `(shape 2, rate 2)` law, for which

\[
 \mathbb E|r-1|=4e^{-2}=.54134\ldots,
 \qquad \mathop{\rm Var}(r)=\frac12.               \tag{2.5}
\]

This predicts `D_1` of constant order and
`D_2 asymp (log Y)/Y`.  Equation (2.5) is only an intuition pump; the exact
countermodel below, rather than this heuristic, supplies the no-go result.

---

## 3. Quantitative thresholds for every generic adapter

Write

\[
 M_x(t)=\sum_jx_j e^{itu_j}.
\]

`CA4` requires, for `T=Y^alpha` and
`1049/1250 <= alpha <= 50/33`, the scale

\[
 \int_T^{2T}|M_\lambda(t)|^4dt
 \ll T Y^{-2q+1/10+o(1)},
 \qquad -2q+\frac1{10}=-\frac{5249}{3250}.          \tag{3.1}
\]

Suppose optimistically that a natural theorem already proves (3.1) with
`eta` in place of `lambda`.  Minkowski shows that it is enough to prove the
same estimate for `delta=lambda-eta`.

### `l1` route

Since `|M_delta(t)|<=D_1`, a sufficient condition is

\[
 D_1\ll Y^{-5249/13000+o(1)}
       =Y^{-.403769\ldots+o(1)}.                   \tag{3.2}
\]

Neither current theorems nor the natural gap model approach (3.2).

### `l2` plus generic mean value

The semiprime coefficients of `M_delta^2` have the exact squared norm

\[
 2D_2^2-\sum_j|\delta_j|^4\leq2D_2^2.
\]

The ordinary mean-value theorem at product length `Y^2` therefore gives

\[
 \int_T^{2T}|M_\delta(t)|^4dt
 \ll (T+Y^2)D_2^2Y^{o(1)}.                         \tag{3.3}
\]

Because `T<Y^2`, this route needs

\[
 D_2\ll
 Y^{-q+1/20+\alpha/2-1+o(1)}.                     \tag{3.4}
\]

At the two endpoints, the exact requirements are

| `alpha` | required squared node distance `D_2` | deficit from the proved exponent `q` |
|---:|---:|---:|
| `1049/1250` | `Y^(-11277/8125)=Y^-1.387938...` | `663/1250=.5304` |
| `50/33` | `Y^(-225217/214500)=Y^-1.049962...` | `127/660=.192424...` |

Even the favorable heuristic scale `D_2=Y^{-1+o(1)}` misses the top
endpoint by a moment factor `Y^(10717/107250)=Y^.099925...`.  The proved
scale (2.4) simply reproduces the generic conductor deficit, at least

\[
 Y^{2-50/33-1/10}=Y^{127/330}.                     \tag{3.5}
\]

### Exact band-norm route

For a nonnegative dyadic cutoff, let

\[
 Q_T(c)=T\sum_{m,n}c_m\overline{c_n}
 K\!\left(T\log\frac mn\right).
\]

This is positive semidefinite.  Hence

\[
 \sqrt{Q_T(a)}\leq\sqrt{Q_T(b)}+\sqrt{Q_T(a-b)}.    \tag{3.6}
\]

Thus a bound of the target size for `Q_T(a-b)` is a correct adapter.  But by
(1.5), this is precisely a four-slot, gap-selector-sensitive twisted
correlation.  Scalar natural correlation control supplies no estimate for
it.

---

## 4. Mass audit of the possible partitions

### 4.1 The one licensed mass-preserving gap truncation

The two shares on one retained edge sum exactly to

\[
 \int_{u_j}^{u_{j+1}}\phi(u)\,du.                  \tag{4.1}
\]

The published exceptional-gap input therefore proves that deleting
`g_j>Y^(163/1000)` removes only

\[
 O_\varepsilon(Y^{-267/13000+\varepsilon})          \tag{4.2}
\]

of the raw hat mass.  Renormalization changes the probability vector by at
most twice that amount in `l1`.  This is a genuine mass-preserving
truncation.  It has already been taken in the definition of `CA4`.

It does not naturalize the retained weights.  In a dyadic interior gap bin
`G<g_j<=2G`, (4.1), `Delta_j~g_j/Y`, and the PNT give

\[
 \begin{aligned}
 \text{hat edge mass}&\asymp
      \frac1Y\sum_{j\ \mathrm{in\ bin}}\phi(u_j)g_j,\\
 \text{natural endpoint mass}&\asymp
      \frac{\log Y}{Y}\sum_{j\ \mathrm{in\ bin}}\phi(u_j).
                                                               \tag{4.3}
 \end{aligned}
\]

Their ratio is of order `G/log Y`.  Rare larger retained gaps are therefore
upweighted by exactly the factor a natural prime count does not see.  The
available tail theorem licenses the power cutoff (4.2), not a fixed or
polylogarithmic cutoff retaining `1-o(1)` of the hat mass.

### 4.2 Small modulus

The Yang--Yang audit gives a complete warning on the natural side.  In their
actual fourth-moment ledger the modulus weight is

\[
 \frac{\Lambda(b_1)\Lambda(b_2)}{b_1b_2}.
\]

Consequently moduli at most `(log X)^B` retain only

\[
 \left(\frac{B\log\log X}{\log X}\right)^2+o(1)\to0. \tag{4.4}
\]

That truncation is not mass-preserving even before the gap mask is
introduced.  A full-power-modulus natural theorem would avoid (4.4), but it
would still estimate only `r=1` in (1.5).

### 4.3 Product conductor, determinant gap, or delta-method modulus

The relevant product resolution is `H=Y^2/T`.  The dyadic pieces in `h` or
in a delta-method modulus are oscillatory, not positive probability cells.
Their signed total can be small while their `l1` and Hilbert mass are large.
Taking absolute values cell by cell restores the `Y^2/T` conductor loss and
therefore loses at least (3.5).  A claimed retained percentage in such a
partition is meaningless unless an `l1` or positive-semidefinite norm ledger
is also supplied.

The exact model in the next section strengthens this observation: **any**
partition that retains `1-o(1)` of both positive semiprime measures retains
the vector discrepancy, even though its retained signed discrepancy tends
to zero.

---

## 5. Exact adversarial gap-mask model

Take `N=4M` cyclic log nodes and a flat local profile.  Repeat the gap motif

\[
 (4,1,2,1)\delta,
 \qquad t_0=\frac\pi\delta.                         \tag{5.1}
\]

The node phases at `t_0` are

\[
 (+1,+1,-1,-1).                                    \tag{5.2}
\]

The exact hat/Voronoi masses are half the sums of the adjacent gaps, hence
are proportional to

\[
 \left(\frac52,\frac52,\frac32,\frac32\right).
\]

After normalization, let

\[
 \eta_j=\frac1N,qquad
 \lambda_j=\frac1N
 \left(\frac54,\frac54,\frac34,\frac34\right)      \tag{5.3}
\]

on every block.  Direct calculation gives

\[
 \|\lambda-\eta\|_1=\frac14,qquad
 \sum_j|\lambda_j-\eta_j|^2=\frac1{16N},          \tag{5.4}
\]

and

\[
 S_\lambda=\frac{17}{16N},\qquad
 S_\eta=C=\frac1N.                                \tag{5.5}
\]

At semiprime level the mass by high/low factor type is

| factor type | natural mass `b` | hat mass `a` | signed difference |
|---|---:|---:|---:|
| high--high | `16/64` | `25/64` | `+9/64` |
| mixed | `32/64` | `30/64` | `-2/64` |
| low--low | `16/64` | `9/64` | `-7/64` |

Therefore

\[
 \sum(a-b)_+=\sum(a-b)_-=\frac9{64},
 \qquad \|a-b\|_1=\frac9{32},                     \tag{5.6}
\]

and substitution in (2.2) gives the exact identity

\[
 \|a-b\|_2^2
 =\frac{33}{128N^2}-\frac{65}{256N^3}.             \tag{5.7}
\]

Now let `R_N` be any union of conductor, modulus, gap, or other cells which
retains both probability masses:

\[
 a(R_N^c)+b(R_N^c)=\varepsilon_N=o(1).             \tag{5.8}
\]

Then

\[
 \left|\sum_{n\in R_N}(a_n-b_n)\right|\leq\varepsilon_N, \tag{5.9}
\]

but

\[
 \sum_{n\in R_N}|a_n-b_n|
 \geq\frac9{32}-\varepsilon_N.                    \tag{5.10}
\]

Since `max_n|a_n-b_n|<=9/(8N^2)`, it also retains

\[
 \sum_{n\in R_N}|a_n-b_n|^2
 \geq \frac{33}{128N^2}-\frac{65}{256N^3}
       -\frac{9\varepsilon_N}{8N^2}.               \tag{5.11}
\]

Thus signed retained mass approaches zero while fixed total variation and
the full leading squared norm survive.  To eliminate them, a partition must
discard a fixed amount of natural or hat mass, or resolve the selector and
prove cancellation inside its cells.

Finally, (5.2)--(5.3) give

\[
 M_\eta(t_0)=0,qquad M_\lambda(t_0)=\frac14,       \tag{5.12}
\]

so the natural semiprime transform is zero while the hat semiprime transform
is `1/16` and the `CA4` integrand is `1/256`.  Since all nodes lie in a fixed
log shell, the peak persists on an interval of fixed width.

The motif embeds asymptotically into the exact tilted tent.  Take
`delta asymp log(Y)/Y`; then `t_0 asymp Y/log Y` lies in the residual `CA4`
band, every physical gap is `O(log Y)<<Y^(163/1000)`, and a blockwise
`C^1` expansion gives

\[
 M_\eta(t_0)=o(1),\qquad M_\lambda(t_0)=\frac14+o(1). \tag{5.13}
\]

Rounding the physical pseudo-nodes to distinct integers perturbs the phases
by `o(1)` and preserves the conclusion.  Random bounded odd cross-block gaps
can destroy extraneous pair-sum coincidences while the signed hat
contribution telescopes to a nonzero constant.  None of these nodes is
asserted to be prime.  The model proves a nonimplication from the listed
soft fields and rules out pointwise or cellwise domination of the masked form
by the natural form; it does not refute a theorem that uses a genuinely
prime-specific selector correlation.

---

## 6. What survives as a research target

Two faithful formulations identified by this audit are:

1. Prove uniformly in the residual band

   \[
    \int_T^{2T}|M_{\lambda-\eta}(t)|^4dt
    \ll T Y^{-2q+1/10+o(1)}.                       \tag{6.1}
   \]

   Together with a natural theorem, Minkowski transfers (6.1) to `CA4`.

2. Prove a vector-valued/twisted `HL*(4)` estimate for

   \[
    \sum_m b_m b_{m+h}R_mR_{m+h},
    \qquad R_{p_ip_j}=r_ir_j,                       \tag{6.2}
   \]

   uniformly through the exact translated kernel and all
   `|h|<=Y^2/T`, summing the signed cells before taking absolute values.

Both targets explicitly retain the adjacent-consecutive-prime selector.
They could be easier than arbitrary-coefficient four-cycle bounds because
`r` is a fixed geometric mask, but neither follows from scalar natural
`Lambda*Lambda` correlation control.

The exact successor-gap identity explains the extra mathematics:

\[
 \mathbf 1_{p^+-p=g}
 =\mathbf 1_{\mathbb P}(p+g)
   \prod_{1\leq h<g}(1-\mathbf 1_{\mathbb P}(p+h)). \tag{6.3}
\]

The mask records both a prime endpoint and the absence of every intervening
prime.  Natural `Lambda*Lambda` sees the endpoints/products but not this
emptiness selector.  Expanding (6.3) through gaps as large as
`Y^(163/1000)` has unbounded order; truncating it is not a signed-power
approximation without additional sieve correlation input.

## Final status ledger

| Claim | Status |
|---|---|
| Long-gap deletion at `Y^(163/1000)` is mass-preserving | **PROVED** |
| Polylog-modulus Yang--Yang truncation is mass-preserving | **FALSE** |
| Current `l1/l2` information transfers natural `HL*(4)` to `CA4` | **FALSE** |
| Any `1-o(1)`-mass partition removes the mask discrepancy in the adversarial model | **FALSE** |
| Scalar natural correlation uniformly dominates the gap-twisted contact | **FALSE in the proof class** |
| Selector-sensitive band-norm/vector-valued adapter | **VALID CONDITIONAL INTERFACE; OPEN INPUT** |
| Actual-prime `CA4` | **OPEN** |
| Uniform zero-free strip | **OPEN; `LTRAD` is independently open** |
| RH | **OPEN** |

**Theorem-level disposition:** stop the coefficient-blind natural-mask
transference branch.  Import a future natural `HL*(4)` theorem only as the
`b` summand in (3.6); the parallel first-open edge is a selector-sensitive
estimate for `lambda-eta` (or equivalently (6.2)).
