"""Exact sparse Fourier and cyclotomic classification for the FGF4 gate.

The module is finite and unconditional.  It does not estimate cousin primes.
It records the sharp support-only Fourier extremum, the exact centered
autocorrelation-energy decomposition, and the Galois orbit of a selected
Fourier energy at a prime modulus.
"""

from __future__ import annotations

import cmath
import itertools
import math
from dataclasses import dataclass
from fractions import Fraction


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def normalized_subset(values: list[int] | tuple[int, ...] | set[int], q: int) -> tuple[int, ...]:
    residues = tuple(sorted({value % q for value in values}))
    if len(residues) != len(values):
        raise ValueError("values must be distinct modulo q")
    return residues


def fourier_sum(values: tuple[int, ...], q: int, frequency: int) -> complex:
    return sum(
        cmath.exp(2j * math.pi * (frequency % q) * value / q)
        for value in values
    )


def fourier_energy(values: tuple[int, ...], q: int, frequency: int) -> float:
    return abs(fourier_sum(values, q, frequency)) ** 2


def cyclic_correlation(values: tuple[int, ...], q: int) -> tuple[int, ...]:
    support = set(values)
    return tuple(
        sum(1 for value in values if (value + shift) % q in support)
        for shift in range(q)
    )


def sharp_support_extremum(q: int, size: int) -> float:
    """Maximum modulus of a sum of ``size`` distinct q-th roots."""

    if q < 2 or not 0 <= size <= q:
        raise ValueError("require q>=2 and 0<=size<=q")
    if size in (0, q):
        return 0.0
    return math.sin(math.pi * size / q) / math.sin(math.pi / q)


def is_cyclic_interval(values: tuple[int, ...], q: int) -> bool:
    if not values or len(values) == q:
        return True
    support = set(values)
    size = len(values)
    return any(
        support == {(start + offset) % q for offset in range(size)}
        for start in range(q)
    )


def is_selected_interval(
    values: tuple[int, ...], q: int, frequency: int
) -> bool:
    if math.gcd(frequency, q) != 1:
        raise ValueError("frequency must be a unit modulo q")
    dilated = tuple(sorted((frequency * value) % q for value in values))
    return is_cyclic_interval(dilated, q)


@dataclass(frozen=True)
class SelectedDiscrepancy:
    q: int
    size: int
    frequency: int
    discrepancy: Fraction
    witness_start: int
    witness_length: int
    witness_signed_discrepancy: Fraction
    selected_modulus: float


def selected_progression_discrepancy(
    values: tuple[int, ...], q: int, frequency: int
) -> SelectedDiscrepancy:
    """Maximum count race on cyclic intervals in selected-frequency order.

    A cyclic interval in the coordinate ``j=frequency*r`` is a modular
    arithmetic progression with step ``frequency^{-1}`` in the original
    residue coordinate.  Abel summation against a cosine of total variation
    at most four gives ``|Ahat(frequency)| <= 4*discrepancy``.
    """

    values = normalized_subset(values, q)
    frequency %= q
    if frequency == 0 or math.gcd(frequency, q) != 1:
        raise ValueError("frequency must be a unit modulo q")
    support = {(frequency * value) % q for value in values}
    size = len(values)
    best = Fraction(-1, 1)
    best_start = 0
    best_length = 0
    best_signed = Fraction(0, 1)
    for start in range(q):
        count = 0
        for length in range(1, q + 1):
            count += int((start + length - 1) % q in support)
            signed = Fraction(count, 1) - Fraction(size * length, q)
            if abs(signed) > best:
                best = abs(signed)
                best_start = start
                best_length = length
                best_signed = signed
    selected = abs(fourier_sum(values, q, frequency))
    if selected > 4 * float(best) + 1e-9:
        raise AssertionError("bounded-variation discrepancy inequality failed")
    return SelectedDiscrepancy(
        q=q,
        size=size,
        frequency=frequency,
        discrepancy=best,
        witness_start=best_start,
        witness_length=best_length,
        witness_signed_discrepancy=best_signed,
        selected_modulus=selected,
    )


@dataclass(frozen=True)
class PhaseArcStability:
    selected_modulus: float
    deficit_from_mass: float
    radius: float
    outliers: int
    outlier_upper_bound: float


