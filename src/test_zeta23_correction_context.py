"""Regression and hostile-mutation tests for Z23C/Z23V context resumption."""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

import zeta23_correction_context as zctx
import zeta23_vector_context as zvec


def source_text() -> str:
    return zctx.SOURCE.read_text(encoding="utf-8")


def test_z23c_roundtrip_and_generated_mirrors_are_exact() -> None:
    data = zctx.load_verified()
    encoded = zctx.render_zctx(data).encode("utf-8")
    assert encoded == zctx.SOURCE.read_bytes()

    vector = zctx._vector_bytes(data, encoded)
    assert vector == zctx.VECTOR_INDEX.read_bytes()
    assert zctx.mirror_json_bytes(data, encoded, vector) == zctx.JSON_MIRROR.read_bytes()
    assert zctx.SOURCE.stat().st_size < zctx.JSON_MIRROR.stat().st_size


def test_z23v_is_deterministic_under_json_key_reordering() -> None:
    data = zctx.parse_zctx(source_text())
    reordered = dict(reversed(list(data.items())))
    source_digest = hashlib.sha256(zctx.SOURCE.read_bytes()).hexdigest()
    semantic_digest = zctx.semantic_sha256(data)
    assert zvec.encode_z23v(
        data, source_sha256=source_digest, semantic_sha256=semantic_digest
    ) == zvec.encode_z23v(
        reordered, source_sha256=source_digest, semantic_sha256=semantic_digest
    )


