"""transport_check.py — post-hoc (NOT pre-registered) marginal-law transport
check for the beta-dial results; see SEAT-magic-functions.md §5.1.
Prediction: d(ln lam)/d beta = (pi^2/2) * sum_{t_k <= eT*} 1/(t_k N'(t_k)).
Output (2026-07-26): S = 1.72639; 0.25->0.75 pred 4.260 vs meas 4.068 (0.955);
0.10->0.90 pred 6.815 vs meas 6.644 (0.975); beta_eff(true) = 0.5034.
"""
import mpmath as mp
mp.mp.dps = 30
pi = mp.pi
L = mp.mpf('2.485'); ell = L / 2
Tstar = 2 * pi * mp.e**ell; eTstar = mp.e * Tstar

def Np(t):
    return mp.log(t / (2 * pi)) / (2 * pi)

def stair(K, beta):
    out = []; g = mp.mpf(14)
    for k in range(1, K + 1):
        target = k - beta - mp.mpf('0.875')
        for _ in range(60):
            f = g / (2 * pi) * mp.log(g / (2 * pi * mp.e)) - target
            fp = mp.log(g / (2 * pi)) / (2 * pi)
            g -= f / fp
            if abs(f / fp) < mp.mpf('1e-25'):
                break
        out.append(+g); g += 2 * pi / mp.log(g / (2 * pi))
    return out

ts = [t for t in stair(30, mp.mpf('0.5')) if t <= eTstar]
S = sum(1 / (t * Np(t)) for t in ts)
print("#nodes<=eT* =", len(ts), " S =", mp.nstr(S, 6))
c = pi**2 / 2
meas = {0.10: mp.mpf('1.6499402e-11'), 0.25: mp.mpf('4.8378669e-11'),
        0.50: mp.mpf('3.286116e-10'), 0.60: mp.mpf('7.4927933e-10'),
        0.75: mp.mpf('2.8262843e-9'), 0.90: mp.mpf('1.2674317e-8')}
for b1, b2 in [(0.25, 0.75), (0.10, 0.90)]:
    pred = c * (b2 - b1) * S
    m = mp.log(meas[b2] / meas[b1])
    print("beta %.2f->%.2f: pred %.3f nats, meas %.3f, ratio %.3f" % (b1, b2, pred, m, m / pred))
slope = mp.log(meas[0.60] / meas[0.50]) / mp.mpf('0.1')
print("beta_eff(true) = 0.5 + %.4f" % (mp.log(mp.mpf('3.3801166e-10') / meas[0.50]) / slope))
