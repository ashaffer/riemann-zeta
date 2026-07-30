import RHBridge.P2RoundedFactorCheckpoint10
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck10_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel10FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel10FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel10FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel10FlatEven0_eq
  · exact panel10FlatEven1_eq
  · exact panel10FlatEven2_eq
  · exact panel10FlatEven3_eq
  · exact panel10FlatEven4_eq
  · exact panel10FlatEven5_eq
  · exact panel10FlatEven6_eq
  · exact panel10FlatEven7_eq
  · exact panel10FlatEven8_eq
  · exact panel10FlatEven9_eq
  · exact panel10FlatEven10_eq
  · exact panel10FlatEven11_eq
  · exact panel10FlatEven12_eq
  · exact panel10FlatEven13_eq
  · exact panel10FlatEven14_eq
  · exact panel10FlatEven15_eq
  · exact panel10FlatEven16_eq
  · exact panel10FlatEven17_eq
  · exact panel10FlatEven18_eq
  · exact panel10FlatEven19_eq
  · exact panel10FlatEven20_eq
  · exact panel10FlatEven21_eq
  · exact panel10FlatEven22_eq
  · exact panel10FlatEven23_eq

theorem panel10FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel10FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel10FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel10FlatOdd0_eq
  · exact panel10FlatOdd1_eq
  · exact panel10FlatOdd2_eq
  · exact panel10FlatOdd3_eq
  · exact panel10FlatOdd4_eq
  · exact panel10FlatOdd5_eq
  · exact panel10FlatOdd6_eq
  · exact panel10FlatOdd7_eq
  · exact panel10FlatOdd8_eq
  · exact panel10FlatOdd9_eq
  · exact panel10FlatOdd10_eq
  · exact panel10FlatOdd11_eq
  · exact panel10FlatOdd12_eq
  · exact panel10FlatOdd13_eq
  · exact panel10FlatOdd14_eq
  · exact panel10FlatOdd15_eq
  · exact panel10FlatOdd16_eq
  · exact panel10FlatOdd17_eq
  · exact panel10FlatOdd18_eq
  · exact panel10FlatOdd19_eq
  · exact panel10FlatOdd20_eq
  · exact panel10FlatOdd21_eq
  · exact panel10FlatOdd22_eq
  · exact panel10FlatOdd23_eq

theorem panel10FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel10FlatCache.EnclosesCanonical
      ⟨10, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel10FlatDefect
    rw [panel10FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel10DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel10FlatEvenComponents).get i)
    rw [panel10FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel10OuterLengthTable
      .even ⟨10, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel10FlatOddComponents).get i)
    rw [panel10FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel10OuterLengthTable
      .odd ⟨10, by decide⟩ i

end RHP2Bridge
