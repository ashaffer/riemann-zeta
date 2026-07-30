import RHBridge.P2RoundedFactorCheckpoint26
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck26_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel26FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel26FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel26FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel26FlatEven0_eq
  · exact panel26FlatEven1_eq
  · exact panel26FlatEven2_eq
  · exact panel26FlatEven3_eq
  · exact panel26FlatEven4_eq
  · exact panel26FlatEven5_eq
  · exact panel26FlatEven6_eq
  · exact panel26FlatEven7_eq
  · exact panel26FlatEven8_eq
  · exact panel26FlatEven9_eq
  · exact panel26FlatEven10_eq
  · exact panel26FlatEven11_eq
  · exact panel26FlatEven12_eq
  · exact panel26FlatEven13_eq
  · exact panel26FlatEven14_eq
  · exact panel26FlatEven15_eq
  · exact panel26FlatEven16_eq
  · exact panel26FlatEven17_eq
  · exact panel26FlatEven18_eq
  · exact panel26FlatEven19_eq
  · exact panel26FlatEven20_eq
  · exact panel26FlatEven21_eq
  · exact panel26FlatEven22_eq
  · exact panel26FlatEven23_eq

theorem panel26FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel26FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel26FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel26FlatOdd0_eq
  · exact panel26FlatOdd1_eq
  · exact panel26FlatOdd2_eq
  · exact panel26FlatOdd3_eq
  · exact panel26FlatOdd4_eq
  · exact panel26FlatOdd5_eq
  · exact panel26FlatOdd6_eq
  · exact panel26FlatOdd7_eq
  · exact panel26FlatOdd8_eq
  · exact panel26FlatOdd9_eq
  · exact panel26FlatOdd10_eq
  · exact panel26FlatOdd11_eq
  · exact panel26FlatOdd12_eq
  · exact panel26FlatOdd13_eq
  · exact panel26FlatOdd14_eq
  · exact panel26FlatOdd15_eq
  · exact panel26FlatOdd16_eq
  · exact panel26FlatOdd17_eq
  · exact panel26FlatOdd18_eq
  · exact panel26FlatOdd19_eq
  · exact panel26FlatOdd20_eq
  · exact panel26FlatOdd21_eq
  · exact panel26FlatOdd22_eq
  · exact panel26FlatOdd23_eq

theorem panel26FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel26FlatCache.EnclosesCanonical
      ⟨26, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel26FlatDefect
    rw [panel26FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel26DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel26FlatEvenComponents).get i)
    rw [panel26FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel26OuterLengthTable
      .even ⟨26, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel26FlatOddComponents).get i)
    rw [panel26FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel26OuterLengthTable
      .odd ⟨26, by decide⟩ i

end RHP2Bridge
