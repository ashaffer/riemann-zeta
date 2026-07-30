"""Arb certificate driver for the unrestricted n=4 window at L=749/250.

This is the three-prime-power analogue of
``fullinf_unrestricted_p3_certificate.py``.  It is a separate driver so the
already stable certificates remain untouched.  The prime-power sum contains
exactly n=2,3,4 because log(4)<L/2<log(5), checked below with Arb.

The exterior cutoff is sharpened beyond the crude absolute-cosine envelope.
Direct Arb evaluation on 50,000 exact panels proves Omega(r)>=29/100 on
[110,160].  For |r|>=160, monotonicity of Re psi and |cos|<=1 give the same
bound because D(160)-C_L>29/100.  Evenness handles the negative half-line.

The script encloses the clipped 132-dimensional normalized-Legendre matrix,
tries a descending exact beta ladder beginning at 1e-15 by interval Cholesky,
and checks the full-space two-by-two transfer at gamma=beta-1e-17.  The
first complete run took 1,040.12 seconds with 12 worker processes.  Its
outward checkpoint is committed at the default path; a cached rerun rebuilds
the matrix and certificate in about 1.3 seconds.  A source file without a
complete, validated checkpoint would still be only a driver.

The real calculation extends to the complexification because the multiplier,
projection, and pole operator have real kernels and the Hermitian form splits
over real and imaginary parts.  All transcendental, quadrature, and matrix
enclosures use python-flint/Arb; no prior matrix is imported.

EXPECTED (2026-07-27, python-flint 0.9.0 / FLINT 3.6.0, 192 bits):

    checkpoint entries              4422
    checkpoint SHA-256              7591f662b1c1a79ed83cb6999881d8fa
                                       ce43836dec1131ccff8d56d6bdf7354f
    smallest shifted pivot          0.000788320717613812...
    lambda_min(A_132)               > 1e-15
    rho                              1.51610795895455e-20
    shifted 2x2 determinant         1.77760228280182e-18
    inf Q_(749/250)                  > 9.9e-16
"""

import argparse
import hashlib
import inspect
import json
from math import factorial, prod
from multiprocessing import get_context
from pathlib import Path
from time import time

from flint import acb, arb, ctx, fmpq

from arb_fullinf_certificate import (
    interval_cholesky,
    require_gt,
    require_lt,
    spherical_i,
)


PRECISION = 192
ABS_TOL_BITS = 105
M = 132
S = 110
ENVELOPE_START = 160
PANEL_DENOMINATOR = 1000
SERIAL_DECIMAL_DIGITS = 80
DEFAULT_CHECKPOINT = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "fullinf_n4_M132_S110_entries.jsonl"
)

ctx.prec = PRECISION
ctx.threads = 1


def Q(n, d=1):
    return fmpq(n, d)


def A(x):
    return arb(x)


BETA_CANDIDATES = [
    Q(1, 10**15),
    Q(9, 10**16),
    Q(8, 10**16),
    Q(5, 10**16),
    Q(2, 10**16),
    Q(1, 10**16),
]


L = Q(749, 250)
A_HALF_WIDTH = Q(749, 1000)
HALF_SUPPORT = 2 * A_HALF_WIDTH
PI = arb.pi()
LOG2 = A(2).log()
LOG3 = A(3).log()
PRIME_2 = A(2).sqrt() * LOG2
PRIME_3 = 2 * LOG3 / A(3).sqrt()
PRIME_4 = LOG2
PRIME_AMPLITUDE = PRIME_2 + PRIME_3 + PRIME_4
I = acb(0, 1)
ALPHA = A(Q(29, 100))
CRUDE_FLOOR_AT_ENVELOPE_START = (
    acb(Q(1, 4), A(ENVELOPE_START) / 2).digamma().real
    - PI.log()
    - PRIME_AMPLITUDE
)
TOLERANCE = A(2) ** (-ABS_TOL_BITS)


def omega(z):
    """Holomorphic symmetrization of the n=2,3,4 Weil symbol."""
    plus = (acb(Q(1, 4)) + I * z / 2).digamma()
    minus = (acb(Q(1, 4)) - I * z / 2).digamma()
    return (
        (plus + minus) / 2
        - PI.log()
        - PRIME_2 * (z * LOG2).cos()
        - PRIME_3 * (z * LOG3).cos()
        - PRIME_4 * (2 * z * LOG2).cos()
    )


