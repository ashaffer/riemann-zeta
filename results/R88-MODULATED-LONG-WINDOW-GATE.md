# Modulated long-window detector: exact response, equivalence, and bank gate

Status: exact detector and fixed-twist exponent theorems proved analytically;
unrestricted-bank obstruction proved; Vaughan/Type-II, mean-value,
large-value, sampling, sparse-bank, and finite-verification routes audited
through 2026-08-07.  The modulation removes the height penalty in R80, but
the resulting arithmetic estimate is exactly fixed-strip strength.  This
report does **not** prove a new zero-free strip, RH, or the nonexistence of a
fixed strip.

## 1. Verdict

The proposed change of detector works on the zero side.

Take one logarithmic interval of length `lambda R` and twist it by
`n^(-i tau)`.  A zero

```text
rho=1/2+delta+i gamma
```

has exact response multiplier

```text
-{exp[z R]-exp[(1-lambda)z R]}/z,
z=delta+i(gamma-tau).                                  (1.1)
```

At `tau=gamma`, this is

```text
-exp(delta R){1-exp(-lambda delta R)}/delta.            (1.2)
```

There is no factor `gamma^(-k)`, hence no R80 penalty
`lambda log gamma`.  On the critical line, (1.1) is a sinc-type frequency
window with principal width `1/(lambda R)`.  Thus the detector idea itself
passes.

The arithmetic reality check is decisive:

1. For **any one fixed modulation** `tau_*`, a fixed-power estimate for this
   prime-minus-continuum transform is exponent-equivalent to a fixed
   zero-free strip.  Moving the carrier away from frequency zero does not
   weaken the theorem that has to be proved; it vertically translates
   `-zeta'/zeta` and leaves all real parts of its poles unchanged.
2. Taking a supremum over all modulations is not a possible workaround.
   Kronecker approximation can align the phases of every prime in the finite
   window, while the continuum transform tends to zero.  Unconditionally,

```text
lim_(R->infinity) R^(-1) log sup_(tau in R)|P_lambda(R,tau)|=1/2. (1.3)
```

   This remains true if RH is true.
3. Restricting to a nested bank `|tau|<=T_R`, `T_R->infinity`, avoids the
   Kronecker obstruction if `T_R` grows slowly.  But such a bank eventually
   retains any fixed twist.  A uniform fixed-power bound on it therefore
   proves the strip by item 1.  Current PNT/Vinogradov--Korobov input gives
   only exponent `1/2-o(1)`.
4. Mean values, large sieve, and modern large-value theorems count
   exceptional frequencies.  Their generic length term permits at least one
   peak of every size `exp(delta R)` with `delta<1/2`.  One peak is enough for
   one off-strip zero.
5. The twist `(mn)^(-i tau)=m^(-i tau)n^(-i tau)` is completely separable.
   It can be absorbed into the two coefficient sequences of a Type-II sum
   without changing their norms.  Consequently modulation creates no new
   Type-II oscillation.  Any useful gain must again be coefficient-specific
   cancellation between the full Vaughan tail, head, and continuum center.

The route therefore gives a cleaner detector, not an easier arithmetic
problem.  Its exact live target is displayed in (6.1) below.

## 2. The exact long-window transform

Fix `0<lambda<1`, put `q=1-lambda`, and define, for real `tau`,

```text
S_tau(x)=sum_(n<=x) Lambda(n)n^(-1/2-i tau),

M_tau(x)=integral_1^x u^(-1/2-i tau)du
        ={x^(1/2-i tau)-1}/(1/2-i tau),

A_tau(x)=S_tau(x)-M_tau(x).                             (2.1)
```

The sharp compact logarithmic-window transform is

```text
P_lambda(R,tau)
 =A_tau(exp R)-A_tau(exp(qR))

 =sum_(exp(qR)<n<=exp R) Lambda(n)n^(-1/2-i tau)
  -{exp[(1/2-i tau)R]-exp[(1/2-i tau)qR]}
       /(1/2-i tau).                                    (2.2)
```

Endpoint half-weights may be inserted without affecting any assertion.  The
support has logarithmic length `lambda R`, as requested.

For a smooth version, let `phi` be supported in `[0,1]` and put

```text
P_(phi,lambda)(R,tau)
 =sum_n Lambda(n)n^(-1/2-i tau)
       phi((R-log n)/(lambda R))
  -integral_1^infinity x^(-1/2-i tau)
       phi((R-log x)/(lambda R))dx.                     (2.3)
```

