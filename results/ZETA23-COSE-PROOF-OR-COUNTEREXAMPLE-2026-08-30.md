# COSE proof-or-counterexample audit

**Date:** 2026-08-30  
**Status:** COSE as defined on ordinary primes is neither proved nor refuted;
its relaxation to abstract source/carrier node systems is refuted exactly;
projection and finite-prime audits completed; no uniform zero-free strip and
no proof of RH

## 0. Verdict

Fix the carrier subspace by joining every opposite-side ordinary-prime pair
with

```text
B|u_p-u_q|<=1,                  B=Y^(50/33),
```

and requiring equal coefficients on each resulting pair.  Same-side prime
spacing makes this graph a matching for large `Y`, so the definition is
independent of `y`.  Write it as `C_Y`.

For a legal source direction

```text
v=a_P(t_0)+Dq_P,                 D>=Y^(-.001+o(1)),
```

the actual-prime COSE assertion is

```text
s_car(v):=inf {sup_(t in H_Y)y.a_P(t):
               y in C_Y, y.v=-1}
          >=Y^(-.0179-o(1)).                         (0.1)
```

The audit has a split verdict.

- The tested relaxation retaining source mass, separation, carrier support,
  and scale but discarding the ordinary-prime mask admits an exact
  carrier-only Fejer countermodel, including the original mass-normalized source-event
  threshold.  Its zero-coefficient source population has prime-scale size;
  the much smaller first padding construction would not have sufficed.
- No countermodel satisfying the ordinary-prime mask and asymptotic legal
  source event was found.
- The best projection/frame proof gives only `Y^(-1+o(1))`, missing the
  desired exponent by `.9821`.
- On a shell with no close reflected pairs, `C_Y` is the whole coefficient
  space, so `(0.1)` is exactly LTRAD at that shell.  No theorem currently
  says a legal event forces even one close pair, much less a large corrector
  sector.

Thus the abstract relaxation is false, while COSE itself remains open.  In
the no-pair branch COSE is not a reduction of LTRAD.

## 1. Exact projected formulation

Let `Pi_C` be orthogonal projection onto `C_Y`.  Restricting the separator to
`C_Y` gives the exact projected radial duality

```text
s_car(v)=max {s>=0:
              -s Pi_C v in conv{Pi_C a_P(t):t in H_Y}}.   (1.1)
```

When attained, its KKT measure obeys

```text
integral Pi_C a_P(t)dnu(t)=-s_car Pi_C v.             (1.2)
```

The projection error is small in absolute Euclidean norm.  For each close
pair,

```text
|v_p-v_q|<=t_0|u_p-u_q|<<Y/B=Y^(-17/33).
```

The integer-product count gives at most
`K<<Y^(16/33+o(1))` pairs.  Therefore

```text
||(I-Pi_C)v||_2^2
 <<K(Y/B)^2
 <<Y^(-6/11+o(1)),

||(I-Pi_C)v||_2<<Y^(-3/11+o(1)).                    (1.3)
```

No relative estimate for `||(I-Pi_C)v||/||v||` is asserted.  The carrier
retains essentially the whole dimension:

```text
L=dim C_Y=Y^(1+o(1)).                               (1.4)
```

The separated-frame and source-evaluation estimates give only

```text
h_Y(y)>>E_C(y)^(1/2)/sqrt(L),
1=|y.v|<<sqrt(L)E_C(y)^(1/2),
```

and hence

```text
s_car(v)>>1/L=Y^(-1+o(1)).                          (1.5)
```

Even replacing the first inequality by the unrealistically lossless
`h>>E_C^(1/2)` yields only `Y^(-1/2+o(1))`.  Projection, KKT, and ordinary
frame conditioning therefore cannot reach `.0179`.

The exact missing inequality is the adaptive one-sided estimate

```text
|F_y(t_0)+D F_y(0)|
 <=Y^(.0179+o(1)) sup_(t in H_Y)F_y(t),
 y in C_Y.                                           (1.6)
```

Equation `(1.6)` is the polar form of COSE, not a simpler consequence.

## 2. Exact generic carrier countermodel

Put

```text
tau=.0179,
m=ceil(Y^(tau+2eta)),
t_0=Y^(1/2),
omega=2pi/t_0,
```

where `eta>0` is fixed and small.  Use `m-1` active one-sided frequencies

```text
u_d=d omega,                      1<=d<m.             (2.1)
```

The original directional premise is mass-normalized, so a source block of
only `O(m)` nodes is not enough.  Instead choose a fixed one-sided interval
`J subset (0,w)`, disjoint from the active band, and put in it

```text
M asymp Y/log Y                                                (2.2)
```

distinct zero-coefficient source nodes, separated by
`>>log(Y)/Y`, all selected from the open arcs

```text
cos(t_0 u)<=-1/2.
```

These arcs occupy a fixed positive proportion of `J`, so the packing in
`(2.2)` exists.  If `I` is this synthetic source interval and

```text
D=-M^(-1)sum_(u in I)cos(t_0u),
```

then `1/2<=D<=1`.  Since `N asymp Y`, its original mass-normalized negative
event has size

```text
e(I,Y,t_0)=DM/N asymp 1/log Y >>Y^(-.001).           (2.3)
```

Thus this is a genuinely legal event in the abstract node class, not merely
a probability-normalized negative direction.  The arithmetic information
it omits is precisely that the complete nodes are ordinary-prime logarithms.

