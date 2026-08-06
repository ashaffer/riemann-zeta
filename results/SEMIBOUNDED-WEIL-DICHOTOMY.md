# Global semiboundedness of the Weil form: exact dichotomy

Status: analytic theorem from standard distribution and screw-function inputs;
the order-theoretic floor consequences are formalized separately in Lean.  This
is not a proof of RH.  It identifies a proposed support-uniform estimate as an
RH-equivalent target and rules out a previously plausible fixed-shift escape.

## 1. Verdict

Let `W` be the Hermitian Weil distribution, with

```text
Q_W(f) = W(f * f_tilde),
f_tilde(x) = conjugate(f(-x)),
```

and let

```text
lambda(a) = inf { Q_W(f) / ||f||_2^2 :
                  0 != f in C_c^infty((-a,a)) }.
```

Then

```text
RH
  <=> there is a finite c >= 0 such that
      Q_W(f) >= -c ||f||_2^2 for every f in C_c^infty(R)
  <=> inf_(a>0) lambda(a) > -infinity
  <=> one fixed real shift sigma satisfies sigma < lambda(a)
      for every a > 0.
```

Consequently there is an exact alternative:

```text
RH true  => lambda(a) >= 0 for every a;
RH false => lambda(a) decreases to -infinity as a tends to infinity.
```

The second line is much stronger than merely saying that some large window is
negative.  It also means that proving any support-independent completed bound

```text
prime_a(f) <= pole_a(f) + arch_a(f) + c ||f||_2^2
```

would already prove RH.  A fixed negative auxiliary shift does not avoid the
global positivity problem: its admissibility on every support is exactly
RH-strength.

## 2. Proof with all normalizations visible

Use Suzuki's Fourier convention

```text
fhat(z) = integral_R f(x) exp(i z x) dx.
```

Let `Psi` be Suzuki's explicit prime-side function and put `g=-Psi`.  Two
unconditional identities from Suzuki's 2023 paper are

```text
W = -g''                                                   (2.1)

integral_0^infinity Psi(t) exp(i z t) dt
  = -z^(-2) (xi'/xi)(1/2-i z),       Im(z) > 1/2.         (2.2)
```

Suppose that `Q_W(f) >= -c ||f||_2^2` globally, increasing `c` to be
nonnegative if necessary.  Since

```text
delta_0(f * f_tilde) = ||f||_2^2,
```

the distribution

```text
S = W + c delta_0
```

is positive definite.  Define

```text
h(t) = g(t) - (c/2) |t|.
```

The normalization `( |t| )''=2 delta_0` gives the exact identity

```text
S = -h''.                                                  (2.3)
```

### The elementary accelerant-to-screw step

For arbitrary points `t_j` and coefficients `a_j`, take a compact smooth
mollifier `rho_eps` and set

```text
u_eps = sum_j a_j [rho_eps(.-t_j)-rho_eps],
v_eps(x) = integral_(-infinity)^x u_eps(y) dy.
```

The zero integral of `u_eps` makes `v_eps` compactly supported and smooth.
Twice integrating by parts in (2.3) gives

```text
0 <= S(v_eps * v_eps_tilde)
   = double_integral h(x-y) u_eps(y) conjugate(u_eps(x)) dx dy.
```

Continuity of `h` permits `eps -> 0`, yielding

```text
sum_(j,k) a_j conjugate(a_k)
  [h(t_k-t_j)-h(t_k)-h(-t_j)+h(0)] >= 0.
```

Thus `h` is a global screw function.  This step uses no growth assumption on
`W`, `g`, or `h`.

The Krein--Langer screw/Nevanlinna correspondence now supplies a Herglotz
function `q_c`, holomorphic on the whole upper half-plane, such that

```text
integral_0^infinity h(t) exp(i z t) dt = -i q_c(z)/z^2.
```

Because `g=-Psi` and

```text
integral_0^infinity t exp(i z t) dt = -1/z^2,
```

comparison with (2.2), initially for `Im(z)>1/2`, fixes every sign and factor:

```text
q_c(z) = i (xi'/xi)(1/2-i z) + i c/2.                    (2.4)
```

The left side is holomorphic throughout the upper half-plane.  A zero `rho`
of `xi` with `Re(rho)>1/2` would give a genuine logarithmic-derivative pole at

