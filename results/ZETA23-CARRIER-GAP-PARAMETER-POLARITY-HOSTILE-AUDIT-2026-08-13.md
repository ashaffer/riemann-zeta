# Carrier/gap parameter polarity: hostile audit

**Date:** 2026-08-13

## Verdict

The arithmetic in the parameter reoptimization passes, including the exact
interior choice

```text
alpha_0=47/100,   d=133/200,
theta=397/2500,  beta=799/5000.
```

Since `beta-theta=.001`, every sufficiently large retained gap
`g<=C Y^theta` has `g<Y^beta`.  A reduced rational whose two endpoint phases
coincide has `q|g`, hence `q<=g`; it is therefore inside the rational cover.
The retained literal one-gap pole sector is genuinely empty.  The stated
tail, collar, inverse-image, Green, and packet inequalities are also strict.

The hostile correction is one of **polarity and quantifiers**, not arithmetic.
This certificate does not close a dual antenna uniformly on the candidate
band `alpha in [.47,.5)`, and it cannot eliminate the carrier architecture.
It removes one sector for one conservative shallow-depth calibration.  The
multi-gap/nonpole high tail, `GP`, and `GA` remain open even there.

No zero-free strip is proved.

## 1. Replayed formulas and exact certificate

For `Y=X^d`, the aperture exponent is

```text
A=1/d.
```

With the licensed Bellotti--Wong constant `a=.10076`, put

```text
E_1(alpha,d)
 =alpha*(d-1/2)*(1-R(y)),
y=pi*a/[alpha*(2d-1)],
R(y)=[y log(1+y^-2)+2 atan(y)]/pi,
kappa(alpha,d)=E_1(alpha,d)/d.
```

The Gafni--Tao branch and continuous rational frontier are

```text
s(x)=(45x-6)/65,
theta_0=2/15+(13/9)kappa,
beta_0=14/15-1/(2d)-(11/9)kappa.
```

Their pole-margin identity is exact:

```text
s(beta_0)-kappa
 =(9/13)(beta_0-theta_0)
 =(24/13)(kappa_crit(d)-kappa),
kappa_crit(d)=3/10-3/(16d).
```

At the explicit interior point the replay gives

```text
A                                      =1.5037593984962406...
E_1                                    =.01165230851907937...
kappa(.47,.665)                        =.01752226844974341...
s(theta)-kappa                         =.00010850078102582...
[2-A-2beta-theta]-kappa                =.00031833305401599...
[1-A/2-beta]-kappa                     =.07079803230213629...
s(beta)-kappa                          =.00080080847333352...
beta-theta                             =.001.
```

The rounded Green--Poisson certificate also fits:

```text
raw carrier alpha*d                    =.31255
Green bill .152+d*1.39/(2pi)           =.2991148716469935...
Green reserve                          =.01343512835300653...
Green reserve-E_1                      =.00178281983392716....
```

The older packet bounds and compact-tail sufficient inequalities pass with
room:

```text
1/2<d<2/3,
alpha>3/8,
alpha*d^2-2a                          =.00632575>0,
alpha*d-a/2                           =.26217>0.
```

Thus `.49` was a target choice, not a structural lower bound.  The Green
majorant itself only uses `0<alpha<=1/2`; its old displayed `.49` floor came
from the chosen `.99` strip.

For the old target `alpha>=.49`, the independent monotonicity argument also
passes.  The best pole margin occurs only at `alpha=.49, d->2/3` and equals

```text
-.001034601762499405... .
```

Every legal interior point is worse.  The limiting crossing depth is

```text
alpha_*=.482559677686675026...,
kappa(alpha_*,2/3)=3/160.
```

## 2. The polarity distinction

The threshold `kappa` has opposite worst endpoints in the two logical
directions.

For a **promotion** sufficient to build a strip state, a uniform construction
may deliberately retain only the lower-end carrier
`E_1(alpha_0,d)`.  Since `kappa(alpha,d)` increases strictly with `alpha`,
the shallow endpoint `alpha_0` is the hardest promotion threshold.

For a **dual antenna/no-go**, this reasoning reverses.  A deeper candidate
has more carrier and can afford a smaller aligned mass.  To eliminate an
architecture which may adapt to the actual candidate depth, a saving `c`
must beat

```text
sup_(alpha_0<=alpha<1/2) kappa(alpha,d)
 =kappa(1/2,d),
```

not the minimum `kappa(alpha_0,d)`.  At the explicit `d=.665`,

```text
kappa(.47,.665)                         =.0175222684497434...
kappa_crit(.665)                        =.0180451127819549...
kappa(.5,.665)                          =.0197404825829421....
```

The fixed rational certificate's smallest positive-mass saving is only

```text
s(.1588)=.0176307692307692... .
```

It therefore clears the conservative lower-end threshold but not the deep
candidate threshold.  With these fixed cutoffs, even the positive-mass
ledger clears candidate-specific `kappa(alpha,.665)` only through

```text
alpha<.47150559635909557...,
```

where the long-gap tail becomes binding.  Optimizing the cutoffs at this
fixed `d` extends the pole crossing only to
`alpha<.47721728945766084...`; taking `d->2/3` gives the absolute limiting
crossing `alpha_*` above.  None reaches the candidates arbitrarily close to
`1/2`.

The sharper conditional Green ledger makes the scope issue even clearer.
Its retained exponent in `Y`-units at the explicit point is

```text
kappa_G
 =[alpha*d-.152-d*1.39/(2pi)]/d
 =.02020320053083691...,
```

which also exceeds `kappa_crit(.665)`.  Hence failure against the smaller
`E_1` reserve cannot be advertised as failure of every carrier allowed by
the same conditional representative geometry.

The use of `a=.10076` has the same direction.  It supplies a worst-case
lower bound for the retained carrier.  Fewer actual collateral rows would
leave more carrier.  A worst-case lower reserve is valid for a sufficient
promotion theorem, but it is not an upper bound with which to prove a
universal carrier no-go.

## 3. Exact conclusion

The legal conclusion is:

```text
At alpha_0=.47 and d=.665, the current tail and rational-cover ledger can be
chosen so that no short retained single gap has coincident rational endpoint
phases; the accompanying worst-case positive-mass errors beat
kappa(.47,.665).
```

This is a real simplification of the fail-fast target.  It does **not** imply
any of the following:

```text
the full retained high-tail antenna is small;
QP is killed for every alpha in [.47,.5);
the old .49 carrier calibration is killed;
the candidate-centered carrier architecture is eliminated;
ZF(.47), ZF(.49), or any fixed strip.
```

Lowering `alpha_0` makes `ZF(alpha_0)` a stronger desired zero-free statement,
but it simultaneously weakens the shallow carrier and makes a dual no-go
easier.  Those are opposite logical directions.  A zero deeper than the
crossing depth does not force a zero at the crossing depth, so shallow-sector
failure cannot be propagated to the whole candidate band.

The remaining fail-fast object is still the signed multi-gap/nonpole
consecutive-transition mode, with natural denominator exponent

```text
1-A/2=.2481203007518797...>beta=.1598,
```

plus the companion interval above the Peano endpoint `.84125425...`.
