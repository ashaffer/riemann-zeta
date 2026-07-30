import RHBridge.P2RoundedFactorCheckpoint31
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck31_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel31FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel31FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel31TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel31FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel31FlatEven0_eq
  · exact panel31FlatEven1_eq
  · exact panel31FlatEven2_eq
  · exact panel31FlatEven3_eq
  · exact panel31FlatEven4_eq
  · exact panel31FlatEven5_eq
  · exact panel31FlatEven6_eq
  · exact panel31FlatEven7_eq
  · exact panel31FlatEven8_eq
  · exact panel31FlatEven9_eq
  · exact panel31FlatEven10_eq
  · exact panel31FlatEven11_eq
  · exact panel31FlatEven12_eq
  · exact panel31FlatEven13_eq
  · exact panel31FlatEven14_eq
  · exact panel31FlatEven15_eq
  · exact panel31FlatEven16_eq
  · exact panel31FlatEven17_eq
  · exact panel31FlatEven18_eq
  · exact panel31FlatEven19_eq
  · exact panel31FlatEven20_eq
  · exact panel31FlatEven21_eq
  · exact panel31FlatEven22_eq
  · exact panel31FlatEven23_eq

theorem panel31FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel31FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel31FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel31FlatOdd0_eq
  · exact panel31FlatOdd1_eq
  · exact panel31FlatOdd2_eq
  · exact panel31FlatOdd3_eq
  · exact panel31FlatOdd4_eq
  · exact panel31FlatOdd5_eq
  · exact panel31FlatOdd6_eq
  · exact panel31FlatOdd7_eq
  · exact panel31FlatOdd8_eq
  · exact panel31FlatOdd9_eq
  · exact panel31FlatOdd10_eq
  · exact panel31FlatOdd11_eq
  · exact panel31FlatOdd12_eq
  · exact panel31FlatOdd13_eq
  · exact panel31FlatOdd14_eq
  · exact panel31FlatOdd15_eq
  · exact panel31FlatOdd16_eq
  · exact panel31FlatOdd17_eq
  · exact panel31FlatOdd18_eq
  · exact panel31FlatOdd19_eq
  · exact panel31FlatOdd20_eq
  · exact panel31FlatOdd21_eq
  · exact panel31FlatOdd22_eq
  · exact panel31FlatOdd23_eq

theorem panel31FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel31FlatCache.EnclosesCanonical
      ⟨31, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel31FlatDefect
    rw [panel31FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel31DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel31FlatEvenComponents).get i)
    rw [panel31FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel31OuterLengthTable
      .even ⟨31, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel31FlatOddComponents).get i)
    rw [panel31FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel31OuterLengthTable
      .odd ⟨31, by decide⟩ i

end RHP2Bridge