def test_single_correction_query_reads_only_selected_vector_payload(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def forbid_whole_file_read(*_: object, **__: object) -> bytes:
        raise AssertionError("selected query attempted Path.read_bytes")

    monkeypatch.setattr(Path, "read_bytes", forbid_whole_file_read)
    with zvec.Z23VReader(zctx.VECTOR_INDEX) as reader:
        seen: list[tuple[int, int]] = []
        original = reader.vector

        def recording_vector(kind: int, key: int = 0) -> list[int]:
            seen.append((kind, key))
            return original(kind, key)

        monkeypatch.setattr(reader, "vector", recording_vector)
        rendered = zctx._query_lines(reader, ["C02"])
        assert "R125_RAW_RESPONSE" in rendered
        assert "NO_ANALYTIC_FIXED_POWER_STRIP_OR_RH_PROOF" in rendered
        assert (zvec.K_CORRECTION, 2) in seen
        assert not any(
            kind == zvec.K_CORRECTION and key != 2 for kind, key in seen
        )
        assert reader.bytes_read < reader.file_size // 3


def test_resume_vector_is_small_lossy_working_state_with_global_guards() -> None:
    with zvec.Z23VReader(zctx.VECTOR_INDEX) as reader:
        rendered = zctx._reload_vector_lines(reader, "resume")
        assert "GRAND_RH_IMMEDIATE_UNIFORM_ZERO_FREE_STRIP" in rendered
        assert "COMPLETE_FIXED_WINDOW_R71_FIXED_POWER_BOUND" in rendered
        assert "R187_MELLIN_DIFFERENCE_AND_ADDITIVE_TAILS_CLOSED" in rendered
        assert "FULL_GLOBALLY_SIGNED_COMPLETED_CORRELATION_REMAINS_STRIP_EQUIVALENT" in rendered
        assert "COMPONENTWISE_WRIGHT_R87_FAILS" in rendered
        assert "DIRECT_KNC_REMAINS_OPEN" in rendered
        assert "UNIFORM_STRIP_R71_TARGET_MATCHED_COMPLETED_ACTUAL_COEFFICIENT_COLLAR" in rendered
        assert "Q_GT_X^(499/500)_ABS_A_LE_X^(1/400)_V_PHYS_LE_X^(1/500+o(1))" in rendered
        assert "NO_TARGET_MATCHED_FIFTH_ORDER_COLLAR_AS_A_POWER_SAVING" in rendered
        assert "QP_TURAN_SINGLE_SOURCE_FIBER_BIFURCATION" not in rendered
        assert "LOSSY_WORKING_STATE_NOT_LATENT_ACTIVATIONS_PRIVATE_REASONING_OR_PROOF" in rendered
        assert "MAX_INFORMATION_GAIN_SUBJECT_TO_FULL_PASSPORT" in rendered
        assert "NO_STRIP_TO_RH_WITHOUT_NEW_AMPLIFIER" in rendered
        assert "NO_ANALYTIC_FIXED_POWER_STRIP_OR_RH_PROOF" in rendered
        assert "SIGNED_COEFFICIENT_REPRESENTATION" not in rendered
        assert reader.bytes_read < 3 * reader.file_size // 4


@pytest.mark.parametrize(
    "mutate",
    [
        lambda text: text.replace("C\tC02\t", "C\tC01\t", 1),
        lambda text: text.replace("I\tQ_H_ZERO_FAITHFULNESS", "ZZ\tQ_H_ZERO_FAITHFULNESS", 1),
        lambda text: text.replace("@R:ZETA23-REMAINING", "=../ZETA23-REMAINING", 1),
        lambda text: text.replace("Q_H_ZERO_FAITHFULNESS", "Q_H_ZERO_FAITHFULNESS\\q", 1),
        lambda text: text.rsplit("X\t", 1)[0],
        lambda text: text + "I\tTRAILING_AFTER_DIGEST\n",
    ],
)
def test_z23c_hostile_mutations_fail_closed(mutate: object) -> None:
    with pytest.raises(zctx.ContextFormatError):
        zctx.parse_zctx(mutate(source_text()))  # type: ignore[operator]


def _corrupt_record(vector: bytes, kind: int, key: int, tmp_path: Path) -> Path:
    original = tmp_path / "original.z23v"
    original.write_bytes(vector)
    with zvec.Z23VReader(original) as reader:
        offset, length, _ = reader._find_entry(kind, key)
    assert length > 0
    damaged = bytearray(vector)
    damaged[offset] ^= 1
    path = tmp_path / f"damaged-{kind}-{key}.z23v"
    path.write_bytes(damaged)
    return path


def test_unselected_corruption_is_isolated_but_full_verify_fails(tmp_path: Path) -> None:
    damaged = _corrupt_record(
        zctx.VECTOR_INDEX.read_bytes(), zvec.K_CORRECTION, 15, tmp_path
    )
    with zvec.Z23VReader(damaged) as reader:
        assert reader.correction("C02")["id"] == "C02"
    with zvec.Z23VReader(damaged) as reader:
        with pytest.raises(zvec.VectorFormatError, match="body SHA-256 mismatch"):
            reader.verify_full()


def test_selected_corruption_fails_its_record_digest(tmp_path: Path) -> None:
    damaged = _corrupt_record(
        zctx.VECTOR_INDEX.read_bytes(), zvec.K_CORRECTION, 2, tmp_path
    )
    with zvec.Z23VReader(damaged) as reader:
        with pytest.raises(zvec.VectorFormatError, match="digest mismatch"):
            reader.correction("C02")


def test_full_vector_projection_equals_canonical_semantics() -> None:
    expected = zctx.parse_zctx(source_text())
    with zvec.Z23VReader(zctx.VECTOR_INDEX) as reader:
        assert reader.verify_full() == expected
        assert reader.source_sha256.hex() == hashlib.sha256(
            zctx.SOURCE.read_bytes()
        ).hexdigest()
        assert reader.semantic_sha256.hex() == zctx.semantic_sha256(expected)


def test_named_reload_vectors_have_stable_membership() -> None:
    with zvec.Z23VReader(zctx.VECTOR_INDEX) as reader:
        vectors = reader.reload_vectors()
    assert vectors["resume"] == ["G", "Y", "R", "D", "N"]
    assert vectors["formal"] == [
        "G", "Y", "C01", "C02", "C03", "C04", "C05", "C08", "C15",
        "C16", "C17", "C18", "C19", "C20", "V"
    ]
    assert vectors["all"] == ["*"]
