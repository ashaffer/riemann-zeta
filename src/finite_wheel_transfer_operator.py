"""Exact finite-wheel renewal operators and coupling certificates.

The module studies an independent Bernoulli process on the ordered units of a
periodic wheel.  It is a model of candidate primes, not a theorem about the
actual primes.

The apparently dense geometric successor kernel factors through the sparse
cyclic system ``I - (1-p) S``.  All mass and coupling certificates below use
``fractions.Fraction`` and are therefore exact.  Roots of unity are needed
only for optional numerical displays; the uniform additive-mode bound is a
rational triangle-inequality certificate.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import cmath
import math
from typing import Iterable, Sequence


def _as_fraction(value: Fraction | int) -> Fraction:
    if isinstance(value, Fraction):
        return value
    return Fraction(value)


def is_prime(n: int) -> bool:
    """Return whether ``n`` is prime (sufficient for the modest wheel tool)."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            return False
        factor += 2
    return True


def periodic_units(modulus: int) -> tuple[int, ...]:
    """Ordered representatives in ``(0, modulus]`` of a unit wheel."""
    if modulus < 1:
        raise ValueError("the modulus must be positive")
    if modulus == 1:
        return (1,)
    return tuple(n for n in range(1, modulus) if math.gcd(n, modulus) == 1)


def cyclic_physical_gaps(period: int, sites: Sequence[int]) -> tuple[int, ...]:
    """One-step physical gaps between cyclically ordered sites."""
    if period < 1 or not sites:
        raise ValueError("a positive period and at least one site are required")
    if tuple(sites) != tuple(sorted(sites)):
        raise ValueError("sites must be strictly ordered")
    if len(set(sites)) != len(sites):
        raise ValueError("sites must be distinct")
    if not all(0 < site <= period for site in sites):
        raise ValueError("sites must lie in (0, period]")
    return tuple(
        (sites[(i + 1) % len(sites)] + (period if i + 1 == len(sites) else 0))
        - sites[i]
        for i in range(len(sites))
    )


