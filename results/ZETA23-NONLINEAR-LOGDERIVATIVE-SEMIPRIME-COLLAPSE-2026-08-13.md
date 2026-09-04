# ZETA23 nonlinear log-derivative / semiprime audit

## Verdict

Squaring the logarithmic derivative does not give a free nonlinear zero
detector.  It does give the positive Dirichlet coefficients
`Lambda * Lambda`, supported on products of two prime powers.  However, at a
selected **simple** zero `rho`, imposing `H(rho)=0` makes the whole selected
residue come from the integrated-by-parts linear logarithmic derivative:

\[
 \mathop{\rm Res}_{s=\rho}H(s)L(s)^2
 =\mathop{\rm Res}_{s=\rho}H'(s)L(s)=H'(\rho),
 \qquad L=\zeta'/\zeta.
\]

The complementary `zeta''/zeta` quotient has zero selected residue.  At the
other zeros it does not vanish.  Equivalently, after applying the functional
equation, a term linear in `L` is forced back into the right-line ledger.  A
reflection-symmetric kernel cancels the entire semiprime term.

This is an exact structural no-go for obtaining a strip merely by replacing a
prime carrier by the denser semiprime carrier and invoking coefficient
positivity.  It is not an impossibility theorem for every estimate that might
also control the other-zero quotient or the forced linear term.

## 1. Local Laurent ledger

Let `rho` be a zero of multiplicity `m`, put `z=s-rho`, and write

