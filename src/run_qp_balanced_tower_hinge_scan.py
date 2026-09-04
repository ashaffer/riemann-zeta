"""Scan persistent transpose-quotiented hinge correlations."""

from __future__ import annotations

import argparse

from qp_balanced_tower_alias_gram import transpose_hinge_correlation_audit


FAMILIES = {
    "A": ((24, 48, 72, 96, 120, 144), lambda F: (7 * F // 8, F, 7 * F // 6)),
    "B": ((40, 80, 120, 160), lambda F: (F, 9 * F // 8, 6 * F // 5)),
    "C": ((36, 72, 108, 144), lambda F: (5 * F // 6, F, 10 * F // 9)),
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--family", choices=("A", "B", "C", "all"), default="all")
    arguments = parser.parse_args()
    families = FAMILIES if arguments.family == "all" else {
        arguments.family: FAMILIES[arguments.family]
    }
    print("family\tF\tR\tK\tlanes\texact_alias\traw_corr\tresidual_corr")
    for family, (scales, lanes_at_scale) in families.items():
        for F in scales:
            audit = transpose_hinge_correlation_audit(F, lanes_at_scale(F))
            print(
                f"{family}\t{F}\t{audit.R}\t{audit.K}\t{audit.lane_triple}\t"
                f"{audit.exact_cross_alias_mass}\t"
                f"{audit.raw_absolute_correlation:.12f}\t"
                f"{audit.alias_removed_absolute_correlation:.12f}",
                flush=True,
            )


if __name__ == "__main__":
    main()

