#!/usr/bin/env python3
"""Cross-check Lean, Markdown, canonical Z23C, JSON, and Z23V projections."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
CONTEXT = RESULTS / "context"
sys.path.insert(0, str(ROOT / "src"))

import zeta23_correction_context as correction_context


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    packet = correction_context.load_verified()
    require(packet["schema"] == "zeta23_correction_bundle_v1", "schema drift")
    require(packet["date"] == "2026-09-04", "bundle date drift")

    report_path = (ROOT / packet["human_authority"]).resolve()
    require(report_path.is_file(), "human authority missing")
    report = report_path.read_text(encoding="utf-8")

    correction_ids = packet["sync_contract"]["correction_ids"]
    actual_ids = [item["id"] for item in packet["corrections"]]
    require(actual_ids == correction_ids, "correction ID order/set drift")
    for correction_id in correction_ids:
        require(f"### {correction_id} " in report, f"Markdown section missing for {correction_id}")

    lean_texts = []
    for relative in packet["lean_authorities"]:
        path = ROOT / relative
        require(path.is_file(), f"Lean authority missing: {relative}")
        lean_texts.append(path.read_text(encoding="utf-8"))
    lean = "\n".join(lean_texts)
    compact_source_theorems = {
        "r71_source_derivative_algebra",
        "shifted_source_derivative_algebra",
        "pole_killed_ramp_multiplier_algebra",
        "causal_ramp_boundary_correction",
        "fixed_sign_lower_of_abs",
    }
    split_closeout_theorems = {
        "fourthRoot_unweighted_partialFraction",
        "fourthRoot_inverseWeighted_partialFraction",
        "twoSided_counterterm_cancel",
        "localCompletion_after_counterterm",
        "weakRadical_iff_operatorKernel",
        "weakRadical_readout_iff_kernelNullCharge",
    }
    for correction in packet["corrections"]:
        namespace = {
            "C08": "RHBridge.S1B1CompletedSourceCommutator",
            "C15": "RHBridge.QPSourceFiberBifurcation",
            "C16": "RHBridge.ExteriorFactorizationAudit",
            "C17": "RHBridge.CompletedSourceConstructiveSearch",
            "C18": "RHBridge.FourCauchyGlobalCompatibility",
            "C19": "RHBridge.R71MinorArcTriage",
            "C20": "RHBridge.R188PrincipalBandSerialization",
        }.get(correction["id"], "RHBridge.CorrectionGuards")
        for theorem in correction["lean"]:
            theorem_namespace = (
                "RHBridge.CompactSourceDerivativeBridge"
                if correction["id"] == "C17" and theorem in compact_source_theorems
                else (
                    "RHBridge.SplitCarlemanFormDomainCloseout"
                    if correction["id"] == "C18" and theorem in split_closeout_theorems
                    else namespace
                )
            )
            require(f"theorem {theorem}" in lean, f"Lean theorem missing: {theorem}")
            require(
                f"#print axioms {theorem_namespace}.{theorem}" in lean,
                f"axiom audit missing: {theorem}",
            )

    aggregate = (ROOT / "lean/rhbridge/RHBridge.lean").read_text(encoding="utf-8")
    require("import RHBridge.CorrectionGuards" in aggregate, "Lean aggregate import missing")
    require(
        "import RHBridge.S1B1CompletedSourceCommutator" in aggregate,
        "S1-B1 Lean aggregate import missing",
    )
    require(
        "import RHBridge.QPSourceFiberBifurcation" in aggregate,
        "QP source-fiber Lean aggregate import missing",
    )
    require(
        "import RHBridge.ExteriorFactorizationAudit" in aggregate,
        "exterior-factorization Lean aggregate import missing",
    )
    require(
        "import RHBridge.CompletedSourceConstructiveSearch" in aggregate
        and "import RHBridge.CompactSourceDerivativeBridge" in aggregate,
        "R184 Lean aggregate import missing",
    )
    require(
        "import RHBridge.FourCauchyGlobalCompatibility" in aggregate,
        "R185 Lean aggregate import missing",
    )
    require(
        "import RHBridge.SplitCarlemanFormDomainCloseout" in aggregate,
        "R186 Lean aggregate import missing",
    )
    require(
        "import RHBridge.R71MinorArcTriage" in aggregate,
        "R187 Lean aggregate import missing",
    )
    require(
        "import RHBridge.R188PrincipalBandSerialization" in aggregate,
        "R188 Lean aggregate import missing",
    )
    require("0<eta<=1/2" in report, "Markdown eta domain missing")
    require("kappa_half_in_strip_domain" in report, "Markdown/Lean domain link missing")
    require(
        "zeta23_correction_bundle_v1.zctx" in report and "Z23V/1" in report,
        "Markdown rapid-resumption projection missing",
    )
    zctx_size = correction_context.SOURCE.stat().st_size
    json_size = correction_context.JSON_MIRROR.stat().st_size
    vector_size = correction_context.VECTOR_INDEX.stat().st_size
    require(
        f"current size it is `{zctx_size}`\nbytes, versus `{json_size}` bytes" in report,
        "Markdown Z23C/JSON size observation drift",
    )
    with correction_context.Z23VReader(correction_context.VECTOR_INDEX) as reader:
        correction_context._query_lines(reader, ["C02"])
        c02_bytes = reader.bytes_read
    with correction_context.Z23VReader(correction_context.VECTOR_INDEX) as reader:
        correction_context._reload_vector_lines(reader, "resume")
        resume_bytes = reader.bytes_read
    require(
        f"C02 query reads `{c02_bytes}/{vector_size}`" in report
        and f"`resume` vector reads `{resume_bytes}/{vector_size}`" in report,
        "Markdown selective-read observation drift",
    )
    require(
        "canonical `Z23C/1` compact ledger" in lean
        and "random-access `Z23V/1` working-state vector" in lean,
        "Lean scope comment does not match compact/runtime projections",
    )
    require(
        "`signed_coefficients_positive_aggregate`, and derives" in report,
        "Markdown must identify both the explicit C01 witness and its consequence",
    )
    require(
        "numeric/algebraic ledger guard" in report and "does not type the R116 analytic object" in report,
        "Markdown overstates the formal scope of C05",
    )
    c05 = next(item for item in packet["corrections"] if item["id"] == "C05")
    require(
        c05["formal_scope"]
        == "CONDITIONAL_NUMERIC_ALGEBRAIC_EXPONENT_LEDGER_ONLY_NOT_AN_R116_OBJECT_TYPE",
        "compact packet overstates the formal scope of C05",
    )
    verification = packet["verification"]
    require(
        verification["synchronization_verifier"] == "PASS_20_CORRECTION_IDS"
        and verification["current_authority_manifest_verifier"]
        == "PASS_6_ROLE_LABELED_ARTIFACTS",
        "recorded verifier status drift",
    )
    require(
        "focused Python baseline passed `129` tests" in report
        and verification["focused_pytest"] == "PASS_129_POST_R187",
        "recorded focused-suite result drift",
    )
    require(
        "full Python suite passed `2428` tests in `71.78s`" in report
        and verification["full_pytest"] == "PASS_2428_IN_71.78_SECONDS",
        "recorded full-suite result drift",
    )
    require(
        "full\nLean aggregate completed successfully (`13470` jobs)" in report
        and verification["lean_aggregate"] == "PASS_13470_JOBS",
        "recorded Lean-build result drift",
    )
    require(
        packet["global_status"]["uniform_zero_free_strip"] == "OPEN"
        and packet["global_status"]["riemann_hypothesis"] == "OPEN",
        "unsupported global claim",
    )
    require(
        packet["sync_contract"]["nonclaim"] == "NO_ANALYTIC_FIXED_POWER_STRIP_OR_RH_PROOF",
        "bundle nonclaim drift",
    )
    resumption = packet["resumption_state"]
    require(
        resumption["objective"] == "GRAND_RH_IMMEDIATE_UNIFORM_ZERO_FREE_STRIP"
        and resumption["analytic_target"]
        == "COMPLETE_FIXED_WINDOW_R71_FIXED_POWER_BOUND_OR_GLOBALLY_ORIENTED_COMPACT_SOURCE_DERIVATIVE_ONE_SIDED_CONTROL"
        and resumption["route_invariant"]
        == "COMPLETE_R71_FIXED_POWER_BOUND_IS_UNIFORM_STRIP_STRENGTH",
        "rapid-resumption objective/route drift",
    )
    require(
        resumption["active_frontier"]
        == "UNIFORM_STRIP_R71_TARGET_MATCHED_COMPLETED_ACTUAL_COEFFICIENT_COLLAR_Q_GT_X^(499/500)_ABS_A_LE_X^(1/400)_V_PHYS_LE_X^(1/500+o(1))_WITH_FULL_PROJECTOR_AND_CENTER_COMPLETION"
        and "R188_EXACT_FINITE_GAMMA_AFFINE_SERIALIZATION_LOW_COFACTOR_SUPPRESSION_AND_TARGET_MATCHED_FIFTH_ORDER_COLLAR_CLOSED"
        in resumption["frontier_status"]
        and "FIELD_ERROR_X^(49/100+o(1))_ONLY_EXPONENT_EQUIVALENT"
        in resumption["frontier_status"]
        and "NATURAL_SEMIPRIME_SUBFIELD_AND_R105_TOP_BOX" in resumption["frontier_status"]
        and "COMPONENTWISE_WRIGHT_R87_FAILS" in resumption["frontier_status"]
        and "FULL_GLOBALLY_SIGNED_COMPLETED_CORRELATION_REMAINS_STRIP_EQUIVALENT"
        in resumption["frontier_status"]
        and "DIRECT_KNC_REMAINS_OPEN" in resumption["frontier_status"]
        and "QP_TURAN_REMAINS_PARKED" in resumption["frontier_status"],
        "R188 frontier/parking drift",
    )
    c18 = next(item for item in packet["corrections"] if item["id"] == "C18")
    require(
        "SPLIT_CARLEMAN_OLD_SERIALIZATION" in c18["claim"]
        and "WEAK_L2_FORM_DOMAIN_STATE" in c18["claim"]
        and "GENERIC_ENDPOINT_JETS_ARE_UNAVAILABLE" in c18["claim"]
        and "EQUIVALENT_TO_KNC" in c18["remaining"],
        "C18/R186 closeout correction drift",
    )
    require(
        "The previous claim that the global calculation was complete was wrong" in report
        and "minimal state" in report
        and "generic form-domain point values" in report
        and "Both preregistered falsifiers" in report,
        "C18 Markdown does not expose the final closeout",
    )
    require(
        resumption["representation_status"]
        == "LOSSY_WORKING_STATE_NOT_LATENT_ACTIVATIONS_PRIVATE_REASONING_OR_PROOF",
        "rapid-resumption scope drift",
    )
    require(
        packet["reload_vectors"]["resume"] == ["G", "Y", "R", "D", "N"],
        "rapid-resumption vector drift",
    )
    c15 = next(item for item in packet["corrections"] if item["id"] == "C15")
    require(
        c15["formal_scope"]
        == "FINITE_SOURCE_FIBER_ALGEBRA_RATIONAL_EXPONENT_LEDGER_AND_SYNTHETIC_REAL_NODE_MODEL_ONLY_NOT_AN_ACTUAL_PRIME_DPA_LTRAD_STRIP_OR_RH_THEOREM",
        "C15 actual-prime scope drift",
    )
    require(
        "No independently stated quantitative prime invariant emerged" in report
        and "QP/Turán is parked" in report
        and "not an actual-prime counterexample" in report,
        "C15 Markdown scope/decision drift",
    )
    c16 = next(item for item in packet["corrections"] if item["id"] == "C16")
    require(
        c16["formal_scope"]
        == "FINITE_LINEAR_ALGEBRA_SCALAR_POSITIVITY_AND_RESOLVENT_GUARDS_ONLY_NOT_DOUGLAS_SUZUKI_COMPLETED_SOURCE_STRIP_OR_RH",
        "C16 formal-scope drift",
    )
    require(
        "Bare existential\nfactorization is therefore exactly KNC" in report
        and "dense-core wording also needed a guard" in report
        and "strip-to-RH amplifier" in report,
        "C16 Markdown scope/decision drift",
    )
    c17 = next(item for item in packet["corrections"] if item["id"] == "C17")
    require(
        c17["formal_scope"]
        == "FINITE_GEOMETRIC_CAUCHY_PAIRING_COUNTERMODEL_DERIVATIVE_MULTIPLIER_AND_COLLAR_ALGEBRA_ONLY_NOT_ANALYTIC_SUZUKI_HANKEL_LANDAU_TSRC_STRIP_OR_RH",
        "C17 formal-scope drift",
    )
    require(
        "every remainder is exactly `Gamma n`" in report
        and "local triangular Cauchy jump" in report
        and "exact initial collar `-V_delta`" in report
        and "not yet a factor `T^src`" in report,
        "C17 Markdown scope/decision drift",
    )
    c18 = next(item for item in packet["corrections"] if item["id"] == "C18")
    require(
        c18["formal_scope"]
        == "FINITE_SCALAR_PULLBACK_ROOT_PARTIAL_FRACTION_NONCOMMUTATIVE_RING_RATIONAL_GAUSSIAN_RATIONAL_AND_SYNTHETIC_CONTACT_ALGEBRA_ONLY_NOT_ANALYTIC_SUZUKI_FORM_CORE_CARLEMAN_INEQUALITY_KNC_TSRC_STRIP_FOUR_CYCLE_OR_RH",
        "C18 formal-scope drift",
    )
    require(
        "fourth-root rotations and" in report
        and "positive dilations\ncommute globally" in report
        and "two-boundary re-entry defect" in report
        and "completion weights are synthetic" in report
        and "exact rational reciprocal three-node" in report
        and "weak old equation" in report
        and "immediate strip target remains complete" in report,
        "C18 Markdown scope/decision drift",
    )
    c19 = next(item for item in packet["corrections"] if item["id"] == "C19")
    require(
        c19["formal_scope"]
        == "RATIONAL_EXPONENT_AFFINE_MOMENT_SIGNED_RECOMBINATION_AND_FINITE_DFT_GUARDS_ONLY_NOT_FOURIER_GEVREY_BSPLINE_DISPERSION_FIXED_POWER_STRIP_FOUR_CYCLE_OR_RH",
        "C19 formal-scope drift",
    )
    require(
        "### C19" in report
        and "hard difference split" in report
        and "completed additive principal band" in report
        and "joint completed correlation theorem" in report,
        "C19 Markdown scope/decision drift",
    )
    c20 = next(item for item in packet["corrections"] if item["id"] == "C20")
    require(
        c20["formal_scope"]
        == "RATIONAL_EXPONENT_DENOMINATOR_DETERMINANT_AFFINE_AND_COMPLETE_SQUARE_GUARDS_ONLY_NOT_POISSON_FOURIER_PNT_SEMIPRIME_LOWER_BLOCK_MASK_ANALYSIS_WRIGHT_R87_FIXED_POWER_STRIP_FOUR_CYCLE_OR_RH",
        "C20 formal-scope drift",
    )
    require(
        "TARGET_MATCHED_Q_GT_X^(499/500)_ABS_A_LE_X^(1/400)_V_PHYS_LE_X^(1/500+o(1))"
        in c20["remaining"],
        "C20 target-matched open theorem drift",
    )
    require(
        "### C20" in report
        and "exact completion-preserving" in report
        and "low-cofactor suppression" in report
        and "high cofactor is not low determinant" in report
        and "target-matched collar" in report
        and "Q=floor(X^(499/500))" in report
        and "||G_R^pri-G_collar||_infinity" in report
        and "equivalent to the `X^(49/50+o(1))` energy target" in report
        and "This is not a power saving" in report
        and "v_phys<=C X^(1/500)" in report
        and "not the Section-5\nsolution-line Poisson dual" in report
        and "isolated unit-alias\nsubfield" in report
        and "not a\nlower bound for the full completed field" in report
        and "Wright II requires both denominator\nsupports to have relative length `X^(-sigma)`" in report
        and "single globally signed" in report
        and "uniform-strip-equivalent" in report,
        "C20 Markdown scope/decision drift",
    )
    r188_postflight = load(
        CONTEXT / "zeta23_r188_principal_band_serialization_postflight_v1.json"
    )
    require(
        r188_postflight["frozen_target"]["status"] == "OPEN"
        and "q>X^(499/500)" in r188_postflight["proved"]["surviving_geometry"]
        and "0<|a|<=X^(1/400)" in r188_postflight["proved"]["surviving_geometry"]
        and "v_phys<=X^(1/500+o(1))"
        in r188_postflight["proved"]["surviving_geometry"]
        and "v_phys is not the solution-line Poisson dual"
        in r188_postflight["proved"]["surviving_geometry"]
        and "discarded field is O(X^(49/100) log^2 X)"
        in r188_postflight["proved"]["target_matched_collar"]
        and "not a proved power saving"
        in r188_postflight["proved"]["target_matched_collar"]
        and "target-matched collar q>X^(499/500)"
        in r188_postflight["surviving_open_theorem"]
        and "v_phys<=X^(1/500+o(1))"
        in r188_postflight["surviving_open_theorem"]
        and r188_postflight["verification"]["focused_r188_python"] == "PASS_7"
        and r188_postflight["verification"]["combined_r187_r188_python"] == "PASS_14"
        and "uniform zero-free strip" in r188_postflight["nonclaim"],
        "R188 postflight/open-status drift",
    )

    for source in packet["sources"]:
        require((ROOT / source).is_file(), f"bundle source missing: {source}")

    import zeta23_proof_tree as proof_tree

    route = proof_tree.current_routing_packet()
    require(route["global_status"]["uniform_zero_free_strip"] == "OPEN", "route strip drift")
    require(route["global_status"]["riemann_hypothesis"] == "OPEN", "route RH drift")

    frozen = load(CONTEXT / "zeta23_recursive_fixed_point_postflight_v1.json")
    require(
        frozen["status"] == "HISTORICAL_COMPLETE_SNAPSHOT_UNATTACHED",
        "V4 unattached-snapshot correction drift",
    )
    require(
        frozen["frozen_terminal_snapshot"]["snapshot_scope"]
        == "HISTORICAL_UNATTACHED_DIGESTS",
        "V4 snapshot scope drift",
    )

    print(
        f"PASS: synchronized correction bundle ({len(correction_ids)} IDs; "
        "Z23C source + JSON mirror + Z23V index)"
    )
    print("NOTE: finite guards only; uniform strip and RH remain open")


if __name__ == "__main__":
    main()
