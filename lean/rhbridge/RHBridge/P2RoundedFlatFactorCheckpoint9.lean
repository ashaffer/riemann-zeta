import RHBridge.P2RoundedFactorCheckpoint9
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck9_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel9FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel9FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel9FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel9FlatEven0_eq
  · exact panel9FlatEven1_eq
  · exact panel9FlatEven2_eq
  · exact panel9FlatEven3_eq
  · exact panel9FlatEven4_eq
  · exact panel9FlatEven5_eq
  · exact panel9FlatEven6_eq
  · exact panel9FlatEven7_eq
  · exact panel9FlatEven8_eq
  · exact panel9FlatEven9_eq
  · exact panel9FlatEven10_eq
  · exact panel9FlatEven11_eq
  · exact panel9FlatEven12_eq
  · exact panel9FlatEven13_eq
  · exact panel9FlatEven14_eq
  · exact panel9FlatEven15_eq
  · exact panel9FlatEven16_eq
  · exact panel9FlatEven17_eq
  · exact panel9FlatEven18_eq
  · exact panel9FlatEven19_eq
  · exact panel9FlatEven20_eq
  · exact panel9FlatEven21_eq
  · exact panel9FlatEven22_eq
  · exact panel9FlatEven23_eq

theorem panel9FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel9FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel9FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel9FlatOdd0_eq
  · exact panel9FlatOdd1_eq
  · exact panel9FlatOdd2_eq
  · exact panel9FlatOdd3_eq
  · exact panel9FlatOdd4_eq
  · exact panel9FlatOdd5_eq
  · exact panel9FlatOdd6_eq
  · exact panel9FlatOdd7_eq
  · exact panel9FlatOdd8_eq
  · exact panel9FlatOdd9_eq
  · exact panel9FlatOdd10_eq
  · exact panel9FlatOdd11_eq
  · exact panel9FlatOdd12_eq
  · exact panel9FlatOdd13_eq
  · exact panel9FlatOdd14_eq
  · exact panel9FlatOdd15_eq
  · exact panel9FlatOdd16_eq
  · exact panel9FlatOdd17_eq
  · exact panel9FlatOdd18_eq
  · exact panel9FlatOdd19_eq
  · exact panel9FlatOdd20_eq
  · exact panel9FlatOdd21_eq
  · exact panel9FlatOdd22_eq
  · exact panel9FlatOdd23_eq

theorem panel9FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel9FlatCache.EnclosesCanonical
      ⟨9, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel9FlatDefect
    rw [panel9FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel9DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel9FlatEvenComponents).get i)
    rw [panel9FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel9OuterLengthTable
      .even ⟨9, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel9FlatOddComponents).get i)
    rw [panel9FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel9OuterLengthTable
      .odd ⟨9, by decide⟩ i

end RHP2Bridge
