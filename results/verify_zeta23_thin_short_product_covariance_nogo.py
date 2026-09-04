#!/usr/bin/env python3
from fractions import Fraction
import sys

sys.path.insert(0, "src")

from thin_short_product_covariance_nogo import (
    H_MIN,
    KAPPA,
    adversarial_eta,
    aligned_block_energy,
    audit,
    closing_eta_frontier,
    diagonal_delta_frontier,
    prime_product_blocks,
    voronoi_difference_diagonal,
)


def main() -> None:
    blocks, unique = prime_product_blocks(20_000, 23, 59, 100)
    assert unique
    result = aligned_block_energy(blocks, 20_000, 100)
    assert result.total_pairs > 0
    assert result.unique_large_factor
    assert abs(result.direct_energy - result.count_energy) < 1e-8
    assert result.count_energy + 1e-12 >= result.cauchy_floor
    assert result.maximum_beta_modulus_error < 1e-12
    assert adversarial_eta(H_MIN) - closing_eta_frontier(H_MIN) == 4 * KAPPA
    assert closing_eta_frontier(H_MIN) > Fraction(16, 100)
    assert Fraction(1, 1000) < diagonal_delta_frontier() < Fraction(11, 10_000)
    diagonal, diagonal_bound = voronoi_difference_diagonal(
        [0, 7, 12], [0, 2, 5, 7, 9, 12]
    )
    assert 0 < diagonal <= diagonal_bound
    print("thin short-product covariance no-go: PASS")
    print(audit())


if __name__ == "__main__":
    main()
