# QP remote AP dilation-shadow gate

**Date:** 2026-08-13

**Verdict:** **QP-PROMOTE remains open, but a genuinely remote and
unconstrained-coefficient class is now sharply localized.**  Let

```text
kappa_promote=.0180303234,
B=Y^(50/33),
M=# distinct actual absolute prime-power log nodes=Y^(1-o(1)).
```

For either the full harmonic support

```text
{tau,2*tau,...,M*tau},
Y^.01<=tau<=B/M,
```

or the genuinely all-remote translate

```text
{c*M+tau,c*M+2*tau,...,c*M+M*tau},
Y^.01<=tau<=(B-c*M)/M,       c>0 fixed,              (0.0)
```

any signed representation of the principal carrier with TV at most `C`
forces `tau` into an explicit dilation shadow of the near-maximal actual
prime-twist set.  The Guth--Maynard large-values estimate and the actual
integer support imply

```text
measure of the shadow <=C^2*Y^o(1).                    (0.1)
```

At the promotion cost `C<=Y^(kappa_promote-eta)`, with fixed
`0<eta<kappa_promote`, while the legal step
interval has length `Y^(17/33+o(1))`, the relative measure is at most

```text
Y^[2*kappa_promote-17/33-2*eta+o(1)]
 =Y^[-.4790908683515...-2*eta+o(1)].                  (0.2)
```

The statement allows arbitrary real coefficients, arbitrary deletion of
harmonics, and every fixed translate of the AP.  In (0.0) **every** atom is
in `[cM,B]`; no shallow atom or confluent cluster is used.

The exceptional shadow is nonempty and can contain a deterministically
chosen optimizer.  Therefore (0.1) is a broad-class obstruction, **not** a
full-aperture lower bound for the atomic cost.  It neither promotes nor
kills QP and proves no zero-free strip.

## 1. Exact polarity and actual rows

Let

```text
N_Y={p^a:Y*exp(-w)<=p^a<=Y*exp(w)},
V_Y={|log(n/Y)|:n in N_Y},
M=#V_Y,
a(t)=(cos(t*v))_(v in V_Y),
q_0=(1,...,1),
S_Y(t)=<q_0,a(t)>=sum_(v in V_Y)cos(t*v).             (1.1)
```

Passing to distinct absolute nodes is exact because cosine rows with the
same absolute node are identical.  At most `Y^o(1)` rows are lost: a
collision for two distinct integers implies `nm=Y^2`.  Selecting one
integer representative for every absolute node leaves a Dirichlet
polynomial with coefficients bounded by one, so the actual-integer
large-values theorem remains applicable.

For a finite high support, define

```text
C_*(q_0)=inf {sum_j |c_j|: sum_j c_j*a(t_j)=q_0}.     (1.2)
```

The promotion direction is an **upper** bound

```text
C_*(q_0)<=Y^(kappa_promote-eta+o(1)).                 (1.3)
```

The stronger positive target

```text
-r*q_0 in conv{a(t):t high},
r>=Y^(-kappa_promote+eta+o(1))                        (1.4)
```

implies (1.3): if `sum w_j a(t_j)=-r q_0`, then
`c_j=-w_j/r` represents `q_0` and has TV `1/r`.  Every lower bound below
is therefore an obstruction to that AP construction.  It is never evidence
for promotion.

## 2. The dilation-shadow theorem

Fix positive integers `K subset {1,...,D}` and a legal step interval `J`
such that `k*tau` belongs to `[Y^.01,B]` for every `tau in J` and `k in K`.

### Theorem 2.1 (remote AP steps with cheap directional TV are rare)

Suppose

```text
q_0=sum_(k in K)c_k*a(k*tau),
sum_(k in K)|c_k|<=C,
C<=Y^(kappa_promote+o(1)).                             (2.1)
```

Define the physical exceptional set

```text
E_C={t in [Y^.01,B]:|S_Y(t)|>=M/C}                    (2.2)
```

and its AP dilation shadow

```text
D_C(K)=union_(k in K){tau:k*tau in E_C}.              (2.3)
```

Then `tau in D_C(K)`.  Moreover

```text
|D_C(K) intersect J|
 <=C^2*Y^o(1)*sum_(k in K)1/k
 <=C^2*Y^o(1)*(1+log D).                              (2.4)
```

The same estimate holds for `a(s+k*tau)` for every fixed shift `s`, on
any interval where those frequencies remain legal.

#### Proof

Take the scalar product of (2.1) with `q_0`.  It gives

```text
M=sum_(k in K)c_k*S_Y(k*tau).                          (2.5)
```

Thus some used harmonic obeys `|S_Y(k*tau)|>=M/C`, which proves membership
in (2.3).  This step uses only total variation and permits completely
unconstrained signs and magnitudes.

