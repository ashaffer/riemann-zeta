import RHBridge.P2RoundedFactorCheckpoint28
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck28_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel28FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel28FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel28TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel28FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel28FlatEven0_eq
  · exact panel28FlatEven1_eq
  · exact panel28FlatEven2_eq
  · exact panel28FlatEven3_eq
  · exact panel28FlatEven4_eq
  · exact panel28FlatEven5_eq
  · exact panel28FlatEven6_eq
  · exact panel28FlatEven7_eq
  · exact panel28FlatEven8_eq
  · exact panel28FlatEven9_eq
  · exact panel28FlatEven10_eq
  · exact panel28FlatEven11_eq
  · exact panel28FlatEven12_eq
  · exact panel28FlatEven13_eq
  · exact panel28FlatEven14_eq
  · exact panel28FlatEven15_eq
  · exact panel28FlatEven16_eq
  · exact panel28FlatEven17_eq
  · exact panel28FlatEven18_eq
  · exact panel28FlatEven19_eq
  · exact panel28FlatEven20_eq
  · exact panel28FlatEven21_eq
  · exact panel28FlatEven22_eq
  · exact panel28FlatEven23_eq

theorem panel28FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel28FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel28FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel28FlatOdd0_eq
  · exact panel28FlatOdd1_eq
  · exact panel28FlatOdd2_eq
  · exact panel28FlatOdd3_eq
  · exact panel28FlatOdd4_eq
  · exact panel28FlatOdd5_eq
  · exact panel28FlatOdd6_eq
  · exact panel28FlatOdd7_eq
  · exact panel28FlatOdd8_eq
  · exact panel28FlatOdd9_eq
  · exact panel28FlatOdd10_eq
  · exact panel28FlatOdd11_eq
  · exact panel28FlatOdd12_eq
  · exact panel28FlatOdd13_eq
  · exact panel28FlatOdd14_eq
  · exact panel28FlatOdd15_eq
  · exact panel28FlatOdd16_eq
  · exact panel28FlatOdd17_eq
  · exact panel28FlatOdd18_eq
  · exact panel28FlatOdd19_eq
  · exact panel28FlatOdd20_eq
  · exact panel28FlatOdd21_eq
  · exact panel28FlatOdd22_eq
  · exact panel28FlatOdd23_eq

theorem panel28FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel28FlatCache.EnclosesCanonical
      ⟨28, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel28FlatDefect
    rw [panel28FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel28DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel28FlatEvenComponents).get i)
    rw [panel28FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel28OuterLengthTable
      .even ⟨28, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel28FlatOddComponents).get i)
    rw [panel28FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel28OuterLengthTable
      .odd ⟨28, by decide⟩ i

end RHP2Bridge
