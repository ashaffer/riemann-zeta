import unittest

from ward_nonlocal_covariance_probe import audit_nonlocal_covariance


class WardNonlocalCovarianceProbeTests(unittest.TestCase):
    def test_complete_remainder_closes_and_has_multiple_products(self) -> None:
        audit = audit_nonlocal_covariance()
        self.assertGreater(audit.active_tail_products, 20)
        self.assertGreater(audit.active_central_semiprimes, 10)
        self.assertLess(abs(audit.covariance_closure_error), 2.0e-12)
        self.assertLess(abs(audit.coordinate_polarization_error), 2.0e-12)

    def test_positive_supply_and_full_domination_fail(self) -> None:
        audit = audit_nonlocal_covariance()
        self.assertGreater(audit.missing_ward_covariance, 0.05)
        self.assertLess(audit.positive_supply_margin, -0.1)
        self.assertLess(
            audit.innovation_dominates_connected_margin,
            -0.1,
        )

    def test_observed_negative_remainder_is_exact_head_polarization(self) -> None:
        audit = audit_nonlocal_covariance()
        self.assertGreater(audit.negative_supply_margin, 0.1)
        self.assertLess(audit.exact_full_innovation, 1.0e-3)
        self.assertLess(
            abs(
                audit.global_covariance_remainder
                - audit.exact_head_global_remainder
                - audit.euler_innovation_correction
            ),
            2.0e-12,
        )

    def test_quadrature_refinement_preserves_all_decisive_signs(self) -> None:
        coarse = audit_nonlocal_covariance(gaussian_order=12)
        fine = audit_nonlocal_covariance(gaussian_order=20)
        fields = (
            "global_covariance_remainder",
            "missing_ward_covariance",
            "full_innovation",
            "retained_nonlocal_remainder",
        )
        for field in fields:
            self.assertLess(
                abs(getattr(coarse, field) - getattr(fine, field)),
                2.0e-10,
            )

    def test_small_complete_model_kills_all_four_natural_orientations(self) -> None:
        # This is inside the k=1 Vaughan endpoint geometry:
        # floor(76^(3/8)) = 5 and 5^2 < 76*exp(-0.05).
        audit = audit_nonlocal_covariance(
            scale=76.0,
            cutoff=5,
            step=0.05,
            input_order=1,
            macro_order=1,
            gaussian_order=16,
        )
        self.assertEqual(audit.active_tail_product_values, (70, 77, 78))
        self.assertEqual(audit.active_central_semiprime_values, (77,))
        self.assertLess(audit.positive_supply_margin, 0.0)
        self.assertLess(audit.negative_supply_margin, 0.0)
        self.assertLess(audit.innovation_dominates_connected_margin, 0.0)
        self.assertLess(audit.retained_cancels_connected_margin, 0.0)
        # Replacing the exact head by its explicit smooth evaluation reverses
        # the sign of G in this complete model.
        self.assertGreater(audit.exact_head_global_remainder, 0.02)
        self.assertLess(audit.global_covariance_remainder, -0.007)

    def test_small_counterexample_is_quadrature_stable(self) -> None:
        arguments = dict(
            scale=76.0,
            cutoff=5,
            step=0.05,
            input_order=1,
            macro_order=1,
        )
        coarse = audit_nonlocal_covariance(**arguments, gaussian_order=8)
        fine = audit_nonlocal_covariance(**arguments, gaussian_order=24)
        for field in (
            "global_covariance_remainder",
            "missing_ward_covariance",
            "full_innovation",
            "retained_cancels_connected_margin",
        ):
            self.assertLess(
                abs(getattr(coarse, field) - getattr(fine, field)),
                2.0e-12,
            )

    def test_larger_cutoff_complete_replication(self) -> None:
        audit = audit_nonlocal_covariance(
            scale=1200.0,
            cutoff=14,
            step=0.05,
            input_order=1,
            macro_order=1,
            gaussian_order=12,
        )
        self.assertEqual(audit.active_tail_products, 44)
        self.assertEqual(audit.active_central_semiprimes, 9)
        self.assertLess(audit.positive_supply_margin, 0.0)
        self.assertLess(audit.negative_supply_margin, 0.0)
        self.assertLess(audit.innovation_dominates_connected_margin, 0.0)
        self.assertLess(audit.retained_cancels_connected_margin, 0.0)


if __name__ == "__main__":
    unittest.main()
