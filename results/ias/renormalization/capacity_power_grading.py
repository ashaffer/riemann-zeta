"""Capacity endpoint for power-law gradings (R3(i) of SEAT-renormalization.md).

For density rho_kappa(t) = (a/pi)(t/T*)^kappa the balayage identity
"super-Nyquist surplus on [T*, t_cap] = deficit mass on [0, T*]" gives
exactly  t_cap = (1+kappa)^{1/kappa} * T*,  which -> e*T* as kappa -> 0
(the measured zeta/RvM capacity height) and = 2*T* at kappa = 1 (the
hyperbolic-surface Weyl grading).  Numerical verification below.
"""
import mpmath as mp

mp.mp.dps = 30
for kap in ['1', '0.5', '0.25', '0.001']:
    k = mp.mpf(kap)
    eta = (1 + k) ** (1 / k)
    deficit = k / (k + 1)                       # int_0^1 (1 - t^k) dt
    surplus = mp.quad(lambda t: t**k - 1, [1, eta])
    print('kappa=%s  eta=%s  deficit=%s  surplus=%s'
          % (kap, mp.nstr(eta, 8), mp.nstr(deficit, 8), mp.nstr(surplus, 8)))
print('kappa->0 limit of eta:', mp.nstr(mp.limit(lambda k: (1 + k)**(1 / k), 0), 8),
      '( = e: the log-grading capacity e*T* )')
