# Global compact Pick transfer: a deep-fan fail-fast audit

Status: exact class formulas, pointwise reflected-pair Poisson correction,
conditional high-jet danger envelope, and primary-literature audit,
2026-08-13.  The global compact Pick gate remains **open**.  No zero-free
strip or RH statement is proved.

## 1. Binary verdict

**LIVE, not falsified and not closed.**  The present ledger is

```text
alpha=.49,                     d=.66,
alpha*d=.3234,
B_G=.304/2+.66*1.39/(2*pi)
   =.2980087447925048...,
S=.3234-B_G
 =.0253912552074952... .                            (1.1)
```

Here `B_G` is the conservative causal one-representative Green bill and
`S` is the available extra Pick/compact surcharge.

This audit gives two sharply different results.

1. A centered, depth-shifted interlaced-binomial screen is a rigorous
   **lower obstruction** for the unrestricted scalar Schur problem.  After
   imposing the pointwise completed-Poisson condition needed by any actual
   reflected zero list, its numerically optimized exponent is

   ```text
   .013984924... < S.                               (1.2)
   ```

   It therefore does not falsify GP.  It is not an upper construction and
   hence also does not prove GP.
2. An optimistic `4r`-rows-for-`r`-jets envelope reaches

   ```text
   .028826834... > S.                               (1.3)
   ```

   But (1.3) is conditional on a growing positive quadrature with uniform
   depth, conditioning, and Taylor/Schur remainder control.  Only the
   fixed-order version is proved.  Thus (1.3) is a precise danger threshold,
   not a counterexample.

No admissible actual-zero list forcing more than `S*L` loss is proved, and
no uniform compact two-leg upper construction below `S*L` is proved.

## 2. The centered binomial class

Fix a horizontal coordinate `b<alpha`, put `eta=alpha-b`, and take two
interlaced chains centered at ordinate zero,

```text
z_n =b-i*(n-K/2)*pi/(d*L),
z'_n=b-i*(n-K/2+1/2)*pi/(d*L),       0<=n<=K,
K/L -> c,
H=pi*c/d.                                           (2.1)
```

The phases are the alternating real and imaginary binomial phases, exactly
as in the unshifted screen.  Put

```text
R=sqrt(eta^2+(H/2)^2),
y=eta/H,
J(y)=1+integral_0^1 log|1/2+i*y-x| dx
    =(1/2)log(1/4+y^2)+2*y*atan(1/(2*y)),           (2.2)
J(0)=-log 2.
```

### Proposition 2.1 (depth-shifted screen exponent)

If `R<alpha` and a right-half-plane Schur function satisfies all screen
half-space signs, then

```text
limsup_(L->infinity) L^(-1)log|U(alpha)|
 <=-F(b,c),

F(b,c)=c*{log[alpha/(2*R)]-J(y)}.                  (2.3)
```

The point of `J(y)` is important.  Taylor expansion at `alpha` gives the
remainder factor `(R/alpha)^(K+o(K))`; positive binomial dependence gives
`2^K`; and evaluation from the chain back at the horizontally displaced
target gives

```text
exp{K*J(y)+o(K)}.                                  (2.4)
```

The last factor follows directly from the complex Lagrange product at
`K*(1/2+i*y)` and Stirling's formula.  Omitting (2.4) treats a complex
off-chain target as an on-chain target and produces a false larger
obstruction.  Multiplying the three factors proves (2.3).

This proposition is an upper bound on the target value for functions which
sign this particular artificial list.  Equivalently, it is a lower bound on
the loss demanded by that list.  Its polarity is not a universal upper bound
on the loss for arbitrary lists.

## 3. The missing pointwise Poisson constraint

Every actual reflected-pair list also obeys the completed-log-derivative
bound, at each ordinate,

```text
sum_pairs [(1/2-b)/((1/2-b)^2+v^2)
          +(1/2+b)/((1/2+b)^2+v^2)]
 <=L/2+o(L).                                        (3.1)
```

At the center of (2.1), its two-chain Riemann sum has normalized load

```text
P(H,b)=(4*d/pi)*{
          atan[H/(2*(1/2-b))]
         +atan[H/(2*(1/2+b))]} .                   (3.2)
```

Consequently a necessary condition for this screen to model an actual list
is

```text
P(H,b)<=1/2,             c=d*H/pi.                 (3.3)
```

This pointwise test is stronger for the centered screen than merely charging
an integrated fixed-window count.  Finite endpoint and lattice errors are
`o(L)` and do not affect (3.3).

Numerically maximizing the exact formula (2.3), subject to (3.3) and the
live horizontal band `alpha*d<=b<alpha`, gives

```text
b             =.4709446182...,
c             =.0079215710...,
P(H,b)        =.4999999940...,
F(b,c)        =.0139849236...,
S-F           =.0114063316... .                    (3.4)
```

The formulas are exact; (3.4) is a reproducible floating optimization, not
an interval-certified global maximization.  Its large gap to `S` makes it a
useful class fail-fast result, but no global claim about all fan geometries
is inferred from it.

## 4. The one surviving high-jet danger

At fixed horizontal coordinate `b`, one reflected row at the center costs

```text
K_b=1/(1/2-b)+1/(1/2+b)                            (4.1)
```

