"""cue_frame_test.py — pre-registered GUE/Sine2 frame-bound test (log-gas seat).

Predictions P1-P7 locked in results/ias/SEAT-log-gas.md BEFORE this run.
Protocol matches src/model_zeros.py EXPECTED: L=2.485, m=48, first KT=180
points per configuration, orthonormal Legendre frame form via
results/agent-law-theory/law_core.lam_min_frame (dps 50).

Configurations:
  rigid    : staircase_zeros(180)                 [anchor 2.75124e-10]
  true     : true_zeros_cached(180)               [anchor 2.68972e-10]
  poisson  : model_zeros.poisson_zeros(180, seed) seeds 7..11 [seed7 anchor 2.89509e-12]
  cue      : N=256 Haar CUE eigenangles, u = N*theta/2pi sorted, first 180,
             pushed through Nbar^{-1}; seeds 1..10
  cueanch  : same, shifted u -> u - u1 + 1/2; seeds 1..6
  surgery  : staircase minus point sets {2},{3},{5},{8},{2,3},{2,5},{2,8}

Per config: lam, E=-ln lam, dE = E - E_rigid, J = sum_stair ln(X/g) -
sum_cfg ln(X/g) over points < X = e*Tstar, supD = sup |N_cfg - N_stair| on [0,X].

Runs sequentially (1 worker), wall guard 1500 s. Output: JSONL + stdout.
"""
import os, sys, time, json, math

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
sys.path.insert(0, os.path.join(ROOT, "results", "agent-law-theory"))

import numpy as np
import mpmath as mp
from law_core import lam_min_frame, staircase_zeros, true_zeros_cached
from model_zeros import poisson_zeros

mp.mp.dps = 50
L = mp.mpf('2.485')
M = 48
KT = 180
TSTART = time.time()
WALL = 1500.0
OUT = open(os.path.join(HERE, "cue_frame_test.jsonl"), "a")

Tstar = 2 * mp.pi * mp.e ** (L / 2)
X = mp.e * Tstar
Xf = float(X)
PI2H = float(mp.pi ** 2 / 2)   # pi^2/2


def nbar_inv(targets):
    """gamma with Nbar(gamma) = u for each u in targets (increasing),
    Nbar(g) = g/2pi ln(g/2pi e) + 7/8. Same Newton as model_zeros."""
    out = []
    g = mp.mpf(14)
    for u in targets:
        t = mp.mpf(float(u)) - mp.mpf('0.875')
        for _ in range(60):
            f = g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) - t
            fp = mp.log(g / (2 * mp.pi)) / (2 * mp.pi)
            step = f / fp
            g = g - step
            if abs(step) < mp.mpf('1e-30'):
                break
        out.append(+g)
    return out


def cue_u(N, seed):
    rng = np.random.default_rng(seed)
    A = (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))) / np.sqrt(2)
    Q, R = np.linalg.qr(A)
    Q = Q * (np.diag(R) / np.abs(np.diag(R)))
    ang = np.mod(np.angle(np.linalg.eigvals(Q)) + rng.uniform(0, 2 * np.pi), 2 * np.pi)
    ang.sort()
    return ang * N / (2 * np.pi)


def J_and_D(cfg, stair):
    """J = sum_stair ln(X/g) - sum_cfg ln(X/g) over points < X;
    supD = sup |N_cfg - N_stair| on (0, X)."""
    c = sorted(float(g) for g in cfg if float(g) < Xf)
    s = sorted(float(g) for g in stair if float(g) < Xf)
    J = sum(math.log(Xf / g) for g in s) - sum(math.log(Xf / g) for g in c)
    pts = sorted(set(c) | set(s))
    supD = 0.0
    for p in pts:
        for eps in (1e-9,):
            nc = sum(1 for g in c if g <= p + eps)
            ns = sum(1 for g in s if g <= p + eps)
            supD = max(supD, abs(nc - ns))
    return J, supD


