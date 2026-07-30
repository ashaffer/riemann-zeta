import RHBridge.P2RoundedFactorCheckpoint12
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck12_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel12FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel12FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel12FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel12FlatEven0_eq
  · exact panel12FlatEven1_eq
  · exact panel12FlatEven2_eq
  · exact panel12FlatEven3_eq
  · exact panel12FlatEven4_eq
  · exact panel12FlatEven5_eq
  · exact panel12FlatEven6_eq
  · exact panel12FlatEven7_eq
  · exact panel12FlatEven8_eq
  · exact panel12FlatEven9_eq
  · exact panel12FlatEven10_eq
  · exact panel12FlatEven11_eq
  · exact panel12FlatEven12_eq
  · exact panel12FlatEven13_eq
  · exact panel12FlatEven14_eq
  · exact panel12FlatEven15_eq
  · exact panel12FlatEven16_eq
  · exact panel12FlatEven17_eq
  · exact panel12FlatEven18_eq
  · exact panel12FlatEven19_eq
  · exact panel12FlatEven20_eq
  · exact panel12FlatEven21_eq
  · exact panel12FlatEven22_eq
  · exact panel12FlatEven23_eq

theorem panel12FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel12FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel12FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel12FlatOdd0_eq
  · exact panel12FlatOdd1_eq
  · exact panel12FlatOdd2_eq
  · exact panel12FlatOdd3_eq
  · exact panel12FlatOdd4_eq
  · exact panel12FlatOdd5_eq
  · exact panel12FlatOdd6_eq
  · exact panel12FlatOdd7_eq
  · exact panel12FlatOdd8_eq
  · exact panel12FlatOdd9_eq
  · exact panel12FlatOdd10_eq
  · exact panel12FlatOdd11_eq
  · exact panel12FlatOdd12_eq
  · exact panel12FlatOdd13_eq
  · exact panel12FlatOdd14_eq
  · exact panel12FlatOdd15_eq
  · exact panel12FlatOdd16_eq
  · exact panel12FlatOdd17_eq
  · exact panel12FlatOdd18_eq
  · exact panel12FlatOdd19_eq
  · exact panel12FlatOdd20_eq
  · exact panel12FlatOdd21_eq
  · exact panel12FlatOdd22_eq
  · exact panel12FlatOdd23_eq

theorem panel12FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel12FlatCache.EnclosesCanonical
      ⟨12, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel12FlatDefect
    rw [panel12FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel12DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel12FlatEvenComponents).get i)
    rw [panel12FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel12OuterLengthTable
      .even ⟨12, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel12FlatOddComponents).get i)
    rw [panel12FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel12OuterLengthTable
      .odd ⟨12, by decide⟩ i

end RHP2Bridge
