import RHBridge.P2RoundedFactorCheckpoint23
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck23_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel23FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel23FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel23TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel23FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel23FlatEven0_eq
  · exact panel23FlatEven1_eq
  · exact panel23FlatEven2_eq
  · exact panel23FlatEven3_eq
  · exact panel23FlatEven4_eq
  · exact panel23FlatEven5_eq
  · exact panel23FlatEven6_eq
  · exact panel23FlatEven7_eq
  · exact panel23FlatEven8_eq
  · exact panel23FlatEven9_eq
  · exact panel23FlatEven10_eq
  · exact panel23FlatEven11_eq
  · exact panel23FlatEven12_eq
  · exact panel23FlatEven13_eq
  · exact panel23FlatEven14_eq
  · exact panel23FlatEven15_eq
  · exact panel23FlatEven16_eq
  · exact panel23FlatEven17_eq
  · exact panel23FlatEven18_eq
  · exact panel23FlatEven19_eq
  · exact panel23FlatEven20_eq
  · exact panel23FlatEven21_eq
  · exact panel23FlatEven22_eq
  · exact panel23FlatEven23_eq

theorem panel23FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel23FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel23FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel23FlatOdd0_eq
  · exact panel23FlatOdd1_eq
  · exact panel23FlatOdd2_eq
  · exact panel23FlatOdd3_eq
  · exact panel23FlatOdd4_eq
  · exact panel23FlatOdd5_eq
  · exact panel23FlatOdd6_eq
  · exact panel23FlatOdd7_eq
  · exact panel23FlatOdd8_eq
  · exact panel23FlatOdd9_eq
  · exact panel23FlatOdd10_eq
  · exact panel23FlatOdd11_eq
  · exact panel23FlatOdd12_eq
  · exact panel23FlatOdd13_eq
  · exact panel23FlatOdd14_eq
  · exact panel23FlatOdd15_eq
  · exact panel23FlatOdd16_eq
  · exact panel23FlatOdd17_eq
  · exact panel23FlatOdd18_eq
  · exact panel23FlatOdd19_eq
  · exact panel23FlatOdd20_eq
  · exact panel23FlatOdd21_eq
  · exact panel23FlatOdd22_eq
  · exact panel23FlatOdd23_eq

theorem panel23FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel23FlatCache.EnclosesCanonical
      ⟨23, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel23FlatDefect
    rw [panel23FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel23DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel23FlatEvenComponents).get i)
    rw [panel23FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel23OuterLengthTable
      .even ⟨23, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel23FlatOddComponents).get i)
    rw [panel23FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel23OuterLengthTable
      .odd ⟨23, by decide⟩ i

end RHP2Bridge
