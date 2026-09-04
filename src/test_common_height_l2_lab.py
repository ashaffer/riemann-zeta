import unittest

from common_height_l2_lab import summarize


class CommonHeightL2LabTests(unittest.TestCase):
    def test_bands_first_projection(self) -> None:
        payload = {
            "rows": [
                {
                    "Y": 100,
                    "H": 10,
                    "height_exponent": 1.0,
                    "block_id": 0,
                    "logarithmic_normalized_real": 0.1,
                    "logarithmic_normalized_imag": 0.0,
                },
                {
                    "Y": 100,
                    "H": 10,
                    "height_exponent": 1.0,
                    "block_id": 0,
                    "logarithmic_normalized_real": 0.2,
                    "logarithmic_normalized_imag": 0.0,
                },
                {
                    "Y": 100,
                    "H": 10,
                    "height_exponent": 1.0,
                    "block_id": 1,
                    "logarithmic_normalized_real": 0.0,
                    "logarithmic_normalized_imag": 0.4,
                },
            ]
        }
        row = summarize(payload)[0]
        self.assertEqual(row["sampled_blocks"], 2)
        self.assertAlmostEqual(row["mean_normalized_square"], (0.3**2 + 0.4**2) / 2)
        self.assertAlmostEqual(row["projected_l2"], 100 * 10 * (0.3**2 + 0.4**2) / 2)


if __name__ == "__main__":
    unittest.main()
