import RHBridge.P2RoundedFactorCheckpoint19
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck19_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel19FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel19FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel19TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel19FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel19FlatEven0_eq
  · exact panel19FlatEven1_eq
  · exact panel19FlatEven2_eq
  · exact panel19FlatEven3_eq
  · exact panel19FlatEven4_eq
  · exact panel19FlatEven5_eq
  · exact panel19FlatEven6_eq
  · exact panel19FlatEven7_eq
  · exact panel19FlatEven8_eq
  · exact panel19FlatEven9_eq
  · exact panel19FlatEven10_eq
  · exact panel19FlatEven11_eq
  · exact panel19FlatEven12_eq
  · exact panel19FlatEven13_eq
  · exact panel19FlatEven14_eq
  · exact panel19FlatEven15_eq
  · exact panel19FlatEven16_eq
  · exact panel19FlatEven17_eq
  · exact panel19FlatEven18_eq
  · exact panel19FlatEven19_eq
  · exact panel19FlatEven20_eq
  · exact panel19FlatEven21_eq
  · exact panel19FlatEven22_eq
  · exact panel19FlatEven23_eq

theorem panel19FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel19FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel19FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel19FlatOdd0_eq
  · exact panel19FlatOdd1_eq
  · exact panel19FlatOdd2_eq
  · exact panel19FlatOdd3_eq
  · exact panel19FlatOdd4_eq
  · exact panel19FlatOdd5_eq
  · exact panel19FlatOdd6_eq
  · exact panel19FlatOdd7_eq
  · exact panel19FlatOdd8_eq
  · exact panel19FlatOdd9_eq
  · exact panel19FlatOdd10_eq
  · exact panel19FlatOdd11_eq
  · exact panel19FlatOdd12_eq
  · exact panel19FlatOdd13_eq
  · exact panel19FlatOdd14_eq
  · exact panel19FlatOdd15_eq
  · exact panel19FlatOdd16_eq
  · exact panel19FlatOdd17_eq
  · exact panel19FlatOdd18_eq
  · exact panel19FlatOdd19_eq
  · exact panel19FlatOdd20_eq
  · exact panel19FlatOdd21_eq
  · exact panel19FlatOdd22_eq
  · exact panel19FlatOdd23_eq

theorem panel19FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel19FlatCache.EnclosesCanonical
      ⟨19, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel19FlatDefect
    rw [panel19FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel19DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel19FlatEvenComponents).get i)
    rw [panel19FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel19OuterLengthTable
      .even ⟨19, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel19FlatOddComponents).get i)
    rw [panel19FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel19OuterLengthTable
      .odd ⟨19, by decide⟩ i

end RHP2Bridge