If `z=rho-1/2-i tau`, its zero multiplier is exactly

```text
-exp(zR) lambda R integral_0^1 phi(u)exp(-lambda R z u)du. (2.4)
```

For example, `phi_m(u)=u^m(1-u)^m 1_[0,1](u)` gives, at
`tau=gamma` and fixed `delta>0`,

```text
lambda R integral_0^1 phi_m(u)exp(-lambda R delta u)du
 ~m! (lambda R)^(-m)delta^(-m-1).                       (2.5)
```

Thus any fixed endpoint vanishing order costs only a power of `R`, never a
power of `gamma`.  The sharp window is preferable for the exact telescoping
theorem below.

## 3. Exact response theorem

### Theorem 3.1 (height-free modulated response)

In the symmetric explicit-formula sense, the contribution of a nontrivial
zero `rho`, counted with multiplicity, to (2.2) is (1.1).  Trivial zeros give
the same expression with `rho=-2m`.  In particular, if `delta>0`, then at
the matching modulation

```text
abs(response_rho(R,gamma))
 =exp(delta R){1-exp(-lambda delta R)}/delta
 =exp(delta R+O_(lambda,delta)(1)).                     (3.1)
```

If `delta=0`, then the continuous value at `tau=gamma` is `lambda R`.
For `delta=0` and `omega=gamma-tau`,

```text
abs(response)=2 abs(sin(lambda R omega/2))/abs(omega),   (3.2)
```

up to a unit phase.  Its principal frequency lobe therefore has width
`asymp 1/(lambda R)`.

#### Proof

For the Mellin test

```text
f_(R,tau)(x)=x^(-1/2-i tau)1_(exp(qR),exp R](x),
```

the pole of `-zeta'/zeta` at one gives exactly the integral in (2.2).
At a zero `rho`, the contour shift has residue

```text
-integral_(exp(qR))^(exp R)x^(rho-3/2-i tau)dx
 =-{exp(zR)-exp(qzR)}/z.                                (3.3)
```

Equations (3.1)--(3.2) follow by substitution and continuity at `z=0`.

This proves the hoped-for detector improvement.  It does not by itself
control cancellation among all residues; Theorem 4.1 identifies exactly
what a prime-side upper bound would mean.

## 4. Fixed-twist exponent theorem

Write

```text
Theta=sup_rho (Re(rho)-1/2).                            (4.1)
```

Functional-equation symmetry gives `0<=Theta<=1/2`.  A fixed strip is the
statement `Theta<1/2`, and RH is `Theta=0`.

For fixed `lambda` and fixed real `tau_*`, define

```text
E_lambda(tau_*)
 =inf{d>=0:
      for every epsilon>0,
      P_lambda(R,tau_*)
       <<_(lambda,tau_*,epsilon) exp[(d+epsilon)R]}.     (4.2)
```

### Theorem 4.1 (one modulation already contains the whole strip)

For every `0<lambda<1` and every fixed real `tau_*`,

```text
E_lambda(tau_*)=Theta.                                  (4.3)
```

In particular, if for one fixed `tau_*` and some `d<1/2`

```text
P_lambda(R,tau_*)<<_epsilon exp[(d+epsilon)R]            (4.4)
```

for every `epsilon>0`, then

```text
zeta(rho)=0  ==>  Re(rho)<=1/2+d.                       (4.5)
```

The modulation need not equal a zero ordinate.  A fixed twist simply shifts
every zero pole vertically and preserves its real part.

#### Proof: telescoping

Equation (2.2) gives exactly

```text
A_(tau_*)(exp R)
 =sum_(j=0)^(J-1)P_lambda(q^j R,tau_*)
  +A_(tau_*)(exp(q^J R)),                               (4.6)
```

where `J` is chosen so that `q^J R` lies in one fixed compact interval.
If (4.4) holds, the first term of this geometrically contracted sum is
dominant; the remaining `O(log R)` terms are
`O(log R exp[(d+epsilon)qR])`.  Hence

```text
A_(tau_*)(x)<<_epsilon x^(d+epsilon).                   (4.7)
```

#### Proof: analytic continuation

Put `a=1/2-i tau_*`.  Initially for `Re(w)>1/2`, partial summation gives