The actual-prime exceptional-packet theorem covers the slightly larger set

```text
{|S_Y(t)|>=M/(2C)}                                    (2.6)
```

by at most

```text
R<=C^2*Y^o(1)                                         (2.7)
```

intervals of radius one.  For completeness, this is the direct
Guth--Maynard ledger.  Applied to a dyadic piece of
`sum_(n in N_Y)n^(it)` with `N asyp Y`, `T<=B`, and
`V>>M/C`, their Theorem 1.1 gives

```text
R<=Y^o(1)[C^2+Y^(-2/5)C^4
                 +Y^(50/33-8/5)C^4].                 (2.8)
```

At `C<=Y^(kappa_promote+o(1))`, the last two exponents are respectively

```text
-.3278787064... and -.0127271912...,                  (2.9)
```

so (2.7) follows.  Proper prime powers and the absolute-node quotient have
bounded coefficients and do not change the exponent.

An interval of radius one in the `t` variable pulls back under
`tau -> k*tau` to an interval of length `2/k`.  Union bounding all packets
and all used harmonics proves (2.4).  Replacing `k*tau` by `s+k*tau` has
the same Jacobian.  QED

### Corollary 2.2 (first-`M` and all-remote translated AP families)

Take `K={1,...,M}` and

```text
J_Y=[Y^.01,B/M].                                       (2.10)
```

The interval has length

```text
|J_Y|=Y^(17/33+o(1)),                                 (2.11)
```

while `sum_(k<=M)1/k=Y^o(1)`.  Hence, for
`C=Y^(kappa_promote-eta+o(1))`, the relative set of steps that can possibly
support (2.1) is bounded by (0.2).  Every step outside this set has

```text
C_*(q_0;{tau,...,M*tau})>Y^(kappa_promote-eta+o(1)).  (2.12)
```

For a fixed `c>0`, take instead

```text
s_Y=c*M,
J_Y^remote=[Y^.01,(B-s_Y)/M],
t_k=s_Y+k*tau.                                        (2.13)
```

This step interval also has length `Y^(17/33+o(1))`, and the translated
version of Theorem 2.1 gives the identical relative exponent (0.2).  Now

```text
c*M<=t_k<=B                                           (2.14)
```

for every atom.  This is the advertised all-remote obstruction.  The
untranslated family is also beyond the nodal-product scale at its top atom,
because `M*Y^.01=Y^(1.01-o(1))`.

The theorem is stronger than a generic-grid calculation in one important
way: the coefficients in (2.1) are not assumed smooth, random, bounded
individually, alternating, or produced by a regular profile.  All their
freedom is retained in the TV identity (2.5).

## 3. Exact directional Cramer formula for every consecutive AP

The exceptional steps can be tested without an unaugmented determinant.
Fix `tau` and put

```text
x_j=cos(tau*v_j),
R_tau(x)=product_(j<=M)(x-x_j)
        =sum_(k=0)^M r_k*T_k(x),                      (3.1)
```

where `T_k` is the Chebyshev polynomial.

### Proposition 3.1 (all real AP Cramer factors at once)

Assume the `x_j` are distinct.  The square first-`M` AP system

```text
sum_(k=1)^M c_k*cos(k*tau*v_j)=1,       j<=M          (3.2)
```

is solvable exactly when `r_0!=0`; then it is nonsingular and

```text
c_k=-r_k/r_0,
C_AP(tau)=sum_(k=1)^M |r_k|/|r_0|.                    (3.3)
```

#### Proof

At every root `x_j`, (3.1) says

```text
sum_(k=1)^M (-r_k/r_0)T_k(x_j)=1.                     (3.4)
```

Distinct `x_j` make the full Chebyshev evaluation matrix
`[T_k(x_j)]_(0<=k<M)` a Vandermonde times a nonzero triangular factor.
If `r_0=0`, (3.1) supplies a nonzero null vector for the no-constant matrix;
and a polynomial with zero constant Chebyshev coefficient cannot differ
from `1` by a multiple of `R_tau`.  Thus (3.2) is then not solvable.
Equation (3.3) is the exact TV.  QED

This is the real directional counterpart of the high-degree Schur factor
in the shifted complex AP calculation.  A small ordinary Vandermonde
denominator cannot be read as a saving: it has already canceled in the
coefficient ratios `r_k/r_0`.

There is also an exact positivity test.  If `c` is the unique vector in
(3.3), then this same support realizes

```text
-r*q_0 in conv{a(k*tau):1<=k<=M}                     (3.5)
```

if and only if every `c_k<=0` and `sum c_k<0`.  In that case

```text
r=-1/sum_k c_k,       w_k=-r*c_k.                     (3.6)
```

Thus the signed and positive polarities are never conflated by the tool.

