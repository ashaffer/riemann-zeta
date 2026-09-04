# Global conductor-L4 information-gain sprint

Date: 2026-08-31

Primary preflight:
[`zeta23_global_conductor_l4_preflight_v1.json`](context/zeta23_global_conductor_l4_preflight_v1.json)

Exact ledger and replay:
[`global_conductor_l4_gate.py`](../src/global_conductor_l4_gate.py),
[`ZETA23-GLOBAL-CONDUCTOR-L4-FROZEN-REPLAY-2026-08-31.json`](ZETA23-GLOBAL-CONDUCTOR-L4-FROZEN-REPLAY-2026-08-31.json)

Secondary preflights:
[`zeta23_adjacent_gap_bin_l4_preflight_v1.json`](context/zeta23_adjacent_gap_bin_l4_preflight_v1.json),
[`zeta23_adjacent_gap_determinant_dispersion_preflight_v1.json`](context/zeta23_adjacent_gap_determinant_dispersion_preflight_v1.json)

## Verdict

The conductor-gain fourth moment is the best identified analytic route **inside
the fixed retained-hat positive-DPA branch**, but it is not proved.  The exact
global target is

\[
 \int_{Y^{839/1000}}^{2Y^{50/33}}|F_{Y,\theta}(t)|^4\,dt
 \ll Y^{13/8-2q+o(1)},
 \qquad
 \theta={161\over1000},\quad q={2789\over3250}.       \tag{0.1}
\]

Its right side is

\[
 Y^{-1187/13000+o(1)}.                               \tag{0.2}
\]

The deterministic adapter is sound and has strict, but small, slack.  The
sprint proved exact reductions to one global signed four-distinct correlation,
then eliminated all currently obvious shortcuts:

* the top window alone is not sufficient;
* absolute near-product incidence cannot work;
* no audited literature theorem imports;
* direct Guth--Maynard large-value use is substantially too weak;
* the first natural determinant-Poisson completion loses the adjacent-gap
  selector and was stopped by its preregistered rule.

The remaining theorem is genuine new arithmetic: fixed-power cancellation of
an adjacent-gap-weighted balanced-\(E_2\) correlation at the exact
\(M^{8/33}\) resolution, uniformly across the whole translated band.

This does not prove positive DPA, LTRAD, a zero-free strip, or RH.

---

## 1. Exact adapter ledger

Delete both endpoint shares of each adjacent-prime edge with physical gap
greater than \(Y^\theta\), and normalize the retained weights \(\lambda_p\) to
mass one.  Put

\[
 F_{Y,\theta}(t)=\sum_p\lambda_p e^{it\log(p/Y)}.
\]

The exact exponents are:

| Quantity | Exact value | Decimal |
|---|---:|---:|
| cutoff \(\theta\) | \(161/1000\) | .161 |
| deleted-mass saving \(s\) | \(249/13000\) | .019153846 |
| retained \(\ell^2\) saving \(q\) | \(2789/3250\) | .858153846 |
| required conductor gain at \(c=.019\) | \(9599/26000\) | .369192308 |
| selected conductor gain | \(3/8\) | .375 |
| fourth-moment decay | \(1187/13000\) | .091307692 |
| bad-point persistence cost | \(171/2000\) | .0855 |
| strict margin | \(151/26000\) | .005807692 |
| resulting pointwise exponent | \(1187/58500\) | .020290598 |

The full-to-retained Fourier error is
\(O(Y^{-s+\varepsilon})\), which is smaller than a
\(Y^{-.019}\) violation.  If
\(\Re F(t_0)\le-\delta\), then
\(|(\Re F)''|\le w^2\).  Choosing the direction opposite the first derivative
gives a negative sublevel interval of length \(\gg\sqrt\delta\).  A violation
therefore forces fourth-moment mass \(\gg\delta^{9/2}\).  Equations (0.1)--(0.2)
contradict this at \(\delta=Y^{-.019}\) by the strict margin above.

The lower endpoint is safe because the proved full-hat range reaches
\(Y^{.8392}\), while (0.1) begins at \(Y^{.839}\).  The upper one-sided
persistence interval is safe because (0.1) extends to \(2B\).

Thus (0.1), if proved, closes the fixed-hat positive-DPA candidate for every
fixed \(c<.019\).  It does not close the independent LTRAD gate.

---

## 2. Strongest exact arithmetic reduction

Write

\[
 M(t)=\sum_p\lambda_p z_p,\quad
 Q(t)=\sum_p\lambda_p^2z_p^2,\quad
 A_3(t)=\sum_p\lambda_p^3z_p,
 \qquad z_p=e^{it\log(p/Y)},
\]