```text
z_rho = i (rho-1/2),       Im(z_rho)=Re(rho)-1/2>0.
```

Its residue is its positive multiplicity and cannot be cancelled by the
constant `i c/2`.  Meromorphic continuation of (2.4) therefore excludes every
zero to the right of the line; the functional equation excludes zeros to its
left.  This proves RH.  The converse is Weil positivity with `c=0`.

### Independent Bochner--Schwartz normalization check

Bochner--Schwartz starts with the positive-definite `S` in `D'(R)` and proves
that positivity itself makes `S` tempered.  Thus no unconditional
temperedness of `W` or `g''` may be assumed.  It supplies a positive tempered
measure `mu_c` with

```text
S(phi) = integral_R phihat(x) d mu_c(x).
```

Mollifying interval indicators in (2.3) gives

```text
-2 h(t) = integral_R 2(1-cos(t x))/x^2 d mu_c(x).
```

Integrating this identity for `0<=t<=1` proves the necessary Cauchy weight,

```text
integral_R d mu_c(x)/(1+x^2) < infinity,
```

because

```text
2[1-sin(x)/x]/x^2  asymp  1/(1+x^2).
```

The regularized Cauchy transform

```text
q_c(z) = integral_R [1/(x-z)-x/(1+x^2)] d mu_c(x)
```

is therefore holomorphic and Herglotz on the upper half-plane.  Direct
Fubini calculation reproduces (2.4).  Under RH the measure normalization is

```text
d mu_c = sum_gamma m_gamma delta_gamma + c dx/(2 pi),
```

and the Lebesgue term contributes exactly `i c/2` to `q_c`.  This independently
checks the sign and factor in the screw proof.  Historically, one can shorten
the last step further: the Benedetto--Joyner criterion, recorded as Theorem
5.4 in Floyd Williams's 1992 paper, says that temperedness of the Weil
distribution is equivalent to RH.

Finally, every compactly supported smooth function lies in some window, and
Suzuki's localized closed-form result identifies `lambda(a)` with this smooth
Rayleigh infimum.  Thus global semiboundedness is equivalent to a common lower
bound for all `lambda(a)`.  The floors are antitone, so failure of every common
lower bound is precisely convergence to `-infinity`.  The Lean theorem is
stated for a real-indexed family; its `truncateBelow` lemmas freeze the family
below any chosen positive support `a0`, exactly matching the physical domain
`a>0` without adding an assumption at nonphysical supports.

## 3. The requested two-bump construction: quantitative update

Let `T_R f(x)=f(x-R)` and take `R` large enough that `f` and `T_R f` have
disjoint supports.  Translation invariance gives `Q_W(T_R f)=Q_W(f)`.  After
choosing the phase of a scalar of modulus one,

```text
Q_W(f + alpha T_R f) / ||f + alpha T_R f||_2^2
  = [Q_W(f)-|Q_W(f,T_R f)|] / ||f||_2^2.                 (3.1)
```

For one nonreal zero parameter `gamma`, the cross term contains a factor of
the form `exp(-i gamma R)`.  A subsequent audit closes the cancellation and
support-cost problem.  If a zero has horizontal displacement `delta>0`, then
for every `epsilon>0`

```text
lambda(a) <= -C_epsilon exp((2 delta-epsilon)a)
```

for every sufficiently large `a`.

There are two independent controls.  For a fixed compact bump, the one-sided
Laplace transform of the *complete* translated cross correlation is a
normally convergent meromorphic zero sum.  Its genuine pole at the selected
off-line node forces exponential large values, giving the rate along a
subsequence without choosing a rightmost zero.  For the all-support upgrade,
the rapidly decaying zeta cardinal functions of
Bondarenko--Radchenko--Seip isolate the quartet; their inverse transforms have
faster-than-every-exponential tails, so smooth truncation costs less than the
translation gain.

The full proof, including the zero-free-strip and subexponential-floor
corollaries, is in
[`QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md`](QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md).
The scalar two-bump passage is Lean-checked in
[`TwoBumpFloorAmplification.lean`](../lean/rhbridge/RHBridge/TwoBumpFloorAmplification.lean).

## 4. Direct prime--archimedean estimate: what standard inequalities give

For the repository normalization, put

