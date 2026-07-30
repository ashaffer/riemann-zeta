import RHBridge.P2RoundedFactorCheckpoint13
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck13_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel13FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel13FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel13TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel13FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel13FlatEven0_eq
  · exact panel13FlatEven1_eq
  · exact panel13FlatEven2_eq
  · exact panel13FlatEven3_eq
  · exact panel13FlatEven4_eq
  · exact panel13FlatEven5_eq
  · exact panel13FlatEven6_eq
  · exact panel13FlatEven7_eq
  · exact panel13FlatEven8_eq
  · exact panel13FlatEven9_eq
  · exact panel13FlatEven10_eq
  · exact panel13FlatEven11_eq
  · exact panel13FlatEven12_eq
  · exact panel13FlatEven13_eq
  · exact panel13FlatEven14_eq
  · exact panel13FlatEven15_eq
  · exact panel13FlatEven16_eq
  · exact panel13FlatEven17_eq
  · exact panel13FlatEven18_eq
  · exact panel13FlatEven19_eq
  · exact panel13FlatEven20_eq
  · exact panel13FlatEven21_eq
  · exact panel13FlatEven22_eq
  · exact panel13FlatEven23_eq

theorem panel13FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel13FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel13FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel13FlatOdd0_eq
  · exact panel13FlatOdd1_eq
  · exact panel13FlatOdd2_eq
  · exact panel13FlatOdd3_eq
  · exact panel13FlatOdd4_eq
  · exact panel13FlatOdd5_eq
  · exact panel13FlatOdd6_eq
  · exact panel13FlatOdd7_eq
  · exact panel13FlatOdd8_eq
  · exact panel13FlatOdd9_eq
  · exact panel13FlatOdd10_eq
  · exact panel13FlatOdd11_eq
  · exact panel13FlatOdd12_eq
  · exact panel13FlatOdd13_eq
  · exact panel13FlatOdd14_eq
  · exact panel13FlatOdd15_eq
  · exact panel13FlatOdd16_eq
  · exact panel13FlatOdd17_eq
  · exact panel13FlatOdd18_eq
  · exact panel13FlatOdd19_eq
  · exact panel13FlatOdd20_eq
  · exact panel13FlatOdd21_eq
  · exact panel13FlatOdd22_eq
  · exact panel13FlatOdd23_eq

theorem panel13FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel13FlatCache.EnclosesCanonical
      ⟨13, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel13FlatDefect
    rw [panel13FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel13DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel13FlatEvenComponents).get i)
    rw [panel13FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel13OuterLengthTable
      .even ⟨13, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel13FlatOddComponents).get i)
    rw [panel13FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel13OuterLengthTable
      .odd ⟨13, by decide⟩ i

end RHP2Bridge
