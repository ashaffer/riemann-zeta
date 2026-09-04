from fractions import Fraction
from math import gcd

from qp_iterated_euclidean_rebranch_ledger import (
    ANTEDB_BETA_PIECES,
    advance_on_rebranch_fibre,
    antedb_beta_bound,
    antedb_local_beta_top_power,
    bounded_type_envelope_fibre_power,
    bourgain_two_line_beta_budget,
    full_rectangle_fibre_lower_count_power,
    in_bourgain_two_line_beta_polytope,
    in_primitive_second_polytope,
    in_primitive_third_polytope,
    primitive_rebranch_polytope_ledger,
    primitive_rebranch_vector,
    primitive_second_degree_interval,
    primitive_third_degree_interval,
    rebranch_fibre_label,
    saturated_fibre_power,
)


def test_primitive_fibre_label_and_saturation_identity() -> None:
    host, step = 101, 37
    # (p,m) is primitive even though the ambient coordinates (p,r) need
    # not be tested for primitivity.
    vector = primitive_rebranch_vector(host, step, 11, 4)
    assert vector.remainder == 3
    defect, wrap = 7, 2
    completion = step * defect - host * wrap
    label = rebranch_fibre_label(vector, defect, completion)
    for amount in range(-5, 6):
        moved = advance_on_rebranch_fibre(
            vector, defect, completion, amount
        )
        assert rebranch_fibre_label(vector, *moved) == label

    # The two vertical lattice directions are primitive as well.  They are
    # exponent-trivial, but the saturation criterion must not exclude them.
    vertical = primitive_rebranch_vector(host, step, 0, 1)
    assert vertical.remainder == -host
    vertical_label = rebranch_fibre_label(vertical, defect, completion)
    for amount in range(-2, 3):
        moved = advance_on_rebranch_fibre(
            vertical, defect, completion, amount
        )
        assert moved[0] == defect
        assert rebranch_fibre_label(vertical, *moved) == vertical_label

    horizontal = primitive_rebranch_vector(host, step, host, step)
    assert horizontal.remainder == 0
    horizontal_label = rebranch_fibre_label(horizontal, defect, completion)
    for amount in (-1, 0, 1):
        moved = advance_on_rebranch_fibre(
            horizontal, defect, completion, amount
        )
        assert moved[1] == completion
        assert rebranch_fibre_label(horizontal, *moved) == horizontal_label


def test_continued_fraction_determinant_identity() -> None:
    # Consecutive reduced approximants (m0/p0,m1/p1) have determinant one.
    host, step = 89, 34
    p0, m0 = 5, 2
    p1, m1 = 8, 3
    assert abs(p0 * m1 - p1 * m0) == 1
    r0 = step * p0 - host * m0
    r1 = step * p1 - host * m1
    assert abs(p0 * r1 - p1 * r0) == host


def test_later_convergent_construction_has_large_first_remainder() -> None:
    # A finite instance of (4.4)--(4.8).  The asymptotic proof only uses the
    # same congruence, coprimality, and Legendre inequality.
    p, r, n = 101, 1009, 40
    host = 10_000_058
    assert (host * n + r) % p == 0
    step = (host * n + r) // p
    assert gcd(host, r) == gcd(host, step) == gcd(p, n) == 1
    assert step * p - host * n == r
    assert 2 * p * r < host
    first_remainder = min(host % step, step - host % step)
    assert step > host // 3
    assert first_remainder > host // 10

    # Replay the continued fraction and verify that n/p is a convergent.
    numerator, denominator = step, host
    partial_quotients = []
    while denominator:
        partial_quotients.append(numerator // denominator)
        numerator, denominator = denominator, numerator % denominator
    old_num, num = 0, 1
    old_den, den = 1, 0
    convergents = set()
    for quotient in partial_quotients:
        old_num, num = num, quotient * num + old_num
        old_den, den = den, quotient * den + old_den
        convergents.add((num, den))
    assert (n, p) in convergents


def test_general_polytopes_are_equivalent_to_nonempty_degree_intervals() -> None:
    samples = [
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(3, 4), Fraction(27, 32)),
        (Fraction(1, 2), Fraction(13, 12)),
        (Fraction(0), Fraction(1, 2)),
        (Fraction(4, 5), Fraction(4, 5)),
        (Fraction(3, 5), Fraction(6, 5)),
    ]
    for u, v in samples:
        b = saturated_fibre_power(u, v)
        lower, upper = primitive_second_degree_interval(b, v)
        assert (lower <= upper) == in_primitive_second_polytope(u, v)
        lower, upper = primitive_third_degree_interval(b, v)
        assert (lower <= upper) == in_primitive_third_polytope(u, v)


def test_first_euclidean_sectors_are_recovered_exactly() -> None:
    # If p=q/w, then u=33/16-s and the drifting-fibre term is inactive in
    # the reported small-remainder sectors.
    second_u = Fraction(33, 16) - Fraction(21, 16)
    second_v = Fraction(27, 32)
    assert second_u == Fraction(3, 4)
    assert in_primitive_second_polytope(second_u, second_v)

    third_u = Fraction(33, 16) - Fraction(25, 16)
    third_v = Fraction(13, 12)
    assert third_u == Fraction(1, 2)
    assert in_primitive_third_polytope(third_u, third_v)