```text
B(a) = sum_(log n < 2a) 2 Lambda(n)/sqrt(n),
```

where only prime powers contribute.  Cauchy--Schwarz for every translated
autocorrelation gives the already formalized estimate

```text
prime_a(f) <= B(a) ||f||_2^2.                            (4.1)
```

Partial summation and the prime number theorem give

```text
B(a) ~ 4 exp(a).
```

This growth is not just an artifact of a loose upper estimate.  For the
normalized interval indicator

```text
f_a = (2a)^(-1/2) 1_[-a,a],
Corr_u(f_a) = 1-u/(2a),       0 <= u <= 2a.
```

Restricting the prime sum to `log n <= a` gives

```text
prime_a(f_a) >= sum_(n <= exp(a)) Lambda(n)/sqrt(n)
             ~ 2 exp(a/2).
```

The indicator is in the logarithmically weighted Fourier form domain, and it
can also be smoothed without changing this conclusion.  Thus the prime term
alone has no support-uniform `L2` bound.

The other componentwise estimates do not repair this:

* the archimedean multiplier is bounded below by a support-independent
  constant but grows only logarithmically at high frequency;
* the rank-two pole form has the separate lower bound
  `pole_a(f) >= -4 sinh(a) ||f||_2^2`;
* combining these with (4.1) still loses an exponential function of support.

Therefore every proof based on bounding the three completed pieces
independently fails at the correct scale.  The desired estimate must exploit
the exact prime--pole--archimedean cancellation, not merely improve a
Cauchy--Schwarz constant.  By Section 2, obtaining a support-independent
remainder after that cancellation is equivalent to RH itself.

This closes the proposed "prove a uniform lower bound first" branch as a
simplification.  It remains a valid formulation of RH, but it is not an
easier preliminary lemma.

## 5. Literature and proof boundary

The proof uses the following named inputs.

* Weil positivity, in the compact smooth formulation used by Yoshida.
* Suzuki, [*Aspects of the screw function corresponding to the Riemann
  zeta-function*](https://arxiv.org/abs/2206.03682), Theorem 1.1(1), Section
  3.5, and the Krein--Langer correspondence quoted before equation (1.6).
* Suzuki, [*Weil's quadratic form via the screw
  function*](https://arxiv.org/abs/2606.09096), for the localized closed forms
  and identification of their spectral floors with the smooth Rayleigh
  infima.
* Bochner--Schwartz and the Benedetto--Joyner tempered-Weil criterion only as
  an independent shorter check; the latter is recorded as Theorem 5.4 in
  Williams, [*An analogue of Huber's formula for Riemann's zeta
  function*](https://doi.org/10.5169/seals-59488).
* The prime number theorem for the asymptotics in Section 4.

The semibounded/floor equivalence is an elementary synthesis of these inputs,
not presently advertised as a new theorem of independent depth.  The useful
research output is the exact quantifier audit: any fixed-shift or
support-uniform-constant strategy has already reached an RH-equivalent gate.

## 6. Next genuine checkpoint

The lower growth direction is now complete.  Put

```text
Delta = sup_rho |Re rho-1/2|,
c(a) = max(0,-lambda(a)).
```

The new theorem gives

```text
Delta <= liminf log(1+c(a))/(2a).
```

The next noncircular target is the reverse stability estimate

```text
lambda(a) >= -C_epsilon exp((2 Delta+epsilon)a).
```

Together these would identify the exact exponential type of the negative
floor.  This reverse direction is now proved when only finitely many zeros
are off the line: the critical-line divisor is positive and each exceptional
quartet has localized operator norm `O(exp(2 delta a))`, so the floor exponent
equals `Delta` exactly.

The infinite-divisor case remains open.  A proof must retain the logarithmic
high-frequency energy while performing vertical Paley--Wiener shifts; a bare
zero-sampling estimate is not enough.  On the prime side, the ordinary bound
`Psi(x)-x=O_eta(x^(1/2+Delta+eta))` gives the right exponential factor after
exact pole cancellation, but Stieltjes partial summation loses an
`H^(1/2)` norm.  The archimedean term controls only logarithmic Fourier
energy, and fixed-support modulations show that it cannot absorb this loss.
Thus cumulative prime-counting error alone does not close the target; a
genuinely oscillatory or joint prime--archimedean estimate is required.
