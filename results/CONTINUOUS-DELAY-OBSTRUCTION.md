# Continuous-delay obstruction to interface propagation

Status: exact identity proved; the proposed finite-interface uniqueness route
is invalidated in its current form.

The zero-mode equation has a finite sum of prime shifts on its arithmetic
side, but its archimedean side is not local between those shifts.  Gauss's
digamma representation gives, in ordinary Fourier frequency,

`psiRe(2 pi xi) - psiRe(0)
  = integral_(t>0) exp(-t/4)
      (1-cos(2 pi xi (t/2))) / (1-exp(-t)) dt`.

Thus the archimedean operator is a positive continuum of translation defects
at every delay `u=t/2>0`.  Compact support truncates which correlations are
nonzero, but it does not discretize the delay set.

Consequences:

1. The intervals cut out by `x = +/-a +/- log n` are not independent cells on
   which a local equation propagates finitely many boundary data.
2. Crossing a prime interface changes an atomic translation term, while the
   continuous archimedean delay operator continues to couple the point to the
   entire support.
3. Smooth endpoint matching plus prime-ramp jump conditions therefore do not
   by themselves overdetermine a solution.

The appropriate zero-mode problem is a Fredholm/Wiener--Hopf-type nonlocal
integral equation: a positive continuous-delay operator plus a rank-two pole
operator balanced against finitely many atomic prime translations.  The next
credible uniqueness mechanisms are:

- strict total positivity or variation diminution of the continuous-delay
  kernel after parity reduction;
- a Wiener--Hopf factorization excluding compactly supported null vectors;
- analytic continuation of the Fourier transform together with the explicit
  meromorphic symbol;
- a canonical-system uniqueness theorem imported from the Suzuki/de Branges
  realization.

This is a genuine negative Bayesian checkpoint for finite-interface
propagation, but a useful one: it prevents investing further effort in a
local recurrence that the exact archimedean operator does not possess.