```text
-zeta'(w+1/2+i tau_*)/zeta(w+1/2+i tau_*)-1/(w-a)

 =w integral_1^infinity A_(tau_*)(x)x^(-w-1)dx.         (4.8)
```

By (4.7), the right side is analytic for `Re(w)>d+epsilon`.
The subtracted pole corresponds to the pole of zeta at one.  A nontrivial
zero `rho` would give an uncancelled pole at

```text
w=rho-1/2-i tau_*,                                     (4.9)
```

whose real part is `Re(rho)-1/2`.  Letting `epsilon` decrease proves (4.5)
and hence `E_lambda(tau_*)>=Theta`.

Conversely, for every `epsilon>0`, the line
`Re(s)=1/2+Theta+epsilon` is a fixed positive distance from every zero.
The standard local zero-counting bound gives polynomial-logarithmic control
of `zeta'/zeta` on suitable horizontal truncation heights.  Truncated Perron
summation, shifted to that line, gives

```text
A_(tau_*)(x)<<_(tau_*,epsilon)x^(Theta+epsilon).         (4.10)
```

Taking the difference at `x=exp R` and `x=exp(qR)` proves the reverse
inequality and (4.3).

### Corollary 4.2 (the real-tilted formulation)

For a proposed edge `d`, define

```text
Q_(lambda,d)(R,tau)=exp(-dR)P_lambda(R,tau).             (4.11)
```

A zero with displacement `delta>d`, at matching modulation, contributes

```text
exp[(delta-d)R+O(1)].                                   (4.12)
```

For any one fixed twist, proving

```text
Q_(lambda,d)(R,tau_*)<<_epsilon exp(epsilon R)           (4.13)
```

is therefore not a preliminary estimate toward the strip: by Theorem 4.1 it
is the strip.

## 5. Why an unrestricted frequency bank is false

### Theorem 5.1 (prime-phase alignment obstruction)

For every fixed `0<lambda<1`,

```text
lim_(R->infinity) (1/R)
 log sup_(tau in R)|P_lambda(R,tau)|=1/2.               (5.1)
```

This is unconditional and is compatible with RH.

#### Proof

For fixed `R`, only finitely many prime bases occur among the prime powers in
the window.  The numbers `log p` for distinct primes are rationally
independent: an integral relation would exponentiate to a nontrivial unique-
factorization relation.  Kronecker's theorem therefore supplies arbitrarily
large `tau` for which all `p^(-i tau)` in this finite set are simultaneously
as close to one as desired.  Their powers are then close to one as well.

Along such a sequence,

```text
abs(integral_(exp(qR))^(exp R)x^(-1/2-i tau)dx)
 <<exp(R/2)/(1+abs(tau)) ->0.                            (5.2)
```

Consequently,

```text
sup_tau |P_lambda(R,tau)|
 >=(1-o(1))sum_(exp(qR)<n<=exp R)Lambda(n)n^(-1/2)
 =exp(R/2+o(R)).                                        (5.3)
```

The final equality is the ordinary PNT plus partial summation.  The reverse
exponential bound follows by absolute values.  This proves (5.1).

The same obstruction applies to any nonnegative compact taper.  Thus a
theorem with `sup_(tau in R)` and exponent below `1/2` is not merely unknown;
it is false.

## 6. The exact surviving arithmetic target

The only viable version restricts the bank before the Kronecker recurrence
scale.  Let `T_R->infinity`, possibly extremely slowly.  A sufficient theorem
for a fixed strip is

```text
there exist lambda in (0,1), d<1/2 such that

sup_(abs(tau)<=T_R)|P_lambda(R,tau)|
 <<_epsilon exp[(d+epsilon)R]                           (6.1)
```

for all large `R` and every `epsilon>0`.

Indeed, the bank eventually contains any chosen fixed `tau_*`, and Theorem
4.1 applies.  Including `tau=0` makes the equivalence especially visible,
but deleting zero does not help if the bank retains any fixed anchor:
`tau_*=1`, `14`, or any other constant gives the same analytic continuation.

The current unconditional consequence of the Vinogradov--Korobov region is
only

```text
P_lambda(R,tau_*)
 <<_(lambda,tau_*)
 exp{R/2-c R^(3/5)(log R)^(-1/5)}                       (6.2)
```

for fixed `tau_*`, with harmless changes in the displayed log power across
standard formulations.  Its horizontal exponent is `1/2-o(1)`.  Modulation
has removed the *detector's* height penalty but has not improved (6.2).