def phase_arc_stability(
    values: tuple[int, ...], q: int, frequency: int, radius: float
) -> PhaseArcStability:
    """Quantify phase concentration around the selected resultant direction."""

    values = normalized_subset(values, q)
    if not 0 < radius <= math.pi:
        raise ValueError("radius must lie in (0, pi]")
    selected = fourier_sum(values, q, frequency)
    direction = cmath.phase(selected) if values else 0.0

    def angular_distance(angle: float) -> float:
        return abs((angle - direction + math.pi) % (2 * math.pi) - math.pi)

    outliers = sum(
        angular_distance(2 * math.pi * (frequency % q) * value / q) >= radius
        for value in values
    )
    deficit = len(values) - abs(selected)
    upper = deficit / (1 - math.cos(radius))
    if outliers > upper + 1e-8:
        raise AssertionError("resultant phase-concentration inequality failed")
    return PhaseArcStability(
        selected_modulus=abs(selected),
        deficit_from_mass=deficit,
        radius=radius,
        outliers=outliers,
        outlier_upper_bound=upper,
    )


@dataclass(frozen=True)
class EnergyRigidity:
    q: int
    size: int
    correlation: tuple[int, ...]
    centered_energy: Fraction
    continuous_floor: Fraction
    excess: Fraction
    integer_floor: Fraction
    quantized_gap: int
    lambda_off_diagonal: Fraction
    mu_fourier: Fraction
    is_difference_set: bool
    is_almost_difference_set: bool


def energy_rigidity(values: tuple[int, ...], q: int) -> EnergyRigidity:
    """Return the exact physical-space centered-energy decomposition."""

    values = normalized_subset(values, q)
    size = len(values)
    correlation = cyclic_correlation(values, q)
    centered = sum(
        (Fraction(row, 1) - Fraction(size * size, q)) ** 2
        for row in correlation
    )
    continuous_floor = Fraction(
        size * size * (q - size) * (q - size), q * (q - 1)
    )
    excess = centered - continuous_floor
    difference_total = size * (size - 1)
    quotient, remainder = divmod(difference_total, q - 1)
    integer_floor = Fraction(remainder * (q - 1 - remainder), q - 1)
    quantized_gap_fraction = excess - integer_floor
    if quantized_gap_fraction.denominator != 1:
        raise AssertionError("the correlation defect must be integral")
    quantized_gap = quantized_gap_fraction.numerator
    if quantized_gap < 0 or quantized_gap % 2:
        raise AssertionError("the correlation defect must be nonnegative and even")
    off_diagonal = correlation[1:]
    allowed = {quotient, quotient + 1}
    almost = all(row in allowed for row in off_diagonal)
    difference = remainder == 0 and all(row == quotient for row in off_diagonal)
    return EnergyRigidity(
        q=q,
        size=size,
        correlation=correlation,
        centered_energy=centered,
        continuous_floor=continuous_floor,
        excess=excess,
        integer_floor=integer_floor,
        quantized_gap=quantized_gap,
        lambda_off_diagonal=Fraction(difference_total, q - 1),
        mu_fourier=Fraction(size * (q - size), q - 1),
        is_difference_set=difference,
        is_almost_difference_set=almost,
    )


@dataclass(frozen=True)
class GaloisEnergyOrbit:
    q: int
    size: int
    frequency: int
    stabilizer: tuple[int, ...]
    stabilizer_size: int
    degree: int
    trace: int
    mu_fourier: Fraction
    selected_energy: float
    trace_bound: Fraction
    cardinality_gcd: int
    level_cosets: tuple[tuple[int, ...], ...]


