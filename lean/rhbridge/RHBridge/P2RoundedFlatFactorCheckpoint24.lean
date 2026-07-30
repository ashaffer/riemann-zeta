import RHBridge.P2RoundedFactorCheckpoint24
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck24_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel24FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel24FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel24FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel24FlatEven0_eq
  · exact panel24FlatEven1_eq
  · exact panel24FlatEven2_eq
  · exact panel24FlatEven3_eq
  · exact panel24FlatEven4_eq
  · exact panel24FlatEven5_eq
  · exact panel24FlatEven6_eq
  · exact panel24FlatEven7_eq
  · exact panel24FlatEven8_eq
  · exact panel24FlatEven9_eq
  · exact panel24FlatEven10_eq
  · exact panel24FlatEven11_eq
  · exact panel24FlatEven12_eq
  · exact panel24FlatEven13_eq
  · exact panel24FlatEven14_eq
  · exact panel24FlatEven15_eq
  · exact panel24FlatEven16_eq
  · exact panel24FlatEven17_eq
  · exact panel24FlatEven18_eq
  · exact panel24FlatEven19_eq
  · exact panel24FlatEven20_eq
  · exact panel24FlatEven21_eq
  · exact panel24FlatEven22_eq
  · exact panel24FlatEven23_eq

theorem panel24FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel24FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel24FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel24FlatOdd0_eq
  · exact panel24FlatOdd1_eq
  · exact panel24FlatOdd2_eq
  · exact panel24FlatOdd3_eq
  · exact panel24FlatOdd4_eq
  · exact panel24FlatOdd5_eq
  · exact panel24FlatOdd6_eq
  · exact panel24FlatOdd7_eq
  · exact panel24FlatOdd8_eq
  · exact panel24FlatOdd9_eq
  · exact panel24FlatOdd10_eq
  · exact panel24FlatOdd11_eq
  · exact panel24FlatOdd12_eq
  · exact panel24FlatOdd13_eq
  · exact panel24FlatOdd14_eq
  · exact panel24FlatOdd15_eq
  · exact panel24FlatOdd16_eq
  · exact panel24FlatOdd17_eq
  · exact panel24FlatOdd18_eq
  · exact panel24FlatOdd19_eq
  · exact panel24FlatOdd20_eq
  · exact panel24FlatOdd21_eq
  · exact panel24FlatOdd22_eq
  · exact panel24FlatOdd23_eq

theorem panel24FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel24FlatCache.EnclosesCanonical
      ⟨24, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel24FlatDefect
    rw [panel24FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel24DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel24FlatEvenComponents).get i)
    rw [panel24FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel24OuterLengthTable
      .even ⟨24, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel24FlatOddComponents).get i)
    rw [panel24FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel24OuterLengthTable
      .odd ⟨24, by decide⟩ i

end RHP2Bridge