@dataclass(frozen=True)
class SparseRenewalOperator:
    """A periodic Bernoulli renewal process in sparse-resolvent form.

    ``sites`` are candidate locations in one physical period.  Each candidate
    is independently retained with probability ``p``.  On candidate indices,
    the successor transition is

        K = p S (I - z S)^(-1),  z = 1-p,

    where ``S`` is cyclic forward shift.  We never need to materialize this
    dense matrix to compute the expected symmetrized Voronoi masses.
    """

    period: int
    sites: tuple[int, ...]
    p: Fraction

    def __post_init__(self) -> None:
        p = _as_fraction(self.p)
        object.__setattr__(self, "p", p)
        cyclic_physical_gaps(self.period, self.sites)
        if not (0 < p <= 1):
            raise ValueError("p must lie in (0,1]")

    @classmethod
    def unit_wheel(
        cls, auxiliary_modulus: int, q: int, p: Fraction | int
    ) -> "SparseRenewalOperator":
        """Bernoulli process on the units modulo ``auxiliary_modulus*q``."""
        if auxiliary_modulus < 1:
            raise ValueError("the auxiliary modulus must be positive")
        if not is_prime(q):
            raise ValueError("q must be prime")
        if math.gcd(auxiliary_modulus, q) != 1:
            raise ValueError("the auxiliary modulus and q must be coprime")
        period = auxiliary_modulus * q
        return cls(period, periodic_units(period), _as_fraction(p))

    @property
    def size(self) -> int:
        return len(self.sites)

    @property
    def z(self) -> Fraction:
        return 1 - self.p

    @property
    def gaps(self) -> tuple[int, ...]:
        return cyclic_physical_gaps(self.period, self.sites)

    def sparse_system_entries(
        self, direction: int = 1
    ) -> tuple[tuple[int, int, Fraction], ...]:
        """Entries of ``I-z*S_direction``, with duplicate entries combined."""
        if direction not in (-1, 1):
            raise ValueError("direction must be +1 or -1")
        entries: dict[tuple[int, int], Fraction] = {}
        for row in range(self.size):
            key = (row, row)
            entries[key] = entries.get(key, Fraction(0)) + 1
            key = (row, (row + direction) % self.size)
            entries[key] = entries.get(key, Fraction(0)) - self.z
        return tuple(
            (row, col, value)
            for (row, col), value in sorted(entries.items())
            if value
        )

    def transition_probability(self, source: int, target: int) -> Fraction:
        """Exact entry of the dense successor kernel, without forming it."""
        if not (0 <= source < self.size and 0 <= target < self.size):
            raise IndexError("candidate index outside the wheel")
        steps = (target - source) % self.size
        if steps == 0:
            steps = self.size
        return self.p * self.z ** (steps - 1) / (1 - self.z**self.size)

    def transition_matrix(self) -> tuple[tuple[Fraction, ...], ...]:
        """Materialize the exact kernel (intended only for small audits)."""
        return tuple(
            tuple(self.transition_probability(i, j) for j in range(self.size))
            for i in range(self.size)
        )

    def _forward_gap_resolvent(self) -> tuple[Fraction, ...]:
        """Solve ``f_i=d_i+z*f_(i+1)`` exactly in linear time."""
        gaps = self.gaps
        z = self.z
        denominator = 1 - z**self.size
        first = sum(
            (z**h * gaps[h] for h in range(self.size)), Fraction(0)
        ) / denominator
        values = [Fraction(0)] * self.size
        values[0] = first
        if self.size > 1:
            values[-1] = gaps[-1] + z * values[0]
            for i in range(self.size - 2, 0, -1):
                values[i] = gaps[i] + z * values[i + 1]
        return tuple(values)

    def _backward_gap_resolvent(self) -> tuple[Fraction, ...]:
        """Solve ``b_(i+1)=d_i+z*b_i`` exactly in linear time."""
        gaps = self.gaps
        z = self.z
        denominator = 1 - z**self.size
        first = sum(
            (z**h * gaps[(-h - 1) % self.size] for h in range(self.size)),
            Fraction(0),
        ) / denominator
        values = [Fraction(0)] * self.size
        values[0] = first
        for i in range(self.size - 1):
            values[i + 1] = gaps[i] + z * values[i]
        return tuple(values)

    def gap_resolvents(self) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
        """Conditional expected right and left physical marked distances."""
        return self._forward_gap_resolvent(), self._backward_gap_resolvent()

    def stationary_voronoi_masses(self) -> tuple[Fraction, ...]:
        """Expected symmetrized cell mass at each candidate, normalized to 1."""
        forward, backward = self.gap_resolvents()
        scale = self.p / (2 * self.period)
        masses = tuple(scale * (forward[i] + backward[i]) for i in range(self.size))
        if sum(masses, Fraction(0)) != 1:
            raise ArithmeticError("stationary mass normalization failed")
        return masses

    def candidate_index_eigenvalue(self, frequency: int) -> complex:
        """Numerical eigenvalue of ``K`` on a candidate-index Fourier mode."""
        xi = cmath.exp(2j * math.pi * (frequency % self.size) / self.size)
        return float(self.p) * xi / (1 - float(self.z) * xi)

    def residue_masses(self, q: int) -> tuple[Fraction, ...]:
        """Aggregate stationary mass by physical residue modulo ``q``."""
        if q < 2 or self.period % q:
            raise ValueError("q must divide the physical period")
        result = [Fraction(0)] * q
        for site, mass in zip(self.sites, self.stationary_voronoi_masses()):
            result[site % q] += mass
        return tuple(result)

    def additive_mode(self, q: int, numerator: int) -> complex:
        """Numerical physical additive mode from exact rational masses."""
        residues = self.residue_masses(q)
        omega = cmath.exp(2j * math.pi * (numerator % q) / q)
        return sum(float(mass) * omega**a for a, mass in enumerate(residues))