and \(S_j=\sum_p\lambda_p^j\).  Direct incidence subtraction proves the
pointwise identity

\[
 C_4(t)=|M^2-Q|^2-4S_2|M|^2
       +8\Re(M\overline{A_3})+2S_2^2-6S_4,           \tag{2.1}
\]

where \(C_4\) is exactly the contribution from ordered quadruples with all
four prime indices distinct.  Equivalently, for a nonnegative smooth
translated window \(\psi\),

\[
 C_{4,\psi}(B)
 =4B\!\!\sum_{\substack{p<r,\ q<s\\
                  \{p,r\}\cap\{q,s\}=\varnothing}}
 \lambda_p\lambda_r\lambda_q\lambda_s
 K_\psi\!\left(B\log{pr\over qs}\right).           \tag{2.2}
\]

The identity (2.1) is implemented and tested both against direct ordered
enumeration and against the pair-kernel formula.

The one-prime mean-value theorem gives

\[
 \text{diagonal + squares + shared-prime sectors}
 \ll (B+Y)S_2^2.                                    \tag{2.3}
\]

Indeed, the terms in (2.1) outside the disjoint-pair contribution reduce to
\(L^2\) pairings of \(M,Q,A_3\); one uses
\(S_4\le S_2^2\), \(S_6\le S_2^3\), and prime-log spacing
\(\gg1/Y\).  Since

\[
 {13\over8}-{50\over33}={29\over264}>0,             \tag{2.4}
\]

(2.3) fits (0.1) with a fixed power to spare.  Only the upper bound for the
signed global integral of \(C_4\) remains.

### Determinant-offset normal form

Schwartz decay restricts (2.2), at the top scale, to

\[
 |pr-qs|\le HY^\varepsilon,qquad H=Y^{16/33}.       \tag{2.5}
\]

Put \(d=pr-qs\), \(n=qs\), and

\[
 W_Y(n,d)=
 \sum_{\substack{qs=n,\ pr=n+d\\p,r,q,s\ {m distinct}}}
 \lambda_p\lambda_r\lambda_q\lambda_s.
\]

On (2.5),

\[
 B\left(\log(1+d/n)-d/n\right)
 \ll Y^{-50/33+2\varepsilon}.                       \tag{2.6}
\]

The fixed-\((p,q)\) near-collision relation is a partial injective matching
\(r\mapsto s\), so its weighted mass is at most \(S_2\).  Consequently the
phase linearization costs only \(O(Y^{-q+2\varepsilon})\), negligible here,
and the sole residual is

\[
 4B\sum_{\substack{|d|\le HY^\varepsilon\\n\asymp Y^2}}
 W_Y(n,d)K_\psi(Bd/n).                               \tag{2.7}
\]

This is a useful normalization, not a bound.

### Why absolute incidence is dead

The same partial-matching argument, used absolutely, yields only

\[
 |C_4|\ll BS_2=Y^{70463/107250+o(1)},               \tag{2.8}
\]

missing (0.2) by

\[
 Y^{321023/429000}=Y^{.748305\ldots}.                \tag{2.9}
\]

Even an ideally smooth product density has unsigned tube mass \(\asymp1/B\),
so multiplication by \(B\) leaves order one.  Since the translated kernel
has zero total moments when its time cutoff is supported away from zero, the
required decay must come from cancellation of the smooth shifted-semiprime
main across determinant offsets.  No absolute close-pair or positive-Fejer
replacement can provide it.

---

## 3. A proved coefficient-serialization adapter

There is one useful sufficient interface.  Put all weights
\(\lambda_p\le Y^{-3/2}\) into \(F_0\).  There are \(O(Y)\) primes, hence

\[
 \|F_0\|_\infty\ll Y^{-1/2},\qquad
 \int_L^{2B}|F_0|^4\ll Y^{-16/33}.                  \tag{3.1}
\]

Split the other weights into \(J=O(\log Y)\) dyadic bins and put
\(E_j=\sum_{p\in P_j}\lambda_p^2\).  Holder gives

\[
 \left|\sum_{j=0}^J F_j\right|^4
 \le(J+1)^3\sum_{j=0}^J|F_j|^4.                    \tag{3.2}
\]

Therefore the binwise statements

\[
 \int_L^{2B}|F_j(t)|^4dt
 \ll Y^{13/8+o(1)}E_j^2                            \tag{3.3}
\]

imply (0.1), since \(\sum_jE_j^2\le(\sum_jE_j)^2\).

