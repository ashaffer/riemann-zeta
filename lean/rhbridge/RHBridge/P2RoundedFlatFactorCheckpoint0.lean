import RHBridge.P2RoundedFactorCheckpoint0
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck0_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel0FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel0FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel0FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel0FlatEven0_eq
  · exact panel0FlatEven1_eq
  · exact panel0FlatEven2_eq
  · exact panel0FlatEven3_eq
  · exact panel0FlatEven4_eq
  · exact panel0FlatEven5_eq
  · exact panel0FlatEven6_eq
  · exact panel0FlatEven7_eq
  · exact panel0FlatEven8_eq
  · exact panel0FlatEven9_eq
  · exact panel0FlatEven10_eq
  · exact panel0FlatEven11_eq
  · exact panel0FlatEven12_eq
  · exact panel0FlatEven13_eq
  · exact panel0FlatEven14_eq
  · exact panel0FlatEven15_eq
  · exact panel0FlatEven16_eq
  · exact panel0FlatEven17_eq
  · exact panel0FlatEven18_eq
  · exact panel0FlatEven19_eq
  · exact panel0FlatEven20_eq
  · exact panel0FlatEven21_eq
  · exact panel0FlatEven22_eq
  · exact panel0FlatEven23_eq

theorem panel0FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel0FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel0FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel0FlatOdd0_eq
  · exact panel0FlatOdd1_eq
  · exact panel0FlatOdd2_eq
  · exact panel0FlatOdd3_eq
  · exact panel0FlatOdd4_eq
  · exact panel0FlatOdd5_eq
  · exact panel0FlatOdd6_eq
  · exact panel0FlatOdd7_eq
  · exact panel0FlatOdd8_eq
  · exact panel0FlatOdd9_eq
  · exact panel0FlatOdd10_eq
  · exact panel0FlatOdd11_eq
  · exact panel0FlatOdd12_eq
  · exact panel0FlatOdd13_eq
  · exact panel0FlatOdd14_eq
  · exact panel0FlatOdd15_eq
  · exact panel0FlatOdd16_eq
  · exact panel0FlatOdd17_eq
  · exact panel0FlatOdd18_eq
  · exact panel0FlatOdd19_eq
  · exact panel0FlatOdd20_eq
  · exact panel0FlatOdd21_eq
  · exact panel0FlatOdd22_eq
  · exact panel0FlatOdd23_eq

theorem panel0FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel0FlatCache.EnclosesCanonical
      ⟨0, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel0FlatDefect
    rw [panel0FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel0DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel0FlatEvenComponents).get i)
    rw [panel0FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel0OuterLengthTable
      .even ⟨0, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel0FlatOddComponents).get i)
    rw [panel0FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel0OuterLengthTable
      .odd ⟨0, by decide⟩ i

end RHP2Bridge
