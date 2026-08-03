# Scale-uniform collar leakage

Status: the uncertainty/leakage estimate is proved; it does not by itself
prove a uniform old--collar Schur ratio below one.

Let `v` be supported on the two collars `[-b,-a] union [a,b]`, whose total
measure is `2 delta`, with `delta = b-a`.  In the ordinary Fourier
normalization used by the project, Cauchy--Schwarz gives

`|vhat(xi)|^2 <= 2 delta ||v||_2^2`.

Consequently

`integral_(|xi|<=R) |vhat(xi)|^2 dxi <= 4 R delta ||v||_2^2`.

Plancherel therefore gives

`integral_(|xi|>R) |vhat(xi)|^2 dxi
    >= (1 - 4 R delta) ||v||_2^2`.

In particular, choosing `R delta <= 1/8` puts at least half the mass outside
the band, uniformly in `delta`.  Since the quarter-line digamma multiplier
grows logarithmically, choosing `R` proportional to `1/delta` produces the
thin-collar diagonal gain of order `log(1/delta) ||v||_2^2`, up to the bounded
low-frequency loss and the rank-two pole term.  This rigorously explains why
a fixed Fourier cutoff under-resolves increasingly thin collars and why
restoring the omitted tail raises their computed diagonal energy.

## Why this does not prove the observed ratio

The required determinant is

`B(old,v)^2 <= Q(old) Q(v)`.

Leakage controls `Q(v)` relative to `||v||_2^2`.  A generic cross estimate
controls `B(old,v)` relative to `||old||_2 ||v||_2`.  But the old Weil margin
`Q(old)/||old||_2^2` becomes extremely small as support grows.  Thus the latter
estimate lacks precisely the factor `sqrt(Q(old))` needed by the determinant.
No support-only uncertainty principle can manufacture this factor.

Accordingly, a universal proof that the normalized ratio is below one would
already prove positivity propagation and hence carry essentially the
remaining RH content.  The next non-circular target is a **form-relative
cross estimate**, for example a representation of the cross operator through
the square root of the old positive form, with a contraction constant.  The
thin-collar leakage theorem supplies the collar-side inverse and shows that
arbitrarily small widths are not the dangerous regime; the old-energy
relative bound remains open.

Lean file: `RHBridge/ScaleUniformLeakage.lean`.