This reduction costs only \(Y^{o(1)}\), but (3.3) is stronger than GCG4:
it forbids helpful cancellation between weight levels.  A failure of (3.3)
would prune this interface, not refute (0.1).  It is also false for arbitrary
prime subsets; the actual adjacent-gap selector must remain in its passport.

---

## 4. Frozen all-window replay

The replay used exactly the four centers and controls frozen in the earlier
HT-HAT preregistration.  It reconstructed the literal retained edge weights,
integrated the complex fourth moment on every dyadic subwindow, and evaluated
(2.1) independently.  Step sizes 2 and 1 agreed in the global moment to less
than \(2\cdot10^{-7}\) relatively.

Every cutoff lies strictly between 2 and 4.  Thus **every retained edge is a
twin-prime edge**.  The retained raw mass is only about .009--.011, or
4.4--5.5 percent of the original truncated hat mass.  These vectors are far
outside the asymptotic \(1-o(1)\) retention regime.

The following moment columns are divided by \(Y^{13/8}S_2^2\):

| \(Y\) | kept edges | retained/full | top total | sum lower total | top \(C_4\) | global \(C_4\) |
|---:|---:|---:|---:|---:|---:|---:|
| 512.5 | 6 | .04421 | .96083 | .82262 | +.04506 | +.01860 |
| 1024.5 | 9 | .05007 | .80949 | 1.00576 | -.07006 | +.05981 |
| 2048.5 | 19 | .05461 | .84169 | .85244 | -.01240 | +.01591 |
| 4096.5 | 38 | .04793 | .77717 | .80109 | -.01182 | +.00302 |

This teaches three bounded facts.

1. There is no finite catastrophic four-distinct excess; easy/diagonal
   sectors dominate these vectors.
2. A top-only theorem is not sufficient.  Lower windows contain comparable
   total mass and can carry a positive residual when top \(C_4\) is negative.
3. One-sided morphology gives only constants: the real fourth moment is
   .366--.382 of the complex fourth moment, and the negative-real part is
   .495--.515 of the real fourth moment.  There is no observed power-sized
   saving that would justify switching to a negative-part target.

None of these is asymptotic evidence.  In particular, the literal
\(Y^{-2q}\) scale is not present yet: the finite \(S_2\) values are much larger
than \(Y^{-q}\).  Adding more nearby scales would mostly measure twin-prime
sampling and has low information value.

---

## 5. Exact literature import audit

No primary-source theorem supplies the missing conductor gain.  Normalize
\(M=Y^2\), so

\[
 B=M^{25/33},\qquad H=M^{8/33},\qquad
 \sum_na_n^2\ll M^{-q}.                             \tag{5.1}
\]

The desired top core improves the generic \(M\sum a_n^2\) to
\(M^{13/16}\sum a_n^2\).

