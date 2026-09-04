# Theta `B_P`: complete inverse-resolvent obstruction

**Date:** 2026-08-13  
**Status:** a complete, infinite-operator route is rigorously closed in a
precise scalar class.  Positive definiteness of the actual `B_P` family is
**not** proved or disproved.  No zero-free strip follows from this note.

## 1. Binary result

The polar-subtracted modular product from the preceding audit is

```text
C(w,d)=R((w+d)/2)R((w-d)/2),
Phi((w+d)/2)Phi((w-d)/2)=mathcal_L C(w,d)/256,

mathcal_L=(partial_w^2-partial_d^2)^2
          -2(partial_w^2+partial_d^2)+1.              (1.1)
```

This identity is already fully recompleted: `C` contains the complete
two-dimensional orbit, both axes, the corner, and all Poisson reflections.
Fourier transform in `w` turns (1.1) into

```text
h_T(d)=L_T c_T(d)/256,

L_T=D_d^4+2(T^2-1)D_d^2+(T^2+1)^2
   =[1-(D_d+iT)^2][1-(D_d-iT)^2].                    (1.2)
```

The Fourier symbol is strictly positive:

```text
p_T(lambda)
 =[1+(lambda+T)^2][1+(lambda-T)^2]
 =lambda^4+2(1-T^2)lambda^2+(1+T^2)^2 >=1.          (1.3)
```

It is therefore natural to try to move between the positive complete
configuration kernel and its differentiated theta density by the inverse
resolvent `L_T^(-1)`.  The following calculation rules out a positive scalar
resolvent once and for all.

> **Theorem 1 (complete scalar-resolvent no-go).**  The unique decaying
> translation-invariant fundamental solution of `L_T` is
>
> ```text
> G_T(d)=exp(-abs(d))/[4(1+T^2)]
>        *[cos(T abs(d))+sin(T abs(d))/T],             (1.4)
> ```
>
> with continuous value
>
> ```text
> G_0(d)=(1+abs(d))exp(-abs(d))/4.                     (1.5)
> ```
>
> It is positive at `d=0`, but for every `T!=0`,
>
> ```text
> G_T(pi/abs(T))
>   =-exp(-pi/abs(T))/[4(1+T^2)] <0.                  (1.6)
> ```
>
> Consequently no **pointwise nonnegative** scalar translation-invariant
> inverse kernel for the fully completed operator exists at any nonzero
> Fourier height.

This is an infinite-orbit/operator result, not a finite-orbit failure.  The
operator being inverted is the exact completed operator after all modular
orbits have been recombined.

## 2. Proof with no numerical premise

The two factors in (1.3) have inverse Fourier kernels

```text
k_+(d)=exp(-abs(d))exp(+iTd)/2,
k_-(d)=exp(-abs(d))exp(-iTd)/2.                       (2.1)
```

Their convolution is the unique tempered convolution inverse because
`p_T(lambda)` has no real zero.  Splitting the convolution integral at
`0` and `d` gives (1.4).  Equivalently, away from the origin direct
differentiation gives `L_T G_T=0`; the even extension is `C^2`, and

```text
G_T'''(0+)-G_T'''(0-)=1.                              (2.2)
```

Thus `L_T G_T=delta_0`.  Formula (1.6) is immediate and proves the sign
change exactly.  As normalization checks,

```text
integral_R G_T(d)dd=1/(1+T^2)^2=1/p_T(0),             (2.3)

first positive zero
 =[pi/2+atan(1/abs(T))]/abs(T).                       (2.4)
```

The sign change is not due to a bad branch or a missing contact term: the
positive symbol, unit jump, total mass, and zero-frequency limit all agree.

## 3. What this eliminates—and what it does not

The theorem eliminates the following proposed proof class:

```text
full modular recompletion
 -> Fourier fiber T
 -> invert the scalar completed d-operator
 -> invoke positivity preservation of its Green kernel
 -> conclude B_P is positive definite.               (3.1)
```

The third arrow is false for every `T!=0`.  Taking absolute values is not a
repair: it destroys the exact axis/interior cancellation, while the signed
kernel has positive total mass only after its negative lobes are retained.

There is an important distinction.  Since `Ghat_T=1/p_T>0`, `G_T` *is* a
positive-definite convolution kernel and `L_T^(-1)` is a positive operator
in the Hilbert-space/Loewner sense.  What fails is order positivity:
convolution by `G_T` does not preserve the cone of pointwise nonnegative
functions.  Therefore Theorem 1 does not kill a genuine quadratic-form Gram
argument; it proves that such an argument cannot be obtained merely by
feeding the already known pointwise sign `C(w,d)>0` through the scalar
resolvent.  New Hilbert-space input identifying the two vectors in the
resulting cross pairing would still be required.

The theorem does **not** establish any of the following stronger claims:

1. It does not show `S_3(P,T)<0` at any actual `(P,T)`.
2. It does not rule out a matrix-valued dilation in which the two axes and
   the interior are separate channels.
3. It does not rule out a non-translation-invariant operator coupling
   different `T` fibers.
4. It does not rule out a direct inequality for the complete signed
   inclusion--exclusion sum.
5. It does not alter the previous numerical survival of `S_3`.

Those qualifications are essential.  The result is a definitive fail-fast
for one genuinely infinite route, not a no-go theorem for `B_P` itself.

## 4. Literature boundary

The endpoint is not an overlooked standard theorem.  At `P=0`, changing
variables `s=d/2`, `t=w/2` gives exactly

