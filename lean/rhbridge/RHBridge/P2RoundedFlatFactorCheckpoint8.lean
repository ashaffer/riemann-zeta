import RHBridge.P2RoundedFactorCheckpoint8
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck8_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel8FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel8FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel8TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel8FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel8FlatEven0_eq
  · exact panel8FlatEven1_eq
  · exact panel8FlatEven2_eq
  · exact panel8FlatEven3_eq
  · exact panel8FlatEven4_eq
  · exact panel8FlatEven5_eq
  · exact panel8FlatEven6_eq
  · exact panel8FlatEven7_eq
  · exact panel8FlatEven8_eq
  · exact panel8FlatEven9_eq
  · exact panel8FlatEven10_eq
  · exact panel8FlatEven11_eq
  · exact panel8FlatEven12_eq
  · exact panel8FlatEven13_eq
  · exact panel8FlatEven14_eq
  · exact panel8FlatEven15_eq
  · exact panel8FlatEven16_eq
  · exact panel8FlatEven17_eq
  · exact panel8FlatEven18_eq
  · exact panel8FlatEven19_eq
  · exact panel8FlatEven20_eq
  · exact panel8FlatEven21_eq
  · exact panel8FlatEven22_eq
  · exact panel8FlatEven23_eq

theorem panel8FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel8FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel8FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel8FlatOdd0_eq
  · exact panel8FlatOdd1_eq
  · exact panel8FlatOdd2_eq
  · exact panel8FlatOdd3_eq
  · exact panel8FlatOdd4_eq
  · exact panel8FlatOdd5_eq
  · exact panel8FlatOdd6_eq
  · exact panel8FlatOdd7_eq
  · exact panel8FlatOdd8_eq
  · exact panel8FlatOdd9_eq
  · exact panel8FlatOdd10_eq
  · exact panel8FlatOdd11_eq
  · exact panel8FlatOdd12_eq
  · exact panel8FlatOdd13_eq
  · exact panel8FlatOdd14_eq
  · exact panel8FlatOdd15_eq
  · exact panel8FlatOdd16_eq
  · exact panel8FlatOdd17_eq
  · exact panel8FlatOdd18_eq
  · exact panel8FlatOdd19_eq
  · exact panel8FlatOdd20_eq
  · exact panel8FlatOdd21_eq
  · exact panel8FlatOdd22_eq
  · exact panel8FlatOdd23_eq

theorem panel8FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel8FlatCache.EnclosesCanonical
      ⟨8, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel8FlatDefect
    rw [panel8FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel8DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel8FlatEvenComponents).get i)
    rw [panel8FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel8OuterLengthTable
      .even ⟨8, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel8FlatOddComponents).get i)
    rw [panel8FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel8OuterLengthTable
      .odd ⟨8, by decide⟩ i

end RHP2Bridge
