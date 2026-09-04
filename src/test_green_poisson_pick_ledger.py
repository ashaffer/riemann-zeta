import math

from green_poisson_pick_ledger import (
    binomial_screen_exponent,
    conditional_green_bill,
    count_compatible_c,
    kernel_switch,
    positive_part_integral,
    positive_root,
    reflected_pair_cap,
)


def test_green_poisson_certificate_constants():
    assert math.isclose(kernel_switch(), 0.43204937989385733, rel_tol=1e-14)
    assert math.isclose(positive_root(), 3.2048162900, rel_tol=2e-10)
    assert math.isclose(positive_part_integral(), 1.3889415384, rel_tol=2e-10)
    assert conditional_green_bill() < 0.298008745


def test_integrated_reflected_pair_crossing():
    c = count_compatible_c()
    assert math.isclose(c, 0.004654164543974, rel_tol=2e-12)
    assert math.isclose(2.0 * c, reflected_pair_cap(c), rel_tol=2e-13)


def test_actual_count_compatible_screen_is_below_both_reserves():
    exponent = binomial_screen_exponent(count_compatible_c())
    assert math.isclose(exponent, 0.011185123086299, rel_tol=2e-12)
    assert exponent < 0.0119000134
    assert exponent < 0.3234 - conditional_green_bill()
