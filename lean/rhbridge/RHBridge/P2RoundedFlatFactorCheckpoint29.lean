import RHBridge.P2RoundedFactorCheckpoint29
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck29_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel29FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel29FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel29TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel29FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel29FlatEven0_eq
  · exact panel29FlatEven1_eq
  · exact panel29FlatEven2_eq
  · exact panel29FlatEven3_eq
  · exact panel29FlatEven4_eq
  · exact panel29FlatEven5_eq
  · exact panel29FlatEven6_eq
  · exact panel29FlatEven7_eq
  · exact panel29FlatEven8_eq
  · exact panel29FlatEven9_eq
  · exact panel29FlatEven10_eq
  · exact panel29FlatEven11_eq
  · exact panel29FlatEven12_eq
  · exact panel29FlatEven13_eq
  · exact panel29FlatEven14_eq
  · exact panel29FlatEven15_eq
  · exact panel29FlatEven16_eq
  · exact panel29FlatEven17_eq
  · exact panel29FlatEven18_eq
  · exact panel29FlatEven19_eq
  · exact panel29FlatEven20_eq
  · exact panel29FlatEven21_eq
  · exact panel29FlatEven22_eq
  · exact panel29FlatEven23_eq

theorem panel29FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel29FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel29FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel29FlatOdd0_eq
  · exact panel29FlatOdd1_eq
  · exact panel29FlatOdd2_eq
  · exact panel29FlatOdd3_eq
  · exact panel29FlatOdd4_eq
  · exact panel29FlatOdd5_eq
  · exact panel29FlatOdd6_eq
  · exact panel29FlatOdd7_eq
  · exact panel29FlatOdd8_eq
  · exact panel29FlatOdd9_eq
  · exact panel29FlatOdd10_eq
  · exact panel29FlatOdd11_eq
  · exact panel29FlatOdd12_eq
  · exact panel29FlatOdd13_eq
  · exact panel29FlatOdd14_eq
  · exact panel29FlatOdd15_eq
  · exact panel29FlatOdd16_eq
  · exact panel29FlatOdd17_eq
  · exact panel29FlatOdd18_eq
  · exact panel29FlatOdd19_eq
  · exact panel29FlatOdd20_eq
  · exact panel29FlatOdd21_eq
  · exact panel29FlatOdd22_eq
  · exact panel29FlatOdd23_eq

theorem panel29FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel29FlatCache.EnclosesCanonical
      ⟨29, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel29FlatDefect
    rw [panel29FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel29DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel29FlatEvenComponents).get i)
    rw [panel29FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel29OuterLengthTable
      .even ⟨29, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel29FlatOddComponents).get i)
    rw [panel29FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel29OuterLengthTable
      .odd ⟨29, by decide⟩ i

end RHP2Bridge
