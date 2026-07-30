import RHBridge.P2RoundedFactorCheckpoint3
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck3_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel3FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel3FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel3TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel3FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel3FlatEven0_eq
  · exact panel3FlatEven1_eq
  · exact panel3FlatEven2_eq
  · exact panel3FlatEven3_eq
  · exact panel3FlatEven4_eq
  · exact panel3FlatEven5_eq
  · exact panel3FlatEven6_eq
  · exact panel3FlatEven7_eq
  · exact panel3FlatEven8_eq
  · exact panel3FlatEven9_eq
  · exact panel3FlatEven10_eq
  · exact panel3FlatEven11_eq
  · exact panel3FlatEven12_eq
  · exact panel3FlatEven13_eq
  · exact panel3FlatEven14_eq
  · exact panel3FlatEven15_eq
  · exact panel3FlatEven16_eq
  · exact panel3FlatEven17_eq
  · exact panel3FlatEven18_eq
  · exact panel3FlatEven19_eq
  · exact panel3FlatEven20_eq
  · exact panel3FlatEven21_eq
  · exact panel3FlatEven22_eq
  · exact panel3FlatEven23_eq

theorem panel3FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel3FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel3FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel3FlatOdd0_eq
  · exact panel3FlatOdd1_eq
  · exact panel3FlatOdd2_eq
  · exact panel3FlatOdd3_eq
  · exact panel3FlatOdd4_eq
  · exact panel3FlatOdd5_eq
  · exact panel3FlatOdd6_eq
  · exact panel3FlatOdd7_eq
  · exact panel3FlatOdd8_eq
  · exact panel3FlatOdd9_eq
  · exact panel3FlatOdd10_eq
  · exact panel3FlatOdd11_eq
  · exact panel3FlatOdd12_eq
  · exact panel3FlatOdd13_eq
  · exact panel3FlatOdd14_eq
  · exact panel3FlatOdd15_eq
  · exact panel3FlatOdd16_eq
  · exact panel3FlatOdd17_eq
  · exact panel3FlatOdd18_eq
  · exact panel3FlatOdd19_eq
  · exact panel3FlatOdd20_eq
  · exact panel3FlatOdd21_eq
  · exact panel3FlatOdd22_eq
  · exact panel3FlatOdd23_eq

theorem panel3FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel3FlatCache.EnclosesCanonical
      ⟨3, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel3FlatDefect
    rw [panel3FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel3DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel3FlatEvenComponents).get i)
    rw [panel3FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel3OuterLengthTable
      .even ⟨3, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel3FlatOddComponents).get i)
    rw [panel3FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel3OuterLengthTable
      .odd ⟨3, by decide⟩ i

end RHP2Bridge