## 7. Vaughan and Type-II audit

Apply Vaughan's identity to the prime sum in (2.2), retaining the complete
Type-I head and the continuum center as required by R71.  A balanced
Type-II block has the schematic form

```text
B(tau)=sum_(m~M,n~N) a_m b_n (mn)^(-i tau)W(mn/X).      (7.1)
```

But

```text
(mn)^(-i tau)=m^(-i tau)n^(-i tau).                    (7.2)
```

Setting

```text
a'_m=a_m m^(-i tau),       b'_n=b_n n^(-i tau)          (7.3)
```

preserves every `L^p` coefficient norm.  Therefore any Type-II theorem
uniform over arbitrary coefficient phases gives **exactly the same bound**
at `tau` as at zero.  Unlike an additive or reciprocal phase, (7.2) has no
mixed oscillation for dispersion to exploit.

High `tau` can help a Type-I inner sum whose second coefficient is the
constant sequence.  It cannot dispose of the balanced Type-II sector.  To
improve (6.2), one must use that one coefficient is specifically Mobius and
then recombine it with the prime head and pole integral.  A fixed-power bound
for that completed recombination is precisely (4.4), hence fixed-strip
strength.

This also explains why the recent R81--R87 reciprocal-phase work does not
automatically transfer.  Wright's gain is for a genuine inverse phase on an
off-axis additive lattice.  The modulation in (7.2) is a separable
multiplicative character, and its resonant Type-II block remains a
rational--Archimedean major arc.

## 8. Mean values, large values, and the one-peak barrier

Let

```text
D_R(tau)=sum_(exp(qR)<n<=exp R)
              Lambda(n)n^(-1/2-i tau).                 (8.1)
```

The Montgomery--Vaughan mean-value theorem gives

```text
integral_(-T)^T |D_R(tau)|^2d tau
 <<(T+exp R) sum_window Lambda(n)^2/n
 <<(T+exp R)R^2.                                       (8.2)
```

The adjacent-log-frequency term `exp R` is the obstruction.  A sampled
large-sieve version for one-separated ordinates has the same length term,
up to powers of `R`.  In particular it permits one value as large as

```text
exp(R/2)R^O(1),                                        (8.3)
```

and hence permits every off-line carrier `exp(delta R)` with
`delta<1/2`.

If one formally assigns a value `exp(delta R)` to each one-separated
candidate ordinate below height `T`, (8.2) gives only the schematic density
bound

```text
N_delta(T)
 <<(T+X)X^(-2delta)R^O(1),       X=exp R.               (8.4)
```

Optimizing at `X` near `T` leaves `T^(1-2delta+o(1))`, a positive power for
every `delta<1/2`.  Higher large-value technology improves density exponents,
not the logical conversion from “few” to “none.”

Guth--Maynard's large-value theorem has exactly this character: its first
term still permits many peaks below the critical endpoint, while its major
consequences are improved zero-density and short-interval theorems.  The
reverse results of Matomaki--Teravainen show that zero-density and
Dirichlet-polynomial large values are tightly coupled rather than independent
sources of an exclusion principle.  Bellotti's 2025 estimate can reduce the
number of zeros to `O(1)` near the Vinogradov--Korobov boundary; `O(1)` is not
zero, and that boundary still approaches the one-line.

Primary sources:

- [Montgomery--Vaughan, *Hilbert's inequality*](https://doi.org/10.1112/jlms/s2-8.1.73);
- [Guth--Maynard, *New large value estimates for Dirichlet polynomials*](https://arxiv.org/abs/2405.20552);
- [Matomaki--Teravainen, *A note on zero density results implying large value estimates for Dirichlet polynomials*](https://arxiv.org/abs/2403.13157);
- [Bellotti, *A new zero-density estimate for zeta and the error term in the Prime Number Theorem*](https://arxiv.org/abs/2508.02041).

## 9. Sparse and adaptive frequency banks

### 9.1 A `1/R` net is not automatically enough

At the zero level, a log window suggests a mesh of order `1/R`.  On the
prime side, however,

```text
abs(partial_tau P_lambda(R,tau))
 <<R exp(R/2+o(R))                                      (9.1)
```

by absolute values.  Transferring a sampled upper bound of size `exp(dR)`
with `d<1/2` to all frequencies using (9.1) would require mesh

```text
Delta tau
 <<R^(-1)exp[-(1/2-d)R],                                (9.2)
```

not `1/R`.  Bernstein's inequality does not repair this: it uses the global
supremum, which Theorem 5.1 places at the critical scale.

Thus a sparse predetermined net needs a new subcritical derivative or
sampling theorem in addition to a value bound.  Such a theorem would itself
have to use the completed arithmetic cancellation.

### 9.2 Average-good frequencies do not locate zeros

Mean values can choose many good sample points, but an unknown off-strip zero
may sit in the exceptional set.  Randomly shifting the net changes the
probability of encountering that point; it does not give a deterministic
exclusion.  A bank chosen after observing large transform values is also
circular unless one proves that every such value is non-spectral.

Sampling at rigorously known zero ordinates would avoid mesh transfer, but an
infinite list containing every possible off-line zero is the object being
controlled.  At finite height this is a computation; at unbounded height it
returns to a zero-density large-value argument and cannot exclude the final
exception.

### 9.3 Nested versus moving banks

There is a useful dichotomy.

- A **nested** bank eventually contains each fixed ordinate for arbitrarily
  large `R`.  It can amplify one zero exponentially, but a fixed-power bound
  on any retained fixed twist is Theorem 4.1, hence strip-equivalent.
- A **moving** bank, for example `tau~T` with `R~c log T`, can exploit
  `t`-aspect oscillation.  It sees a particular zero only at a scale tied to
  its height, so one cannot send `R` to infinity with that carrier fixed.
  Optimizing the available exponential-sum estimates in this regime is the
  classical zero-free-region calculation; current input returns a
  height-dependent Vinogradov--Korobov gap, not a fixed strip.

This is the modulation analogue of R80's temperature tradeoff.  The explicit
`lambda log gamma` loss disappears, but it is replaced by a choice between a
strip-equivalent fixed-twist theorem and a height-coupled classical estimate.

## 10. Finite verified height

Let `H_ver` be any rigorously verified RH height.  It removes candidate
off-line zeros below `H_ver`, but does not alter the preceding asymptotic
gates.

- A nested bank beginning at `H_ver` still contains fixed twists.  A power
  theorem at one of them analytically continues the same global
  `-zeta'/zeta` and proves the strip; verified zeros were not the missing
  input.
- A moving bank above `H_ver` still supplies only a height-dependent estimate.
- Combining finite verification with an `O(1)` zero-density theorem cannot
  close the argument: one possible zero at arbitrarily large height remains
  fatal.

Finite verification is valuable for explicit constants after a strip theorem
exists.  It does not turn density into exclusion.

## 11. Fail-fast conclusion and next admissible theorem

The modulation mechanism is **proved on the detector side** and **closed as
a shortcut**.

What it achieved:

- an exact compact detector whose matching response is independent of zero
  height at exponential scale;
- removal of R80's `lambda log gamma` spectral penalty;
- an exact identity showing that the fixed-twist growth exponent is the
  horizontal zero edge `Theta`.

What kills the hoped-for easy completion:

- an all-frequency supremum has exponent exactly `1/2` by prime-phase
  alignment;
- a restricted nested-bank fixed power is already the desired strip;
- generic Type-II estimates cannot see the separable twist;
- mean values and large values allow the one exceptional peak that matters;
- sparse sampling below the critical scale needs exponentially fine mesh or
  a new completed derivative estimate.

The minimal genuinely new theorem is therefore not “bound a modulated prime
sum on average.”  It is one of the following equivalent-strength statements:

```text
FIXED TWIST:
  for some tau_* and d<1/2,
  P_lambda(R,tau_*)<<_epsilon exp[(d+epsilon)R]
  for every large R;                                   (11.1)

or

PREDETERMINED BANK:
  a completed tail+head-continuum estimate below
  exp(R/2) at every frequency in a nested covering bank,
  together with subcritical sampling control.          (11.2)
```

Statement (11.1) is exactly a fixed zero-free strip by Theorem 4.1.
Statement (11.2) is stronger.  No surveyed result proves either one.

Accordingly, this route neither proves that a fixed strip exists nor that it
does not exist.  It gives a rigorous reality check: modulation solves the
wrong half of the problem.  Any further work on it must introduce a new
coefficient-specific theorem for the completed von Mangoldt field, not a new
window, frequency net, mean value, or generic Type-II inequality.
