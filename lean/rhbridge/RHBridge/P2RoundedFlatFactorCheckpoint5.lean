import RHBridge.P2RoundedFactorCheckpoint5
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck5_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel5FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel5FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel5TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel5FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel5FlatEven0_eq
  · exact panel5FlatEven1_eq
  · exact panel5FlatEven2_eq
  · exact panel5FlatEven3_eq
  · exact panel5FlatEven4_eq
  · exact panel5FlatEven5_eq
  · exact panel5FlatEven6_eq
  · exact panel5FlatEven7_eq
  · exact panel5FlatEven8_eq
  · exact panel5FlatEven9_eq
  · exact panel5FlatEven10_eq
  · exact panel5FlatEven11_eq
  · exact panel5FlatEven12_eq
  · exact panel5FlatEven13_eq
  · exact panel5FlatEven14_eq
  · exact panel5FlatEven15_eq
  · exact panel5FlatEven16_eq
  · exact panel5FlatEven17_eq
  · exact panel5FlatEven18_eq
  · exact panel5FlatEven19_eq
  · exact panel5FlatEven20_eq
  · exact panel5FlatEven21_eq
  · exact panel5FlatEven22_eq
  · exact panel5FlatEven23_eq

theorem panel5FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel5FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel5FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel5FlatOdd0_eq
  · exact panel5FlatOdd1_eq
  · exact panel5FlatOdd2_eq
  · exact panel5FlatOdd3_eq
  · exact panel5FlatOdd4_eq
  · exact panel5FlatOdd5_eq
  · exact panel5FlatOdd6_eq
  · exact panel5FlatOdd7_eq
  · exact panel5FlatOdd8_eq
  · exact panel5FlatOdd9_eq
  · exact panel5FlatOdd10_eq
  · exact panel5FlatOdd11_eq
  · exact panel5FlatOdd12_eq
  · exact panel5FlatOdd13_eq
  · exact panel5FlatOdd14_eq
  · exact panel5FlatOdd15_eq
  · exact panel5FlatOdd16_eq
  · exact panel5FlatOdd17_eq
  · exact panel5FlatOdd18_eq
  · exact panel5FlatOdd19_eq
  · exact panel5FlatOdd20_eq
  · exact panel5FlatOdd21_eq
  · exact panel5FlatOdd22_eq
  · exact panel5FlatOdd23_eq

theorem panel5FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel5FlatCache.EnclosesCanonical
      ⟨5, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel5FlatDefect
    rw [panel5FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel5DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel5FlatEvenComponents).get i)
    rw [panel5FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel5OuterLengthTable
      .even ⟨5, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel5FlatOddComponents).get i)
    rw [panel5FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel5OuterLengthTable
      .odd ⟨5, by decide⟩ i

end RHP2Bridge
