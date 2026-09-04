"""Command-line scan for the exact balanced-tower alias Gram audit."""

from __future__ import annotations

import argparse

from qp_balanced_tower_alias_gram import (
    balanced_tower_alias_gram_audit,
    decode_packet_pair,
)


def _packet_name(packet_id: int, lanes: tuple[int, ...]) -> str:
    left, right = decode_packet_pair(packet_id, len(lanes))
    return f"({lanes[left]},{lanes[right]})"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--F-values",
        type=int,
        nargs="+",
        default=(6, 8, 10, 12, 16, 20, 24, 28, 32, 36, 40, 44),
    )
    parser.add_argument(
        "--no-spectrum",
        action="store_true",
        help="skip the whitened residual eigenvalue computation",
    )
    parser.add_argument(
        "--transpose-quotient",
        action="store_true",
        help="report columns G_(a,b)+G_(b,a), with diagonal columns once",
    )
    arguments = parser.parse_args()
    if arguments.transpose_quotient:
        print(
            "F\tR\tq\tK\tlanes\tpoints\tcolumns\tM/target\tPS/target\t"
            "M/PS\talias/PS\tresidual/PS\trho\trow_l1\tmaxcorr\twitness"
        )
    else:
        print(
            "F\tR\tq\tK\tlanes\tpoints\tM/target\tPS/target\tM/PS\t"
            "alias/PS\tresidual/PS\trho\trow_l1\tmaxcorr\twitness"
        )
    for F in arguments.F_values:
        audit = balanced_tower_alias_gram_audit(
            F, compute_spectrum=not arguments.no_spectrum
        )
        if arguments.transpose_quotient:
            diagnostic = audit.transpose_quotient
            witness = "~".join(
                str(audit.transpose_quotient_columns[column_id])
                for column_id in diagnostic.maximum_correlation_column_ids
            )
            print(
                f"{audit.F}\t{audit.R}\t{audit.q}\t{audit.K}\t"
                f"{len(audit.lane_parameters)}\t{audit.point_count}\t"
                f"{diagnostic.column_count}\t{audit.normalized_total_mass:.9f}\t"
                f"{diagnostic.normalized_packet_diagonal_mass:.9f}\t"
                f"{diagnostic.translate_aggregation_ratio:.9f}\t"
                f"{diagnostic.exact_cross_alias_over_diagonal:.9f}\t"
                f"{diagnostic.signed_nonalias_cross_over_diagonal:.9f}\t"
                f"{diagnostic.whitened_residual_spectral_radius:.9f}\t"
                f"{diagnostic.whitened_residual_maximum_absolute_row_sum:.9f}\t"
                f"{diagnostic.maximum_absolute_pair_correlation:.9f}\t{witness}",
                flush=True,
            )
        else:
            witness = "~".join(
                _packet_name(packet_id, audit.lane_parameters)
                for packet_id in audit.maximum_correlation_packet_pair_ids
            )
            print(
                f"{audit.F}\t{audit.R}\t{audit.q}\t{audit.K}\t"
                f"{len(audit.lane_parameters)}\t{audit.point_count}\t"
                f"{audit.normalized_total_mass:.9f}\t"
                f"{audit.normalized_packet_pair_diagonal_mass:.9f}\t"
                f"{audit.translate_aggregation_ratio:.9f}\t"
                f"{audit.exact_cross_alias_over_diagonal:.9f}\t"
                f"{audit.signed_nonalias_cross_over_diagonal:.9f}\t"
                f"{audit.whitened_residual_spectral_radius:.9f}\t"
                f"{audit.whitened_residual_maximum_absolute_row_sum:.9f}\t"
                f"{audit.maximum_absolute_pair_correlation:.9f}\t{witness}",
                flush=True,
            )


if __name__ == "__main__":
    main()
