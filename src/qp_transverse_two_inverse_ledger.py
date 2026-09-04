"""Exact ledgers for the transverse two-inverse codegree problem.

The analytic theorem proved in the companion report uses the defect

    k = x*a - y*b

and the least absolute modular step of the lifts ``a(k)`` and ``b(k)``.
This module only records the exact arithmetic coordinates and exponent
bookkeeping; the Selberg/van-der-Corput argument is written out in the
report.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd


def least_absolute_residue(value: int, modulus: int) -> int:
    """Return ``min(r, modulus-r)`` for ``r=value (mod modulus)``.

    The residue must be nonzero.  In the application ``value`` is a unit.
    """

    if modulus <= 1:
        raise ValueError("the modulus must exceed one")
    residue = value % modulus
    if residue == 0:
        raise ValueError("the residue must be nonzero")
    return min(residue, modulus - residue)


@dataclass(frozen=True)
class EndpointInverseSteps:
    """Least steps in the two defect-lift charts for endpoints ``x<y``."""

    x: int
    y: int
    gap: int
    step_mod_y: int
    step_mod_x: int


@dataclass(frozen=True)
class SharedBezoutChart:
    """One signed Bezout chart shared by both completion rotations."""

    x: int
    y: int
    gap: int
    s: int
    m: int
    step_mod_x: int
    step_mod_y: int


def endpoint_inverse_steps(x: int, y: int) -> EndpointInverseSteps:
    """Return the least absolute modular steps for the two completion lifts.

    From ``x*a-y*b=k`` one has

    ``a = x^{-1} k (mod y)`` and ``b = -y^{-1} k (mod x)``.

    If ``g=y-x``, both steps are also least absolute inverses of ``g``
    (up to sign) in their respective moduli.
    """

    if not 1 < x < y or gcd(x, y) != 1:
        raise ValueError("endpoints must be ordered, coprime integers")
    gap = y - x
    step_y = least_absolute_residue(pow(x, -1, y), y)
    step_x = least_absolute_residue(-pow(y, -1, x), x)
    if (gap * step_y) % y not in (1, y - 1):
        raise AssertionError("the y-chart inverse relation failed")
    if (gap * step_x) % x not in (1, x - 1):
        raise AssertionError("the x-chart inverse relation failed")
    return EndpointInverseSteps(x, y, gap, step_y, step_x)


def shared_bezout_chart(x: int, y: int) -> SharedBezoutChart:
    """Return signed ``s,m`` with ``m*x-(y-x)*s=1``.

    The exact defect lifts are

    ``a=(s+m)k+y*n`` and ``b=s*k+x*n``.

    Thus ``s`` represents ``-y^{-1} (mod x)`` while ``s+m`` represents
    ``x^{-1} (mod y)``.  This records that the two inverse steps are two
    faces of one Bezout relation, rather than independent rotations.
    """

    if not 1 < x < y or gcd(x, y) != 1:
        raise ValueError("endpoints must be ordered, coprime integers")
    gap = y - x
    residue = (-pow(gap, -1, x)) % x
    s = residue if 2 * residue <= x else residue - x
    numerator = gap * s + 1
    if numerator % x:
        raise AssertionError("signed Bezout lift lost divisibility")
    m = numerator // x
    if m * x - gap * s != 1:
        raise AssertionError("shared Bezout identity failed")
    step_x = least_absolute_residue(s, x)
    step_y = least_absolute_residue(s + m, y)
    endpoint = endpoint_inverse_steps(x, y)
    if (step_x, step_y) != (endpoint.step_mod_x, endpoint.step_mod_y):
        raise AssertionError("shared chart disagrees with endpoint inverse steps")
    return SharedBezoutChart(x, y, gap, s, m, step_x, step_y)


def shared_defect_lift(
    chart: SharedBezoutChart, defect: int, wrap: int
) -> DefectLift:
    """Return the exact two-completion lift from the shared Bezout chart."""

    first = (chart.s + chart.m) * defect + chart.y * wrap
    second = chart.s * defect + chart.x * wrap
    if chart.x * first - chart.y * second != defect:
        raise AssertionError("shared defect parametrization failed")
    return DefectLift(defect, first, second)


@dataclass(frozen=True)
class DefectLift:
    """One exact shell lift of ``x*a-y*b=k``."""

    defect: int
    first_completion: int
    second_completion: int


@dataclass(frozen=True)
class EuclideanRebranchChart:
    """Nearest-remainder chart for reorganizing wrapped defect lifts.

    If ``host=L*step+r`` and an oriented completion lift is

    ``a=step*k-host*n``, then, with ``t=k-L*n``, one has exactly

    ``k=t+L*n`` and ``a=step*t-r*n``.

    Thus fixing ``t`` replaces the large completion step ``step`` by the
    nearest Euclidean remainder ``abs(r)``.
    """

    host: int
    step: int
    quotient: int
    signed_remainder: int
    rho: int


def euclidean_rebranch_chart(host: int, step: int) -> EuclideanRebranchChart:
    """Return ``host=L*step+r`` with ``|r|`` the least nonzero residue.

    In the application ``step`` is a modular inverse step and hence is
    coprime to ``host``.  The nearest-remainder convention is useful but
    not essential: changing its sign only reverses the rebranched sums.
    """

    if not 1 < step < host or gcd(host, step) != 1:
        raise ValueError("host and step must be coprime with 1 < step < host")
    residue = host % step
    signed_remainder = residue if 2 * residue <= step else residue - step
    quotient, remainder = divmod(host - signed_remainder, step)
    if remainder:
        raise AssertionError("nearest Euclidean division failed")
    rho = abs(signed_remainder)
    if not 1 <= rho <= step // 2:
        raise AssertionError("remainder is not the least absolute residue")
    return EuclideanRebranchChart(
        host, step, quotient, signed_remainder, rho
    )


def euclidean_rebranch_lift(
    chart: EuclideanRebranchChart, defect: int, wrap: int
) -> tuple[int, int]:
    """Return ``(t,a)`` in the exact Euclidean rebranch identity.

    Here the oriented old lift is ``a=step*defect-host*wrap`` and the new
    sequence label is ``t=defect-quotient*wrap``.
    """

    sequence = defect - chart.quotient * wrap
    completion = chart.step * sequence - chart.signed_remainder * wrap
    old_completion = chart.step * defect - chart.host * wrap
    if completion != old_completion:
        raise AssertionError("Euclidean rebranch identity failed")
    return sequence, completion


def defect_lifts(
    x: int,
    y: int,
    defect: int,
    first_lower: int,
    first_upper: int,
    second_lower: int,
    second_upper: int,
) -> tuple[DefectLift, ...]:
    """Enumerate exact completion lifts in two supplied integer intervals."""

    if gcd(x, y) != 1:
        raise ValueError("the endpoints must be coprime")
    if min(first_lower, second_lower) <= 0:
        raise ValueError("completion intervals must be positive")
    if first_upper < first_lower or second_upper < second_lower:
        raise ValueError("invalid completion interval")

    residue = (pow(x, -1, y) * defect) % y
    first = residue + ((first_lower - residue + y - 1) // y) * y
    answer: list[DefectLift] = []
    while first <= first_upper:
        numerator = x * first - defect
        if numerator % y:
            raise AssertionError("defect lift lost divisibility")
        second = numerator // y
        if second_lower <= second <= second_upper:
            answer.append(DefectLift(defect, first, second))
        first += y
    return tuple(answer)


@dataclass(frozen=True)
class TransverseExponentLedger:
    """Exact power ledger at ``D=q^(16/33)``."""

    degree_in_q: Fraction
    target_in_q: Fraction
    window_in_q: Fraction
    selberg_degree_in_q: Fraction
    close_gap_in_q: Fraction
    completion_barrier_in_q: Fraction
    completion_barrier_in_degree: Fraction
    completion_loss_to_target_in_degree: Fraction
    classical_large_sieve_in_degree: Fraction
    inverse_step_branch_target_in_degree: Fraction
    optimized_inverse_step_cutoff_in_degree: Fraction
    optimized_selberg_degree_at_cutoff_in_degree: Fraction
    third_derivative_inverse_step_cutoff_in_degree: Fraction
    third_derivative_selberg_degree_at_cutoff_in_degree: Fraction
    third_derivative_wrap_endpoint_at_cutoff_in_degree: Fraction
    bourgain_pair_inverse_step_cutoff_in_degree: Fraction
    antedb_pair_inverse_step_cutoff_in_degree: Fraction
    bourgain_beta_inverse_step_cutoff_in_degree: Fraction
    bourgain_beta_gain_over_third_derivative_in_degree: Fraction
    principal_two_box_in_degree: Fraction


def transverse_exponent_ledger() -> TransverseExponentLedger:
    """Return the exact exponents used in the literature/no-go audit."""

    degree = Fraction(16, 33)
    target_q = degree * Fraction(7, 8)
    completion_q = Fraction(1, 2)
    return TransverseExponentLedger(
        degree_in_q=degree,
        target_in_q=target_q,
        window_in_q=degree - 1,
        selberg_degree_in_q=1 - degree,
        close_gap_in_q=degree * Fraction(3, 8),
        completion_barrier_in_q=completion_q,
        completion_barrier_in_degree=completion_q / degree,
        completion_loss_to_target_in_degree=(completion_q - target_q) / degree,
        classical_large_sieve_in_degree=Fraction(49, 32),
        inverse_step_branch_target_in_degree=Fraction(7, 8),
        optimized_inverse_step_cutoff_in_degree=Fraction(27, 32),
        optimized_selberg_degree_at_cutoff_in_degree=Fraction(1, 8),
        third_derivative_inverse_step_cutoff_in_degree=Fraction(13, 12),
        third_derivative_selberg_degree_at_cutoff_in_degree=Fraction(1, 8),
        third_derivative_wrap_endpoint_at_cutoff_in_degree=Fraction(61, 96),
        bourgain_pair_inverse_step_cutoff_in_degree=Fraction(109, 96),
        antedb_pair_inverse_step_cutoff_in_degree=Fraction(1194107, 1050032),
        bourgain_beta_inverse_step_cutoff_in_degree=Fraction(73, 64),
        bourgain_beta_gain_over_third_derivative_in_degree=Fraction(11, 192),
        principal_two_box_in_degree=Fraction(-1, 16),
    )


def inverse_step_branch_exponents() -> dict[str, Fraction]:
    """Powers in the optimized branch bound at ``w=D^(27/32)``.

    With ``K=(q/w^2)^(1/3)=D^(1/8)``, the terms are

    ``D^2/q``, ``D/K``, ``D*w*sqrt(K/q)``, and
    ``sqrt(q)/(w*sqrt(K))``.
    """

    return {
        "principal": Fraction(-1, 16),
        "selberg_resolution_at_cutoff": Fraction(7, 8),
        "curvature_at_cutoff": Fraction(7, 8),
        "vd_c_endpoint_at_cutoff": Fraction(1, 8),
    }


def third_derivative_branch_exponents() -> dict[str, Fraction]:
    """Powers at the third-derivative cutoff ``w=D^(13/12)``.

    Here ``K=q^(2/7)w^(-3/7)=D^(1/8)``.  The two endpoint entries come
    respectively from the one-branch term and from the extra
    ``sqrt(wD/q)`` supplied by the wrap count.
    """

    return {
        "principal": Fraction(-1, 16),
        "selberg_and_curvature": Fraction(7, 8),
        "one_branch_endpoint": Fraction(5, 8),
        "wrap_endpoint": Fraction(61, 96),
    }


def exponent_pair_wrap_cutoff(kappa: Fraction, lambd: Fraction) -> Fraction:
    """Largest ``b`` obtained from one exponent pair for ``w=D^b``.

    In the wrap regime the balanced Selberg degree is

    ``K=q^((1-lambda)/(1+kappa))
         w^(-(1+kappa-lambda)/(1+kappa))``.

    Requiring ``K>=D^(1/8)`` at ``q=D^(33/16)`` gives the returned
    cutoff.  The routine validates the usual exponent-pair triangle.
    """

    kappa = Fraction(kappa)
    lambd = Fraction(lambd)
    if not (
        0 <= kappa <= Fraction(1, 2)
        and Fraction(1, 2) <= lambd <= 1
        and kappa + lambd <= 1
    ):
        raise ValueError("point is outside the exponent-pair triangle")
    denominator = 1 + kappa - lambd
    if denominator <= 0:
        raise ValueError("the cutoff is degenerate for this exponent pair")
    return (
        Fraction(33, 16) * (1 - lambd) - (1 + kappa) * Fraction(1, 8)
    ) / denominator


def antedb_wrap_pair_cutoffs() -> dict[str, Fraction]:
    """Cutoffs needed to scan the current ANTEDB convex-hull table.

    This includes the finite positive-side vertices, their van der Corput
    ``B`` transforms, ``(1/2,1/2)``, and the first Heath--Brown tail pair.
    The second Tao--Trudgian--Yang point is included too, although it is not
    a hull vertex.  For the rest of the positive Heath--Brown tail the
    numerator of the cutoff is negative; every transformed tail pair has
    cutoff below one.
    """

    pairs = {
        "bourgain": (Fraction(13, 84), Fraction(55, 84)),
        "trudgian_yang_1": (
            Fraction(4742, 38463),
            Fraction(35731, 51284),
        ),
        "trudgian_yang_2": (Fraction(18, 199), Fraction(593, 796)),
        "trudgian_yang_3": (
            Fraction(2779, 38033),
            Fraction(58699, 76066),
        ),
        "tao_trudgian_yang_1": (Fraction(89, 1282), Fraction(997, 1282)),
        "cushing_1": (Fraction(311, 4822), Fraction(3799, 4822)),
        "cushing_2": (
            Fraction(80219, 1298878),
            Fraction(515638, 649439),
        ),
        "a_trudgian_yang_2": (Fraction(9, 217), Fraction(1461, 1736)),
        "tao_trudgian_yang_3": (
            Fraction(10769, 351096),
            Fraction(609317, 702192),
        ),
        "tao_trudgian_yang_4": (Fraction(89, 3478), Fraction(15327, 17390)),
        "tao_trudgian_yang_2": (
            Fraction(652397, 9713986),
            Fraction(7599781, 9713986),
        ),
    }
    cutoffs = {
        name: exponent_pair_wrap_cutoff(kappa, lambd)
        for name, (kappa, lambd) in pairs.items()
    }
    cutoffs["half"] = exponent_pair_wrap_cutoff(Fraction(1, 2), Fraction(1, 2))
    for name, (kappa, lambd) in pairs.items():
        cutoffs[f"b_{name}"] = exponent_pair_wrap_cutoff(
            lambd - Fraction(1, 2), kappa + Fraction(1, 2)
        )

    # The ANTEDB tail begins with m=6 in the Heath--Brown family.
    m = 6
    hb_kappa = Fraction(2, (m - 1) ** 2 * (m + 2))
    hb_lambda = 1 - Fraction(3 * m - 2, m * (m - 1) * (m + 2))
    cutoffs["heath_brown_6"] = exponent_pair_wrap_cutoff(hb_kappa, hb_lambda)
    cutoffs["b_heath_brown_6"] = exponent_pair_wrap_cutoff(
        hb_lambda - Fraction(1, 2), hb_kappa + Fraction(1, 2)
    )
    return cutoffs


def bourgain_beta_wrap_exponents() -> dict[str, Fraction]:
    """Exact endpoint ledger for the local-beta cutoff ``w=D^(73/64)``.

    Take ``K=D^(1/8)``.  A natural wrap branch has length
    ``N=q/w=D^(59/64)``, its top-frequency phase parameter is
    ``T_K=Kq=D^(35/16)``, and hence ``alpha=59/140``.  Bourgain's
    local bound is ``beta(alpha)<=1/12+2*alpha/3=51/140``.
    """

    return {
        "selberg_degree": Fraction(1, 8),
        "branch_length": Fraction(59, 64),
        "phase_parameter": Fraction(35, 16),
        "alpha": Fraction(59, 140),
        "beta": Fraction(51, 140),
        "wrap_count": Fraction(5, 64),
        "per_branch_sum": Fraction(51, 64),
        "all_branches_sum": Fraction(7, 8),
    }


def euclidean_second_rebranch_degree_interval(
    step_power: Fraction, remainder_power: Fraction
) -> tuple[Fraction, Fraction]:
    """Admissible degree powers for the second-derivative rebranch bound.

    Write ``w=D^step_power``, ``rho=D^remainder_power`` and ``K=D^k``.
    The lower endpoint makes both the Selberg resolution and the
    second-derivative endpoint term at most ``D^(7/8)``.  The upper endpoint
    includes the Selberg range and the stronger curvature-to-target
    constraint

    ``K <= q/(rho^2 D^(1/4))``.

    The returned interval is nonempty precisely when these recorded
    sufficient inequalities are compatible.
    """

    step_power = Fraction(step_power)
    remainder_power = Fraction(remainder_power)
    q_power = Fraction(33, 16)
    lower = max(
        Fraction(1, 8),
        3 * q_power
        - 2 * step_power
        - 2 * remainder_power
        - Fraction(7, 4),
    )
    upper = min(
        q_power - 1,
        q_power - 2 * remainder_power,
        q_power - 2 * remainder_power - Fraction(1, 4),
    )
    return lower, upper


def euclidean_third_rebranch_degree_interval(
    step_power: Fraction, remainder_power: Fraction
) -> tuple[Fraction, Fraction]:
    """Admissible degree powers for the third-derivative rebranch bound.

    The endpoint term requires

    ``K >= q^5/(w^3 rho^3 D^(9/4))``,

    while the curvature term is at most the target provided

    ``K <= q^2/(rho^3 D^(3/4))``.
    """

    step_power = Fraction(step_power)
    remainder_power = Fraction(remainder_power)
    q_power = Fraction(33, 16)
    lower = max(
        Fraction(1, 8),
        5 * q_power
        - 3 * step_power
        - 3 * remainder_power
        - Fraction(9, 4),
    )
    upper = min(
        q_power - 1,
        2 * q_power - 3 * remainder_power,
        2 * q_power - 3 * remainder_power - Fraction(3, 4),
    )
    return lower, upper


def euclidean_rebranch_and_poisson_exponents() -> dict[str, Fraction]:
    """Exact powers for the new rebranch sectors and cross-wrap no-go.

    The Poisson entries concern the top Selberg frequency
    ``h=K=D^(1/8)``.  Taking absolute values after stationary phase costs
    ``sqrt(hq)=D^(35/32)``, a ``D^(7/32)`` loss over the target.  Ordinary
    large sieve at ``w=D^(73/64)`` is still worse.
    """

    return {
        "second_step_minimum": Fraction(21, 16),
        "second_remainder_maximum": Fraction(27, 32),
        "second_product_minimum": Fraction(27, 16),
        "second_small_remainder_margin": Fraction(-7, 32),
        "third_step_minimum": Fraction(25, 16),
        "third_remainder_maximum": Fraction(13, 12),
        "third_product_minimum": Fraction(7, 3),
        "third_drifting_fibre_endpoint": Fraction(61, 96),
        "selberg_degree_floor": Fraction(1, 8),
        "poisson_stationary_amplitude": Fraction(31, 32),
        "poisson_l1_barrier": Fraction(35, 32),
        "poisson_l1_loss_to_target": Fraction(7, 32),
        "poisson_alias_orthogonal_large_sieve": Fraction(137, 128),
        "poisson_alias_orthogonal_loss_to_target": Fraction(25, 128),
        "poisson_large_sieve_at_beta_cutoff": Fraction(145, 128),
        "poisson_large_sieve_loss_to_target": Fraction(33, 128),
    }