## 4. Actual-node diagnostics

The verifier scans all legal first-`M` AP steps on three finite actual-node
systems, locally refines the best sampled signed cost, and separately checks
the positive sign condition (3.6).  Every reported row satisfies the exact
interpolation equations to the displayed floating tolerance.

| `Y` | `M` | best sampled signed TV | signed log-`Y` exponent | best sampled positive TV | positive depth `r` |
|---:|---:|---:|---:|---:|---:|
| 100 | 9 | 3.8469440 | .292558 | 5.973837 | .167397 |
| 300 | 23 | 7.5638660 | .354744 | 13.17756 | .075887 |
| 1000 | 61 | 12.8985632 | .370180 | 32.61680 | .030659 |

At these scales the promotion budget `Y^kappa_promote` is only
`1.087,1.108,1.133`, respectively.  No scanned design promotes.  The
positive depths are of order `1/M`, not `Y^-kappa_promote`.

These values are exploratory, not global continuous certificates and not
asymptotic lower bounds.  Their role is fail-fast: the exact Cramer family
does not reveal a hidden cheap AP at the tested scales, while (2.4) explains
why a successful step would have to be exceptionally phase-selected.

## 5. Literature audit

The survey was restricted to theorem scopes that could plausibly control
the directional TV rather than a common Gram determinant.

* [Guth--Maynard, *New large value estimates for Dirichlet polynomials*](https://arxiv.org/abs/2405.20552),
  Theorem 1.1, is exactly the arithmetic input in (2.8).  It bounds the
  number of separated near-maximal values for arbitrary coefficients
  bounded by one.  Pulling its packets back through every AP dilation is
  the new step here.
* [Elfving, *Optimum Allocation in Linear Regression Theory*](https://doi.org/10.1214/aoms/1177729442)
  identifies the principal TV problem as a directional convex-hull or
  `c`-optimal problem and gives sparse exposed-face designs.  It does not
  quantify which scalar orbit parameters can support that face.
* [Dette--Melas, *Optimal Designs for Estimating Individual Coefficients in Fourier Regression Models*](https://doi.org/10.1214/aos/1065705122)
  solves fixed integer-harmonic `c`-optimal problems on full or partial
  circles using Chebyshev approximation.  The present regression order,
  actual prime-log nodes, and AP step all grow, so those explicit designs
  do not furnish an exceptional step in (2.3).
* [Ingham, *Some Trigonometrical Inequalities with Applications to the Theory of Series*](https://doi.org/10.1007/BF01180426)
  and [Duffin--Schaeffer, *A Class of Nonharmonic Fourier Series*](https://doi.org/10.1090/S0002-9947-1952-0047179-6)
  provide gap-based `L^2` frame inequalities.  They control ordinary
  conditioning but give only the known square-root directional scale.
* [Fattorini--Russell, *Uniform Bounds on Biorthogonal Functions for Real Exponentials*](https://doi.org/10.1090/qam/510972)
  constructs norm-controlled biorthogonals for separated real exponentials
  in the control-theory moment method.  Its norm is an `L^2` synthesis
  quantity; it neither bounds the replacement ratios in (3.3) nor removes
  the exceptional actual-prime dilation shadow.
* [Landau, *Necessary Density Conditions for Sampling and Interpolation of Certain Entire Functions*](https://doi.org/10.1007/BF02395039)
  supplies density conditions for stable Paley--Wiener sampling and
  interpolation.  Density is compatible with one distinguished carrier
  lying in an exceptional directional span, so it does not decide (1.3).

No paper in this audit proves that the exceptional shadow is empty, and no
no-go theorem surveyed eliminates an actual prime-selected step inside it.

## 6. Exact disposition

```text
exact real AP Cramer/TV formula:                         PROVED;
exact positive-antipode sign/depth test:                 PROVED;
arbitrary-coefficient cheap AP => exceptional dilation: PROVED;
relative exceptional-step exponent -.479090868...:      PROVED;
every AP step outside the explicit zero-density shadow: KILLED;
deterministically selected exceptional AP step:          OPEN;
arbitrary incommensurable remote atoms:                  OPEN;
QP-PROMOTE:                                              OPEN;
uniform zero-free strip:                                 NOT PROVED.
```

The next admissible AP attempt must explicitly construct a step in the
dilation shadow and then pass the exact directional ratios (3.3), including
the positive sign test if (1.4) is claimed.  Random-step sampling, smooth
step profiles, unaugmented Vandermonde conditioning, and another average
frame estimate cannot do this.

## 7. Replay

```bash
python3 src/test_qp_remote_ap_gate.py
python3 results/verify_zeta23_qp_remote_ap_gate.py
python3 src/qp_remote_ap_gate.py --Y 100 300 1000 --samples 1500
```
