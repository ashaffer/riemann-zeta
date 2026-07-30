import RHBridge.P2RoundedFactorCheckpoint18
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck18_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel18FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel18FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel18TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel18FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel18FlatEven0_eq
  · exact panel18FlatEven1_eq
  · exact panel18FlatEven2_eq
  · exact panel18FlatEven3_eq
  · exact panel18FlatEven4_eq
  · exact panel18FlatEven5_eq
  · exact panel18FlatEven6_eq
  · exact panel18FlatEven7_eq
  · exact panel18FlatEven8_eq
  · exact panel18FlatEven9_eq
  · exact panel18FlatEven10_eq
  · exact panel18FlatEven11_eq
  · exact panel18FlatEven12_eq
  · exact panel18FlatEven13_eq
  · exact panel18FlatEven14_eq
  · exact panel18FlatEven15_eq
  · exact panel18FlatEven16_eq
  · exact panel18FlatEven17_eq
  · exact panel18FlatEven18_eq
  · exact panel18FlatEven19_eq
  · exact panel18FlatEven20_eq
  · exact panel18FlatEven21_eq
  · exact panel18FlatEven22_eq
  · exact panel18FlatEven23_eq

theorem panel18FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel18FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel18FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel18FlatOdd0_eq
  · exact panel18FlatOdd1_eq
  · exact panel18FlatOdd2_eq
  · exact panel18FlatOdd3_eq
  · exact panel18FlatOdd4_eq
  · exact panel18FlatOdd5_eq
  · exact panel18FlatOdd6_eq
  · exact panel18FlatOdd7_eq
  · exact panel18FlatOdd8_eq
  · exact panel18FlatOdd9_eq
  · exact panel18FlatOdd10_eq
  · exact panel18FlatOdd11_eq
  · exact panel18FlatOdd12_eq
  · exact panel18FlatOdd13_eq
  · exact panel18FlatOdd14_eq
  · exact panel18FlatOdd15_eq
  · exact panel18FlatOdd16_eq
  · exact panel18FlatOdd17_eq
  · exact panel18FlatOdd18_eq
  · exact panel18FlatOdd19_eq
  · exact panel18FlatOdd20_eq
  · exact panel18FlatOdd21_eq
  · exact panel18FlatOdd22_eq
  · exact panel18FlatOdd23_eq

theorem panel18FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel18FlatCache.EnclosesCanonical
      ⟨18, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel18FlatDefect
    rw [panel18FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel18DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel18FlatEvenComponents).get i)
    rw [panel18FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel18OuterLengthTable
      .even ⟨18, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel18FlatOddComponents).get i)
    rw [panel18FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel18OuterLengthTable
      .odd ⟨18, by decide⟩ i

end RHP2Bridge
