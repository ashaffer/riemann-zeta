"""run_window.py — one deep-window rung of the spectral (Legendre) ladder.

Usage: python3 run_window.py L m dps_assembly dps_solve [tag]

Drives src/spectral_margins.spectral_form / spectral_lam_min unchanged (no repo
edits).  Each invocation is one single-threaded process; it appends one CSV line
to results/agent-deep-windows/runs.csv (with a portable lockfile against
concurrent appends) and writes a per-run log.  Every lambda produced here is a
Rayleigh-Ritz UPPER bound on the operator margin at that support L.
"""
import os
import sys
import time
import json

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "src"))
sys.path.insert(0, SRC)

import mpmath as mp                                   # noqa: E402
from spectral_margins import spectral_form, spectral_lam_min   # noqa: E402

CSV = os.path.join(HERE, "runs.csv")
LOCK = CSV + ".lock"


def append_csv(line):
    # simple mkdir-based lock, portable and NFS-safe enough for 3 writers
    for _ in range(600):
        try:
            os.mkdir(LOCK)
            break
        except FileExistsError:
            time.sleep(0.1)
    try:
        new = not os.path.exists(CSV)
        with open(CSV, "a") as f:
            if new:
                f.write("L,m,dps_assembly,dps_solve,lam_min,assembly_s,"
                        "solve_s,total_s,finished_utc,tag\n")
            f.write(line + "\n")
    finally:
        try:
            os.rmdir(LOCK)
        except OSError:
            pass


def main():
    L = float(sys.argv[1])
    m = int(sys.argv[2])
    dps_a = int(sys.argv[3])
    dps_s = int(sys.argv[4])
    tag = sys.argv[5] if len(sys.argv) > 5 else ""

    print(f"[run_window] L={L} m={m} dps_assembly={dps_a} dps_solve={dps_s} "
          f"pid={os.getpid()}", flush=True)
    t0 = time.time()
    Q = spectral_form(L, m, dps=dps_a)
    t1 = time.time()
    print(f"[run_window] assembly done in {t1 - t0:.1f} s", flush=True)
    lams = spectral_lam_min(Q, nev=3, dps=dps_s)
    t2 = time.time()
    lam = lams[0]
    lam_str = mp.nstr(lam, 12)
    print(f"[run_window] lam_min = {lam_str}   (bottom 3: "
          f"{[mp.nstr(x, 8) for x in lams]})", flush=True)
    print(f"[run_window] solve {t2 - t1:.1f} s, total {t2 - t0:.1f} s", flush=True)

    stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    append_csv(f"{L},{m},{dps_a},{dps_s},{lam_str},{t1 - t0:.1f},"
               f"{t2 - t1:.1f},{t2 - t0:.1f},{stamp},{tag}")
    # per-run machine-readable record as well
    rec = dict(L=L, m=m, dps_assembly=dps_a, dps_solve=dps_s,
               lam_min=lam_str,
               bottom3=[mp.nstr(x, 10) for x in lams],
               assembly_s=round(t1 - t0, 1), solve_s=round(t2 - t1, 1),
               total_s=round(t2 - t0, 1), finished_utc=stamp, tag=tag,
               bound="Rayleigh-Ritz upper bound")
    with open(os.path.join(HERE, "logs",
                           f"run_L{L}_m{m}_dps{dps_a}-{dps_s}.json"), "w") as f:
        json.dump(rec, f, indent=1)


if __name__ == "__main__":
    main()