_ODD_DOUBLE_FACTORIAL = [prod(range(1, 2 * k + 2, 2)) for k in range(M)]


def spherical_j_series(k, r):
    """Entire spherical-j formula on the first panel containing zero."""
    z = A(A_HALF_WIDTH) * r
    return (
        z**k / _ODD_DOUBLE_FACTORIAL[k]
        * (-z * z / 4).hypgeom_0f1(Q(2 * k + 3, 2))
    )


def spherical_j_bessel(k, r, analytic):
    """Spherical j_k through Arb's Bessel J on positive panels."""
    z = A(A_HALF_WIDTH) * r
    return (
        z.bessel_j(Q(2 * k + 1, 2))
        * (PI / (2 * z)).sqrt(analytic=analytic)
    )


def spherical_j_elementary(k, r):
    """Stable sin/cos recurrence when the argument exceeds the order."""
    z = A(A_HALF_WIDTH) * r
    j0 = z.sin() / z
    if k == 0:
        return j0
    j1 = z.sin() / (z * z) - z.cos() / z
    for n in range(1, k):
        j0, j1 = j1, (2 * n + 1) * j1 / z - j0
    return j1


def spherical_j_panel(k, r, analytic, left):
    """Choose a stable exact representation on one positive unit panel.

    Upward recurrence is stable below the turning point (order <= argument).
    Arb's Bessel J is used above it.  The 0F1 representation is reserved for
    the first panel near zero: despite being an exact identity, its alternating
    cancellation becomes expensive on some high-frequency regular panels.
    """
    if k <= A_HALF_WIDTH * left:
        return spherical_j_elementary(k, r)
    return spherical_j_bessel(k, r, analytic)


def band_integral(k, j):
    """Enclose integral_0^S (Omega-alpha)j_k(ar)j_j(ar)dr."""

    def first_panel(r, _analytic):
        return (
            (omega(r) - ALPHA)
            * spherical_j_series(k, r)
            * spherical_j_series(j, r)
        )

    result = acb.integral(
        first_panel,
        0,
        1,
        abs_tol=TOLERANCE,
        rel_tol=TOLERANCE,
        deg_limit=80,
        eval_limit=100_000,
        depth_limit=25,
    )
    if not result.is_finite():
        raise ArithmeticError(f"non-finite first-panel integral ({k}, {j})")
    for left in range(1, S):
        def regular_panel(r, analytic):
            return (
                (omega(r) - ALPHA)
                * spherical_j_panel(k, r, analytic, left)
                * spherical_j_panel(j, r, analytic, left)
            )

        panel = acb.integral(
            regular_panel,
            left,
            left + 1,
            abs_tol=TOLERANCE,
            rel_tol=TOLERANCE,
            deg_limit=80,
            eval_limit=100_000,
            depth_limit=25,
        )
        if not panel.is_finite():
            raise ArithmeticError(
                f"non-finite integral for ({k}, {j}) on [{left},{left + 1}]"
            )
        result += panel
    if not result.imag.contains(0):
        raise ArithmeticError(f"real-path integral ({k}, {j}) excludes reality")
    return result.real


def serialize_ball(value):
    """Return Arb's documented decimal enclosure triple using plain integers.

    ``mid_rad_10exp`` guarantees that ``value`` is contained in
    ``[mid +/- rad] * 10**exp``.  Converting the FLINT integers to decimal
    strings makes the worker result safely pickleable without treating a
    printed midpoint as exact.
    """
    mid, rad, exponent = value.mid_rad_10exp(SERIAL_DECIMAL_DIGITS)
    return str(mid), str(rad), int(exponent)


def deserialize_ball(data):
    """Reconstruct an outward Arb enclosure from ``serialize_ball`` data."""
    mid_string, rad_string, exponent = data
    mid = int(mid_string)
    rad = int(rad_string)
    if exponent >= 0:
        scale = 10**exponent
        midpoint = Q(mid * scale)
        radius = Q(rad * scale)
    else:
        scale = 10 ** (-exponent)
        midpoint = Q(mid, scale)
        radius = Q(rad, scale)
    return arb(midpoint, radius)


def band_integral_worker(pair):
    """Pickle-safe independent worker for one indexed matrix integral."""
    k, j = pair
    return k, j, serialize_ball(band_integral(k, j))


