import RHBridge.P2RoundedFactorCheckpoint6
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck6_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel6FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel6FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel6TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel6FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel6FlatEven0_eq
  · exact panel6FlatEven1_eq
  · exact panel6FlatEven2_eq
  · exact panel6FlatEven3_eq
  · exact panel6FlatEven4_eq
  · exact panel6FlatEven5_eq
  · exact panel6FlatEven6_eq
  · exact panel6FlatEven7_eq
  · exact panel6FlatEven8_eq
  · exact panel6FlatEven9_eq
  · exact panel6FlatEven10_eq
  · exact panel6FlatEven11_eq
  · exact panel6FlatEven12_eq
  · exact panel6FlatEven13_eq
  · exact panel6FlatEven14_eq
  · exact panel6FlatEven15_eq
  · exact panel6FlatEven16_eq
  · exact panel6FlatEven17_eq
  · exact panel6FlatEven18_eq
  · exact panel6FlatEven19_eq
  · exact panel6FlatEven20_eq
  · exact panel6FlatEven21_eq
  · exact panel6FlatEven22_eq
  · exact panel6FlatEven23_eq

theorem panel6FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel6FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel6FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel6FlatOdd0_eq
  · exact panel6FlatOdd1_eq
  · exact panel6FlatOdd2_eq
  · exact panel6FlatOdd3_eq
  · exact panel6FlatOdd4_eq
  · exact panel6FlatOdd5_eq
  · exact panel6FlatOdd6_eq
  · exact panel6FlatOdd7_eq
  · exact panel6FlatOdd8_eq
  · exact panel6FlatOdd9_eq
  · exact panel6FlatOdd10_eq
  · exact panel6FlatOdd11_eq
  · exact panel6FlatOdd12_eq
  · exact panel6FlatOdd13_eq
  · exact panel6FlatOdd14_eq
  · exact panel6FlatOdd15_eq
  · exact panel6FlatOdd16_eq
  · exact panel6FlatOdd17_eq
  · exact panel6FlatOdd18_eq
  · exact panel6FlatOdd19_eq
  · exact panel6FlatOdd20_eq
  · exact panel6FlatOdd21_eq
  · exact panel6FlatOdd22_eq
  · exact panel6FlatOdd23_eq

theorem panel6FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel6FlatCache.EnclosesCanonical
      ⟨6, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel6FlatDefect
    rw [panel6FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel6DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel6FlatEvenComponents).get i)
    rw [panel6FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel6OuterLengthTable
      .even ⟨6, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel6FlatOddComponents).get i)
    rw [panel6FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel6OuterLengthTable
      .odd ⟨6, by decide⟩ i

end RHP2Bridge