in (3.1).  If, hypothetically, a uniformly conditioned growing fixture used
`4r+o(r)` rows to force `r` Schur steps while all its rows had
`K_b+o(1)` Poisson cost, then (3.1) would permit

```text
r/L <=1/(8*K_b)+o(1).                              (4.2)
```

Each step at `b` costs

```text
log[(alpha+b)/(alpha-b)]                           (4.3)
```

at the target.  The resulting conditional envelope is

```text
E_4(b)={1/(8*K_b)}log[(alpha+b)/(alpha-b)].         (4.4)
```

Over the same live band,

```text
max E_4(b)=.0288268337...
at b=.3268277905...,
max E_4-S=.0034355785... .                         (4.5)
```

Equation (4.5) identifies the first constants-compatible danger, but its
premise is not known.  The proved convex-geometric lemma supplies at most
`4r+4` rows only for each **fixed** `r`; its positive-spanning constant and
largest scaled depth are uncontrolled as `r` grows.  Taylor remainder and
iterated Schur errors are likewise not uniform.  The companion shallow-fan
theorem in fact makes every fixture with maximum scaled depth
`o(L/log L)` harmless at fixed-power scale.  A genuine counterexample must
therefore solve the growing deep-cusp conditioning problem, not merely count
real dimensions.

## 5. What the primary literature does and does not supply

* Carleson's bounded interpolation theorem characterizes unrestricted
  `H^infinity` interpolation by uniform separation.  Deep confluent fans
  need not be separated, so it gives no uniform GP construction:
  L. Carleson, *An Interpolation Problem for Bounded Analytic Functions*,
  Amer. J. Math. 80 (1958), 921--930,
  <https://doi.org/10.2307/2372840>.
* Sarason's generalized interpolation theorem covers exact finite and
  confluent `H^infinity` feasibility through the compressed-shift norm.  It
  does not bound that norm from reflected-pair Poisson mass alone and does
  not impose compact two-leg Paley--Wiener support:
  D. Sarason, *Generalized interpolation in H-infinity*, Trans. AMS 127
  (1967), 179--203,
  <https://doi.org/10.1090/S0002-9947-1967-0208383-8>.
* McPhail's weighted interpolation theorem requires a weighted
  interpolation/Carleson condition.  The completed-Poisson bound is only an
  upper mass condition and supplies neither separation nor the needed
  confluent conditioning:
  J. McPhail, *A weighted interpolation problem for analytic functions*,
  Studia Math. 96 (1990), 105--116,
  <https://doi.org/10.4064/sm-96-2-105-116>.
* Tchakaloff's theorem gives positive finite cubature for each prescribed
  finite moment degree, including noncompactly supported measures.  It gives
  no uniform bound on node depth or positive-spanning condition number when
  the degree grows with `L`:
  C. Bayer and J. Teichmann, *The proof of Tchakaloff's Theorem*, Proc. AMS
  134 (2006), 3035--3040, <https://arxiv.org/abs/math/0502473>.

Thus classical Pick theory handles a finite unconstrained problem, and
classical quadrature handles fixed moment order.  Neither theorem bridges
the two missing quantifiers: growing deep fans under only (3.1), and compact
causal realization on two physical endpoint legs.  Rational inner Pick
solutions also have infinite causal tails, so unrestricted Pick feasibility
is not the compact transfer asserted by GP.

## 6. Weakest theorem which would close GP

It is enough to prove the following statement; no one-representative rule or
cellwise multiplication theorem need appear in its conclusion.

> There exist fixed `epsilon>0` and `L_0` such that, for every `L>=L_0` and
> every actual candidate-local reflected zero list allowed by the completed
> Poisson bound, there is a scalar causal two-leg Schur state `F_R,F_L`
> satisfying every required half-disk sign, whose inverse Laplace transforms
> fit in the two available endpoint layers, for which reverse-endpoint and
> base-profile errors are subcarrier, and
> 
> ```text
> -log|F_R(alpha)F_L(alpha)|
>  <=(.3234-epsilon)*L+o(L).                        (6.1)
> ```

Equivalently, if the state is obtained by composing the audited Green base,
whose loss is at most `B_G*L`, it is enough that the residual correction cost
at most `(S-epsilon)*L+o(L)`.  The full-state form (6.1) is the logically
weakest target: it does not require that particular decomposition.  An
unrestricted Schur solution without compact two-leg realization is
insufficient; an obstruction below `S` is also insufficient.

## 7. Truth table

| assertion | verdict |
|---|---|
| centered depth-shifted screen exponent (2.3) | **proved** |
| pointwise reflected-pair cap (3.3) is necessary for an actual screen | **proved** |
| optimized centered-screen obstruction exceeds the surcharge | **no**, by (3.4) |
| a proved growing high-jet fan exceeds the surcharge | **no** |
| the optimistic `4r` envelope crosses the surcharge | **yes, conditional**, by (4.5) |
| existing interpolation or cubature literature supplies the missing uniform compact theorem | **no** |
| GP is falsified | **no** |
| GP is proved | **no** |

## 8. Reproduction

```bash
python3 src/test_global_pick_deep_fan_gate.py
python3 results/verify_zeta23_global_pick_deep_fan_gate.py
```

The checker intentionally returns `gp_closed=False`; `PASS` means that the
normalizations and the scoped inequalities above replay, not that GP closes.