@dataclass(frozen=True)
class UniformWheelCertificate:
    """Exact rational certificate for the growing-auxiliary-wheel theorem."""

    auxiliary_modulus: int
    q: int
    p: Fraction
    residue_masses: tuple[Fraction, ...]
    excesses: tuple[Fraction, ...]

    @property
    def nonprincipal_bound(self) -> Fraction:
        """Certified bound for every reduced nonzero additive numerator."""
        return Fraction(1, self.q - 1)

    @property
    def redistributed_mass(self) -> Fraction:
        return sum(self.excesses[1:], Fraction(0))

    def validate(self) -> None:
        if not is_prime(self.q):
            raise ArithmeticError("q is not prime")
        if math.gcd(self.auxiliary_modulus, self.q) != 1:
            raise ArithmeticError("P and q are not coprime")
        if len(self.residue_masses) != self.q or len(self.excesses) != self.q:
            raise ArithmeticError("wrong residue-vector length")
        if self.residue_masses[0] != 0:
            raise ArithmeticError("the Pq wheel retained a q-divisible site")
        if sum(self.residue_masses, Fraction(0)) != 1:
            raise ArithmeticError("residue masses do not normalize")
        if self.excesses[0] != 0:
            raise ArithmeticError("residue zero has no survivor excess")
        for a in range(1, self.q):
            if self.excesses[a] != self.residue_masses[a] - Fraction(1, self.q):
                raise ArithmeticError("incorrect coupling excess")
            if self.excesses[a] < 0:
                raise ArithmeticError("Voronoi deletion monotonicity failed")
        if self.redistributed_mass != Fraction(1, self.q):
            raise ArithmeticError("deleted baseline mass was not redistributed")

    def numerical_nonprincipal_mode(self, numerator: int) -> complex:
        omega = cmath.exp(2j * math.pi * (numerator % self.q) / self.q)
        full = sum(
            float(self.residue_masses[a]) * omega**a
            for a in range(1, self.q)
        )
        return full + Fraction(1, self.q - 1)

    def exact_triangle_ledger(self) -> tuple[Fraction, Fraction, Fraction]:
        """Return the three exact terms in the uniform disk certificate.

        The nonprincipal mode is

            1/[q(q-1)] + sum_(a!=0) excess_a e_q(ra).

        Its radius is therefore ``1/q`` and its absolute value is at most
        ``1/[q(q-1)] + 1/q = 1/(q-1)``.
        """
        center = Fraction(1, self.q * (self.q - 1))
        radius = self.redistributed_mass
        return center, radius, center + radius


def uniform_wheel_certificate(
    auxiliary_modulus: int, q: int, p: Fraction | int
) -> UniformWheelCertificate:
    """Build and verify the exact all-``P`` additive-mode certificate.

    The proof input not recomputed by floating point is geometric: couple the
    P-wheel process and delete all marked centers divisible by q.  A surviving
    one-dimensional Voronoi cell can only expand.  P-periodicity gives exact
    baseline mass 1/q in every q-residue, so the rational masses computed by
    the independent sparse resolvent must have nonnegative excesses.
    """
    operator = SparseRenewalOperator.unit_wheel(auxiliary_modulus, q, p)
    masses = operator.residue_masses(q)
    excesses = [Fraction(0)] * q
    for a in range(1, q):
        excesses[a] = masses[a] - Fraction(1, q)
    certificate = UniformWheelCertificate(
        auxiliary_modulus,
        q,
        _as_fraction(p),
        masses,
        tuple(excesses),
    )
    certificate.validate()
    return certificate


