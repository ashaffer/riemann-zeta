#!/usr/bin/env python3
"""Replay the closed-form signed-kernel capacity ledger."""

from __future__ import annotations

import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qp_signed_kernel_capacity_gate import (  # noqa: E402
    audit_signed_kernel,
    chebyshev_log_resonant_bound,
    chebyshev_theta,
    turan_vertical_envelope_floor,
)


def main() -> None:
    a0, a1, width = 0.001, 0.019, 0.2
    xi = (a1 * a1 + a0 * a0) / (a1 * a1 - a0 * a0)
    assert math.isclose(chebyshev_theta(a0, a1), math.acosh(xi))
    assert turan_vertical_envelope_floor(width) == 10.0

    audit = audit_signed_kernel(1000.0, 0.019, a0, a1, width)
    assert audit.resonant_log_bound <= -19.0
    assert chebyshev_log_resonant_bound(
        audit.order - 1, a0, a1, width
    ) > -19.0
    assert audit.spike_log_value > 1000.0
    print(
        "signed-kernel capacity gate verified: "
        f"order={audit.order}, "
        f"resonant_log_bound={audit.resonant_log_bound:.6f}, "
        f"spike_log={audit.spike_log_value:.6f}, "
        f"vertical_floor={audit.vertical_envelope_floor:.6f}"
    )


if __name__ == "__main__":
    main()

