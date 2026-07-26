"""runs.py — shared runner: one frame job -> one json line (append-only).

Every record carries the full convergence context (m, Gcut, dps, K) and the
semantics reminder: lam is a LOWER bound in Gcut (truncation deletes positive
rank-ones) and, at fixed Gcut, a Galerkin minimum over the m-dim Legendre
space (so an UPPER bound for that truncated operator, decreasing in m).
"""
import os, json, time
import mpmath as mp
from law_core import lam_min_frame

_HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(_HERE, "data")
os.makedirs(DATA, exist_ok=True)


def record(path, tag, gammas, L, m, dps=50, extra=None):
    """Run lam_min_frame and append a json record.  Returns lam (mpf)."""
    t0 = time.time()
    lam = lam_min_frame(gammas, L, m, dps=dps)[0]
    rec = {
        "tag": tag,
        "L": float(L),
        "m": int(m),
        "K": len(gammas),
        "gmax": float(max(gammas)) if gammas else 0.0,
        "dps": int(dps),
        "lam": mp.nstr(lam, 12),
        "lnlam": float(mp.log(lam)) if lam > 0 else None,
        "secs": round(time.time() - t0, 1),
    }
    if extra:
        rec.update(extra)
    with open(os.path.join(DATA, path), "a") as f:
        f.write(json.dumps(rec) + "\n")
    print("[%s] %s L=%.4g m=%d K=%d -> lam=%s (%.0fs)"
          % (path, tag, L, m, len(gammas), mp.nstr(lam, 6), rec["secs"]),
          flush=True)
    return lam
