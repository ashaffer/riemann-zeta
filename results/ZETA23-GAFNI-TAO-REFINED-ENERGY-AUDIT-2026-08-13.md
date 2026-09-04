# Gafni--Tao refined-energy audit at the high-denominator gap threshold

**Verdict.** The refined `L^4`/additive-energy theorem does **not** improve
the unconditional Gafni--Tao envelope used by the half-cell truncation near
`theta=.15--.17`.  On the full certified Table-1 branch

```text
3/20 <= theta <= 353/1445,
```

the numerical consequence of the refined theorem is exactly the general
second-moment consequence

```text
mu(theta) <= 1-(45 theta-6)/65.
```

This is an exact rational conclusion, not a grid observation.  Consequently
the optimized gap threshold `theta>.1593771338` and rational cutoff
`beta<.153720513824...` are unchanged.

## 1. What was checked

The primary source is Gafni--Tao,
[*On the number of exceptional intervals to the prime number theorem in short
intervals*](https://doi.org/10.2140/ent.2026.5.221), Essential Number Theory
5 (2026), 221--241.  Its general theorem uses

```text
mu_2(theta,sigma)
 =(1-theta)(1-sigma)A(sigma)+2sigma-1,
```

and its refined theorem replaces this by

```text
min(mu_2(theta,sigma),mu_4(theta,sigma)),
mu_4(theta,sigma)
 =(1-theta)(1-sigma)A*(sigma)+4sigma-3.
```

Tables 1 and 2 give the published unconditional upper envelopes for `A` and
`A*`.  The authors' [ANTEDB implementation](https://github.com/teorth/expdb/blob/main/blueprint/src/python/prime_gap.py)
implements this same minimization numerically.  Its own docstring says that
the exceptional-set calculation is discretized, so it is useful as a
cross-check but not as the exponent certificate used here.  The exact checker
below uses rational arithmetic.

## 2. One binding point settles all additive-energy pieces

Let `Abar,Abar*` be the lower envelopes of all published Table-1 and Table-2
upper bounds.  At the binding point

```text
sigma=7/10,
Abar(7/10)=30/13,
Abar*(7/10)=235/39.
```

The `A*` value is the common endpoint of the Heath--Brown and
Tao--Trudgian--Yang pieces in Table 2.  Therefore

```text
M2(theta):=mu_2(theta,7/10)
 = (9/13)(1-theta)+2/5
 = 1-(45 theta-6)/65,

M4(theta):=mu_4(theta,7/10)
 = (47/26)(1-theta)-1/5,

M4(theta)-M2(theta)
 = (29/26)(1-theta)-3/5.                    (2.1)
```

The last expression is positive for `theta<67/145=.462...`, hence throughout
the relevant branch.  Thus the refined minimum at the binding point is still
`M2`.

The exact all-piece Table-1 audit shows that on the stated branch the general
computed envelope is precisely `M2`.  If `G2` and `G24` denote respectively
the general and refined computed envelopes, then

```text
G24 <= G2                                      (min <= mu_2),
G24 >= min(M2,M4)=M2=G2                       (sigma=7/10 witness).
```

So `G24=G2`.  This shortcut genuinely covers **every** other published `A*`
piece: changing or even perfecting `A*` away from `sigma=7/10` cannot remove
the witness already fixing the supremum.

At the selected gap exponent `theta=797/5000`, the exact values are

```text
M2 = 63827/65000       = .981953846153...,
M4 = 171541/130000     = 1.319546153846...,
M4-M2 = 43887/130000   = .337592307692....
```

The fourth-moment branch is therefore not close to binding.  At this `theta`,
an `A*` upper bound at `sigma=7/10` would have to improve from

```text
235/39 = 6.025641... 
```

to strictly below

```text
30/13 + 2/(1-theta)
 =256090/54639
 =4.686945...
```

before `mu_4` could beat `mu_2` at the witness.

## 3. Half-cell propagation

Because the refined envelope is identical here, the tail saving remains

```text
s(theta)=(45 theta-6)/65.
```

For

```text
kappa=.0180303234,
aperture exponent=50/33,
```

the strict tail constraint gives

```text
theta > (65 kappa+6)/45
      = .1593771338.
```

The half-cell collar constraint

```text
2-50/33-2 beta-theta > kappa
```

then gives, on the continuous boundary,

```text
beta < .153720513824....
```

Thus the existing interior rational choice

```text
theta=797/5000=.1594,
beta=1537/10000=.1537
```

remains optimal within this certificate.  Its three savings are

```text
tail       1173/65000  = .018046153846...,
collar     1489/82500  = .018048484848...,
main       29279/330000= .088724242424...,
```

all strictly above `kappa`.

## 4. Scope of the negative result

This is a no-improvement result for the **published `A,A*` envelope
calculation**, not a no-go theorem for actual primes.  It does not eliminate:

1. a substantially sharper `A*` estimate at `sigma=7/10`;
2. a sharper zero-density estimate that moves or removes the binding point;
3. genuinely new higher-energy or mixed-moment input;
4. a direct theorem for the retained consecutive-gap Fourier sum.

The journal paper itself notes that no nontrivial unconditional higher-energy
bounds beyond consequences of `A,A*` are known, and that the stronger
Heath--Brown-identity mixed-moment route has not been put into a parameterized
envelope usable here.  Nothing in that discussion eliminates the actual-prime
coherence target.

## 5. Reproduction

```bash
python3 results/verify_zeta23_gafni_tao_refined_energy.py
```

The verifier invokes the existing exact scan of every active Table-1 branch,
then proves the refined-envelope equality and half-cell propagation using
exact fractions.
