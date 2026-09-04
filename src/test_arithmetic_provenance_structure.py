import unittest
from fractions import Fraction

from arithmetic_provenance_structure import (
    AdapterLoss,
    boundary_first,
    boundary_second,
    cumulative_flux,
    finite_dual_certificate,
    matrix_add,
    outer,
    path_boundary,
    polarized_product_divergence_defect,
    polarized_symmetric_square_defect,
    product_divergence_defect,
    semiprime_difference_diagonal,
    symmetric_square_defect,
)


class PathFluxTests(unittest.TestCase):
    def test_boundary_and_cumulative_flux_are_exact_inverses(self):
        discrepancy = [Fraction(2), Fraction(-5), Fraction(7), Fraction(-4)]
        flux = cumulative_flux(discrepancy)
        self.assertEqual(flux, [Fraction(2), Fraction(-3), Fraction(4)])
        self.assertEqual(path_boundary(flux), discrepancy)

    def test_nonzero_mass_is_rejected(self):
        with self.assertRaises(ValueError):
            cumulative_flux([Fraction(1), Fraction(2)])

    def test_one_vertex_path_convention(self):
        self.assertEqual(cumulative_flux([Fraction(0)]), [])
        self.assertEqual(path_boundary([]), [0])

    def test_discrete_fourier_summation_by_parts(self):
        discrepancy = [Fraction(3), Fraction(-1), Fraction(-4), Fraction(2)]
        nodes = [Fraction(2), Fraction(-3), Fraction(5), Fraction(11)]
        flux = cumulative_flux(discrepancy)
        vertex_pairing = sum((d * z for d, z in zip(discrepancy, nodes)), Fraction(0))
        edge_pairing = sum(
            (flux[j] * (nodes[j] - nodes[j + 1]) for j in range(len(flux))),
            Fraction(0),
        )
        self.assertEqual(vertex_pairing, edge_pairing)


class ProductDivergenceTests(unittest.TestCase):
    def test_mixed_terms_are_coordinate_boundaries(self):
        natural = [Fraction(2), Fraction(3), Fraction(5)]
        flux = [Fraction(7), Fraction(-2)]
        discrepancy = path_boundary(flux)
        self.assertEqual(boundary_first(outer(flux, natural)), outer(discrepancy, natural))
        self.assertEqual(boundary_second(outer(natural, flux)), outer(natural, discrepancy))
        self.assertEqual(
            boundary_second(boundary_first(outer(flux, flux))),
            outer(discrepancy, discrepancy),
        )

    def test_symmetric_square_defect_is_product_divergence(self):
        natural = [Fraction(1, 3), Fraction(2, 5), Fraction(4, 7), Fraction(11, 13)]
        discrepancy = [Fraction(3, 2), Fraction(-7, 3), Fraction(5, 6), Fraction(0)]
        discrepancy[-1] = -sum(discrepancy[:-1], Fraction(0))
        flux = cumulative_flux(discrepancy)
        self.assertEqual(
            symmetric_square_defect(natural, discrepancy),
            product_divergence_defect(natural, flux),
        )

    def test_two_channel_polarization_matches_three_term_expansion(self):
        natural = [Fraction(2, 7), Fraction(3, 11), Fraction(5, 13)]
        discrepancy = [Fraction(4, 9), Fraction(-1, 6), Fraction(-5, 18)]
        flux = cumulative_flux(discrepancy)
        expected = symmetric_square_defect(natural, discrepancy)
        self.assertEqual(polarized_symmetric_square_defect(natural, discrepancy), expected)
        self.assertEqual(polarized_product_divergence_defect(natural, flux), expected)

    def test_product_divergences_cover_the_one_vertex_path(self):
        natural = [Fraction(7, 9)]
        discrepancy = [Fraction(0)]
        expected = [[Fraction(0)]]
        self.assertEqual(symmetric_square_defect(natural, discrepancy), expected)
        self.assertEqual(product_divergence_defect(natural, []), expected)
        self.assertEqual(polarized_product_divergence_defect(natural, []), expected)

    def test_semiprime_diagonal_formula_matches_direct_unordered_sum(self):
        discrepancy = [Fraction(2, 5), Fraction(-1, 3), Fraction(7, 11)]
        summed = [Fraction(5, 7), Fraction(3, 2), Fraction(4, 9)]
        direct = sum(
            (discrepancy[i] * summed[i]) ** 2 for i in range(len(discrepancy))
        )
        direct += sum(
            (
                discrepancy[i] * summed[j]
                + discrepancy[j] * summed[i]
            ) ** 2
            for i in range(len(discrepancy))
            for j in range(i + 1, len(discrepancy))
        )
        self.assertEqual(semiprime_difference_diagonal(discrepancy, summed), direct)