E_RIGID = None


def run(tag, cfg, stair, extra=None):
    global E_RIGID
    t0 = time.time()
    lam = lam_min_frame(cfg, L, M, dps=50)[0]
    E = -mp.log(lam)
    J, supD = J_and_D(cfg, stair)
    dE = float(E - E_RIGID) if E_RIGID is not None else 0.0
    rec = {"tag": tag, "lam": mp.nstr(lam, 8), "E": float(E), "dE": dE,
           "J": J, "pi2h_J": PI2H * J, "supD": supD,
           "npts": len(cfg), "secs": round(time.time() - t0, 1)}
    if extra:
        rec.update(extra)
    OUT.write(json.dumps(rec) + "\n"); OUT.flush()
    print("%-14s lam=%-14s E=%8.3f dE=%+7.3f  (pi2/2)J=%+7.3f supD=%.1f  (%.0fs)"
          % (tag, rec["lam"], rec["E"], dE, PI2H * J, supD, rec["secs"]), flush=True)
    return E, lam


def left():
    return WALL - (time.time() - TSTART)


print("=== pre-registered CUE frame test; L=%s m=%d KT=%d X=eT*=%.4f ==="
      % (mp.nstr(L, 5), M, KT, Xf), flush=True)

# exact quadratures for the locked Var estimates (report only)
rho = lambda s: math.log(s / (2 * math.pi)) / (2 * math.pi)
ss = np.linspace(2 * math.pi + 1e-9, Xf, 20001)
varJP = np.trapz([math.log(Xf / s) ** 2 * max(rho(s), 0.0) for s in ss], ss)
print("quadrature Var J(Poisson from 2pi) = %.3f -> sigma_lin = %.2f nats"
      % (varJP, PI2H * math.sqrt(varJP)), flush=True)

# --- block A: anchors ---
stair = staircase_zeros(KT)
E_RIGID, lam_r = run("rigid", stair, stair)
print("  anchor rigid: expect 2.75124e-10", flush=True)
tz = true_zeros_cached(KT)
run("true", tz, stair)
print("  anchor true: expect 2.68972e-10", flush=True)
po7 = poisson_zeros(KT, seed=7)
run("poisson7", po7, stair)
print("  anchor poisson7: expect 2.89509e-12", flush=True)

# --- block B: free CUE seeds 1..10 ---
for seed in range(1, 11):
    if left() < 200: print("WALL GUARD: stopping CUE at seed", seed); break
    us = cue_u(256, seed)[:KT]
    cfg = nbar_inv(us)
    run("cue%d" % seed, cfg, stair, {"u1": float(us[0])})

# --- block C: anchored CUE seeds 1..6 ---
for seed in range(1, 7):
    if left() < 150: print("WALL GUARD: stopping anchored at seed", seed); break
    us = cue_u(256, seed)[:KT]
    us = us - us[0] + 0.5
    cfg = nbar_inv(us)
    run("cueanch%d" % seed, cfg, stair, {"u1": float(us[0])})

# --- block D: extra Poisson seeds ---
for seed in range(8, 12):
    if left() < 120: print("WALL GUARD: stopping poisson at seed", seed); break
    cfg = poisson_zeros(KT, seed=seed)
    run("poisson%d" % seed, cfg, stair)

# --- block E: surgeries (LG-4 / P6) ---
def minus(idxs):
    return [g for i, g in enumerate(stair, 1) if i not in idxs]

surg = [({2}, "del2"), ({3}, "del3"), ({5}, "del5"), ({8}, "del8"),
        ({2, 3}, "del23"), ({2, 5}, "del25"), ({2, 8}, "del28")]
for idxs, tag in surg:
    if left() < 60: print("WALL GUARD: stopping surgeries at", tag); break
    run(tag, minus(idxs), stair, {"deleted": sorted(idxs)})

print("total wall: %.0fs" % (time.time() - TSTART), flush=True)
OUT.close()