```text
B_0(w)=2 K_1(w/2),
K_1(t)=integral_R s^2 Phi(s+t)Phi(s-t)ds.              (4.1)
```

In [Csordas, Theorem 3.7](https://arxiv.org/abs/1309.0055), the Fourier
positivity of this canonical `K_1` is the first Laguerre inequality.  The
same paper explicitly leaves its validity for the Riemann theta kernel as
Open Problem 4.7.  Thus the present all-`P` target contains a published open
problem already at its endpoint; the literature does not supply a hidden
`P=0` lemma.

Csordas's Proposition 3.10 is the closest directly reusable lemma.  If
`G(t)=integral_t^infinity K_1(u)du` and `A=G(0)`, it rewrites `K_1` positive
definiteness as

```text
integral_0^infinity G(t)sin(x t)dt <= A/x,  x>0.        (4.2)
```

Monotonicity makes the sine transform positive by the alternating-series
argument, but does not give the upper bound in (4.2).  That upper bound is
equivalent to the open Fourier sign, so citing the Pólya sine criterion does
not discharge the endpoint.

The modern classification in [Belton--Guillot--Khare--Putinar, *Totally
positive kernels, Pólya frequency functions, and their transforms*](https://arxiv.org/abs/2006.16213)
describes the rigidity of Hankel and Pólya-frequency preservers.  It does not
turn a kernel failing the requisite Hankel minors into a totally positive
one.  The preceding exact theta audit already found
`Phi(0)Phi''(0)<0` in the relevant Hankel orientation, so this theory cannot
be imported to certify (4.1), much less the excised `P>0` family.

Jacobi inversion and the triple product remain indispensable for the full
orbit recompletion, but they provide modular identities rather than a
Bochner measure.  The distinction is visible in (1.4): a positive Fourier
symbol need not have a pointwise-positive inverse Green function.

Finally, [Csordas, *The Laguerre inequalities and the zeros of the Riemann
xi-function*](https://doi.org/10.1080/17476930903394820) proves that a finite
Fourier-cosine truncation of the Jacobi-theta kernel can acquire nonreal
zeros.  This is consistent with the exact odd-jet obstruction already in
the local cache and confirms that finite truncation is not a literature
shortcut to (4.1).  None of these sources gives a theorem for the excised
`P>0` kernels.

## 5. Counterexample search status

No rigorous Arb counterexample to the actual `S_3(P,T)` was obtained in
this attack.  A rescaled continuation with `dx=.025`, `T` spacing `.25`, and
`1000<=T<=2000` returned only apparent negatives of size at most
`3.7*10^(-10)` relative to the local Laguerre scale.  They lie at the known
double-precision cancellation floor.

The worst broad-grid point was near

```text
T=1302.5, P=2.36109422.                                (5.1)
```

Here the extrapolated endpoint used by the fast grid was wrong by more than
the alleged negative.  The new tool
`src/theta_s3_arb_simpson_target.py` computes that endpoint from an exact
Arb power-series jet and accumulates the normalized Simpson sum in Arb
arithmetic.  At mesh widths `.1,.05,.025` it gives

```text
scaled S_3 discrete Simpson
  .1    0.0001400198816132159910...
  .05   0.0001298204663983125656...
  .025  0.0001291863344770681209... .                   (5.2)
```

The two successive differences have ratio `16.084`, the expected
fourth-order Simpson convergence, and Richardson extrapolation is
`+0.000129144059...`.  Thus the worst apparent negative is numerically
rejected, not promoted to interval certification.  Arb rigorously encloses
the node values and each discrete sum in (5.2), but no continuum Simpson
remainder is claimed; this remains a high-precision falsification result.

The logical status is therefore

```text
pointwise-positive scalar inverse resolvent      RIGOROUSLY FALSE
finite/primal-dual orbit Gram                   ALREADY FALSE
actual B_P positive definiteness                OPEN
actual Arb counterexample                       NOT FOUND
uniform zero-free strip                         NOT PROVED.          (5.3)
```

## 6. Reproduction

```bash
python3 -m pytest -q src/test_theta_bp_complete_resolvent_nogo.py
python3 results/verify_zeta23_theta_bp_complete_resolvent_nogo.py
python3 src/theta_bp_complete_resolvent_nogo.py
python3 -m pytest -q src/test_theta_s3_arb_simpson_target.py
python3 src/theta_s3_arb_simpson_target.py \
  --t 1302.5 --p 2.36109422 --dx 0.1 --margin 60 --dps 50
```

The verifier independently checks the symbol factorization and the Green
ODE/jump with SymPy, then gives outward-rounded Arb negative intervals at
`T=1/2,1,2,10`.  The five unit tests also check evenness, the `T->0` limit,
the explicit negative witness, and the total mass.  Two additional fast
tests audit the exact normalized Laguerre jet and the analytic sine-cubic
tail used by the target scout.

## 7. Exact successor

If the direct theta route is retained, the next admissible construction is
strictly narrower than “use the full resolvent”:

> Build an explicit **matrix-valued** modular orbit operator whose channels
> keep the interior, two axes, and corner distinct, prove the resulting
> operator-valued spectral measure is positive, and show that contraction
> with the exact tail boundary vector equals (not merely bounds) (2.6) of
> the preceding cross-orbit note.

Absent such a channel-positive dilation, the efficient falsification move is
targeted Arb certification near any scale-separated negative returned by a
rescaled `S_3` scout.
