from fractions import Fraction

from qp_parabolic_chart_progression_gate import (
    PrimitiveFaceLedger,
    affine_steps,
    chart_colors,
    common_component_divisor,
    common_x_modulus,
    flat_chart_trace_exponent,
)


def test_common_x_is_one_crt_progression() -> None:
    colors0 = chart_colors(x=103, r1=3, r2=2, s1=5, s2=3, eta=1, theta=1)
    colors1 = chart_colors(x=109, r1=3, r2=2, s1=5, s2=3, eta=1, theta=1)
    assert all(value.denominator == 1 for value in colors0 + colors1)
    assert common_x_modulus(r1=3, r2=2, s1=5, s2=3) == 6
    assert tuple(int(b - a) for a, b in zip(colors0, colors1)) == affine_steps(
        r1=3, r2=2, s1=5, s2=3
    )


def test_common_component_is_forced_into_x() -> None:
    colors = chart_colors(x=100, r1=3, r2=2, s1=5, s2=2, eta=1, theta=1)
    assert all(value.denominator == 1 for value in colors)
    divisor = common_component_divisor(r2=2, s2=2)
    assert divisor == 2
    assert int(colors[0]) % divisor == 0


def test_relocated_face_reuse_ledgers() -> None:
    ledger = PrimitiveFaceLedger()
    assert ledger.chart_count == Fraction(11, 4)
    assert ledger.unrestricted_x_length == Fraction(13, 8)
    assert ledger.actual_x_length == Fraction(19, 16)
    assert ledger.required_principal_matrix_count == Fraction(73, 16)
    assert ledger.unrestricted_matrix_count == Fraction(35, 8)
    assert ledger.actual_matrix_count == Fraction(63, 16)
    assert ledger.flat_trace(actual_prime_powers=False) == Fraction(15, 16)
    assert ledger.flat_trace(actual_prime_powers=True) == Fraction(1, 2)


def test_nonprincipal_residual_is_137_over_128() -> None:
    ledger = PrimitiveFaceLedger()
    assert ledger.nonprincipal_mass == Fraction(97, 128)
    assert ledger.nonprincipal_trace == Fraction(137, 128)


def test_general_flat_formula_matches_actual_critical_face() -> None:
    assert flat_chart_trace_exponent(
        row=Fraction(7, 16),
        column=Fraction(7, 16),
        eta=Fraction(1, 2),
        theta=Fraction(1, 2),
        gcd_height=Fraction(0),
        occupied_lines=Fraction(5, 16),
        support=Fraction(15, 8),
        actual_prime_powers=True,
    ) == Fraction(1, 2)
