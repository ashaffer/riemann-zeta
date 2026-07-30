import RHBridge.P2RoundedFactorCheckpoint20
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck20_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel20FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel20FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel20TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel20FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel20FlatEven0_eq
  · exact panel20FlatEven1_eq
  · exact panel20FlatEven2_eq
  · exact panel20FlatEven3_eq
  · exact panel20FlatEven4_eq
  · exact panel20FlatEven5_eq
  · exact panel20FlatEven6_eq
  · exact panel20FlatEven7_eq
  · exact panel20FlatEven8_eq
  · exact panel20FlatEven9_eq
  · exact panel20FlatEven10_eq
  · exact panel20FlatEven11_eq
  · exact panel20FlatEven12_eq
  · exact panel20FlatEven13_eq
  · exact panel20FlatEven14_eq
  · exact panel20FlatEven15_eq
  · exact panel20FlatEven16_eq
  · exact panel20FlatEven17_eq
  · exact panel20FlatEven18_eq
  · exact panel20FlatEven19_eq
  · exact panel20FlatEven20_eq
  · exact panel20FlatEven21_eq
  · exact panel20FlatEven22_eq
  · exact panel20FlatEven23_eq

theorem panel20FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel20FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel20FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel20FlatOdd0_eq
  · exact panel20FlatOdd1_eq
  · exact panel20FlatOdd2_eq
  · exact panel20FlatOdd3_eq
  · exact panel20FlatOdd4_eq
  · exact panel20FlatOdd5_eq
  · exact panel20FlatOdd6_eq
  · exact panel20FlatOdd7_eq
  · exact panel20FlatOdd8_eq
  · exact panel20FlatOdd9_eq
  · exact panel20FlatOdd10_eq
  · exact panel20FlatOdd11_eq
  · exact panel20FlatOdd12_eq
  · exact panel20FlatOdd13_eq
  · exact panel20FlatOdd14_eq
  · exact panel20FlatOdd15_eq
  · exact panel20FlatOdd16_eq
  · exact panel20FlatOdd17_eq
  · exact panel20FlatOdd18_eq
  · exact panel20FlatOdd19_eq
  · exact panel20FlatOdd20_eq
  · exact panel20FlatOdd21_eq
  · exact panel20FlatOdd22_eq
  · exact panel20FlatOdd23_eq

theorem panel20FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel20FlatCache.EnclosesCanonical
      ⟨20, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel20FlatDefect
    rw [panel20FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel20DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel20FlatEvenComponents).get i)
    rw [panel20FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel20OuterLengthTable
      .even ⟨20, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel20FlatOddComponents).get i)
    rw [panel20FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel20OuterLengthTable
      .odd ⟨20, by decide⟩ i

end RHP2Bridge
