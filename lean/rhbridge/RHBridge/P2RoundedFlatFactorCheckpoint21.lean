import RHBridge.P2RoundedFactorCheckpoint21
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck21_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel21FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel21FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel21FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel21FlatEven0_eq
  · exact panel21FlatEven1_eq
  · exact panel21FlatEven2_eq
  · exact panel21FlatEven3_eq
  · exact panel21FlatEven4_eq
  · exact panel21FlatEven5_eq
  · exact panel21FlatEven6_eq
  · exact panel21FlatEven7_eq
  · exact panel21FlatEven8_eq
  · exact panel21FlatEven9_eq
  · exact panel21FlatEven10_eq
  · exact panel21FlatEven11_eq
  · exact panel21FlatEven12_eq
  · exact panel21FlatEven13_eq
  · exact panel21FlatEven14_eq
  · exact panel21FlatEven15_eq
  · exact panel21FlatEven16_eq
  · exact panel21FlatEven17_eq
  · exact panel21FlatEven18_eq
  · exact panel21FlatEven19_eq
  · exact panel21FlatEven20_eq
  · exact panel21FlatEven21_eq
  · exact panel21FlatEven22_eq
  · exact panel21FlatEven23_eq

theorem panel21FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel21FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel21FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel21FlatOdd0_eq
  · exact panel21FlatOdd1_eq
  · exact panel21FlatOdd2_eq
  · exact panel21FlatOdd3_eq
  · exact panel21FlatOdd4_eq
  · exact panel21FlatOdd5_eq
  · exact panel21FlatOdd6_eq
  · exact panel21FlatOdd7_eq
  · exact panel21FlatOdd8_eq
  · exact panel21FlatOdd9_eq
  · exact panel21FlatOdd10_eq
  · exact panel21FlatOdd11_eq
  · exact panel21FlatOdd12_eq
  · exact panel21FlatOdd13_eq
  · exact panel21FlatOdd14_eq
  · exact panel21FlatOdd15_eq
  · exact panel21FlatOdd16_eq
  · exact panel21FlatOdd17_eq
  · exact panel21FlatOdd18_eq
  · exact panel21FlatOdd19_eq
  · exact panel21FlatOdd20_eq
  · exact panel21FlatOdd21_eq
  · exact panel21FlatOdd22_eq
  · exact panel21FlatOdd23_eq

theorem panel21FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel21FlatCache.EnclosesCanonical
      ⟨21, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel21FlatDefect
    rw [panel21FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel21DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel21FlatEvenComponents).get i)
    rw [panel21FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel21OuterLengthTable
      .even ⟨21, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel21FlatOddComponents).get i)
    rw [panel21FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel21OuterLengthTable
      .odd ⟨21, by decide⟩ i

end RHP2Bridge
