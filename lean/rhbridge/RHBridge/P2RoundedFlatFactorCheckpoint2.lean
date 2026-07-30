import RHBridge.P2RoundedFactorCheckpoint2
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck2_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel2FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel2FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel2FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel2FlatEven0_eq
  · exact panel2FlatEven1_eq
  · exact panel2FlatEven2_eq
  · exact panel2FlatEven3_eq
  · exact panel2FlatEven4_eq
  · exact panel2FlatEven5_eq
  · exact panel2FlatEven6_eq
  · exact panel2FlatEven7_eq
  · exact panel2FlatEven8_eq
  · exact panel2FlatEven9_eq
  · exact panel2FlatEven10_eq
  · exact panel2FlatEven11_eq
  · exact panel2FlatEven12_eq
  · exact panel2FlatEven13_eq
  · exact panel2FlatEven14_eq
  · exact panel2FlatEven15_eq
  · exact panel2FlatEven16_eq
  · exact panel2FlatEven17_eq
  · exact panel2FlatEven18_eq
  · exact panel2FlatEven19_eq
  · exact panel2FlatEven20_eq
  · exact panel2FlatEven21_eq
  · exact panel2FlatEven22_eq
  · exact panel2FlatEven23_eq

theorem panel2FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel2FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel2FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel2FlatOdd0_eq
  · exact panel2FlatOdd1_eq
  · exact panel2FlatOdd2_eq
  · exact panel2FlatOdd3_eq
  · exact panel2FlatOdd4_eq
  · exact panel2FlatOdd5_eq
  · exact panel2FlatOdd6_eq
  · exact panel2FlatOdd7_eq
  · exact panel2FlatOdd8_eq
  · exact panel2FlatOdd9_eq
  · exact panel2FlatOdd10_eq
  · exact panel2FlatOdd11_eq
  · exact panel2FlatOdd12_eq
  · exact panel2FlatOdd13_eq
  · exact panel2FlatOdd14_eq
  · exact panel2FlatOdd15_eq
  · exact panel2FlatOdd16_eq
  · exact panel2FlatOdd17_eq
  · exact panel2FlatOdd18_eq
  · exact panel2FlatOdd19_eq
  · exact panel2FlatOdd20_eq
  · exact panel2FlatOdd21_eq
  · exact panel2FlatOdd22_eq
  · exact panel2FlatOdd23_eq

theorem panel2FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel2FlatCache.EnclosesCanonical
      ⟨2, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel2FlatDefect
    rw [panel2FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel2DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel2FlatEvenComponents).get i)
    rw [panel2FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel2OuterLengthTable
      .even ⟨2, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel2FlatOddComponents).get i)
    rw [panel2FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel2OuterLengthTable
      .odd ⟨2, by decide⟩ i

end RHP2Bridge
