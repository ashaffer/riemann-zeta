import RHBridge.P2RoundedFactorCheckpoint15
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck15_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel15FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel15FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel15TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel15FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel15FlatEven0_eq
  · exact panel15FlatEven1_eq
  · exact panel15FlatEven2_eq
  · exact panel15FlatEven3_eq
  · exact panel15FlatEven4_eq
  · exact panel15FlatEven5_eq
  · exact panel15FlatEven6_eq
  · exact panel15FlatEven7_eq
  · exact panel15FlatEven8_eq
  · exact panel15FlatEven9_eq
  · exact panel15FlatEven10_eq
  · exact panel15FlatEven11_eq
  · exact panel15FlatEven12_eq
  · exact panel15FlatEven13_eq
  · exact panel15FlatEven14_eq
  · exact panel15FlatEven15_eq
  · exact panel15FlatEven16_eq
  · exact panel15FlatEven17_eq
  · exact panel15FlatEven18_eq
  · exact panel15FlatEven19_eq
  · exact panel15FlatEven20_eq
  · exact panel15FlatEven21_eq
  · exact panel15FlatEven22_eq
  · exact panel15FlatEven23_eq

theorem panel15FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel15FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel15FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel15FlatOdd0_eq
  · exact panel15FlatOdd1_eq
  · exact panel15FlatOdd2_eq
  · exact panel15FlatOdd3_eq
  · exact panel15FlatOdd4_eq
  · exact panel15FlatOdd5_eq
  · exact panel15FlatOdd6_eq
  · exact panel15FlatOdd7_eq
  · exact panel15FlatOdd8_eq
  · exact panel15FlatOdd9_eq
  · exact panel15FlatOdd10_eq
  · exact panel15FlatOdd11_eq
  · exact panel15FlatOdd12_eq
  · exact panel15FlatOdd13_eq
  · exact panel15FlatOdd14_eq
  · exact panel15FlatOdd15_eq
  · exact panel15FlatOdd16_eq
  · exact panel15FlatOdd17_eq
  · exact panel15FlatOdd18_eq
  · exact panel15FlatOdd19_eq
  · exact panel15FlatOdd20_eq
  · exact panel15FlatOdd21_eq
  · exact panel15FlatOdd22_eq
  · exact panel15FlatOdd23_eq

theorem panel15FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel15FlatCache.EnclosesCanonical
      ⟨15, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel15FlatDefect
    rw [panel15FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel15DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel15FlatEvenComponents).get i)
    rw [panel15FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel15OuterLengthTable
      .even ⟨15, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel15FlatOddComponents).get i)
    rw [panel15FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel15OuterLengthTable
      .odd ⟨15, by decide⟩ i

end RHP2Bridge