Give all source nodes coefficient zero and put on the active nodes

```text
y_d=-[2/(1+D)](m-d)/[m(m-1)].                       (2.4)
```

For

```text
K_m(t)=m^(-1)|sum_(a=0)^(m-1) exp(i a omega t)|^2,
```

direct expansion gives

```text
F_y(t)=[1-K_m(t)]/[(1+D)(m-1)].                     (2.5)
```

Thus

```text
F_y(t_0)=F_y(0)=-1/(1+D),
y.[a(t_0)+Dq]=-1,                                   (2.6)
sup_t F_y(t)=1/[(1+D)(m-1)]
             <<Y^(-(.0179+eta)).                    (2.7)
```

Equality in `(2.7)` occurs at `t=t_0/m`, which lies in `H_Y`.  All nodes are
one-sided and lie in a fixed shell.  The active spacing is
`asymp Y^(-1/2)>>B^-1`, and the source-node spacing is
`>>log(Y)/Y>>B^-1`; consequently the entire coefficient vector is
carrier-only.

This proves that source depth, carrier separation, KKT geometry, and frame
bounds cannot prove COSE.  The missing ingredient must distinguish ordinary
prime logarithms from the mesh `(2.1)`.

Replay the identities and exponents with

```bash
python3 results/verify_zeta23_cose.py
```

## 3. Why the canonical projected separator does not refute prime COSE

The natural carrier-supported candidate is

```text
w=Pi_C v,                    y_0=-w/||w||_2^2.       (3.1)
```

It has `y_0.v=-1`, but its cap is

```text
h_Y(y_0)
=-min_(t in H_Y)<w,Pi_C a_P(t)>/||w||_2^2.          (3.2)
```

Without projection, its numerator is a combination of the shell
correlations

```text
S(s)=sum_(p in P_Y) cos(s|log(p/Y)|)
```

at `t-t_0`, `t+t_0`, and `t`.  The fixed logarithmic shell itself has
constant negative Fourier sidelobes.  For example, at `s_0=pi/w`, the
continuous symmetric prime-density model has normalized transform

```text
integral_0^w cosh(u)cos(s_0u)du / integral_0^w cosh(u)du
 =-1/(1+s_0^2).                                     (3.3)
```

Hence norm projection does not generate a small one-sided cap; it inherits
fixed sidelobes.  A successful counterexample needs a specially designed
adaptive prime weight, not `-Pi_Cv`.

Constructing such a weight is itself a prime-supported one-sided Turan
problem.  Scalar prime Dirichlet estimates do not settle it because the
coefficient vector is selected adaptively after seeing the source.

## 4. Finite actual-prime diagnostic

Carrier-constrained and unrestricted sampled saddles were compared after
enforcing equal coefficients on every canonical close pair.

| `Y` | pairs | unrestricted radius, exchange bracket | carrier radius, exchange bracket |
|---:|---:|---:|---:|
| 254.5 | 2 | [.59617,.60152] | [.63558,.63757] |
| 299.5 | 3 | [.53171,.53623] | [.54118,.54232] |
| 500.5 | 2 | [.48903,.49145] | [.49348,.49594] |
| 800.5 | 1 | [.37805,.37941] | [.38013,.38147] |
| 1600.5 | 1 | [.27685,.27885] | [.27705,.27906] |
| 3000.5 | 1 | [.23763,.24053] | [.23771,.24010] |

The carrier penalty shrinks from a few percent to numerically unresolved in
the larger examples.  With unit constant and a chosen `.00005` exponent
margin, the finite plug-in `Y^(-(.0179+.00005))` is about `.87--.91`, so
every displayed carrier radius lies below it.  This plug-in is not the
asymptotic theorem, whose constants and `o(1)` term are unspecified.

This does not refute `(0.1)`: the sampled depths are only `.14--.49`, versus
`Y^-.001` about `.992--.994` at these sizes; the exchange bounds are floating
rather than interval-certified; and only one to three pairs occur.  Only the
cases through `Y=800.5` have a resolved positive carrier penalty under the
displayed brackets.  The experiment shows merely that corrector cancellation
is not the first obstruction in these finite surrogate models.

## 5. Exact remaining alternatives

An actual-prime resolution must do one of the following.

1. Prove the adaptive one-sided prime Turan inequality `(1.6)` with a fixed
   power `.0179`.
2. Construct, from a legal actual-prime source event, a carrier coefficient
   vector emulating `(2.4)` with a certified cap below the target.
3. Prove first that every legal source event forces a quantitatively large
   close-reflected sector.  Without this theorem the no-pair branch makes
   COSE identical to full LTRAD.

None is currently available.  The first alternative is COSE itself; the
second is an actual-prime counterexample; the third would finally make the
carrier/corrector split a genuine reduction.

```text
abstract source/carrier relaxation of COSE:          REFUTED
COSE (actual-prime asymptotic statement):            OPEN
projection error ||(I-Pi_C)v||<<Y^(-3/11+o(1)):     PROVED
projection/frame lower bound Y^(-1+o(1)):           PROVED
finite carrier/unrestricted comparison:             DIAGNOSTIC ONLY
legal event forces close reflected pairs:            OPEN
LTRAD_P(.0189,.001):                                 OPEN
uniform zero-free strip:                             NOT PROVED
RH:                                                  NOT PROVED
```