def cache_kernel_source_sha256():
    """Bind cached raw integrals to the code that defines their integrand.

    Matrix normalization, pole assembly, Cholesky, and the full-space transfer
    are deliberately not cached and are rerun on every replay.  Their source
    need not invalidate these raw band-integral enclosures.
    """
    functions = (
        omega,
        spherical_j_series,
        spherical_j_bessel,
        spherical_j_elementary,
        spherical_j_panel,
        band_integral,
    )
    source = "\n\n".join(inspect.getsource(function) for function in functions)
    return hashlib.sha256(source.encode("utf-8")).hexdigest()


def checkpoint_metadata():
    return {
        "version": 2,
        "L": str(L),
        "M": M,
        "S": S,
        "alpha": "29/100",
        "precision": PRECISION,
        "abs_tol_bits": ABS_TOL_BITS,
        "method": "elementary-below-turning-point-bessel-above",
        "integrand": "zeta-n2-n3-n4-clipped-at-29/100",
        "kernel_source_sha256": cache_kernel_source_sha256(),
        "serial_decimal_digits": SERIAL_DECIMAL_DIGITS,
    }


def load_checkpoint(path, valid_pairs):
    """Load rigor-preserving serialized entries from a JSONL checkpoint."""
    path = Path(path)
    if not path.exists() or path.stat().st_size == 0:
        return {}
    valid = set(valid_pairs)
    entries = {}
    with path.open("r", encoding="utf-8") as handle:
        first = handle.readline()
        if not first:
            return {}
        header = json.loads(first)
        if header.get("meta") != checkpoint_metadata():
            raise ArithmeticError(f"checkpoint metadata mismatch: {path}")
        for line_number, line in enumerate(handle, start=2):
            if not line.strip():
                continue
            item = json.loads(line)
            pair = (int(item["k"]), int(item["j"]))
            if pair not in valid:
                raise ArithmeticError(
                    f"invalid checkpoint pair {pair} on line {line_number}"
                )
            if pair in entries:
                raise ArithmeticError(
                    f"duplicate checkpoint pair {pair} on line {line_number}"
                )
            data = tuple(item["ball"])
            # Parse now so a corrupted enclosure fails before expensive work.
            deserialize_ball(data)
            entries[pair] = data
    return entries