def primitive_root_prime(q: int) -> int:
    """Return the least primitive root modulo a prime q."""
    if not is_prime(q):
        raise ValueError("q must be prime")
    phi = q - 1
    factors: list[int] = []
    remainder = phi
    factor = 2
    while factor * factor <= remainder:
        if remainder % factor == 0:
            factors.append(factor)
            while remainder % factor == 0:
                remainder //= factor
        factor += 1
    if remainder > 1:
        factors.append(remainder)
    for candidate in range(2, q):
        if all(pow(candidate, phi // factor, q) != 1 for factor in factors):
            return candidate
    if q == 2:
        return 1
    raise ArithmeticError("primitive root search failed")


def multiplicative_character_table(q: int) -> tuple[tuple[complex, ...], ...]:
    """All multiplicative characters of ``F_q^*``, principal first."""
    generator = primitive_root_prime(q)
    logs = [0] * q
    value = 1
    for exponent in range(q - 1):
        logs[value] = exponent
        value = value * generator % q
    table = []
    for frequency in range(q - 1):
        table.append(
            tuple(
                0j
                if a == 0
                else cmath.exp(2j * math.pi * frequency * logs[a] / (q - 1))
                for a in range(q)
            )
        )
    return tuple(table)


def character_diagonalization(
    residue_masses: Sequence[Fraction], q: int, numerator: int
) -> tuple[complex, complex]:
    """Compare direct additive mode with its exact character decomposition.

    The returned complex values are numerical evaluations of an algebraic
    identity.  Exact rational certification of the uniform bound is supplied
    by :class:`UniformWheelCertificate`, not by floating-point agreement here.
    """
    if len(residue_masses) != q or not is_prime(q):
        raise ValueError("masses must be indexed modulo a prime q")
    omega = cmath.exp(2j * math.pi * (numerator % q) / q)
    direct = sum(float(residue_masses[a]) * omega**a for a in range(q))
    characters = multiplicative_character_table(q)
    reconstructed = 0j
    for character in characters:
        character_mode = sum(
            float(residue_masses[a]) * character[a] for a in range(1, q)
        )
        gauss = sum(
            omega**b * character[b].conjugate() for b in range(1, q)
        )
        reconstructed += gauss * character_mode / (q - 1)
    return direct, reconstructed


def repeated_base_wheel_operator(
    auxiliary_modulus: int, q: int, p: Fraction | int
) -> SparseRenewalOperator:
    """The P-wheel repeated over the common physical period Pq.

    Unlike :meth:`SparseRenewalOperator.unit_wheel`, this does *not* delete
    the candidates divisible by q.  It is the exact base object in the
    deletion coupling.  Its physical q-mode has zero period mean.
    """
    if auxiliary_modulus < 1 or not is_prime(q):
        raise ValueError("require a positive P and prime q")
    if math.gcd(auxiliary_modulus, q) != 1:
        raise ValueError("P and q must be coprime")
    period = auxiliary_modulus * q
    sites = tuple(
        n
        for n in range(1, period + 1)
        if math.gcd(n, auxiliary_modulus) == 1
    )
    return SparseRenewalOperator(period, sites, _as_fraction(p))


@dataclass(frozen=True)
class PrefixDiscrepancyCertificate:
    """Exact formal q-residue coboundary for a periodic atomic mass.

    ``physical_weights`` sum to ``period``.  For the vector measure ``mu``
    obtained by placing each weight in its site's q-residue, put

        H(x) = mu((0,x]) - (x/period) mu((0,period]).

    The vector H is period-periodic after extension to the real line, and
    every interval discrepancy is exactly ``H(right)-H(left)``.  The stored
    l1 maximum is rational and uniformly bounds every additive q-mode.
    """

    period: int
    q: int
    sites: tuple[int, ...]
    physical_weights: tuple[Fraction, ...]
    total_residues: tuple[Fraction, ...]
    max_formal_l1: Fraction

    def _prefix_in_period(
        self, x: Fraction, include_endpoint: bool = True
    ) -> tuple[Fraction, ...]:
        if not (0 <= x <= self.period):
            raise ValueError("x must lie in one physical period")
        vector = [Fraction(0)] * self.q
        for site, weight in zip(self.sites, self.physical_weights):
            if site < x or (include_endpoint and site == x):
                vector[site % self.q] += weight
        return tuple(vector)

    def centered_prefix(
        self, x: Fraction | int, include_endpoint: bool = True
    ) -> tuple[Fraction, ...]:
        """Evaluate the exact periodic prefix H at a point in one period."""
        x = _as_fraction(x)
        prefix = self._prefix_in_period(x, include_endpoint)
        return tuple(
            prefix[a] - x * self.total_residues[a] / self.period
            for a in range(self.q)
        )

    def cumulative_residue_vector(self, x: int) -> tuple[Fraction, ...]:
        """Physical mass vector on ``(0,x]`` for any integer x."""
        cycles, remainder = divmod(x, self.period)
        prefix = self._prefix_in_period(Fraction(remainder), True)
        return tuple(
            cycles * self.total_residues[a] + prefix[a] for a in range(self.q)
        )

    def interval_residue_vector(self, left: int, right: int) -> tuple[Fraction, ...]:
        """Physical mass vector on ``(left,right]`` in the periodic extension."""
        if right < left:
            raise ValueError("right endpoint must not precede left endpoint")
        before = self.cumulative_residue_vector(left)
        after = self.cumulative_residue_vector(right)
        return tuple(after[a] - before[a] for a in range(self.q))

    def interval_discrepancy(self, left: int, right: int) -> tuple[Fraction, ...]:
        """Subtract the exact period mean from an interval mass vector."""
        interval = self.interval_residue_vector(left, right)
        return tuple(
            interval[a]
            - Fraction(right - left, self.period) * self.total_residues[a]
            for a in range(self.q)
        )

    def endpoint_coboundary(self, left: int, right: int) -> tuple[Fraction, ...]:
        """Compute H(right)-H(left), which must equal interval_discrepancy."""
        left_cycles, left_remainder = divmod(left, self.period)
        right_cycles, right_remainder = divmod(right, self.period)
        del left_cycles, right_cycles  # H is periodic.
        left_h = self.centered_prefix(left_remainder, True)
        right_h = self.centered_prefix(right_remainder, True)
        return tuple(right_h[a] - left_h[a] for a in range(self.q))

    def validate(self) -> None:
        if self.period < 1 or self.q < 2 or self.period % self.q:
            raise ArithmeticError("the formal period must be divisible by q")
        if len(self.sites) != len(self.physical_weights):
            raise ArithmeticError("site/weight length mismatch")
        if len(self.total_residues) != self.q:
            raise ArithmeticError("wrong residue total length")
        if sum(self.physical_weights, Fraction(0)) != self.period:
            raise ArithmeticError("physical weights do not partition the period")
        recomputed = [Fraction(0)] * self.q
        for site, weight in zip(self.sites, self.physical_weights):
            recomputed[site % self.q] += weight
        if tuple(recomputed) != self.total_residues:
            raise ArithmeticError("incorrect residue totals")
        if self.centered_prefix(0) != (Fraction(0),) * self.q:
            raise ArithmeticError("prefix does not start at zero")
        if self.centered_prefix(self.period) != (Fraction(0),) * self.q:
            raise ArithmeticError("prefix does not close over a period")


def prefix_discrepancy_certificate(
    operator: SparseRenewalOperator, q: int
) -> PrefixDiscrepancyCertificate:
    """Build an exact rational l1 certificate for interval truncation.

    The maximum of a convex piecewise-linear l1 norm occurs at a one-sided
    atom endpoint, so evaluating both sides of every site is exact.
    """
    if operator.period % q:
        raise ValueError("the chosen physical period must be divisible by q")
    normalized = operator.stationary_voronoi_masses()
    weights = tuple(operator.period * mass for mass in normalized)
    totals = [Fraction(0)] * q
    for site, weight in zip(operator.sites, weights):
        totals[site % q] += weight

    provisional = PrefixDiscrepancyCertificate(
        operator.period,
        q,
        operator.sites,
        weights,
        tuple(totals),
        Fraction(0),
    )
    maximum = Fraction(0)
    for x in (0, *operator.sites, operator.period):
        for include in (False, True):
            vector = provisional.centered_prefix(x, include)
            maximum = max(maximum, sum((abs(value) for value in vector), Fraction(0)))
    result = PrefixDiscrepancyCertificate(
        operator.period,
        q,
        operator.sites,
        weights,
        tuple(totals),
        maximum,
    )
    result.validate()
    return result


def direct_geometric_masses(
    period: int, sites: Sequence[int], p: Fraction | int, terms: int
) -> tuple[Fraction, ...]:
    """Truncated defining renewal series, solely for independent tests."""
    if terms < 1:
        raise ValueError("terms must be positive")
    p = _as_fraction(p)
    z = 1 - p
    m = len(sites)
    result = []
    for i, site in enumerate(sites):
        distance_sum = Fraction(0)
        for k in range(1, terms + 1):
            plus_cycles, plus_index = divmod(i + k, m)
            minus_cycles, minus_index = divmod(i - k, m)
            plus = sites[plus_index] + plus_cycles * period
            minus = sites[minus_index] + minus_cycles * period
            distance_sum += z ** (k - 1) * (plus - minus)
        result.append(p * p * distance_sum / (2 * period))
    return tuple(result)


def apply_sparse_entries(
    entries: Iterable[tuple[int, int, Fraction]], vector: Sequence[Fraction]
) -> tuple[Fraction, ...]:
    """Apply a sparse rational matrix represented by coordinate entries."""
    output = [Fraction(0)] * len(vector)
    for row, col, value in entries:
        output[row] += value * vector[col]
    return tuple(output)
