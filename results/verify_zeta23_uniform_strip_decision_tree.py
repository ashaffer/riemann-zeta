#!/usr/bin/env python3
"""Exact checks for the 2026-08-30 uniform-strip decision-tree audit.

The companion report contains the analytic proofs.  This script checks the
exponent arithmetic, the finite tensor-Fejer identities, the balanced-digit
AP bound on a nontrivial fixture, and a small rank-two prime matrix.  Floating
point sampling is not used as proof of a continuum trigonometric statement.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import isqrt


def certify_exponent_ledger() -> dict[str, Fraction]:
    """Check all four localized-carrier thresholds exactly."""

    aperture = Fraction(50, 33)
    delsarte_floor = Fraction(19, 1000)
    transverse_floor = Fraction(179, 10_000)
    quadratic_scale = Fraction(8, 33)

    published = (3 * aperture - 2 + 6 * delsarte_floor) / 11
    localized_range = (2 + 3 * delsarte_floor) / 7
    calibrated_global = (aperture + 2 * delsarte_floor) / 5
    calibrated_local = (1 + delsarte_floor) / 3

    assert published < quadratic_scale < localized_range
    assert localized_range < calibrated_global < calibrated_local

    # Excursion exponents evaluated at theta=8/33.
    published_excursion = (
        aperture / 2 - Fraction(1, 3) - 11 * quadratic_scale / 6
    )
    old_antipode_local_range = (2 - 7 * quadratic_scale) / 3
    calibrated_global_excursion = aperture / 2 - 5 * quadratic_scale / 2
    calibrated_local_excursion = 1 - 3 * quadratic_scale

    assert published_excursion == -Fraction(2, 99)
    assert old_antipode_local_range == Fraction(10, 99)
    assert calibrated_global_excursion == Fraction(5, 33)
    assert calibrated_local_excursion == Fraction(3, 11)
    assert published_excursion < -delsarte_floor
    assert old_antipode_local_range > 0

    return {
        "aperture": aperture,
        "delsarte_floor": delsarte_floor,
        "transverse_floor": transverse_floor,
        "quadratic_scale": quadratic_scale,
        "published_threshold": published,
        "localized_range_threshold": localized_range,
        "calibrated_global_threshold": calibrated_global,
        "calibrated_local_threshold": calibrated_local,
        "published_excursion_at_quadratic_scale": published_excursion,
        "old_antipode_local_excursion": old_antipode_local_range,
        "calibrated_global_excursion": calibrated_global_excursion,
        "calibrated_local_excursion": calibrated_local_excursion,
    }


def longest_ap_length(values: set[int]) -> int:
    """Return the longest increasing arithmetic progression in a finite set."""

    ordered = sorted(values)
    present = set(values)
    best = 1 if ordered else 0
    for start in ordered:
        for second in ordered:
            if second <= start:
                continue
            step = second - start
            if start - step in present:
                continue
            length = 2
            cursor = second + step
            while cursor in present:
                length += 1
                cursor += step
            best = max(best, length)
    return best


def certify_digit_box(n: int = 5, rank: int = 3) -> dict[str, object]:
    """Check the exact autocorrelation ledger on a finite digit-box fixture."""

    if n < 3 or rank < 2:
        raise ValueError("use n>=3 and rank>=2")
    q_base = 10 * n
    box = [0]
    for j in range(rank):
        place = q_base**j
        box = [old + digit * place for old in box for digit in range(n)]

    multiplicity = Counter(a - b for a in box for b in box)
    m = n**rank
    t_n = (2 * n**3 + n) // 3
    assert len(box) == m
    assert multiplicity[0] == m
    assert len(multiplicity) == (2 * n - 1) ** rank
    assert sum(value * value for value in multiplicity.values()) == t_n**rank
    assert all(multiplicity[d] == multiplicity[-d] for d in multiplicity)

    positive = [d for d in multiplicity if d > 0]
    assert sum(multiplicity[d] for d in positive) == m * (m - 1) // 2
    square_sum = sum(multiplicity[d] ** 2 for d in positive)
    assert 2 * square_sum == t_n**rank - m**2

    s_one = Fraction(1, 2)
    energy = Fraction(square_sum, m * m * (m - 1) ** 2)
    participation = s_one * s_one / energy
    height = Fraction(1, 2 * (m - 1))
    expected_participation = Fraction(
        m * m * (m - 1) ** 2,
        2 * (t_n**rank - m**2),
    )
    assert participation == expected_participation
    assert height * participation > Fraction(1, 4)

    difference_support = set(multiplicity)
    ap_length = longest_ap_length(difference_support)
    assert ap_length == 2 * n - 1

    return {
        "n": n,
        "rank": rank,
        "base": q_base,
        "m": m,
        "active_positive_frequencies": len(positive),
        "energy": energy,
        "participation": participation,
        "height": height,
        "height_times_participation": height * participation,
        "longest_ap": ap_length,
    }


def is_prime(value: int) -> bool:
    """Deterministic trial division, sufficient for the tiny fixture below."""

    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def determinant_3(matrix: list[list[int]]) -> int:
    """Exact determinant of a 3 by 3 integer matrix."""

    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def certify_rank_two_prime_fixture() -> dict[str, object]:
    """Show that rank two plus primality is not a local contradiction."""

    values = [199 + 210 * index for index in range(9)]
    assert all(is_prime(value) for value in values)
    matrix = [values[3 * row : 3 * row + 3] for row in range(3)]
    assert determinant_3(matrix) == 0
    assert matrix[0][0] * matrix[1][1] != matrix[0][1] * matrix[1][0]
    assert len(set(values)) == 9
    return {"matrix": matrix, "determinant": 0, "rank": 2}


def certify_tensor_flattening_margin() -> dict[str, Fraction]:
    """Check the determinant-integrality and dimension exponents."""

    aperture = Fraction(50, 33)
    physical_error_exponent = 1 - aperture
    determinant_exponent = 1 + 2 * physical_error_exponent
    assert physical_error_exponent == -Fraction(17, 33)
    assert determinant_exponent == -Fraction(1, 33)
    return {
        "physical_error_exponent": physical_error_exponent,
        "three_by_three_determinant_exponent": determinant_exponent,
    }


def main() -> None:
    ledger = certify_exponent_ledger()
    box = certify_digit_box()
    prime_matrix = certify_rank_two_prime_fixture()
    flattening = certify_tensor_flattening_margin()

    print("quadratic localization scale:", float(ledger["quadratic_scale"]))
    print("published short-carrier threshold:",
          float(ledger["published_threshold"]))
    print("localized-range threshold:",
          float(ledger["localized_range_threshold"]))
    print("calibrated localized threshold:",
          float(ledger["calibrated_local_threshold"]))
    print("digit-box active frequencies:", box["active_positive_frequencies"])
    print("digit-box effective participation:", float(box["participation"]))
    print("digit-box longest AP:", box["longest_ap"])
    print("prime fixture rank:", prime_matrix["rank"])
    print("flattening determinant exponent:",
          flattening["three_by_three_determinant_exponent"])
    print("all decision-tree certificates passed")


if __name__ == "__main__":
    main()
