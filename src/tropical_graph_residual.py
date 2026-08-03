"""Fail-fast test for the naive graphic-matroid model of the Weil form.

In the localized hat basis the prime matrix P has nonnegative entries.  Put
D = diag(P 1).  Then -P = (D-P)-D, where D-P is the weighted graph
Laplacian.  This script tests whether the non-prime part B=Q+P dominates D.
If B-D were positive, ordinary graphic Hodge/Laplacian positivity would prove
Q positive.  A negative residual shows that a successful tropical model must
encode more than the prime adjacency graph.
"""
from __future__ import annotations

import argparse

import numpy as np

from weil_core import build_form, lam_min_of


def checkpoint(support: float, dimension: int, cutoff: float, samples: int):
    q, gram, extra = build_form(support, dimension, R=cutoff, K=samples)
    prime = extra["P"]
    degree = np.diag(prime.sum(axis=1))
    laplacian = degree - prime
    nonprime = q + prime
    residual = nonprime - degree
    return (
        lam_min_of(q, gram),
        lam_min_of(residual, gram),
        np.linalg.eigvalsh(laplacian)[0],
        np.max(np.diag(degree)),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--supports", nargs="+", type=float,
                        default=[1.75, 2.485, 2.996, 3.555])
    parser.add_argument("--dimension", type=int, default=31)
    parser.add_argument("--arch-cutoff", type=float, default=500.0)
    parser.add_argument("--arch-samples", type=int, default=60000)
    args = parser.parse_args()

    print("L,m,min_weil,min_residual,min_graph_laplacian,max_degree")
    for support in args.supports:
        values = checkpoint(support, args.dimension,
                            args.arch_cutoff, args.arch_samples)
        print(f"{support:.9g},{args.dimension}," +
              ",".join(f"{value:.12e}" for value in values))


if __name__ == "__main__":
    main()
