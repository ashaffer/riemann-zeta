import RHBridge.P2RoundedFactorCheckpoint7
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck7_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel7FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel7FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel7TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel7FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel7FlatEven0_eq
  · exact panel7FlatEven1_eq
  · exact panel7FlatEven2_eq
  · exact panel7FlatEven3_eq
  · exact panel7FlatEven4_eq
  · exact panel7FlatEven5_eq
  · exact panel7FlatEven6_eq
  · exact panel7FlatEven7_eq
  · exact panel7FlatEven8_eq
  · exact panel7FlatEven9_eq
  · exact panel7FlatEven10_eq
  · exact panel7FlatEven11_eq
  · exact panel7FlatEven12_eq
  · exact panel7FlatEven13_eq
  · exact panel7FlatEven14_eq
  · exact panel7FlatEven15_eq
  · exact panel7FlatEven16_eq
  · exact panel7FlatEven17_eq
  · exact panel7FlatEven18_eq
  · exact panel7FlatEven19_eq
  · exact panel7FlatEven20_eq
  · exact panel7FlatEven21_eq
  · exact panel7FlatEven22_eq
  · exact panel7FlatEven23_eq

theorem panel7FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel7FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel7FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel7FlatOdd0_eq
  · exact panel7FlatOdd1_eq
  · exact panel7FlatOdd2_eq
  · exact panel7FlatOdd3_eq
  · exact panel7FlatOdd4_eq
  · exact panel7FlatOdd5_eq
  · exact panel7FlatOdd6_eq
  · exact panel7FlatOdd7_eq
  · exact panel7FlatOdd8_eq
  · exact panel7FlatOdd9_eq
  · exact panel7FlatOdd10_eq
  · exact panel7FlatOdd11_eq
  · exact panel7FlatOdd12_eq
  · exact panel7FlatOdd13_eq
  · exact panel7FlatOdd14_eq
  · exact panel7FlatOdd15_eq
  · exact panel7FlatOdd16_eq
  · exact panel7FlatOdd17_eq
  · exact panel7FlatOdd18_eq
  · exact panel7FlatOdd19_eq
  · exact panel7FlatOdd20_eq
  · exact panel7FlatOdd21_eq
  · exact panel7FlatOdd22_eq
  · exact panel7FlatOdd23_eq

theorem panel7FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel7FlatCache.EnclosesCanonical
      ⟨7, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel7FlatDefect
    rw [panel7FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel7DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel7FlatEvenComponents).get i)
    rw [panel7FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel7OuterLengthTable
      .even ⟨7, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel7FlatOddComponents).get i)
    rw [panel7FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel7OuterLengthTable
      .odd ⟨7, by decide⟩ i

end RHP2Bridge