def galois_energy_orbit(
    values: tuple[int, ...], q: int, frequency: int = 1
) -> GaloisEnergyOrbit:
    """Classify the Galois orbit of |sum_A e_q(frequency*r)|^2.

    At a prime q, equality of two Fourier energies is equivalent to a
    multiplicative symmetry of the integer cyclic autocorrelation.  This lets
    the stabilizer, degree, trace, and level multiplicities be certified using
    integer arithmetic only.
    """

    if not is_prime(q) or q < 5:
        raise ValueError("q must be an odd prime at least 5")
    values = normalized_subset(values, q)
    size = len(values)
    if not 0 < size < q:
        raise ValueError("use a nonempty proper subset")
    frequency %= q
    if frequency == 0:
        raise ValueError("frequency must be nonzero modulo q")

    correlation = cyclic_correlation(values, q)
    stabilizer = tuple(
        multiplier
        for multiplier in range(1, q)
        if all(
            correlation[(multiplier * shift) % q] == correlation[shift]
            for shift in range(q)
        )
    )
    h = len(stabilizer)
    if (q - 1) % h:
        raise AssertionError("the stabilizer size must divide q-1")
    if q - 1 not in stabilizer:
        raise AssertionError("correlation symmetry must contain -1")
    degree = (q - 1) // h
    difference_total = size * (size - 1)
    if difference_total % h:
        raise AssertionError("the stabilizer size must divide N(N-1)")
    l2_mass = size * (q - size)
    if l2_mass % h:
        raise AssertionError("the stabilizer size must divide N(q-N)")
    trace = l2_mass // h
    mu = Fraction(l2_mass, q - 1)

    unseen = set(range(1, q))
    cosets: list[tuple[int, ...]] = []
    while unseen:
        representative = min(unseen)
        coset = tuple(sorted({representative * row % q for row in stabilizer}))
        unseen.difference_update(coset)
        cosets.append(coset)
    if len(cosets) != degree or any(len(row) != h for row in cosets):
        raise AssertionError("nonzero frequencies must split into equal H-cosets")

    selected = fourier_energy(values, q, frequency)
    return GaloisEnergyOrbit(
        q=q,
        size=size,
        frequency=frequency,
        stabilizer=stabilizer,
        stabilizer_size=h,
        degree=degree,
        trace=trace,
        mu_fourier=mu,
        selected_energy=selected,
        trace_bound=Fraction(degree * l2_mass, q - 1),
        cardinality_gcd=math.gcd(q - 1, difference_total),
        level_cosets=tuple(cosets),
    )


def degree_sensitive_energy_floor(
    rigidity: EnergyRigidity, orbit: GaloisEnergyOrbit
) -> float:
    """Lower bound for centered energy using one Galois energy level."""

    if rigidity.q != orbit.q or rigidity.size != orbit.size:
        raise ValueError("rigidity and orbit rows must describe the same subset")
    if orbit.degree == 1:
        return float(rigidity.continuous_floor)
    deviation = orbit.selected_energy - float(orbit.mu_fourier)
    return float(rigidity.continuous_floor) + (
        (orbit.q - 1) * deviation * deviation
        / (orbit.q * (orbit.degree - 1))
    )


@dataclass(frozen=True)
class LocalSparseModel:
    q: int
    numerator: int
    size: int
    values: tuple[int, ...]
    selected_sum: complex
    geometric_modulus: float


def local_sparse_model(q: int, size: int, start: int = 1) -> LocalSparseModel:
    """A locally admissible, gap-four-free sparse coherent configuration.

    The values are consecutive members of one class modulo 12.  Therefore
    n and n+4 avoid the local prime obstructions 2 and 3, and distinct lower
    endpoints never differ by 4.  This is not asserted to be a prime model.
    """

    if q <= 3 or q % 4 != 3 or math.gcd(q, 3) != 1:
        raise ValueError("require q>3, q=3 mod 4, and 3 not dividing q")
    if start % 12 != 1:
        raise ValueError("start must be 1 modulo 12")
    if size < 1 or 12 * (size - 1) >= q:
        raise ValueError("the progression must fit in an interval of length q")
    numerator = (q + 1) // 4
    values = tuple(start + 12 * index for index in range(size))
    selected = sum(
        cmath.exp(2j * math.pi * numerator * value / q) for value in values
    )
    geometric = abs(math.sin(3 * math.pi * size / q) / math.sin(3 * math.pi / q))
    return LocalSparseModel(
        q=q,
        numerator=numerator,
        size=size,
        values=values,
        selected_sum=selected,
        geometric_modulus=geometric,
    )


def exhaustive_support_maximum(q: int, size: int, frequency: int = 1) -> tuple[float, int]:
    """Small-q verifier: return the maximum and number of maximizers."""

    rows = []
    for subset in itertools.combinations(range(q), size):
        rows.append((abs(fourier_sum(subset, q, frequency)), subset))
    maximum = max(row[0] for row in rows)
    maximizers = sum(abs(value - maximum) < 1e-10 for value, _ in rows)
    return maximum, maximizers