\[
 \zeta(s)=z^m g(s),\qquad a_\rho={g'(\rho)\over g(\rho)}.
\]

Then

\[
\begin{aligned}
 L(s)&={m\over z}+a_\rho+O(z),\\
 L(s)^2&={m^2\over z^2}+{2ma_\rho\over z}+O(1),\\
 {\zeta''\over\zeta}(s)
 &= {m(m-1)\over z^2}+{2ma_\rho\over z}+O(1).
\end{aligned}
\]

Consequently

\[
 \mathop{\rm Res}_\rho HL^2
 =m^2H'(\rho)+2ma_\rho H(\rho).                 \tag{1}
\]

The identity

\[
 L^2={\zeta''\over\zeta}-L'                    \tag{2}
\]

and contour integration by parts give

\[
 \oint H L^2
 =\oint H{\zeta''\over\zeta}+\oint H'L.       \tag{3}
\]

The two local residues on the right of (3) are

\[
\begin{aligned}
 \mathop{\rm Res}_\rho H{\zeta''\over\zeta}
 &=m(m-1)H'(\rho)+2ma_\rho H(\rho),\\
 \mathop{\rm Res}_\rho H'L&=mH'(\rho).
                                                        \tag{4}
\end{aligned}
\]

Thus, if `H(rho)=0`, the nominal `m^2 H'(rho)` gain splits as
`m(m-1)H'(rho)+mH'(rho)`.  For a simple zero the first summand is exactly zero:
the selected detector is the original linear `L` detector.  A strip proof
must allow simple zeros, so the multiplicity correction cannot supply a
uniform gain.

At every other zero `eta` for which `H(eta)` is not zero, the Laurent term
`2 m_eta a_eta H(eta)` remains.  These regular parts encode interactions with
the other zeros (and, in the uncompleted form, the gamma and pole terms).

## 2. Exact arithmetic coefficient ledger

For `Re(s)>1`,

\[
 L(s)^2=\sum_{n\ge1}{(\Lambda*\Lambda)(n)\over n^s},
 \qquad
 L'(s)=\sum_{n\ge1}{\Lambda(n)\log n\over n^s}.
\]

If

\[
 Q(n)=\sum_{d\mid n}\mu(d)\bigl(\log(n/d)\bigr)^2,
\]

then

\[
 {\zeta''\over\zeta}(s)=\sum_{n\ge1}{Q(n)\over n^s},
 \qquad
 Q(n)=\Lambda(n)\log n+(\Lambda*\Lambda)(n).    \tag{5}
\]

In fact the apparently alternating Mobius quotient simplifies to

\[
 Q(n)=
 \begin{cases}
  (2a-1)(\log p)^2,&n=p^a,\\
  2\log p\log q,&n=p^a q^b,\ p\ne q,\\
  0,&n\text{ has at least three distinct prime factors}.
 \end{cases}                                      \tag{6}
\]

So its Dirichlet coefficients are themselves nonnegative.  The obstruction
is sharper than a coefficient-sign complaint: target localization is lost.
Equation (5) says that semiprime positivity is exactly what remains after the
prime-power linear term is subtracted from the broader quotient.  Equations
(3)--(4) say that when the quotient is made blind to a selected simple zero,
that same prime-power term carries the entire selected residue.

Accordingly, greater density of the log mesh below `Y^2` may improve an
arithmetic quadrature estimate, but it does not change the local zero ledger.

## 3. Uncompleted functional-equation ledger

Fix `1<c<2`.  Let

\[
 \chi(s)=\pi^{s-1/2}{\Gamma((1-s)/2)\over\Gamma(s/2)},
 \qquad
 A(s)={\chi'\over\chi}(s)
 =\log\pi-\tfrac12\psi((1-s)/2)-\tfrac12\psi(s/2).
\]

The functional equation gives

\[
 L(s)+L(1-s)=A(s).                                \tag{7}
\]

Write `H^R(s)=H(1-s)` and

\[
 I_c(H)={1\over2\pi i}\int_{(c)}H(s)L(s)^2\,ds.
\]

For a holomorphic kernel with sufficient vertical decay, interpreted first
on a finite rectangle and then along any sequence for which the horizontal
integrals vanish, shifting from `c` to `1-c` gives

\[
\begin{split}
 &\sum_\rho\{m_\rho^2H'(\rho)
       +2m_\rho a_\rho H(\rho)\}
       +H'(1)-2\gamma H(1)\\
 &= {1\over2\pi i}\int_{(c)}
 \left[(H-H^R)L^2+2H^R A L-H^R A^2\right](s)\,ds. \tag{8}
\end{split}
\]

Here the sum is the corresponding symmetric-height limit over nontrivial
zeros, and `gamma` is Euler's constant.  The last term on the first line is
the exact residue at the pole `s=1`.

Identity (8) has two immediate consequences.

1. For `H=H^R`, the semiprime term `(H-H^R)L^2` disappears identically.
2. For a nonzero holomorphic `H`, the linear coefficient `2H^R A` cannot
   disappear identically: `A` is not identically zero, and
   `H^R A identically 0` would force `H identically 0`.

Thus reflection cannot turn the right line into a same-state inequality
containing only the positive semiprime series.

## 4. Completed functional-equation ledger

Let

\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \quad D={\xi'\over\xi}=L+g,
\]

where

\[
 g(s)={1\over s}+{1\over s-1}-{1\over2}\log\pi
       +{1\over2}\psi(s/2).
\]

Since `xi(s)=xi(1-s)`,

\[
 D(1-s)=-D(s),\qquad D(1-s)^2=D(s)^2.            \tag{9}
\]

If

\[
 D(s)={m_\rho\over s-\rho}+b_\rho+O(s-\rho)
\]

at a zero, the completed contour identity is

\[
 \sum_\rho\{m_\rho^2H'(\rho)+2m_\rho b_\rho H(\rho)\}
 ={1\over2\pi i}\int_{(c)}(H-H^R)(s)D(s)^2\,ds. \tag{10}
\]

There are no separate `0` or `1` residues in (10).  Expanding

\[
 (H-H^R)D^2=(H-H^R)(L^2+2gL+g^2)                \tag{11}
\]

shows precisely where the gamma/pole completion re-enters.  A symmetric
kernel makes the whole completed ledger zero; the residues at reflected zero
pairs cancel.  Also

\[
 D^2={\xi''\over\xi}-D',                         \tag{12}
\]

so the simple-zero collapse (3)--(4) persists verbatim in completed form.

## 5. What remains logically possible

The audit rules out this inference:

> positive and denser coefficients of `L^2` + `H(rho)=0` + reflection
> automatically give a stronger sign inequality than the linear prime
> carrier.

An actual advance would have to add a new estimate that does at least one of
the following:

- controls the forced `A L` term in (8) with a strict surplus;
- controls all nonselected quotient residues in (3), including their regular
  Laurent parts;
- uses an asymmetric kernel for which the completed cross and gamma terms in
  (11) have a proved favorable sign or a quantitatively smaller norm.

Without such an estimate, `L^2` repackages the original principal debt rather
than paying it.  No fixed zero-free strip follows from this route as it
currently stands.

