import RHBridge.P2RoundedFactorCheckpoint22
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck22_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel22FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel22FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel22FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel22FlatEven0_eq
  · exact panel22FlatEven1_eq
  · exact panel22FlatEven2_eq
  · exact panel22FlatEven3_eq
  · exact panel22FlatEven4_eq
  · exact panel22FlatEven5_eq
  · exact panel22FlatEven6_eq
  · exact panel22FlatEven7_eq
  · exact panel22FlatEven8_eq
  · exact panel22FlatEven9_eq
  · exact panel22FlatEven10_eq
  · exact panel22FlatEven11_eq
  · exact panel22FlatEven12_eq
  · exact panel22FlatEven13_eq
  · exact panel22FlatEven14_eq
  · exact panel22FlatEven15_eq
  · exact panel22FlatEven16_eq
  · exact panel22FlatEven17_eq
  · exact panel22FlatEven18_eq
  · exact panel22FlatEven19_eq
  · exact panel22FlatEven20_eq
  · exact panel22FlatEven21_eq
  · exact panel22FlatEven22_eq
  · exact panel22FlatEven23_eq

theorem panel22FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel22FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel22FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel22FlatOdd0_eq
  · exact panel22FlatOdd1_eq
  · exact panel22FlatOdd2_eq
  · exact panel22FlatOdd3_eq
  · exact panel22FlatOdd4_eq
  · exact panel22FlatOdd5_eq
  · exact panel22FlatOdd6_eq
  · exact panel22FlatOdd7_eq
  · exact panel22FlatOdd8_eq
  · exact panel22FlatOdd9_eq
  · exact panel22FlatOdd10_eq
  · exact panel22FlatOdd11_eq
  · exact panel22FlatOdd12_eq
  · exact panel22FlatOdd13_eq
  · exact panel22FlatOdd14_eq
  · exact panel22FlatOdd15_eq
  · exact panel22FlatOdd16_eq
  · exact panel22FlatOdd17_eq
  · exact panel22FlatOdd18_eq
  · exact panel22FlatOdd19_eq
  · exact panel22FlatOdd20_eq
  · exact panel22FlatOdd21_eq
  · exact panel22FlatOdd22_eq
  · exact panel22FlatOdd23_eq

theorem panel22FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel22FlatCache.EnclosesCanonical
      ⟨22, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel22FlatDefect
    rw [panel22FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel22DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel22FlatEvenComponents).get i)
    rw [panel22FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel22OuterLengthTable
      .even ⟨22, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel22FlatOddComponents).get i)
    rw [panel22FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel22OuterLengthTable
      .odd ⟨22, by decide⟩ i

end RHP2Bridge