class AdapterAndDualTests(unittest.TestCase):
    def test_negative_adapter_loss_is_rejected(self):
        with self.assertRaises(ValueError):
            AdapterLoss(exponent_loss=Fraction(-1, 100))

    def test_adapter_losses_compose_and_boolean_debt_is_monotone(self):
        first = AdapterLoss(
            exponent_loss=Fraction(1, 100),
            forgotten_fields=frozenset({"mask"}),
        )
        second = AdapterLoss(
            exponent_loss=Fraction(1, 200),
            complexity_exponent=Fraction(1, 10),
            forgotten_fields=frozenset({"source"}),
        )
        total = first.then(second)
        self.assertEqual(total.exponent_loss, Fraction(3, 200))
        self.assertEqual(total.forgotten_fields, frozenset({"mask", "source"}))
        self.assertFalse(
            total.fits(
                exponent_budget=Fraction(1, 50),
                complexity_budget=Fraction(1, 10),
                required_fields={"mask"},
            )
        )

    def test_a_certified_reconstruction_can_discharge_boolean_debt(self):
        forget_mask = AdapterLoss(forgotten_fields=frozenset({"mask", "source"}))
        reconstruct_mask = AdapterLoss(certified_recoveries=frozenset({"mask"}))
        total = forget_mask.then(reconstruct_mask)
        self.assertEqual(total.forgotten_fields, frozenset({"source"}))
        self.assertEqual(total.certified_recoveries, frozenset({"mask"}))

    def test_a_later_forgetting_reopens_a_recovered_field(self):
        recover_mask = AdapterLoss(certified_recoveries=frozenset({"mask"}))
        forget_mask = AdapterLoss(forgotten_fields=frozenset({"mask"}))
        total = recover_mask.then(forget_mask)
        self.assertEqual(total.forgotten_fields, frozenset({"mask"}))
        self.assertEqual(total.certified_recoveries, frozenset())

    def test_forget_recover_forget_composition_is_associative(self):
        forget = AdapterLoss(forgotten_fields=frozenset({"mask"}))
        recover = AdapterLoss(certified_recoveries=frozenset({"mask"}))
        forget_again = AdapterLoss(forgotten_fields=frozenset({"mask"}))
        self.assertEqual(
            forget.then(recover).then(forget_again),
            forget.then(recover.then(forget_again)),
        )

    def test_field_obligation_composition_is_exhaustively_associative(self):
        steps = [
            AdapterLoss(),
            AdapterLoss(forgotten_fields=frozenset({"mask"})),
            AdapterLoss(certified_recoveries=frozenset({"mask"})),
        ]
        for first in steps:
            for second in steps:
                for third in steps:
                    self.assertEqual(
                        first.then(second).then(third),
                        first.then(second.then(third)),
                    )

    def test_finite_atomic_dual_lower_bound(self):
        target = [Fraction(3), Fraction(-2)]
        functional = [Fraction(1), Fraction(-1)]
        atoms = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
        valid, lower_bound = finite_dual_certificate(
            target, functional, atoms, [Fraction(1), Fraction(1)]
        )
        self.assertTrue(valid)
        self.assertEqual(lower_bound, Fraction(5))

    def test_negative_atomic_gauge_cost_is_rejected(self):
        with self.assertRaises(ValueError):
            finite_dual_certificate(
                [Fraction(1)],
                [Fraction(1)],
                [[Fraction(1)]],
                [Fraction(-1)],
            )


if __name__ == "__main__":
    unittest.main()