def test_two_line_beta_vertices() -> None:
    ledger = primitive_rebranch_polytope_ledger()
    assert bourgain_two_line_beta_budget(Fraction(33, 32)) == Fraction(1, 48)
    assert bourgain_two_line_beta_budget(Fraction(9, 8)) == Fraction(13, 192)
    assert bourgain_two_line_beta_budget(Fraction(221, 192)) == Fraction(49, 576)
    assert ledger["beta_budget_at_ceiling"] == Fraction(49, 576)
    assert in_bourgain_two_line_beta_polytope(
        Fraction(1, 16), Fraction(9, 8)
    )
    assert not in_bourgain_two_line_beta_polytope(
        Fraction(1, 12), Fraction(9, 8)
    )


def test_full_antedb_beta_table_is_contiguous() -> None:
    assert ANTEDB_BETA_PIECES[0].alpha_lower == 0
    assert ANTEDB_BETA_PIECES[-1].alpha_upper == Fraction(1, 2)
    for left, right in zip(ANTEDB_BETA_PIECES, ANTEDB_BETA_PIECES[1:]):
        assert left.alpha_upper == right.alpha_lower
    for piece in ANTEDB_BETA_PIECES:
        assert piece.intercept > 0
        assert 0 <= piece.slope <= 1
    # Both source intervals include their common endpoint.  The first pair
    # has a genuine (small) jump, and the better left-hand value must win.
    boundary = ANTEDB_BETA_PIECES[0].alpha_upper
    left = ANTEDB_BETA_PIECES[0]
    right = ANTEDB_BETA_PIECES[1]
    assert antedb_beta_bound(boundary) == min(
        left.intercept + left.slope * boundary,
        right.intercept + right.slope * boundary,
    )


def test_full_current_beta_table_misses_badly_approximable_ray() -> None:
    # On v=33/16-u the fibre exponent is at least
    # min(1,max(u,1-u)).  Since every table slope lies in [0,1], the cost
    # decreases up to u=1/2 and increases afterwards.  The exact minimum is
    # therefore at u=1/2.
    u = Fraction(1, 2)
    v = Fraction(33, 16) - u
    alpha = u / Fraction(35, 16)
    assert alpha == Fraction(8, 35)
    assert antedb_beta_bound(alpha) == Fraction(3223, 14490)
    cost = antedb_local_beta_top_power(u, v)
    assert cost == Fraction(6535, 6624)
    assert cost - Fraction(7, 8) == Fraction(739, 6624)
    # On each affine piece the top-block cost is monotone on either side of
    # u=1/2, so its global minimum occurs at 1/2 or at a table endpoint.
    candidates = [cost]
    phase_power = Fraction(35, 16)
    for piece in ANTEDB_BETA_PIECES:
        for endpoint in (piece.alpha_lower, piece.alpha_upper):
            trial_u = phase_power * endpoint
            fibre = min(Fraction(1), max(trial_u, 1 - trial_u))
            candidates.append(
                fibre
                + phase_power * piece.intercept
                + piece.slope * trial_u
            )
    assert min(candidates) == cost
    for numerator in range(0, 71):
        trial_u = Fraction(numerator, 64)
        if trial_u > Fraction(35, 32):
            break
        trial_v = Fraction(33, 16) - trial_u
        fibre = min(Fraction(1), max(trial_u, 1 - trial_u))
        assert antedb_local_beta_top_power(fibre, trial_v) >= cost


def test_nonconvergents_cannot_beat_the_bounded_type_envelope() -> None:
    q_power = Fraction(33, 16)
    claimed_minimum = Fraction(6535, 6624)
    for numerator in range(0, 71):
        natural = Fraction(numerator, 64)
        if natural > Fraction(35, 32):
            break
        envelope = bounded_type_envelope_fibre_power(natural)
        for excess in (Fraction(0), Fraction(1, 64), Fraction(1, 8)):
            p_power = natural + excess
            remainder = q_power - natural
            forced = full_rectangle_fibre_lower_count_power(
                p_power, remainder
            )
            assert forced >= envelope
            assert not in_primitive_second_polytope(p_power, remainder)
            assert not in_primitive_third_polytope(p_power, remainder)
            assert not in_bourgain_two_line_beta_polytope(
                p_power, remainder
            )
            assert antedb_local_beta_top_power(forced, remainder) >= claimed_minimum


def test_bounded_partial_quotient_ray_misses_every_closed_polytope() -> None:
    # A uniformly badly approximable step has v=33/16-u and
    # b>=min(1,max(u,1-u)).  Sampling all breakpoints suffices for the
    # piecewise-linear predicates, and the report gives the exact symbolic
    # exclusions.
    for numerator in range(0, 133):
        u = Fraction(numerator, 64)
        v = Fraction(33, 16) - u
        if v < 0:
            continue
        assert not in_primitive_second_polytope(u, v)
        assert not in_primitive_third_polytope(u, v)
        assert not in_bourgain_two_line_beta_polytope(u, v)


def test_fibonacci_hosts_give_two_large_badly_approximable_steps() -> None:
    fib = [0, 1]
    for _ in range(2, 18):
        fib.append(fib[-1] + fib[-2])
    for index in range(8, 18):
        x, y = fib[index - 1], fib[index]
        assert gcd(x, y) == 1
        step_y = min(pow(x, -1, y), y - pow(x, -1, y))
        residue_x = (-pow(y, -1, x)) % x
        step_x = min(residue_x, x - residue_x)
        assert step_y == fib[index - 2]
        assert step_x == fib[index - 3]