def open_checkpoint(path):
    """Open a checkpoint for append, creating its exact metadata header."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists() and path.stat().st_size > 0
    handle = path.open("a", encoding="utf-8")
    if not exists:
        handle.write(json.dumps({"meta": checkpoint_metadata()}, sort_keys=True))
        handle.write("\n")
        handle.flush()
    return handle


def append_checkpoint(handle, k, j, data):
    if handle is None:
        return
    handle.write(
        json.dumps(
            {"k": k, "j": j, "ball": list(data)},
            separators=(",", ":"),
        )
        + "\n"
    )
    handle.flush()


def clipped_matrix(verbose=True, workers=1, checkpoint_path=None):
    """Assemble the clipped form in the normalized Legendre basis."""
    matrix = [[A(0) for _ in range(M)] for _ in range(M)]
    normalization = [
        (2 * A(A_HALF_WIDTH) * (2 * k + 1)).sqrt()
        for k in range(M)
    ]
    pairs = [
        (k, j)
        for k in range(M)
        for j in range(k, M)
        if (k + j) % 2 == 0
    ]
    serialized_entries = (
        load_checkpoint(checkpoint_path, pairs) if checkpoint_path else {}
    )
    band_entries = {
        pair: deserialize_ball(data)
        for pair, data in serialized_entries.items()
    }
    missing_pairs = [pair for pair in pairs if pair not in band_entries]
    if verbose and band_entries:
        print(
            f"loaded {len(band_entries)}/{len(pairs)} checkpointed entries",
            flush=True,
        )
    checkpoint_handle = (
        open_checkpoint(checkpoint_path) if checkpoint_path else None
    )
    started = time()
    try:
        if workers == 1:
            for count, (k, j) in enumerate(missing_pairs, start=1):
                value = band_integral(k, j)
                data = serialize_ball(value)
                band_entries[k, j] = deserialize_ball(data)
                append_checkpoint(checkpoint_handle, k, j, data)
                if verbose and count % 50 == 0:
                    print(
                        f"integrated {len(serialized_entries) + count}/"
                        f"{len(pairs)} entries",
                        flush=True,
                    )
        else:
            # Separate processes avoid Python-callback thread-safety issues in
            # acb_calc.  Indexed results are assembled deterministically below.
            with get_context("fork").Pool(workers) as pool:
                results = pool.imap_unordered(
                    band_integral_worker,
                    missing_pairs,
                    chunksize=1,
                )
                for count, (k, j, data) in enumerate(results, start=1):
                    band_entries[k, j] = deserialize_ball(data)
                    append_checkpoint(checkpoint_handle, k, j, data)
                    if verbose and count % 100 == 0:
                        print(
                            f"integrated {len(serialized_entries) + count}/"
                            f"{len(pairs)} entries in {time() - started:.1f}s",
                            flush=True,
                        )
    finally:
        if checkpoint_handle is not None:
            checkpoint_handle.close()

    for k, j in pairs:
        phase = (-1) ** ((j - k) // 2)
        entry = (
            phase
            * normalization[k]
            * normalization[j]
            / PI
            * band_entries[k, j]
        )
        if k == j:
            entry += ALPHA
        matrix[k][j] = matrix[j][k] = entry

    pole_vector = [
        normalization[k] * spherical_i(k, A_HALF_WIDTH / 2)
        for k in range(M)
    ]
    for k in range(M):
        for j in range(M):
            if (k + j) % 2 == 0:
                matrix[k][j] += (
                    pole_vector[k]
                    * pole_vector[j]
                    * ((-1) ** j + (-1) ** k)
                )
    return matrix


def exterior_checks():
    """Certify support decisions and Omega>=alpha outside [-S,S]."""
    if not LOG2 < A(HALF_SUPPORT):
        raise ArithmeticError("failed to prove n=2 is present")
    if not LOG3 < A(HALF_SUPPORT):
        raise ArithmeticError("failed to prove n=3 is present")
    if not A(4).log() < A(HALF_SUPPORT):
        raise ArithmeticError("failed to prove n=4 is present")
    if not A(5).log() > A(HALF_SUPPORT):
        raise ArithmeticError("failed to prove every n>=5 is absent")
    require_gt(
        CRUDE_FLOOR_AT_ENVELOPE_START,
        Q(29, 100),
        "crude exterior floor at r=160",
    )

    count = (ENVELOPE_START - S) * PANEL_DENOMINATOR
    denominator = 2 * PANEL_DENOMINATOR
    worst = None
    worst_panel = None
    for k in range(count):
        numerator = 2 * S * PANEL_DENOMINATOR + 2 * k + 1
        r = arb(Q(numerator, denominator), Q(1, denominator))
        gap = omega(r).real - ALPHA
        require_gt(gap, Q(0), f"exterior bridge panel {k}")
        if worst is None or gap.lower() < worst.lower():
            worst = gap
            worst_panel = k
    return worst_panel, worst


def certify_finite_core(verbose=True, workers=1, checkpoint_path=None):
    worst_panel, worst_gap = exterior_checks()
    print(
        "exterior bridge worst panel",
        worst_panel,
        worst_gap.str(20, radius=True),
        flush=True,
    )
    started = time()
    matrix = clipped_matrix(
        verbose=verbose,
        workers=workers,
        checkpoint_path=checkpoint_path,
    )
    assembly_seconds = time() - started
    failures = []
    for beta in BETA_CANDIDATES:
        try:
            pivots = interval_cholesky(matrix, [Q(1)] * M, beta=beta)
            return matrix, pivots, beta, assembly_seconds
        except ArithmeticError as error:
            failures.append(f"beta={beta}: {error}")
            if verbose:
                print("Cholesky candidate failed", failures[-1], flush=True)
    raise ArithmeticError("no beta candidate passed; " + "; ".join(failures))


def full_space_transfer(beta):
    """Certify Legendre leakage and the shifted two-by-two transfer."""
    a = A_HALF_WIDTH
    z = a * S
    geometric_ratio = z * z / ((2 * M + 1) * (2 * M + 3))
    if not geometric_ratio < 1:
        raise ArithmeticError("exact Bessel-tail ratio is not below one")
    odd_double_factorial = prod(range(1, 2 * M + 2, 2))
    first_tail_term = (
        (2 * M + 1) * z ** (2 * M) / odd_double_factorial**2
    )
    b_star = first_tail_term / (1 - geometric_ratio)
    rho = 2 * A(a) * S / PI * A(b_star)

    delta = (
        (2 * A(a)).sqrt()
        * (A(a) / 2).exp()
        * A((a / 2) ** M)
        / factorial(M)
    )
    sinh_a = (A(a).exp() - (-A(a)).exp()) / 2
    pole_norm = (2 * sinh_a).sqrt()
    kappa = arb.const_euler() + PI / 2 + 3 * LOG2 + PI.log()
    # On the band, D(0)-C-alpha = -(kappa+C+alpha).  Monotonicity and
    # S<ENVELOPE_START give the other direction as
    # D(160)+C-alpha = 2C+(crude_floor-alpha), which the two checks below
    # place strictly below the same multiplier_bound.
    multiplier_bound = kappa + PRIME_AMPLITUDE + ALPHA
    require_gt(
        multiplier_bound - 2 * PRIME_AMPLITUDE,
        Q(2),
        "gap between M_bound and the upper symbol direction",
    )
    require_lt(
        CRUDE_FLOOR_AT_ENVELOPE_START - ALPHA,
        Q(2),
        "residual upper symbol allowance",
    )
    d = ALPHA - multiplier_bound * rho - 2 * delta * delta
    c = multiplier_bound * rho.sqrt() + 2 * pole_norm * delta

    require_lt(rho, Q(152, 10**22), "Legendre band defect rho")
    require_lt(delta, Q(8, 10**281), "one-sign pole residual delta")
    require_lt(multiplier_bound, Q(8605, 1000), "band multiplier bound")
    require_gt(d, Q(289, 1000), "complement diagonal d")
    require_lt(c, Q(106, 10**11), "low/high coupling c")

    gamma = beta - Q(1, 10**17)
    if not beta > gamma:
        raise ArithmeticError("finite beta does not exceed full target gamma")
    determinant = A(beta - gamma) * (d - A(gamma)) - c * c
    require_gt(d - A(gamma), Q(289, 1000), "shifted complement diagonal")
    require_gt(determinant, Q(17, 10**19), "2x2 shifted determinant")
    return {
        "q": geometric_ratio,
        "B_star": b_star,
        "rho": rho,
        "delta": delta,
        "multiplier_bound": multiplier_bound,
        "d": d,
        "c": c,
        "gamma": gamma,
        "determinant": determinant,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="independent Arb integration worker processes (default: 1)",
    )
    parser.add_argument(
        "--checkpoint",
        type=Path,
        default=DEFAULT_CHECKPOINT,
        help=f"resumable JSONL entry checkpoint (default: {DEFAULT_CHECKPOINT})",
    )
    args = parser.parse_args()
    if args.workers < 1:
        parser.error("--workers must be positive")
    print("alpha", ALPHA.str(30, radius=True), flush=True)
    print("integration workers", args.workers, flush=True)
    print("entry checkpoint", args.checkpoint, flush=True)
    clipped, pivot_lowers, beta, seconds = certify_finite_core(
        workers=args.workers,
        checkpoint_path=args.checkpoint,
    )
    print(f"assembly seconds {seconds:.2f}")
    print("smallest shifted Cholesky pivot", min(pivot_lowers).str(25))
    print("last shifted Cholesky pivot", pivot_lowers[-1].str(25))
    print("A00", clipped[0][0].str(25, radius=True))
    print("A131,131", clipped[131][131].str(25, radius=True))
    print(
        "ARBITRARY-PRECISION BALL CERTIFIED: lambda_min(A_132) >",
        A(beta).str(18, radius=False),
    )
    transfer = full_space_transfer(beta)
    print("Bessel geometric ratio", transfer["q"])
    print("B_star", A(transfer["B_star"]).str(18, radius=True))
    print("rho", transfer["rho"].str(18, radius=True))
    print("pole residual delta", transfer["delta"].str(18, radius=True))
    print("multiplier bound M", transfer["multiplier_bound"].str(18, radius=True))
    print("complement diagonal d", transfer["d"].str(18, radius=True))
    print("coupling c", transfer["c"].str(18, radius=True))
    print("shifted 2x2 determinant", transfer["determinant"].str(18, radius=True))
    print("ANALYTIC INPUT: monotonicity of Re psi(1/4+ir/2) in |r|")
    print(
        "ARBITRARY-PRECISION BALL CERTIFIED: inf Q_(749/250) >",
        A(transfer["gamma"]).str(18, radius=False),
    )
