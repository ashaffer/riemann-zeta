import RHBridge.P2RoundedFactorCheckpoint27
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck27_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel27FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel27FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel27FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel27FlatEven0_eq
  · exact panel27FlatEven1_eq
  · exact panel27FlatEven2_eq
  · exact panel27FlatEven3_eq
  · exact panel27FlatEven4_eq
  · exact panel27FlatEven5_eq
  · exact panel27FlatEven6_eq
  · exact panel27FlatEven7_eq
  · exact panel27FlatEven8_eq
  · exact panel27FlatEven9_eq
  · exact panel27FlatEven10_eq
  · exact panel27FlatEven11_eq
  · exact panel27FlatEven12_eq
  · exact panel27FlatEven13_eq
  · exact panel27FlatEven14_eq
  · exact panel27FlatEven15_eq
  · exact panel27FlatEven16_eq
  · exact panel27FlatEven17_eq
  · exact panel27FlatEven18_eq
  · exact panel27FlatEven19_eq
  · exact panel27FlatEven20_eq
  · exact panel27FlatEven21_eq
  · exact panel27FlatEven22_eq
  · exact panel27FlatEven23_eq

theorem panel27FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel27FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel27FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel27FlatOdd0_eq
  · exact panel27FlatOdd1_eq
  · exact panel27FlatOdd2_eq
  · exact panel27FlatOdd3_eq
  · exact panel27FlatOdd4_eq
  · exact panel27FlatOdd5_eq
  · exact panel27FlatOdd6_eq
  · exact panel27FlatOdd7_eq
  · exact panel27FlatOdd8_eq
  · exact panel27FlatOdd9_eq
  · exact panel27FlatOdd10_eq
  · exact panel27FlatOdd11_eq
  · exact panel27FlatOdd12_eq
  · exact panel27FlatOdd13_eq
  · exact panel27FlatOdd14_eq
  · exact panel27FlatOdd15_eq
  · exact panel27FlatOdd16_eq
  · exact panel27FlatOdd17_eq
  · exact panel27FlatOdd18_eq
  · exact panel27FlatOdd19_eq
  · exact panel27FlatOdd20_eq
  · exact panel27FlatOdd21_eq
  · exact panel27FlatOdd22_eq
  · exact panel27FlatOdd23_eq

theorem panel27FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel27FlatCache.EnclosesCanonical
      ⟨27, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel27FlatDefect
    rw [panel27FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel27DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel27FlatEvenComponents).get i)
    rw [panel27FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel27OuterLengthTable
      .even ⟨27, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel27FlatOddComponents).get i)
    rw [panel27FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel27OuterLengthTable
      .odd ⟨27, by decide⟩ i

end RHP2Bridge