* [Matomaki--Radziwill--Tao (2017), Theorem 1.3 and Proposition
  3.4](https://arxiv.org/abs/1707.01315) reach natural
  \(\Lambda,d_k\) correlations only for
  \(H\ge M^{8/33+\varepsilon}\).  We are at the exact endpoint; covering it
  costs a fixed \(M^\varepsilon\), while their saving is logarithmic.  Their
  Type-II input also requires one factor \(\ll H\), whereas both of ours have
  length \(M^{1/2}\), and it does not accept adjacent-gap coefficients.
* [Matomaki--Teravainen (2022), Lemmas 3.3--3.4](https://arxiv.org/abs/2207.05038)
  apply to the serialized sparse polynomial, but retain an absolute
  close-pair term.  Binwise this is \(Y^2E_j^2\), missing (3.3) by exactly
  \(Y^{3/8}\).
* [Guth--Maynard (2024), Theorem 1.1](https://arxiv.org/abs/2405.20552)
  has a nominal large-value term that would fit, but its
  \(TY^{12/5}V^{-4}\) term does not.  In the favorable dense-bin
  normalization the deficit is
  \(Y^{383/1320}=Y^{.290151\ldots}\).
* Applying Guth--Maynard directly to the full weighted vector is worse.  The
  audited optimum gives
  \[
    \int_L^{2B}|F(t)|^4dt
    \ll Y^{4613/8250+o(1)},                          \tag{5.2}
  \]
  missing (0.2) by
  \[
    Y^{279047/429000}=Y^{.650459\ldots}.             \tag{5.3}
  \]
* [Higher Uniformity II, Theorem 1.8](https://arxiv.org/abs/2411.05770)
  concerns dense modelled divisor coefficients, almost-all starts, and a
  fixed-phase discrepancy.  Even under a fictitious perfect coefficient
  transfer, its stated power is far smaller than the required \(M^{-3/16}\).

The endpoint coincidence \(H=M^{8/33}\) is real and informative, but it is
not an importable theorem.  Re-running coefficient-blind sparse mean-value or
large-value machinery has now been falsified as a high-value next step.

---

## 6. Bounded determinant-dispersion attempt

The preregistered one-shot objective was to Poisson-sum the determinant offset
\(d=pr-qs\) before taking any absolute value, with the zero dual mode matched
to the smooth correlation main.

The derivation reaches a precise first loss.  Fixing \(p,q,d\) imposes

\[
 pr\equiv d\pmod q,\qquad s={pr-d\over q}.           \tag{6.1}
\]

Here \(q\asymp Y\), while the significant \(d\)-interval has length
\(H=Y^{16/33}\ll q\).  Completion in \(d\bmod q\) therefore exposes about

\[
 {q\over H}=Y^{17/33}                               \tag{6.2}
\]

dual modes.  Their coefficient is not a standard prime transform: it retains
\(\lambda_r\lambda_{(pr-d)/q}\), and each \(\lambda\) depends on whether an
incident edge is a consecutive-prime edge of length at most \(Y^\theta\).
Expanding that condition exactly introduces the no-prime-in-between selector;
there is no fixed-complexity \(\Lambda\)-correlation to which the audited
theorems apply.

The zero mode is equally non-free: identifying it with the continuous main
requires a fixed-power local limit theorem for this weighted balanced-\(E_2\)
measure, which is the missing content of (2.7), not an elementary identity.
The first Cauchy step removes the selector, returns arbitrary coefficients or
an unsigned close-pair tube, and falls back to (2.8) or the failed large-value
bounds in Section 5.

The stop condition therefore fired.  This is a **method failure**, not a
counterexample to GCG4.  A determinant approach should be reopened only if a
new selector-sensitive transform norm is identified before Cauchy/completion.

---

## 7. Decision-tree update

| Executed target | Result | Information gained |
|---|---|---|
| Exact global-GCG4 ledger | **PROVED conditional adapter** | \(3/8\) is sufficient; the true threshold is .3691923 |
| Exact sector algebra | **PROVED** | only signed global four-distinct correlation remains |
| Top-window falsifier | **PASSED finitely / insufficient** | no top obstruction, but no top-to-lower implication |
| All-window frozen replay | **INCONCLUSIVE asymptotically** | lower windows are parallel; no one-sided power gain |
| Bin serialization | **PROVED adapter** | isolates a literature-compatible but stronger target |
| Literature import | **FAILED** | exact coefficient, endpoint, and fixed-power mismatches located |
| Determinant Poisson | **METHOD STOPPED** | first completion loses the adaptive selector |

The next sufficient theorem, if this fixed-hat branch is continued, is the
**global signed four-distinct bound** obtained by summing a nonnegative dyadic
partition of all windows in \([Y^{.839},2Y^{50/33}]\):

\[
 \sum_j C_4(T_j)
 \ll Y^{13/8+o(1)}\left(\sum_p\lambda_p^2\right)^2. \tag{7.1}
\]

The top scale is only its sharpest-resolution boundary test.  Work on (7.1)
must stop immediately if it substitutes natural weights, takes absolute
close-pair values, asks for coefficient-uniformity, or loses a fixed power at
the \(M^{8/33}\) endpoint.

Priority is **low--medium**, not high: the target is logically clean and the
finite residual is benign, but all known machinery misses it by a fixed power
and the first new dispersion attempt collapsed to the same selector problem.
The renewal boundary estimate is stronger and currently farther away.  A
weight redesign could reduce the conductor gain, but it would reopen the
already-proved low-band approximation and natural-weight transfer is itself
strip-strength.  Neither presently dominates (7.1) on information per unit
effort.

Finally, this is only one side of an AND gate.  `LTRAD_P(.0189,.001)` remains
independently open, so even a proof of (7.1) would not by itself establish the
contemplated zero-free strip.  RH remains much farther away and would still
require a new amplifier beyond that strip.

## Status

| Statement | Status |
|---|---|
| Frozen-hat floor through \(Y^{.8392}\) | **PROVED (prior result)** |
| GCG4(161/1000,3/8) | **OPEN** |
| Global signed four-distinct core (7.1) | **OPEN** |
| Fixed-hat positive DPA for every \(c<.019\) | **OPEN** |
| LTRAD | **OPEN** |
| Uniform zero-free strip | **OPEN** |
| RH | **OPEN** |
